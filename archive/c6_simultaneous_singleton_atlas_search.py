#!/usr/bin/env python3
"""Search the NetworkX graph atlas for singleton-portal counterexamples.

For an injectively labelled six-terminal connected host, demand e_i joins
terminal i to i+1 (mod 6).  We test the proposed simultaneous-state claim:

* e_i and e_{i+3} are not linkable for i=0,1,2; and
* two opposite frame pairs are present, where frame f links e_{f-2} to
  e_{f+2}.

A linkage is represented exactly by two disjoint connected vertex sets,
one containing each prescribed terminal pair.  Other terminals are allowed
inside a carrier, matching the full carrier definition used in the notes.
"""

from __future__ import annotations

import itertools

import networkx as nx


def connected_masks(graph: nx.Graph) -> tuple[int, ...]:
    vertices = tuple(graph)
    return tuple(
        mask
        for mask in range(1, 1 << len(vertices))
        if nx.is_connected(
            graph.subgraph(vertices[i] for i in range(len(vertices)) if mask >> i & 1)
        )
    )


def linkable(
    masks: tuple[int, ...], pair_a: tuple[int, int], pair_b: tuple[int, int]
) -> bool:
    bit_a = (1 << pair_a[0]) | (1 << pair_a[1])
    bit_b = (1 << pair_b[0]) | (1 << pair_b[1])
    carriers_a = [mask for mask in masks if mask & bit_a == bit_a]
    carriers_b = [mask for mask in masks if mask & bit_b == bit_b]
    return any(not (first & second) for first in carriers_a for second in carriers_b)


def state(
    graph: nx.Graph, masks: tuple[int, ...], terminals: tuple[int, ...]
) -> tuple[bool, ...]:
    relabel = {vertex: index for index, vertex in enumerate(graph)}
    demands = tuple(
        (relabel[terminals[i]], relabel[terminals[(i + 1) % 6]]) for i in range(6)
    )
    return tuple(
        linkable(masks, demands[i], demands[j])
        for i in range(6)
        for j in range(i + 1, 6)
    )


def lookup(bits: tuple[bool, ...], i: int, j: int) -> bool:
    if i > j:
        i, j = j, i
    index = 0
    for first in range(6):
        for second in range(first + 1, 6):
            if (first, second) == (i, j):
                return bits[index]
            index += 1
    raise AssertionError


def is_counterstate(bits: tuple[bool, ...]) -> bool:
    if any(lookup(bits, i, i + 3) for i in range(3)):
        return False
    frame = {
        f: lookup(bits, (f - 2) % 6, (f + 2) % 6) for f in range(6)
    }
    owned = [frame[j] and frame[j + 3] for j in range(3)]
    return sum(owned) >= 2


def main() -> None:
    checked = 0
    for graph in nx.graph_atlas_g():
        if (
            not 6 <= len(graph) <= 7
            or not nx.is_connected(graph)
            or nx.node_connectivity(graph) < 2
        ):
            continue
        vertices = tuple(graph)
        masks = connected_masks(graph)
        # The state is invariant under the dihedral action on the six
        # labels.  Normalize terminal 0 and orientation within each chosen
        # six-set to avoid twelve duplicate tests.
        for chosen in itertools.combinations(vertices, 6):
            first = min(chosen)
            remainder = tuple(vertex for vertex in chosen if vertex != first)
            for tail in itertools.permutations(remainder):
                terminals = (first,) + tail
                if terminals[1] > terminals[5]:
                    continue
                terminal_set = set(terminals)
                # Optimistically allow every shore vertex to see the
                # seventh boundary root z.  Actual minimum degree seven
                # still forces d_D(x)+number_of_C6_portals(x) >= 6.
                if any(
                    graph.degree(vertex) + (vertex in terminal_set) < 6
                    for vertex in vertices
                ):
                    continue
                checked += 1
                bits = state(graph, masks, terminals)
                if is_counterstate(bits):
                    print("SAT", len(graph), sorted(graph.edges()), terminals)
                    return
    print("UNSAT through graph atlas order 7; labelled states", checked)


if __name__ == "__main__":
    main()
