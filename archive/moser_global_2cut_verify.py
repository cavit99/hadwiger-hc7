#!/usr/bin/env python3
"""Exhaust all N-meeting K6 models in global pure-Moser 2-cut quotients."""

from itertools import combinations

N = set(range(7))
M_EDGES = {
    (0, 1), (0, 2), (0, 3), (0, 4),
    (1, 2), (1, 6), (2, 6),
    (3, 4), (3, 5), (4, 5), (5, 6),
}
DEFECTS = [set(s) for k in range(3) for s in combinations(sorted(N), k)]
EXPECTED = [({1, 3}, {2, 4}), ({1, 4}, {2, 3})]


def quotient_edges(d_1, d_2):
    edges = {frozenset(e) for e in M_EDGES}
    # Vertices 7,8 are adjacent shores from one split component.
    # Vertex 9 is the other full-attachment exterior component.
    edges.add(frozenset((7, 8)))
    for shore, defect in ((7, d_1), (8, d_2), (9, set())):
        for x in N - defect:
            edges.add(frozenset((shore, x)))
    return edges


def connected(bag, edges):
    reached = {next(iter(bag))}
    while True:
        more = {
            y for x in reached for y in bag - reached
            if frozenset((x, y)) in edges
        }
        if not more:
            return reached == bag
        reached |= more


def adjacent(a, b, edges):
    return any(frozenset((x, y)) in edges for x in a for y in b)


def find_model(d_1, d_2):
    edges = quotient_edges(d_1, d_2)
    vertices = tuple(range(10))
    for size in range(6, 11):
        for used in combinations(vertices, size):
            labels = [0]

            def search(index, maximum):
                if index == size:
                    if maximum != 5:
                        return None
                    bags = [set() for _ in range(6)]
                    for vertex, label in zip(used, labels):
                        bags[label].add(vertex)
                    if not all(bag & N for bag in bags):
                        return None
                    if not all(connected(bag, edges) for bag in bags):
                        return None
                    if not all(
                        adjacent(bags[i], bags[j], edges)
                        for i in range(6) for j in range(i)
                    ):
                        return None
                    return bags
                for label in range(min(maximum + 1, 5) + 1):
                    labels.append(label)
                    model = search(index + 1, max(maximum, label))
                    if model is not None:
                        return model
                    labels.pop()
                return None

            model = search(1, 0)
            if model is not None:
                return model
    return None


tested = 0
failures = []
for i, d_1 in enumerate(DEFECTS):
    for d_2 in DEFECTS[i:]:
        if d_1 & d_2:
            continue
        tested += 1
        if find_model(d_1, d_2) is None:
            failures.append((d_1, d_2))

assert tested == 260
assert failures == EXPECTED, failures
print("verified 260 global two-cut quotients; residual=2")
print(failures)

