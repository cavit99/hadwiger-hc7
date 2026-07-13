#!/usr/bin/env python3
"""Search the 7-connected K2-join-icosahedron barrier for a literal
two-cycle/three-row counterexample to the proposed three-anchor amplifier.

The two universal vertices and one icosahedron vertex are singleton rows.
We search the remaining icosahedron for two disjoint four-cycles, four
literal matching edges whose cyclic orders disagree, and compute the exact
packing number of duty-complete port sectors.
"""

from __future__ import annotations

from itertools import combinations, permutations

import networkx as nx


def canonical_cycle(cycle: tuple[int, ...]) -> tuple[int, ...]:
    rotations = []
    for order in (cycle, tuple(reversed(cycle))):
        rotations.extend(order[i:] + order[:i] for i in range(len(order)))
    return min(rotations)


def four_cycles(graph: nx.Graph) -> list[tuple[int, int, int, int]]:
    values = set()
    for vertices in combinations(graph, 4):
        for order_tail in permutations(vertices[1:]):
            order = (vertices[0],) + order_tail
            if all(graph.has_edge(order[i], order[(i + 1) % 4]) for i in range(4)):
                values.add(canonical_cycle(order))
    return sorted(values)


def cyclic_subpaths(order: tuple[int, ...], root: int) -> set[frozenset[int]]:
    values: set[frozenset[int]] = set()
    n = len(order)
    for start in range(n):
        for length in range(1, n + 1):
            path = frozenset(order[(start + step) % n] for step in range(length))
            if root in path:
                values.add(path)
    return values


def sector_family(
    left: tuple[int, ...], right: tuple[int, ...], neighbours: set[int]
) -> list[frozenset[int]]:
    values = set()
    for index in range(4):
        for a_path in cyclic_subpaths(left, left[index]):
            for b_path in cyclic_subpaths(right, right[index]):
                sector = a_path | b_path
                if sector & neighbours:
                    values.add(sector)
    return sorted(values, key=lambda value: (len(value), tuple(sorted(value))))


def sector_family_three_rows(
    left: tuple[int, ...], right: tuple[int, ...], supports: tuple[set[int], ...]
) -> list[frozenset[int]]:
    values = set()
    for index in range(4):
        for a_path in cyclic_subpaths(left, left[index]):
            for b_path in cyclic_subpaths(right, right[index]):
                sector = a_path | b_path
                if all(sector & support for support in supports):
                    values.add(sector)
    return sorted(values, key=lambda value: (len(value), tuple(sorted(value))))


def packing_number(family: list[frozenset[int]]) -> int:
    best = 0

    def search(position: int, used: frozenset[int], count: int) -> None:
        nonlocal best
        best = max(best, count)
        for i in range(position, len(family)):
            if not used & family[i]:
                search(i + 1, used | family[i], count + 1)

    search(0, frozenset(), 0)
    return best


def mismatched(left: tuple[int, ...], right_labels: tuple[int, ...]) -> bool:
    # Left labels are 0,1,2,3.  Agreement up to reversal means a dihedral
    # ordering of that tuple.
    base = (0, 1, 2, 3)
    dihedral = set()
    for order in (base, tuple(reversed(base))):
        dihedral.update(order[i:] + order[:i] for i in range(4))
    return right_labels not in dihedral


def minimal_for_support(
    graph: nx.Graph, row: frozenset[int], skeleton: set[int]
) -> bool:
    support = set().union(*(set(graph[v]) & skeleton for v in row))
    for size in range(1, len(row)):
        for subset in combinations(row, size):
            subset = frozenset(subset)
            if not nx.is_connected(graph.subgraph(subset)):
                continue
            subset_support = set().union(*(set(graph[v]) & skeleton for v in subset))
            if subset_support == support:
                return False
    return True


