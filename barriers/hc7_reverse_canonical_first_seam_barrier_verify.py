"""Verify the canonical reverse first-seam barrier.

The script uses only NetworkX.  It checks connectivity, exact packet
numbers, the named contraction and demand-three trace, absence of every
reserved-anchor rooted K5, the displayed literal K7 model, a five-colouring,
and the precise failure of Dirac's neighbourhood inequality.
"""

from __future__ import annotations

import itertools
import sys
from pathlib import Path

DEPS = Path(__file__).resolve().parents[1] / "active" / "runtime" / "deps"
if DEPS.exists():
    sys.path.insert(0, str(DEPS))

import networkx as nx


OMEGA = tuple(range(7))
I = frozenset({0, 1, 2})
J = frozenset({3, 4, 5, 6})
D = ("d1", "d2")
B = ("b",)


def build_graph() -> nx.Graph:
    graph = nx.Graph()
    graph.add_nodes_from(OMEGA)
    graph.add_nodes_from(D + B)
    graph.add_edges_from((i, j) for i in I for j in J)
    graph.add_edges_from(((6, 3), (3, 4), (4, 5)))
    graph.add_edge(*D)
    for packet_vertex in D + B:
        graph.add_edges_from((packet_vertex, s) for s in OMEGA)
    return graph


G = build_graph()
H = G.subgraph(OMEGA).copy()


def independence_number(graph: nx.Graph) -> int:
    return max(
        (len(clique) for clique in nx.find_cliques(nx.complement(graph))),
        default=0,
    )


def clique_number(graph: nx.Graph) -> int:
    return max((len(clique) for clique in nx.find_cliques(graph)), default=0)


def connected_full_packets(vertices: tuple[object, ...]) -> list[frozenset[object]]:
    packets: list[frozenset[object]] = []
    for size in range(1, len(vertices) + 1):
        for candidate_tuple in itertools.combinations(vertices, size):
            candidate = frozenset(candidate_tuple)
            if not nx.is_connected(G.subgraph(candidate)):
                continue
            if all(any(G.has_edge(v, s) for v in candidate) for s in OMEGA):
                packets.append(candidate)
    return packets


def packing_number(packets: list[frozenset[object]]) -> int:
    best = 0
    for size in range(1, len(packets) + 1):
        if any(
            all(left.isdisjoint(right) for left, right in itertools.combinations(choice, 2))
            for choice in itertools.combinations(packets, size)
        ):
            best = size
    return best


def contract_cluster(cluster: frozenset[object], name: object) -> nx.Graph:
    minor = nx.Graph()
    outside = set(G) - set(cluster)
    minor.add_nodes_from(outside | {name})
    minor.add_edges_from((u, v) for u, v in G.edges() if u in outside and v in outside)
    for v in outside:
        if any(G.has_edge(v, w) for w in cluster):
            minor.add_edge(name, v)
    return minor


def proper_colouring(graph: nx.Graph, colouring: dict[object, int]) -> bool:
    return set(colouring) == set(graph) and all(
        colouring[u] != colouring[v] for u, v in graph.edges()
    )


def rooted_k5(graph: nx.Graph, roots: tuple[object, ...]) -> bool:
    """Exact rooted-model search; every root is fixed in its named bag."""

    assert len(roots) == 5 and len(set(roots)) == 5
    extras = tuple(v for v in graph if v not in roots)
    # -1 means unused; 0,...,4 assigns an extra vertex to that rooted bag.
    for assignment in itertools.product(range(-1, 5), repeat=len(extras)):
        bags = [{roots[index]} for index in range(5)]
        for vertex, label in zip(extras, assignment, strict=True):
            if label >= 0:
                bags[label].add(vertex)
        if not all(nx.is_connected(graph.subgraph(bag)) for bag in bags):
            continue
        if all(
            any(graph.has_edge(u, v) for u in bags[i] for v in bags[j])
            for i in range(5)
            for j in range(i)
        ):
            return True
    return False


