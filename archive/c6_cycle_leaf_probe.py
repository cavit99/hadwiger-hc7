#!/usr/bin/env python3
"""Exact certificate for the only possible cycle leaf of a C6 shore.

The cyclic labels used by the contact atlas are the original boundary
labels with missing cycle 0-4-2-3-1-5-0.  Normalize the unique portal
label to v=0.  Then a one-vertex leaf has contact mask 79 and the rest
of the shore has mask 126.

A genuine S-node leaf with two or more internal vertices is excluded
before this enumeration.  At an end internal vertex x, its two shore
neighbours are nonadjacent along the chordless S-torso path.  Both miss
the unique boundary label v_x, so those two neighbours together with
v_x form an independent triple in N_G(x), contrary to Dirac's
alpha(N_G(x)) <= 2 bound.  Thus only the one-vertex ear remains.
"""

from __future__ import annotations

import itertools

import networkx as nx

from c6_portal_tetrahedron_verify import has_k7_minor
from c6_twocut_support_probe import negative_pairs


FULL = 127
MISSING = {
    tuple(sorted(edge))
    for edge in ((0, 4), (4, 2), (2, 3), (3, 1), (1, 5), (5, 0))
}
BOUNDARY_EDGES = set(itertools.combinations(range(7), 2)) - MISSING


def alpha_at_most_two(mask_p: int, mask_q: int) -> bool:
    # The degree-seven leaf x sees boundary row 79 and p,q.  Dirac's
    # equality bound requires alpha(N(x)) <= 2; pq is forced present.
    vertices = [vertex for vertex in range(7) if 79 >> vertex & 1] + [7, 8]

    def adjacent(first: int, second: int) -> bool:
        if first >= 7 and second >= 7:
            return True
        if first >= 7:
            first, second = second, first
        if second == 7:
            return bool(mask_p >> first & 1)
        if second == 8:
            return bool(mask_q >> first & 1)
        return tuple(sorted((first, second))) not in MISSING

    return not any(
        all(not adjacent(a, b) for a, b in itertools.combinations(triple, 2))
        for triple in itertools.combinations(vertices, 3)
    )


def one_vertex_states():
    negative = negative_pairs()
    answer = []
    leaf = 79
    for body in range(128):
        if body.bit_count() < 5:
            continue
        for p in range(128):
            for q in range(128):
                if body | p | q != 126 or not alpha_at_most_two(p, q):
                    continue
                tests = (
                    (leaf, body | p | q),
                    (leaf | p, body | q),
                    (leaf | q, body | p),
                    (leaf | p | q, body),
                    (p, leaf | body | q),
                    (q, leaf | body | p),
                )
                if all(test in negative for test in tests):
                    answer.append((body, p, q))
    return answer


def quotient_one_vertex(body_mask: int, p_mask: int, q_mask: int) -> nx.Graph:
    graph = nx.Graph()
    graph.add_nodes_from(range(12))
    graph.add_edges_from(BOUNDARY_EDGES)
    x, body, p, q, helper = 7, 8, 9, 10, 11
    graph.add_edges_from(((x, p), (x, q), (body, p), (body, q), (p, q)))
    graph.add_edges_from((helper, s) for s in range(7))
    for vertex, mask in ((x, 79), (body, body_mask), (p, p_mask), (q, q_mask)):
        graph.add_edges_from((vertex, s) for s in range(7) if mask >> s & 1)
    return graph


def main() -> None:
    states = one_vertex_states()
    maximal = [
        state for state in states
        if not any(
            state != other
            and all(state[i] | other[i] == other[i] for i in range(3))
            for other in states
        )
    ]
    assert len(states) == 64
    assert set(maximal) == {
        (126, 70, 70), (126, 70, 72),
        (126, 72, 70), (126, 72, 72),
    }
    print("one-vertex alpha/atlas states", len(states))
    print("maximal states", maximal)

    # First test the four maxima of the split/Dirac state system.
    results = {}
    for body, p, q in maximal:
        model, checked = has_k7_minor(quotient_one_vertex(body, p, q))
        results[(body, p, q)] = model
        print("one-vertex", (body, p, q), "model", model, "checked", checked)
        if (p, q) == (70, 70):
            assert model is not None
        else:
            assert model is None

    # The positive broad/broad maximum has five immediate maximal
    # descendants in the retained state poset.  Three remain positive;
    # the two obtained by deleting the z-contact at exactly one cut
    # vertex are negative.  Every further broad/broad state is below one
    # of these five, so together with the three broad/thin maxima this is
    # the complete maximal negative frontier.
    broad_descendants = (
        (62, 70, 70), (122, 70, 70), (124, 70, 70),
        (126, 6, 70), (126, 70, 6),
    )
    broad_negative = set()
    for state in broad_descendants:
        model, checked = has_k7_minor(quotient_one_vertex(*state))
        results[state] = model
        print("broad descendant", state, "model", model, "checked", checked)
        if model is None:
            broad_negative.add(state)
    assert broad_negative == {(126, 6, 70), (126, 70, 6)}

    maximal_negative = {
        (126, 6, 70), (126, 70, 6),
        (126, 70, 72), (126, 72, 70), (126, 72, 72),
    }
    broad_positive = {
        (126, 70, 70),
        (62, 70, 70), (122, 70, 70), (124, 70, 70),
    }
    assert all(
        any(all(state[i] | top[i] == top[i] for i in range(3))
            for top in maximal_negative)
        or state in broad_positive
        for state in states
    )
    assert all(results[state] is not None for state in broad_positive)
    print("maximal quotient-negative states", sorted(maximal_negative))

if __name__ == "__main__":
    main()
