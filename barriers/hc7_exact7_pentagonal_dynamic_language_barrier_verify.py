#!/usr/bin/env python3
"""Verify the exact-seven K2-join-C5 dynamic-language barrier."""

from itertools import combinations


VERTICES = ("p", "q", "0", "1", "2", "3", "4")
CYCLE = tuple(str(i) for i in range(5))


def canonical_partition(blocks):
    return tuple(sorted(tuple(sorted(block)) for block in blocks))


def all_partitions(items):
    if not items:
        yield ()
        return
    first, *rest = items
    for partition in all_partitions(rest):
        yield ((first,),) + partition
        for index in range(len(partition)):
            yield (
                partition[:index]
                + (tuple(sorted(partition[index] + (first,))),)
                + partition[index + 1 :]
            )


def cycle_edge(index):
    return frozenset((str(index % 5), str((index + 1) % 5)))


COMPLEMENTARY_EDGES = {cycle_edge(i) for i in range(5)}


def boundary_edges():
    edges = {frozenset(("p", "q"))}
    for universal in ("p", "q"):
        edges.update(frozenset((universal, vertex)) for vertex in CYCLE)
    # Edges on the five cycle vertices are the nonedges of the displayed
    # complementary cycle.
    for pair in combinations(CYCLE, 2):
        edge = frozenset(pair)
        if edge not in COMPLEMENTARY_EDGES:
            edges.add(edge)
    return edges


BOUNDARY_EDGES = boundary_edges()


def is_independent(block):
    return all(frozenset(pair) not in BOUNDARY_EDGES for pair in combinations(block, 2))


def blocks(partition):
    return {frozenset(block) for block in partition}


def main():
    partitions = {
        canonical_partition(partition) for partition in all_partitions(VERTICES)
    }
    proper = {
        partition
        for partition in partitions
        if len(partition) <= 6 and all(is_independent(block) for block in partition)
    }
    assert len(proper) == 10

    single_pair = {partition for partition in proper if len(partition) == 6}
    double_pair = {partition for partition in proper if len(partition) == 5}
    assert len(single_pair) == len(double_pair) == 5
    assert proper == single_pair | double_pair
    assert not (single_pair & double_pair)

    independent_sets = {
        frozenset(subset)
        for size in range(1, len(VERTICES) + 1)
        for subset in combinations(VERTICES, size)
        if is_independent(subset)
    }
    assert len(independent_sets) == 12  # seven singletons and five pairs

    for independent_set in independent_sets:
        assert any(independent_set in blocks(partition) for partition in single_pair)
        assert any(independent_set in blocks(partition) for partition in double_pair)

    for vertex in VERTICES:
        singleton = frozenset((vertex,))
        assert any(singleton in blocks(partition) for partition in single_pair)
        assert any(singleton in blocks(partition) for partition in double_pair)

    trace_complete = []
    proper_list = sorted(proper)
    for mask in range(1, 1 << len(proper_list)):
        family = {
            proper_list[index]
            for index in range(len(proper_list))
            if mask & (1 << index)
        }
        if all(
            any(independent_set in blocks(partition) for partition in family)
            for independent_set in independent_sets
        ):
            trace_complete.append(family)

    minimum_size = min(map(len, trace_complete))
    assert minimum_size == 3
    minimum_families = [family for family in trace_complete if len(family) == 3]
    assert len(minimum_families) == 5
    assert all(
        sum(len(partition) == 6 for partition in family) == 1
        and sum(len(partition) == 5 for partition in family) == 2
        for family in minimum_families
    )

    state_s = {}
    state_d = {}
    for index in range(5):
        paired = cycle_edge(index)
        state_s[index] = canonical_partition(
            [paired, ("p",), ("q",)]
            + [(vertex,) for vertex in CYCLE if vertex not in paired]
        )
        matching = (cycle_edge(index + 1), cycle_edge(index + 3))
        state_d[index] = canonical_partition(
            [*matching, ("p",), ("q",), (str(index),)]
        )
    expected_minimum = {
        frozenset((state_s[index], state_d[index], state_d[(index + 1) % 5]))
        for index in range(5)
    }
    assert {frozenset(family) for family in minimum_families} == expected_minimum

    disjoint_minimum_pairs = {
        frozenset((i, j))
        for i, j in combinations(range(len(minimum_families)), 2)
        if minimum_families[i].isdisjoint(minimum_families[j])
    }
    assert len(disjoint_minimum_pairs) == 5

    complementary_splits = 0
    for family in trace_complete:
        if (proper - family) in trace_complete:
            complementary_splits += 1
    assert complementary_splits == 202  # oriented; 101 up to swapping sides

    print("proper boundary partitions", len(proper))
    print("six-block / five-block", len(single_pair), len(double_pair))
    print("nonempty independent traces", len(independent_sets))
    print("minimum trace-complete size", minimum_size)
    print("minimum trace-complete families", len(minimum_families))
    print("disjoint pairs of minimum families", len(disjoint_minimum_pairs))
    print("oriented complementary trace-complete splits", complementary_splits)
    print("PASS: exact-seven pentagonal response languages remain disjoint")


if __name__ == "__main__":
    main()
