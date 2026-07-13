#!/usr/bin/env python3
"""Verify the K4-anchor closure for every cutvertex-lobe defect pair."""

from itertools import combinations


S = ("v", "h", "1", "2", "5", "6", "z")
QH = frozenset(("v", "h", "1", "2"))
Q6 = frozenset(("v", "6", "1", "2"))
X, Y, D = "X", "Y", "D"


def norm(e):
    return tuple(sorted(e))


BOUNDARY = {norm(e) for e in (
    ("v", "h"), ("v", "1"), ("v", "2"),
    ("h", "1"), ("h", "2"), ("1", "2"),
    ("v", "5"), ("v", "6"), ("1", "6"),
    ("2", "6"), ("5", "6"),
)}


def assignment(dx, dy):
    for clique in (QH, Q6):
        outside = tuple(s for s in S if s not in clique)
        choices = []
        for defect in (dx, dy):
            choices.append(tuple(
                a for a in outside
                if a != defect
                and (defect is None or defect not in clique
                     or norm((a, defect)) in BOUNDARY)
            ))
        for ax in choices[0]:
            for ay in choices[1]:
                if ax != ay:
                    return clique, ax, ay
    return None


def connected(bag, edges):
    reached = {next(iter(bag))}
    while True:
        nxt = reached | {b for a in reached for b in bag
                         if norm((a, b)) in edges}
        if nxt == reached:
            return reached == bag
        reached = nxt


def adjacent(a, b, edges):
    return any(norm((x, y)) in edges for x in a for y in b)


def main():
    defects = (None,) + S
    failures = []
    checked = 0
    for dx in defects:
        for dy in defects:
            if dx is not None and dx == dy:
                # Fullness of X union Y excludes a common defect.
                continue
            witness = assignment(dx, dy)
            if witness is None:
                failures.append((dx, dy))
                continue
            clique, ax, ay = witness
            edges = set(BOUNDARY)
            edges.add(norm((X, Y)))
            edges |= {norm((X, s)) for s in S if s != dx}
            edges |= {norm((Y, s)) for s in S if s != dy}
            edges |= {norm((D, s)) for s in S}
            bags = tuple({q} for q in clique) + (
                {D}, {X, ax}, {Y, ay},
            )
            assert all(connected(set(b), edges) for b in bags)
            assert all(set(a).isdisjoint(b)
                       for a, b in combinations(bags, 2))
            assert all(adjacent(set(a), set(b), edges)
                       for a, b in combinations(bags, 2))
            checked += 1
    assert failures == [("1", "2"), ("2", "1")]
    print(f"verified {checked} cutvertex defect pairs")
    print("only residual ordered pairs: 1|2 and 2|1")


if __name__ == "__main__":
    main()
