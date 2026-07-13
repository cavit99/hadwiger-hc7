#!/usr/bin/env python3
"""Classify candidate neighbourhoods at an interior degree-five vertex.

The five shore neighbours induce an outerplanar graph of independence
number at most two.  (The cyclic edges in a triangulated supergraph need
not be original shore edges.)  We enumerate all seven unlabelled
outerplanar five-vertex types with alpha<=2, then arbitrary contacts from
w and a and the optional edge wa.  Graphs already containing K6 as a minor
are discarded and the survivors are grouped up to isomorphism.
"""

from __future__ import annotations

import itertools

import networkx as nx


C = tuple(range(5))
W, A = 5, 6


def has_k6_minor_on_seven(g: nx.Graph) -> bool:
    # Six singleton branch sets after deleting one vertex.
    for deleted in g:
        h = g.copy()
        h.remove_node(deleted)
        if h.number_of_edges() == 15:
            return True

    # Or use all seven vertices and contract one edge.
    for u, v in g.edges():
        parts = [{x} for x in g if x not in (u, v)] + [{u, v}]
        if all(
            any(g.has_edge(x, y) for x in parts[i] for y in parts[j])
            for i in range(6) for j in range(i)
        ):
            return True
    return False


def has_k_minor(g: nx.Graph, k: int) -> bool:
    nodes = tuple(g.nodes())
    # Every branch set is nonempty.  Unused vertices receive label k.
    for assignment in itertools.product(range(k + 1), repeat=len(nodes)):
        if set(range(k)) - set(assignment):
            continue
        # Canonical first-occurrence order removes k! duplicate labellings.
        first = [assignment.index(i) for i in range(k)]
        if first != sorted(first):
            continue
        bags = [
            {nodes[j] for j, label in enumerate(assignment) if label == i}
            for i in range(k)
        ]
        if not all(nx.is_connected(g.subgraph(bag)) for bag in bags):
            continue
        if all(
            any(g.has_edge(x, y) for x in bags[i] for y in bags[j])
            for i in range(k) for j in range(i)
        ):
            return True
    return False


def alpha(g: nx.Graph) -> int:
    for size in range(g.number_of_nodes(), 0, -1):
        for subset in itertools.combinations(g.nodes(), size):
            if all(not g.has_edge(x, y) for x, y in itertools.combinations(subset, 2)):
                return size
    raise AssertionError


def canonical_classes(graphs: list[nx.Graph]) -> list[tuple[nx.Graph, int]]:
    classes: list[tuple[nx.Graph, int]] = []
    for graph in graphs:
        for i, (representative, count) in enumerate(classes):
            if nx.is_isomorphic(graph, representative):
                classes[i] = (representative, count + 1)
                break
        else:
            classes.append((graph, 1))
    return classes


def outerplanar(graph: nx.Graph) -> bool:
    cone = graph.copy()
    apex = max(cone.nodes(), default=-1) + 1
    cone.add_node(apex)
    cone.add_edges_from((apex, vertex) for vertex in graph)
    return nx.check_planarity(cone)[0]


def main() -> None:
    shore_types = []
    for graph in nx.graph_atlas_g():
        if len(graph) != 5 or not outerplanar(graph) or alpha(graph) > 2:
            continue
        shore_types.append(graph.copy())
    assert len(shore_types) == 7

    survivors: list[nx.Graph] = []
    for shore in shore_types:
        for w_mask in range(1 << 5):
            for a_mask in range(1 << 5):
                for wa in (False, True):
                    graph = shore.copy()
                    graph.add_nodes_from((W, A))
                    for i in C:
                        if w_mask & (1 << i):
                            graph.add_edge(W, i)
                        if a_mask & (1 << i):
                            graph.add_edge(A, i)
                    if wa:
                        graph.add_edge(W, A)
                    if alpha(graph) > 2:
                        continue
                    if has_k6_minor_on_seven(graph):
                        continue
                    survivors.append(graph)

    classes = canonical_classes(survivors)
    print("shore types", len(shore_types), "labelled survivors", len(survivors),
          "isomorphism classes", len(classes))
    moser = nx.Graph()
    moser.add_nodes_from(range(7))
    moser.add_edges_from((
        (0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (1, 6),
        (2, 6), (3, 4), (3, 5), (4, 5), (5, 6),
    ))
    k34 = nx.disjoint_union(nx.complete_graph(3), nx.complete_graph(4))
    for i, (graph, count) in enumerate(sorted(classes, key=lambda x: (sorted(dict(x[0].degree()).values()), x[0].number_of_edges()))):
        degrees = sorted((d for _, d in graph.degree()), reverse=True)
        print(i, "count", count, "edges", graph.number_of_edges(),
              "degrees", degrees,
              "eta>=5", has_k_minor(graph, 5),
              "planar", nx.check_planarity(graph)[0],
              "moser", nx.is_isomorphic(graph, moser),
              "k3+k4", nx.is_isomorphic(graph, k34),
              "graph6", nx.to_graph6_bytes(graph, header=False).decode().strip())


if __name__ == "__main__":
    main()
