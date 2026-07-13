"""Enumerate the equality case in the K3 disjoint-union K4 neighbourhood cell.

This is a discovery/sanity-check script, not part of a proof.  In the equality
case |C|=6 left by the rooted K^*_{4,2} density bound, C has nine edges,
each A-root has four neighbours in C, each B-root has three, and every
vertex of C has total degree seven in C union N.

The script searches for two disjoint B-dominating sets in C and distinct A
attachments such that each set becomes connected after its A vertex is
adjoined.  The resulting two helper bags complete the four singleton B bags
to an N-meeting K6.
"""

from __future__ import annotations

from collections import defaultdict
from itertools import combinations, combinations_with_replacement

import networkx as nx
import z3


VERTICES = tuple(range(6))
FOUR_SETS = tuple(frozenset(s) for s in combinations(VERTICES, 4))
THREE_SETS = tuple(frozenset(s) for s in combinations(VERTICES, 3))


def column_sums(rows: tuple[frozenset[int], ...]) -> tuple[int, ...]:
    return tuple(sum(v in row for row in rows) for v in VERTICES)


def connected_masks(graph: nx.Graph) -> list[frozenset[int]]:
    ans: list[frozenset[int]] = []
    for size in range(1, 7):
        for vertices in combinations(VERTICES, size):
            subset = frozenset(vertices)
            if nx.is_connected(graph.subgraph(subset)):
                ans.append(subset)
    return ans


def has_two_helpers(
    components_by_subset: dict[frozenset[int], tuple[frozenset[int], ...]],
    a_rows: tuple[frozenset[int], ...],
    b_rows: tuple[frozenset[int], ...],
) -> bool:
    candidates: list[tuple[frozenset[int], set[int]]] = []
    for size in range(1, 7):
        for vertices in combinations(VERTICES, size):
            subset = frozenset(vertices)
            if not all(subset & neighbourhood for neighbourhood in b_rows):
                continue
            possible_roots = set()
            for a_index, a_neighbourhood in enumerate(a_rows):
                if all(
                    component & a_neighbourhood
                    for component in components_by_subset[subset]
                ):
                    possible_roots.add(a_index)
            if possible_roots:
                candidates.append((subset, possible_roots))

    for i, (first, first_roots) in enumerate(candidates):
        for second, second_roots in candidates[i + 1 :]:
            if first & second:
                continue
            if any(x != y for x in first_roots for y in second_roots):
                return True
    return False


def build_host(
    graph: nx.Graph,
    a_rows: tuple[frozenset[int], ...],
    b_rows: tuple[frozenset[int], ...],
) -> tuple[nx.Graph, tuple[str, ...]]:
    a = tuple(f"a{i}" for i in range(3))
    b = tuple(f"b{i}" for i in range(4))
    c = tuple(f"c{i}" for i in range(6))
    host = nx.Graph()
    host.add_nodes_from(a + b + c)
    host.add_edges_from(combinations(a, 2))
    host.add_edges_from(combinations(b, 2))
    host.add_edges_from((c[x], c[y]) for x, y in graph.edges())
    for i, row in enumerate(a_rows):
        host.add_edges_from((a[i], c[x]) for x in row)
    for i, row in enumerate(b_rows):
        host.add_edges_from((b[i], c[x]) for x in row)
    return host, a + b


