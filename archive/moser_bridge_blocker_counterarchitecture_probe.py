#!/usr/bin/env python3
# /// script
# dependencies = ["networkx==3.6.1"]
# ///
"""Verifier for the central-orbit static bridge/model counterarchitecture.

The construction deliberately satisfies one exact Moser trace, all of its
Kempe connections, seven-connectivity, and a forced supported connector, but
is not a counterexample-derived palette wall.
"""

from itertools import combinations

import networkx as nx


EDGES = [
    (0,8),(0,20),(0,23),(0,35),(0,39),(1,17),(1,18),(1,20),(1,22),(1,24),
    (2,6),(2,17),(2,22),(2,23),(2,26),(2,39),(3,10),(3,19),(3,28),(3,31),
    (3,40),(4,13),(4,16),(4,30),(4,37),(4,38),(4,41),(5,22),(5,26),(5,29),
    (5,32),(5,34),(6,12),(6,26),(6,35),(6,39),(7,10),(7,31),(7,36),(7,37),
    (7,41),(8,14),(8,15),(8,18),(8,20),(8,35),(9,12),(9,14),(9,19),(9,25),
    (9,26),(9,31),(9,38),(10,31),(10,36),(10,40),(11,13),(11,16),(11,22),
    (11,24),(11,34),(12,14),(12,26),(12,35),(13,15),(13,16),(13,24),(13,38),
    (14,15),(14,35),(14,38),(15,18),(15,24),(15,38),(16,29),(16,30),(16,34),
    (17,20),(17,22),(17,23),(18,20),(18,24),(19,21),(19,28),(19,31),(19,38),
    (20,23),(21,27),(21,28),(21,37),(21,38),(22,24),(22,26),(22,34),(23,39),
    (25,26),(25,31),(25,32),(25,33),(26,32),(27,28),(27,36),(27,37),(27,40),
    (28,40),(29,30),(29,32),(29,33),(29,34),(30,31),(30,33),(30,41),(31,33),
    (31,41),(32,33),(35,39),(36,37),(36,40),(37,38),(37,41),
]

# Moser label -> vertex of the planar triangulation L.
MOSER = {0:31, 1:7, 2:41, 3:9, 4:19, 5:38, 6:37}
MOSER_EDGES = {
    tuple(sorted(e)) for e in
    [(0,1),(0,2),(0,3),(0,4),(1,2),(1,6),(2,6),
     (3,4),(3,5),(4,5),(5,6)]
}

T1, T2, APEX = 42, 43, 44
D, L_END = MOSER[6], MOSER[3]       # central repeated pair 6|3
UNIQUE_LABELS = (0, 1, 2, 4, 5)
UNIQUE = tuple(MOSER[i] for i in UNIQUE_LABELS)

# Exact 6-colouring: d,l have colour 0 and the five roots are rainbow.
TRACE_COLOUR = {
    0:2,8:0,20:1,23:0,35:3,39:1,1:0,17:3,18:3,22:1,24:2,2:2,6:0,
    26:3,3:3,10:0,19:4,28:1,31:1,40:2,4:2,13:3,16:1,30:0,37:0,
    38:5,41:3,5:0,29:2,32:1,34:3,12:1,7:2,36:1,14:2,15:1,9:0,
    25:2,11:0,21:2,27:3,33:3,T1:4,T2:5,
}

# One bichromatic path for every missing edge on the five unique roots.
KEMPE_PATHS = {
    tuple(sorted((MOSER[0], MOSER[5]))): [MOSER[0], T2, 15, MOSER[5]],
    tuple(sorted((MOSER[1], MOSER[4]))): [MOSER[1], T1, 21, MOSER[4]],
    tuple(sorted((MOSER[1], MOSER[5]))): [MOSER[1], T2, 4, MOSER[5]],
    tuple(sorted((MOSER[2], MOSER[4]))): [MOSER[2], T1, 3, MOSER[4]],
    tuple(sorted((MOSER[2], MOSER[5]))): [MOSER[2], T2, 13, MOSER[5]],
}

# A U-rooted K5.  The last two bags deliberately use T1,T2.
ROOTED_K5 = [
    {MOSER[0]}, {MOSER[1]}, {MOSER[2]},
    {MOSER[4], 21, T1}, {MOSER[5], 14, T2},
]

# An unrelated six-colouring of G, proving that the palette wall fails.
G_COLOUR = {
    0:2,8:3,20:1,23:3,35:1,39:0,1:3,17:0,18:2,22:1,24:0,2:2,6:3,
    26:0,3:3,10:2,19:4,28:1,31:0,40:0,4:0,13:2,16:1,30:2,37:5,
    38:3,41:3,5:3,29:0,32:1,34:2,12:2,7:1,36:3,14:0,15:1,9:1,
    25:2,11:3,21:0,27:2,33:3,T1:4,T2:5,APEX:2,
}


