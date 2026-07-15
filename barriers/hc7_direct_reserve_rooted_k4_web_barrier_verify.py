#!/usr/bin/env python3
"""Solver-free replay of the direct-reserve rooted-K4 web barrier."""

from __future__ import annotations

from itertools import combinations, product


ROOTS = ("z", "x", "y", "r")
INTERNAL = ("t1", "t3", "t5")
J_VERTICES = set(ROOTS + INTERNAL)


def edge(left: str, right: str) -> tuple[str, str]:
    assert left != right
    return tuple(sorted((left, right)))


J_EDGES = {
    edge("x", "t1"),
    edge("x", "t3"),
    edge("x", "y"),
    edge("x", "t5"),
    edge("t1", "z"),
    edge("t1", "t5"),
    edge("t1", "r"),
    edge("z", "t3"),
    edge("z", "t5"),
    edge("t3", "y"),
    edge("t3", "t5"),
}


def connected(vertices: set[str], edges: set[tuple[str, str]]) -> bool:
    if not vertices:
        return False
    reached = {next(iter(vertices))}
    while True:
        larger = reached | {
            vertex
            for vertex in vertices - reached
            if any(edge(vertex, old) in edges for old in reached)
        }
        if larger == reached:
            return reached == vertices
        reached = larger


def adjacent(
    left: set[str], right: set[str], edges: set[tuple[str, str]]
) -> bool:
    return any(edge(x, y) in edges for x in left for y in right)


DIAMOND = ({"z", "t3", "t5"}, {"x"}, {"y"}, {"r", "t1"})
assert all(connected(bag, J_EDGES) for bag in DIAMOND)
assert all(left.isdisjoint(right) for left, right in combinations(DIAMOND, 2))
missing = {
    (i, j)
    for i, j in combinations(range(4), 2)
    if not adjacent(DIAMOND[i], DIAMOND[j], J_EDGES)
}
assert missing == {(2, 3)}


def has_rooted_k4() -> bool:
    # Every rooted model is represented by assigning each nonroot either
    # to one of the four root bags or to the unused state 4.
    for assignment in product(range(5), repeat=len(INTERNAL)):
        bags = [{root} for root in ROOTS]
        for vertex, label in zip(INTERNAL, assignment):
            if label < 4:
                bags[label].add(vertex)
        if not all(connected(bag, J_EDGES) for bag in bags):
            continue
        if all(
            adjacent(bags[i], bags[j], J_EDGES)
            for i, j in combinations(range(4), 2)
        ):
            return True
    return False


assert not has_rooted_k4()

# Internal rooted four-connectivity: deleting fewer than four vertices
# leaves no component without a surviving root.
for order in range(4):
    for deleted_tuple in combinations(J_VERTICES, order):
        deleted = set(deleted_tuple)
        remaining = J_VERTICES - deleted
        unseen = set(remaining)
        while unseen:
            component = {next(iter(unseen))}
            while True:
                larger = component | {
                    vertex
                    for vertex in remaining - component
                    if any(edge(vertex, old) in J_EDGES for old in component)
                }
                if larger == component:
                    break
                component = larger
            unseen -= component
            assert component & (set(ROOTS) - deleted)

# Extend to the literal seven-boundary path.
S = {"x", "y", "b", "c", "r", "a", "u"}
A = {"z", "t1", "t3", "t5"}
H_PATH = ("x", "y", "b", "c", "r", "a", "u")
E = set(J_EDGES)
E |= {edge(H_PATH[i], H_PATH[i + 1]) for i in range(len(H_PATH) - 1)}
E.add(edge("z", "u"))
E |= {edge(boundary, inside) for boundary in ("a", "b", "c") for inside in A}

assert {inside for inside in A if edge(inside, "u") in E} == {"z"}
assert edge("z", "x") not in E and edge("z", "y") not in E
assert edge("z", "r") not in E
assert connected(A - {"z"}, E)
assert all(any(edge(w, inside) in E for inside in A - {"z"}) for w in S - {"u"})

# Relative seven-cut inequality for every connected nonempty A-side set.
for size in range(1, len(A) + 1):
    for chosen in combinations(A, size):
        D = set(chosen)
        if not connected(D, E):
            continue
        neighbours_a = {v for v in A - D if any(edge(v, d) in E for d in D)}
        neighbours_s = {v for v in S if any(edge(v, d) in E for d in D)}
        assert len(neighbours_a) + len(neighbours_s) >= 7

# The canonical reserved component after deleting x,y,r.
H_REMAINING = S - {"x", "y", "r"}
assert connected({"a", "u"}, E)
assert not any(edge(v, w) in E for v in {"a", "u"} for w in {"b", "c"})
assert edge("u", "z") in E and edge("a", "r") in E

# Explicit adaptive-carrier terminal.
C0 = {"t1"}
C1 = {"t3", "z"}
I0 = {"x", "b", "a"}
I1 = {"y", "c", "u"}
assert connected(C0, E) and connected(C1, E) and adjacent(C0, C1, E)
assert all(edge(left, right) not in E for left, right in combinations(I0, 2))
assert all(edge(left, right) not in E for left, right in combinations(I1, 2))
assert all(any(edge(carrier, literal) in E for carrier in C0) for literal in I0)
assert all(any(edge(carrier, literal) in E for carrier in C1) for literal in I1)

print("GREEN: exact cofacial rooted-diamond barrier; adaptive carrier exit verified")
