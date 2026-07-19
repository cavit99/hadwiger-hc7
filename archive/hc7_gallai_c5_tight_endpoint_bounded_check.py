#!/usr/bin/env python3
"""Exhaust a normalized C5 Gallai-tree endpoint family.

This is a bounded mechanism check, not a proof of an unbounded theorem and
not a search for a counterexample to Hadwiger's conjecture.  It tests the
family stated in the adjacent Markdown note.
"""

from __future__ import annotations

import functools
import itertools
import sys
from collections.abc import Iterable

sys.path.insert(0, "active/runtime/deps")

import networkx as nx


S = tuple(range(7))
R = tuple(range(5))
FULL_S = (1 << 7) - 1

# The boundary cycle s0 ... s6 s0 has this proper four-colouring.
S_COLOUR = (0, 1, 0, 2, 1, 3, 2)

# The simultaneous-contraction colouring on r0 ... r4.  The only conflicts
# with boundary edges are s0-r0 and s1-r2, which are the two deleted edges.
R_COLOUR = (0, 4, 1, 5, 4)
MARKED = {0: 0, 2: 1}  # r_i -> its unique same-colour boundary neighbour


def attachment_options(index: int) -> tuple[int, ...]:
    """Return all permitted S-neighbourhood masks of r_index."""

    answer: list[int] = []
    for mask in range(1 << 7):
        vertices = tuple(vertex for vertex in S if mask >> vertex & 1)
        if len(vertices) < 5:
            continue
        if {S_COLOUR[vertex] for vertex in vertices} != {0, 1, 2, 3}:
            continue

        same_colour = tuple(
            vertex
            for vertex in vertices
            if S_COLOUR[vertex] == R_COLOUR[index]
        )
        if index in MARKED:
            if same_colour != (MARKED[index],):
                continue
        elif same_colour:
            continue
        answer.append(mask)
    return tuple(answer)


OPTIONS = tuple(attachment_options(index) for index in R)


def adjacency(attachments: tuple[int, ...]) -> tuple[int, ...]:
    """Build ell, C7=S, C5=R with the specified S-R edges."""

    graph = [0] * 13

    def add_edge(left: int, right: int) -> None:
        graph[left] |= 1 << right
        graph[right] |= 1 << left

    # Vertex 0 is ell, vertices 1..7 are S, and vertices 8..12 are R.
    for vertex in S:
        add_edge(0, 1 + vertex)
        add_edge(1 + vertex, 1 + (vertex + 1) % 7)
    for vertex in R:
        add_edge(8 + vertex, 8 + (vertex + 1) % 5)
    for index, mask in enumerate(attachments):
        for vertex in S:
            if mask >> vertex & 1:
                add_edge(1 + vertex, 8 + index)
    return tuple(graph)


def as_networkx(graph: tuple[int, ...]) -> nx.Graph:
    answer = nx.Graph()
    answer.add_nodes_from(range(len(graph)))
    answer.add_edges_from(
        (left, right)
        for left in range(len(graph))
        for right in range(left + 1, len(graph))
        if graph[left] >> right & 1
    )
    return answer


def contains_k7(graph: tuple[int, ...]) -> bool:
    return any(
        all(
            graph[left] >> right & 1
            for left, right in itertools.combinations(vertices, 2)
        )
        for vertices in itertools.combinations(range(len(graph)), 7)
    )


def contract_edge(
    graph: tuple[int, ...], left: int, right: int
) -> tuple[int, ...]:
    if left > right:
        left, right = right, left
    assert graph[left] >> right & 1

    image = [vertex if vertex < right else vertex - 1 for vertex in range(len(graph))]
    image[right] = left
    answer = [0] * (len(graph) - 1)
    for first in range(len(graph)):
        for second in range(first + 1, len(graph)):
            if not (graph[first] >> second & 1):
                continue
            new_first, new_second = image[first], image[second]
            if new_first == new_second:
                continue
            answer[new_first] |= 1 << new_second
            answer[new_second] |= 1 << new_first
    return tuple(answer)


@functools.lru_cache(maxsize=None)
def has_k7_minor(graph: tuple[int, ...]) -> bool:
    """Exact contraction test for a K7 minor in a connected graph."""

    if contains_k7(graph):
        return True
    if len(graph) == 7:
        return False

    edges = [
        (left, right)
        for left in range(len(graph))
        for right in range(left + 1, len(graph))
        if graph[left] >> right & 1
    ]
    # This ordering affects running time only.
    edges.sort(
        key=lambda edge: -(graph[edge[0]] | graph[edge[1]]).bit_count()
    )
    return any(has_k7_minor(contract_edge(graph, *edge)) for edge in edges)


def is_subtuple(
    smaller: tuple[int, ...], larger: tuple[int, ...]
) -> bool:
    return all((small & large) == small for small, large in zip(smaller, larger))


def all_attachment_tuples() -> Iterable[tuple[int, ...]]:
    yield from itertools.product(*OPTIONS)


def main() -> None:
    assert tuple(map(len, OPTIONS)) == (5, 19, 5, 19, 19)

    total = 0
    two_full_arcs = 0
    minimum_degree_seven = 0
    seven_connected: list[tuple[int, ...]] = []

    for attachments in all_attachment_tuples():
        total += 1
        # {r0,r1} and {r2,r3,r4} are the two disjoint connected S-full arcs.
        if attachments[0] | attachments[1] != FULL_S:
            continue
        if attachments[2] | attachments[3] | attachments[4] != FULL_S:
            continue
        two_full_arcs += 1

        graph = adjacency(attachments)
        if min(mask.bit_count() for mask in graph) < 7:
            continue
        minimum_degree_seven += 1
        if nx.node_connectivity(as_networkx(graph)) == 7:
            seven_connected.append(attachments)

    minimal: list[tuple[int, ...]] = []
    for attachments in sorted(
        seven_connected, key=lambda item: sum(mask.bit_count() for mask in item)
    ):
        if any(is_subtuple(old, attachments) for old in minimal):
            continue
        minimal.append(attachments)

    assert total == 171_475
    assert two_full_arcs == 85_536
    assert minimum_degree_seven == 647
    assert len(seven_connected) == 647
    assert len(minimal) == 234
    assert {sum(mask.bit_count() for mask in item) for item in minimal} == {29}
    assert all(
        any(is_subtuple(small, large) for small in minimal)
        for large in seven_connected
    )
    assert all(has_k7_minor(adjacency(item)) for item in minimal)

    print("normalized C5 tight-endpoint family")
    print(f"attachment tuples: {total}")
    print(f"two S-full arcs: {two_full_arcs}")
    print(f"minimum degree at least seven: {minimum_degree_seven}")
    print(f"seven-connected: {len(seven_connected)}")
    print(f"edge-minimal seven-connected tuples: {len(minimal)}")
    print("every edge-minimal tuple has a K7 minor: yes")
    print("therefore every seven-connected tuple has a K7 minor: yes")


if __name__ == "__main__":
    main()