def main() -> None:
    triangulation = nx.icosahedral_graph()
    cycles = four_cycles(triangulation)
    print("four-cycles", len(cycles))

    for left in cycles:
        for right_cycle in cycles:
            if set(left) & set(right_cycle):
                continue
            skeleton = set(left) | set(right_cycle)
            leftovers = set(triangulation) - skeleton
            for row_size in range(1, len(leftovers) + 1):
                for row_tuple in combinations(leftovers, row_size):
                    row = frozenset(row_tuple)
                    if not nx.is_connected(triangulation.subgraph(row)):
                        continue
                    row_neighbours = set().union(
                        *(set(triangulation[v]) & skeleton for v in row)
                    )
                    if not minimal_for_support(triangulation, row, skeleton):
                        continue
                    available = set(triangulation) - set(row)
                    # Choose the port bijection by reordering the second cycle.
                    for right in (right_cycle, tuple(reversed(right_cycle))):
                        for shift in range(4):
                            ordered_right = right[shift:] + right[:shift]
                            if not all(
                                triangulation.has_edge(left[i], ordered_right[i])
                                for i in range(4)
                            ):
                                continue
                            # Labels on the right are determined by which left
                            # endpoint each right vertex is matched to.  In this
                            # representation they are 0,1,2,3, while its cyclic
                            # order is read in the canonical right_cycle order.
                            label_of = {ordered_right[i]: i for i in range(4)}
                            labels = tuple(label_of[v] for v in right_cycle)
                            if not mismatched(left, labels):
                                continue
                            family = sector_family(left, ordered_right, row_neighbours)
                            packing = packing_number(family)
                            if packing <= 3:
                                print("FOUND")
                                print(
                                    "row", sorted(row),
                                    "row-neighbours-on-skeleton", sorted(row_neighbours),
                                )
                                print("left", left)
                                print("right matched", ordered_right)
                                print("right cyclic", right_cycle, "labels", labels)
                                print("matching", list(zip(left, ordered_right)))
                                print("family", len(family), "packing", packing)
                                print("unused icosahedron", sorted(available - skeleton))
                                return
    raise SystemExit("no witness found")


def joined_icosahedron_singleton_rows() -> None:
    triangulation = nx.icosahedral_graph()
    graph = triangulation.copy()
    graph.add_edge(12, 13)
    for apex in (12, 13):
        graph.add_edges_from((apex, vertex) for vertex in triangulation)
    assert nx.node_connectivity(graph) == 7

    cycles = four_cycles(graph)
    print("joined four-cycles", len(cycles))
    for left in cycles:
        for right_cycle in cycles:
            skeleton = set(left) | set(right_cycle)
            if len(skeleton) != 8:
                continue
            leftovers = set(graph) - skeleton
            row_triples = [
                triple
                for triple in combinations(leftovers, 3)
                if all(graph.has_edge(*edge) for edge in combinations(triple, 2))
            ]
            if not row_triples:
                continue
            for right in (right_cycle, tuple(reversed(right_cycle))):
                for shift in range(4):
                    ordered_right = right[shift:] + right[:shift]
                    if not all(graph.has_edge(left[i], ordered_right[i]) for i in range(4)):
                        continue
                    label_of = {ordered_right[i]: i for i in range(4)}
                    labels = tuple(label_of[v] for v in right_cycle)
                    if not mismatched(left, labels):
                        continue
                    for rows in row_triples:
                        supports = tuple(set(graph[row]) & skeleton for row in rows)
                        family = sector_family_three_rows(left, ordered_right, supports)
                        packing = packing_number(family)
                        if packing <= 3:
                            print("FOUND JOINED")
                            print("rows", rows, "supports", [sorted(s) for s in supports])
                            print("left", left)
                            print("right matched", ordered_right)
                            print("right cyclic", right_cycle, "labels", labels)
                            print("family", len(family), "packing", packing)
                            print("unused", sorted(leftovers - set(rows)))
                            return
    raise SystemExit("no joined witness found")


if __name__ == "__main__":
    # main()
    joined_icosahedron_singleton_rows()
