#!/usr/bin/env python3
"""Verify the separated equality-gadget barrier for boundary transitions."""

from collections import deque
from itertools import combinations


VERTICES = (
    "a", "b", "ap", "bp", "pa", "qa", "pb", "qb", "c", "d"
)
S = ("ap", "bp")
G_EDGE = tuple(sorted(("a", "b")))
H_EDGE = tuple(sorted(("c", "d")))


def edge(x, y):
    return tuple(sorted((x, y)))


def make_edges(include_g=True, include_h=True):
    edges = set()
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
    if include_g:
        edges.add(G_EDGE)
    if include_h:
        edges.add(H_EDGE)
    return frozenset(edges)


def colourings(edges, colours=3):
    adjacency = {v: set() for v in VERTICES}
    for x, y in edges:
        adjacency[x].add(y)
        adjacency[y].add(x)
    order = sorted(VERTICES, key=lambda v: -len(adjacency[v]))
    assignment = {}
    out = []

    def search(i):
        if i == len(order):
            out.append(tuple(assignment[v] for v in VERTICES))
            return
        v = order[i]
        forbidden = {assignment[w] for w in adjacency[v] if w in assignment}
        for colour in range(colours):
            if colour not in forbidden:
                assignment[v] = colour
                search(i + 1)
                del assignment[v]

    search(0)
    return out


def as_dict(colouring):
    return dict(zip(VERTICES, colouring))


def boundary_partition(colouring):
    c = as_dict(colouring)
    return "equal" if c[S[0]] == c[S[1]] else "different"


def signature(colouring):
    c = as_dict(colouring)
    return (
        "equal" if c["a"] == c["b"] else "proper",
        "equal" if c["c"] == c["d"] else "proper",
    )


def kempe_neighbours(colouring, edges):
    c = as_dict(colouring)
    adjacency = {v: set() for v in VERTICES}
    for x, y in edges:
        adjacency[x].add(y)
        adjacency[y].add(x)
    neighbours = set()
    for alpha in range(3):
        for beta in range(alpha + 1, 3):
            remaining = {v for v in VERTICES if c[v] in (alpha, beta)}
            while remaining:
                root = min(remaining)
                component = {root}
                queue = [root]
                remaining.remove(root)
                while queue:
                    v = queue.pop()
                    for w in adjacency[v]:
                        if w in remaining and c[w] in (alpha, beta):
                            remaining.remove(w)
                            component.add(w)
                            queue.append(w)
                switched = dict(c)
                for v in component:
                    switched[v] = beta if c[v] == alpha else alpha
                neighbours.add(tuple(switched[v] for v in VERTICES))
    return neighbours


def connected_components(nodes, edges):
    nodes = set(nodes)
    unseen = set(nodes)
    components = []
    while unseen:
        root = min(unseen)
        unseen.remove(root)
        comp = {root}
        queue = deque([root])
        while queue:
            current = queue.popleft()
            for nxt in kempe_neighbours(current, edges):
                if nxt in nodes and nxt not in comp:
                    comp.add(nxt)
                    unseen.discard(nxt)
                    queue.append(nxt)
        components.append(comp)
    return components


def padded_hc7_graph(edges):
    """Lift the base graph by K3 and three false twins of one clique vertex."""
    triangle = ("t0", "t1", "t2")
    twins = ("w0", "w1", "w2")
    lifted = set(edges)
    for x, y in combinations(triangle, 2):
        lifted.add(edge(x, y))
    for t in triangle:
        for v in VERTICES:
            lifted.add(edge(t, v))
    for w in twins:
        for v in VERTICES:
            lifted.add(edge(w, v))
        lifted.add(edge(w, "t1"))
        lifted.add(edge(w, "t2"))
    return frozenset(lifted), triangle, twins


def is_connected_after_deleting(vertices, edges, deleted):
    remaining = set(vertices) - set(deleted)
    if len(remaining) <= 1:
        return True
    adjacency = {v: set() for v in remaining}
    for x, y in edges:
        if x in remaining and y in remaining:
            adjacency[x].add(y)
            adjacency[y].add(x)
    root = next(iter(remaining))
    reached = {root}
    queue = [root]
    while queue:
        v = queue.pop()
        for w in adjacency[v]:
            if w not in reached:
                reached.add(w)
                queue.append(w)
    return reached == remaining


def apply_switch(colouring, component, alpha, beta):
    c = as_dict(colouring)
    for v in component:
        assert c[v] in (alpha, beta)
        c[v] = beta if c[v] == alpha else alpha
    return tuple(c[v] for v in VERTICES)


