#!/usr/bin/env python3
"""Verify the spanning crossed-frame/rural-quotient barrier.

The bundled workspace NetworkX runtime is sufficient.  Besides the local
structural assertions, the script checks an explicit width-five tree
decomposition, which certifies exclusion of a K7 minor.
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "active" / "runtime" / "deps"))

import networkx as nx  # noqa: E402


def edge_cycle(vertices: list[str]) -> list[tuple[str, str]]:
    return list(zip(vertices, vertices[1:] + vertices[:1]))


x, y = "0", "5"
qs = ["q1", "q2", "q3"]
ps = ["p1", "p2", "p3", "p4", "p5"]
rim = [x, *qs, y, *ps]

H = nx.Graph()
H.add_edges_from(edge_cycle(rim))
H.add_edges_from(("h", z) for z in rim)
H.add_edges_from(
    [
        (x, "2"),
        ("2", "6"),
        ("6", y),
        (y, "4"),
        ("4", x),
        ("2", "m"),
        ("m", "4"),
        ("q1", "2"),
        ("q2", "m"),
        ("q3", "4"),
        ("q2", "6"),
        ("w", "ell"),
        ("t", "ell"),
    ]
)
H.add_edges_from(("ell", p) for p in ps)

K = {x, y, "h", *qs, *ps}
X = {"2", "m", "4", "6"}
Y = {"ell"}
U = {x, "2", "6", y, "4"}

assert nx.node_connectivity(H.subgraph(K)) == 3
assert nx.is_connected(H.subgraph(X))
assert nx.is_connected(H.subgraph(Y))
assert not any(H.has_edge(u, v) for u in X for v in Y)

q_actual = {z for z in K - {x, y} if any(H.has_edge(z, u) for u in X)}
p_actual = {z for z in K - {x, y} if any(H.has_edge(z, u) for u in Y)}
assert q_actual == set(qs)
assert p_actual == set(ps)
assert q_actual.isdisjoint(p_actual)
assert set(H.neighbors("ell")) == {*ps, "w", "t"}
open_shore = set(H) - U - {"w", "t"}
assert nx.is_connected(H.subgraph(open_shore))
assert set(nx.node_boundary(H, open_shore)) == U | {"w", "t"}

# The literal boundary is the present Moser five-cycle.
assert {frozenset(e) for e in H.subgraph(U).edges()} == {
    frozenset(e)
    for e in [(x, "2"), ("2", "6"), ("6", y), (y, "4"), ("4", x)]
}

# Contract the two poles and verify the claimed planar quotient.
Q = nx.Graph()
Q.add_edges_from(edge_cycle(rim))
Q.add_edges_from(("h", z) for z in rim)
Q.add_edges_from(("alpha", z) for z in [x, *qs, y])
Q.add_edges_from(("beta", z) for z in ps)
assert nx.check_planarity(Q)[0]

# Adding a new vertex adjacent to all of U tests whether U is cofacial in
# some plane embedding.  Nonplanarity agrees with the direct Jordan proof.
cofacial_test = H.subgraph(set(H) - {"w", "t"}).copy()
cofacial_test.add_edges_from(("outer", u) for u in U)
assert not nx.check_planarity(cofacial_test)[0]

# Explicit tree decomposition of H, width five.
bags = [
    frozenset(["0", "2", "4", "5", "h", "q2"]),
    frozenset(["4", "5", "h", "q2", "q3"]),
    frozenset(["0", "2", "h", "q1", "q2"]),
    frozenset(["2", "4", "m", "q2"]),
    frozenset(["0", "5", "h", "p5"]),
    frozenset(["2", "5", "6", "q2"]),
    frozenset(["5", "h", "p1", "p5"]),
    frozenset(["ell", "h", "p1", "p5"]),
    frozenset(["ell", "h", "p1", "p4", "p5"]),
    frozenset(["ell", "h", "p1", "p3", "p4"]),
    frozenset(["ell", "h", "p1", "p2", "p3"]),
    frozenset(["ell", "t"]),
    frozenset(["ell", "w"]),
]
tree_edges = [
    (0, 1),
    (0, 2),
    (0, 3),
    (0, 4),
    (0, 5),
    (4, 6),
    (6, 7),
    (7, 8),
    (8, 9),
    (9, 10),
    (7, 11),
    (7, 12),
]
T = nx.Graph(tree_edges)
assert nx.is_tree(T)
assert max(map(len, bags)) - 1 == 5
assert set().union(*bags) == set(H)
for u, v in H.edges():
    assert any({u, v} <= bag for bag in bags)
for vertex in H:
    indices = {i for i, bag in enumerate(bags) if vertex in bag}
    assert nx.is_connected(T.subgraph(indices))

print("GREEN: crossed frame blocks every U-disk page")
print("GREEN: spanning quotient is planar with disjoint 3/5-port sets")
print("GREEN: explicit width-five decomposition excludes a K7 minor")
