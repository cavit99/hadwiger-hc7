#!/usr/bin/env python3
"""Classify the static eight-vertex boundary left by the bilateral funnel.

The five fixed vertices induce either K5 minus two adjacent edges or K5
minus two independent edges.  The other three vertices have arbitrary
edges.  We retain graphs for which every vertex deletion is K5-minor-free
and report whether the whole boundary is 4-colourable or 5-chromatic.
The script is diagnostic; no computational output is used as a theorem.
"""

from __future__ import annotations

import itertools
from collections import Counter

import networkx as nx


N = 8
ALL_PAIRS = tuple(itertools.combinations(range(N), 2))


def adjacency(edges):
    a = [0] * N
    for x, y in edges:
        a[x] |= 1 << y
        a[y] |= 1 << x
    return a


def connected(mask, a):
    seen = mask & -mask
    while True:
        nxt = seen
        todo = seen
        while todo:
            bit = todo & -todo
            todo ^= bit
            nxt |= a[bit.bit_length() - 1] & mask
        if nxt == seen:
            return seen == mask
        seen = nxt


def adjacent(x, y, a):
    todo = x
    while todo:
        bit = todo & -todo
        todo ^= bit
        if a[bit.bit_length() - 1] & y:
            return True
    return False


def partitions_k5(vertices):
    vertices = tuple(vertices)
    out = []
    # Five singleton bags.
    for used in itertools.combinations(vertices, 5):
        out.append(tuple(1 << x for x in used))
    # Six used vertices: one pair.
    for used in itertools.combinations(vertices, 6):
        for pair in itertools.combinations(used, 2):
            rest = [x for x in used if x not in pair]
            out.append(((1 << pair[0]) | (1 << pair[1]),)
                       + tuple(1 << x for x in rest))
    # Seven used vertices: one triple or two pairs.
    for used in itertools.combinations(vertices, 7):
        for triple in itertools.combinations(used, 3):
            rest = [x for x in used if x not in triple]
            out.append((sum(1 << x for x in triple),)
                       + tuple(1 << x for x in rest))
        for four in itertools.combinations(used, 4):
            a, b, c, d = four
            for p, q in (((a, b), (c, d)),
                         ((a, c), (b, d)),
                         ((a, d), (b, c))):
                rest = [x for x in used if x not in four]
                out.append(((1 << p[0]) | (1 << p[1]),
                            (1 << q[0]) | (1 << q[1]))
                           + tuple(1 << x for x in rest))
    return tuple(out)


def clique(vertices, a):
    return all((a[x] >> y) & 1 for x, y in itertools.combinations(vertices, 2))


def sees_set(mask, vertices, a):
    return all(any((a[x] >> y) & 1 for x in range(N) if mask >> x & 1)
               for y in vertices)


def has_k5_after_delete(x, a):
    """Exact specialized search: seven vertices leave at most two extras."""
    vertices = tuple(v for v in range(N) if v != x)
    # Five singleton bags.
    for five in itertools.combinations(vertices, 5):
        if clique(five, a):
            return True
    # One pair and four singleton bags (six used vertices).
    for pair in itertools.combinations(vertices, 2):
        if not ((a[pair[0]] >> pair[1]) & 1):
            continue
        p_mask = (1 << pair[0]) | (1 << pair[1])
        outside = [v for v in vertices if v not in pair]
        for four in itertools.combinations(outside, 4):
            if clique(four, a) and sees_set(p_mask, four, a):
                return True
    # One connected triple and four singleton bags (all seven used).
    for triple in itertools.combinations(vertices, 3):
        t_mask = sum(1 << v for v in triple)
        if not connected(t_mask, a):
            continue
        four = tuple(v for v in vertices if v not in triple)
        if clique(four, a) and sees_set(t_mask, four, a):
            return True
    # Two connected pairs and three singleton bags (all seven used).
    for four_vertices in itertools.combinations(vertices, 4):
        w, y, z, q = four_vertices
        for p1, p2 in (((w, y), (z, q)), ((w, z), (y, q)), ((w, q), (y, z))):
            if not ((a[p1[0]] >> p1[1]) & 1 and (a[p2[0]] >> p2[1]) & 1):
                continue
            m1 = (1 << p1[0]) | (1 << p1[1])
            m2 = (1 << p2[0]) | (1 << p2[1])
            singles = tuple(v for v in vertices if v not in four_vertices)
            if not clique(singles, a):
                continue
            if not sees_set(m1, singles, a) or not sees_set(m2, singles, a):
                continue
            if adjacent(m1, m2, a):
                return True
    return False


