#!/usr/bin/env python3
"""Verify the contact-span and opposite-state counterexamples."""

from __future__ import annotations

from itertools import combinations

import networkx as nx


def span_host() -> nx.Graph:
    graph = nx.Graph()
    left = (0, 1, 2, 3)
    right = (0, 2, 1, 3)
    for order, prefix in ((left, "l"), (right, "r")):
        graph.add_edges_from(
            (f"{prefix}{order[i]}", f"{prefix}{order[(i + 1) % 4]}")
            for i in range(4)
        )
    graph.add_edges_from((f"l{i}", f"r{i}") for i in range(4))
    rows = ("f0", "f1", "f2")
    graph.add_edges_from(combinations(rows, 2))
    contacts = {
        "f0": ("l0", "r1", "l2"),
        "f1": ("l0", "r1", "r2"),
        "f2": ("r0", "r1", "l2"),
    }
    for row, anchors in contacts.items():
        graph.add_edges_from((row, anchor) for anchor in anchors)
    return graph


def fill_degrees(graph: nx.Graph, order: tuple[str, ...]) -> list[int]:
    work = graph.copy()
    degrees = []
    for vertex in order:
        neighbours = list(work[vertex])
        degrees.append(len(neighbours))
        work.add_edges_from(combinations(neighbours, 2))
        work.remove_node(vertex)
    assert not work
    return degrees


def cyclic_subpaths(order: tuple[str, ...], root: str) -> set[frozenset[str]]:
    values: set[frozenset[str]] = set()
    n = len(order)
    for start in range(n):
        for length in range(1, n + 1):
            path = frozenset(order[(start + step) % n] for step in range(length))
            if root in path:
                values.add(path)
    return values


def complete_sectors(graph: nx.Graph) -> list[tuple[int, frozenset[str]]]:
    left = ("l0", "l1", "l2", "l3")
    right = ("r0", "r2", "r1", "r3")
    values: set[tuple[int, frozenset[str]]] = set()
    for port in range(4):
        for a_path in cyclic_subpaths(left, f"l{port}"):
            for b_path in cyclic_subpaths(right, f"r{port}"):
                sector = a_path | b_path
                if all(
                    any(graph.has_edge(vertex, row) for vertex in sector)
                    for row in ("f0", "f1", "f2")
                ):
                    values.add((port, sector))
    return list(values)


def maximum_disjoint_sector_count(
    sectors: list[tuple[int, frozenset[str]]]
) -> int:
    best = 0

    def search(position: int, chosen: list[frozenset[str]]) -> None:
        nonlocal best
        best = max(best, len(chosen))
        for index in range(position, len(sectors)):
            sector = sectors[index][1]
            if all(not sector & old for old in chosen):
                search(index + 1, [*chosen, sector])

    search(0, [])
    return best


def colour(graph: nx.Graph, k: int) -> dict[str, int] | None:
    assigned: dict[str, int] = {}

    def search() -> dict[str, int] | None:
        if len(assigned) == len(graph):
            return assigned.copy()
        vertex = max(
            (v for v in graph if v not in assigned),
            key=lambda v: (
                len({assigned[w] for w in graph[v] if w in assigned}),
                graph.degree(v),
                str(v),
            ),
        )
        forbidden = {assigned[w] for w in graph[vertex] if w in assigned}
        for value in range(k):
            if value in forbidden:
                continue
            assigned[vertex] = value
            answer = search()
            if answer is not None:
                return answer
            del assigned[vertex]
        return None

    return search()


def state_host() -> tuple[nx.Graph, nx.Graph, nx.Graph]:
    equality = nx.Graph()
    c_core = tuple(f"c{i}" for i in range(5))
    equality.add_edges_from(combinations(c_core, 2))
    for root in ("s", "t"):
        equality.add_edges_from((root, vertex) for vertex in c_core)

    inequality = nx.Graph()
    d_core = tuple(f"d{i}" for i in range(6))
    inequality.add_edges_from(combinations(d_core, 2))
    inequality.add_edges_from(("t", f"d{i}") for i in (0, 2, 3, 4, 5))
    inequality.add_edge("s", "d1")

    graph = nx.compose(equality, inequality)
    return graph, equality, inequality


def boundary_states(graph: nx.Graph) -> set[bool]:
    """Return whether s=t in every canonical six-colouring found."""
    states: set[bool] = set()
    assigned: dict[str, int] = {}

    def search() -> None:
        if len(assigned) == len(graph):
            states.add(assigned["s"] == assigned["t"])
            return
        vertex = max(
            (v for v in graph if v not in assigned),
            key=lambda v: (
                len({assigned[w] for w in graph[v] if w in assigned}),
                graph.degree(v),
                str(v),
            ),
        )
        forbidden = {assigned[w] for w in graph[vertex] if w in assigned}
        for value in range(6):
            if value in forbidden:
                continue
            assigned[vertex] = value
            search()
            del assigned[vertex]

    search()
    return states


