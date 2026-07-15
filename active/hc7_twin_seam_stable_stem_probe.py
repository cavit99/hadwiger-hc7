#!/usr/bin/env python3
"""Verify the exact-seven stable-stem barrier in two response modes.

This is a mechanism falsifier, not an HC7 counterexample.  Both variants
have the literal residual twin seam, exact connectivity seven, an equal/equal
common-host colouring, and no matched pair of Z-full lobe carriers.  The
base variant realizes the full separating response bundle.  Adding the
single allowed gate--I edge q-i2 turns the same named lock into a
response-matched bypass.  Both hosts are six-colourable and contain the
displayed K7 minor.
"""

from __future__ import annotations

import itertools
from pathlib import Path
import sys


DEPS = Path(__file__).resolve().parent / "runtime" / "deps"
if DEPS.exists():
    sys.path.insert(0, str(DEPS))

import networkx as nx


Z = ("p", "q")
D = ("d", "d1", "x2", "x3", "x4", "x5")
E = ("z", "e1", "y2", "y3", "y4", "y5")
I = ("i1", "i2", "i3")
A0 = ("a1", "a2")
B0 = ("u", "b")
S = I + A0 + B0
R = ("r1", "r2")
A = Z + D + E

EDGE_E = ("z", "u")
EDGE_F = ("q", "d")
OMEGA_D = frozenset(Z + I + A0)
OMEGA_E = frozenset(Z + I + B0)


PHI = {
    "z": 0,
    "u": 0,
    "p": 1,
    "q": 0,
    "d": 1,
    "d1": 2,
    "e1": 2,
    "x2": 2,
    "x3": 3,
    "x4": 4,
    "x5": 5,
    "y2": 2,
    "y3": 3,
    "y4": 4,
    "y5": 5,
    "i1": 0,
    "i2": 1,
    "i3": 1,
    "a1": 0,
    "a2": 1,
    "b": 1,
    "r1": 2,
    "r2": 3,
}

# The bridge-side swap on the z,p,q side of the 0--1 lock.
SEPARATING_RESPONSE = dict(PHI, z=1, p=0, q=1)

# A G/f response for the one-edge bypass variant.  Its z colour is already
# aligned with PHI(z), while u has colour one, so it selects the displayed
# 0--1 e-lock exactly.
BYPASS_RESPONSE = {
    "p": 2,
    "q": 0,
    "d": 0,
    "d1": 5,
    "x2": 1,
    "x3": 5,
    "x4": 1,
    "x5": 1,
    "z": 0,
    "e1": 5,
    "y2": 5,
    "y3": 1,
    "y4": 5,
    "y5": 1,
    "i1": 2,
    "i2": 3,
    "i3": 3,
    "a1": 3,
    "a2": 4,
    "u": 1,
    "b": 4,
    "r1": 0,
    "r2": 5,
}

EE_SEPARATING = {
    "p": 3,
    "q": 5,
    "d": 5,
    "d1": 2,
    "x2": 4,
    "x3": 2,
    "x4": 2,
    "x5": 4,
    "z": 2,
    "e1": 4,
    "y2": 4,
    "y3": 5,
    "y4": 4,
    "y5": 5,
    "i1": 0,
    "i2": 1,
    "i3": 1,
    "a1": 1,
    "a2": 1,
    "u": 2,
    "b": 3,
    "r1": 4,
    "r2": 5,
}

EE_BYPASS = {
    "p": 3,
    "q": 4,
    "d": 4,
    "d1": 5,
    "x2": 3,
    "x3": 2,
    "x4": 2,
    "x5": 5,
    "z": 2,
    "e1": 5,
    "y2": 5,
    "y3": 4,
    "y4": 5,
    "y5": 4,
    "i1": 0,
    "i2": 1,
    "i3": 1,
    "a1": 1,
    "a2": 1,
    "u": 2,
    "b": 3,
    "r1": 4,
    "r2": 5,
}

PP_SEPARATING = {
    "p": 3,
    "q": 5,
    "d": 3,
    "d1": 4,
    "x2": 4,
    "x3": 4,
    "x4": 1,
    "x5": 1,
    "z": 0,
    "e1": 1,
    "y2": 1,
    "y3": 4,
    "y4": 1,
    "y5": 4,
    "i1": 2,
    "i2": 5,
    "i3": 5,
    "a1": 5,
    "a2": 0,
    "u": 2,
    "b": 3,
    "r1": 4,
    "r2": 1,
}

PP_BYPASS = {
    "p": 0,
    "q": 2,
    "d": 3,
    "d1": 4,
    "x2": 4,
    "x3": 4,
    "x4": 4,
    "x5": 4,
    "z": 3,
    "e1": 1,
    "y2": 1,
    "y3": 4,
    "y4": 1,
    "y5": 4,
    "i1": 2,
    "i2": 5,
    "i3": 5,
    "a1": 5,
    "a2": 0,
    "u": 2,
    "b": 3,
    "r1": 4,
    "r2": 1,
}

