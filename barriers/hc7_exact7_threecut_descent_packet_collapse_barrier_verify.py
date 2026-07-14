#!/usr/bin/env python3
"""Verify the order-minimal three-cut packet-collapse barrier.

This script uses only the Python standard library.  It verifies every
finite claim in the adjacent note, including exact connectivity, packet
numbers, Dirac inequalities, chromatic number, the attained state, and the
explicit K7 model.
"""

from __future__ import annotations

from itertools import combinations, permutations


Vertex = str
Edge = frozenset[Vertex]

S = frozenset({"c", "b1", "a1", "b2", "a2", "b3", "a3"})
BLOCKS = (
    frozenset({"b1", "a1"}),
    frozenset({"b2", "a2"}),
    frozenset({"b3", "a3"}),
)
T = frozenset({"z1", "z2", "z3"})
L = T | {"x", "y"}
R = frozenset({"p", "q"})
V = S | L | R


def edge(left: Vertex, right: Vertex) -> Edge:
    if left == right:
        raise ValueError("loops are forbidden")
    return frozenset({left, right})


EDGES: set[Edge] = set()


def add(left: Vertex, right: Vertex) -> None:
    EDGES.add(edge(left, right))


for triangle in (("a1", "a2", "a3"), ("b1", "b2", "b3"), ("z1", "z2", "z3")):
    for left, right in combinations(triangle, 2):
        add(left, right)

for i in range(1, 4):
    add("c", f"a{i}")
add("c", "b1")

for left, right in (("b1", "a2"), ("b2", "a3"), ("b3", "a1")):
    add(left, right)

for lobe in ("x", "y"):
    for gate in T:
        add(lobe, gate)

for literal in ("c", "b1", "b2", "b3"):
    add("x", literal)
for literal in ("c", "a1", "a2", "a3"):
    add("y", literal)

for j in range(1, 4):
    for i in range(1, 4):
        add(f"z{j}", f"b{i}")
    add(f"z{j}", f"a{j}")

add("p", "q")
for packet in ("p", "q"):
    for literal in S:
        add(packet, literal)


def adjacency(vertices: frozenset[Vertex] = V, edges: set[Edge] = EDGES):
    answer = {vertex: set() for vertex in vertices}
    for item in edges:
        left, right = tuple(item)
        if left in vertices and right in vertices:
            answer[left].add(right)
            answer[right].add(left)
    return answer


ADJ = adjacency()


def components(vertices: frozenset[Vertex], adj=ADJ) -> list[frozenset[Vertex]]:
    unseen = set(vertices)
    answer: list[frozenset[Vertex]] = []
    while unseen:
        start = unseen.pop()
        found = {start}
        stack = [start]
        while stack:
            current = stack.pop()
            for neighbour in adj[current] & unseen:
                unseen.remove(neighbour)
                found.add(neighbour)
                stack.append(neighbour)
        answer.append(frozenset(found))
    return answer


def connected(vertices: frozenset[Vertex], adj=ADJ) -> bool:
    return bool(vertices) and len(components(vertices, adj)) == 1


def neighbours(vertices: frozenset[Vertex], target: frozenset[Vertex], adj=ADJ):
    return frozenset().union(*(adj[vertex] & target for vertex in vertices))


def full_packets(shore: frozenset[Vertex], boundary: frozenset[Vertex]):
    ordered = sorted(shore)
    answer: list[frozenset[Vertex]] = []
    for size in range(1, len(ordered) + 1):
        for choice in combinations(ordered, size):
            candidate = frozenset(choice)
            if connected(candidate) and neighbours(candidate, boundary) == boundary:
                answer.append(candidate)
    return answer


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
        if packets[index].isdisjoint(used):
            search(index + 1, used | packets[index], count + 1)

    search(0, frozenset(), 0)
    return best


def proper_colouring(vertices, edges, colouring) -> bool:
    return set(colouring) == set(vertices) and all(
        colouring[left] != colouring[right]
        for item in edges
        if item <= set(vertices)
        for left, right in [tuple(item)]
    )


def find_colouring(vertices, edges, colour_count: int, preset=None):
    vertices = frozenset(vertices)
    adj = adjacency(vertices, edges)
    colouring = dict(preset or {})
    if not set(colouring) <= vertices:
        raise ValueError("preset contains a foreign vertex")
    if any(
        colouring[left] == colouring[right]
        for item in edges
        if item <= set(colouring)
        for left, right in [tuple(item)]
    ):
        return None

    def search():
        if len(colouring) == len(vertices):
            return dict(colouring)
        vertex = max(
            (item for item in vertices if item not in colouring),
            key=lambda item: (
                len({colouring[x] for x in adj[item] if x in colouring}),
                len(adj[item]),
            ),
        )
        forbidden = {colouring[x] for x in adj[vertex] if x in colouring}
        for colour in range(colour_count):
            if colour in forbidden:
                continue
            colouring[vertex] = colour
            witness = search()
            if witness is not None:
                return witness
            del colouring[vertex]
        return None

    return search()


