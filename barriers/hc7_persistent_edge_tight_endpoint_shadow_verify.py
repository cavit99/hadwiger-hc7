#!/usr/bin/env python3
"""Verify the tight-persistent-endpoint sharpness architecture.

Run with

    PYTHONPATH=active/runtime/deps python3 \
        barriers/hc7_persistent_edge_tight_endpoint_shadow_verify.py
"""

from __future__ import annotations

from itertools import combinations

import networkx as nx


U = tuple(f"u{i}" for i in range(5))
W = tuple(f"w{i}" for i in range(5))
RIM = tuple(f"r{i}" for i in range(5))
APICES = ("a", "b")


def planar_core() -> nx.Graph:
    graph = nx.Graph()
    graph.add_nodes_from(U + W + RIM + ("dB", "h"))
    for i in range(5):
        graph.add_edge(U[i], U[(i + 1) % 5])
        for rim, hub in ((W, "dB"), (RIM, "h")):
            graph.add_edge(rim[i], rim[(i + 1) % 5])
            graph.add_edge(hub, rim[i])
            graph.add_edge(U[i], rim[i])
            graph.add_edge(U[i], rim[(i - 1) % 5])
    return graph


def host() -> tuple[nx.Graph, nx.Graph]:
    core = planar_core()
    graph = core.copy()
    graph.add_edge(*APICES)
    for apex in APICES:
        graph.add_edges_from((apex, vertex) for vertex in core)
    return graph, core


def proper(graph: nx.Graph, colour: dict[str, int]) -> bool:
    return set(colour) == set(graph) and all(
        colour[u] != colour[v] for u, v in graph.edges()
    )


def list_colouring(
    graph: nx.Graph,
    lists: dict[str, frozenset[int]],
    *,
    remove_vertices: frozenset[str] = frozenset(),
    remove_edges: frozenset[frozenset[str]] = frozenset(),
) -> dict[str, int] | None:
    vertices = set(graph) - set(remove_vertices)
    colour: dict[str, int] = {}

    def search() -> dict[str, int] | None:
        if len(colour) == len(vertices):
            return dict(colour)
        vertex = min(
            (v for v in vertices if v not in colour),
            key=lambda v: (len(lists[v]), -graph.degree(v), v),
        )
        for value in sorted(lists[vertex]):
            if all(
                neighbour not in colour
                or colour[neighbour] != value
                or frozenset((vertex, neighbour)) in remove_edges
                for neighbour in graph[vertex]
                if neighbour in vertices
            ):
                colour[vertex] = value
                result = search()
                if result is not None:
                    return result
                del colour[vertex]
        return None

    return search()


def verify_planarity_and_connectivity(graph: nx.Graph, core: nx.Graph) -> None:
    planar, embedding = nx.check_planarity(core)
    assert planar
    embedding.check_structure()
    seen: set[tuple[str, str]] = set()
    faces = []
    for u, v in embedding.edges():
        if (u, v) not in seen:
            faces.append(embedding.traverse_face(u, v, seen))
    assert (core.number_of_nodes(), core.number_of_edges()) == (17, 45)
    assert len(faces) == 30 and all(len(face) == 3 for face in faces)
    assert nx.node_connectivity(core) == 5
    assert nx.node_connectivity(graph) == 7
    assert all(set(graph[apex]) == set(graph) - {apex} for apex in APICES)


def verify_interface(graph: nx.Graph) -> tuple[set[str], set[str], set[str]]:
    y = set(APICES) | set(U)
    x = y | {"r0"}
    left = {"dB"} | set(W)
    right = {"h", "r1", "r2", "r3", "r4"}
    assert left | x | right == set(graph)
    assert not any(graph.has_edge(u, v) for u in left for v in right)
    assert set().union(*(set(graph[v]) for v in left)) - left == y
    assert set().union(*(set(graph[v]) for v in right)) - right == x
    components = list(nx.connected_components(graph.subgraph(set(graph) - y)))
    assert {frozenset(left), frozenset(right | {"r0"})} == {
        frozenset(component) for component in components
    }
    return x, left, right


def fixed_trace() -> dict[str, int]:
    colour = dict(zip(U, (0, 1, 0, 1, 2), strict=True))
    colour.update(dict(zip(W, (2, 3, 2, 0, 3), strict=True)))
    colour.update({"dB": 1, "r0": 3, "a": 4, "b": 5})
    return colour


def verify_lists(
    graph: nx.Graph, x: set[str], left: set[str], right: set[str]
) -> tuple[nx.Graph, dict[str, frozenset[int]]]:
    trace = fixed_trace()
    assert proper(graph.subgraph(left | x), trace)
    lists = {
        vertex: frozenset(range(6))
        - {trace[neighbour] for neighbour in graph[vertex] if neighbour in x}
        for vertex in right
    }
    expected = {
        "h": frozenset((0, 1, 2)),
        "r1": frozenset((2,)),
        "r2": frozenset((2, 3)),
        "r3": frozenset((0, 3)),
        "r4": frozenset((1,)),
    }
    assert lists == expected
    shore = graph.subgraph(right).copy()
    assert list_colouring(shore, lists) is None
    assert all(
        list_colouring(shore, lists, remove_vertices=frozenset((vertex,)))
        is not None
        for vertex in shore
    )
    assert all(shore.degree(vertex) == len(lists[vertex]) + 1 for vertex in shore)
    return shore, lists


def model_bags() -> dict[str, set[str]]:
    return {
        "A0": {"a"},
        "A1": {"b"},
        "B0": {"u2", "w2"},
        "B1": {"u3"},
        "B2": {"w3"},
        "R": {
            "dB", "h", "r0", "r1", "r3", "r4",
            "u0", "u1", "u4", "w0", "w1", "w4",
        },
        "B": {"r2"},
    }


