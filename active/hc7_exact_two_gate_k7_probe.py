#!/usr/bin/env python3
"""Exact probes for the four-gate residue in the exact-two-row branch.

The underlying twelve-vertex graph is the audited example in
``hc7_five_colour_exact_two_row_linkage.md``.  Four more vertices are the
two deleted matching rows.  This script enumerates the smallest row-support
attachments and uses an exact SMT branch-set encoding for ``K_7`` minors.

No positive output is a theorem about contraction-critical graphs: the
point is to determine which additional exact-two hypotheses genuinely remove
the four-gate obstruction.
"""

from __future__ import annotations

from itertools import combinations, product

from z3 import And, Bool, If, Implies, Int, Not, Or, PbEq, PbLe, Solver, Sum, is_true, sat


QE = (0, 1, 2, 3)
QF = (4, 5, 6, 7)
Z = (8, 9, 10, 11)
A = (12, 13)
B = (14, 15)
N = 16

COLOUR = {
    0: 1,
    1: 2,
    2: 3,
    3: 4,
    4: 0,
    5: 2,
    6: 3,
    7: 4,
    8: 0,
    9: 1,
    10: 2,
    11: 3,
    12: 0,
    13: 0,
    14: 1,
    15: 1,
}


def edge(left: int, right: int) -> tuple[int, int]:
    return (left, right) if left < right else (right, left)


def base_edges() -> set[tuple[int, int]]:
    answer = set(combinations(QE, 2)) | set(combinations(QF, 2))
    for gate in Z:
        for core in QE + QF:
            if COLOUR[gate] != COLOUR[core]:
                answer.add(edge(gate, core))
    answer.add(edge(10, 11))
    answer.update(combinations(A + B, 2))
    return answer


def support_graph(
    qe_choices: tuple[int, ...],
    qf_choices: tuple[int, ...],
    common_choices_a: tuple[int, int],
    common_choices_b: tuple[int, int],
) -> frozenset[tuple[int, int]]:
    """Add exactly one required row edge at each named support contact.

    ``qe_choices`` and ``qf_choices`` select one endpoint of the appropriate
    row for every core vertex.  ``common_choices_*`` select one endpoint of
    each row for each of the colour-2 and colour-3 gate vertices.
    """

    answer = base_edges()
    answer.update(edge(core, A[choice]) for core, choice in zip(QE, qe_choices))
    answer.update(edge(core, B[choice]) for core, choice in zip(QF, qf_choices))
    for gate, choice in zip((10, 11), common_choices_a):
        answer.add(edge(gate, A[choice]))
    for gate, choice in zip((10, 11), common_choices_b):
        answer.add(edge(gate, B[choice]))
    return frozenset(answer)


def adjacency(edges: frozenset[tuple[int, int]]) -> tuple[tuple[int, ...], ...]:
    rows = [[] for _ in range(N)]
    for left, right in edges:
        rows[left].append(right)
        rows[right].append(left)
    return tuple(tuple(row) for row in rows)


def validate_model(edges: frozenset[tuple[int, int]], bags: tuple[tuple[int, ...], ...]) -> None:
    rows = adjacency(edges)
    assert len(bags) == 7 and all(bags)
    assert sum(map(len, bags)) == len(set().union(*map(set, bags)))
    for bag in bags:
        reached = {bag[0]}
        stack = [bag[0]]
        while stack:
            vertex = stack.pop()
            for neighbour in rows[vertex]:
                if neighbour in bag and neighbour not in reached:
                    reached.add(neighbour)
                    stack.append(neighbour)
        assert reached == set(bag)
    for first, second in combinations(bags, 2):
        assert any(edge(u, v) in edges for u in first for v in second)


