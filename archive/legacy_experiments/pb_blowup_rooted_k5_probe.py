#!/usr/bin/env python3
"""Probe rooted K5 models in clique blowups of the pentagonal bipyramid."""

from __future__ import annotations

from itertools import combinations
from itertools import product
from pathlib import Path
import random
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "active" / "runtime" / "deps"))

import networkx as nx
import z3


def pb() -> nx.Graph:
    graph = nx.Graph()
    poles = ("a", "b")
    rim = tuple(f"r{i}" for i in range(5))
    graph.add_nodes_from(poles + rim)
    graph.add_edges_from((pole, vertex) for pole in poles for vertex in rim)
    graph.add_edges_from((rim[i], rim[(i + 1) % 5]) for i in range(5))
    return graph


def blowup(size: int) -> tuple[nx.Graph, dict[str, set[str]], set[str]]:
    quotient = pb()
    graph = nx.Graph()
    columns = {
        label: {f"{label}_{i}" for i in range(size)} for label in quotient
    }
    for column in columns.values():
        graph.add_edges_from(combinations(column, 2))
    for left, right in quotient.edges():
        graph.add_edges_from((x, y) for x in columns[left] for y in columns[right])
    terminals = {f"{label}_0" for label in quotient}
    return graph, columns, terminals


def clique_minor(
    graph: nx.Graph,
    order: int,
    terminals: set[str] | tuple[set[str], ...] | None = None,
) -> tuple[set[str], ...] | None:
    vertices = tuple(graph)
    solver = z3.Solver()
    label = {v: z3.Int(f"l_{i}") for i, v in enumerate(vertices)}
    depth = {v: z3.Int(f"d_{i}") for i, v in enumerate(vertices)}
    root = {
        (v, bag): z3.Bool(f"root_{i}_{bag}")
        for i, v in enumerate(vertices)
        for bag in range(order)
    }
    for vertex in vertices:
        solver.add(-1 <= label[vertex], label[vertex] < order)
        solver.add(0 <= depth[vertex], depth[vertex] < len(vertices))
    for bag in range(order):
        solver.add(z3.PbEq([(root[v, bag], 1) for v in vertices], 1))
        if terminals is not None:
            terminal_sets = terminals if isinstance(terminals, tuple) else (terminals,)
            for terminal_set in terminal_sets:
                solver.add(z3.Or(*(label[v] == bag for v in terminal_set)))
        for vertex in vertices:
            solver.add(
                z3.Implies(
                    root[vertex, bag],
                    z3.And(label[vertex] == bag, depth[vertex] == 0),
                )
            )
            predecessors = [
                z3.And(label[w] == bag, depth[w] < depth[vertex])
                for w in graph[vertex]
            ]
            solver.add(
                z3.Implies(
                    z3.And(label[vertex] == bag, z3.Not(root[vertex, bag])),
                    z3.And(depth[vertex] > 0, z3.Or(*predecessors)),
                )
            )
    for left, right in combinations(range(order), 2):
        solver.add(
            z3.Or(
                *(
                    z3.Or(
                        z3.And(label[x] == left, label[y] == right),
                        z3.And(label[x] == right, label[y] == left),
                    )
                    for x, y in graph.edges()
                )
            )
        )
    if solver.check() != z3.sat:
        return None
    model = solver.model()
    return tuple(
        {v for v in vertices if model.eval(label[v]).as_long() == bag}
        for bag in range(order)
    )


