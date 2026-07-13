#!/usr/bin/env python3
"""Counterexample to the rank-four SPQR leaf inference.

The graph is a 2-sum of two 3-connected wheel-like torsos along p,q.
The four singleton portal classes a,c,b,d occur in alternating order on
the facial cycle p-a-c-q-b-d-p.  Hence the prescribed a-b and c-d
linkage is absent.  Nevertheless the two interiors of the unique SPQR
edge contain respectively {a,c,u} and {b,d,v}; each has portal rank two.

Thus cofaciality in one embedding does not imply that reflecting an
SPQR leaf produces another embedding in which all four portals are
cofacial.  The block-reversal argument in the proposed C6 closure needs
an additional embedding-synchronisation theorem.
"""

from __future__ import annotations

import itertools

import networkx as nx


P, Q = "p", "q"
LEFT = frozenset(("a", "c", "u"))
RIGHT = frozenset(("b", "d", "v"))
PORTALS = ({"a"}, {"c"}, {"b"}, {"d"})


def graph() -> nx.Graph:
    answer = nx.Graph()
    answer.add_edges_from(
        (
            # Left torso: adding the virtual edge pq makes a wheel W_5.
            (P, "a"), ("a", "c"), ("c", Q),
            (P, "u"), ("u", Q), ("u", "a"), ("u", "c"),
            # Right torso, symmetrically.
            (P, "d"), ("d", "b"), ("b", Q),
            (P, "v"), ("v", Q), ("v", "d"), ("v", "b"),
        )
    )
    return answer


def has_disjoint_linkage(host: nx.Graph) -> bool:
    first = nx.all_simple_paths(host, "a", "b")
    second = tuple(nx.all_simple_paths(host, "c", "d"))
    return any(set(path).isdisjoint(other) for path in first for other in second)


def main() -> None:
    host = graph()

    assert nx.is_biconnected(host)
    assert nx.node_connectivity(host) == 2

    reduced = host.copy()
    reduced.remove_nodes_from((P, Q))
    assert {frozenset(component) for component in nx.connected_components(reduced)} == {
        LEFT, RIGHT
    }

    # Each side plus the virtual edge pq is a 3-connected R-torso.
    for interior in (LEFT, RIGHT):
        torso = host.subgraph(interior | {P, Q}).copy()
        torso.add_edge(P, Q)
        assert nx.node_connectivity(torso) == 3

    # This cycle can be chosen as the outer facial cycle: draw virtual pq
    # as a chord, put the two wheel hubs on its two sides, then delete pq.
    facial_cycle = (P, "a", "c", Q, "b", "d")
    assert all(
        host.has_edge(facial_cycle[index], facial_cycle[(index + 1) % 6])
        for index in range(6)
    )
    planar, embedding = nx.check_planarity(host)
    assert planar
    visited: set[tuple[str, str]] = set()
    faces = []
    for first, second in embedding.edges():
        if (first, second) not in visited:
            faces.append(tuple(embedding.traverse_face(first, second, visited)))

    def cyclically_equal(first: tuple[str, ...], second: tuple[str, ...]) -> bool:
        if len(first) != len(second):
            return False
        doubled = second + second
        reverse = tuple(reversed(second))
        doubled_reverse = reverse + reverse
        return any(
            first == doubled[index:index + len(first)]
            or first == doubled_reverse[index:index + len(first)]
            for index in range(len(first))
        )

    assert any(cyclically_equal(facial_cycle, face) for face in faces)

    # Alternating cofacial terminals forbid the prescribed linkage; the
    # exhaustive path check verifies the abstract graph statement too.
    assert not has_disjoint_linkage(host)

    # Singleton portal classes have a unique SDR.  Its intersection with
    # each SPQR-edge interior has size exactly two, so neither side has
    # transversal rank at most one.
    representatives = frozenset().union(*PORTALS)
    assert representatives & LEFT == {"a", "c"}
    assert representatives & RIGHT == {"b", "d"}

    # There are no shore-degree-two vertices, so a degree-two portal-lock
    # hypothesis is vacuous in this example.
    assert min(dict(host.degree()).values()) >= 3

    print("planar with required facial cycle", True)
    print("two-cut components", sorted(map(sorted, (LEFT, RIGHT))))
    print("augmented torso connectivities", (3, 3))
    print("prescribed disjoint linkage", has_disjoint_linkage(host))
    print("portal ranks across SPQR edge", (2, 2))


if __name__ == "__main__":
    main()