def k7_model(edges: frozenset[tuple[int, int]]) -> tuple[tuple[int, ...], ...] | None:
    """Return an exact ``K_7`` model or certify that none exists."""

    rows = adjacency(edges)
    solver = Solver()
    assigned = [[Bool(f"x_{v}_{bag}") for bag in range(7)] for v in range(N)]
    root = [[Bool(f"r_{v}_{bag}") for bag in range(7)] for v in range(N)]
    depth = [[Int(f"d_{v}_{bag}") for bag in range(7)] for v in range(N)]

    for vertex in range(N):
        solver.add(PbLe([(assigned[vertex][bag], 1) for bag in range(7)], 1))
    root_names = []
    for bag in range(7):
        solver.add(PbEq([(root[vertex][bag], 1) for vertex in range(N)], 1))
        for vertex in range(N):
            solver.add(
                Implies(root[vertex][bag], And(assigned[vertex][bag], depth[vertex][bag] == 0))
            )
            solver.add(
                Implies(assigned[vertex][bag], And(depth[vertex][bag] >= 0, depth[vertex][bag] < N))
            )
            solver.add(
                Implies(
                    And(assigned[vertex][bag], Not(root[vertex][bag])),
                    Or(
                        [
                            And(assigned[other][bag], depth[other][bag] < depth[vertex][bag])
                            for other in rows[vertex]
                        ]
                    ),
                )
            )
        root_names.append(Sum([If(root[vertex][bag], vertex, 0) for vertex in range(N)]))
    for bag in range(6):
        solver.add(root_names[bag] < root_names[bag + 1])
    for first, second in combinations(range(7), 2):
        solver.add(
            Or(
                [And(assigned[u][first], assigned[v][second]) for u, v in edges]
                + [And(assigned[v][first], assigned[u][second]) for u, v in edges]
            )
        )

    if solver.check() != sat:
        return None
    model = solver.model()
    answer = tuple(
        tuple(vertex for vertex in range(N) if is_true(model[assigned[vertex][bag]]))
        for bag in range(7)
    )
    validate_model(edges, answer)
    return answer


def induced_pair_connected(
    edges: frozenset[tuple[int, int]], vertices: frozenset[int], ends: tuple[int, int]
) -> bool:
    # Kempe connectivity is tested in K=G-{aa',bb'}, not in G.
    kempe_edges = frozenset(set(edges) - {edge(*A), edge(*B)})
    rows = adjacency(kempe_edges)
    reached = {ends[0]}
    stack = [ends[0]]
    while stack:
        vertex = stack.pop()
        for neighbour in rows[vertex]:
            if neighbour in vertices and neighbour not in reached:
                reached.add(neighbour)
                stack.append(neighbour)
    return ends[1] in reached


def has_two_locks(edges: frozenset[tuple[int, int]]) -> bool:
    for beta in (2, 3):
        allowed_a = frozenset(v for v in range(N) if COLOUR[v] in (0, beta))
        allowed_b = frozenset(v for v in range(N) if COLOUR[v] in (1, beta))
        if not induced_pair_connected(edges, allowed_a, A) or not induced_pair_connected(
            edges, allowed_b, B
        ):
            return False
    return True


def uniform_gate_model() -> tuple[tuple[int, ...], ...]:
    """The same literal model works for every minimal support assignment."""

    return (
        (0,),
        (1,),
        (2, 12, 13),
        (3,),
        (5, 11),
        (6, 8, 14, 15),
        (7, 9, 10),
    )


def enumerate_minimal_supports() -> None:
    total = locked = 0
    model = uniform_gate_model()
    for choices in product(product((0, 1), repeat=4), repeat=2):
        qe_choices, qf_choices = choices
        for common_a in product((0, 1), repeat=2):
            for common_b in product((0, 1), repeat=2):
                total += 1
                edges = support_graph(qe_choices, qf_choices, common_a, common_b)
                locked += has_two_locks(edges)
                validate_model(edges, model)
    print("minimal_support_graphs", total)
    print("two_lock_graphs", locked)
    print("graphs_with_literal_uniform_K7", total)
    print("uniform_K7_model", model)

    # One independent exact-SMT replay guards against an error in the fixed
    # model checker or in the intended graph reconstruction.
    sample = support_graph((0, 1, 0, 1), (1, 0, 1, 0), (0, 1), (1, 0))
    exact = k7_model(sample)
    assert exact is not None
    print("independent_exact_sample_K7", exact)


if __name__ == "__main__":
    enumerate_minimal_supports()
