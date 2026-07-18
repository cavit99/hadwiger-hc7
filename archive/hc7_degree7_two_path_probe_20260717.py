#!/usr/bin/env python3
"""Probe the degree-seven boundary after adding two returned path edges.

This is a theorem-discovery script, not a promoted finite result.  It ranges
over the 1,044 unlabeled graphs on seven vertices and retains precisely the
static boundary conditions proved for the current bounded-interface setup.
For every pair of disjoint nonedges it asks whether adding those edges gives
a K5 minor on the boundary.
"""

from __future__ import annotations

from functools import lru_cache
from itertools import combinations

import networkx as nx


def bits(graph: nx.Graph) -> tuple[int, ...]:
    vertices = tuple(sorted(graph))
    position = {vertex: index for index, vertex in enumerate(vertices)}
    adjacency = [0] * len(vertices)
    for left, right in graph.edges():
        i, j = position[left], position[right]
        adjacency[i] |= 1 << j
        adjacency[j] |= 1 << i
    return tuple(adjacency)


def delete_vertex(adjacency: tuple[int, ...], vertex: int) -> tuple[int, ...]:
    keep = tuple(index for index in range(len(adjacency)) if index != vertex)
    position = {old: new for new, old in enumerate(keep)}
    result = [0] * len(keep)
    for i, old_i in enumerate(keep):
        for old_j in keep:
            if adjacency[old_i] & (1 << old_j):
                result[i] |= 1 << position[old_j]
    return tuple(result)


def contract_edge(
    adjacency: tuple[int, ...], left: int, right: int
) -> tuple[int, ...]:
    if left > right:
        left, right = right, left
    keep = tuple(index for index in range(len(adjacency)) if index != right)
    position = {old: new for new, old in enumerate(keep)}
    result = [0] * len(keep)
    for i, old_i in enumerate(keep):
        for j in range(i + 1, len(keep)):
            old_j = keep[j]
            adjacent = bool(adjacency[old_i] & (1 << old_j))
            if old_i == left:
                adjacent |= bool(adjacency[right] & (1 << old_j))
            if old_j == left:
                adjacent |= bool(adjacency[old_i] & (1 << right))
            if adjacent:
                result[i] |= 1 << j
                result[j] |= 1 << i
    return tuple(result)


@lru_cache(maxsize=None)
def has_clique_minor(adjacency: tuple[int, ...], order: int) -> bool:
    size = len(adjacency)
    if size < order:
        return False
    if size == order:
        return all(row.bit_count() == order - 1 for row in adjacency)
    for vertex in range(size):
        if has_clique_minor(delete_vertex(adjacency, vertex), order):
            return True
    for left in range(size):
        for right in range(left + 1, size):
            if adjacency[left] & (1 << right):
                if has_clique_minor(contract_edge(adjacency, left, right), order):
                    return True
    return False


def join_independent_pair(graph: nx.Graph) -> nx.Graph:
    result = graph.copy()
    left, right = 7, 8
    result.add_nodes_from((left, right))
    for vertex in range(7):
        result.add_edge(left, vertex)
        result.add_edge(right, vertex)
    return result


def join_independent_set(graph: nx.Graph, order: int) -> nx.Graph:
    result = graph.copy()
    new_vertices = tuple(range(7, 7 + order))
    result.add_nodes_from(new_vertices)
    for new_vertex in new_vertices:
        for vertex in range(7):
            result.add_edge(new_vertex, vertex)
    return result


def is_split(graph: nx.Graph) -> bool:
    return nx.is_chordal(graph) and nx.is_chordal(nx.complement(graph))


def graph_code(graph: nx.Graph) -> str:
    return nx.to_graph6_bytes(graph, header=False).decode().strip()


def colorable(graph: nx.Graph, colour_count: int) -> bool:
    adjacency = bits(graph)
    colours = [-1] * len(adjacency)

    def search(coloured: int) -> bool:
        if coloured == len(adjacency):
            return True
        uncoloured = [v for v, colour in enumerate(colours) if colour < 0]
        vertex = max(uncoloured, key=lambda v: adjacency[v].bit_count())
        forbidden = {
            colours[other]
            for other in range(len(adjacency))
            if colours[other] >= 0 and adjacency[vertex] & (1 << other)
        }
        for colour in range(colour_count):
            if colour in forbidden:
                continue
            colours[vertex] = colour
            if search(coloured + 1):
                return True
            colours[vertex] = -1
        return False

    return search(0)


def main() -> None:
    boundaries = []
    for graph in nx.graph_atlas_g():
        if len(graph) != 7:
            continue
        complement = nx.complement(graph)
        if max(map(len, nx.find_cliques(complement)), default=0) > 2:
            continue
        if not colorable(graph, 4):
            continue
        if is_split(graph):
            continue
        if has_clique_minor(bits(join_independent_pair(graph)), 7):
            continue
        boundaries.append(graph)

    total_pairs = 0
    bad = []
    profile = {minimum: [0, 0, 0] for minimum in range(4, 7)}
    for minimum in profile:
        profile[minimum][0] = sum(
            1 for graph in boundaries if min(dict(graph.degree()).values()) >= minimum
        )
    for graph in boundaries:
        nonedges = tuple(tuple(sorted(edge)) for edge in nx.complement(graph).edges())
        for first, second in combinations(nonedges, 2):
            if set(first) & set(second):
                continue
            total_pairs += 1
            for minimum in profile:
                if min(dict(graph.degree()).values()) >= minimum:
                    profile[minimum][1] += 1
            augmented = graph.copy()
            augmented.add_edges_from((first, second))
            if not has_clique_minor(bits(augmented), 5):
                bad.append((graph_code(graph), first, second, graph.number_of_edges()))
                for minimum in profile:
                    if min(dict(graph.degree()).values()) >= minimum:
                        profile[minimum][2] += 1

    print(f"boundaries={len(boundaries)}")
    print(f"disjoint_nonedges_tested={total_pairs}")
    print(f"bad_pairs={len(bad)}")
    for minimum, (graph_count, pair_count, bad_count) in profile.items():
        print(
            f"minimum_degree_at_least_{minimum}: "
            f"boundaries={graph_count} pairs={pair_count} bad={bad_count}"
        )
    print("minimum_degree_four_boundaries:")
    for graph in boundaries:
        if min(dict(graph.degree()).values()) >= 4:
            print(
                graph_code(graph),
                sorted(dict(graph.degree()).values()),
                sorted(nx.complement(graph).edges()),
                "I3joinK7=",
                has_clique_minor(bits(join_independent_set(graph, 3)), 7),
            )
    for item in bad[:40]:
        print(item)


if __name__ == "__main__":
    main()
