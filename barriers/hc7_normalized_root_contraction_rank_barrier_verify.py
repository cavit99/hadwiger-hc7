#!/usr/bin/env python3
"""Verify the normalized root-contraction rank barrier."""

from __future__ import annotations

import networkx as nx


H_VERTICES = ("a", "b", "t", "x", "s")
CYCLE = tuple(f"c{i}" for i in range(6))


def adjacent_sets(graph: nx.Graph, left: set[str], right: set[str]) -> bool:
    return any(graph.has_edge(u, v) for u in left for v in right)


def is_model(
    graph: nx.Graph,
    bags: list[set[str]],
    missing: set[tuple[int, int]],
    *,
    spanning: bool = True,
) -> bool:
    used = set().union(*bags)
    if not used <= set(graph):
        return False
    if spanning and used != set(graph):
        return False
    if sum(map(len, bags)) != len(used):
        return False
    if any(not nx.is_connected(graph.subgraph(bag)) for bag in bags):
        return False
    for i in range(len(bags)):
        for j in range(i + 1, len(bags)):
            if (i, j) not in missing and not adjacent_sets(graph, bags[i], bags[j]):
                return False
    return True


def build_graph() -> nx.Graph:
    graph = nx.Graph()
    graph.add_nodes_from(H_VERTICES + CYCLE)
    missing_edges = {frozenset(("a", "b")), frozenset(("t", "x"))}
    for i, u in enumerate(H_VERTICES):
        for v in H_VERTICES[i + 1 :]:
            if frozenset((u, v)) not in missing_edges:
                graph.add_edge(u, v)
    graph.add_edges_from((CYCLE[i], CYCLE[(i + 1) % 6]) for i in range(6))
    graph.add_edges_from((u, v) for u in H_VERTICES for v in CYCLE)
    return graph


def main() -> None:
    graph = build_graph()
    assert nx.node_connectivity(graph) == 7

    near_bags = [
        {"a"},
        {"b"},
        {"t"},
        {"s", "x"},
        {"c0", "c1", "c2", "c3"},
        {"c4"},
        {"c5"},
    ]
    assert is_model(graph, near_bags, {(0, 1)})
    assert not adjacent_sets(graph, near_bags[0], near_bags[1])
    assert nx.shortest_path_length(graph, "a", "b") == 2
    assert all(graph.has_edge(u, v) for u, v in zip(("a", "x"), ("x", "b")))

    j_graph = graph.subgraph(set(graph) - {"a", "b"}).copy()
    model = [{"t"}, {"s"}, {"c0", "c1", "c2", "c3"}, {"c4"}, {"c5"}]
    assert is_model(j_graph, model, set(), spanning=False)
    for i, earlier in enumerate(model):
        for later in model[i + 1 :]:
            assert all(
                any(j_graph.has_edge(v, u) for u in earlier) for v in later
            )

    terminal_cycle = set(CYCLE)
    actual_cycle_edges = {
        frozenset(edge) for edge in j_graph.subgraph(terminal_cycle).edges()
    }
    expected_cycle_edges = {
        frozenset((CYCLE[i], CYCLE[(i + 1) % 6])) for i in range(6)
    }
    assert actual_cycle_edges == expected_cycle_edges
    separator = {"s", *CYCLE}
    components = [
        set(component)
        for component in nx.connected_components(
            j_graph.subgraph(set(j_graph) - separator)
        )
    ]
    assert {frozenset(component) for component in components} == {
        frozenset({"t"}),
        frozenset({"x"}),
    }
    e_side = {"t"}
    x_side = {"x"}
    roots_at_e = {
        root for root in ("a", "b") if adjacent_sets(graph, {root}, e_side)
    }
    assert (len(separator) + len(roots_at_e), len(e_side), len(x_side)) == (
        9,
        1,
        1,
    )

    contracted = nx.contracted_nodes(graph, "a", "t", self_loops=False)
    assert "t" not in contracted
    assert contracted.has_edge("a", "b")
    contraction_colouring = {
        "a": 0,
        "b": 1,
        "x": 2,
        "s": 3,
        "c0": 4,
        "c1": 5,
        "c2": 4,
        "c3": 5,
        "c4": 4,
        "c5": 5,
    }
    assert all(
        contraction_colouring[u] != contraction_colouring[v]
        for u, v in contracted.edges()
    )
    assert len(set(contraction_colouring.values())) == 6
    expanded = {**contraction_colouring, "t": contraction_colouring["a"]}
    assert all(
        expanded[u] != expanded[v]
        for u, v in graph.edges()
        if frozenset((u, v)) != frozenset(("a", "t"))
    )
    assert expanded["a"] == expanded["t"]

    colouring = {
        "a": 0,
        "b": 0,
        "t": 1,
        "x": 1,
        "s": 2,
        "c0": 3,
        "c1": 4,
        "c2": 3,
        "c3": 4,
        "c4": 3,
        "c5": 4,
    }
    assert all(colouring[u] != colouring[v] for u, v in graph.edges())
    assert len(set(colouring.values())) == 5

    k7_bags = [
        {"a", "t"},
        {"b"},
        {"x"},
        {"s"},
        {"c0", "c1"},
        {"c2", "c3"},
        {"c4", "c5"},
    ]
    assert is_model(graph, k7_bags, set())
    print("node_connectivity=7")
    print("normalized_signature=(9,1,1)")
    print("contracted_roots_adjacent=true")
    print("contracted_minor_colours=6")
    print("host_five_colouring=true")
    print("explicit_K7_model=true")
    print("GREEN: normalized root-contraction rank barrier verified")


if __name__ == "__main__":
    main()
