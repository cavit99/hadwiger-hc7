#!/usr/bin/env python3
"""Classify the finite boundary residue behind three full components.

Read the complete unlabelled order-eight graph6 catalogue from stdin:

    geng -q 8 | python3 results/hc7_order8_three_component_boundary_verify.py

The retained graphs H satisfy all three boundary-only conditions:

* chi(H) is 3 or 4;
* no clique U has H-U bipartite; and
* H-Z is K4-minor-free for every two-vertex set Z.

The last condition is exactly the absence of a K4 model supported on at
most six of the eight boundary vertices.  Such a model, three full
components, and two unused boundary anchors give an explicit K7 model.

This script enumerates boundary graphs only.  It never represents or
enumerates the interiors of the full components.
"""

from __future__ import annotations

import argparse
import hashlib
import sys
from collections import Counter
from functools import lru_cache
from itertools import combinations


N = 8
ALL = (1 << N) - 1


def decode_g6(line: str) -> tuple[int, ...]:
    text = line.strip()
    if not text or text.startswith(">"):
        return ()
    values = [ord(char) - 63 for char in text]
    n = values[0]
    assert n == N
    bits: list[int] = []
    for value in values[1:]:
        bits.extend((value >> shift) & 1 for shift in range(5, -1, -1))
    adjacency = [0] * n
    index = 0
    for right in range(1, n):
        for left in range(right):
            if bits[index]:
                adjacency[left] |= 1 << right
                adjacency[right] |= 1 << left
            index += 1
    return tuple(adjacency)


def encode_g6(adjacency: tuple[int, ...]) -> str:
    n = len(adjacency)
    bits = [
        (adjacency[left] >> right) & 1
        for right in range(1, n)
        for left in range(right)
    ]
    while len(bits) % 6:
        bits.append(0)
    values = [n]
    for start in range(0, len(bits), 6):
        value = 0
        for bit in bits[start : start + 6]:
            value = (value << 1) | bit
        values.append(value)
    return "".join(chr(value + 63) for value in values)


def induced(adjacency: tuple[int, ...], keep: tuple[int, ...]) -> tuple[int, ...]:
    position = {vertex: index for index, vertex in enumerate(keep)}
    answer = [0] * len(keep)
    for index, vertex in enumerate(keep):
        neighbours = adjacency[vertex]
        for other in keep:
            if (neighbours >> other) & 1:
                answer[index] |= 1 << position[other]
    return tuple(answer)


def colourable(adjacency: tuple[int, ...], colours: int) -> bool:
    n = len(adjacency)
    assigned = [-1] * n

    def search(done: int) -> bool:
        if done == n:
            return True
        uncoloured = [vertex for vertex in range(n) if assigned[vertex] < 0]
        vertex = max(
            uncoloured,
            key=lambda item: (
                len(
                    {
                        assigned[other]
                        for other in range(n)
                        if assigned[other] >= 0
                        and ((adjacency[item] >> other) & 1)
                    }
                ),
                adjacency[item].bit_count(),
            ),
        )
        forbidden = {
            assigned[other]
            for other in range(n)
            if assigned[other] >= 0 and ((adjacency[vertex] >> other) & 1)
        }
        for colour in range(colours):
            if colour in forbidden:
                continue
            assigned[vertex] = colour
            if search(done + 1):
                return True
        assigned[vertex] = -1
        return False

    return search(0)


def bipartite_after_deleting(adjacency: tuple[int, ...], deleted: int) -> bool:
    n = len(adjacency)
    colour = [-1] * n
    for root in range(n):
        if (deleted >> root) & 1 or colour[root] >= 0:
            continue
        colour[root] = 0
        stack = [root]
        while stack:
            vertex = stack.pop()
            neighbours = adjacency[vertex] & ~deleted
            while neighbours:
                bit = neighbours & -neighbours
                neighbours ^= bit
                other = bit.bit_length() - 1
                if colour[other] < 0:
                    colour[other] = colour[vertex] ^ 1
                    stack.append(other)
                elif colour[other] == colour[vertex]:
                    return False
    return True


def clique(adjacency: tuple[int, ...], vertices: int) -> bool:
    remainder = vertices
    while remainder:
        bit = remainder & -remainder
        remainder ^= bit
        vertex = bit.bit_length() - 1
        if remainder & ~adjacency[vertex]:
            return False
    return True


def has_clique_odd_cycle_transversal(adjacency: tuple[int, ...]) -> bool:
    for vertices in range(1 << len(adjacency)):
        if clique(adjacency, vertices) and bipartite_after_deleting(
            adjacency, vertices
        ):
            return True
    return False


def delete_vertex(adjacency: tuple[int, ...], vertex: int) -> tuple[int, ...]:
    return induced(
        adjacency,
        tuple(index for index in range(len(adjacency)) if index != vertex),
    )


def contract_edge(
    adjacency: tuple[int, ...], left: int, right: int
) -> tuple[int, ...]:
    if left > right:
        left, right = right, left
    keep = [vertex for vertex in range(len(adjacency)) if vertex != right]
    position = {vertex: index for index, vertex in enumerate(keep)}
    answer = [0] * len(keep)
    for first_index, first in enumerate(keep):
        for second_index in range(first_index + 1, len(keep)):
            second = keep[second_index]
            edge = ((adjacency[first] >> second) & 1) != 0
            if first == left:
                edge |= ((adjacency[right] >> second) & 1) != 0
            if second == left:
                edge |= ((adjacency[first] >> right) & 1) != 0
            if edge:
                answer[first_index] |= 1 << second_index
                answer[second_index] |= 1 << first_index
    return tuple(answer)


