#!/usr/bin/env python3
"""Exact quotient certificate for the three-pole four-bouquet.

The six literal labels induce the weakest one-complex boundary
J=K6-{ab,ac}.  Four lobe vertices have portal pairs pq,pq,pr,pr and
each misses exactly one literal label.  For all 6^4 missed-row profiles
we search an exact K7 branch-set model.  Positive certificates are
replayed from the literal quotient graph.

The other portal multiplicities either contain a three-lobe two-pole
bouquet or contain all three portal types; both have short hand proofs.
Thus this is the sole static allocation row which needs certification.
"""

from __future__ import annotations

from itertools import combinations, permutations, product

from reserved_terminal_specific_web_quotient_verify import e


LABELS = range(6)
PAIRS = ((6, 7), (6, 7), (6, 8), (6, 8))
NAMES = ("a", "b", "c", "q1", "q2", "q3",
         "p", "q", "r", "X1", "X2", "Y1", "Y2")


def edges_for(profile: tuple[int, int, int, int]):
    edges = {
        e(i, j)
        for i in LABELS
        for j in LABELS
        if i < j and (i, j) not in {(0, 1), (0, 2)}
    }
    for index, (pair, missed) in enumerate(zip(PAIRS, profile)):
        lobe = 9 + index
        edges.update(e(lobe, pole) for pole in pair)
        edges.update(e(lobe, label) for label in LABELS if label != missed)
    return edges


def connected(bag: int, edges: set[tuple[int, int]]) -> bool:
    vertices = [v for v in range(13) if bag >> v & 1]
    reached = {vertices[0]}
    while True:
        expanded = reached | {
            y for x in reached for y in vertices if e(x, y) in edges
        }
        if expanded == reached:
            return len(reached) == len(vertices)
        reached = expanded


def verify(model: tuple[int, ...], edges: set[tuple[int, int]]) -> None:
    assert len(model) == 7 and all(model)
    assert not any(model[i] & model[j]
                   for i in range(7) for j in range(i))
    assert all(connected(bag, edges) for bag in model)
    for i in range(7):
        for j in range(i):
            assert any(
                e(x, y) in edges
                for x in range(13) if model[i] >> x & 1
                for y in range(13) if model[j] >> y & 1
            )


def render(model: tuple[int, ...]) -> str:
    return " | ".join(
        "{" + ",".join(NAMES[v] for v in range(13) if bag >> v & 1) + "}"
        for bag in model
    )


def mask(*vertices: int) -> int:
    answer = 0
    for vertex in vertices:
        answer |= 1 << vertex
    return answer


def allocation_model(profile: tuple[int, int, int, int],
                     edges: set[tuple[int, int]], mode: str | None = None):
    """Find one of two uniform seven-bag allocation certificates.

    Template A spends two literal labels on the two secondary pole bags
    and leaves a literal K4.  Template B is the deficient-triangle
    certificate used when every miss is in {a,b,c}.
    """
    groups = ((9, 10, 7), (11, 12, 8))  # lobe pair, noncommon pole

    # P=p+A1+B1, Q=q+A2+x, R=r+B2+y, plus J-{x,y}.
    if mode in (None, "spent-pair"):
        for order in (groups, groups[::-1]):
            (aa, bb, u), (cc, dd, v) = order
            for a1, a2 in permutations((aa, bb)):
                for b1, b2 in permutations((cc, dd)):
                    for x in LABELS:
                        for y in LABELS:
                            if x == y:
                                continue
                            bags = (
                                mask(6, a1, b1),
                                mask(u, a2, x),
                                mask(v, b2, y),
                                *(mask(z) for z in LABELS if z not in {x, y}),
                            )
                            try:
                                verify(bags, edges)
                            except AssertionError:
                                continue
                            return bags, "spent-pair"

    # Four-helper frame.  Choose a literal clique S of order three seen
    # by every lobe, and a row x missed by at most one lobe.  Orient that
    # possible exception as P; x then joins Q to both R and T.
    if mode not in (None, "four-helper"):
        return None
    for singleton_triangle in combinations(LABELS, 3):
        if any(profile[i] in singleton_triangle for i in range(4)):
            continue
        if any(e(u, v) not in edges
               for u, v in combinations(singleton_triangle, 2)):
            continue
        for x in LABELS:
            if x in singleton_triangle:
                continue
            exceptional = [9 + i for i, miss in enumerate(profile) if miss == x]
            if len(exceptional) > 1:
                continue
            for order in (groups, groups[::-1]):
                (aa, bb, u), (cc, dd, v) = order
                for a1, a2 in permutations((aa, bb)):
                    if exceptional and a1 != exceptional[0]:
                        continue
                    for b1, b2 in permutations((cc, dd)):
                        bags = (
                            mask(6, a1),
                            mask(u, a2, x),
                            mask(v, b1),
                            mask(b2),
                            *(mask(z) for z in singleton_triangle),
                        )
                        try:
                            verify(bags, edges)
                        except AssertionError:
                            continue
                        return bags, "four-helper"
    return None


def main() -> None:
    witnesses = {}
    templates = {}
    for profile in product(LABELS, repeat=4):
        edges = edges_for(profile)
        missed = set(profile)
        unmissed = set(LABELS) - missed
        has_unmissed_triangle = any(
            set(triangle) <= unmissed
            and all(e(u, v) in edges for u, v in combinations(triangle, 2))
            for triangle in combinations(LABELS, 3)
        )
        required = "four-helper" if has_unmissed_triangle else "spent-pair"
        answer = allocation_model(profile, edges, required)
        assert answer is not None, profile
        model, template = answer
        verify(model, edges)
        witnesses[profile] = model
        templates[profile] = template
    print("profiles", len(witnesses))
    print("K7-positive", len(witnesses))
    print("spent-pair", sum(value == "spent-pair" for value in templates.values()))
    print("four-helper", sum(value == "four-helper" for value in templates.values()))
    for profile in ((0, 0, 0, 0), (1, 1, 1, 1),
                    (0, 1, 2, 3), (3, 4, 5, 1)):
        print(profile, render(witnesses[profile]))


if __name__ == "__main__":
    main()