def main():
    full = make_edges()
    minus_g = make_edges(include_g=False)
    minus_h = make_edges(include_h=False)
    common = make_edges(include_g=False, include_h=False)

    assert not colourings(full)
    assert colourings(full, colours=4)
    cg = colourings(minus_g)
    ch = colourings(minus_h)
    cc = colourings(common)
    assert cg and ch and cc
    assert (len(cg), len(ch), len(cc)) == (24, 24, 72)

    assert {boundary_partition(c) for c in cg} == {"equal"}
    assert {boundary_partition(c) for c in ch} == {"different"}

    signatures = {signature(c) for c in cc}
    assert signatures == {
        ("equal", "equal"),
        ("equal", "proper"),
        ("proper", "equal"),
    }

    components = connected_components(cc, common)
    assert len(components) == 1
    only = components[0]
    assert {boundary_partition(c) for c in only} == {"equal", "different"}
    assert {signature(c) for c in only} == signatures

    direct = any(set(kempe_neighbours(c, common)) & set(ch) for c in cg)
    assert not direct

    # An explicit two-switch route from (proper,equal) to
    # (equal,proper), with (equal,equal) as the intermediate state.
    start_map = {
        "a": 0, "ap": 0, "pa": 1, "qa": 2,
        "b": 1, "bp": 1, "pb": 0, "qb": 2,
        "c": 2, "d": 2,
    }
    start = tuple(start_map[v] for v in VERTICES)
    middle = apply_switch(start, {"b", "bp", "pb"}, 0, 1)
    finish = apply_switch(middle, {"d"}, 1, 2)
    assert start in ch
    assert middle in cc
    assert finish in cg
    assert [signature(c) for c in (start, middle, finish)] == [
        ("proper", "equal"),
        ("equal", "equal"),
        ("equal", "proper"),
    ]
    assert middle in kempe_neighbours(start, common)
    assert finish in kempe_neighbours(middle, common)

    # The named one-edge response families are exactly the appropriate
    # signature faces inside the common host.
    cg_set = set(cg)
    ch_set = set(ch)
    assert cg_set == {c for c in cc if signature(c) == ("equal", "proper")}
    assert ch_set == {c for c in cc if signature(c) == ("proper", "equal")}

    # The displayed vertex separation has no cross-edge.
    A = {"a", "b", "pa", "qa", "pb", "qb"}
    B = {"c", "d"}
    for x, y in full:
        assert not ((x in A and y in B) or (x in B and y in A))
    assert set(VERTICES) == A | set(S) | B
    assert G_EDGE[0] in A and G_EDGE[1] in A
    assert H_EDGE[0] in B and H_EDGE[1] in B

    # H contains a literal triangle and is connected, hence its triangle
    # model can be enlarged to a spanning K3 model.
    assert all(edge(x, y) in common for x, y in (("a", "pa"), ("a", "qa"), ("pa", "qa")))
    assert is_connected_after_deleting(VERTICES, common, set())
    for v in VERTICES:
        assert is_connected_after_deleting(VERTICES, full, {v})

    # Exact order-eight, eight-connected HC7-palette lift.
    lifted_full, triangle, twins = padded_hc7_graph(full)
    lifted_common, _, _ = padded_hc7_graph(common)
    lifted_vertices = tuple(VERTICES) + triangle + twins
    boundary = set(S) | set(triangle) | set(twins)
    assert len(boundary) == 8
    assert not is_connected_after_deleting(lifted_vertices, lifted_full, boundary)

    # Every deletion of at most seven vertices leaves the lift connected;
    # the displayed boundary of order eight disconnects it.
    for size in range(8):
        for deleted in combinations(lifted_vertices, size):
            assert is_connected_after_deleting(lifted_vertices, lifted_full, deleted)
    assert not is_connected_after_deleting(lifted_vertices, lifted_full, boundary)

    A = {"a", "b", "pa", "qa", "pb", "qb"}
    B = {"c", "d"}
    assert set(lifted_vertices) == A | boundary | B
    for x, y in lifted_full:
        assert not ((x in A and y in B) or (x in B and y in A))
    assert is_connected_after_deleting(A, lifted_full, set())
    assert is_connected_after_deleting(B, lifted_full, set())
    for shore in (A, B):
        for s in boundary:
            assert any(edge(v, s) in lifted_full for v in shore)

    # The common host contains the literal K6 formed by the join triangle
    # and one equality-gadget triangle.
    literal_k6 = set(triangle) | {"a", "pa", "qa"}
    assert len(literal_k6) == 6
    assert all(edge(x, y) in lifted_common for x, y in combinations(literal_k6, 2))

    # The full lift contains a K7 minor: triangle singletons plus the four
    # displayed connected base branch sets.
    k7_bags = [{t} for t in triangle] + [
        {"a", "pa", "ap"},
        {"b", "pb", "bp"},
        {"c"},
        {"d"},
    ]
    assert len(k7_bags) == 7
    for bag in k7_bags:
        assert is_connected_after_deleting(bag, lifted_full, set())
    for left, right in combinations(k7_bags, 2):
        assert any(edge(x, y) in lifted_full for x in left for y in right)

    print("GREEN separated opposite-response transition barrier")
    print(f"colourings: G-g={len(cg)}, G-h={len(ch)}, H={len(cc)}")
    print("boundary languages: G-g={equal}, G-h={different}")
    print("common-host signatures: EE, EP, PE; PP absent")
    print("Kempe reconfiguration graph of H: one component containing both languages")
    print("shortest response-to-response Kempe distance=2, through EE")
    print("padded lift: q=6, boundary=8, connectivity=8, both shores full")
    print("padded common host contains K6; padded full host contains K7 minor")


if __name__ == "__main__":
    main()
