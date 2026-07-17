#!/usr/bin/env python3
"""Verify the two-missing-colour-path quotient barrier.

Requires NetworkX and z3-solver.  The repository runtime supplies NetworkX;
z3-solver is used only for the finite K7-minor exclusion.
"""

from __future__ import annotations

from itertools import combinations
import sys

sys.path.insert(0, "active/runtime/deps")

import networkx as nx
from z3 import And, Bool, If, Int, Not, Or, Solver, Sum, is_true, sat, unsat


def build_quotient() -> nx.Graph:
    graph = nx.Graph()
    graph.add_nodes_from(
        ["p", "q"]
        + [f"A{i}" for i in range(5)]
        + [f"B{i}" for i in range(5)]
        + ["u", "v", "w"]
    )
    for i in range(5):
        graph.add_edge(f"A{i}", f"A{(i + 1) % 5}")
        graph.add_edge(f"B{i}", f"B{(i + 1) % 5}")
        graph.add_edge("p", f"A{i}")
        graph.add_edge("q", f"B{i}")
        graph.add_edge(f"A{i}", f"B{i}")
        graph.add_edge(f"A{(i + 1) % 5}", f"B{i}")
    graph.remove_edge("p", "A0")
    graph.remove_edge("p", "A1")

    for attachment in ("u", "v", "w"):
        for terminal in ("p", "A1", "A2"):
            graph.add_edge(attachment, terminal)
    graph.add_edges_from(combinations(("u", "v", "w"), 2))
    return graph


def build_host() -> nx.Graph:
    graph = build_quotient()
    roots = ("A0", "A4", "p", "A1")
    triangle = ("r0", "r1", "r2")
    graph.add_edges_from(combinations(triangle, 2))
    for vertex in triangle:
        for root in roots:
            graph.add_edge(vertex, root)
    graph.add_edges_from((('r0', 'u'), ('r1', 'v'), ('r2', 'w')))
    return graph


def is_clique(graph: nx.Graph, vertices: set[str]) -> bool:
    return all(graph.has_edge(left, right) for left, right in combinations(vertices, 2))


def has_linkage(
    graph: nx.Graph,
    first_pair: tuple[str, str],
    second_pair: tuple[str, str],
) -> bool:
    """Return whether two vertex-disjoint paths join the prescribed pairs."""
    first, second = first_pair, second_pair
    for path in nx.all_simple_paths(graph, *first):
        remainder = graph.copy()
        remainder.remove_nodes_from(path)
        if second[0] in remainder and second[1] in remainder:
            if nx.has_path(remainder, *second):
                return True
    return False


