#!/usr/bin/env python3
"""Verify an exact-seven, same-shore three-response barrier.

The graph deliberately contains a K7 minor and is not minor-minimal.  The
certificate isolates what the exact boundary, packet vector, demand, and
three deletion/contraction responses do not prove without those two global
HC7 hypotheses.
"""

from itertools import combinations


CORE = ("a", "b", "ap", "bp", "pa", "qa", "pb", "qb", "c", "d")
TRIANGLE = ("t0", "t1", "t2")
TWINS = ("w0", "w1")
ELL = "ell"
VERTICES = CORE + TRIANGLE + TWINS + (ELL,)

E = tuple(sorted(("a", "b")))
F = tuple(sorted(("c", "d")))
OPEN_A = frozenset(("a", "ap", "bp", "pa", "qa", "pb", "qb", "c"))
BOUNDARY = frozenset(("b", "d") + TRIANGLE + TWINS)
OPEN_B = frozenset((ELL,))


def edge(x, y):
    assert x != y
    return tuple(sorted((x, y)))


def core_edges(include_e=True, include_f=True):
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
    if include_e:
        edges.add(E)
    if include_f:
        edges.add(F)
    return frozenset(edges)


def host_edges(include_e=True, include_f=True):
    edges = set(core_edges(include_e, include_f))
    for x, y in combinations(TRIANGLE, 2):
        edges.add(edge(x, y))
    for u in TRIANGLE + TWINS:
        for v in CORE:
            edges.add(edge(u, v))
    for w in TWINS:
        edges.add(edge(w, "t1"))
        edges.add(edge(w, "t2"))
    for s in BOUNDARY:
        edges.add(edge(ELL, s))
    return frozenset(edges)


def adjacency(vertices, edges):
    out = {v: set() for v in vertices}
    for x, y in edges:
        if x in out and y in out:
            out[x].add(y)
            out[y].add(x)
    return out


def connected(vertices, edges):
    vertices = set(vertices)
    if not vertices:
        return False
    adj = adjacency(vertices, edges)
    reached = {next(iter(vertices))}
    stack = list(reached)
    while stack:
        v = stack.pop()
        for w in adj[v] - reached:
            reached.add(w)
            stack.append(w)
    return reached == vertices


def connected_after_deleting(edges, deleted):
    remaining = set(VERTICES) - set(deleted)
    return len(remaining) <= 1 or connected(remaining, edges)


def colourings(vertices, edges, colours):
    adj = adjacency(vertices, edges)
    order = sorted(vertices, key=lambda v: (-len(adj[v]), v))
    assignment = {}
    output = []

    def search(i):
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


def signature(colouring):
    return (
        "equal" if colouring["a"] == colouring["b"] else "proper",
        "equal" if colouring["c"] == colouring["d"] else "proper",
    )


def lifted_colouring(core_colouring):
    result = dict(core_colouring)
    result.update({"t0": 3, "t1": 4, "t2": 5, "w0": 3, "w1": 3})
    unused_at_boundary = {0, 1, 2} - {result["b"], result["d"]}
    assert len(unused_at_boundary) == 1
    result[ELL] = unused_at_boundary.pop()
    return result


def proper(colouring, edges):
    return all(colouring[x] != colouring[y] for x, y in edges)


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
            chosen = set(subset)
            if not connected(chosen, edges):
                continue
            if all(any(edge(v, s) in edges for v in chosen) for s in BOUNDARY):
                output.append(frozenset(chosen))
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
    vertices = tuple(vertices)
    for size in range(len(vertices), 0, -1):
        for chosen in combinations(vertices, size):
            if all(edge(x, y) in edges for x, y in combinations(chosen, 2)):
                return size
    return 0


