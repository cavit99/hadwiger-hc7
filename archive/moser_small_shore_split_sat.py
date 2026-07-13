#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = ["networkx>=3.4", "z3-solver>=4.13"]
# ///
"""Search for a small full shore with no two defect-at-most-two sides.

This is a falsification/discovery tool.  It imposes only the local
minimum-degree and fullness inequalities, then asks whether every
connected bipartition has a side contacting at most four boundary roots.
"""

from __future__ import annotations

import itertools

import networkx as nx
from z3 import And, Bool, If, Or, Solver, Sum, is_true


def connected_bipartitions(graph: nx.Graph):
    vertices = tuple(graph.nodes())
    first = vertices[0]
    for size in range(1, len(vertices)):
        for side in itertools.combinations(vertices, size):
            side = set(side)
            if first not in side:
                continue
            other = set(vertices) - side
            if nx.is_connected(graph.subgraph(side)) and nx.is_connected(
                graph.subgraph(other)
            ):
                yield side, other


def main() -> None:
    atlas = nx.graph_atlas_g()
    for order in range(1, 6):
        graphs = [
            graph
            for graph in atlas
            if len(graph) == order
            and (order == 1 or nx.is_connected(graph))
        ]
        survivors = 0
        for index, graph in enumerate(graphs):
            contacts = {
                (vertex, root): Bool(f"x_{order}_{index}_{vertex}_{root}")
                for vertex in graph
                for root in range(7)
            }
            solver = Solver()
            for vertex in graph:
                solver.add(
                    Sum([If(contacts[vertex, root], 1, 0) for root in range(7)])
                    >= 7 - graph.degree(vertex)
                )
            for root in range(7):
                solver.add(Or([contacts[vertex, root] for vertex in graph]))

            # Every nonempty proper shore subset is separated from the
            # other two full shores by its internal vertex boundary plus
            # the boundary roots it contacts.  Seven-connectivity forces
            # that neighbourhood to have order at least seven.
            vertices = tuple(graph.nodes())
            for size in range(1, order):
                for subset_tuple in itertools.combinations(vertices, size):
                    subset = set(subset_tuple)
                    internal_boundary = {
                        vertex
                        for vertex in vertices
                        if vertex not in subset
                        and any(graph.has_edge(vertex, member) for member in subset)
                    }
                    boundary_count = Sum(
                        [
                            If(
                                Or([contacts[vertex, root] for vertex in subset]),
                                1,
                                0,
                            )
                            for root in range(7)
                        ]
                    )
                    solver.add(boundary_count + len(internal_boundary) >= 7)

            for left, right in connected_bipartitions(graph):
                left_count = Sum(
                    [
                        If(Or([contacts[vertex, root] for vertex in left]), 1, 0)
                        for root in range(7)
                    ]
                )
                right_count = Sum(
                    [
                        If(Or([contacts[vertex, root] for vertex in right]), 1, 0)
                        for root in range(7)
                    ]
                )
                solver.add(Or(left_count <= 4, right_count <= 4))

            if solver.check().r == 1:
                survivors += 1
                model = solver.model()
                rows = {
                    vertex: tuple(
                        root
                        for root in range(7)
                        if is_true(model.eval(contacts[vertex, root], model_completion=True))
                    )
                    for vertex in graph
                }
                print(
                    "SAT",
                    "order",
                    order,
                    "graph6",
                    nx.to_graph6_bytes(graph, header=False).strip().decode(),
                    "edges",
                    sorted(graph.edges()),
                    "rows",
                    rows,
                )
        print("order", order, "graphs", len(graphs), "survivors", survivors)


if __name__ == "__main__":
    main()
