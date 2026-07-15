#!/usr/bin/env python3
"""Independent small-order audit for the universal five-root fan claim.

For every simple three-connected graph on five through seven vertices and every
five-set of roots, test for a rooted copy of F5 = K1 join P4 as a minor.
The six-vertex census also records the residue in which the sole nonroot
is incident with no contractible edge.  The script is an audit of the
finite induction bases, not a proof for unbounded order.
"""

from __future__ import annotations

import itertools
import subprocess

import networkx as nx


def three_connected(graph: nx.Graph) -> bool:
    return len(graph) >= 4 and nx.node_connectivity(graph) >= 3


def connected(graph: nx.Graph, vertices: set[int]) -> bool:
    return bool(vertices) and nx.is_connected(graph.subgraph(vertices))


def touch(graph: nx.Graph, left: set[int], right: set[int]) -> bool:
    return any(graph.has_edge(x, y) for x in left for y in right)


def fan_targets(roots: tuple[int, ...]) -> tuple[frozenset[tuple[int, int]], ...]:
    """All labelled edge sets isomorphic to K1 join P4 on the five roots."""
    answers = set()
    for centre in roots:
        leaves = tuple(root for root in roots if root != centre)
        for path in itertools.permutations(leaves):
            edges = {
                tuple(sorted((centre, leaf))) for leaf in leaves
            } | {
                tuple(sorted((path[i], path[i + 1]))) for i in range(3)
            }
            answers.add(frozenset(edges))
    return tuple(answers)


def rooted_fan_model(
    graph: nx.Graph, roots: tuple[int, ...]
) -> tuple[set[int], ...] | None:
    other = tuple(vertex for vertex in graph if vertex not in roots)
    for assignment in itertools.product(range(6), repeat=len(other)):
        bags = [{root} for root in roots]
        for vertex, owner in zip(other, assignment):
            if owner < 5:
                bags[owner].add(vertex)
        if not all(connected(graph, bag) for bag in bags):
            continue
        quotient = {
            tuple(sorted((roots[i], roots[j])))
            for i, j in itertools.combinations(range(5), 2)
            if touch(graph, bags[i], bags[j])
        }
        if any(target <= quotient for target in fan_targets(roots)):
            return tuple(bags)
    return None


def contract(graph: nx.Graph, x: int, y: int) -> nx.Graph:
    answer = nx.contracted_nodes(graph, x, y, self_loops=False)
    answer = nx.Graph(answer)
    answer.remove_edges_from(nx.selfloop_edges(answer))
    return answer


def contractible(graph: nx.Graph, x: int, y: int) -> bool:
    return three_connected(contract(graph, x, y))


def graphs_of_order(n: int):
    process = subprocess.Popen(
        ["geng", "-q", "-d3", str(n)], stdout=subprocess.PIPE
    )
    assert process.stdout is not None
    for raw in process.stdout:
        graph = nx.from_graph6_bytes(raw.strip())
        if three_connected(graph):
            yield graph
    assert process.wait() == 0


def main() -> None:
    for n in (5, 6, 7):
        graph_count = root_count = residue_count = 0
        for graph in graphs_of_order(n):
            graph_count += 1
            for roots in itertools.combinations(tuple(graph), 5):
                root_count += 1
                model = rooted_fan_model(graph, roots)
                assert model is not None, (
                    "COUNTEREXAMPLE",
                    nx.to_graph6_bytes(graph, header=False).strip().decode(),
                    roots,
                )
                if n == 6:
                    nonroot = next(vertex for vertex in graph if vertex not in roots)
                    if not any(
                        contractible(graph, nonroot, neighbour)
                        for neighbour in graph[nonroot]
                    ):
                        residue_count += 1
                        print(
                            "  residue",
                            nx.to_graph6_bytes(graph, header=False).strip().decode(),
                            f"nonroot={nonroot}",
                            f"edges={sorted(tuple(sorted(edge)) for edge in graph.edges())}",
                            f"model={model}",
                        )
        print(
            f"n={n} graphs={graph_count} root_sets={root_count} "
            f"nonroot_noncontractible_residues={residue_count} counterexamples=0"
        )


if __name__ == "__main__":
    main()
