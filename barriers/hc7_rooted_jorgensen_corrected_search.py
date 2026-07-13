#!/usr/bin/env python3
"""Exact small-order search for the corrected rooted-Jorgensen target.

Input is a graph6 stream of complements.  For every host H the program
tests six-connectivity, non-two-apexness, robust contact with a set X, an
unrooted K6 minor, and absence of an X-meeting K6 model.

For six specified roots, a rooted model is searched exactly: each branch
set is a connected subset containing its own root and no other root, and
the six sets must be disjoint and pairwise adjacent.  An X-meeting model
exists iff one six-subset of X is rootable.
"""

from __future__ import annotations

from functools import lru_cache
from itertools import combinations
import sys

import networkx as nx


class RootedOracle:
    def __init__(self, graph: nx.Graph):
        self.graph = nx.convert_node_labels_to_integers(graph)
        self.n = len(self.graph)
        self.rows = [0] * self.n
        for u, v in self.graph.edges:
            self.rows[u] |= 1 << v
            self.rows[v] |= 1 << u
        self.root_cache: dict[tuple[int, ...], tuple[int, ...] | None] = {}

    @lru_cache(maxsize=None)
    def connected(self, mask: int) -> bool:
        reached = mask & -mask
        while reached:
            old = reached
            bits = reached
            while bits:
                bit = bits & -bits
                bits ^= bit
                reached |= self.rows[bit.bit_length() - 1] & mask
            if reached == old:
                return reached == mask
        return False

    def neighbourhood(self, mask: int) -> int:
        value = 0
        bits = mask
        while bits:
            bit = bits & -bits
            bits ^= bit
            value |= self.rows[bit.bit_length() - 1]
        return value & ~mask

    def rooted_k6(self, roots: tuple[int, ...]) -> tuple[int, ...] | None:
        roots = tuple(sorted(roots))
        if roots in self.root_cache:
            return self.root_cache[roots]
        root_mask = sum(1 << root for root in roots)
        free = [v for v in range(self.n) if not root_mask >> v & 1]
        candidates: dict[int, list[tuple[int, int]]] = {}
        for root in roots:
            values = []
            for choice in range(1 << len(free)):
                mask = 1 << root
                for i, vertex in enumerate(free):
                    if choice >> i & 1:
                        mask |= 1 << vertex
                if self.connected(mask):
                    values.append((mask, self.neighbourhood(mask)))
            values.sort(key=lambda item: item[0].bit_count())
            candidates[root] = values

        order = sorted(roots, key=lambda root: len(candidates[root]))

        def search(
            position: int, used: int, chosen: list[tuple[int, int]]
        ) -> tuple[int, ...] | None:
            if position == 6:
                return tuple(mask for mask, _ in chosen)
            root = order[position]
            for mask, neighbourhood in candidates[root]:
                if mask & used:
                    continue
                if any(not neighbourhood & old_mask for old_mask, _ in chosen):
                    continue
                answer = search(
                    position + 1,
                    used | mask,
                    [*chosen, (mask, neighbourhood)],
                )
                if answer is not None:
                    return answer
            return None

        answer = search(0, 0, [])
        self.root_cache[roots] = answer
        return answer

    def robust(self, x_mask: int) -> bool:
        """Test the deletion-set condition via connected X-free shores."""
        outside = ((1 << self.n) - 1) ^ x_mask
        shore = outside
        while shore:
            if self.connected(shore) and self.neighbourhood(shore).bit_count() <= 6:
                return False
            shore = (shore - 1) & outside
        return True


def two_apex(graph: nx.Graph) -> bool:
    vertices = tuple(graph)
    return any(
        nx.check_planarity(graph.subgraph(set(vertices) - set(pair)))[0]
        for pair in combinations(vertices, 2)
    )


def main() -> None:
    counts: dict[str, int] = {}
    for raw in sys.stdin.buffer:
        raw = raw.strip()
        if not raw:
            continue
        complement = nx.from_graph6_bytes(raw)
        graph = nx.complement(complement)
        if nx.node_connectivity(graph) < 6:
            counts["connectivity<6"] = counts.get("connectivity<6", 0) + 1
            continue
        if two_apex(graph):
            counts["two-apex"] = counts.get("two-apex", 0) + 1
            continue

        oracle = RootedOracle(graph)
        rootable: dict[tuple[int, ...], bool] = {
            roots: oracle.rooted_k6(roots) is not None
            for roots in combinations(range(oracle.n), 6)
        }
        if not any(rootable.values()):
            counts["no-K6"] = counts.get("no-K6", 0) + 1
            continue

        full = (1 << oracle.n) - 1
        found = False
        for x_mask in range(full + 1):
            if x_mask.bit_count() < 7 or not oracle.robust(x_mask):
                continue
            x_vertices = [v for v in range(oracle.n) if x_mask >> v & 1]
            if any(rootable[roots] for roots in combinations(x_vertices, 6)):
                continue
            code = nx.to_graph6_bytes(graph, header=False).decode().strip()
            print(
                {
                    "graph6": code,
                    "kappa": nx.node_connectivity(graph),
                    "X": x_vertices,
                    "bad_root_sets": sum(not value for value in rootable.values()),
                },
                flush=True,
            )
            counts["candidate"] = counts.get("candidate", 0) + 1
            found = True
            break
        if not found:
            counts["closed"] = counts.get("closed", 0) + 1
    print(counts)


if __name__ == "__main__":
    main()
