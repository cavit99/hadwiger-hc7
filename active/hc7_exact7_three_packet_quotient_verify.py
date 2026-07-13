#!/usr/bin/env python3
"""Exhaustively test the literal three-full-packet boundary quotient.

For a seven-vertex boundary H, adjoin three pairwise nonadjacent vertices,
each complete to H.  These vertices represent the three disjoint S-full
packets available in an exact `(1,2)` adhesion.  Every clique-minor model
in this ten-vertex quotient lifts literally by replacing a packet vertex
with its connected full packet.

The verifier enumerates all set partitions of the ten quotient vertices
into seven nonempty branch sets.  It is therefore an exact K7-minor test,
not merely the two-anchor sufficient construction.
"""

from __future__ import annotations

from collections import Counter

import networkx as nx

from hc7_exact7_adaptive_12_packet_quotient_probe import (
    certified_packet_k7,
    has_clique_minor,
    omega,
    robust_independent_block,
)


BOUNDARY_ORDER = 7
ORDER = 10
PACKETS = range(7, 10)


def set_partitions_masks(order: int, blocks: int):
    """Yield canonical unordered partitions as tuples of nonzero masks."""

    assignment = [0] * order

    def visit(vertex: int, used: int):
        if vertex == order:
            if used == blocks:
                masks = [0] * blocks
                for item, label in enumerate(assignment):
                    masks[label] |= 1 << item
                yield tuple(masks)
            return

        # Existing labels and, canonically, at most one new label.
        for label in range(min(used + 1, blocks)):
            assignment[vertex] = label
            yield from visit(vertex + 1, max(used, label + 1))

    assignment[0] = 0
    yield from visit(1, 1)


PARTITIONS = tuple(set_partitions_masks(ORDER, 7))
assert len(PARTITIONS) == 5880


def quotient_adjacency(
    boundary: nx.Graph, *, adjacent_rich_packets: bool = False
) -> tuple[int, ...]:
    adjacency = [0] * ORDER
    for left, right in boundary.edges():
        adjacency[left] |= 1 << right
        adjacency[right] |= 1 << left
    boundary_mask = (1 << BOUNDARY_ORDER) - 1
    for packet in PACKETS:
        adjacency[packet] = boundary_mask
        for vertex in range(BOUNDARY_ORDER):
            adjacency[vertex] |= 1 << packet
    if adjacent_rich_packets:
        # P2 and P3 represent the two packets in the same rich open shore.
        adjacency[8] |= 1 << 9
        adjacency[9] |= 1 << 8
    return tuple(adjacency)


def connected(mask: int, adjacency: tuple[int, ...]) -> bool:
    reached = mask & -mask
    frontier = reached
    while frontier:
        bit = frontier & -frontier
        frontier ^= bit
        vertex = bit.bit_length() - 1
        new = adjacency[vertex] & mask & ~reached
        reached |= new
        frontier |= new
    return reached == mask


def adjacent(left: int, right: int, adjacency: tuple[int, ...]) -> bool:
    scan = left
    while scan:
        bit = scan & -scan
        scan ^= bit
        vertex = bit.bit_length() - 1
        if adjacency[vertex] & right:
            return True
    return False


def k7_model(
    boundary: nx.Graph, *, adjacent_rich_packets: bool = False
) -> tuple[int, ...] | None:
    adjacency = quotient_adjacency(
        boundary, adjacent_rich_packets=adjacent_rich_packets
    )
    connected_cache: dict[int, bool] = {}
    for partition in PARTITIONS:
        if not all(
            connected_cache.setdefault(mask, connected(mask, adjacency))
            for mask in partition
        ):
            continue
        if all(
            adjacent(partition[i], partition[j], adjacency)
            for i in range(7)
            for j in range(i + 1, 7)
        ):
            return partition
    return None


def format_mask(mask: int) -> tuple[str, ...]:
    return tuple(
        f"s{vertex}" if vertex < 7 else f"P{vertex - 6}"
        for vertex in range(ORDER)
        if mask >> vertex & 1
    )


def main() -> None:
    graphs = [
        graph
        for graph in nx.graph_atlas_g()
        if len(graph) == 7 and omega(graph) <= 3
    ]
    counts = Counter()
    connected_rich_counts = Counter()
    residual = []
    examples = {}
    equivalence_checks = 0
    for index, graph in enumerate(graphs):
        robust = robust_independent_block(graph) is not None
        model = k7_model(graph)
        connected_rich_model = k7_model(graph, adjacent_rich_packets=True)
        two_anchor = certified_packet_k7(graph)
        one_anchor = any(
            has_clique_minor(
                graph.subgraph(set(range(BOUNDARY_ORDER)) - {vertex}), 4
            )
            for vertex in range(BOUNDARY_ORDER)
        )
        assert (model is not None) == two_anchor
        assert (connected_rich_model is not None) == one_anchor
        equivalence_checks += 2
        counts[(robust, model is not None)] += 1
        connected_rich_counts[(robust, connected_rich_model is not None)] += 1
        if model is not None and "model" not in examples:
            examples["model"] = (index, model)
        if not robust and model is None:
            residual.append((index, graph))

    print("EXACT THREE-PACKET QUOTIENT VERIFIER")
    print(f"branch_partitions={len(PARTITIONS)}")
    print(f"k4_free_boundaries={len(graphs)}")
    print(f"anchor_equivalence_checks={equivalence_checks}")
    for key, count in sorted(counts.items()):
        print(f"robust={key[0]} quotient_k7={key[1]} count={count}")
    print(f"closed_by_robust_or_exact_quotient={len(graphs)-len(residual)}")
    print(f"residual={len(residual)}")
    print("adjacent_rich_packet_counts:")
    for key, count in sorted(connected_rich_counts.items()):
        print(f"  robust={key[0]} quotient_k7={key[1]} count={count}")
    if "model" in examples:
        index, model = examples["model"]
        print(f"first_model_graph_index={index}")
        print(f"first_model={tuple(format_mask(mask) for mask in model)}")
    print("residual_by_alpha_edges:")
    profile = Counter(
        (omega(nx.complement(graph)), graph.number_of_edges())
        for _, graph in residual
    )
    for key, count in sorted(profile.items()):
        print(f"  {key}: {count}")


if __name__ == "__main__":
    main()
