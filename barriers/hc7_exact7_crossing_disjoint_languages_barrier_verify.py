#!/usr/bin/env python3
"""Verify the exact-seven crossing-edge disjoint-language barrier."""

from __future__ import annotations

from itertools import combinations


CORE = ("a", "b", "ap", "bp", "pa", "qa", "pb", "qb", "c", "d")
X = ("x1", "x2")
Y = ("y1", "y2", "y3")
W = X + Y
Q = ("q0", "q1", "q2", "q3")
R, Z, ELL = "r", "s", "ell"
VERTICES = CORE + W + Q + (R, Z, ELL)

EDGE_E = tuple(sorted(("a", "b")))
EDGE_F = tuple(sorted(("c", "d")))
BOUNDARY = frozenset(("b", "d") + W)
OPEN_A = frozenset(CORE) - {"b", "d"}
OPEN_B = frozenset(Q + (R, Z, ELL))


def edge(x: str, y: str) -> tuple[str, str]:
    assert x != y
    return tuple(sorted((x, y)))


def host_edges(include_e: bool = True, include_f: bool = True):
    edges: set[tuple[str, str]] = set()

    for x, xp, p, q in (
        ("a", "ap", "pa", "qa"),
        ("b", "bp", "pb", "qb"),
    ):
        edges.add(edge(p, q))
        for z in (x, xp):
            edges.add(edge(z, p))
            edges.add(edge(z, q))

    for z in ("c", "d"):
        edges.add(edge(z, "ap"))
        edges.add(edge(z, "bp"))
    if include_e:
        edges.add(EDGE_E)
    if include_f:
        edges.add(EDGE_F)

    for x in X:
        for y in Y:
            edges.add(edge(x, y))
    for w in W:
        for v in CORE:
            edges.add(edge(w, v))

    for u, v in combinations(Q, 2):
        edges.add(edge(u, v))
    for q in Q:
        for v in ("y1", "y2", R, Z):
            edges.add(edge(q, v))
    edges.update((edge("y1", R), edge(R, Z), edge(Z, "y2")))

    for v in BOUNDARY:
        edges.add(edge(ELL, v))
    edges.add(edge(ELL, "q0"))

    boundary_neighbours = {
        "q0": {"b", "d", "y1", "y2", "y3"},
        "q1": {"d", "x2", "y1", "y2", "y3"},
        "q2": {"b", "x2", "y1", "y2", "y3"},
        "q3": {"b", "x2", "y1", "y2", "y3"},
        R: {"b", "d", "x2", "y1", "y3"},
        Z: {"b", "d", "x2", "y2"},
    }
    for u, neighbours in boundary_neighbours.items():
        for v in neighbours:
            edges.add(edge(u, v))

    return frozenset(edges)


def adjacency(vertices, edges):
    out = {v: set() for v in vertices}
    for x, y in edges:
        if x in out and y in out:
            out[x].add(y)
            out[y].add(x)
    return out


def components(vertices, edges):
    remaining = set(vertices)
    adj = adjacency(remaining, edges)
    output = []
    while remaining:
        reached = {next(iter(remaining))}
        stack = list(reached)
        while stack:
            v = stack.pop()
            for w in adj[v] - reached:
                reached.add(w)
                stack.append(w)
        output.append(frozenset(reached))
        remaining -= reached
    return output


def connected(vertices, edges):
    vertices = set(vertices)
    return bool(vertices) and len(components(vertices, edges)) == 1


def colourings(vertices, edges, colours, *, preset=None, limit=None):
    vertices = tuple(sorted(vertices))
    adj = adjacency(vertices, edges)
    assignment = {} if preset is None else dict(preset)
    assert all(v in adj and 0 <= c < colours for v, c in assignment.items())
    assert all(
        x not in assignment or y not in assignment or assignment[x] != assignment[y]
        for x, y in edges
    )
    order = sorted(
        (v for v in vertices if v not in assignment),
        key=lambda v: (-len(adj[v]), v),
    )
    output = []

    def search(i):
        if limit is not None and len(output) >= limit:
            return
        if i == len(order):
            output.append(dict(assignment))
            return
        v = order[i]
        forbidden = {assignment[w] for w in adj[v] if w in assignment}
        for colour in range(colours):
            if colour not in forbidden:
                assignment[v] = colour
                search(i + 1)
                del assignment[v]

    search(0)
    return output


def proper(colouring, edges):
    return all(colouring[x] != colouring[y] for x, y in edges)


