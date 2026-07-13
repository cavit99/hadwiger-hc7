#!/usr/bin/env python3
"""Probe the maximal quotient of the audited two-path normalization.

The five row vertices are C,U1,U2,U3,U4.  The A path is split into its
two endpoint shores.  Four rows are partitioned into the two endpoint
bundles of the B path; the fifth (mobile) row is made adjacent to both B
shores.  This is deliberately the edge-maximal bare crossed frame.
"""

from itertools import combinations

import networkx as nx


ROWS = range(4, 9)
C, U1, U2, U3, U4 = ROWS


def add_edge(adjacency: list[int], left: int, right: int) -> None:
    adjacency[left] |= 1 << right
    adjacency[right] |= 1 << left


def build(mobile: int, left_bundle: frozenset[int]) -> list[int]:
    # 0,1 are A-left,A-right; 2,3 are B-left,B-right.
    adjacency = [0] * 9
    for left, right in combinations(ROWS, 2):
        add_edge(adjacency, left, right)
    add_edge(adjacency, 0, 1)
    add_edge(adjacency, 2, 3)
    for row in (U1, U2):
        add_edge(adjacency, 0, row)
    for row in (U3, U4):
        add_edge(adjacency, 1, row)
    remaining = frozenset(ROWS) - {mobile}
    right_bundle = remaining - left_bundle
    for row in left_bundle | {mobile}:
        add_edge(adjacency, 2, row)
    for row in right_bundle | {mobile}:
        add_edge(adjacency, 3, row)
    return adjacency


def clique_minor_model(adjacency: list[int], target: int = 7):
    order = len(adjacency)
    neighbours = [0] * (1 << order)
    connected: list[int] = []
    for mask in range(1, 1 << order):
        bit = mask & -mask
        neighbours[mask] = neighbours[mask ^ bit] | adjacency[bit.bit_length() - 1]
        reached = bit
        while True:
            expanded = reached | (neighbours[reached] & mask)
            if expanded == reached:
                break
            reached = expanded
        if reached == mask:
            connected.append(mask)
    connected.sort(key=lambda mask: (mask.bit_count(), mask))

    def search(chosen: list[int], candidates: list[int], used: int):
        if len(chosen) == target:
            return tuple(chosen)
        needed = target - len(chosen)
        for position, bag in enumerate(candidates):
            if bag & used:
                continue
            following = [
                other
                for other in candidates[position + 1 :]
                if not other & (used | bag) and neighbours[bag] & other
            ]
            if len(following) >= needed - 1:
                answer = search(chosen + [bag], following, used | bag)
                if answer is not None:
                    return answer
        return None

    return search([], connected, 0)


def decode(model) -> list[list[str]] | None:
    names = ["A0", "A1", "B0", "B1", "C", "U1", "U2", "U3", "U4"]
    if model is None:
        return None
    return [[names[index] for index in range(9) if bag >> index & 1] for bag in model]


def canonical_rows(rows: frozenset[int]) -> str:
    names = {C: "C", U1: "U1", U2: "U2", U3: "U3", U4: "U4"}
    return "{" + ",".join(names[row] for row in sorted(rows)) + "}"


def two_apex_pairs(adjacency: list[int]) -> list[tuple[int, int]]:
    graph = nx.Graph()
    graph.add_nodes_from(range(len(adjacency)))
    graph.add_edges_from(
        (left, right)
        for left in range(len(adjacency))
        for right in range(left + 1, len(adjacency))
        if adjacency[left] >> right & 1
    )
    return [
        pair
        for pair in combinations(graph.nodes, 2)
        if nx.check_planarity(graph.subgraph(set(graph) - set(pair)))[0]
    ]


def main() -> None:
    seen = set()
    for mobile in ROWS:
        remaining = frozenset(ROWS) - {mobile}
        for pair in combinations(sorted(remaining), 2):
            left = frozenset(pair)
            right = remaining - left
            key = (mobile, min(tuple(sorted(left)), tuple(sorted(right))))
            if key in seen:
                continue
            seen.add(key)
            adjacency = build(mobile, left)
            model = clique_minor_model(adjacency)
            print(
                "mobile", canonical_rows(frozenset({mobile})),
                "bundles", canonical_rows(left), canonical_rows(right),
                "K7", decode(model),
                "2apex", two_apex_pairs(adjacency),
            )


if __name__ == "__main__":
    main()
