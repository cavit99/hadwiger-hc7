#!/usr/bin/env python3
"""Falsify a seven-terminal rooted-kernel dichotomy through order eight.

For every simple three-connected graph on seven or eight vertices and every
choice of seven labelled terminals, test whether the terminals root either

* a seven-cycle; or
* ``K_{3,4}``.

There is at most one nonterminal, so an exact rooted model merely assigns
that vertex to one terminal bag or deletes it.  The script tests the stronger
statement for every three-connected graph, not only terminal-irreducible
kernels.  It is evidence and a falsifier, not a proof.
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


def quotient(graph: nx.Graph, terminals: tuple[int, ...], owner: int | None):
    nonterminals = tuple(set(graph) - set(terminals))
    assert len(nonterminals) <= 1
    extra = nonterminals[0] if nonterminals else None
    answer = nx.Graph()
    answer.add_nodes_from(terminals)
    for x, y in itertools.combinations(terminals, 2):
        adjacent = graph.has_edge(x, y)
        if extra is not None and owner is not None:
            adjacent |= x == owner and graph.has_edge(extra, y)
            adjacent |= y == owner and graph.has_edge(extra, x)
        if adjacent:
            answer.add_edge(x, y)
    return answer


def has_spanning_cycle(graph: nx.Graph, terminals: tuple[int, ...]) -> bool:
    first = terminals[0]
    return any(
        all(graph.has_edge(order[i], order[(i + 1) % 7]) for i in range(7))
        for order in ((first,) + tail for tail in itertools.permutations(terminals[1:]))
    )


def has_spanning_three_four_biclique(
    graph: nx.Graph, terminals: tuple[int, ...]
) -> bool:
    for clique in itertools.combinations(terminals, 3):
        rest = tuple(vertex for vertex in terminals if vertex not in clique)
        required = itertools.product(clique, rest)
        if all(graph.has_edge(x, y) for x, y in required):
            return True
    return False


def rooted_outcome(graph: nx.Graph, terminals: tuple[int, ...]) -> str | None:
    nonterminals = tuple(set(graph) - set(terminals))
    owners = (None,) + terminals if nonterminals else (None,)
    for owner in owners:
        if nonterminals and owner is not None and not graph.has_edge(nonterminals[0], owner):
            continue
        model = quotient(graph, terminals, owner)
        if has_spanning_cycle(model, terminals):
            return "C7"
        if has_spanning_three_four_biclique(model, terminals):
            return "K3,4"
    return None


def terminal_irreducible(graph: nx.Graph, terminals: tuple[int, ...]) -> bool:
    """Check that no edge incident with the sole nonterminal is contractible."""
    nonterminals = tuple(set(graph) - set(terminals))
    if not nonterminals:
        return True
    extra = nonterminals[0]
    for neighbour in graph[extra]:
        contracted = nx.contracted_nodes(graph, extra, neighbour, self_loops=False)
        contracted = nx.Graph(contracted)
        contracted.remove_edges_from(nx.selfloop_edges(contracted))
        if nx.node_connectivity(contracted) >= 3:
            return False
    return True


def main() -> None:
    for order in (7, 8):
        graph_count = 0
        rooted_count = 0
        outcomes = {"C7": 0, "K3,4": 0}
        irreducible = 0
        irreducible_biclique = set()
        irreducible_records = set()
        for graph in graphs_of_order(order):
            if nx.node_connectivity(graph) < 3:
                continue
            graph_count += 1
            for terminals in itertools.combinations(graph.nodes, 7):
                rooted_count += 1
                outcome = rooted_outcome(graph, tuple(terminals))
                if outcome is None:
                    print(
                        "COUNTEREXAMPLE",
                        "order",
                        order,
                        "graph6",
                        nx.to_graph6_bytes(graph, header=False).decode().strip(),
                        "terminals",
                        terminals,
                    )
                    return
                outcomes[outcome] += 1
                if terminal_irreducible(graph, tuple(terminals)):
                    irreducible += 1
                    extra = next(iter(set(graph) - set(terminals)), None)
                    if extra is not None:
                        terminal_graph = graph.subgraph(terminals)
                        charge = tuple(
                            sorted(
                                vertex
                                for vertex in terminals
                                if graph.has_edge(extra, vertex)
                                and graph.degree(vertex) == 3
                            )
                        )
                        irreducible_records.add(
                            (
                                nx.to_graph6_bytes(graph, header=False).decode().strip(),
                                extra,
                                len(charge),
                                tuple(sorted(dict(terminal_graph.degree()).values())),
                            )
                        )
                    if outcome == "K3,4":
                        irreducible_biclique.add(
                            (
                                nx.to_graph6_bytes(graph, header=False).decode().strip(),
                                extra,
                            )
                        )
        print(
            f"order={order} graphs={graph_count} rooted_sets={rooted_count} "
            f"outcomes={outcomes} irreducible={irreducible} "
            f"irreducible_biclique={len(irreducible_biclique)}"
        )
        if irreducible_biclique:
            print("  irreducible_biclique_examples", sorted(irreducible_biclique)[:20])
        if irreducible_records:
            print("  irreducible_records", sorted(irreducible_records))


if __name__ == "__main__":
    main()
