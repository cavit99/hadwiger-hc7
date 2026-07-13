#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = ["networkx"]
# ///

"""Probe a Helly-type portal-split conjecture on small 3-connected graphs.

For roots a,z and four portal sets P_i of size at least two, test whether
there is a connected bipartition separating a,z and splitting every P_i.
The program searches NetworkX's graph atlas for the first counterexample.
"""

from __future__ import annotations

from itertools import combinations

import networkx as nx


def connected_cut_masks(graph: nx.Graph, a: int, z: int) -> list[int]:
    """Return a-side masks for connected a-z bipartitions."""
    vertices = tuple(graph.nodes())
    bit = {v: 1 << i for i, v in enumerate(vertices)}
    full = (1 << len(vertices)) - 1
    cuts: list[int] = []
    for mask in range(1 << len(vertices)):
        if not (mask & bit[a]) or mask & bit[z]:
            continue
        other = full ^ mask
        left = [v for v in vertices if mask & bit[v]]
        right = [v for v in vertices if other & bit[v]]
        if nx.is_connected(graph.subgraph(left)) and nx.is_connected(graph.subgraph(right)):
            cuts.append(mask)
    return cuts


def portal_split_bits(portal: int, cuts: list[int], full: int) -> int:
    """Encode the connected cuts which split a portal set."""
    result = 0
    for index, cut in enumerate(cuts):
        if portal & cut and portal & (full ^ cut):
            result |= 1 << index
    return result


def hit_by_two(portals: list[int], full: int) -> bool:
    """Return whether at most two vertices meet all four portal sets."""
    vertices = [1 << index for index in range(full.bit_length())]
    candidates = vertices + [left | right for left, right in combinations(vertices, 2)]
    return any(all(candidate & portal for portal in portals) for candidate in candidates)


def find_four_empty_intersection(
    split_bits: list[int],
    portals: list[int],
    full: int,
    graph: nx.Graph,
    roots: tuple[int, int],
) -> tuple[int, int, int, int] | None:
    """Find a 3-transversal Helly failure with no rooted K6 rerouting."""
    size = len(split_bits)
    for i in range(size):
        first = split_bits[i]
        for j in range(i, size):
            second = first & split_bits[j]
            for k in range(j, size):
                third = second & split_bits[k]
                for ell in range(k, size):
                    selected = [portals[index] for index in (i, j, k, ell)]
                    if (
                        third & split_bits[ell] == 0
                        and not hit_by_two(selected, full)
                        and rooted_clique_model(graph, roots, selected) is None
                    ):
                        return i, j, k, ell
    return None


def rooted_clique_model(
    bag: nx.Graph,
    roots: tuple[int, int],
    portals: list[int],
) -> list[list[int]] | None:
    """Find a K6 model rooted at a,z and four new terminal vertices."""
    quotient = bag.copy()
    offset = len(bag)
    terminals = list(range(offset, offset + 4))
    quotient.add_nodes_from(terminals)
    quotient.add_edges_from(combinations(terminals, 2))
    for terminal, portal in zip(terminals, portals, strict=True):
        quotient.add_edges_from(
            (terminal, vertex)
            for vertex in bag.nodes()
            if portal & (1 << vertex)
        )
    designated = [roots[0], roots[1], *terminals]
    extras = [vertex for vertex in bag.nodes() if vertex not in roots]
    # Each extra is unused (0) or assigned to one of six rooted bags (1..6).
    for code in range(7 ** len(extras)):
        branch_sets = [{root} for root in designated]
        value = code
        for vertex in extras:
            choice = value % 7
            value //= 7
            if choice:
                branch_sets[choice - 1].add(vertex)
        if not all(nx.is_connected(quotient.subgraph(branch)) for branch in branch_sets):
            continue
        if all(
            any(quotient.has_edge(u, v) for u in first for v in second)
            for first, second in combinations(branch_sets, 2)
        ):
            return [sorted(branch) for branch in branch_sets]
    return None


def main() -> None:
    atlas = [
        nx.convert_node_labels_to_integers(graph)
        for graph in nx.graph_atlas_g()
        if (
            5 <= len(graph) <= 7
            and nx.node_connectivity(graph) >= 4
            and not nx.check_planarity(graph)[0]
        )
    ]
    checked = 0
    for graph in atlas:
        vertices = tuple(graph.nodes())
        full = (1 << len(vertices)) - 1
        for a, z in combinations(vertices, 2):
            root_mask = (1 << a) | (1 << z)
            portals = [
                mask
                for mask in range(1, full + 1)
                if (mask & ~root_mask).bit_count() >= 2
            ]
            cuts = connected_cut_masks(graph, a, z)
            bits = [portal_split_bits(portal, cuts, full) for portal in portals]
            witness = find_four_empty_intersection(bits, portals, full, graph, (a, z))
            checked += 1
            if witness is None:
                continue
            selected = [portals[index] for index in witness]
            print("COUNTEREXAMPLE")
            print(f"n={len(vertices)} edges={sorted(graph.edges())} roots={(a, z)}")
            print(
                "portals=",
                [[v for v in vertices if mask & (1 << v)] for mask in selected],
            )
            print("rooted_K6_model=", rooted_clique_model(graph, (a, z), selected))
            print(f"connected_cuts={len(cuts)} checked_rooted_graphs={checked}")
            return
    print(f"NO_COUNTEREXAMPLE checked_rooted_graphs={checked} atlas_graphs={len(atlas)}")


if __name__ == "__main__":
    main()
