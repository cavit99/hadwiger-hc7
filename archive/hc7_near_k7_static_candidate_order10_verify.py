#!/usr/bin/env python3
"""Exact certificate: every 7-connected graph through order 10 has K7.

The complement has maximum degree at most n-8, hence at most two.  Such
graphs are exactly disjoint unions of paths and cycles.  We generate their
component multisets and find/recheck an explicit seven-bag minor model.
"""

from __future__ import annotations

import hashlib

import networkx as nx


Component = tuple[str, int]


def component_types(max_order: int) -> list[Component]:
    return [*(('P', n) for n in range(1, max_order + 1)),
            *(('C', n) for n in range(3, max_order + 1))]


def component_multisets(
    order: int, types: list[Component], start: int = 0
):
    if order == 0:
        yield ()
        return
    for index in range(start, len(types)):
        kind, size = types[index]
        if size > order:
            continue
        for rest in component_multisets(order - size, types, index):
            yield ((kind, size), *rest)


def graph_from_components(components: tuple[Component, ...]) -> nx.Graph:
    graph = nx.Graph()
    offset = 0
    for kind, size in components:
        graph.add_nodes_from(range(offset, offset + size))
        if kind == 'P':
            graph.add_edges_from((offset + i, offset + i + 1)
                                 for i in range(size - 1))
        else:
            graph.add_edges_from((offset + i, offset + (i + 1) % size)
                                 for i in range(size))
        offset += size
    return graph


def k7_model(graph: nx.Graph) -> list[list[int]] | None:
    vertices = list(graph)
    n = len(vertices)
    members: dict[int, list[int]] = {}
    candidates: list[int] = []

    for mask in range(1, 1 << n):
        # Six other nonempty bags leave at most n-6 vertices here.
        if mask.bit_count() > n - 6:
            continue
        subset = [vertices[i] for i in range(n) if mask >> i & 1]
        if nx.is_connected(graph.subgraph(subset)):
            candidates.append(mask)
            members[mask] = subset

    def compatible(left: int, right: int) -> bool:
        return not left & right and any(
            graph.has_edge(x, y)
            for x in members[left]
            for y in members[right]
        )

    # Put small candidates at the pop end; this is only a speed ordering.
    candidates.sort(key=lambda mask: -mask.bit_count())

    def search(chosen: list[int], available: list[int]):
        if len(chosen) == 7:
            return chosen
        while len(chosen) + len(available) >= 7:
            candidate = available.pop()
            result = search(
                [*chosen, candidate],
                [other for other in available
                 if compatible(candidate, other)],
            )
            if result is not None:
                return result
        return None

    masks = search([], candidates)
    return None if masks is None else [members[mask] for mask in masks]


def verify_model(graph: nx.Graph, bags: list[list[int]]) -> None:
    assert len(bags) == 7
    assert all(bag and nx.is_connected(graph.subgraph(bag)) for bag in bags)
    assert sum(map(len, bags)) == len(set().union(*(map(set, bags))))
    for i in range(7):
        for j in range(i + 1, 7):
            assert any(graph.has_edge(x, y) for x in bags[i] for y in bags[j])


def main() -> None:
    digest = hashlib.sha256()
    summary = []
    for n in (8, 9, 10):
        degree_bound = n - 8
        generated = surviving = 0
        for components in component_multisets(n, component_types(n)):
            complement = graph_from_components(components)
            if max(dict(complement.degree()).values(), default=0) > degree_bound:
                continue
            generated += 1
            graph = nx.complement(complement)
            if nx.node_connectivity(graph) < 7:
                continue
            surviving += 1
            bags = k7_model(graph)
            assert bags is not None, (n, components, sorted(graph.edges()))
            verify_model(graph, bags)
            digest.update(repr((n, components, bags)).encode())
        summary.append((n, generated, surviving))

    assert summary == [(8, 1, 1), (9, 5, 5), (10, 106, 87)]
    print('GREEN', summary)
    print('certificate_sha256', digest.hexdigest())


if __name__ == '__main__':
    main()
