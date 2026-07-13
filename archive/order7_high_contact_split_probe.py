#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = ["networkx>=3.4"]
# ///
"""Exact high-contact split atlas for every sharp seven-boundary.

For every unlabelled seven-vertex boundary whose missing graph is nonsplit
and whose two-full-shore quotient is K7-negative, add a full helper h and
two adjacent split vertices x,y.  Each split vertex misses exactly one
boundary label.  The verifier simultaneously checks all 7*7 ordered defect
pairs with bit-parallel edge predicates and archives an explicit branch-set
partition for every positive instance.
"""

from __future__ import annotations

import itertools

import networkx as nx

import contact_order7_sixedge_web_probe as nine_vertex
from contact_order7_all_unlabelled_atlas import is_split
from contact_order7_five_edge_verify import PAIRS, edge_mask, verify_model
from k331_two_piece_contact_atlas import CANDIDATES, H, S, X, Y
from order7_induced_core_direct_atlas import canonical_orders


STATES = tuple(itertools.product(S, repeat=2))
ALL_STATES = (1 << len(STATES)) - 1


def edge_state_mask(edge: tuple[int, int], boundary_edges: set[tuple[int, int]]) -> int:
    """Return the 49-bit mask of defect pairs in which ``edge`` is present."""
    a, b = sorted(edge)
    if a in S and b in S:
        return ALL_STATES if (a, b) in boundary_edges else 0
    if (a, b) == (X, Y) or (a in S and b == H):
        return ALL_STATES
    if a in S and b == X:
        return sum(1 << i for i, (dx, _dy) in enumerate(STATES) if dx != a)
    if a in S and b == Y:
        return sum(1 << i for i, (_dx, dy) in enumerate(STATES) if dy != a)
    return 0


def state_edges(
    boundary_edges: set[tuple[int, int]], defect_x: int, defect_y: int
) -> set[tuple[int, int]]:
    edges = set(boundary_edges)
    edges.add((X, Y))
    edges.update((s, H) for s in S)
    edges.update((s, X) for s in S if s != defect_x)
    edges.update((s, Y) for s in S if s != defect_y)
    return {tuple(sorted(edge)) for edge in edges}


def connected(mask: int, adjacency: list[int]) -> bool:
    reached = mask & -mask
    while True:
        expanded = reached
        todo = reached
        while todo:
            low = todo & -todo
            todo ^= low
            expanded |= adjacency[low.bit_length() - 1] & mask
        if expanded == reached:
            return reached == mask
        reached = expanded


def cover_states(
    boundary_edges: set[tuple[int, int]],
) -> tuple[int, dict[int, tuple[int, ...]]]:
    edge_masks = {
        (a, b): edge_state_mask((a, b), boundary_edges)
        for a, b in itertools.combinations(range(10), 2)
    }
    adjacency_by_state: list[list[int]] = []
    for index in range(len(STATES)):
        adjacency = [0] * 10
        for (a, b), mask in edge_masks.items():
            if mask >> index & 1:
                adjacency[a] |= 1 << b
                adjacency[b] |= 1 << a
        adjacency_by_state.append(adjacency)

    connected_cache: dict[int, int] = {}
    adjacent_cache: dict[tuple[int, int], int] = {}

    def connected_states(bag: int) -> int:
        if bag not in connected_cache:
            connected_cache[bag] = sum(
                1 << i
                for i, adjacency in enumerate(adjacency_by_state)
                if connected(bag, adjacency)
            )
        return connected_cache[bag]

    def adjacent_states(first: int, second: int) -> int:
        key = (first, second) if first < second else (second, first)
        if key not in adjacent_cache:
            available = 0
            left = first
            while left:
                low_left = left & -left
                left ^= low_left
                a = low_left.bit_length() - 1
                right = second
                while right:
                    low_right = right & -right
                    right ^= low_right
                    b = low_right.bit_length() - 1
                    available |= edge_masks[tuple(sorted((a, b)))]
            adjacent_cache[key] = available
        return adjacent_cache[key]

    covered = 0
    witness: dict[int, tuple[int, ...]] = {}
    for bags in CANDIDATES:
        valid = ALL_STATES
        for bag in bags:
            valid &= connected_states(bag)
            if not valid:
                break
        if not valid:
            continue
        for i in range(7):
            for j in range(i):
                valid &= adjacent_states(bags[i], bags[j])
                if not valid:
                    break
            if not valid:
                break
        new = valid & ~covered
        while new:
            low = new & -new
            index = low.bit_length() - 1
            witness[index] = bags
            new ^= low
        covered |= valid
        if covered == ALL_STATES:
            break
    return covered, witness


def main() -> None:
    boundaries = 0
    verified_models = 0
    failures: list[tuple[int, tuple[int, int]]] = []
    compatible_crossings = 0
    crossing_failures: list[
        tuple[int, tuple[int, ...], tuple[int, int], tuple[int, int], tuple[int, int]]
    ] = []
    for atlas_index, raw in enumerate(nx.graph_atlas_g()):
        if raw.number_of_nodes() != 7:
            continue
        boundary = nx.convert_node_labels_to_integers(raw)
        missing = nx.complement(boundary)
        if is_split(missing):
            continue
        missing_mask = edge_mask(tuple(sorted(edge)) for edge in missing.edges())
        if nine_vertex.quotient_model(missing_mask) is not None:
            continue

        boundaries += 1
        boundary_edges = {tuple(sorted(edge)) for edge in boundary.edges()}
        covered, witness = cover_states(boundary_edges)
        for index, defects in enumerate(STATES):
            if not (covered >> index & 1):
                failures.append((atlas_index, defects))
                continue
            bags = tuple(
                tuple(v for v in range(10) if mask >> v & 1)
                for mask in witness[index]
            )
            verify_model(state_edges(boundary_edges, *defects), bags)
            verified_models += 1

        # A real split extends an alternating crossing, so its omitted roots
        # cannot be one of the two prescribed contacts on the corresponding
        # carrier.  Test this extra geometric information for every cyclic
        # hull, not merely for a conveniently selected one.
        for size in range(4, 8):
            for cyclic_vertices in itertools.combinations(S, size):
                omitted = tuple(s for s in S if s not in cyclic_vertices)
                if not nx.is_bipartite(boundary.subgraph(omitted)):
                    continue
                for order in canonical_orders(cyclic_vertices, boundary_edges):
                    for i, r, j, s in itertools.combinations(range(size), 4):
                        first = (order[i], order[j])
                        second = (order[r], order[s])
                        for left, right in ((first, second), (second, first)):
                            for index, (dx, dy) in enumerate(STATES):
                                if dx in left or dy in right:
                                    continue
                                compatible_crossings += 1
                                if not (covered >> index & 1):
                                    crossing_failures.append(
                                        (atlas_index, order, left, right, (dx, dy))
                                    )

    print("surviving nonsplit boundaries", boundaries)
    print("high-contact split quotients", boundaries * len(STATES))
    print("verified K7 models", verified_models)
    print("negative quotients", len(failures))
    print("crossing-compatible high-contact quotients", compatible_crossings)
    print("crossing-compatible negative quotients", len(crossing_failures))
    for failure in failures[:20]:
        print("failure", failure)
    for failure in crossing_failures[:20]:
        print("crossing failure", failure)


if __name__ == "__main__":
    main()
