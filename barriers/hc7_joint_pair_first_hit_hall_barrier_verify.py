#!/usr/bin/env python3
"""Verify two first-hit Hall barriers for a jointly persistent edge pair.

The checker uses only the Python standard library.  It verifies two graphs:

* a nonadjacent-end exact-star-trace example on 13 vertices; and
* an adjacent-end EP/PE-transition example on 15 vertices.

Both graphs are 8-connected and 7-chromatic, and both contain an explicit
K7.  They are therefore barriers to intermediate palette-to-label claims,
not counterexamples to HC7.
"""

from __future__ import annotations

from itertools import combinations


Edge = frozenset[str]


def edge(x: str, y: str) -> Edge:
    assert x != y
    return frozenset((x, y))


class Graph:
    def __init__(self) -> None:
        self.vertices: set[str] = set()
        self.edges: set[Edge] = set()

    def add_vertex(self, vertex: str) -> None:
        self.vertices.add(vertex)

    def add_edge(self, x: str, y: str) -> None:
        self.vertices.update((x, y))
        self.edges.add(edge(x, y))

    def remove_edge(self, x: str, y: str) -> None:
        self.edges.remove(edge(x, y))

    def copy(self) -> "Graph":
        result = Graph()
        result.vertices = set(self.vertices)
        result.edges = set(self.edges)
        return result

    def has_edge(self, x: str, y: str) -> bool:
        return edge(x, y) in self.edges

    def neighbours(self, vertex: str) -> set[str]:
        return {
            next(iter(item - {vertex}))
            for item in self.edges
            if vertex in item
        }

    def connected(self, vertices: set[str] | None = None) -> bool:
        live = set(self.vertices if vertices is None else vertices)
        if len(live) <= 1:
            return True
        start = next(iter(live))
        seen = {start}
        stack = [start]
        while stack:
            current = stack.pop()
            for neighbour in self.neighbours(current) & live:
                if neighbour not in seen:
                    seen.add(neighbour)
                    stack.append(neighbour)
        return seen == live

    def connected_after_deleting(self, deleted: set[str]) -> bool:
        return self.connected(self.vertices - deleted)


def verify_connectivity_exactly_eight(graph: Graph) -> None:
    vertices = sorted(graph.vertices)
    for order in range(8):
        for deleted in combinations(vertices, order):
            assert graph.connected_after_deleting(set(deleted))
    minimum_degree = min(len(graph.neighbours(vertex)) for vertex in vertices)
    assert minimum_degree == 8
    low_vertex = next(
        vertex for vertex in vertices if len(graph.neighbours(vertex)) == 8
    )
    assert not graph.connected_after_deleting(graph.neighbours(low_vertex))


def proper_colouring(graph: Graph, colouring: dict[str, int]) -> bool:
    assert set(colouring) == graph.vertices
    return all(
        colouring[x] != colouring[y]
        for x, y in (tuple(item) for item in graph.edges)
    )


def verify_literal_clique(graph: Graph, vertices: set[str]) -> None:
    for x, y in combinations(sorted(vertices), 2):
        assert graph.has_edge(x, y)


def model_missing_pairs(
    graph: Graph, bags: dict[str, set[str]]
) -> set[frozenset[str]]:
    assert set().union(*bags.values()) == graph.vertices
    assert sum(map(len, bags.values())) == len(graph.vertices)
    for bag in bags.values():
        assert bag
        assert graph.connected(bag)
    missing: set[frozenset[str]] = set()
    for left, right in combinations(sorted(bags), 2):
        if not any(
            graph.has_edge(x, y) for x in bags[left] for y in bags[right]
        ):
            missing.add(frozenset((left, right)))
    return missing


def support_by_colour(
    graph: Graph,
    root: str,
    colouring: dict[str, int],
    bags: dict[str, set[str]],
    colours: set[int],
) -> dict[int, set[str]]:
    root_neighbours = graph.neighbours(root)
    return {
        colour: {
            label
            for label, bag in bags.items()
            if label != "R"
            and any(
                vertex in root_neighbours and colouring[vertex] == colour
                for vertex in bag
            )
        }
        for colour in colours
    }


