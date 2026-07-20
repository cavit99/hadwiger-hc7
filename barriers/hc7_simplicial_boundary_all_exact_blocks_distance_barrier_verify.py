#!/usr/bin/env python3
"""Verify the all-exact-block Kempe-distance barrier.

The boundary consists of two disjoint K4s and one simplicial vertex d
adjacent to the ends of an edge in the first K4.  A state is an equality
partition into at most six independent blocks.  The two certificate
families below are checked to cover every nonempty independent block while
having no Kempe-adjacent pair, even after restricting to any fixed block.
"""

from collections import Counter, deque
from itertools import combinations


N = 9
D_VERTEX = 8


def adjacent(u: int, v: int) -> bool:
    if u == v:
        return False
    if u < 4 and v < 4:
        return True
    if 4 <= u < 8 and 4 <= v < 8:
        return True
    return (u == D_VERTEX and v in (0, 1)) or (
        v == D_VERTEX and u in (0, 1)
    )


def canonical(blocks):
    return tuple(
        sorted(
            (frozenset(block) for block in blocks),
            key=lambda block: (len(block), tuple(block)),
        )
    )


LEFT_ROWS = [
    [(0,), (2,), (4,), (6,), (1, 5), (3, 7, 8)],
    [(1,), (3,), (6,), (0, 7), (2, 5), (4, 8)],
    [(2,), (4,), (8,), (0, 5), (1, 6), (3, 7)],
    [(0,), (5,), (1, 7), (3, 4), (2, 6, 8)],
    [(0,), (7,), (1, 4), (3, 6), (2, 5, 8)],
    [(1,), (0, 4), (2, 7), (3, 6), (5, 8)],
    [(1,), (2,), (4,), (0, 6), (3, 5), (7, 8)],
    [(0,), (6,), (7,), (1, 5), (2, 4), (3, 8)],
    [(3,), (5,), (6,), (0, 4), (1, 7), (2, 8)],
    [(2,), (4,), (0, 7), (1, 6), (3, 5, 8)],
    [(1,), (4,), (0, 5), (3, 6), (2, 7, 8)],
    [(1,), (0, 5), (2, 7), (3, 4), (6, 8)],
    [(0,), (3,), (6,), (7,), (1, 5), (2, 4, 8)],
    [(0,), (1,), (7,), (2, 6), (3, 4), (5, 8)],
    [(2,), (6,), (0, 5), (1, 7), (3, 4, 8)],
    [(0,), (1,), (4,), (5,), (2, 7), (3, 6, 8)],
]

RIGHT_ROWS = [
    [(1,), (5,), (7,), (0, 6), (3, 4), (2, 8)],
    [(0,), (4,), (6,), (1, 7), (2, 5), (3, 8)],
    [(3,), (0, 5), (1, 6), (2, 4), (7, 8)],
    [(0, 4), (1, 5), (2, 7), (3, 6, 8)],
    [(0,), (2,), (7,), (1, 4), (3, 5), (6, 8)],
    [(0, 5), (1, 4), (2, 6), (3, 7, 8)],
    [(1,), (4,), (8,), (0, 7), (2, 6), (3, 5)],
    [(3,), (5,), (0, 6), (1, 7), (2, 4, 8)],
    [(1,), (2,), (5,), (0, 6), (3, 7), (4, 8)],
    [(1,), (7,), (0, 6), (2, 5), (3, 4, 8)],
    [(0,), (6,), (1, 4), (2, 7), (3, 5, 8)],
    [(3,), (4,), (0, 6), (1, 5), (2, 7, 8)],
    [(0, 5), (1, 4), (3, 7), (2, 6, 8)],
    [(1,), (6,), (0, 4), (3, 7), (2, 5, 8)],
    [(1,), (2,), (5,), (0, 4), (3, 6), (7, 8)],
    [(2,), (3,), (5,), (0, 7), (1, 6), (4, 8)],
    [(0,), (1,), (6,), (2, 4), (3, 7), (5, 8)],
]


