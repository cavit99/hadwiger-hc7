#!/usr/bin/env python3
"""Search small static apex-shadow societies.

This is a falsification tool, not part of a proof.  It searches the graph
atlas for connected bipartite complex bags B and portal/foot sets for the
r=4 base cell.  Joining a found base example with K_2 gives the r=6
spanning K_6 shell while preserving bipartiteness of B.
"""

from __future__ import annotations

import itertools
import random

import networkx as nx


def connected_split(B: nx.Graph, portals: tuple[frozenset[int], ...]) -> bool:
    vertices = tuple(B)
    anchor = vertices[0]
    for bits in range(1, 1 << len(vertices)):
        A = {vertices[i] for i in range(len(vertices)) if bits >> i & 1}
        if anchor not in A or len(A) == len(vertices):
            continue
        D = set(vertices) - A
        if not nx.is_connected(B.subgraph(A)) or not nx.is_connected(B.subgraph(D)):
            continue
        if all(A & P and D & P for P in portals):
            return True
    return False


def list_colourable(
    B: nx.Graph,
    portals: tuple[frozenset[int], frozenset[int], frozenset[int]],
    feet: frozenset[int],
) -> bool:
    # Colours 0=alpha, 1,2,3=p_1,p_2,p_3; v has colour p_3.
    lists: dict[int, tuple[int, ...]] = {}
    for x in B:
        allowed = {0}
        if x not in portals[0]:
            allowed.add(1)
        if x not in portals[1]:
            allowed.add(2)
        if x not in portals[2] and x not in feet:
            allowed.add(3)
        lists[x] = tuple(allowed)
    order = sorted(B, key=lambda x: (len(lists[x]), -B.degree(x)))
    colour: dict[int, int] = {}

    def rec(pos: int) -> bool:
        if pos == len(order):
            return True
        x = order[pos]
        used = {colour[y] for y in B[x] if y in colour}
        for c in lists[x]:
            if c not in used:
                colour[x] = c
                if rec(pos + 1):
                    return True
                del colour[x]
        return False

    return rec(0)


def make_graph(
    B: nx.Graph,
    portals: tuple[frozenset[int], frozenset[int], frozenset[int]],
    feet: frozenset[int],
) -> tuple[nx.Graph, nx.Graph]:
    H = nx.Graph(B)
    ss = ("s1", "s2", "s3")
    H.add_edges_from(itertools.combinations(ss, 2))
    for i, P in enumerate(portals):
        H.add_edges_from((x, ss[i]) for x in P)
    G = nx.Graph(H)
    G.add_node("v")
    # This forces the quotient colour p_3.
    G.add_edges_from((("v", "s1"), ("v", "s2")))
    G.add_edges_from(("v", x) for x in feet)
    return H, G


def candidates(B: nx.Graph) -> list[frozenset[int]]:
    V = tuple(B)
    return [
        frozenset(V[i] for i in range(len(V)) if mask >> i & 1)
        for mask in range(1, 1 << len(V))
        if mask.bit_count() >= 2
    ]


def search(samples_per_bag: int = 300_000) -> None:
    bags = []
    for B in nx.graph_atlas_g():
        if len(B) == 6 and nx.is_connected(B) and nx.is_bipartite(B):
            bags.append(nx.convert_node_labels_to_integers(B))
    random.Random(937_441).shuffle(bags)
    rng = random.Random(41_771)
    print("bags", len(bags), flush=True)
    for bag_no, B in enumerate(bags):
        print("bag", bag_no, len(B), sorted(B.edges()), flush=True)
        subs = candidates(B)
        total = len(subs) ** 3 * (2 ** len(B) - 1)
        exhaustive = total <= samples_per_bag
        iterator = (
            itertools.product(subs, subs, subs, [
                frozenset(x for i, x in enumerate(B) if mask >> i & 1)
                for mask in range(1, 1 << len(B))
            ])
            if exhaustive
            else (
                (rng.choice(subs), rng.choice(subs), rng.choice(subs),
                 frozenset(x for x in B if rng.randrange(2)))
                for _ in range(samples_per_bag)
            )
        )
        for P1, P2, P3, F in iterator:
            if not F:
                continue
            portals = (P1, P2, P3)
            if connected_split(B, portals):
                continue
            if list_colourable(B, portals, F):
                continue
            H, G = make_graph(B, portals, F)
            if nx.node_connectivity(H) < 4:
                continue
            planar, _ = nx.check_planarity(G)
            if not planar:
                continue
            print("FOUND")
            print("B_edges", sorted(B.edges()))
            print("portals", tuple(sorted(P) for P in portals))
            print("feet", sorted(F))
            print("H_connectivity", nx.node_connectivity(H))
            print("G_edges", sorted(map(str, G.edges())))
            return
    print("NONE")


if __name__ == "__main__":
    search(50_000)
