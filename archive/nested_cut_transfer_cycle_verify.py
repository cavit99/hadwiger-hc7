#!/usr/bin/env python3
"""Certificate that disjoint cut transport can cycle six-colour states.

Each equality block is K5 joined to two nonadjacent terminals.  In every
proper six-colouring the terminal colours are equal.  Seven disjoint
blocks implement an arbitrary permutation of a seven-vertex boundary;
an inverse layer returns every labelled boundary assignment.  A tree of
bridges connects the construction without creating a K7 minor.
"""

from __future__ import annotations

from itertools import product

import networkx as nx


COLOURS = tuple(range(6))
ORDER = 7
PERMUTATION = tuple((i + 1) % ORDER for i in range(ORDER))
INVERSE = tuple(PERMUTATION.index(i) for i in range(ORDER))


def add_equality_layer(
    graph: nx.Graph,
    left: tuple[str, ...],
    right: tuple[str, ...],
    permutation: tuple[int, ...],
    prefix: str,
    connect_blocks: bool,
) -> None:
    anchors = []
    for i in range(ORDER):
        clique = tuple(f"{prefix}_c{i}_{j}" for j in range(5))
        graph.add_edges_from((u, v) for pos, u in enumerate(clique) for v in clique[pos + 1 :])
        graph.add_edges_from((left[i], vertex) for vertex in clique)
        graph.add_edges_from((right[permutation[i]], vertex) for vertex in clique)
        anchors.append(clique[0])
    if connect_blocks:
        graph.add_edges_from((anchors[i], anchors[i + 1]) for i in range(ORDER - 1))


def verify_local_equality_gadget() -> None:
    # Brute-force the five clique colours for every endpoint colour pair.
    feasible = set()
    for left_colour, right_colour in product(COLOURS, repeat=2):
        for clique_colours in product(COLOURS, repeat=5):
            if len(set(clique_colours)) < 5:
                continue
            if left_colour in clique_colours or right_colour in clique_colours:
                continue
            feasible.add((left_colour, right_colour))
            break
    assert feasible == {(colour, colour) for colour in COLOURS}


def main() -> None:
    verify_local_equality_gadget()

    left = tuple(f"s{i}" for i in range(ORDER))
    middle = tuple(f"m{i}" for i in range(ORDER))
    right = tuple(f"z{i}" for i in range(ORDER))
    graph = nx.Graph()
    graph.add_nodes_from((*left, *middle, *right))
    add_equality_layer(graph, left, middle, PERMUTATION, "forward", True)
    add_equality_layer(graph, middle, right, INVERSE, "inverse", False)

    assert nx.is_connected(graph)
    assert PERMUTATION != tuple(range(ORDER))
    assert all(INVERSE[PERMUTATION[i]] == i for i in range(ORDER))

    # Seven explicitly disjoint transport paths in each layer.
    forward_paths = [
        (left[i], f"forward_c{i}_0", middle[PERMUTATION[i]]) for i in range(ORDER)
    ]
    inverse_paths = [
        (middle[i], f"inverse_c{i}_0", right[INVERSE[i]]) for i in range(ORDER)
    ]
    assert len(set().union(*(set(path) for path in forward_paths))) == 3 * ORDER
    assert len(set().union(*(set(path) for path in inverse_paths))) == 3 * ORDER
    assert all(graph.has_edge(path[0], path[1]) and graph.has_edge(path[1], path[2])
               for path in (*forward_paths, *inverse_paths))

    # Every 2-connected block has at most seven vertices.  A seven-vertex
    # block is exactly K7 minus the nonedge between its two terminals, so
    # it has no K7 minor; smaller blocks cannot contain one.  Since K7 is
    # 2-connected, the whole graph is K7-minor-free.
    blocks = tuple(nx.biconnected_components(graph))
    assert max(map(len, blocks)) == 7
    for block in blocks:
        if len(block) == 7:
            assert graph.subgraph(block).number_of_edges() == 20
        else:
            assert len(block) <= 2

    # Symbolic composition: m[pi(i)]=s[i], then
    # z[pi^{-1}(j)]=m[j], hence z[i]=s[i].
    for i in range(ORDER):
        middle_index = PERMUTATION[i]
        final_index = INVERSE[middle_index]
        assert final_index == i

    print("local six-colour equality gadget verified")
    print("connected vertices", graph.number_of_nodes(), "edges", graph.number_of_edges())
    print("biconnected blocks", len(blocks), "maximum order", max(map(len, blocks)))
    print("forward permutation", PERMUTATION)
    print("inverse composition returns every boundary assignment")
    print("transport-cycle counterarchitecture verified")


if __name__ == "__main__":
    main()
