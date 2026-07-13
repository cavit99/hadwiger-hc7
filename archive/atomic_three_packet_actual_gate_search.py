"""Embed the rank-two K4 packet circuit in the seven-edge gate atlas.

For every fully-positive matching type and every orientation of its three
matching edges, attach the four-vertex strict-surplus packet shore and one
opposite full helper.  The script checks seven-connectivity and searches
exactly for a K7 minor, returning explicit negative realizations if any.
"""

from __future__ import annotations

from itertools import combinations, permutations, product

import networkx as nx

from equality_gate_seven_edge_packet_atlas import (
    EXPECTED_RESIDUAL_MANIFEST,
    FULL_PACKET_TRIANGLES,
)


CIRCUITS = {
    2: (
        {(0, 1)},
        (frozenset(range(7)), frozenset(range(7))),
    ),
    4: (
        set(combinations(range(4), 2)),
        (
            frozenset((1, 2, 4, 5, 6)),
            frozenset((0, 3, 4, 5, 6)),
            frozenset((0, 2, 4, 5, 6)),
            frozenset((1, 3, 4, 5, 6)),
        ),
    ),
    5: (
        set(combinations(range(5), 2)),
        (
            frozenset((0, 3, 5, 6)),
            frozenset((0, 2, 4, 6)),
            frozenset((1, 2, 5, 6)),
            frozenset((1, 3, 4, 6)),
            frozenset((1, 2, 4, 6)),
        ),
    ),
    6: (
        {
            (0, 1), (0, 2), (0, 4), (0, 5), (1, 2), (1, 3), (1, 5),
            (2, 3), (2, 4), (2, 5), (3, 4), (3, 5), (4, 5),
        },
        (
            frozenset((0, 2, 4, 6)),
            frozenset((1, 3, 4, 6)),
            frozenset((0, 2, 6)),
            frozenset((1, 3, 5, 6)),
            frozenset((0, 2, 5, 6)),
            frozenset((1, 3, 6)),
        ),
    ),
}


def k_clique_minor_model(graph: nx.Graph, target: int = 7):
    order = graph.number_of_nodes()
    adjacency = [0] * order
    for left, right in graph.edges():
        adjacency[left] |= 1 << right
        adjacency[right] |= 1 << left

    neighbours = [0] * (1 << order)
    connected = []
    for mask in range(1, 1 << order):
        bit = mask & -mask
        vertex = bit.bit_length() - 1
        neighbours[mask] = neighbours[mask ^ bit] | adjacency[vertex]
        reached = bit
        while True:
            expanded = reached | (neighbours[reached] & mask)
            if expanded == reached:
                break
            reached = expanded
        if reached == mask:
            connected.append(mask)
    connected.sort(key=lambda mask: (mask.bit_count(), mask))

    def adjacent(left: int, right: int) -> bool:
        return not (left & right) and bool(neighbours[left] & right)

    def recurse(chosen: list[int], candidates: list[int], used: int):
        if len(chosen) == target:
            return tuple(chosen)
        needed = target - len(chosen)
        if len(candidates) < needed:
            return None
        for position, bag in enumerate(candidates):
            if bag & used:
                continue
            following = [
                other
                for other in candidates[position + 1:]
                if not other & (used | bag) and adjacent(bag, other)
            ]
            if len(following) < needed - 1:
                continue
            answer = recurse(chosen + [bag], following, used | bag)
            if answer is not None:
                return answer
        return None

    return recurse([], connected, 0)


def mappings(matching):
    local_pairs = ((0, 1), (2, 3), (4, 5))
    for pair_order in permutations(matching):
        for flips in product((0, 1), repeat=3):
            mapping = {6: next(iter(set(range(7)) - set(sum((list(pair) for pair in matching), []))))}
            for local, actual, flip in zip(local_pairs, pair_order, flips):
                actual = actual[::-1] if flip else actual
                mapping[local[0]] = actual[0]
                mapping[local[1]] = actual[1]
            yield mapping


def gate_graph(index: int, mapping: dict[int, int], circuit_order: int) -> nx.Graph:
    missing = set(EXPECTED_RESIDUAL_MANIFEST[index][1])
    circuit_edges, local_rows = CIRCUITS[circuit_order]
    helper = 7 + circuit_order
    graph = nx.Graph()
    graph.add_nodes_from(range(helper + 1))
    graph.add_edges_from(set(combinations(range(7), 2)) - missing)
    graph.add_edges_from((7 + left, 7 + right) for left, right in circuit_edges)
    for local_vertex, row in enumerate(local_rows):
        graph.add_edges_from((7 + local_vertex, mapping[label]) for label in row)
    graph.add_edges_from((helper, label) for label in range(7))
    return graph


def verify_strict_shore(graph: nx.Graph, circuit_order: int) -> None:
    shore = set(range(7, 7 + circuit_order))
    for size in range(1, circuit_order):
        for raw in combinations(shore, size):
            subset = set(raw)
            assert len(set().union(*(set(graph.neighbors(v)) for v in subset)) - subset) >= 8


def main() -> None:
    for circuit_order in CIRCUITS:
        print("circuit order", circuit_order)
        for index, matching in FULL_PACKET_TRIANGLES.items():
            negative = []
            seen = set()
            for mapping in mappings(matching):
                key = tuple(mapping[label] for label in range(7))
                if key in seen:
                    continue
                seen.add(key)
                graph = gate_graph(index, mapping, circuit_order)
                verify_strict_shore(graph, circuit_order)
                connectivity = nx.node_connectivity(graph)
                model = k_clique_minor_model(graph)
                if model is None:
                    negative.append((key, connectivity, graph.number_of_edges()))
            print(index, EXPECTED_RESIDUAL_MANIFEST[index][0], "negative", negative)


if __name__ == "__main__":
    main()
