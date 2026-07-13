#!/usr/bin/env python3
"""Verify the complete raw-list residue with no boundary-anchored K4.

The already proved pair-bicycle and full-list completion results reduce the
search to nonempty masks of size one or two, with at least one singleton.
There are only 9,450 labelled support-valid assignments.  This verifier
checks each against all 107 unlabelled triangle-free graphs of order seven.

Run from the repository root with

  PYTHONPATH=active/runtime/deps python3 \
      results/hc7_exact7_raw_list_no_k4_verify.py
"""

from __future__ import annotations

from collections import Counter
from itertools import combinations, permutations, product

import networkx as nx


NONFULL_MASKS = range(1, 7)
PALETTE_PERMUTATIONS = tuple(permutations(range(3)))
ROOT_SETS = tuple(combinations(range(7), 4))
CARRIER_ASSIGNMENTS = tuple(product(range(5), repeat=3))
BAG_PAIRS = tuple(combinations(range(4), 2))


def triangle_free(graph: nx.Graph) -> bool:
    return not any(nx.triangles(graph).values())


def support_valid(lists: tuple[int, ...]) -> bool:
    return all(
        sum(bool(mask & (1 << colour)) for mask in lists) >= 4
        for colour in range(3)
    )


def unit_propagation(
    graph: nx.Graph, lists: tuple[int, ...]
) -> tuple[bool, int, tuple[int, ...]]:
    """Return (conflict, alive mask, propagated lists)."""

    current = list(lists)
    alive = (1 << 7) - 1
    while True:
        singleton = next(
            (
                vertex
                for vertex in range(7)
                if alive & (1 << vertex) and current[vertex].bit_count() == 1
            ),
            None,
        )
        if singleton is None:
            return False, alive, tuple(current)
        colour_mask = current[singleton]
        alive &= ~(1 << singleton)
        for neighbour in graph[singleton]:
            if not alive & (1 << neighbour):
                continue
            if current[neighbour] & colour_mask:
                current[neighbour] &= ~colour_mask
                if current[neighbour] == 0:
                    return True, alive, tuple(current)


def residual_colourable(
    graph: nx.Graph, alive: int, lists: tuple[int, ...]
) -> bool:
    vertices = [vertex for vertex in range(7) if alive & (1 << vertex)]
    vertices.sort(key=lambda vertex: (lists[vertex].bit_count(), -graph.degree[vertex]))
    colours: dict[int, int] = {}

    def extend(position: int) -> bool:
        if position == len(vertices):
            return True
        vertex = vertices[position]
        forbidden = {
            colours[neighbour]
            for neighbour in graph[vertex]
            if neighbour in colours
        }
        for colour in range(3):
            if lists[vertex] & (1 << colour) and colour not in forbidden:
                colours[vertex] = colour
                if extend(position + 1):
                    return True
                del colours[vertex]
        return False

    return extend(0)


def uncolourable(graph: nx.Graph, lists: tuple[int, ...]) -> tuple[bool, bool]:
    conflict, alive, propagated = unit_propagation(graph, lists)
    if conflict:
        return True, True
    return not residual_colourable(graph, alive, propagated), False


def anchored_k4(graph: nx.Graph, lists: tuple[int, ...]) -> bool:
    """Exact standard four-root/three-carrier model search."""

    for roots in ROOT_SETS:
        for assignment in CARRIER_ASSIGNMENTS:
            # carriers[index] is the three-bit carrier subset in rooted bag i.
            carriers = [0, 0, 0, 0]
            for colour, bag_index in enumerate(assignment):
                if bag_index < 4:
                    carriers[bag_index] |= 1 << colour

            # A root plus carrier subset is connected iff it contacts at least
            # one carrier in that subset; the carriers themselves form K3.
            if any(
                carriers[index]
                and not lists[roots[index]] & carriers[index]
                for index in range(4)
            ):
                continue

            valid = True
            for left, right in BAG_PAIRS:
                if carriers[left] and carriers[right]:
                    continue
                if graph.has_edge(roots[left], roots[right]):
                    continue
                if lists[roots[right]] & carriers[left]:
                    continue
                if lists[roots[left]] & carriers[right]:
                    continue
                valid = False
                break
            if valid:
                return True
    return False


def remap_mask(mask: int, permutation: tuple[int, int, int]) -> int:
    return sum(
        1 << permutation[colour]
        for colour in range(3)
        if mask & (1 << colour)
    )


def canonical_lists(graph: nx.Graph, lists: tuple[int, ...]) -> tuple[int, ...]:
    best: tuple[int, ...] | None = None
    matcher = nx.algorithms.isomorphism.GraphMatcher(graph, graph)
    for automorphism in matcher.isomorphisms_iter():
        for palette_permutation in PALETTE_PERMUTATIONS:
            image = [0] * 7
            for old_vertex, new_vertex in automorphism.items():
                image[new_vertex] = remap_mask(lists[old_vertex], palette_permutation)
            candidate = tuple(image)
            if best is None or candidate < best:
                best = candidate
    assert best is not None
    return best


def forced_path_type(graph: nx.Graph, lists: tuple[int, ...]) -> str | None:
    singletons = [vertex for vertex, mask in enumerate(lists) if mask.bit_count() == 1]
    if len(singletons) != 2:
        return None
    first, second = singletons
    if lists[first] == lists[second] and graph.has_edge(first, second):
        return "edge"
    for left, right in ((first, second), (second, first)):
        for middle in graph[left]:
            if (
                graph.has_edge(middle, right)
                and lists[middle] == lists[left] | lists[right]
            ):
                return "two_edge_path"
    return None


