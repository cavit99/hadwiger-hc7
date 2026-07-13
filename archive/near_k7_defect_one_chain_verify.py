#!/usr/bin/env python3
"""Exact certificate for the K7^vee defect-one three-piece theorem.

The six labelled vertices induce K6 with the two incident edges ab,ac
deleted.  Three helper vertices represent arbitrary connected pieces in a
path.  Each helper is adjacent to all six labels or misses exactly one.

For every one of the 7^3 support profiles, enumerate every spanning
partition of the nine quotient vertices into seven nonempty branch bags.
Connectedness lets any K7 model be made spanning, so this is exhaustive.
The program replays connectivity and all 21 adjacencies of every positive
certificate and checks the ten advertised negative words.
"""

from __future__ import annotations

import argparse
from itertools import product


LABELS = tuple(range(6))
A, B, C = 0, 1, 2
Q = (3, 4, 5)
PIECES = (6, 7, 8)


def partitions(n: int, k: int = 7):
    labels = [0] * n

    def rec(pos: int, maximum: int):
        if pos == n:
            if maximum + 1 == k:
                blocks = [0] * k
                for vertex, label in enumerate(labels):
                    blocks[label] |= 1 << vertex
                yield tuple(blocks)
            return
        remaining = n - pos
        missing = k - (maximum + 1)
        if missing > remaining:
            return
        for label in range(min(maximum + 1, k - 1) + 1):
            labels[pos] = label
            yield from rec(pos + 1, max(maximum, label))

    yield from rec(1, 0)


PARTITIONS = tuple(partitions(9))
assert len(PARTITIONS) == 462


def adjacency(profile: tuple[int | None, ...]) -> tuple[int, ...]:
    """`None` is a full row; an integer is the unique missed label."""
    adj = [0] * 9

    def add(u: int, v: int) -> None:
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    for u in LABELS:
        for v in range(u + 1, 6):
            if (u, v) not in {(A, B), (A, C)}:
                add(u, v)
    add(6, 7)
    add(7, 8)
    for piece, missed in zip(PIECES, profile):
        for label in LABELS:
            if label != missed:
                add(piece, label)
    return tuple(adj)


def connected(mask: int, adj: tuple[int, ...]) -> bool:
    reached = mask & -mask
    while True:
        neighbours = 0
        scan = reached
        while scan:
            bit = scan & -scan
            scan ^= bit
            neighbours |= adj[bit.bit_length() - 1]
        expanded = reached | (neighbours & mask)
        if expanded == reached:
            return reached == mask
        reached = expanded


def verify_model(blocks: tuple[int, ...], adj: tuple[int, ...]) -> None:
    assert len(blocks) == 7
    assert all(blocks)
    assert sum(block.bit_count() for block in blocks) == 9
    assert not any(blocks[i] & blocks[j]
                   for i in range(7) for j in range(i))
    assert all(connected(block, adj) for block in blocks)
    for i in range(7):
        neighbours = 0
        scan = blocks[i]
        while scan:
            bit = scan & -scan
            scan ^= bit
            neighbours |= adj[bit.bit_length() - 1]
        for j in range(i):
            assert neighbours & blocks[j]


def model(profile: tuple[int | None, ...]) -> tuple[int, ...] | None:
    adj = adjacency(profile)
    for blocks in PARTITIONS:
        try:
            verify_model(blocks, adj)
        except AssertionError:
            continue
        return blocks
    return None


EXPECTED_NEGATIVE = {
    (C, q, B) for q in Q
} | {
    (B, q, C) for q in Q
} | {
    (C, C, A),
    (B, B, A),
    (A, B, B),
    (A, C, C),
}


def block_names(blocks: tuple[int, ...]) -> str:
    names = ("a", "b", "c", "q1", "q2", "q3", "X1", "X2", "X3")
    rendered = []
    for block in blocks:
        rendered.append("{" + ",".join(
            names[v] for v in range(9) if block >> v & 1
        ) + "}")
    return " | ".join(rendered)


def profile_names(profile: tuple[int | None, ...]) -> str:
    names = ("a", "b", "c", "q1", "q2", "q3")
    return "(" + ",".join("*" if item is None else names[item]
                           for item in profile) + ")"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--catalogue", action="store_true",
        help="print an exact seven-branch certificate for every positive profile",
    )
    args = parser.parse_args()
    types = (None,) + LABELS
    negative = set()
    witnesses = {}
    for profile in product(types, repeat=3):
        certificate = model(profile)
        if certificate is None:
            negative.add(profile)
        else:
            # Replay the complete certificate before retaining it.
            verify_model(certificate, adjacency(profile))
            witnesses[profile] = certificate

    assert negative == EXPECTED_NEGATIVE, (negative, EXPECTED_NEGATIVE)

    words_by_length = {}
    alphabet = LABELS
    for length in range(3, 6):
        words = {
            word
            for word in product(alphabet, repeat=length)
            if all(tuple(word[i:i + 3]) in negative
                   for i in range(length - 2))
        }
        words_by_length[length] = words
    assert words_by_length[3] == EXPECTED_NEGATIVE
    assert words_by_length[4] == {
        (A, B, B, A),
        (A, C, C, A),
    }
    assert not words_by_length[5]

    print("profiles", len(types) ** 3)
    print("K7-positive", len(witnesses))
    print("K7-negative", len(negative))
    print("negative words", sorted(negative))
    print("length-four words", sorted(words_by_length[4]))
    print("length-five words", len(words_by_length[5]))
    if args.catalogue:
        for profile in sorted(
            witnesses,
            key=lambda row: tuple(-1 if item is None else item for item in row),
        ):
            print(profile_names(profile), block_names(witnesses[profile]))


if __name__ == "__main__":
    main()
