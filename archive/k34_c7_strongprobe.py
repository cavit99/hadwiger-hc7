"""Discovery probe for the |C|=7 two-helper lemma under kappa(G) >= 7.

Unlike k34_c7_probe.py, a violated cut is strengthened to the complete
connectivity condition after deleting a six-set.  Since any separator of
order at most six can be extended to such a six-set while leaving vertices
in two components, enforcing all encountered six-deletions is equivalent to
seven-connectivity when the loop terminates.

This remains a discovery search, not a proof artifact.
"""

from itertools import combinations

import networkx as nx
import z3


N = 7
ENFORCE_C_BOUNDARIES = False
ENFORCE_DIRAC_NEIGHBOURHOODS = False
ENFORCE_SPARSE_EQUALITY_CASES = False
C_VERTICES = tuple(range(N))
C_SUBSETS = tuple(range(1, 1 << N))
V = "v"
A = tuple(f"a{i}" for i in range(3))
B = tuple(f"b{i}" for i in range(4))
C = tuple(f"c{i}" for i in C_VERTICES)
HOST_VERTICES = (V,) + A + B + C


def members(mask: int) -> tuple[int, ...]:
    return tuple(x for x in C_VERTICES if mask >> x & 1)


def main() -> None:
    solver = z3.Tactic("qffpbv").solver()
    c_edge = {
        (x, y): z3.Bool(f"e_{x}_{y}")
        for x, y in combinations(C_VERTICES, 2)
    }
    a_edge = {
        (i, x): z3.Bool(f"a_{i}_{x}")
        for i in range(3)
        for x in C_VERTICES
    }
    b_edge = {
        (j, x): z3.Bool(f"b_{j}_{x}")
        for j in range(4)
        for x in C_VERTICES
    }

    def ce(x: int, y: int) -> z3.BoolRef:
        return c_edge[tuple(sorted((x, y)))]

    # C is connected.
    for mask in C_SUBSETS:
        if mask == (1 << N) - 1 or not mask & 1:
            continue
        solver.add(
            z3.Or(
                [
                    ce(x, y)
                    for x in members(mask)
                    for y in members(((1 << N) - 1) ^ mask)
                ]
            )
        )

    # Boundary row lower bounds and degrees of C vertices in the full host.
    for i in range(3):
        solver.add(z3.PbGe([(a_edge[i, x], 1) for x in C_VERTICES], 4))
    for j in range(4):
        solver.add(z3.PbGe([(b_edge[j, x], 1) for x in C_VERTICES], 3))
    for x in C_VERTICES:
        terms = [(ce(x, y), 1) for y in C_VERTICES if y != x]
        terms += [(a_edge[i, x], 1) for i in range(3)]
        terms += [(b_edge[j, x], 1) for j in range(4)]
        solver.add(z3.PbGe(terms, 7))

    if ENFORCE_SPARSE_EQUALITY_CASES:
        p_terms = [
            a_edge[i, x] for i in range(3) for x in C_VERTICES
        ] + [b_edge[j, x] for j in range(4) for x in C_VERTICES]
        q_terms = list(c_edge.values())
        solver.add(
            z3.Or(
                z3.And(z3.PbEq([(term, 1) for term in p_terms], 25),
                       z3.PbEq([(term, 1) for term in q_terms], 12)),
                z3.And(z3.PbEq([(term, 1) for term in p_terms], 24),
                       z3.PbEq([(term, 1) for term in q_terms], 13)),
            )
        )

    if ENFORCE_DIRAC_NEIGHBOURHOODS:
        # In a contraction-critical minimal counterexample, every C-vertex of
        # degree exactly seven has no independent triple in its neighbourhood.
        # The possible neighbours of c_x are the other C vertices and A union B
        # (v is not adjacent to C).
        typed_vertices = (
            tuple(("a", i) for i in range(3))
            + tuple(("b", j) for j in range(4))
            + tuple(("c", y) for y in C_VERTICES)
        )

        def incident_to_c(x: int, vertex: tuple[str, int]) -> z3.BoolRef | bool:
            kind, index = vertex
            if kind == "a":
                return a_edge[index, x]
            if kind == "b":
                return b_edge[index, x]
            if index == x:
                return False
            return ce(index, x)

        def typed_edge(
            first: tuple[str, int], second: tuple[str, int]
        ) -> z3.BoolRef | bool:
            (first_kind, first_index), (second_kind, second_index) = first, second
            if first_kind == second_kind == "a":
                return True
            if first_kind == second_kind == "b":
                return True
            if {first_kind, second_kind} == {"a", "b"}:
                return False
            if first_kind == second_kind == "c":
                return ce(first_index, second_index)
            if first_kind == "c":
                first_kind, second_kind = second_kind, first_kind
                first_index, second_index = second_index, first_index
            if first_kind == "a" and second_kind == "c":
                return a_edge[first_index, second_index]
            if first_kind == "b" and second_kind == "c":
                return b_edge[first_index, second_index]
            return False

        for x in C_VERTICES:
            degree_terms = [(ce(x, y), 1) for y in C_VERTICES if y != x]
            degree_terms += [(a_edge[i, x], 1) for i in range(3)]
            degree_terms += [(b_edge[j, x], 1) for j in range(4)]
            degree_is_seven = z3.PbEq(degree_terms, 7)
            candidates = tuple(vertex for vertex in typed_vertices if vertex != ("c", x))
            for triple in combinations(candidates, 3):
                internal = [typed_edge(y, z) for y, z in combinations(triple, 2)]
                if True in internal:
                    continue
                neighbour_terms = [incident_to_c(x, vertex) for vertex in triple]
                solver.add(
                    z3.Implies(
                        z3.And(degree_is_seven, *neighbour_terms),
                        z3.Or([term for term in internal if term is not False]),
                    )
                )

    # If the full host is seven-connected, then for every nonempty X in C,
    # N_G(X) separates X from v and therefore has order at least seven.  This
    # compact family of 127 necessary inequalities is much stronger than the
    # singleton degree constraints above.
    def enforce_c_boundary(mask: int) -> None:
        side = members(mask)
        outside = members(((1 << N) - 1) ^ mask)
        neighbour_indicators = [
            z3.Or([ce(x, y) for x in side]) for y in outside
        ]
        neighbour_indicators += [
            z3.Or([a_edge[i, x] for x in side]) for i in range(3)
        ]
        neighbour_indicators += [
            z3.Or([b_edge[j, x] for x in side]) for j in range(4)
        ]
        solver.add(
            z3.PbGe([(indicator, 1) for indicator in neighbour_indicators], 7)
        )

    if ENFORCE_C_BOUNDARIES:
        for mask in C_SUBSETS:
            enforce_c_boundary(mask)

    # Symmetry only inside A and inside B.
    a_code = [
        z3.Sum([z3.If(a_edge[i, x], 1 << x, 0) for x in C_VERTICES])
        for i in range(3)
    ]
    b_code = [
        z3.Sum([z3.If(b_edge[j, x], 1 << x, 0) for x in C_VERTICES])
        for j in range(4)
    ]
    solver.add(a_code[0] <= a_code[1], a_code[1] <= a_code[2])
    solver.add(
        b_code[0] <= b_code[1],
        b_code[1] <= b_code[2],
        b_code[2] <= b_code[3],
    )

    # h[R,P] is equivalent to: P meets every B row and P union R is
    # connected, where R is a nonempty subset of the A-clique.  The cut test
    # fixes all roots on one side and checks every proper subset of P there.
    helper: dict[tuple[int, int], z3.BoolRef] = {}
    for mask in C_SUBSETS:
        side = members(mask)
        b_dominating = z3.And(
            [z3.Or([b_edge[j, x] for x in side]) for j in range(4)]
        )
        for root_mask in range(1, 1 << 3):
            cuts = []
            root_side = mask
            while True:
                root_side = (root_side - 1) & mask
                complement = mask ^ root_side
                crossing = [
                    a_edge[i, y]
                    for i in range(3)
                    if root_mask >> i & 1
                    for y in members(complement)
                ]
                crossing += [
                    ce(x, y)
                    for x in members(root_side)
                    for y in members(complement)
                ]
                cuts.append(z3.Or(crossing))
                if root_side == 0:
                    break
            helper[root_mask, mask] = z3.And(b_dominating, *cuts)

    # No two disjoint helpers may use disjoint nonempty subsets of A.  It is
    # harmless to leave an A-vertex unused.
    for left in C_SUBSETS:
        for right in C_SUBSETS:
            if left >= right or left & right:
                continue
            for first_roots in range(1, 1 << 3):
                for second_roots in range(1, 1 << 3):
                    if not first_roots & second_roots:
                        solver.add(
                            z3.Not(
                                z3.And(
                                    helper[first_roots, left],
                                    helper[second_roots, right],
                                )
                            )
                        )

    def variable_edge(x: str, y: str) -> z3.BoolRef | bool:
        """Return the edge's Boolean variable, or its fixed truth value."""
        if x > y:
            x, y = y, x
        if x == V or y == V:
            other = y if x == V else x
            return other in A or other in B
        if x in A and y in A:
            return True
        if x in B and y in B:
            return True
        if (x in A and y in B) or (x in B and y in A):
            return False
        if x in C and y in C:
            return ce(int(x[1:]), int(y[1:]))
        if x in A and y in C:
            return a_edge[int(x[1:]), int(y[1:])]
        if x in B and y in C:
            return b_edge[int(x[1:]), int(y[1:])]
        if y in A and x in C:
            return a_edge[int(y[1:]), int(x[1:])]
        if y in B and x in C:
            return b_edge[int(y[1:]), int(x[1:])]
        return False

    def extract(model: z3.ModelRef) -> nx.Graph:
        host = nx.Graph()
        host.add_nodes_from(HOST_VERTICES)
        for x, y in combinations(HOST_VERTICES, 2):
            value = variable_edge(x, y)
            if value is True or (
                value is not False and z3.is_true(model.eval(value))
            ):
                host.add_edge(x, y)
        return host

    def enforce_connected_after(deleted: frozenset[str]) -> int:
        """Add every cut inequality for the induced nine-vertex graph."""
        remaining = tuple(x for x in HOST_VERTICES if x not in deleted)
        assert len(remaining) == 9
        anchor, others = remaining[0], remaining[1:]
        added = 0
        for bits in range((1 << len(others)) - 1):
            left = {anchor}
            left.update(others[i] for i in range(len(others)) if bits >> i & 1)
            right = set(remaining) - left
            crossing = [variable_edge(x, y) for x in left for y in right]
            if True in crossing:
                continue
            variables = [value for value in crossing if value is not False]
            solver.add(z3.Or(variables))
            added += 1
        return added

    deletion_sets: set[frozenset[str]] = set()
    c_boundary_masks: set[int] = set()
    clauses_added = 0
    while True:
        status = solver.check()
        print(
            "solve",
            len(c_boundary_masks),
            len(deletion_sets),
            clauses_added,
            status,
            flush=True,
        )
        if status != z3.sat:
            return
        model = solver.model()
        host = extract(model)

        violated_mask = None
        for mask in C_SUBSETS:
            side = {C[x] for x in members(mask)}
            boundary = set().union(*(set(host.neighbors(x)) for x in side)) - side
            if len(boundary) < 7:
                violated_mask = mask
                break
        if violated_mask is not None:
            if violated_mask in c_boundary_masks:
                raise AssertionError("repeated violated C-boundary inequality")
            c_boundary_masks.add(violated_mask)
            enforce_c_boundary(violated_mask)
            continue

        connectivity = nx.node_connectivity(host)
        if connectivity >= 7:
            print("SEVEN-CONNECTED OBSTRUCTION")
            print("C edges", sorted((x, y) for x, y in host.edges() if x in C and y in C))
            print("A rows", [sorted(set(host.neighbors(a)) & set(C)) for a in A])
            print("B rows", [sorted(set(host.neighbors(b)) & set(C)) for b in B])
            print("order/size", host.number_of_nodes(), host.number_of_edges())
            print("minimum degree", min(dict(host.degree()).values()))
            print("vertex connectivity", connectivity)
            return

        separator = set(nx.minimum_node_cut(host))
        remainder = host.copy()
        remainder.remove_nodes_from(separator)
        components = list(nx.connected_components(remainder))
        keep = {next(iter(components[0])), next(iter(components[1]))}
        available = [x for x in HOST_VERTICES if x not in separator | keep]
        deleted = frozenset(separator | set(available[: 6 - len(separator)]))
        assert len(deleted) == 6
        check = host.copy()
        check.remove_nodes_from(deleted)
        assert not nx.is_connected(check)
        if deleted in deletion_sets:
            raise AssertionError("repeated violated six-deletion")
        deletion_sets.add(deleted)
        clauses_added += enforce_connected_after(deleted)


if __name__ == "__main__":
    main()