def missing_model_pairs(
    graph: nx.Graph, bags: dict[str, set[str]]
) -> set[frozenset[str]]:
    missing = set()
    for first, second in combinations(bags, 2):
        if not any(
            graph.has_edge(u, v) for u in bags[first] for v in bags[second]
        ):
            missing.add(frozenset((first, second)))
    return missing


def verify_model_and_persistent_edges(
    graph: nx.Graph,
    shore: nx.Graph,
    lists: dict[str, frozenset[int]],
) -> None:
    bags = model_bags()
    assert set().union(*bags.values()) == set(graph)
    assert sum(map(len, bags.values())) == len(graph)
    assert all(nx.is_connected(graph.subgraph(bag)) for bag in bags.values())
    assert missing_model_pairs(graph, bags) == {frozenset(("B2", "B"))}

    cross_edges = {
        frozenset((u, v))
        for u in bags["B"]
        for v in bags["R"]
        if graph.has_edge(u, v)
    }
    expected = {
        frozenset(("r2", "h")),
        frozenset(("r2", "r1")),
        frozenset(("r2", "r3")),
    }
    assert cross_edges == expected
    for edge in expected:
        modified = graph.copy()
        modified.remove_edge(*tuple(edge))
        assert missing_model_pairs(modified, bags) == {frozenset(("B2", "B"))}

    attaining = {}
    for edge in expected:
        result = list_colouring(shore, lists, remove_edges=frozenset((edge,)))
        attaining[edge] = result
        if result is not None:
            u, v = tuple(edge)
            assert result[u] == result[v]
    assert attaining[frozenset(("r2", "h"))] is None
    assert attaining[frozenset(("r2", "r1"))] is not None
    assert attaining[frozenset(("r2", "r3"))] is not None


def verify_boundary_edge_and_fan(graph: nx.Graph, x: set[str], left: set[str]) -> None:
    operation = frozenset(("u3", "r2"))
    modified = graph.copy()
    modified.remove_edge(*tuple(operation))
    colour = fixed_trace()
    colour.update({"h": 0, "r1": 2, "r2": 1, "r3": 3, "r4": 1})
    assert proper(modified, colour)
    assert colour["u3"] == colour["r2"] == 1

    paths = {
        0: ("r2", "u2", "u3"),
        2: ("r2", "r1", "u1", "w0", "dB", "w2", "u3"),
        3: ("r2", "r3", "u3"),
        4: ("r2", "a", "u3"),
        5: ("r2", "b", "u3"),
    }
    interiors = []
    for beta, path in paths.items():
        assert all(modified.has_edge(u, v) for u, v in zip(path, path[1:]))
        assert {colour[v] for v in path} <= {1, beta}
        interiors.append(set(path[1:-1]))
    assert all(not left_set & right_set for left_set, right_set in combinations(interiors, 2))

    y = set(APICES) | set(U)
    first_hits = set()
    for path in paths.values():
        first_hits.add(next(vertex for vertex in path[1:] if vertex in y))
    assert first_hits == {"u1", "u2", "u3", "a", "b"}

    fan = (
        ("r2", "u3"),
        ("r2", "u2"),
        ("r2", "r1", "u1"),
        ("r2", "r3", "u4"),
        ("r2", "a"),
        ("r2", "b"),
    )
    fan_interiors = []
    ends = set()
    for path in fan:
        assert all(graph.has_edge(u, v) for u, v in zip(path, path[1:]))
        assert path[-1] in y
        ends.add(path[-1])
        fan_interiors.append(set(path[1:]))
    assert len(ends) == 6
    assert all(not p & q for p, q in combinations(fan_interiors, 2))


def verify_terminals(graph: nx.Graph, core: nx.Graph) -> None:
    global_colour = {
        "u0": 0, "u1": 1, "u2": 2, "u3": 0, "u4": 3,
        "w0": 2, "w1": 0, "w2": 1, "w3": 2, "w4": 1,
        "dB": 3, "r0": 2, "r1": 0, "r2": 1, "r3": 2,
        "r4": 1, "h": 3, "a": 4, "b": 5,
    }
    assert proper(graph, global_colour)
    assert nx.check_planarity(core)[0]

    y = set(APICES) | set(U)
    boundary = {**dict(zip(U, (0, 1, 0, 1, 2), strict=True)), "a": 4, "b": 5}
    left_extension = dict(boundary)
    left_extension.update(dict(zip(W, (2, 3, 2, 0, 3), strict=True)))
    left_extension["dB"] = 1
    right_extension = dict(boundary)
    right_extension.update(dict(zip(RIM, (2, 3, 2, 0, 3), strict=True)))
    right_extension["h"] = 1
    assert proper(graph.subgraph(y | set(W) | {"dB"}), left_extension)
    assert proper(graph.subgraph(y | set(RIM) | {"h"}), right_extension)


def main() -> None:
    graph, core = host()
    verify_planarity_and_connectivity(graph, core)
    x, left, right = verify_interface(graph)
    shore, lists = verify_lists(graph, x, left, right)
    verify_model_and_persistent_edges(graph, shore, lists)
    verify_boundary_edge_and_fan(graph, x, left)
    verify_terminals(graph, core)

    print("GREEN: seven-connected K7-free aligned persistent-edge shadow")
    print("fixed trace: shore-filling vertex-minimal obstruction, all excess one")
    print("spanning K7^- model: three deletion-persistent edges at r2")
    print("responses: two attain the trace, one totally rejects it")
    print("boundary edge: five disjoint bichromatic paths and explicit six-fan")
    print("trust boundary: six-colourable; compatible exact-seven/apex-pair terminal")


if __name__ == "__main__":
    main()
