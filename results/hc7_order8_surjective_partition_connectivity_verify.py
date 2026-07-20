#!/usr/bin/env python3
"""Verify surjective equality-partition connectivity at order eight."""

from __future__ import annotations

import collections
import itertools
import subprocess

import networkx as nx


def canonical_partitions(order: int, blocks: int) -> tuple[tuple[int, ...], ...]:
    answer: list[tuple[int, ...]] = []
    word = [0] * order

    def visit(index: int, maximum: int) -> None:
        if index == order:
            if maximum + 1 == blocks:
                answer.append(tuple(word))
            return
        for value in range(min(maximum + 1, blocks - 1) + 1):
            word[index] = value
            visit(index + 1, max(maximum, value))

    visit(1, 0)
    return tuple(answer)


FIVE_BLOCKS = canonical_partitions(8, 5)


def proper(graph: nx.Graph, partition: tuple[int, ...]) -> bool:
    return all(partition[x] != partition[y] for x, y in graph.edges())


def canonical(word: list[int]) -> tuple[int, ...]:
    names: dict[int, int] = {}
    return tuple(names.setdefault(value, len(names)) for value in word)


def partition_components(graph: nx.Graph) -> tuple[int, ...]:
    states = {partition for partition in FIVE_BLOCKS if proper(graph, partition)}
    adjacency = {partition: set() for partition in states}
    for partition in states:
        multiplicity = collections.Counter(partition)
        for vertex in range(8):
            if multiplicity[partition[vertex]] == 1:
                continue
            for target in range(5):
                if target == partition[vertex]:
                    continue
                changed = list(partition)
                changed[vertex] = target
                neighbour = canonical(changed)
                if neighbour in states:
                    adjacency[partition].add(neighbour)

    sizes: list[int] = []
    unseen = set(states)
    while unseen:
        stack = [unseen.pop()]
        size = 0
        while stack:
            current = stack.pop()
            size += 1
            for neighbour in adjacency[current]:
                if neighbour in unseen:
                    unseen.remove(neighbour)
                    stack.append(neighbour)
        sizes.append(size)
    return tuple(sorted(sizes))


def k_colourable(graph: nx.Graph, colours: int) -> bool:
    order = sorted(graph, key=graph.degree, reverse=True)
    assignment = [-1] * len(graph)

    def visit(index: int) -> bool:
        if index == len(order):
            return True
        vertex = order[index]
        forbidden = {assignment[x] for x in graph[vertex] if assignment[x] >= 0}
        for colour in range(colours):
            if colour not in forbidden:
                assignment[vertex] = colour
                if visit(index + 1):
                    return True
        assignment[vertex] = -1
        return False

    return visit(0)


def set_partitions(items: tuple[int, ...], block_count: int):
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
    for retained_order in range(5, len(vertices) + 1):
        for retained in itertools.combinations(vertices, retained_order):
            for branch_sets in set_partitions(retained, 5):
                if not all(nx.is_connected(graph.subgraph(part)) for part in branch_sets):
                    continue
                if all(
                    any(graph.has_edge(x, y) for x in branch_sets[i] for y in branch_sets[j])
                    for i in range(5)
                    for j in range(i + 1, 5)
                ):
                    return True
    return False


def main() -> None:
    stream = subprocess.run(
        ["geng", "-q", "8"], check=True, capture_output=True
    ).stdout.splitlines()
    assert len(stream) == 12346

    not_three_colourable = 0
    nonconnected = 0
    empty = 0
    counterexamples: list[str] = []
    first_positive_control = None

    for raw in stream:
        graph = nx.from_graph6_bytes(raw)
        if k_colourable(graph, 3):
            continue
        not_three_colourable += 1
        components = partition_components(graph)
        if len(components) == 1:
            continue
        nonconnected += 1
        if not components:
            empty += 1
        if first_positive_control is None:
            first_positive_control = (raw.decode(), components)
        if not has_k5_minor(graph):
            counterexamples.append(raw.decode())

    assert (not_three_colourable, nonconnected, empty) == (6322, 236, 89)
    assert counterexamples == []
    assert first_positive_control == ("G?aN~w", (27, 37))

    low_chromatic_control = nx.from_graph6_bytes(b"G??F~w")
    assert k_colourable(low_chromatic_control, 3)
    assert partition_components(low_chromatic_control) == (65, 90)

    print(
        "order8 graphs=12346 not_3_colourable=6322 "
        "nonconnected_five_block_partition_graph=236 empty=89"
    )
    print("positive_control G?aN~w components=27,37 has_K5_minor=yes")
    print("low_chromatic_control G??F~w components=65,90")
    print("PASS order8_K5_minor_free_chromatic_at_least_four_partition_graph_connected")


if __name__ == "__main__":
    main()