def contract(cluster: frozenset[Vertex], image: Vertex):
    if not connected(cluster):
        raise ValueError("contracted set is disconnected")
    if image in V:
        raise ValueError("image name is not fresh")
    vertices = (V - cluster) | {image}
    edges: set[Edge] = set()
    for item in EDGES:
        left, right = tuple(item)
        new_left = image if left in cluster else left
        new_right = image if right in cluster else right
        if new_left != new_right:
            edges.add(edge(new_left, new_right))
    return frozenset(vertices), edges


def independence_number(vertices: frozenset[Vertex]) -> int:
    ordered = sorted(vertices)
    for size in range(len(ordered), -1, -1):
        for choice in combinations(ordered, size):
            if all(edge(left, right) not in EDGES for left, right in combinations(choice, 2)):
                return size
    raise RuntimeError("unreachable")


def verify_model(bags: tuple[frozenset[Vertex], ...]) -> None:
    if len(bags) != 7 or any(not bag for bag in bags):
        raise AssertionError("model must have seven nonempty bags")
    if any(not left.isdisjoint(right) for left, right in combinations(bags, 2)):
        raise AssertionError("model bags overlap")
    if any(not connected(bag) for bag in bags):
        raise AssertionError("a model bag is disconnected")
    if any(
        not any(edge(left_vertex, right_vertex) in EDGES
                for left_vertex in left for right_vertex in right)
        for left, right in combinations(bags, 2)
    ):
        raise AssertionError("two model bags are nonadjacent")


# Paired boundary and a literal spanning non-path tree.
for block in BLOCKS:
    if any(edge(left, right) in EDGES for left, right in combinations(block, 2)):
        raise AssertionError("a paired block is not independent")
for left, right in combinations(BLOCKS, 2):
    if not any(edge(x, y) in EDGES for x in left for y in right):
        raise AssertionError("two paired blocks are nonadjacent")
if not all(any(edge("c", x) in EDGES for x in block) for block in BLOCKS):
    raise AssertionError("c misses a paired block")
TREE_EDGES = {
    edge("c", "a1"), edge("c", "a2"), edge("c", "a3"),
    edge("a2", "b1"), edge("a3", "b2"), edge("a1", "b3"),
}
if not TREE_EDGES <= EDGES:
    raise AssertionError("advertised spanning tree is not literal")
tree_adj = adjacency(S, TREE_EDGES)
if not connected(S, tree_adj) or max(map(len, tree_adj.values())) < 3:
    raise AssertionError("advertised tree is not a spanning non-path tree")

# Exact old separation and connectivity seven.
if any(edge(left, right) in EDGES for left in L for right in R):
    raise AssertionError("old open shores are not anticomplete")
if set(components(V - S)) != {L, R}:
    raise AssertionError("S is not the advertised old boundary")
for size in range(7):
    for deleted in combinations(sorted(V), size):
        if not connected(V - frozenset(deleted)):
            raise AssertionError(("cut below seven", deleted))
if len(components(V - S)) < 2:
    raise AssertionError("deleting S does not disconnect")

# Every Dirac neighbourhood inequality.
dirac = {}
for vertex in V:
    value = independence_number(frozenset(ADJ[vertex]))
    bound = len(ADJ[vertex]) - 5
    dirac[vertex] = (len(ADJ[vertex]), value, bound)
    if value > bound:
        raise AssertionError(("Dirac failure", vertex, dirac[vertex]))

# Exact old packet vector.
packets_l = full_packets(L, S)
packets_r = full_packets(R, S)
if packing_number(packets_l) != 1 or packing_number(packets_r) != 2:
    raise AssertionError("old packet vector is not (1,2)")
if frozenset({"p"}) not in packets_r or frozenset({"q"}) not in packets_r:
    raise AssertionError("old singleton packets are not full")

# Three-connected old thin shore, exact three-cut, and support-four lobes.
for size in range(3):
    for deleted in combinations(sorted(L), size):
        if not connected(L - frozenset(deleted)):
            raise AssertionError(("L is not three-connected", deleted))
if set(components(L - T)) != {frozenset({"x"}), frozenset({"y"})}:
    raise AssertionError("T is not the advertised two-lobe three-cut")
