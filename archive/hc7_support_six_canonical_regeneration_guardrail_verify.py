#!/usr/bin/env python3
"""Verify the concrete canonical-regeneration joined-planar guardrail."""

from __future__ import annotations

import sys

sys.path.insert(0, "active")
from hc7_global_contraction_pullback_probe import (  # noqa: E402
    add_two_apices,
    dual_truncated_icosahedron,
)

import networkx as nx  # noqa: E402


def main() -> None:
    base = dual_truncated_icosahedron()
    u = 1
    triangle = {0, 12, 13}
    apex_a, apex_b = 32, 33

    assert nx.node_connectivity(base) == 5
    base_minus_u = base.copy()
    base_minus_u.remove_node(u)
    assert nx.node_connectivity(base_minus_u) == 5
    assert all(base.has_edge(x, y) for x in triangle for y in triangle if x < y)
    assert not base.has_edge(u, 0)

    graph = add_two_apices(base, adjacent=False)
    assert nx.node_connectivity(graph) == 7

    core = triangle | {apex_a}
    assert all(graph.has_edge(x, y) for x in core for y in core if x < y)
    assert graph.has_edge(u, apex_b)
    assert all(
        graph.has_edge(q, u) or graph.has_edge(q, apex_b) for q in core
    )
    assert {q for q in core if not graph.has_edge(u, q)} == {0}
    assert {q for q in core if not graph.has_edge(apex_b, q)} == {apex_a}

    quotient = nx.Graph(nx.contracted_nodes(graph, u, apex_b, self_loops=False))
    z = u
    assert nx.node_connectivity(quotient) == 7
    assert all(quotient.has_edge(z, v) for v in quotient if v != z)
    assert all(quotient.has_edge(apex_a, v) for v in quotient if v != apex_a)

    remainder_vertices = set(base) - triangle - {u}
    remainder = quotient.subgraph(remainder_vertices)
    assert nx.is_connected(remainder)
    quotient_clique = triangle | {apex_a, z}
    assert all(
        quotient.has_edge(x, y)
        for x in quotient_clique
        for y in quotient_clique
        if x < y
    )
    assert all(
        any(quotient.has_edge(q, v) for v in remainder)
        for q in quotient_clique
    )

    assert nx.check_planarity(graph.subgraph(set(graph) - {apex_a, apex_b}))[0]
    assert nx.check_planarity(
        quotient.subgraph(set(quotient) - {apex_a, z})
    )[0]

    literal_k5s = [
        clique
        for clique in nx.enumerate_all_cliques(graph)
        if len(clique) == 5
    ]
    assert not literal_k5s

    print("GREEN: canonical quotient-regeneration guardrail verified")
    print("base connectivity", nx.node_connectivity(base))
    print("base-u connectivity", nx.node_connectivity(base_minus_u))
    print("G connectivity", nx.node_connectivity(graph))
    print("G/ub connectivity", nx.node_connectivity(quotient))
    print("deficiencies", {u: [0], apex_b: [apex_a]})


if __name__ == "__main__":
    main()
