#!/usr/bin/env python3
"""Exact boundary-transition probe for a pentagonal-antiprism web.

The outer five-cycle carries one portal from each missing-C5 class in
pentagram order.  Two extra labels w,a are complete to the planar shore.
"""

from __future__ import annotations

import itertools


O = tuple(range(5))
I = tuple(range(5, 10))
H = 10
D = O + I + (H,)
U = tuple(range(5))
W, A = 5, 6
L = tuple(range(7))


def e(x: int, y: int) -> tuple[int, int]:
    return tuple(sorted((x, y)))


INT = {e(i, (i + 1) % 5) for i in O}
INT |= {e(5 + i, 5 + (i + 1) % 5) for i in O}
INT |= {e(i, 5 + i) for i in O} | {e(i, 5 + (i - 1) % 5) for i in O}
INT |= {e(H, 5 + i) for i in O}
MISSING = {e(i, (i + 1) % 5) for i in U}
BOUNDARY = {e(i, j) for i, j in itertools.combinations(U, 2) if e(i, j) not in MISSING}
BOUNDARY |= {e(A, x) for x in (0, 2, 4)}
PENTAGRAM = (0, 2, 4, 1, 3)
ROWS = tuple(
    ((1 << W) | (1 << A) | (1 << PENTAGRAM[x])) if x in O
    else ((1 << W) | (1 << A))
    for x in D
)


def connected(xs: frozenset[int]) -> bool:
    seen = {next(iter(xs))}
    stack = list(seen)
    while stack:
        x = stack.pop()
        for y in xs:
            if y not in seen and e(x, y) in INT:
                seen.add(y)
                stack.append(y)
    return seen == set(xs)


def linked(frame: int) -> bool:
    ab = ((frame + 1) % 5, (frame + 2) % 5)
    cd = ((frame + 3) % 5, (frame + 4) % 5)
    sets = [frozenset(x for x in D if mask >> x & 1) for mask in range(1, 1 << len(D))]
    sets = [x for x in sets if connected(x)]
    xsets = [x for x in sets if any(ROWS[v] >> ab[0] & 1 for v in x) and any(ROWS[v] >> ab[1] & 1 for v in x)]
    ysets = [x for x in sets if any(ROWS[v] >> cd[0] & 1 for v in x) and any(ROWS[v] >> cd[1] & 1 for v in x)]
    return any(x.isdisjoint(y) for x in xsets for y in ysets)


def cut_ok() -> bool:
    for mask in range(1, (1 << len(D)) - 1):
        x = {v for v in D if mask >> v & 1}
        inner = {v for v in set(D) - x if any(e(v, z) in INT for z in x)}
        labels = {j for v in x for j in L if ROWS[v] >> j & 1}
        if len(inner) + len(labels) < 7:
            print("bad cut", x, inner, labels)
            return False
    return True


def partitions(items: tuple[int, ...]):
    blocks: list[list[int]] = []
    def rec(i: int):
        if i == len(items):
            yield tuple(tuple(b) for b in blocks)
            return
        x = items[i]
        for b in blocks:
            b.append(x); yield from rec(i + 1); b.pop()
        blocks.append([x]); yield from rec(i + 1); blocks.pop()
    yield from rec(0)


def independent(state) -> bool:
    return len(state) <= 6 and all(e(x, y) not in BOUNDARY for b in state for x, y in itertools.combinations(b, 2))


def extends(state, *, delete_vertex=None, delete_edge=None, contract_edge=None) -> bool:
    vertices = tuple(x for x in D if x != delete_vertex)
    edges = set(INT)
    if delete_edge is not None: edges.discard(delete_edge)
    if contract_edge is not None: edges.discard(contract_edge)
    bcolor = {x: c for c, b in enumerate(state) for x in b}
    color: dict[int, int] = {}
    def ok(x, c):
        if contract_edge is not None and x in contract_edge:
            y = contract_edge[0] if x == contract_edge[1] else contract_edge[1]
            if y in color and color[y] != c: return False
        if any(y in color and color[y] == c and e(x, y) in edges for y in vertices): return False
        return all(bcolor.get(j) != c for j in L if ROWS[x] >> j & 1)
    def dfs(left):
        if not left: return contract_edge is None or color[contract_edge[0]] == color[contract_edge[1]]
        x = max(left, key=lambda z: sum(e(z, y) in edges for y in vertices))
        rest = tuple(z for z in left if z != x)
        choices = range(6)
        if contract_edge is not None and x in contract_edge:
            y = contract_edge[0] if x == contract_edge[1] else contract_edge[1]
            if y in color: choices = (color[y],)
        for c in choices:
            if ok(x, c):
                color[x] = c
                if dfs(rest): return True
                del color[x]
        return False
    return dfs(vertices)


def decorated_states():
    out = set()
    for j in U:
        base = [{(j+1)%5,(j+2)%5},{(j+3)%5,(j+4)%5},{j},{A}]
        for pos in range(5):
            blocks=[set(x) for x in base]
            if pos<4: blocks[pos].add(W)
            else: blocks.append({W})
            blocks.sort(key=min)
            out.add(tuple(tuple(sorted(x)) for x in blocks))
    return out


def main():
    print("cut", cut_ok(), "linked frames", [j for j in U if linked(j)])
    states = tuple(p for p in partitions(L) if independent(p))
    base = {p for p in states if extends(p)}
    target = decorated_states()
    print("states",len(states),"base",len(base),"missingT",len(target-base))
    unchanged=[]; tg=[]
    for edge in sorted(INT):
        for op in ("delete","contract"):
            kw={"delete_edge":edge} if op=="delete" else {"contract_edge":edge}
            now={p for p in states if extends(p,**kw)}
            gain=now-base
            if now==base: unchanged.append((op,edge))
            if gain&target: tg.append((op,edge,len(gain&target)))
    for x in D:
        now={p for p in states if extends(p,delete_vertex=x)}
        gain=now-base
        if now==base: unchanged.append(("delete-v",x))
        if gain&target: tg.append(("delete-v",x,len(gain&target)))
    print("unchanged",unchanged)
    print("target gains",tg)


if __name__ == "__main__": main()
