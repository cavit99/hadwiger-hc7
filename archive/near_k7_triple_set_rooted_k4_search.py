#!/usr/bin/env python3
"""Adversarial search for the exceptional-shell triple-set K4 lemma.

Build the homogeneous (c,c,a) shell with three 3-vertex pieces.  A neutral
triangle Q has common neighbours a,b,c and one private portal in each
piece for each neutral vertex.  Thus all three anti-nesting witnesses are
present.  Randomly delete optional shell-expansion edges while preserving
4-connectivity of H=G-Q, 7-connectivity of G, connected pieces, and every
required quotient contact.  Test exactly for a K4 model in H whose four
bags each meet all three Q-neighbour sets.

Finding a negative graph refutes the static triple-set lemma even under
the actual exceptional-shell hypotheses.  Persistent positivity is only
evidence, not a proof.
"""

from __future__ import annotations

import argparse
from itertools import combinations, product
import random

import networkx as nx


ROLES = {
    "a": (0,), "b": (1,), "c": (2,),
    "1": (3, 4, 5), "2": (6, 7, 8), "3": (9, 10, 11),
}
Q = (12, 13, 14)
ALLOWED_ROLE_EDGES = (
    ("b", "c"),
    ("a", "1"), ("b", "1"),
    ("a", "2"), ("b", "2"),
    ("b", "3"), ("c", "3"),
    ("1", "2"), ("2", "3"),
)
PORTAL_SETS = tuple(
    frozenset((0, 1, 2, 3 + i, 6 + i, 9 + i)) for i in range(3)
)


def role_of(vertex: int) -> str:
    return next(role for role, vertices in ROLES.items() if vertex in vertices)


def base_graph() -> tuple[nx.Graph, nx.Graph]:
    h = nx.Graph()
    h.add_nodes_from(range(12))
    for left, right in ALLOWED_ROLE_EDGES:
        h.add_edges_from((u, v) for u in ROLES[left] for v in ROLES[right])
    for role in "123":
        h.add_edges_from(combinations(ROLES[role], 2))
    g = h.copy()
    g.add_edges_from(combinations(Q, 2))
    for q in Q:
        g.add_edges_from((q, z) for z in (0, 1, 2))
    for i, q in enumerate(Q):
        g.add_edges_from((q, z) for z in (3 + i, 6 + i, 9 + i))
    return h, g


def valid_shell(h: nx.Graph) -> bool:
    if any(not nx.is_connected(h.subgraph(ROLES[role])) for role in "123"):
        return False
    contacts = {
        frozenset((role_of(u), role_of(v)))
        for u, v in h.edges() if role_of(u) != role_of(v)
    }
    required = {frozenset(pair) for pair in ALLOWED_ROLE_EDGES}
    return contacts == required


def with_q(h: nx.Graph) -> nx.Graph:
    g = h.copy()
    g.add_edges_from(combinations(Q, 2))
    for q in Q:
        g.add_edges_from((q, z) for z in (0, 1, 2))
    for i, q in enumerate(Q):
        g.add_edges_from((q, z) for z in (3 + i, 6 + i, 9 + i))
    return g


def with_portal_options(h: nx.Graph,
                        options: tuple[tuple[int, int, int], ...]) -> nx.Graph:
    g = h.copy()
    g.add_edges_from(combinations(Q, 2))
    for q in Q:
        g.add_edges_from((q, z) for z in (0, 1, 2))
    for q, row in zip(Q, options):
        g.add_edges_from((q, z) for z in row)
    return g


def minimise(seed: int) -> nx.Graph:
    h, _ = base_graph()
    edges = list(h.edges())
    random.Random(seed).shuffle(edges)
    changed = True
    while changed:
        changed = False
        for edge in edges:
            if not h.has_edge(*edge):
                continue
            h.remove_edge(*edge)
            if (valid_shell(h) and nx.node_connectivity(h) >= 4
                    and nx.node_connectivity(with_q(h)) >= 7):
                changed = True
            else:
                h.add_edge(*edge)
        random.Random(seed + h.number_of_edges()).shuffle(edges)
    return h