def main():
    full = host_edges()
    minus_e = host_edges(include_e=False)
    minus_f = host_edges(include_f=False)
    common = host_edges(include_e=False, include_f=False)

    assert set(VERTICES) == OPEN_A | BOUNDARY | OPEN_B
    assert not (OPEN_A & BOUNDARY or OPEN_A & OPEN_B or BOUNDARY & OPEN_B)
    assert not any(
        (x in OPEN_A and y in OPEN_B) or (x in OPEN_B and y in OPEN_A)
        for x, y in full
    )
    assert E[0] in OPEN_A and E[1] in BOUNDARY
    assert F[0] in OPEN_A and F[1] in BOUNDARY
    assert connected(OPEN_A, full) and connected(OPEN_B, full)
    for shore in (OPEN_A, OPEN_B):
        for s in BOUNDARY:
            assert any(edge(v, s) in full for v in shore)

    # Exact seven-connectivity and the displayed actual separation.
    for size in range(7):
        for deleted in combinations(VERTICES, size):
            assert connected_after_deleting(full, deleted)
    assert not connected_after_deleting(full, BOUNDARY)

    full_a = connected_full_subsets(OPEN_A, full)
    full_b = connected_full_subsets(OPEN_B, full)
    assert packing_number(full_a) == 2
    assert packing_number(full_b) == 1

    # The core has the exact EE/EP/PE chamber profile.
    core_common = colourings(CORE, core_edges(False, False), 3)
    assert core_common
    assert {signature(c) for c in core_common} == {
        ("equal", "equal"),
        ("equal", "proper"),
        ("proper", "equal"),
    }
    assert not colourings(CORE, core_edges(), 3)
    assert colourings(CORE, core_edges(), 4)

    response_partitions = set()
    for core_colouring in core_common:
        colouring = lifted_colouring(core_colouring)
        assert proper(colouring, common)
        response_partitions.add(boundary_partition(colouring))
    expected_partition = frozenset(
        (
            frozenset(("t0", "w0", "w1")),
            frozenset(("t1",)),
            frozenset(("t2",)),
            frozenset(("b",)),
            frozenset(("d",)),
        )
    )
    assert response_partitions == {expected_partition}

    # Each one-edge response and the double-contraction response is exact.
    for core_colouring in colourings(CORE, core_edges(False, True), 3):
        assert signature(core_colouring) == ("equal", "proper")
        assert proper(lifted_colouring(core_colouring), minus_e)
    for core_colouring in colourings(CORE, core_edges(True, False), 3):
        assert signature(core_colouring) == ("proper", "equal")
        assert proper(lifted_colouring(core_colouring), minus_f)

    # T plus the left diamond triangle is a literal K6 in all response hosts.
    literal_k6 = set(TRIANGLE) | {"a", "pa", "qa"}
    assert all(edge(x, y) in common for x, y in combinations(literal_k6, 2))

    # The boundary is four-colourable, and the selected five-block response
    # has full-subgraph demand 5-3=2 > nu_B=1.
    boundary_edges = {
        edge(x, y) for x, y in full if x in BOUNDARY and y in BOUNDARY
    }
    assert colourings(tuple(BOUNDARY), boundary_edges, 4)
    assert not colourings(tuple(BOUNDARY), boundary_edges, 3)
    singleton_vertices = {next(iter(block)) for block in expected_partition if len(block) == 1}
    demand = len(expected_partition) - clique_number(singleton_vertices, boundary_edges)
    assert demand == 2 > packing_number(full_b)

    # The singleton shore realizes the selected response: ell receives the
    # sixth colour absent from the five boundary blocks.  The intact A-side
    # rejects it (indeed T join J is seven-chromatic).
    for core_colouring in core_common:
        assert proper(lifted_colouring(core_colouring), common)
    assert not colourings(tuple(OPEN_A | BOUNDARY), full, 6)

    # Explicit terminal deliberately omitted by the proposed local inference.
    k7_bags = [{t} for t in TRIANGLE] + [
        {"a", "pa", "ap"},
        {"b", "pb", "bp"},
        {"c"},
        {"d"},
    ]
    assert len(k7_bags) == 7
    for bag in k7_bags:
        assert connected(bag, full)
    for left, right in combinations(k7_bags, 2):
        assert any(edge(x, y) in full for x in left for y in right)

    print("GREEN exact-seven crossing three-chamber barrier")
    print("kappa=7 boundary=7 chi_boundary=4 packing=(2,1)")
    print("two vertex-disjoint boundary-to-shore edges; chambers=EE,EP,PE; PP absent")
    print("all chambers induce one five-block boundary partition of demand=2>1")
    print("opposite singleton shore accepts the partition; intact operated shore rejects it")
    print("common response host contains K6; full host contains K7 minor")


if __name__ == "__main__":
    main()
