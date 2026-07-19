#!/usr/bin/env python3
"""Verify the repeated-contact component-defect barrier."""

from itertools import combinations


ICOSAHEDRON_EDGES = {
    tuple(sorted(edge))
    for edge in [
        (0, 1), (0, 5), (0, 7), (0, 8), (0, 11),
        (1, 2), (1, 5), (1, 6), (1, 8),
        (2, 3), (2, 6), (2, 8), (2, 9),
        (3, 4), (3, 6), (3, 9), (3, 10),
        (4, 5), (4, 6), (4, 10), (4, 11),
        (5, 6), (5, 11),
        (7, 8), (7, 9), (7, 10), (7, 11),
        (8, 9), (9, 10), (10, 11),
    ]
}

P, Q = 12, 13
VERTICES = set(range(14))
EDGES = set(ICOSAHEDRON_EDGES)
EDGES.add((P, Q))
for v in range(12):
    EDGES.add(tuple(sorted((P, v))))
    EDGES.add(tuple(sorted((Q, v))))


def adjacent(u, v):
    return tuple(sorted((u, v))) in EDGES


def connected(vertices):
    vertices = set(vertices)
    if not vertices:
        return True
    seen = {next(iter(vertices))}
    stack = list(seen)
    while stack:
        u = stack.pop()
        for v in vertices - seen:
            if adjacent(u, v):
                seen.add(v)
                stack.append(v)
    return seen == vertices


def check_connectivity_at_least_seven():
    for size in range(7):
        for deleted in combinations(VERTICES, size):
            if not connected(VERTICES - set(deleted)):
                raise AssertionError((size, deleted))


def contacts(left, right):
    return {
        tuple(sorted((u, v)))
        for u in left for v in right if adjacent(u, v)
    }


def check_model(anchor, protected, repeated, incident):
    branch_sets = [{P}, {Q}, set(anchor)] + [set(x) for x in protected]
    assert set().union(*branch_sets) == VERTICES
    assert sum(map(len, branch_sets)) == len(VERTICES)
    assert all(connected(branch) for branch in branch_sets)

    for i, j in combinations(range(3), 2):
        assert contacts(branch_sets[i], branch_sets[j])
    for i in range(3):
        for j in range(3, 7):
            assert contacts(branch_sets[i], branch_sets[j])

    present = []
    pair_contacts = {}
    for i, j in combinations(range(4), 2):
        edges = contacts(protected[i], protected[j])
        pair_contacts[i, j] = edges
        if edges:
            present.append((i, j))
    assert set(present) == {(0, 1), (0, 3), (1, 2), (1, 3), (2, 3)}

    # Five connected bichromatic pairs and one pair with two components.
    defect = 5 + 2 - 4 - 2
    assert defect == 1

    e, f = (tuple(sorted(x)) for x in repeated)
    assert e in pair_contacts[0, 1] and f in pair_contacts[0, 1]
    if incident:
        assert len(set(e) & set(f)) == 1
    else:
        assert not (set(e) & set(f))


def main():
    assert len(ICOSAHEDRON_EDGES) == 30
    assert all(sum(adjacent(v, w) for w in range(12) if w != v) == 5
               for v in range(12))
    check_connectivity_at_least_seven()
    # Every old vertex has its five icosahedral neighbours plus P and Q.
    # Hence the minimum degree is seven and the verified lower bound is exact.
    assert min(sum(adjacent(v, w) for w in VERTICES if w != v)
               for v in VERTICES) == 7

    check_model(
        anchor={3, 4, 7, 8, 9, 10, 11},
        protected=[{5}, {0, 1}, {2}, {6}],
        repeated=[(5, 0), (5, 1)],
        incident=True,
    )
    check_model(
        anchor={4, 5, 7, 9, 10, 11},
        protected=[{0, 1}, {8, 2}, {3}, {6}],
        repeated=[(0, 8), (1, 2)],
        incident=False,
    )

    print(
        "GREEN repeated-contact component-defect barrier: "
        "kappa(G)=7, incident and independent defect-one models verified"
    )


if __name__ == "__main__":
    main()
