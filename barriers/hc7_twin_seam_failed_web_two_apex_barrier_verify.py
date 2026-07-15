#!/usr/bin/env python3
"""Verify the failed-web plus spanning-K6 two-apex guardrail."""

from __future__ import annotations

import itertools
from pathlib import Path
import sys


DEPS = Path(__file__).resolve().parents[1] / "active" / "runtime" / "deps"
if DEPS.exists():
    sys.path.insert(0, str(DEPS))

import networkx as nx


U = tuple(f"U{i}" for i in range(5))
L = tuple(f"L{i}" for i in range(5))
ICO = ("T", "B") + U + L


def build() -> nx.Graph:
    graph = nx.Graph()
    graph.add_nodes_from(("a", "b") + ICO)
    for index in range(5):
        graph.add_edge("T", U[index])
        graph.add_edge("B", L[index])
        graph.add_edge(U[index], U[(index + 1) % 5])
        graph.add_edge(L[index], L[(index + 1) % 5])
        graph.add_edge(U[index], L[index])
        graph.add_edge(U[index], L[(index - 1) % 5])
    graph.add_edge("a", "b")
    for apex in ("a", "b"):
        graph.add_edges_from((apex, vertex) for vertex in ICO)
    return graph


def paired_feasible(
    graph: nx.Graph, first: tuple[str, str], second: tuple[str, str]
) -> bool:
    """Exact two-fragment feasibility by connected-set enumeration."""

    fixed = frozenset(first)
    forbidden = frozenset(second)
    free = tuple(set(graph) - fixed - forbidden)
    for mask in range(1 << len(free)):
        carrier = set(fixed)
        carrier.update(
            free[index] for index in range(len(free)) if (mask >> index) & 1
        )
        if not nx.is_connected(graph.subgraph(carrier)):
            continue
        remainder = graph.copy()
        remainder.remove_nodes_from(carrier)
        if nx.has_path(remainder, *second):
            return True
    return False


def verify_model(graph: nx.Graph, bags: tuple[frozenset[str], ...]) -> None:
    assert set().union(*bags) == set(graph)
    assert sum(map(len, bags)) == graph.number_of_nodes()
    assert all(nx.is_connected(graph.subgraph(bag)) for bag in bags)
    assert all(
        any(graph.has_edge(x, y) for x in bags[left] for y in bags[right])
        for left, right in itertools.combinations(range(len(bags)), 2)
    )


def main() -> None:
    graph = build()
    base = graph.subgraph(ICO).copy()
    assert nx.check_planarity(base)[0]
    assert nx.node_connectivity(graph) == 7

    web = base.copy()
    web.remove_node("T")
    assert not paired_feasible(web, ("U0", "U3"), ("U1", "U4"))
    assert paired_feasible(web, ("U1", "U3"), ("U0", "U4"))

    common_host = graph.copy()
    common_host.remove_edges_from((("a", "T"), ("b", "B")))
    bags = (
        frozenset(("T", "U3", "U4")),
        frozenset(("L0", "L4")),
        frozenset(("U0", "U1", "U2")),
        frozenset(("L1", "L2")),
        frozenset(("a", "B", "L3")),
        frozenset(("b",)),
    )
    verify_model(common_host, bags)

    fixed_pair_remainder = graph.copy()
    fixed_pair_remainder.remove_nodes_from(("a", "b"))
    assert nx.check_planarity(fixed_pair_remainder)[0]

    print("GREEN failed_web_two_apex_guardrail")
    print("order=14 connectivity=7 K7_minor=false")
    print("rst_pairings=false,true spanning_K6_in_common_host=true")
    print("fixed_pair={a,b} planar_remainder=true")


if __name__ == "__main__":
    main()
