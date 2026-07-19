#!/usr/bin/env python3
"""Verify the order-three portal classification and its sharp barriers.

The complete-minor test is an exact decreasing-depth SMT encoding.  Every
branch set has one root, and every other selected vertex has a selected
neighbour at smaller depth.  Thus no bound is imposed on branch-set size.

Run with::

    PYTHONPATH=active/runtime/deps python3 \
      barriers/hc7_order8_three_vertex_portal_reversal_barrier_verify.py
"""

from __future__ import annotations

from itertools import combinations, product

import networkx as nx
from z3 import (
    And,
    Bool,
    If,
    Implies,
    Int,
    Not,
    Or,
    PbEq,
    PbLe,
    Solver,
    Sum,
    is_true,
    sat,
    unsat,
)


S = ("d", "e", "xd", "yd", "xe", "ye", "x0", "y0")
W = ("xe", "ye", "x0", "y0")
E3 = ("u1", "u2", "u3")


def connected(graph: nx.Graph, vertices: set[str]) -> bool:
    return bool(vertices) and nx.is_connected(graph.subgraph(vertices))


def adjacent(graph: nx.Graph, left: set[str], right: set[str]) -> bool:
    return any(graph.has_edge(u, v) for u in left for v in right)


def validate_model(graph: nx.Graph, bags: list[set[str]], order: int = 7) -> None:
    assert len(bags) == order and all(bags)
    assert sum(map(len, bags)) == len(set().union(*bags))
    assert all(connected(graph, bag) for bag in bags)
    assert all(
        adjacent(graph, bags[i], bags[j])
        for i in range(order)
        for j in range(i + 1, order)
    )


def k7_model(graph: nx.Graph) -> list[set[str]] | None:
    """Return an exact K7 model, or ``None`` after an exhaustive SMT test."""

    vertices = tuple(graph)
    order = len(vertices)
    index = {vertex: i for i, vertex in enumerate(vertices)}
    neighbours = tuple(
        tuple(index[other] for other in graph.neighbors(vertex))
        for vertex in vertices
    )
    edges = tuple((index[u], index[v]) for u, v in graph.edges())

    solver = Solver()
    solver.set("random_seed", 0)
    selected = [[Bool(f"x_{v}_{bag}") for bag in range(7)] for v in range(order)]
    root = [[Bool(f"r_{v}_{bag}") for bag in range(7)] for v in range(order)]
    depth = [[Int(f"h_{v}_{bag}") for bag in range(7)] for v in range(order)]

    for vertex in range(order):
        solver.add(PbLe([(selected[vertex][bag], 1) for bag in range(7)], 1))

    root_index = []
    for bag in range(7):
        solver.add(PbEq([(root[vertex][bag], 1) for vertex in range(order)], 1))
        for vertex in range(order):
            solver.add(
                Implies(
                    root[vertex][bag],
                    And(selected[vertex][bag], depth[vertex][bag] == 0),
                )
            )
            solver.add(
                Implies(
                    selected[vertex][bag],
                    And(depth[vertex][bag] >= 0, depth[vertex][bag] < order),
                )
            )
            solver.add(
                Implies(
                    And(selected[vertex][bag], Not(root[vertex][bag])),
                    Or(
                        [
                            And(
                                selected[other][bag],
                                depth[other][bag] < depth[vertex][bag],
                            )
                            for other in neighbours[vertex]
                        ]
                    ),
                )
            )
        root_index.append(
            Sum([If(root[vertex][bag], vertex, 0) for vertex in range(order)])
        )

    # Every unordered model has an ordering by increasing root name.
    for bag in range(6):
        solver.add(root_index[bag] < root_index[bag + 1])

    for first, second in combinations(range(7), 2):
        solver.add(
            Or(
                [
                    Or(
                        And(selected[u][first], selected[v][second]),
                        And(selected[v][first], selected[u][second]),
                    )
                    for u, v in edges
                ]
            )
        )

    verdict = solver.check()
    if verdict == unsat:
        return None
    assert verdict == sat
    model = solver.model()
    answer = [
        {
            vertices[vertex]
            for vertex in range(order)
            if is_true(model.eval(selected[vertex][bag]))
        }
        for bag in range(7)
    ]
    validate_model(graph, answer)
    return answer