def has_k7_minor(graph: nx.Graph) -> bool:
    """Exact finite test using a spanning branch-set flow formulation."""
    assert nx.is_connected(graph)
    vertices = list(graph)
    index = {vertex: position for position, vertex in enumerate(vertices)}
    order = len(vertices)
    target = 7
    arcs = [
        arc
        for left, right in graph.edges()
        for arc in ((index[left], index[right]), (index[right], index[left]))
    ]

    member = [
        [Bool(f"member_{vertex}_{branch}") for branch in range(target)]
        for vertex in range(order)
    ]
    root = [
        [Bool(f"root_{vertex}_{branch}") for branch in range(target)]
        for vertex in range(order)
    ]
    size = [Int(f"size_{branch}") for branch in range(target)]
    supply = [
        [Int(f"supply_{vertex}_{branch}") for branch in range(target)]
        for vertex in range(order)
    ]
    flow = {
        (left, right, branch): Int(f"flow_{left}_{right}_{branch}")
        for left, right in arcs
        for branch in range(target)
    }

    solver = Solver()
    solver.set(timeout=60_000)

    # A connected host permits every minor model to be made spanning.
    for vertex in range(order):
        solver.add(
            Sum([If(member[vertex][branch], 1, 0) for branch in range(target)])
            == 1
        )

    root_indices = []
    for branch in range(target):
        solver.add(
            size[branch]
            == Sum([If(member[vertex][branch], 1, 0) for vertex in range(order)]),
            size[branch] >= 1,
        )

        # The root is canonically the least-indexed member of the branch set.
        for vertex in range(order):
            solver.add(
                root[vertex][branch]
                == And(
                    member[vertex][branch],
                    *[Not(member[earlier][branch]) for earlier in range(vertex)],
                )
            )
        root_indices.append(
            Sum(
                [
                    vertex * If(root[vertex][branch], 1, 0)
                    for vertex in range(order)
                ]
            )
        )

        # The root supplies |B|-1 units and every other branch vertex consumes
        # one unit.  Flow may use precisely the edges internal to the branch.
        for vertex in range(order):
            root_value = If(root[vertex][branch], 1, 0)
            solver.add(
                supply[vertex][branch] >= 0,
                supply[vertex][branch] <= order * root_value,
                supply[vertex][branch] <= size[branch],
                supply[vertex][branch]
                >= size[branch] - order * (1 - root_value),
            )
            incoming = Sum(
                [flow[(left, right, branch)] for left, right in arcs if right == vertex]
            )
            outgoing = Sum(
                [flow[(left, right, branch)] for left, right in arcs if left == vertex]
            )
            solver.add(
                outgoing - incoming
                == supply[vertex][branch] - If(member[vertex][branch], 1, 0)
            )

        for left, right in arcs:
            solver.add(
                flow[(left, right, branch)] >= 0,
                flow[(left, right, branch)]
                <= order * If(And(member[left][branch], member[right][branch]), 1, 0),
            )

    # Branch labels are immaterial; order their canonical roots.
    for branch in range(target - 1):
        solver.add(root_indices[branch] < root_indices[branch + 1])

    edge_indices = [(index[left], index[right]) for left, right in graph.edges()]
    for first, second in combinations(range(target), 2):
        solver.add(
            Or(
                *[
                    And(member[left][first], member[right][second])
                    for left, right in edge_indices
                ],
                *[
                    And(member[right][first], member[left][second])
                    for left, right in edge_indices
                ],
            )
        )

    result = solver.check()
    if result == sat:
        model = solver.model()
        branches = [
            {
                vertices[vertex]
                for vertex in range(order)
                if is_true(model.eval(member[vertex][branch]))
            }
            for branch in range(target)
        ]
        assert all(nx.is_connected(graph.subgraph(branch)) for branch in branches)
        assert all(
            any(graph.has_edge(left, right) for left in one for right in two)
            for one, two in combinations(branches, 2)
        )
        return True
    assert result == unsat, f"minor solver returned {result}"
    return False


