#!/usr/bin/env python3
"""Exhaustive verifier for three-palette list obstructions on <= 7 vertices.

The graph atlas in NetworkX contains one representative of every unlabelled
simple graph on at most seven vertices.  We retain the connected triangle-free
graphs and enumerate lists of size at least two from the fixed palette
{1,2,3}.  A critical instance is required to become colourable after

  * deleting any vertex,
  * deleting any edge, or
  * adding any one missing colour to any list.

Representatives are quotiented by graph automorphisms and palette
permutations.  The script also enumerates all residual (no-singleton)
uncolourable assignments on triangle-free graphs of order exactly seven and
checks the simple invariant that at most two vertices can have a full list.

Run from the repository root with

  PYTHONPATH=active/runtime/deps python3 \
      active/hc7_exact7_triangle_list_critical_verify.py
"""

from __future__ import annotations

from collections.abc import Iterable
from itertools import permutations, product

import networkx as nx


PAIR_OR_FULL = (0b011, 0b101, 0b110, 0b111)
PALETTE_PERMUTATIONS = tuple(permutations(range(3)))


def triangle_free(graph: nx.Graph) -> bool:
    return not any(nx.triangles(graph).values())


def colourable(graph: nx.Graph, lists: tuple[int, ...]) -> bool:
    """Exact backtracking test for a list colouring with colours 0,1,2."""

    order = sorted(
        graph,
        key=lambda vertex: (lists[vertex].bit_count(), -graph.degree[vertex]),
    )
    colour: dict[int, int] = {}

    def extend(position: int) -> bool:
        if position == len(order):
            return True
        vertex = order[position]
        forbidden = {colour[neighbour] for neighbour in graph[vertex] if neighbour in colour}
        for candidate in range(3):
            if lists[vertex] & (1 << candidate) and candidate not in forbidden:
                colour[vertex] = candidate
                if extend(position + 1):
                    return True
                del colour[vertex]
        return False

    return extend(0)


def remap_mask(mask: int, permutation: tuple[int, int, int]) -> int:
    image = 0
    for colour in range(3):
        if mask & (1 << colour):
            image |= 1 << permutation[colour]
    return image


def canonical_lists(graph: nx.Graph, lists: tuple[int, ...]) -> tuple[int, ...]:
    """Canonicalize a list assignment under Aut(graph) x Sym(3)."""

    best: tuple[int, ...] | None = None
    matcher = nx.algorithms.isomorphism.GraphMatcher(graph, graph)
    for automorphism in matcher.isomorphisms_iter():
        for palette_permutation in PALETTE_PERMUTATIONS:
            image = [0] * len(graph)
            for old_vertex, new_vertex in automorphism.items():
                image[new_vertex] = remap_mask(lists[old_vertex], palette_permutation)
            candidate = tuple(image)
            if best is None or candidate < best:
                best = candidate
    assert best is not None
    return best


def critical(graph: nx.Graph, lists: tuple[int, ...]) -> bool:
    if colourable(graph, lists):
        return False

    # Vertex-critical.
    for vertex in graph:
        smaller = graph.copy()
        smaller.remove_node(vertex)
        if not colourable(smaller, lists):
            return False

    # Edge-critical.
    for edge in graph.edges():
        smaller = graph.copy()
        smaller.remove_edge(*edge)
        if not colourable(smaller, lists):
            return False

    # Inclusion-maximal among uncolourable list assignments.
    for vertex, mask in enumerate(lists):
        for colour in range(3):
            if not mask & (1 << colour):
                enlarged = list(lists)
                enlarged[vertex] |= 1 << colour
                if not colourable(graph, tuple(enlarged)):
                    return False
    return True


def atlas_graphs(order: int | None = None) -> Iterable[nx.Graph]:
    for graph in nx.graph_atlas_g():
        if order is not None and len(graph) != order:
            continue
        if order is None and not 1 <= len(graph) <= 7:
            continue
        if nx.is_connected(graph) and triangle_free(graph):
            yield graph


def graph6(graph: nx.Graph) -> str:
    return nx.to_graph6_bytes(graph, header=False).strip().decode("ascii")


def find_critical_templates() -> list[tuple[str, tuple[int, ...]]]:
    templates: list[tuple[str, tuple[int, ...]]] = []
    for graph in atlas_graphs():
        representatives: set[tuple[int, ...]] = set()
        for lists in product(PAIR_OR_FULL, repeat=len(graph)):
            if critical(graph, lists):
                representatives.add(canonical_lists(graph, lists))
        for lists in sorted(representatives):
            templates.append((graph6(graph), lists))
    return templates


EXPECTED = [
    ("Dhc", (3, 3, 3, 3, 3)),
    ("ElEG", (3, 5, 6, 3, 5, 6)),
    ("FhCKG", (3, 3, 3, 3, 3, 3, 3)),
    ("F`EBW", (3, 5, 3, 5, 6, 6, 6)),
    ("Fh_gg", (3, 3, 5, 6, 5, 5, 3)),
    ("FhEK_", (3, 5, 5, 3, 6, 6, 3)),
    ("FXJGg", (3, 5, 3, 3, 6, 7, 3)),
    ("FpUK_", (7, 3, 3, 3, 3, 5, 5)),
    ("FlO[O", (7, 7, 3, 3, 3, 3, 3)),
    ("FhELO", (3, 5, 6, 3, 5, 6, 7)),
]


def residual_order_seven_statistics() -> tuple[int, int, int, int]:
    """Return graph count, raw count, orbit count, max full-list count."""

    graph_count = 0
    raw_count = 0
    orbit_count = 0
    maximum_full_lists = 0
    # The literal boundary graph itself need not be connected.  Critical
    # cores are connected, but this census intentionally includes all 107
    # triangle-free unlabelled graphs of order seven.
    for graph in nx.graph_atlas_g():
        if len(graph) != 7 or not triangle_free(graph):
            continue
        uncolourable: list[tuple[int, ...]] = []
        for lists in product(PAIR_OR_FULL, repeat=7):
            if not colourable(graph, lists):
                uncolourable.append(lists)
                maximum_full_lists = max(maximum_full_lists, lists.count(0b111))
        if uncolourable:
            graph_count += 1
            raw_count += len(uncolourable)
            orbit_count += len({canonical_lists(graph, lists) for lists in uncolourable})
    return graph_count, raw_count, orbit_count, maximum_full_lists


def format_lists(lists: tuple[int, ...]) -> str:
    names = {3: "12", 5: "13", 6: "23", 7: "123"}
    return " ".join(f"{vertex}:{names[mask]}" for vertex, mask in enumerate(lists))


def main() -> None:
    templates = find_critical_templates()
    assert templates == EXPECTED, (templates, EXPECTED)

    stats = residual_order_seven_statistics()
    assert stats == (34, 3294, 239, 2), stats

    print("VERIFIED")
    print("critical_templates=10")
    print("orders=5:1,6:1,7:8")
    for index, (encoding, lists) in enumerate(templates, start=1):
        graph = nx.from_graph6_bytes(encoding.encode("ascii"))
        edges = " ".join(f"{u}{v}" for u, v in sorted(graph.edges()))
        print(f"T{index}: graph6={encoding} edges={edges} lists={format_lists(lists)}")
    print("order7_uncolourable_graphs=34")
    print("order7_raw_residual_assignments=3294")
    print("order7_residual_orbits=239")
    print("maximum_full_lists_in_uncolourable_residual=2")


if __name__ == "__main__":
    main()
