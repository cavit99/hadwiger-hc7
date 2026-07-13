#!/usr/bin/env python3
"""Exact verifier for the tetrahedral C6 portal obstruction.

The graph has the C6+K1 boundary S, a singleton full shore h, and a K4
shore D with the portal rows from `hadwiger_c6_portal_tetrahedron_obstruction.md`.
The script checks the linkage signature, every two-piece split lock, six
connectivity, and (by exhaustive branch-set partitions) absence of a K7 minor.
"""

from __future__ import annotations

import itertools

import networkx as nx

from c6_two_piece_contact_atlas import fast_k7_model, quotient_edges


CYCLE = (0, 4, 2, 3, 1, 5)
PORTALS = (0b1100, 0b0001, 0b1010, 0b0100, 0b1001, 0b0010)
ROWS = (
    frozenset((1, 4, 6)),
    frozenset((2, 5, 6)),
    frozenset((0, 3, 6)),
    frozenset((0, 1, 2, 6)),
)


def pieces(first_class: int, second_class: int) -> tuple[int, ...]:
    return tuple(
        mask
        for mask in range(1, 1 << 4)
        if mask & PORTALS[first_class] and mask & PORTALS[second_class]
    )


def two_linkage(
    first_edge: tuple[int, int],
    second_edge: tuple[int, int],
    outward: tuple[int, int] | None = None,
):
    for left in pieces(*first_edge):
        for right in pieces(*second_edge):
            if left & right:
                continue
            if outward is None or left & PORTALS[outward[0]] or right & PORTALS[outward[1]]:
                return left, right
    return None


def three_linkage(edges: tuple[tuple[int, int], ...]):
    candidates = tuple(pieces(*edge) for edge in edges)
    for first in candidates[0]:
        for second in candidates[1]:
            for third in candidates[2]:
                if not (first & second or first & third or second & third):
                    return first, second, third
    return None


def ambient_graph() -> nx.Graph:
    boundary = tuple(range(7))
    shore = tuple(range(7, 11))
    helper = 11
    missing = {
        (0, 4), (0, 5), (1, 3), (1, 5), (2, 3), (2, 4),
    }
    graph = nx.Graph()
    graph.add_nodes_from(range(12))
    graph.add_edges_from(set(itertools.combinations(boundary, 2)) - missing)
    graph.add_edges_from(itertools.combinations(shore, 2))
    graph.add_edges_from((vertex, helper) for vertex in boundary)
    for vertex, row in zip(shore, ROWS):
        graph.add_edges_from((vertex, boundary_vertex) for boundary_vertex in row)
    return graph


def set_partitions(values: tuple[int, ...], blocks: int):
    current = [[values[0]]]

    def recurse(index: int):
        if index == len(values):
            if len(current) == blocks:
                yield tuple(
                    sum(1 << vertex for vertex in block) for block in current
                )
            return
        vertex = values[index]
        for block in current:
            block.append(vertex)
            yield from recurse(index + 1)
            block.pop()
        if len(current) < blocks:
            current.append([vertex])
            yield from recurse(index + 1)
            current.pop()

    yield from recurse(1)


def has_k7_minor(graph: nx.Graph):
    order = len(graph)
    adjacency = [0] * order
    for first, second in graph.edges:
        adjacency[first] |= 1 << second
        adjacency[second] |= 1 << first

    connected_cache: dict[int, bool] = {}
    neighbour_cache: dict[int, int] = {}

    def connected(mask: int) -> bool:
        if mask not in connected_cache:
            reached = mask & -mask
            while True:
                expanded = reached
                bits = reached
                while bits:
                    bit = bits & -bits
                    bits ^= bit
                    expanded |= adjacency[bit.bit_length() - 1] & mask
                if expanded == reached:
                    break
                reached = expanded
            connected_cache[mask] = reached == mask
        return connected_cache[mask]

    def neighbours(mask: int) -> int:
        if mask not in neighbour_cache:
            union = 0
            bits = mask
            while bits:
                bit = bits & -bits
                bits ^= bit
                union |= adjacency[bit.bit_length() - 1]
            neighbour_cache[mask] = union
        return neighbour_cache[mask]

    checked = 0
    for support_order in range(order, 6, -1):
        for support in itertools.combinations(range(order), support_order):
            for bags in set_partitions(support, 7):
                checked += 1
                if not all(connected(bag) for bag in bags):
                    continue
                if all(
                    neighbours(bags[first]) & bags[second]
                    for first in range(7)
                    for second in range(first)
                ):
                    return bags, checked
    return None, checked


def main() -> None:
    frame_witnesses = []
    for i in range(6):
        first = ((i - 2) % 6, (i - 1) % 6)
        second = ((i + 2) % 6, (i + 3) % 6)
        witness = two_linkage(first, second)
        assert witness is not None
        assert two_linkage(first, second, (i, (i + 1) % 6)) is None
        frame_witnesses.append(witness)

    for i in range(3):
        assert two_linkage(
            (i, (i + 1) % 6), ((i + 3) % 6, (i + 4) % 6)
        ) is None
    assert three_linkage(((0, 1), (2, 3), (4, 5))) is None
    assert three_linkage(((1, 2), (3, 4), (5, 0))) is None

    # K4 makes every nontrivial vertex bipartition connected and adjacent.
    for side in range(1, (1 << 4) - 1):
        left = set().union(*(ROWS[v] for v in range(4) if side >> v & 1))
        right = set().union(*(ROWS[v] for v in range(4) if not side >> v & 1))
        assert fast_k7_model(quotient_edges(left, right)) is None

    graph = ambient_graph()
    assert nx.node_connectivity(graph) == 6
    model, partitions_checked = has_k7_minor(graph)
    assert model is None
    assert partitions_checked == 1_899_612

    print("portal masks", PORTALS)
    print("frame witnesses", frame_witnesses)
    print("all owned frames are tight")
    print("all antipodal and nonidentity three-linkages are absent")
    print("all 14 ordered K4 splits are exact-atlas negative")
    print("ambient connectivity", nx.node_connectivity(graph))
    print("ambient degrees", tuple(dict(graph.degree()).values()))
    print("K7 branch partitions checked", partitions_checked)
    print("K7 minor", model)


if __name__ == "__main__":
    main()
