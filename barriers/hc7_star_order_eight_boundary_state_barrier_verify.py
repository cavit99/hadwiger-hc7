#!/usr/bin/env python3
"""Census the exact order-eight boundary from the five-support star branch."""

from __future__ import annotations

from collections import Counter
from functools import lru_cache
from itertools import combinations, permutations, product
import sys

sys.path.insert(0, "active/runtime/deps")
import networkx as nx  # noqa: E402


R = (0, 1, 2)
EDGE_A = (3, 4)
EDGE_B = (5, 6)
EXTRA = 7
VERTEX_COUNT = 8
ALL_PAIRS = tuple(combinations(range(VERTEX_COUNT), 2))
PAIR_INDEX = {edge: index for index, edge in enumerate(ALL_PAIRS)}
FULL_MASK = (1 << VERTEX_COUNT) - 1


def add_edge(code: int, left: int, right: int) -> int:
    return code | (1 << PAIR_INDEX[tuple(sorted((left, right)))])


def adjacency(code: int) -> tuple[int, ...]:
    result = [0] * VERTEX_COUNT
    for index, (left, right) in enumerate(ALL_PAIRS):
        if (code >> index) & 1:
            result[left] |= 1 << right
            result[right] |= 1 << left
    return tuple(result)


def contact_group() -> tuple[tuple[int, ...], ...]:
    group = []
    for image_r in permutations(R):
        for interchange_edges in (False, True):
            for reverse_a in (False, True):
                for reverse_b in (False, True):
                    image = list(range(VERTEX_COUNT))
                    for old, new in zip(R, image_r):
                        image[old] = new
                    if not interchange_edges:
                        image[3], image[4] = (
                            (4, 3) if reverse_a else (3, 4)
                        )
                        image[5], image[6] = (
                            (6, 5) if reverse_b else (5, 6)
                        )
                    else:
                        image[3], image[4] = (
                            (6, 5) if reverse_a else (5, 6)
                        )
                        image[5], image[6] = (
                            (4, 3) if reverse_b else (3, 4)
                        )
                    image[EXTRA] = EXTRA
                    group.append(tuple(image))
    return tuple(dict.fromkeys(group))


CONTACT_GROUP = contact_group()
assert len(CONTACT_GROUP) == 48


def relabel(code: int, image: tuple[int, ...]) -> int:
    result = 0
    for index, (left, right) in enumerate(ALL_PAIRS):
        if (code >> index) & 1:
            result = add_edge(result, image[left], image[right])
    return result


def canonical_contact_code(code: int) -> int:
    return min(relabel(code, image) for image in CONTACT_GROUP)


def candidate_orbits() -> tuple[dict[int, int], int]:
    base = 0
    for left, right in combinations(R, 2):
        base = add_edge(base, left, right)
    base = add_edge(base, *EDGE_A)
    base = add_edge(base, *EDGE_B)

    multiplicity: dict[int, int] = {}
    labelled = 0
    for contacts_a in product((1, 2, 3), repeat=3):
        for contacts_b in product((1, 2, 3), repeat=3):
            code = base
            for root, contact in zip(R, contacts_a):
                if contact & 1:
                    code = add_edge(code, root, EDGE_A[0])
                if contact & 2:
                    code = add_edge(code, root, EDGE_A[1])
            for root, contact in zip(R, contacts_b):
                if contact & 1:
                    code = add_edge(code, root, EDGE_B[0])
                if contact & 2:
                    code = add_edge(code, root, EDGE_B[1])
            for extra_contacts in range(1 << 7):
                completed = code
                for vertex in range(7):
                    if (extra_contacts >> vertex) & 1:
                        completed = add_edge(completed, EXTRA, vertex)
                canonical = canonical_contact_code(completed)
                multiplicity[canonical] = multiplicity.get(canonical, 0) + 1
                labelled += 1
    return multiplicity, labelled


def induced_mask(adj: tuple[int, ...], keep_mask: int) -> tuple[int, ...]:
    keep = tuple(
        vertex for vertex in range(len(adj)) if (keep_mask >> vertex) & 1
    )
    position = {vertex: index for index, vertex in enumerate(keep)}
    return tuple(
        sum(
            1 << position[other]
            for other in keep
            if (adj[vertex] >> other) & 1
        )
        for vertex in keep
    )


def delete_vertex(adj: tuple[int, ...], vertex: int) -> tuple[int, ...]:
    return induced_mask(adj, ((1 << len(adj)) - 1) ^ (1 << vertex))


