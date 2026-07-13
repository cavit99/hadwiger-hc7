#!/usr/bin/env python3
"""Probe endpoint-path repairs after a sacrificial neutral-row split.

The connected entry shore has already been merged with X to a vertex z;
r is the residual neutral shore.  The old B path is reduced to its two
endpoint roles b0,b1 and Q0..Q3 are C plus the other three neutral rows.
The sacrificed row W is represented only by its B-endpoint state and by
the z/r contacts to those endpoints.
"""

from itertools import combinations, product

import networkx as nx


ROWS = ("C", "Q1", "Q2", "Q3", "W")
RETAINED = ROWS[:-1]


def k7_certificate(graph: nx.Graph):
    """Exact for this eight-vertex quotient: one deletion or contraction."""
    for vertex in graph:
        reduced = graph.copy()
        reduced.remove_node(vertex)
        if reduced.number_of_edges() == 21:
            return "delete", vertex
    for left, right in graph.edges():
        contracted = nx.contracted_nodes(graph, left, right, self_loops=False)
        if contracted.number_of_nodes() == 7 and contracted.number_of_edges() == 21:
            return "contract", (left, right)
    return None


def build(state: tuple[str, ...], r_missing: frozenset[str], zr_b: str) -> nx.Graph:
    graph = nx.Graph()
    graph.add_nodes_from(("z", "r", "b0", "b1", *RETAINED))
    graph.add_edges_from(combinations(RETAINED, 2))
    graph.add_edge("z", "r")
    graph.add_edges_from(("z", row) for row in RETAINED)
    graph.add_edges_from(("r", row) for row in RETAINED if row not in r_missing)
    graph.add_edge("b0", "b1")
    for row, side in zip(ROWS, state, strict=True):
        if row != "W":
            if side in {"L", "M"}:
                graph.add_edge("b0", row)
            if side in {"R", "M"}:
                graph.add_edge("b1", row)
    # Entry shore z must see B.  The letters list which B endpoints also
    # receive a literal contact from z or r through the sacrificed row.
    for endpoint, marker in (("b0", "0"), ("b1", "1")):
        if f"z{marker}" in zr_b:
            graph.add_edge("z", endpoint)
        if f"r{marker}" in zr_b:
            graph.add_edge("r", endpoint)
    return graph


def compatible_patterns(w_state: str) -> tuple[str, ...]:
    allowed = ("0",) if w_state == "L" else ("1",) if w_state == "R" else ("0", "1")
    patterns = []
    # z needs at least one W-B contact.  r may see B or miss it.
    for zset_size in range(1, len(allowed) + 1):
        for zset in combinations(allowed, zset_size):
            for rset_size in range(len(allowed) + 1):
                for rset in combinations(allowed, rset_size):
                    patterns.append("".join(f"z{x}" for x in zset) + "".join(f"r{x}" for x in rset))
    return tuple(patterns)


def main() -> None:
    counts: dict[tuple[int, bool], list[tuple]] = {}
    for state in product("LRM", repeat=5):
        if state.count("L") < 2 or state.count("R") < 2 or state.count("M") > 1:
            continue
        for missing_size in range(3):
            for missing in combinations(RETAINED, missing_size):
                for pattern in compatible_patterns(state[-1]):
                    graph = build(state, frozenset(missing), pattern)
                    cert = k7_certificate(graph)
                    key = (missing_size, cert is not None)
                    counts.setdefault(key, []).append(("".join(state), missing, pattern, cert))
    for key in sorted(counts):
        print(key, len(counts[key]))
    print("survivors with full residual")
    for row in counts.get((0, False), ())[:40]:
        print(row)
    print("K7 with one missing residual row")
    for row in counts.get((1, True), ())[:40]:
        print(row)


if __name__ == "__main__":
    main()
