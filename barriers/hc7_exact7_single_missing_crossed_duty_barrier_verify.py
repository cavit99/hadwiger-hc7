#!/usr/bin/env python3
"""Verify the single-missing crossed-duty carrier barrier.

The script is dependency-free.  It verifies two finite graphs:

* the five-vertex exact gate quotient, in both the isolated and concentrated
  gate-contact alternatives; and
* a minimum-degree-seven expansion with an icosahedral K-lobe, an actual
  old seven-boundary, packet vector (1,2), and a legally attained paired
  state.

The expansion deliberately is not asserted to be seven-connected.  The
script finds a cut of order below seven.  This is the point of the example:
minimum degree does not replace the cell-cut use of seven-connectivity.
"""

from __future__ import annotations

from itertools import combinations


if not __debug__:
    raise RuntimeError("this assertion-based adversarial verifier must run without -O")


Vertex = str
Edge = frozenset[Vertex]


S = frozenset({"c", "a1", "t1", "a2", "t2", "a3", "t3"})
BLOCKS = (
    frozenset({"a1", "t1"}),
    frozenset({"a2", "t2"}),
    frozenset({"a3", "t3"}),
)
X = frozenset({"x1", "x2", "x3"})


def edge(u: Vertex, v: Vertex) -> Edge:
    assert u != v
    return frozenset({u, v})


def add(edges: set[Edge], u: Vertex, v: Vertex) -> None:
    edges.add(edge(u, v))


def adjacency(vertices: frozenset[Vertex], edges: set[Edge]) -> dict[Vertex, set[Vertex]]:
    answer = {v: set() for v in vertices}
    for e in edges:
        u, v = tuple(e)
        answer[u].add(v)
        answer[v].add(u)
    return answer


def components(
    vertices: frozenset[Vertex], adjacency_map: dict[Vertex, set[Vertex]]
) -> list[frozenset[Vertex]]:
    unseen = set(vertices)
    answer: list[frozenset[Vertex]] = []
    while unseen:
        start = next(iter(unseen))
        found: set[Vertex] = set()
        stack = [start]
        while stack:
            u = stack.pop()
            if u in found:
                continue
            found.add(u)
            stack.extend((adjacency_map[u] & vertices) - found)
        unseen -= found
        answer.append(frozenset(found))
    return answer


def connected(
    vertices: frozenset[Vertex], adjacency_map: dict[Vertex, set[Vertex]]
) -> bool:
    return bool(vertices) and len(components(vertices, adjacency_map)) == 1


def boundary_neighbourhood(
    vertices: frozenset[Vertex], adjacency_map: dict[Vertex, set[Vertex]]
) -> frozenset[Vertex]:
    return frozenset().union(*(adjacency_map[v] & S for v in vertices))


def carriers(
    cell: frozenset[Vertex], adjacency_map: dict[Vertex, set[Vertex]]
) -> dict[int, list[frozenset[Vertex]]]:
    ordered = tuple(sorted(cell))
    answer = {i: [] for i in range(3)}
    for mask in range(1, 1 << len(ordered)):
        candidate = frozenset(
            ordered[i] for i in range(len(ordered)) if mask >> i & 1
        )
        if not connected(candidate, adjacency_map):
            continue
        trace = boundary_neighbourhood(candidate, adjacency_map)
        for i, block in enumerate(BLOCKS):
            if block <= trace:
                answer[i].append(candidate)
    return answer


def assert_no_disjoint_duties(found: dict[int, list[frozenset[Vertex]]]) -> None:
    assert all(found[i] for i in range(3))
    for i, j in combinations(range(3), 2):
        assert not any(
            left.isdisjoint(right) for left in found[i] for right in found[j]
        ), (i, j)


def quotient(concentrated: bool) -> tuple[frozenset[Vertex], set[Edge]]:
    vertices = S | X | {"k", "j"}
    edges: set[Edge] = set()
    for u, v in combinations(X, 2):
        add(edges, u, v)
    for x in X:
        add(edges, "k", x)
        add(edges, "j", x)
    for s in ("c", "a1", "a2", "a3"):
        add(edges, "k", s)
    for s in ("c", "a1", "t2", "t3"):
        add(edges, "j", s)
    add(edges, "x1", "t1")
    if concentrated:
        add(edges, "x1", "t2")
    return frozenset(vertices), edges


