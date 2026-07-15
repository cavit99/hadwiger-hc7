#!/usr/bin/env python3
"""Falsify bundle-only RST feasibility in the atomic twin seam.

The certificate has exact connectivity seven, the literal twin boundary
maps, packet vector (1,1)/(1,1), crossed named edge responses, a common
equal/equal response, and the full separating five-rung bundle.  One of
the two Robertson--Seymour--Thomas (2.1) feasibility pairings nevertheless
fails in the reserve quotient.  The host is six-colourable, so this is a
mechanism barrier rather than an HC7 counterexample.
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
D = ("w2", "w3", "w4", "w6", "w7", "w9", "w10", "w11")
E = ("z", "e1", "y2", "y3", "y4", "y5")
I = ("i1", "i2", "i3")
A0 = ("a1", "a2")
B0 = ("u", "b")
S = I + A0 + B0
R = ("r1", "r2")
A = Z + D + E

EDGE_E = ("z", "u")
EDGE_F = ("q", "w2")
OMEGA_D = frozenset(Z + I + A0)
OMEGA_E = frozenset(Z + I + B0)


PHI = {
    "z": 0,
    "u": 0,
    "q": 0,
    "w2": 1,
    "i1": 2,
    "i2": 3,
    "w9": 4,
    "i3": 3,
    "w3": 5,
    "w7": 5,
    "p": 1,
    "y3": 4,
    "y2": 5,
    "y4": 5,
    "y5": 4,
    "b": 1,
    "e1": 5,
    "r1": 4,
    "r2": 5,
    "a1": 0,
    "w6": 4,
    "a2": 1,
    "w4": 0,
    "w10": 1,
    "w11": 4,
}

# The z-side swap in the 0--1 lock of PHI after EDGE_F is removed.
PSI = dict(PHI, z=1, q=1, p=0)

EQUAL_EQUAL = {
    "z": 0,
    "u": 0,
    "q": 0,
    "w2": 0,
    "i1": 1,
    "i2": 2,
    "p": 3,
    "y3": 4,
    "y2": 5,
    "i3": 2,
    "y4": 5,
    "y5": 4,
    "b": 2,
    "w7": 4,
    "w9": 3,
    "w3": 4,
    "w10": 0,
    "w11": 5,
    "w4": 3,
    "w6": 5,
    "a2": 2,
    "e1": 3,
    "a1": 1,
    "r1": 3,
    "r2": 4,
}

# This colouring deliberately witnesses the missing global hypothesis.
PROPER_PROPER = {
    "i1": 0,
    "i2": 1,
    "p": 2,
    "y3": 3,
    "y2": 4,
    "i3": 1,
    "y4": 4,
    "y5": 3,
    "b": 1,
    "q": 3,
    "w7": 4,
    "w9": 2,
    "w2": 4,
    "w3": 3,
    "w10": 5,
    "w11": 3,
    "w4": 2,
    "w6": 5,
    "a2": 1,
    "a1": 0,
    "z": 0,
    "e1": 2,
    "r1": 2,
    "r2": 3,
    "u": 4,
}


# A literal terminal certificate.  The shell is useful only as a
# localization falsifier: it is already killed by the K7 branch as well as
# by the displayed proper/proper colouring.
K7_MODEL = (
    frozenset(("b", "r2")),
    frozenset(("i2", "w10")),
    frozenset(("e1", "q", "w3", "w9", "y4", "z")),
    frozenset(("a1", "r1", "w4", "w6")),
    frozenset(("i3", "w2")),
    frozenset(("u",)),
    frozenset(("a2", "i1", "p", "w11", "w7", "y3")),
)


def build() -> nx.Graph:
    graph = nx.Graph()
    graph.add_nodes_from(A + S + R)

    # Start with the icosahedron.  For the edge 0--1 its two common
    # neighbours are 5 and 8.  Deleting 0--1, 8--1 and 0--5 exposes the
    # crossless frame p,q,a1,a2 in that cyclic order, while retaining the
    # two legal frame edges p--q and a1--a2.
    web = nx.icosahedral_graph()
    labels = {0: "p", 8: "q", 1: "a1", 5: "a2"}
    labels.update({vertex: f"w{vertex}" for vertex in web if vertex not in labels})
    web = nx.relabel_nodes(web, labels)
    web.remove_edges_from((("p", "a1"), ("q", "a1"), ("p", "a2")))
    assert set(web) == set(Z + D + A0)
    graph.add_edges_from(web.edges())

    # Every web vertex sees the three common old-boundary literals.  The
    # gates do too, but neither gate sees A0 or B0.
    graph.add_edges_from(itertools.product(D, I))
    graph.add_edges_from(itertools.product(Z, I))

    # The opposite lobe is the same six-vertex literal portal core used in
    # the stable-stem shell.
    graph.add_edges_from(
        (
            ("p", "z"),
            ("z", "e1"),
            ("q", "e1"),
            ("e1", "y3"),
            ("y2", "y3"),
            ("y3", "y4"),
            ("y4", "y5"),
            ("y5", "y2"),
        )
    )
    for index in range(2, 6):
        graph.add_edges_from((("z", f"y{index}"), (f"y{index}", "p")))
    for vertex in E[1:]:
        graph.add_edges_from((vertex, literal) for literal in I + ("b",))
    graph.add_edge(*EDGE_E)

    # Connected bipartite old boundary.  The final three edges are legal
    # additions across the same bipartition and are outside the reserve
    # quotient.
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
            ("a1", "a2"),
            ("a1", "i2"),
            ("a1", "i3"),
        )
    )

    graph.add_edge(*R)
    for packet in R:
        graph.add_edges_from((packet, literal) for literal in S)
    return graph


def external_neighbourhood(graph: nx.Graph, vertices) -> frozenset[str]:
    vertices = frozenset(vertices)
    return frozenset(
        neighbour
        for vertex in vertices
        for neighbour in graph[vertex]
        if neighbour not in vertices
    )


def proper_off(
    graph: nx.Graph,
    colouring: dict[str, int],
    omitted: tuple[tuple[str, str], ...] = (),
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


def full_packet_masks(
    graph: nx.Graph, shore: tuple[str, ...], boundary: frozenset[str]
) -> list[int]:
    masks: list[int] = []
    for mask in range(1, 1 << len(shore)):
        packet = {
            shore[index] for index in range(len(shore)) if (mask >> index) & 1
        }
        if not nx.is_connected(graph.subgraph(packet)):
            continue
        if all(
            any(graph.has_edge(vertex, literal) for vertex in packet)
            for literal in boundary
        ):
            masks.append(mask)
    return masks


def packet_number_one(
    graph: nx.Graph, shore: tuple[str, ...], boundary: frozenset[str]
) -> bool:
    masks = full_packet_masks(graph, shore, boundary)
    return bool(masks) and not any(
        left & right == 0
        for index, left in enumerate(masks)
        for right in masks[index + 1 :]
    )


def reserve_quotient(graph: nx.Graph) -> nx.Graph:
    quotient = graph.subgraph(D + A0 + R + Z).copy()
    for old, new in (({"a1", "r1"}, "c1"), ({"a2", "r2"}, "c2")):
        neighbours = set().union(*(set(quotient[vertex]) for vertex in old)) - old
        quotient.remove_nodes_from(old)
        quotient.add_node(new)
        quotient.add_edges_from((new, neighbour) for neighbour in neighbours)
    return quotient


def paired_feasible(
    graph: nx.Graph, first: tuple[str, str], second: tuple[str, str]
) -> bool:
    """Exact two-fragment feasibility by connected-set enumeration."""

    fixed = frozenset(first)
    forbidden = frozenset(second)
    free = tuple(set(graph) - fixed - forbidden)
    for mask in range(1 << len(free)):
        carrier = set(fixed)
        carrier.update(
            free[index] for index in range(len(free)) if (mask >> index) & 1
        )
        if not nx.is_connected(graph.subgraph(carrier)):
            continue
        remainder = graph.copy()
        remainder.remove_nodes_from(carrier)
        if nx.has_path(remainder, *second):
            return True
    return False


def literal_clique_model(
    graph: nx.Graph, bags: tuple[frozenset[str], ...]
) -> bool:
    return (
        all(bags)
        and len(set().union(*bags)) == sum(map(len, bags))
        and all(nx.is_connected(graph.subgraph(bag)) for bag in bags)
        and all(
            any(graph.has_edge(left, right) for left in bags[i] for right in bags[j])
            for i in range(len(bags))
            for j in range(i + 1, len(bags))
        )
    )


def verify() -> dict[int, list[str]]:
    graph = build()

    assert nx.node_connectivity(graph) == 7
    assert min(dict(graph.degree()).values()) == 7
    assert nx.is_biconnected(graph.subgraph(A))
    assert nx.is_connected(graph.subgraph(S))
    assert nx.is_bipartite(graph.subgraph(S))
    assert not any(graph.has_edge(a_vertex, rich) for a_vertex in A for rich in R)
    assert [vertex for vertex in A if graph.has_edge(vertex, "u")] == ["z"]
    assert external_neighbourhood(graph, D) == OMEGA_D
    assert external_neighbourhood(graph, E) == OMEGA_E
    assert (
        (set(graph["p"]) | set(graph["q"])) & set(S)
    ) <= set(I)
    assert graph.has_edge(*R)
    assert all(set(S) <= set(graph[packet]) for packet in R)

    b_d = E + B0 + R
    b_e = D + A0 + R
    assert packet_number_one(graph, D, OMEGA_D)
    assert packet_number_one(graph, b_d, OMEGA_D)
    assert packet_number_one(graph, E, OMEGA_E)
    assert packet_number_one(graph, b_e, OMEGA_E)

    quotient = reserve_quotient(graph)
    assert not paired_feasible(quotient, ("p", "c1"), ("q", "c2"))
    assert paired_feasible(quotient, ("q", "c1"), ("p", "c2"))

    # Jung's global linkages do exist, and even survive deletion of both
    # named edges, but they escape the reserve host through I.  Thus they
    # cannot be substituted for either local RST feasibility test.
    global_linkages = (
        (("p", "i2", "a1"), ("q", "i1", "a2")),
        (("q", "i2", "a1"), ("p", "i1", "a2")),
    )
    named_edges = {frozenset(EDGE_E), frozenset(EDGE_F)}
    reserve_host = set(D + A0 + R + Z)
    for first, second in global_linkages:
        assert set(first).isdisjoint(second)
        assert all(graph.has_edge(left, right) for left, right in zip(first, first[1:]))
        assert all(graph.has_edge(left, right) for left, right in zip(second, second[1:]))
        assert all(
            frozenset((left, right)) not in named_edges
            for path in (first, second)
            for left, right in zip(path, path[1:])
        )
        assert not set(first + second) <= reserve_host

    assert proper_off(graph, PHI, (EDGE_E,))
    assert PHI[EDGE_E[0]] == PHI[EDGE_E[1]] == 0
    assert PHI[EDGE_F[0]] != PHI[EDGE_F[1]]

    edge_deleted = graph.copy()
    edge_deleted.remove_edge(*EDGE_E)
    lock = edge_deleted.subgraph(
        vertex for vertex in edge_deleted if PHI[vertex] in (0, 1)
    ).copy()
    assert nx.has_path(lock, *EDGE_E)
    assert lock.has_edge(*EDGE_F)
    lock.remove_edge(*EDGE_F)
    assert not nx.has_path(lock, *EDGE_E)
    swapped_side = nx.node_connected_component(lock, "z")
    swapped = dict(PHI)
    for vertex in swapped_side:
        swapped[vertex] = 1 - swapped[vertex]
    assert swapped == PSI

    assert proper_off(graph, PSI, (EDGE_F,))
    assert PSI[EDGE_F[0]] == PSI[EDGE_F[1]] == 1
    assert exact_partition(PHI, OMEGA_D) != exact_partition(PSI, OMEGA_D)
    assert exact_partition(PHI, OMEGA_E) != exact_partition(PSI, OMEGA_E)

    response_host = graph.copy()
    response_host.remove_edge(*EDGE_F)
    response_paths: dict[int, list[str]] = {}
    for alternate in (2, 3, 4, 5):
        layer = response_host.subgraph(
            vertex for vertex in response_host if PSI[vertex] in (1, alternate)
        )
        assert nx.has_path(layer, *EDGE_F)
        response_paths[alternate] = nx.shortest_path(layer, *EDGE_F)

    complementary_path = ("q", "p", "z", "u", "a2", "a1", "w2")
    assert all(
        graph.has_edge(left, right)
        for left, right in zip(complementary_path, complementary_path[1:])
    )
    assert set(PSI[vertex] for vertex in complementary_path) == {0, 1}
    assert EDGE_E[0] in complementary_path and EDGE_E[1] in complementary_path

    common_host = graph.copy()
    common_host.remove_edge(*EDGE_E)
    common_host.remove_edge(*EDGE_F)
    assert proper_off(common_host, EQUAL_EQUAL)
    assert EQUAL_EQUAL[EDGE_E[0]] == EQUAL_EQUAL[EDGE_E[1]]
    assert EQUAL_EQUAL[EDGE_F[0]] == EQUAL_EQUAL[EDGE_F[1]]

    assert proper_off(graph, PROPER_PROPER)
    assert literal_clique_model(graph, K7_MODEL)
    return response_paths


def main() -> None:
    paths = verify()
    print("GREEN twin_seam_rst_feasibility_falsifier")
    print("order=25 connectivity=7 packet_vector=(1,1)/(1,1)")
    print("pairing_p_c1_q_c2=false pairing_q_c1_p_c2=true")
    print("response_paths", paths)
    print("global_pairings=true local_first_pairing=false")
    print("equal_equal=true proper_proper=true literal_K7=true")


if __name__ == "__main__":
    main()
