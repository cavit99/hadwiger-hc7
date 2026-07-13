#!/usr/bin/env python3
"""Exact atlas for cross-splitting an exceptional near-K7 piece.

The six labels induce K6-{ab,ac}.  Three defect-one pieces form a path
and have one of the ten exceptional missed-label profiles.  Delete the
two neutral labels prescribed by the canonical maximal-planar quotient,
read the forced cyclic order around a selected piece, and choose four
distinct neighbour classes in alternating order as the feet of a society
cross.  Replace that piece by two adjacent connected sides U,V, give the
alternating feet to opposite sides, and distribute every remaining
neighbour class minimally to one side.  The program exhaustively tests
whether the resulting ten-vertex quotient has a K7 minor.

This is a quotient atlas, not a proof that a society cross always has this
minimal split form.  Its purpose is to expose the exact support invariant
needed by a retained-shell theorem.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from itertools import combinations, product
import argparse


A, B, C, Q1, Q2, Q3 = range(6)
LABELS = tuple(range(6))
Q = (Q1, Q2, Q3)
X = (6, 7, 8)

EXCEPTIONAL = {
    (C, q, B) for q in Q
} | {
    (B, q, C) for q in Q
} | {
    (C, C, A), (B, B, A), (A, B, B), (A, C, C),
}

NAMES = ("a", "b", "c", "q1", "q2", "q3", "x1", "x2", "x3")


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


PARTITIONS10 = tuple(partitions(10))
assert len(PARTITIONS10) == 5880


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


def find_k7(adj: tuple[int, ...]) -> tuple[int, ...] | None:
    for blocks in PARTITIONS10:
        if not all(connected(block, adj) for block in blocks):
            continue
        good = True
        for i in range(7):
            neighbours = 0
            scan = blocks[i]
            while scan:
                bit = scan & -scan
                scan ^= bit
                neighbours |= adj[bit.bit_length() - 1]
            if any(not (neighbours & blocks[j]) for j in range(i)):
                good = False
                break
        if good:
            return blocks
    return None


def has_k7(adj: tuple[int, ...]) -> bool:
    return find_k7(adj) is not None


def add(adj: list[int], u: int, v: int) -> None:
    adj[u] |= 1 << v
    adj[v] |= 1 << u


def full_neighbours(profile: tuple[int, int, int], index: int) -> set[int]:
    result = set(LABELS) - {profile[index]}
    if index > 0:
        result.add(X[index - 1])
    if index < 2:
        result.add(X[index + 1])
    return result


FACE_ROWS = {
    # Representatives from Theorem 2.3; q means the retained neutral q1.
    (C, Q1, B): (
        "ax1q", "ax2x1", "ax3x2", "aqx3", "bcq", "bx2c",
        "bx1x2", "bqx1", "cx2x3", "cx3q",
    ),
    (C, C, A): (
        "ax1q", "ax2x1", "aqx2", "bcq", "bx3c", "bx2x3",
        "bx1x2", "bqx1", "cx3q", "qx3x2",
    ),
    (A, B, B): (
        "ax2q", "ax3x2", "aqx3", "bcq", "bx1c", "bqx1",
        "cx1x2", "cx3q", "cx2x3", "qx2x1",
    ),
}


def tokens(face: str) -> tuple[str, str, str]:
    out = []
    i = 0
    while i < len(face):
        if face[i] == "x":
            out.append(face[i:i + 2])
            i += 2
        else:
            out.append(face[i])
            i += 1
    assert len(out) == 3
    return tuple(out)


def representative(profile: tuple[int, int, int]):
    """Map a profile to one face-row representative and vertex relabelling.

    Returns representative profile and a map representative-name -> actual
    vertex.  Allowed symmetries are path reversal, b/c interchange, and a
    permutation of neutral q labels.
    """
    for rep in FACE_ROWS:
        for reverse in (False, True):
            for swap_bc in (False, True):
                for qperm in (
                    (Q1, Q2, Q3), (Q1, Q3, Q2), (Q2, Q1, Q3),
                    (Q2, Q3, Q1), (Q3, Q1, Q2), (Q3, Q2, Q1),
                ):
                    label_map = {A: A, B: C if swap_bc else B,
                                 C: B if swap_bc else C,
                                 Q1: qperm[0], Q2: qperm[1], Q3: qperm[2]}
                    word = tuple(label_map[z] for z in rep)
                    if reverse:
                        word = word[::-1]
                    if word != profile:
                        continue
                    vertex_map = {
                        "a": A, "b": label_map[B], "c": label_map[C],
                        "q": label_map[Q1],
                    }
                    for i in range(3):
                        actual_i = 2 - i if reverse else i
                        vertex_map[f"x{i + 1}"] = X[actual_i]
                    return rep, vertex_map
    raise AssertionError(profile)


def cyclic_order(profile: tuple[int, int, int], target: int) -> tuple[int, ...]:
    rep, vertex_map = representative(profile)
    inverse = {actual: name for name, actual in vertex_map.items()}
    target_name = inverse[X[target]]
    neighbour_cycle: dict[str, set[str]] = defaultdict(set)
    for face in FACE_ROWS[rep]:
        row = tokens(face)
        if target_name not in row:
            continue
        others = [z for z in row if z != target_name]
        neighbour_cycle[others[0]].add(others[1])
        neighbour_cycle[others[1]].add(others[0])
    assert neighbour_cycle and all(len(v) == 2 for v in neighbour_cycle.values())
    start = min(neighbour_cycle)
    order = [start]
    previous = None
    current = start
    while True:
        candidates = sorted(neighbour_cycle[current] - ({previous} if previous else set()))
        nxt = candidates[0]
        if nxt == start:
            break
        order.append(nxt)
        previous, current = current, nxt
    result = tuple(vertex_map[z] for z in order)
    assert set(result) == (full_neighbours(profile, target) & set(vertex_map.values()))
    return result


def alternating_four(order: tuple[int, ...]):
    n = len(order)
    seen = set()
    for indices in combinations(range(n), 4):
        feet = tuple(order[i] for i in indices)
        # A cyclic 4-subset has one order up to reversal/rotation.  Canonicalise.
        variants = []
        for row in (feet, feet[::-1]):
            variants.extend(row[i:] + row[:i] for i in range(4))
        key = min(variants)
        if key not in seen:
            seen.add(key)
            yield feet


def split_adjacency(profile: tuple[int, int, int], target: int,
                    side_u: set[int], side_v: set[int]) -> tuple[int, ...]:
    """Replace X[target] by vertices U=9 and V=X[target]."""
    u = 9
    v = X[target]
    adj = [0] * 10
    for x in LABELS:
        for y in range(x + 1, 6):
            if (x, y) not in {(A, B), (A, C)}:
                add(adj, x, y)
    # Untouched piece-to-label edges.
    for i, piece in enumerate(X):
        if i == target:
            continue
        for label in LABELS:
            if label != profile[i]:
                add(adj, piece, label)
    # Untouched path edge, or its allocation to one/both split sides.
    for i in range(2):
        left, right = X[i], X[i + 1]
        if target not in (i, i + 1):
            add(adj, left, right)
    add(adj, u, v)
    for neighbour in side_u:
        add(adj, u, neighbour)
    for neighbour in side_v:
        add(adj, v, neighbour)
    return tuple(adj)


def name_set(values: set[int], target: int) -> str:
    names = list(NAMES) + ["U"]
    # The old target vertex is V after splitting.
    names[X[target]] = "V"
    return "{" + ",".join(names[v] for v in sorted(values)) + "}"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--catalogue", action="store_true")
    parser.add_argument("--maximal-catalogue", action="store_true")
    args = parser.parse_args()
    negatives = []
    tested = 0
    for profile in sorted(EXCEPTIONAL):
        for target in range(3):
            full = full_neighbours(profile, target)
            order = cyclic_order(profile, target)
            for feet in alternating_four(order):
                prescribed_u = {feet[0], feet[2]}
                prescribed_v = {feet[1], feet[3]}
                rest = sorted(full - prescribed_u - prescribed_v)
                for choices in product((0, 1), repeat=len(rest)):
                    side_u = set(prescribed_u)
                    side_v = set(prescribed_v)
                    for z, choice in zip(rest, choices):
                        (side_u if choice == 0 else side_v).add(z)
                    tested += 1
                    adj = split_adjacency(profile, target, side_u, side_v)
                    if not has_k7(adj):
                        negatives.append((profile, target, feet, side_u, side_v))

    print("tested", tested)
    print("negative", len(negatives))
    by_profile_target = Counter((row[0], row[1]) for row in negatives)
    print("negative by profile,target")
    for key, count in sorted(by_profile_target.items()):
        print(key, count)
    support_sizes = Counter(tuple(sorted((len(row[3]), len(row[4]))))
                            for row in negatives)
    print("support-size pairs", sorted(support_sizes.items()))
    min_side = Counter(min(len(row[3]), len(row[4])) for row in negatives)
    print("minimum support size", sorted(min_side.items()))
    shared_adjacent = Counter()
    for profile, target, feet, side_u, side_v in negatives:
        adjacent_pieces = ({X[target - 1]} if target > 0 else set()) | \
                          ({X[target + 1]} if target < 2 else set())
        shared_adjacent[(len(side_u & adjacent_pieces),
                         len(side_v & adjacent_pieces))] += 1
    print("adjacent-piece supports", sorted(shared_adjacent.items()))
    if args.catalogue:
        print("catalogue")
        for profile, target, feet, side_u, side_v in negatives:
            pnames = tuple(NAMES[z] for z in profile)
            fnames = tuple(NAMES[z] for z in feet)
            print(pnames, "target", target + 1, "feet", fnames,
                  "U", name_set(side_u, target),
                  "V", name_set(side_v, target))

    # Stronger audit: permit every neighbour class to contact both sides.
    # Cache by the actual support pair, since many crosses generate the same
    # quotient.  This checks whether the clean invariant "both sides see four
    # classes" survives portal duplication.
    all_cover_negative = []
    seen_supports = set()
    for profile in sorted(EXCEPTIONAL):
        for target in range(3):
            full = full_neighbours(profile, target)
            order = cyclic_order(profile, target)
            for feet in alternating_four(order):
                prescribed_u = {feet[0], feet[2]}
                prescribed_v = {feet[1], feet[3]}
                options = []
                for z in sorted(full):
                    if z in prescribed_u and z in prescribed_v:
                        options.append(((True, True),))
                    elif z in prescribed_u:
                        options.append(((True, False), (True, True)))
                    elif z in prescribed_v:
                        options.append(((False, True), (True, True)))
                    else:
                        options.append(((True, False), (False, True),
                                        (True, True)))
                for choices in product(*options):
                    side_u = {z for z, (left, _) in zip(sorted(full), choices)
                              if left}
                    side_v = {z for z, (_, right) in zip(sorted(full), choices)
                              if right}
                    key = (profile, target, frozenset(side_u), frozenset(side_v))
                    if key in seen_supports:
                        continue
                    seen_supports.add(key)
                    adj = split_adjacency(profile, target, side_u, side_v)
                    if not has_k7(adj):
                        all_cover_negative.append(key)

    print("all-cover support pairs tested", len(seen_supports))
    print("all-cover negative", len(all_cover_negative))
    print("all-cover negative with both support sizes >=4",
          sum(len(row[2]) >= 4 and len(row[3]) >= 4
              for row in all_cover_negative))
    print("all-cover negative support-size pairs",
          sorted(Counter(tuple(sorted((len(row[2]), len(row[3]))))
                         for row in all_cover_negative).items()))

    negative_set = set(all_cover_negative)
    maximal = []
    for profile, target, side_u, side_v in all_cover_negative:
        full = full_neighbours(profile, target)
        extensions = [
            (profile, target, frozenset(set(side_u) | {z}), side_v)
            for z in full - set(side_u)
        ] + [
            (profile, target, side_u, frozenset(set(side_v) | {z}))
            for z in full - set(side_v)
        ]
        if not any(row in negative_set for row in extensions):
            maximal.append((profile, target, side_u, side_v))
    print("inclusion-maximal all-cover negative", len(maximal))
    print("maximal by profile,target",
          sorted(Counter((row[0], row[1]) for row in maximal).items()))
    print("maximal (sizes, intersection, private sizes)",
          sorted(Counter((tuple(sorted((len(row[2]), len(row[3])))),
                          len(row[2] & row[3]),
                          tuple(sorted((len(row[2] - row[3]),
                                        len(row[3] - row[2])))))
                         for row in maximal).items()))
    if args.maximal_catalogue:
        print("maximal all-cover catalogue")
        for profile, target, side_u, side_v in maximal:
            if profile != (C, C, A):
                continue
            print(tuple(NAMES[z] for z in profile), "target", target + 1,
                  "U", name_set(set(side_u), target),
                  "V", name_set(set(side_v), target))


if __name__ == "__main__":
    main()
