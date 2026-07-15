"""Verify the reduced near-K7 rotation triangle.

Run from the repository root with:
  PYTHONPATH=active/runtime/deps python3 \
      barriers/hc7_global_invariant_rotation_triangle_verify.py
"""

from __future__ import annotations

import networkx as nx


Vertex = object


def pentagonal_tube(length: int) -> nx.Graph:
    """Return T_length; T_1 is the icosahedron."""
    assert length >= 1
    graph = nx.Graph()
    graph.add_nodes_from(("T", "B"))
    for layer in range(length + 1):
        for index in range(5):
            graph.add_edge((layer, index), (layer, (index + 1) % 5))
    for index in range(5):
        graph.add_edge("T", (0, index))
        graph.add_edge("B", (length, index))
    for layer in range(length):
        for index in range(5):
            graph.add_edge((layer, index), (layer + 1, index))
            graph.add_edge((layer, index), (layer + 1, (index - 1) % 5))
    return graph


def two_apex_host(length: int) -> tuple[nx.Graph, nx.Graph]:
    core = pentagonal_tube(length)
    host = core.copy()
    host.add_edge("p", "q")
    for apex in ("p", "q"):
        host.add_edges_from((apex, vertex) for vertex in core)
    return core, host


def has_edge_between(graph: nx.Graph, first: set[Vertex], second: set[Vertex]) -> bool:
    return any(graph.has_edge(x, y) for x in first for y in second)


def connected(graph: nx.Graph, vertices: set[Vertex]) -> bool:
    return bool(vertices) and nx.is_connected(graph.subgraph(vertices))


def missing_rows(
    graph: nx.Graph, centre: set[Vertex], rows: list[set[Vertex]]
) -> tuple[int, ...]:
    return tuple(
        index for index, row in enumerate(rows) if not has_edge_between(graph, centre, row)
    )


def check_state(
    graph: nx.Graph,
    centre: set[Vertex],
    active: set[Vertex],
    frame: list[set[Vertex]],
    expected_missing: int,
) -> None:
    bags = [centre, active, *frame]
    assert all(connected(graph, bag) for bag in bags)
    assert sum(map(len, bags)) == len(set().union(*bags))
    rows = [active, *frame]
    for first in range(6):
        for second in range(first + 1, 6):
            assert has_edge_between(graph, rows[first], rows[second])
    assert missing_rows(graph, centre, rows) == (expected_missing,)


def check_pivot(
    graph: nx.Graph,
    old_centre: set[Vertex],
    old_active: set[Vertex],
    frame: list[set[Vertex]],
    gate: set[Vertex],
    new_centre: set[Vertex],
    new_active: set[Vertex],
) -> None:
    old_rows = [old_active, *frame]
    old_missing = missing_rows(graph, old_centre, old_rows)
    assert old_centre.isdisjoint(old_active)
    assert gate and gate < old_active
    residual = old_active - gate
    assert residual == new_centre
    assert old_centre | gate == new_active
    assert connected(graph, gate)
    assert connected(graph, residual)
    assert has_edge_between(graph, gate, residual)
    assert has_edge_between(graph, gate, old_centre)
    assert all(has_edge_between(graph, gate, old_rows[index]) for index in old_missing)


def verify(length: int) -> None:
    core, host = two_apex_host(length)
    assert nx.check_planarity(core)[0]
    assert nx.node_connectivity(core) == 5
    assert nx.node_connectivity(host) == 7
    assert set(host) - {"p", "q"} == set(core)

    top = {"T"}
    u0 = {(0, 0)}
    carrier = {(0, 3), (0, 4), (1, 3), (1, 4)}
    f1 = {(0, 1), (1, 1)}
    f2 = {(0, 2)}
    f3 = {(1, 0), (1, 2), "B"}
    if length >= 2:
        f3 |= {
            (layer, index)
            for layer in range(2, length + 1)
            for index in range(5)
        }
    frame = [f1, f2, f3, {"p"}, {"q"}]

    # M_T, M_C, M_0.  Row indices include the active row as index zero.
    states = [
        (top, u0 | carrier, 3),
        (carrier, top | u0, 1),
        (u0, top | carrier, 2),
    ]
    for centre, active, missing in states:
        check_state(host, centre, active, frame, missing)

    check_pivot(host, states[0][0], states[0][1], frame, u0, states[1][0], states[1][1])
    check_pivot(host, states[1][0], states[1][1], frame, top, states[2][0], states[2][1])
    check_pivot(
        host,
        states[2][0],
        states[2][1],
        frame,
        carrier,
        states[0][0],
        states[0][1],
    )

    unions = {frozenset(centre | active) for centre, active, _ in states}
    assert unions == {frozenset(top | u0 | carrier)}
    assert [len(centre) for centre, _, _ in states] == [1, 4, 1]
    assert [(len(centre), len(active)) for centre, active, _ in states] == [
        (1, 5),
        (4, 2),
        (1, 5),
    ]

    if length == 8:
        for layer in range(1, length):
            boundary_ring = {(layer, index) for index in range(5)}
            boundary = {"p", "q"} | boundary_ring
            left = {"T"} | {
                (old_layer, index)
                for old_layer in range(layer)
                for index in range(5)
            }
            right = {"B"} | {
                (old_layer, index)
                for old_layer in range(layer + 1, length + 1)
                for index in range(5)
            }
            assert connected(host, left) and connected(host, right)
            assert all(any(host.has_edge(x, y) for y in left) for x in boundary)
            assert all(any(host.has_edge(x, y) for y in right) for x in boundary)

            left_portals = {(layer - 1, index) for index in range(5)}
            right_portals = {(layer + 1, index) for index in range(5)}
            assert all(
                len(set(host.neighbors(vertex)) & boundary_ring) == 2
                for vertex in left_portals | right_portals
            )
            assert all(
                not (set(host.neighbors(vertex)) & boundary_ring)
                for vertex in (left - left_portals) | (right - right_portals)
                if vertex not in {"p", "q"}
            )
    print(
        f"GREEN length={length}: core connectivity 5, host connectivity 7; "
        "literal reduced rotation triangle verified"
    )


def main() -> None:
    verify(1)
    verify(8)
    print("fixed frame and active carrier union are constant around the cycle")
    print("common fixed pair: {p,q}; deleting it leaves the planar tube")


if __name__ == "__main__":
    main()
