#!/usr/bin/env python3
"""Verify the twelve-vertex fourfold-incidence shore-filling barrier."""

from itertools import combinations


S = ("p", "q", "i1", "i2", "i3", "t1", "t2", "t3")
I = frozenset(("i1", "i2", "i3"))
T = frozenset(("t1", "t2", "t3"))
V = S + ("u", "e", "x", "y")
E = frozenset(("e",))
F = frozenset(("x", "y"))
P_E = ("p", "e", "q")
P_F = ("p", "x", "y", "q")


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def edge(a, b):
    return frozenset((a, b))


EDGES = {
    edge("p", "t1"), edge("t1", "i1"), edge("i1", "p"),
    edge("q", "i2"), edge("i2", "t2"), edge("t2", "q"),
    edge("i1", "t3"), edge("t3", "i3"), edge("i3", "t2"),
    *(edge("u", v) for v in S),
    *(edge("e", v) for v in S),
    edge("x", "y"),
    *(edge("x", v) for v in S if v != "q"),
    *(edge("y", v) for v in S if v != "p"),
}


def adjacent(a, b):
    return edge(a, b) in EDGES


def induced_edges(vertices):
    vertices = set(vertices)
    return {e for e in EDGES if e <= vertices}


def components(vertices):
    remaining = set(vertices)
    answer = []
    while remaining:
        start = min(remaining)
        found = {start}
        stack = [start]
        remaining.remove(start)
        while stack:
            v = stack.pop()
            new = {w for w in remaining if adjacent(v, w)}
            remaining -= new
            found |= new
            stack.extend(new)
        answer.append(frozenset(found))
    return answer


def fill_width(vertices, edges, order):
    graph = {v: set() for v in vertices}
    for e in edges:
        a, b = tuple(e)
        graph[a].add(b)
        graph[b].add(a)
    width = 0
    for v in order:
        neighbours = graph[v]
        width = max(width, len(neighbours))
        for a, b in combinations(neighbours, 2):
            graph[a].add(b)
            graph[b].add(a)
        for w in neighbours:
            graph[w].remove(v)
        del graph[v]
    require(not graph, "fill order does not eliminate every vertex")
    return width


def proper(colouring, vertices):
    vertices = set(vertices)
    return all(
        colouring[a] != colouring[b]
        for a, b in (tuple(e) for e in induced_edges(vertices))
    )


def colour_component(colouring, vertices, start, colours):
    allowed = {v for v in vertices if colouring[v] in colours}
    return next(c for c in components(allowed) if start in c)


def k_colourable(k):
    colours = {}

    def search():
        if len(colours) == len(V):
            return dict(colours)
        uncoloured = [v for v in V if v not in colours]
        v = max(
            uncoloured,
            key=lambda w: (
                len({colours[z] for z in V if z in colours and adjacent(w, z)}),
                sum(adjacent(w, z) for z in V),
                w,
            ),
        )
        forbidden = {colours[z] for z in V if z in colours and adjacent(v, z)}
        for c in range(k):
            if c not in forbidden:
                colours[v] = c
                answer = search()
                if answer is not None:
                    return answer
                del colours[v]
        return None

    return search()


def vertex_connectivity():
    for size in range(len(V) - 1):
        for cut in combinations(V, size):
            remaining = set(V) - set(cut)
            if len(remaining) > 1 and len(components(remaining)) > 1:
                return size, cut
    raise AssertionError("no vertex cut found")


require(len(V) == 12 and len(EDGES) == 40, "wrong graph order or size")
require(
    all(not adjacent(a, b) for a, b in combinations(I, 2)),
    "I is not independent",
)
require(
    all(not adjacent(a, b) for a, b in combinations(T, 2)),
    "T is not independent",
)
require(not adjacent("p", "q"), "the roots are adjacent")
require(
    all(
        any(adjacent(root, vertex) for vertex in block)
        for root in ("p", "q")
        for block in (I, T)
    ),
    "a root-to-block contact is missing",
)
require(any(adjacent(a, b) for a in I for b in T), "I and T are anticomplete")

