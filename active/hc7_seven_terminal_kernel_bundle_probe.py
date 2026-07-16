#!/usr/bin/env python3
"""Independent falsifier for the seven-terminal irreducible-kernel bundle.

This is evidence, not a dependency of the proof.  It enumerates all simple
three-connected graphs of orders seven and eight.  For order seven it counts
the labelled inclusion-minimal three-connected carrier masks.  For every
choice of seven terminals in order eight it tests terminal irreducibility and,
when irreducible, verifies the full charged-cycle owner bundle promised by the
hand theorem.
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


def three_connected(graph: nx.Graph) -> bool:
    return len(graph) >= 4 and nx.node_connectivity(graph) >= 3


def contractible(graph: nx.Graph, left: int, right: int) -> bool:
    quotient = nx.contracted_nodes(graph, left, right, self_loops=False)
    quotient = nx.Graph(quotient)
    quotient.remove_edges_from(nx.selfloop_edges(quotient))
    return three_connected(quotient)


def terminal_irreducible(graph: nx.Graph, terminals: frozenset[int]) -> bool:
    return not any(
        contractible(graph, left, right)
        for left, right in graph.edges
        if not (left in terminals and right in terminals)
    )


def hamilton_cycles(graph: nx.Graph, vertices: tuple[int, ...]):
    first = vertices[0]
    for tail in itertools.permutations(vertices[1:]):
        order = (first,) + tail
        if order[1] > order[-1]:
            continue
        if all(graph.has_edge(order[i], order[(i + 1) % 7]) for i in range(7)):
            yield order


def owner_quotient(graph: nx.Graph, extra: int, owner: int) -> nx.Graph:
    quotient = nx.contracted_nodes(graph, owner, extra, self_loops=False)
    quotient = nx.Graph(quotient)
    quotient.remove_edges_from(nx.selfloop_edges(quotient))
    return quotient


def verify_bundle(graph: nx.Graph, terminals: tuple[int, ...], extra: int) -> bool:
    terminal_graph = graph.subgraph(terminals)
    charged = tuple(
        terminal
        for terminal in terminals
        if graph.has_edge(extra, terminal) and graph.degree(terminal) == 3
    )
    if len(charged) < 4:
        return False
    for cycle in hamilton_cycles(terminal_graph, terminals):
        cycle_edges = {
            frozenset((cycle[i], cycle[(i + 1) % 7])) for i in range(7)
        }
        for charge_four in itertools.combinations(charged, 4):
            if not all(
                all(
                    quotient.has_edge(cycle[i], cycle[(i + 1) % 7])
                    for i in range(7)
                )
                and all(
                    quotient.has_edge(owner, other)
                    for other in charge_four
                    if other != owner
                )
                for owner in charge_four
                for quotient in (owner_quotient(graph, extra, owner),)
            ):
                return False

            # Every chord of this cycle has both ends outside the charged set.
            if any(
                frozenset(edge) not in cycle_edges
                and bool(set(edge) & set(charged))
                for edge in terminal_graph.edges
            ):
                return False
        return True
    return False


def labelled_mask(graph: nx.Graph, image: tuple[int, ...]) -> int:
    pairs = tuple(itertools.combinations(range(7), 2))
    index = {edge: position for position, edge in enumerate(pairs)}
    return sum(
        1 << index[tuple(sorted((image[left], image[right])))]
        for left, right in graph.edges
    )


def abstract_order_eight_patterns():
    """Enumerate the cycle/chord/contact patterns allowed by irreducibility."""

    cycle = {(i, (i + 1) % 7) for i in range(7)}
    cycle = {tuple(sorted(edge)) for edge in cycle}
    candidates = []

    # Seven charges: no chord is possible.
    candidates.append(((), (), tuple(range(7))))

    # Five charges: the two uncharged vertices support the unique chord.
    for uncharged in itertools.combinations(range(7), 2):
        chord = tuple(sorted(uncharged))
        if chord in cycle:
            continue
        charged = tuple(v for v in range(7) if v not in uncharged)
        for optional_count in range(3):
            for optional in itertools.combinations(uncharged, optional_count):
                candidates.append((uncharged, (chord,), charged + optional))

    # Four charges: the two chords on the three uncharged vertices form P3.
    for uncharged in itertools.combinations(range(7), 3):
        charged = tuple(v for v in range(7) if v not in uncharged)
        for centre in uncharged:
            chord_set = tuple(
                tuple(sorted((centre, end)))
                for end in uncharged
                if end != centre
            )
            if any(chord in cycle for chord in chord_set):
                continue
            for optional_count in range(4):
                for optional in itertools.combinations(uncharged, optional_count):
                    candidates.append((uncharged, chord_set, charged + optional))

    accepted = []
    for uncharged, chords, neighbours in candidates:
        graph = nx.Graph()
        graph.add_nodes_from(range(8))
        graph.add_edges_from(cycle)
        graph.add_edges_from(chords)
        graph.add_edges_from((7, vertex) for vertex in neighbours)
        if not three_connected(graph):
            continue
        if any(contractible(graph, 7, vertex) for vertex in neighbours):
            continue
        accepted.append((uncharged, tuple(sorted(chords)), tuple(sorted(neighbours)), graph))

    classes = []
    for pattern in accepted:
        for representative, members in classes:
            if nx.is_isomorphic(pattern[3], representative[3]):
                members.append(pattern)
                break
        else:
            classes.append((pattern, [pattern]))
    return accepted, classes


def main() -> None:
    minimal_labelled = set()
    minimal_unlabelled = 0
    for graph in graphs_of_order(7):
        if not three_connected(graph):
            continue
        if any(
            three_connected(nx.Graph(graph.edge_subgraph(set(graph.edges) - {edge})))
            for edge in graph.edges
        ):
            continue
        minimal_unlabelled += 1
        for image in itertools.permutations(range(7)):
            minimal_labelled.add(labelled_mask(graph, image))

    irreducible = 0
    failures = []
    records = set()
    labelled_order_eight = set()
    for graph in graphs_of_order(8):
        if not three_connected(graph):
            continue
        for extra in graph:
            terminals = tuple(vertex for vertex in graph if vertex != extra)
            terminal_set = frozenset(terminals)
            if not terminal_irreducible(graph, terminal_set):
                continue
            irreducible += 1
            charged = tuple(
                terminal
                for terminal in terminals
                if graph.has_edge(extra, terminal) and graph.degree(terminal) == 3
            )
            records.add((len(charged), tuple(sorted(dict(graph.subgraph(terminals).degree()).values()))))
            local_pairs = tuple(itertools.combinations(range(7), 2))
            local_index = {edge: position for position, edge in enumerate(local_pairs)}
            for order in itertools.permutations(terminals):
                inverse = {old: new for new, old in enumerate(order)}
                terminal_mask = sum(
                    1 << local_index[tuple(sorted((inverse[left], inverse[right])))]
                    for left, right in graph.subgraph(terminals).edges
                )
                neighbour_mask = sum(
                    1 << inverse[terminal]
                    for terminal in terminals
                    if graph.has_edge(extra, terminal)
                )
                labelled_order_eight.add((terminal_mask, neighbour_mask))
            if not verify_bundle(graph, terminals, extra):
                failures.append((nx.to_graph6_bytes(graph, header=False).decode().strip(), extra))

    print("minimal_order7_unlabelled", minimal_unlabelled)
    print("minimal_order7_labelled", len(minimal_labelled))
    print("order8_rooted_irreducible", irreducible)
    print("order8_labelled_exact_templates", len(labelled_order_eight))
    print("order8_profiles", sorted(records))
    print("bundle_failures", failures)
    accepted, classes = abstract_order_eight_patterns()
    print("abstract_accepted", len(accepted))
    print("abstract_isomorphism_classes", len(classes))
    for index, (representative, members) in enumerate(classes, 1):
        uncharged, chords, neighbours, _graph = representative
        print(
            "pattern",
            index,
            "uncharged",
            uncharged,
            "chords",
            chords,
            "extra_neighbours",
            neighbours,
            "cycle_presentations",
            len(members),
        )
    assert not failures
    assert len(classes) == 10


if __name__ == "__main__":
    main()
