#!/usr/bin/env python3
"""Search standard 4-connected planar graphs for the homogeneous shell.

This is an adversarial test for a proposed triple-set rooted-K4 lemma.
It asks whether a 4-connected planar graph admits a spanning partition
into singleton a,b,c and connected X1,X2,X3 with exceptional word
(c,c,a), with no contacts outside the exact quotient support.
"""

from __future__ import annotations

from itertools import permutations, product

import networkx as nx


def antiprism(n: int) -> nx.Graph:
    graph = nx.Graph()
    for i in range(n):
        graph.add_edge(i, (i + 1) % n)
        graph.add_edge(n + i, n + (i + 1) % n)
        graph.add_edge(i, n + i)
        graph.add_edge(i, n + (i - 1) % n)
    return graph


def connected_part(graph: nx.Graph, vertices: set[int]) -> bool:
    return bool(vertices) and nx.is_connected(graph.subgraph(vertices))


def decompositions(graph: nx.Graph):
    vertices = set(graph)
    # Allowed quotient edges for roles a,b,c,1,2,3.
    allowed = {
        frozenset(edge) for edge in (
            ("b", "c"),
            ("a", "1"), ("b", "1"),
            ("a", "2"), ("b", "2"),
            ("b", "3"), ("c", "3"),
            ("1", "2"), ("2", "3"),
        )
    }
    required = allowed
    for a, b, c in permutations(vertices, 3):
        if graph.has_edge(a, b) or graph.has_edge(a, c) or not graph.has_edge(b, c):
            continue
        rest = sorted(vertices - {a, b, c})
        for assignment in product("123", repeat=len(rest)):
            rows = {"a": {a}, "b": {b}, "c": {c},
                    "1": set(), "2": set(), "3": set()}
            for vertex, role in zip(rest, assignment):
                rows[role].add(vertex)
            if not all(connected_part(graph, rows[role]) for role in "123"):
                continue
            contacts = set()
            valid = True
            for u, v in graph.edges():
                role_u = next(role for role, row in rows.items() if u in row)
                role_v = next(role for role, row in rows.items() if v in row)
                if role_u == role_v:
                    continue
                pair = frozenset((role_u, role_v))
                if pair not in allowed:
                    valid = False
                    break
                contacts.add(pair)
            if valid and contacts == required:
                yield rows


def main() -> None:
    graphs = [(f"antiprism-{n}", antiprism(n)) for n in range(4, 6)]
    for name, graph in graphs:
        assert nx.check_planarity(graph)[0]
        connectivity = nx.node_connectivity(graph)
        found = next(decompositions(graph), None)
        print(name, "n", len(graph), "kappa", connectivity,
              "homogeneous-shell", found)


if __name__ == "__main__":
    main()