alpha = max(
    len(block)
    for size in range(len(S) + 1)
    for block in combinations(S, size)
    if all(not adjacent(a, b) for a, b in combinations(block, 2))
)
require(alpha == 3, "boundary independence number is not three")

boundary_width = fill_width(
    S,
    induced_edges(S),
    ("p", "t1", "q", "i2", "i1", "t3", "i3", "t2"),
)
require(boundary_width == 2, "boundary fill width is not two")
require(
    components(set(V) - set(S) - {"u"}) == [E, F],
    "the open shores are not exactly E and F",
)
require(all(any(adjacent(v, z) for z in E) for v in S), "E is not full")
require(all(any(adjacent(v, z) for z in F) for v in S), "F is not full")

c_e = {**{v: 0 for v in I}, **{v: 1 for v in T}, "p": 2, "q": 2, "e": 3}
c_f = {
    **{v: 0 for v in I}, **{v: 1 for v in T},
    "p": 2, "q": 3, "x": 3, "y": 2,
}
require(proper(c_e, set(S) | E), "the E-shore colouring is improper")
require(proper(c_f, set(S) | F), "the F-shore colouring is improper")
require({v for v in S if c_e[v] == 0} == I, "E does not realize exact I")
require({v for v in S if c_e[v] == 1} == T, "E does not realize exact T")
require({v for v in S if c_f[v] == 0} == I, "F does not realize exact I")
require({v for v in S if c_f[v] == 1} == T, "F does not realize exact T")
require(
    colour_component(c_e, S, "q", {2, 3}) == frozenset({"q"}),
    "q is not a singleton boundary component in the E colouring",
)
require(
    colour_component(c_f, S, "q", {2, 3}) == frozenset({"q"}),
    "q is not a singleton boundary component in the F colouring",
)
require(
    colour_component(c_e, set(S) | E, "q", {2, 3}) == frozenset(P_E),
    "the E full two-colour component is not P_E",
)
require(
    colour_component(c_f, set(S) | F, "q", {2, 3}) == frozenset(P_F),
    "the F full two-colour component is not P_F",
)

cycle = P_E + tuple(reversed(P_F[1:-1]))
cycle_edges = {edge(cycle[j], cycle[(j + 1) % 5]) for j in range(5)}
require(induced_edges(cycle) == cycle_edges, "the trace cycle is not induced")
require(
    E == frozenset(P_E[1:-1]) and F == frozenset(P_F[1:-1]),
    "a selected path does not fill its open shore",
)
off_cycle = set(V) - set(cycle)
require(components(off_cycle) == [frozenset(off_cycle)], "off-cycle graph disconnected")
require(
    all(any(adjacent(v, z) for z in off_cycle) for v in cycle),
    "the off-cycle component does not attach around the whole cycle",
)

c_e_split = {**{v: 0 for v in I}, **{v: 1 for v in T}, "p": 2, "q": 3, "e": 4}
c_f_merged = {
    **{v: 0 for v in I}, **{v: 1 for v in T},
    "p": 2, "q": 2, "x": 3, "y": 4,
}
require(proper(c_e_split, set(S) | E), "the split E response is improper")
require(proper(c_f_merged, set(S) | F), "the merged F response is improper")

host_width = fill_width(
    V,
    EDGES,
    ("p", "q", "i2", "t1", "i1", "t2", "i3", "t3", "u", "e", "x", "y"),
)
require(host_width == 5, "host fill width is not five")
require(k_colourable(4) is None, "host is four-colourable")
require(k_colourable(5) is not None, "host is not five-colourable")
kappa, cut = vertex_connectivity()
require(kappa == 5, "host vertex connectivity is not five")

print("vertices", len(V))
print("edges", len(EDGES))
print("boundary_alpha", alpha)
print("boundary_fill_width", boundary_width)
print("host_fill_width", host_width)
print("chromatic_number", 5)
print("vertex_connectivity", kappa)
print("minimum_cut", " ".join(cut))
print("aligned_paths", "p-e-q", "p-x-y-q")
print("PASS degree8_fourfold_incidence_bridge_interval_barrier")
