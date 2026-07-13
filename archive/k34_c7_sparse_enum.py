"""Enumerate the degree-feasible boundary rows in the two sparse n=7 cells.

This starts a direct, atlas-based certificate independent of the Z3 probe.
At present it reports the exact number of C/A states and compatible B-row
systems surviving the degree equations.  Helper, Dirac-neighbourhood, and
seven-connectivity filters are added below as the certificate is refined.
"""

from collections import Counter, defaultdict
from itertools import combinations, combinations_with_replacement

import networkx as nx


N = 7
V = tuple(range(N))
ROWS3 = tuple(sum(1 << x for x in row) for row in combinations(V, 3))
ROWS4 = tuple(sum(1 << x for x in row) for row in combinations(V, 4))
ROWS5 = tuple(sum(1 << x for x in row) for row in combinations(V, 5))


def column_degrees(rows: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(sum(row >> x & 1 for row in rows) for x in V)


def b_systems() -> tuple[dict[tuple[int, ...], list[tuple[int, ...]]], dict[tuple[int, ...], list[tuple[int, ...]]]]:
    total12: dict[tuple[int, ...], list[tuple[int, ...]]] = defaultdict(list)
    for rows in combinations_with_replacement(ROWS3, 4):
        total12[column_degrees(rows)].append(rows)

    total13: dict[tuple[int, ...], list[tuple[int, ...]]] = defaultdict(list)
    for row4 in ROWS4:
        for rows3 in combinations_with_replacement(ROWS3, 3):
            rows = tuple(sorted((row4,) + rows3))
            total13[column_degrees(rows)].append(rows)
    return total12, total13


def degree_targets(lower: tuple[int, ...], total: int):
    extra = total - sum(lower)
    if extra < 0:
        return

    def extend(index: int, remaining: int, values: list[int]):
        if index == N:
            if remaining == 0:
                yield tuple(values)
            return
        for add in range(min(4 - lower[index], remaining) + 1):
            values.append(lower[index] + add)
            yield from extend(index + 1, remaining - add, values)
            values.pop()

    yield from extend(0, extra, [])


def c_graphs(edge_count: int):
    for graph in nx.graph_atlas_g():
        if len(graph) == N and graph.number_of_edges() == edge_count and nx.is_connected(graph):
            yield nx.convert_node_labels_to_integers(graph)


def scan_case(
    edge_count: int,
    a_systems: tuple[tuple[int, ...], ...],
    b_total: int,
    b_by_columns: dict[tuple[int, ...], list[tuple[int, ...]]],
) -> Counter[str]:
    counts: Counter[str] = Counter()
    for graph in c_graphs(edge_count):
        counts["C_graphs"] += 1
        c_degree = tuple(graph.degree(x) for x in V)
        for a_rows in a_systems:
            counts["C_A_states"] += 1
            a_degree = column_degrees(a_rows)
            lower = tuple(max(0, 7 - c_degree[x] - a_degree[x]) for x in V)
            candidates = []
            for target in degree_targets(lower, b_total):
                candidates.extend(b_by_columns.get(target, ()))
            if not candidates:
                continue
            counts["degree_feasible_C_A"] += 1
            counts["degree_feasible_incidence_systems"] += len(candidates)
    return counts


def main() -> None:
    b12, b13 = b_systems()
    a12 = tuple(combinations_with_replacement(ROWS4, 3))
    a13 = tuple(
        tuple(sorted((row5,) + rows4))
        for row5 in ROWS5
        for rows4 in combinations_with_replacement(ROWS4, 2)
    )
    print("B column types", len(b12), len(b13))
    print("A systems", len(a12), len(a13))
    print("(p,q)=(24,13)", dict(scan_case(13, a12, 12, b12)))
    case25a = scan_case(12, a13, 12, b12)
    case25b = scan_case(12, a12, 13, b13)
    print("(p,q)=(25,12), extra A", dict(case25a))
    print("(p,q)=(25,12), extra B", dict(case25b))


if __name__ == "__main__":
    main()
