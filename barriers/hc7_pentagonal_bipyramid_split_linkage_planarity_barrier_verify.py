#!/usr/bin/env python3
"""Verify the PB split/linkage/planarity barrier without dependencies."""

from itertools import combinations, product


V = tuple((x, i) for x in range(7) for i in range(2))
E = {frozenset(((x, 0), (x, 1))) for x in range(7)}
CROSS = (
    (1,0,2,1),(0,0,4,1),(3,0,4,0),(3,1,4,0),(3,1,4,1),
    (1,0,5,0),(1,1,5,0),(1,1,5,1),(0,0,3,1),(1,0,4,0),
    (0,1,6,0),(0,1,6,1),(2,0,3,0),(2,0,3,1),(2,1,3,0),
    (0,0,2,0),(0,0,2,1),(0,1,2,0),(0,1,2,1),(4,0,5,0),
    (4,1,5,0),(4,1,5,1),(2,1,6,0),(5,1,6,1),(0,1,5,1),
    (1,0,6,0),(1,0,6,1),(1,1,6,0),(1,1,6,1),(1,0,3,0),
)
E.update(frozenset(((x, i), (y, j))) for x, i, y, j in CROSS)

PB = {frozenset((p, r)) for p in (0, 1) for r in range(2, 7)}
PB.update(frozenset((2 + i, 2 + ((i + 1) % 5))) for i in range(5))

ORDER = {0: (2,3,4,5,6), 1: (2,6,5,4,3)}
for i in range(5):
    ORDER[2+i] = (0, 2+((i+1)%5), 1, 2+((i-1)%5))


def adjacent(u, v):
    return u != v and frozenset((u, v)) in E


def connected(vertices):
    vertices = set(vertices)
    if not vertices:
        return False
    seen = {next(iter(vertices))}
    stack = list(seen)
    while stack:
        u = stack.pop()
        for v in vertices - seen:
            if adjacent(u, v):
                seen.add(v)
                stack.append(v)
    return seen == vertices


def meets(vertices, label):
    return any(adjacent(v, (label, j)) for v in vertices for j in range(2))


# Exact PB contact graph and induced two-vertex paths.
for x, y in combinations(range(7), 2):
    contact = any(adjacent((x, i), (y, j)) for i in range(2) for j in range(2))
    assert contact == (frozenset((x, y)) in PB)
for x in range(7):
    assert adjacent((x, 0), (x, 1))

# Connectivity at least five by exhaustive deletion; degree gives at most five.
for size in range(5):
    for deleted in combinations(V, size):
        assert connected(set(V) - set(deleted))
degrees = {v: sum(adjacent(v, w) for w in V) for v in V}
assert min(degrees.values()) == 5

# No four-label alternating internal path cut.
for x in range(7):
    sides = []
    for i in range(2):
        sides.append({y for y in ORDER[x] if meets({(x, i)}, y)})
    for positions in combinations(range(len(ORDER[x])), 4):
        q = tuple(ORDER[x][j] for j in positions)
        assert not (q[0] in sides[0] and q[1] in sides[1]
                    and q[2] in sides[0] and q[3] in sides[1])
        assert not (q[0] in sides[1] and q[1] in sides[0]
                    and q[2] in sides[1] and q[3] in sides[0])

# Every adjacent-rim linkage instance is negative.
for i in range(5):
    ci, cj = 2+i, 2+((i+1)%5)
    left, right = 2+((i-1)%5), 2+((i+2)%5)
    universe = ((ci,0),(ci,1),(cj,0),(cj,1))
    found = False
    for assignment in product((0, 1, 2), repeat=4):
        xset = {v for v, mark in zip(universe, assignment) if mark == 1}
        yset = {v for v, mark in zip(universe, assignment) if mark == 2}
        if (connected(xset) and connected(yset)
                and meets(xset, 0) and meets(xset, 1)
                and meets(yset, left) and meets(yset, right)):
            found = True
            break
    assert not found

# Explicit K3,3 subdivision.
left = ((4,0),(5,1),(6,0))
right = ((4,1),(5,0),(6,1))
paths = (
    ((4,0),(4,1)), ((4,0),(5,0)), ((4,0),(3,0),(1,0),(6,1)),
    ((5,1),(4,1)), ((5,1),(5,0)), ((5,1),(6,1)),
    ((6,0),(2,1),(2,0),(3,1),(4,1)),
    ((6,0),(1,1),(5,0)), ((6,0),(6,1)),
)
interiors = []
for path in paths:
    assert path[0] in left and path[-1] in right
    assert all(adjacent(path[j], path[j+1]) for j in range(len(path)-1))
    interiors.extend(path[1:-1])
assert len(interiors) == len(set(interiors))
assert not (set(interiors) & (set(left) | set(right)))

# Explicit anchored K5 model.
bags = (
    {(6,0),(6,1)},
    {(4,0),(4,1),(2,1),(0,0)},
    {(3,0),(3,1),(2,0),(0,1)},
    {(1,0),(1,1)},
    {(5,0),(5,1)},
)
assert len(set().union(*bags)) == sum(map(len, bags))
assert all(connected(bag) for bag in bags)
for first, second in combinations(bags, 2):
    assert any(adjacent(u, v) for u in first for v in second)
for bag, label in zip(bags, (6,4,3,1,5)):
    assert {(label,0),(label,1)} <= bag

print("pentagonal-bipyramid split/linkage/planarity barrier: PASS")
