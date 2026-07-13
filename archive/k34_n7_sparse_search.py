"""Discovery search for the |C|=7 exceptional K3 disjoint K4 cell.

This is not a proof artifact.  It asks Z3 for a graph in either sparse
density cell (p,q)=(24,13) or (25,12), with the fixed neighbourhood
K3 disjoint K4, vertex connectivity at least seven, and no pair of
disjoint connected helper bags in C union A which both meet A and all
four B-neighbourhoods.
"""

from itertools import combinations, product

import networkx as nx
import z3


A = frozenset(range(3))
C = frozenset(range(3, 10))
B = frozenset(range(10, 14))
VTX = frozenset(range(15))
V = 14


def build(case: tuple[int, int]):
    variables: dict[tuple[int, int], z3.BoolRef] = {}

    def edge(x: int, y: int) -> z3.BoolRef:
        x, y = min(x, y), max(x, y)
        if x == y:
            return z3.BoolVal(False)
        if V in (x, y):
            other = y if x == V else x
            return z3.BoolVal(other in A | B)
        if x in A and y in A:
            return z3.BoolVal(True)
        if x in B and y in B:
            return z3.BoolVal(True)
        if (x in A and y in B) or (x in B and y in A):
            return z3.BoolVal(False)
        if (x, y) not in variables:
            variables[x, y] = z3.Bool(f"e_{x}_{y}")
        return variables[x, y]

    solver = z3.Solver()
    p, q = case
    solver.add(
        z3.Sum(
            [z3.If(edge(x, y), 1, 0) for x in C for y in A | B]
        )
        == p
    )
    solver.add(
        z3.Sum(
            [z3.If(edge(x, y), 1, 0) for x, y in combinations(sorted(C), 2)]
        )
        == q
    )

    degrees = {
        x: z3.Sum([z3.If(edge(x, y), 1, 0) for y in VTX - {x}])
        for x in VTX
    }
    for degree in degrees.values():
        solver.add(degree >= 7)

    # Dirac's contraction-critical neighbourhood lemma.  In a
    # 7-contraction-critical graph every degree-seven vertex has no
    # independent triple in its neighbourhood.
    for x in VTX:
        others = sorted(VTX - {x})
        for y, z, w in combinations(others, 3):
            solver.add(
                z3.Implies(
                    degrees[x] == 7,
                    z3.Or(
                        z3.Not(edge(x, y)),
                        z3.Not(edge(x, z)),
                        z3.Not(edge(x, w)),
                        edge(y, z),
                        edge(y, w),
                        edge(z, w),
                    ),
                )
            )

    universe = tuple(sorted(A | C))
    connected_cache: dict[frozenset[int], z3.BoolRef] = {}

    def connected(subset: frozenset[int]) -> z3.BoolRef:
        if subset in connected_cache:
            return connected_cache[subset]
        vertices = tuple(sorted(subset))
        if len(vertices) <= 1:
            result = z3.BoolVal(True)
        else:
            root, rest = vertices[0], vertices[1:]
            cut_contacts = []
            for mask in range(1 << len(rest)):
                left = {root} | {
                    rest[i] for i in range(len(rest)) if (mask >> i) & 1
                }
                if len(left) == len(vertices):
                    continue
                right = set(vertices) - left
                cut_contacts.append(z3.Or([edge(x, y) for x in left for y in right]))
            result = z3.And(cut_contacts)
        connected_cache[subset] = result
        return result

    # Enumerate all two-bag assignments; 0 means unused.  This also
    # permits a helper to contain two A vertices.
    for assignment in product(range(3), repeat=len(universe)):
        first = frozenset(universe[i] for i, value in enumerate(assignment) if value == 1)
        second = frozenset(universe[i] for i, value in enumerate(assignment) if value == 2)
        if not (first & A and second & A):
            continue
        if min(first & A) > min(second & A):
            continue
        hits = [
            z3.Or([edge(b, x) for x in helper])
            for b in B
            for helper in (first, second)
        ]
        solver.add(z3.Not(z3.And(connected(first), connected(second), *hits)))

    return solver, variables, edge


def main() -> None:
    for case in ((24, 13), (25, 12)):
        print("building", case, flush=True)
        solver, variables, edge = build(case)
        print("solving", case, flush=True)
        for iteration in range(1000):
            result = solver.check()
            if result != z3.sat:
                print(case, result, "after", iteration, "cuts", flush=True)
                break
            model = solver.model()
            edges = [
                (x, y)
                for x, y in combinations(sorted(VTX), 2)
                if z3.is_true(model.eval(edge(x, y), model_completion=True))
            ]
            graph = nx.Graph()
            graph.add_nodes_from(VTX)
            graph.add_edges_from(edges)
            connectivity = nx.node_connectivity(graph)
            if connectivity >= 7:
                print(case, "sat", "after", iteration, "cuts", flush=True)
                print("connectivity", connectivity, flush=True)
                print("degrees", dict(graph.degree()), flush=True)
                print("edges", edges, flush=True)
                break
            cut = nx.minimum_node_cut(graph)
            remainder = graph.copy()
            remainder.remove_nodes_from(cut)
            components = list(nx.connected_components(remainder))
            contacts = [
                edge(x, y)
                for first, second in combinations(components, 2)
                for x in first
                for y in second
                if not z3.is_false(edge(x, y))
            ]
            solver.add(z3.Or(contacts) if contacts else z3.BoolVal(False))
            if iteration % 25 == 0:
                print(case, "cut", iteration, connectivity, sorted(cut), flush=True)


if __name__ == "__main__":
    main()
