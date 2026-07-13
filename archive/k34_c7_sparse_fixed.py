"""Per-C discovery search for sparse |C|=7 actual-helper obstructions.

For each unlabelled connected seven-vertex C with 12 or 13 edges, fix C and
ask whether A/B incidences can satisfy:

* (p,q)=(25,12) or (24,13), hence every C vertex has degree >= 7;
* all 127 necessary kappa(G)>=7 boundary inequalities for X subset C;
* alpha(G[N(c)])<=2 whenever d_G(c)=7 (Dirac neighbourhood condition);
* no two valid Lemma 1.1 bags, allowing one bag to use two A vertices.

This is a discovery program, not a proof artifact.
"""

import hashlib
from itertools import combinations

import networkx as nx
import z3


N = 7
V = tuple(range(N))
FULL = (1 << N) - 1
SUBSETS = tuple(range(1, 1 << N))
EXPECTED_GRAPH_ID_DIGEST = "e9cc59585d83825c03de308caa6f775350e548e18e89342acadefbee03caf760"
EXPECTED_STATUS_DIGEST = "ff15c316a703c69235124ce7431d8e01914c05881c04fb6dbd5be0f8aa562e42"
EXPECTED_LABELLED_COUNTS = {12: 290_745, 13: 202_755}


def members(mask: int) -> tuple[int, ...]:
    return tuple(x for x in V if mask >> x & 1)


def solve_graph(
    graph: nx.Graph,
    timeout_ms: int = 20_000,
    *,
    enforce_sparse: bool = True,
    enforce_dirac: bool = True,
):
    q = graph.number_of_edges()
    if enforce_sparse:
        assert q in (12, 13)
    p = 49 - 2 * q if q == 12 else 50 - 2 * q
    # Explicitly: (p,q)=(25,12) or (24,13).

    solver = z3.Solver()
    solver.set(timeout=timeout_ms)
    a = {(i, x): z3.Bool(f"a_{i}_{x}") for i in range(3) for x in V}
    b = {(j, x): z3.Bool(f"b_{j}_{x}") for j in range(4) for x in V}

    for i in range(3):
        solver.add(z3.PbGe([(a[i, x], 1) for x in V], 4))
    for j in range(4):
        solver.add(z3.PbGe([(b[j, x], 1) for x in V], 3))
    if enforce_sparse:
        all_incidence = list(a.values()) + list(b.values())
        solver.add(z3.PbEq([(term, 1) for term in all_incidence], p))
    for x in V:
        boundary_degree = [(a[i, x], 1) for i in range(3)]
        boundary_degree += [(b[j, x], 1) for j in range(4)]
        solver.add(z3.PbGe(boundary_degree, 7 - graph.degree(x)))

    # Harmless row permutations.
    a_code = [z3.Sum([z3.If(a[i, x], 1 << x, 0) for x in V]) for i in range(3)]
    b_code = [z3.Sum([z3.If(b[j, x], 1 << x, 0) for x in V]) for j in range(4)]
    solver.add(a_code[0] <= a_code[1], a_code[1] <= a_code[2])
    solver.add(b_code[0] <= b_code[1], b_code[1] <= b_code[2], b_code[2] <= b_code[3])

    # Necessary kappa-seven inequalities: N_G(X) separates X from v.
    for mask in SUBSETS:
        side = set(members(mask))
        c_boundary = set().union(*(set(graph.neighbors(x)) for x in side)) - side
        indicators = [z3.Or([a[i, x] for x in side]) for i in range(3)]
        indicators += [z3.Or([b[j, x] for x in side]) for j in range(4)]
        solver.add(z3.PbGe([(term, 1) for term in indicators], 7 - len(c_boundary)))

    # Conditional Dirac neighbourhood condition at every degree-seven C vertex.
    typed = tuple(("a", i) for i in range(3)) + tuple(("b", j) for j in range(4)) + tuple(("c", y) for y in V)

    def xc(x, vertex):
        kind, index = vertex
        if kind == "a":
            return a[index, x]
        if kind == "b":
            return b[index, x]
        return index != x and graph.has_edge(index, x)

    def yz(first, second):
        (fk, fi), (sk, si) = first, second
        if fk == sk == "a" or fk == sk == "b":
            return True
        if {fk, sk} == {"a", "b"}:
            return False
        if fk == sk == "c":
            return graph.has_edge(fi, si)
        if fk == "c":
            fk, sk, fi, si = sk, fk, si, fi
        if fk == "a":
            return a[fi, si]
        return b[fi, si]

    if enforce_dirac:
        for x in V:
            need = 7 - graph.degree(x)
            incident = [(a[i, x], 1) for i in range(3)] + [(b[j, x], 1) for j in range(4)]
            degree_seven = z3.PbEq(incident, need)
            candidates = tuple(vertex for vertex in typed if xc(x, vertex) is not False)
            for triple in combinations(candidates, 3):
                antecedent = [xc(x, vertex) for vertex in triple]
                if False in antecedent:
                    continue
                internal = [yz(y, z) for y, z in combinations(triple, 2)]
                if True in internal:
                    continue
                solver.add(
                    z3.Implies(
                        z3.And(degree_seven, *antecedent),
                        z3.Or([term for term in internal if term is not False]),
                    )
                )

    # Components of every induced C[P] are fixed.  A root subset R connects P
    # exactly when each component has an A-neighbour in R.
    helper = {}
    for mask in SUBSETS:
        side = members(mask)
        components = tuple(
            frozenset(component)
            for component in nx.connected_components(graph.subgraph(side))
        )
        b_complete = z3.And([z3.Or([b[j, x] for x in side]) for j in range(4)])
        for roots in range(1, 1 << 3):
            connected = z3.And(
                [
                    z3.Or(
                        [a[i, x] for i in range(3) if roots >> i & 1 for x in component]
                    )
                    for component in components
                ]
            )
            helper[roots, mask] = z3.And(b_complete, connected)

    for left in SUBSETS:
        for right in SUBSETS:
            if left >= right or left & right:
                continue
            for left_roots in range(1, 1 << 3):
                for right_roots in range(1, 1 << 3):
                    if not left_roots & right_roots:
                        solver.add(z3.Not(z3.And(helper[left_roots, left], helper[right_roots, right])))

    status = solver.check()
    if status != z3.sat:
        return status, None
    model = solver.model()
    rows_a = [tuple(x for x in V if z3.is_true(model.eval(a[i, x]))) for i in range(3)]
    rows_b = [tuple(x for x in V if z3.is_true(model.eval(b[j, x]))) for j in range(4)]
    return status, (rows_a, rows_b)


