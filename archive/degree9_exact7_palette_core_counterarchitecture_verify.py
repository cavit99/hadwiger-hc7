#!/usr/bin/env python3
"""Independent graph-level audit of the exact-seven palette-core barrier.

The graph has the ordered boundary r,a1,...,a6 and two open K6 shores.
It is not six-colourable.  Every deletion or contraction of an edge with
an interior end, and every interior-vertex deletion, is six-colourable.
For every portal-edge deletion the deleted ends coincide in colour and
the interior end sees all other five colours.  Both shores are connected
and full.  The graph deliberately has a K7 minor and connectivity five;
it is a sharp warning, not an HC7 counterexample.
"""

from __future__ import annotations

from itertools import combinations


P = (32, 52, 60, 40, 35, 52, 40)
Q = (59, 21, 27, 8, 10, 34, 51)
S = ("r", "a1", "a2", "a3", "a4", "a5", "a6")
INTERIOR = tuple(f"p{i}" for i in range(6)) + tuple(f"q{i}" for i in range(6))


def build():
    vertices = set(S) | set(INTERIOR)
    edges = set()

    def add(x, y):
        assert x != y
        edges.add(frozenset((x, y)))

    for i in range(1, 6):
        add(S[i], S[i + 1])
    for i in range(2, 7):
        add("r", S[i])
    for side, masks in (("p", P), ("q", Q)):
        core = tuple(f"{side}{j}" for j in range(6))
        for x, y in combinations(core, 2):
            add(x, y)
        for i, mask in enumerate(masks):
            for j in range(6):
                if mask >> j & 1:
                    add(S[i], core[j])
    return vertices, edges


def adjacency(vertices, edges):
    out = {v: set() for v in vertices}
    for e in edges:
        x, y = tuple(e)
        out[x].add(y)
        out[y].add(x)
    return out


def six_colouring(vertices, edges, precolour=None):
    adj = adjacency(vertices, edges)
    colour = dict(precolour or {})
    if any(colour[x] == colour[y] for e in edges
           for x, y in [tuple(e)] if x in colour and y in colour):
        return None

    def rec(max_used):
        if len(colour) == len(vertices):
            return dict(colour)
        uncoloured = [v for v in vertices if v not in colour]
        v = max(uncoloured, key=lambda x: (len({colour[y] for y in adj[x] if y in colour}), len(adj[x]), x))
        blocked = {colour[y] for y in adj[v] if y in colour}
        upper = min(5, max_used + 1)
        for c in range(upper + 1):
            if c in blocked:
                continue
            colour[v] = c
            ans = rec(max(max_used, c))
            if ans is not None:
                return ans
            del colour[v]
        return None

    return rec(max(colour.values(), default=-1))


def set_partitions(items):
    blocks = []

    def rec(i):
        if i == len(items):
            yield tuple(tuple(b) for b in blocks)
            return
        x = items[i]
        for block in blocks:
            block.append(x)
            yield from rec(i + 1)
            block.pop()
        blocks.append([x])
        yield from rec(i + 1)
        blocks.pop()

    yield from rec(0)


def boundary_signature(vertices, edges, side):
    core = {f"{side}{j}" for j in range(6)}
    vv = set(S) | core
    ee = {e for e in edges if e <= vv}
    sig = set()
    for pi in set_partitions(S):
        if len(pi) > 6:
            continue
        pre = {x: i for i, block in enumerate(pi) for x in block}
        if six_colouring(vv, ee, pre) is not None:
            sig.add(pi)
    return sig


def contract(vertices, edges, keep, lose):
    assert frozenset((keep, lose)) in edges
    vv = set(vertices)
    vv.remove(lose)
    ee = set()
    for e in edges:
        x, y = tuple(e)
        x = keep if x == lose else x
        y = keep if y == lose else y
        if x != y:
            ee.add(frozenset((x, y)))
    return vv, ee


def connected_after_delete(vertices, edges, deleted):
    remain = set(vertices) - set(deleted)
    if len(remain) <= 1:
        return True
    adj = adjacency(vertices, edges)
    start = next(iter(remain))
    reached = {start}
    todo = [start]
    while todo:
        x = todo.pop()
        for y in adj[x] & remain - reached:
            reached.add(y)
            todo.append(y)
    return reached == remain


def verify_connectivity_five(vertices, edges):
    for k in range(5):
        for cut in combinations(vertices, k):
            assert connected_after_delete(vertices, edges, cut), cut
    cut = {"p2", "p3", "p4", "p5", "a4"}
    assert not connected_after_delete(vertices, edges, cut)


def adjacent_bags(a, b, edges):
    return any(frozenset((x, y)) in edges for x in a for y in b if x != y)


def connected_bag(bag, edges):
    bag = set(bag)
    if not bag:
        return False
    vertices = set().union(*map(set, edges))
    return connected_after_delete(vertices, edges, vertices - bag)


def verify_k7(vertices, edges):
    model = [
        {"r"}, {"a2"}, {"a3"}, {"p5"},
        {"a6", "p3"}, {"a4", "q1"}, {"a1", "q0", "q3"},
    ]
    assert all(connected_bag(b, edges) for b in model)
    assert len(set().union(*model)) == sum(map(len, model))
    assert all(adjacent_bags(a, b, edges) for a, b in combinations(model, 2))


def main():
    vertices, edges = build()
    sig_p = boundary_signature(vertices, edges, "p")
    sig_q = boundary_signature(vertices, edges, "q")
    assert len(sig_p) == 32 and len(sig_q) == 9
    assert sig_p.isdisjoint(sig_q)
    assert six_colouring(vertices, edges) is None

    # Full connected open shores.
    for side in ("p", "q"):
        core = {f"{side}{j}" for j in range(6)}
        assert connected_bag(core, edges)
        assert all(any(frozenset((x, y)) in edges for y in core) for x in S)

    operated = [e for e in edges if e & set(INTERIOR)]
    for e in operated:
        x, y = tuple(e)
        deleted = edges - {e}
        c = six_colouring(vertices, deleted)
        assert c is not None, ("delete", e)
        assert c[x] == c[y], ("endpoint equality", e)

        # Keep the boundary label under a portal contraction.
        if x in S:
            keep, lose = x, y
        elif y in S:
            keep, lose = y, x
        else:
            keep, lose = x, y
        cv, ce = contract(vertices, edges, keep, lose)
        assert six_colouring(cv, ce) is not None, ("contract", e)

        if (x in S) != (y in S):
            u, portal = (y, x) if x in S else (x, y)
            other_colours = {c[z] for z in adjacency(vertices, edges)[u] - {portal}}
            assert other_colours == set(range(6)) - {c[u]}, (e, c[u], other_colours)

    for z in INTERIOR:
        vv = vertices - {z}
        ee = {e for e in edges if z not in e}
        assert six_colouring(vv, ee) is not None, ("vertex delete", z)

    verify_connectivity_five(vertices, edges)
    verify_k7(vertices, edges)
    print("connected/full K6 shores: PASS")
    print("boundary signatures 32 and 9, disjoint: PASS")
    print("all interior/portal deletions and contractions: PASS")
    print("all interior vertex deletions: PASS")
    print("portal endpoint equality and five-colour fans: PASS")
    print("connectivity exactly five; explicit K7 model: PASS")


if __name__ == "__main__":
    main()
