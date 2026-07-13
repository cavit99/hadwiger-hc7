#!/usr/bin/env python3
"""Verify the finite boundary classification for adaptive exact-seven (1,2).

This is deliberately a boundary-only calculation.  A partition enumerated
here need not be realizable as the equality state of a shore minor.

Run from the repository root with

  PYTHONPATH=active/runtime/deps python3 \
      active/hc7_exact7_adaptive_12_boundary_verify.py
"""

from __future__ import annotations

from collections import Counter
from itertools import combinations
from itertools import permutations

import networkx as nx


S = tuple(range(7))


def set_partitions(vertices: tuple[int, ...]):
    if not vertices:
        yield ()
        return
    first, *rest = vertices
    for partition in set_partitions(tuple(rest)):
        yield (frozenset({first}),) + partition
        for index in range(len(partition)):
            enlarged = list(partition)
            enlarged[index] = enlarged[index] | {first}
            yield tuple(enlarged)


PARTITIONS = tuple(
    partition for partition in set_partitions(S) if len(partition) <= 6
)
assert len(PARTITIONS) == 876


def independent(graph: nx.Graph, vertices: frozenset[int]) -> bool:
    return graph.subgraph(vertices).number_of_edges() == 0


def omega(graph: nx.Graph) -> int:
    if len(graph) == 0:
        return 0
    return max(map(len, nx.find_cliques(graph)))


def clique_number_on(graph: nx.Graph, vertices: frozenset[int]) -> int:
    return omega(graph.subgraph(vertices))


def demand(graph: nx.Graph, partition: tuple[frozenset[int], ...]) -> int:
    singletons = frozenset(
        next(iter(block)) for block in partition if len(block) == 1
    )
    return len(partition) - clique_number_on(graph, singletons)


def is_split(graph: nx.Graph) -> bool:
    vertices = tuple(graph.nodes())
    for size in range(len(vertices) + 1):
        for choice in combinations(vertices, size):
            clique = frozenset(choice)
            remainder = frozenset(vertices) - clique
            if (
                clique_number_on(graph, clique) == len(clique)
                and independent(graph, remainder)
            ):
                return True
    return False


def singleton_safe_condition(graph: nx.Graph, vertex: int) -> bool:
    """The exact structural condition for some demand-at-most-two state."""

    others = frozenset(graph) - {vertex}
    for size in range(4):  # H is K4-free, so every clique has size at most 3.
        for choice in combinations(others, size):
            clique = frozenset(choice)
            if clique_number_on(graph, clique) != len(clique):
                continue

            # The maximum singleton clique may exclude the prescribed
            # singleton.  Then all remaining vertices form one independent
            # block.
            if independent(graph, others - clique):
                return True

            # Or it may contain the prescribed singleton.  Then the remainder
            # needs at most two independent blocks.
            if all(graph.has_edge(vertex, member) for member in clique):
                if nx.is_bipartite(graph.subgraph(others - clique)):
                    return True
    return False


def exact_states(graph: nx.Graph, block: frozenset[int]):
    return [
        partition
        for partition in PARTITIONS
        if block in partition
        and all(independent(graph, part) for part in partition)
    ]


def has_k4_minor_on_five(graph: nx.Graph) -> bool:
    """Exact K4-minor test for a graph on five vertices."""

    assert len(graph) == 5
    if omega(graph) >= 4:
        return True
    vertices = frozenset(graph)
    for left, right in graph.edges():
        singleton_vertices = vertices - {left, right}
        if omega(graph.subgraph(singleton_vertices)) != 3:
            continue
        if all(
            graph.has_edge(left, vertex) or graph.has_edge(right, vertex)
            for vertex in singleton_vertices
        ):
            return True
    return False


def has_two_anchor_lift(graph: nx.Graph) -> bool:
    for anchors in combinations(S, 2):
        remainder = graph.subgraph(frozenset(S) - frozenset(anchors))
        if has_k4_minor_on_five(remainder):
            return True
    return False


def has_triangle_edge_coverage(graph: nx.Graph) -> bool:
    """Label-free form of the two-anchor K4 lift in a K4-free boundary."""

    for triangle_choice in combinations(S, 3):
        triangle = frozenset(triangle_choice)
        if omega(graph.subgraph(triangle)) != 3:
            continue
        outside = frozenset(S) - triangle
        for left, right in combinations(outside, 2):
            if not graph.has_edge(left, right):
                continue
            if all(
                graph.has_edge(left, vertex)
                or graph.has_edge(right, vertex)
                for vertex in triangle
            ):
                return True
    return False


