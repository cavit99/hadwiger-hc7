#!/usr/bin/env python3
"""Search cyclic twin lobes for a static-return-irreducible portal layout.

This is an adversarial topology probe, not a census.  The lobe topology is
fixed to two cycles joined to two alternating gates.  Random contact maps
are sampled subject to the exact twin supports and every relative
seven-cut inequality.  A survivor must defeat every literal adaptive
two-carrier allocation.  Such a survivor would be a substrate on which to
test the third-response locks; absence is evidence only for this web
family.
"""

from __future__ import annotations

import itertools
import os
from pathlib import Path
import random
import sys


DEPS = Path(__file__).resolve().parent / "runtime" / "deps"
if DEPS.exists():
    sys.path.insert(0, str(DEPS))

import networkx as nx


S = tuple(range(7))
U = 0
I = frozenset((3, 5, 6))
A0 = frozenset((1, 2))
B0 = frozenset((0, 4))
TD = I | A0
TE = I | B0
H_EDGES = ((0, 4), (1, 2), (1, 6), (3, 5), (3, 6), (4, 6))


def topology(n: int) -> tuple[nx.Graph, tuple[str, ...], tuple[str, ...]]:
    d = tuple(f"d{i}" for i in range(n))
    e = tuple(["z"] + [f"e{i}" for i in range(1, n)])
    graph = nx.Graph()
    graph.add_edges_from((d[i], d[(i + 1) % n]) for i in range(n))
    graph.add_edges_from((e[i], e[(i + 1) % n]) for i in range(n))
    # Alternating three/four-vertex gate fans.  Consecutive vertices share
    # one gate, while every lobe vertex sees at least one gate.
    for i, vertex in enumerate(d):
        graph.add_edge("p" if i % 2 == 0 else "q", vertex)
        if i % 3 == 0:
            graph.add_edge("q" if i % 2 == 0 else "p", vertex)
    for i, vertex in enumerate(e):
        graph.add_edge("q" if i % 2 == 0 else "p", vertex)
        if i % 3 == 0:
            graph.add_edge("p" if i % 2 == 0 else "q", vertex)
    graph.add_edge("p", "q")
    return graph, d, e


def random_topology(
    order: int, rng: random.Random
) -> tuple[nx.Graph, tuple[str, ...], tuple[str, ...]] | None:
    """Generate one biconnected literal twin topology of fixed order."""

    if order < 6:
        return None
    lobe_order = order - 2
    d_order = rng.randint(2, lobe_order - 2)
    e_order = lobe_order - d_order
    d = tuple(f"d{i}" for i in range(d_order))
    e = tuple(["z"] + [f"e{i}" for i in range(1, e_order)])
    graph = nx.Graph()
    graph.add_nodes_from(("p", "q", *d, *e))

    for lobe in (d, e):
        # Start with a random tree, then add lobe chords independently.
        for index in range(1, len(lobe)):
            graph.add_edge(lobe[index], rng.choice(lobe[:index]))
        for x, y in itertools.combinations(lobe, 2):
            if rng.random() < 0.35:
                graph.add_edge(x, y)

    for gate in ("p", "q"):
        for vertex in (*d, *e):
            if rng.random() < 0.62:
                graph.add_edge(gate, vertex)
    if rng.random() < 0.5:
        graph.add_edge("p", "q")

    if not nx.is_biconnected(graph):
        return None
    # A singleton relative cut must be fundable within its allowed support.
    max_support = {
        **{v: 5 for v in d},
        **{v: 4 for v in e if v != "z"},
        "z": 5,
        "p": 3,
        "q": 3,
    }
    if any(graph.degree(v) + max_support[v] < 7 for v in graph):
        return None
    return graph, d, e


def connected_subsets(graph: nx.Graph):
    vertices = tuple(graph)
    answer = []
    for mask in range(1, 1 << len(vertices)):
        chosen = frozenset(
            vertices[i] for i in range(len(vertices)) if (mask >> i) & 1
        )
        if nx.is_connected(graph.subgraph(chosen)):
            answer.append(chosen)
    return answer


def adaptive_partitions():
    boundary = nx.Graph(H_EDGES)
    boundary.add_nodes_from(S)
    answer = []
    for r in range(3):  # a clique in this tree has order at most two
        for reservoir in map(frozenset, itertools.combinations(S, r)):
            if r == 2 and not boundary.has_edge(*tuple(reservoir)):
                continue
            free = tuple(set(S) - reservoir)
            for mask in range(1, 1 << (len(free) - 1)):
                left = frozenset(
                    free[i] for i in range(len(free)) if (mask >> i) & 1
                )
                right = frozenset(free) - left
                if not right:
                    continue
                if boundary.subgraph(left).number_of_edges():
                    continue
                if boundary.subgraph(right).number_of_edges():
                    continue
                answer.append((left, right, reservoir))
    return answer


