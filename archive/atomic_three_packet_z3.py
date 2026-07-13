"""Exact small-order audit of the strict-surplus three-packet conjecture.

The open shore has ``n`` vertices and seven labelled boundary portal
classes.  Labels (0,1), (2,3), (4,5) are the three demands; label 6 is
unused by the linkage.  We ask for:

* relative boundary order at least eight for every nonempty proper shore
  subset;
* a linkage for each two-demand subfamily; and
* no simultaneous three-demand linkage.

Connected carriers may be shrunk to simple paths, so the finite encoding
uses one Boolean for each demand and exact path-vertex mask.
"""

from __future__ import annotations

from itertools import combinations, permutations, product

from z3 import And, Bool, If, Not, Or, PbGe, Solver, sat


DEMANDS = ((0, 1), (2, 3), (4, 5))


def edge_name(left: int, right: int) -> str:
    left, right = sorted((left, right))
    return f"e_{left}_{right}"


def solve_order(n: int):
    solver = Solver()
    edge = {
        (left, right): Bool(edge_name(left, right))
        for left, right in combinations(range(n), 2)
    }
    portal = {
        (vertex, label): Bool(f"p_{vertex}_{label}")
        for vertex in range(n)
        for label in range(7)
    }

    def edge_var(left: int, right: int):
        return edge[tuple(sorted((left, right)))]

    # Every boundary label really contacts the shore.
    for label in range(7):
        solver.add(Or(*(portal[vertex, label] for vertex in range(n))))

    # Strict minimum-fragment surplus.
    full = (1 << n) - 1
    for mask in range(1, full):
        inside = [vertex for vertex in range(n) if mask & (1 << vertex)]
        outside = [vertex for vertex in range(n) if not mask & (1 << vertex)]
        indicators = []
        for vertex in outside:
            indicators.append(Or(*(edge_var(vertex, other) for other in inside)))
        for label in range(7):
            indicators.append(Or(*(portal[vertex, label] for vertex in inside)))
        solver.add(PbGe([(indicator, 1) for indicator in indicators], 8))

    # Carrier[demand, mask] means that some simple path with exactly this
    # vertex mask joins the two portal classes of the demand.
    carrier = {}
    for demand_index, (left_label, right_label) in enumerate(DEMANDS):
        for mask in range(1, 1 << n):
            vertices = tuple(vertex for vertex in range(n) if mask & (1 << vertex))
            terms = []
            for order in permutations(vertices):
                if len(order) > 1 and order[0] > order[-1]:
                    continue
                endpoint = Or(
                    And(portal[order[0], left_label], portal[order[-1], right_label]),
                    And(portal[order[0], right_label], portal[order[-1], left_label]),
                )
                path_edges = [edge_var(order[i], order[i + 1]) for i in range(len(order) - 1)]
                terms.append(And(endpoint, *path_edges))
            variable = Bool(f"c_{demand_index}_{mask}")
            solver.add(variable == Or(*terms))
            carrier[demand_index, mask] = variable

    # All three two-demand packets exist.
    masks = range(1, 1 << n)
    for first, second in combinations(range(3), 2):
        solver.add(Or(*(
            And(carrier[first, left_mask], carrier[second, right_mask])
            for left_mask in masks
            for right_mask in masks
            if not (left_mask & right_mask)
        )))

    # No triple linkage.  A disjoint triple is an assignment of each shore
    # vertex to one of the three path masks or to the unused class.
    triple_terms = []
    for assignment in product(range(4), repeat=n):
        path_masks = [0, 0, 0]
        for vertex, owner in enumerate(assignment):
            if owner < 3:
                path_masks[owner] |= 1 << vertex
        if not all(path_masks):
            continue
        triple_terms.append(And(*(
            carrier[index, path_masks[index]] for index in range(3)
        )))
    solver.add(Not(Or(*triple_terms)))

    result = solver.check()
    if result != sat:
        return result, None
    model = solver.model()
    graph_edges = [pair for pair, variable in edge.items() if bool(model.eval(variable))]
    rows = [
        [label for label in range(7) if bool(model.eval(portal[vertex, label]))]
        for vertex in range(n)
    ]
    return result, (graph_edges, rows)


def main() -> None:
    for order in range(2, 7):
        result, witness = solve_order(order)
        print("order", order, result)
        if witness is not None:
            print(" edges", witness[0])
            print(" rows", witness[1])


if __name__ == "__main__":
    main()