for lobe, support in (
    (frozenset({"x"}), frozenset({"c", "b1", "b2", "b3"})),
    (frozenset({"y"}), frozenset({"c", "a1", "a2", "a3"})),
):
    if neighbours(lobe, L - lobe) != T or neighbours(lobe, S) != support:
        raise AssertionError(("wrong lobe trace", lobe))

# Legal attainment of the old paired state.
cluster = frozenset({"y", "z2", "b1", "a1"})
minor_vertices, minor_edges = contract(cluster, "tau")
minor_colouring = {
    "tau": 0,
    "b2": 1, "a2": 1,
    "b3": 2, "a3": 2,
    "c": 3, "z3": 3,
    "q": 4, "x": 4,
    "p": 5, "z1": 5,
}
if not proper_colouring(minor_vertices, minor_edges, minor_colouring):
    raise AssertionError("advertised proper-minor colouring is invalid")
expanded_boundary = {
    "b1": 0, "a1": 0,
    "b2": 1, "a2": 1,
    "b3": 2, "a3": 2,
    "c": 3,
}
if any(expanded_boundary[left] == expanded_boundary[right]
       for item in EDGES if item <= S for left, right in [tuple(item)]):
    raise AssertionError("expanded paired boundary state is improper")

# Exact descended boundary and packet collapse.
OMEGA = T | {"c", "b1", "b2", "b3"}
D = frozenset({"x"})
O = V - OMEGA - D
if neighbours(D, V - D) != OMEGA:
    raise AssertionError("the descended lobe boundary is not exact")
if set(components(V - OMEGA)) != {D, O}:
    raise AssertionError("Omega does not expose the two advertised shores")
if neighbours(D, OMEGA) != OMEGA or neighbours(O, OMEGA) != OMEGA:
    raise AssertionError("a descended shore is not Omega-full")
packets_d = full_packets(D, OMEGA)
packets_o = full_packets(O, OMEGA)
if packing_number(packets_d) != 1 or packing_number(packets_o) != 1:
    raise AssertionError("descended packet vector is not (1,1)")
if frozenset({"p"}) in packets_o or frozenset({"q"}) in packets_o:
    raise AssertionError("an old packet unexpectedly remains Omega-full")

# Every natural old-literal/gate paired block is forbidden.
b_vertices = ("b1", "b2", "b3")
z_vertices = ("z1", "z2", "z3")
if not all(edge(left, right) in EDGES for left in b_vertices for right in z_vertices):
    raise AssertionError("compatibility graph is not empty")
for sigma in permutations(z_vertices):
    if all(edge(b_vertices[i], sigma[i]) not in EDGES for i in range(3)):
        raise AssertionError("a paired pullback permutation exists")

# Chromatic number exactly seven and failure of vertex criticality.
seven_colouring = {
    "b1": 0, "b3": 1, "b2": 2,
    "z2": 3, "z1": 4, "z3": 5, "x": 6,
    "p": 3, "q": 4,
    "a3": 0, "a1": 2, "c": 1, "y": 6, "a2": 5,
}
if not proper_colouring(V, EDGES, seven_colouring):
    raise AssertionError("advertised seven-colouring is invalid")
if find_colouring(V, EDGES, 6) is not None:
    raise AssertionError("host is unexpectedly six-colourable")
if find_colouring(V - {"a1"}, {item for item in EDGES if "a1" not in item}, 6) is not None:
    raise AssertionError("advertised failure of vertex criticality is false")

# Explicit K7 model: the target-minor hypothesis is intentionally violated.
MODEL = (
    frozenset({"x", "z1"}),
    frozenset({"y", "z2"}),
    frozenset({"b1"}),
    frozenset({"b3", "a2", "q"}),
    frozenset({"a3", "a1", "p"}),
    frozenset({"z3"}),
    frozenset({"b2"}),
)
verify_model(MODEL)

if len(V) != 14 or not (len(S) == 7 and len(L) == 5 and len(R) == 2):
    raise AssertionError("order-minimal size accounting failed")

print("VERIFIED")
print("vertices", len(V), "edges", len(EDGES), "connectivity", 7)
print("old_packet_vector", (packing_number(packets_l), packing_number(packets_r)))
print("descended_packet_vector", (packing_number(packets_d), packing_number(packets_o)))
print("old_state", "legally attained")
print("paired_pullback_compatibility_edges", 0)
print("Dirac", dirac)
print("chromatic_number", 7)
print("K7_model", MODEL)
print("violated_HC7_inputs", "K7-minor-free and minor-minimality")
