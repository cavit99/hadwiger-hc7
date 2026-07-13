"""Verify the finite three-gate pullback-matching barrier.

This script has no third-party dependencies.  It checks the exact finite
claims in the adjacent Markdown note; it does not test contraction
criticality or K_7-minor exclusion.
"""

from __future__ import annotations

from itertools import combinations, permutations


Vertex = str
Edge = frozenset[Vertex]


S = frozenset({"c", "b1", "a1", "b2", "a2", "b3", "a3"})
B = (
    frozenset({"b1", "a1"}),
    frozenset({"b2", "a2"}),
    frozenset({"b3", "a3"}),
)
Z = frozenset({"z1", "z2", "z3"})
P = Z | {"x", "y"}
Q = frozenset({"q"})
L = frozenset({"ell"})
R = P | Q
V = S | L | R


def edge(u: Vertex, v: Vertex) -> Edge:
    assert u != v
    return frozenset({u, v})


EDGES: set[Edge] = set()


def add(u: Vertex, v: Vertex) -> None:
    EDGES.add(edge(u, v))


for triangle in (("a1", "a2", "a3"), ("b1", "b2", "b3")):
    for u, v in combinations(triangle, 2):
        add(u, v)

for i in range(1, 4):
    add("c", f"a{i}")

for u, v in (("b1", "a2"), ("b2", "a3"), ("b3", "a1")):
    add(u, v)

for lobe in ("x", "y"):
    for z in Z:
        add(lobe, z)
add("z1", "z2")
add("z2", "z3")

for s in ("c", "b1", "b2", "b3"):
    add("x", s)
for s in ("c", "a1", "a2", "a3"):
    add("y", s)

for j in range(1, 4):
    for i in range(1, 4):
        add(f"z{j}", f"b{i}")
    add(f"z{j}", f"a{j}")

for packet in ("q", "ell"):
    for s in S:
        add(packet, s)


def adjacency(vertices: frozenset[Vertex] = V) -> dict[Vertex, set[Vertex]]:
    answer = {v: set() for v in vertices}
    for e in EDGES:
        u, v = tuple(e)
        if u in vertices and v in vertices:
            answer[u].add(v)
            answer[v].add(u)
    return answer


ADJ = adjacency()


def components(vertices: frozenset[Vertex]) -> list[frozenset[Vertex]]:
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
            stack.extend((ADJ[u] & vertices) - found)
        unseen -= found
        answer.append(frozenset(found))
    return answer


def connected(vertices: frozenset[Vertex]) -> bool:
    return bool(vertices) and len(components(vertices)) == 1


def neighbour_set(vertices: frozenset[Vertex], target: frozenset[Vertex]) -> frozenset[Vertex]:
    return frozenset().union(*(ADJ[v] & target for v in vertices))


def proper_colouring(
    vertices: frozenset[Vertex], graph_edges: set[Edge], colours: dict[Vertex, int]
) -> bool:
    return set(colours) == set(vertices) and all(
        colours[u] != colours[v]
        for e in graph_edges
        if e <= vertices
        for u, v in [tuple(e)]
    )


def equality_partition(labels: frozenset[Vertex], colours: dict[Vertex, int]) -> set[frozenset[Vertex]]:
    classes: dict[int, set[Vertex]] = {}
    for v in labels:
        classes.setdefault(colours[v], set()).add(v)
    return {frozenset(block) for block in classes.values()}


def contract(cluster: frozenset[Vertex], image: Vertex) -> tuple[frozenset[Vertex], set[Edge]]:
    assert connected(cluster)
    assert image not in V
    vertices = (V - cluster) | {image}
    graph_edges: set[Edge] = set()
    for e in EDGES:
        ends = set(e)
        outside = ends - cluster
        if not outside:
            continue
        if len(outside) == 1 and ends & cluster:
            graph_edges.add(edge(image, next(iter(outside))))
        elif len(outside) == 2:
            u, v = tuple(outside)
            graph_edges.add(edge(u, v))
    return frozenset(vertices), graph_edges


def full_packets(shore: frozenset[Vertex], boundary: frozenset[Vertex]) -> list[frozenset[Vertex]]:
    packets: list[frozenset[Vertex]] = []
    ordered = sorted(shore)
    for size in range(1, len(ordered) + 1):
        for choice in combinations(ordered, size):
            candidate = frozenset(choice)
            if connected(candidate) and neighbour_set(candidate, boundary) == boundary:
                packets.append(candidate)
    return packets


