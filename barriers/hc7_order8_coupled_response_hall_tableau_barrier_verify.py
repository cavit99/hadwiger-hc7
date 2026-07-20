#!/usr/bin/env python3
"""Verify the minimum coupled-switch/Hall tableau and its literal shell."""

from collections import deque


def add_edge(adj, x, y):
    assert x != y
    adj.setdefault(x, set()).add(y)
    adj.setdefault(y, set()).add(x)


def connected(adj, vertices):
    vertices = set(vertices)
    if not vertices:
        return False
    seen = {next(iter(vertices))}
    queue = deque(seen)
    while queue:
        x = queue.popleft()
        for y in adj[x] & vertices:
            if y not in seen:
                seen.add(y)
                queue.append(y)
    return seen == vertices


def component(adj, colours, start, palette, deleted=frozenset()):
    seen = {start}
    queue = deque([start])
    while queue:
        x = queue.popleft()
        for y in adj[x]:
            if frozenset((x, y)) in deleted or colours[y] not in palette:
                continue
            if y not in seen:
                seen.add(y)
                queue.append(y)
    return seen


def proper(adj, colours, deleted=frozenset()):
    return all(
        colours[x] != colours[y]
        for x in adj
        for y in adj[x]
        if x < y and frozenset((x, y)) not in deleted
    )


def partition(vertices, colours):
    blocks = {}
    for v in vertices:
        blocks.setdefault(colours[v], set()).add(v)
    return {frozenset(block) for block in blocks.values()}


B = {"d", "xd", "yd", "xe", "ye", "x0", "y0", "w", "r"}
S = {"d", "e", "xd", "yd", "xe", "ye", "x0", "y0"}
adj = {v: set() for v in B | {"e", "u", "q", "p"}}

for edge in (
    ("d", "xd"), ("xd", "yd"), ("yd", "d"),
    ("xe", "ye"), ("r", "xd"), ("r", "xe"), ("xd", "xe"),
    ("e", "xe"), ("e", "ye"),
):
    add_edge(adj, *edge)

# E: u--yd directly, u--w is the selected edge, and private two-edge
# contacts make E boundary-full without changing the selected components.
E = {"u"}
add_edge(adj, "u", "yd")
add_edge(adj, "u", "w")
for t in sorted(B - {"yd", "w"}):
    h = f"h_{t}"
    E.add(h)
    add_edge(adj, "u", h)
    add_edge(adj, h, t)

# Q1 is S-full, meets w through the second selected edge, and misses r.
Q1 = {"q"}
add_edge(adj, "q", "d")
add_edge(adj, "q", "w")
for s in sorted(S - {"d"}):
    k = f"k_{s}"
    Q1.add(k)
    add_edge(adj, "q", k)
    add_edge(adj, k, s)

# Q0 is B-full, contains e, and is adjacent to Q1.
Q0 = {"p", "e"}
add_edge(adj, "p", "q")
add_edge(adj, "p", "e")
for s in sorted(S - {"e"}):
    ell = f"l_{s}"
    Q0.add(ell)
    add_edge(adj, "p", ell)
    add_edge(adj, ell, s)
for t in ("r", "w"):
    ell = f"l_{t}"
    Q0.add(ell)
    add_edge(adj, "p", ell)
    add_edge(adj, ell, t)

colours = {
    "w": 0, "d": 1, "r": 1, "xd": 2, "xe": 3,
    "yd": 4, "ye": 4, "x0": 4, "y0": 4,
    "u": 0, "q": 0, "p": 5, "e": 2,
}
for v in E - {"u"}:
    colours[v] = 5
for v in Q1 - {"q"}:
    colours[v] = 5
for v in Q0 - {"p", "e"}:
    colours[v] = 2 if v == "l_w" else 0

deleted = {frozenset(("u", "w")), frozenset(("q", "w"))}
assert proper(adj, colours, deleted)
assert connected(adj, E) and connected(adj, Q0) and connected(adj, Q1)
assert any(y in Q1 for x in Q0 for y in adj[x])

def has_neighbour(subgraph, vertex):
    return bool(adj[vertex] & set(subgraph))

assert all(has_neighbour(Q0, s) for s in S)
assert all(has_neighbour(Q1, s) for s in S)
assert all(has_neighbour(Q0, b) for b in B)
assert all(has_neighbour(Q1, b) for b in B - {"r"})
assert not has_neighbour(Q1, "r")

A = component(adj, colours, "u", {0, 4}, deleted)
D = component(adj, colours, "q", {0, 1}, deleted)
assert A & B == {"yd"}
assert D & B == {"d"}
assert A.isdisjoint(D)
cross = {
    frozenset((x, y))
    for x in A if colours[x] == 4
    for y in D if colours[y] == 1 and y in adj[x]
}
assert cross == {frozenset(("yd", "d"))}

switch_A = dict(colours)
for v in A:
    switch_A[v] = 4 if colours[v] == 0 else 0
switch_D = dict(colours)
for v in D:
    switch_D[v] = 1 if colours[v] == 0 else 0
assert proper(adj, switch_A, {frozenset(("q", "w"))})
assert proper(adj, switch_D, {frozenset(("u", "w"))})

sigma_E = {
    frozenset(("w", "yd")), frozenset(("d", "r")),
    frozenset(("xd",)), frozenset(("xe",)),
    frozenset(("ye", "x0", "y0")),
}
sigma_C = {
    frozenset(("w", "d")), frozenset(("r",)),
    frozenset(("xd",)), frozenset(("xe",)),
    frozenset(("yd", "ye", "x0", "y0")),
}
assert partition(B, switch_A) == sigma_E
assert partition(B, switch_D) == sigma_C
assert sigma_E != sigma_C

U = {"r", "xd", "xe"}
assert all(y in adj[x] for x in U for y in U if x != y)
C1 = {"w", "d"}
C2 = {"yd", "ye", "x0", "y0"}

def required(block):
    return set(block) | {u for u in U if not (adj[u] & set(block))}

assert required(C1) == C1 | {"r", "xe"}
assert required(C2) == C2 | {"r"}

supports = (Q0, Q1)
incidence = []
for support in supports:
    incidence.append([
        all(has_neighbour(support, v) for v in required(block))
        for block in (C1, C2)
    ])
assert incidence == [[True, True], [False, False]]

print("GREEN minimum coupled-response Hall tableau")
