#!/usr/bin/env python3
"""Diagnostic order-eight census for the two-vertex-shore contraction.

The script requires Brendan McKay's ``geng`` executable from nauty.  It
enumerates one representative of every isomorphism class of graph on eight
vertices, then tests every ordered endpoint-miss pair admitted by the finite
definition below.
"""

from __future__ import annotations

import collections
import functools
import itertools
import shutil
import subprocess


ORDER = 8
ALL = (1 << ORDER) - 1
FULL = ORDER


def decode_graph6(raw: bytes) -> tuple[int, ...]:
    """Decode a short graph6 word of order ``ORDER`` into adjacency masks."""
    values = [byte - 63 for byte in raw.strip()]
    if not values or values[0] != ORDER:
        raise ValueError("unexpected graph6 order")
    bits: list[int] = []
    for value in values[1:]:
        bits.extend((value >> shift) & 1 for shift in range(5, -1, -1))
    rows = [0] * ORDER
    position = 0
    for right in range(1, ORDER):
        for left in range(right):
            if bits[position]:
                rows[left] |= 1 << right
                rows[right] |= 1 << left
            position += 1
    return tuple(rows)


def is_independent(rows: tuple[int, ...], mask: int) -> bool:
    return all(not (rows[vertex] & mask) for vertex in range(ORDER) if mask >> vertex & 1)


def independence_number(rows: tuple[int, ...], mask: int = ALL) -> int:
    return max(
        subset.bit_count()
        for subset in range(1 << ORDER)
        if subset & ~mask == 0 and is_independent(rows, subset)
    )


def is_colourable(rows: tuple[int, ...], colour_count: int) -> bool:
    assignment = [-1] * ORDER

    def search(done: int) -> bool:
        if done == ORDER:
            return True
        vertex = max(
            (candidate for candidate in range(ORDER) if assignment[candidate] < 0),
            key=lambda candidate: rows[candidate].bit_count(),
        )
        forbidden = {
            assignment[neighbour]
            for neighbour in range(ORDER)
            if assignment[neighbour] >= 0 and rows[vertex] >> neighbour & 1
        }
        for colour in range(colour_count):
            if colour in forbidden:
                continue
            assignment[vertex] = colour
            if search(done + 1):
                return True
        assignment[vertex] = -1
        return False

    return search(0)


def canonical_five_partitions() -> tuple[tuple[int, ...], ...]:
    """Return restricted-growth words for partitions into exactly five blocks."""
    result: list[tuple[int, ...]] = []
    word = [0] * ORDER

    def search(index: int, maximum: int) -> None:
        if index == ORDER:
            if maximum == 4:
                result.append(tuple(word))
            return
        for value in range(min(maximum + 1, 4) + 1):
            word[index] = value
            search(index + 1, max(maximum, value))

    search(1, 0)
    return tuple(result)


FIVE_PARTITIONS = canonical_five_partitions()


def admissible_miss_pairs(rows: tuple[int, ...]) -> set[tuple[int, int]]:
    """Return the ordered endpoint-miss pairs exposed by five-block traces.

    ``FULL`` records a boundary-full endpoint.  A non-full miss may be a
    vertex in a non-singleton block of some proper surjective five-colouring.
    Two non-full misses are required to be distinct.
    """
    answer: set[tuple[int, int]] = set()
    for partition in FIVE_PARTITIONS:
        if any(
            partition[left] == partition[right]
            for left in range(ORDER)
            for right in range(left + 1, ORDER)
            if rows[left] >> right & 1
        ):
            continue
        multiplicity = collections.Counter(partition)
        repeated = [
            vertex
            for vertex in range(ORDER)
            if multiplicity[partition[vertex]] >= 2
        ]
        choices = [FULL, *repeated]
        answer.update(
            (first, second)
            for first in choices
            for second in choices
            if first == FULL or second == FULL or first != second
        )
    return answer