K7_MODEL = (
    frozenset(("d", "i1", "r1", "x4")),
    frozenset(("u",)),
    frozenset(("e1", "i2")),
    frozenset(("b",)),
    frozenset(("d1", "i3", "y2", "y5")),
    frozenset(("a1", "r2", "x3")),
    frozenset(("a2", "p", "q", "x2", "x5", "y3", "y4", "z")),
)


def build(*, bypass: bool) -> nx.Graph:
    graph = nx.Graph()
    graph.add_nodes_from(A + S + R)

    # Crossed stable stems: p has the unique D-portal d1, while q has the
    # unique E-portal e1.  The other gate has four response-rung portals.
    graph.add_edges_from(
        (
            ("p", "q"),
            ("p", "z"),
            ("z", "e1"),
            ("q", "e1"),
            ("d", "d1"),
            ("p", "d1"),
            EDGE_F,
        )
    )
    for index in range(2, 6):
        graph.add_edges_from(
            (
                ("d", f"x{index}"),
                (f"x{index}", "q"),
                ("z", f"y{index}"),
                (f"y{index}", "p"),
            )
        )
    graph.add_edges_from(
        (
            ("e1", "y3"),
            ("y2", "y3"),
            ("y3", "y4"),
            ("y4", "y5"),
            ("y5", "y2"),
        )
    )

    for vertex in ("d1", "x2", "x3", "x4", "x5"):
        graph.add_edges_from((vertex, literal) for literal in I + A0)
    graph.add_edges_from(("d", literal) for literal in ("i1", "a1"))

    graph.add_edge(*EDGE_E)
    for vertex in ("e1", "y2", "y3", "y4", "y5"):
        graph.add_edges_from((vertex, literal) for literal in I + ("b",))

    graph.add_edges_from(
        (
            ("a1", "b"),
            ("b", "u"),
            ("b", "i1"),
            ("i1", "a2"),
            ("i1", "i2"),
            ("i1", "i3"),
            ("u", "i2"),
            ("u", "i3"),
            ("u", "a2"),
        )
    )
    graph.add_edge("r1", "r2")
    for packet in R:
        graph.add_edges_from((packet, literal) for literal in S)

    if bypass:
        graph.add_edge("q", "i2")
    return graph


def proper_off(
    graph: nx.Graph, colouring: dict[str, int], omitted: tuple[tuple[str, str], ...]
) -> bool:
    missing = {frozenset(edge) for edge in omitted}
    return all(
        frozenset((left, right)) in missing
        or colouring[left] != colouring[right]
        for left, right in graph.edges()
    )


def exact_partition(
    colouring: dict[str, int], boundary: frozenset[str]
) -> tuple[tuple[str, ...], ...]:
    blocks: dict[int, list[str]] = {}
    for vertex in boundary:
        blocks.setdefault(colouring[vertex], []).append(vertex)
    return tuple(sorted(tuple(sorted(block)) for block in blocks.values()))


def external_neighbourhood(graph: nx.Graph, vertices) -> frozenset[str]:
    vertices = frozenset(vertices)
    return frozenset(
        neighbour
        for vertex in vertices
        for neighbour in graph[vertex]
        if neighbour not in vertices
    )


def connected_full_packets(graph: nx.Graph, shore, boundary) -> list[frozenset[str]]:
    vertices = tuple(shore)
    packets: list[frozenset[str]] = []
    for mask in range(1, 1 << len(vertices)):
        packet = frozenset(
            vertices[index]
            for index in range(len(vertices))
            if (mask >> index) & 1
        )
        if not nx.is_connected(graph.subgraph(packet)):
            continue
        if all(
            any(graph.has_edge(vertex, literal) for vertex in packet)
            for literal in boundary
        ):
            packets.append(packet)
    return packets


def packet_number(packets: list[frozenset[str]]) -> int:
    for order in range(3, 0, -1):
        if any(
            all(
                family[left].isdisjoint(family[right])
                for left in range(order)
                for right in range(left)
            )
            for family in itertools.combinations(packets, order)
        ):
            return order
    return 0


def matched_gate_carriers(graph: nx.Graph, lobe, seeds) -> list[tuple]:
    lobe = tuple(lobe)
    candidates: list[tuple[str, frozenset[str]]] = []
    for seed in seeds:
        allowed = lobe + (seed,)
        for mask in range(1, 1 << len(allowed)):
            carrier = frozenset(
                allowed[index]
                for index in range(len(allowed))
                if (mask >> index) & 1
            )
            if seed not in carrier or not nx.is_connected(graph.subgraph(carrier)):
                continue
            if all(
                any(graph.has_edge(vertex, gate) for vertex in carrier)
                for gate in Z
            ):
                candidates.append((seed, carrier))
    return [
        (left, right)
        for left, right in itertools.combinations(candidates, 2)
        if left[0] != right[0] and left[1].isdisjoint(right[1])
    ]


def check_clique_model(graph: nx.Graph, model) -> bool:
    if any(not bag for bag in model):
        return False
    if any(
        model[left] & model[right]
        for left in range(len(model))
        for right in range(left)
    ):
        return False
    if any(not nx.is_connected(graph.subgraph(bag)) for bag in model):
        return False
    return all(
        any(graph.has_edge(x, y) for x in model[left] for y in model[right])
        for left in range(len(model))
        for right in range(left)
    )