def main() -> None:
    circular = span_host()
    assert (len(circular), circular.number_of_edges()) == (11, 24)
    assert nx.node_connectivity(circular) == 3
    assert nx.to_graph6_bytes(
        nx.convert_node_labels_to_integers(circular), header=False
    ).strip() == b"Jl_iGua`hT_"

    anchors = {"l0", "l2", "r1"}
    tiny_sectors = [{f"l{i}", f"r{i}"} for i in range(3)]
    assert all(
        nx.is_connected(circular.subgraph(sector)) for sector in tiny_sectors
    )
    assert all(
        any(circular.has_edge(vertex, row) for vertex in sector)
        for sector in tiny_sectors
        for row in ("f0", "f1", "f2")
    )
    assert all(
        not tiny_sectors[i] & tiny_sectors[j]
        for i in range(3)
        for j in range(i)
    )
    assert len(anchors) == 3

    sectors = complete_sectors(circular)
    assert len(sectors) == 187
    assert maximum_disjoint_sector_count(sectors) == 3
    cycle_vertices = tuple(f"{prefix}{i}" for prefix in "lr" for i in range(4))
    transversal_number = next(
        size
        for size in range(9)
        if any(
            all(set(candidate) & sector for _, sector in sectors)
            for candidate in combinations(cycle_vertices, size)
        )
    )
    assert transversal_number == 3
    assert all(anchors & sector for _, sector in sectors)
    after_anchors = circular.copy()
    after_anchors.remove_nodes_from(anchors)
    assert sorted(
        sorted(component) for component in nx.connected_components(after_anchors)
    ) == [
        ["f0", "f1", "f2", "l3", "r0", "r2", "r3"],
        ["l1"],
    ]

    elimination = (
        "l1",
        "l3",
        "r0",
        "f0",
        "f1",
        "f2",
        "l0",
        "l2",
        "r1",
        "r2",
        "r3",
    )
    degrees = fill_degrees(circular, elimination)
    assert degrees == [3, 3, 4, 5, 5, 5, 4, 3, 2, 1, 0]
    assert max(degrees) == 5

    near_k7_bags = [
        {"f0"},
        {"f1"},
        {"r1"},
        {"r0", "f2"},
        {"l0", "l1"},
        {"l2", "r2"},
        {"l3", "r3"},
    ]
    assert all(nx.is_connected(circular.subgraph(bag)) for bag in near_k7_bags)
    assert all(
        not near_k7_bags[i] & near_k7_bags[j]
        for i in range(7)
        for j in range(i)
    )
    missing_pairs = [
        (i, j)
        for i in range(7)
        for j in range(i)
        if not any(
            circular.has_edge(u, v)
            for u in near_k7_bags[i]
            for v in near_k7_bags[j]
        )
    ]
    assert missing_pairs == [(6, 0), (6, 1)]

    critical, equality, inequality = state_host()
    assert (len(critical), critical.number_of_edges()) == (13, 41)
    assert nx.node_connectivity(critical) == 2
    assert nx.to_graph6_bytes(
        nx.convert_node_labels_to_integers(critical), header=False
    ).strip() == b"L~~~oCD?wF_^?~"
    assert boundary_states(equality) == {True}
    assert boundary_states(inequality) == {False}
    assert colour(critical, 6) is None
    assert colour(critical, 7) is not None

    assert all(
        colour(critical.subgraph(set(critical) - {vertex}).copy(), 6)
        is not None
        for vertex in critical
    )
    for edge in list(critical.edges):
        deletion = critical.copy()
        deletion.remove_edge(*edge)
        assert colour(deletion, 6) is not None, ("deletion", edge)
        contraction = nx.contracted_edge(critical, edge, self_loops=False)
        assert colour(contraction, 6) is not None, ("contraction", edge)

    k7_bags = [
        {"c0"},
        {"c1"},
        {"c2"},
        {"c3"},
        {"c4"},
        {"t"},
        {"s", "d1", "d0"},
    ]
    assert all(nx.is_connected(critical.subgraph(bag)) for bag in k7_bags)
    assert all(
        not k7_bags[i] & k7_bags[j]
        for i in range(7)
        for j in range(i)
    )
    assert all(
        any(critical.has_edge(u, v) for u in k7_bags[i] for v in k7_bags[j])
        for i in range(7)
        for j in range(i)
    )

    print("GREEN: contact-span packing barrier verified")
    print("span host: n=11, kappa=3, treewidth <=5")
    print("187 complete sectors: packing number = transversal number = 3")
    print("the three anchors form an actual cut, and K7^vee is explicit")
    print("state host: n=13, kappa=2, all single operations six-colourable")
    print("explicit K7 model proves it is not contraction-critical")
    print("opposite boundary states: equality versus inequality")


if __name__ == "__main__":
    main()
