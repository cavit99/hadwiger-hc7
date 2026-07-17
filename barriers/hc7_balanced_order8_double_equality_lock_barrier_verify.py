#!/usr/bin/env python3
"""Verify the balanced order-eight double-equality lock barrier.

The script is dependency-free and exhaustive on its finite graph.  Colour
names are 0,...,5 (or 0,...,6 for the displayed seven-colouring).
"""

from collections import deque
from itertools import combinations


VERTICES = (
    "a", "b", "ap", "bp", "pa", "qa", "pb", "qb", "c", "d",
    "t0", "t1", "t2", "u", "v", "x", "y0", "y1", "y2",
)
R = ("t0", "t1", "t2")
A_OPEN = frozenset(("a", "b", "pa", "qa", "pb", "qb"))
B_OPEN = frozenset(("c", "d", "y0", "y1", "y2"))
S = frozenset(R + ("ap", "u", "bp", "v", "x"))
E_BOUNDARY = frozenset(("ap", "u"))
F_BOUNDARY = frozenset(("bp", "v"))
G_EDGE = tuple(sorted(("a", "b")))
H_EDGE = tuple(sorted(("c", "d")))


def edge(x, y):
    return tuple(sorted((x, y)))


# These are respectively colourings of G-h, G-{g,h}, and G-g.  They are
# also used to define a compact deterministic edge-saturation construction.
TARGET_PE = {
    "a": 0, "b": 1, "ap": 0, "bp": 1, "pa": 1, "qa": 2,
    "pb": 0, "qb": 2, "c": 2, "d": 2, "t0": 3, "t1": 4,
    "t2": 5, "u": 4, "v": 4, "x": 3, "y0": 1, "y1": 3,
    "y2": 0,
}
TARGET_EE = {
    "a": 0, "b": 0, "ap": 0, "bp": 0, "pa": 1, "qa": 2,
    "pb": 1, "qb": 2, "c": 2, "d": 2, "t0": 3, "t1": 4,
    "t2": 5, "u": 5, "v": 4, "x": 5, "y0": 0, "y1": 3,
    "y2": 1,
}
TARGET_EP = {
    "a": 0, "b": 0, "ap": 0, "bp": 0, "pa": 1, "qa": 2,
    "pb": 1, "qb": 2, "c": 2, "d": 1, "t0": 3, "t1": 4,
    "t2": 5, "u": 5, "v": 5, "x": 5, "y0": 0, "y1": 3,
    "y2": 4,
}


def make_graph():
    edges = set()

    # Two K4-minus-an-edge equality gadgets.
    for z, zp, p, q in (
        ("a", "ap", "pa", "qa"),
        ("b", "bp", "pb", "qb"),
    ):
        edges.add(edge(p, q))
        for w in (z, zp):
            edges.add(edge(w, p))
            edges.add(edge(w, q))
    for z in ("c", "d"):
        edges.add(edge(z, "ap"))
        edges.add(edge(z, "bp"))

    edges.update((G_EDGE, H_EDGE))

    # The original K5 has vertex set R union {a,b}.
    for p, q in combinations(R, 2):
        edges.add(edge(p, q))
    for r in R:
        for z in ("a", "b", "ap", "bp", "pa", "qa", "pb", "qb", "c", "d"):
            edges.add(edge(r, z))

    # Boundary defect edges and minimum full-shore contacts.
    edges.add(edge("ap", "u"))
    edges.add(edge("bp", "v"))
    edges.update((edge("u", "b"), edge("u", "c")))
    edges.update((edge("v", "a"), edge("v", "d")))
    edges.update((edge("x", "a"), edge("x", "c")))

    # The second K5 has vertex set {c,d,y0,y1,y2}.
    for p, q in combinations(("c", "d", "y0", "y1", "y2"), 2):
        edges.add(edge(p, q))

    forbidden = {
        edge("ap", "bp"), edge("ap", "v"), edge("u", "bp"), edge("u", "v"),
        edge("a", "ap"), edge("a", "u"), edge("b", "bp"), edge("b", "v"),
    }
    for p in A_OPEN:
        for q in B_OPEN:
            forbidden.add(edge(p, q))

    # Add every remaining edge which is proper in all three displayed
    # response colourings.  The two restored critical edges were inserted
    # separately above because one or both are monochromatic in each target.
    targets = (TARGET_PE, TARGET_EE, TARGET_EP)
    for p, q in combinations(VERTICES, 2):
        pq = edge(p, q)
        if pq not in forbidden and all(col[p] != col[q] for col in targets):
            edges.add(pq)

    # These six omissions enforce the live endpoint-rigidity and leaf-side
    # boundary-contact patterns.
    edges.discard(edge("ap", "t0"))
    edges.discard(edge("bp", "t0"))
    for z in ("pa", "qa", "pb", "qb"):
        edges.discard(edge("t2", z))

    return frozenset(edges)


