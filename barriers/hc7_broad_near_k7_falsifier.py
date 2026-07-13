#!/usr/bin/env python3
"""Small-order falsifier for the broad near-K7 -> two-apex claim.

The input is a graph6 stream describing *complements*.  This is convenient
for seven-connected graphs: at order n their complements have maximum
degree at most n-8.  Each complement is inverted and subjected to exact
tests for

* vertex connectivity at least seven;
* a K7 minor (by all spanning connected seven-block partitions);
* two-apexness (all deletion pairs and exact planarity); and
* a K7^vee minor when needed.

For a connected graph every clique-minor model can be extended to a
spanning model: attach each component outside the model to an adjacent
branch set, one component at a time.  Consequently the spanning-partition
search is complete, not merely a heuristic.
"""

from __future__ import annotations

import argparse
from functools import lru_cache
from itertools import combinations
import sys

import networkx as nx


def adjacency_rows(graph: nx.Graph) -> tuple[tuple[int, ...], list[int]]:
    names = tuple(graph)
    index = {v: i for i, v in enumerate(names)}
    rows = [0] * len(names)
    for u, v in graph.edges:
        i, j = index[u], index[v]
        rows[i] |= 1 << j
        rows[j] |= 1 << i
    return names, rows


def spanning_quotients(
    graph: nx.Graph, block_count: int = 7
):
    """Yield every connected spanning block partition and its quotient.

    Blocks are generated in restricted-growth order, so each unordered
    partition occurs exactly once.  ``quotient[i]`` is the bitset of other
    blocks adjacent to block i.
    """

    names, rows = adjacency_rows(graph)
    n = len(names)
    blocks: list[list[int]] = []

    @lru_cache(maxsize=None)
    def connected(mask: int) -> bool:
        reached = mask & -mask
        while reached:
            old = reached
            bits = reached
            while bits:
                bit = bits & -bits
                bits ^= bit
                reached |= rows[bit.bit_length() - 1] & mask
            if reached == old:
                return reached == mask
        return False

    def rec(pos: int):
        if pos == n:
            if len(blocks) != block_count:
                return
            masks = [sum(1 << v for v in block) for block in blocks]
            if not all(connected(mask) for mask in masks):
                return
            quotient = [0] * block_count
            for i in range(block_count):
                neighbourhood = 0
                for v in blocks[i]:
                    neighbourhood |= rows[v]
                for j in range(i):
                    if neighbourhood & masks[j]:
                        quotient[i] |= 1 << j
                        quotient[j] |= 1 << i
            yield tuple(tuple(names[v] for v in block) for block in blocks), quotient
            return

        remaining = n - pos
        if len(blocks) + remaining < block_count:
            return

        for block in blocks:
            block.append(pos)
            yield from rec(pos + 1)
            block.pop()
        if len(blocks) < block_count:
            blocks.append([pos])
            yield from rec(pos + 1)
            blocks.pop()

    yield from rec(0)


def exact_minor_models(
    graph: nx.Graph,
) -> tuple[tuple[tuple[object, ...], ...] | None, tuple[tuple[object, ...], ...] | None, int]:
    """Return exact K7 and K7^vee witnesses (if any), plus partitions seen.

    K7^vee is K7 with two incident edges deleted.  A seven-vertex quotient
    contains it exactly when it has six vertices inducing K6 and the seventh
    vertex has at least four neighbours in that K6.
    """

    k7 = None
    vee = None
    checked = 0
    full = (1 << 7) - 1
    for blocks, quotient in spanning_quotients(graph, 7):
        checked += 1
        if k7 is None and all(row.bit_count() == 6 for row in quotient):
            k7 = blocks
            # A K7 witness is automatically also a K7^vee witness.
            if vee is None:
                vee = blocks
            break
        if vee is None:
            for centre in range(7):
                rim = full ^ (1 << centre)
                if (quotient[centre] & rim).bit_count() < 4:
                    continue
                if all(
                    (quotient[v] & (rim ^ (1 << v))).bit_count() == 5
                    for v in range(7)
                    if rim >> v & 1
                ):
                    vee = blocks
                    break
    return k7, vee, checked


def planarizing_pairs(graph: nx.Graph) -> list[tuple[object, object]]:
    pairs = []
    vertices = tuple(graph)
    for pair in combinations(vertices, 2):
        remainder = graph.subgraph(set(vertices) - set(pair))
        if nx.check_planarity(remainder, counterexample=False)[0]:
            pairs.append(pair)
    return pairs


def process(graph: nx.Graph) -> dict[str, object] | None:
    connectivity = nx.node_connectivity(graph)
    if connectivity < 7:
        return None
    apex_pairs = planarizing_pairs(graph)
    # A two-apex graph is not a counterexample to the broad dichotomy.  The
    # exact minor search is expensive, so test it only after this filter.
    if apex_pairs:
        return {"kind": "two-apex", "kappa": connectivity, "pairs": apex_pairs}
    k7, vee, checked = exact_minor_models(graph)
    if k7 is not None:
        return {"kind": "K7", "kappa": connectivity, "model": k7, "checked": checked}
    # If K7 is absent, exact_minor_models exhausted all partitions and hence
    # also completed the K7^vee test.
    return {
        "kind": "candidate" if vee is not None else "no-vee",
        "kappa": connectivity,
        "vee_model": vee,
        "checked": checked,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--complements",
        action="store_true",
        help="interpret each graph6 input graph as the complement of the host",
    )
    parser.add_argument("--stop", action="store_true", help="stop at first candidate")
    args = parser.parse_args()

    counts: dict[str, int] = {}
    read = 0
    tested = 0
    for raw in sys.stdin.buffer:
        raw = raw.strip()
        if not raw:
            continue
        read += 1
        graph = nx.from_graph6_bytes(raw)
        if args.complements:
            graph = nx.complement(graph)
        result = process(graph)
        if result is None:
            counts["connectivity<7"] = counts.get("connectivity<7", 0) + 1
            continue
        tested += 1
        kind = str(result["kind"])
        counts[kind] = counts.get(kind, 0) + 1
        if kind in {"candidate", "no-vee"}:
            code = nx.to_graph6_bytes(graph, header=False).decode().strip()
            print({"graph6": code, **result}, flush=True)
            if kind == "candidate" and args.stop:
                break

    print({"read": read, "seven_connected": tested, "counts": counts})


if __name__ == "__main__":
    main()
