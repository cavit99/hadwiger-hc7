#!/usr/bin/env python3
"""Probe K7 minors in the maximal both-missing endpoint quotient.

The first path is a0-a1 with U1,U2 on a0 and U3,U4 on a1.  The second
path is b0-b1.  Each row C,U1,...,U4 is assigned L, R, or (for at most
one row) M at the second path; M is maximally joined to both endpoints.
All five rows form a clique.  We test K7 minors by all combinations of at
most two deletions/contractions, sufficient for this nine-vertex graph.
"""

from itertools import combinations, product

import networkx as nx


ROWS = ("C", "U1", "U2", "U3", "U4")


def build(state: tuple[str, ...]) -> nx.Graph:
    graph = nx.Graph()
    graph.add_nodes_from(("a0", "a1", "b0", "b1", *ROWS))
    graph.add_edge("a0", "a1")
    graph.add_edge("b0", "b1")
    graph.add_edges_from(combinations(ROWS, 2))
    graph.add_edges_from(("a0", row) for row in ("U1", "U2"))
    graph.add_edges_from(("a1", row) for row in ("U3", "U4"))
    for row, side in zip(ROWS, state, strict=True):
        if side in {"L", "M"}:
            graph.add_edge("b0", row)
        if side in {"R", "M"}:
            graph.add_edge("b1", row)
    return graph


def key(graph: nx.Graph) -> tuple[tuple[str, ...], tuple[tuple[str, str], ...]]:
    return tuple(sorted(graph)), tuple(sorted(tuple(sorted(edge)) for edge in graph.edges()))


def contract(graph: nx.Graph, edge: tuple[str, str], name: str) -> nx.Graph:
    left, right = edge
    result = nx.Graph()
    result.add_nodes_from(vertex for vertex in graph if vertex not in {left, right})
    result.add_node(name)
    for x, y in graph.edges():
        xx = name if x in {left, right} else x
        yy = name if y in {left, right} else y
        if xx != yy:
            result.add_edge(xx, yy)
    return result


def is_complete_order_seven(graph: nx.Graph) -> bool:
    return graph.number_of_nodes() == 7 and graph.number_of_edges() == 21


def k7_certificate(graph: nx.Graph) -> tuple[str, tuple] | None:
    vertices = list(graph)
    for deleted in combinations(vertices, 2):
        candidate = graph.copy()
        candidate.remove_nodes_from(deleted)
        if is_complete_order_seven(candidate):
            return "delete2", deleted

    for deleted in vertices:
        reduced = graph.copy()
        reduced.remove_node(deleted)
        for edge in list(reduced.edges()):
            candidate = contract(reduced, edge, "z")
            if is_complete_order_seven(candidate):
                return "delete1_contract1", (deleted, edge)

    seen: set[tuple] = set()
    for first_edge in list(graph.edges()):
        first = contract(graph, first_edge, "z1")
        for second_edge in list(first.edges()):
            second = contract(first, second_edge, "z2")
            state_key = key(second)
            if state_key in seen:
                continue
            seen.add(state_key)
            if is_complete_order_seven(second):
                return "contract2", (first_edge, second_edge)
    return None


def main() -> None:
    rows = []
    for state in product("LRM", repeat=5):
        if state.count("L") < 2 or state.count("R") < 2 or state.count("M") > 1:
            continue
        graph = build(state)
        rows.append((state, k7_certificate(graph)))

    forced = [entry for entry in rows if entry[1] is not None]
    survivors = [entry for entry in rows if entry[1] is None]
    print("states", len(rows), "K7", len(forced), "survivors", len(survivors))
    for state, certificate in rows:
        print("".join(state), "K7" if certificate else "OPEN", certificate or "")


if __name__ == "__main__":
    main()
