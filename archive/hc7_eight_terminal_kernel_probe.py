#!/usr/bin/env python3
"""Falsify structural claims about eight-terminal irreducible kernels.

The order-nine scan uses nauty ``geng`` and the vendored NetworkX runtime.
It treats each vertex in turn as the unique nonterminal and retains exactly
the rooted graphs in which every incident edge is noncontractible.  The
order-ten branch is generated from the charged-partition structure forced by
Wu's theorem, rather than from all ten-vertex graphs.

This is a discovery probe, not a dependency of a proof.
"""

from __future__ import annotations

import collections
import itertools
import subprocess
import sys

sys.path.insert(0, "active/runtime/deps")
import networkx as nx  # noqa: E402


TERMINALS = tuple(range(8))
PAIRS = tuple(itertools.combinations(TERMINALS, 2))
PAIR_INDEX = {edge: position for position, edge in enumerate(PAIRS)}


def edge_mask(graph: nx.Graph) -> int:
    return sum(
        1 << PAIR_INDEX[tuple(sorted(edge))]
        for edge in graph.edges
    )


def carrier_masks() -> frozenset[int]:
    """All labelled C8, K3,5 and twisted-K3,5 masks."""

    cycle = nx.cycle_graph(8)
    k35 = nx.from_graph6_bytes(b"G?B~vo")
    twisted = nx.from_graph6_bytes(b"G?brvo")
    masks = set()
    for carrier in (cycle, k35, twisted):
        for image in itertools.permutations(TERMINALS):
            relabelled = nx.relabel_nodes(
                carrier,
                {old: new for old, new in enumerate(image)},
            )
            masks.add(edge_mask(relabelled))
    return frozenset(masks)


CARRIERS = carrier_masks()


def contains_carrier(graph: nx.Graph) -> bool:
    mask = edge_mask(graph)
    return any(carrier & mask == carrier for carrier in CARRIERS)


def quotient(graph: nx.Graph, absorptions: tuple[tuple[int, int], ...]) -> nx.Graph:
    answer = graph.copy()
    for owner, extra in absorptions:
        answer = nx.Graph(
            nx.contracted_nodes(answer, owner, extra, self_loops=False)
        )
        answer.remove_edges_from(nx.selfloop_edges(answer))
    assert set(answer) == set(TERMINALS)
    return answer


def hamiltonian(graph: nx.Graph, vertices: tuple[int, ...]) -> bool:
    first = vertices[0]
    index = {vertex: position for position, vertex in enumerate(vertices)}
    states = {(1 << index[first], first)}
    for _ in range(1, len(vertices)):
        following = set()
        for mask, last in states:
            for neighbour in graph.neighbors(last):
                position = index.get(neighbour)
                if position is not None and not (mask >> position & 1):
                    following.add((mask | 1 << position, neighbour))
        states = following
    full = (1 << len(vertices)) - 1
    return any(
        mask == full and graph.has_edge(last, first)
        for mask, last in states
    )


def edge_at_root_contractible(graph: nx.Graph, root: int, neighbour: int) -> bool:
    remainder = graph.copy()
    remainder.remove_nodes_from((root, neighbour))
    return nx.is_biconnected(remainder)


def rooted_irreducible(graph: nx.Graph, root: int) -> bool:
    return not any(
        edge_at_root_contractible(graph, root, neighbour)
        for neighbour in graph.neighbors(root)
    )