def quotient_graph(
    e_edges: set[tuple[str, str]], portals: dict[str, str]
) -> nx.Graph:
    graph = nx.Graph()
    graph.add_nodes_from(S + E3 + ("D", "P0", "P1"))
    graph.add_edges_from(
        [
            ("d", "xd"),
            ("xd", "yd"),
            ("yd", "d"),
            ("e", "xe"),
            ("xe", "ye"),
            ("ye", "e"),
            ("P0", "P1"),
        ]
    )
    graph.add_edges_from(e_edges)
    for packet in ("P0", "P1"):
        graph.add_edges_from((packet, boundary) for boundary in S)
    graph.add_edges_from(("D", boundary) for boundary in S if boundary != "d")
    for vertex in E3:
        graph.add_edge("d", vertex)
        graph.add_edge("D", vertex)
    graph.add_edge("xd", portals["v"])
    graph.add_edge("yd", portals["v"])
    for boundary in W:
        graph.add_edge(boundary, portals[boundary])
    return graph


def path_between(graph: nx.Graph, left: str, right: str) -> set[str]:
    return set(nx.shortest_path(graph.subgraph(E3), left, right))


def verify_classification() -> nx.Graph:
    path_edge_sets = [
        {tuple(sorted(edge)) for edge in edges}
        for edges in (
            (("u1", "u2"), ("u2", "u3")),
            (("u1", "u2"), ("u1", "u3")),
            (("u1", "u3"), ("u2", "u3")),
        )
    ]
    triangle_edges = set(combinations(E3, 2))
    survivors = []

    for e_edges in path_edge_sets + [triangle_edges]:
        e_graph = nx.Graph(e_edges)
        for v in E3:
            for choices in product(E3, repeat=4):
                portals = {"v": v, **dict(zip(W, choices))}
                graph = quotient_graph(e_edges, portals)
                witness = None
                for boundary in W:
                    candidate = path_between(e_graph, v, portals[boundary])
                    if len(candidate) < 3:
                        witness = (boundary, candidate)
                        break
                if witness is None:
                    survivors.append((e_edges, portals))
                    continue

                boundary, centre = witness
                remainder = set(E3) - centre
                bags = [
                    {"P0"},
                    {"P1"},
                    {"d"},
                    {"xd"},
                    {"yd"},
                    centre | {boundary},
                    remainder | {"D", "e"},
                ]
                validate_model(graph, bags)

    # Three labelled paths, two orientations each.  Structurally these are
    # one endpoint-reversal configuration.
    assert len(survivors) == 6
    for e_edges, portals in survivors:
        e_graph = nx.Graph(e_edges)
        assert e_graph.number_of_edges() == 2
        assert e_graph.degree(portals["v"]) == 1
        opposite = next(
            vertex
            for vertex in E3
            if nx.shortest_path_length(e_graph, portals["v"], vertex) == 2
        )
        assert {portals[boundary] for boundary in W} == {opposite}

    # Return the canonical orientation of the unique quotient survivor.  Its
    # exact K7 exclusion is checked below by expanding D and then contracting
    # that expansion back to this graph.
    canonical = quotient_graph(
        {("u1", "u2"), ("u2", "u3")},
        {"v": "u1", "xe": "u3", "ye": "u3", "x0": "u3", "y0": "u3"},
    )
    # Either one extra portal or the closing path edge triggers the displayed
    # branch-set construction.
    extra_portal = canonical.copy()
    extra_portal.add_edge("x0", "u2")
    validate_model(
        extra_portal,
        [
            {"P0"}, {"P1"}, {"d"}, {"xd"}, {"yd"},
            {"u1", "u2", "x0"}, {"u3", "D", "e"},
        ],
    )
    closed_triangle = canonical.copy()
    closed_triangle.add_edge("u1", "u3")
    validate_model(
        closed_triangle,
        [
            {"P0"}, {"P1"}, {"d"}, {"xd"}, {"yd"},
            {"u1", "u3", "xe"}, {"u2", "D", "e"},
        ],
    )
    return canonical


def expanded_barrier(subdivisions: int = 0, second_contact: str | None = None) -> nx.Graph:
    assert subdivisions in (0, 1, 2)
    graph = nx.Graph()
    graph.add_nodes_from(S + E3 + ("z", "b1", "b2", "b3", "P0", "P1"))
    graph.add_edges_from(
        [
            ("d", "xd"), ("xd", "yd"), ("yd", "d"),
            ("e", "xe"), ("xe", "ye"), ("ye", "e"),
            ("u1", "u2"), ("P0", "P1"),
        ]
    )
    previous = "u2"
    for index in range(1, subdivisions + 1):
        current = f"t{index}"
        graph.add_edge(previous, current)
        previous = current
    graph.add_edge(previous, "u3")

    for packet in ("P0", "P1"):
        graph.add_edges_from((packet, boundary) for boundary in S)
    for index, vertex in enumerate(E3, 1):
        graph.add_edge("d", vertex)
        graph.add_edge(vertex, "z")
        graph.add_edge("z", f"b{index}")
        graph.add_edge(f"b{index}", "e")
    graph.add_edges_from(("u1", boundary) for boundary in ("xd", "yd"))
    graph.add_edges_from(("u3", boundary) for boundary in W)
    graph.add_edges_from(("z", boundary) for boundary in S[2:])

    if second_contact is not None:
        assert second_contact in E3
        graph.add_edges_from((("z", "r"), ("r", "z2"), ("z2", second_contact)))
    return graph


