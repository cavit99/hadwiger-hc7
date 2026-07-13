#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = ["networkx>=3.4", "z3-solver>=4.13"]
# ///
"""CEGIS search for a terminal small low-owner Moser shore.

The seven Moser boundary vertices are followed by the vertices of one
explicit shore D and two contracted full helper shores.  Contact edges
from D to the boundary are variables.  The solver enforces fullness,
minimum degree seven, all relative seven-connectivity inequalities, and
ownership of at most five of the sixteen optimal Moser partitions.
Every proposed assignment is checked by an exact K7-minor solver.
"""

from __future__ import annotations

import hashlib
import itertools

import networkx as nx
from z3 import And, Bool, If, Or, Solver, Sum, is_true


S = tuple(range(7))
MOSER = {
    tuple(sorted(map(int, edge)))
    for edge in "01 02 03 04 12 16 26 34 35 45 56".split()
}
NONEDGES = set(itertools.combinations(S, 2)) - MOSER


def optimal_matchings():
    answer = []
    for singleton in S:
        for matching in itertools.combinations(NONEDGES, 3):
            ends = {vertex for edge in matching for vertex in edge}
            if ends == set(S) - {singleton}:
                answer.append(tuple(sorted(matching)))
    return tuple(sorted(set(answer)))


MATCHINGS = optimal_matchings()
assert len(MATCHINGS) == 16


def connected_masks(graph: nx.Graph):
    answer = []
    for mask in range(1, 1 << len(graph)):
        vertices = [vertex for vertex in graph if mask >> vertex & 1]
        if nx.is_connected(graph.subgraph(vertices)):
            answer.append(mask)
    return tuple(answer)


def minor_model(graph: nx.Graph, target: int = 7):
    vertices = tuple(graph.nodes())
    n = len(vertices)
    assert vertices == tuple(range(n))
    adjacency = [0] * n
    for u, v in graph.edges():
        adjacency[u] |= 1 << v
        adjacency[v] |= 1 << u
    neighbour_union = [0] * (1 << n)
    connected = []
    for mask in range(1, 1 << n):
        bit = mask & -mask
        neighbour_union[mask] = (
            neighbour_union[mask ^ bit] | adjacency[bit.bit_length() - 1]
        )
        reached = bit
        while True:
            expanded = reached | (neighbour_union[reached] & mask)
            if expanded == reached:
                break
            reached = expanded
        if reached == mask:
            connected.append(mask)
    connected.sort(key=lambda item: (item.bit_count(), item))

    def rec(chosen, candidates, used):
        needed = target - len(chosen)
        if needed == 0:
            return tuple(chosen)
        if len(candidates) < needed:
            return None
        for position, bag in enumerate(candidates):
            if bag & used:
                continue
            nxt = [
                other
                for other in candidates[position + 1 :]
                if not other & (used | bag) and neighbour_union[bag] & other
            ]
            if len(nxt) >= needed - 1:
                result = rec(chosen + [bag], nxt, used | bag)
                if result is not None:
                    return result
        return None

    return rec([], connected, 0)


