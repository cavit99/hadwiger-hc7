#!/usr/bin/env python3
"""Exact Z3 exhaustion of the order-four compulsory thin shore.

For every canonical width-two frontier and both possible order-four thin
graphs, rule out a literal contact map which satisfies all relative
seven-cut inequalities but admits no adaptive two-carrier allocation.
"""

from __future__ import annotations

import itertools
import sys
from pathlib import Path


DEPS = Path(__file__).resolve().parent / "runtime" / "deps"
if DEPS.exists():
    sys.path.insert(0, str(DEPS))

import networkx as nx
import z3


S = tuple(range(7))
U_LITERAL = 0
W = tuple(range(1, 7))
THIN = ("z", "a", "b", "c")
ROOT = "z"

# Generate the paired width-two boundary rather than choosing one arbitrary
# compulsory literal in each unrooted shape.  Before the final relabelling,
# the paired blocks are {0,1},{2,3},{4,5}, the paired singleton is 6, and
# the compulsory literal may be any of the six paired vertices (never the
# singleton).  Rooted isomorphism preserves only the compulsory literal:
# the adaptive carrier conclusion depends on the literal graph and u, not
# on the names of the three old equality pairs.
PAIRS = ((0, 1), (2, 3), (4, 5))
PAIRED_CENTRE = 6


def paired_boundary(graph: nx.Graph) -> bool:
    if any(graph.has_edge(*pair) for pair in PAIRS):
        return False
    if any(
        not any(graph.has_edge(PAIRED_CENTRE, vertex) for vertex in pair)
        for pair in PAIRS
    ):
        return False
    return all(
        any(graph.has_edge(x, y) for x in left for y in right)
        for left, right in itertools.combinations(PAIRS, 2)
    )


def width_two_form(graph: nx.Graph) -> bool:
    if nx.is_connected(graph):
        if graph.number_of_edges() == 6:
            return nx.is_tree(graph)
        if graph.number_of_edges() != 7:
            return False
        cycles = nx.cycle_basis(graph)
        return len(cycles) == 1 and len(cycles[0]) == 6

    components = [
        graph.subgraph(vertices).copy()
        for vertices in nx.connected_components(graph)
    ]
    if sorted(map(len, components)) != [3, 4]:
        return False
    small = next(component for component in components if len(component) == 3)
    large = next(component for component in components if len(component) == 4)
    return nx.is_isomorphic(small, nx.complete_graph(3)) and nx.is_isomorphic(
        large, nx.star_graph(3)
    )


def rooted_frontiers():
    allowed_edges = tuple(
        pair for pair in itertools.combinations(S, 2) if pair not in PAIRS
    )
    labelled = []
    for edge_count in (6, 7):
        for edges in itertools.combinations(allowed_edges, edge_count):
            graph = nx.Graph()
            graph.add_nodes_from(S)
            graph.add_edges_from(edges)
            if paired_boundary(graph) and width_two_form(graph):
                labelled.append(graph)
    assert len(labelled) == 192

    def same_root(left, right):
        return left["root"] == right["root"]

    representatives = []
    for graph in labelled:
        for root in range(6):
            rooted = graph.copy()
            nx.set_node_attributes(rooted, False, "root")
            rooted.nodes[root]["root"] = True
            if any(
                nx.is_isomorphic(rooted, old, node_match=same_root)
                for old in representatives
            ):
                continue
            representatives.append(rooted)
    assert len(representatives) == 19

    adjacent_centre = []
    for graph in labelled:
        for root in range(6):
            if not graph.has_edge(root, PAIRED_CENTRE):
                continue
            rooted = graph.copy()
            nx.set_node_attributes(rooted, False, "root")
            rooted.nodes[root]["root"] = True
            if any(
                nx.is_isomorphic(rooted, old, node_match=same_root)
                for old in adjacent_centre
            ):
                continue
            adjacent_centre.append(rooted)
    assert len(adjacent_centre) == 9

    normalized = []
    for rooted in representatives:
        root = next(vertex for vertex in rooted if rooted.nodes[vertex]["root"])
        others = sorted(set(rooted) - {root})
        mapping = {root: U_LITERAL}
        mapping.update({vertex: index + 1 for index, vertex in enumerate(others)})
        graph = nx.relabel_nodes(rooted, mapping, copy=True)
        normalized.append(graph)
    normalized.sort(
        key=lambda graph: (
            graph.number_of_edges(),
            graph.degree(U_LITERAL),
            nx.to_graph6_bytes(graph, header=False),
        )
    )
    return {
        f"rooted_frontier_{index:02d}": tuple(sorted(graph.edges()))
        for index, graph in enumerate(normalized)
    }


FRONTIERS = rooted_frontiers()

THIN_GRAPHS = {
    "k4_minus": (("z", "a"), ("z", "b"), ("z", "c"), ("a", "c"), ("b", "c")),
    "k4": tuple(itertools.combinations(THIN, 2)),
}


def connected_sets(graph: nx.Graph):
    vertices = tuple(graph)
    answer = []
    for mask in range(1, 1 << len(vertices)):
        chosen = frozenset(
            vertices[index]
            for index in range(len(vertices))
            if mask >> index & 1
        )
        if nx.is_connected(graph.subgraph(chosen)):
            answer.append(chosen)
    return answer


