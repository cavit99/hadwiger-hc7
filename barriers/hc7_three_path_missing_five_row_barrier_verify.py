#!/usr/bin/env python3
"""Verify the sharp one-missing-contact three-path barrier."""

from __future__ import annotations

from itertools import combinations
import sys

sys.path.insert(0, "active/runtime/deps")

import networkx as nx
from z3 import And, Bool, If, Implies, Int, Not, Or, PbEq, PbLe, Solver, Sum, is_true, sat, unsat


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def build(extra_contact: str | None = None) -> nx.Graph:
    graph = nx.Graph()
    U = [f"u{i}" for i in range(4)]
    B = [f"b{i}" for i in range(3)]
    X = [f"x{i}" for i in range(5)]
    Y = [f"y{i}" for i in range(5)]
    graph.add_nodes_from(U + B + X + Y + ["v"])

    for index in range(4):
        graph.add_edge(U[index], U[(index + 1) % 4])
        graph.add_edge(U[index], X[index])
    for index in range(5):
        graph.add_edge(X[index], X[(index + 1) % 5])
        graph.add_edge("v", X[index])
        graph.add_edge("b1", X[index])
        graph.add_edge("b2", X[index])
    for vertex in B:
        graph.add_edge("v", vertex)
    graph.add_edge("b0", "x3")
    graph.add_edge("b0", "x4")

    for index in range(1, 5):
        graph.add_edge("y0", f"y{index}")
    graph.add_edges_from(
        (("y1", "y2"), ("y2", "y3"), ("y3", "y4"), ("y4", "y1"))
    )
    graph.add_edges_from(
        (
            ("b1", "u0"),
            ("b1", "y1"), ("y1", "u0"),
            ("b1", "y2"), ("y2", "u0"),
            ("b1", "y3"), ("y3", "u0"),
            ("y1", "u1"), ("y1", "u2"), ("y1", "u3"),
            ("y1", "b2"),
        )
    )
    if extra_contact is not None:
        graph.add_edge("b0", extra_contact)
    return graph


def validate_model(graph: nx.Graph, branches: tuple[set[str], ...]) -> None:
    require(
        len(branches) == 7 and all(branches),
        "the certificate must have seven nonempty branch sets",
    )
    require(
        sum(map(len, branches)) == len(set().union(*branches)),
        "branch sets must be pairwise disjoint",
    )
    require(
        all(nx.is_connected(graph.subgraph(branch)) for branch in branches),
        "every branch set must be connected",
    )
    require(
        all(
            any(graph.has_edge(left, right) for left in first for right in second)
            for first, second in combinations(branches, 2)
        ),
        "every two branch sets must be adjacent",
    )


def exact_k7_model(graph: nx.Graph) -> tuple[set[str], ...] | None:
    """Exact decreasing-depth encoding of seven connected branch sets."""
    vertices = sorted(graph)
    index = {vertex: position for position, vertex in enumerate(vertices)}
    order = len(vertices)
    target = 7
    assigned = [
        [Bool(f"x_{vertex}_{bag}") for bag in range(target)]
        for vertex in range(order)
    ]
    root = [
        [Bool(f"r_{vertex}_{bag}") for bag in range(target)]
        for vertex in range(order)
    ]
    depth = [
        [Int(f"d_{vertex}_{bag}") for bag in range(target)]
        for vertex in range(order)
    ]
    solver = Solver()
    solver.set(timeout=60_000)

    for vertex in range(order):
        solver.add(PbLe([(assigned[vertex][bag], 1) for bag in range(target)], 1))

    root_indices = []
    for bag in range(target):
        solver.add(PbEq([(root[vertex][bag], 1) for vertex in range(order)], 1))
        for vertex, name in enumerate(vertices):
            solver.add(
                Implies(root[vertex][bag], And(assigned[vertex][bag], depth[vertex][bag] == 0)),
                Implies(assigned[vertex][bag], And(depth[vertex][bag] >= 0, depth[vertex][bag] < order)),
                Implies(
                    And(assigned[vertex][bag], Not(root[vertex][bag])),
                    Or(
                        *[
                            And(
                                assigned[index[neighbour]][bag],
                                depth[index[neighbour]][bag] < depth[vertex][bag],
                            )
                            for neighbour in graph[name]
                        ]
                    ),
                ),
            )
        root_indices.append(
            Sum([If(root[vertex][bag], vertex, 0) for vertex in range(order)])
        )
    for bag in range(target - 1):
        solver.add(root_indices[bag] < root_indices[bag + 1])

    indexed_edges = [(index[left], index[right]) for left, right in graph.edges()]
    for first, second in combinations(range(target), 2):
        solver.add(
            Or(
                *[
                    And(assigned[left][first], assigned[right][second])
                    for left, right in indexed_edges
                ],
                *[
                    And(assigned[right][first], assigned[left][second])
                    for left, right in indexed_edges
                ],
            )
        )

    result = solver.check()
    if result == unsat:
        return None
    require(result == sat, f"minor solver returned {result}")
    model = solver.model()
    branches = tuple(
        {
            vertices[vertex]
            for vertex in range(order)
            if is_true(model.eval(assigned[vertex][bag]))
        }
        for bag in range(target)
    )
    validate_model(graph, branches)
    return branches