@lru_cache(maxsize=None)
def has_k4_minor(adjacency: tuple[int, ...]) -> bool:
    n = len(adjacency)
    if n < 4:
        return False
    if n == 4:
        return all(row.bit_count() == 3 for row in adjacency)
    for vertex in range(n):
        if has_k4_minor(delete_vertex(adjacency, vertex)):
            return True
    for left in range(n):
        for right in range(left + 1, n):
            if (adjacency[left] >> right) & 1 and has_k4_minor(
                contract_edge(adjacency, left, right)
            ):
                return True
    return False


def has_compact_k4(adjacency: tuple[int, ...]) -> bool:
    for deleted in combinations(range(N), 2):
        keep = tuple(vertex for vertex in range(N) if vertex not in deleted)
        if has_k4_minor(induced(adjacency, keep)):
            return True
    return False


def induced_cycle(adjacency: tuple[int, ...], vertices: frozenset[int]) -> bool:
    mask = sum(1 << vertex for vertex in vertices)
    if any((adjacency[vertex] & mask).bit_count() != 2 for vertex in vertices):
        return False
    reached = 1 << next(iter(vertices))
    while True:
        expanded = reached
        todo = reached
        while todo:
            bit = todo & -todo
            todo ^= bit
            expanded |= adjacency[bit.bit_length() - 1] & mask
        if expanded == reached:
            return reached == mask
        reached = expanded


def disjoint_odd_cycle_type(adjacency: tuple[int, ...]) -> tuple[int, int] | None:
    cycles = [
        frozenset(choice)
        for order in (3, 5, 7)
        for choice in combinations(range(N), order)
        if induced_cycle(adjacency, frozenset(choice))
    ]
    types = [
        tuple(sorted((len(first), len(second))))
        for first, second in combinations(cycles, 2)
        if first.isdisjoint(second)
    ]
    return min(types) if types else None


def three_colour_partition_count(adjacency: tuple[int, ...]) -> int:
    blocks: list[int] = []
    answer = 0

    def search(vertex: int) -> None:
        nonlocal answer
        if vertex == N:
            if len(blocks) == 3:
                answer += 1
            return
        for index, block in enumerate(blocks):
            if adjacency[vertex] & block:
                continue
            blocks[index] |= 1 << vertex
            search(vertex + 1)
            blocks[index] = block
        if len(blocks) < 3:
            blocks.append(1 << vertex)
            search(vertex + 1)
            blocks.pop()

    search(0)
    return answer


def delete_edge(
    adjacency: tuple[int, ...], left: int, right: int
) -> tuple[int, ...]:
    answer = list(adjacency)
    answer[left] &= ~(1 << right)
    answer[right] &= ~(1 << left)
    return tuple(answer)


def is_residual(adjacency: tuple[int, ...]) -> bool:
    return (
        not colourable(adjacency, 2)
        and colourable(adjacency, 4)
        and not has_clique_odd_cycle_transversal(adjacency)
        and not has_compact_k4(adjacency)
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--list", action="store_true", help="print survivor codes")
    args = parser.parse_args()

    total = 0
    no_oct = {3: 0, 4: 0}
    survivors: list[str] = []
    odd_cycle_packings: dict[tuple[int, int] | None, int] = {}
    partition_spectrum: Counter[int] = Counter()
    edge_minimal: list[str] = []

    for line in sys.stdin:
        adjacency = decode_g6(line)
        if not adjacency:
            continue
        total += 1
        if colourable(adjacency, 2) or not colourable(adjacency, 4):
            continue
        chromatic = 3 if colourable(adjacency, 3) else 4
        if has_clique_odd_cycle_transversal(adjacency):
            continue
        no_oct[chromatic] += 1
        if has_compact_k4(adjacency):
            continue
        code = encode_g6(adjacency)
        survivors.append(code)
        packing = disjoint_odd_cycle_type(adjacency)
        odd_cycle_packings[packing] = odd_cycle_packings.get(packing, 0) + 1
        partition_spectrum[three_colour_partition_count(adjacency)] += 1
        if not any(
            is_residual(delete_edge(adjacency, left, right))
            for left in range(N)
            for right in range(left + 1, N)
            if (adjacency[left] >> right) & 1
        ):
            edge_minimal.append(code)

    survivors.sort()
    digest = hashlib.sha256(("\n".join(survivors) + "\n").encode()).hexdigest()

    assert total == 12_346
    assert no_oct == {3: 746, 4: 953}
    assert len(survivors) == 82
    assert odd_cycle_packings == {(3, 3): 80, (3, 5): 2}
    assert partition_spectrum == Counter(
        {
            1: 2,
            2: 4,
            3: 7,
            4: 16,
            5: 2,
            6: 12,
            7: 2,
            8: 11,
            9: 1,
            10: 1,
            11: 1,
            12: 8,
            16: 4,
            18: 2,
            24: 5,
            30: 1,
            36: 2,
            54: 1,
        }
    )
    assert sorted(edge_minimal) == sorted(
        ("G?`CQG", "G?qbUG", "G?otYw", "GCQR@O", "GCR`uo")
    )

    print(f"order-eight graphs: {total}")
    print(f"three-chromatic without clique OCT: {no_oct[3]}")
    print(f"four-chromatic without clique OCT: {no_oct[4]}")
    print(f"compact-K4-free survivors: {len(survivors)}")
    print("four-chromatic survivors: 0")
    print("survivor odd-cycle packings: (3,3)=80 (3,5)=2")
    print("three-colour partition counts: min=1 max=54")
    print("edge-minimal survivor cores: 5")
    print("core graph6 codes: " + " ".join(sorted(edge_minimal)))
    print(f"survivor-code sha256: {digest}")
    if args.list:
        print("survivor graph6 codes:")
        print("\n".join(survivors))


if __name__ == "__main__":
    main()
