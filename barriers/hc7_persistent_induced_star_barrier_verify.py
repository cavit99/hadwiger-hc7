#!/usr/bin/env python3
"""Verify the dual-truncated-icosahedron persistent-edge barrier."""

from itertools import combinations

import networkx as nx


def build_graphs():
    ico = nx.icosahedral_graph()
    planar, embedding = nx.check_planarity(ico)
    assert planar

    faces = []
    seen = set()
    for u, v in embedding.edges():
        if (u, v) not in seen:
            faces.append(tuple(embedding.traverse_face(u, v, seen)))
    assert faces == [
        (0, 8, 1), (0, 7, 8), (0, 11, 7), (0, 5, 11), (0, 1, 5),
        (1, 2, 6), (1, 8, 2), (1, 6, 5), (2, 3, 6), (2, 9, 3),
        (2, 8, 9), (3, 4, 6), (3, 10, 4), (3, 9, 10), (4, 5, 6),
        (4, 11, 5), (4, 10, 11), (7, 9, 8), (7, 10, 9),
        (7, 11, 10),
    ]

    h = nx.Graph()
    h.add_nodes_from(("V", u) for u in ico)
    h.add_nodes_from(("F", i) for i in range(len(faces)))
    edge_faces = {}
    for i, face in enumerate(faces):
        for u in face:
            h.add_edge(("V", u), ("F", i))
        for j, u in enumerate(face):
            edge = tuple(sorted((u, face[(j + 1) % 3])))
            edge_faces.setdefault(edge, []).append(i)
    for incident_faces in edge_faces.values():
        assert len(incident_faces) == 2
        h.add_edge(("F", incident_faces[0]), ("F", incident_faces[1]))

    g = h.copy()
    alpha = ("A", 0)
    beta = ("A", 1)
    g.add_edge(alpha, beta)
    for vertex in h:
        g.add_edge(alpha, vertex)
        g.add_edge(beta, vertex)
    return h, g, alpha, beta


def verify():
    h, g, alpha, beta = build_graphs()
    assert len(h) == 32 and h.number_of_edges() == 90
    assert nx.check_planarity(h)[0]
    assert nx.node_connectivity(h) == 5
    assert nx.node_connectivity(g) == 7

    root = ("F", 0)
    bags = {
        "R": {root},
        "S": {alpha, ("V", 0), ("F", 1)},
        "P": {beta},
        "C0": {("F", 17), ("F", 18), ("F", 19), ("F", 2),
               ("V", 7), ("V", 8)},
        "C1": {("F", 5), ("V", 1), ("V", 6)},
        "C2": {("F", 10), ("F", 6), ("F", 8), ("F", 9),
               ("V", 2), ("V", 3), ("V", 9)},
        "C3": {("F", 11), ("F", 12), ("F", 13), ("F", 14),
               ("F", 15), ("F", 16), ("F", 3), ("F", 4),
               ("F", 7), ("V", 10), ("V", 11), ("V", 4),
               ("V", 5)},
    }
    assert set().union(*bags.values()) == set(g)
    assert sum(map(len, bags.values())) == len(g)
    assert all(nx.is_connected(g.subgraph(bag)) for bag in bags.values())

    labels = list(bags)
    quotient_edges = set()
    for a, b in combinations(labels, 2):
        if any(g.has_edge(x, y) for x in bags[a] for y in bags[b]):
            quotient_edges.add(frozenset((a, b)))
    missing = {
        frozenset((a, b)) for a, b in combinations(labels, 2)
    } - quotient_edges
    assert missing == {frozenset(("C0", "C1"))}

    persistent = {
        frozenset((root, alpha)),
        frozenset((root, ("V", 0))),
        frozenset((root, ("F", 1))),
    }
    assert g.degree(root) == 8
    for edge in g.edges(root):
        edge = frozenset(edge)
        target = next(
            name for name, bag in bags.items()
            if name != "R" and next(iter(edge - {root})) in bag
        )
        contacts = {
            frozenset((x, y))
            for x in bags["R"] for y in bags[target] if g.has_edge(x, y)
        }
        assert (len(contacts) >= 2) == (edge in persistent)

    for first, second in combinations(persistent, 2):
        remaining = persistent - {first, second}
        assert remaining
    leaves = [next(iter(edge - {root})) for edge in persistent]
    assert all(g.has_edge(x, y) for x, y in combinations(leaves, 2))

    degree_five = next(vertex for vertex, degree in h.degree if degree == 5)
    separator = {alpha, beta, *h.neighbors(degree_five)}
    assert len(separator) == 7
    assert not nx.is_connected(g.subgraph(set(g) - separator))


if __name__ == "__main__":
    verify()
    print("verified persistent induced-star barrier")