def verify_quotient(concentrated: bool) -> None:
    vertices, edges = quotient(concentrated)
    adj = adjacency(vertices, edges)
    cell = X | {"k", "j"}

    # K_5-kj is three-connected, X is its literal three-cut, and the lobe
    # supports are the exact single-missing supports.
    for size in range(3):
        for deleted in combinations(sorted(cell), size):
            assert connected(cell - frozenset(deleted), adj)
    assert set(components(cell - X, adj)) == {
        frozenset({"k"}),
        frozenset({"j"}),
    }
    assert adj["k"] & S == {"c", "a1", "a2", "a3"}
    assert adj["j"] & S == {"c", "a1", "t2", "t3"}

    gate_sets = {
        "U1": adj["t1"] & X,
        "U2": adj["t2"] & X,
        "U3": adj["t3"] & X,
        "W1": adj["t1"] & X,
        "W2": adj["a2"] & X,
        "W3": adj["a3"] & X,
    }
    assert gate_sets["U1"] == {"x1"}
    if concentrated:
        assert gate_sets["U2"] == {"x1"}
        assert all(
            not gate_sets[name] for name in ("U3", "W2", "W3")
        )
    else:
        assert all(
            not gate_sets[name] for name in ("U2", "U3", "W2", "W3")
        )

    found = carriers(cell, adj)
    assert_no_disjoint_duties(found)
    # The obstruction is literal: each crossed carrier contains both lobe
    # anchors, while every first-duty carrier contains x1 and k or j.
    assert all({"k", "j"} <= carrier for carrier in found[2])
    if concentrated:
        assert all(
            "k" in carrier and ("j" in carrier or "x1" in carrier)
            for carrier in found[1]
        )
    else:
        assert all({"k", "j"} <= carrier for carrier in found[1])
    assert all(
        "x1" in carrier and bool({"k", "j"} & carrier)
        for carrier in found[0]
    )


def icosahedron() -> tuple[frozenset[Vertex], set[Edge]]:
    upper = tuple(f"u{i}" for i in range(5))
    lower = tuple(f"v{i}" for i in range(5))
    vertices = frozenset({"north", "south", *upper, *lower})
    edges: set[Edge] = set()
    for i in range(5):
        add(edges, "north", upper[i])
        add(edges, "south", lower[i])
        add(edges, upper[i], upper[(i + 1) % 5])
        add(edges, lower[i], lower[(i + 1) % 5])
        add(edges, upper[i], lower[i])
        add(edges, upper[i], lower[(i - 1) % 5])
    adj = adjacency(vertices, edges)
    assert len(edges) == 30
    assert all(len(adj[v]) == 5 for v in vertices)
    return vertices, edges


def expanded_host() -> tuple[
    frozenset[Vertex], set[Edge], frozenset[Vertex], frozenset[Vertex]
]:
    k_lobe, k_edges = icosahedron()
    cell = k_lobe | X | {"j"}
    vertices = S | cell | {"p", "q"}
    edges = set(k_edges)

    # Saturate only across the four equality classes on S.  This preserves
    # the paired partition and makes the degree calculation transparent.
    classes = (*BLOCKS, frozenset({"c"}))
    for left, right in combinations(classes, 2):
        for u in left:
            for v in right:
                add(edges, u, v)

    for packet in ("p", "q"):
        for s in S:
            add(edges, packet, s)

    for u, v in combinations(X, 2):
        add(edges, u, v)
    for x in X:
        add(edges, x, "j")

    # Each icosahedral vertex gets one gate edge.  Together with its five
    # lobe edges and its c-edge, every non-anchor lobe vertex has degree 7.
    groups = {
        "x1": ("north", "south", "u0", "v0"),
        "x2": ("u1", "u2", "v1", "v2"),
        "x3": ("u3", "u4", "v3", "v4"),
    }
    assert set().union(*(set(group) for group in groups.values())) == set(k_lobe)
    for x, group in groups.items():
        for v in group:
            add(edges, x, v)

    for v in k_lobe:
        add(edges, v, "c")
    anchor = "north"
    for s in ("a1", "a2", "a3"):
        add(edges, anchor, s)
    for s in ("c", "a1", "t2", "t3"):
        add(edges, "j", s)
    add(edges, "x1", "t1")
    return frozenset(vertices), edges, cell, k_lobe


def contract(
    vertices: frozenset[Vertex], edges: set[Edge], cluster: frozenset[Vertex], image: Vertex
) -> tuple[frozenset[Vertex], set[Edge]]:
    assert image not in vertices
    answer_vertices = (vertices - cluster) | {image}
    answer_edges: set[Edge] = set()
    for e in edges:
        ends = set(e)
        outside = ends - cluster
        if not outside:
            continue
        if len(outside) == 1 and ends & cluster:
            add(answer_edges, image, next(iter(outside)))
        elif len(outside) == 2:
            u, v = tuple(outside)
            add(answer_edges, u, v)
    return frozenset(answer_vertices), answer_edges