def adaptive_partitions(frontier: nx.Graph):
    """All ordered nonempty independent seeds with a clique reservoir."""
    answer = []
    for size in range(len(S) + 1):
        for reservoir_tuple in itertools.combinations(S, size):
            reservoir = frozenset(reservoir_tuple)
            if any(
                not frontier.has_edge(left, right)
                for left, right in itertools.combinations(reservoir, 2)
            ):
                continue
            free = tuple(literal for literal in S if literal not in reservoir)
            # Reversing the two seeds is handled explicitly in the solver.
            for mask in range(1, 1 << (len(free) - 1)):
                first = frozenset(
                    free[index]
                    for index in range(len(free))
                    if mask >> index & 1
                )
                second = frozenset(free) - first
                if not second:
                    continue
                if any(
                    frontier.has_edge(left, right)
                    for left, right in itertools.combinations(first, 2)
                ):
                    continue
                if any(
                    frontier.has_edge(left, right)
                    for left, right in itertools.combinations(second, 2)
                ):
                    continue
                answer.append((first, second, reservoir))
    return answer


def exhaust_instance(
    thin_name: str,
    thin: nx.Graph,
    root,
    frontier_name: str,
    frontier_edges,
    allow_sat: bool = False,
):
    vertices = tuple(thin)
    assert nx.is_biconnected(thin)
    assert thin.degree(root) >= 3
    assert nx.is_connected(thin.subgraph(set(vertices) - {root}))

    frontier = nx.Graph()
    frontier.add_nodes_from(S)
    frontier.add_edges_from(frontier_edges)

    contact = {
        (vertex, literal): z3.Bool(
            f"e_{thin_name}_{frontier_name}_{vertex}_{literal}"
        )
        for vertex in vertices
        for literal in W
    }
    solver = z3.Solver()

    # Root deletion normalization: A-z meets every noncompulsory literal.
    for literal in W:
        solver.add(
            z3.Or(*(contact[vertex, literal] for vertex in vertices if vertex != root))
        )

    # Every relative cut inequality for every connected thin-side set.
    thin_sets = connected_sets(thin)
    for chosen in thin_sets:
        internal_neighbours = {
            vertex
            for vertex in vertices
            if vertex not in chosen
            and any(thin.has_edge(vertex, old) for old in chosen)
        }
        boundary_terms = []
        if root in chosen:
            # zu is present, and no other thin vertex sees u.
            boundary_terms.append(z3.BoolVal(True))
        for literal in W:
            boundary_terms.append(
                z3.Or(*(contact[vertex, literal] for vertex in chosen))
            )
        solver.add(
            z3.PbGe(
                [(term, 1) for term in boundary_terms],
                7 - len(internal_neighbours),
            )
        )

    subsets = connected_sets(thin)
    carrier_pairs = [
        (left, right)
        for left in subsets
        for right in subsets
        if root in left
        and left.isdisjoint(right)
        and any(thin.has_edge(x, y) for x in left for y in right)
    ]
    partitions = adaptive_partitions(frontier)

    def hits(carrier: frozenset[str], literal: int):
        terms = []
        if literal == U_LITERAL and root in carrier:
            terms.append(z3.BoolVal(True))
        if literal in W:
            terms.extend(contact[vertex, literal] for vertex in carrier)
        return z3.Or(*terms) if terms else z3.BoolVal(False)

    # Negate every permitted adaptive return, in both seed orientations.
    for left, right in carrier_pairs:
        for first, second, _ in partitions:
            solver.add(
                z3.Not(
                    z3.And(
                        *(hits(left, literal) for literal in first),
                        *(hits(right, literal) for literal in second),
                    )
                )
            )
            solver.add(
                z3.Not(
                    z3.And(
                        *(hits(left, literal) for literal in second),
                        *(hits(right, literal) for literal in first),
                    )
                )
            )

    result = solver.check()
    if result == z3.sat and allow_sat:
        optimizer = z3.Optimize()
        optimizer.add(*solver.assertions())
        optimizer.minimize(
            z3.Sum(
                *(z3.If(variable, 1, 0) for variable in contact.values())
            )
        )
        assert optimizer.check() == z3.sat
        model = optimizer.model()
        witness = {
            vertex: tuple(
                literal
                for literal in W
                if z3.is_true(
                    model.eval(contact[vertex, literal], model_completion=True)
                )
            )
            for vertex in vertices
        }
        return len(thin_sets), len(carrier_pairs), len(partitions), witness
    assert result == z3.unsat
    if allow_sat:
        return len(thin_sets), len(carrier_pairs), len(partitions), None
    return len(thin_sets), len(carrier_pairs), len(partitions)


def exhaust(thin_name: str, thin_edges, frontier_name: str, frontier_edges):
    thin = nx.Graph()
    thin.add_nodes_from(THIN)
    thin.add_edges_from(thin_edges)
    return exhaust_instance(thin_name, thin, ROOT, frontier_name, frontier_edges)


def main() -> None:
    cells = 0
    for thin_name, thin_edges in THIN_GRAPHS.items():
        for frontier_name, frontier_edges in FRONTIERS.items():
            thin_sets, carrier_pairs, partitions = exhaust(
                thin_name, thin_edges, frontier_name, frontier_edges
            )
            cells += 1
            print(
                "UNSAT",
                thin_name,
                frontier_name,
                "contact_maps",
                1 << 24,
                "connected_thin_sets",
                thin_sets,
                "carrier_pairs",
                carrier_pairs,
                "adaptive_partitions",
                partitions,
            )
    assert len(FRONTIERS) == 19
    assert cells == 38
    print(
        "GREEN: every order-four compulsory atom has an adaptive carrier return",
        "rooted_frontiers",
        len(FRONTIERS),
        "unsat_cells",
        cells,
    )


if __name__ == "__main__":
    main()
