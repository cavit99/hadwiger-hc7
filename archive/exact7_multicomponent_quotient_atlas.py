#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = ["networkx>=3.4"]
# ///
"""Exact K7-minor atlas for seven roots plus three or four full helpers.

The quotient has a seven-vertex boundary J and m independent helper
vertices, each complete to J.  It is connected, so any K7 model can be
made spanning.  For n=10,11, spanning models are exactly partitions into
seven nonempty connected, pairwise adjacent blocks.  There are only
S(10,7)=5,880 and S(11,7)=63,987 such set partitions.
"""

from __future__ import annotations

from collections import Counter
from functools import lru_cache
import itertools

import networkx as nx


def partitions_masks(n: int, k: int = 7) -> tuple[tuple[int, ...], ...]:
    """Restricted-growth enumeration of set partitions into k blocks."""
    answer: list[tuple[int, ...]] = []
    labels = [0] * n

    def rec(pos: int, maximum: int) -> None:
        if pos == n:
            if maximum + 1 == k:
                blocks = [0] * k
                for vertex, label in enumerate(labels):
                    blocks[label] |= 1 << vertex
                answer.append(tuple(blocks))
            return
        remaining = n - pos
        missing = k - (maximum + 1)
        if missing > remaining:
            return
        for label in range(min(maximum + 1, k - 1) + 1):
            labels[pos] = label
            rec(pos + 1, max(maximum, label))

    labels[0] = 0
    rec(1, 0)
    return tuple(answer)


@lru_cache(maxsize=None)
def partitions_for_n(n: int) -> tuple[tuple[int, ...], ...]:
    return partitions_masks(n)


def quotient_adjacency(boundary: nx.Graph, helpers: int) -> tuple[int, ...]:
    n = 7 + helpers
    adjacency = [0] * n
    for first, second in boundary.edges():
        adjacency[first] |= 1 << second
        adjacency[second] |= 1 << first
    for root in range(7):
        for helper in range(7, n):
            adjacency[root] |= 1 << helper
            adjacency[helper] |= 1 << root
    return tuple(adjacency)


def connected(mask: int, adjacency: tuple[int, ...]) -> bool:
    reached = mask & -mask
    while True:
        neighbours = 0
        scan = reached
        while scan:
            bit = scan & -scan
            scan ^= bit
            neighbours |= adjacency[bit.bit_length() - 1]
        expanded = reached | (neighbours & mask)
        if expanded == reached:
            return reached == mask
        reached = expanded


def k7_model(boundary: nx.Graph, helpers: int) -> tuple[int, ...] | None:
    adjacency = quotient_adjacency(boundary, helpers)
    n = len(adjacency)
    neighbour_union = [0] * (1 << n)
    is_connected = [False] * (1 << n)
    for mask in range(1, 1 << n):
        low = mask & -mask
        vertex = low.bit_length() - 1
        neighbour_union[mask] = neighbour_union[mask ^ low] | adjacency[vertex]
        is_connected[mask] = connected(mask, adjacency)

    for blocks in partitions_for_n(n):
        if not all(is_connected[block] for block in blocks):
            continue
        if all(neighbour_union[blocks[i]] & blocks[j]
               for i in range(7) for j in range(i)):
            return blocks
    return None


def signature(graph: nx.Graph) -> tuple[object, ...]:
    return (
        graph.number_of_edges(),
        tuple(sorted(dict(graph.degree()).values(), reverse=True)),
        tuple(sorted((len(c) for c in nx.connected_components(graph)), reverse=True)),
        nx.is_bipartite(graph),
    )


def k_colourable(graph: nx.Graph, colours: int) -> bool:
    order = sorted(graph.nodes(), key=graph.degree, reverse=True)
    assigned: dict[int, int] = {}

    def rec(pos: int) -> bool:
        if pos == len(order):
            return True
        vertex = order[pos]
        forbidden = {assigned[neighbour]
                     for neighbour in graph.neighbors(vertex)
                     if neighbour in assigned}
        for colour in range(colours):
            if colour in forbidden:
                continue
            assigned[vertex] = colour
            if rec(pos + 1):
                return True
            del assigned[vertex]
        return False

    return rec(0)


def chromatic_number(graph: nx.Graph) -> int:
    for colours in range(1, 8):
        if k_colourable(graph, colours):
            return colours
    raise AssertionError


def has_adjacent_singleton_pair_four_colouring(graph: nx.Graph) -> bool:
    vertices = tuple(graph.nodes())
    for colours in itertools.product(range(4), repeat=len(vertices)):
        if set(colours) != set(range(4)):
            continue
        assignment = dict(zip(vertices, colours))
        if any(assignment[first] == assignment[second]
               for first, second in graph.edges()):
            continue
        classes = [[v for v in vertices if assignment[v] == colour]
                   for colour in range(4)]
        singletons = [block[0] for block in classes if len(block) == 1]
        if any(graph.has_edge(first, second)
               for first, second in itertools.combinations(singletons, 2)):
            return True
    return False


