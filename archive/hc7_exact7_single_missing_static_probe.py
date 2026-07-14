#!/usr/bin/env python3
"""Probe the contracted single-missing-duty gate architecture.

This is an adversarial discovery script, not a proof.  It tests whether a
small literal expansion can simultaneously realize the audited support
pattern, seven-connectivity, exact old-state attainment, and a width-five
certificate excluding a K7 minor.
"""

from __future__ import annotations

from itertools import combinations

import networkx as nx


S = ("c", "a1", "t1", "a2", "t2", "a3", "t3")
X = ("x1", "x2", "x3")
K = ("k1", "k2")
J = ("j1", "j2")
V = set(S + X + K + J + ("q", "ell"))


def add_complete_bipartite(graph: nx.Graph, left, right) -> None:
    graph.add_edges_from((u, v) for u in left for v in right)


def build() -> nx.Graph:
    graph = nx.Graph()
    graph.add_nodes_from(V)

    # The old thin packet and the second rich packet are S-full.
    add_complete_bipartite(graph, ("ell", "q"), S)

    # Exact lobe supports and a literal three-gate.
    graph.add_edge(*K)
    graph.add_edge(*J)
    add_complete_bipartite(graph, K, X)
    add_complete_bipartite(graph, J, X)
    graph.add_edges_from(combinations(X, 2))
    add_complete_bipartite(graph, K, ("c", "a1", "a2", "a3"))
    add_complete_bipartite(graph, J, ("c", "a1", "t2", "t3"))

    # Isolated-gate alternative: only the missing t1 has a gate contact;
    # c may contact the gate without funding a new paired duty.
    graph.add_edge("t1", "x1")
    graph.add_edges_from(("c", x) for x in X)

    # The pure Moser boundary under the proper four-colour partition
    # {0,5}|{2,3}|{4,6}|{1}.  The degree-four vertex 0 is t1, exactly
    # compensating for its unique gate contact.
    labels = {0: "t1", 5: "a1", 2: "a2", 3: "t2", 4: "a3", 6: "t3", 1: "c"}
    moser_edges = (
        (0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (1, 6),
        (2, 6), (3, 4), (3, 5), (4, 5), (5, 6),
    )
    graph.add_edges_from((labels[u], labels[v]) for u, v in moser_edges)
    return graph


def contract(graph: nx.Graph, vertices: set[str], name: str) -> nx.Graph:
    answer = nx.Graph()
    answer.add_nodes_from((set(graph) - vertices) | {name})
    for u, v in graph.edges:
        left = name if u in vertices else u
        right = name if v in vertices else v
        if left != right:
            answer.add_edge(left, right)
    return answer


def colouring(graph: nx.Graph, colours: int) -> dict[str, int] | None:
    order = sorted(graph, key=lambda v: graph.degree(v), reverse=True)
    assigned: dict[str, int] = {}

    def search() -> bool:
        if len(assigned) == len(order):
            return True
        vertex = max(
            (v for v in order if v not in assigned),
            key=lambda v: (len({assigned[w] for w in graph[v] if w in assigned}), graph.degree(v)),
        )
        forbidden = {assigned[w] for w in graph[vertex] if w in assigned}
        for colour in range(colours):
            if colour in forbidden:
                continue
            assigned[vertex] = colour
            if search():
                return True
            del assigned[vertex]
        return False

    return assigned if search() else None


def elimination_width(graph: nx.Graph, order: tuple[str, ...]) -> int:
    work = graph.copy()
    width = 0
    for vertex in order:
        later = list(work[vertex])
        width = max(width, len(later))
        work.add_edges_from(combinations(later, 2))
        work.remove_node(vertex)
    return width


def main() -> None:
    graph = build()
    connectivity = nx.node_connectivity(graph)

    minor = contract(graph, {"ell", "a1", "t1"}, "b1")
    witness = colouring(minor, 6)

    # A min-fill heuristic is enough if it returns width at most five;
    # the explicit order is printed for subsequent solver-free freezing.
    width, decomposition = nx.approximation.treewidth_min_fill_in(graph)
    print("minimum degree", min(dict(graph.degree()).values()))
    print("connectivity", connectivity)
    print("min-fill width", width)
    print("six-colouring after forcing B1", witness)
    if width <= 5:
        print("STATIC BARRIER: treewidth at most five, hence no K7 minor")
    else:
        print("no width-five certificate found")
    print("decomposition bags", sorted((sorted(bag) for bag in decomposition), key=lambda b: (len(b), b)))


if __name__ == "__main__":
    main()