def canonical_double_triangle_signature(graph: nx.Graph) -> str | None:
    """Canonical 9 cross bits + 6 extra-vertex bits for a spanning 2K3+K1."""

    triangles = [
        frozenset(choice)
        for choice in combinations(S, 3)
        if omega(graph.subgraph(choice)) == 3
    ]
    signatures = []
    for left, right in combinations(triangles, 2):
        if not left.isdisjoint(right):
            continue
        extra = next(iter(frozenset(S) - left - right))
        for first, second in ((left, right), (right, left)):
            for ordered_first in permutations(first):
                for ordered_second in permutations(second):
                    bits = tuple(
                        int(graph.has_edge(x, y))
                        for x in ordered_first
                        for y in ordered_second
                    ) + tuple(
                        int(graph.has_edge(extra, x))
                        for x in ordered_first + ordered_second
                    )
                    signatures.append("".join(map(str, bits)))
    return min(signatures) if signatures else None


def two_triangles_and_isolate() -> nx.Graph:
    graph = nx.Graph()
    graph.add_nodes_from(S)
    graph.add_edges_from(((0, 1), (1, 2), (0, 2)))
    graph.add_edges_from(((3, 4), (4, 5), (3, 5)))
    return graph


def three_edges_and_isolate() -> nx.Graph:
    graph = nx.Graph()
    graph.add_nodes_from(S)
    graph.add_edges_from(((0, 1), (2, 3), (4, 5)))
    return graph


def anti_cycle_seven() -> nx.Graph:
    return nx.complement(nx.cycle_graph(7))


