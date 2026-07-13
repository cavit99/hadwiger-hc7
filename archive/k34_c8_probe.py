"""Search the |C|=8 exceptional cell for a no-helper incidence system.

The base search imposes connected C, boundary row lower bounds, degree at
least seven at C, and absence of the *actual* two Lemma 1.1 helpers (including
a singleton/pair split of A).  The 255 necessary kappa-seven shore
inequalities are added lazily.  A resulting model is then checked for full
vertex connectivity of the 16-vertex host.

This is a discovery probe, not a proof artifact.
"""

from itertools import combinations

import networkx as nx
import z3


N = 8
V = tuple(range(N))
FULL = (1 << N) - 1
SUBSETS = tuple(range(1, 1 << N))
ROOT_SUBSETS = tuple(range(1, 1 << 3))


def members(mask: int) -> tuple[int, ...]:
    return tuple(x for x in V if mask >> x & 1)


def main() -> None:
    solver = z3.Tactic("qffpbv").solver()
    c_edge = {(x, y): z3.Bool(f"e_{x}_{y}") for x, y in combinations(V, 2)}
    a = {(i, x): z3.Bool(f"a_{i}_{x}") for i in range(3) for x in V}
    b = {(j, x): z3.Bool(f"b_{j}_{x}") for j in range(4) for x in V}

    def ce(x: int, y: int) -> z3.BoolRef:
        return c_edge[tuple(sorted((x, y)))]

    # Connectedness of C: one representative of every proper cut.
    for mask in SUBSETS:
        if mask == FULL or not mask & 1:
            continue
        solver.add(
            z3.Or(
                [
                    ce(x, y)
                    for x in members(mask)
                    for y in members(FULL ^ mask)
                ]
            )
        )

    for i in range(3):
        solver.add(z3.PbGe([(a[i, x], 1) for x in V], 4))
    for j in range(4):
        solver.add(z3.PbGe([(b[j, x], 1) for x in V], 3))
    for x in V:
        terms = [(ce(x, y), 1) for y in V if y != x]
        terms += [(a[i, x], 1) for i in range(3)]
        terms += [(b[j, x], 1) for j in range(4)]
        solver.add(z3.PbGe(terms, 7))

    # Only harmless permutations inside the two boundary cliques.
    a_code = [z3.Sum([z3.If(a[i, x], 1 << x, 0) for x in V]) for i in range(3)]
    b_code = [z3.Sum([z3.If(b[j, x], 1 << x, 0) for x in V]) for j in range(4)]
    solver.add(a_code[0] <= a_code[1], a_code[1] <= a_code[2])
    solver.add(b_code[0] <= b_code[1], b_code[1] <= b_code[2], b_code[2] <= b_code[3])

    # h[R,P] exactly means that P union the nonempty A-root set R is
    # connected and that P meets every B-neighbourhood.
    helper = {}
    for mask in SUBSETS:
        side = members(mask)
        b_complete = z3.And([z3.Or([b[j, x] for x in side]) for j in range(4)])
        for roots in ROOT_SUBSETS:
            cuts = []
            submask = mask
            while submask:
                crossing = [
                    a[i, x]
                    for i in range(3)
                    if roots >> i & 1
                    for x in members(submask)
                ]
                crossing += [
                    ce(x, y)
                    for x in members(submask)
                    for y in members(mask ^ submask)
                ]
                cuts.append(z3.Or(crossing))
                submask = (submask - 1) & mask
            value = z3.Bool(f"h_{roots}_{mask}")
            solver.add(value == z3.And(b_complete, *cuts))
            helper[roots, mask] = value

    # Forbid every pair of actual helpers.  The C-parts and A-parts are both
    # disjoint; unused C and A vertices are permitted.
    for left in SUBSETS:
        for right in SUBSETS:
            if left >= right or left & right:
                continue
            for left_roots in ROOT_SUBSETS:
                for right_roots in ROOT_SUBSETS:
                    if not left_roots & right_roots:
                        solver.add(
                            z3.Not(
                                z3.And(
                                    helper[left_roots, left],
                                    helper[right_roots, right],
                                )
                            )
                        )

    def enforce_boundary(mask: int) -> None:
        side = members(mask)
        outside = members(FULL ^ mask)
        indicators = [z3.Or([ce(x, y) for x in side]) for y in outside]
        indicators += [z3.Or([a[i, x] for x in side]) for i in range(3)]
        indicators += [z3.Or([b[j, x] for x in side]) for j in range(4)]
        solver.add(z3.PbGe([(term, 1) for term in indicators], 7))

    v_name = "v"
    a_names = tuple(f"a{i}" for i in range(3))
    b_names = tuple(f"b{i}" for i in range(4))
    c_names = tuple(f"c{x}" for x in V)

    def extract(model: z3.ModelRef):
        c_edges = [edge for edge, variable in c_edge.items() if z3.is_true(model.eval(variable))]
        a_rows = [tuple(x for x in V if z3.is_true(model.eval(a[i, x]))) for i in range(3)]
        b_rows = [tuple(x for x in V if z3.is_true(model.eval(b[j, x]))) for j in range(4)]
        host = nx.Graph()
        host.add_nodes_from((v_name,) + a_names + b_names + c_names)
        host.add_edges_from(combinations(a_names, 2))
        host.add_edges_from(combinations(b_names, 2))
        host.add_edges_from((v_name, x) for x in a_names + b_names)
        host.add_edges_from((c_names[x], c_names[y]) for x, y in c_edges)
        for i, row in enumerate(a_rows):
            host.add_edges_from((a_names[i], c_names[x]) for x in row)
        for j, row in enumerate(b_rows):
            host.add_edges_from((b_names[j], c_names[x]) for x in row)
        return host, c_edges, a_rows, b_rows

    enforced = set()
    while True:
        status = solver.check()
        print("solve", len(enforced), status, flush=True)
        if status != z3.sat:
            return
        model = solver.model()
        host, c_edges, a_rows, b_rows = extract(model)
        if not enforced:
            print("initial C edges", c_edges, flush=True)
            print("initial A rows", a_rows, flush=True)
            print("initial B rows", b_rows, flush=True)

        violations = []
        for mask in SUBSETS:
            side = {c_names[x] for x in members(mask)}
            boundary = set().union(*(set(host.neighbors(x)) for x in side)) - side
            if len(boundary) < 7:
                violations.append(mask)
        if violations:
            new_violations = [mask for mask in violations if mask not in enforced]
            if not new_violations:
                raise AssertionError("only repeated violated boundaries")
            print("adding boundary masks", new_violations, flush=True)
            for violation in new_violations:
                enforced.add(violation)
                enforce_boundary(violation)
            continue

        print("BOUNDARY-FEASIBLE NO-HELPER MODEL")
        print("C edges", c_edges)
        print("A rows", a_rows)
        print("B rows", b_rows)
        print("host order/size", host.number_of_nodes(), host.number_of_edges())
        print("minimum degree", min(dict(host.degree()).values()))
        print("vertex connectivity", nx.node_connectivity(host))
        print("minimum cut", nx.minimum_node_cut(host))
        return


if __name__ == "__main__":
    main()
