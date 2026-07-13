#!/usr/bin/env python3
"""Exact small search for simultaneous C6 linkage obstructions.

The six terminals are distinct vertices of a two-connected graph.  Around a
cyclic order C, frame i asks for two disjoint connected pieces joining the
two cycle edges e_{i-2} and e_{i+2}; the pieces are required to be adjacent,
as in the C6 shore crossing.  An ``unlock'' additionally puts c_i in the
first piece or c_{i+1} in the second piece.

The search enumerates NetworkX's graph atlas (orders six and seven), all
six-terminal subsets, and cyclic orders modulo the dihedral group.  It looks
for graphs which

* own at least two opposite frame pairs;
* have no unlock for an owned frame;
* have none of the three antipodal two-linkages; and
* have neither alternating three-linkage.

The last two bullets are precisely the nonidentity P--Q perfect-matching
exclusions for the complementary triangular-prism boundary.
"""

from __future__ import annotations

import argparse
import itertools
from collections import Counter

import networkx as nx


def connected_masks(graph: nx.Graph) -> tuple[tuple[int, ...], tuple[tuple[int, int], ...]]:
    n = len(graph)
    adjacency = [0] * n
    for u, v in graph.edges:
        adjacency[u] |= 1 << v
        adjacency[v] |= 1 << u

    connected: list[int] = []
    neighbourhood: dict[int, int] = {}
    for mask in range(1, 1 << n):
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
        if reached == mask:
            connected.append(mask)
            union = 0
            bits = mask
            while bits:
                bit = bits & -bits
                bits ^= bit
                union |= adjacency[bit.bit_length() - 1]
            neighbourhood[mask] = union

    adjacent_disjoint = tuple(
        (left, right)
        for left in connected
        for right in connected
        if not left & right and neighbourhood[left] & right
    )
    return tuple(connected), adjacent_disjoint


def contains(mask: int, vertices: tuple[int, ...]) -> bool:
    return all(mask >> vertex & 1 for vertex in vertices)


def has_two_linkage(
    adjacent_disjoint: tuple[tuple[int, int], ...],
    first: tuple[int, int],
    second: tuple[int, int],
    outward: tuple[int, int] | None = None,
) -> bool:
    for left, right in adjacent_disjoint:
        if contains(left, first) and contains(right, second):
            if outward is None or left >> outward[0] & 1 or right >> outward[1] & 1:
                return True
        if contains(right, first) and contains(left, second):
            if outward is None or right >> outward[0] & 1 or left >> outward[1] & 1:
                return True
    return False


def has_three_linkage(
    connected: tuple[int, ...], pairs: tuple[tuple[int, int], ...]
) -> bool:
    candidates = tuple(
        tuple(mask for mask in connected if contains(mask, pair)) for pair in pairs
    )
    return any(
        not (first & second or first & third or second & third)
        for first in candidates[0]
        for second in candidates[1]
        for third in candidates[2]
    )


def cyclic_orders(vertices: tuple[int, ...]):
    first = min(vertices)
    remainder = tuple(vertex for vertex in vertices if vertex != first)
    for permutation in itertools.permutations(remainder):
        if permutation[0] < permutation[-1]:
            yield (first,) + permutation


def signature(
    connected: tuple[int, ...],
    adjacent_disjoint: tuple[tuple[int, int], ...],
    cycle: tuple[int, ...],
):
    support: list[bool] = []
    unlock: list[bool] = []
    for i in range(6):
        first = (cycle[(i - 2) % 6], cycle[(i - 1) % 6])
        second = (cycle[(i + 2) % 6], cycle[(i + 3) % 6])
        support.append(has_two_linkage(adjacent_disjoint, first, second))
        unlock.append(
            has_two_linkage(
                adjacent_disjoint,
                first,
                second,
                (cycle[i], cycle[(i + 1) % 6]),
            )
        )

    antipodal = tuple(
        has_two_linkage(
            adjacent_disjoint,
            (cycle[i], cycle[(i + 1) % 6]),
            (cycle[(i + 3) % 6], cycle[(i + 4) % 6]),
        )
        for i in range(3)
    )
    alternating = tuple(
        has_three_linkage(
            connected,
            tuple((cycle[i], cycle[(i + 1) % 6]) for i in parity),
        )
        for parity in ((0, 2, 4), (1, 3, 5))
    )
    opposite_pairs = sum(support[i] and support[i + 3] for i in range(3))
    return tuple(support), tuple(unlock), antipodal, alternating, opposite_pairs


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-order", type=int, default=7, choices=(6, 7))
    parser.add_argument("--connectivity", type=int, default=3, choices=(2, 3, 4))
    parser.add_argument("--print-limit", type=int, default=30)
    args = parser.parse_args()

    examples: list[tuple[nx.Graph, tuple[int, ...], tuple[bool, ...], int]] = []
    for source in nx.graph_atlas_g():
        if not 6 <= len(source) <= args.max_order or not nx.is_biconnected(source):
            continue
        connectivity = nx.node_connectivity(source)
        if connectivity < args.connectivity:
            continue
        graph = nx.convert_node_labels_to_integers(source)
        connected, adjacent_disjoint = connected_masks(graph)
        found_for_graph = False
        for terminals in itertools.combinations(range(len(graph)), 6):
            for cycle in cyclic_orders(terminals):
                support, unlock, antipodal, alternating, opposite_pairs = signature(
                    connected, adjacent_disjoint, cycle
                )
                if (
                    opposite_pairs >= 2
                    and not any(antipodal)
                    and not any(alternating)
                    and not any(unlock[i] for i in range(6) if support[i])
                ):
                    examples.append((graph.copy(), cycle, support, connectivity))
                    if len(examples) <= args.print_limit:
                        print(
                            "EXAMPLE",
                            "n=", len(graph),
                            "m=", graph.number_of_edges(),
                            "kappa=", connectivity,
                            "cycle=", cycle,
                            "support=", "".join("1" if value else "0" for value in support),
                            "edges=", sorted(tuple(sorted(edge)) for edge in graph.edges),
                        )
                    found_for_graph = True
                    break
            if found_for_graph:
                break

    counts = Counter(
        (len(graph), graph.number_of_edges(), connectivity)
        for graph, _, _, connectivity in examples
    )
    print("TOTAL_GRAPH_TYPES", len(examples))
    print("COUNTS", sorted(counts.items()))


if __name__ == "__main__":
    main()
