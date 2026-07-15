"""Verify the explicit joint-contact-five icosahedral guardrail.

This checks only the finite literal data in Section 6 of
hc7_atomic_two_pole_contact_trichotomy.md.  Seven-connectivity and
K7-minor-freeness are proved structurally in the cited audited note.
"""

from __future__ import annotations

Vertex = str
Edge = frozenset[Vertex]


def edge(first: Vertex, second: Vertex) -> Edge:
    assert first != second
    return frozenset((first, second))


def icosahedron_join() -> tuple[set[Vertex], set[Edge]]:
    vertices: set[Vertex] = set()
    edges: set[Edge] = set()
    top, bottom = "t", "b"
    upper = [f"u{i}" for i in range(5)]
    lower = [f"w{i}" for i in range(5)]
    vertices.update([top, bottom, *upper, *lower, "p", "q"])

    for index in range(5):
        edges.add(edge(top, upper[index]))
        edges.add(edge(bottom, lower[index]))
        edges.add(edge(upper[index], upper[(index + 1) % 5]))
        edges.add(edge(lower[index], lower[(index + 1) % 5]))
        edges.add(edge(upper[index], lower[index]))
        edges.add(edge(upper[index], lower[(index - 1) % 5]))

    edges.add(edge("p", "q"))
    for apex in ("p", "q"):
        for vertex in vertices - {"p", "q"}:
            edges.add(edge(apex, vertex))
    return vertices, edges


def adjacent(edges: set[Edge], first: Vertex, second: Vertex) -> bool:
    return edge(first, second) in edges


def connected(vertices: set[Vertex], edges: set[Edge]) -> bool:
    if not vertices:
        return False
    reached = {next(iter(vertices))}
    while True:
        expanded = reached | {
            vertex
            for vertex in vertices - reached
            if any(adjacent(edges, vertex, old) for old in reached)
        }
        if expanded == reached:
            return reached == vertices
        reached = expanded


def main() -> None:
    vertices, edges = icosahedron_join()
    poles = {"u3", "u4"}
    rows = [
        {"t", "u0"},
        {"u1"},
        {"u2"},
        {"b", "w0", "w1", "w2", "w3", "w4"},
        {"p"},
        {"q"},
    ]

    assert set().union(*rows) == vertices - poles
    assert sum(map(len, rows)) == len(vertices - poles)
    assert all(connected(row, edges) for row in rows)
    for first in range(6):
        for second in range(first + 1, 6):
            assert any(
                adjacent(edges, x, y)
                for x in rows[first]
                for y in rows[second]
            )

    contacts: dict[str, set[int]] = {}
    for pole in sorted(poles):
        contacts[pole] = {
            index + 1
            for index, row in enumerate(rows)
            if any(adjacent(edges, pole, vertex) for vertex in row)
        }

    assert adjacent(edges, "u3", "u4")
    assert contacts["u3"] == {1, 3, 4, 5, 6}
    assert contacts["u4"] == {1, 4, 5, 6}
    assert len(contacts["u3"] | contacts["u4"]) == 5

    print("GREEN: spanning K6 rows are connected and pairwise adjacent")
    print("contacts", contacts)
    print("joint_contact", len(contacts["u3"] | contacts["u4"]))


if __name__ == "__main__":
    main()
