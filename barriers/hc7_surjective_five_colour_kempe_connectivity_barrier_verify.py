#!/usr/bin/env python3
"""Verify the labelled-surjective Kempe obstruction on K_{2,6}."""

from itertools import product


N = 8
LEFT = frozenset((6, 7))
RIGHT = frozenset(range(6))
EDGES = frozenset((u, v) for u in RIGHT for v in LEFT)
COLORS = range(5)


def encode_graph6(order: int, edges: frozenset[tuple[int, int]]) -> str:
    """Encode a small graph in graph6 format."""
    bits = []
    for j in range(1, order):
        for i in range(j):
            bits.append(int((i, j) in edges or (j, i) in edges))
    while len(bits) % 6:
        bits.append(0)
    payload = []
    for start in range(0, len(bits), 6):
        value = 0
        for bit in bits[start : start + 6]:
            value = 2 * value + bit
        payload.append(chr(value + 63))
    return chr(order + 63) + "".join(payload)


def graph6() -> str:
    return encode_graph6(N, EDGES)


def connected(vertex_set: frozenset[int]) -> bool:
    if not vertex_set:
        return False
    reached = {next(iter(vertex_set))}
    frontier = list(reached)
    while frontier:
        u = frontier.pop()
        for v in vertex_set - reached:
            if (u, v) in EDGES or (v, u) in EDGES:
                reached.add(v)
                frontier.append(v)
    return reached == set(vertex_set)


def set_partitions(items: tuple[int, ...], blocks: int):
    """Yield unlabelled partitions of items into exactly `blocks` blocks."""
    current: list[list[int]] = []

    def visit(index: int):
        if index == len(items):
            if len(current) == blocks:
                yield tuple(frozenset(block) for block in current)
            return
        item = items[index]
        for block in current:
            block.append(item)
            yield from visit(index + 1)
            block.pop()
        if len(current) < blocks:
            current.append([item])
            yield from visit(index + 1)
            current.pop()

    yield from visit(0)


def has_k5_minor() -> bool:
    vertices = tuple(range(N))
    # Deleted vertices are represented by choosing the retained subset first.
    for keep_mask in range(1 << N):
        retained = tuple(v for v in vertices if keep_mask & (1 << v))
        if len(retained) < 5:
            continue
        for branch_sets in set_partitions(retained, 5):
            if not all(connected(branch_set) for branch_set in branch_sets):
                continue
            if all(
                any(
                    (u, v) in EDGES or (v, u) in EDGES
                    for u in branch_sets[i]
                    for v in branch_sets[j]
                )
                for i in range(5)
                for j in range(i + 1, 5)
            ):
                return True
    return False


def proper_surjective(
    colouring: tuple[int, ...], edges: frozenset[tuple[int, int]] = EDGES
) -> bool:
    return len(set(colouring)) == 5 and all(
        colouring[u] != colouring[v] for u, v in edges
    )


def two_colour_components(
    colouring: tuple[int, ...],
    a: int,
    b: int,
    edges: frozenset[tuple[int, int]] = EDGES,
):
    remaining = {v for v in range(N) if colouring[v] in (a, b)}
    while remaining:
        root = next(iter(remaining))
        component = {root}
        remaining.remove(root)
        frontier = [root]
        while frontier:
            u = frontier.pop()
            neighbours = {
                v
                for v in remaining
                if (u, v) in edges or (v, u) in edges
            }
            component.update(neighbours)
            remaining.difference_update(neighbours)
            frontier.extend(neighbours)
        yield component


def kempe_neighbours(
    colouring: tuple[int, ...], edges: frozenset[tuple[int, int]] = EDGES
):
    for a in COLORS:
        for b in range(a + 1, 5):
            for component in two_colour_components(colouring, a, b, edges):
                changed = list(colouring)
                for v in component:
                    changed[v] = b if colouring[v] == a else a
                result = tuple(changed)
                if len(set(result)) == 5:
                    yield result


def kempe_component_orders(edges: frozenset[tuple[int, int]]):
    states = {
        colouring
        for colouring in product(COLORS, repeat=N)
        if proper_surjective(colouring, edges)
    }
    unseen = set(states)
    components = []
    while unseen:
        root = next(iter(unseen))
        unseen.remove(root)
        reached = {root}
        frontier = [root]
        while frontier:
            colouring = frontier.pop()
            for neighbour in kempe_neighbours(colouring, edges):
                assert neighbour in states
                if neighbour in unseen:
                    unseen.remove(neighbour)
                    reached.add(neighbour)
                    frontier.append(neighbour)
        components.append(reached)
    return states, components


def check_tree_decomposition(order, edges, bags, tree_edges, width):
    assert max(map(len, bags)) - 1 <= width
    assert all(
        any(u in bag and v in bag for bag in bags) for u, v in edges
    )
    for vertex in range(order):
        containing = {index for index, bag in enumerate(bags) if vertex in bag}
        assert containing
        reached = {next(iter(containing))}
        frontier = list(reached)
        while frontier:
            bag = frontier.pop()
            for x, y in tree_edges:
                other = y if x == bag else x if y == bag else None
                if other in containing - reached:
                    reached.add(other)
                    frontier.append(other)
        assert reached == containing


def main() -> None:
    assert graph6() == "G??F~w"
    assert not has_k5_minor()

    states, components = kempe_component_orders(EDGES)
    assert len(states) == 18_600

    assert sorted(map(len, components)) == [7_800, 10_800]
    palette_counts = [
        {len({colouring[6], colouring[7]}) for colouring in component}
        for component in components
    ]
    assert {frozenset(values) for values in palette_counts} == {
        frozenset((1,)),
        frozenset((2,)),
    }

    first = (1, 1, 1, 2, 3, 4, 0, 0)
    second = (2, 2, 2, 2, 3, 4, 0, 1)
    assert proper_surjective(first) and proper_surjective(second)
    assert len({first[6], first[7]}) == 1
    assert len({second[6], second[7]}) == 2

    static_edges = EDGES | frozenset(((0, 4), (1, 5)))
    assert encode_graph6(8, static_edges) == "G?`F~w"
    static_states, static_components = kempe_component_orders(static_edges)
    assert len(static_states) == 11_040
    assert sorted(map(len, static_components)) == [5_520, 5_520]
    assert {
        frozenset({colouring[6] == colouring[7] for colouring in component})
        for component in static_components
    } == {frozenset((False,)), frozenset((True,))}

    static_bags = [
        frozenset((6, 7, 0, 4)),
        frozenset((6, 7, 1, 5)),
        frozenset((6, 7, 2)),
        frozenset((6, 7, 3)),
    ]
    static_tree = [(0, 1), (0, 2), (0, 3)]
    check_tree_decomposition(8, static_edges, static_bags, static_tree, 3)

    extended_edges = static_edges | frozenset(((0, 8), (4, 8)))
    assert encode_graph6(9, extended_edges) == "H?`F~yG"
    check_tree_decomposition(
        9,
        extended_edges,
        static_bags + [frozenset((8, 0, 4))],
        static_tree + [(0, 4)],
        3,
    )

    print(
        "PASS K26=G??F~w components=7800,10800 "
        "static=G?`F~w components=5520,5520 invariant=twin_equality"
    )


if __name__ == "__main__":
    main()