def contract_edge(
    adj: tuple[int, ...], left: int, right: int
) -> tuple[int, ...]:
    if left > right:
        left, right = right, left
    keep = [vertex for vertex in range(len(adj)) if vertex != right]
    result = [0] * len(keep)
    for first_index, first in enumerate(keep):
        for second_index in range(first_index + 1, len(keep)):
            second = keep[second_index]
            edge = bool((adj[first] >> second) & 1)
            if first == left:
                edge |= bool((adj[right] >> second) & 1)
            if second == left:
                edge |= bool((adj[first] >> right) & 1)
            if edge:
                result[first_index] |= 1 << second_index
                result[second_index] |= 1 << first_index
    return tuple(result)


def complete(adj: tuple[int, ...]) -> bool:
    return all(row.bit_count() == len(adj) - 1 for row in adj)


def colorable(adj: tuple[int, ...], colors_available: int) -> bool:
    colors = [-1] * len(adj)
    saturation = [0] * len(adj)

    def search(colored: int) -> bool:
        if colored == len(adj):
            return True
        uncolored = [
            vertex for vertex in range(len(adj)) if colors[vertex] < 0
        ]
        vertex = max(
            uncolored,
            key=lambda item: (
                saturation[item].bit_count(),
                adj[item].bit_count(),
            ),
        )
        for color in range(colors_available):
            if (saturation[vertex] >> color) & 1:
                continue
            colors[vertex] = color
            changed = []
            for other in uncolored:
                if (
                    other != vertex
                    and ((adj[vertex] >> other) & 1)
                    and not ((saturation[other] >> color) & 1)
                ):
                    saturation[other] |= 1 << color
                    changed.append(other)
            if search(colored + 1):
                return True
            colors[vertex] = -1
            for other in changed:
                mask = 0
                for neighbour in range(len(adj)):
                    if (
                        colors[neighbour] >= 0
                        and ((adj[other] >> neighbour) & 1)
                    ):
                        mask |= 1 << colors[neighbour]
                saturation[other] = mask
        return False

    return search(0)


def has_clique_minor(adj: tuple[int, ...], order: int) -> bool:
    @lru_cache(maxsize=None)
    def search(graph: tuple[int, ...]) -> bool:
        if len(graph) < order:
            return False
        if len(graph) == order:
            return complete(graph)
        if any(
            search(delete_vertex(graph, vertex))
            for vertex in range(len(graph))
        ):
            return True
        return any(
            ((graph[left] >> right) & 1)
            and search(contract_edge(graph, left, right))
            for left in range(len(graph))
            for right in range(left + 1, len(graph))
        )

    return search(adj)


def join_i2_has_k7(adj: tuple[int, ...]) -> bool:
    """Use the exact two-universal-nonadjacent-vertex reduction."""

    if has_clique_minor(adj, 6):
        return True
    return any(
        has_clique_minor(delete_vertex(adj, vertex), 5)
        for vertex in range(len(adj))
    )


def independent(adj: tuple[int, ...], mask: int) -> bool:
    remaining = mask
    while remaining:
        bit = remaining & -remaining
        vertex = bit.bit_length() - 1
        remaining ^= bit
        if adj[vertex] & remaining:
            return False
    return True


def clique(adj: tuple[int, ...], mask: int) -> bool:
    vertices = [
        vertex for vertex in range(len(adj)) if (mask >> vertex) & 1
    ]
    return all(
        (adj[left] >> right) & 1
        for index, left in enumerate(vertices)
        for right in vertices[index + 1 :]
    )


def has_clique_oct(adj: tuple[int, ...]) -> bool:
    full = (1 << len(adj)) - 1
    return any(
        clique(adj, mask)
        and colorable(induced_mask(adj, full ^ mask), 2)
        for mask in range(1 << len(adj))
    )


def complement_has_perfect_matching(adj: tuple[int, ...]) -> bool:
    @lru_cache(maxsize=None)
    def search(mask: int) -> bool:
        if not mask:
            return True
        first_bit = mask & -mask
        first = first_bit.bit_length() - 1
        rest = mask ^ first_bit
        return any(
            not ((adj[first] >> second) & 1)
            and search(rest ^ (1 << second))
            for second in range(len(adj))
            if (rest >> second) & 1
        )

    return search((1 << len(adj)) - 1)


def all_partitions() -> tuple[tuple[int, ...], ...]:
    result = set()

    def extend(vertex: int, blocks: list[int]) -> None:
        if vertex == VERTEX_COUNT:
            if len(blocks) <= 6:
                result.add(tuple(sorted(blocks)))
            return
        bit = 1 << vertex
        for index in range(len(blocks)):
            updated = blocks.copy()
            updated[index] |= bit
            extend(vertex + 1, updated)
        if len(blocks) < 6:
            extend(vertex + 1, blocks + [bit])

    extend(0, [])
    return tuple(sorted(result))


