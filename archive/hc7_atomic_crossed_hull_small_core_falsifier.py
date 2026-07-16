#!/usr/bin/env python3
"""Exhaust the first fully crossed path-hull contact systems.

This is a falsifier for the geometry-only residue, not a proof of the
unbounded crossed-hull lemma.  The boundary is the paired width-two tree.
The thin graph is C_n, the selected core is the path obtained by deleting
one cycle vertex/closing segment, and the omitted part crosses every core
edge.  Contact masks satisfy the singleton consequences of relative
seven-connectivity and the unique-u convention.

For n=3 the script checks the exact disjunction

    list-compatible adjacent carriers OR an S-rooted K5.

For n=4,5 it finds list-compatible carriers in every case, so no rooted
minor search is needed.
"""

from __future__ import annotations

import itertools
import sys
from pathlib import Path


DEPS = Path(__file__).resolve().parents[1] / "active" / "runtime" / "deps"
if DEPS.exists():
    sys.path.insert(0, str(DEPS))

import networkx as nx


S = ("c", "a1", "t1", "a2", "t2", "a3", "t3")
U = "t1"
W = tuple(s for s in S if s != U)
S_SET = frozenset(S)

H = nx.Graph()
H.add_nodes_from(S)
H.add_edges_from(
    (
        ("c", "a1"),
        ("c", "a2"),
        ("c", "a3"),
        ("a1", "t2"),
        ("t1", "a3"),
        ("a2", "t3"),
    )
)
BIPARTITION = nx.bipartite.color(H)


def connected_subsets(graph: nx.Graph):
    vertices = tuple(graph)
    for size in range(1, len(vertices) + 1):
        for subset in itertools.combinations(vertices, size):
            subset = frozenset(subset)
            if nx.is_connected(graph.subgraph(subset)):
                yield subset


def rooted_k5(graph: nx.Graph, contacts) -> bool:
    closed = nx.compose(H, graph)
    for x in graph:
        closed.add_edges_from((x, s) for s in contacts[x])

    vertices = tuple(closed)
    candidates = []
    for mask in range(1, 1 << len(vertices)):
        subset = frozenset(
            vertices[i] for i in range(len(vertices)) if mask >> i & 1
        )
        if subset & S_SET and nx.is_connected(closed.subgraph(subset)):
            candidates.append(subset)
    candidates.sort(key=lambda subset: (len(subset), tuple(sorted(map(str, subset)))))

    def search(chosen, start, used):
        if len(chosen) == 5:
            return True
        for i in range(start, len(candidates)):
            candidate = candidates[i]
            if candidate & used:
                continue
            if not all(
                any(closed.has_edge(x, y) for x in candidate for y in old)
                for old in chosen
            ):
                continue
            if search(chosen + (candidate,), i + 1, used | candidate):
                return True
        return False

    return search((), 0, frozenset())


def run_cycle(order: int):
    names = ("z",) + tuple(f"v{i}" for i in range(1, order))
    graph = nx.cycle_graph(names)
    subsets = tuple(connected_subsets(graph))
    carrier_pairs = tuple(
        (left, right)
        for left in subsets
        for right in subsets
        if left.isdisjoint(right)
        and any(graph.has_edge(x, y) for x in left for y in right)
    )
    cut_rows = tuple(
        (
            subset,
            {
                y
                for x in subset
                for y in graph
                if y not in subset and graph.has_edge(x, y)
            },
        )
        for subset in subsets
    )

    def repairs(contacts):
        for left, right in carrier_pairs:
            lists = {
                s: {
                    i
                    for i, carrier in enumerate((left, right))
                    if any(s in contacts[x] for x in carrier)
                }
                for s in S
            }
            if any(not lists[s] for s in S):
                continue
            for flip in (0, 1):
                if all((BIPARTITION[s] ^ flip) in lists[s] for s in S):
                    return True
        return False

    def satisfies_relative_cuts(contacts):
        return all(
            len(internal_boundary)
            + len(set().union(*(contacts[x] for x in subset)))
            >= 7
            for subset, internal_boundary in cut_rows
        )

    masks = [
        frozenset(combination)
        for size in range(7)
        for combination in itertools.combinations(W, size)
    ]
    z_masks = [mask | {U} for mask in masks if len(mask) >= 4]
    other_masks = [mask for mask in masks if len(mask) >= 5]

    total = repaired = rooted = unresolved = 0
    for z_mask in z_masks:
        for values in itertools.product(other_masks, repeat=order - 1):
            # This is the audited A-z W-full normalization.
            if set().union(*values) != set(W):
                continue
            contacts = {"z": z_mask, **dict(zip(names[1:], values))}
            assert satisfies_relative_cuts(contacts)
            total += 1
            if repairs(contacts):
                repaired += 1
            elif order == 3 and rooted_k5(graph, contacts):
                rooted += 1
            else:
                unresolved += 1

    return total, repaired, rooted, unresolved


def main():
    expected = {
        3: (946, 850, 96, 0),
        4: (7414, 7414, 0, 0),
        5: (52690, 52690, 0, 0),
    }
    for order in (3, 4, 5):
        result = run_cycle(order)
        assert result == expected[order]
        print(
            "cycle_order",
            order,
            "total",
            result[0],
            "carrier_repair",
            result[1],
            "S_rooted_K5",
            result[2],
            "unresolved",
            result[3],
        )
    print("BOUNDED_CORES_GREEN")


if __name__ == "__main__":
    main()
