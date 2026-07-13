#!/usr/bin/env python3
"""Verify the five-connected birooted-K4 counterarchitecture."""

from __future__ import annotations

import networkx as nx

from birooted_k4_principle_search import (
    colourings4,
    has_birooted_k4,
)


def colourable(graph: nx.Graph, number: int) -> bool:
    order = sorted(graph, key=lambda vertex: -graph.degree(vertex))
    colours: dict[object, int] = {}

    def search(index: int) -> bool:
        if index == len(order):
            return True
        vertex = order[index]
        forbidden = {colours[w] for w in graph[vertex] if w in colours}
        for colour in range(number):
            if colour not in forbidden:
                colours[vertex] = colour
                if search(index + 1):
                    return True
                del colours[vertex]
        return False

    return search(0)


def slice_graph():
    graph = nx.Graph()
    a = [f"a{i}" for i in range(4)]
    b = [f"b{i}" for i in range(4)]
    graph.add_nodes_from(a + b)
    graph.add_edges_from(zip(a, a[1:]))
    graph.add_edges_from(zip(b, b[1:]))
    graph.add_edges_from((x, y) for x in a for y in b)
    x_set = {a[0], a[1], b[0], b[3]}
    y_set = {a[2], a[3], b[0], b[3]}
    return graph, a, b, x_set, y_set


def ambient_graph():
    graph, a, b, x_set, y_set = slice_graph()
    graph = graph.copy()
    graph.add_edges_from([("d0", "d1"), ("u", "w")])
    for blocker in ("d0", "d1"):
        graph.add_edges_from((blocker, vertex) for vertex in a + b)
    graph.add_edges_from([("u", "d1"), ("w", "d1")])
    graph.add_edges_from(("u", vertex) for vertex in x_set)
    graph.add_edges_from(("w", vertex) for vertex in y_set)

    # Two alpha-coloured relay vertices provide the nontrivial matched
    # Kempe carriers.  They have no edge to u,w,d0,d1.
    graph.add_edges_from([("a0", "h0"), ("h0", "a2")])
    graph.add_edges_from([("a1", "h1"), ("h1", "a3")])
    return graph, a, b, x_set, y_set


def main() -> None:
    graph, a, b, x_set, y_set = slice_graph()
    integer_graph = nx.convert_node_labels_to_integers(graph, label_attribute="old")
    old_to_new = {data["old"]: vertex for vertex, data in integer_graph.nodes(data=True)}
    integer_x = {old_to_new[v] for v in x_set}
    integer_y = {old_to_new[v] for v in y_set}
    colourings = list(colourings4(integer_graph))

    assert nx.node_connectivity(graph) == 5
    assert not colourable(graph, 3) and colourable(graph, 4)
    assert all({colouring[v] for v in integer_x} == set(range(4))
               for colouring in colourings)
    assert all({colouring[v] for v in integer_y} == set(range(4))
               for colouring in colourings)
    assert not has_birooted_k4(integer_graph, integer_x, integer_y)

    ambient, a, b, x_set, y_set = ambient_graph()
    assert not colourable(ambient, 6)
    deleted = ambient.copy()
    deleted.remove_edge("u", "w")

    # Four colours on the two paths, alpha=4, beta=5.
    colouring = {
        a[0]: 0, a[2]: 0,
        a[1]: 1, a[3]: 1,
        b[0]: 2, b[2]: 2,
        b[1]: 3, b[3]: 3,
        "u": 4, "w": 4, "d0": 4, "h0": 4, "h1": 4,
        "d1": 5,
    }
    assert all(colouring[x] != colouring[y] for x, y in deleted.edges())

    carriers = [
        ["u", a[0], "h0", a[2], "w"],
        ["u", a[1], "h1", a[3], "w"],
        ["u", b[0], "w"],
        ["u", b[3], "w"],
    ]
    interiors = []
    for colour, path in enumerate(carriers):
        assert all(deleted.has_edge(path[i], path[i + 1])
                   for i in range(len(path) - 1))
        assert {colouring[v] for v in path} == {4, colour}
        interiors.append(set(path[1:-1]))
    assert all(interiors[i].isdisjoint(interiors[j])
               for i in range(4) for j in range(i + 1, 4))

    print({
        "slice_order": len(graph),
        "slice_connectivity": nx.node_connectivity(graph),
        "four_colourings": len(colourings),
        "X": sorted(x_set),
        "Y": sorted(y_set),
        "birooted_K4": False,
        "ambient_six_colourable": False,
        "matched_disjoint_carriers": len(carriers),
    })


if __name__ == "__main__":
    main()
