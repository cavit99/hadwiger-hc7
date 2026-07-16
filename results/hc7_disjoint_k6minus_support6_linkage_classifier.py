#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = ["networkx==3.6.1"]
# ///
"""Classify the six-link quotient and one additional linkage bridge.

The computation is finite and exact.  The only dependency is NetworkX.
"""

from __future__ import annotations

import functools
import itertools

import networkx as nx  # noqa: E402


CORE = range(4)
LEFT = range(6)
RIGHT = range(6, 12)
MISSING_RIGHT_EDGE = (10, 11)

CONTACTS = {
    "3+1": ((4, 0), (4, 1), (4, 2), (5, 3)),
    "2+2": ((4, 0), (4, 1), (5, 2), (5, 3)),
}

EXPECTED_BAD_MATCHINGS = {
    "3+1": ((0, 5), (1, 5), (2, 5), (3, 4)),
    "2+2": ((0, 5), (1, 5), (2, 4), (3, 4)),
}

EXPECTED_BAD_BRIDGES = {
    ("3+1", (0, 5)): (
        (0, 1), (0, 2), (0, 3), (0, 4), (1, 2),
        (1, 5), (2, 5), (3, 5), (4, 5),
    ),
    ("3+1", (1, 5)): (
        (0, 1), (0, 2), (0, 5), (1, 2), (1, 3),
        (1, 4), (2, 5), (3, 5), (4, 5),
    ),
    ("3+1", (2, 5)): (
        (0, 1), (0, 2), (0, 5), (1, 2), (1, 5),
        (2, 3), (2, 4), (3, 5), (4, 5),
    ),
    ("3+1", (3, 4)): (
        (0, 1), (0, 2), (0, 3), (0, 4), (1, 2),
        (1, 3), (1, 4), (2, 3), (2, 4), (3, 5), (4, 5),
    ),
    ("2+2", (0, 5)): (
        (0, 1), (0, 2), (0, 3), (0, 4),
        (1, 5), (2, 5), (3, 5), (4, 5),
    ),
    ("2+2", (1, 5)): (
        (0, 1), (0, 5), (1, 2), (1, 3), (1, 4),
        (2, 5), (3, 5), (4, 5),
    ),
    ("2+2", (2, 4)): (
        (0, 2), (0, 4), (1, 2), (1, 4),
        (2, 3), (2, 5), (3, 4), (4, 5),
    ),
    ("2+2", (3, 4)): (
        (0, 3), (0, 4), (1, 3), (1, 4),
        (2, 3), (2, 4), (3, 5), (4, 5),
    ),
}

# For the representative bad matchings, a Rolek--Song bridge forced from
# path i to path j always yields the endpoint edge i--matching[j].  These are
# the target sets for which that one oriented contraction still fails.
EXPECTED_BAD_ORIENTED_TARGETS = {
    ("3+1", (0, 5)): {
        0: (1, 2, 3, 4),
        1: (0, 2, 5),
        2: (0, 1, 5),
        3: (0, 1, 2, 5),
        4: (0, 1, 2, 5),
        5: (1, 2, 3, 4),
    },
    ("3+1", (3, 4)): {
        0: (1, 2, 3, 4),
        1: (0, 2, 3, 4),
        2: (0, 1, 3, 4),
        3: (0, 1, 2, 5),
        4: (0, 1, 2, 5),
        5: (0, 1, 2, 3, 4),
    },
    ("2+2", (0, 5)): {
        0: (1, 2, 3, 4),
        1: (0, 5),
        2: (0, 1, 5),
        3: (0, 1, 5),
        4: (0, 1, 5),
        5: (1, 2, 3, 4),
    },
}

# Each set below consists entirely of residual oriented contractions and
# nevertheless crosses every admissible connected left/right bipartition
# from the six-vertex deletion argument in Section 5 of the note.
ALL_BAD_CUT_COVERS = {
    ("3+1", (0, 5)): (
        (0, 3), (1, 5), (2, 0), (3, 1), (4, 2), (5, 4),
    ),
    ("3+1", (3, 4)): (
        (0, 3), (1, 4), (2, 1), (3, 5), (4, 0), (5, 2),
    ),
    ("2+2", (0, 5)): (
        (0, 2), (0, 3), (1, 5), (2, 5), (3, 1), (4, 0), (5, 4),
    ),
}


def left_edges(normal_form: str) -> list[tuple[int, int]]:
    return [
        *itertools.combinations(CORE, 2),
        (4, 5),
        *CONTACTS[normal_form],
    ]


