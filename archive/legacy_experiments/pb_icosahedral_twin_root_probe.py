#!/usr/bin/env python3
"""Probe paired rooting after adjoining an adjacent true twin in one PB column."""

import networkx as nx

from pb_blowup_rooted_k5_probe import clique_minor


COLUMNS = {
    "a": {2},
    "b": {4},
    "r0": {6},
    "r1": {3},
    "r2": {9, 10},
    "r3": {7, 8, 11},
    "r4": {0, 1, 5},
}


def label_of(vertex: int) -> str:
    return next(label for label, column in COLUMNS.items() if vertex in column)


def main() -> None:
    canonical = {label: next(iter(column)) for label, column in COLUMNS.items()}
    failures = []
    for twin_of in range(12):
        graph = nx.icosahedral_graph()
        twin = f"t{twin_of}"
        graph.add_edge(twin, twin_of)
        graph.add_edges_from((twin, neighbour) for neighbour in list(graph[twin_of]) if neighbour != twin)
        assert nx.node_connectivity(graph) >= 5
        assert not nx.check_planarity(graph)[0]
        label = label_of(twin_of)
        for orientation in ((twin_of, twin), (twin, twin_of)):
            left_choice = canonical.copy()
            right_choice = canonical.copy()
            left_choice[label], right_choice[label] = orientation
            left = set(left_choice.values())
            right = set(right_choice.values())
            if clique_minor(graph, 5, (left, right)) is None:
                failures.append((twin_of, orientation, left, right))
                print("FAIL", failures[-1])
    print("icosahedral_twins", "tested=24", f"failures={len(failures)}")


if __name__ == "__main__":
    main()
