#!/usr/bin/env python3
"""Verify the exact-seven bichromatic-path/full-subgraph barrier."""

from __future__ import annotations

from functools import lru_cache
from itertools import combinations


S = tuple(range(7))
A = ("a1", "a2", "c1", "c2")
B = ("b",)
VERTICES = S + A + B
INDEX = {vertex: index for index, vertex in enumerate(VERTICES)}
ALL = (1 << len(VERTICES)) - 1


def edge(left, right):
    return frozenset((left, right))


BASE_EDGES = {edge(i, (i + 1) % 7) for i in S}
BASE_EDGES.update((edge(0, 2), edge(1, 3)))
BASE_EDGES.update((edge("a1", "a2"), edge("a2", "c1"), edge("c1", "c2")))

CONTACTS = {
    "a1": {0, 1, 4, 5, 6},
    "a2": {2, 3, 4, 5},
    "c1": {0, 2, 5, 6},
    "c2": {1, 2, 3, 4, 5, 6},
    "b": set(S),
}
for vertex, contacts in CONTACTS.items():
    BASE_EDGES.update(edge(vertex, boundary) for boundary in contacts)

COLOUR = {
    0: 4,
    1: 0,
    2: 1,
    3: 4,
    4: 2,
    5: 4,
    6: 3,
    "a1": 1,
    "a2": 3,
    "c1": 2,
    "c2": 5,
    "b": 5,
}

SINGLETONS = frozenset((1, 2, 4, 6))
PATH = (4, "a2", "c1", 6)
FULL_PAIR = (frozenset(("a1", "a2")), frozenset(("c1", "c2")))


def adjacency(edges):
    rows = [0] * len(VERTICES)
    for pair in edges:
        if len(pair) != 2:
            raise RuntimeError("loop in edge set")
        left, right = tuple(pair)
        rows[INDEX[left]] |= 1 << INDEX[right]
        rows[INDEX[right]] |= 1 << INDEX[left]
    return tuple(rows)


def vertex_mask(vertices):
    result = 0
    for vertex in vertices:
        result |= 1 << INDEX[vertex]
    return result


def connected(mask, rows):
    if not mask:
        return False
    seen = mask & -mask
    frontier = seen
    while frontier:
        bit = frontier & -frontier
        frontier ^= bit
        new = rows[bit.bit_length() - 1] & mask & ~seen
        seen |= new
        frontier |= new
    return seen == mask


def neighbours(mask, rows):
    result = 0
    remaining = mask
    while remaining:
        bit = remaining & -remaining
        remaining ^= bit
        result |= rows[bit.bit_length() - 1]
    return result & ~mask


def connectivity_at_least(edges, order):
    rows = adjacency(edges)
    for size in range(order):
        for deleted in combinations(VERTICES, size):
            if not connected(ALL ^ vertex_mask(deleted), rows):
                return False
    return True


def has_spanning_k7_model(edges):
    """Search canonical spanning partitions into seven connected bags."""

    rows = adjacency(edges)

    @lru_cache(maxsize=None)
    def is_connected(mask):
        return connected(mask, rows)

    @lru_cache(maxsize=None)
    def open_neighbours(mask):
        return neighbours(mask, rows)

    def search(remaining, chosen, parts_left):
        if parts_left == 1:
            return is_connected(remaining) and all(
                open_neighbours(remaining) & part for part in chosen
            )
        if remaining.bit_count() < parts_left:
            return False

        pivot = remaining & -remaining
        part = remaining
        while part:
            rest = remaining ^ part
            if (
                part & pivot
                and rest.bit_count() >= parts_left - 1
                and is_connected(part)
                and all(open_neighbours(part) & old for old in chosen)
                and search(rest, chosen + (part,), parts_left - 1)
            ):
                return True
            part = (part - 1) & remaining
        return False

    return search(ALL, tuple(), 7)


def is_boundary_full(subset, edges):
    return all(any(edge(vertex, boundary) in edges for vertex in subset) for boundary in S)


def connected_subsets(vertices, edges):
    rows = adjacency(edges)
    vertices = tuple(vertices)
    for size in range(1, len(vertices) + 1):
        for subset in combinations(vertices, size):
            if connected(vertex_mask(subset), rows):
                yield frozenset(subset)


def has_singleton_triangle(edges):
    return any(
        all(edge(left, right) in edges for left, right in combinations(triple, 2))
        for triple in combinations(SINGLETONS, 3)
    )