def matching_for(missing_preimage: tuple[int, int]) -> dict[int, int]:
    remaining = [vertex for vertex in LEFT if vertex not in missing_preimage]
    return dict(
        [*zip(missing_preimage, MISSING_RIGHT_EDGE), *zip(remaining, range(6, 10))]
    )


def base_graph(normal_form: str, missing_preimage: tuple[int, int]) -> nx.Graph:
    graph = nx.Graph()
    graph.add_nodes_from(range(12))
    graph.add_edges_from(left_edges(normal_form))
    graph.add_edges_from(
        edge
        for edge in itertools.combinations(RIGHT, 2)
        if edge != MISSING_RIGHT_EDGE
    )
    graph.add_edges_from(matching_for(missing_preimage).items())
    return graph


def bridged_graph(
    normal_form: str,
    missing_preimage: tuple[int, int],
    bridge_pair: tuple[int, int],
) -> nx.Graph:
    """Subdivide two matching edges and join their subdivision vertices."""

    graph = base_graph(normal_form, missing_preimage)
    matching = matching_for(missing_preimage)
    for left, subdivision in zip(bridge_pair, (12, 13)):
        right = matching[left]
        graph.remove_edge(left, right)
        graph.add_edges_from(((left, subdivision), (subdivision, right)))
    graph.add_edge(12, 13)
    return graph


def exact_k7_at_most_twelve(graph: nx.Graph) -> bool:
    """Exact branch-set search on a graph of order at most twelve.

    A seven-bag model on n<=12 vertices has at least 14-n singleton bags.
    The singleton bags form a clique.  The search fixes that exact singleton
    clique and enumerates the remaining disjoint connected bags.
    """

    graph = nx.convert_node_labels_to_integers(graph)
    order = len(graph)
    assert order <= 12
    if order < 7:
        return False

    adjacency = [
        sum(1 << neighbour for neighbour in graph[vertex])
        for vertex in range(order)
    ]
    full = (1 << order) - 1

    @functools.lru_cache(maxsize=None)
    def connected(mask: int) -> bool:
        reached = mask & -mask
        while True:
            old = reached
            neighbours = 0
            for vertex in range(order):
                if reached >> vertex & 1:
                    neighbours |= adjacency[vertex]
            reached |= neighbours & mask
            if reached == old:
                return reached == mask

    @functools.lru_cache(maxsize=None)
    def touches(left: int, right: int) -> bool:
        return any(
            adjacency[vertex] & right
            for vertex in range(order)
            if left >> vertex & 1
        )

    minimum_singletons = max(0, 14 - order)
    for singleton_count in range(7, minimum_singletons - 1, -1):
        non_singleton_count = 7 - singleton_count
        for singleton_vertices in itertools.combinations(range(order), singleton_count):
            if any(
                not (adjacency[left] >> right & 1)
                for left, right in itertools.combinations(singleton_vertices, 2)
            ):
                continue
            if non_singleton_count == 0:
                return True

            singleton_mask = sum(1 << vertex for vertex in singleton_vertices)
            remainder = full ^ singleton_mask
            maximum_size = remainder.bit_count() - 2 * (non_singleton_count - 1)
            candidates: list[int] = []
            subset = remainder
            while subset:
                if (
                    2 <= subset.bit_count() <= maximum_size
                    and connected(subset)
                    and all(
                        touches(subset, 1 << vertex)
                        for vertex in singleton_vertices
                    )
                ):
                    candidates.append(subset)
                subset = (subset - 1) & remainder

            def search(start: int, chosen: tuple[int, ...], used: int) -> bool:
                missing = non_singleton_count - len(chosen)
                if missing == 0:
                    return True
                if (remainder & ~used).bit_count() < 2 * missing:
                    return False
                for position in range(start, len(candidates)):
                    candidate = candidates[position]
                    if candidate & used:
                        continue
                    if all(touches(candidate, old) for old in chosen) and search(
                        position + 1,
                        chosen + (candidate,),
                        used | candidate,
                    ):
                        return True
                return False

            if search(0, (), 0):
                return True
    return False


def contract(graph: nx.Graph, left: int, right: int) -> nx.Graph:
    return nx.Graph(nx.contracted_nodes(graph, left, right, self_loops=False, copy=True))


