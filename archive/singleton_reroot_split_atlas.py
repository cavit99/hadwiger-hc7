#!/usr/bin/env python3
"""Exact contact atlas for a bipartition of the common Moser exterior.

The 5-side A has the mandatory contacts v,3,4 and the 6-side B has the
mandatory contacts v,1,2.  Four bits record the reverse contacts
A--1,A--2,B--3,B--4.  Each of p,q has state 1=A only, 2=B only, or
3=both.  For each of the 2^4*3^2 states, the script exhausts every
branch-set partition of the ten-vertex quotient and tests for K7.
"""

from itertools import combinations, product


VERTICES = ("0", "v", "1", "2", "3", "4", "p", "q", "A", "B")
INDEX = {vertex: index for index, vertex in enumerate(VERTICES)}


def edge(a, b):
    return frozenset((INDEX[a], INDEX[b]))


FIXED = {
    *(edge("0", x) for x in ("v", "1", "2", "3", "4", "p", "q")),
    *(edge("v", x) for x in ("1", "2", "3", "4")),
    edge("1", "2"), edge("3", "4"),
    edge("p", "q"), edge("p", "3"), edge("p", "4"),
    edge("q", "1"), edge("q", "2"),
    edge("A", "B"),
    edge("A", "v"), edge("A", "3"), edge("A", "4"),
    edge("B", "v"), edge("B", "1"), edge("B", "2"),
}


def partitions(sequence, number):
    blocks = []

    def visit(position):
        if position == len(sequence):
            if len(blocks) == number:
                yield tuple(tuple(block) for block in blocks)
            return
        item = sequence[position]
        for block in blocks:
            block.append(item)
            yield from visit(position + 1)
            block.pop()
        if len(blocks) < number:
            blocks.append([item])
            yield from visit(position + 1)
            blocks.pop()

    yield from visit(0)


PARTITIONS = []
for used_order in range(7, len(VERTICES) + 1):
    for used in combinations(range(len(VERTICES)), used_order):
        PARTITIONS.extend(partitions(used, 7))


def state_edges(state):
    answer = set(FIXED)
    for bit, pair in zip(state[:4], (("A", "1"), ("A", "2"),
                                     ("B", "3"), ("B", "4"))):
        if bit:
            answer.add(edge(*pair))
    for vertex, side_state in zip(("p", "q"), state[4:]):
        if side_state & 1:
            answer.add(edge("A", vertex))
        if side_state & 2:
            answer.add(edge("B", vertex))
    return answer


def find_model(edges):
    order = len(VERTICES)
    adjacency = [[False] * order for _ in range(order)]
    for a, b in map(tuple, edges):
        adjacency[a][b] = adjacency[b][a] = True

    for bags in PARTITIONS:
        valid = True
        for bag in bags:
            seen = {bag[0]}
            todo = [bag[0]]
            while todo:
                x = todo.pop()
                for y in bag:
                    if y not in seen and adjacency[x][y]:
                        seen.add(y)
                        todo.append(y)
            if len(seen) != len(bag):
                valid = False
                break
        if not valid:
            continue
        if all(any(adjacency[x][y] for x in bags[i] for y in bags[j])
               for i, j in combinations(range(7), 2)):
            return bags
    return None


def predecessors(state):
    for index in range(4):
        if state[index]:
            other = list(state)
            other[index] = 0
            yield tuple(other)
    for index in (4, 5):
        if state[index] == 3:
            for replacement in (1, 2):
                other = list(state)
                other[index] = replacement
                yield tuple(other)


def successors(state):
    for index in range(4):
        if not state[index]:
            other = list(state)
            other[index] = 1
            yield tuple(other)
    for index in (4, 5):
        if state[index] != 3:
            other = list(state)
            other[index] = 3
            yield tuple(other)


EXPECTED_MAXIMAL_BAD = {
    (0, 0, 1, 1, 3, 3),
    (0, 1, 0, 1, 3, 3),
    (0, 1, 1, 0, 3, 3),
    (0, 1, 1, 1, 2, 2),
    (1, 0, 0, 1, 3, 3),
    (1, 0, 1, 0, 3, 3),
    (1, 0, 1, 1, 2, 2),
    (1, 1, 0, 0, 3, 3),
    (1, 1, 0, 1, 1, 1),
    (1, 1, 1, 0, 1, 1),
}


def main():
    states = [bits + sides
              for bits in product((0, 1), repeat=4)
              for sides in product((1, 2, 3), repeat=2)]
    models = {state: find_model(state_edges(state)) for state in states}

    good = {state for state, model in models.items() if model is not None}
    bad = set(states) - good
    maximal_bad = {
        state for state in bad
        if all(successor in good for successor in successors(state))
    }
    minimal_good = {
        state for state in good
        if all(predecessor in bad for predecessor in predecessors(state))
    }

    assert len(good) == 41
    assert len(bad) == 103
    assert len(minimal_good) == 12
    assert maximal_bad == EXPECTED_MAXIMAL_BAD
    assert all((1, 1, 1, 1, p_state, q_state) in good
               for p_state, q_state in product((1, 2, 3), repeat=2))

    print("states", len(states), "positive", len(good), "negative", len(bad))
    print("minimal positive states", len(minimal_good))
    print("maximal negative states")
    for state in sorted(maximal_bad):
        print("".join(map(str, state[:4])), "|", state[4], state[5])
    print("every cross-saturated state 1111|** is positive")


if __name__ == "__main__":
    main()
