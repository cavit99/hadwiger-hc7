#!/usr/bin/env python3
"""Audit the exact irreducible kernels for six prescribed terminals.

This is a falsifier/census for the accompanying hand theorem.  It checks
all simple three-connected graphs of orders six and seven.  At order seven
each possible sole nonterminal is distinguished, and only rooted instances
with no contractible edge incident with that nonterminal are retained.
"""

from __future__ import annotations

import itertools
import subprocess
import sys

sys.path.insert(0, "active/runtime/deps")
import networkx as nx  # noqa: E402


def graphs_of_order(order: int):
    process = subprocess.Popen(
        ["geng", "-q", "-c", "-d3", str(order)],
        stdout=subprocess.PIPE,
        text=True,
    )
    assert process.stdout is not None
    for line in process.stdout:
        yield nx.from_graph6_bytes(line.strip().encode())
    assert process.wait() == 0


def contracted_simple(graph: nx.Graph, x: int, y: int) -> nx.Graph:
    answer = nx.contracted_nodes(graph, x, y, self_loops=False)
    answer = nx.Graph(answer)
    answer.remove_edges_from(nx.selfloop_edges(answer))
    return answer


def incident_edges_noncontractible(graph: nx.Graph, vertex: int) -> bool:
    return all(
        nx.node_connectivity(contracted_simple(graph, vertex, neighbour)) < 3
        for neighbour in graph[vertex]
    )


def hamilton_cycles(graph: nx.Graph):
    vertices = tuple(graph)
    first = vertices[0]
    for tail in itertools.permutations(vertices[1:]):
        order = (first,) + tail
        if order[1] > order[-1]:
            continue
        if all(
            graph.has_edge(order[i], order[(i + 1) % len(order)])
            for i in range(len(order))
        ):
            yield order


def cycle_classification(graph: nx.Graph, extra: int):
    terminals = tuple(vertex for vertex in graph if vertex != extra)
    terminal_graph = graph.subgraph(terminals).copy()
    cycles = tuple(hamilton_cycles(terminal_graph))
    if not cycles:
        return None

    classifications = []
    for cycle in cycles:
        cycle_edges = {
            frozenset((cycle[i], cycle[(i + 1) % 6])) for i in range(6)
        }
        chords = tuple(
            sorted(
                tuple(sorted(edge))
                for edge in terminal_graph.edges
                if frozenset(edge) not in cycle_edges
            )
        )
        charged = tuple(
            index
            for index, terminal in enumerate(cycle)
            if graph.has_edge(extra, terminal)
            and terminal_graph.degree(terminal) == 2
        )
        hub_neighbours = tuple(
            index
            for index, terminal in enumerate(cycle)
            if graph.has_edge(extra, terminal)
        )
        chord_positions = tuple(
            sorted(
                tuple(sorted((cycle.index(x), cycle.index(y))))
                for x, y in chords
            )
        )
        classifications.append((chord_positions, charged, hub_neighbours))
    return min(classifications)


def main() -> None:
    order_six = 0
    nonhamiltonian_six = []
    for graph in graphs_of_order(6):
        if nx.node_connectivity(graph) < 3:
            continue
        order_six += 1
        if not any(hamilton_cycles(graph)):
            nonhamiltonian_six.append(
                nx.to_graph6_bytes(graph, header=False).decode().strip()
            )

    rooted_irreducible = 0
    nonhamiltonian_terminal_graph = []
    nonclassified = []
    records: dict[tuple, list[tuple[str, int]]] = {}
    for graph in graphs_of_order(7):
        if nx.node_connectivity(graph) < 3:
            continue
        graph6 = nx.to_graph6_bytes(graph, header=False).decode().strip()
        for extra in graph:
            if not incident_edges_noncontractible(graph, extra):
                continue
            rooted_irreducible += 1
            terminal_graph = graph.subgraph(set(graph) - {extra}).copy()
            if not any(hamilton_cycles(terminal_graph)):
                nonhamiltonian_terminal_graph.append((graph6, extra))
                continue
            classification = cycle_classification(graph, extra)
            assert classification is not None
            chords, charged, hub_neighbours = classification
            if len(charged) < 4 or len(chords) > 1:
                nonclassified.append(
                    (graph6, extra, chords, charged, hub_neighbours)
                )
            records.setdefault(classification, []).append((graph6, extra))

    print(
        "order6_three_connected",
        order_six,
        "nonhamiltonian",
        nonhamiltonian_six,
    )
    print(
        "order7_rooted_irreducible",
        rooted_irreducible,
        "nonhamiltonian_terminal_graph",
        nonhamiltonian_terminal_graph,
        "nonclassified",
        nonclassified,
    )
    print("rooted_classifications", len(records))
    for classification, examples in sorted(records.items()):
        print(classification, "count", len(examples), "example", examples[0])


if __name__ == "__main__":
    main()