def signature(colouring):
    return (
        "E" if colouring["a"] == colouring["b"] else "P",
        "E" if colouring["c"] == colouring["d"] else "P",
    )


def boundary_partition(colouring):
    classes = {}
    for v in BOUNDARY:
        classes.setdefault(colouring[v], set()).add(v)
    return frozenset(frozenset(block) for block in classes.values())


def connected_full_subsets(shore, edges):
    shore = tuple(sorted(shore))
    output = []
    for size in range(1, len(shore) + 1):
        for subset in combinations(shore, size):
            chosen = frozenset(subset)
            if not connected(chosen, edges):
                continue
            if all(any(edge(v, s) in edges for v in chosen) for s in BOUNDARY):
                output.append(chosen)
    return output


def packing_number(full_sets):
    best = 0

    def search(start, used, count):
        nonlocal best
        best = max(best, count)
        for i in range(start, len(full_sets)):
            if used.isdisjoint(full_sets[i]):
                search(i + 1, used | full_sets[i], count + 1)

    search(0, frozenset(), 0)
    return best


def clique_number(vertices, edges):
    vertices = tuple(sorted(vertices))
    for size in range(len(vertices), 0, -1):
        for chosen in combinations(vertices, size):
            if all(edge(x, y) in edges for x, y in combinations(chosen, 2)):
                return size
    return 0


def verify_explicit_responses(common):
    shared = {
        "q0": 0, "q1": 1, "q2": 2, "q3": 3,
        "x1": 0, "x2": 0,
        "y1": 4, "y2": 5, "y3": 4,
        R: 5, Z: 4,
    }
    rows = {
        ("E", "E"): (1, 1, 1, 1, 2, 3, 2, 3, 2, 2, 3),
        ("E", "P"): (1, 1, 1, 1, 2, 3, 2, 3, 3, 2, 3),
        ("P", "E"): (2, 1, 2, 1, 1, 3, 2, 3, 3, 3, 2),
    }
    response_vertices = CORE + (ELL,)
    output = {}
    for sig, values in rows.items():
        colouring = dict(shared)
        colouring.update(zip(response_vertices, values))
        assert set(colouring) == set(VERTICES)
        assert proper(colouring, common)
        assert signature(colouring) == sig
        output[sig] = colouring
    return output


