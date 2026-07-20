#!/usr/bin/env python3
"""Try to augment the canonical PB path expansion without a paired-rooted K5."""

from __future__ import annotations

from itertools import combinations
from pathlib import Path
import random
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "active" / "runtime" / "deps"))

import networkx as nx
import z3


LABELS = ("a", "b", "r0", "r1", "r2", "r3", "r4")


def quotient() -> nx.Graph:
    graph = nx.Graph()
    graph.add_nodes_from(LABELS)
    for pole in ("a", "b"):
        for rim in LABELS[2:]:
            graph.add_edge(pole, rim)
    for i in range(5):
        graph.add_edge(f"r{i}", f"r{(i + 1) % 5}")
    return graph


def build(length: int = 3) -> tuple[nx.Graph, dict[str, tuple[str, ...]]]:
    q = quotient()
    columns = {
        label: tuple(f"{label}_{i}" for i in range(length)) for label in LABELS
    }
    graph = nx.Graph()
    for column in columns.values():
        graph.add_edges_from(zip(column, column[1:]))
    middle = length // 2
    graph.add_edges_from(
        (columns[left][middle], columns[right][middle]) for left, right in q.edges()
    )
    return graph, columns


def has_paired_rooted_k5(
    graph: nx.Graph,
    left_roots: set[str],
    right_roots: set[str],
) -> bool:
    vertices = tuple(graph)
    order = 5
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
        solver.add(z3.Or(*(label[v] == bag for v in left_roots)))
        solver.add(z3.Or(*(label[v] == bag for v in right_roots)))
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
    for first, second in combinations(range(order), 2):
        solver.add(
            z3.Or(
                *(
                    z3.Or(
                        z3.And(label[x] == first, label[y] == second),
                        z3.And(label[x] == second, label[y] == first),
                    )
                    for x, y in graph.edges()
                )
            )
        )
    return solver.check() == z3.sat


def candidates(
    graph: nx.Graph,
    columns: dict[str, tuple[str, ...]],
) -> list[tuple[str, str]]:
    q = quotient()
    edges = []
    for left, right in combinations(graph, 2):
        if graph.has_edge(left, right):
            continue
        left_label = left.rsplit("_", 1)[0]
        right_label = right.rsplit("_", 1)[0]
        if left_label == right_label or q.has_edge(left_label, right_label):
            edges.append((left, right))
    return edges


def main() -> None:
    best = None
    for trial in range(12):
        graph, columns = build()
        left = {column[0] for column in columns.values()}
        right = {column[-1] for column in columns.values()}
        assert not has_paired_rooted_k5(graph, left, right)
        edges = candidates(graph, columns)
        random.Random(0xC011 + trial).shuffle(edges)
        for edge in edges:
            graph.add_edge(*edge)
            if has_paired_rooted_k5(graph, left, right):
                graph.remove_edge(*edge)
        score = (nx.node_connectivity(graph), len(graph.edges()))
        print(
            f"trial={trial}",
            f"connectivity={score[0]}",
            f"edges={score[1]}",
            f"planar={nx.check_planarity(graph)[0]}",
        )
        if best is None or score > best[0]:
            best = (score, graph.copy(), left, right)
    assert best is not None
    score, graph, left, right = best
    print("BEST", score, "planar", nx.check_planarity(graph)[0])
    print("edges", sorted(tuple(sorted(edge)) for edge in graph.edges()))
    print("left", sorted(left), "right", sorted(right))


if __name__ == "__main__":
    main()
