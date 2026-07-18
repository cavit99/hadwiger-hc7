#!/usr/bin/env python3
"""Verify the universal blocker first-hit concentration barrier."""

from __future__ import annotations

from itertools import combinations


A = {"b", "i0", "i1", "aJ"}
K = {"q", "j0", "j1", "kI"}
C = {"r"}
D = {"d"}
E = {"e"}
F = {"f"}
PARTS = [A, K, C, D, E, F]

T = {"b", "i0", "i1", "q", "j0", "j1", "r"}
R = {"aJ", "kI", "d", "e", "f"}
L = {f"x{k}" for k in range(5)}
V = set().union(*PARTS, L)
BLOCKER = frozenset({"b", "i0"})


def pair(x: str, y: str) -> frozenset[str]:
    return frozenset({x, y})


edges: set[frozenset[str]] = set()
for first, second in combinations(PARTS, 2):
    edges.update(pair(x, y) for x in first for y in second)
edges.add(BLOCKER)
for k in range(5):
    edges.add(pair(f"x{k}", f"x{(k + 1) % 5}"))
for x in L:
    edges.update(pair(x, t) for t in T)


def adjacent(x: str, y: str) -> bool:
    return pair(x, y) in edges


def has_edge(left: set[str], right: set[str]) -> bool:
    return any(adjacent(x, y) for x in left for y in right)


def connected(vertices: set[str], removed: set[str] | None = None) -> bool:
    removed = removed or set()
    live = vertices - removed
    if not live:
        return True
    seen = {next(iter(live))}
    stack = list(seen)
    while stack:
        x = stack.pop()
        for y in live - seen:
            if adjacent(x, y):
                seen.add(y)
                stack.append(y)
    return seen == live


def verify_connectivity() -> None:
    for size in range(7):
        for removed_tuple in combinations(V, size):
            assert connected(V, set(removed_tuple))


def verify_geometry() -> None:
    assert len(T) == 7
    assert not has_edge(L, R)
    assert connected(L)
    assert connected(R)

    named_subgraphs = {
        "QI": {"i0", "i1", "kI"},
        "QJ": {"j0", "j1", "aJ"},
        "Qb": {"b"},
        "Qq": {"q"},
        "Q0": {"d", "e", "f"},
    }
    traces = [
        {"i0", "i1"}, {"j0", "j1"}, {"b"}, {"q"}, set()
    ]
    assert [subgraph & T for subgraph in named_subgraphs.values()] == traces
    assert set().union(*named_subgraphs.values()) & T == T - {"r"}
    assert all(connected(subgraph) for subgraph in named_subgraphs.values())
    for first, second in combinations(named_subgraphs.values(), 2):
        assert has_edge(first, second)
    assert all(has_edge({"r"}, subgraph) for subgraph in named_subgraphs.values())

    sectors = [
        {"i0", "x0"}, {"j0", "x1"}, {"i1", "x2"},
        {"j1", "x3"}, {"x4"},
    ]
    assert [sector & T for sector in sectors] == [
        {"i0"}, {"j0"}, {"i1"}, {"j1"}, set()
    ]
    assert all(connected(sector) for sector in sectors)
    assert all(
        has_edge(sectors[k], sectors[(k + 1) % 5]) for k in range(5)
    )
    assert has_edge({"b"}, sectors[0]) and has_edge({"b"}, sectors[2])
    assert has_edge({"q"}, sectors[1]) and has_edge({"q"}, sectors[3])
    assert {edge for edge in edges if "b" in edge and edge & {"i0", "i1"}} == {
        BLOCKER
    }
    assert not any(adjacent(x, y) for x, y in combinations({"q", "j0", "j1"}, 2))


def verify_colouring_and_locks() -> None:
    colour: dict[str, int] = {}
    for index, part in enumerate(PARTS):
        colour.update({x: index for x in part})
    colour.update({"x0": 3, "x1": 4, "x2": 3, "x3": 4, "x4": 5})
    assert set(colour) == V
    for edge in edges - {BLOCKER}:
        x, y = tuple(edge)
        assert colour[x] != colour[y]

    # A six-colouring of the complete six-partite core is constant on each
    # part: one chosen vertex from every part is a K6, and every other
    # vertex is adjacent to the five representatives outside its own part.
    representatives = [next(iter(part)) for part in PARTS]
    assert all(adjacent(x, y) for x, y in combinations(representatives, 2))
    for part, representative in zip(PARTS, representatives):
        others = set(representatives) - {representative}
        assert all(all(adjacent(x, y) for y in others) for x in part)

    assert colour["b"] == colour["i0"] == 0
    for other_colour in range(1, 6):
        witnesses = {x for x in V if colour[x] == other_colour}
        assert has_edge({"b"}, witnesses)
        assert has_edge({"i0"}, witnesses)

    # The three colours absent on T have one far-side vertex each.  Every
    # shortest alpha/beta path has that vertex internally, and all three
    # vertices belong to the same boundary-free row.
    assert {colour[x] for x in T} == {0, 1, 2}
    q0 = {"d", "e", "f"}
    for witness, beta in [("d", 3), ("e", 4), ("f", 5)]:
        assert {x for x in R | T if colour[x] == beta} == {witness}
        assert adjacent("b", witness) and adjacent(witness, "i0")
        assert witness in q0


def verify_scope() -> None:
    clique = {"b", "i0", "q", "r", "d", "e", "f"}
    assert all(adjacent(x, y) for x, y in combinations(clique, 2))
    assert "x0" not in clique


def main() -> None:
    verify_connectivity()
    print("host: seven-connected with an actual order-seven L-T-R separation")
    verify_geometry()
    print("geometry: five named connected subgraphs and five cyclic left-side subgraphs verified")
    verify_colouring_and_locks()
    print("response: universal obstructing-edge equality and all five colour locks verified")
    print("first hits: all three absent colours enter the same boundary-free connected subgraph")
    verify_scope()
    print("scope: an explicit K7 remains after deleting a left-side vertex")


if __name__ == "__main__":
    main()
