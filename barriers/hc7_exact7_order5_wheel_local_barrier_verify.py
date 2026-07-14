#!/usr/bin/env python3
"""Verify the sharp order-five wheel portal architecture.

The local W5 cell meets the degree demand and blocks every two-duty carrier
packing.  The maximally paired-state boundary completion is tested for the
old packet vector, state-attainment compatibility, vertex connectivity,
and an explicit K7 model.  This is one exact host test, not a census.
"""

from __future__ import annotations

from itertools import combinations

from hc7_exact7_single_missing_crossed_duty_barrier_verify import (
    BLOCKS,
    S,
    add,
    adjacency,
    assert_no_disjoint_duties,
    boundary_neighbourhood,
    carriers,
    components,
    connected,
    contract,
    edge,
    extend_colouring,
)


CELL = frozenset({"0", "1", "2", "3", "4"})


def build() -> tuple[frozenset[str], set[frozenset[str]]]:
    vertices = S | CELL | {"p", "q"}
    edges: set[frozenset[str]] = set()

    # W5 with hub 0 and rim 1-3-2-4-1.
    for v in ("1", "2", "3", "4"):
        add(edges, "0", v)
    for u, v in (("1", "3"), ("3", "2"), ("2", "4"), ("4", "1")):
        add(edges, u, v)

    portals = {
        "a1": CELL,
        "t1": frozenset({"1"}),
        "a2": frozenset({"0", "2", "3", "4"}),
        "t2": frozenset({"1"}),
        "a3": frozenset({"1"}),
        "t3": CELL,
        "c": CELL,
    }
    for s, neighbours in portals.items():
        for v in neighbours:
            add(edges, s, v)

    # Maximal literal boundary graph preserving the four equality classes.
    classes = (*BLOCKS, frozenset({"c"}))
    for left, right in combinations(classes, 2):
        for u in left:
            for v in right:
                add(edges, u, v)

    for packet in ("p", "q"):
        for s in S:
            add(edges, packet, s)
    return frozenset(vertices), edges


def main() -> None:
    vertices, edges = build()
    adj = adjacency(vertices, edges)

    # The wheel is exactly three-connected.
    for size in range(3):
        for deleted_tuple in combinations(sorted(CELL), size):
            assert connected(CELL - frozenset(deleted_tuple), adj)
    assert not connected(CELL - {"0", "1", "2"}, adj)

    assert min(len(adj[v]) for v in vertices) == 7
    found = carriers(CELL, adj)
    assert_no_disjoint_duties(found)
    assert all("1" in carrier for duty in found.values() for carrier in duty)

    # Actual old separation and exact packet vector (1,2).  Every full
    # packet in C contains the unique t1 portal 1.
    left = frozenset({"p"})
    right = CELL | {"q"}
    assert not any(edge(u, v) in edges for u in left for v in right)
    assert set(components(vertices - S, adj)) == {
        left,
        frozenset({"q"}),
        CELL,
    }
    assert boundary_neighbourhood(left, adj) == S
    assert boundary_neighbourhood(frozenset({"q"}), adj) == S
    assert boundary_neighbourhood(CELL, adj) == S
    ordered = tuple(sorted(CELL))
    for mask in range(1, 1 << len(ordered)):
        packet = frozenset(
            ordered[i] for i in range(len(ordered)) if mask >> i & 1
        )
        if connected(packet, adj) and boundary_neighbourhood(packet, adj) == S:
            assert "1" in packet

    # The portal pattern itself forbids legal attainment of Pi from the
    # opposite shore.  Every cell vertex sees all four equality classes, so
    # a six-colouring inducing Pi leaves only two colours on C, while W5
    # contains the triangle 0-1-3.  The natural proper contraction confirms
    # the incompatibility computationally.
    classes = (*BLOCKS, frozenset({"c"}))
    assert all(
        all(bool((adj[v] & S) & block) for block in classes) for v in CELL
    )
    assert all(edge(u, v) in edges for u, v in (("0", "1"), ("1", "3"), ("3", "0")))
    cluster = left | BLOCKS[0]
    minor_vertices, minor_edges = contract(vertices, edges, cluster, "b1")
    fixed = {
        "b1": 0,
        "a2": 1,
        "t2": 1,
        "a3": 2,
        "t3": 2,
        "c": 3,
    }
    witness = extend_colouring(minor_vertices, minor_edges, fixed, 6)
    assert witness is None

    # Exact connectivity: exhaustive deletion below five plus one displayed
    # five-cut.  Hence boundary saturation cannot lift the local model to
    # the required seven-connected host.
    cut = frozenset({"1", "a1", "a2", "c", "t3"})
    for size in range(5):
        for deleted_tuple in combinations(sorted(vertices), size):
            assert connected(vertices - frozenset(deleted_tuple), adj)
    assert not connected(vertices - cut, adj)

    # Saturating the old boundary also creates a literal K7 model: p and q
    # repair two paired nonedges and the common wheel portal repairs the
    # third.  This prevents accidental interpretation as an HC7 barrier.
    model = (
        frozenset({"a1", "p"}),
        frozenset({"t1"}),
        frozenset({"a2", "q"}),
        frozenset({"t2"}),
        frozenset({"a3", "1"}),
        frozenset({"t3"}),
        frozenset({"c"}),
    )
    assert all(connected(bag, adj) for bag in model)
    assert all(
        any(edge(u, v) in edges for u in left_bag for v in right_bag)
        for left_bag, right_bag in combinations(model, 2)
    )

    print("W5 cell: degree demand and common-portal carrier lock verified")
    print("old separation: packet vector (1,2) verified")
    print("state scope: Pi would leave only two colours on non-bipartite W5; attainment impossible")
    print("maximal paired boundary: connectivity 5, not 7; cut:", sorted(cut))
    print("scope guard: explicit K7 model verified")


if __name__ == "__main__":
    main()
