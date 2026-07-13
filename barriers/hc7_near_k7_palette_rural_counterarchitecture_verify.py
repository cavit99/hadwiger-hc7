#!/usr/bin/env python3
"""Verify the literal palette/model/rural counterarchitecture.

Run with

    PYTHONPATH=active/runtime/deps python3 \
        barriers/hc7_near_k7_palette_rural_counterarchitecture_verify.py
"""

from itertools import combinations

import networkx as nx


def frequency_two_icosahedron() -> nx.Graph:
    """Return the frequency-two triangular refinement of the icosahedron."""
    base = nx.icosahedral_graph()
    planar, embedding = nx.check_planarity(base)
    assert planar

    faces = []
    seen = set()
    for u, v in embedding.edges():
        if (u, v) in seen:
            continue
        face = embedding.traverse_face(u, v, seen)
        assert len(face) == 3
        faces.append(tuple(face))
    assert len(faces) == 20

    old_edges = sorted(tuple(sorted(edge)) for edge in base.edges())
    midpoint = {edge: 12 + i for i, edge in enumerate(old_edges)}
    graph = nx.Graph()
    graph.add_nodes_from(base)
    for u, v in base.edges():
        m = midpoint[tuple(sorted((u, v)))]
        graph.add_edges_from(((u, m), (m, v)))
    for a, b, c in faces:
        m_ab = midpoint[tuple(sorted((a, b)))]
        m_bc = midpoint[tuple(sorted((b, c)))]
        m_ca = midpoint[tuple(sorted((c, a)))]
        graph.add_edges_from(((m_ab, m_bc), (m_bc, m_ca), (m_ca, m_ab)))
    return graph


P = frequency_two_icosahedron()
assert (P.number_of_nodes(), P.number_of_edges()) == (42, 120)
assert nx.check_planarity(P)[0]
assert nx.node_connectivity(P) == 5

# Add two adjacent universal apices.  Joining K_2 raises connectivity to 7.
a, b = "a", "b"
G = P.copy()
G.add_edge(a, b)
for u in P:
    G.add_edge(a, u)
    G.add_edge(b, u)
assert nx.node_connectivity(G) == 7

# The operation edge and a six-colouring after its deletion.
x, y = 0, 12
assert G.has_edge(x, y)
colour = {
    0: 0, 1: 3, 2: 2, 3: 0, 4: 3, 5: 0, 6: 1, 7: 1, 8: 1,
    9: 0, 10: 0, 11: 2, 12: 0, 13: 2, 14: 2, 15: 3, 16: 1,
    17: 1, 18: 1, 19: 0, 20: 2, 21: 1, 22: 3, 23: 0,
    24: 3, 25: 1, 26: 2, 27: 2, 28: 3, 29: 2, 30: 0,
    31: 2, 32: 1, 33: 3, 34: 3, 35: 0, 36: 3, 37: 2,
    38: 0, 39: 2, 40: 1, 41: 3,
    a: 4, b: 5,
}
H = G.copy()
H.remove_edge(x, y)
assert colour[x] == colour[y] == 0
assert all(colour[u] != colour[v] for u, v in H.edges())
for beta in range(1, 6):
    bichromatic = H.subgraph(
        vertex for vertex in H if colour[vertex] in {0, beta}
    )
    assert nx.has_path(bichromatic, x, y)
    assert any(colour[z] == beta for z in H[x])
    assert any(colour[z] == beta for z in H[y])

# A fixed K_5-model, disjoint from x,y, with an SDR of the five non-alpha
# palette colours.  The third bag is deliberately multicoloured.
frame = ({a}, {b}, {21, 27}, {22}, {26})
assert all(x not in bag and y not in bag for bag in frame)
assert all(nx.is_connected(G.subgraph(bag)) for bag in frame)
for left, right in combinations(frame, 2):
    assert any(G.has_edge(u, v) for u in left for v in right)
representatives = (a, b, 21, 22, 26)
assert [colour[z] for z in representatives] == [4, 5, 1, 3, 2]

# Remove the three planar frame bags.  The singleton C is an off-gate lobe
# behind the two poles 25,28.  It misses exactly frame bag {22} and has two
# literal portals, 21 and 27, in the repeated owner {21,27}.
planar_frame_vertices = {21, 27, 22, 26}
D = P.subgraph(set(P) - planar_frame_vertices).copy()
poles = {25, 28}
components = list(nx.connected_components(D.subgraph(set(D) - poles)))
assert {3} in components
C = {3}
assert set(G[3]) == {a, b, 21, 25, 26, 27, 28}
assert set(G[3]) & {21, 27} == {21, 27}
assert G.has_edge(3, 26)
assert not G.has_edge(3, 22)
assert len(set(G[3])) == 7

print("frequency-two icosahedron: planar and 5-connected")
print("two-apex join: 7-connected and K7-minor-free by planarity")
print("operation edge: endpoint-complete common five-palette state")
print("fixed K5 frame: distinct-colour SDR present")
print("exact-seven lobe: repeated owner, one missed frame row, two gate poles")
print("coherent rural certificate: G-{a,b}=P is planar")
