#!/usr/bin/env python3
"""Falsify portal-capacity claims for overlapping q=2 rotation states.

The old and new missing sets are D={c,d}, E={c,e}.  The common portal
class is represented by two vertices c1,c2; the private classes by d,e.
The search asks whether all four three-of-four rooted carrier patterns can
fail simultaneously.
"""

from itertools import permutations

import networkx as nx


def connected_hitting(graph: nx.Graph, vertices: set[int], groups: tuple[set[int], ...]) -> bool:
    return bool(vertices) and nx.is_connected(graph.subgraph(vertices)) and all(vertices & group for group in groups)


def has_disjoint_group_carriers(
    graph: nx.Graph,
    left_groups: tuple[set[int], ...],
    right_groups: tuple[set[int], ...],
) -> bool:
    nodes = list(graph)
    for left_mask in range(1, 1 << len(nodes)):
        left = {nodes[i] for i in range(len(nodes)) if left_mask & (1 << i)}
        if not connected_hitting(graph, left, left_groups):
            continue
        available = set(nodes) - left
        for component in nx.connected_components(graph.subgraph(available)):
            if all(component & group for group in right_groups):
                return True
    return False


def overlap_robust_obstruction(graph: nx.Graph, terminals: tuple[int, ...]) -> bool:
    alpha, beta, c1, c2, d, e = terminals
    a, b = {alpha}, {beta}
    common, private_d, private_e = {c1, c2}, {d}, {e}
    demands = (
        ((a, common, private_d), (b, common)),
        ((a, common, private_d), (b, private_e)),
        ((a, common), (b, common, private_e)),
        ((a, private_d), (b, common, private_e)),
    )
    return all(not has_disjoint_group_carriers(graph, left, right) for left, right in demands)


def find_first(minimum_connectivity: int, require_nonplanar: bool = False) -> dict | None:
    for graph in nx.graph_atlas_g():
        if len(graph) < 6 or not nx.is_connected(graph):
            continue
        if nx.node_connectivity(graph) < minimum_connectivity:
            continue
        planar = nx.check_planarity(graph)[0]
        if require_nonplanar and planar:
            continue
        for terminals in permutations(graph.nodes, 6):
            if overlap_robust_obstruction(graph, terminals):
                return {
                    "minimum_connectivity": minimum_connectivity,
                    "actual_connectivity": nx.node_connectivity(graph),
                    "order": len(graph),
                    "size": graph.number_of_edges(),
                    "planar": planar,
                    "edges": sorted(tuple(sorted(edge)) for edge in graph.edges),
                    "terminals": terminals,
                }
    return None


def main() -> None:
    for connectivity in range(2, 7):
        print(find_first(connectivity))
    print({"nonplanar_kappa_3": find_first(3, require_nonplanar=True)})


if __name__ == "__main__":
    main()
