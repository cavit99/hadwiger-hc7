#!/usr/bin/env python3
"""Exact N-meeting K6-minor check for a cutvertex split of one exterior.

Vertices 0,...,6 induce the pure Moser spindle.  Vertices 7 and 8
represent disjoint connected adjacent shores.  Each shore has boundary
defect at most one, and the two nonempty defects are distinct.
"""

from itertools import combinations

N = set(range(7))
M_EDGES = {
    (0, 1), (0, 2), (0, 3), (0, 4),
    (1, 2), (1, 6), (2, 6),
    (3, 4), (3, 5), (4, 5), (5, 6),
}


def quotient_edges(d_1, d_2):
    edges = {frozenset(e) for e in M_EDGES}
    edges.add(frozenset((7, 8)))
    for shore, defect in ((7, d_1), (8, d_2)):
        for n in N - defect:
            edges.add(frozenset((shore, n)))
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
    vertices = tuple(range(9))
    for size in range(6, 10):
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


def fmt(defect):
    return "-" if not defect else str(next(iter(defect)))


def canonical_model(model):
    return tuple(sorted(tuple(sorted(bag)) for bag in model))


defects = [set()] + [{i} for i in sorted(N)]
failures = []
models = {}
for d_1 in defects:
    for d_2 in defects:
        if d_1 and d_1 == d_2:
            continue
        model = find_model(d_1, d_2)
        if model is None:
            failures.append((d_1, d_2))
        else:
            models[(fmt(d_1), fmt(d_2))] = canonical_model(model)

print(f"tested={len(models) + len(failures)} failures={len(failures)}")
for pair in failures:
    print("failure", fmt(pair[0]), fmt(pair[1]))

# Print distinct witnesses; symmetry between the two shore labels is retained.
for key in sorted(models):
    print(key, models[key])

