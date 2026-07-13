"""Exact check of the smallest all-degree-four K3,3 routing core.

Each colour has three non-root vertices.  They have supports {0,1}, {0,2},
and {1,2}; hence every non-root has degree four in the union of the nine
Kempe paths.  Each of the 18 bits chooses one of the two possible orders of
the relevant support vertices on one side of one path.  Root-preserving
K3,3 automorphisms reduce the 2^18 cases to 3692 orbits.  Z3 checks the
rooted branch-set conditions exactly.
"""

from __future__ import annotations

import itertools
import multiprocessing as mp
import os
import sys
import time

from z3 import And, Implies, Int, Or, Solver, sat, unknown


PERMS = list(itertools.permutations(range(3)))


def parity_map(p: tuple[int, ...], omit: int) -> int:
    source = [x for x in range(3) if x != omit]
    return int([p[x] for x in source] != sorted(p[x] for x in source))


PBIT = {(p, omit): parity_map(p, omit) for p in PERMS for omit in range(3)}


def transform(bits: int, rows: tuple[int, ...], cols: tuple[int, ...], swap: bool) -> int:
    result = 0
    for i in range(3):
        for j in range(3):
            row_order = (bits >> (3 * i + j)) & 1
            col_order = (bits >> (9 + 3 * i + j)) & 1
            ni, nj = rows[i], cols[j]
            row_order ^= PBIT[cols, j]
            col_order ^= PBIT[rows, i]
            if swap:
                # Swapping the bipartition also reverses the orientation of
                # every root-to-root path.  Each relevant order has length
                # two, so reversal toggles its bit.
                result |= (row_order ^ 1) << (9 + 3 * nj + ni)
                result |= (col_order ^ 1) << (3 * nj + ni)
            else:
                result |= row_order << (3 * ni + nj)
                result |= col_order << (9 + 3 * ni + nj)
    return result


def orbit_representatives() -> list[int]:
    seen: set[int] = set()
    representatives: list[int] = []
    for bits in range(1 << 18):
        if bits in seen:
            continue
        orbit = {
            transform(bits, rows, cols, swap)
            for rows in PERMS
            for cols in PERMS
            for swap in (False, True)
        }
        seen.update(orbit)
        representatives.append(min(orbit))
    assert len(seen) == 1 << 18
    assert len(representatives) == 3692
    return representatives


def graph(bits: int) -> list[tuple[int, int]]:
    # Roots are 0,...,5.  Vertex (colour, omitted neighbour) follows.
    vertex: dict[tuple[int, int], int] = {}
    next_vertex = 6
    for colour in range(6):
        for omitted in range(3):
            vertex[colour, omitted] = next_vertex
            next_vertex += 1

    edges: set[tuple[int, int]] = set()
    for i in range(3):
        for j0 in range(3):
            j = 3 + j0
            row_vertices = [vertex[i, k] for k in range(3) if k != j0]
            col_vertices = [vertex[j, k] for k in range(3) if k != i]
            if (bits >> (3 * i + j0)) & 1:
                row_vertices.reverse()
            if (bits >> (9 + 3 * i + j0)) & 1:
                col_vertices.reverse()
            path = [i, col_vertices[0], row_vertices[0], col_vertices[1], row_vertices[1], j]
            for u, v in zip(path, path[1:]):
                edges.add(tuple(sorted((u, v))))
    return sorted(edges)


def check(bits: int) -> tuple[int, str, list[tuple[int, int]]]:
    edges = graph(bits)
    n = 24
    adjacency = [[] for _ in range(n)]
    for u, v in edges:
        adjacency[u].append(v)
        adjacency[v].append(u)

    solver = Solver()
    solver.set(timeout=10_000)
    owner = [Int(f"o{v}") for v in range(n)]
    depth = [Int(f"d{v}") for v in range(n)]
    for v in range(n):
        solver.add(owner[v] >= -1, owner[v] < 6, depth[v] >= 0, depth[v] <= n)
    for root in range(6):
        solver.add(owner[root] == root, depth[root] == 0)
    for v in range(6, n):
        for label in range(6):
            solver.add(
                Implies(
                    owner[v] == label,
                    And(
                        depth[v] > 0,
                        Or(*[
                            And(owner[w] == label, depth[w] < depth[v])
                            for w in adjacency[v]
                        ]),
                    ),
                )
            )
    for i in range(3):
        for j in range(3, 6):
            solver.add(
                Or(*[
                    Or(And(owner[u] == i, owner[v] == j), And(owner[u] == j, owner[v] == i))
                    for u, v in edges
                ])
            )
    return bits, str(solver.check()), edges


def main() -> int:
    representatives = orbit_representatives()
    workers = min(12, os.cpu_count() or 4)
    start = time.time()
    unknown_cases: list[int] = []
    with mp.Pool(workers) as pool:
        for count, (bits, result, edges) in enumerate(
            pool.imap_unordered(check, representatives, chunksize=4), 1
        ):
            if result == "unsat":
                print(f"COUNTEREXAMPLE bits={bits} edges={edges}")
                pool.terminate()
                return 1
            if result == str(unknown):
                unknown_cases.append(bits)
            if count % 500 == 0:
                print(f"checked={count} seconds={time.time()-start:.1f} unknown={len(unknown_cases)}")
    print(
        f"All {len(representatives)} orbits are satisfiable; "
        f"unknown={len(unknown_cases)} seconds={time.time()-start:.1f}."
    )
    return 2 if unknown_cases else 0


if __name__ == "__main__":
    sys.exit(main())
