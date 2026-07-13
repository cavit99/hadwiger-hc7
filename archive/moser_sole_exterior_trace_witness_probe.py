#!/usr/bin/env python3
"""Verify the sharp fixed-trace witness from the accompanying note.

Run with

    PYTHONPATH=.deps python3 moser_sole_exterior_trace_witness_probe.py

The script uses NetworkX only for connectivity.  Colour extension is
checked by an explicit DSATUR-style exhaustive backtracking routine.
"""

from __future__ import annotations

import itertools

import networkx as nx


MOSER_EDGES = {
    (0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (1, 6),
    (2, 6), (3, 4), (3, 5), (4, 5), (5, 6),
}
U = (0, 5, 2, 4, 6)
MISSING_CYCLE = tuple(zip(U, U[1:] + U[:1]))
R = ("r0", "r1", "r2")


def build_graph() -> tuple[nx.Graph, tuple[str, ...]]:
    g = nx.Graph()
    g.add_nodes_from(range(7))
    g.add_edges_from(MOSER_EDGES)

    z_vertices: list[str] = []
    for i, (x, y) in enumerate(MISSING_CYCLE):
        q, p = f"q{i}", f"p{i}"
        z_vertices.extend((q, p))
        g.add_edges_from(((x, q), (q, p), (p, y)))

    # The repeated-colour vertices raise all subdivision vertices to
    # degree seven.  They do not belong to the five-colour KM host.
    for r in R:
        for z in z_vertices:
            g.add_edge(r, z)

    for z in z_vertices:
        g.add_edge(1, z)
        g.add_edge(3, z)

    # Four sparse boundary contacts are exactly enough to raise the four
    # low-degree boundary vertices and the global connectivity to seven.
    g.add_edges_from(((2, "r0"), (4, "r0"), (5, "r0"), (6, "r1")))

    g.add_node("v")
    g.add_edges_from(("v", x) for x in range(7))
    return g, tuple(z_vertices)


def extend_colouring(
    graph: nx.Graph, precolouring: dict[object, int], colours: int = 6
) -> dict[object, int] | None:
    assignment = dict(precolouring)
    vertices = tuple(graph)

    for x, y in graph.edges:
        if x in assignment and y in assignment and assignment[x] == assignment[y]:
            return None

    def search() -> dict[object, int] | None:
        if len(assignment) == len(vertices):
            return dict(assignment)

        uncoloured = (x for x in vertices if x not in assignment)
        x = max(
            uncoloured,
            key=lambda z: (
                len({assignment[n] for n in graph[z] if n in assignment}),
                graph.degree(z),
            ),
        )
        forbidden = {assignment[n] for n in graph[x] if n in assignment}
        for colour in range(colours):
            if colour in forbidden:
                continue
            assignment[x] = colour
            answer = search()
            if answer is not None:
                return answer
            del assignment[x]
        return None

    return search()


def exact_trace(pair: tuple[int, int]) -> dict[int, int]:
    remaining = [x for x in range(7) if x not in pair]
    result = {pair[0]: 0, pair[1]: 0}
    result.update({x: i + 1 for i, x in enumerate(remaining)})
    return result


def main() -> None:
    g, z_vertices = build_graph()
    h = g.copy()
    h.remove_node("v")
    c = g.subgraph((*z_vertices, *R)).copy()

    assert set(g.subgraph(range(7)).edges) == MOSER_EDGES
    assert nx.is_connected(c)
    assert min(dict(g.degree()).values()) == 7
    assert nx.node_connectivity(g) == 7
    assert set(nx.minimum_node_cut(g)) == set(range(7))

    nonedges = tuple(
        pair for pair in itertools.combinations(range(7), 2)
        if not g.has_edge(*pair)
    )
    assert len(nonedges) == 10
    for pair in nonedges:
        assert extend_colouring(h, exact_trace(pair)) is not None

    trace_13 = {1: 0, 3: 0, 0: 1, 5: 2, 2: 3, 4: 4, 6: 5}
    base = dict(trace_13)
    for i, (x, y) in enumerate(MISSING_CYCLE):
        base[f"q{i}"] = trace_13[y]
        base[f"p{i}"] = trace_13[x]
    base.update({r: 0 for r in R})
    assert len(base) == len(h)
    assert all(base[x] != base[y] for x, y in h.edges)

    # Every internal edge has the aligned trace-edge witness: deleting it
    # and identifying its ends is exactly the precolouring-extension test.
    for x, y in c.edges:
        deleted = h.copy()
        deleted.remove_edge(x, y)
        identified = nx.contracted_nodes(deleted, x, y, self_loops=False)
        assert extend_colouring(identified, trace_13) is not None

    # The five-colour host is exactly a subdivision of K5.  For every
    # missing root edge its two private degree-two vertices are compulsory
    # in any rooted K5 model confined to this host: otherwise that required
    # bag adjacency has no realizing edge.  The assertions below certify
    # the displayed decomposition.
    w = h.subgraph((*U, *z_vertices)).copy()
    for i, (x, y) in enumerate(MISSING_CYCLE):
        q, p = f"q{i}", f"p{i}"
        assert set(w[q]) == {x, p}
        assert set(w[p]) == {q, y}
    assert all(w.has_edge(x, y) for x, y in itertools.combinations(U, 2)
               if (x, y) not in MISSING_CYCLE and (y, x) not in MISSING_CYCLE)

    # The warning is deliberately not an uncoloured counterexample.  These
    # explicit bags form another rooted K5 model using repeated-colour
    # vertices and leave (for example) q1 as a 1--3 connector.
    bags = (
        {0},
        {5, "q0", "p0"},
        {2, "r0"},
        {4},
        {6, "r1", "p2", "p4"},
    )
    assert all(nx.is_connected(h.subgraph(bag)) for bag in bags)
    assert all(
        any(h.has_edge(x, y) for x in bags[i] for y in bags[j])
        for i, j in itertools.combinations(range(5), 2)
    )
    used = set().union(*bags)
    assert "q1" not in used and h.has_edge(1, "q1") and h.has_edge(3, "q1")

    assert extend_colouring(g, {}, colours=5) is not None
    assert extend_colouring(g, {}, colours=4) is None

    print("verified: kappa=delta=7")
    print("verified: all ten exact one-pair traces")
    print("verified: every internal edge has a fixed-13 aligned witness")
    print("verified: fixed five-colour subdivision certificate is locked")
    print("verified: palette wall fails and an uncoloured repair exists")


if __name__ == "__main__":
    main()