def main() -> None:
    graphs = [
        graph
        for graph in nx.graph_atlas_g()
        if len(graph) == 7 and omega(graph) <= 3
    ]
    assert len(graphs) == 685

    categories = Counter()
    range_counts = Counter()
    graph_no_safe_choice = 0
    robust_graphs_by_alpha = Counter()
    residual_graphs_by_alpha_and_safe_existence = Counter()
    two_anchor_residual_by_alpha_and_safe_existence = Counter()
    absolute_hard_two_anchor_residuals = []

    for graph in graphs:
        alpha = omega(nx.complement(graph))
        assert has_two_anchor_lift(graph) == has_triangle_edge_coverage(graph)
        graph_has_safe_choice = False
        graph_has_robust_choice = False

        for size in range(1, alpha + 1):
            for choice in combinations(S, size):
                block = frozenset(choice)
                if not independent(graph, block):
                    continue

                states = exact_states(graph, block)
                assert states
                values = [demand(graph, state) for state in states]
                minimum = min(values)
                maximum = max(values)
                range_counts[(size, minimum, maximum)] += 1
                graph_has_safe_choice |= minimum <= 2

                if size >= 2:
                    remainder_vertices = frozenset(S) - block
                    remainder = graph.subgraph(remainder_vertices)

                    # Exact maximum: refine every residual block to literal
                    # singletons.  Adding an independent block to the
                    # singleton set raises clique number by at most one.
                    expected_maximum = (
                        1 + len(remainder_vertices) - omega(remainder)
                    )
                    assert maximum == expected_maximum

                    # Exact low-demand criterion: after retaining a maximum
                    # singleton clique, at most I and one other independent
                    # block remain.  Equivalently H-I is split.
                    split = is_split(remainder)
                    assert (minimum <= 2) == split

                    # In the K4-free seven-vertex range, every nonsplit
                    # remainder has minimum demand exactly three.
                    if not split:
                        assert minimum == 3

                    # Every returned state is reflectable exactly when the
                    # all-singleton residual state is reflectable.
                    near_clique = omega(remainder) >= len(remainder_vertices) - 1
                    assert (maximum <= 2) == near_clique

                    if maximum <= 2:
                        categories["all_safe_non_singleton"] += 1
                        graph_has_robust_choice = True
                    elif minimum <= 2:
                        categories["mixed_non_singleton"] += 1
                    else:
                        categories["none_safe_non_singleton"] += 1
                else:
                    vertex = next(iter(block))
                    assert (minimum <= 2) == singleton_safe_condition(
                        graph, vertex
                    )

                    other_vertices = frozenset(S) - block
                    pairs = [
                        frozenset(pair)
                        for pair in combinations(other_vertices, 2)
                        if independent(graph, frozenset(pair))
                    ]
                    assert pairs  # K4-free rules out a K6 on the other side.
                    expected_maximum = 6 - min(
                        clique_number_on(graph, frozenset(S) - pair)
                        for pair in pairs
                    )
                    assert maximum == expected_maximum
                    assert maximum >= 3

                    if minimum <= 2:
                        categories["mixed_singleton"] += 1
                    else:
                        categories["none_safe_singleton"] += 1

        if not graph_has_safe_choice:
            graph_no_safe_choice += 1
        if graph_has_robust_choice:
            robust_graphs_by_alpha[alpha] += 1
        else:
            residual_graphs_by_alpha_and_safe_existence[
                (alpha, graph_has_safe_choice)
            ] += 1
            if not has_two_anchor_lift(graph):
                two_anchor_residual_by_alpha_and_safe_existence[
                    (alpha, graph_has_safe_choice)
                ] += 1
                if not graph_has_safe_choice:
                    absolute_hard_two_anchor_residuals.append(graph.copy())

    # Three explicit guardrail families.
    obstruction = two_triangles_and_isolate()
    assert omega(obstruction) == 3
    assert omega(nx.complement(obstruction)) == 3
    for size in range(1, 4):
        for choice in combinations(S, size):
            block = frozenset(choice)
            if independent(obstruction, block):
                assert min(map(lambda state: demand(obstruction, state),
                               exact_states(obstruction, block))) >= 3

    nonrobust = three_edges_and_isolate()
    maximum_sets = [
        frozenset(choice)
        for choice in combinations(S, 4)
        if independent(nonrobust, frozenset(choice))
    ]
    assert maximum_sets
    for block in maximum_sets:
        values = [demand(nonrobust, state) for state in exact_states(nonrobust, block)]
        assert min(values) <= 2 < max(values)

    anti_cycle = anti_cycle_seven()
    assert omega(anti_cycle) == 3
    assert omega(nx.complement(anti_cycle)) == 2
    for size in (1, 2):
        for choice in combinations(S, size):
            block = frozenset(choice)
            if independent(anti_cycle, block):
                assert {
                    demand(anti_cycle, state)
                    for state in exact_states(anti_cycle, block)
                } == {3}

    assert sum(robust_graphs_by_alpha.values()) == 446
    assert sum(residual_graphs_by_alpha_and_safe_existence.values()) == 239
    assert sum(two_anchor_residual_by_alpha_and_safe_existence.values()) == 129
    assert graph_no_safe_choice == 37
    assert two_anchor_residual_by_alpha_and_safe_existence == Counter(
        {
            (2, False): 1,
            (2, True): 1,
            (3, False): 9,
            (3, True): 87,
            (4, True): 31,
        }
    )
    assert len(absolute_hard_two_anchor_residuals) == 10
    hard_signatures = {
        canonical_double_triangle_signature(graph)
        for graph in absolute_hard_two_anchor_residuals
    }
    assert None not in hard_signatures
    assert hard_signatures == {
        "000000000000000",
        "000000000000001",
        "000000000001001",
        "000000000000011",
        "000000000001011",
        "000000000011011",
        "000000001010110",
        "000001010100100",
        "000001010100101",
        "000000001110110",
    }

    print("VERIFIED")
    print(f"k4_free_unlabeled_boundaries={len(graphs)}")
    print(f"proper_partitions={len(PARTITIONS)}")
    print(f"graphs_with_no_combinatorially_safe_I={graph_no_safe_choice}")
    print(f"graphs_with_robust_I={sum(robust_graphs_by_alpha.values())}")
    print(
        "graphs_without_robust_I="
        f"{sum(residual_graphs_by_alpha_and_safe_existence.values())}"
    )
    print("robust_graphs_by_alpha:")
    for key, value in sorted(robust_graphs_by_alpha.items()):
        print(f"  alpha={key}: {value}")
    print("residual_graphs_by_alpha_and_safe_existence:")
    for key, value in sorted(residual_graphs_by_alpha_and_safe_existence.items()):
        print(f"  alpha={key[0]},some_safe={key[1]}: {value}")
    print("two_anchor_residual_by_alpha_and_safe_existence:")
    for key, value in sorted(two_anchor_residual_by_alpha_and_safe_existence.items()):
        print(f"  alpha={key[0]},some_safe={key[1]}: {value}")
    print("absolute_hard_two_anchor_residuals=10")
    print("all_ten_have_two_vertex_disjoint_triangles=True")
    print("categories:")
    for key, value in sorted(categories.items()):
        print(f"  {key}={value}")
    print("independent_set_demand_ranges:")
    for key, value in sorted(range_counts.items()):
        print(f"  {key}={value}")
    print("explicit_guardrails=2K3+K1,3K2+K1,complement(C7)")


if __name__ == "__main__":
    main()