def cut_ok(graph: nx.Graph, contacts: dict[str, frozenset[int]], subsets) -> bool:
    vertices = set(graph)
    for chosen in subsets:
        outside_neighbours = set()
        support = set()
        for vertex in chosen:
            outside_neighbours.update(set(graph[vertex]) - set(chosen))
            support.update(contacts[vertex])
        if len(outside_neighbours) + len(support) < 7:
            return False
    return True


def return_witness(graph, contacts, subsets, partitions):
    root_sets = [chosen for chosen in subsets if "z" in chosen]
    for left in root_sets:
        left_support = set().union(*(contacts[v] for v in left))
        remaining = set(graph) - set(left)
        for component in nx.connected_components(graph.subgraph(remaining)):
            # Every connected right carrier is contained in a component;
            # enlarging it to the component preserves support and adjacency.
            if not any(graph.has_edge(x, y) for x in left for y in component):
                continue
            right_support = set().union(*(contacts[v] for v in component))
            for first, second, reservoir in partitions:
                if first <= left_support and second <= right_support:
                    return left, frozenset(component), first, second, reservoir
                if second <= left_support and first <= right_support:
                    return left, frozenset(component), second, first, reservoir
    return None


def random_contacts(graph, d, e, rng: random.Random):
    contacts: dict[str, set[int]] = {v: set() for v in graph}
    contacts["z"].add(U)
    allowed = {
        **{v: TD for v in d},
        **{v: TE - {U} for v in e},
        "p": I,
        "q": I,
    }
    # Meet the singleton cut lower bound first.
    for vertex in graph:
        need = max(0, 7 - graph.degree(vertex) - len(contacts[vertex]))
        choices = list(set(allowed[vertex]) - contacts[vertex])
        rng.shuffle(choices)
        contacts[vertex].update(choices[:need])
    # Exact collective supports and root-deletion fullness.
    for literal in TD:
        if not any(literal in contacts[v] for v in d):
            contacts[rng.choice(d)].add(literal)
    for literal in TE - {U}:
        if not any(literal in contacts[v] for v in e):
            contacts[rng.choice(e[1:])].add(literal)
    for literal in I:
        if literal not in contacts["p"] | contacts["q"]:
            contacts[rng.choice(("p", "q"))].add(literal)
    for literal in set(S) - {U}:
        if not any(literal in contacts[v] for v in graph if v != "z"):
            candidates = [v for v in graph if v != "z" and literal in allowed[v]]
            contacts[rng.choice(candidates)].add(literal)
    return {v: frozenset(values) for v, values in contacts.items()}


def main() -> None:
    n = int(os.environ.get("HC7_WEB_N", "5"))
    cap = int(os.environ.get("HC7_WEB_CAP", "20000"))
    seed = int(os.environ.get("HC7_WEB_SEED", "1"))
    partitions = adaptive_partitions()
    rng = random.Random(seed)
    if os.environ.get("HC7_WEB_TOPOLOGY", "cycle") == "random":
        topology_cap = int(os.environ.get("HC7_WEB_TOPOLOGY_CAP", "1000"))
        samples_per_topology = int(os.environ.get("HC7_WEB_PER_TOPOLOGY", "100"))
        tested = cut_survivors = 0
        for _ in range(topology_cap):
            generated = random_topology(n, rng)
            if generated is None:
                continue
            graph, d, e = generated
            subsets = connected_subsets(graph)
            for _ in range(samples_per_topology):
                contacts = random_contacts(graph, d, e, rng)
                tested += 1
                if not cut_ok(graph, contacts, subsets):
                    continue
                cut_survivors += 1
                witness = return_witness(graph, contacts, subsets, partitions)
                if witness is None:
                    print(
                        "STATIC_IRREDUCIBLE_RANDOM_TWIN",
                        "order",
                        n,
                        "graph6",
                        nx.to_graph6_bytes(graph, header=False).decode().strip(),
                    )
                    print("D", d, "E", e, "edges", tuple(graph.edges()))
                    print("contacts", contacts)
                    return
        print(
            "NO_RANDOM_TWIN_SURVIVOR",
            "order",
            n,
            "tested_maps",
            tested,
            "relative_cut_survivors",
            cut_survivors,
        )
        return

    graph, d, e = topology(n)
    subsets = connected_subsets(graph)
    cut_survivors = 0
    for iteration in range(1, cap + 1):
        contacts = random_contacts(graph, d, e, rng)
        if not cut_ok(graph, contacts, subsets):
            continue
        cut_survivors += 1
        witness = return_witness(graph, contacts, subsets, partitions)
        if witness is None:
            print("STATIC_IRREDUCIBLE_WEB", "n", n, "iteration", iteration)
            print("contacts", contacts)
            return
    print(
        "NO_WEB_SURVIVOR",
        "n",
        n,
        "samples",
        cap,
        "relative_cut_survivors",
        cut_survivors,
    )


if __name__ == "__main__":
    main()
