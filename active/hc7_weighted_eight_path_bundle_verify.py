#!/usr/bin/env python3
"""Verify the width-five eight-path bundle barrier without dependencies."""

from itertools import combinations


CORES = {
    "A": ("a0", "a1", "a2", "a3"),
    "B": ("b0", "b1", "b2", "b3"),
    "C": ("c0", "c1", "c2", "c3"),
}
SPLITS = {"A": ("xA", "yA"), "B": ("xB", "yB"), "C": ("xC", "yC")}
CONTACTS = {
    "A": (("xA", "a0"), ("xA", "a1"), ("xA", "a2"), ("yA", "a3")),
    "B": (("xB", "b0"), ("xB", "b2"), ("yB", "b1"), ("yB", "b3")),
    "C": (("xC", "c2"), ("xC", "c3"), ("yC", "c0"), ("yC", "c1")),
}
CONNECTORS = (
    ("a0", "c2"),
    ("a1", "yB"),
    ("a2", "c3"),
    ("a3", "xB"),
    ("xA", "c1"),
    ("yA", "c0"),
    ("b1", "yC"),
    ("b2", "xC"),
)

CERTIFICATE = (
    ("b0", ("b1", "b2", "b3", "xB")),
    ("b3", ("b1", "b2", "xB", "yB")),
    ("yA", ("a3", "xA", "c0")),
    ("b1", ("b2", "xB", "yB", "yC")),
    ("b2", ("xB", "yB", "xC", "yC")),
    ("xB", ("a3", "yB", "xC", "yC")),
    ("yB", ("a1", "a3", "xC", "yC")),
    ("a0", ("a1", "a2", "a3", "xA", "c2")),
    ("a2", ("a1", "a3", "xA", "c2", "c3")),
    ("xC", ("a1", "a3", "c2", "c3", "yC")),
    ("a1", ("a3", "xA", "c2", "c3", "yC")),
    ("a3", ("xA", "c0", "c2", "c3", "yC")),
    ("xA", ("c0", "c1", "c2", "c3", "yC")),
    ("c0", ("c1", "c2", "c3", "yC")),
    ("c1", ("c2", "c3", "yC")),
    ("c2", ("c3", "yC")),
    ("c3", ("yC",)),
    ("yC", ()),
)


def edge(u: str, v: str) -> frozenset[str]:
    return frozenset((u, v))


def build_graph() -> dict[str, set[str]]:
    vertices = {v for core in CORES.values() for v in core}
    vertices |= {v for split in SPLITS.values() for v in split}
    adjacency = {v: set() for v in vertices}

    edges = set()
    for label, core in CORES.items():
        edges.update(edge(u, v) for u, v in combinations(core, 2))
        edges.add(edge(*SPLITS[label]))
        edges.update(edge(u, v) for u, v in CONTACTS[label])
    edges.update(edge(u, v) for u, v in CONNECTORS)

    assert len(vertices) == 18
    assert len(edges) == 41
    for pair in edges:
        u, v = tuple(pair)
        adjacency[u].add(v)
        adjacency[v].add(u)
    return adjacency


def verify_supports(adjacency: dict[str, set[str]]) -> None:
    used = {label: [] for label in CORES}
    owner = {v: label for label in CORES for v in (*CORES[label], *SPLITS[label])}
    for u, v in CONNECTORS:
        assert owner[u] != owner[v]
        used[owner[u]].append(u)
        used[owner[v]].append(v)
    assert sorted(map(len, used.values())) == [4, 6, 6]
    assert all(len(values) == len(set(values)) for values in used.values())

    for label, core in CORES.items():
        x, y = SPLITS[label]
        assert y in adjacency[x]
        assert all(v in adjacency[u] for u, v in combinations(core, 2))
        dx = {q for q in core if q not in adjacency[x]}
        dy = {q for q in core if q not in adjacency[y]}
        assert dx and dy and dx.isdisjoint(dy)


def verify_fill(adjacency: dict[str, set[str]]) -> int:
    graph = {v: set(neighbours) for v, neighbours in adjacency.items()}
    width = 0
    for vertex, expected in CERTIFICATE:
        actual = graph[vertex]
        assert actual == set(expected), (vertex, sorted(actual), sorted(expected))
        width = max(width, len(actual))
        for u, v in combinations(actual, 2):
            graph[u].add(v)
            graph[v].add(u)
        for neighbour in actual:
            graph[neighbour].remove(vertex)
        del graph[vertex]
    assert not graph
    assert width == 5
    return width


def main() -> None:
    graph = build_graph()
    verify_supports(graph)
    width = verify_fill(graph)
    print({"vertices": 18, "edges": 41, "connectors": 8, "fill_width": width})


if __name__ == "__main__":
    main()
