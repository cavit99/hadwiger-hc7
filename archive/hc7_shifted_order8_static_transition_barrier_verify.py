#!/usr/bin/env python3
"""Verify the shifted order-eight static transition barrier."""

from __future__ import annotations

from itertools import combinations


NAMES = ("v", "x", "r1", "r2", "a", "b", "c", "d", "s", "u1", "u2", "p", "q")
INDEX = {name: index for index, name in enumerate(NAMES)}
T = tuple(range(8))
L = (INDEX["s"], INDEX["u1"], INDEX["u2"])
R = (INDEX["p"], INDEX["q"])


def edge(left: str | int, right: str | int) -> tuple[int, int]:
    if isinstance(left, str):
        left = INDEX[left]
    if isinstance(right, str):
        right = INDEX[right]
    return tuple(sorted((left, right)))


EDGES: set[tuple[int, int]] = set()


def add(left: str | int, right: str | int) -> None:
    EDGES.add(edge(left, right))


for pair in (
    ("r1", "r2"),
    ("r1", "b"),
    ("b", "a"),
    ("a", "r2"),
    ("r1", "d"),
    ("d", "c"),
    ("c", "r2"),
    ("v", "a"),
    ("v", "r1"),
    ("v", "d"),
):
    add(*pair)

for terminal in T:
    add("s", terminal)

add("s", "u1")
add("u1", "u2")
for root in ("u1", "u2"):
    for terminal in ("a", "r1", "d"):
        add(root, terminal)

add("p", "q")
for terminal in ("v", "x", "r1", "c", "d"):
    add("p", terminal)
for terminal in ("r1", "r2", "a", "b", "c"):
    add("q", terminal)


def neighbours(vertex: int, vertices: set[int], edges: set[tuple[int, int]]) -> set[int]:
    return {
        other
        for other in vertices
        if other != vertex and edge(vertex, other) in edges
    }


def connected(vertices: set[int], edges: set[tuple[int, int]]) -> bool:
    if not vertices:
        return False
    reached = {next(iter(vertices))}
    while True:
        enlarged = reached | {
            other
            for vertex in reached
            for other in neighbours(vertex, vertices, edges)
        }
        if enlarged == reached:
            return reached == vertices
        reached = enlarged


def partitions(order: int):
    blocks: list[list[int]] = []

    def visit(vertex: int):
        if vertex == order:
            yield tuple(tuple(block) for block in blocks)
            return
        for block in blocks:
            block.append(vertex)
            yield from visit(vertex + 1)
            block.pop()
        blocks.append([vertex])
        yield from visit(vertex + 1)
        blocks.pop()

    yield from visit(0)


def contract_pq(edges: set[tuple[int, int]]) -> tuple[set[int], set[tuple[int, int]]]:
    p, q = R
    vertices = set(range(len(NAMES))) - {q}
    result: set[tuple[int, int]] = set()
    for left, right in edges:
        if {left, right} == {p, q}:
            continue
        new_left = p if left == q else left
        new_right = p if right == q else right
        if new_left != new_right:
            result.add(edge(new_left, new_right))
    return vertices, result


def extends(
    partition: tuple[tuple[int, ...], ...],
    vertices: set[int],
    edges: set[tuple[int, int]],
) -> bool:
    colours = {
        vertex: colour
        for colour, block in enumerate(partition)
        for vertex in block
    }
    if any(
        left in T and right in T and colours[left] == colours[right]
        for left, right in edges
    ):
        return False

    uncoloured = [vertex for vertex in vertices if vertex not in T]

    def search() -> bool:
        if not uncoloured:
            return True
        vertex = max(
            uncoloured,
            key=lambda item: (
                len(
                    {
                        colours[other]
                        for other in neighbours(item, vertices, edges)
                        if other in colours
                    }
                ),
                len(neighbours(item, vertices, edges)),
            ),
        )
        uncoloured.remove(vertex)
        forbidden = {
            colours[other]
            for other in neighbours(vertex, vertices, edges)
            if other in colours
        }
        for colour in range(6):
            if colour in forbidden:
                continue
            colours[vertex] = colour
            if search():
                uncoloured.append(vertex)
                return True
            del colours[vertex]
        uncoloured.append(vertex)
        return False

    return search()


