#!/usr/bin/env python3
"""Exact one-defect census for the two-transition HC7 boundary.

For n in {7,8,9}, read the complete graph6 catalogue from stdin.  Retain
boundary graphs H satisfying the promoted static conditions

    chi(H) <= 4,  alpha(H) <= n-5.

Optional filters spend further hypotheses that are genuinely available in
the corresponding proof branch:

* ``--nonsplit`` removes split boundaries, which already synchronize;
* ``--join-target`` requires the quotient ``overline(K_2) join H`` to avoid
  K7 or K7-minus.  In a K7-minus-minor-free host, the latter is mandatory,
  since this quotient is obtained by contracting the two full open shores.

For every pair e,f of vertex-disjoint nonedges, put J=H+e+f and ask whether
J contains K6-minus as a minor.  Such a model lifts through the two literal
disjoint host paths, and adjoining the low-degree vertex gives K7-minus.

All minor tests are exact.  Since the largest tested quotient has order 11,
every possible model is one of the precomputed partitions of an arbitrary
vertex subset into the required number of connected branch sets.
"""

from __future__ import annotations

import argparse
from collections import Counter
from functools import lru_cache
from itertools import combinations
import json
import sys

import networkx as nx


def graph6(graph: nx.Graph) -> str:
    return nx.to_graph6_bytes(graph, header=False).decode().strip()


def adjacency_masks(graph: nx.Graph) -> tuple[int, ...]:
    vertices = tuple(sorted(graph.nodes()))
    assert vertices == tuple(range(len(vertices)))
    masks = [0] * len(vertices)
    for u, v in graph.edges():
        masks[u] |= 1 << v
        masks[v] |= 1 << u
    return tuple(masks)


@lru_cache(maxsize=None)
def set_partitions_with_unused(n: int, k: int) -> tuple[tuple[int, ...], ...]:
    """All partitions of an arbitrary subset of [n] into exactly k blocks."""

    result: list[tuple[int, ...]] = []
    labels = [-2] * n

    def rec(i: int, used: int) -> None:
        remaining = n - i
        if used > k or used + remaining < k:
            return
        if i == n:
            if used != k:
                return
            blocks = [0] * k
            for v, label in enumerate(labels):
                if label >= 0:
                    blocks[label] |= 1 << v
            result.append(tuple(blocks))
            return

        labels[i] = -1
        rec(i + 1, used)

        for label in range(used):
            labels[i] = label
            rec(i + 1, used)

        if used < k:
            labels[i] = used
            rec(i + 1, used + 1)

        labels[i] = -2

    rec(0, 0)
    result.sort(key=lambda blocks: (sum(mask.bit_count() for mask in blocks), blocks))
    return tuple(result)


def connected_and_neighbour_masks(
    adj: tuple[int, ...],
) -> tuple[tuple[bool, ...], tuple[int, ...]]:
    n = len(adj)
    connected = [False] * (1 << n)
    neighbours = [0] * (1 << n)
    for mask in range(1, 1 << n):
        seed = mask & -mask
        seen = seed
        while True:
            nxt = seen
            todo = seen
            while todo:
                bit = todo & -todo
                todo -= bit
                nxt |= adj[bit.bit_length() - 1] & mask
            if nxt == seen:
                break
            seen = nxt
        connected[mask] = seen == mask

        hood = 0
        todo = mask
        while todo:
            bit = todo & -todo
            todo -= bit
            hood |= adj[bit.bit_length() - 1]
        neighbours[mask] = hood & ~mask
    return tuple(connected), tuple(neighbours)


def clique_minor_model(
    graph: nx.Graph,
    order: int,
    allowed_missing: int,
) -> tuple[int, ...] | None:
    """Return an exact branch-set model with at most allowed_missing nonedges."""

    n = graph.number_of_nodes()
    adj = adjacency_masks(graph)
    connected, neighbours = connected_and_neighbour_masks(adj)

    for blocks in set_partitions_with_unused(n, order):
        if any(not connected[block] for block in blocks):
            continue
        missing = 0
        for i, j in combinations(range(order), 2):
            if not (neighbours[blocks[i]] & blocks[j]):
                missing += 1
                if missing > allowed_missing:
                    break
        if missing <= allowed_missing:
            return blocks
    return None


def independence_number_at_most(graph: nx.Graph, bound: int) -> bool:
    n = graph.number_of_nodes()
    adj = adjacency_masks(graph)
    for mask in range(1 << n):
        if mask.bit_count() <= bound:
            continue
        independent = True
        todo = mask
        while todo:
            bit = todo & -todo
            todo -= bit
            v = bit.bit_length() - 1
            if adj[v] & todo:
                independent = False
                break
        if independent:
            return False
    return True


def is_k_colourable(graph: nx.Graph, k: int) -> bool:
    n = graph.number_of_nodes()
    adj = adjacency_masks(graph)
    order = sorted(range(n), key=lambda v: (adj[v].bit_count(), v), reverse=True)
    colour = [-1] * n

    def rec(i: int) -> bool:
        if i == n:
            return True
        v = order[i]
        forbidden = 0
        todo = adj[v]
        while todo:
            bit = todo & -todo
            todo -= bit
            c = colour[bit.bit_length() - 1]
            if c >= 0:
                forbidden |= 1 << c
        for c in range(k):
            if forbidden & (1 << c):
                continue
            colour[v] = c
            if rec(i + 1):
                return True
            colour[v] = -1
        return False

    return rec(0)


