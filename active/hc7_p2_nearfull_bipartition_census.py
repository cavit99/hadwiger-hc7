#!/usr/bin/env python3
"""Diagnostic order-eight census for the two-vertex-shore contraction.

The script requires Brendan McKay's ``geng`` executable from nauty.  It
enumerates one representative of every isomorphism class of graph on eight
vertices, then tests every ordered endpoint-miss pair admitted by the finite
definition below.
"""

from __future__ import annotations

import collections
import itertools
import shutil
import subprocess


ORDER = 8
ALL = (1 << ORDER) - 1
FULL = ORDER
PAIR_WIDTH = ORDER + 1


def pair_bit(first: int, second: int) -> int:
    return 1 << (first * PAIR_WIDTH + second)


SUBSETS_BY_SIZE = tuple(
    tuple(mask for mask in range(1 << ORDER) if mask.bit_count() == size)
    for size in range(ORDER + 1)
)
DELETION_MASKS = tuple(
    sum(1 << vertex for vertex in vertices)
    for size in range(3)
    for vertices in itertools.combinations(range(ORDER), size)
)
PAIR_CLASS_MASKS = tuple(
    sum(
        pair_bit(first, second)
        for first in range(PAIR_WIDTH)
        for second in range(PAIR_WIDTH)
        if int(first != FULL) + int(second != FULL) == miss_count
        and (first == FULL or second == FULL or first != second)
    )
    for miss_count in range(3)
)
FIRST_ENDPOINT_MASKS = tuple(
    sum(pair_bit(first, second) for second in range(PAIR_WIDTH))
    for first in range(ORDER)
)
SECOND_ENDPOINT_MASKS = tuple(
    sum(pair_bit(first, second) for first in range(PAIR_WIDTH))
    for second in range(ORDER)
)
SAME_SIDE_PAIR_MASKS = tuple(
    sum(
        pair_bit(first, second)
        for first in range(ORDER)
        for second in range(ORDER)
        if first != second and mask >> first & 1 and mask >> second & 1
    )
    for mask in range(1 << ORDER)
)


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


def independent_masks(rows: tuple[int, ...]) -> tuple[bool, ...]:
    """Classify all vertex subsets by independence in one dynamic pass."""
    answer = [False] * (1 << ORDER)
    answer[0] = True
    for mask in range(1, 1 << ORDER):
        bit = mask & -mask
        vertex = bit.bit_length() - 1
        rest = mask ^ bit
        answer[mask] = answer[rest] and not rows[vertex] & rest
    return tuple(answer)


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


def canonical_five_partitions() -> tuple[tuple[int, int], ...]:
    """Encode every five-block partition by conflicts and admitted miss pairs."""
    result: list[tuple[int, int]] = []
    word = [0] * ORDER

    def search(index: int, maximum: int) -> None:
        if index == ORDER:
            if maximum == 4:
                multiplicities = [word.count(block) for block in range(5)]
                repeated = [
                    vertex
                    for vertex in range(ORDER)
                    if multiplicities[word[vertex]] >= 2
                ]
                choices = [FULL, *repeated]
                admitted = sum(
                    pair_bit(first, second)
                    for first in choices
                    for second in choices
                    if first == FULL or second == FULL or first != second
                )
                conflicts = 0
                position = 0
                for right in range(1, ORDER):
                    for left in range(right):
                        if word[left] == word[right]:
                            conflicts |= 1 << position
                        position += 1
                result.append((conflicts, admitted))
            return
        for value in range(min(maximum + 1, 4) + 1):
            word[index] = value
            search(index + 1, max(maximum, value))

    search(1, 0)
    return tuple(result)


FIVE_PARTITIONS = canonical_five_partitions()


def graph_edge_mask(rows: tuple[int, ...]) -> int:
    edges = 0
    position = 0
    for right in range(1, ORDER):
        for left in range(right):
            if rows[left] >> right & 1:
                edges |= 1 << position
            position += 1
    return edges