def adjacency(vertices, edges):
    out = {v: set() for v in vertices}
    for p, q in edges:
        out[p].add(q)
        out[q].add(p)
    return out


def is_proper(colouring, edges):
    return all(colouring[p] != colouring[q] for p, q in edges)


def enumerate_colourings(vertices, edges, colours, fixed=None, limit=None):
    vertices = tuple(vertices)
    adj = adjacency(vertices, edges)
    assignment = {} if fixed is None else dict(fixed)
    for p, q in edges:
        if p in assignment and q in assignment and assignment[p] == assignment[q]:
            return []
    out = []

    def search():
        if len(assignment) == len(vertices):
            out.append(tuple(assignment[v] for v in vertices))
            return limit is not None and len(out) >= limit
        unassigned = [v for v in vertices if v not in assignment]
        v = max(
            unassigned,
            key=lambda z: (
                len({assignment[w] for w in adj[z] if w in assignment}),
                len(adj[z]),
                z,
            ),
        )
        forbidden = {assignment[w] for w in adj[v] if w in assignment}
        for colour in range(colours):
            if colour not in forbidden:
                assignment[v] = colour
                if search():
                    return True
                del assignment[v]
        return False

    search()
    return out


def colour_dict(colouring):
    return dict(zip(VERTICES, colouring))


def boundary_partition(colouring):
    c = colour_dict(colouring)
    blocks = []
    for colour in sorted(set(c.values())):
        block = tuple(sorted(v for v in S if c[v] == colour))
        if block:
            blocks.append(block)
    return tuple(sorted(blocks))


def signature(colouring):
    c = colour_dict(colouring)
    return (c["a"] == c["b"], c["c"] == c["d"])


def connected(vertices, edges):
    vertices = set(vertices)
    if len(vertices) <= 1:
        return True
    adj = adjacency(VERTICES, edges)
    root = next(iter(vertices))
    seen = {root}
    queue = [root]
    while queue:
        v = queue.pop()
        for w in adj[v] & vertices:
            if w not in seen:
                seen.add(w)
                queue.append(w)
    return seen == vertices


def connected_after_deleting(edges, deleted):
    return connected(set(VERTICES) - set(deleted), edges)


def kempe_neighbours(colouring, edges):
    c = colour_dict(colouring)
    adj = adjacency(VERTICES, edges)
    neighbours = set()
    for alpha, beta in combinations(range(6), 2):
        remaining = {v for v in VERTICES if c[v] in (alpha, beta)}
        while remaining:
            root = min(remaining)
            component = {root}
            queue = [root]
            remaining.remove(root)
            while queue:
                v = queue.pop()
                for w in adj[v] & remaining:
                    remaining.remove(w)
                    component.add(w)
                    queue.append(w)
            switched = dict(c)
            for v in component:
                switched[v] = beta if c[v] == alpha else alpha

            # Normalize the triangle colours back to 0,1,2.  Its vertices
            # have distinct colours in every proper colouring.
            relabel = {switched["t0"]: 0, switched["t1"]: 1, switched["t2"]: 2}
            next_colour = 3
            for value in range(6):
                if value not in relabel:
                    relabel[value] = next_colour
                    next_colour += 1
            neighbours.add(tuple(relabel[switched[v]] for v in VERTICES))
    return neighbours


