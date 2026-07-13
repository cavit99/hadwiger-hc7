#!/usr/bin/env python3
"""Search small all-crossless pentagram shores for critical transitions.

Discovery aid.  The first target is the six-vertex odd wheel.  The five
root labels are ordered along the *missing* C5; labels 5,6 are w,a.
"""

from __future__ import annotations

import itertools


N = 6
D = tuple(range(N))
HUB = 5
U = tuple(range(5))
W, A = 5, 6
L = tuple(range(7))
INT = {
    tuple(sorted((i, (i + 1) % 5))) for i in range(5)
} | {(i, HUB) for i in range(5)}
MISSING = {tuple(sorted((i, (i + 1) % 5))) for i in range(5)}
BOUNDARY = {
    (i, j) for i, j in itertools.combinations(U, 2)
    if (i, j) not in MISSING
} | {(A, x) if A < x else (x, A) for x in (0, 2, 4)}


def connected(xs: frozenset[int]) -> bool:
    if not xs:
        return False
    seen = {next(iter(xs))}
    stack = list(seen)
    while stack:
        x = stack.pop()
        for e in INT:
            if x not in e:
                continue
            y = next(iter(set(e) - {x}))
            if y in xs and y not in seen:
                seen.add(y)
                stack.append(y)
    return seen == set(xs)


CONN = [frozenset(x for x in D if mask >> x & 1)
        for mask in range(1, 1 << N)]
CONN = [x for x in CONN if connected(x)]


def linked(rows: tuple[int, ...], frame: int) -> bool:
    a, b = (frame + 1) % 5, (frame + 2) % 5
    c, d = (frame + 3) % 5, (frame + 4) % 5
    pa = {x for x in D if rows[x] >> a & 1}
    pb = {x for x in D if rows[x] >> b & 1}
    pc = {x for x in D if rows[x] >> c & 1}
    pd = {x for x in D if rows[x] >> d & 1}
    xsets = [x for x in CONN if x & pa and x & pb]
    ysets = [x for x in CONN if x & pc and x & pd]
    return any(x.isdisjoint(y) for x in xsets for y in ysets)


def cut_ok(rows: tuple[int, ...]) -> bool:
    if set().union(*({j for j in L if rows[x] >> j & 1} for x in D)) != set(L):
        return False
    for mask in range(1, (1 << N) - 1):
        x = {i for i in D if mask >> i & 1}
        inner = {v for e in INT for v in e if v not in x and any(u in x for u in e)}
        labels = {j for i in x for j in L if rows[i] >> j & 1}
        if len(inner) + len(labels) < 7:
            return False
    return True


def search() -> None:
    # Pair-profile core.  The wrapper
    # pentagram_critical_web_fullprofile_probe.py separately adds every exact
    # triple-lock profile and its required singleton shield.
    pairs = tuple(sum(1 << i for i in pair) for pair in itertools.combinations(U, 2))
    base = (1 << W) | (1 << A)
    found = 0
    for choices in itertools.product(pairs, repeat=5):
        if set().union(*({j for j in U if choices[x] >> j & 1} for x in range(5))) != set(U):
            continue
        rows = tuple(base | choices[x] for x in range(5)) + (base,)
        if not cut_ok(rows):
            continue
        bad = tuple(i for i in U if linked(rows, i))
        if bad:
            continue
        print("all-crossless", tuple(f"{r:07b}" for r in rows))
        transition_report(rows)
        found += 1
    assert found == 10, found
    print("found", found)


def partitions(items: tuple[int, ...]):
    blocks: list[list[int]] = []

    def rec(i: int):
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


def boundary_adjacent(x: int, y: int) -> bool:
    return tuple(sorted((x, y))) in BOUNDARY


def independent_state(state: tuple[tuple[int, ...], ...]) -> bool:
    return len(state) <= 6 and all(
        not boundary_adjacent(x, y)
        for block in state for x, y in itertools.combinations(block, 2)
    )


def extends(rows: tuple[int, ...], state: tuple[tuple[int, ...], ...], *,
            delete_vertex: int | None = None,
            delete_edge: tuple[int, int] | None = None,
            contract_edge: tuple[int, int] | None = None) -> bool:
    vertices = [x for x in D if x != delete_vertex]
    edges = set(INT)
    if delete_edge is not None:
        edges.discard(delete_edge)
    if contract_edge is not None:
        edges.discard(contract_edge)
    color: dict[tuple[str, int], int] = {}
    for c, block in enumerate(state):
        for x in block:
            color[("l", x)] = c
    if any(color[("l", x)] == color[("l", y)] for x, y in BOUNDARY):
        return False

    def compatible(x: int, c: int) -> bool:
        if contract_edge is not None and x in contract_edge:
            other = contract_edge[0] if x == contract_edge[1] else contract_edge[1]
            if ("d", other) in color and color[("d", other)] != c:
                return False
        for y in vertices:
            if ("d", y) in color and tuple(sorted((x, y))) in edges and color[("d", y)] == c:
                return False
        return all(
            color.get(("l", j)) != c for j in L if rows[x] >> j & 1
        )

    def dfs(left: tuple[int, ...]) -> bool:
        if not left:
            return contract_edge is None or color[("d", contract_edge[0])] == color[("d", contract_edge[1])]
        x = max(left, key=lambda z: sum(tuple(sorted((z, y))) in edges for y in vertices))
        rest = tuple(y for y in left if y != x)
        if contract_edge is not None and x in contract_edge:
            other = contract_edge[0] if x == contract_edge[1] else contract_edge[1]
            choices = (color[("d", other)],) if ("d", other) in color else range(6)
        else:
            choices = range(6)
        for c in choices:
            if compatible(x, c):
                color[("d", x)] = c
                if dfs(rest):
                    return True
                del color[("d", x)]
        return False

    return dfs(tuple(vertices))


def decorated_states() -> set[tuple[tuple[int, ...], ...]]:
    out = set()
    for j in U:
        e = {(j + 1) % 5, (j + 2) % 5}
        f = {(j + 3) % 5, (j + 4) % 5}
        r = {j}
        base = [e, f, r, {A}]
        for pos in range(5):
            blocks = [set(x) for x in base]
            if pos < 4:
                blocks[pos].add(W)
            else:
                blocks.append({W})
            # canonical restricted-growth ordering on labels L.
            blocks.sort(key=min)
            out.add(tuple(tuple(sorted(x)) for x in blocks))
    return out


def transition_report(rows: tuple[int, ...]) -> None:
    states = tuple(p for p in partitions(L) if independent_state(p))
    base = {p for p in states if extends(rows, p)}
    assert base == set(states)
    target = decorated_states()
    assert target <= set(states)
    unchanged = []
    gains_target = []
    for e in sorted(INT):
        for op in ("delete", "contract"):
            kw = {"delete_edge": e} if op == "delete" else {"contract_edge": e}
            now = {p for p in states if extends(rows, p, **kw)}
            gain = now - base
            if now == base:
                unchanged.append((op, e))
            if gain & target:
                gains_target.append((op, e, len(gain & target)))
    for x in D:
        now = {p for p in states if extends(rows, p, delete_vertex=x)}
        gain = now - base
        if now == base:
            unchanged.append(("delete-vertex", x))
        if gain & target:
            gains_target.append(("delete-vertex", x, len(gain & target)))
    assert all(("delete", e) in unchanged for e in INT)
    assert all(("delete-vertex", x) in unchanged for x in D)
    assert not gains_target
    print("states", len(states), "base", len(base), "missing-T", len(target - base),
          "unchanged", unchanged, "T-gains", gains_target)


if __name__ == "__main__":
    search()
