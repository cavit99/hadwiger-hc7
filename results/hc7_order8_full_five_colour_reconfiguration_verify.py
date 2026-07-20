#!/usr/bin/env python3
"""Verify full single-vertex 5-colour connectivity through order eight."""

from __future__ import annotations

import itertools
import subprocess
from collections import Counter, deque

import networkx as nx


def connected(graph: nx.Graph, vertices: frozenset[int]) -> bool:
    return bool(vertices) and nx.is_connected(graph.subgraph(vertices))


def partitions(items: tuple[int, ...], block_count: int):
    blocks: list[list[int]] = []

    def visit(index: int):
        if index == len(items):
            if len(blocks) == block_count:
                yield tuple(frozenset(block) for block in blocks)
            return
        item = items[index]
        for block in blocks:
            block.append(item)
            yield from visit(index + 1)
            block.pop()
        if len(blocks) < block_count:
            blocks.append([item])
            yield from visit(index + 1)
            blocks.pop()

    yield from visit(0)


def has_k5_minor(graph: nx.Graph) -> bool:
    vertices = tuple(graph)
    for retained_count in range(5, len(vertices) + 1):
        for retained in itertools.combinations(vertices, retained_count):
            for branch_sets in partitions(retained, 5):
                if not all(connected(graph, part) for part in branch_sets):
                    continue
                if all(
                    any(graph.has_edge(x, y) for x in branch_sets[i] for y in branch_sets[j])
                    for i in range(5)
                    for j in range(i + 1, 5)
                ):
                    return True
    return False


def proper_colourings(graph: nx.Graph) -> set[tuple[int, ...]]:
    order = sorted(graph, key=graph.degree, reverse=True)
    colour = [-1] * len(graph)
    answer: set[tuple[int, ...]] = set()

    def visit(position: int) -> None:
        if position == len(order):
            answer.add(tuple(colour))
            return
        vertex = order[position]
        forbidden = {colour[x] for x in graph[vertex] if colour[x] >= 0}
        for candidate in range(5):
            if candidate not in forbidden:
                colour[vertex] = candidate
                visit(position + 1)
        colour[vertex] = -1

    visit(0)
    return answer


def component_sizes(graph: nx.Graph, *, surjective: bool = False) -> tuple[int, ...]:
    states = proper_colourings(graph)
    if surjective:
        states = {state for state in states if len(set(state)) == 5}
    unseen = set(states)
    sizes: list[int] = []
    while unseen:
        root = unseen.pop()
        queue = deque([root])
        size = 0
        while queue:
            current = queue.popleft()
            size += 1
            for vertex in graph:
                forbidden = {current[x] for x in graph[vertex]}
                for candidate in range(5):
                    if candidate == current[vertex] or candidate in forbidden:
                        continue
                    changed = list(current)
                    changed[vertex] = candidate
                    neighbour = tuple(changed)
                    if neighbour in unseen:
                        unseen.remove(neighbour)
                        queue.append(neighbour)
        sizes.append(size)
    return tuple(sorted(sizes))


def degeneracy(graph: nx.Graph) -> int:
    work = graph.copy()
    value = 0
    while work:
        vertex = min(work, key=work.degree)
        value = max(value, work.degree(vertex))
        work.remove_node(vertex)
    return value


def main() -> None:
    expected = {
        5: [],
        6: [("E]~o", 12, (780,), Counter({1: 360}))],
        7: [("FUZ~o", 15, (1800,), Counter({15: 40, 20: 30}))],
        8: [
            ("GEhf~w", 18, (4980,), Counter({1: 120, 54: 20, 480: 5})),
            ("GQyurg", 16, (6120,), Counter({5280: 1})),
            ("GQyurw", 17, (4440,), Counter({3960: 1})),
            ("GQyuzw", 18, (3480,), Counter({1560: 2})),
        ],
    }
    for order in range(5, 9):
        stream = subprocess.run(
            ["geng", "-q", "-d4", str(order)], check=True, capture_output=True
        ).stdout.splitlines()
        survivors = []
        for raw in stream:
            graph = nx.from_graph6_bytes(raw)
            if has_k5_minor(graph):
                continue
            full_sizes = component_sizes(graph)
            surjective_sizes = component_sizes(graph, surjective=True)
            survivors.append(
                (
                    raw.decode(),
                    graph.number_of_edges(),
                    full_sizes,
                    surjective_sizes,
                )
            )
        print(
            f"order={order} candidates={len(stream)} "
            f"k5_minor_free_min_degree4={len(survivors)}"
        )
        observed = [
            (code, edges, full_sizes, Counter(surjective_sizes))
            for code, edges, full_sizes, surjective_sizes in survivors
        ]
        assert observed == expected[order]
        for survivor in survivors:
            code, edges, full_sizes, surjective_sizes = survivor
            print(
                code,
                f"edges={edges}",
                f"full={Counter(full_sizes)}",
                f"surjective={Counter(surjective_sizes)}",
            )

    static_expected = {
        "G??F~w": ((35060,), Counter({540: 20, 1560: 5})),
        "G?`F~w": ((18000,), Counter({276: 20, 1104: 5})),
    }
    for code, wanted in static_expected.items():
        graph = nx.from_graph6_bytes(code.encode())
        full_sizes = component_sizes(graph)
        surjective_sizes = component_sizes(graph, surjective=True)
        assert (full_sizes, Counter(surjective_sizes)) == wanted
        print(
            code,
            f"full={Counter(full_sizes)}",
            f"surjective={Counter(surjective_sizes)}",
        )
    print("PASS full_R5_connected_for_every_K5_minor_free_graph_of_order_at_most_8")


if __name__ == "__main__":
    main()
