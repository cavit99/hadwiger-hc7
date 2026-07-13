#!/usr/bin/env python3
"""Search small 3-connected graphs for the robust rotation obstruction."""

from itertools import permutations

import networkx as nx


def has_disjoint_carriers(graph: nx.Graph, left: frozenset, right: frozenset) -> bool:
    """Return whether disjoint connected sets can contain left and right."""
    optional = set(graph) - set(left) - set(right)
    optional_list = list(optional)
    for mask in range(1 << len(optional_list)):
        carrier = set(left)
        carrier.update(
            optional_list[index]
            for index in range(len(optional_list))
            if mask & (1 << index)
        )
        if not nx.is_connected(graph.subgraph(carrier)):
            continue
        remainder = graph.subgraph(set(graph) - carrier)
        if right and all(vertex in remainder for vertex in right):
            component = nx.node_connected_component(remainder, next(iter(right)))
            if right <= component:
                return True
    return False


def robust_obstruction(graph: nx.Graph, terminals: tuple[int, ...]) -> bool:
    alpha, beta, a1, a2, b1, b2 = terminals
    demands = (
        (frozenset((alpha, a1, a2)), frozenset((beta, b1))),
        (frozenset((alpha, a1, a2)), frozenset((beta, b2))),
        (frozenset((alpha, a1)), frozenset((beta, b1, b2))),
        (frozenset((alpha, a2)), frozenset((beta, b1, b2))),
    )
    return all(not has_disjoint_carriers(graph, left, right) for left, right in demands)


def find_first(minimum_connectivity: int) -> dict | None:
    for graph in nx.graph_atlas_g():
        if len(graph) < 6 or not nx.is_connected(graph):
            continue
        if nx.node_connectivity(graph) < minimum_connectivity:
            continue
        for terminals in permutations(graph.nodes, 6):
            if robust_obstruction(graph, terminals):
                return {
                    "minimum_connectivity": minimum_connectivity,
                    "actual_connectivity": nx.node_connectivity(graph),
                    "order": len(graph),
                    "size": graph.number_of_edges(),
                    "planar": nx.check_planarity(graph)[0],
                    "edges": sorted(tuple(sorted(edge)) for edge in graph.edges),
                    "terminals": terminals,
                }
    return None


def main() -> None:
    for minimum_connectivity in range(3, 7):
        result = find_first(minimum_connectivity)
        print(result or {"minimum_connectivity": minimum_connectivity, "result": None})


if __name__ == "__main__":
    main()
