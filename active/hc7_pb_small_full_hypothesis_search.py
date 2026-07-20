#!/usr/bin/env python3
"""Exact small-order search for the paired-rooted pentagonal-bipyramid target.

This is a finite experiment, not an unbounded proof.  It enumerates unlabelled
graphs with minimum degree at least five using ``geng``.  For every graph it
checks, exactly:

* five-connectivity;
* failure of four-colourability;
* every connected seven-part partition whose contact graph is the
  pentagonal bipyramid; and
* every choice of one A-root and one B-root in each part.

For each resulting full-hypothesis instance it exhaustively searches all five
pairwise disjoint connected branch sets that are pairwise adjacent and each
meet both root sets.  Testing one root of each kind per part loses no possible
counterexample: any larger A and B contain such a choice, and a model for the
smaller root sets is also a model for the larger ones.

Expected invocation from the repository root:

    .venv/bin/python active/hc7_pb_small_full_hypothesis_search.py --max-order 9

The program stops and prints a complete small instance if it finds a failure.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from itertools import combinations, product
import shutil
import subprocess
import sys
import tempfile
from typing import Iterable, Iterator

import networkx as nx


PARTS = 7


@dataclass
class OrderStats:
    generated: int = 0
    five_connected: int = 0
    non_four_colourable: int = 0
    pb_partitions: int = 0
    endpoint_instances: int = 0


def bit_vertices(mask: int) -> Iterator[int]:
    while mask:
        bit = mask & -mask
        yield bit.bit_length() - 1
        mask ^= bit


def adjacency_masks(graph: nx.Graph) -> tuple[int, ...]:
    return tuple(sum(1 << v for v in graph.neighbors(u)) for u in graph)


def connected_mask(mask: int, adjacency: tuple[int, ...]) -> bool:
    if not mask:
        return False
    reached = mask & -mask
    frontier = reached
    while frontier:
        bit = frontier & -frontier
        frontier ^= bit
        vertex = bit.bit_length() - 1
        new = adjacency[vertex] & mask & ~reached
        reached |= new
        frontier |= new
    return reached == mask


def is_five_connected(adjacency: tuple[int, ...]) -> bool:
    n = len(adjacency)
    full = (1 << n) - 1
    if n <= 5 or any(mask.bit_count() < 5 for mask in adjacency):
        return False
    vertices = range(n)
    for order in range(5):
        for removed_vertices in combinations(vertices, order):
            removed = sum(1 << v for v in removed_vertices)
            if not connected_mask(full ^ removed, adjacency):
                return False
    return True


def is_four_colourable(adjacency: tuple[int, ...]) -> bool:
    """Exact DSATUR backtracking with four colours."""
    n = len(adjacency)
    colours = [-1] * n

    def search(coloured: int) -> bool:
        if coloured == n:
            return True
        best = -1
        best_key = (-1, -1)
        for vertex in range(n):
            if colours[vertex] >= 0:
                continue
            used = {
                colours[other]
                for other in bit_vertices(adjacency[vertex])
                if colours[other] >= 0
            }
            key = (len(used), adjacency[vertex].bit_count())
            if key > best_key:
                best = vertex
                best_key = key
        forbidden = {
            colours[other]
            for other in bit_vertices(adjacency[best])
            if colours[other] >= 0
        }
        for colour in range(4):
            if colour in forbidden:
                continue
            colours[best] = colour
            if search(coloured + 1):
                return True
            colours[best] = -1
        return False

    return search(0)


def seven_partitions(n: int) -> Iterator[tuple[int, ...]]:
    """Yield all unlabelled partitions of [n] into seven nonempty masks."""
    labels = [0] * n

    def rec(position: int, maximum: int) -> Iterator[tuple[int, ...]]:
        if position == n:
            if maximum == PARTS - 1:
                masks = [0] * PARTS
                for vertex, label in enumerate(labels):
                    masks[label] |= 1 << vertex
                yield tuple(masks)
            return
        remaining_after = n - position - 1
        for label in range(min(maximum + 1, PARTS - 1) + 1):
            new_maximum = max(maximum, label)
            missing_labels = PARTS - 1 - new_maximum
            if missing_labels > remaining_after:
                continue
            labels[position] = label
            yield from rec(position + 1, new_maximum)

    yield from rec(1, 0)


def contact_is_pentagonal_bipyramid(
    parts: tuple[int, ...], adjacency: tuple[int, ...]
) -> bool:
    quotient = [0] * PARTS
    for i, left in enumerate(parts):
        neighbours = 0
        for vertex in bit_vertices(left):
            neighbours |= adjacency[vertex]
        for j in range(i + 1, PARTS):
            if neighbours & parts[j]:
                quotient[i] |= 1 << j
                quotient[j] |= 1 << i
    degrees = [mask.bit_count() for mask in quotient]
    if sorted(degrees) != [4, 4, 4, 4, 4, 5, 5]:
        return False
    apices = [i for i, degree in enumerate(degrees) if degree == 5]
    if quotient[apices[0]] & (1 << apices[1]):
        return False
    rim = [i for i, degree in enumerate(degrees) if degree == 4]
    rim_mask = sum(1 << i for i in rim)
    if any((quotient[i] & rim_mask).bit_count() != 2 for i in rim):
        return False
    reached = 1 << rim[0]
    frontier = reached
    while frontier:
        bit = frontier & -frontier
        frontier ^= bit
        vertex = bit.bit_length() - 1
        new = quotient[vertex] & rim_mask & ~reached
        reached |= new
        frontier |= new
    return reached == rim_mask


def connected_pb_partitions(
    n: int, adjacency: tuple[int, ...]
) -> Iterator[tuple[int, ...]]:
    for parts in seven_partitions(n):
        if not all(connected_mask(part, adjacency) for part in parts):
            continue
        if contact_is_pentagonal_bipyramid(parts, adjacency):
            yield parts


def endpoint_choices(parts: tuple[int, ...]) -> Iterator[tuple[int, int]]:
    per_part = []
    for part in parts:
        vertices = tuple(bit_vertices(part))
        per_part.append(tuple(product(vertices, repeat=2)))
    for choices in product(*per_part):
        a_mask = sum(1 << a for a, _ in choices)
        b_mask = sum(1 << b for _, b in choices)
        yield a_mask, b_mask


def connected_subsets(adjacency: tuple[int, ...]) -> tuple[int, ...]:
    n = len(adjacency)
    return tuple(
        mask
        for mask in range(1, 1 << n)
        if connected_mask(mask, adjacency)
    )


def bags_adjacent(
    left: int, right: int, adjacency: tuple[int, ...]
) -> bool:
    neighbours = 0
    for vertex in bit_vertices(left):
        neighbours |= adjacency[vertex]
    return bool(neighbours & right)


def paired_rooted_k5(
    adjacency: tuple[int, ...],
    all_connected: tuple[int, ...],
    a_mask: int,
    b_mask: int,
) -> tuple[int, ...] | None:
    n = len(adjacency)
    candidates = tuple(
        mask
        for mask in all_connected
        if mask & a_mask
        and mask & b_mask
        and mask.bit_count() <= n - 4
    )
    compatibility = [0] * len(candidates)
    for i, left in enumerate(candidates):
        compatible = 0
        for j in range(i + 1, len(candidates)):
            right = candidates[j]
            if left & right:
                continue
            if bags_adjacent(left, right, adjacency):
                compatible |= 1 << j
        compatibility[i] = compatible

    def search(available: int, chosen: tuple[int, ...]) -> tuple[int, ...] | None:
        need = 5 - len(chosen)
        if need == 0:
            return chosen
        if available.bit_count() < need:
            return None
        while available:
            bit = available & -available
            available ^= bit
            index = bit.bit_length() - 1
            answer = search(available & compatibility[index], chosen + (candidates[index],))
            if answer is not None:
                return answer
        return None

    return search((1 << len(candidates)) - 1, ())


def graph6_stream(geng: str, order: int) -> Iterable[tuple[str, nx.Graph]]:
    command = [geng, "-cq", "-d5", str(order)]
    with tempfile.TemporaryFile(mode="w+") as stderr_file:
        process = subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            stderr=stderr_file,
            text=True,
        )
        assert process.stdout is not None
        completed = False
        try:
            for line in process.stdout:
                graph6 = line.strip()
                if graph6:
                    yield graph6, nx.from_graph6_bytes(graph6.encode("ascii"))
            completed = True
        finally:
            process.stdout.close()
            if process.poll() is None:
                process.terminate()
            return_code = process.wait()
        if completed and return_code:
            stderr_file.seek(0)
            stderr = stderr_file.read().strip()
            raise RuntimeError(f"geng failed with status {return_code}: {stderr}")


def mask_list(mask: int) -> list[int]:
    return list(bit_vertices(mask))


def search_order(geng: str, order: int) -> tuple[OrderStats, bool]:
    stats = OrderStats()
    for graph6, graph in graph6_stream(geng, order):
        stats.generated += 1
        adjacency = adjacency_masks(graph)
        if not is_five_connected(adjacency):
            continue
        stats.five_connected += 1
        if is_four_colourable(adjacency):
            continue
        stats.non_four_colourable += 1
        all_connected = connected_subsets(adjacency)
        for parts in connected_pb_partitions(order, adjacency):
            stats.pb_partitions += 1
            for a_mask, b_mask in endpoint_choices(parts):
                stats.endpoint_instances += 1
                if paired_rooted_k5(adjacency, all_connected, a_mask, b_mask) is not None:
                    continue
                print("COUNTEREXAMPLE_CANDIDATE")
                print(f"order={order}")
                print(f"graph6={graph6}")
                print(f"edges={sorted(tuple(sorted(edge)) for edge in graph.edges())}")
                print(f"parts={[mask_list(part) for part in parts]}")
                print(f"A={mask_list(a_mask)}")
                print(f"B={mask_list(b_mask)}")
                return stats, True
    return stats, False


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--min-order", type=int, default=7)
    parser.add_argument("--max-order", type=int, default=9)
    args = parser.parse_args()
    if args.min_order < 7 or args.max_order < args.min_order:
        parser.error("require 7 <= min-order <= max-order")
    geng = shutil.which("geng")
    if geng is None:
        parser.error("geng is required but was not found on PATH")

    for order in range(args.min_order, args.max_order + 1):
        stats, found = search_order(geng, order)
        print(
            f"order={order} generated={stats.generated} "
            f"five_connected={stats.five_connected} "
            f"non_four_colourable={stats.non_four_colourable} "
            f"pb_partitions={stats.pb_partitions} "
            f"endpoint_instances={stats.endpoint_instances}"
        )
        if found:
            return 1
    print("NO_COUNTEREXAMPLE_IN_SEARCHED_ORDERS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