def has_sdr(supports: dict[int, set[str]]) -> bool:
    colours = sorted(supports, key=lambda colour: len(supports[colour]))

    def search(index: int, used: set[str]) -> bool:
        if index == len(colours):
            return True
        return any(
            search(index + 1, used | {label})
            for label in supports[colours[index]] - used
        )

    return search(0, set())


def verify_contraction_trace(
    graph: Graph,
    deletion_graph: Graph,
    contracted: set[str],
    colouring: dict[str, int],
) -> None:
    assert proper_colouring(deletion_graph, colouring)
    assert graph.connected(contracted)
    alpha = colouring[next(iter(contracted))]
    assert all(colouring[vertex] == alpha for vertex in contracted)
    for outside in graph.vertices - contracted:
        if any(graph.has_edge(outside, inside) for inside in contracted):
            assert colouring[outside] != alpha


def build_nonadjacent_example() -> tuple[
    Graph, Graph, dict[str, int], dict[str, set[str]]
]:
    base_edges = {
        "01", "02", "03", "04", "05", "12", "13",
        "15", "23", "24", "34", "35", "45",
    }
    graph = Graph()
    base = {str(index) for index in range(6)}
    apices = {"A3", "A4", "A5"}
    for vertex in base | apices:
        graph.add_vertex(vertex)
    for item in base_edges:
        graph.add_edge(item[0], item[1])
    for x, y in combinations(sorted(apices), 2):
        graph.add_edge(x, y)
    for apex in apices:
        for vertex in base:
            graph.add_edge(apex, vertex)

    colouring = {
        "0": 0,
        "1": 0,
        "4": 0,
        "3": 1,
        "2": 2,
        "5": 2,
        "A3": 3,
        "A4": 4,
        "A5": 5,
        "p": 3,
        "y3": 3,
        "y4": 4,
        "y5": 5,
    }

    old_vertices = set(graph.vertices)
    graph.add_vertex("p")
    for vertex in old_vertices:
        if colouring[vertex] != colouring["p"]:
            graph.add_edge("p", vertex)

    for new_vertex in ("y3", "y4", "y5"):
        old_vertices = set(graph.vertices)
        graph.add_vertex(new_vertex)
        for vertex in old_vertices:
            if vertex in {"4", "p"}:
                continue
            if colouring[vertex] != colouring[new_vertex]:
                graph.add_edge(new_vertex, vertex)

    deletion_graph = graph.copy()
    deletion_graph.remove_edge("0", "1")
    deletion_graph.remove_edge("0", "4")
    bags = {
        "R": {"0"},
        "C": {"1", "2", "3", "5"},
        "B": {"4", "p"},
        "A3": {"A3"},
        "A4": {"A4"},
        "A5": {"A5"},
        "Y": {"y3", "y4", "y5"},
    }
    return graph, deletion_graph, colouring, bags


def verify_nonadjacent_example() -> None:
    graph, deletion_graph, colouring, bags = build_nonadjacent_example()
    verify_connectivity_exactly_eight(graph)

    clique = {"0", "1", "2", "3", "A3", "A4", "A5"}
    verify_literal_clique(graph, clique)
    seven_colouring = dict(colouring)
    seven_colouring["0"] = 6
    assert proper_colouring(graph, seven_colouring)

    expected_missing = {frozenset(("B", "Y"))}
    assert model_missing_pairs(graph, bags) == expected_missing
    assert model_missing_pairs(deletion_graph, bags) == expected_missing
    assert not graph.has_edge("1", "4")
    verify_contraction_trace(
        graph, deletion_graph, {"0", "1", "4"}, colouring
    )
    assert {
        vertex
        for vertex in graph.neighbours("0")
        if colouring[vertex] == colouring["0"]
    } == {"1", "4"}

    supports = support_by_colour(
        graph, "0", colouring, bags, {1, 2, 3, 4, 5}
    )
    assert supports[1] == {"C"}
    assert supports[2] == {"C"}
    assert not has_sdr(supports)


