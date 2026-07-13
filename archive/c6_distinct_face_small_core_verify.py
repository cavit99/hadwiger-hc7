#!/usr/bin/env python3
"""Finite base for the three-distinct-face C6 prism-web outcome.

Enumerate 3-connected planar shores of order 4, 5, and 6 from the graph
atlas, ordered triples of distinct faces, and all nonempty portal subsets
allowed by the three face intersections.  Retain a state only if it has
at least four same-parity frames, none of the three antipodal two-
linkages, and none of the five nonidentity even-to-odd three-linkages.
"""

from __future__ import annotations

from functools import lru_cache
from itertools import permutations, product

import networkx as nx


CYCLE_EDGES = tuple((i, (i + 1) % 6) for i in range(6))
EVEN = (0, 2, 4)
ODD = (1, 3, 5)
IDENTITY = ((0, 3), (2, 5), (4, 1))
NONIDENTITY = tuple(
    tuple(zip(EVEN, image))
    for image in permutations(ODD)
    if tuple(zip(EVEN, image)) != IDENTITY
)


def facial_cycles(graph):
    planar, embedding = nx.check_planarity(graph)
    assert planar
    seen = set()
    answer = []
    for u, v in embedding.edges():
        if (u, v) in seen:
            continue
        face = tuple(embedding.traverse_face(u, v, seen))
        answer.append(face)
    return tuple(answer)


def nonempty_subsets(values):
    values = tuple(values)
    return tuple(
        frozenset(values[i] for i in range(len(values)) if mask >> i & 1)
        for mask in range(1, 1 << len(values))
    )


class PortalLinkages:
    def __init__(self, graph, portals, connected_sets):
        self.graph = graph
        self.portals = portals
        self.vertices = frozenset(graph)
        self.connected_sets = connected_sets

    @lru_cache(maxsize=None)
    def path_masks(self, a, b):
        # At these orders it is much faster to enumerate connected vertex
        # sets than to enumerate all simple paths repeatedly.  Every path
        # yields such a set, and every connected set meeting both portal
        # classes contains a path with a subset of that set; disjointness
        # is therefore preserved in both directions.
        return tuple(
            subset for subset in self.connected_sets
            if subset & self.portals[a] and subset & self.portals[b]
        )

    def linked(self, pairs):
        pairs = tuple(pairs)

        def search(index, used):
            if index == len(pairs):
                return True
            a, b = pairs[index]
            for path in self.path_masks(a, b):
                if path.isdisjoint(used) and search(index + 1, used | path):
                    return True
            return False

        return search(0, frozenset())

    def signature(self):
        frames = tuple(
            self.linked((CYCLE_EDGES[(i - 2) % 6],
                         CYCLE_EDGES[(i + 2) % 6]))
            for i in range(6)
        )
        antipodal = tuple(
            self.linked((CYCLE_EDGES[i], CYCLE_EDGES[i + 3]))
            for i in range(3)
        )
        nonidentity = tuple(self.linked(matching) for matching in NONIDENTITY)
        return frames, antipodal, nonidentity


def main():
    counts = {4: 0, 5: 0, 6: 0}
    examples = []
    for graph_index, graph in enumerate(nx.graph_atlas_g()):
        n = len(graph)
        if n not in counts or nx.node_connectivity(graph) < 3:
            continue
        planar, _ = nx.check_planarity(graph)
        if not planar:
            continue
        vertices = tuple(graph)
        connected_sets = tuple(
            subset
            for mask in range(1, 1 << n)
            for subset in (
                frozenset(vertices[i] for i in range(n) if mask >> i & 1),
            )
            if nx.is_connected(graph.subgraph(subset))
        )
        signature_cache = {}
        faces = facial_cycles(graph)
        for f0, f1, f2 in permutations(faces, 3):
            intersections = (
                frozenset(f2) & frozenset(f0),  # labels 0,3
                frozenset(f0) & frozenset(f1),  # labels 1,4
                frozenset(f1) & frozenset(f2),  # labels 2,5
            )
            if any(not x or len(x) > 2 for x in intersections):
                continue
            choices = [nonempty_subsets(x) for x in intersections]
            # Labels are grouped as (0,3), (1,4), (2,5).
            for p0, p3, p1, p4, p2, p5 in product(
                    choices[0], choices[0],
                    choices[1], choices[1],
                    choices[2], choices[2]):
                portals = (p0, p1, p2, p3, p4, p5)
                if portals not in signature_cache:
                    oracle = PortalLinkages(graph, portals, connected_sets)
                    signature_cache[portals] = oracle.signature()
                frames, antipodal, nonidentity = signature_cache[portals]
                if sum(frames) < 4 or any(antipodal) or any(nonidentity):
                    continue
                counts[n] += 1
                if len(examples) < 20:
                    examples.append((graph_index, portals, frames))

    print("surviving labelled states by shore order", counts)
    for example in examples:
        print("example", example)
    # Linkage plus face incidence alone has small abstract survivors.
    # This is a falsification probe, not a closure certificate.
    assert counts[4] > 0 and counts[5] > 0


if __name__ == "__main__":
    main()
