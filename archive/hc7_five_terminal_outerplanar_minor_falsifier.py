#!/usr/bin/env python3
"""Search for a counterexample to a five-terminal outerplanar principle.

Candidate: if a 3-connected graph has no K4 model whose four bags each
meet a prescribed five-set T, then it has a T-rooted maximal outerplanar
minor on five vertices.  The program is a finite falsifier only.
"""

from __future__ import annotations

import argparse
import itertools
import subprocess

import networkx as nx


def is_k_connected(graph: nx.Graph, k: int) -> bool:
    vertices = tuple(graph)
    if len(vertices) <= k:
        return False
    for size in range(k):
        for deleted in itertools.combinations(vertices, size):
            remaining = graph.copy()
            remaining.remove_nodes_from(deleted)
            if not nx.is_connected(remaining):
                return False
    return True


def connected(graph: nx.Graph, vertices: set[int]) -> bool:
    return bool(vertices) and nx.is_connected(graph.subgraph(vertices))


def touches(graph: nx.Graph, left: set[int], right: set[int]) -> bool:
    return any(graph.has_edge(u, v) for u in left for v in right)


def rooted_k4(graph: nx.Graph, roots: tuple[int, ...]) -> bool:
    remaining = tuple(v for v in graph if v not in roots)
    for assignment in itertools.product(range(5), repeat=len(remaining)):
        bags = [{root} for root in roots]
        for vertex, owner in zip(remaining, assignment):
            if owner < 4:
                bags[owner].add(vertex)
        if all(connected(graph, bag) for bag in bags) and all(
            touches(graph, left, right)
            for left, right in itertools.combinations(bags, 2)
        ):
            return True
    return False


def maximal_outerplanar_targets(terminals: tuple[int, ...]) -> tuple[frozenset[tuple[int, int]], ...]:
    targets = set()
    first = terminals[0]
    for tail in itertools.permutations(terminals[1:]):
        cycle = (first,) + tail
        if cycle[1] > cycle[-1]:
            continue
        cycle_edges = {
            tuple(sorted((cycle[i], cycle[(i + 1) % 5]))) for i in range(5)
        }
        for center_index in range(5):
            center = cycle[center_index]
            nonneighbors = (cycle[(center_index + 2) % 5], cycle[(center_index + 3) % 5])
            edges = cycle_edges | {
                tuple(sorted((center, nonneighbors[0]))),
                tuple(sorted((center, nonneighbors[1]))),
            }
            targets.add(frozenset(edges))
    return tuple(targets)


def rooted_mop5(graph: nx.Graph, terminals: tuple[int, ...]) -> bool:
    remaining = tuple(v for v in graph if v not in terminals)
    targets = maximal_outerplanar_targets(terminals)
    for assignment in itertools.product(range(6), repeat=len(remaining)):
        bags = [{root} for root in terminals]
        for vertex, owner in zip(remaining, assignment):
            if owner < 5:
                bags[owner].add(vertex)
        if not all(connected(graph, bag) for bag in bags):
            continue
        quotient_edges = {
            tuple(sorted((terminals[i], terminals[j])))
            for i, j in itertools.combinations(range(5), 2)
            if touches(graph, bags[i], bags[j])
        }
        if any(target <= quotient_edges for target in targets):
            return True
    return False


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    args = parser.parse_args()
    process = subprocess.Popen(
        ["geng", "-q", "-d3", str(args.n)], stdout=subprocess.PIPE
    )
    assert process.stdout is not None
    graphs = terminal_sets = no_k4 = 0
    for raw in process.stdout:
        graph = nx.from_graph6_bytes(raw.strip())
        if not is_k_connected(graph, 3):
            continue
        graphs += 1
        for terminals in itertools.combinations(tuple(graph), 5):
            terminal_sets += 1
            if any(rooted_k4(graph, roots) for roots in itertools.combinations(terminals, 4)):
                continue
            no_k4 += 1
            if not rooted_mop5(graph, terminals):
                print(
                    "COUNTEREXAMPLE",
                    nx.to_graph6_bytes(graph, header=False).strip().decode(),
                    terminals,
                )
                process.terminate()
                return
    assert process.wait() == 0
    print(
        f"n={args.n} graphs={graphs} terminal_sets={terminal_sets} "
        f"no_terminal_rooted_k4={no_k4} counterexamples=0"
    )


if __name__ == "__main__":
    main()
