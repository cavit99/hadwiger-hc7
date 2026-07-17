#!/usr/bin/env python3
"""Verify the HEhutxm witnesses in the one-step minor-dynamics draft.

Requires NetworkX 3.x.  This script checks only the finite sharpness
example in Section 6; the uniform theorems have written proofs.
"""

from __future__ import annotations

import networkx as nx


R_GRAPH6 = b"HEhutxm"
S_POLE = frozenset({0, 3, 5, 7})
T_POLE = frozenset({0, 4, 6, 8})
Z = 9
U = 10
S0 = frozenset(range(9))
T0 = frozenset({0, 3, 4, 5, 6, 7, 8, 9, 10})


def build_q() -> nx.Graph:
    r = nx.from_graph6_bytes(R_GRAPH6)
    q = r.copy()
    q.add_edges_from((Z, v) for v in S_POLE)
    q.add_edges_from((U, v) for v in T_POLE)
    q.add_edge(Z, U)
    return q


def proper(g: nx.Graph, colouring: dict[int, int]) -> bool:
    return set(g) == set(colouring) and all(
        colouring[v] != colouring[w] for v, w in g.edges()
    )


def colourable(g: nx.Graph, k: int) -> bool:
    order = sorted(g, key=lambda v: (-g.degree(v), v))
    colour: dict[int, int] = {}

    def search(i: int) -> bool:
        if i == len(order):
            return True
        v = order[i]
        forbidden = {colour[w] for w in g[v] if w in colour}
        for c in range(k):
            if c not in forbidden:
                colour[v] = c
                if search(i + 1):
                    return True
                del colour[v]
        return False

    return search(0)


def proper_colourings(g: nx.Graph, k: int):
    order = sorted(g, key=lambda v: (-g.degree(v), v))
    colour: dict[int, int] = {}

    def search(i: int):
        if i == len(order):
            yield dict(colour)
            return
        v = order[i]
        forbidden = {colour[w] for w in g[v] if w in colour}
        for c in range(k):
            if c not in forbidden:
                colour[v] = c
                yield from search(i + 1)
                del colour[v]

    yield from search(0)


def missing(colouring: dict[int, int], roots: set[int] | frozenset[int]):
    return set(range(5)) - {colouring[v] for v in roots}


def main() -> None:
    q = build_q()

    # Both original root sets are five-colour-saturating.  The second one
    # is itself five-chromatic; the first is the four-chromatic core, so its
    # saturation is checked over every five-colouring of Q.
    assert not colourable(q.subgraph(T0).copy(), 4)
    assert colourable(q, 5)
    count = 0
    for colouring in proper_colourings(q, 5):
        count += 1
        assert missing(colouring, S0) == set()
        assert missing(colouring, T0) == set()
    assert count == 6840

    deleted_edge = q.copy()
    deleted_edge.remove_edge(0, 3)
    c_de = {
        0: 2, 1: 3, 2: 3, 3: 2, 4: 0, 5: 0,
        6: 1, 7: 1, 8: 2, 9: 3, 10: 4,
    }
    assert proper(deleted_edge, c_de)
    assert missing(c_de, S0) == {4}
    assert missing(c_de, T0) == set()
    assert c_de[0] == c_de[3]

    deleted_vertex = q.copy()
    deleted_vertex.remove_node(0)
    c_dv = {
        1: 3, 2: 3, 3: 1, 4: 0, 5: 0,
        6: 2, 7: 2, 8: 1, 9: 3, 10: 4,
    }
    assert proper(deleted_vertex, c_dv)
    assert missing(c_dv, S0 - {0}) == {4}
    assert missing(c_dv, T0 - {0}) == set()
    assert {c_dv[v] for v in q.neighbors(0)} == set(range(5))

    contracted = nx.contracted_nodes(q, 0, 3, self_loops=False)
    c_ec = {
        0: 0, 1: 3, 2: 3, 4: 1, 5: 1,
        6: 2, 7: 2, 8: 0, 9: 4, 10: 3,
    }
    assert proper(contracted, c_ec)
    image_s0 = S0 - {3}
    image_t0 = T0 - {3}
    assert missing(c_ec, image_s0) == {4}
    assert missing(c_ec, image_t0) == set()
    list_0 = set(range(5)) - {
        c_ec[v] for v in q.neighbors(0) if v != 3
    }
    list_3 = set(range(5)) - {
        c_ec[v] for v in q.neighbors(3) if v != 0
    }
    assert list_0 == list_3 == {0}

    print("PASS HEhutxm full-root saturation")
    print("PASS vertex deletion, edge deletion and edge contraction witnesses")


if __name__ == "__main__":
    main()