def colourable4(a):
    order = sorted(range(N), key=lambda v: -(a[v].bit_count()))
    colour = [-1] * N

    def rec(pos):
        if pos == N:
            return True
        v = order[pos]
        forbidden = {colour[u] for u in range(N)
                     if colour[u] >= 0 and (a[v] >> u) & 1}
        for c in range(4):
            if c not in forbidden:
                colour[v] = c
                if rec(pos + 1):
                    return True
        colour[v] = -1
        return False

    return rec(0)


def graph_from_edges(edges):
    g = nx.Graph()
    g.add_nodes_from(range(N))
    g.add_edges_from(edges)
    return g


def classify(name, missing_fixed, forbidden_optional=()):
    fixed = set(itertools.combinations(range(5), 2)) - set(missing_fixed)
    forbidden_optional = {tuple(sorted(e)) for e in forbidden_optional}
    optional = [e for e in ALL_PAIRS
                if e not in set(itertools.combinations(range(5), 2))
                and e not in forbidden_optional]
    counts = Counter()
    reps = []
    survivors = set()
    for bits in range(1 << len(optional)):
        edges = set(fixed)
        edges.update(optional[i] for i in range(len(optional)) if bits >> i & 1)
        a = adjacency(edges)
        if any(has_k5_after_delete(x, a) for x in range(N)):
            continue
        c4 = colourable4(a)
        counts[(len(edges), c4)] += 1
        survivors.add(bits)
        if not c4:
            g = graph_from_edges(edges)
            if not any(nx.is_isomorphic(g, h) for h in reps):
                reps.append(g)
    print(name, "survivors", sum(counts.values()), "5chromatic reps", len(reps))
    print("counts", sorted(counts.items()))
    for i, g in enumerate(reps):
        print("rep", i, "edges", sorted(tuple(sorted(e)) for e in g.edges()),
              "degrees", sorted(dict(g.degree()).values()))
    maximal = [bits for bits in survivors
               if all((bits | (1 << i)) not in survivors
                      for i in range(len(optional)) if not bits >> i & 1)]
    max_reps = []
    for bits in maximal:
        edges = set(fixed)
        edges.update(optional[i] for i in range(len(optional)) if bits >> i & 1)
        g = graph_from_edges(edges)
        if not any(nx.is_isomorphic(g, h) for h in max_reps):
            max_reps.append(g)
    print("maximal", len(maximal), "isomorphism reps", len(max_reps))
    for i, g in enumerate(max_reps):
        print("maxrep", i, "edges", sorted(tuple(sorted(e)) for e in g.edges()),
              "degrees", sorted(dict(g.degree()).values()),
              "chi4", colourable4(adjacency(g.edges())))


def main():
    # In the one-hole polarity the three cut vertices collectively miss
    # one literal K4-core vertex, here vertex 0.
    classify("one-hole-forced", {(1, 3), (2, 3)},
             {(t, 0) for t in range(5, 8)})
    # In the antipodal polarity they collectively miss one present C4
    # edge; in this normalization use vertices 0 and 2.
    classify("antipodal-forced", {(0, 1), (2, 3)},
             {(t, b) for t in range(5, 8) for b in (0, 2)})


if __name__ == "__main__":
    main()
