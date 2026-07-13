#!/usr/bin/env python3
"""RETRACTED failed falsifier for the labelled gate-triangle principle.

This file is retained only as a record of a rejected construction.  Its
main assertion deliberately fails: degree one at a literal root does not
preclude a rooted minor, because the root bag may absorb its unique
neighbour.  For example, on the C side the bags
``{a,c0}, {b}, {c,c1}`` already form a T-rooted triangle.  Do not use or
run this file as a verifier.

The host has an actual order-seven separation (L,S,R), is
seven-connected, has packet vector (nu_L,nu_R)=(1,3), and its thin shore
L is nonplanar and three-connected.  A literal edgeless three-cut T of L
has exactly two lobes C,D.  All audited local and global portal-matching
bounds hold.  Nevertheless neither C+T nor D+T has a T-rooted K3, so a
fortiori neither has one whose three bags admit three distinct S labels.

This does not claim that the host is K7-minor-free or
7-contraction-critical.  It isolates exactly why those global hypotheses
must be used by any proof of the proposed labelled rooted-model step.
"""

from itertools import combinations, product

import networkx as nx


T = ("a", "b", "c")
C = ("c0", "c1", "c2", "c3")
D = ("d0", "d1", "d2", "d3")
S = tuple(f"s{i}" for i in range(7))


def shore_graph() -> nx.Graph:
    g = nx.Graph()
    g.add_nodes_from(T + C + D)
    g.add_edges_from(zip(C, C[1:]))
    g.add_edges_from(zip(D, D[1:]))

    # C-side: a has the unique neighbour c0; b sees all of C; c sees
    # c1,c2,c3.  Thus C+T cannot contain a cycle through a,b,c.
    g.add_edge("a", "c0")
    g.add_edges_from(("b", x) for x in C)
    g.add_edges_from(("c", x) for x in C[1:])

    # D-side: a sees all of D; b has the unique neighbour d2; c sees
    # d0,d3.  Thus D+T cannot contain a cycle through a,b,c.
    g.add_edges_from(("a", x) for x in D)
    g.add_edge("b", "d2")
    g.add_edges_from(("c", x) for x in ("d0", "d3"))
    return g


def add_portals(g: nx.Graph) -> None:
    g.add_nodes_from(S)

    # Five common labels give every four-vertex lobe the full
    # forbidden-label matching bound.  s0 is unique at c0 on L, and s6
    # is unique at d2 on L; these two unique hits force nu_L=1.
    for x in C:
        g.add_edges_from((x, f"s{i}") for i in range(1, 6))
    g.add_edge("c0", "s0")
    for x in D:
        g.add_edges_from((x, f"s{i}") for i in range(1, 6))
    g.add_edge("d2", "s6")

    # Gate contacts only raise host connectivity; they use common labels
    # and hence do not disturb either unique-hit certificate.
    g.add_edges_from(("a", s) for s in ("s1", "s2"))
    g.add_edges_from(("b", s) for s in ("s3", "s4"))
    g.add_edges_from(("c", s) for s in ("s1", "s5"))


def host_graph() -> tuple[nx.Graph, list[tuple[str, ...]]]:
    g = shore_graph()
    add_portals(g)
    packets: list[tuple[str, ...]] = []

    # Three opposite C8 components.  Every vertex sees S-s5 and exactly
    # one distinguished vertex per component also sees s5.  Consequently
    # each component contains exactly one disjoint S-full packet, while
    # all its vertices have enough boundary degree for seven-connectivity.
    for j in range(3):
        p = tuple(f"p{j}_{i}" for i in range(8))
        packets.append(p)
        g.add_edges_from((p[i], p[(i + 1) % 8]) for i in range(8))
        for x in p:
            g.add_edges_from((x, s) for s in S if s != "s5")
        g.add_edge(p[0], "s5")
    return g, packets