def bipartition(
    rows: tuple[int, ...], kept: int
) -> tuple[bool, tuple[tuple[int, int], ...]]:
    """Return the independently orientable bipartite components of ``kept``."""
    components: list[tuple[int, int]] = []
    unseen = kept
    while unseen:
        root = (unseen & -unseen).bit_length() - 1
        left = 1 << root
        right = 0
        frontier = [root]
        unseen &= ~(1 << root)
        while frontier:
            vertex = frontier.pop()
            vertex_side = 0 if left >> vertex & 1 else 1
            for neighbour in range(ORDER):
                bit = 1 << neighbour
                if not (kept & bit and rows[vertex] & bit):
                    continue
                if vertex_side == 0:
                    if left & bit:
                        return False, ()
                    if not (right & bit):
                        right |= bit
                        unseen &= ~bit
                        frontier.append(neighbour)
                else:
                    if right & bit:
                        return False, ()
                    if not (left & bit):
                        left |= bit
                        unseen &= ~bit
                        frontier.append(neighbour)
        components.append((left, right))
    return True, tuple(components)


def compatible_bipartition(
    rows: tuple[int, ...], miss_v: int, miss_a: int
) -> tuple[int, int, int] | None:
    """Find ``Z,P,Q`` compatible with the two endpoint neighbourhoods.

    Here ``|Z| <= 2``, ``X-Z = P dotcup Q``, both ``P`` and ``Q`` are
    independent, ``P`` avoids the unique vertex missed by ``v``, and ``Q``
    avoids the unique vertex missed by ``a``.
    """
    for deleted_size in range(3):
        for deleted_tuple in itertools.combinations(range(ORDER), deleted_size):
            deleted = sum(1 << vertex for vertex in deleted_tuple)
            kept = ALL ^ deleted
            okay, components = bipartition(rows, kept)
            if not okay:
                continue
            for orientation in range(1 << len(components)):
                p = 0
                q = 0
                for index, (left, right) in enumerate(components):
                    if orientation >> index & 1:
                        left, right = right, left
                    p |= left
                    q |= right
                if miss_v != FULL and p >> miss_v & 1:
                    continue
                if miss_a != FULL and q >> miss_a & 1:
                    continue
                if p and q:
                    return deleted, p, q
    return None


def induced(rows: tuple[int, ...], keep: tuple[int, ...]) -> tuple[int, ...]:
    position = {vertex: index for index, vertex in enumerate(keep)}
    result = [0] * len(keep)
    for index, vertex in enumerate(keep):
        for other in keep:
            if rows[vertex] >> other & 1:
                result[index] |= 1 << position[other]
    return tuple(result)


def contract_edge(
    rows: tuple[int, ...], first: int, second: int
) -> tuple[int, ...]:
    if first > second:
        first, second = second, first
    keep = tuple(vertex for vertex in range(len(rows)) if vertex != second)
    result = [0] * len(keep)
    for left_index, left in enumerate(keep):
        for right_index in range(left_index + 1, len(keep)):
            right = keep[right_index]
            present = bool(rows[left] >> right & 1)
            if left == first:
                present |= bool(rows[second] >> right & 1)
            if right == first:
                present |= bool(rows[left] >> second & 1)
            if present:
                result[left_index] |= 1 << right_index
                result[right_index] |= 1 << left_index
    return tuple(result)


@functools.lru_cache(maxsize=None)
def has_complete_minor(rows: tuple[int, ...], order: int) -> bool:
    if len(rows) < order:
        return False
    if len(rows) == order:
        return all(row.bit_count() == order - 1 for row in rows)
    for vertex in range(len(rows)):
        if has_complete_minor(
            induced(rows, tuple(other for other in range(len(rows)) if other != vertex)),
            order,
        ):
            return True
    for first in range(len(rows)):
        for second in range(first + 1, len(rows)):
            if rows[first] >> second & 1 and has_complete_minor(
                contract_edge(rows, first, second), order
            ):
                return True
    return False


