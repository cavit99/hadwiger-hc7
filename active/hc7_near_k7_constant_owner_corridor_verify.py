"""Checks the explicit transition colourings in Proposition 5.1.

This verifier is intentionally elementary: it verifies the displayed
colourings and the exact K7^vee model edges.  The proof of
non-six-colourability is the forced-list argument in the note.
"""

import sys

import networkx as nx

# The workspace virtual environment provides NetworkX; the local Z3 wheel
# is installed in Homebrew's matching Python 3.14 site-packages.
sys.path.append("/opt/homebrew/lib/python3.14/site-packages")
import z3


def build(m: int):
    g = nx.Graph()
    alpha = 0
    C = ["a"] + [f"b{i}" for i in range(1, 6)]
    S = [f"s{i}" for i in range(1, 6)]
    T = [f"x{k}" for k in range(2 * m)]
    g.add_edges_from((C[i], C[j]) for i in range(6) for j in range(i + 1, 6))
    g.add_edges_from((S[i], S[j]) for i in range(5) for j in range(i + 1, 5))
    for i in range(1, 6):
        g.add_edges_from((f"s{i}", z) for z in C if z != f"b{i}")
    g.add_edges_from(("v", z) for z in C if z != "b1")
    g.add_edges_from((T[k], T[k + 1]) for k in range(2 * m - 1))
    g.add_edges_from([
        ("v", "s3"), ("v", "s4"), ("v", "s5"),
        ("v", T[0]), ("v", T[-1]),
        (T[0], "s1"), (T[0], "s2"),
        (T[-1], "s3"), (T[-1], "s4"), (T[-1], "s5"),
    ])
    rows = {0: (3, 4, 5), 2 * m - 1: (2,)}
    for k in range(1, 2 * m - 1):
        rows[k] = (2, 3, 4, 5)
    for k, indices in rows.items():
        for i in indices:
            y = f"y{k}_{i}"
            g.add_edge(T[k], y)
            g.add_edges_from((y, z) for z in C if z != f"b{i}")

    outside = {"a": alpha, **{f"b{i}": i for i in range(1, 6)}}
    outside.update({f"s{i}": i for i in range(1, 6)})
    outside["v"] = 1
    for k, indices in rows.items():
        outside.update({f"y{k}_{i}": i for i in indices})
    return g, T, outside


def proper(g, colour, omitted=None):
    omitted = omitted or frozenset()
    return all(frozenset((u, v)) in omitted or colour[u] != colour[v]
               for u, v in g.edges())


def six_colourable(g):
    solver = z3.Solver()
    colour = {v: z3.Int(f"c_{i}") for i, v in enumerate(g.nodes())}
    solver.add(*(z3.And(0 <= colour[v], colour[v] < 6) for v in g))
    solver.add(*(colour[u] != colour[v] for u, v in g.edges()))
    return solver.check() == z3.sat


for m in range(2, 9):
    g, T, outside = build(m)
    if m <= 5:
        assert not six_colourable(g)
    for k in range(len(T) - 1):
        colour = dict(outside)
        for i in range(k + 1):
            colour[T[i]] = i % 2
        for i in range(len(T) - 1, k, -1):
            colour[T[i]] = (len(T) - 1 - i) % 2
        edge = frozenset((T[k], T[k + 1]))
        assert colour[T[k]] == colour[T[k + 1]] == k % 2
        assert proper(g, colour, {edge})

    # Exact displayed K7^vee adjacencies.
    assert not g.has_edge("v", "s1") and not g.has_edge("v", "s2")
    assert all(g.has_edge("v", f"s{i}") for i in (3, 4, 5))
    assert all(g.has_edge(f"s{i}", f"s{j}")
               for i in range(1, 6) for j in range(i + 1, 6))
    assert g.has_edge(T[0], "s1") and g.has_edge(T[0], "s2")
    assert all(g.has_edge(T[-1], f"s{i}") for i in (3, 4, 5))
    assert g.has_edge("v", T[0]) and g.has_edge("v", T[-1])

print("verified Proposition 5.1 transition states for m=2,...,8")