def main() -> None:
    for size in (2, 3):
        graph, _, terminals = blowup(size)
        rooted = clique_minor(graph, 5, terminals)
        print(
            f"size={size}",
            f"order={len(graph)}",
            f"connectivity={nx.node_connectivity(graph)}",
            f"rooted_k5={rooted is not None}",
            rooted,
        )

    # The audited icosahedral PB partition, with the unique missing edge
    # inside a nonsingleton column added.  Since the icosahedron is a
    # maximal planar graph, this is a five-connected nonplanar PB expansion.
    ico = nx.icosahedral_graph()
    columns = {
        "a": {2},
        "b": {4},
        "r0": {6},
        "r1": {3},
        "r2": {9, 10},
        "r3": {7, 8, 11},
        "r4": {0, 1, 5},
    }
    ico.add_edge(8, 11)
    assert nx.node_connectivity(ico) == 5
    assert not nx.check_planarity(ico)[0]
    choices = []
    for a in columns["a"]:
        for b in columns["b"]:
            for r0 in columns["r0"]:
                for r1 in columns["r1"]:
                    for r2 in columns["r2"]:
                        for r3 in columns["r3"]:
                            for r4 in columns["r4"]:
                                terminals = {a, b, r0, r1, r2, r3, r4}
                                choices.append(terminals)
    failures = [terminals for terminals in choices if clique_minor(ico, 5, terminals) is None]
    print(
        "icosahedral_plus_8_11",
        f"terminal_choices={2 * 3 * 3}",
        f"rooted_failures={len(failures)}",
        failures,
    )
    paired_failures = []
    for left in choices:
        for right in choices:
            if clique_minor(ico, 5, (left, right)) is None:
                paired_failures.append((left, right))
    print(
        "icosahedral_plus_8_11_paired",
        f"pairs={len(choices) ** 2}",
        f"rooted_failures={len(paired_failures)}",
        paired_failures[:5],
    )

    random.seed(0xB1F1)
    base, base_columns, _ = blowup(2)
    sparse_samples = 0
    sparse_failures = []
    for trial in range(40):
        graph = base.copy()
        edges = list(graph.edges())
        random.shuffle(edges)
        for edge in edges:
            candidate = graph.copy()
            candidate.remove_edge(*edge)
            if nx.node_connectivity(candidate) < 5:
                continue
            if nx.check_planarity(candidate)[0]:
                continue
            # Keep every PB contact represented.
            if any(
                not any(candidate.has_edge(x, y) for x in base_columns[left] for y in base_columns[right])
                for left, right in pb().edges()
            ):
                continue
            graph = candidate
        sparse_samples += 1
        left = {f"{label}_0" for label in base_columns}
        right = {f"{label}_1" for label in base_columns}
        rooted = clique_minor(graph, 5, (left, right))
        if rooted is None:
            sparse_failures.append((graph, left, right))
            break
    print(
        "random_sparse_pb2",
        f"samples={sparse_samples}",
        f"failures={len(sparse_failures)}",
        f"last_edges={len(graph.edges())}",
        f"last_connectivity={nx.node_connectivity(graph)}",
    )
    if sparse_failures:
        bad, left, right = sparse_failures[0]
        print("bad_edges", sorted(tuple(sorted(edge)) for edge in bad.edges()))
        print("bad_left", sorted(left), "bad_right", sorted(right))

    # Exhaust all single-vertex splits of PB.  Each old neighbour attaches
    # to the first clone, the second clone, or both.  Test the genuinely
    # five-connected nonplanar splits against all two-root choices in the
    # split column.
    q = pb()
    split_total = split_five_connected = split_failures = 0
    for split_vertex in q:
        neighbours = tuple(q[split_vertex])
        for pattern in product((1, 2, 3), repeat=len(neighbours)):
            graph = q.copy()
            graph.remove_node(split_vertex)
            x, y = f"{split_vertex}x", f"{split_vertex}y"
            graph.add_edge(x, y)
            for neighbour, incidence in zip(neighbours, pattern):
                if incidence & 1:
                    graph.add_edge(x, neighbour)
                if incidence & 2:
                    graph.add_edge(y, neighbour)
            if nx.check_planarity(graph)[0]:
                continue
            split_total += 1
            if nx.node_connectivity(graph) < 5:
                continue
            split_five_connected += 1
            fixed = set(q) - {split_vertex}
            for left_choice in (x, y):
                for right_choice in (x, y):
                    left = fixed | {left_choice}
                    right = fixed | {right_choice}
                    if clique_minor(graph, 5, (left, right)) is None:
                        split_failures += 1
                        print("split_failure", split_vertex, pattern, left_choice, right_choice)
    print(
        "pb_single_splits",
        f"nonplanar={split_total}",
        f"five_connected={split_five_connected}",
        f"paired_failures={split_failures}",
    )


if __name__ == "__main__":
    main()
