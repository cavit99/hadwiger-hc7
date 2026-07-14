#!/usr/bin/env python3
"""Exhaustively verify the rooted-K4 cross-lobe K7^vee quotient.

Requires the optional ``z3-solver`` package.  This is an active discovery
certificate: every SMT model is independently checked by ordinary graph
routines, and monotone reuse is allowed only after the same bags have been
checked with all unadvertised optional edges deleted.
"""

from __future__ import annotations

import argparse
import json
from itertools import combinations, product
from pathlib import Path
from typing import Iterable

import z3


Vertex = str
Edge = tuple[Vertex, Vertex]
Bag = frozenset[Vertex]

S = ("c", "a1", "t1", "a2", "t2", "a3", "t3")
PAIRS = (("a1", "t1"), ("a2", "t2"), ("a3", "t3"))
CORE = ("r", "h1", "h2", "h3")
PACKETS = ("p", "q")
VERTICES = (*S, *CORE, *PACKETS)
TARGET = 7


def require(condition: bool, message: str) -> None:
    """Keep proof checks active under ``python -O``."""

    if not condition:
        raise RuntimeError(message)


def edge(left: Vertex, right: Vertex) -> Edge:
    require(left != right, "loops are not valid quotient edges")
    return tuple(sorted((left, right)))


def boundary_groups() -> tuple[tuple[Edge, ...], ...]:
    groups: list[tuple[Edge, ...]] = []
    for pair in PAIRS:
        groups.append(tuple(edge("c", endpoint) for endpoint in pair))
    for first, second in combinations(PAIRS, 2):
        groups.append(tuple(edge(left, right) for left in first for right in second))
    return tuple(groups)


GROUPS = boundary_groups()
BOUNDARIES = tuple(frozenset(choice) for choice in product(*GROUPS))
require(len(BOUNDARIES) == 512, "wrong number of minimal boundaries")
require(len(set(BOUNDARIES)) == 512, "minimal boundaries are not distinct")


def fixed_edges(c_contact: Vertex) -> frozenset[Edge]:
    answer = {
        edge("h1", "a1"),
        edge("h1", "t3"),
        edge("h2", "a2"),
        edge("h2", "t2"),
        edge("h3", "a3"),
        edge("h3", "t1"),
        edge(c_contact, "c"),
    }
    answer.update(edge(left, right) for left, right in combinations(CORE, 2))
    answer.update(edge(packet, literal) for packet in PACKETS for literal in S)
    return frozenset(answer)


def neighbours(vertices: Iterable[Vertex], edges: frozenset[Edge]) -> dict[Vertex, set[Vertex]]:
    answer = {vertex: set() for vertex in vertices}
    for left, right in sorted(edges):
        answer[left].add(right)
        answer[right].add(left)
    return answer


def connected(bag: Bag, edges: frozenset[Edge]) -> bool:
    if not bag:
        return False
    adjacency = neighbours(bag, frozenset(e for e in edges if set(e) <= set(bag)))
    reached: set[Vertex] = set()
    stack = [min(bag)]
    while stack:
        vertex = stack.pop()
        if vertex in reached:
            continue
        reached.add(vertex)
        stack.extend(sorted(adjacency[vertex] - reached))
    return reached == set(bag)


def bags_adjacent(left: Bag, right: Bag, edges: frozenset[Edge]) -> bool:
    return any(edge(u, v) in edges for u in left for v in right)


def verify_model(edges: frozenset[Edge], bags: tuple[Bag, ...]) -> None:
    require(len(bags) == TARGET, "certificate does not have seven bags")
    require(all(bags), "certificate has an empty bag")
    require(
        all(left.isdisjoint(right) for left, right in combinations(bags, 2)),
        "certificate bags overlap",
    )
    require(
        all(bag <= set(VERTICES) for bag in bags),
        "certificate uses an unknown quotient vertex",
    )
    require(all(connected(bag, edges) for bag in bags), "a bag is disconnected")
    for left_index, right_index in combinations(range(TARGET), 2):
        if left_index == 0 and right_index in {1, 2}:
            continue
        require(
            bags_adjacent(bags[left_index], bags[right_index], edges),
            f"required bags {left_index},{right_index} are nonadjacent",
        )


