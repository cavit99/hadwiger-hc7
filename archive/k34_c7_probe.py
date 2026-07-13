"""Find a seven-vertex obstruction to the simple two-helper certificate.

This is a discovery probe, not a proof artifact.  It asks Z3 for a connected
graph C on seven vertices and A/C, B/C incidences satisfying the degree lower
bounds of the exceptional K3 disjoint-union K4 neighbourhood, but having no
two disjoint sets P,Q in C which are B-dominating and become connected after
adjoining two distinct A roots.
"""

from itertools import combinations

import networkx as nx
import z3


N = 7
V = tuple(range(N))
SUBSETS = tuple(range(1, 1 << N))
USE_EXACT_SEVEN_CONNECTIVITY = False


def members(mask: int) -> tuple[int, ...]:
    return tuple(x for x in V if mask >> x & 1)


def main() -> None:
    solver = z3.Solver()
    edge = {(x, y): z3.Bool(f"e_{x}_{y}") for x, y in combinations(V, 2)}
    a = {(i, x): z3.Bool(f"a_{i}_{x}") for i in range(3) for x in V}
    b = {(j, x): z3.Bool(f"b_{j}_{x}") for j in range(4) for x in V}
    v = "v"
    aa = tuple(f"a{i}" for i in range(3))
    bb = tuple(f"b{i}" for i in range(4))
    cc = tuple(f"c{x}" for x in V)

    def e(x: int, y: int) -> z3.BoolRef:
        return edge[tuple(sorted((x, y)))]

    # C is connected: every proper cut whose first side contains 0 is crossed.
    for mask in SUBSETS:
        if mask == (1 << N) - 1 or not (mask & 1):
            continue
        crossing = [e(x, y) for x in members(mask) for y in members(((1 << N) - 1) ^ mask)]
        solver.add(z3.Or(crossing))

    for i in range(3):
        solver.add(z3.PbGe([(a[i, x], 1) for x in V], 4))
    for j in range(4):
        solver.add(z3.PbGe([(b[j, x], 1) for x in V], 3))
    for x in V:
        terms = [(e(x, y), 1) for y in V if y != x]
        terms += [(a[i, x], 1) for i in range(3)]
        terms += [(b[j, x], 1) for j in range(4)]
        solver.add(z3.PbGe(terms, 7))

    # A much smaller necessary consequence of seven-connectivity.  For every
    # nonempty X in C, its external neighbourhood separates X from v and must
    # therefore have order at least seven.
    for mask in SUBSETS:
        side = members(mask)
        outside = members(((1 << N) - 1) ^ mask)
        neighbourhood_indicators = [
            z3.Or([e(x, y) for x in side]) for y in outside
        ]
        neighbourhood_indicators += [
            z3.Or([a[i, x] for x in side]) for i in range(3)
        ]
        neighbourhood_indicators += [
            z3.Or([b[j, x] for x in side]) for j in range(4)
        ]
        solver.add(z3.PbGe([(indicator, 1) for indicator in neighbourhood_indicators], 7))

    # Break only the harmless permutations within A and within B.
    a_code = [z3.Sum([z3.If(a[i, x], 1 << x, 0) for x in V]) for i in range(3)]
    b_code = [z3.Sum([z3.If(b[j, x], 1 << x, 0) for x in V]) for j in range(4)]
    solver.add(a_code[0] <= a_code[1], a_code[1] <= a_code[2])
    solver.add(b_code[0] <= b_code[1], b_code[1] <= b_code[2], b_code[2] <= b_code[3])

    connected_to_root: dict[tuple[int, int], z3.BoolRef] = {}
    b_dominating: dict[int, z3.BoolRef] = {}
    for mask in SUBSETS:
        side = members(mask)
        b_dominating[mask] = z3.And(
            [z3.Or([b[j, x] for x in side]) for j in range(4)]
        )
        for i in range(3):
            cut_conditions = []
            # The cut side containing the A root is root union X.  It suffices
            # to check every X properly contained in P.
            submask = mask
            while True:
                submask = (submask - 1) & mask
                if submask == mask:
                    continue
                complement = mask ^ submask
                crossing = [a[i, y] for y in members(complement)]
                crossing += [
                    e(x, y)
                    for x in members(submask)
                    for y in members(complement)
                ]
                cut_conditions.append(z3.Or(crossing))
                if submask == 0:
                    break
            connected_to_root[i, mask] = z3.And(cut_conditions)

    # Forbid every pair of disjoint B-dominating sets which can use distinct
    # A roots.  Unused vertices of C are allowed.
    for left in SUBSETS:
        for right in SUBSETS:
            if left >= right or left & right:
                continue
            for i in range(3):
                for j in range(3):
                    if i == j:
                        continue
                    solver.add(
                        z3.Not(
                            z3.And(
                                b_dominating[left],
                                b_dominating[right],
                                connected_to_root[i, left],
                                connected_to_root[j, right],
                            )
                        )
                    )

    # Exact seven-connectivity clauses.  On fifteen vertices it is enough to
    # require G-S connected for every six-set S: any smaller separator can be
    # enlarged to six vertices while retaining a vertex in two components.
    # Each cut of each remaining nine-set gives one crossing-edge clause.
    fixed_edges = {
        frozenset(pair)
        for pair in (
            tuple(combinations(aa, 2))
            + tuple(combinations(bb, 2))
            + tuple((v, x) for x in aa + bb)
        )
    }
    potential = {
        frozenset((cc[x], cc[y])): e(x, y) for x, y in combinations(V, 2)
    }
    potential.update(
        {frozenset((aa[i], cc[x])): a[i, x] for i in range(3) for x in V}
    )
    potential.update(
        {frozenset((bb[j], cc[x])): b[j, x] for j in range(4) for x in V}
    )
    variable_by_name = {var.decl().name(): var for var in potential.values()}

    if USE_EXACT_SEVEN_CONNECTIVITY:
        host_vertices = (v,) + aa + bb + cc
        connectivity_clauses: set[frozenset[str]] = set()
        all_vertices = frozenset(host_vertices)
        for deleted_tuple in combinations(host_vertices, 6):
            remaining = tuple(all_vertices - frozenset(deleted_tuple))
            anchor, tail = remaining[0], remaining[1:]
            for mask in range((1 << len(tail)) - 1):
                left = frozenset((anchor,)) | frozenset(
                    tail[i] for i in range(len(tail)) if mask >> i & 1
                )
                right = all_vertices - frozenset(deleted_tuple) - left
                crossing_pairs = {
                    frozenset((x, y)) for x in left for y in right
                }
                if fixed_edges & crossing_pairs:
                    continue
                names = frozenset(
                    potential[pair].decl().name()
                    for pair in crossing_pairs
                    if pair in potential
                )
                assert names
                connectivity_clauses.add(names)

        # Keep only inclusion-minimal clauses; supersets are redundant.
        minimal_clauses: list[frozenset[str]] = []
        for names in sorted(connectivity_clauses, key=len):
            if not any(previous <= names for previous in minimal_clauses):
                minimal_clauses.append(names)
        print(
            "seven-connectivity clauses",
            len(connectivity_clauses),
            "minimal",
            len(minimal_clauses),
        )
        for start in range(0, len(minimal_clauses), 1000):
            solver.add(
                *[
                    z3.Or([variable_by_name[name] for name in names])
                    for names in minimal_clauses[start : start + 1000]
                ]
            )

    def extract_host(model: z3.ModelRef) -> tuple[nx.Graph, list[tuple[int, int]], list[tuple[int, ...]], list[tuple[int, ...]]]:
        c_edges = [xy for xy, var in edge.items() if z3.is_true(model.eval(var))]
        a_rows = [tuple(x for x in V if z3.is_true(model.eval(a[i, x]))) for i in range(3)]
        b_rows = [tuple(x for x in V if z3.is_true(model.eval(b[j, x]))) for j in range(4)]
        host = nx.Graph()
        host.add_nodes_from((v,) + aa + bb + cc)
        host.add_edges_from(combinations(aa, 2))
        host.add_edges_from(combinations(bb, 2))
        host.add_edges_from((v, x) for x in aa + bb)
        host.add_edges_from((cc[x], cc[y]) for x, y in c_edges)
        for i, row in enumerate(a_rows):
            host.add_edges_from((aa[i], cc[x]) for x in row)
        for j, row in enumerate(b_rows):
            host.add_edges_from((bb[j], cc[x]) for x in row)
        return host, c_edges, a_rows, b_rows

    def variable_for_pair(x: str, y: str) -> z3.BoolRef | None:
        if x[0] == "c" and y[0] == "c":
            return e(int(x[1:]), int(y[1:]))
        if x[0] == "c":
            x, y = y, x
        if x[0] == "a" and y[0] == "c":
            return a[int(x[1:]), int(y[1:])]
        if x[0] == "b" and y[0] == "c":
            return b[int(x[1:]), int(y[1:])]
        return None

    # With exact connectivity enabled, the lazy check verifies the full clause
    # family.  Otherwise it reports the first model satisfying only the compact
    # external-neighbourhood inequalities.
    cuts_added = 0
    while True:
        status = solver.check()
        print("solve", cuts_added, status)
        if status != z3.sat:
            return
        model = solver.model()
        host, c_edges, a_rows, b_rows = extract_host(model)
        connectivity = nx.node_connectivity(host)
        if connectivity >= 7 or not USE_EXACT_SEVEN_CONNECTIVITY:
            break
        separator = nx.minimum_node_cut(host)
        remainder = host.copy()
        remainder.remove_nodes_from(separator)
        components = sorted(nx.connected_components(remainder), key=len)
        left = components[0]
        right = set(remainder) - set(left)
        crossing_variables = {
            variable
            for x in left
            for y in right
            if (variable := variable_for_pair(x, y)) is not None
        }
        assert crossing_variables
        solver.add(z3.Or(tuple(crossing_variables)))
        cuts_added += 1

    print("C edges", c_edges)
    print("A rows", a_rows)
    print("B rows", b_rows)
    print("host order/size", host.number_of_nodes(), host.number_of_edges())
    print("minimum degree", min(dict(host.degree()).values()))
    print("vertex connectivity", connectivity)
    print("separation cuts added", cuts_added)
    print("chromatic upper bound (greedy)", max(nx.coloring.greedy_color(host).values()) + 1)


if __name__ == "__main__":
    main()
