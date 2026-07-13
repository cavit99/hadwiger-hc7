#!/usr/bin/env python3
"""Bounded audit of the rooted-triangle obstruction and lobe lemma.

The test is exhaustive over the NetworkX graph atlas (all unlabeled
graphs of order at most seven), over every ordered choice-free root
triple, and over every actual three-cut of every three-connected atlas
graph.  It is supporting evidence only; the theorem has a hand proof.
"""

from itertools import combinations, product

import networkx as nx


def connected_root_bags(
    graph: nx.Graph, root: int, other_roots: set[int]
) -> list[frozenset[int]]:
    allowed = sorted(set(graph) - other_roots - {root})
    bags: list[frozenset[int]] = []
    for mask in range(1 << len(allowed)):
        bag = {root}
        bag.update(allowed[i] for i in range(len(allowed)) if mask >> i & 1)
        if nx.is_connected(graph.subgraph(bag)):
            bags.append(frozenset(bag))
    return bags


def adjacent(graph: nx.Graph, x: frozenset[int], y: frozenset[int]) -> bool:
    return any(graph.has_edge(u, v) for u in x for v in y)


def has_rooted_k3(graph: nx.Graph, roots: tuple[int, int, int]) -> bool:
    root_set = set(roots)
    choices = [
        connected_root_bags(graph, root, root_set - {root})
        for root in roots
    ]
    for bags in product(*choices):
        if any(bags[i] & bags[j] for i, j in combinations(range(3), 2)):
            continue
        if all(
            adjacent(graph, bags[i], bags[j])
            for i, j in combinations(range(3), 2)
        ):
            return True
    return False


def has_cutvertex_obstruction(
    graph: nx.Graph, roots: tuple[int, int, int]
) -> bool:
    root_set = set(roots)
    for x in graph:
        remainder = graph.copy()
        remainder.remove_node(x)
        surviving_roots = root_set - {x}
        if all(
            len(set(component) & surviving_roots) <= 1
            for component in nx.connected_components(remainder)
        ):
            return True
    return False


def verify() -> None:
    criterion_tests = 0
    lobe_tests = 0
    for graph0 in nx.graph_atlas_g():
        if len(graph0) < 3 or not nx.is_connected(graph0):
            continue
        graph = nx.convert_node_labels_to_integers(graph0)

        for roots in combinations(graph.nodes, 3):
            rooted = has_rooted_k3(graph, roots)
            obstructed = has_cutvertex_obstruction(graph, roots)
            assert rooted != obstructed
            criterion_tests += 1

        if len(graph) < 4 or nx.node_connectivity(graph) < 3:
            continue
        for gate in combinations(graph.nodes, 3):
            remainder = graph.copy()
            remainder.remove_nodes_from(gate)
            lobes = list(nx.connected_components(remainder))
            if len(lobes) != 2:
                continue
            for lobe in lobes:
                if len(lobe) < 2:
                    continue
                bridge = graph.subgraph(set(gate) | set(lobe)).copy()
                assert has_rooted_k3(bridge, gate)
                lobe_tests += 1

    print("VERIFIED")
    print(f"rooted_obstruction_triples={criterion_tests}")
    print(f"nontrivial_two_lobe_bridges={lobe_tests}")


if __name__ == "__main__":
    verify()