def is_split(graph: nx.Graph) -> bool:
    """Exact split-graph test by all clique/independent-set partitions."""

    n = graph.number_of_nodes()
    adj = adjacency_masks(graph)
    all_vertices = (1 << n) - 1
    for clique in range(1 << n):
        independent = all_vertices ^ clique
        good = True
        todo = clique
        while todo and good:
            bit = todo & -todo
            todo -= bit
            v = bit.bit_length() - 1
            if (todo & ~adj[v]) != 0:
                good = False
        if not good:
            continue
        todo = independent
        while todo and good:
            bit = todo & -todo
            todo -= bit
            v = bit.bit_length() - 1
            if todo & adj[v]:
                good = False
        if good:
            return True
    return False


def two_shore_quotient(graph: nx.Graph) -> nx.Graph:
    """Return overline(K2) join H with canonical integer labels."""

    n = graph.number_of_nodes()
    quotient = graph.copy()
    quotient.add_nodes_from((n, n + 1))
    quotient.add_edges_from((apex, v) for apex in (n, n + 1) for v in range(n))
    return quotient


def invariant_signature(graph: nx.Graph) -> str:
    complement = nx.complement(graph)
    component_orders = sorted(len(component) for component in nx.connected_components(graph))
    complement_components = sorted(
        len(component) for component in nx.connected_components(complement)
    )
    degrees = sorted(dict(graph.degree()).values())
    complement_degrees = sorted(dict(complement.degree()).values())
    return (
        f"m{graph.number_of_edges()}"
        f"-c{','.join(map(str, component_orders))}"
        f"-d{','.join(map(str, degrees))}"
        f"-bc{','.join(map(str, complement_components))}"
        f"-bd{','.join(map(str, complement_degrees))}"
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--order", type=int, choices=(7, 8, 9), required=True)
    parser.add_argument("--survivor-limit", type=int, default=1000)
    parser.add_argument("--nonsplit", action="store_true")
    parser.add_argument(
        "--join-target",
        choices=("none", "k7", "k7minus"),
        default="none",
        help="minor forbidden in overline(K2) join H",
    )
    args = parser.parse_args()

    n = args.order
    counts = {
        "graphs": 0,
        "static_boundaries": 0,
        "nonsplit_boundaries": 0,
        "join_target_free_boundaries": 0,
        "disjoint_nonedge_pairs": 0,
        "k6minus_positive": 0,
        "k6minus_survivors": 0,
    }
    survivors: list[dict[str, object]] = []
    survivor_boundaries: Counter[str] = Counter()
    survivor_signatures: Counter[str] = Counter()

    for raw in sys.stdin:
        raw = raw.strip()
        if not raw or raw.startswith(">>"):
            continue
        graph = nx.from_graph6_bytes(raw.encode())
        graph = nx.convert_node_labels_to_integers(graph, ordering="sorted")
        assert graph.number_of_nodes() == n
        counts["graphs"] += 1

        if not independence_number_at_most(graph, n - 5):
            continue
        if not is_k_colourable(graph, 4):
            continue
        counts["static_boundaries"] += 1

        if args.nonsplit and is_split(graph):
            continue
        counts["nonsplit_boundaries"] += 1

        if args.join_target != "none":
            quotient = two_shore_quotient(graph)
            allowed_missing = 0 if args.join_target == "k7" else 1
            if clique_minor_model(quotient, 7, allowed_missing) is not None:
                continue
        counts["join_target_free_boundaries"] += 1

        nonedges = [
            (u, v)
            for u, v in combinations(range(n), 2)
            if not graph.has_edge(u, v)
        ]
        for e, f in combinations(nonedges, 2):
            if set(e) & set(f):
                continue
            counts["disjoint_nonedge_pairs"] += 1
            augmented = graph.copy()
            augmented.add_edges_from((e, f))
            model = clique_minor_model(augmented, 6, 1)
            if model is not None:
                counts["k6minus_positive"] += 1
                continue

            counts["k6minus_survivors"] += 1
            code = graph6(graph)
            survivor_boundaries[code] += 1
            survivor_signatures[invariant_signature(graph)] += 1
            if len(survivors) < args.survivor_limit:
                survivors.append(
                    {
                        "H": code,
                        "e": list(e),
                        "f": list(f),
                        "J": graph6(augmented),
                        "signature": invariant_signature(graph),
                    }
                )

    result = {
        "order": n,
        "nonsplit": args.nonsplit,
        "join_target": args.join_target,
        "partition_counts": {
            "k6minus": len(set_partitions_with_unused(n, 6)),
            "join": (
                len(set_partitions_with_unused(n + 2, 7))
                if args.join_target != "none"
                else 0
            ),
        },
        "counts": counts,
        "survivor_boundary_type_count": len(survivor_boundaries),
        "survivor_boundaries": dict(sorted(survivor_boundaries.items())),
        "survivor_signatures": dict(sorted(survivor_signatures.items())),
        "survivors_truncated": counts["k6minus_survivors"] > len(survivors),
        "survivors": survivors,
    }
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