def canonical(partition: tuple[tuple[int, ...], ...]) -> str:
    return "|".join("".join(NAMES[vertex] for vertex in block) for block in partition)


def main() -> None:
    all_vertices = set(range(len(NAMES)))

    assert connected(set(L), EDGES)
    assert connected(set(R), EDGES)
    assert not any(edge(left, right) in EDGES for left in L for right in R)
    assert all(any(edge(vertex, terminal) in EDGES for vertex in L) for terminal in T)
    assert all(any(edge(vertex, terminal) in EDGES for vertex in R) for terminal in T)

    model = (
        {INDEX["u1"]},
        {INDEX["u2"]},
        {INDEX["r1"]},
        {INDEX["d"]},
        {INDEX["v"], INDEX["a"]},
    )
    assert all(connected(branch, EDGES) for branch in model)
    assert all(
        any(edge(left, right) in EDGES for left in first for right in second)
        for first, second in combinations(model, 2)
    )

    assert not any(
        all(edge(left, right) in EDGES for left, right in combinations(clique, 2))
        for clique in combinations(all_vertices, 5)
    )

    bags = (
        {INDEX[name] for name in ("a", "c", "p", "q", "r1", "s")},
        {INDEX[name] for name in ("a", "c", "d", "p", "r1", "s")},
        {INDEX[name] for name in ("a", "c", "q", "r1", "r2", "s")},
        {INDEX[name] for name in ("a", "b", "q", "r1", "s")},
        {INDEX[name] for name in ("p", "s", "x")},
        {INDEX[name] for name in ("a", "d", "p", "r1", "s", "v")},
        {INDEX[name] for name in ("a", "d", "r1", "s", "u1")},
        {INDEX[name] for name in ("a", "d", "r1", "u1", "u2")},
    )
    tree_edges = ((0, 1), (0, 2), (0, 3), (0, 4), (1, 5), (1, 6), (6, 7))
    assert max(map(len, bags)) == 6
    assert all(any({left, right} <= bag for bag in bags) for left, right in EDGES)
    for vertex in all_vertices:
        containing = {index for index, bag in enumerate(bags) if vertex in bag}
        reached = {next(iter(containing))}
        while True:
            enlarged = reached | {
                right
                for left, right in tree_edges
                if left in reached and right in containing
            } | {
                left
                for left, right in tree_edges
                if right in reached and left in containing
            }
            if enlarged == reached:
                break
            reached = enlarged
        assert reached == containing

    proper = tuple(
        partition
        for partition in partitions(8)
        if len(partition) <= 6
        and not any(
            any(left in block and right in block for block in partition)
            for left, right in EDGES
            if left in T and right in T
        )
    )
    assert len(tuple(partitions(8))) == 4140
    assert len(tuple(partition for partition in partitions(8) if len(partition) <= 6)) == 4111

    full_language = {
        canonical(partition)
        for partition in proper
        if extends(partition, all_vertices, EDGES)
    }
    deleted_edge_language = {
        canonical(partition)
        for partition in proper
        if extends(partition, all_vertices, EDGES - {edge("p", "q")})
    }
    contracted_vertices, contracted_edges = contract_pq(EDGES)
    contracted_language = {
        canonical(partition)
        for partition in proper
        if extends(partition, contracted_vertices, contracted_edges)
    }
    deleted_component_vertices = all_vertices - set(R)
    deleted_component_edges = {
        pair for pair in EDGES if not (set(pair) & set(R))
    }
    deleted_component_language = {
        canonical(partition)
        for partition in proper
        if extends(partition, deleted_component_vertices, deleted_component_edges)
    }

    assert len(full_language) == 354
    assert len(deleted_edge_language) == 358
    assert contracted_language == deleted_edge_language
    assert deleted_component_language == deleted_edge_language

    expected_missing = {
        "vr2|xa|r1|bd|c",
        "vr2|xb|r1|ad|c",
        "vb|xr2|r1|ad|c",
        "vb|xa|r1|r2d|c",
    }
    assert deleted_edge_language - full_language == expected_missing

    print("GREEN: shifted order-eight static transition barrier verified")
    print("boundary partitions with at most six blocks: 4111")
    print("left-side language: 358")
    print("full graph language: 354")
    print("edge deletion/contraction language: 358")
    print("new states:")
    for state in sorted(expected_missing):
        print(f"  {state}")


if __name__ == "__main__":
    main()