def solve_shore(shore: nx.Graph, graph_index: int):
    n = len(shore)
    contacts = {
        (vertex, root): Bool(f"c_{n}_{graph_index}_{vertex}_{root}")
        for vertex in shore
        for root in S
    }
    solver = Solver()

    for root in S:
        solver.add(Or([contacts[vertex, root] for vertex in shore]))
    for vertex in shore:
        solver.add(
            Sum([If(contacts[vertex, root], 1, 0) for root in S])
            + shore.degree(vertex)
            >= 7
        )

    vertices = tuple(shore.nodes())
    for size in range(1, n):
        for subset_tuple in itertools.combinations(vertices, size):
            subset = set(subset_tuple)
            internal_boundary = {
                vertex
                for vertex in vertices
                if vertex not in subset
                and any(shore.has_edge(vertex, member) for member in subset)
            }
            boundary_contacts = Sum(
                [
                    If(Or([contacts[vertex, root] for vertex in subset]), 1, 0)
                    for root in S
                ]
            )
            solver.add(boundary_contacts + len(internal_boundary) >= 7)

    carriers = connected_masks(shore)

    def supports(mask, edge):
        return And(
            [
                Or(
                    [
                        contacts[vertex, root]
                        for vertex in vertices
                        if mask >> vertex & 1
                    ]
                )
                for root in edge
            ]
        )

    owner_expressions = []
    for matching in MATCHINGS:
        witnesses = []
        for edge_1, edge_2 in itertools.combinations(matching, 2):
            for mask_1 in carriers:
                for mask_2 in carriers:
                    if mask_1 & mask_2:
                        continue
                    witnesses.append(
                        And(supports(mask_1, edge_1), supports(mask_2, edge_2))
                    )
        owner_expressions.append(Or(witnesses))
    solver.add(Sum([If(expression, 1, 0) for expression in owner_expressions]) <= 5)

    iterations = 0
    while solver.check().r == 1:
        iterations += 1
        model = solver.model()
        rows = {
            vertex: {
                root
                for root in S
                if is_true(model.eval(contacts[vertex, root], model_completion=True))
            }
            for vertex in shore
        }

        full = nx.Graph()
        total = 7 + n + 2
        full.add_nodes_from(range(total))
        full.add_edges_from(MOSER)
        full.add_edges_from((7 + u, 7 + v) for u, v in shore.edges())
        for vertex, roots in rows.items():
            full.add_edges_from((root, 7 + vertex) for root in roots)
        helper_1, helper_2 = 7 + n, 8 + n
        full.add_edges_from((root, helper) for root in S for helper in (helper_1, helper_2))

        clique = minor_model(full)
        if clique is None:
            owners = [
                index
                for index, expression in enumerate(owner_expressions)
                if is_true(model.eval(expression, model_completion=True))
            ]
            return {
                "iterations": iterations,
                "rows": rows,
                "owners": owners,
                "graph": full,
            }

        true_variables = [
            contacts[vertex, root]
            for vertex in shore
            for root in S
            if root in rows[vertex]
        ]
        # Every contact supergraph of this assignment contains the same
        # fixed K7 model, so it is safe to exclude all such supergraphs.
        solver.add(Or([~variable for variable in true_variables]))

    return {"iterations": iterations, "rows": None}


def main() -> None:
    atlas = nx.graph_atlas_g()
    expected_counts = {1: 1, 2: 1, 3: 2, 4: 1, 5: 3, 6: 17}
    records = []
    survivors = []
    for order in range(1, 7):
        graphs = [
            nx.convert_node_labels_to_integers(graph)
            for graph in atlas
            if len(graph) == order
            and (order == 1 or nx.is_connected(graph))
            and (order <= 3 or nx.node_connectivity(graph) >= 3)
        ]
        graphs.sort(key=lambda graph: nx.to_graph6_bytes(graph, header=False))
        assert len(graphs) == expected_counts[order]
        print("order", order, "terminal candidate graphs", len(graphs))
        for index, shore in enumerate(graphs):
            graph6 = nx.to_graph6_bytes(shore, header=False).strip().decode()
            result = solve_shore(shore, index)
            if result["rows"] is not None:
                row_record = tuple(
                    tuple(sorted(result["rows"][vertex])) for vertex in shore
                )
                survivors.append((order, graph6, row_record, tuple(result["owners"])))
                records.append(
                    f"{order}:{graph6}:SURVIVOR:{result['iterations']}:"
                    f"{row_record}:{tuple(result['owners'])}"
                )
                print(
                    "SURVIVOR",
                    "order",
                    order,
                    "graph6",
                    graph6,
                    "edges",
                    sorted(shore.edges()),
                    "iterations",
                    result["iterations"],
                    "owners",
                    result["owners"],
                    "rows",
                    {vertex: sorted(roots) for vertex, roots in result["rows"].items()},
                )
            else:
                records.append(
                    f"{order}:{graph6}:UNSAT:{result['iterations']}"
                )
                print(
                    "UNSAT",
                    graph6,
                    "iterations",
                    result["iterations"],
                )

    expected_survivor = (
        1,
        "@",
        ((0, 1, 2, 3, 4, 5, 6),),
        (),
    )
    assert survivors == [expected_survivor]
    assert all(
        record.endswith(":UNSAT:0")
        for record in records
        if ":UNSAT:" in record
    )
    digest = hashlib.sha256("\n".join(records).encode()).hexdigest()
    assert digest == "d74287d353e0f3d49b1f24c90f42938b08ba40e3543cad5070348a908d75576b"
    print("records", len(records), "sha256", digest)


if __name__ == "__main__":
    main()