def build_adjacent_example() -> tuple[
    Graph,
    Graph,
    dict[str, int],
    dict[str, int],
    dict[str, set[str]],
]:
    vertices = {
        "v", "a", "b", "c1", "c2", "c3", "c4",
        "pA", "pB", "p1", "r1", "p2", "r2", "p3", "r3",
    }
    first = {
        "v": 0,
        "a": 0,
        "b": 2,
        "c1": 1,
        "c2": 3,
        "c3": 4,
        "c4": 5,
        "pA": 1,
        "pB": 1,
        "p1": 1,
        "r1": 0,
        "p2": 1,
        "r2": 2,
        "p3": 1,
        "r3": 0,
    }
    second = dict(first)
    second["v"] = 2
    y1 = {"p1", "r1"}
    y2 = {"p2", "r2"}

    deletion_graph = Graph()
    for vertex in vertices:
        deletion_graph.add_vertex(vertex)
    for x, y in combinations(sorted(vertices), 2):
        if first[x] == first[y] or second[x] == second[y]:
            continue
        if (x in y1 and y in y2) or (x in y2 and y in y1):
            continue
        deletion_graph.add_edge(x, y)

    graph = deletion_graph.copy()
    graph.add_edge("v", "a")
    graph.add_edge("v", "b")
    bags = {
        "R": {"v"},
        "A": {"a", "pA"},
        "B": {"b", "pB"},
        "C": {"c1", "c2", "c3", "c4"},
        "Y1": y1,
        "Y2": y2,
        "Y3": {"p3", "r3"},
    }
    return graph, deletion_graph, first, second, bags


def verify_adjacent_example() -> None:
    graph, deletion_graph, first, second, bags = build_adjacent_example()
    verify_connectivity_exactly_eight(graph)

    clique = {"v", "a", "b", "c1", "c2", "c3", "c4"}
    verify_literal_clique(graph, clique)
    seven_colouring = dict(first)
    seven_colouring["v"] = 6
    assert proper_colouring(graph, seven_colouring)
    assert proper_colouring(deletion_graph, first)
    assert proper_colouring(deletion_graph, second)

    expected_missing = {frozenset(("Y1", "Y2"))}
    assert model_missing_pairs(graph, bags) == expected_missing
    assert model_missing_pairs(deletion_graph, bags) == expected_missing

    core = clique
    for x, y in combinations(sorted(core), 2):
        expected = frozenset((x, y)) not in {
            frozenset(("v", "a")),
            frozenset(("v", "b")),
        }
        assert deletion_graph.has_edge(x, y) == expected
    assert graph.has_edge("a", "b")

    alpha_beta_vertices = {
        vertex for vertex in graph.vertices if first[vertex] in {0, 2}
    }
    assert deletion_graph.connected({"v"})
    assert not any(
        deletion_graph.has_edge("v", other)
        for other in alpha_beta_vertices - {"v"}
    )
    switched = dict(first)
    switched["v"] = 2
    assert switched == second

    supports = support_by_colour(
        graph, "v", first, bags, {1, 3, 4, 5}
    )
    assert supports[3] == {"C"}
    assert supports[4] == {"C"}
    assert supports[5] == {"C"}
    assert not has_sdr(supports)


def main() -> None:
    verify_nonadjacent_example()
    print(
        "nonadjacent star: kappa=8, singleton rooted K7^- model, "
        "joint persistence, exact trace, Hall failure, explicit K7"
    )
    verify_adjacent_example()
    print(
        "adjacent triangle: kappa=8, singleton rooted K7^- model, "
        "EP/PE transition, Hall failure, explicit K7"
    )
    print("verified joint-pair first-hit Hall barriers")


if __name__ == "__main__":
    main()
