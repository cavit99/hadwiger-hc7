#!/usr/bin/env python3
"""Exact forced-hub test for the proposed two-safe-transit continuation."""

from __future__ import annotations

from functools import lru_cache
from itertools import combinations

import networkx as nx


CORE_VERTICES = tuple("abcdefg")
ALL_VERTICES = CORE_VERTICES + ("x", "h", "p", "q", "r", "s")
EXPECTED_SAFE = ("p",)


def pair(left: str, right: str) -> frozenset[str]:
    return frozenset((left, right))


def build_core() -> nx.Graph:
    """Build the thirteen-vertex exact two-bridge core C."""

    graph = nx.Graph()
    graph.add_nodes_from(ALL_VERTICES)
    graph.add_edges_from(
        (left, right)
        for left, right in combinations(CORE_VERTICES, 2)
        if pair(left, right) not in {pair("a", "b"), pair("c", "d")}
    )
    graph.add_edges_from(("x", vertex) for vertex in "abcd")
    for route in (
        ("f", "p", "a"),
        ("g", "q", "a"),
        ("f", "h", "g"),
        ("a", "r", "s", "c"),
    ):
        graph.remove_edge(route[0], route[-1])
        graph.add_edges_from(zip(route, route[1:]))
    graph.add_edges_from((("e", "h"), ("h", "x"), ("p", "r"), ("s", "q")))
    assert (len(graph), graph.number_of_edges()) == (13, 32)
    return graph


def contract_hub(graph: nx.Graph, hub: tuple[str, ...]) -> nx.Graph:
    """Contract a prescribed connected hub to its first listed vertex."""

    contracted = graph.copy()
    root = hub[0]
    for vertex in hub[1:]:
        contracted = nx.contracted_nodes(contracted, root, vertex, self_loops=False)
    return contracted


def spanning_k7_model(graph: nx.Graph) -> tuple[frozenset[str], ...] | None:
    """Enumerate canonical spanning partitions into seven clique-minor bags."""

    vertices = tuple(graph)
    index = {vertex: position for position, vertex in enumerate(vertices)}
    adjacency = [0] * len(vertices)
    for left, right in graph.edges():
        i, j = index[left], index[right]
        adjacency[i] |= 1 << j
        adjacency[j] |= 1 << i

    @lru_cache(maxsize=None)
    def connected(mask: int) -> bool:
        reached = mask & -mask
        while True:
            previous = reached
            pending = reached
            while pending:
                bit = pending & -pending
                pending ^= bit
                reached |= adjacency[bit.bit_length() - 1] & mask
            if reached == previous:
                return reached == mask

    blocks: list[list[int]] = []

    def search(position: int) -> tuple[frozenset[str], ...] | None:
        if position == len(vertices):
            if len(blocks) != 7:
                return None
            masks = tuple(sum(1 << item for item in block) for block in blocks)
            if not all(connected(mask) for mask in masks):
                return None
            for left, right in combinations(range(7), 2):
                neighbourhood = 0
                pending = masks[left]
                while pending:
                    bit = pending & -pending
                    pending ^= bit
                    neighbourhood |= adjacency[bit.bit_length() - 1]
                if not neighbourhood & masks[right]:
                    return None
            return tuple(
                frozenset(vertices[item] for item in block) for block in blocks
            )

        if len(blocks) + len(vertices) - position < 7:
            return None
        for block in blocks:
            block.append(position)
            answer = search(position + 1)
            block.pop()
            if answer is not None:
                return answer
        if len(blocks) < 7:
            blocks.append([position])
            answer = search(position + 1)
            blocks.pop()
            if answer is not None:
                return answer
        return None

    return search(0)


def validate_model(graph: nx.Graph, model: tuple[tuple[str, ...], ...]) -> None:
    """Directly validate a displayed spanning seven-bag certificate."""

    bags = tuple(frozenset(bag) for bag in model)
    assert len(bags) == 7
    assert sum(map(len, bags)) == len(graph)
    assert set().union(*bags) == set(graph)
    assert all(nx.is_connected(graph.subgraph(bag)) for bag in bags)
    assert all(
        any(graph.has_edge(u, v) for u in left for v in right)
        for left, right in combinations(bags, 2)
    )


def main() -> None:
    core = build_core()
    candidates = tuple(sorted(set(core) - {"q", "x"}))
    safe: list[str] = []

    for transit in candidates:
        augmented = core.copy()
        augmented.add_edges_from((
            ("q", transit),
            (transit, "x"),
            ("q", "e"),
        ))
        contracted = contract_hub(augmented, ("q", transit, "x"))
        if spanning_k7_model(contracted) is not None:
            safe.append(transit)

    assert tuple(safe) == EXPECTED_SAFE

    positive = core.copy()
    positive.add_edges_from((("q", "p"), ("p", "x"), ("q", "e")))
    validate_model(
        positive,
        (
            ("p", "q", "x"),
            ("a", "c", "r", "s"),
            ("b",),
            ("d",),
            ("e",),
            ("f", "h"),
            ("g",),
        ),
    )

    unsafe = tuple(candidate for candidate in candidates if candidate not in safe)
    print("GREEN atomic two-safe-transit-label barrier")
    print(f"candidates={','.join(candidates)}")
    print(f"forced_hub_safe={','.join(safe)}")
    print(f"forced_hub_unsafe={','.join(unsafe)}")
    print("explicit_positive_hub={p,q,x}")


if __name__ == "__main__":
    main()