def has_clique_residual_block_colouring(
    graph: nx.Graph, components: int = 3, palette: int = 6
) -> bool:
    vertices = tuple(graph.nodes())
    for colour_count in range(components - 1, palette + 1):
        residual_count = colour_count - components + 1
        for colours in itertools.product(range(colour_count), repeat=len(vertices)):
            if set(colours) != set(range(colour_count)):
                continue
            assignment = dict(zip(vertices, colours))
            if any(assignment[first] == assignment[second]
                   for first, second in graph.edges()):
                continue
            classes = [[v for v in vertices if assignment[v] == colour]
                       for colour in range(colour_count)]
            singleton_vertices = [block[0] for block in classes if len(block) == 1]
            for residual in itertools.combinations(singleton_vertices, residual_count):
                if graph.subgraph(residual).number_of_edges() == residual_count * (residual_count - 1) // 2:
                    return True
    return False


def has_singleton_three_colouring(graph: nx.Graph) -> bool:
    vertices = tuple(graph.nodes())
    for colours in itertools.product(range(3), repeat=len(vertices)):
        if set(colours) != set(range(3)):
            continue
        assignment = dict(zip(vertices, colours))
        if any(assignment[first] == assignment[second]
               for first, second in graph.edges()):
            continue
        if any(sum(assignment[v] == colour for v in vertices) == 1
               for colour in range(3)):
            return True
    return False


def has_k4_model_on_at_most_five_vertices(graph: nx.Graph) -> bool:
    vertices = tuple(graph.nodes())
    for used in itertools.combinations(vertices, 4):
        if graph.subgraph(used).number_of_edges() == 6:
            return True
    for support in itertools.combinations(vertices, 5):
        support_set = set(support)
        for pair in itertools.combinations(support, 2):
            if not graph.has_edge(*pair):
                continue
            singles = tuple(support_set - set(pair))
            if graph.subgraph(singles).number_of_edges() != 3:
                continue
            if all(any(graph.has_edge(vertex, endpoint) for endpoint in pair)
                   for vertex in singles):
                return True
    return False


def main() -> None:
    assert len(partitions_for_n(10)) == 5_880
    assert len(partitions_for_n(11)) == 63_987
    for helpers in (4, 3):
        checked = positive = 0
        checked_by_chi: Counter[int] = Counter()
        positive_by_chi: Counter[int] = Counter()
        failures: list[nx.Graph] = []
        for raw in nx.graph_atlas_g():
            if raw.number_of_nodes() != 7:
                continue
            graph = nx.convert_node_labels_to_integers(raw)
            if helpers == 4 and any(len(cycle) == 3 for cycle in nx.simple_cycles(graph, length_bound=3)):
                continue
            clique_number = max((len(clique) for clique in nx.find_cliques(graph)), default=0)
            if helpers == 3 and clique_number >= 4:
                continue
            checked += 1
            chi = chromatic_number(graph)
            checked_by_chi[chi] += 1
            if k7_model(graph, helpers) is not None:
                positive += 1
                positive_by_chi[chi] += 1
            else:
                failures.append(graph)
        counts = Counter(signature(graph) for graph in failures)
        edge_counts = Counter(graph.number_of_edges() for graph in failures)
        chromatic_counts = Counter(chromatic_number(graph) for graph in failures)
        if helpers == 3:
            chi3_failures = [graph for graph in failures if chromatic_number(graph) == 3]
            chi3_residual = [graph for graph in chi3_failures
                             if not has_clique_residual_block_colouring(graph)]
            chi4_failures = [graph for graph in failures if chromatic_number(graph) == 4]
            chi4_residual = [graph for graph in chi4_failures
                             if not has_clique_residual_block_colouring(graph)]
        else:
            chi3_residual = []
            chi4_residual = []
        print("helpers", helpers, "checked", checked, "positive", positive,
              "negative", len(failures), "signatures", len(counts),
              "negative_by_edges", sorted(edge_counts.items()),
              "checked_by_chi", sorted(checked_by_chi.items()),
              "positive_by_chi", sorted(positive_by_chi.items()),
              "negative_by_chi", sorted(chromatic_counts.items()),
              "chi3_after_block_gluing", len(chi3_residual),
              "chi4_after_block_gluing", len(chi4_residual))
        for graph in chi4_residual:
            print(" chi4_residual_edges", sorted(tuple(sorted(edge)) for edge in graph.edges()),
                  "graph6", nx.to_graph6_bytes(graph, header=False).decode().strip())
        for graph in chi3_residual:
            print(" chi3_residual_edges", sorted(tuple(sorted(edge)) for edge in graph.edges()),
                  "graph6", nx.to_graph6_bytes(graph, header=False).decode().strip())

    alpha_two = []
    small_support_failures = []
    for raw in nx.graph_atlas_g():
        if raw.number_of_nodes() != 7:
            continue
        graph = nx.convert_node_labels_to_integers(raw)
        if any(graph.subgraph(triple).number_of_edges() == 0
               for triple in itertools.combinations(graph.nodes(), 3)):
            continue
        alpha_two.append(graph)
        if not has_k4_model_on_at_most_five_vertices(graph):
            small_support_failures.append(graph)
    print("alpha_at_most_two", len(alpha_two),
          "true_small_support_failures", len(small_support_failures),
          "failure_edge_counts",
          sorted(Counter(graph.number_of_edges() for graph in small_support_failures).items()))


if __name__ == "__main__":
    main()