def main() -> None:
    if not __debug__:
        raise SystemExit("census checks require normal Python mode (without -O)")

    geng = shutil.which("geng")
    if geng is None:
        raise SystemExit("missing dependency: install nauty so that `geng` is on PATH")

    process = subprocess.Popen([geng, "-q", str(ORDER)], stdout=subprocess.PIPE)
    if process.stdout is None:
        raise RuntimeError("failed to capture geng output")

    graph_count = 0
    eligible_graph_count = 0
    k4_minor_free_graph_count = 0
    eligible_instances = collections.Counter()
    incompatible_instances = collections.Counter()
    k4_minor_free_eligible = collections.Counter()
    k4_minor_free_incompatible = collections.Counter()

    for raw in process.stdout:
        rows = decode_graph6(raw)
        graph_count += 1
        if independence_number(rows) > 4 or not is_colourable(rows, 4):
            continue
        eligible_graph_count += 1
        k4_minor_free = not has_complete_minor(rows, 4)
        if k4_minor_free:
            k4_minor_free_graph_count += 1

        for miss_v, miss_a in admissible_miss_pairs(rows):
            if miss_v != FULL and independence_number(
                rows, ALL ^ (1 << miss_v)
            ) > 3:
                continue
            if miss_a != FULL and independence_number(
                rows, ALL ^ (1 << miss_a)
            ) > 3:
                continue

            miss_count = int(miss_v != FULL) + int(miss_a != FULL)
            eligible_instances[miss_count] += 1
            if k4_minor_free:
                k4_minor_free_eligible[miss_count] += 1

            if compatible_bipartition(rows, miss_v, miss_a) is not None:
                continue
            incompatible_instances[miss_count] += 1
            if k4_minor_free:
                k4_minor_free_incompatible[miss_count] += 1

    if process.wait() != 0:
        raise RuntimeError("geng failed")

    expected = {
        "graph_count": 12_346,
        "eligible_graph_count": 10_460,
        "eligible_instances": {0: 10_460, 1: 117_796, 2: 341_596},
        "incompatible_instances": {0: 2_514, 1: 39_742, 2: 166_990},
        "k4_minor_free_graph_count": 1_116,
        "k4_minor_free_eligible": {0: 1_116, 1: 6_446, 2: 11_282},
        "k4_minor_free_incompatible": {0: 0, 1: 0, 2: 520},
    }
    observed = {
        "graph_count": graph_count,
        "eligible_graph_count": eligible_graph_count,
        "eligible_instances": {
            miss_count: eligible_instances[miss_count] for miss_count in range(3)
        },
        "incompatible_instances": {
            miss_count: incompatible_instances[miss_count] for miss_count in range(3)
        },
        "k4_minor_free_graph_count": k4_minor_free_graph_count,
        "k4_minor_free_eligible": {
            miss_count: k4_minor_free_eligible[miss_count] for miss_count in range(3)
        },
        "k4_minor_free_incompatible": {
            miss_count: k4_minor_free_incompatible[miss_count]
            for miss_count in range(3)
        },
    }
    if observed != expected:
        raise AssertionError((observed, expected))

    print(f"graphs={graph_count}")
    print(f"eligible_graphs={eligible_graph_count}")
    print(
        "eligible_instances="
        f"{sum(eligible_instances.values())} "
        f"by_miss_count={observed['eligible_instances']}"
    )
    print(
        "incompatible_instances="
        f"{sum(incompatible_instances.values())} "
        f"by_miss_count={observed['incompatible_instances']}"
    )
    print(f"k4_minor_free_eligible_graphs={k4_minor_free_graph_count}")
    print(
        "k4_minor_free_eligible_instances="
        f"{sum(k4_minor_free_eligible.values())} "
        f"by_miss_count={observed['k4_minor_free_eligible']}"
    )
    print(
        "k4_minor_free_incompatible_instances="
        f"{sum(k4_minor_free_incompatible.values())} "
        f"by_miss_count={observed['k4_minor_free_incompatible']}"
    )


if __name__ == "__main__":
    main()