def extend_colouring(
    vertices: frozenset[Vertex],
    edges: set[Edge],
    fixed: dict[Vertex, int],
    colour_count: int,
) -> dict[Vertex, int] | None:
    adj = adjacency(vertices, edges)
    assert set(fixed) <= set(vertices)
    assert all(
        fixed[u] != fixed[v]
        for e in edges
        if e <= fixed.keys()
        for u, v in [tuple(e)]
    )
    assigned = dict(fixed)

    def search() -> bool:
        if len(assigned) == len(vertices):
            return True
        unassigned = set(vertices) - assigned.keys()
        vertex = max(
            unassigned,
            key=lambda v: (
                len({assigned[w] for w in adj[v] if w in assigned}),
                len(adj[v]),
                v,
            ),
        )
        forbidden = {assigned[w] for w in adj[vertex] if w in assigned}
        for colour in range(colour_count):
            if colour in forbidden:
                continue
            assigned[vertex] = colour
            if search():
                return True
            del assigned[vertex]
        return False

    return dict(assigned) if search() else None


def verify_expanded_host() -> frozenset[Vertex]:
    vertices, edges, cell, k_lobe = expanded_host()
    adj = adjacency(vertices, edges)
    anchor = "north"

    assert min(len(adj[v]) for v in vertices) == 7
    for size in range(3):
        for deleted in combinations(sorted(cell), size):
            assert connected(cell - frozenset(deleted), adj)
    assert set(components(cell - X, adj)) == {k_lobe, frozenset({"j"})}
    assert boundary_neighbourhood(k_lobe, adj) == {"c", "a1", "a2", "a3"}
    assert adj["j"] & S == {"c", "a1", "t2", "t3"}
    assert adj["t1"] & X == {"x1"}
    assert all(not (adj[s] & X) for s in ("a2", "t2", "a3", "t3"))

    # The old separation is actual.  C and q are two disjoint full packets;
    # every full packet contained in C includes the same three bottlenecks.
    left = frozenset({"p"})
    right = cell | {"q"}
    assert not any(edge(u, v) in edges for u in left for v in right)
    assert boundary_neighbourhood(left, adj) == S
    assert boundary_neighbourhood(frozenset({"q"}), adj) == S
    assert boundary_neighbourhood(cell, adj) == S
    # Check the literal bottleneck certificate directly.  Every B2- or
    # B3-carrier must contain both unique endpoint portals north and j.
    # Every B1-carrier must contain x1 and one of north,j.  Hence no two
    # distinct duties can have disjoint carriers.  This avoids disguising
    # the structural certificate as a large connected-subset census.
    assert adj["a1"] & cell == {anchor, "j"}
    assert adj["t1"] & cell == {"x1"}
    assert adj["a2"] & cell == {anchor}
    assert adj["t2"] & cell == {"j"}
    assert adj["a3"] & cell == {anchor}
    assert adj["t3"] & cell == {"j"}

    # A proper contraction of p together with B1 returns exactly the old
    # equality partition in a six-colouring.
    cluster = left | BLOCKS[0]
    assert connected(cluster, adj)
    minor_vertices, minor_edges = contract(vertices, edges, cluster, "b1")
    fixed = {
        "b1": 0,
        "a2": 1,
        "t2": 1,
        "a3": 2,
        "t3": 2,
        "c": 3,
    }
    witness = extend_colouring(minor_vertices, minor_edges, fixed, 6)
    assert witness is not None

    # This particular degree-seven expansion is not K7-free.  Freeze an
    # explicit model so the example cannot be mistaken for an HC7 host.
    model = (
        frozenset({"a1", "p"}),
        frozenset({"t1"}),
        frozenset({"a2", "q"}),
        frozenset({"t2"}),
        frozenset({"a3", anchor, "x1"}),
        frozenset({"t3", "j"}),
        frozenset({"c"}),
    )
    assert all(connected(bag, adj) for bag in model)
    assert all(
        any(edge(u, v) in edges for u in left for v in right)
        for left, right in combinations(model, 2)
    )

    # The displayed four-cut is minimum.  Its existence is forced by the
    # common-face/cell-cut theorem, but the finite witness keeps the scope
    # of this barrier executable.
    cut = frozenset({"c", "j", anchor, "t1"})
    for size in range(4):
        for deleted_tuple in combinations(sorted(vertices), size):
            deleted = frozenset(deleted_tuple)
            assert connected(vertices - deleted, adj)
    assert not connected(vertices - cut, adj)
    return cut


def main() -> None:
    verify_quotient(concentrated=False)
    verify_quotient(concentrated=True)
    cut = verify_expanded_host()
    print("static quotient: isolated and concentrated alternatives verified")
    print("static quotient: all three duties exist, but no two have disjoint carriers")
    print("expanded host: exact supports, packet vector (1,2), and attained state verified")
    print("expanded host: minimum degree 7, connectivity 4; minimum cut:", sorted(cut))
    print("expanded host: explicit K7 model verified; no HC7 counterexample is claimed")


if __name__ == "__main__":
    main()
