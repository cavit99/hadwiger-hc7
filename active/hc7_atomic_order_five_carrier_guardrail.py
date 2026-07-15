#!/usr/bin/env python3
"""Exact order-five guardrail for the compulsory-atom carrier outcome."""

from __future__ import annotations

import itertools
import sys
from pathlib import Path


DEPS = Path(__file__).resolve().parent / "runtime" / "deps"
if DEPS.exists():
    sys.path.insert(0, str(DEPS))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import networkx as nx
import z3

from hc7_atomic_order_four_carrier_exhaustion import FRONTIERS, exhaust_instance
from results.hc7_atomic_four_vertex_packet_path_classification import (
    spanning_minor_model,
)


S = tuple(range(7))
U_LITERAL = 0
RICH = ("p", "q")


def full_host(thin, root, frontier_edges, rows):
    thin_name = {vertex: f"a{vertex}" for vertex in thin}
    graph = nx.Graph()
    graph.add_nodes_from(tuple(thin_name.values()) + S + RICH)
    graph.add_edges_from((thin_name[x], thin_name[y]) for x, y in thin.edges())
    graph.add_edges_from(frontier_edges)
    graph.add_edge(thin_name[root], U_LITERAL)
    for vertex, literals in rows.items():
        graph.add_edges_from((thin_name[vertex], literal) for literal in literals)
    graph.add_edge(*RICH)
    for rich in RICH:
        graph.add_edges_from((rich, literal) for literal in S)
    return graph, frozenset(thin_name.values())


def rooted_k5(thin_closed: nx.Graph) -> bool:
    """Exact test for five clique bags containing five distinct S literals."""
    nodes = tuple(thin_closed)
    for roots in itertools.combinations(S, 5):
        solver = z3.Solver()
        label = {
            vertex: z3.Int(f"label_{index}")
            for index, vertex in enumerate(nodes)
        }
        depth = {
            vertex: z3.Int(f"depth_{index}")
            for index, vertex in enumerate(nodes)
        }
        for vertex in nodes:
            solver.add(label[vertex] >= -1, label[vertex] <= 4)
            solver.add(depth[vertex] >= 0, depth[vertex] < len(nodes))
        for index, root in enumerate(roots):
            solver.add(label[root] == index, depth[root] == 0)
            for vertex in nodes:
                if vertex == root:
                    continue
                solver.add(
                    z3.Implies(
                        label[vertex] == index,
                        z3.And(
                            depth[vertex] > 0,
                            z3.Or(
                                *(
                                    z3.And(
                                        label[neighbour] == index,
                                        depth[neighbour] < depth[vertex],
                                    )
                                    for neighbour in thin_closed[vertex]
                                )
                            ),
                        ),
                    )
                )
        for left in range(5):
            for right in range(left + 1, 5):
                solver.add(
                    z3.Or(
                        *(
                            z3.Or(
                                z3.And(label[x] == left, label[y] == right),
                                z3.And(label[x] == right, label[y] == left),
                            )
                            for x, y in thin_closed.edges()
                        )
                    )
                )
        if solver.check() == z3.sat:
            return True
    return False


def full_packets(graph: nx.Graph, shore):
    vertices = tuple(shore)
    packets = []
    for mask in range(1, 1 << len(vertices)):
        chosen = frozenset(
            vertices[index]
            for index in range(len(vertices))
            if mask >> index & 1
        )
        if not nx.is_connected(graph.subgraph(chosen)):
            continue
        if all(
            any(graph.has_edge(vertex, literal) for vertex in chosen)
            for literal in S
        ):
            packets.append(chosen)
    return packets


def packing_number(packets):
    best = 0

    def search(start, used, count):
        nonlocal best
        best = max(best, count)
        for index in range(start, len(packets)):
            if packets[index].isdisjoint(used):
                search(index + 1, used | packets[index], count + 1)

    search(0, frozenset(), 0)
    return best


