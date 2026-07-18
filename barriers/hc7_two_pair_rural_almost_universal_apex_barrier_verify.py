"""Verify the almost-universal two-apex rural barrier.

Run from the repository root with:
  PYTHONPATH=active/runtime/deps python3 \
      barriers/hc7_two_pair_rural_almost_universal_apex_barrier_verify.py
"""

from __future__ import annotations

from itertools import combinations
from pathlib import Path
import sys


LOCAL_DEPS = Path(__file__).resolve().parents[1] / "active" / "runtime" / "deps"
if LOCAL_DEPS.is_dir():
    sys.path.insert(0, str(LOCAL_DEPS))

import networkx as nx


Vertex = object


def pentagonal_tube() -> nx.Graph:
    graph = nx.Graph()
    graph.add_nodes_from(("Top", "Bottom"))
    for layer in range(3):
        for index in range(5):
            graph.add_edge((layer, index), (layer, (index + 1) % 5))
    for index in range(5):
        graph.add_edge("Top", (0, index))
        graph.add_edge("Bottom", (2, index))
    for layer in range(2):
        for index in range(5):
            graph.add_edge((layer, index), (layer + 1, index))
            graph.add_edge((layer, index), (layer + 1, (index - 1) % 5))
    return graph


def has_edge_between(graph: nx.Graph, left: set[Vertex], right: set[Vertex]) -> bool:
    return any(graph.has_edge(x, y) for x in left for y in right)


def linked(
    graph: nx.Graph,
    first: tuple[Vertex, Vertex],
    second: tuple[Vertex, Vertex],
) -> bool:
    for path in nx.all_simple_paths(graph, *first):
        if set(path) & set(second):
            continue
        remainder = graph.copy()
        remainder.remove_nodes_from(path)
        if nx.has_path(remainder, *second):
            return True
    return False


core = pentagonal_tube()
assert nx.check_planarity(core)[0]
assert nx.node_connectivity(core) == 5
print("tube: planar and 5-connected")

x = (0, 0)
u = (1, 0)
v = (1, 4)
p = "p"
q = "q"

host = core.copy()
host.add_edge(p, q)
host.add_edges_from((p, vertex) for vertex in core if vertex != u)
host.add_edges_from((q, vertex) for vertex in core if vertex != v)

assert nx.node_connectivity(host) == 7
assert host.degree(x) == 7
# The Markdown proof certifies K7-minor exclusion: deleting p,q leaves the
# planar core, while at most two branch sets of a K7 model can contain p,q.
print("host: 7-connected and K7-minor-free by the two-apex argument")

boundary = set(host.neighbors(x))
left = {x}
right = set(host) - left - boundary
I = {p, u}
J = {q, v}
B = boundary - I - J

assert len(boundary) == 7
assert B == {"Top", (0, 1), (0, 4)}
assert nx.is_connected(host.subgraph(right))
assert not has_edge_between(host, left, right)
assert not host.has_edge(p, u)
assert not host.has_edge(q, v)

independence_number = max(
    len(candidate)
    for size in range(len(boundary) + 1)
    for candidate in combinations(boundary, size)
    if all(not host.has_edge(a, b) for a, b in combinations(candidate, 2))
)
assert independence_number == 2

rooted = host.subgraph(left | I | J).copy()
assert {frozenset(edge) for edge in rooted.edges()} == {
    frozenset(edge)
    for edge in [
        (x, p),
        (x, q),
        (x, u),
        (x, v),
        (p, q),
        (q, u),
        (u, v),
        (v, p),
    ]
}
assert nx.check_planarity(rooted)[0]
assert not linked(rooted, (p, u), (q, v))
print("boundary: alpha 2; alternating wheel has no required two-linkage")

a = "Top"
s = (0, 1)
t = (0, 4)
rows = {
    "I": {p, u, (2, 0)},
    "J": {q, v, (2, 4)},
    "s": {s, (1, 1), (1, 2)},
    "t": {t, (1, 3), (0, 3)},
    "0": {(0, 2)},
}
assert sum(map(len, rows.values())) == len(set().union(*rows.values()))
assert set().union(*rows.values()) <= (right | boundary) - {a}
for row in rows.values():
    assert nx.is_connected(host.subgraph(row))
    assert has_edge_between(host, {a}, row)
for first, second in combinations(rows.values(), 2):
    assert has_edge_between(host, first, second)
assert rows["I"] & boundary == I
assert rows["J"] & boundary == J
assert rows["s"] & boundary == {s}
assert rows["t"] & boundary == {t}
assert not rows["0"] & boundary
print("rows: exact traces and all required adjacencies verified")

explicit_k5 = {
    frozenset({s, t}): {p, q, "Top", (0, 2), (0, 3)},
    frozenset({"Top", s}): {p, q, "Bottom", (2, 0), (2, 1)},
    frozenset({"Top", t}): {p, q, "Bottom", (2, 0), (2, 1)},
}
for deleted in combinations(B, 2):
    clique = explicit_k5[frozenset(deleted)]
    assert clique.isdisjoint(deleted)
    assert len(clique) == 5
    assert all(host.has_edge(y, z) for y, z in combinations(clique, 2))
print("transversal: every pair in B misses an explicit K5 subgraph")

# Supply a deterministic explicit six-colouring rather than rely only on the
# Four Colour Theorem in the verification script.
core_colouring = nx.coloring.greedy_color(
    core, strategy="saturation_largest_first"
)
assert max(core_colouring.values()) < 4
colouring = {**core_colouring, p: 4, q: 5}
assert all(colouring[y] != colouring[z] for y, z in host.edges())
print("colouring: explicit proper 6-colouring verified")
