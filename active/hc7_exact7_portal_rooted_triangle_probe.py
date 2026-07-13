#!/usr/bin/env python3
"""Verify a full-connectivity counterexample to a per-lobe rank-3 claim.

The explicit 18-vertex host satisfies the complete exact-seven (1,3)
setup, including ambient seven-connectivity.  Its order-three lobe C
satisfies every forbidden-label portal-matching inequality, but no
T-rooted K3 in C+T has literal portal rank three.

The host also contains an explicit literal K7 model, obtained from the
other lobe D.  Thus this is a guardrail against the overbroad assertion
that *each* order-at-least-three lobe has a rank-three model.  It does not
refute the target-free disjunction that one of the two lobes closes.
"""

from __future__ import annotations

from itertools import combinations, product

import networkx as nx


T = ("t0", "t1", "t2")
S = tuple(f"s{i}" for i in range(7))
C = ("c0", "c1", "c2")
D = ("d0", "d1")
R = ("p0", "p1", "p2")


def connected_root_bags(h: nx.Graph, root: str):
    others = set(T) - {root}
    allowed = sorted(set(h) - others - {root})
    for mask in range(1 << len(allowed)):
        bag = {root}
        bag.update(allowed[i] for i in range(len(allowed)) if mask >> i & 1)
        if nx.is_connected(h.subgraph(bag)):
            yield frozenset(bag)


def adjacent(h: nx.Graph, a: frozenset[str], b: frozenset[str]) -> bool:
    return any(h.has_edge(x, y) for x in a for y in b)


def portal_labels(g: nx.Graph, bag: frozenset[str]) -> set[str]:
    return {s for s in S if any(g.has_edge(s, x) for x in bag)}


def has_sdr(sets: list[set[str]]) -> bool:
    return all(
        len(set().union(*(sets[i] for i in ix))) >= len(ix)
        for r in range(1, len(sets) + 1)
        for ix in combinations(range(len(sets)), r)
    )


def rooted_models(h: nx.Graph):
    choices = [list(connected_root_bags(h, t)) for t in T]
    for bags in product(*choices):
        if any(bags[i] & bags[j] for i, j in combinations(range(3), 2)):
            continue
        if all(adjacent(h, bags[i], bags[j]) for i, j in combinations(range(3), 2)):
            yield bags


def portal_rank(g: nx.Graph, labels: set[str], vertices: set[str]) -> int:
    b = nx.Graph()
    left = {("s", s) for s in labels}
    right = {("v", x) for x in vertices}
    b.add_nodes_from(left, bipartite=0)
    b.add_nodes_from(right, bipartite=1)
    b.add_edges_from(
        (("s", s), ("v", x))
        for s in labels
        for x in vertices
        if g.has_edge(s, x)
    )
    m = nx.algorithms.bipartite.maximum_matching(b, top_nodes=left)
    return sum(x in m for x in left)


def forbidden_rank_ok(g: nx.Graph, k: set[str]) -> bool:
    for f_size in range(4):
        for forbidden in combinations(S, f_size):
            if portal_rank(g, set(S) - set(forbidden), k) < min(4 - f_size, len(k)):
                return False
    return True


def labelled_model_exists(g: nx.Graph, k: tuple[str, ...]) -> bool:
    h = g.subgraph(T + k).copy()
    return any(has_sdr([portal_labels(g, b) for b in bags]) for bags in rooted_models(h))


def explicit_host() -> nx.Graph:
    g = nx.Graph()
    g.add_nodes_from(T + C + D + S + R)

    # The thin shore.  T induces the path t1-t0-t2.  Deleting T leaves
    # exactly the path C and the edge D.
    g.add_edges_from(
        [
            ("c0", "c1"),
            ("c1", "c2"),
            ("t0", "c0"),
            ("t0", "c1"),
            ("t0", "c2"),
            ("t1", "c0"),
            ("t2", "c2"),
            ("t0", "t1"),
            ("t0", "t2"),
            ("d0", "d1"),
        ]
    )
    g.add_edges_from((t, d) for t in T for d in D)

    # C has six common labels, and c1 has the seventh.  This satisfies
    # all forbidden-label ranks, while s6 is unique at c1 on the whole
    # thin shore and therefore certifies nu_L=1.
    for c in C:
        g.add_edges_from((c, s) for s in S[:6])
    g.add_edge("c1", "s6")

    # D has the same six common labels.  The two leaf gates receive three
    # common labels to meet the ambient degree/connectivity requirement;
    # the middle gate t0 deliberately has no S portal.
    for d in D:
        g.add_edges_from((d, s) for s in S[:6])
    for t in ("t1", "t2"):
        g.add_edges_from((t, s) for s in S[:3])

    # The literal boundary is K_{3,4}, hence triangle-free.
    g.add_edges_from((x, y) for x in S[:3] for y in S[3:])

    # Three singleton S-full packets form the opposite shore.
    g.add_edges_from((p, s) for p in R for s in S)
    return g