def portal_rank(g: nx.Graph, labels: set[str], vertices: set[str]) -> int:
    h = nx.Graph()
    left = {f"L:{s}" for s in labels}
    right = {f"V:{x}" for x in vertices}
    h.add_nodes_from(left, bipartite=0)
    h.add_nodes_from(right, bipartite=1)
    for s in labels:
        for x in vertices:
            if g.has_edge(s, x):
                h.add_edge(f"L:{s}", f"V:{x}")
    matching = nx.algorithms.bipartite.maximum_matching(h, top_nodes=left)
    return sum(1 for x in left if x in matching)


def connected_root_bags(g: nx.Graph, root: str, other_roots: set[str]):
    allowed = sorted(set(g) - other_roots - {root})
    for mask in range(1 << len(allowed)):
        bag = {root}
        bag.update(allowed[i] for i in range(len(allowed)) if mask >> i & 1)
        if nx.is_connected(g.subgraph(bag)):
            yield frozenset(bag)


def bags_adjacent(g: nx.Graph, x: frozenset[str], y: frozenset[str]) -> bool:
    return any(g.has_edge(u, v) for u in x for v in y)


def has_t_rooted_k3(g: nx.Graph) -> bool:
    choices = [
        list(connected_root_bags(g, t, set(T) - {t}))
        for t in T
    ]
    for bags in product(*choices):
        if any(bags[i] & bags[j] for i, j in combinations(range(3), 2)):
            continue
        if all(
            bags_adjacent(g, bags[i], bags[j])
            for i, j in combinations(range(3), 2)
        ):
            return True
    return False


def verify() -> None:
    g, packets = host_graph()
    l = g.subgraph(T + C + D).copy()
    r_vertices = set().union(*(set(p) for p in packets))

    assert nx.node_connectivity(l) == 3
    assert not nx.check_planarity(l)[0]
    assert not any(l.has_edge(x, y) for x, y in combinations(T, 2))
    assert {frozenset(x) for x in nx.connected_components(l.subgraph(C + D))} == {
        frozenset(C), frozenset(D)
    }
    assert all(any(l.has_edge(t, x) for x in k) for t in T for k in (C, D))

    # Neither augmented lobe even has the unlabelled rooted triangle.
    assert not has_t_rooted_k3(l.subgraph(T + C).copy())
    assert not has_t_rooted_k3(l.subgraph(T + D).copy())
    assert l.subgraph(T + C).degree("a") == 1
    assert l.subgraph(T + D).degree("b") == 1

    # Exact localized forbidden-label rank, for every forbidden F of
    # order at most three, and global rank seven.
    for k in (C, D):
        for f_size in range(4):
            for forbidden in combinations(S, f_size):
                rank = portal_rank(g, set(S) - set(forbidden), set(k))
                assert rank >= min(4 - f_size, len(k))
    assert portal_rank(g, set(S), set(T + C + D)) == 7

    # Literal thinness certificates.  On L, s0 and s6 have unique portal
    # vertices c0,d2, so every full packet contains both.  On each R
    # component, s5 has the unique portal p[0], so at most one full packet
    # lies there; p[0] itself is full.
    assert set(g.neighbors("s0")) & set(T + C + D) == {"c0"}
    assert set(g.neighbors("s6")) & set(T + C + D) == {"d2"}
    for p in packets:
        assert set(g.neighbors("s5")) & set(p) == {p[0]}
        assert all(g.has_edge(p[0], s) for s in S)

    # This is a literal seven-connected order-seven separation.
    assert not any(g.has_edge(x, y) for x in T + C + D for y in r_vertices)
    assert nx.node_connectivity(g) == 7
    assert set(S) == nx.minimum_node_cut(g)

    print("VERIFIED")
    print(f"host_order={len(g)} host_edges={g.number_of_edges()}")
    print("host_connectivity=7 thin_connectivity=3 thin_nonplanar=True")
    print("packet_vector=(1,3) global_portal_rank=7")
    print("rooted_K3_C=False rooted_K3_D=False")
    print("guardrail=host_not_asserted_K7_minor_free_or_contraction_critical")


if __name__ == "__main__":
    verify()
