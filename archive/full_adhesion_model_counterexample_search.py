#!/usr/bin/env python3
"""Random falsification of a full-adhesion/model-cover conjecture.

Build r pairwise-adjacent connected labelled bags covering r+1 terminals,
add two anticomplete vertices complete to the terminals, and search exactly
for a K_(r+1) minor.  This tests the static core of the proposed owner
exchange theorem; ambient connectivity is checked separately.
"""

from __future__ import annotations

import argparse
import itertools
import random

import networkx as nx


def connected_masks(g: nx.Graph) -> list[int]:
    n = len(g)
    out: list[int] = []
    for mask in range(1, 1 << n):
        nodes = [i for i in range(n) if mask >> i & 1]
        if nx.is_connected(g.subgraph(nodes)):
            out.append(mask)
    return out


def has_clique_minor(g: nx.Graph, order: int) -> bool:
    """Exact disjoint-connected-branch-set search for small graphs."""
    g = nx.convert_node_labels_to_integers(g)
    sets = connected_masks(g)
    nbrmask = [0] * len(sets)
    for i, a in enumerate(sets):
        na = 0
        for u in range(len(g)):
            if a >> u & 1:
                for v in g[u]:
                    na |= 1 << v
        nbrmask[i] = na

    # Larger sets first often exposes a model quickly; singleton clique
    # candidates remain included.
    sets.sort(key=lambda x: (-x.bit_count(), x))
    nbr_for = {}
    for a in sets:
        na = 0
        for u in range(len(g)):
            if a >> u & 1:
                for v in g[u]:
                    na |= 1 << v
        nbr_for[a] = na

    def rec(chosen: list[int], start: int, used: int) -> bool:
        if len(chosen) == order:
            return True
        for idx in range(start, len(sets)):
            s = sets[idx]
            if s & used:
                continue
            if all(nbr_for[s] & t for t in chosen):
                if rec(chosen + [s], idx + 1, used | s):
                    return True
        return False

    return rec([], 0, 0)


def random_instance(r: int, rng: random.Random) -> tuple[nx.Graph, list[set[int]], set[int]]:
    # Each bag is a random tree of order 1--3 initially.
    g = nx.Graph()
    bags: list[set[int]] = []
    nxt = 0
    for _ in range(r):
        size = rng.randint(1, 3)
        bag = set(range(nxt, nxt + size))
        g.add_nodes_from(bag)
        if size >= 2:
            tree = nx.random_labeled_tree(size, seed=rng.randrange(1 << 30))
            g.add_edges_from((nxt + u, nxt + v) for u, v in tree.edges())
        bags.append(bag)
        nxt += size

    # One arbitrary edge per pair of bags, plus occasional redundant edges.
    for i, j in itertools.combinations(range(r), 2):
        u, v = rng.choice(tuple(bags[i])), rng.choice(tuple(bags[j]))
        g.add_edge(u, v)
        if rng.random() < 0.2:
            g.add_edge(rng.choice(tuple(bags[i])), rng.choice(tuple(bags[j])))

    # r+1 distinct terminal vertices, distributed arbitrarily among bags;
    # if needed enlarge bags by terminal leaves.
    terminals: set[int] = set()
    owners = [rng.randrange(r) for _ in range(r + 1)]
    for owner in owners:
        z = nxt
        nxt += 1
        g.add_node(z)
        g.add_edge(z, rng.choice(tuple(bags[owner])))
        bags[owner].add(z)
        terminals.add(z)

    a, b = nxt, nxt + 1
    g.add_nodes_from([a, b])
    for z in terminals:
        g.add_edges_from([(a, z), (b, z)])
    return g, bags, terminals


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--r", type=int, default=4)
    parser.add_argument("--trials", type=int, default=1000)
    parser.add_argument("--seed", type=int, default=1)
    args = parser.parse_args()
    rng = random.Random(args.seed)
    for trial in range(args.trials):
        g, bags, terminals = random_instance(args.r, rng)
        if not has_clique_minor(g, args.r + 1):
            print("STATIC_COUNTEREXAMPLE", trial)
            print("connectivity", nx.node_connectivity(g))
            print("terminals", sorted(terminals))
            print("bags", [sorted(x) for x in bags])
            print("edges", sorted(tuple(sorted(e)) for e in g.edges()))
            return
    print("NO_COUNTEREXAMPLE", args.trials)


if __name__ == "__main__":
    main()
