#!/usr/bin/env python3
"""Certificates for the bilateral same-bag saturation obstruction.

The script is deliberately dependency-free.  It verifies

* the width-five chordal completion of the conservative quotient;
* three differently rooted K7-minus-edge models;
* nine explicit Kuratowski subdivisions with vertex transversal number 3;
* the absence of a K6-minus-edge subgraph (and hence of a near-K7 model
  having six singleton bags).
"""

from itertools import combinations

from degree9_opposite_bypass_quotient_probe import (
    ELIMINATION_ORDER,
    build,
    verify_width_five_completion,
)


V, E0 = build()
E = {frozenset(edge) for edge in E0}


def adjacent_sets(a, b, edges=E):
    return any(frozenset((x, y)) in edges for x in a for y in b if x != y)


def connected_set(bag, edges=E):
    bag = set(bag)
    reached = {next(iter(bag))}
    while True:
        nxt = reached | {
            x for x in bag
            if any(frozenset((x, y)) in edges for y in reached if x != y)
        }
        if nxt == reached:
            return reached == bag
        reached = nxt


def missing_pairs(model, edges=E):
    assert all(connected_set(bag, edges) for bag in model)
    assert sum(map(len, model)) == len(set().union(*model))
    return [
        (i, j)
        for i, j in combinations(range(len(model)), 2)
        if not adjacent_sets(model[i], model[j], edges)
    ]


MODELS = {
    # The added edge U-C joins bags 3 and 5.
    "UC": [
        {"h"}, {"1"}, {"2"}, {"U"}, {"L0"}, {"v", "C"},
        {"D", "R0"},
    ],
    # The added edge V-D joins bags 3 and 5 in the symmetric model.
    "VD": [
        {"h"}, {"3"}, {"4"}, {"V"}, {"R0"}, {"v", "D"},
        {"C", "L0"},
    ],
    # The added edge U-V joins the first deficient bag to the bag
    # containing V (the latter is already connected through v-3-V).
    "UV": [
        {"U"}, {"v", "3", "V"}, {"h"}, {"1"}, {"2"},
        {"4", "D", "C"}, {"L0", "R0"},
    ],
}


def verify_near_models():
    completion_edges = {
        "UC": frozenset(("U", "C")),
        "VD": frozenset(("V", "D")),
        "UV": frozenset(("U", "V")),
    }
    for name, model in MODELS.items():
        miss = missing_pairs(model)
        assert len(miss) == 1, (name, miss)
        completed = set(E)
        completed.add(completion_edges[name])
        assert missing_pairs(model, completed) == []


def has_all_edges(xs, ys):
    return all(frozenset((x, y)) in E for x in xs for y in ys if x != y)


# Nine nonplanar subgraphs.  The entries are (vertex set, type, data).
# K5s and K3,3s are literal.  A subdivision entry records the branch
# vertices/parts and one subdivided edge x-z-y.
WITNESSES = [
    ({"1", "2", "L0", "U", "h"}, "K5", None),
    ({"3", "4", "R0", "V", "h"}, "K5", None),
    ({"1", "2", "C", "D", "L0", "v"}, "K33",
     ({"1", "2", "C"}, {"D", "L0", "v"})),
    ({"3", "4", "C", "D", "R0", "v"}, "K33",
     ({"3", "4", "D"}, {"C", "R0", "v"})),
    ({"C", "D", "L0", "R0", "U", "h", "v"}, "K33sub",
     ({"C", "R0", "U"}, {"D", "L0", "h"}, ("C", "v", "h"))),
    ({"1", "2", "D", "U", "h", "v"}, "K5sub",
     ({"1", "2", "D", "U", "h"}, ("D", "v", "h"))),
    ({"3", "4", "C", "V", "h", "v"}, "K5sub",
     ({"3", "4", "C", "V", "h"}, ("C", "v", "h"))),
    ({"1", "2", "D", "L0", "R0", "U"}, "K5sub",
     ({"1", "2", "D", "L0", "U"}, ("D", "R0", "L0"))),
    ({"3", "4", "C", "L0", "R0", "V"}, "K5sub",
     ({"3", "4", "C", "R0", "V"}, ("C", "L0", "R0"))),
]


def verify_kuratowski_witnesses():
    for vertices, kind, data in WITNESSES:
        if kind == "K5":
            assert has_all_edges(vertices, vertices)
        elif kind == "K33":
            left, right = data
            assert left | right == vertices and not left & right
            assert has_all_edges(left, right)
        elif kind == "K5sub":
            branch, (x, z, y) = data
            assert vertices == branch | {z}
            assert frozenset((x, z)) in E and frozenset((z, y)) in E
            assert all(
                frozenset((a, b)) in E
                for a, b in combinations(branch, 2)
                if {a, b} != {x, y}
            )
        elif kind == "K33sub":
            left, right, (x, z, y) = data
            assert vertices == left | right | {z}
            assert x in left and y in right
            assert frozenset((x, z)) in E and frozenset((z, y)) in E
            assert all(
                frozenset((a, b)) in E
                for a in left for b in right if {a, b} != {x, y}
            )
        else:
            raise AssertionError(kind)

    # Every pair of possible apices avoids at least one Kuratowski witness.
    for a, b in combinations(V, 2):
        assert any(a not in S and b not in S for S, _, _ in WITNESSES), (a, b)


def verify_no_k6_minus_edge_subgraph():
    k5s = {
        frozenset(five)
        for five in combinations(V, 5)
        if all(frozenset(pair) in E for pair in combinations(five, 2))
    }
    assert k5s == {
        frozenset(("h", "1", "2", "U", "L0")),
        frozenset(("h", "3", "4", "V", "R0")),
    }
    for six in combinations(V, 6):
        present = sum(frozenset(pair) in E for pair in combinations(six, 2))
        assert present <= 13, (six, present)


def main():
    bags = verify_width_five_completion(V, E)
    assert tuple(x for x, _ in bags) == ELIMINATION_ORDER
    assert max(len(bag) - 1 for _, bag in bags) == 5
    verify_near_models()
    verify_kuratowski_witnesses()
    verify_no_k6_minus_edge_subgraph()
    print("width-five certificate: PASS")
    print("three port-labelled K7^- models: PASS")
    print("nine Kuratowski witnesses, apex transversal >= 3: PASS")
    print("no K6^- subgraph / no one-complex-bag K7^- model: PASS")


if __name__ == "__main__":
    main()
