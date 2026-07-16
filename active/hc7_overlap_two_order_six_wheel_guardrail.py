#!/usr/bin/env python3
"""Independent guardrail for the order-six/overlap-two seven-root route.

The script uses no project decoder.  It verifies one admissible normalized
support state, a fixed-private-pair rooted ``W_7`` carrier, and—by exhaustive
edge-contraction search—that their quotient has no ``K_7`` minor.  Thus an
arbitrary edge-minimal three-connected seven-terminal kernel is not by itself
a sufficient carrier guarantee in this cell.
"""

from __future__ import annotations

import functools
import itertools


ORDER = 11
PAIRS = tuple(itertools.combinations(range(ORDER), 2))
PAIR_INDEX = {edge: index for index, edge in enumerate(PAIRS)}

# A normalized joined state.  The two masks are kept literal: carrier edges
# are added only in the quotient layer below, never fed back into a support.
ONES = 668533641445374
ZEROS = 17337923981017089

A = (0, 1, 2, 3, 4, 5)
I = (0, 1)
X = (0, 1, 6, 7, 8)
P, Q = 9, 10
SUPPORTS = (
    A,
    X + (P,),
    X + (Q,),
    (1, 2, 3, 4, 5, P),
    (1, 2, 3, 4, 5, Q),
    (0, 2, 3, 4, 5, P),
    (0, 2, 3, 4, 5, Q),
)

# Local W_7: hub 0 and rim 1-3-2-5-4-6-1.  Map local labels increasingly
# to the seven protected terminals 2,...,8 after reserving {p,q}={9,10}.
LOCAL_WHEEL = (
    (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6),
    (1, 3), (3, 2), (2, 5), (5, 4), (4, 6), (6, 1),
)
TERMINALS = tuple(range(2, 9))
WHEEL_EDGES = tuple(
    tuple(sorted((TERMINALS[left], TERMINALS[right])))
    for left, right in LOCAL_WHEEL
)
WHEEL = sum(1 << PAIR_INDEX[edge] for edge in WHEEL_EDGES)


def has_edge(mask: int, left: int, right: int) -> bool:
    if left > right:
        left, right = right, left
    return bool(mask >> PAIR_INDEX[(left, right)] & 1)


def local_support_is_allowed(support: tuple[int, ...]) -> bool:
    """Recheck the exact local relation without importing its generator."""

    assert len(support) == 6
    assert all(
        has_edge(ONES | ZEROS, left, right)
        for left, right in itertools.combinations(support, 2)
    )
    literal_k5 = any(
        all(has_edge(ONES, left, right) for left, right in itertools.combinations(five, 2))
        for five in itertools.combinations(support, 5)
    )
    exact = any(
        has_edge(ONES, x, y)
        and all(
            has_edge(ONES, left, right)
            for left, right in itertools.combinations(
                tuple(vertex for vertex in support if vertex not in (x, y)), 2
            )
        )
        and all(
            has_edge(ONES, x, z) or has_edge(ONES, y, z)
            for z in support
            if z not in (x, y)
        )
        for x, y in itertools.combinations(support, 2)
    )
    return exact and not literal_k5


def connected(mask: int, vertices: tuple[int, ...]) -> bool:
    reached = {vertices[0]}
    while True:
        old = set(reached)
        reached.update(
            right
            for left in old
            for right in vertices
            if right not in old and has_edge(mask, left, right)
        )
        if reached == old:
            return len(reached) == len(vertices)


def three_connected(mask: int, vertices: tuple[int, ...]) -> bool:
    return all(
        connected(mask, tuple(vertex for vertex in vertices if vertex not in deleted))
        for size in range(3)
        for deleted in itertools.combinations(vertices, size)
    )


def common_rooted_k4() -> bool:
    """Independent copy of the normalized common-outcome predicate."""

    def partitions(items: tuple[int, ...], count: int):
        blocks: list[list[int]] = []

        def visit(index: int):
            if index == len(items):
                if len(blocks) == count:
                    yield tuple(tuple(block) for block in blocks)
                return
            item = items[index]
            for block in blocks:
                block.append(item)
                yield from visit(index + 1)
                block.pop()
            if len(blocks) < count:
                blocks.append([item])
                yield from visit(index + 1)
                blocks.pop()

        yield from visit(0)

    for root in I:
        available = tuple(vertex for vertex in A if vertex != root)
        for size in (4, 5):
            for support in itertools.combinations(available, size):
                for bags in partitions(support, 4):
                    if not all(connected(ONES, bag) for bag in bags):
                        continue
                    if not all(
                        any(has_edge(ONES, x, y) for x in left for y in right)
                        for left, right in itertools.combinations(bags, 2)
                    ):
                        continue
                    if all(
                        all(
                            any(has_edge(ONES, named, vertex) for vertex in bag)
                            for bag in bags
                        )
                        for named in (root, P, Q)
                    ):
                        return True
    return False


def adjacency(mask: int, order: int) -> tuple[int, ...]:
    answer = [0] * order
    for index, (left, right) in enumerate(PAIRS):
        if left >= order or right >= order or not (mask >> index & 1):
            continue
        answer[left] |= 1 << right
        answer[right] |= 1 << left
    return tuple(answer)


def clique7(graph: tuple[int, ...]) -> bool:
    return any(
        all(graph[left] >> right & 1 for left, right in itertools.combinations(vertices, 2))
        for vertices in itertools.combinations(range(len(graph)), 7)
    )


def contract(graph: tuple[int, ...], left: int, right: int) -> tuple[int, ...]:
    assert left < right and graph[left] >> right & 1
    image = tuple(
        left if vertex == right else vertex - (vertex > right)
        for vertex in range(len(graph))
    )
    answer = [0] * (len(graph) - 1)
    for u in range(len(graph)):
        for v in range(u + 1, len(graph)):
            if not (graph[u] >> v & 1):
                continue
            x, y = image[u], image[v]
            if x == y:
                continue
            answer[x] |= 1 << y
            answer[y] |= 1 << x
    return tuple(answer)


@functools.lru_cache(maxsize=None)
def has_k7(graph: tuple[int, ...]) -> bool:
    """Exact for order at most eleven: a model needs at most four contractions."""

    if clique7(graph):
        return True
    if len(graph) == 7:
        return False
    return any(
        has_k7(contract(graph, left, right))
        for left in range(len(graph))
        for right in range(left + 1, len(graph))
        if graph[left] >> right & 1
    )


def main() -> None:
    assert not (ONES & ZEROS)
    assert all(local_support_is_allowed(support) for support in SUPPORTS)
    assert not common_rooted_k4()

    assert three_connected(WHEEL, TERMINALS)
    assert all(
        not three_connected(WHEEL & ~(1 << PAIR_INDEX[edge]), TERMINALS)
        for edge in WHEEL_EDGES
    )

    quotient = ONES | WHEEL
    assert not has_k7(adjacency(quotient, ORDER))

    print("order-six overlap-two W7 guardrail: verified")
    print("reserved_pair", (P, Q))
    print("joined_state", ONES, ZEROS)
    print("carrier_edges", WHEEL_EDGES)
    print("carrier_edge_count", len(WHEEL_EDGES))
    print("quotient_has_K7", False)


if __name__ == "__main__":
    main()