def rooted_order_five_types():
    representatives = []
    unrooted_count = 0
    labelled_root_count = 0

    def same_root(left_attributes, right_attributes):
        return left_attributes["root"] == right_attributes["root"]

    for graph in nx.graph_atlas_g():
        if len(graph) != 5 or not nx.is_biconnected(graph):
            continue
        unrooted_count += 1
        graph = nx.convert_node_labels_to_integers(graph)
        for root in graph:
            if graph.degree(root) < 3:
                continue
            if not nx.is_connected(graph.subgraph(set(graph) - {root})):
                continue
            labelled_root_count += 1
            rooted = graph.copy()
            nx.set_node_attributes(rooted, False, "root")
            rooted.nodes[root]["root"] = True
            if any(
                nx.is_isomorphic(rooted, old, node_match=same_root)
                for old in representatives
            ):
                continue
            representatives.append(rooted)

    representatives.sort(
        key=lambda graph: (
            graph.number_of_edges(),
            nx.to_graph6_bytes(graph, header=False),
            next(graph.degree(v) for v in graph if graph.nodes[v]["root"]),
        )
    )
    return representatives, unrooted_count, labelled_root_count


def main() -> None:
    rooted_types, unrooted_count, labelled_root_count = rooted_order_five_types()
    assert unrooted_count == 10
    assert labelled_root_count == 32
    assert len(rooted_types) == 14

    cells = 0
    for index, thin in enumerate(rooted_types):
        root = next(vertex for vertex in thin if thin.nodes[vertex]["root"])
        graph6 = nx.to_graph6_bytes(thin, header=False).decode().strip()
        for frontier_name, frontier_edges in FRONTIERS.items():
            thin_sets, carrier_pairs, partitions, witness = exhaust_instance(
                f"atlas5_{index}",
                thin,
                root,
                frontier_name,
                frontier_edges,
                allow_sat=True,
            )
            cells += 1
            if witness is not None:
                host, thin_vertices = full_host(
                    thin, root, frontier_edges, witness
                )
                thin_closed = host.subgraph(thin_vertices | frozenset(S)).copy()
                packets = full_packets(host, thin_vertices)
                k7_model = spanning_minor_model(host, 7)
                rooted_terminal = rooted_k5(thin_closed)
                print(
                    "SAT",
                    "type",
                    index,
                    "graph6",
                    graph6,
                    "root",
                    root,
                    "root_degree",
                    thin.degree(root),
                    "thin_edges",
                    tuple(sorted(thin.edges())),
                    "frontier",
                    frontier_name,
                    "frontier_edges",
                    tuple(sorted(frontier_edges)),
                    "minimum_contact_count",
                    sum(map(len, witness.values())),
                    "contact_rows",
                    witness,
                    "host_connectivity",
                    nx.node_connectivity(host),
                    "thin_packet_number",
                    packing_number(packets),
                    "K7",
                    k7_model is not None,
                    "K7_model",
                    k7_model,
                    "S_rooted_K5",
                    rooted_terminal,
                )
                return
            print(
                "UNSAT",
                "type",
                index,
                "graph6",
                graph6,
                "root",
                root,
                "root_degree",
                thin.degree(root),
                "edges",
                thin.number_of_edges(),
                "frontier",
                frontier_name,
                "contact_maps",
                1 << 30,
                "connected_thin_sets",
                thin_sets,
                "carrier_pairs",
                carrier_pairs,
                "adaptive_partitions",
                partitions,
            )

    assert len(FRONTIERS) == 19
    assert cells == 266
    print(
        "GREEN",
        "unrooted_graphs",
        unrooted_count,
        "eligible_labelled_roots",
        labelled_root_count,
        "rooted_isomorphism_types",
        len(rooted_types),
        "frontiers",
        len(FRONTIERS),
        "unsat_cells",
        cells,
    )


if __name__ == "__main__":
    main()