def is_clique_model(g: nx.Graph, bags: list[set[str]]) -> bool:
    return (
        all(bags)
        and all(nx.is_connected(g.subgraph(bag)) for bag in bags)
        and all(not (bags[i] & bags[j]) for i, j in combinations(range(len(bags)), 2))
        and all(
            any(g.has_edge(x, y) for x in bags[i] for y in bags[j])
            for i, j in combinations(range(len(bags)), 2)
        )
    )


def verify() -> None:
    g = explicit_host()
    l_vertices = set(T + C + D)
    l = g.subgraph(l_vertices).copy()

    # Actual separation, exact gate/lobe geometry, and thin-shore
    # connectivity.
    assert not any(g.has_edge(x, y) for x in l_vertices for y in R)
    assert nx.node_connectivity(l) == 3
    assert not nx.check_planarity(l)[0]
    remainder = l.copy()
    remainder.remove_nodes_from(T)
    assert {frozenset(x) for x in nx.connected_components(remainder)} == {
        frozenset(C),
        frozenset(D),
    }
    assert all(any(l.has_edge(t, x) for x in k) for t in T for k in (C, D))

    # Full ambient seven-connectivity.  The explicit subset loop checks
    # every possible cut of order at most six, independently of the
    # optimized NetworkX connectivity routine.
    vertices = tuple(g)
    for order in range(7):
        for cut in combinations(vertices, order):
            assert nx.is_connected(g.subgraph(set(vertices) - set(cut)))
    assert nx.node_connectivity(g) == 7
    assert not nx.is_connected(g.subgraph(set(g) - set(S)))

    # Exact packet vector.  c1 is the unique L-neighbour of s6, so every
    # S-full packet in L contains c1; c1 itself is full.  The three
    # opposite singleton vertices are precisely three disjoint packets.
    assert set(g.neighbors("s6")) & l_vertices == {"c1"}
    assert all(g.has_edge("c1", s) for s in S)
    assert all(all(g.has_edge(p, s) for s in S) for p in R)

    # All actual portal-rank consequences hold, including the global
    # order-seven portal matching.
    assert forbidden_rank_ok(g, set(C))
    assert forbidden_rank_ok(g, set(D))
    assert portal_rank(g, set(S), l_vertices) == 7

    # The claimed per-lobe conclusion fails on C.  Exhaustive branch-set
    # enumeration shows that every rooted model leaves the t0 bag equal
    # to the portal-free singleton {t0}; hence its rank is at most two.
    c_models = list(rooted_models(g.subgraph(T + C).copy()))
    assert c_models
    assert all(bags[0] == frozenset({"t0"}) for bags in c_models)
    assert all(not has_sdr([portal_labels(g, bag) for bag in bags]) for bags in c_models)
    assert not labelled_model_exists(g, C)

    # This counterexample is not target-free: D has a rank-three rooted
    # model and gives the following literal seven-bag clique model.
    assert labelled_model_exists(g, D)
    k7_bags = [
        {"t0", "d0", "s0"},
        {"t1", "s1"},
        {"t2", "d1", "s2"},
        set(C) | {"s6"},
        {"p0", "s3"},
        {"p1", "s4"},
        {"p2", "s5"},
    ]
    assert is_clique_model(g, k7_bags)

    print("VERIFIED_FULL_COUNTEREXAMPLE")
    print(f"order={len(g)} edges={g.number_of_edges()}")
    print("ambient_connectivity=7 thin_connectivity=3 packet_vector=(1,3)")
    print("C_order=3 C_forbidden_rank=True C_rank3_rooted_model=False")
    print("D_rank3_rooted_model=True literal_K7=True")
    print("edges=" + repr(sorted(tuple(sorted(e)) for e in g.edges())))


if __name__ == "__main__":
    verify()