def bichromatic_component(colouring, edges, side, root, alpha, beta):
    c = colour_dict(colouring)
    adj = adjacency(VERTICES, edges)
    allowed = {v for v in side if c[v] in (alpha, beta)}
    seen = {root}
    queue = [root]
    while queue:
        v = queue.pop()
        for w in adj[v] & allowed:
            if w not in seen:
                seen.add(w)
                queue.append(w)
    return seen


def list_colourable(vertices, edges, lists):
    vertices = set(vertices)
    adj = adjacency(VERTICES, edges)
    assignment = {}

    def search():
        if len(assignment) == len(vertices):
            return True
        v = min(
            vertices - set(assignment),
            key=lambda z: (len(lists[z]), -len(adj[z] & vertices), z),
        )
        used = {assignment[w] for w in adj[v] & set(assignment)}
        for colour in sorted(lists[v] - used):
            assignment[v] = colour
            if search():
                return True
            del assignment[v]
        return False

    return search()


def verify_branch_sets(edges, branch_sets):
    assert all(connected(branch, edges) for branch in branch_sets)
    assert sum(len(branch) for branch in branch_sets) == len(set().union(*map(set, branch_sets)))
    for i, j in combinations(range(len(branch_sets)), 2):
        assert any(edge(p, q) in edges for p in branch_sets[i] for q in branch_sets[j])


