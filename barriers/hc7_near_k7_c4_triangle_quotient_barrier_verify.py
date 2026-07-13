#!/usr/bin/env python3
"""Verify the exact C4/common-triangle frame in K2 join the icosahedron."""

import networkx as nx


def build() -> tuple[nx.Graph, set[str]]:
    graph = nx.Graph()
    t, b = "t", "b"
    us = [f"u{i}" for i in range(5)]
    ws = [f"w{i}" for i in range(5)]
    ico = {t, b, *us, *ws}
    graph.add_nodes_from([*ico, "p", "q"])
    for i in range(5):
        graph.add_edge(t, us[i])
        graph.add_edge(b, ws[i])
        graph.add_edge(us[i], us[(i + 1) % 5])
        graph.add_edge(ws[i], ws[(i + 1) % 5])
        graph.add_edge(us[i], ws[i])
        graph.add_edge(us[i], ws[(i - 1) % 5])
    for vertex in ico:
        graph.add_edge("p", vertex)
        graph.add_edge("q", vertex)
    graph.add_edge("p", "q")
    return graph, ico


def adjacent(graph: nx.Graph, left: set[str], right: set[str]) -> bool:
    return any(graph.has_edge(x, y) for x in left for y in right)


def main() -> None:
    graph, ico = build()
    common = [
        {"p", "b", "w0", "w1", "w2", "w3", "w4"},
        {"q"},
        {"t"},
    ]
    roots = [
        {"u0", "u1"},
        {"u2"},
        {"u3"},
        {"u4"},
    ]
    bags = [*common, *roots]

    assert set().union(*bags) == set(graph)
    assert sum(map(len, bags)) == graph.number_of_nodes()
    assert all(nx.is_connected(graph.subgraph(bag)) for bag in bags)
    assert all(
        adjacent(graph, common[i], common[j])
        for i in range(3)
        for j in range(i + 1, 3)
    )
    assert all(
        adjacent(graph, triangle_bag, root_bag)
        for triangle_bag in common
        for root_bag in roots
    )

    root_edges = {
        (i, j)
        for i in range(4)
        for j in range(i + 1, 4)
        if adjacent(graph, roots[i], roots[j])
    }
    assert root_edges == {(0, 1), (1, 2), (2, 3), (0, 3)}

    assert nx.node_connectivity(graph) == 7
    assert nx.check_planarity(graph.subgraph(ico))[0]
    assert min(dict(graph.degree()).values()) == 7

    print("GREEN: spanning quotient is exactly K3 join C4")
    for index, bag in enumerate(common, 1):
        print(f"T{index}", sorted(bag))
    for index, bag in enumerate(roots, 1):
        print(f"X{index}", sorted(bag))
    print("root quotient edges", sorted(root_edges))
    print("kappa=7, delta=7; deleting p,q leaves the planar icosahedron")


if __name__ == "__main__":
    main()