def packing_number(packets: list[frozenset[Vertex]]) -> int:
    best = 0

    def search(index: int, used: frozenset[Vertex], count: int) -> None:
        nonlocal best
        if count + len(packets) - index <= best:
            return
        if index == len(packets):
            best = max(best, count)
            return
        search(index + 1, used, count)
        packet = packets[index]
        if packet.isdisjoint(used):
            search(index + 1, used | packet, count + 1)

    search(0, frozenset(), 0)
    return best


# The old boundary really carries the paired-triangle data.
for block in B:
    assert all(edge(u, v) not in EDGES for u, v in combinations(block, 2))
for left, right in combinations(B, 2):
    assert any(edge(u, v) in EDGES for u in left for v in right)
assert all(any(edge("c", v) in EDGES for v in block) for block in B)

# S is an actual seven-boundary with the declared orientation.
assert L and R and L.isdisjoint(R)
assert not any(edge(u, v) in EDGES for u in L for v in R)
assert set(components(V - S)) == {L, P, Q}

# Exhaust all 6,476 deletions of fewer than seven vertices.  Deleting S
# disconnects, so the vertex-connectivity is exactly seven.
for size in range(7):
    for deleted_tuple in combinations(sorted(V), size):
        deleted = frozenset(deleted_tuple)
        assert connected(V - deleted), (size, deleted)
assert len(components(V - S)) > 1

# Enumerate every connected full packet and every disjoint packet packing.
packets_l = full_packets(L, S)
packets_r = full_packets(R, S)
assert packing_number(packets_l) == 1
assert packing_number(packets_r) == 2
assert P in packets_r and Q in packets_r
assert not any(
    left.isdisjoint(right)
    for left, right in combinations(full_packets(P, S), 2)
)

# The old state is returned by a literal proper-minor operation.
cluster = L | B[0]
minor_vertices, minor_edges = contract(cluster, "t")
minor_colours = {
    "t": 1,
    "b2": 2,
    "a2": 2,
    "b3": 3,
    "a3": 3,
    "c": 4,
    "z1": 4,
    "z3": 4,
    "q": 5,
    "x": 5,
    "y": 5,
    "z2": 6,
}
assert minor_vertices != V
assert proper_colouring(minor_vertices, minor_edges, minor_colours)
pulled_boundary_colours = {
    "b1": minor_colours["t"],
    "a1": minor_colours["t"],
    **{v: minor_colours[v] for v in S - B[0]},
}
assert equality_partition(S, pulled_boundary_colours) == set(B) | {frozenset({"c"})}

# P is exactly 3-connected, Z is its 3-cut, and x has the audited trace.
for size in range(3):
    for deleted_tuple in combinations(sorted(P), size):
        assert connected(P - frozenset(deleted_tuple))
assert set(components(P - Z)) == {frozenset({"x"}), frozenset({"y"})}
trace = frozenset({"c", "b1", "b2", "b3"})
assert ADJ["x"] & P == Z
assert ADJ["x"] & S == trace
assert all(not block <= trace for block in B)

# The lobe boundary is a genuine exact-seven adhesion, full on both sides.
S_X = Z | trace
new_components = components(V - S_X)
assert len(S_X) == 7
assert frozenset({"x"}) in new_components
assert len(new_components) == 2
assert all(neighbour_set(component, S_X) == S_X for component in new_components)
assert frozenset(ADJ["x"]) == S_X
assert 1 < len(P)

# Every proposed old-literal/gate pair is an edge.  Hence no permutation
# produces three independent blocks on S_X.
b_vertices = ("b1", "b2", "b3")
z_vertices = ("z1", "z2", "z3")
assert all(edge(b, z) in EDGES for b in b_vertices for z in z_vertices)
for sigma in permutations(z_vertices):
    assert any(edge(b_vertices[i], sigma[i]) in EDGES for i in range(3))

# Scope guard: the host itself is six-colourable, so this is not an HC_7
# counterexample and does not falsify a terminal-disjunctive conditional.
host_colours = {
    "b1": 1,
    "a1": 1,
    "b2": 2,
    "a2": 2,
    "b3": 3,
    "a3": 3,
    "c": 4,
    "z1": 4,
    "z3": 4,
    "q": 5,
    "ell": 5,
    "x": 5,
    "y": 5,
    "z2": 6,
}
assert proper_colouring(V, EDGES, host_colours)

print("host: 14 vertices, exactly 7-connected, explicitly 6-colourable")
print("old separation: actual seven-boundary with packet vector (1,2)")
print("old paired-triangle state: legally attained by a proper contraction")
print("gate: P is 3-connected and x has exact c-plus-rainbow trace")
print("descendant: strict actual seven-adhesion")
print("pullback compatibility graph: empty; no independent-pair permutation")