def verify_coloured_barrier(
    graph: nx.Graph,
    subdivisions: int,
    second_contact: str | None,
) -> None:
    colour = {
        "d": 0, "e": 0, "z": 0,
        "xd": 1, "xe": 1, "x0": 1,
        "yd": 2, "ye": 2, "y0": 2,
        "u1": 3, "b1": 3, "P0": 3,
        "u2": 4, "b2": 4, "P1": 4,
        "u3": 5, "b3": 5,
    }
    if subdivisions >= 1:
        colour["t1"] = 0
    if subdivisions >= 2:
        colour["t2"] = 3
    if second_contact is not None:
        colour["r"] = 1
        colour["z2"] = 0

    assert all(colour[u] != colour[v] for u, v in graph.edges())
    for index in range(1, 4):
        path = ("d", f"u{index}", "z", f"b{index}", "e")
        assert all(graph.has_edge(path[j], path[j + 1]) for j in range(4))
        assert {colour[vertex] for vertex in path} == {0, index + 2}
    assert set(graph.neighbors("d")) & set(E3) == set(E3)
    assert set(graph.neighbors("e")) & set(E3) == set()
    assert set(graph.neighbors("xd")) & set(E3) == {"u1"}
    assert set(graph.neighbors("yd")) & set(E3) == {"u1"}
    assert all(set(graph.neighbors(boundary)) & set(E3) == {"u3"} for boundary in W)
    expected_contacts = {"z"} if second_contact is None else {"z", "z2"}
    d_vertices = {"z", "b1", "b2", "b3", "r", "z2"} & set(graph)
    assert set().union(*(set(graph.neighbors(vertex)) & d_vertices for vertex in E3)) == expected_contacts
    assert k7_model(graph) is None

    if subdivisions == 0 and second_contact is None:
        split_colour = {
            "d": 0, "e": 3, "z": 0,
            "xd": 1, "xe": 1, "x0": 1,
            "yd": 2, "ye": 2, "y0": 2,
            "u1": 3, "u2": 1, "u3": 3,
            "b1": 1, "b2": 1, "b3": 1,
            # P0,P1 do not belong to the closed D-union-E side.  Values are
            # supplied only so the whole displayed graph can also be checked.
            "P0": 4, "P1": 5,
        }
        assert all(split_colour[u] != split_colour[v] for u, v in graph.edges())


def suppress_subdivision(graph: nx.Graph) -> nx.Graph:
    answer = graph.copy()
    internal = sorted(vertex for vertex in answer if vertex.startswith("t"))
    if not internal:
        return answer
    answer.remove_nodes_from(internal)
    answer.add_edge("u2", "u3")
    return answer


def contract_d_star(graph: nx.Graph) -> nx.Graph:
    answer = graph.copy()
    for leaf in ("b1", "b2", "b3"):
        answer = nx.contracted_nodes(answer, "z", leaf, self_loops=False)
    return nx.relabel_nodes(answer, {"z": "D"})


def main() -> None:
    canonical = verify_classification()
    base = expanded_barrier(0)
    verify_coloured_barrier(base, 0, None)
    contracted = contract_d_star(base)
    assert set(contracted) == set(canonical)
    assert {frozenset(edge) for edge in contracted.edges()} == {
        frozenset(edge) for edge in canonical.edges()
    }
    for subdivisions in (1, 2):
        graph = expanded_barrier(subdivisions)
        verify_coloured_barrier(graph, subdivisions, None)
        suppressed = suppress_subdivision(graph)
        assert set(suppressed) == set(base)
        assert {frozenset(edge) for edge in suppressed.edges()} == {
            frozenset(edge) for edge in base.edges()
        }
    for vertex in E3:
        verify_coloured_barrier(expanded_barrier(0, vertex), 0, vertex)
    print(
        "GREEN: three-vertex portal classification, exact reversal obstruction, "
        "three Kempe paths, subdivisions, and two-contact barriers verified"
    )


if __name__ == "__main__":
    main()