def find_n_meeting_k6(
    graph: nx.Graph,
    a_rows: tuple[frozenset[int], ...],
    b_rows: tuple[frozenset[int], ...],
) -> list[list[str]] | None:
    """Find six clique bags in H, each rooted in N, using an SMT model."""

    host, boundary = build_host(graph, a_rows, b_rows)
    vertices = tuple(host)
    edges = tuple(host.edges())
    order = len(vertices)

    root_schemes = [
        tuple((v,) for v in chosen)
        for chosen in combinations(boundary, 6)
    ]
    for repeated_pair in combinations(boundary, 2):
        remaining = tuple(v for v in boundary if v not in repeated_pair)
        root_schemes.append((repeated_pair,) + tuple((v,) for v in remaining))

    for roots in root_schemes:
        solver = z3.Solver()
        belongs = {
            (v, i): z3.Bool(f"x_{v}_{i}")
            for v in vertices
            for i in range(6)
        }
        depth = {
            (v, i): z3.Int(f"d_{v}_{i}")
            for v in vertices
            for i in range(6)
        }

        for v in vertices:
            solver.add(z3.PbLe([(belongs[v, i], 1) for i in range(6)], 1))

        for i, root_set in enumerate(roots):
            primary = root_set[0]
            for root in root_set:
                solver.add(belongs[root, i])
            for j, other_roots in enumerate(roots):
                if i != j:
                    for root in other_roots:
                        solver.add(z3.Not(belongs[root, i]))
            solver.add(depth[primary, i] == 0)
            for v in vertices:
                if v == primary:
                    continue
                predecessors = [
                    z3.And(belongs[w, i], depth[w, i] < depth[v, i])
                    for w in host.neighbors(v)
                ]
                solver.add(
                    z3.Implies(
                        belongs[v, i],
                        z3.And(
                            depth[v, i] >= 1,
                            depth[v, i] < order,
                            z3.Or(*predecessors),
                        ),
                    )
                )

        for i in range(6):
            for j in range(i):
                contacts = []
                for x, y in edges:
                    contacts.append(z3.And(belongs[x, i], belongs[y, j]))
                    contacts.append(z3.And(belongs[y, i], belongs[x, j]))
                solver.add(z3.Or(*contacts))

        if solver.check() == z3.sat:
            model = solver.model()
            return [
                [v for v in vertices if z3.is_true(model.eval(belongs[v, i]))]
                for i in range(6)
            ]
    return None


def main() -> None:
    b_by_sums: dict[tuple[int, ...], list[tuple[frozenset[int], ...]]] = defaultdict(list)
    for indices in combinations_with_replacement(range(len(THREE_SETS)), 4):
        rows = tuple(THREE_SETS[i] for i in indices)
        b_by_sums[column_sums(rows)].append(rows)

    c_graphs = []
    for graph in nx.graph_atlas_g():
        if len(graph) == 6 and graph.number_of_edges() == 9 and nx.is_connected(graph):
            c_graphs.append(nx.convert_node_labels_to_integers(graph))

    tested = 0
    helper_failures = 0
    model_failures = []
    for graph in c_graphs:
        components_by_subset: dict[
            frozenset[int], tuple[frozenset[int], ...]
        ] = {}
        for size in range(1, 7):
            for vertices in combinations(VERTICES, size):
                subset = frozenset(vertices)
                components_by_subset[subset] = tuple(
                    frozenset(component)
                    for component in nx.connected_components(graph.subgraph(subset))
                )
        target = tuple(7 - graph.degree(v) for v in VERTICES)
        for indices in combinations_with_replacement(range(len(FOUR_SETS)), 3):
            a_rows = tuple(FOUR_SETS[i] for i in indices)
            a_sums = column_sums(a_rows)
            residual = tuple(target[v] - a_sums[v] for v in VERTICES)
            if min(residual) < 0:
                continue
            for b_rows in b_by_sums.get(residual, ()):
                tested += 1
                if not has_two_helpers(components_by_subset, a_rows, b_rows):
                    helper_failures += 1
                    model = find_n_meeting_k6(graph, a_rows, b_rows)
                    if model is None:
                        model_failures.append(
                            {
                                "C_graph6": nx.to_graph6_bytes(graph, header=False)
                                .decode()
                                .strip(),
                                "A": [sorted(row) for row in a_rows],
                                "B": [sorted(row) for row in b_rows],
                                "target": target,
                            }
                        )
                        print("MODEL FAILURE", model_failures[-1])
                        return

    print(
        {
            "unlabelled_C_graphs": len(c_graphs),
            "incidence_systems": tested,
            "two_helper_failures": helper_failures,
            "N_meeting_K6_failures": 0,
        }
    )


if __name__ == "__main__":
    main()