PARTITIONS = all_partitions()
assert len(PARTITIONS) == 4111


def verify_trace_parity(adj: tuple[int, ...]) -> int:
    valid = [
        partition
        for partition in PARTITIONS
        if all(independent(adj, block) for block in partition)
    ]
    cylinders = 0
    for mask in range(1, FULL_MASK + 1):
        if not independent(adj, mask):
            continue
        parities = {
            len(partition) % 2 for partition in valid if mask in partition
        }
        assert parities == {0, 1}
        cylinders += 1
    return cylinders


def graph_from_code(code: int) -> nx.Graph:
    graph = nx.Graph()
    graph.add_nodes_from(range(VERTEX_COUNT))
    graph.add_edges_from(
        edge
        for index, edge in enumerate(ALL_PAIRS)
        if (code >> index) & 1
    )
    return graph


def isomorphism_classes(
    codes: list[int],
) -> list[tuple[tuple[bool, bool], list[int], nx.Graph]]:
    classes: list[tuple[tuple[bool, bool], list[int], nx.Graph]] = []
    for code in codes:
        adj = adjacency(code)
        flags = (has_clique_oct(adj), complement_has_perfect_matching(adj))
        graph = graph_from_code(code)
        for old_flags, members, representative in classes:
            if old_flags == flags and nx.is_isomorphic(graph, representative):
                members.append(code)
                break
        else:
            classes.append((flags, [code], graph))
    return classes


def main() -> None:
    multiplicity, labelled_count = candidate_orbits()
    assert labelled_count == 93_312
    assert len(multiplicity) == 2_568

    survivors = []
    trace_cylinders = 0
    for code in sorted(multiplicity):
        adj = adjacency(code)
        if join_i2_has_k7(adj):
            continue
        assert colorable(adj, 4)
        trace_cylinders += verify_trace_parity(adj)
        survivors.append(code)

    assert len(survivors) == 899
    survivor_labelled_count = sum(multiplicity[code] for code in survivors)

    flag_counts = Counter(
        (has_clique_oct(adjacency(code)),
         complement_has_perfect_matching(adjacency(code)))
        for code in survivors
    )
    assert flag_counts == Counter(
        {
            (True, True): 719,
            (True, False): 129,
            (False, True): 50,
            (False, False): 1,
        }
    )

    classes = isomorphism_classes(survivors)
    assert len(classes) == 710
    class_flag_counts = Counter(flags for flags, _, _ in classes)
    assert class_flag_counts == Counter(
        {
            (True, True): 566,
            (True, False): 102,
            (False, True): 41,
            (False, False): 1,
        }
    )

    unique_neither = [
        code
        for code in survivors
        if not has_clique_oct(adjacency(code))
        and not complement_has_perfect_matching(adjacency(code))
    ]
    assert unique_neither == [119_876_351]
    assert not colorable(adjacency(unique_neither[0]), 3)
    exceptional_edges = {
        edge
        for index, edge in enumerate(ALL_PAIRS)
        if (unique_neither[0] >> index) & 1
    }
    assert exceptional_edges == {
        (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7),
        (1, 2), (1, 4), (1, 6), (2, 3), (2, 6), (3, 4), (3, 7),
        (4, 7), (5, 6), (5, 7),
    }

    sparse = 33_858_967
    assert sparse in survivors
    sparse_graph = graph_from_code(sparse)
    assert sparse_graph.number_of_edges() == 11
    assert sparse_graph.degree(EXTRA) == 0
    assert set(sparse_graph[3]) & set(R) == set(R)
    assert not (set(sparse_graph[4]) & set(R))
    assert set(sparse_graph[5]) & set(R) == set(R)
    assert not (set(sparse_graph[6]) & set(R))

    print("GREEN: exact order-eight star-boundary census verified")
    print("labelled candidates", labelled_count)
    print("contact orbits", len(multiplicity))
    print("surviving contact orbits", len(survivors))
    print("surviving labelled candidates", survivor_labelled_count)
    print("ordinary isomorphism types", len(classes))
    print("cliqueOCT/perfect-matching counts", dict(sorted(flag_counts.items())))
    print("trace cylinders checked", trace_cylinders)
    print("unique neither code", unique_neither[0], "graph6 G|uFKw")
    print("sparse portal code", sparse, "graph6 G~F_G?")


if __name__ == "__main__":
    main()