def verify_base():
    if len(VERTICES) != 12 or len(BASE_EDGES) != 38:
        raise RuntimeError("wrong base order or size")
    if any(edge(left, right) in BASE_EDGES for left in A for right in B):
        raise RuntimeError("open shores are not anticomplete")
    if any(COLOUR[left] == COLOUR[right] for left, right in map(tuple, BASE_EDGES)):
        raise RuntimeError("displayed colouring is not proper")

    if frozenset((0, 3, 5)) != frozenset(v for v in S if COLOUR[v] == 4):
        raise RuntimeError("wrong non-singleton boundary block")
    if edge(4, 6) in BASE_EDGES or edge(1, 2) not in BASE_EDGES:
        raise RuntimeError("wrong demand-critical singleton pair")
    if has_singleton_triangle(BASE_EDGES):
        raise RuntimeError("singleton graph is not triangle-free")
    if 5 in {COLOUR[boundary] for boundary in S}:
        raise RuntimeError("sixth colour is not absent from the boundary")

    for left, right in zip(PATH, PATH[1:]):
        if edge(left, right) not in BASE_EDGES:
            raise RuntimeError("missing bichromatic path edge")
    if tuple(COLOUR[vertex] for vertex in PATH) != (2, 3, 2, 3):
        raise RuntimeError("wrong bichromatic path colours")

    rows = adjacency(BASE_EDGES)
    for part in FULL_PAIR:
        if not connected(vertex_mask(part), rows) or not is_boundary_full(part, BASE_EDGES):
            raise RuntimeError("selected subgraph is not connected and boundary-full")
    if not (neighbours(vertex_mask(FULL_PAIR[0]), rows) & vertex_mask(FULL_PAIR[1])):
        raise RuntimeError("selected subgraphs are not adjacent")

    full = [
        subset
        for subset in connected_subsets(A, BASE_EDGES)
        if is_boundary_full(subset, BASE_EDGES)
    ]
    minimal = [subset for subset in full if not any(other < subset for other in full)]
    if set(minimal) != set(FULL_PAIR):
        raise RuntimeError(f"unexpected minimal full subgraphs: {minimal}")
    if any(
        all(left.isdisjoint(right) for left, right in combinations(family, 2))
        for family in combinations(full, 3)
    ):
        raise RuntimeError("three disjoint boundary-full subgraphs exist")

    if not connectivity_at_least(BASE_EDGES, 6):
        raise RuntimeError("base graph is not six-connected")
    six_cut = frozenset((0, 2, 5, 6, "a2", "c2"))
    if connected(ALL ^ vertex_mask(six_cut), rows):
        raise RuntimeError("displayed six-cut does not disconnect")
    if has_spanning_k7_model(BASE_EDGES):
        raise RuntimeError("base graph unexpectedly has a K7 minor")


def admissible_edges():
    answer = []
    for left, right in combinations(VERTICES, 2):
        pair = edge(left, right)
        if pair in BASE_EDGES:
            continue
        if (left in A and right in B) or (right in A and left in B):
            continue
        if COLOUR[left] == COLOUR[right]:
            continue
        if pair == edge(4, 6):
            continue
        answer.append(pair)
    return tuple(answer)


def augmentation_census():
    candidates = admissible_edges()
    if len(candidates) != 17:
        raise RuntimeError(f"wrong number of admissible edges: {len(candidates)}")

    base_rows = adjacency(BASE_EDGES)
    low_vertices = {
        vertex
        for vertex in VERTICES
        if base_rows[INDEX[vertex]].bit_count() < 7
    }

    minimal_masks = []
    counts = {}
    for size in range(len(candidates) + 1):
        for indices in combinations(range(len(candidates)), size):
            mask = sum(1 << index for index in indices)
            if any(mask & old == old for old in minimal_masks):
                continue

            additions = tuple(candidates[index] for index in indices)
            covered = {
                vertex
                for pair in additions
                for vertex in pair
                if vertex in low_vertices
            }
            if covered != low_vertices:
                continue

            augmented = BASE_EDGES | set(additions)
            if has_singleton_triangle(augmented):
                continue
            if not connectivity_at_least(augmented, 7):
                continue

            minimal_masks.append(mask)
            counts[size] = counts.get(size, 0) + 1
            if not has_spanning_k7_model(augmented):
                raise RuntimeError(
                    "seven-connected K7-minor-free augmentation found: "
                    f"{sorted((tuple(pair) for pair in additions), key=str)}"
                )

    expected = {4: 2, 5: 66, 6: 89, 7: 8}
    if counts != expected or len(minimal_masks) != 165:
        raise RuntimeError(f"wrong augmentation census: {counts}")
    return counts


def main():
    verify_base()
    counts = augmentation_census()
    print("GREEN exact-seven bichromatic-path/full-subgraph barrier")
    print("base: vertices=12 edges=38 connectivity=6 K7_minor=no demand=3")
    print("augmentations: allowed_edges=17 minimal_7_connected=165 all_have_K7=yes")
    print(
        "augmentation_sizes:",
        " ".join(f"{size}:{counts[size]}" for size in sorted(counts)),
    )


if __name__ == "__main__":
    main()
