#!/usr/bin/env python3
"""Exact K7-minor probe for the d=2 exact-lobe quotient."""

from __future__ import annotations

import itertools
import networkx as nx


def clique_minor_model(graph: nx.Graph, target: int = 7):
    vertices = tuple(graph)
    idx = {v: i for i, v in enumerate(vertices)}
    n = len(vertices)
    adj = [0] * n
    for u, v in graph.edges():
        i, j = idx[u], idx[v]
        adj[i] |= 1 << j
        adj[j] |= 1 << i
    nbr = [0] * (1 << n)
    connected: list[int] = []
    for mask in range(1, 1 << n):
        bit = mask & -mask
        nbr[mask] = nbr[mask ^ bit] | adj[bit.bit_length() - 1]
        reached = bit
        while True:
            new = reached | (nbr[reached] & mask)
            if new == reached:
                break
            reached = new
        if reached == mask:
            connected.append(mask)
    connected.sort(key=lambda m: (m.bit_count(), m))

    def rec(chosen: list[int], candidates: list[int], used: int):
        if len(chosen) == target:
            return tuple(tuple(vertices[i] for i in range(n) if m >> i & 1)
                         for m in chosen)
        need = target - len(chosen)
        for pos, bag in enumerate(candidates):
            if bag & used:
                continue
            following = [
                other for other in candidates[pos + 1:]
                if not other & (used | bag) and nbr[bag] & other
            ]
            if len(following) >= need - 1:
                ans = rec(chosen + [bag], following, used | bag)
                if ans is not None:
                    return ans
        return None

    return rec([], connected, 0)


def quotient(misses: tuple[int, ...]) -> nx.Graph:
    # Deficient labels s0,s1; contact labels s2,s3,s4.
    S = tuple(f"s{i}" for i in range(5))
    G = nx.Graph()
    G.add_edges_from(itertools.combinations(S, 2))
    G.add_edges_from(("v", s) for s in S[2:])
    G.add_edges_from((("v", "x0"), ("v", "x1")))
    for j in range(2):
        G.add_edges_from((f"x{j}", s) for i, s in enumerate(S) if i != j)
    for t, miss in enumerate(misses):
        r = f"r{t}"
        G.add_edges_from(((r, "v"), (r, "x0"), (r, "x1")))
        G.add_edges_from((r, s) for i, s in enumerate(S) if i != miss)
    return G


def main() -> None:
    for count in range(1, 7):
        negative = []
        for misses in itertools.product(range(5), repeat=count):
            # Components are interchangeable.
            if tuple(sorted(misses)) != misses:
                continue
            G = quotient(misses)
            model = clique_minor_model(G)
            if model is None:
                negative.append(misses)
            else:
                print("positive", misses, model)
        print("count", count, "negative", negative)


if __name__ == "__main__":
    main()