def find_model(edges: frozenset[Edge]) -> tuple[Bag, ...] | None:
    """Find K7^vee bags; bag 0 is the deficient row."""

    index = {vertex: i for i, vertex in enumerate(VERTICES)}
    incidence = {vertex: [] for vertex in VERTICES}
    for left, right in sorted(edges):
        incidence[left].append(right)
        incidence[right].append(left)

    solver = z3.Solver()
    solver.set("random_seed", 0)
    assigned = [
        [z3.Bool(f"assigned_{i}_{branch}") for branch in range(TARGET)]
        for i in range(len(VERTICES))
    ]
    root = [
        [z3.Bool(f"root_{i}_{branch}") for branch in range(TARGET)]
        for i in range(len(VERTICES))
    ]
    depth = [
        [z3.Int(f"depth_{i}_{branch}") for branch in range(TARGET)]
        for i in range(len(VERTICES))
    ]
    root_index = [z3.Int(f"root_index_{branch}") for branch in range(TARGET)]

    for i in range(len(VERTICES)):
        solver.add(z3.PbLe([(assigned[i][branch], 1) for branch in range(TARGET)], 1))

    for branch in range(TARGET):
        solver.add(z3.PbEq([(root[i][branch], 1) for i in range(len(VERTICES))], 1))
        for i, vertex in enumerate(VERTICES):
            solver.add(depth[i][branch] >= 0, depth[i][branch] < len(VERTICES))
            solver.add(
                z3.Implies(
                    root[i][branch],
                    z3.And(
                        assigned[i][branch],
                        root_index[branch] == i,
                        depth[i][branch] == 0,
                    ),
                )
            )
            parents = [
                z3.And(
                    assigned[index[other]][branch],
                    depth[index[other]][branch] < depth[i][branch],
                )
                for other in incidence[vertex]
            ]
            solver.add(
                z3.Implies(
                    z3.And(assigned[i][branch], z3.Not(root[i][branch])),
                    z3.And(depth[i][branch] >= 1, z3.Or(parents)),
                )
            )

    # Remove the S_2 x S_4 symmetry among the two permitted missing columns
    # and the four columns which must meet the deficient row.
    solver.add(root_index[1] < root_index[2])
    solver.add(
        root_index[3] < root_index[4],
        root_index[4] < root_index[5],
        root_index[5] < root_index[6],
    )

    for left_branch, right_branch in combinations(range(TARGET), 2):
        if left_branch == 0 and right_branch in {1, 2}:
            continue
        witnesses = []
        for left, right in sorted(edges):
            i, j = index[left], index[right]
            witnesses.extend(
                (
                    z3.And(assigned[i][left_branch], assigned[j][right_branch]),
                    z3.And(assigned[j][left_branch], assigned[i][right_branch]),
                )
            )
        solver.add(z3.Or(witnesses))

    if solver.check() != z3.sat:
        return None
    model = solver.model()
    answer = tuple(
        frozenset(
            vertex
            for i, vertex in enumerate(VERTICES)
            if z3.is_true(model.eval(assigned[i][branch]))
        )
        for branch in range(TARGET)
    )
    verify_model(edges, answer)
    return answer


def audit_contact(c_contact: Vertex, show: bool) -> list[dict[str, object]]:
    base = fixed_edges(c_contact)
    uncovered = set(range(len(BOUNDARIES)))
    certificates: list[dict[str, object]] = []

    while uncovered:
        case_index = min(uncovered)
        boundary = BOUNDARIES[case_index]
        model = find_model(base | boundary)
        require(model is not None, f"uncovered quotient: {c_contact}, {sorted(boundary)}")

        # Greedily delete optional edges while retaining this exact model.
        required = set(boundary)
        advertised = set(base | boundary)
        for optional in sorted(required):
            smaller = frozenset(advertised - {optional})
            try:
                verify_model(smaller, model)
            except RuntimeError:
                continue
            advertised.remove(optional)
            required.remove(optional)

        literal_certificate_edges = frozenset(base | required)
        verify_model(literal_certificate_edges, model)
        covered = {
            index
            for index in uncovered
            if required <= BOUNDARIES[index]
        }
        require(bool(covered), "certificate covers no outstanding boundary")
        uncovered.difference_update(covered)
        certificates.append(
            {
                "c_contact": c_contact,
                "required_boundary_edges": [list(item) for item in sorted(required)],
                "bags": [sorted(bag) for bag in model],
            }
        )
        if show:
            print(
                c_contact,
                "requires",
                sorted(required),
                "bags",
                [sorted(bag) for bag in model],
                "covers",
                len(covered),
            )

    return certificates


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--show-certificates", action="store_true")
    parser.add_argument("--write-catalogue", type=Path)
    arguments = parser.parse_args()

    catalogue: list[dict[str, object]] = []
    for c_contact in CORE:
        certificates = audit_contact(c_contact, arguments.show_certificates)
        catalogue.extend(certificates)
        print(
            f"c contact {c_contact}: all 512 boundaries covered by "
            f"{len(certificates)} certificates"
        )
    print(f"all 2048 quotients covered; {len(catalogue)} monotone certificates used")
    if arguments.write_catalogue is not None:
        payload = {
            "format": "hc7-cross-lobe-rooted-k4-k7vee-v1",
            "vertices": list(VERTICES),
            "certificates": catalogue,
        }
        arguments.write_catalogue.write_text(
            json.dumps(payload, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        print(f"wrote {arguments.write_catalogue}")


if __name__ == "__main__":
    main()
