#!/usr/bin/env python3
"""Falsification probe for the smallest concentrated K5-column expansion.

The pentagonal-bipyramid columns A0 and R0 are K5s and all other columns
are singletons.  Every edge allowed by the quotient is variable.  The SMT
instance requires the quotient contacts, minimum degree five, and no
alternating split of either clique column.  Separator CEGAR then asks for
five-connectivity.  Every added clause is necessary for five-connectivity.

This is a finite experiment, not an unbounded theorem.
"""

from __future__ import annotations

import itertools

import networkx as nx
import z3


LABELS = ("A0", "A1", "R0", "R1", "R2", "R3", "R4")
RIM = tuple(f"R{i}" for i in range(5))
COLUMNS = {
    "A0": tuple(f"a{i}" for i in range(5)),
    "R0": tuple(f"b{i}" for i in range(5)),
    **{label: (label,) for label in LABELS if label not in ("A0", "R0")},
}


def pb_edges() -> tuple[tuple[str, str], ...]:
    return tuple(
        [(apex, rim) for apex in ("A0", "A1") for rim in RIM]
        + [(RIM[i], RIM[(i + 1) % 5]) for i in range(5)]
    )


def ordered_edge(edge: frozenset[str]) -> tuple[str, str]:
    left, right = sorted(edge)
    return left, right


def main() -> None:
    vertices = tuple(itertools.chain.from_iterable(COLUMNS.values()))
    fixed: set[frozenset[str]] = set()
    variables: dict[frozenset[str], z3.BoolRef] = {}

    for column in COLUMNS.values():
        fixed |= {frozenset(edge) for edge in itertools.combinations(column, 2)}
    for left, right in pb_edges():
        for x in COLUMNS[left]:
            for y in COLUMNS[right]:
                edge = frozenset((x, y))
                if len(COLUMNS[left]) == len(COLUMNS[right]) == 1:
                    fixed.add(edge)
                else:
                    variables[edge] = z3.Bool("edge_" + "_".join(sorted(edge)))

    solver = z3.Solver()
    solver.set(random_seed=0)

    def edge_term(x: str, y: str):
        edge = frozenset((x, y))
        if edge in fixed:
            return z3.BoolVal(True)
        return variables[edge]

    for left, right in pb_edges():
        solver.add(
            z3.Or(
                *(
                    edge_term(x, y)
                    for x in COLUMNS[left]
                    for y in COLUMNS[right]
                )
            )
        )

    for x in vertices:
        incident = []
        for y in vertices:
            if x == y:
                continue
            edge = frozenset((x, y))
            if edge in fixed:
                incident.append((z3.BoolVal(True), 1))
            elif edge in variables:
                incident.append((variables[edge], 1))
        solver.add(z3.PbGe(incident, 5))

    cyclic_orders = {
        "A0": RIM,
        "R0": ("R4", "A0", "R1", "A1"),
    }

    def touches(side: set[str], label: str):
        return z3.Or(
            *(edge_term(x, y) for x in side for y in COLUMNS[label])
        )

    for owner, order in cyclic_orders.items():
        column = COLUMNS[owner]
        anchor = column[0]
        rest = column[1:]
        for mask in range(1 << len(rest)):
            left = {anchor} | {
                rest[index]
                for index in range(len(rest))
                if mask & (1 << index)
            }
            right = set(column) - left
            if not right:
                continue
            for indices in itertools.combinations(range(len(order)), 4):
                labels = tuple(order[index] for index in indices)
                for flip in (0, 1):
                    solver.add(
                        z3.Not(
                            z3.And(
                                *(
                                    touches(
                                        left if (position + flip) % 2 == 0 else right,
                                        labels[position],
                                    )
                                    for position in range(4)
                                )
                            )
                        )
                    )

    def model_graph(model: z3.ModelRef) -> nx.Graph:
        graph = nx.Graph()
        graph.add_nodes_from(vertices)
        graph.add_edges_from(ordered_edge(edge) for edge in sorted(fixed, key=ordered_edge))
        graph.add_edges_from(
            ordered_edge(edge)
            for edge, variable in sorted(variables.items(), key=lambda item: ordered_edge(item[0]))
            if z3.is_true(model.eval(variable, model_completion=True))
        )
        return graph

    cuts_added = 0
    while solver.check() == z3.sat:
        graph = model_graph(solver.model())
        if nx.node_connectivity(graph) >= 5:
            raise AssertionError("unexpected five-connected survivor")

        cut = nx.minimum_node_cut(graph)
        remainder = graph.copy()
        remainder.remove_nodes_from(cut)
        components = sorted(
            (set(component) for component in nx.connected_components(remainder)),
            key=lambda component: tuple(sorted(component)),
        )
        crossing = []
        for first, second in itertools.combinations(components, 2):
            for x in first:
                for y in second:
                    edge = frozenset((x, y))
                    if edge in variables:
                        crossing.append(variables[edge])
        solver.add(z3.Or(*crossing) if crossing else z3.BoolVal(False))
        cuts_added += 1

    assert cuts_added > 0
    print("UNSAT two-K5 PB nonsplit five-connectivity probe")


if __name__ == "__main__":
    main()
