#!/usr/bin/env python3
"""Probe rooted K4-e minors in small 3-connected graphs.

The target bags are A,B,D,S, with all target edges except D--S.
For each ordered choice of four distinct roots (a,b,d,s), the search
requires the corresponding root to stay in its labelled branch set.
"""

from itertools import permutations, product

import networkx as nx


TARGET_EDGES = ((0, 1), (0, 2), (1, 2), (0, 3), (1, 3))


def rooted_diamond_model(graph: nx.Graph, roots: tuple[object, object, object, object]):
    vertices = list(graph.nodes())
    root_sets = [set(root) if isinstance(root, (tuple, list, set, frozenset)) else {root}
                 for root in roots]
    if any(root_sets[i] & root_sets[j] for i in range(4) for j in range(i + 1, 4)):
        return None
    occupied = set().union(*root_sets)
    free = [v for v in vertices if v not in occupied]
    # 0..3 are labelled bags; 4 means unused.
    for choices in product(range(5), repeat=len(free)):
        bags = [set(root_sets[i]) for i in range(4)]
        for vertex, choice in zip(free, choices):
            if choice < 4:
                bags[choice].add(vertex)
        if not all(nx.is_connected(graph.subgraph(bag)) for bag in bags):
            continue
        if all(
            any(graph.has_edge(x, y) for x in bags[i] for y in bags[j])
            for i, j in TARGET_EDGES
        ):
            return bags
    return None


def main():
    checked_graphs = checked_roots = 0
    for graph in nx.graph_atlas_g():
        if len(graph) < 4 or not nx.is_connected(graph):
            continue
        if nx.node_connectivity(graph) < 5:
            continue
        checked_graphs += 1
        nodes = tuple(graph.nodes())
        # Test the stronger form in which the D-root bag must contain
        # both ends of a prescribed edge.
        for a, b, s in permutations(nodes, 3):
            remaining = set(nodes) - {a, b, s}
            for x, y in graph.edges():
                if x not in remaining or y not in remaining:
                    continue
                roots = (a, b, (x, y), s)
                checked_roots += 1
                if rooted_diamond_model(graph, roots) is None:
                    print("COUNTEREXAMPLE", len(graph), sorted(graph.edges()), roots)
                    return
    print("PASS", checked_graphs, "3-connected atlas graphs", checked_roots, "root tuples")


if __name__ == "__main__":
    main()