def main() -> None:
    quotient = build_quotient()
    host = build_host()
    a, b, c, d, t = "A0", "A4", "p", "A1", "A2"
    triangle = {"r0", "r1", "r2"}

    assert quotient.number_of_nodes() == 15
    assert host.number_of_nodes() == 18
    assert nx.node_connectivity(host) == 5
    assert nx.node_connectivity(quotient) == 3
    three_cuts = {
        frozenset(cut)
        for cut in combinations(quotient, 3)
        if not nx.is_connected(quotient.subgraph(set(quotient) - set(cut)))
    }
    assert three_cuts == {frozenset({c, d, t})}

    quotient_components = list(nx.connected_components(quotient.subgraph(set(quotient) - {c, d, t})))
    assert len(quotient_components) == 2
    assert all(
        all(any(quotient.has_edge(vertex, terminal) for vertex in component) for terminal in (c, d, t))
        for component in quotient_components
    )

    # The large component is the side containing the original five-clique
    # roots a,b.  Even after restoring the two relevant boundary terminals,
    # it does not contain the disjoint (b-t,a-c) linkage used by the
    # label-preserving two-path completion.
    clique_side = next(component for component in quotient_components if a in component)
    assert b in clique_side
    clique_side_closure = quotient.subgraph(clique_side | {c, t}).copy()
    assert not has_linkage(clique_side_closure, (b, t), (a, c))

    assert has_linkage(quotient, (a, b), (c, d))
    assert has_linkage(quotient, (a, d), (b, c))
    assert not has_linkage(quotient, (a, c), (b, d))

    L = triangle | {a, b}
    Y = {c, t, "u", "v", "w"}
    assert L.isdisjoint(Y)
    assert is_clique(host, L)
    assert is_clique(host, Y)

    boundary = triangle | {c, d, t}
    components = list(nx.connected_components(host.subgraph(set(host) - boundary)))
    assert len(components) == 2
    assert all(
        all(any(host.has_edge(vertex, terminal) for vertex in component) for terminal in boundary)
        for component in components
    )

    colour_classes = {
        0: {"A0", "A4", "A2", "q"},
        1: {"A1", "B2", "p", "B4"},
        2: {"B0", "B3", "u"},
        3: {"B1", "A3", "v", "r0"},
        4: {"w", "r1"},
        5: {"r2"},
    }
    colour = {
        vertex: value
        for value, vertices in colour_classes.items()
        for vertex in vertices
    }
    assert set(colour) == set(host)
    deleted = host.copy()
    deleted.remove_edge(a, b)
    assert all(colour[left] != colour[right] for left, right in deleted.edges())
    assert colour[a] == colour[b] == 0
    assert {colour[vertex] for vertex in L} == {0, 3, 4, 5}

    expected_paths = {
        1: [a, "B4", b],
        2: [a, "B0", "q", "B3", b],
        3: [a, "r0", b],
        4: [a, "r1", b],
        5: [a, "r2", b],
    }
    for other_colour, path in expected_paths.items():
        assert all(deleted.has_edge(left, right) for left, right in zip(path, path[1:]))
        assert all(colour[vertex] in {0, other_colour} for vertex in path)
        bichromatic = deleted.subgraph(
            [vertex for vertex in deleted if colour[vertex] in {0, other_colour}]
        )
        assert nx.has_path(bichromatic, a, b)

    # A second colouring is a simultaneous-equality trace after deleting
    # g=A0A4 and h=uv.  The two cyclic orientations on the colours absent
    # from L-g give oppositely ordered replacement paths.
    double_deleted = host.copy()
    double_deleted.remove_edge(a, b)
    double_deleted.remove_edge("u", "v")
    cyclic_classes = {
        0: {"A0", "A4"},
        1: {"A1", "A3", "B4"},
        2: {"p", "B0", "B3"},
        3: {"q", "A2", "r0"},
        4: {"B1", "w", "r1"},
        5: {"B2", "u", "v", "r2"},
    }
    cyclic_colour = {
        vertex: value
        for value, vertices in cyclic_classes.items()
        for vertex in vertices
    }
    assert set(cyclic_colour) == set(host)
    assert all(
        cyclic_colour[left] != cyclic_colour[right]
        for left, right in double_deleted.edges()
    )
    assert cyclic_colour[a] == cyclic_colour[b] == 0
    assert cyclic_colour["u"] == cyclic_colour["v"] == 5
    assert {cyclic_colour[vertex] for vertex in triangle} == {3, 4, 5}

    successor = {0: 1, 1: 2, 2: 0}
    cyclic_orientation = nx.DiGraph()
    cyclic_orientation.add_nodes_from(
        vertex for vertex in double_deleted if cyclic_colour[vertex] in successor
    )
    cyclic_orientation.add_edges_from(
        (left, right)
        for edge in double_deleted.edges()
        for left, right in (edge, edge[::-1])
        if cyclic_colour.get(left) in successor
        and cyclic_colour.get(right) == successor[cyclic_colour[left]]
    )
    plus_path = [a, "B4", "B3", b]
    reverse_minus_path = [b, "B4", "B0", a]
    assert all(
        cyclic_orientation.has_edge(left, right)
        for left, right in zip(plus_path, plus_path[1:])
    )
    assert all(
        cyclic_orientation.has_edge(left, right)
        for left, right in zip(reverse_minus_path, reverse_minus_path[1:])
    )
    root_component = nx.node_connected_component(
        double_deleted.subgraph(cyclic_orientation.nodes), a
    )
    root_scc = next(
        component
        for component in nx.strongly_connected_components(cyclic_orientation)
        if a in component
    )
    assert root_scc == root_component
    assert root_scc == {
        "A0", "A4", "A1", "A3", "B0", "B3", "B4", "p"
    }

    # A third colouring has complementary natural supports for g and h.
    # It realizes the exact coupled-fork outcome: g is locked in both
    # cyclic orientations, while h is locked in one and unlocked in the
    # other.
    disjoint_classes = {
        0: {"A0", "A2", "A4"},
        1: {"A1", "B4", "p"},
        2: {"B0", "B3", "w"},
        3: {"A3", "B1", "r0"},
        4: {"B2", "r1"},
        5: {"q", "r2", "u", "v"},
    }
    disjoint_colour = {
        vertex: value
        for value, vertices in disjoint_classes.items()
        for vertex in vertices
    }
    assert set(disjoint_colour) == set(host)
    assert all(
        disjoint_colour[left] != disjoint_colour[right]
        for left, right in double_deleted.edges()
    )
    assert disjoint_colour[a] == disjoint_colour[b] == 0
    assert disjoint_colour["u"] == disjoint_colour["v"] == 5
    assert {disjoint_colour[vertex] for vertex in triangle} == {3, 4, 5}
    assert {
        disjoint_colour[vertex] for vertex in {"p", "A2", "w"}
    } == {0, 1, 2}

    def cyclic_digraph(cycle: tuple[int, int, int]) -> nx.DiGraph:
        advance = {cycle[index]: cycle[(index + 1) % 3] for index in range(3)}
        digraph = nx.DiGraph()
        digraph.add_nodes_from(
            vertex for vertex in double_deleted if disjoint_colour[vertex] in advance
        )
        digraph.add_edges_from(
            (left, right)
            for edge in double_deleted.edges()
            for left, right in (edge, edge[::-1])
            if disjoint_colour.get(left) in advance
            and disjoint_colour.get(right) == advance[disjoint_colour[left]]
        )
        return digraph

    coupled_paths = {
        (0, 1, 2): [a, "B4", "B3", b],
        (0, 2, 1): [a, "B0", "B4", b],
        (5, 3, 4): ["u", "r0", "r1", "v"],
    }
    for cycle, path in coupled_paths.items():
        digraph = cyclic_digraph(cycle)
        assert all(
            digraph.has_edge(left, right)
            for left, right in zip(path, path[1:])
        )
    reverse_h = cyclic_digraph((5, 4, 3))
    assert not nx.has_path(reverse_h, "u", "v")

    g_paths = [set(coupled_paths[(0, 1, 2)]), set(coupled_paths[(0, 2, 1)])]
    h_path = set(coupled_paths[(5, 3, 4)])
    assert all(path.isdisjoint(h_path) for path in g_paths)

    host_colouring = {
        "A1": 0,
        "A2": 1,
        "u": 2,
        "v": 3,
        "w": 4,
        "p": 0,
        "r0": 1,
        "r1": 2,
        "r2": 3,
        "A4": 4,
        "A0": 5,
        "A3": 2,
        "B0": 1,
        "B4": 0,
        "B3": 1,
        "q": 2,
        "B1": 3,
        "B2": 0,
    }
    assert set(host_colouring) == set(host)
    assert all(
        host_colouring[left] != host_colouring[right]
        for left, right in host.edges()
    )

    # Validate the exact minor encoding on positive and negative controls.
    assert has_k7_minor(nx.complete_graph(7))
    assert not has_k7_minor(host)

    print("quotient vertices: 15; unique three-cut: {p,A1,A2}")
    print("two missing-colour paths: A0-B4-A4 and A0-B0-q-B3-A4")
    print("all five alpha/beta Kempe components contain both ends of g")
    print("double-equality cyclic paths: A0-B4-B3-A4 and A0-B0-B4-A4")
    print("their root three-colour component is strongly connected")
    print("complementary palettes realize the coupled path/response outcome")
    print("target rooted linkage: absent")
    print("clique-side (A4-A2,A0-p) completion linkage: absent")
    print("K7 minor in the eighteen-vertex augmented quotient: absent")
    print("scope: five-connected, six-colourable quotient; not an HC7 counterexample")


if __name__ == "__main__":
    main()
