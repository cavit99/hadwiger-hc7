#!/usr/bin/env python3
"""Exact quotient audit for repeated roots at a two-shore equality gate.

The seven-edge layer has missing graph a triangle with four pendant
vertices when exactly three boundary vertices have missing degree at
least two.  A connected split of one shore is represented by adjacent
vertices x,y whose contact rows cover the boundary and share two of the
triangle vertices; h is the contracted opposite full shore.

The first audit classifies all negative ten-vertex quotients.  The
second audit asks, in the sole balanced pendant distribution, which
cyclic-hull crossings can still be placed in the opposite shore without
making the eleven-vertex quotient K7-positive.
"""

from __future__ import annotations

from functools import lru_cache
from itertools import combinations, permutations

import networkx as nx


S = tuple(range(7))
ALL_BOUNDARY = frozenset(S)


@lru_cache(maxsize=None)
def set_partitions(values: tuple[int, ...], blocks: int):
    if not values:
        return ((),) if blocks == 0 else ()
    first = values[0]
    out: list[tuple[tuple[int, ...], ...]] = []

    def rec(index: int, current: list[list[int]]) -> None:
        if index == len(values):
            if len(current) == blocks:
                out.append(tuple(tuple(block) for block in current))
            return
        value = values[index]
        for position in range(len(current)):
            current[position].append(value)
            rec(index + 1, current)
            current[position].pop()
        if len(current) < blocks:
            current.append([value])
            rec(index + 1, current)
            current.pop()

    rec(1, [[first]])
    return tuple(out)


@lru_cache(maxsize=None)
def candidate_models(order: int, target: int = 7) -> tuple[tuple[int, ...], ...]:
    answer: list[tuple[int, ...]] = []
    vertices = tuple(range(order))
    for support_order in range(target, order + 1):
        for support in combinations(vertices, support_order):
            for partition in set_partitions(tuple(support), target):
                answer.append(tuple(sum(1 << x for x in block) for block in partition))
    answer.sort(key=lambda bags: (-sum(mask.bit_count() for mask in bags), bags))
    return tuple(answer)


def k7_model(order: int, edges: set[tuple[int, int]]):
    adjacency = [0] * order
    for a, b in edges:
        adjacency[a] |= 1 << b
        adjacency[b] |= 1 << a

    neighbourhood = [0] * (1 << order)
    connected = [False] * (1 << order)
    for mask in range(1, 1 << order):
        bit = mask & -mask
        vertex = bit.bit_length() - 1
        neighbourhood[mask] = neighbourhood[mask ^ bit] | adjacency[vertex]
        reached = bit
        while True:
            expanded = reached | (neighbourhood[reached] & mask)
            if expanded == reached:
                break
            reached = expanded
        connected[mask] = reached == mask

    for bags in candidate_models(order):
        if not all(connected[bag] for bag in bags):
            continue
        if all(
            neighbourhood[bags[i]] & bags[j]
            for i in range(7)
            for j in range(i)
        ):
            return bags
    return None


def bits(mask: int) -> frozenset[int]:
    return frozenset(x for x in S if mask >> x & 1)


def missing_graph(distribution: tuple[int, int, int]) -> set[tuple[int, int]]:
    """Triangle 012 with pendant counts given by distribution."""
    answer = {(0, 1), (0, 2), (1, 2)}
    leaf = 3
    for hub, count in enumerate(distribution):
        for _ in range(count):
            answer.add(tuple(sorted((hub, leaf))))
            leaf += 1
    assert leaf == 7 and len(answer) == 7
    return answer


def split_quotient(
    missing: set[tuple[int, int]], row_x: frozenset[int], row_y: frozenset[int]
) -> set[tuple[int, int]]:
    x, y, helper = 7, 8, 9
    boundary = set(combinations(S, 2)) - missing
    answer = set(boundary)
    answer.add((x, y))
    answer.update((helper, s) for s in S)
    answer.update((x, s) for s in row_x)
    answer.update((y, s) for s in row_y)
    return {tuple(sorted(edge)) for edge in answer}


def covering_rows(common: tuple[int, int]):
    remaining = tuple(s for s in S if s not in common)
    for code in range(3 ** len(remaining)):
        value = code
        row_x = set(common)
        row_y = set(common)
        for s in remaining:
            choice = value % 3
            value //= 3
            if choice != 1:
                row_x.add(s)
            if choice != 0:
                row_y.add(s)
        yield frozenset(row_x), frozenset(row_y)


