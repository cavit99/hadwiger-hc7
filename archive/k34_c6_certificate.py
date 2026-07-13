"""Independent standard-library checker for hadwiger_k34_c6_human.md.

This checks the two finite tables in that note.  It deliberately uses neither
NetworkX nor Z3.  The mathematical reduction and the exceptional-case argument
are in the note; this file only makes the finite classification reproducible.
"""

from collections import Counter
from itertools import combinations, combinations_with_replacement, permutations


V = frozenset(range(6))
PAIRS = tuple(combinations(range(6), 2))
PARTS = tuple(
    (frozenset((0, *tail)), V - frozenset((0, *tail)))
    for tail in combinations(range(1, 6), 2)
)

EDGE_ROWS = (
    "01 02 03 12 13 15 23 24 25",
    "01 02 03 04 12 13 15 23 25",
    "01 03 04 12 14 23 24 34 45",
    "02 12 13 14 23 25 34 35 45",
    "01 02 03 12 13 15 23 25 45",
    "04 05 14 15 24 25 34 35 45",
    "01 02 03 04 05 12 23 25 34",
    "01 02 04 05 12 13 14 34 45",
    "01 02 05 12 13 14 15 34 45",
    "01 02 03 04 05 12 13 23 45",
    "01 03 04 05 12 15 23 34 35",
    "02 03 04 05 12 13 23 34 45",
    "02 03 05 12 13 23 24 34 45",
    "01 02 04 05 12 15 23 25 34",
    "02 04 05 14 15 24 25 34 35",
    "01 04 05 12 23 25 34 35 45",
    "01 03 04 05 12 15 23 25 34",
    "01 03 05 12 23 24 25 34 45",
    "01 02 03 14 15 23 25 34 45",
    "01 03 05 12 14 23 25 34 45",
)

EXPECTED_AUT = (2, 2, 8, 2, 4, 48, 2, 6, 2, 12, 1, 2, 4, 4, 8, 2, 2, 2, 12, 72)
EXPECTED_C = (3, 3, 4, 3, 2, 6, 4, 3, 3, 1, 5, 3, 5, 4, 6, 5, 4, 6, 7, 9)

EXPECTED_DISTRIBUTIONS = {
    1: {7: 8, 8: 30, 9: 156, 10: 147},
    2: {7: 2, 8: 46, 9: 152, 10: 265},
    3: {7: 4, 8: 6, 9: 238, 10: 107},
    4: {7: 6, 8: 25, 9: 226, 10: 238},
    5: {6: 2, 8: 24, 9: 110, 10: 359},
    7: {7: 12, 8: 70, 9: 171, 10: 162},
    8: {7: 9, 8: 90, 9: 163, 10: 316},
    9: {8: 24, 9: 187, 10: 219},
    10: {9: 99, 10: 331},
    12: {6: 2, 8: 34, 9: 144, 10: 431},
    14: {4: 1, 6: 2, 7: 4, 8: 33, 9: 140, 10: 431},
    17: {6: 3, 7: 2, 8: 38, 9: 183, 10: 419},
}


def parse(row: str) -> frozenset[tuple[int, int]]:
    return frozenset((int(token[0]), int(token[1])) for token in row.split())


def induced_edge_count(edges: frozenset[tuple[int, int]], side: frozenset[int]) -> int:
    return sum(u in side and v in side for u, v in edges)


def root_set(
    edges: frozenset[tuple[int, int]],
    side: frozenset[int],
    missing: tuple[tuple[int, int], ...],
) -> frozenset[int]:
    inside = tuple((u, v) for u, v in edges if u in side and v in side)
    if len(inside) >= 2:
        return frozenset(range(3))
    if len(inside) == 1:
        edge = frozenset(inside[0])
        isolated = next(iter(side - edge))
        return frozenset(
            i
            for i, pair in enumerate(missing)
            if isolated not in pair and frozenset(pair) != edge
        )
    other = V - side
    return frozenset(
        i for i, pair in enumerate(missing) if frozenset(pair) <= other
    )


def compatible_count(edges: frozenset[tuple[int, int]], missing: tuple[tuple[int, int], ...]) -> int:
    total = 0
    for left, right in PARTS:
        left_roots = root_set(edges, left, missing)
        right_roots = root_set(edges, right, missing)
        total += bool(left_roots and right_roots and len(left_roots | right_roots) >= 2)
    return total


def main() -> None:
    graphs = tuple(parse(row) for row in EDGE_ROWS)
    orbit_sum = 0
    invariants = []
    exceptional = []

    for number, edges in enumerate(graphs, 1):
        degree = tuple(sum(v in edge for edge in edges) for v in range(6))
        degree_sequence = tuple(sorted(degree))
        aut = sum(
            frozenset(tuple(sorted((p[u], p[v]))) for u, v in edges) == edges
            for p in permutations(range(6))
        )
        connected_partitions = sum(
            induced_edge_count(edges, left) >= 2
            and induced_edge_count(edges, right) >= 2
            for left, right in PARTS
        )
        assert aut == EXPECTED_AUT[number - 1]
        assert connected_partitions == EXPECTED_C[number - 1]
        orbit_sum += 720 // aut
        invariants.append((degree_sequence, connected_partitions, aut))

        if connected_partitions >= 5:
            continue

        distribution = Counter()
        for indices in combinations_with_replacement(range(15), 3):
            missing = tuple(PAIRS[i] for i in indices)
            missing_degree = tuple(sum(v in pair for pair in missing) for v in range(6))
            if any(
                not (degree[v] - 4 <= missing_degree[v] <= degree[v])
                for v in range(6)
            ):
                continue
            q = compatible_count(edges, missing)
            distribution[q] += 1
            if q < 5:
                exceptional.append((number, missing, q))
        assert dict(distribution) == EXPECTED_DISTRIBUTIONS[number]

    assert len(set(invariants)) == 20
    assert orbit_sum == 4945
    assert exceptional == [(14, ((1, 5), (3, 4), (3, 4)), 4)]
    print("certificate verified: 20 graph orbits, 4945 labelled graphs")
    print("unique low-compatible state:", exceptional[0])


if __name__ == "__main__":
    main()
