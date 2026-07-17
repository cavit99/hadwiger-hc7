#!/usr/bin/env python3
"""Probe three six-supports U+r for a common three-rooted K4 in U."""

from __future__ import annotations

import itertools
import subprocess


N = 8


def decode_g6(data: bytes) -> tuple[int, ...]:
    values = [byte - 63 for byte in data.strip()]
    assert values[0] == N
    bits = [bit for value in values[1:] for bit in ((value >> s) & 1 for s in range(5, -1, -1))]
    adjacency = [0] * N
    cursor = 0
    for high in range(1, N):
        for low in range(high):
            if bits[cursor]:
                adjacency[low] |= 1 << high
                adjacency[high] |= 1 << low
            cursor += 1
    return tuple(adjacency)


def connected(mask: int, adjacency: tuple[int, ...]) -> bool:
    reached = mask & -mask
    frontier = reached
    while frontier:
        bit = frontier & -frontier
        frontier ^= bit
        new = adjacency[bit.bit_length() - 1] & mask & ~reached
        reached |= new
        frontier |= new
    return reached == mask


def touch(left: int, right: int, adjacency: tuple[int, ...]) -> bool:
    return any(adjacency[v] & right for v in range(N) if left & (1 << v))


def exact_six_support(mask: int, adjacency: tuple[int, ...]) -> bool:
    vertices = [v for v in range(N) if mask & (1 << v)]
    for x, y in itertools.combinations(vertices, 2):
        if not adjacency[x] & (1 << y):
            continue
        singletons = [v for v in vertices if v not in (x, y)]
        if all(adjacency[u] & (1 << v) for u, v in itertools.combinations(singletons, 2)) and all(
            (adjacency[x] | adjacency[y]) & (1 << v) for v in singletons
        ):
            return True
    return False


def contains_literal_k5(mask: int, adjacency: tuple[int, ...]) -> bool:
    vertices = [v for v in range(N) if mask & (1 << v)]
    return any(
        all(adjacency[u] & (1 << v) for u, v in itertools.combinations(five, 2))
        for five in itertools.combinations(vertices, 5)
    )


def partitions(items: tuple[int, ...], block_count: int):
    bags: list[int] = []

    def visit(index: int):
        if index == len(items):
            if len(bags) == block_count:
                yield tuple(bags)
            return
        bit = 1 << items[index]
        for position in range(len(bags)):
            bags[position] |= bit
            yield from visit(index + 1)
            bags[position] ^= bit
        if len(bags) < block_count:
            bags.append(bit)
            yield from visit(index + 1)
            bags.pop()

    yield from visit(0)


def common_rooted_k4(common: tuple[int, ...], roots: tuple[int, ...], adjacency: tuple[int, ...]) -> bool:
    for size in (4, 5):
        for used in itertools.combinations(common, size):
            for bags in partitions(used, 4):
                if not all(connected(bag, adjacency) for bag in bags):
                    continue
                if not all(touch(x, y, adjacency) for x, y in itertools.combinations(bags, 2)):
                    continue
                if all(all(adjacency[root] & bag for bag in bags) for root in roots):
                    return True
    return False


def has_k7_minor(adjacency: tuple[int, ...]) -> bool:
    # On eight vertices a seven-bag model is either a literal K7 on a
    # seven-set, or six singleton bags plus one two-vertex edge bag.
    for used in itertools.combinations(range(N), 7):
        if all(adjacency[u] & (1 << v) for u, v in itertools.combinations(used, 2)):
            return True
    for x, y in itertools.combinations(range(N), 2):
        if not adjacency[x] & (1 << y):
            continue
        rest = [v for v in range(N) if v not in (x, y)]
        if all(adjacency[u] & (1 << v) for u, v in itertools.combinations(rest, 2)) and all(
            (adjacency[x] | adjacency[y]) & (1 << v) for v in rest
        ):
            return True
    return False


def main() -> None:
    process = subprocess.Popen(["geng", "-q", "8"], stdout=subprocess.PIPE)
    assert process.stdout is not None
    tested = configurations = survivors = 0
    examples: list[bytes] = []
    for line in process.stdout:
        tested += 1
        adjacency = decode_g6(line)
        if has_k7_minor(adjacency):
            continue
        for common in itertools.combinations(range(N), 5):
            roots = tuple(v for v in range(N) if v not in common)
            supports = [sum(1 << v for v in common + (root,)) for root in roots]
            if not all(exact_six_support(support, adjacency) for support in supports):
                continue
            if any(contains_literal_k5(support, adjacency) for support in supports):
                continue
            configurations += 1
            if not common_rooted_k4(common, roots, adjacency):
                survivors += 1
                if len(examples) < 10:
                    examples.append(line.strip() + b" U=" + str(common).encode())
    assert process.wait() == 0
    print(f"graphs={tested} irredundant_triples={configurations} no_common_rooted_k4={survivors}")
    for example in examples:
        print(example.decode())


if __name__ == "__main__":
    main()
