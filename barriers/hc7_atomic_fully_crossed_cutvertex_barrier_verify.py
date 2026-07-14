#!/usr/bin/env python3
"""Verify that a fully crossed selected core need not make A 2-connected."""

from itertools import combinations


S = ("c", "a1", "t1", "a2", "t2", "a3", "t3")
U = "t1"
W = tuple(s for s in S if s != U)
A = ("z", "v", "w", "x")
R = tuple(f"r{i}" for i in range(6))
V = S + A + R


def pair(x, y):
    assert x != y
    return frozenset((x, y))


E = {
    pair("c", "a1"),
    pair("c", "a2"),
    pair("c", "a3"),
    pair("a1", "t2"),
    pair("t1", "a3"),
    pair("a2", "t3"),
    pair("z", "v"),
    pair("v", "w"),
    pair("w", "z"),
    pair("v", "x"),
}
E.update(pair(a, s) for a in A for s in W)
E.add(pair("z", U))
E.update(pair(x, y) for x, y in combinations(R, 2))
for i, r in enumerate(R):
    E.update(pair(r, s) for s in (S if i < 2 else tuple(s for s in S if s != "c")))


def adjacent(x, y):
    return pair(x, y) in E


def neighbours(x, allowed=None):
    if allowed is None:
        allowed = set(V)
    return {y for y in allowed if y != x and adjacent(x, y)}


def connected(vertices):
    vertices = set(vertices)
    if not vertices:
        return False
    reached = {next(iter(vertices))}
    stack = list(reached)
    while stack:
        reached_now = neighbours(stack.pop(), vertices) - reached
        reached.update(reached_now)
        stack.extend(reached_now)
    return reached == vertices


def full(packet):
    packet = set(packet)
    return connected(packet) and all(neighbours(s, packet) for s in S)


def full_packets(shore):
    answer = []
    for size in range(1, len(shore) + 1):
        for packet in combinations(shore, size):
            if full(packet):
                answer.append(frozenset(packet))
    return answer


def packing_number(packets):
    best = 0

    def search(start, used, count):
        nonlocal best
        best = max(best, count)
        for i in range(start, len(packets)):
            if packets[i].isdisjoint(used):
                search(i + 1, used | packets[i], count + 1)

    search(0, frozenset(), 0)
    return best


# Literal exact-seven separation and connectivity.
assert not any(adjacent(a, r) for a in A for r in R)
for size in range(7):
    for deleted in combinations(V, size):
        assert connected(set(V) - set(deleted)), ("small cut", deleted)
assert not connected(set(V) - set(S))

# Paired width-two boundary.
boundary_edges = {edge for edge in E if edge <= set(S)}
assert boundary_edges == {
    pair("c", "a1"),
    pair("c", "a2"),
    pair("c", "a3"),
    pair("a1", "t2"),
    pair("t1", "a3"),
    pair("a2", "t3"),
}

# Exact packet vector and compulsory portal.
packets_A = full_packets(A)
packets_R = full_packets(R)
assert all("z" in packet for packet in packets_A)
assert all("r0" in packet or "r1" in packet for packet in packets_R)
assert (packing_number(packets_A), packing_number(packets_R)) == (1, 2)
assert neighbours(U, set(A)) == {"z"}
assert connected(set(A) - {"z"})
assert all(neighbours(s, set(A) - {"z"}) for s in W)

# T=z-v-w is a rooted path.  The trivial T-bridge zw crosses both edges.
T = ("z", "v", "w")
assert adjacent("z", "v") and adjacent("v", "w") and adjacent("z", "w")
for left, right in (({"z"}, {"v", "w"}), ({"z", "v"}, {"w"})):
    assert "z" in left and "w" in right

# Nevertheless v is a cutvertex of the whole thin shore: x becomes isolated.
assert not connected(set(A) - {"v"})
assert neighbours("x", set(A)) == {"v"}

# The one-attachment bridge already exposes the exact-seven geometric cut
# W union {v}; no equality state is asserted on it.
assert neighbours("x") == set(W) | {"v"}
assert len(neighbours("x")) == 7

# Exact trust boundary: this static graph contains a literal K7.
literal_k7 = set(R) | {"a1"}
assert len(literal_k7) == 7
assert all(adjacent(a, b) for a, b in combinations(literal_k7, 2))

print("vertices", len(V), "edges", len(E), "connectivity", 7)
print("packet_vector", (packing_number(packets_A), packing_number(packets_R)))
print("unique_portal", "z-t1")
print("selected_core", "z-v-w", "crossing_bridge", "z-w")
print("thin_cutvertex", "v", "exact_seven_lobe", "{x}")
print("literal_K7", sorted(literal_k7))
print("missing_full_kernel", "K7-minor-freeness and universal minor-critical state")
print("VERIFIED")
