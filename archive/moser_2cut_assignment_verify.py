#!/usr/bin/env python3
"""Finite anchor audit for a 2-cut in the Moser 4+1 component."""

from itertools import combinations, product

N = set(range(7))
U = {0, 2, 4, 5, 6}
M_EDGES = {
    (0, 1), (0, 2), (0, 3), (0, 4),
    (1, 2), (1, 6), (2, 6),
    (3, 4), (3, 5), (4, 5), (5, 6),
}
M_EDGES |= {(b, a) for a, b in tuple(M_EDGES)}


def closes(edge, omitted, d_1, d_2):
    retained = U - {omitted}
    available = (omitted, 1, 3)
    # 0 means unused; 1 and 2 assign the anchor to that shore.
    for labels in product((0, 1, 2), repeat=3):
        anchors = [set(), set()]
        for a, label in zip(available, labels):
            if label:
                anchors[label - 1].add(a)
        if not anchors[0] or not anchors[1]:
            continue
        valid = True
        for defect, chosen in ((d_1, anchors[0]), (d_2, anchors[1])):
            # An anchor in the defect set has no neighbour in the shore.
            if defect & chosen:
                valid = False
                break
            # Every missed retained root needs a Moser edge to an anchor.
            for u in defect & retained:
                if not any((u, a) in M_EDGES for a in chosen):
                    valid = False
                    break
        if valid:
            return True
    return False


DEFECTS = [frozenset(s) for k in range(3) for s in combinations(N, k)]


def residual(edge):
    bad = []
    for i, d_1 in enumerate(DEFECTS):
        for d_2 in DEFECTS[i:]:
            if d_1 & d_2:
                continue
            if not any(
                closes(edge, omitted, a, b)
                for omitted in edge
                for a, b in ((d_1, d_2), (d_2, d_1))
            ):
                bad.append((d_1, d_2))
    return bad


EXPECTED = {
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

for edge, expected in EXPECTED.items():
    got = residual(edge)
    want = [(frozenset(a), frozenset(b)) for a, b in expected]
    assert got == want, (edge, got, want)

print("Moser 2-cut anchor residual verified")
for edge in EXPECTED:
    print(f"edge={edge}: {len(EXPECTED[edge])} unordered residual pairs")
    print(" ".join(
        f"[{''.join(map(str, sorted(a))) or '-'}|"
        f"{''.join(map(str, sorted(b))) or '-'}]"
        for a, b in EXPECTED[edge]
    ))