def main() -> None:
    graphs = [
        nx.convert_node_labels_to_integers(graph)
        for graph in nx.graph_atlas_g()
        if len(graph) == 7 and nx.is_connected(graph) and graph.number_of_edges() in (12, 13)
    ]
    labelled_counts = {12: 0, 13: 0}
    for graph in graphs:
        automorphisms = sum(
            1
            for _ in nx.algorithms.isomorphism.GraphMatcher(
                graph, graph
            ).isomorphisms_iter()
        )
        labelled_counts[graph.number_of_edges()] += 5040 // automorphisms
    assert labelled_counts == EXPECTED_LABELLED_COUNTS
    print("graphs", len(graphs), flush=True)
    print("labelled orbit coverage", labelled_counts, flush=True)
    counts = {"sat": 0, "unsat": 0, "unknown": 0}
    records = []
    for index, graph in enumerate(graphs):
        status, model = solve_graph(graph)
        counts[str(status)] += 1
        code = nx.to_graph6_bytes(graph, header=False).decode().strip()
        records.append(f"{code}:{status}")
        print(index, graph.number_of_edges(), code, status, counts, flush=True)
        if status == z3.sat:
            print("edges", sorted(graph.edges()))
            print("A", model[0])
            print("B", model[1])
            break

    graph_codes = [record.rsplit(":", 1)[0] for record in records]
    graph_digest = hashlib.sha256(("\n".join(graph_codes) + "\n").encode()).hexdigest()
    status_digest = hashlib.sha256(("\n".join(records) + "\n").encode()).hexdigest()
    print("graph-id sha256", graph_digest)
    print("graph-id/status sha256", status_digest)
    print("final counts", counts)
    assert len(records) == 221
    assert counts == {"sat": 0, "unsat": 221, "unknown": 0}
    assert graph_digest == EXPECTED_GRAPH_ID_DIGEST
    assert status_digest == EXPECTED_STATUS_DIGEST
    print("all sparse fixed-C instances certified UNSAT")


if __name__ == "__main__":
    main()
