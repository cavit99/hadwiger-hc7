#!/usr/bin/env python3
"""Audit the two-component lifting condition in the seven-vertex atlas.

The usable local certificate is a K4 model whose unused boundary vertices
contain an edge, so that the two anticomplete exterior components can be
anchored to adjacent roots.
"""

import itertools

import networkx as nx


def independent_number_at_most_two(graph):
    return not any(
        all(not graph.has_edge(x, y) for x, y in itertools.combinations(triple, 2))
        for triple in itertools.combinations(graph.nodes, 3)
    )


def connected(graph, bag):
    return nx.is_connected(graph.subgraph(bag))


def adjacent(graph, left, right):
    return any(graph.has_edge(x, y) for x in left for y in right)


def k4_models_at_most_five(graph):
    vertices = tuple(graph.nodes)
    for size in range(4, 6):
        for used in itertools.combinations(vertices, size):
            labels = [0]

            def search(index, maximum):
                if index == size:
                    if maximum != 3:
                        return None
                    bags = [set() for _ in range(4)]
                    for vertex, label in zip(used, labels):
                        bags[label].add(vertex)
                    if all(connected(graph, bag) for bag in bags) and all(
                        adjacent(graph, bags[i], bags[j])
                        for i, j in itertools.combinations(range(4), 2)
                    ):
                        return bags
                    return None
                for label in range(min(maximum + 1, 3) + 1):
                    labels.append(label)
                    result = search(index + 1, max(maximum, label))
                    if result is not None:
                        return result
                    labels.pop()
                return None

            model = search(1, 0)
            if model is not None:
                yield model


graphs = [
    graph
    for graph in nx.graph_atlas_g()
    if len(graph) == 7 and independent_number_at_most_two(graph)
]
weak_failures = []
strong_failures = []
for index, graph in enumerate(graphs):
    models = list(k4_models_at_most_five(graph))
    if not models:
        weak_failures.append((index, graph.number_of_edges(), graph))
    if not any(
        any(graph.has_edge(x, y) for x, y in itertools.combinations(set(graph) - set().union(*model), 2))
        for model in models
    ):
        strong_failures.append((index, graph.number_of_edges(), graph))

print("alpha<=2", len(graphs))
print("weak failures", [(i, e) for i, e, _ in weak_failures])
print("strong failures", [(i, e) for i, e, _ in strong_failures])
