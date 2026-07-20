#!/usr/bin/env python3
"""Exhaust the five-connected single-vertex splits of PB."""

from itertools import product

import networkx as nx

from pb_blowup_rooted_k5_probe import clique_minor, pb


def main() -> None:
    quotient = pb()
    nonplanar = five_connected = failures = 0
    for split_vertex in quotient:
        neighbours = tuple(quotient[split_vertex])
        for pattern in product((1, 2, 3), repeat=len(neighbours)):
            graph = quotient.copy()
            graph.remove_node(split_vertex)
            x, y = f"{split_vertex}x", f"{split_vertex}y"
            graph.add_edge(x, y)
            for neighbour, incidence in zip(neighbours, pattern):
                if incidence & 1:
                    graph.add_edge(x, neighbour)
                if incidence & 2:
                    graph.add_edge(y, neighbour)
            if nx.check_planarity(graph)[0]:
                continue
            nonplanar += 1
            if nx.node_connectivity(graph) < 5:
                continue
            five_connected += 1
            print("five_connected_split", split_vertex, pattern)
            fixed = set(quotient) - {split_vertex}
            for left_choice in (x, y):
                for right_choice in (x, y):
                    if clique_minor(
                        graph,
                        5,
                        (fixed | {left_choice}, fixed | {right_choice}),
                    ) is None:
                        failures += 1
                        print(
                            "FAIL",
                            split_vertex,
                            pattern,
                            left_choice,
                            right_choice,
                        )
    print(
        "pb_single_splits",
        f"nonplanar={nonplanar}",
        f"five_connected={five_connected}",
        f"paired_failures={failures}",
    )


if __name__ == "__main__":
    main()