def exact_k7_with_low_degree_reduction(graph: nx.Graph) -> bool:
    """Exact detector for the 14-vertex one-bridge graphs.

    If deg(v)<6, v cannot be a singleton bag of a K7 model.  Hence a K7
    model either avoids v or contains an edge vu inside v's branch set.
    This gives the exact deletion/contraction recurrence below.  It removes
    the two degree-three subdivision vertices before invoking the <=12
    detector.
    """

    if len(graph) <= 12:
        return exact_k7_at_most_twelve(graph)
    vertex = min(graph, key=graph.degree)
    assert graph.degree(vertex) < 6
    without = graph.subgraph([old for old in graph if old != vertex]).copy()
    if exact_k7_with_low_degree_reduction(without):
        return True
    return any(
        exact_k7_with_low_degree_reduction(contract(graph, vertex, neighbour))
        for neighbour in tuple(graph[vertex])
    )


def main() -> None:
    for normal_form in CONTACTS:
        bad_matchings = tuple(
            pair
            for pair in itertools.combinations(LEFT, 2)
            if not exact_k7_at_most_twelve(base_graph(normal_form, pair))
        )
        assert bad_matchings == EXPECTED_BAD_MATCHINGS[normal_form]
        print(normal_form, "bad_matchings", bad_matchings)

        for missing_preimage in bad_matchings:
            bad_bridges = tuple(
                pair
                for pair in itertools.combinations(LEFT, 2)
                if not exact_k7_with_low_degree_reduction(
                    bridged_graph(normal_form, missing_preimage, pair)
                )
            )
            assert bad_bridges == EXPECTED_BAD_BRIDGES[(normal_form, missing_preimage)]
            print(normal_form, missing_preimage, "bad_bridges", bad_bridges)

    for key, expected in EXPECTED_BAD_ORIENTED_TARGETS.items():
        normal_form, missing_preimage = key
        graph = base_graph(normal_form, missing_preimage)
        matching = matching_for(missing_preimage)
        actual = {}
        for source in LEFT:
            bad_targets = []
            for target in LEFT:
                if source == target:
                    continue
                augmented = graph.copy()
                augmented.add_edge(source, matching[target])
                if not exact_k7_at_most_twelve(augmented):
                    bad_targets.append(target)
            actual[source] = tuple(bad_targets)
        assert actual == expected
        print(normal_form, missing_preimage, "bad_oriented_targets", actual)

        left = nx.Graph()
        left.add_nodes_from(LEFT)
        left.add_edges_from(left_edges(normal_form))
        right = nx.Graph()
        right.add_nodes_from(RIGHT)
        right.add_edges_from(
            edge
            for edge in itertools.combinations(RIGHT, 2)
            if edge != MISSING_RIGHT_EDGE
        )
        cut_cover = ALL_BAD_CUT_COVERS[key]
        assert all(target in expected[source] for source, target in cut_cover)
        matching = matching_for(missing_preimage)
        for mask in range(1, (1 << 6) - 1):
            left_indices = {index for index in LEFT if mask >> index & 1}
            right_indices = set(LEFT) - left_indices
            if not nx.is_connected(left.subgraph(left_indices)):
                continue
            right_vertices = {matching[index] for index in right_indices}
            if not nx.is_connected(right.subgraph(right_vertices)):
                continue
            assert any(
                source in left_indices and target in right_indices
                for source, target in cut_cover
            )
        print(normal_form, missing_preimage, "all_bad_cut_cover", cut_cover)

    # Check the invariant formulation with arbitrary common contacts.  Status
    # 0 means adjacent only to 4, status 1 only to 5, and status 2 to both.
    # Requiring both 0 and 1 is exactly the irredundancy condition that neither
    # endpoint of the split edge alone completes the K4 to a K5.
    right_edges = [
        edge
        for edge in itertools.combinations(RIGHT, 2)
        if edge != MISSING_RIGHT_EDGE
    ]
    contact_patterns = 0
    for statuses in itertools.product(range(3), repeat=4):
        if 0 not in statuses or 1 not in statuses:
            continue
        contact_patterns += 1
        left = [*itertools.combinations(CORE, 2), (4, 5)]
        for core_vertex, status in enumerate(statuses):
            if status in (0, 2):
                left.append((core_vertex, 4))
            if status in (1, 2):
                left.append((core_vertex, 5))
        left_edge_set = {tuple(sorted(edge)) for edge in left}
        for missing_preimage in itertools.combinations(LEFT, 2):
            graph = nx.Graph()
            graph.add_nodes_from(range(12))
            graph.add_edges_from(left)
            graph.add_edges_from(right_edges)
            graph.add_edges_from(matching_for(missing_preimage).items())
            assert exact_k7_at_most_twelve(graph) == (
                missing_preimage in left_edge_set
            )

    print("general_contact_patterns", contact_patterns)

    print("GREEN: exact matching and one-bridge classifications verified")


if __name__ == "__main__":
    main()
