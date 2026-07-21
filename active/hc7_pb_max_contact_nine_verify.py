#!/usr/bin/env python3
"""
Finite laboratory checks for the maximum-contact PB programme
(active/hc7_pb_max_contact_nine_four_colour.md, Section 4).

Scope (explicit, finite):
  Two-vertex path-column expansions of the pentagonal bipyramid on 14 vertices.
  A = layer 0, B = layer 1.  Exhaustive five-part AB spanning partition search
  with no bag-size cutoff for contact counts.

Checks:
  (1) Canonical pack (poles separate; rim pairs 2∪3, 4, 5∪6) has contact 9
      on every host with exact PB contact graph.
  (2) Every five-connected host in the tested family has c*=10.
  (3) Every tested host with c*≤9 is four-colourable and not five-connected.

Invocation:
  /usr/bin/python3 active/hc7_pb_max_contact_nine_verify.py
"""

from __future__ import annotations

import sys
from itertools import product
from pathlib import Path
from random import Random

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from active.hc7_pb_paired_rooted_adversarial_probe import (  # noqa: E402
    A_MASK14,
    ALL_V14,
    AUDITED_CROSS,
    B_MASK14,
    FOUR_COLOUR_WORDS,
    FULL14,
    IDX14,
    PB_EDGES,
    build_adj14,
    contact_edge_count,
    cross_from_tuples,
    cross_from_words,
    enumerate_five_part_ab_spanning,
    four_colourable,
    full_bundles14,
    is_connected_mask,
    mask_meets_ab,
    node_connectivity_ge5,
)


def column_mask(lab: int) -> int:
    return (1 << IDX14[(lab, 0)]) | (1 << IDX14[(lab, 1)])


def canonical_pack() -> tuple:
    return (
        column_mask(0),
        column_mask(1),
        column_mask(2) | column_mask(3),
        column_mask(4),
        column_mask(5) | column_mask(6),
    )


def assert_canonical_nine(adj) -> None:
    parts = canonical_pack()
    for p in parts:
        assert is_connected_mask(adj, p)
        assert mask_meets_ab(p, A_MASK14, B_MASK14)
    assert sum(bin(p).count("1") for p in parts) == 14
    c = contact_edge_count(adj, parts)
    assert c == 9, c


def c_star(adj) -> int:
    parts = enumerate_five_part_ab_spanning(adj, A_MASK14, B_MASK14, FULL14)
    if not parts:
        return -1
    return max(contact_edge_count(adj, p) for p in parts)


def half_ladder_cross():
    cross = []
    for e in PB_EDGES:
        x, y = tuple(sorted(e))
        cross.append(((x, 0), (y, 0)))
    for x in range(7):
        for y in range(7):
            if frozenset((x, y)) in PB_EDGES:
                cross.append(((x, 1), (y, 0)))
    return cross


def ladder_cross():
    return [
        ((x, i), (y, i))
        for e in PB_EDGES
        for x, y in [tuple(sorted(e))]
        for i in range(2)
    ]


def layer0_cross():
    return [((x, 0), (y, 0)) for e in PB_EDGES for x, y in [tuple(sorted(e))]]


def random_five_conn_hosts(rng: Random, trials: int = 40):
    hosts = []
    for _ in range(trials):
        edges = set()
        for e in PB_EDGES:
            x, y = tuple(e)
            for i, j in product(range(2), repeat=2):
                edges.add(frozenset(((x, i), (y, j))))
        order = list(edges)
        rng.shuffle(order)
        es = set(edges)

        def deg_ok(eset):
            adj = build_adj14([(tuple(e)[0], tuple(e)[1]) for e in eset])
            return min(bin(adj[i]).count("1") for i in range(14)) >= 5

        for e in order:
            trial = es - {e}
            u, v = tuple(e)
            lab = frozenset((u[0], v[0]))
            rem = sum(
                1
                for f in trial
                if frozenset((tuple(f)[0][0], tuple(f)[1][0])) == lab
            )
            if rem < 1:
                continue
            if deg_ok(trial):
                es = trial
        cross = [(tuple(e)[0], tuple(e)[1]) for e in es]
        adj = build_adj14(cross)
        if node_connectivity_ge5(adj):
            hosts.append(adj)
    return hosts


def main() -> None:
    print("=== hc7_pb_max_contact_nine_verify (two-vertex laboratory) ===")

    named = [
        ("layer0", layer0_cross()),
        ("ladder", ladder_cross()),
        ("half_ladder", half_ladder_cross()),
        ("audited", cross_from_tuples(AUDITED_CROSS)),
        ("four_colour", cross_from_words(FOUR_COLOUR_WORDS)),
        ("full_K22", full_bundles14()),
    ]

    five_conn_cstar = []
    low_cstar = []

    for name, cross in named:
        adj = build_adj14(cross)
        assert_canonical_nine(adj)
        cs = c_star(adj)
        k5 = node_connectivity_ge5(adj)
        col4 = four_colourable(adj)
        print(f"{name}: c*={cs} kappa5={k5} four_col={col4}")
        if k5:
            five_conn_cstar.append((name, cs))
            assert cs == 10, (name, cs)
        if cs <= 9:
            low_cstar.append((name, cs, k5, col4))
            assert col4 and not k5, (name, cs, k5, col4)

    rng = Random(20260720)
    random_hosts = random_five_conn_hosts(rng, trials=40)
    print(f"random five-conn hosts: {len(random_hosts)}")
    for i, adj in enumerate(random_hosts):
        assert_canonical_nine(adj)
        cs = c_star(adj)
        assert cs == 10, (i, cs)
        five_conn_cstar.append((f"random_{i}", cs))

    print("--- summary ---")
    print(f"five_conn_checked={len(five_conn_cstar)} all_cstar_10={all(c==10 for _,c in five_conn_cstar)}")
    print(f"low_cstar_hosts={len(low_cstar)} (all four-colourable and not five-conn)")
    print("PASS finite maximum-contact laboratory checks")


if __name__ == "__main__":
    main()
