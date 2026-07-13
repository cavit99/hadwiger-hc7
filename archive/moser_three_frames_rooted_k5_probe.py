#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = ["networkx"]
# ///
"""Falsify the claim that three linked Moser frames force a rooted K5.

The five roots induce the complement of a missing C5.  Each root has one
portal in a three-connected shore D.  The probe enumerates small unlabelled
shores and all portal maps, then compares the number of linked disjoint-edge
frames with existence of a rooted K5 model.  A found example only refutes the
bare linkage implication; it need not satisfy the full HC7 relative-cut or
minor-transition axioms.
"""

from __future__ import annotations

from itertools import product

import networkx as nx


ROOTS = tuple(range(5))
MISSING = {tuple(sorted((i, (i + 1) % 5))) for i in ROOTS}
PRESENT = {
    tuple(sorted(edge))
    for edge in nx.complete_graph(5).edges()
    if tuple(sorted(edge)) not in MISSING
}
FRAMES = tuple(
    (first, second)
    for first in sorted(MISSING)
    for second in sorted(MISSING)
    if first < second and set(first).isdisjoint(second)
)


def connected_masks(graph: nx.Graph) -> list[int]:
    """Return all nonempty connected vertex masks of a 0-indexed graph."""
    order = graph.number_of_nodes()
    adjacency = [sum(1 << w for w in graph.neighbors(v)) for v in range(order)]
    masks: list[int] = []
    for mask in range(1, 1 << order):
        reached = mask & -mask
        frontier = reached
        while frontier:
            bit = frontier & -frontier
            frontier ^= bit
            vertex = bit.bit_length() - 1
            new = adjacency[vertex] & mask & ~reached
            reached |= new
            frontier |= new
        if reached == mask:
            masks.append(mask)
    return masks


def linked_frames(graph: nx.Graph, portals: tuple[int, ...]) -> list[int]:
    """List frame indices admitting two disjoint connected portal carriers."""
    masks = connected_masks(graph)
    answer: list[int] = []
    for index, (first, second) in enumerate(FRAMES):
        first_need = (1 << portals[first[0]]) | (1 << portals[first[1]])
        second_need = (1 << portals[second[0]]) | (1 << portals[second[1]])
        first_carriers = [mask for mask in masks if mask & first_need == first_need]
        second_carriers = [mask for mask in masks if mask & second_need == second_need]
        if any(not left & right for left in first_carriers for right in second_carriers):
            answer.append(index)
    return answer


def full_relative_cut(graph: nx.Graph, portals: tuple[int, ...]) -> bool:
    """Check phi(X)>=7 when the two extra labels a,w see all of D."""
    order = graph.number_of_nodes()
    for mask in range(1, (1 << order) - 1):
        inside = {vertex for vertex in range(order) if mask >> vertex & 1}
        shore_boundary = {
            neighbour
            for vertex in inside
            for neighbour in graph.neighbors(vertex)
            if neighbour not in inside
        }
        root_contacts = sum(portals[root] in inside for root in ROOTS)
        if len(shore_boundary) + root_contacts + 2 < 7:
            return False
    return True


def rooted_k5(graph: nx.Graph, portals: tuple[int, ...]) -> tuple[int, ...] | None:
    """Find a rooted K5 model in D plus the fixed five-root graph."""
    order = graph.number_of_nodes()
    # -1 means unused; 0,...,4 assigns a shore vertex to that root bag.
    for allocation in product(range(-1, 5), repeat=order):
        bags = [{root} for root in ROOTS]
        for vertex, bag in enumerate(allocation):
            if bag >= 0:
                bags[bag].add(5 + vertex)

        whole = nx.Graph()
        whole.add_nodes_from(range(5 + order))
        whole.add_edges_from(PRESENT)
        whole.add_edges_from((5 + x, 5 + y) for x, y in graph.edges())
        whole.add_edges_from((root, 5 + portals[root]) for root in ROOTS)

        if any(not nx.is_connected(whole.subgraph(bag)) for bag in bags):
            continue
        if all(
            any(whole.has_edge(x, y) for x in bags[i] for y in bags[j])
            for i in ROOTS
            for j in range(i)
        ):
            return tuple(allocation)
    return None


def main() -> None:
    atlas = nx.graph_atlas_g()
    checked = 0
    for order in range(6, 8):
        shores = [
            nx.convert_node_labels_to_integers(graph)
            for graph in atlas
            if graph.number_of_nodes() == order and nx.node_connectivity(graph) >= 3
        ]
        for shore in shores:
            for portals in product(range(order), repeat=5):
                if not full_relative_cut(shore, portals):
                    continue
                linked = linked_frames(shore, portals)
                if len(linked) < 3:
                    continue
                checked += 1
                if rooted_k5(shore, portals) is None:
                    print("COUNTEREXAMPLE")
                    print("shore_order", order)
                    print("shore_edges", sorted(tuple(sorted(edge)) for edge in shore.edges()))
                    print("portals", portals)
                    print("linked_frame_indices", linked)
                    print("frames", FRAMES)
                    print("checked_dense_cases", checked)
                    return
        print("finished_order", order, "three_linked_cases", checked, flush=True)
    print("NO_COUNTEREXAMPLE", checked)


if __name__ == "__main__":
    main()
