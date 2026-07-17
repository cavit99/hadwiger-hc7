#!/usr/bin/env python3
"""Exact checks for the paired-colourful planar-core barrier.

Requires NetworkX 3.x.  The two complete-minor checks deliberately use
different exhaustive encodings:

1. a clique search over all connected vertex subsets; and
2. canonical assignments of vertices to six branch sets or an unused set.

Neither search imposes a bound on branch-set size.
"""

from __future__ import annotations

import itertools

import networkx as nx


R_GRAPH6 = b"HEhutxm"
S = frozenset({0, 3, 5, 7})
T = frozenset({0, 4, 6, 8})
Z = 9
U = 10


def proper_colourings(g: nx.Graph, k: int):
    """Generate every labelled proper k-colouring as a vertex dictionary."""
    order = sorted(g, key=lambda v: (-g.degree(v), v))
    colour: dict[int, int] = {}

    def search(i: int):
        if i == len(order):
            yield dict(colour)
            return
        v = order[i]
        forbidden = {colour[w] for w in g[v] if w in colour}
        for value in range(k):
            if value not in forbidden:
                colour[v] = value
                yield from search(i + 1)
                del colour[v]

    yield from search(0)


def is_k_colourable(g: nx.Graph, k: int) -> bool:
    return next(proper_colourings(g, k), None) is not None


def canonical_partition(colouring: dict[int, int]) -> tuple[tuple[int, ...], ...]:
    blocks = []
    for value in sorted(set(colouring.values())):
        blocks.append(tuple(sorted(v for v, c in colouring.items() if c == value)))
    return tuple(sorted(blocks))


def connected_masks(g: nx.Graph) -> list[int]:
    vertices = sorted(g)
    assert vertices == list(range(len(vertices)))
    masks = []
    for mask in range(1, 1 << len(vertices)):
        subset = [v for v in vertices if mask & (1 << v)]
        if nx.is_connected(g.subgraph(subset)):
            masks.append(mask)
    return masks


def masks_adjacent(g: nx.Graph, a: int, b: int) -> bool:
    for v, w in g.edges():
        if ((a >> v) & 1 and (b >> w) & 1) or ((a >> w) & 1 and (b >> v) & 1):
            return True
    return False


def clique_minor_by_connected_subsets(g: nx.Graph, order: int):
    """Return an exact K_order model, or None, by connected-subset search."""
    candidates = connected_masks(g)
    compatible: list[set[int]] = [set() for _ in candidates]
    for i, a in enumerate(candidates):
        for j in range(i + 1, len(candidates)):
            b = candidates[j]
            if not (a & b) and masks_adjacent(g, a, b):
                compatible[i].add(j)

    def search(chosen: list[int], allowed: set[int]):
        if len(chosen) == order:
            return chosen
        if len(chosen) + len(allowed) < order:
            return None
        while allowed:
            i = min(allowed)
            allowed = allowed - {i}
            result = search(chosen + [i], allowed & compatible[i])
            if result is not None:
                return result
        return None

    indices = search([], set(range(len(candidates))))
    if indices is None:
        return None
    return [candidates[i] for i in indices]


def clique_minor_by_canonical_assignments(g: nx.Graph, order: int):
    """Independent exact search over branch-set/unused assignments.

    Branch-set labels are introduced in first-occurrence order, so every
    unordered collection of branch sets is tested once.  Label -1 denotes
    the unused vertices.
    """
    n = len(g)
    assert sorted(g) == list(range(n))

    # This implementation intentionally does not call connected_masks() or
    # masks_adjacent(), which are the primitives of the first encoding.
    vertex_neighbours = [0] * n
    for v, w in g.edges():
        vertex_neighbours[v] |= 1 << w
        vertex_neighbours[w] |= 1 << v

    def bit_connected(mask: int) -> bool:
        reached = mask & -mask
        while True:
            frontier = 0
            bits = reached
            while bits:
                bit = bits & -bits
                bits ^= bit
                frontier |= vertex_neighbours[bit.bit_length() - 1]
            enlarged = reached | (frontier & mask)
            if enlarged == reached:
                return reached == mask
            reached = enlarged

    is_connected = [False] * (1 << n)
    neighbour_union = [0] * (1 << n)
    for a in range(1, 1 << n):
        is_connected[a] = bit_connected(a)
        bit = a & -a
        rest = a ^ bit
        neighbour_union[a] = (
            neighbour_union[rest] | vertex_neighbours[bit.bit_length() - 1]
        )

    bags: list[int] = []

    def search(v: int):
        if v == n:
            if len(bags) != order:
                return None
            if not all(is_connected[bag] for bag in bags):
                return None
            if not all(neighbour_union[bags[i]] & bags[j]
                       for i in range(order) for j in range(i + 1, order)):
                return None
            return list(bags)

        remaining_after = n - v - 1

        # Leave v unused.
        result = search(v + 1)
        if result is not None:
            return result

        # Put v into an existing canonically labelled bag.
        for i in range(len(bags)):
            bags[i] |= 1 << v
            result = search(v + 1)
            bags[i] ^= 1 << v
            if result is not None:
                return result

        # Introduce the next label.  Prune if the remaining vertices cannot
        # create all still-missing nonempty bags.
        if len(bags) < order and remaining_after >= order - len(bags) - 1:
            bags.append(1 << v)
            result = search(v + 1)
            bags.pop()
            if result is not None:
                return result
        return None

    return search(0)