def verify(*, bypass: bool) -> tuple[int, int, int, int]:
    graph = build(bypass=bypass)
    response = BYPASS_RESPONSE if bypass else SEPARATING_RESPONSE
    equal_equal = EE_BYPASS if bypass else EE_SEPARATING
    proper_proper = PP_BYPASS if bypass else PP_SEPARATING

    assert nx.is_biconnected(graph.subgraph(A))
    assert nx.is_connected(graph.subgraph(S))
    assert nx.is_bipartite(graph.subgraph(S))
    assert not any(graph.has_edge(a_vertex, rich) for a_vertex in A for rich in R)
    assert [vertex for vertex in A if graph.has_edge(vertex, "u")] == ["z"]
    assert external_neighbourhood(graph, D) == OMEGA_D
    assert external_neighbourhood(graph, E) == OMEGA_E
    assert set(graph.neighbors("p")) & set(D) == {"d1"}
    assert set(graph.neighbors("q")) & set(E) == {"e1"}
    assert (set(graph.neighbors("p")) | set(graph.neighbors("q"))) & set(S) <= set(I)
    assert all(set(S) <= set(graph.neighbors(packet)) for packet in R)
    assert graph.has_edge(*R)

    assert nx.node_connectivity(graph) == 7
    assert min(dict(graph.degree()).values()) == 7

    assert proper_off(graph, PHI, (EDGE_E,))
    assert PHI[EDGE_E[0]] == PHI[EDGE_E[1]]
    assert proper_off(graph, response, (EDGE_F,))
    assert response[EDGE_F[0]] == response[EDGE_F[1]]
    assert response[EDGE_E[0]] != response[EDGE_E[1]]
    assert exact_partition(PHI, OMEGA_D) != exact_partition(response, OMEGA_D)
    assert exact_partition(PHI, OMEGA_E) != exact_partition(response, OMEGA_E)

    common_host = graph.copy()
    common_host.remove_edge(*EDGE_E)
    common_host.remove_edge(*EDGE_F)
    assert proper_off(common_host, equal_equal, ())
    assert equal_equal[EDGE_E[0]] == equal_equal[EDGE_E[1]]
    assert equal_equal[EDGE_F[0]] == equal_equal[EDGE_F[1]]
    assert proper_off(graph, proper_proper, ())

    lock_host = graph.copy()
    lock_host.remove_edge(*EDGE_E)
    lock_vertices = [vertex for vertex in lock_host if PHI[vertex] in (0, 1)]
    lock = lock_host.subgraph(lock_vertices).copy()
    assert nx.has_path(lock, *EDGE_E)
    assert lock.has_edge(*EDGE_F)
    lock.remove_edge(*EDGE_F)
    if bypass:
        assert response["z"] == PHI["z"]
        assert response["u"] == 1
        assert nx.has_path(lock, *EDGE_E)
        assert nx.shortest_path(lock, *EDGE_E) == ["z", "p", "q", "i2", "u"]
    else:
        assert not nx.has_path(lock, *EDGE_E)
        changed = {vertex for vertex in graph if PHI[vertex] != response[vertex]}
        assert changed == {"z", "p", "q"}
        for index in range(2, 6):
            path = ("d", f"x{index}", "q")
            assert all(graph.has_edge(x, y) for x, y in zip(path, path[1:]))
            assert {response[vertex] for vertex in path} == {1, index}
        through_e = ("d", "a1", "b", "u", "z", "p", "q")
        assert all(graph.has_edge(x, y) for x, y in zip(through_e, through_e[1:]))
        assert EDGE_E[0] in through_e and EDGE_E[1] in through_e
        assert {response[vertex] for vertex in through_e} == {0, 1}

    b_d = set(E + B0 + R)
    b_e = set(D + A0 + R)
    packet_lists = (
        connected_full_packets(graph, D, OMEGA_D),
        connected_full_packets(graph, b_d, OMEGA_D),
        connected_full_packets(graph, E, OMEGA_E),
        connected_full_packets(graph, b_e, OMEGA_E),
    )
    vector = tuple(packet_number(packets) for packets in packet_lists)
    assert vector == (1, 1, 1, 1)

    assert not matched_gate_carriers(graph, D, A0)
    assert not matched_gate_carriers(graph, E, B0)
    assert check_clique_model(graph, K7_MODEL)
    return vector


def main() -> None:
    separating_vector = verify(bypass=False)
    bypass_vector = verify(bypass=True)
    print("GREEN twin_seam_stable_stem")
    print("separating_packet_numbers", separating_vector)
    print("bypass_packet_numbers", bypass_vector)
    print("orders", build(bypass=False).number_of_nodes(), build(bypass=False).number_of_edges())
    print("connectivity 7; matched_carriers_D=0; matched_carriers_E=0")
    print("six_colourable=true; explicit_K7_model=true")


if __name__ == "__main__":
    main()
