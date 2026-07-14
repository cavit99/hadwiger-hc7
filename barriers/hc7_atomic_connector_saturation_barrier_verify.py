#!/usr/bin/env python3
"""Verify the atomic connector-saturation barrier.

The certificate is deliberately dependency-free.  It checks the exact
seven-connectivity, the actual (1,2) packet vector, the unique thin portal,
the failed two-carrier list instance, the displayed double-contraction
colouring, and the literal K7 model.
"""

from itertools import combinations, product


S = ("s", "t", "w", "a", "b", "c", "d")
X = ("s", "t", "w")
Y = ("a", "b", "c", "d")
A = ("p", "q")
R = ("r1", "r2")
V = S + A + R


def pair(x, y):
    assert x != y
    return frozenset((x, y))


E = set()
E.update(pair(x, y) for x, y in product(X, Y))
E.add(pair("p", "q"))
E.add(pair("r1", "r2"))
E.update(pair("p", v) for v in S if v != "s")
E.update(pair("q", v) for v in S if v != "t")
E.update(pair(r, v) for r in R for v in S)


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
    seen = {next(iter(vertices))}
    todo = list(seen)
    while todo:
        x = todo.pop()
        for y in neighbours(x, vertices) - seen:
            seen.add(y)
            todo.append(y)
    return seen == vertices


def full_packet(packet):
    packet = set(packet)
    return connected(packet) and all(neighbours(s, packet) for s in S)


def full_packets(shore):
    shore = tuple(shore)
    answer = []
    for size in range(1, len(shore) + 1):
        for subset in combinations(shore, size):
            if full_packet(subset):
                answer.append(frozenset(subset))
    return answer


def packing_number(packets):
    best = 0

    def search(index, used, count):
        nonlocal best
        best = max(best, count)
        for j in range(index, len(packets)):
            if packets[j].isdisjoint(used):
                search(j + 1, used | packets[j], count + 1)

    search(0, frozenset(), 0)
    return best


def edge_proper(colouring, removed_edges=()):
    removed = {pair(x, y) for x, y in removed_edges}
    for edge in E - removed:
        x, y = tuple(edge)
        if colouring[x] == colouring[y]:
            return False
    return True


def carrier_splits():
    """Ordered connected adjacent partitions of the selected core A."""
    answer = []
    aset = set(A)
    for size in range(1, len(A)):
        for first_tuple in combinations(A, size):
            first = frozenset(first_tuple)
            second = frozenset(aset - first)
            if (
                connected(first)
                and connected(second)
                and any(adjacent(x, y) for x in first for y in second)
            ):
                answer.append((first, second))
    return answer


def carrier_lists(split):
    first, second = split
    lists = {}
    for s in S:
        labels = set()
        if neighbours(s, first):
            labels.add(0)
        if neighbours(s, second):
            labels.add(1)
        lists[s] = labels
    return lists


def has_list_colouring(lists):
    for values in product((0, 1), repeat=len(S)):
        colouring = dict(zip(S, values))
        if any(colouring[s] not in lists[s] for s in S):
            continue
        if all(colouring[x] != colouring[y] for x in X for y in Y):
            return True
    return False


def check_branch_model(branch_sets):
    assert len(branch_sets) == 7
    sets = [frozenset(branch) for branch in branch_sets]
    assert all(sets)
    assert all(connected(branch) for branch in sets)
    assert all(sets[i].isdisjoint(sets[j]) for i in range(7) for j in range(i))
    assert all(
        any(adjacent(x, y) for x in sets[i] for y in sets[j])
        for i in range(7)
        for j in range(i)
    )


# The old boundary is exactly K_{3,4}.
assert {edge for edge in E if edge <= set(S)} == {
    pair(x, y) for x, y in product(X, Y)
}

# There are no thin-rich edges, and S is an actual separator.
assert not any(adjacent(x, y) for x in A for y in R)
assert connected(A) and connected(R)

# Exact seven-connectivity: no deletion of at most six vertices disconnects,
# while deleting the literal seven-set S leaves the two shores apart.
for size in range(0, 7):
    for deleted in combinations(V, size):
        remaining = set(V) - set(deleted)
        assert connected(remaining), ("small cut", deleted)
assert not connected(set(V) - set(S))

# Exact packet vector (1,2).
packets_A = full_packets(A)
packets_R = full_packets(R)
assert packets_A == [frozenset(("p", "q"))]
assert set(packets_R) == {
    frozenset(("r1",)),
    frozenset(("r2",)),
    frozenset(("r1", "r2")),
}
assert (packing_number(packets_A), packing_number(packets_R)) == (1, 2)

# The compulsory portal e=pt is the unique A-t edge, and t-p-q-s is the
# selected opposite-shore connector with internal core A.
assert neighbours("t", set(A)) == {"p"}
assert all(adjacent(x, y) for x, y in zip(("t", "p", "q"), ("p", "q", "s")))

# The only carrier split has an inconsistent orientation: s and t are in
# the same K_{3,4} bipartition class, but their singleton lists differ.
splits = carrier_splits()
assert len(splits) == 2  # the same unordered split in its two orientations
for split in splits:
    lists = carrier_lists(split)
    assert all(lists[s] for s in S)
    assert len(lists["s"]) == len(lists["t"]) == 1
    assert lists["s"] != lists["t"]
    assert not has_list_colouring(lists)

# This is the lift of the displayed colouring of G/e/f, where e=pt and
# f=r1r2.  Both contracted pairs are equal and all six colours are used.
double_colouring = {
    "p": 0,
    "t": 0,
    "s": 0,
    "r1": 1,
    "r2": 1,
    "q": 1,
    "w": 2,
    "a": 3,
    "b": 3,
    "c": 4,
    "d": 5,
}
assert edge_proper(double_colouring, (("p", "t"), ("r1", "r2")))
assert set(double_colouring.values()) == set(range(6))
assert double_colouring["p"] == double_colouring["t"]
assert double_colouring["r1"] == double_colouring["r2"]
assert {
    double_colouring[v] for v in neighbours("p") - {"t"}
} == {1, 2, 3, 4, 5}
for r, mate in (("r1", "r2"), ("r2", "r1")):
    assert {
        double_colouring[v] for v in neighbours(r) - {mate}
    } == {0, 2, 3, 4, 5}

# The graph is visibly outside the full HC7 kernel: it is four-colourable
# and contains the following literal K7 model.
four_colouring = {
    "s": 0,
    "t": 0,
    "w": 0,
    "p": 1,
    "r1": 1,
    "q": 2,
    "r2": 2,
    "a": 3,
    "b": 3,
    "c": 3,
    "d": 3,
}
assert edge_proper(four_colouring)
model = (
    {"d", "r1", "r2"},
    {"q"},
    {"p"},
    {"c", "t"},
    {"b", "s"},
    {"a"},
    {"w"},
)
check_branch_model(model)

print("vertices", len(V), "edges", len(E), "connectivity", 7)
print("packet_vector", (packing_number(packets_A), packing_number(packets_R)))
print("unique_portal", "p-t", "connector", "t-p-q-s")
print("carrier_splits", len(splits), "list_colourable", False)
print("double_contraction_colouring", double_colouring)
print("thin_and_rich_endpoints_are_five_colour_saturated", True)
print("K7_model", model)
print("violated_full_kernel_inputs", "K7-minor-free, chi=7, minor-criticality")
print("VERIFIED")
