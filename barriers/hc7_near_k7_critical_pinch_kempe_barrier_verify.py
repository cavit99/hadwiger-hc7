#!/usr/bin/env python3
"""Verify the seven-connected critical-pinch Kempe barrier."""

from itertools import product

import networkx as nx


BASE_GRAPH6 = b"HCpvbqk"
CRITICAL_EDGE = (1, 5)
BASE_COLOURING = {
    0: 0,
    1: 0,
    5: 0,
    2: 1,
    3: 1,
    4: 1,
    6: 2,
    7: 2,
    8: 2,
}


def colourings(graph: nx.Graph, k: int):
    order = sorted(graph, key=lambda v: -graph.degree(v))
    colour = {}

    def rec(pos: int):
        if pos == len(order):
            yield dict(colour)
            return
        v = order[pos]
        forbidden = {colour[u] for u in graph[v] if u in colour}
        for value in range(k):
            if value not in forbidden:
                colour[v] = value
                yield from rec(pos + 1)
                del colour[v]

    yield from rec(0)


def is_proper(graph: nx.Graph, colouring: dict) -> bool:
    return all(colouring[u] != colouring[v] for u, v in graph.edges)


def is_vertex_critical(graph: nx.Graph, k: int) -> bool:
    if next(colourings(graph, k - 1), None) is not None:
        return False
    if next(colourings(graph, k), None) is None:
        return False
    for v in graph:
        reduced = graph.copy()
        reduced.remove_node(v)
        if next(colourings(reduced, k - 1), None) is None:
            return False
    return True


def pair_paths(graph: nx.Graph, colouring: dict, s: int, w: int, other: int):
    zero = colouring[s]
    allowed = [v for v in graph if colouring[v] in {zero, other}]
    return list(nx.all_simple_paths(graph.subgraph(allowed), s, w))


def has_disjoint_transversal(path_families) -> bool:
    for choice in product(*path_families):
        interiors = [set(path[1:-1]) for path in choice]
        if all(
            interiors[i].isdisjoint(interiors[j])
            for i in range(len(interiors))
            for j in range(i)
        ):
            return True
    return False


def join_with_triangle(base: nx.Graph):
    graph = base.copy()
    triangle = (9, 10, 11)
    graph.add_edges_from(((9, 10), (10, 11), (9, 11)))
    graph.add_edges_from((q, v) for q in triangle for v in base)
    return graph, triangle


def main() -> None:
    base = nx.from_graph6_bytes(BASE_GRAPH6)
    assert nx.node_connectivity(base) == 4
    assert is_vertex_critical(base, 4)

    deleted = base.copy()
    deleted.remove_edge(*CRITICAL_EDGE)
    assert is_proper(deleted, BASE_COLOURING)
    s, w = CRITICAL_EDGE
    assert BASE_COLOURING[s] == BASE_COLOURING[w] == 0

    base_families = [
        pair_paths(deleted, BASE_COLOURING, s, w, colour)
        for colour in (1, 2)
    ]
    assert base_families == [
        [[1, 4, 0, 3, 5]],
        [[1, 6, 0, 8, 5]],
    ]
    assert not has_disjoint_transversal(base_families)

    graph, triangle = join_with_triangle(base)
    assert nx.node_connectivity(graph) == 7
    assert is_vertex_critical(graph, 7)

    joined_deleted = graph.copy()
    joined_deleted.remove_edge(*CRITICAL_EDGE)
    joined_colouring = dict(BASE_COLOURING)
    joined_colouring.update({q: 3 + index for index, q in enumerate(triangle)})
    assert is_proper(joined_deleted, joined_colouring)

    families = [
        pair_paths(joined_deleted, joined_colouring, s, w, colour)
        for colour in range(1, 6)
    ]
    assert families[:2] == base_families
    assert families[2:] == [
        [[1, 9, 5]],
        [[1, 10, 5]],
        [[1, 11, 5]],
    ]
    assert not has_disjoint_transversal(families)

    # A literal K_4 model in the base, hence a K_7 model after the join.
    base_bags = ({0}, {3}, {6}, {1, 4, 5})
    assert all(nx.is_connected(base.subgraph(bag)) for bag in base_bags)
    assert all(
        any(base.has_edge(x, y) for x in base_bags[i] for y in base_bags[j])
        for i in range(4)
        for j in range(i)
    )

    print("GREEN: seven-connected seven-critical pinch barrier verified")


if __name__ == "__main__":
    main()