def admissible_miss_pair_bits(rows: tuple[int, ...]) -> int:
    """Return the ordered endpoint-miss pairs exposed by five-block traces.

    ``FULL`` records a boundary-full endpoint.  A non-full miss may be a
    vertex in a non-singleton block of some proper surjective five-colouring.
    Two non-full misses are required to be distinct.
    """
    edges = graph_edge_mask(rows)
    answer = 0
    for conflicts, admitted in FIVE_PARTITIONS:
        if not edges & conflicts:
            answer |= admitted
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


def compatible_miss_pair_bits(rows: tuple[int, ...], needed: int) -> int:
    """Return marked pairs compatible with some ``Z,P,Q``.

    Here ``|Z| <= 2``, ``X-Z = P dotcup Q``, both ``P`` and ``Q`` are
    independent, ``P`` avoids the unique vertex missed by ``v``, and ``Q``
    avoids the unique vertex missed by ``a``.

    For a fixed bipartite component, its two sides may be reversed
    independently.  Two retained misses are therefore incompatible exactly
    when they occur on the same side of the same component.  A deleted miss
    imposes no restriction.  Since at least six vertices remain, the two
    independent classes can always both be kept nonempty.
    """
    compatible = 0
    for deleted in DELETION_MASKS:
        okay, components = bipartition(rows, ALL ^ deleted)
        if not okay:
            continue
        forbidden = 0
        for left, right in components:
            forbidden |= SAME_SIDE_PAIR_MASKS[left] | SAME_SIDE_PAIR_MASKS[right]
        compatible |= needed & ~forbidden
        if compatible == needed:
            break
    return compatible


def has_k4_minor(rows: tuple[int, ...]) -> bool:
    """Recognize a ``K_4`` minor by exact series reduction.

    A graph is ``K_4``-minor-free exactly when it has treewidth at most two.
    Deleting a vertex of degree at most one, or suppressing a degree-two
    vertex after joining its neighbours, preserves the presence of a
    ``K_4`` minor.  If no such vertex remains on at least four vertices, the
    remaining minimum-degree-three graph has a ``K_4`` minor.
    """
    adjacency = list(rows)
    active = ALL
    while active.bit_count() >= 4:
        vertex = next(
            (
                candidate
                for candidate in range(ORDER)
                if active >> candidate & 1
                and (adjacency[candidate] & active).bit_count() <= 2
            ),
            None,
        )
        if vertex is None:
            return True
        neighbours = adjacency[vertex] & active
        if neighbours.bit_count() == 2:
            first_bit = neighbours & -neighbours
            second_bit = neighbours ^ first_bit
            first = first_bit.bit_length() - 1
            second = second_bit.bit_length() - 1
            adjacency[first] |= second_bit
            adjacency[second] |= first_bit
        active ^= 1 << vertex
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
        independent = independent_masks(rows)
        if any(independent[mask] for mask in SUBSETS_BY_SIZE[5]):
            continue
        if not is_colourable(rows, 4):
            continue
        eligible_graph_count += 1
        k4_minor_free = not has_k4_minor(rows)
        if k4_minor_free:
            k4_minor_free_graph_count += 1

        admitted = admissible_miss_pair_bits(rows)
        for vertex in range(ORDER):
            if any(
                independent[mask] and not (mask >> vertex & 1)
                for mask in SUBSETS_BY_SIZE[4]
            ):
                admitted &= ~FIRST_ENDPOINT_MASKS[vertex]
                admitted &= ~SECOND_ENDPOINT_MASKS[vertex]

        compatible = compatible_miss_pair_bits(rows, admitted)
        incompatible = admitted & ~compatible
        for miss_count, class_mask in enumerate(PAIR_CLASS_MASKS):
            eligible_count = (admitted & class_mask).bit_count()
            incompatible_count = (incompatible & class_mask).bit_count()
            eligible_instances[miss_count] += eligible_count
            incompatible_instances[miss_count] += incompatible_count
            if k4_minor_free:
                k4_minor_free_eligible[miss_count] += eligible_count
                k4_minor_free_incompatible[miss_count] += incompatible_count

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
