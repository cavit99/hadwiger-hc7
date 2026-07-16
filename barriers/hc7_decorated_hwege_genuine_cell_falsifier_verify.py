#!/usr/bin/env python3
"""Exact falsifier for the decorated three-model genuine-cell decoder.

The graph has three disjoint marked K5s covering its vertex set.  It has
weighted separator order seven, but no K7 minor.  Since every vertex is a
terminal, every Mader cell has ``Y_j = X_j``; there is no genuine cell.

Two independent SMT encodings certify the absence of a K7 minor:

* a rooted decreasing-depth encoding of connected branch sets; and
* a Floyd--Warshall reachability encoding inside each branch set.

The script also verifies all weighted separators and the sharp ordinary
five-cuts.  Finally, it checks that every minimum two-edge augmentation
which repairs all seven five-cuts already creates a literal K7 model.
"""

from __future__ import annotations

from itertools import combinations

from z3 import And, Bool, BoolVal, If, Implies, Int, Not, Or, PbEq, PbLe, Solver, Sum, is_true, sat, unsat


N = 15
MARKS = frozenset({12, 13, 14})
CLIQUES = (
    frozenset({2, 6, 7, 8, 12}),
    frozenset({0, 3, 4, 9, 13}),
    frozenset({1, 5, 10, 11, 14}),
)

EDGES = frozenset(
    {
        (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 9), (0, 10), (0, 13),
        (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 10), (1, 11), (1, 14),
        (2, 3), (2, 5), (2, 6), (2, 7), (2, 8), (2, 12),
        (3, 4), (3, 9), (3, 13),
        (4, 9), (4, 13), (4, 14),
        (5, 6), (5, 7), (5, 10), (5, 11), (5, 14),
        (6, 7), (6, 8), (6, 12),
        (7, 8), (7, 12), (7, 14),
        (8, 12), (8, 14),
        (9, 13), (9, 14),
        (10, 11), (10, 13), (10, 14),
        (11, 12), (11, 14),
        (12, 13),
    }
)


def adjacency(edges: frozenset[tuple[int, int]]) -> tuple[tuple[int, ...], ...]:
    rows = [[] for _ in range(N)]
    for left, right in edges:
        rows[left].append(right)
        rows[right].append(left)
    return tuple(tuple(row) for row in rows)


def components_after_deletion(
    edges: frozenset[tuple[int, int]], deleted: frozenset[int]
) -> tuple[frozenset[int], ...]:
    rows = adjacency(edges)
    unseen = set(range(N)) - set(deleted)
    answer = []
    while unseen:
        root = unseen.pop()
        component = {root}
        stack = [root]
        while stack:
            vertex = stack.pop()
            for neighbour in rows[vertex]:
                if neighbour in unseen:
                    unseen.remove(neighbour)
                    component.add(neighbour)
                    stack.append(neighbour)
        answer.append(frozenset(component))
    return tuple(answer)


def exact_separators() -> tuple[int, tuple[frozenset[int], ...], tuple[frozenset[int], ...]]:
    separators = []
    for order in range(N - 1):
        for raw in combinations(range(N), order):
            deleted = frozenset(raw)
            if len(components_after_deletion(EDGES, deleted)) > 1:
                separators.append(deleted)

    minimum_weight = min(len(item) + len(item & MARKS) for item in separators)
    weighted_minima = tuple(
        item
        for item in separators
        if len(item) + len(item & MARKS) == minimum_weight
    )
    ordinary_order = min(map(len, separators))
    ordinary_minima = tuple(item for item in separators if len(item) == ordinary_order)
    return minimum_weight, weighted_minima, ordinary_minima


def validate_model(edges: frozenset[tuple[int, int]], bags: tuple[tuple[int, ...], ...]) -> None:
    assert len(bags) == 7 and all(bags)
    assert len(set().union(*map(set, bags))) == sum(map(len, bags))
    rows = adjacency(edges)
    for bag in bags:
        target = set(bag)
        reached = {bag[0]}
        stack = [bag[0]]
        while stack:
            vertex = stack.pop()
            for neighbour in rows[vertex]:
                if neighbour in target - reached:
                    reached.add(neighbour)
                    stack.append(neighbour)
        assert reached == target
    for left, right in combinations(bags, 2):
        assert any(tuple(sorted((u, v))) in edges for u in left for v in right)


def depth_minor_model(
    edges: frozenset[tuple[int, int]], prefix: str
) -> tuple[tuple[int, ...], ...] | None:
    """Exact K7-minor oracle using decreasing depths to a unique root."""

    rows = adjacency(edges)
    solver = Solver()
    assigned = [[Bool(f"{prefix}_x_{v}_{b}") for b in range(7)] for v in range(N)]
    root = [[Bool(f"{prefix}_r_{v}_{b}") for b in range(7)] for v in range(N)]
    depth = [[Int(f"{prefix}_d_{v}_{b}") for b in range(7)] for v in range(N)]

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

    result = solver.check()
    if result == unsat:
        return None
    assert result == sat
    model = solver.model()
    answer = tuple(
        tuple(vertex for vertex in range(N) if is_true(model[assigned[vertex][bag]]))
        for bag in range(7)
    )
    validate_model(edges, answer)
    return answer