def main():
    full = make_graph()
    minus_g = full - {G_EDGE}
    minus_h = full - {H_EDGE}
    common = full - {G_EDGE, H_EDGE}
    assert len(full) == 105

    # Exact balanced order-eight geometry.
    assert set(VERTICES) == set(A_OPEN) | set(S) | set(B_OPEN)
    assert not any(
        (p in A_OPEN and q in B_OPEN) or (q in A_OPEN and p in B_OPEN)
        for p, q in full
    )
    assert connected(A_OPEN, full) and connected(B_OPEN, full)
    adj = adjacency(VERTICES, full)
    for shore in (A_OPEN, B_OPEN):
        assert all(any(w in adj[s] for w in shore) for s in S)

    # Exhaustive vertex-connectivity check; S itself is an eight-cut.
    for size in range(8):
        for deleted in combinations(VERTICES, size):
            assert connected_after_deleting(full, deleted)
    assert not connected_after_deleting(full, S)

    assert all(edge(p, q) in full for p, q in combinations(R, 2))
    assert edge("ap", "u") in full and edge("bp", "v") in full
    assert all(edge(p, q) not in full for p in E_BOUNDARY for q in F_BOUNDARY)

    # Defect-edge incidences for L=R union {a,b}.
    assert all(edge("a", z) not in full for z in E_BOUNDARY)
    assert all(edge("b", z) not in full for z in F_BOUNDARY)
    assert any(edge("b", z) in full for z in E_BOUNDARY)
    assert any(edge("a", z) in full for z in F_BOUNDARY)
    for r in R:
        assert any(edge(r, z) in full for z in E_BOUNDARY)
        assert any(edge(r, z) in full for z in F_BOUNDARY)

    # Endpoint rigidity: the two nonneighbour sets in R are nonempty and
    # disjoint for each boundary edge.
    for pair in (E_BOUNDARY, F_BOUNDARY):
        p, q = sorted(pair)
        miss_p = {r for r in R if edge(p, r) not in full}
        miss_q = {r for r in R if edge(q, r) not in full}
        assert miss_p and miss_q and miss_p.isdisjoint(miss_q)

    L = frozenset(R + ("a", "b"))
    Y = frozenset(("c", "d", "y0", "y1", "y2"))
    assert L.isdisjoint(Y)
    assert all(edge(p, q) in full for p, q in combinations(L, 2))
    assert all(edge(p, q) in full for p, q in combinations(Y, 2))

    leaf_remainder = frozenset(("pa", "qa", "pb", "qb"))
    assert connected(leaf_remainder, full)
    assert {s for s in S if adj[s] & leaf_remainder} == set(S) - {"t2"}

    # A perfect matching in the complement of the boundary graph.
    complement_matching = (
        edge("t0", "x"), edge("t1", "u"), edge("t2", "v"), edge("ap", "bp")
    )
    assert all(pq not in full for pq in complement_matching)
    assert set().union(*(set(pq) for pq in complement_matching)) == set(S)

    # Exact chromatic and response data.  Fixing the triangle colours loses
    # no colouring because any colouring can be globally relabelled.
    fixed = {"t0": 0, "t1": 1, "t2": 2}
    assert not enumerate_colourings(VERTICES, full, 6, fixed=fixed, limit=1)
    assert is_proper(TARGET_PE, minus_h)
    assert is_proper(TARGET_EE, common)
    assert is_proper(TARGET_EP, minus_g)
    seven_colouring = {
        "a": 5, "b": 4, "ap": 5, "bp": 4, "pa": 4, "qa": 3,
        "pb": 5, "qb": 3, "c": 3, "d": 6, "t0": 0, "t1": 1,
        "t2": 2, "u": 1, "v": 1, "x": 0, "y0": 4, "y1": 0,
        "y2": 5,
    }
    assert is_proper(seven_colouring, full)

    cg = enumerate_colourings(VERTICES, minus_g, 6, fixed=fixed)
    ch = enumerate_colourings(VERTICES, minus_h, 6, fixed=fixed)
    cc = enumerate_colourings(VERTICES, common, 6, fixed=fixed)
    assert (len(cg), len(ch), len(cc)) == (24, 342, 792)
    assert {signature(c) for c in cc} == {
        (True, True), (True, False), (False, True)
    }
    assert sum(signature(c) == (True, False) for c in cc) == 24
    assert sum(signature(c) == (False, True) for c in cc) == 342
    assert sum(signature(c) == (True, True) for c in cc) == 426

    partitions_g = {boundary_partition(c) for c in cg}
    partitions_h = {boundary_partition(c) for c in ch}
    assert (len(partitions_g), len(partitions_h)) == (2, 12)
    assert partitions_g.isdisjoint(partitions_h)

    # A simultaneous-equality colouring whose boundary partition is not
    # returned by either one-edge restoration.
    witness_map = {
        "a": 3, "b": 3, "ap": 3, "bp": 3, "pa": 2, "qa": 4,
        "pb": 2, "qb": 4, "c": 4, "d": 4, "t0": 0, "t1": 1,
        "t2": 2, "u": 5, "v": 5, "x": 0, "y0": 3, "y1": 0,
        "y2": 1,
    }
    assert is_proper(witness_map, common)
    witness = tuple(witness_map[v] for v in VERTICES)
    assert signature(witness) == (True, True)
    assert boundary_partition(witness) == tuple(sorted((
        ("ap", "bp"), ("t0", "x"), ("t1",), ("t2",), ("u", "v")
    )))
    assert boundary_partition(witness) not in partitions_g | partitions_h

    # Exact local boundary-lock certificate.  For g all alternate palettes
    # are locked except colour 5; there the two endpoint components both hit
    # S.  For h every alternate palette is locked.
    side_a = set(A_OPEN) | set(S)
    side_b = set(B_OPEN) | set(S)
    for beta in (0, 1, 2, 4):
        ca = bichromatic_component(witness, common, side_a, "a", 3, beta)
        assert "b" in ca
    ca = bichromatic_component(witness, common, side_a, "a", 3, 5)
    cb = bichromatic_component(witness, common, side_a, "b", 3, 5)
    assert ca.isdisjoint(cb)
    assert ca & set(S) == {"bp", "v"}
    assert cb & set(S) == {"ap", "u"}
    for beta in (0, 1, 2, 3, 5):
        cc_component = bichromatic_component(witness, common, side_b, "c", 4, beta)
        assert "d" in cc_component

    # The open A-shore is planar: it is the octahedral graph
    # \bar K_2 join C4 with one rim edge removed, equivalently
    # \bar K_2 join P4.  Its selected minimal fixed-boundary list-critical
    # core is not a Gallai tree.
    path = ("pa", "a", "b", "pb")
    hubs = ("qa", "qb")
    expected_a_edges = {edge(path[i], path[i + 1]) for i in range(3)}
    expected_a_edges |= {edge(hub, z) for hub in hubs for z in path}
    assert {pq for pq in full if set(pq) <= set(A_OPEN)} == expected_a_edges

    lists = {
        z: set(range(6)) - {witness_map[s] for s in adj[z] & set(S)}
        for z in A_OPEN
    }
    critical_core = {"a", "b", "pa", "pb", "qa"}
    assert {z: lists[z] for z in critical_core} == {
        "a": {3, 4}, "b": {3, 4},
        "pa": {2, 4}, "pb": {2, 4}, "qa": {2, 4},
    }
    assert not list_colourable(critical_core, full, lists)
    assert all(list_colourable(critical_core - {z}, full, lists) for z in critical_core)
    assert list_colourable(critical_core, full - {G_EDGE}, lists)

    # The core is one 2-connected block but is neither a clique nor an odd
    # cycle, so it is not a Gallai tree.
    assert all(connected(critical_core - {z}, full) for z in critical_core)
    core_degrees = {
        z: len(adj[z] & critical_core) for z in critical_core
    }
    assert core_degrees == {"a": 3, "b": 3, "pa": 2, "pb": 2, "qa": 4}
    assert any(core_degrees[z] != len(lists[z]) for z in critical_core)

    # No single Kempe interchange joins the two one-edge response families.
    cg_set = set(cg)
    assert not any(kempe_neighbours(c, common) & cg_set for c in ch)

    # The common deletion is exactly six-chromatic and has an explicit K6
    # minor model.
    assert not enumerate_colourings(VERTICES, common, 5, fixed=fixed, limit=1)
    k6_branch_sets = [
        {"t0"}, {"t1"}, {"t2"},
        {"a", "pa", "ap"},
        {"b", "pb", "bp", "qa", "qb"},
        {"c", "y0", "d"},
    ]
    verify_branch_sets(common, k6_branch_sets)

    # Exact trust boundary: a K7 model is explicit, the graph is not
    # minor-minimal, and the canonical missing linkage is present.
    branch_sets = [
        {"t0"}, {"t1"}, {"t2"},
        {"a", "pa", "ap"}, {"b", "pb", "bp"}, {"c"}, {"d"},
    ]
    verify_branch_sets(full, branch_sets)

    remaining = tuple(v for v in VERTICES if v != "u")
    remaining_edges = frozenset(pq for pq in full if "u" not in pq)
    assert not enumerate_colourings(remaining, remaining_edges, 6, fixed=fixed, limit=1)

    # After contracting ap-u to z_e and bp-v to z_f and deleting R, these
    # are two disjoint same-index paths: a-x-z_e and b-qa-z_f.
    assert edge("a", "x") in full and edge("x", "ap") in full
    assert edge("b", "qa") in full and edge("qa", "bp") in full

    print("balanced order-eight double-equality lock barrier: verified")
    print("vertices=19 edges=105 connectivity=8 chromatic_number=7")
    print("fixed-triangle six-colourings: G-g=24 G-h=342 H=792")
    print("response partitions: 2 versus 12, with empty intersection")
    print("planar leaf side: minimal fixed-boundary core is not a Gallai tree")
    print("trust boundary: contains K7; non-minimal; canonical missing linkage fails")


if __name__ == "__main__":
    main()