def literal_clique_model(graph: nx.Graph, bags: tuple[frozenset[object], ...]) -> bool:
    if any(not bag for bag in bags):
        return False
    if any(not left.isdisjoint(right) for left, right in itertools.combinations(bags, 2)):
        return False
    if not all(nx.is_connected(graph.subgraph(bag)) for bag in bags):
        return False
    return all(
        any(graph.has_edge(u, v) for u in bags[i] for v in bags[j])
        for i in range(len(bags))
        for j in range(i)
    )


# Exact separation and connectivity.
assert not any(G.has_edge(d, b) for d in D for b in B)
assert nx.node_connectivity(G) == 7
open_shores = G.subgraph(set(G) - set(OMEGA))
assert len(list(nx.connected_components(open_shores))) == 2

# Packet vector and exhaustion.
d_packets = connected_full_packets(D)
b_packets = connected_full_packets(B)
assert packing_number(d_packets) == 2
assert packing_number(b_packets) == 1
assert frozenset({"d1"}) in d_packets and frozenset({"d2"}) in d_packets
assert frozenset(D) == frozenset({"d1"}) | frozenset({"d2"})

# Boundary invariants and the canonical maximum-independent contraction.
assert independence_number(H) == 3
assert I in [frozenset(clique) for clique in nx.find_cliques(nx.complement(H))]
assert clique_number(H) == 3

cluster = frozenset(B) | I
minor = contract_cluster(cluster, "t")
minor_colouring = {
    "t": 0,
    4: 1,
    3: 2,
    5: 2,
    6: 3,
    "d1": 4,
    "d2": 5,
}
assert proper_colouring(minor, minor_colouring)

partition = (I, frozenset({4}), frozenset({3, 5}), frozenset({6}))
assert all(
    not any(H.has_edge(u, v) for u, v in itertools.combinations(block, 2))
    for block in partition
)
singletons = frozenset().union(*(block for block in partition if len(block) == 1))
demand = len(partition) - clique_number(H.subgraph(singletons))
assert singletons == frozenset({4, 6})
assert demand == 3

# No reserved-anchor rooted K5 for any of the 21 anchor pairs.
for x, y in itertools.combinations(OMEGA, 2):
    roots = tuple(s for s in OMEGA if s not in {x, y})
    closed_side = G.subgraph(set(roots) | set(B)).copy()
    assert not rooted_k5(closed_side, roots), (x, y)

# Literal K7 terminal certificate.
k7_bags = (
    frozenset({2, 6}),
    frozenset({1, 4}),
    frozenset({5}),
    frozenset({"b", 3}),
    frozenset({0}),
    frozenset({"d1"}),
    frozenset({"d2"}),
)
assert literal_clique_model(G, k7_bags)

# The graph is five-colourable and hence is not an HC7 kernel graph.
five_colouring = {
    0: 0,
    1: 0,
    2: 0,
    3: 1,
    5: 1,
    4: 2,
    6: 2,
    "d1": 3,
    "d2": 4,
    "b": 3,
}
assert proper_colouring(G, five_colouring)

# Exact Dirac-neighbourhood failures.
dirac_failures = {
    v
    for v in G
    if independence_number(G.subgraph(tuple(G.neighbors(v)))) > G.degree(v) - 5
}
assert dirac_failures == {5, 6, "b"}

print("vertices", G.number_of_nodes())
print("connectivity", nx.node_connectivity(G))
print("packet_vector", (packing_number(d_packets), packing_number(b_packets)))
print("canonical_independent_block", sorted(I))
print("boundary_partition", [sorted(block) for block in partition])
print("demand", demand)
print("reserved_anchor_pairs_without_rooted_K5", 21)
print("literal_K7_bags", [sorted(map(str, bag)) for bag in k7_bags])
print("five_colourable", True)
print("Dirac_failures", sorted(map(str, dirac_failures)))