def warshall_has_k7(edges: frozenset[tuple[int, int]]) -> bool:
    """Independent exact oracle using in-bag Floyd--Warshall reachability."""

    solver = Solver()
    assigned = [[Bool(f"fw_x_{v}_{b}") for b in range(7)] for v in range(N)]
    for vertex in range(N):
        solver.add(PbLe([(assigned[vertex][bag], 1) for bag in range(7)], 1))
    for bag in range(7):
        solver.add(Or([assigned[vertex][bag] for vertex in range(N)]))

    minima = []
    for bag in range(7):
        minimum = Int(f"fw_min_{bag}")
        minima.append(minimum)
        solver.add(
            Or(
                [
                    And(
                        minimum == vertex,
                        assigned[vertex][bag],
                        *[Not(assigned[earlier][bag]) for earlier in range(vertex)],
                    )
                    for vertex in range(N)
                ]
            )
        )
    for bag in range(6):
        solver.add(minima[bag] < minima[bag + 1])

    for first, second in combinations(range(7), 2):
        solver.add(
            Or(
                [And(assigned[u][first], assigned[v][second]) for u, v in edges]
                + [And(assigned[v][first], assigned[u][second]) for u, v in edges]
            )
        )

    for bag in range(7):
        previous = [
            [
                And(
                    BoolVal(u == v or tuple(sorted((u, v))) in edges),
                    assigned[u][bag],
                    assigned[v][bag],
                )
                for v in range(N)
            ]
            for u in range(N)
        ]
        for middle in range(N):
            current = [
                [Bool(f"fw_r_{bag}_{middle}_{u}_{v}") for v in range(N)]
                for u in range(N)
            ]
            for u in range(N):
                for v in range(N):
                    solver.add(
                        current[u][v]
                        == Or(
                            previous[u][v],
                            And(
                                previous[u][middle],
                                previous[middle][v],
                                assigned[middle][bag],
                            ),
                        )
                    )
            previous = current
        for u in range(N):
            for v in range(N):
                solver.add(
                    Implies(And(assigned[u][bag], assigned[v][bag]), previous[u][v])
                )

    return solver.check() == sat


def minimum_augmentations(
    ordinary_minima: tuple[frozenset[int], ...]
) -> tuple[tuple[tuple[int, int], tuple[int, int]], ...]:
    all_edges = set(combinations(range(N), 2))
    missing = tuple(sorted(all_edges - set(EDGES)))
    crossing_sets = []
    for separator in ordinary_minima:
        components = components_after_deletion(EDGES, separator)
        assert len(components) == 2
        left, right = components
        crossing_sets.append(
            frozenset(
                edge
                for edge in missing
                if (edge[0] in left and edge[1] in right)
                or (edge[1] in left and edge[0] in right)
            )
        )

    assert not any(all(edge in crossing for crossing in crossing_sets) for edge in missing)
    pairs = tuple(
        pair
        for pair in combinations(missing, 2)
        if all(any(edge in crossing for edge in pair) for crossing in crossing_sets)
    )
    assert len(pairs) == 20
    for index, pair in enumerate(pairs):
        model = depth_minor_model(frozenset(set(EDGES) | set(pair)), f"aug_{index}")
        assert model is not None
    return pairs


def main() -> None:
    assert len(EDGES) == 49
    assert set().union(*map(set, CLIQUES)) == set(range(N))
    assert sum(map(len, CLIQUES)) == N
    assert {12, 13, 14} == {next(iter(clique & MARKS)) for clique in CLIQUES}
    for clique in CLIQUES:
        assert all(tuple(sorted(edge)) in EDGES for edge in combinations(clique, 2))

    minimum_weight, weighted_minima, ordinary_minima = exact_separators()
    assert minimum_weight == 7
    assert len(weighted_minima) == 11
    assert len(ordinary_minima) == 7
    assert all(len(separator) == 5 and len(separator & MARKS) == 2 for separator in ordinary_minima)

    assert depth_minor_model(EDGES, "host") is None
    assert not warshall_has_k7(EDGES)
    pairs = minimum_augmentations(ordinary_minima)

    print("vertices", N)
    print("edges", len(EDGES))
    print("weighted_separator_order", minimum_weight)
    print("weighted_minima", tuple(tuple(sorted(item)) for item in weighted_minima))
    print("ordinary_connectivity", 5)
    print("ordinary_five_cuts", tuple(tuple(sorted(item)) for item in ordinary_minima))
    print("depth_K7", False)
    print("warshall_K7", False)
    print("minimum_two_edge_connectivity_augmentations", len(pairs))
    print("all_minimum_augmentations_have_K7", True)
    print("all_vertices_are_named_terminals", True)
    print("genuine_Mader_cell_possible", False)


if __name__ == "__main__":
    main()
