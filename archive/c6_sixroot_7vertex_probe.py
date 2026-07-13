#!/usr/bin/env python3
"""Seven-vertex laboratory for the six-terminal C6 linkage core.

This is not used as a proof of the unbounded theorem.  It tests the
label-preserving structural target suggested by the exact C6 analysis:
among 3-connected graphs with six prescribed roots and one additional
vertex, do the audited forbidden linkages and four owned frames force a
rooted triangular-prism minor?
"""

from functools import lru_cache
from itertools import permutations

import networkx as nx


CYCLE_EDGES = tuple((i, (i + 1) % 6) for i in range(6))
EVEN = (0, 2, 4)
ODD = (1, 3, 5)
IDENTITY = frozenset(((0, 3), (2, 5), (4, 1)))
NONIDENTITY_MATCHINGS = tuple(
    tuple(zip(EVEN, image))
    for image in permutations(ODD)
    if frozenset(zip(EVEN, image)) != IDENTITY
)
PRISM_EDGES = frozenset(
    {
        (0, 2),
        (2, 4),
        (0, 4),
        (1, 3),
        (3, 5),
        (1, 5),
        (0, 3),
        (2, 5),
        (1, 4),
    }
)


class LinkageOracle:
    def __init__(self, graph):
        self.graph = graph

    @lru_cache(maxsize=None)
    def path_masks(self, a, b):
        return tuple(
            frozenset(path)
            for path in nx.all_simple_paths(self.graph, a, b)
        )

    @lru_cache(maxsize=None)
    def linked(self, normalized_pairs):
        pairs = tuple(normalized_pairs)

        def search(index, used):
            if index == len(pairs):
                return True
            a, b = pairs[index]
            for path in self.path_masks(a, b):
                if path.isdisjoint(used) and search(index + 1, used | path):
                    return True
            return False

        return search(0, frozenset())

    def has_linkage(self, pairs):
        normalized = tuple(sorted(tuple(sorted(pair)) for pair in pairs))
        return self.linked(normalized)


def rooted_prism_minor(graph, roots, extra):
    """Test all models in which the sole extra vertex is deleted or
    absorbed into one prescribed root bag."""

    def sees(label_a, label_b, absorbed):
        a, b = roots[label_a], roots[label_b]
        if graph.has_edge(a, b):
            return True
        if absorbed == label_a and graph.has_edge(extra, b):
            return True
        if absorbed == label_b and graph.has_edge(extra, a):
            return True
        return False

    for absorbed in (None, *range(6)):
        if absorbed is not None and not graph.has_edge(extra, roots[absorbed]):
            continue
        if all(sees(a, b, absorbed) for a, b in PRISM_EDGES):
            return True
    return False


def frame_signature(oracle, roots):
    def translate(pairs):
        return tuple((roots[a], roots[b]) for a, b in pairs)

    frames = tuple(
        oracle.has_linkage(
            translate(
                (
                    CYCLE_EDGES[(i - 2) % 6],
                    CYCLE_EDGES[(i + 2) % 6],
                )
            )
        )
        for i in range(6)
    )
    antipodal = tuple(
        oracle.has_linkage(
            translate((CYCLE_EDGES[i], CYCLE_EDGES[(i + 3) % 6]))
        )
        for i in range(3)
    )
    nonidentity = tuple(
        oracle.has_linkage(translate(matching))
        for matching in NONIDENTITY_MATCHINGS
    )
    return frames, antipodal, nonidentity


def main():
    labelled_survivors = set()
    nonprism_survivors = set()
    underlying_survivors = set()

    for graph_index, graph in enumerate(nx.graph_atlas_g()):
        if len(graph) != 7 or nx.node_connectivity(graph) < 3:
            continue
        oracle = LinkageOracle(graph)
        for extra in graph:
            root_vertices = tuple(v for v in graph if v != extra)
            for roots in permutations(root_vertices):
                frames, antipodal, nonidentity = frame_signature(oracle, roots)
                if sum(frames) < 4:
                    continue
                if any(antipodal) or any(nonidentity):
                    continue

                edge_code = tuple(
                    sorted(
                        tuple(
                            sorted(
                                (
                                    6 if u == extra else roots.index(u),
                                    6 if v == extra else roots.index(v),
                                )
                            )
                        )
                        for u, v in graph.edges
                    )
                )
                key = (edge_code, frames)
                labelled_survivors.add(key)
                underlying_survivors.add(graph_index)
                if not rooted_prism_minor(graph, roots, extra):
                    nonprism_survivors.add(key)

    print("underlying 3-connected atlas graphs:", len(underlying_survivors),
          sorted(underlying_survivors))
    print("labelled survivor types:", len(labelled_survivors))
    print("survivors without the prescribed rooted prism:", len(nonprism_survivors))
    for edge_code, frames in sorted(nonprism_survivors)[:20]:
        print("counterexample", frames, edge_code)

    assert not nonprism_survivors


if __name__ == "__main__":
    main()