def order_nine_scan() -> None:
    process = subprocess.Popen(
        ["geng", "-q", "-d3", "9"],
        stdout=subprocess.PIPE,
        text=True,
    )
    assert process.stdout is not None
    graphs = three_connected = rooted = 0
    profiles = collections.Counter()
    nonhamiltonian = []
    carrier_failures = []
    for line in process.stdout:
        graph = nx.from_graph6_bytes(line.strip().encode())
        graphs += 1
        if nx.node_connectivity(graph) < 3:
            continue
        three_connected += 1
        for root in graph:
            if not rooted_irreducible(graph, root):
                continue
            rooted += 1
            old_terminals = tuple(vertex for vertex in graph if vertex != root)
            image = {old: new for new, old in enumerate(old_terminals)}
            image[root] = 8
            kernel = nx.relabel_nodes(graph, image)
            root = 8
            terminals = TERMINALS
            terminal_graph = kernel.subgraph(terminals)
            charged = tuple(
                terminal
                for terminal in terminals
                if kernel.has_edge(root, terminal) and kernel.degree(terminal) == 3
            )
            has_cycle = hamiltonian(terminal_graph, terminals)
            profile = (
                len(charged),
                tuple(sorted(dict(terminal_graph.degree()).values())),
                kernel.degree(root),
                has_cycle,
            )
            profiles[profile] += 1
            if not has_cycle:
                nonhamiltonian.append(
                    (
                        nx.to_graph6_bytes(kernel, header=False).decode().strip(),
                        root,
                        charged,
                        tuple(sorted(kernel.neighbors(root))),
                    )
                )
            if contains_carrier(terminal_graph):
                continue
            charged_owner_outcomes = {
                owner: contains_carrier(quotient(kernel, ((owner, root),)))
                for owner in charged
            }
            if not charged_owner_outcomes or not all(charged_owner_outcomes.values()):
                carrier_failures.append(
                    (
                        nx.to_graph6_bytes(kernel, header=False).decode().strip(),
                        root,
                        charged_owner_outcomes,
                    )
                )
    assert process.wait() == 0
    print("order9_graphs", graphs)
    print("order9_three_connected", three_connected)
    print("order9_rooted_irreducible", rooted)
    print("order9_profiles", len(profiles))
    for profile, multiplicity in sorted(profiles.items()):
        print("profile", multiplicity, profile)
    print("order9_nonhamiltonian", len(nonhamiltonian))
    for record in nonhamiltonian[:20]:
        print("nonhamiltonian", record)
    print("order9_carrier_failures", carrier_failures)


def order_ten_charged_candidates() -> None:
    terminals = TERMINALS
    cycle_edges = {
        tuple(sorted((position, (position + 1) % 8)))
        for position in terminals
    }
    accepted = []
    for charge_x in itertools.combinations(terminals, 4):
        charge_x = frozenset(charge_x)
        charge_y = frozenset(set(terminals) - charge_x)
        for xy in (False, True):
            graph = nx.Graph()
            graph.add_nodes_from(range(10))
            graph.add_edges_from(cycle_edges)
            graph.add_edges_from((8, terminal) for terminal in charge_x)
            graph.add_edges_from((9, terminal) for terminal in charge_y)
            if xy:
                graph.add_edge(8, 9)
            if nx.node_connectivity(graph) < 3:
                continue
            terminal_set = frozenset(terminals)
            if any(
                nx.node_connectivity(
                    nx.Graph(nx.contracted_nodes(graph, left, right, self_loops=False))
                )
                >= 3
                for left, right in graph.edges
                if not (left in terminal_set and right in terminal_set)
            ):
                continue
            owner_outcomes = {
                (owner_x, owner_y): contains_carrier(
                    quotient(graph, ((owner_x, 8), (owner_y, 9)))
                )
                for owner_x in charge_x
                for owner_y in charge_y
            }
            accepted.append((charge_x, xy, owner_outcomes))
    print("order10_cycle_colourings", len(accepted))
    print("order10_charge_sets", [(sorted(charge), xy) for charge, xy, _ in accepted])
    print(
        "order10_carrier_failures",
        [
            (sorted(charge), xy, owners)
            for charge, xy, owners in accepted
            if not all(owners.values())
        ],
    )


def order_eight_scan() -> None:
    process = subprocess.Popen(
        ["geng", "-q", "-d3", "8"],
        stdout=subprocess.PIPE,
        text=True,
    )
    assert process.stdout is not None
    three_connected = minimal = 0
    minimal_codes = []
    failures = []
    for line in process.stdout:
        graph = nx.from_graph6_bytes(line.strip().encode())
        if nx.node_connectivity(graph) < 3:
            continue
        three_connected += 1
        if any(
            nx.node_connectivity(nx.Graph(graph.edge_subgraph(set(graph.edges) - {edge}))) >= 3
            for edge in graph.edges
        ):
            continue
        minimal += 1
        code = nx.to_graph6_bytes(graph, header=False).decode().strip()
        minimal_codes.append(code)
        if not contains_carrier(graph):
            failures.append(code)
    assert process.wait() == 0
    print("order8_three_connected", three_connected)
    print("order8_edge_minimal", minimal)
    print("order8_minimal_codes", minimal_codes)
    print("order8_carrier_failures", failures)


def main() -> None:
    print("labelled_carrier_masks", len(CARRIERS))
    order_eight_scan()
    order_nine_scan()
    order_ten_charged_candidates()


if __name__ == "__main__":
    main()