def maximal_rows(rows):
    return tuple(
        row
        for row in rows
        if not any(
            row != other and row[0] <= other[0] and row[1] <= other[1]
            for other in rows
        )
    )


def cyclic_hulls(missing: set[tuple[int, int]]):
    boundary = set(combinations(S, 2)) - missing
    answer = set()
    for length in range(4, 8):
        for core in combinations(S, length):
            omitted = set(S) - set(core)
            # Bipartiteness on at most three vertices: no triangle.
            if len(omitted) == 3 and set(combinations(omitted, 2)) <= boundary:
                continue
            first = min(core)
            for tail in permutations(set(core) - {first}):
                cycle = (first,) + tail
                if cycle[1] > cycle[-1]:
                    continue
                frame_edges = {
                    tuple(sorted((cycle[i], cycle[(i + 1) % length])))
                    for i in range(length)
                }
                if boundary & set(combinations(core, 2)) <= frame_edges:
                    answer.add(cycle)
    return tuple(sorted(answer))


def double_split_quotient(
    missing: set[tuple[int, int]],
    first_rows: tuple[frozenset[int], frozenset[int]],
    second_rows: tuple[frozenset[int], frozenset[int]],
) -> set[tuple[int, int]]:
    x, y, p, q = 7, 8, 9, 10
    boundary = set(combinations(S, 2)) - missing
    answer = set(boundary) | {(x, y), (p, q)}
    answer.update((x, s) for s in first_rows[0])
    answer.update((y, s) for s in first_rows[1])
    answer.update((p, s) for s in second_rows[0])
    answer.update((q, s) for s in second_rows[1])
    return {tuple(sorted(edge)) for edge in answer}


def audit_forced_packet_completion():
    """Replay the transparent K7 model closing the balanced packet."""
    missing = missing_graph((2, 1, 1))
    c15, c26, helper = 7, 8, 9
    edges = set(combinations(S, 2)) - missing
    edges.add((c15, c26))
    edges.update((c15, s) for s in (1, 5))
    edges.update((c26, s) for s in (2, 6))
    edges.update((helper, s) for s in S)
    edges = {tuple(sorted(edge)) for edge in edges}
    bags = (
        frozenset((0, 5)),
        frozenset((1, c15)),
        frozenset((2, c26)),
        frozenset((3,)),
        frozenset((4,)),
        frozenset((6,)),
        frozenset((helper,)),
    )

    def connected(bag):
        if len(bag) == 1:
            return True
        reached = {next(iter(bag))}
        while True:
            expanded = reached | {
                y
                for x in reached
                for y in bag
                if tuple(sorted((x, y))) in edges
            }
            if expanded == reached:
                return reached == set(bag)
            reached = expanded

    assert len(set().union(*bags)) == sum(map(len, bags))
    assert all(connected(bag) for bag in bags)
    assert all(
        any(tuple(sorted((x, y))) in edges for x in bags[i] for y in bags[j])
        for i in range(7)
        for j in range(i)
    )
    print("balanced forced-packet K7 bags", tuple(tuple(sorted(bag)) for bag in bags))


def audit_four_high_static_obstruction():
    """Show why the three-high closure is not all seven-edge gates."""
    missing = {
        (0, 1),
        (1, 2), (1, 3), (1, 4),
        (2, 3), (2, 4), (3, 4),
    }
    full = frozenset(S)
    common_only = frozenset((1, 2))
    assert k7_model(10, split_quotient(missing, full, common_only)) is None
    print(
        "four-high negative static row",
        tuple(sorted(full)), "|", tuple(sorted(common_only)),
    )


def audit_seven_edge_layer():
    distributions = ((4, 0, 0), (3, 1, 0), (2, 2, 0), (2, 1, 1))
    all_negative = {}
    for distribution in distributions:
        missing = missing_graph(distribution)
        for common in combinations(range(3), 2):
            negative = tuple(
                rows
                for rows in covering_rows(common)
                if k7_model(10, split_quotient(missing, *rows)) is None
            )
            maxima = maximal_rows(negative)
            all_negative[(distribution, common)] = negative
            print(
                "distribution", distribution,
                "common", common,
                "negative", len(negative),
                "maximal", len(maxima),
            )
            for row_x, row_y in maxima:
                print(
                    "  defects",
                    tuple(sorted(ALL_BOUNDARY - row_x)),
                    "|",
                    tuple(sorted(ALL_BOUNDARY - row_y)),
                )

    for key, negative in all_negative.items():
        distribution, _ = key
        if distribution != (2, 1, 1):
            assert not negative
        else:
            assert len(negative) == 10
            assert len(maximal_rows(negative)) == 4
    return all_negative


