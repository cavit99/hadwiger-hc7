#!/usr/bin/env python3
"""Exact N-meeting K6-minor check for the 2-cut quotient graphs.

Vertices 0,...,6 are boundary vertices.  Vertices 7,8 represent the two
connected adjacent shores.  This script checks every set partition of
every used vertex subset into six nonempty bags, with each bag required
to meet the boundary.
"""

from itertools import combinations

N = set(range(7))
U = {0, 2, 4, 5, 6}
M_EDGES = {
    (0, 1), (0, 2), (0, 3), (0, 4),
    (1, 2), (1, 6), (2, 6),
    (3, 4), (3, 5), (4, 5), (5, 6),
}

ANCHOR_RESIDUAL = {
    (5, 2): [
        ({2}, {3, 5}), ({4}, {1, 2}), ({5}, {1, 2}),
        ({0, 2}, {3, 5}), ({0, 4}, {1, 2}), ({0, 5}, {1, 2}),
        ({1, 2}, {3, 4}), ({1, 2}, {3, 5}), ({1, 2}, {4, 5}),
        ({1, 2}, {4, 6}), ({1, 2}, {5, 6}), ({1, 6}, {3, 4}),
        ({2, 4}, {3, 5}), ({2, 4}, {5, 6}), ({2, 6}, {3, 5}),
    ],
    (2, 4): [
        ({2}, {3, 4}), ({4}, {1, 2}), ({5}, {1, 2}), ({6}, {3, 4}),
        ({0, 2}, {3, 4}), ({0, 4}, {1, 2}), ({0, 5}, {1, 2}),
        ({0, 6}, {3, 4}), ({1, 2}, {3, 4}), ({1, 2}, {3, 5}),
        ({1, 2}, {4, 5}), ({1, 2}, {4, 6}), ({1, 2}, {5, 6}),
        ({1, 6}, {3, 4}), ({1, 6}, {3, 5}), ({2, 4}, {5, 6}),
        ({2, 5}, {3, 4}), ({2, 5}, {4, 6}), ({2, 6}, {3, 4}),
        ({3, 4}, {5, 6}),
    ],
    (4, 6): [
        ({2}, {3, 4}), ({4}, {1, 6}), ({6}, {3, 4}),
        ({0, 2}, {3, 4}), ({0, 4}, {1, 6}), ({0, 6}, {3, 4}),
        ({1, 2}, {3, 4}), ({1, 2}, {3, 5}), ({1, 6}, {2, 4}),
        ({1, 6}, {3, 4}), ({1, 6}, {4, 5}), ({2, 4}, {5, 6}),
        ({2, 5}, {3, 4}), ({2, 6}, {3, 4}), ({3, 4}, {5, 6}),
    ],
}

EXPECTED_FINAL = {
    (5, 2): [
        ({2}, {3, 5}), ({5}, {1, 2}), ({0, 2}, {3, 5}),
        ({0, 5}, {1, 2}), ({1, 2}, {3, 5}), ({1, 2}, {4, 5}),
        ({1, 2}, {5, 6}), ({1, 6}, {3, 4}), ({2, 4}, {3, 5}),
        ({2, 4}, {5, 6}), ({2, 6}, {3, 5}),
    ],
    (2, 4): [
        ({2}, {3, 4}), ({4}, {1, 2}), ({0, 2}, {3, 4}),
        ({0, 4}, {1, 2}), ({1, 2}, {3, 4}), ({1, 2}, {4, 5}),
        ({1, 2}, {4, 6}), ({1, 6}, {3, 5}), ({2, 5}, {3, 4}),
        ({2, 5}, {4, 6}), ({2, 6}, {3, 4}),
    ],
    (4, 6): [
        ({4}, {1, 6}), ({6}, {3, 4}), ({0, 4}, {1, 6}),
        ({0, 6}, {3, 4}), ({1, 2}, {3, 5}), ({1, 6}, {2, 4}),
        ({1, 6}, {3, 4}), ({1, 6}, {4, 5}), ({2, 4}, {5, 6}),
        ({2, 6}, {3, 4}), ({3, 4}, {5, 6}),
    ],
}


def quotient_edges(missing, d_1, d_2):
    edges = {frozenset(e) for e in M_EDGES}
    edges.add(frozenset((7, 8)))
    for shore, defect in ((7, d_1), (8, d_2)):
        for n in N - defect:
            edges.add(frozenset((shore, n)))
    for a, b in combinations(sorted(U), 2):
        if {a, b} != set(missing):
            edges.add(frozenset((a, b)))
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


def find_model(missing, d_1, d_2):
    edges = quotient_edges(missing, d_1, d_2)
    vertices = tuple(range(9))
    for size in range(6, 10):
        for used in combinations(vertices, size):
            # Restricted-growth strings enumerate each partition once.
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


for missing, pairs in ANCHOR_RESIDUAL.items():
    final = []
    for a, b in pairs:
        d_1, d_2 = set(a), set(b)
        if find_model(missing, d_1, d_2) is None:
            final.append((d_1, d_2))
    assert final == EXPECTED_FINAL[missing], (missing, final)

print("Moser 2-cut quotient models verified")
for missing, pairs in EXPECTED_FINAL.items():
    print(f"edge={missing}: {len(pairs)} final unordered residual pairs")
    print(" ".join(
        f"[{''.join(map(str, sorted(a))) or '-'}|"
        f"{''.join(map(str, sorted(b))) or '-'}]"
        for a, b in pairs
    ))

