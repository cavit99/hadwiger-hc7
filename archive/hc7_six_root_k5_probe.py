#!/usr/bin/env python3
"""Falsify a six-root K5 meeting principle on small 5-connected graphs.

Candidate principle: if F is 5-connected and has a K5 minor, then for
every six-set W, F has a K5 model whose five bags each meet W.

The first test family is the icosahedron plus one nonedge.  It is
5-connected and nonplanar, hence has a K5 minor.  The search below is an
exact rooted branch-set search, not a heuristic.
"""

from __future__ import annotations

import itertools
import sys
from functools import lru_cache
from pathlib import Path


DEPS = Path(__file__).resolve().parent / "runtime" / "deps"
if DEPS.exists():
    sys.path.insert(0, str(DEPS))

import networkx as nx


def rows(graph: nx.Graph):
    names = tuple(graph)
    index = {v: i for i, v in enumerate(names)}
    adj = [0] * len(names)
    for x, y in graph.edges:
        i, j = index[x], index[y]
        adj[i] |= 1 << j
        adj[j] |= 1 << i
    return names, index, tuple(adj)


def rooted_k5(graph: nx.Graph, roots: tuple[int, ...]):
    """Return five bags, one through each prescribed root, or None."""
    names, index, adj = rows(graph)
    n = len(names)
    root_bits = tuple(1 << index[root] for root in roots)
    all_root_bits = sum(root_bits)

    @lru_cache(maxsize=None)
    def connected(mask: int) -> bool:
        reached = mask & -mask
        while True:
            expanded = reached
            bits = reached
            while bits:
                bit = bits & -bits
                bits ^= bit
                expanded |= adj[bit.bit_length() - 1] & mask
            if expanded == reached:
                return reached == mask
            reached = expanded

    candidates: list[list[tuple[int, int]]] = []
    for root_bit in root_bits:
        current = []
        for mask in range(1, 1 << n):
            if not (mask & root_bit):
                continue
            if mask & (all_root_bits ^ root_bit):
                continue
            if not connected(mask):
                continue
            neighbourhood = 0
            bits = mask
            while bits:
                bit = bits & -bits
                bits ^= bit
                neighbourhood |= adj[bit.bit_length() - 1]
            current.append((mask, neighbourhood))
        current.sort(key=lambda item: (item[0].bit_count(), item[0]))
        candidates.append(current)

    def search(i: int, used: int, chosen: tuple[int, ...]):
        if i == 5:
            return chosen
        for mask, neighbourhood in candidates[i]:
            if mask & used:
                continue
            if all(neighbourhood & old for old in chosen):
                found = search(i + 1, used | mask, chosen + (mask,))
                if found is not None:
                    return found
        return None

    answer = search(0, 0, ())
    if answer is None:
        return None
    return tuple(tuple(names[i] for i in range(n) if mask >> i & 1) for mask in answer)


def five_of_six_model(graph: nx.Graph, six: tuple[int, ...]):
    for omitted in six:
        roots = tuple(root for root in six if root != omitted)
        model = rooted_k5(graph, roots)
        if model is not None:
            return omitted, model
    return None


def main() -> None:
    base = nx.icosahedral_graph()
    nonedge = next(iter(nx.non_edges(base)))
    graph = base.copy()
    graph.add_edge(*nonedge)
    assert nx.node_connectivity(graph) >= 5
    assert not nx.check_planarity(graph)[0]

    checked = 0
    for six in itertools.combinations(graph.nodes, 6):
        checked += 1
        model = five_of_six_model(graph, six)
        if model is None:
            print("COUNTEREXAMPLE", "added_edge", nonedge, "roots", six)
            print("graph6", nx.to_graph6_bytes(graph, header=False).decode().strip())
            return
    print("ALL_ROOT_SETS_HAVE_MODEL", "added_edge", nonedge, "checked", checked)


if __name__ == "__main__":
    main()
