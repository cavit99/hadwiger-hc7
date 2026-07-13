#!/usr/bin/env python3
"""Probe a three-vertex full shore opposite one contracted full shore."""

import itertools

import networkx as nx

from portal_oneone_small_probe import A, B, M, N, U, W, nmeeting_k6


LABELS = U + (W, A)
DA = (8, 9, 10)
DB = 11


def graph(kind, rows, aw):
    g = nx.Graph()
    g.add_nodes_from(range(12))
    g.add_edges_from(M)
    if aw:
        g.add_edge(A, W)
    if kind == "path":
        g.add_edges_from(((8, 9), (9, 10)))
    else:
        g.add_edges_from(itertools.combinations(DA, 2))
    for d, row in zip(DA, rows):
        g.add_edges_from((d, LABELS[i]) for i in range(7) if row >> i & 1)
    g.add_edges_from((DB, x) for x in set(U) | {W, B})
    return g


def valid(kind, rows, aw):
    internal = (1, 2, 1) if kind == "path" else (2, 2, 2)
    if any(row.bit_count() + degree < 7 for row, degree in zip(rows, internal)):
        return False
    if rows[0] | rows[1] | rows[2] != (1 << 7) - 1:
        return False
    a_bit = 1 << 6
    a_contacts = sum(bool(row & a_bit) for row in rows)
    if 4 + aw + a_contacts < 7:
        return False
    return True


def run(kind):
    internal = (1, 2, 1) if kind == "path" else (2, 2, 2)
    choices = [
        [row for row in range(1 << 7) if row.bit_count() + degree >= 7]
        for degree in internal
    ]
    count = 0
    for aw in (False, True):
        for rows in itertools.product(*choices):
            if not valid(kind, rows, aw):
                continue
            count += 1
            model = nmeeting_k6(graph(kind, rows, aw))
            if model is None:
                print("failure", kind, aw, rows)
                return False, count, (aw, rows)
        print(kind, "aw", aw, "complete", count, flush=True)
    return True, count, None


def collect_triangle_failures():
    choices = [row for row in range(1 << 7) if row.bit_count() >= 5]
    failures = set()
    count = 0
    for aw in (False, True):
        for rows in itertools.combinations_with_replacement(choices, 3):
            if not valid("triangle", rows, aw):
                continue
            count += 1
            if nmeeting_k6(graph("triangle", rows, aw)) is None:
                failures.add((aw, rows))
    print("triangle canonical cases", count, "failures", len(failures))
    for item in sorted(failures):
        print("triangle survivor", item)
    return failures


def main():
    for kind in ("path",):
        print(kind, run(kind), flush=True)
    collect_triangle_failures()


if __name__ == "__main__":
    main()