def main():
    full = host_edges()
    common = host_edges(False, False)
    minus_e = host_edges(False, True)
    minus_f = host_edges(True, False)

    assert len(VERTICES) == 22
    assert len(full) == 124
    assert set(VERTICES) == OPEN_A | BOUNDARY | OPEN_B
    assert not (OPEN_A & BOUNDARY or OPEN_A & OPEN_B or BOUNDARY & OPEN_B)
    assert not any(
        (x in OPEN_A and y in OPEN_B) or (x in OPEN_B and y in OPEN_A)
        for x, y in full
    )
    assert EDGE_E[0] in OPEN_A and EDGE_E[1] in BOUNDARY
    assert EDGE_F[0] in OPEN_A and EDGE_F[1] in BOUNDARY
    assert connected(OPEN_A, full) and connected(OPEN_B, full)
    for shore in (OPEN_A, OPEN_B):
        for s in BOUNDARY:
            assert any(edge(v, s) in full for v in shore)

    # Exhaust all cuts of order at most six and check the displayed cut.
    for size in range(7):
        for deleted in combinations(VERTICES, size):
            assert len(components(set(VERTICES) - set(deleted), full)) == 1
    assert len(components(set(VERTICES) - set(BOUNDARY), full)) == 2

    # The finite neighbourhood certificate used in the written proof.
    h = frozenset(Q + (R, Z))
    minimum_by_size = []
    adj = adjacency(VERTICES, full)
    for size in range(1, 7):
        values = []
        for chosen in combinations(sorted(h), size):
            chosen = set(chosen)
            neighbours = set().union(*(adj[v] for v in chosen)) - chosen
            values.append(len(neighbours))
        minimum_by_size.append(min(values))
    assert minimum_by_size == [9, 9, 9, 8, 7, 7]
    for size in range(1, len(OPEN_B) + 1):
        for chosen in combinations(sorted(OPEN_B), size):
            chosen = set(chosen)
            neighbours = set().union(*(adj[v] for v in chosen)) - chosen
            assert len(neighbours) >= 7

    full_a = connected_full_subsets(OPEN_A, full)
    full_b = connected_full_subsets(OPEN_B, full)
    assert packing_number(full_a) == 2
    assert packing_number(full_b) == 1

    boundary_edges = frozenset(
        e for e in full if e[0] in BOUNDARY and e[1] in BOUNDARY
    )
    assert colourings(BOUNDARY, boundary_edges, 3, limit=1)
    assert not colourings(BOUNDARY, boundary_edges, 2, limit=1)

    # Exact chromatic assertions for the two intact closed shores.
    triangle_preset = {"a": 0, "pa": 1, "qa": 2}
    assert not colourings(OPEN_A | BOUNDARY, full, 5,
                          preset=triangle_preset, limit=1)
    assert colourings(OPEN_A | BOUNDARY, full, 6,
                      preset=triangle_preset, limit=1)
    q_preset = {q: i for i, q in enumerate(Q)}
    assert not colourings(OPEN_B | BOUNDARY, full, 5,
                          preset=q_preset, limit=1)
    assert colourings(OPEN_B | BOUNDARY, full, 6,
                      preset=q_preset, limit=1)

    # The languages are disjoint: verify their forced opposite equalities.
    for colouring in colourings(OPEN_A | BOUNDARY, full, 6,
                                 preset=triangle_preset):
        assert colouring["y1"] == colouring["y2"]
    for colouring in colourings(OPEN_B | BOUNDARY, full, 6,
                                 preset=q_preset):
        assert colouring["y1"] != colouring["y2"]
    assert not colourings(VERTICES, full, 6, preset=q_preset, limit=1)

    explicit = verify_explicit_responses(common)
    assert proper(explicit[("E", "P")], minus_e)
    assert proper(explicit[("P", "E")], minus_f)
    assert explicit[("E", "P")]["a"] == explicit[("E", "P")]["b"]
    assert explicit[("P", "E")]["c"] == explicit[("P", "E")]["d"]
    assert explicit[("E", "E")]["a"] == explicit[("E", "E")]["b"]
    assert explicit[("E", "E")]["c"] == explicit[("E", "E")]["d"]

    # Normalizing the K4 colours loses no equality partition or signature.
    common_colourings = colourings(VERTICES, common, 6, preset=q_preset)
    assert len(common_colourings) == 48
    assert {signature(c) for c in common_colourings} == {
        ("E", "E"), ("E", "P"), ("P", "E")
    }
    expected_partition = frozenset((
        frozenset(("b",)),
        frozenset(("d",)),
        frozenset(("x1", "x2")),
        frozenset(("y1", "y3")),
        frozenset(("y2",)),
    ))
    assert {boundary_partition(c) for c in common_colourings} == {
        expected_partition
    }

    singleton_vertices = {
        next(iter(block)) for block in expected_partition if len(block) == 1
    }
    demand = len(expected_partition) - clique_number(
        singleton_vertices, boundary_edges
    )
    assert demand == 3 > packing_number(full_b)

    literal_k6 = frozenset(Q + (R, Z))
    assert all(edge(x, y) in common for x, y in combinations(literal_k6, 2))

    k7_bags = [
        {"q0"}, {"q1"}, {"q2"}, {"q3"},
        {"y1"}, {R}, {Z, "y2", "x2"},
    ]
    for bag in k7_bags:
        assert connected(bag, full)
    for left, right in combinations(k7_bags, 2):
        assert any(edge(x, y) in full for x in left for y in right)

    # Deleting y3 leaves a non-six-colourable graph, while deleting e as
    # well has the displayed EP six-colouring.
    without_y3 = set(VERTICES) - {"y3"}
    assert not colourings(without_y3, full, 6, preset=q_preset, limit=1)
    restricted_ep = {
        v: c for v, c in explicit[("E", "P")].items() if v != "y3"
    }
    restricted_minus_e = frozenset(
        edge for edge in minus_e if "y3" not in edge
    )
    assert proper(restricted_ep, restricted_minus_e)

    print("GREEN exact-seven crossing disjoint-languages barrier")
    print("order=22 size=124 kappa=7 boundary=7 chi_boundary=3 packing=(2,1)")
    print("common signatures=EE,EP,PE; PP absent; one five-block partition of demand=3")
    print("both intact closed shores are exactly 6-colourable and their languages are disjoint")
    print("full host contains explicit K7 minor; deleting y3 leaves a 7-chromatic graph")


if __name__ == "__main__":
    main()