def build():
    planar = nx.Graph(EDGES)
    h = planar.copy()
    h.add_edge(T1, T2)
    for x in planar:
        if x not in {L_END, MOSER[4]}:
            h.add_edge(T1, x)
        if x not in {D, MOSER[5]}:
            h.add_edge(T2, x)
    g = h.copy()
    g.add_edges_from((APEX, MOSER[i]) for i in range(7))
    return planar, h, g


def is_path(graph, path):
    return all(graph.has_edge(x, y) for x, y in zip(path, path[1:]))


def pairwise_adjacent(graph, bags):
    return all(any(graph.has_edge(x, y) for x in bags[i] for y in bags[j])
               for i, j in combinations(range(len(bags)), 2))


def main():
    planar, h, g = build()
    boundary = set(MOSER.values())
    exterior = set(h) - boundary

    assert planar.number_of_nodes() == 42 and planar.number_of_edges() == 120
    assert nx.check_planarity(planar)[0]
    assert nx.node_connectivity(planar) == 5
    actual = {
        tuple(sorted((i, j))) for i, j in combinations(range(7), 2)
        if planar.has_edge(MOSER[i], MOSER[j])
    }
    assert actual == MOSER_EDGES

    assert nx.is_connected(h.subgraph(exterior))
    assert {s for s in boundary if nx.has_path(h.subgraph(exterior | {s}), s, T1)} == boundary
    assert nx.node_connectivity(h) == 7
    assert nx.node_connectivity(g) == 7
    assert min(dict(h.degree()).values()) == 7
    assert min(dict(g.degree()).values()) == 7

    connector = [D, T1, T2, L_END]
    assert is_path(h, connector)
    assert h.subgraph(connector).number_of_edges() == 3       # induced
    carrier_graph = h.subgraph(exterior | {D, L_END})
    assert nx.shortest_path_length(carrier_graph, D, L_END) == 3

    assert set(TRACE_COLOUR) == set(h)
    assert all(TRACE_COLOUR[x] != TRACE_COLOUR[y] for x, y in h.edges)
    assert TRACE_COLOUR[D] == TRACE_COLOUR[L_END] == 0
    assert len({TRACE_COLOUR[x] for x in UNIQUE}) == 5
    assert {TRACE_COLOUR[x] for x in UNIQUE} == {1, 2, 3, 4, 5}

    missing = {
        tuple(sorted((x, y))) for x, y in combinations(UNIQUE, 2)
        if not h.has_edge(x, y)
    }
    assert set(KEMPE_PATHS) == missing
    for (x, y), path in KEMPE_PATHS.items():
        assert path[0] in {x, y} and path[-1] in {x, y}
        assert is_path(h, path)
        assert set(path[1:-1]) <= exterior
        assert {TRACE_COLOUR[z] for z in path} <= {TRACE_COLOUR[x], TRACE_COLOUR[y]}
    for e, f in combinations(missing, 2):
        if set(e).isdisjoint(f):
            assert set(KEMPE_PATHS[e]).isdisjoint(KEMPE_PATHS[f])

    # The two non-alpha colours have exactly one off-root representative.
    assert {x for x, c in TRACE_COLOUR.items() if c == 4} == {MOSER[4], T1}
    assert {x for x, c in TRACE_COLOUR.items() if c == 5} == {MOSER[5], T2}
    supported_vertices = {
        x for x in h if TRACE_COLOUR[x] in {0, 4, 5}
    } - set(UNIQUE)
    supported = h.subgraph(supported_vertices)
    assert nx.has_path(supported, D, L_END)
    assert not nx.has_path(supported.subgraph(set(supported) - {T1}), D, L_END)
    assert not nx.has_path(supported.subgraph(set(supported) - {T2}), D, L_END)

    assert all(nx.is_connected(h.subgraph(bag)) for bag in ROOTED_K5)
    assert pairwise_adjacent(h, ROOTED_K5)
    assert [next(iter(bag & set(UNIQUE))) for bag in ROOTED_K5] == list(UNIQUE)
    assert nx.check_planarity(h.subgraph(set(h) - {T1, T2}))[0]
    # Hence every K5-model, rooted or not, uses T1 or T2: otherwise it is
    # a K5-minor of the displayed planar graph.

    assert set(G_COLOUR) == set(g)
    assert all(G_COLOUR[x] != G_COLOUR[y] for x, y in g.edges)

    print("planar_core", planar.number_of_nodes(), planar.number_of_edges(),
          "kappa", nx.node_connectivity(planar))
    print("induced_boundary=pure_Moser repeated_pair=6|3")
    print("sole_exterior", len(exterior), "kappa_H", nx.node_connectivity(h),
          "kappa_G", nx.node_connectivity(g))
    print("minimum_supported_connector", connector, "forced_vertices", (T1, T2))
    print("exact_trace_and_all_Kempe_paths=True")
    print("explicit_rooted_K5", ROOTED_K5)
    print("every_rooted_K5_hits_forced_vertices=True (planarity certificate)")
    print("G_six_colourable=True; full_palette_wall_axiom=False")


if __name__ == "__main__":
    main()
