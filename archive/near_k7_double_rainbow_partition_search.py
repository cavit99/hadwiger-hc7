#!/usr/bin/env python3
"""Stress-test the double-rainbow bipartition mechanism.

For homogeneous exceptional-shell blow-ups with four vertices per piece,
randomly minimise edges subject to kappa(H)>=4 and kappa(G)>=7.  Test
whether D=X2 union X3 has a connected adjacent bipartition whose two
sides both meet all three neutral portal sets and both contact c and the
connected bag {a,b} union X1.  Such a partition gives the four rainbow
K4 bags ({a,b} union X1), {c}, R, S.
"""

from __future__ import annotations

from itertools import combinations, product
import random

import networkx as nx


SIZE = 4
A, B, C = 0, 1, 2
X1 = tuple(range(3, 3 + SIZE))
X2 = tuple(range(3 + SIZE, 3 + 2 * SIZE))
X3 = tuple(range(3 + 2 * SIZE, 3 + 3 * SIZE))
Q = tuple(range(3 + 3 * SIZE, 6 + 3 * SIZE))
ROLES = {"a": (A,), "b": (B,), "c": (C,), "1": X1, "2": X2, "3": X3}
ALLOWED = (
    ("b", "c"), ("a", "1"), ("b", "1"), ("a", "2"),
    ("b", "2"), ("b", "3"), ("c", "3"), ("1", "2"),
    ("2", "3"),
)


def role(vertex: int) -> str:
    return next(key for key, row in ROLES.items() if vertex in row)


def full_h() -> nx.Graph:
    h = nx.Graph()
    h.add_nodes_from(range(3 + 3 * SIZE))
    for left, right in ALLOWED:
        h.add_edges_from((u, v) for u in ROLES[left] for v in ROLES[right])
    for row in (X1, X2, X3):
        h.add_edges_from(combinations(row, 2))
    return h


def with_q(h: nx.Graph) -> nx.Graph:
    g = h.copy()
    g.add_edges_from(combinations(Q, 2))
    for q in Q:
        g.add_edges_from((q, z) for z in (A, B, C))
    for i, q in enumerate(Q):
        g.add_edges_from((q, row[i]) for row in (X1, X2, X3))
    return g


def valid(h: nx.Graph) -> bool:
    if any(not nx.is_connected(h.subgraph(row)) for row in (X1, X2, X3)):
        return False
    contacts = {
        frozenset((role(u), role(v))) for u, v in h.edges() if role(u) != role(v)
    }
    return contacts == {frozenset(pair) for pair in ALLOWED}


def minimise(seed: int) -> nx.Graph:
    h = full_h()
    edges = list(h.edges())
    rng = random.Random(seed)
    rng.shuffle(edges)
    for edge in edges:
        h.remove_edge(*edge)
        if not (valid(h) and nx.node_connectivity(h) >= 4
                and nx.node_connectivity(with_q(h)) >= 7):
            h.add_edge(*edge)
    return h


def double_partition(h: nx.Graph):
    d = X2 + X3
    dmask = sum(1 << z for z in d)
    portal_masks = tuple((1 << X2[i]) | (1 << X3[i]) for i in range(3))
    b0 = {A, B, *X1}
    for bits in range(1, 1 << len(d) - 1):
        r = {d[i] for i in range(len(d)) if bits >> i & 1}
        s = set(d) - r
        if not (nx.is_connected(h.subgraph(r)) and nx.is_connected(h.subgraph(s))):
            continue
        if not any(h.has_edge(u, v) for u in r for v in s):
            continue
        rm = sum(1 << z for z in r)
        sm = dmask ^ rm
        if not all(rm & row and sm & row for row in portal_masks):
            continue
        if not (any(h.has_edge(C, z) for z in r)
                and any(h.has_edge(C, z) for z in s)):
            continue
        if not (any(h.has_edge(u, z) for u in b0 for z in r)
                and any(h.has_edge(u, z) for u in b0 for z in s)):
            continue
        return r, s
    return None


def valid_splits(h: nx.Graph):
    d = X2 + X3
    b0 = {A, B, *X1}
    rows = []
    for bits in range(1, 1 << (len(d) - 1)):
        r = {d[i] for i in range(len(d)) if bits >> i & 1}
        s = set(d) - r
        if not (nx.is_connected(h.subgraph(r)) and nx.is_connected(h.subgraph(s))):
            continue
        if not any(h.has_edge(u, v) for u in r for v in s):
            continue
        if not (any(h.has_edge(C, z) for z in r)
                and any(h.has_edge(C, z) for z in s)):
            continue
        if not (any(h.has_edge(u, z) for u in b0 for z in r)
                and any(h.has_edge(u, z) for u in b0 for z in s)):
            continue
        rows.append((r, s))
    return rows


def with_portals(h: nx.Graph, options):
    g = h.copy()
    g.add_edges_from(combinations(Q, 2))
    for q in Q:
        g.add_edges_from((q, z) for z in (A, B, C))
    for q, row in zip(Q, options):
        g.add_edges_from((q, z) for z in row)
    return g


def scan_portals(h: nx.Graph) -> bool:
    options = tuple(product(X1, X2, X3))
    splits = valid_splits(h)
    split_options = []
    for r, s in splits:
        split_options.append({
            i for i, (_, x2, x3) in enumerate(options)
            if (x2 in r and x3 in s) or (x2 in s and x3 in r)
        })
    negative = 0
    for indices in product(range(len(options)), repeat=3):
        chosen = tuple(options[index] for index in indices)
        if any(chosen[0][column] == chosen[1][column] == chosen[2][column]
               for column in range(3)):
            # a fourth triple-common portal; Corollary 1.4 already handles it
            continue
        if any(all(index in row for index in indices) for row in split_options):
            continue
        negative += 1
        rows = chosen
        g = with_portals(h, rows)
        if nx.node_connectivity(g) >= 7:
            print("DOUBLE-PARTITION COUNTEREXAMPLE", rows,
                  "Hedges", h.number_of_edges(), "kappaG", nx.node_connectivity(g),
                  tuple(sorted(h.edges())))
            return False
    print("portal triples without displayed split", negative,
          "none are 7-connected")
    return True


def main() -> None:
    seen = set()
    for seed in range(200):
        h = minimise(seed)
        key = tuple(sorted(h.edges()))
        if key in seen:
            continue
        seen.add(key)
        split = double_partition(h)
        if split is None:
            print("NEGATIVE", seed, "edges", h.number_of_edges(),
                  "kappaH", nx.node_connectivity(h),
                  "kappaG", nx.node_connectivity(with_q(h)), key)
            return
        if seed < 5 and not scan_portals(h):
            return
    print("all positive", len(seen), "distinct minimal expansions")


if __name__ == "__main__":
    main()