def partitions(n: int, k: int = 4):
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


PORTAL_MASKS = tuple(sum(1 << z for z in row) for row in PORTAL_SETS)
RAINBOW_PARTITIONS = tuple(
    blocks for blocks in partitions(12)
    if all(all(block & portal for portal in PORTAL_MASKS) for block in blocks)
)


def adjacency(h: nx.Graph) -> tuple[int, ...]:
    rows = [0] * 12
    for u, v in h.edges():
        rows[u] |= 1 << v
        rows[v] |= 1 << u
    return tuple(rows)


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


def rainbow_k4(h: nx.Graph) -> tuple[int, ...] | None:
    adj = adjacency(h)
    for blocks in RAINBOW_PARTITIONS:
        if not all(connected(block, adj) for block in blocks):
            continue
        good = True
        for i, block in enumerate(blocks):
            neighbours = 0
            scan = block
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


def all_k4_models(h: nx.Graph) -> list[tuple[int, ...]]:
    adj = adjacency(h)
    models = []
    for blocks in partitions(12):
        if not all(connected(block, adj) for block in blocks):
            continue
        good = True
        for i, block in enumerate(blocks):
            neighbours = 0
            scan = block
            while scan:
                bit = scan & -scan
                scan ^= bit
                neighbours |= adj[bit.bit_length() - 1]
            if any(not (neighbours & blocks[j]) for j in range(i)):
                good = False
                break
        if good:
            models.append(blocks)
    return models


def portal_scan(h: nx.Graph) -> None:
    options = tuple(
        (x1, x2, x3)
        for x1 in ROLES["1"] for x2 in ROLES["2"] for x3 in ROLES["3"]
    )
    models = all_k4_models(h)
    print("all spanning K4 models", len(models))
    common = (1 << 0) | (1 << 1) | (1 << 2)
    coverage = []
    for row in options:
        portal = common | sum(1 << z for z in row)
        bits = 0
        for index, blocks in enumerate(models):
            if all(block & portal for block in blocks):
                bits |= 1 << index
        coverage.append(bits)
    tested = 0
    for i, j, k in product(range(len(options)), repeat=3):
        if i == j == k:
            continue  # this is the nested, not anti-nested, state
        if coverage[i] & coverage[j] & coverage[k]:
            continue
        tested += 1
        rows = (options[i], options[j], options[k])
        g = with_portal_options(h, rows)
        if nx.node_connectivity(g) >= 7:
            print("STATIC COUNTEREXAMPLE", "Hedges", h.number_of_edges(),
                  "portals", rows, "kappaG", nx.node_connectivity(g),
                  "edges", tuple(sorted(h.edges())))
            return
    print("portal scan: no 7-connected negative; nonmodel triples", tested)


def render(blocks: tuple[int, ...] | None) -> str:
    if blocks is None:
        return "NONE"
    return " | ".join(
        "{" + ",".join(str(z) for z in range(12) if block >> z & 1) + "}"
        for block in blocks
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--seeds", type=int, default=30)
    parser.add_argument("--portal-scan", action="store_true")
    parser.add_argument("--portal-seed", type=int, default=0)
    args = parser.parse_args()
    print("rainbow spanning partitions", len(RAINBOW_PARTITIONS))
    if args.portal_scan:
        h = minimise(args.portal_seed)
        portal_scan(h)
        return
    seen = set()
    for seed in range(args.seeds):
        h = minimise(seed)
        key = tuple(sorted(h.edges()))
        if key in seen:
            continue
        seen.add(key)
        witness = rainbow_k4(h)
        print("seed", seed, "edges", h.number_of_edges(),
              "kappaH", nx.node_connectivity(h),
              "kappaG", nx.node_connectivity(with_q(h)),
              "model", render(witness))
        if witness is None:
            print("COUNTEREXAMPLE EDGES", key)
            return
    print("distinct minimal graphs", len(seen), "all positive")


if __name__ == "__main__":
    main()
