#!/usr/bin/env python3
"""Enumerate raw three-palette obstructions with no anchored K4.

This is a research enumerator.  It uses one fresh Python/Z3 process per
triangle-free seven-vertex atlas graph so that the fairly large finite model
formulae do not accumulate in Z3's global context.

Run from the repository root with

  PYTHONPATH=active/runtime/deps python3 \
      active/hc7_exact7_raw_list_no_k4_search.py
"""

from __future__ import annotations

import argparse
import itertools
import json
import os
import subprocess
import sys
from collections import Counter

import networkx as nx
import z3


def triangle_free(graph: nx.Graph) -> bool:
    return not any(nx.triangles(graph).values())


def atlas_graphs() -> list[nx.Graph]:
    return [
        graph
        for graph in nx.graph_atlas_g()
        if len(graph) == 7 and triangle_free(graph)
    ]


def no_anchored_k4_constraints(
    graph: nx.Graph, contacts: list[list[z3.BoolRef]]
) -> list[z3.BoolRef]:
    """Forbid every four-root/three-carrier literal minor model."""

    constraints: list[z3.BoolRef] = []
    for roots in itertools.combinations(range(7), 4):
        # A carrier belongs to one of the four rooted bags, or is unused (4).
        for assignment in itertools.product(range(5), repeat=3):
            bags: list[tuple[int, list[int]]] = [
                (roots[index], []) for index in range(4)
            ]
            for carrier, bag_index in enumerate(assignment):
                if bag_index < 4:
                    bags[bag_index][1].append(carrier)

            requirements: list[z3.BoolRef] = []
            possible = True

            # A root plus a nonempty carrier subset is connected exactly when
            # the root sees at least one member of that subset.
            for root, carriers in bags:
                if carriers:
                    requirements.append(
                        z3.Or(*(contacts[root][colour] for colour in carriers))
                    )

            # Two carrier-bearing bags are adjacent through the carrier
            # triangle.  Otherwise use a literal root edge or a root-carrier
            # incidence.
            for left, right in itertools.combinations(range(4), 2):
                root_left, carriers_left = bags[left]
                root_right, carriers_right = bags[right]
                if carriers_left and carriers_right:
                    continue
                alternatives: list[z3.BoolRef] = []
                if graph.has_edge(root_left, root_right):
                    alternatives.append(z3.BoolVal(True))
                alternatives.extend(
                    contacts[root_right][colour] for colour in carriers_left
                )
                alternatives.extend(
                    contacts[root_left][colour] for colour in carriers_right
                )
                if not alternatives:
                    possible = False
                    break
                requirements.append(z3.Or(*alternatives))

            if possible:
                constraints.append(z3.Not(z3.And(*requirements)))
    return constraints


def propagated_outcome(
    graph: nx.Graph, masks: tuple[int, ...]
) -> tuple[str, int, tuple[int, ...]]:
    """Run exact singleton propagation and report conflict or residual."""

    current = list(masks)
    alive = set(range(7))
    while True:
        singleton = next(
            (vertex for vertex in sorted(alive) if current[vertex].bit_count() == 1),
            None,
        )
        if singleton is None:
            residual = tuple(current[vertex] for vertex in sorted(alive))
            return "residual", len(alive), residual
        colour_mask = current[singleton]
        alive.remove(singleton)
        for neighbour in graph[singleton]:
            if neighbour not in alive:
                continue
            if current[neighbour] & colour_mask:
                current[neighbour] &= ~colour_mask
                if current[neighbour] == 0:
                    return "conflict", len(alive), ()


def solve_graph(index: int) -> dict[str, object]:
    graph = atlas_graphs()[index]
    contacts = [
        [z3.Bool(f"x_{vertex}_{colour}") for colour in range(3)]
        for vertex in range(7)
    ]
    solver = z3.Solver()

    # Nonempty raw lists and support at least four for every carrier.
    for vertex in range(7):
        solver.add(z3.Or(*contacts[vertex]))
    for colour in range(3):
        solver.add(
            z3.PbGe([(contacts[vertex][colour], 1) for vertex in range(7)], 4)
        )

    # Uncolourability: block every proper three-colouring of the literal
    # boundary graph.
    for colouring in itertools.product(range(3), repeat=7):
        if all(colouring[u] != colouring[v] for u, v in graph.edges()):
            solver.add(
                z3.Or(
                    *(z3.Not(contacts[v][colouring[v]]) for v in range(7))
                )
            )

    solver.add(*no_anchored_k4_constraints(graph, contacts))

    assignments: list[tuple[int, ...]] = []
    while solver.check() == z3.sat:
        model = solver.model()
        masks = tuple(
            sum(
                1 << colour
                for colour in range(3)
                if z3.is_true(model.eval(contacts[vertex][colour]))
            )
            for vertex in range(7)
        )
        assignments.append(masks)
        solver.add(
            z3.Or(
                *(
                    contacts[vertex][colour]
                    != model.eval(contacts[vertex][colour])
                    for vertex in range(7)
                    for colour in range(3)
                )
            )
        )

    outcomes = Counter(
        (propagated_outcome(graph, masks)[0], propagated_outcome(graph, masks)[1])
        for masks in assignments
    )
    singleton_histogram = Counter(
        sum(mask.bit_count() == 1 for mask in masks) for masks in assignments
    )
    full_histogram = Counter(masks.count(0b111) for masks in assignments)
    return {
        "index": index,
        "graph6": nx.to_graph6_bytes(graph, header=False).strip().decode("ascii"),
        "edges": sorted(tuple(edge) for edge in graph.edges()),
        "assignments": assignments,
        "outcomes": sorted((list(key), count) for key, count in outcomes.items()),
        "singleton_histogram": sorted(singleton_histogram.items()),
        "full_histogram": sorted(full_histogram.items()),
    }


def child(index: int) -> None:
    print(json.dumps(solve_graph(index), separators=(",", ":")))


def parent(start: int, end: int | None) -> None:
    graphs = atlas_graphs()
    if end is None:
        end = len(graphs)
    records: list[dict[str, object]] = []
    environment = dict(os.environ)
    dependency_path = os.path.join(os.path.dirname(__file__), "runtime", "deps")
    environment["PYTHONPATH"] = dependency_path
    for index in range(start, end):
        completed = subprocess.run(
            [sys.executable, __file__, "--graph", str(index)],
            check=True,
            capture_output=True,
            text=True,
            env=environment,
        )
        record = json.loads(completed.stdout)
        print(
            f"scanned={index} assignments={len(record['assignments'])}",
            flush=True,
        )
        if record["assignments"]:
            records.append(record)

    output_path = os.path.join(
        os.path.dirname(__file__),
        f"hc7_exact7_raw_list_no_k4_catalogue_{start}_{end}.json",
    )
    with open(output_path, "w", encoding="utf-8") as stream:
        json.dump(records, stream, indent=2)
        stream.write("\n")

    print(f"triangle_free_graphs={len(graphs)}")
    print(f"graphs_with_obstructions={len(records)}")
    print(f"raw_assignments={sum(len(record['assignments']) for record in records)}")
    print(f"catalogue={output_path}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--graph", type=int)
    parser.add_argument("--start", type=int, default=0)
    parser.add_argument("--end", type=int)
    arguments = parser.parse_args()
    if arguments.graph is None:
        parent(arguments.start, arguments.end)
    else:
        child(arguments.graph)


if __name__ == "__main__":
    main()