def enumerate_states():
    states = set()

    def visit(vertex, blocks):
        if vertex == N:
            states.add(canonical(blocks))
            return

        for index, block in enumerate(blocks):
            if all(not adjacent(vertex, old) for old in block):
                block.add(vertex)
                visit(vertex + 1, blocks)
                block.remove(vertex)

        if len(blocks) < 6:
            blocks.append({vertex})
            visit(vertex + 1, blocks)
            blocks.pop()

    visit(0, [])
    return sorted(states, key=repr)


def kempe_neighbours(state, state_index):
    blocks = [set(block) for block in state]
    neighbours = set()

    # Both colours are used.  Interchange one connected component of their
    # induced two-colour graph.
    for first, second in combinations(range(len(blocks)), 2):
        unseen = blocks[first] | blocks[second]
        components = []
        while unseen:
            queue = [unseen.pop()]
            component = set(queue)
            while queue:
                u = queue.pop()
                new = {v for v in unseen if adjacent(u, v)}
                unseen -= new
                queue.extend(new)
                component |= new
            components.append(component)

        for component in components:
            new_first = (blocks[first] - component) | (
                blocks[second] & component
            )
            new_second = (blocks[second] - component) | (
                blocks[first] & component
            )
            changed = [
                set(block)
                for index, block in enumerate(blocks)
                if index not in (first, second)
            ]
            if new_first:
                changed.append(new_first)
            if new_second:
                changed.append(new_second)
            candidate = canonical(changed)
            if candidate != state and candidate in state_index:
                neighbours.add(state_index[candidate])

    # One colour is unused.  Since a colour class is independent, each
    # vertex is a component of the corresponding two-colour graph.
    if len(blocks) < 6:
        for index, block in enumerate(blocks):
            if len(block) < 2:
                continue
            for vertex in block:
                changed = [
                    set(old)
                    for old_index, old in enumerate(blocks)
                    if old_index != index
                ]
                changed.extend(({vertex}, block - {vertex}))
                candidate = canonical(changed)
                if candidate != state and candidate in state_index:
                    neighbours.add(state_index[candidate])

    return neighbours


def independent_sets():
    answer = []
    for order in range(1, N + 1):
        for vertices in combinations(range(N), order):
            if all(not adjacent(u, v) for u, v in combinations(vertices, 2)):
                answer.append(frozenset(vertices))
    return answer


def main():
    states = enumerate_states()
    state_index = {state: index for index, state in enumerate(states)}
    adjacency = [kempe_neighbours(state, state_index) for state in states]
    for u, neighbours in enumerate(adjacency):
        for v in tuple(neighbours):
            adjacency[v].add(u)

    left = {state_index[canonical(row)] for row in LEFT_ROWS}
    right = {state_index[canonical(row)] for row in RIGHT_ROWS}
    assert left.isdisjoint(right)
    assert not any(v in adjacency[u] for u in left for v in right)

    traces = independent_sets()
    distances = []
    for trace in traces:
        allowed = {
            index for index, state in enumerate(states) if trace in state
        }
        starts = left & allowed
        targets = right & allowed
        assert starts and targets

        queue = deque((start, 0) for start in starts)
        seen = set(starts)
        distance = None
        while queue:
            current, depth = queue.popleft()
            if current in targets:
                distance = depth
                break
            for neighbour in adjacency[current] & allowed:
                if neighbour not in seen:
                    seen.add(neighbour)
                    queue.append((neighbour, depth + 1))

        assert distance is not None
        assert distance >= 2
        distances.append(distance)

    counts = Counter(distances)
    assert counts == Counter({2: 33, 3: 6})
    assert len(states) == 744
    assert sum(map(len, adjacency)) // 2 == 6708
    assert len(traces) == 39

    print("states=744 kempe_edges=6708 independent_blocks=39")
    print("left_states=16 right_states=17 cross_kempe_edges=0")
    print("exact_block_quotient_distances: 2=>33 3=>6")
    print("PASS: every independent exact block occurs on both sides at distance at least two")


if __name__ == "__main__":
    main()
