#!/usr/bin/env python3
"""Small-witness search for failures of Kriesell--Mohr property (*).

Every colour class has two vertices: its prescribed root and one auxiliary
vertex.  Edges are sampled only between colour pairs prescribed by the
routing graph.  A rooted model is checked exhaustively by assigning every
auxiliary vertex to one of the root bags or leaving it unused.

This is a falsification tool, not a proof of property (*).
"""

from __future__ import annotations

import argparse
import itertools
import random

import networkx as nx


def local_patterns() -> list[tuple[tuple[int, int], ...]]:
    """All edge sets in K_{2,2} connecting the two 0-labelled roots."""
    possible = ((0, 0), (0, 1), (1, 0), (1, 1))
    out = []
    for mask in range(1, 1 << 4):
        edges = tuple(possible[i] for i in range(4) if mask & (1 << i))
        h = nx.Graph()
        h.add_nodes_from(((0, 0), (0, 1), (1, 0), (1, 1)))
        h.add_edges_from(((0, a), (1, b)) for a, b in edges)
        if nx.has_path(h, (0, 0), (1, 0)):
            out.append(edges)
    return out


PATTERNS = local_patterns()
MINIMAL_PATTERNS = [((0, 0),), ((0, 1), (1, 0), (1, 1))]


def rooted_model(g: nx.Graph, target: nx.Graph, k: int) -> tuple[int, ...] | None:
    roots = [(i, 0) for i in range(k)]
    extras = sorted(set(g) - set(roots))
    nodes = roots + extras
    index = {v: i for i, v in enumerate(nodes)}
    # Bit positions 0..k-1 are roots; the remaining positions are auxiliaries.
    adj = [0] * len(nodes)
    for x, y in g.edges:
        u, v = index[x], index[y]
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    def connected(vertices: int) -> bool:
        seen = vertices & -vertices
        frontier = seen
        while frontier:
            xbit = frontier & -frontier
            frontier ^= xbit
            x = xbit.bit_length() - 1
            new = adj[x] & vertices & ~seen
            seen |= new
            frontier |= new
        return seen == vertices

    candidates: list[list[tuple[int, int, int]]] = []
    for root in range(k):
        row = []
        for extras_mask in range(1 << len(extras)):
            vertices = (1 << root) | (extras_mask << k)
            if connected(vertices):
                neighborhood = 0
                bits = vertices
                while bits:
                    xbit = bits & -bits
                    bits ^= xbit
                    neighborhood |= adj[xbit.bit_length() - 1]
                row.append((extras_mask, vertices, neighborhood))
        candidates.append(row)

    order = sorted(range(k), key=target.degree, reverse=True)
    chosen: dict[int, tuple[int, int, int]] = {}

    def dfs(pos: int, used_extras: int) -> tuple[int, ...] | None:
        if pos == k:
            assignment = [k] * len(extras)
            for bag, (mask, _, _) in chosen.items():
                for extra in range(len(extras)):
                    if mask & (1 << extra):
                        assignment[extra] = bag
            return tuple(assignment)
        bag = order[pos]
        for cand in candidates[bag]:
            mask, vertices, neighborhood = cand
            if mask & used_extras:
                continue
            if any(
                other in chosen
                and not (neighborhood & chosen[other][1])
                for other in target.neighbors(bag)
            ):
                continue
            chosen[bag] = cand
            answer = dfs(pos + 1, used_extras | mask)
            if answer is not None:
                return answer
            del chosen[bag]
        return None

    return dfs(0, 0)


def sample_graph(target: nx.Graph, rng: random.Random) -> nx.Graph:
    k = target.number_of_nodes()
    g = nx.Graph()
    g.add_nodes_from((i, bit) for i in range(k) for bit in range(2))
    for u, v in target.edges:
        pattern = rng.choice(PATTERNS)
        g.add_edges_from(((u, a), (v, b)) for a, b in pattern)
    return g


