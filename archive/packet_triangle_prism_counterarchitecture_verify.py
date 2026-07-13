#!/usr/bin/env python3
"""A 3-connected pairwise-but-not-triple packet counterarchitecture.

Six singleton portal classes are placed at the six vertices of a
triangular prism.  Each two-demand subset of the displayed matching is
linkable by disjoint connected carriers, but the three demands are not
simultaneously linkable.  Thus a uniform packet theorem needs a coherent
planar/prism outcome; a two-cut alternative alone is false.
"""

import itertools

import networkx as nx


EDGES = {
    (0, 1), (0, 2), (0, 3),
    (1, 4), (1, 5),
    (2, 3), (2, 5),
    (3, 4),
    (4, 5),
}
DEMANDS = ((0, 2), (1, 3), (4, 5))


def path_masks(graph, ends):
    first, second = ends
    return {
        frozenset(path)
        for path in nx.all_simple_paths(graph, first, second)
    }


def main():
    graph = nx.Graph()
    graph.add_nodes_from(range(6))
    graph.add_edges_from(EDGES)

    assert nx.is_isomorphic(graph, nx.circular_ladder_graph(3))
    assert nx.node_connectivity(graph) == 3

    carriers = [path_masks(graph, demand) for demand in DEMANDS]
    pair_witnesses = {}
    for first, second in itertools.combinations(range(3), 2):
        witness = next(
            (
                (left, right)
                for left in carriers[first]
                for right in carriers[second]
                if left.isdisjoint(right)
            ),
            None,
        )
        assert witness is not None
        pair_witnesses[(first, second)] = witness

    triple = next(
        (
            (first, second, third)
            for first in carriers[0]
            for second in carriers[1]
            for third in carriers[2]
            if first.isdisjoint(second)
            and first.isdisjoint(third)
            and second.isdisjoint(third)
        ),
        None,
    )
    assert triple is None

    print("core: triangular prism; vertex connectivity 3")
    for pair, witness in sorted(pair_witnesses.items()):
        print("packet", pair, "carriers", tuple(tuple(sorted(x)) for x in witness))
    print("simultaneous three-linkage: none")


if __name__ == "__main__":
    main()
