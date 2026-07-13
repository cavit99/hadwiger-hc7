#!/usr/bin/env python3
"""Search for a strict-relative-boundary three-demand obstruction.

The shore graph is fixed.  Boolean variables choose its contacts to a
seven-label boundary.  We require every proper relative boundary to have
order at least eight, all three two-demand packets to exist, and no
simultaneous three-demand linkage.

This is a falsification tool only: UNSAT for one fixed shore is not used as
a theorem.  A SAT model is a concrete counterarchitecture to the proposed
minimum-fragment principle.
"""

from __future__ import annotations

from itertools import combinations
import os

from z3 import And, Bool, If, Not, Or, Solver, Sum, sat


LABELS = range(7)
DEMANDS = ((0, 1), (2, 3), (4, 5))

PRESET = os.environ.get("SHORE_PRESET", "clean_web")
GRAPH6 = os.environ.get("SHORE_GRAPH6")
if GRAPH6:
    import networkx as nx

    graph = nx.from_graph6_bytes(GRAPH6.encode("ascii"))
    N = len(graph)
    raw_edges = tuple(graph.edges())
    PRESET = f"graph6:{GRAPH6}"
elif PRESET == "prism":
    N = 6
    raw_edges = (
        (0, 2), (2, 3), (3, 0),
        (1, 4), (4, 5), (5, 1),
        (0, 1), (2, 5), (3, 4),
    )
elif PRESET == "clean_web":
    N = 8
    raw_edges = (
        (0, 1), (0, 2), (0, 5), (0, 6),
        (1, 3), (1, 6), (1, 7),
        (2, 3), (2, 4), (2, 5), (2, 6), (2, 7),
        (3, 7),
        (4, 5), (4, 6),
        (5, 6), (5, 7),
        (6, 7),
    )
else:
    raise ValueError(f"unknown SHORE_PRESET={PRESET!r}")

EDGES = {tuple(sorted(edge)) for edge in raw_edges}


def neighbours(vertex: int) -> set[int]:
    return {
        other
        for other in range(N)
        if tuple(sorted((vertex, other))) in EDGES
    }


NEIGHBOURS = tuple(neighbours(vertex) for vertex in range(N))


def vertices(mask: int) -> tuple[int, ...]:
    return tuple(vertex for vertex in range(N) if mask >> vertex & 1)


def connected(mask: int) -> bool:
    if not mask:
        return False
    start = (mask & -mask).bit_length() - 1
    reached = {start}
    while True:
        expanded = reached | {
            neighbour
            for vertex in reached
            for neighbour in NEIGHBOURS[vertex]
            if mask >> neighbour & 1
        }
        if expanded == reached:
            return len(reached) == mask.bit_count()
        reached = expanded


CONNECTED = tuple(mask for mask in range(1, 1 << N) if connected(mask))


def disjoint_tuples(order: int):
    def recurse(chosen: tuple[int, ...], start: int, used: int):
        if len(chosen) == order:
            yield chosen
            return
        for index in range(start, len(CONNECTED)):
            mask = CONNECTED[index]
            if mask & used:
                continue
            yield from recurse(chosen + (mask,), index + 1, used | mask)

    yield from recurse((), 0, 0)


def main() -> None:
    solver = Solver()
    contact = {
        (vertex, label): Bool(f"p_{vertex}_{label}")
        for vertex in range(N)
        for label in LABELS
    }

    def hits(mask: int, label: int):
        return Or(*(contact[vertex, label] for vertex in vertices(mask)))

    # Every label has a portal.
    for label in LABELS:
        solver.add(Or(*(contact[vertex, label] for vertex in range(N))))

    # A minimum-fragment shore has no nested exact seven-boundary: every
    # proper relative boundary has order at least eight.
    for mask in range(1, (1 << N) - 1):
        inside = set(vertices(mask))
        internal_boundary = {
            neighbour
            for vertex in inside
            for neighbour in NEIGHBOURS[vertex]
            if neighbour not in inside
        }
        needed = 8 - len(internal_boundary)
        if needed > 0:
            solver.add(
                Sum(*(If(hits(mask, label), 1, 0) for label in LABELS))
                >= needed
            )

    # Each pair of demands has two disjoint connected carriers.  The two
    # carriers are labelled by the two demands, so both orientations of an
    # unordered mask pair are admitted.
    disjoint_pairs = tuple(disjoint_tuples(2))
    for first, second in combinations(range(3), 2):
        a, b = DEMANDS[first]
        c, d = DEMANDS[second]
        witnesses = []
        for left, right in disjoint_pairs:
            witnesses.append(
                And(hits(left, a), hits(left, b), hits(right, c), hits(right, d))
            )
            witnesses.append(
                And(hits(right, a), hits(right, b), hits(left, c), hits(left, d))
            )
        solver.add(Or(*witnesses))

    # Forbid three pairwise disjoint carriers, one for each demand.
    triple_constraints = 0
    for masks in disjoint_tuples(3):
        for assignment in (
            (0, 1, 2), (0, 2, 1), (1, 0, 2),
            (1, 2, 0), (2, 0, 1), (2, 1, 0),
        ):
            terms = []
            for mask, demand_index in zip(masks, assignment):
                a, b = DEMANDS[demand_index]
                terms.extend((hits(mask, a), hits(mask, b)))
            solver.add(Not(And(*terms)))
            triple_constraints += 1

    result = solver.check()
    print("preset", PRESET)
    print("connected masks", len(CONNECTED))
    print("disjoint pairs", len(disjoint_pairs))
    print("forbidden labelled triples", triple_constraints)
    print("result", result)
    if result == sat:
        model = solver.model()
        rows = {
            label: tuple(
                vertex
                for vertex in range(N)
                if model.evaluate(contact[vertex, label], model_completion=True)
            )
            for label in LABELS
        }
        print("portal rows", rows)


if __name__ == "__main__":
    main()
