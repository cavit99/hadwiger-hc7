#!/usr/bin/env python3
"""Rooted-K5 atlas for a split pole over a literal C5 boundary."""

from __future__ import annotations

import itertools
import networkx as nx


ROOTS = tuple(range(5))


def connected_masks(graph: nx.Graph) -> list[int]:
    verts = tuple(graph)
    out = []
    for mask in range(1, 1 << len(verts)):
        chosen = [verts[i] for i in range(len(verts)) if mask >> i & 1]
        if nx.is_connected(graph.subgraph(chosen)):
            out.append(mask)
    return out


def rooted_k5(graph: nx.Graph):
    verts = tuple(graph)
    index = {v: i for i, v in enumerate(verts)}
    masks = connected_masks(graph)
    nbr: dict[int, int] = {}
    adjacency = [0] * len(verts)
    for u, v in graph.edges():
        adjacency[index[u]] |= 1 << index[v]
        adjacency[index[v]] |= 1 << index[u]
    for mask in masks:
        value = 0
        for i in range(len(verts)):
            if mask >> i & 1:
                value |= adjacency[i]
        nbr[mask] = value
    choices = []
    for root in ROOTS:
        bit = 1 << index[root]
        choices.append([m for m in masks if m & bit and
                        all(not (m >> index[r] & 1) for r in ROOTS if r != root)])

    def rec(i: int, picked: list[int], used: int):
        if i == 5:
            return tuple(tuple(verts[j] for j in range(len(verts)) if m >> j & 1)
                         for m in picked)
        for m in choices[i]:
            if m & used:
                continue
            if all(nbr[m] & old for old in picked):
                ans = rec(i + 1, picked + [m], used | m)
                if ans is not None:
                    return ans
        return None

    return rec(0, [], 0)


def intervals(mask: int) -> bool:
    # Nonempty proper subsets of C5 which occur consecutively.
    selected = {i for i in ROOTS if mask >> i & 1}
    changes = sum(((i in selected) != ((i + 1) % 5 in selected)) for i in ROOTS)
    return changes <= 2


def host(a_mask: int, d_mask: int) -> nx.Graph:
    G = nx.cycle_graph(5)
    G.add_node("z")
    G.add_edges_from(("z", i) for i in ROOTS)
    G.add_edge("A", "D")
    G.add_edges_from(("A", i) for i in ROOTS if a_mask >> i & 1)
    G.add_edges_from(("D", i) for i in ROOTS if d_mask >> i & 1)
    return G


def main() -> None:
    negative = []
    for a_mask in range(1, 32):
        for d_mask in range(1, 32):
            if a_mask | d_mask != 31:
                continue
            model = rooted_k5(host(a_mask, d_mask))
            if model is None:
                negative.append((a_mask, d_mask))
    maximal = []
    for pair in negative:
        if not any(
            pair != other and pair[0] & ~other[0] == 0 and pair[1] & ~other[1] == 0
            for other in negative
        ):
            maximal.append(pair)
    for a_mask, d_mask in maximal:
        print(
            "A", tuple(i for i in ROOTS if a_mask >> i & 1),
            "D", tuple(i for i in ROOTS if d_mask >> i & 1),
            "intervals", intervals(a_mask), intervals(d_mask),
        )
    print("negative", len(negative), "maximal", len(maximal))


if __name__ == "__main__":
    main()
