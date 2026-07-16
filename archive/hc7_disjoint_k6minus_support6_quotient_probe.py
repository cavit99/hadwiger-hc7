#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = ["networkx==3.6.1"]
# ///
"""Falsify the six-link quotient proposed for one support-six residue.

The left side is a minimal six-vertex K5 model: a K4 on 0,1,2,3,
an edge 4--5, and for each K4 vertex a nonempty subset of {4,5} as
neighbours.  Neither 4 nor 5 is allowed to be complete to the K4.

The right side is K6 minus edge 10--11 on vertices 6,...,11.  We add a
perfect matching between the two six-sets, representing six disjoint
linking paths after contraction, and test for a K7 minor.  A survivor
falsifies the quotient lemma; absence of survivors is only computational
evidence until the orbit coverage and minor certificates are exported.
"""

from __future__ import annotations

import itertools
from functools import lru_cache

import networkx as nx  # noqa: E402


def canonical_graph6(graph: nx.Graph) -> bytes:
    return nx.to_graph6_bytes(graph, header=False).strip()


@lru_cache(maxsize=None)
def has_k7(graph6: bytes) -> bool:
    graph = nx.from_graph6_bytes(graph6)
    vertices = tuple(graph)
    index = {vertex: i for i, vertex in enumerate(vertices)}
    n = len(vertices)
    adjacency = [0] * n
    for vertex in vertices:
        for neighbour in graph[vertex]:
            adjacency[index[vertex]] |= 1 << index[neighbour]

    connected: list[int] = []
    neighbourhood: dict[int, int] = {}
    for mask in range(1, 1 << n):
        seed = mask & -mask
        seen = seed
        frontier = seed
        while frontier:
            bit = frontier & -frontier
            frontier ^= bit
            new = adjacency[bit.bit_length() - 1] & mask & ~seen
            seen |= new
            frontier |= new
        if seen != mask:
            continue
        connected.append(mask)
        neighbours = 0
        todo = mask
        while todo:
            bit = todo & -todo
            todo ^= bit
            neighbours |= adjacency[bit.bit_length() - 1]
        neighbourhood[mask] = neighbours & ~mask

    connected.sort(key=lambda mask: (mask.bit_count(), mask))
    by_vertex = {
        vertex: tuple(mask for mask in connected if mask & (1 << vertex))
        for vertex in range(n)
    }

    def search(chosen: tuple[int, ...], available: int) -> bool:
        if len(chosen) == 7:
            return True
        if available.bit_count() < 7 - len(chosen):
            return False
        first_bit = available & -available
        first = first_bit.bit_length() - 1

        # The least available vertex is either unused by the minor model or
        # lies in the canonically next branch set.  This enumerates every
        # unordered collection of branch sets once.
        for branch in by_vertex[first]:
            if branch & ~available:
                continue
            if any(not (neighbourhood[branch] & old) for old in chosen):
                continue
            if search(chosen + (branch,), available ^ branch):
                return True
        return search(chosen, available ^ first_bit)

    return search((), (1 << n) - 1)


def host(contacts: tuple[int, ...], permutation: tuple[int, ...]) -> nx.Graph:
    graph = nx.Graph()
    graph.add_nodes_from(range(12))
    graph.add_edges_from(itertools.combinations(range(4), 2))
    graph.add_edge(4, 5)
    for q, mask in enumerate(contacts):
        if mask & 1:
            graph.add_edge(q, 4)
        if mask & 2:
            graph.add_edge(q, 5)

    graph.add_edges_from(
        edge for edge in itertools.combinations(range(6, 12), 2)
        if edge != (10, 11)
    )
    graph.add_edges_from((left, 6 + permutation[left]) for left in range(6))
    return graph


def main() -> None:
    if len(sys.argv) > 1 and sys.argv[1] == "repair":
        contacts = (1, 1, 1, 2)
        permutation = (0, 1, 2, 4, 5, 3)
        graph = host(contacts, permutation)
        assert not has_k7(canonical_graph6(graph))
        surviving_edges = []
        for left, right in itertools.combinations(range(12), 2):
            if graph.has_edge(left, right):
                continue
            augmented = graph.copy()
            augmented.add_edge(left, right)
            if not has_k7(canonical_graph6(augmented)):
                surviving_edges.append((left, right))
                print("nonrepair_edge", left, right, flush=True)
        print("nonrepair_count", len(surviving_edges))
        return

    tested = 0
    survivors: dict[bytes, tuple[tuple[int, ...], tuple[int, ...]]] = {}
    for contacts in itertools.product((1, 2, 3), repeat=4):
        if all(mask & 1 for mask in contacts):
            continue
        if all(mask & 2 for mask in contacts):
            continue
        for permutation in itertools.permutations(range(6)):
            tested += 1
            graph = host(contacts, permutation)
            if not has_k7(canonical_graph6(graph)):
                key = canonical_graph6(graph)
                survivors.setdefault(key, (contacts, permutation))
                print("first_survivor", key.decode())
                print("contacts", contacts, "matching", permutation)
                print("tested", tested)
                return
    print("tested", tested)
    print("minor_cache", has_k7.cache_info())
    print("labelled_survivor_isomorphism_upper_bound", len(survivors))
    for graph6, witness in list(survivors.items())[:20]:
        print(graph6.decode(), "contacts", witness[0], "matching", witness[1])


if __name__ == "__main__":
    main()
