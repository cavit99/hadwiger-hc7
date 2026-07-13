#!/usr/bin/env python3
"""Verify the double-saturation rooted-K5 barrier."""

from itertools import combinations

import networkx as nx


def adjacent(graph, left, right):
    return any(graph.has_edge(x, y) for x in left for y in right)


def partitions_into_five(vertices):
    """All five-block partitions of an arbitrary used subset."""
    vertices = tuple(vertices)
    for used_order in range(5, len(vertices) + 1):
        for used in combinations(vertices, used_order):
            labels = [0] * used_order

            def rec(position, maximum):
                if position == used_order:
                    if maximum == 4:
                        yield tuple(
                            {used[i] for i, label in enumerate(labels) if label == j}
                            for j in range(5)
                        )
                    return
                for label in range(min(maximum + 1, 4) + 1):
                    labels[position] = label
                    yield from rec(position + 1, max(maximum, label))

            yield from rec(1, 0)


def main():
    core = list(range(6))
    h = nx.complete_graph(core)
    h.remove_edge(0, 3)
    s_set = {0, 1, 2, 4, 5}
    t_set = {1, 2, 3, 4, 5}

    assert nx.is_isomorphic(h.subgraph(s_set), nx.complete_graph(5))
    assert nx.is_isomorphic(h.subgraph(t_set), nx.complete_graph(5))

    for bags in partitions_into_five(core):
        if not all(nx.is_connected(h.subgraph(bag)) for bag in bags):
            continue
        if not all(bag & s_set and bag & t_set for bag in bags):
            continue
        if all(adjacent(h, bags[i], bags[j]) for i in range(5) for j in range(i)):
            raise AssertionError(bags)

    q = h.copy()
    q.add_nodes_from(("s", "w"))
    q.add_edges_from(("s", x) for x in s_set)
    q.add_edges_from(("w", x) for x in t_set)
    q.add_edge("s", "w")

    # The displayed six-colouring has classes {0,w}, {3,s}, and the four
    # singleton classes 1,2,4,5.  The literal K6 on s,w,1,2,4,5 proves
    # optimality.
    colouring = {
        0: 0,
        "w": 0,
        3: 1,
        "s": 1,
        1: 2,
        2: 3,
        4: 4,
        5: 5,
    }
    assert all(colouring[x] != colouring[y] for x, y in q.edges())
    assert max(map(len, nx.find_cliques(q))) == 6

    # On eight vertices a K7 model has one two-vertex bag, or is a K7 subgraph.
    vertices = tuple(q)
    for x, y in q.edges():
        bags = ({x, y},) + tuple({v} for v in vertices if v not in {x, y})
        assert not all(
            adjacent(q, bags[i], bags[j])
            for i in range(7)
            for j in range(i)
        )

    print("GREEN: double saturation without a doubly rooted K5 verified")


if __name__ == "__main__":
    main()