def audit_all_seven_edge_types():
    """Audit all 65 unlabelled seven-edge missing graphs.

    A common pair is tested only when both of its vertices have missing
    degree at least two, exactly the pairs that can be supplied by the
    low-boundary-degree multiplicity count.
    """
    types = tuple(
        graph
        for graph in nx.graph_atlas_g()
        if len(graph) == 7 and graph.number_of_edges() == 7
    )
    assert len(types) == 65
    survivors = []
    states = 0
    for missing_graph_nx in types:
        missing = {tuple(sorted(edge)) for edge in missing_graph_nx.edges()}
        low_boundary_degree = tuple(
            vertex
            for vertex in S
            if missing_graph_nx.degree(vertex) >= 2
        )
        type_rows = []
        for common in combinations(low_boundary_degree, 2):
            negative = []
            for rows in covering_rows(common):
                states += 1
                if k7_model(10, split_quotient(missing, *rows)) is None:
                    negative.append(rows)
            if negative:
                type_rows.append((common, tuple(negative)))
        if type_rows:
            survivors.append((missing_graph_nx.copy(), tuple(type_rows)))

    print("all seven-edge atlas states", states)
    print("unlabelled missing types with a negative repeated-root split", len(survivors))
    for graph, rows_by_pair in survivors:
        print(
            " type",
            nx.to_graph6_bytes(graph, header=False).strip().decode(),
            "degrees", tuple(sorted(dict(graph.degree()).values(), reverse=True)),
            "edges", tuple(sorted(tuple(sorted(edge)) for edge in graph.edges())),
        )
        for common, rows in rows_by_pair:
            print(
                "  common", common,
                "negative", len(rows),
                "maximal", len(maximal_rows(rows)),
            )
    return tuple(survivors)


def audit_opposite_crossings(all_negative):
    distribution = (2, 1, 1)
    missing = missing_graph(distribution)
    hulls = cyclic_hulls(missing)
    assert hulls == (
        (0, 1, 3, 5),
        (0, 1, 4, 5),
        (0, 2, 3, 6),
        (0, 2, 4, 6),
        (1, 2, 5, 6),
    )
    print("balanced cyclic hulls", hulls)

    for common in combinations(range(3), 2):
        union_survivable = set()
        forced_hull = (1, 2, 5, 6)
        for first_rows in all_negative[(distribution, common)]:
            survivable_hulls = set()
            for hull in hulls:
                pair_a = frozenset((hull[0], hull[2]))
                pair_b = frozenset((hull[1], hull[3]))
                for left, right in ((pair_a, pair_b), (pair_b, pair_a)):
                    remainder = tuple(sorted(ALL_BOUNDARY - left - right))
                    for mask in range(1 << len(remainder)):
                        row_p = left | frozenset(
                            s for i, s in enumerate(remainder) if mask >> i & 1
                        )
                        row_q = ALL_BOUNDARY - row_p
                        edges = double_split_quotient(
                            missing, first_rows, (row_p, row_q)
                        )
                        if k7_model(11, edges) is None:
                            survivable_hulls.add(hull)
                            break
                    if hull in survivable_hulls:
                        break
            union_survivable.update(survivable_hulls)
            # This is the literal assertion used in Proposition 4.2:
            # the 15/26 packet cannot be placed in the opposite shore for
            # any individual negative repeated-root row.
            assert forced_hull not in survivable_hulls
            print(
                "common", common,
                "rows",
                tuple(sorted(first_rows[0])),
                "|",
                tuple(sorted(first_rows[1])),
                "opposite-shore hulls",
                tuple(sorted(survivable_hulls)),
            )
        unavoidable = set(hulls) - union_survivable
        print(
            "common", common,
            "hulls forced into repeated-root shore",
            tuple(sorted(unavoidable)),
        )
        assert unavoidable == {forced_hull}


def main():
    print("candidate models n=10", len(candidate_models(10)))
    print("candidate models n=11", len(candidate_models(11)))
    negatives = audit_seven_edge_layer()
    audit_opposite_crossings(negatives)
    audit_forced_packet_completion()
    audit_four_high_static_obstruction()
    print("all exact quotient assertions verified")


if __name__ == "__main__":
    main()
