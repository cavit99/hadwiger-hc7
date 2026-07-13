#!/usr/bin/env python3
"""Probe the pentakis-dodecahedron C5 patch for critical web behaviour."""

from __future__ import annotations

import itertools


FACES = [
    [0, 1, 4, 7, 2],
    [0, 2, 6, 9, 3],
    [0, 3, 8, 5, 1],
    [1, 5, 11, 10, 4],
    [2, 7, 13, 12, 6],
    [3, 9, 15, 14, 8],
    [4, 10, 16, 13, 7],
    [5, 8, 14, 17, 11],
    [6, 12, 18, 15, 9],
    [10, 11, 17, 19, 16],
    [12, 13, 16, 19, 18],
    [14, 15, 18, 19, 17],
]


def edge(x: int, y: int) -> tuple[int, int]:
    return (x, y) if x < y else (y, x)


EDGES: set[tuple[int, int]] = set()
for face in FACES:
    for i in range(5):
        EDGES.add(edge(face[i], face[(i + 1) % 5]))
for i, face in enumerate(FACES):
    center = 20 + i
    for x in face:
        EDGES.add(edge(center, x))

BOUNDARY = tuple(FACES[0])
V = tuple(range(32))
PATCH_V = tuple(x for x in V if x != 20)
PATCH_E = {e for e in EDGES if 20 not in e}
INTERNAL = tuple(x for x in PATCH_V if x not in BOUNDARY)


def normalized_boundary_words():
    words = []
    for word in itertools.product(range(4), repeat=5):
        if word[0] != 0:
            continue
        if any(word[i] == word[(i + 1) % 5] for i in range(5)):
            continue
        # Restricted-growth normalization under color permutations.
        seen: list[int] = []
        normalized = []
        for c in word:
            if c not in seen:
                seen.append(c)
            normalized.append(seen.index(c))
        if tuple(normalized) == word:
            words.append(word)
    return words


def extends(
    word: tuple[int, ...],
    *,
    deleted_vertex: int | None = None,
    deleted_edge: tuple[int, int] | None = None,
    contracted_edge: tuple[int, int] | None = None,
) -> bool:
    vertices = [x for x in PATCH_V if x != deleted_vertex]
    edges = set(PATCH_E)
    if deleted_edge:
        edges.discard(deleted_edge)
    if contracted_edge:
        edges.discard(contracted_edge)
    color = {x: word[i] for i, x in enumerate(BOUNDARY)}

    def compatible(x: int, c: int) -> bool:
        if contracted_edge and x in contracted_edge:
            y = contracted_edge[0] if x == contracted_edge[1] else contracted_edge[1]
            if y in color and color[y] != c:
                return False
        return all(color.get(y) != c for y in vertices if edge(x, y) in edges)

    def dfs(left: list[int]) -> bool:
        if not left:
            return contracted_edge is None or color[contracted_edge[0]] == color[contracted_edge[1]]
        x = max(
            left,
            key=lambda z: (
                len({color[y] for y in vertices if y in color and edge(z, y) in edges}),
                sum(edge(z, y) in edges for y in vertices),
            ),
        )
        rest = [y for y in left if y != x]
        if contracted_edge and x in contracted_edge:
            y = contracted_edge[0] if x == contracted_edge[1] else contracted_edge[1]
            choices = [color[y]] if y in color else range(4)
        else:
            choices = range(4)
        for c in choices:
            if compatible(x, c):
                color[x] = c
                if dfs(rest):
                    return True
                del color[x]
        return False

    return dfs([x for x in vertices if x not in color])


def connected_after_delete(deleted: set[int]) -> bool:
    left = set(V) - deleted
    if not left:
        return True
    seen = {next(iter(left))}
    stack = list(seen)
    while stack:
        x = stack.pop()
        for y in left:
            if y not in seen and edge(x, y) in EDGES:
                seen.add(y)
                stack.append(y)
    return seen == left


def main() -> None:
    assert len(EDGES) == 90 and len(PATCH_E) == 85
    for k in range(5):
        for deleted in itertools.combinations(V, k):
            assert connected_after_delete(set(deleted))
    print("pentakis triangulation verified 5-connected")

    words = normalized_boundary_words()
    base = {w for w in words if extends(w)}
    print("boundary words", len(words), "extend", sorted(base), "fail", sorted(set(words) - base))

    preserving = []
    for e in sorted(e for e in PATCH_E if e[0] in INTERNAL and e[1] in INTERNAL):
        de = {w for w in words if extends(w, deleted_edge=e)}
        ce = {w for w in words if extends(w, contracted_edge=e)}
        if de == base:
            preserving.append(("delete-edge", e))
        if ce == base:
            preserving.append(("contract-edge", e))
    for x in INTERNAL:
        ve = {w for w in words if extends(w, deleted_vertex=x)}
        if ve == base:
            preserving.append(("delete-vertex", x))
    print("extension-family-preserving internal operations", preserving[:30], "count", len(preserving))


if __name__ == "__main__":
    main()