def colourful_clique_minor(g: nx.Graph, first: set[int] | frozenset[int],
                           second: set[int] | frozenset[int], order: int):
    """Exact connected-subset search for a minor meeting both sets per bag."""
    first_mask = sum(1 << v for v in first)
    second_mask = sum(1 << v for v in second)
    candidates = [mask for mask in connected_masks(g)
                  if mask & first_mask and mask & second_mask]
    compatible: list[set[int]] = [set() for _ in candidates]
    for i, a in enumerate(candidates):
        for j in range(i + 1, len(candidates)):
            b = candidates[j]
            if not (a & b) and masks_adjacent(g, a, b):
                compatible[i].add(j)

    def search(chosen: list[int], allowed: set[int]):
        if len(chosen) == order:
            return chosen
        if len(chosen) + len(allowed) < order:
            return None
        while allowed:
            i = min(allowed)
            allowed = allowed - {i}
            result = search(chosen + [i], allowed & compatible[i])
            if result is not None:
                return result
        return None

    result = search([], set(range(len(candidates))))
    return None if result is None else [candidates[i] for i in result]


def build_graphs() -> tuple[nx.Graph, nx.Graph]:
    r = nx.from_graph6_bytes(R_GRAPH6)
    q = r.copy()
    q.add_edges_from((Z, s) for s in S)
    q.add_edges_from((U, t) for t in T)
    q.add_edge(Z, U)
    return r, q


def main() -> None:
    r, q = build_graphs()

    expected_edges = {
        (0, 3), (0, 4), (0, 6), (0, 7),
        (1, 3), (1, 5), (1, 6), (1, 8),
        (2, 4), (2, 5), (2, 7), (2, 8),
        (3, 5), (3, 6), (3, 7),
        (4, 6), (4, 7), (4, 8),
        (5, 7), (5, 8), (6, 8),
    }
    assert {tuple(sorted(edge)) for edge in r.edges()} == expected_edges
    assert len(r) == 9 and r.number_of_edges() == 21
    assert nx.check_planarity(r)[0]
    assert nx.node_connectivity(r) == 4

    colourings = list(proper_colourings(r, 4))
    assert len(colourings) == 48
    partitions = {canonical_partition(c) for c in colourings}
    assert partitions == {
        ((0, 1, 2), (3, 4), (5, 6), (7, 8)),
        ((0, 1, 2), (3, 8), (4, 5), (6, 7)),
    }
    assert not is_k_colourable(r, 3)
    assert all({c[v] for v in S} == set(range(4)) for c in colourings)
    assert all({c[v] for v in T} == set(range(4)) for c in colourings)
    assert colourful_clique_minor(r, S, T, 4) is None

    assert not is_k_colourable(q, 4)
    assert is_k_colourable(q, 5)

    # Positive controls for both complete-minor encodings.
    k6 = nx.complete_graph(6)
    assert clique_minor_by_connected_subsets(k6, 6) is not None
    assert clique_minor_by_canonical_assignments(k6, 6) is not None

    # Two independent exhaustive checks of the computer-assisted claim.
    assert clique_minor_by_connected_subsets(q, 6) is None
    assert clique_minor_by_canonical_assignments(q, 6) is None

    print("PASS graph6=HEhutxm")
    print("PASS R: planar, kappa=4, chi=4, labelled_4_colourings=48")
    print("PASS S,T: colourful; no paired K4 minor")
    print("PASS Q: chi=5; no K6 minor (two exact exhaustive encodings)")


if __name__ == "__main__":
    main()