def sample_path_graph(
    target: nx.Graph, rng: random.Random, sizes: tuple[int, ...]
) -> nx.Graph:
    """Sample a minimal witness: one alternating root path per target edge."""
    g = nx.Graph()
    g.add_nodes_from((c, i) for c, size in enumerate(sizes) for i in range(size))
    for u, v in target.edges:
        paths = alternating_paths(u, v, sizes)
        path = rng.choice(paths)
        g.add_edges_from(zip(path, path[1:]))
    return g


def targets() -> dict[str, nx.Graph]:
    k33 = nx.complete_bipartite_graph(3, 3)
    k24 = nx.complete_bipartite_graph(2, 4)
    theta = nx.Graph()
    theta.add_nodes_from(range(6))
    # Three internally disjoint 0--1 paths of lengths 2, 2, and 3.
    theta.add_edges_from(((0, 2), (2, 1), (0, 3), (3, 1),
                          (0, 4), (4, 5), (5, 1)))
    return {"k33": k33, "k24": k24, "theta": theta}


def alternating_paths(u: int, v: int, sizes: tuple[int, ...]) -> list[tuple[tuple[int, int], ...]]:
    """All simple alternating root-to-root paths for one colour pair."""
    left = [(u, i) for i in range(1, sizes[u])]
    right = [(v, i) for i in range(1, sizes[v])]
    out = [((u, 0), (v, 0))]
    for length in range(1, min(len(left), len(right)) + 1):
        for lseq in itertools.permutations(left, length):
            for rseq in itertools.permutations(right, length):
                path = [(u, 0)]
                for rv, lv in zip(rseq, lseq):
                    path.extend((rv, lv))
                path.append((v, 0))
                out.append(tuple(path))
    return out


def exhaustive_path_graphs(target: nx.Graph, sizes: tuple[int, ...]):
    edge_paths = [alternating_paths(u, v, sizes) for u, v in target.edges]
    for chosen in itertools.product(*edge_paths):
        g = nx.Graph()
        g.add_nodes_from((c, i) for c, size in enumerate(sizes) for i in range(size))
        for path in chosen:
            g.add_edges_from(zip(path, path[1:]))
        yield g


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("target", choices=targets())
    parser.add_argument("--trials", type=int, default=10000)
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--exhaustive-minimal", action="store_true")
    parser.add_argument(
        "--sizes",
        help="comma-separated class sizes; exhaust all minimal alternating paths",
    )
    parser.add_argument(
        "--random-sizes",
        help="comma-separated class sizes; randomly sample minimal alternating paths",
    )
    args = parser.parse_args()
    target = targets()[args.target]
    rng = random.Random(args.seed)
    if args.sizes:
        sizes = tuple(map(int, args.sizes.split(",")))
        if len(sizes) != 6 or min(sizes) < 1:
            raise SystemExit("--sizes needs six positive integers")
        choices = exhaustive_path_graphs(target, sizes)
    elif args.random_sizes:
        sizes = tuple(map(int, args.random_sizes.split(",")))
        if len(sizes) != 6 or min(sizes) < 1:
            raise SystemExit("--random-sizes needs six positive integers")
        choices = (sample_path_graph(target, rng, sizes) for _ in range(args.trials))
    elif args.exhaustive_minimal:
        choices = itertools.product(MINIMAL_PATTERNS, repeat=target.number_of_edges())
    else:
        choices = (None for _ in range(args.trials))
    for trial, prescribed in enumerate(choices, 1):
        if isinstance(prescribed, nx.Graph):
            g = prescribed
        elif prescribed is None:
            g = sample_graph(target, rng)
        else:
            g = nx.Graph()
            g.add_nodes_from((i, bit) for i in range(6) for bit in range(2))
            for (u, v), pattern in zip(target.edges, prescribed):
                g.add_edges_from(((u, a), (v, b)) for a, b in pattern)
        if rooted_model(g, target, 6) is None:
            print(f"COUNTEREXAMPLE target={args.target} trial={trial}")
            print(sorted(g.edges()))
            return
        if trial % 1000 == 0:
            print(f"checked {trial}")
    print(f"no counterexample in {trial} trials")


if __name__ == "__main__":
    main()