def has_one_block_edge(graph: nx.Graph) -> bool:
    """Some edge pq leaves the other five literal vertices independent."""

    for left, right in graph.edges():
        complement = set(range(7)) - {left, right}
        if not any(
            u in complement and v in complement for u, v in graph.edges()
        ):
            return True
    return False


EXPECTED_ORBITS = {
    # K2 + 5K1: the edge is the equal-singleton conflict.
    "F???G": {(3, 3, 3, 5, 6, 4, 4)},
    # P3 + 4K1: one direct conflict and one two-step implication type.
    "FH???": {
        (3, 1, 1, 5, 6, 6, 6),
        (3, 1, 5, 4, 3, 6, 6),
    },
    # P4 + 3K1: the central edge is the equal-singleton conflict.
    "F??KG": {(3, 5, 5, 5, 6, 2, 2)},
}


def main() -> None:
    patterns = [
        lists
        for lists in product(NONFULL_MASKS, repeat=7)
        if support_valid(lists)
        and any(mask.bit_count() == 1 for mask in lists)
    ]
    assert len(patterns) == 9450

    graphs = [
        graph
        for graph in nx.graph_atlas_g()
        if len(graph) == 7 and triangle_free(graph)
    ]
    assert len(graphs) == 107

    uncolourable_count = 0
    colourable_count = 0
    anchored_uncolourable_count = 0
    bad_trichotomy_count = 0
    survivors: dict[str, list[tuple[int, ...]]] = {}
    propagation = Counter()

    for graph in graphs:
        encoding = nx.to_graph6_bytes(graph, header=False).strip().decode("ascii")
        for lists in patterns:
            is_uncolourable, immediate_conflict = uncolourable(graph, lists)
            if not is_uncolourable:
                colourable_count += 1
                continue
            uncolourable_count += 1
            if anchored_k4(graph, lists):
                anchored_uncolourable_count += 1
                continue
            # This is the directly asserted third arm of the exhaustive
            # trichotomy, not an inference from the final orbit names.
            if not has_one_block_edge(graph):
                bad_trichotomy_count += 1
            survivors.setdefault(encoding, []).append(lists)
            propagation["unit_conflict" if immediate_conflict else "residual"] += 1

    assert uncolourable_count == 194706
    assert colourable_count == 816444
    assert anchored_uncolourable_count == 194556
    assert bad_trichotomy_count == 0
    assert {encoding: len(states) for encoding, states in survivors.items()} == {
        "F???G": 60,
        "FH???": 84,
        "F??KG": 6,
    }
    assert sum(map(len, survivors.values())) == 150
    assert propagation == {"unit_conflict": 150}

    orbit_catalogue: dict[str, set[tuple[int, ...]]] = {}
    path_types = Counter()
    for graph in graphs:
        encoding = nx.to_graph6_bytes(graph, header=False).strip().decode("ascii")
        if encoding not in survivors:
            continue
        orbit_catalogue[encoding] = {
            canonical_lists(graph, lists) for lists in survivors[encoding]
        }
        for lists in survivors[encoding]:
            # These are conclusions, not search restrictions.
            assert all(
                sum(bool(mask & (1 << colour)) for mask in lists) == 4
                for colour in range(3)
            )
            assert sum(mask.bit_count() == 1 for mask in lists) == 2
            assert sum(mask.bit_count() == 2 for mask in lists) == 5
            certificate = forced_path_type(graph, lists)
            assert certificate is not None
            path_types[certificate] += 1

    assert orbit_catalogue == EXPECTED_ORBITS, orbit_catalogue
    assert path_types == {"edge": 114, "two_edge_path": 36}

    # Explicitly retain both externally supplied sparse counterexamples.
    path_graph = nx.Graph()
    path_graph.add_nodes_from(range(7))
    path_graph.add_edges_from(((1, 2), (2, 3)))
    supplied_direct = (5, 6, 2, 2, 3, 5, 5)
    assert support_valid(supplied_direct)
    assert uncolourable(path_graph, supplied_direct)[0]
    assert not anchored_k4(path_graph, supplied_direct)
    supplied_implication = (1, 3, 2, 5, 5, 6, 6)
    relabelled_path = nx.Graph()
    relabelled_path.add_nodes_from(range(7))
    relabelled_path.add_edges_from(((0, 1), (1, 2)))
    assert support_valid(supplied_implication)
    assert uncolourable(relabelled_path, supplied_implication)[0]
    assert not anchored_k4(relabelled_path, supplied_implication)
    assert forced_path_type(relabelled_path, supplied_implication) == "two_edge_path"

    print("VERIFIED")
    print("triangle_free_graphs=107")
    print("reduced_raw_patterns=9450")
    print("uncolourable_candidates=194706")
    print("colourable_states=816444")
    print("anchored_K4_uncolourable_states=194556")
    print("no_anchored_K4_assignments=150")
    print("no_anchored_K4_orbits=4")
    print("boundary_graphs=K2+5K1:60,P3+4K1:84,P4+3K1:6")
    print("forced_certificates=edge:114,two_edge_path:36")
    print("all_survivors_have_exactly_two_singletons_and_five_pairs=True")
    print("all_survivors_have_each_support_exactly_four=True")
    print("all_survivors_end_in_unit_conflict=True")
    print("trichotomy=colourable_OR_anchored_K4_OR_edge_with_independent_complement")
    print("counterexamples_to_trichotomy=0")


if __name__ == "__main__":
    main()
