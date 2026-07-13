#!/usr/bin/env python3
"""Audit all crossings of the six-terminal order for K_{3,2,2}."""

import itertools

import c5_core_k2_shore_verify as exact


ORDER = (1, 3, 5, 2, 4, 6)
X, Y, H = exact.X, exact.Y, exact.D


def edges_for(first_pair, second_pair):
    edges = set(exact.boundary_edges("K3+2K2"))
    edges.add((X, Y))
    edges.update((s, H) for s in exact.S)
    edges.update(tuple(sorted((X, s))) for s in first_pair)
    edges.update(tuple(sorted((Y, s))) for s in second_pair)
    return {tuple(sorted(edge)) for edge in edges}


def bags(model):
    return tuple(tuple(v for v in exact.V if mask >> v & 1) for mask in model)


def main():
    failures = []
    full_partition_failures = []
    checked = 0
    for i, r, j, s in itertools.combinations(range(6), 4):
        first = (ORDER[i], ORDER[j])
        second = (ORDER[r], ORDER[s])
        model = exact.k_minor_model(edges_for(first, second))
        checked += 1
        if model is None:
            failures.append((first, second))
        else:
            print(first, second, bags(model))
        free = tuple(v for v in exact.S if v not in first and v not in second)
        bad_partitions = []
        for choices in itertools.product((0, 1), repeat=len(free)):
            nx = set(first)
            ny = set(second)
            for vertex, side in zip(free, choices):
                (nx if side == 0 else ny).add(vertex)
            full_model = exact.k_minor_model(edges_for(tuple(nx), tuple(ny)))
            if full_model is None:
                bad_partitions.append((tuple(sorted(nx)), tuple(sorted(ny))))
        if bad_partitions:
            full_partition_failures.append((first, second, bad_partitions))
    print("checked", checked, "failures", failures)
    print("crossings with a bad full bipartition", len(full_partition_failures))
    for item in full_partition_failures:
        print(" bad", item)


if __name__ == "__main__":
    main()