def main() -> None:
    graph = build()
    require(graph.number_of_nodes() == 18, "the barrier must have order eighteen")
    require(nx.node_connectivity(graph) == 3, "the host must be three-connected")
    require(
        nx.node_connectivity(graph.subgraph({f"y{i}" for i in range(5)})) == 3,
        "the far-side wheel must be three-connected",
    )

    cyclic_sets = (
        {"u0", "x0"}, {"u1", "x1"}, {"u2", "x2"},
        {"u3", "x3"}, {"x4"},
    )
    require(
        all(nx.is_connected(graph.subgraph(item)) for item in cyclic_sets),
        "all five cyclic sets must be connected",
    )
    require(
        all(
            any(
                graph.has_edge(left, right)
                for left in cyclic_sets[index]
                for right in cyclic_sets[(index + 1) % 5]
            )
            for index in range(5)
        ),
        "consecutive cyclic sets must be adjacent",
    )

    colouring = {
        "b0": 0, "b1": 0, "u0": 0, "u2": 0, "y0": 0,
        "b2": 1, "u1": 1, "u3": 1, "y4": 1,
        "v": 2, "y1": 2,
        "x0": 3, "x3": 3, "y2": 3,
        "x1": 4, "x4": 4, "y3": 4,
        "x2": 5,
    }
    deleted = graph.copy()
    deleted.remove_edge("b1", "u0")
    require(
        all(colouring[left] != colouring[right] for left, right in deleted.edges()),
        "the displayed colouring must be proper after deleting b1-u0",
    )
    require(
        colouring["b1"] == colouring["u0"] == colouring["u2"],
        "I union {b1} must be monochromatic",
    )
    require(
        colouring["b2"] == colouring["u1"] == colouring["u3"],
        "J union {b2} must be monochromatic",
    )
    require(
        {colouring[f"y{i}"] for i in (1, 2, 3)} == {2, 3, 4},
        "the three path interiors must use the three advertised colours",
    )

    Y = {f"y{i}" for i in range(5)}
    boundary = {f"u{i}" for i in range(4)} | {f"b{i}" for i in range(3)}
    met = {vertex for vertex in boundary if set(graph[vertex]) & Y}
    require(
        met == boundary - {"b0"},
        "the far-side subgraph must meet exactly six boundary labels",
    )
    require(exact_k7_model(graph) is None, "the base graph must be K7-minor-free")
    print("base: exact K7-minor exclusion verified")

    for portal in ("y1", "y2", "y3", "y4"):
        augmented = build(portal)
        model = exact_k7_model(augmented)
        require(model is not None, f"adding b0-{portal} must create a K7 minor")
        print(f"b0-{portal}: K7 model verified")
    print("GREEN: the one-missing-contact barrier is verified")


if __name__ == "__main__":
    main()
