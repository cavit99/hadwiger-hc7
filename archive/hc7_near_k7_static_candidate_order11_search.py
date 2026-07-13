#!/usr/bin/env python3
"""Exact nauty-assisted certificate at order 11.

For a 7-connected 11-vertex graph, the complement has maximum degree at
most three.  `geng -D3 11` generates every such complement once up to
isomorphism.  This script complements each graph, filters exact
7-connectivity, and runs a complete connected-branch-set K7 search.

The expected graph counts and certificate digest are asserted at the end.
"""

from __future__ import annotations

import subprocess
import hashlib

import networkx as nx


def k7_model(graph: nx.Graph) -> list[list[int]] | None:
    vertices = list(graph)
    n = len(vertices)

    # Fast literal-clique branch.
    for clique in nx.find_cliques(graph):
        if len(clique) >= 7:
            return [[x] for x in clique[:7]]

    # On eleven vertices the common certificate type uses only singleton
    # and edge bags.  Search that small exact family first.
    small = [[x] for x in vertices]
    small.extend([[x, y] for x, y in graph.edges()])

    def sets_compatible(left: list[int], right: list[int]) -> bool:
        return set(left).isdisjoint(right) and any(
            graph.has_edge(x, y) for x in left for y in right
        )

    compatibility = {
        i: {j for j in range(len(small)) if j != i
            and sets_compatible(small[i], small[j])}
        for i in range(len(small))
    }

    def small_search(chosen: list[int], available: list[int]):
        if len(chosen) == 7:
            return chosen
        while len(chosen) + len(available) >= 7:
            candidate = available.pop()
            result = small_search(
                [*chosen, candidate],
                [other for other in available
                 if other in compatibility[candidate]],
            )
            if result is not None:
                return result
        return None

    small_masks = small_search([], list(range(len(small))))
    if small_masks is not None:
        return [small[index] for index in small_masks]

    members: dict[int, list[int]] = {}
    candidates: list[int] = []
    for mask in range(1, 1 << n):
        if mask.bit_count() > n - 6:
            continue
        subset = [vertices[i] for i in range(n) if mask >> i & 1]
        if nx.is_connected(graph.subgraph(subset)):
            candidates.append(mask)
            members[mask] = subset

    def compatible(left: int, right: int) -> bool:
        return not left & right and any(
            graph.has_edge(x, y)
            for x in members[left]
            for y in members[right]
        )

    # Small bags are tried first.  Dense complements usually yield a
    # certificate before compatibility preprocessing would pay for itself.
    candidates.sort(key=lambda mask: -mask.bit_count())

    def search(chosen: list[int], available: list[int]):
        if len(chosen) == 7:
            return chosen
        while len(chosen) + len(available) >= 7:
            candidate = available.pop()
            result = search(
                [*chosen, candidate],
                [other for other in available
                 if compatible(candidate, other)],
            )
            if result is not None:
                return result
        return None

    masks = search([], candidates)
    return None if masks is None else [members[mask] for mask in masks]


def verify_model(graph: nx.Graph, bags: list[list[int]]) -> None:
    assert len(bags) == 7
    assert all(bag and nx.is_connected(graph.subgraph(bag)) for bag in bags)
    assert sum(map(len, bags)) == len(set().union(*(map(set, bags))))
    assert all(
        any(graph.has_edge(x, y) for x in bags[i] for y in bags[j])
        for i in range(7)
        for j in range(i + 1, 7)
    )


def main() -> None:
    process = subprocess.Popen(
        ['geng', '-q', '-D3', '11'],
        stdout=subprocess.PIPE,
        text=False,
    )
    assert process.stdout is not None
    generated = connected = excluded = 0
    digest = hashlib.sha256()
    for raw in process.stdout:
        if not raw.strip():
            continue
        generated += 1
        complement = nx.from_graph6_bytes(raw.strip())
        graph = nx.complement(complement)
        if nx.node_connectivity(graph) < 7:
            continue
        connected += 1
        bags = k7_model(graph)
        if bags is None:
            print('CANDIDATE_GRAPH6', raw.decode().strip())
            print('COMPLEMENT_EDGES', sorted(complement.edges()))
            print('GRAPH_EDGES', sorted(graph.edges()))
            process.terminate()
            return
        verify_model(graph, bags)
        digest.update(raw.strip())
        digest.update(repr(bags).encode())
        excluded += 1
        if generated % 1000 == 0:
            print('progress', generated, connected, flush=True)

    assert process.wait() == 0
    assert (generated, connected, excluded) == (10946, 9940, 9940)
    certificate = digest.hexdigest()
    assert certificate == 'df8e05ea22f8b8426b70503c2d353ec633152e63ec6d8b9eeb8949f04c7eda2d'
    print('NO_CANDIDATE', generated, connected, excluded)
    print('certificate_sha256', certificate)


if __name__ == '__main__':
    main()
