#!/usr/bin/env python3
"""Solver-free replay of the frozen cross-lobe K7^vee catalogue.

This checker deliberately shares no graph or certificate-checking code with
the Z3 discovery script.  Every catalogue row is checked on the graph with
only its advertised boundary edges, and all 2,048 minimal quotients must be
covered monotonically.
"""

from __future__ import annotations

import json
from itertools import combinations, product
from pathlib import Path


HERE = Path(__file__).resolve().parent
CATALOGUE = HERE / "hc7_exact7_cross_lobe_rooted_k4_handoff_catalogue.json"

S = ("c", "a1", "t1", "a2", "t2", "a3", "t3")
PAIRS = (("a1", "t1"), ("a2", "t2"), ("a3", "t3"))
CORE = ("r", "h1", "h2", "h3")
VERTICES = frozenset((*S, *CORE, "p", "q"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def edge(left: str, right: str) -> tuple[str, str]:
    require(left != right, "loop in certificate")
    return tuple(sorted((left, right)))


def boundary_groups() -> tuple[tuple[tuple[str, str], ...], ...]:
    groups: list[tuple[tuple[str, str], ...]] = []
    for pair in PAIRS:
        groups.append(tuple(edge("c", endpoint) for endpoint in pair))
    for first, second in combinations(PAIRS, 2):
        groups.append(tuple(edge(x, y) for x in first for y in second))
    return tuple(groups)


BOUNDARIES = tuple(
    frozenset(chosen) for chosen in product(*boundary_groups())
)
require(len(BOUNDARIES) == 512, "wrong boundary universe")
require(len(set(BOUNDARIES)) == 512, "duplicate minimal boundary")


def base_edges(contact: str) -> frozenset[tuple[str, str]]:
    require(contact in CORE, f"invalid c-contact {contact}")
    answer = {edge(x, y) for x, y in combinations(CORE, 2)}
    answer.update(
        {
            edge("h1", "a1"),
            edge("h1", "t3"),
            edge("h2", "a2"),
            edge("h2", "t2"),
            edge("h3", "a3"),
            edge("h3", "t1"),
            edge("c", contact),
        }
    )
    answer.update(edge(packet, literal) for packet in ("p", "q") for literal in S)
    return frozenset(answer)


def is_connected(bag: frozenset[str], edges: frozenset[tuple[str, str]]) -> bool:
    if not bag:
        return False
    reached = {min(bag)}
    while True:
        enlarged = reached | {
            vertex
            for vertex in bag - reached
            if any(edge(vertex, old) in edges for old in reached)
        }
        if enlarged == reached:
            return reached == set(bag)
        reached = enlarged


def are_adjacent(
    left: frozenset[str],
    right: frozenset[str],
    edges: frozenset[tuple[str, str]],
) -> bool:
    return any(edge(x, y) in edges for x in left for y in right)


def check_bags(
    bags: tuple[frozenset[str], ...],
    edges: frozenset[tuple[str, str]],
    row: int,
) -> None:
    require(len(bags) == 7, f"row {row}: not seven bags")
    require(all(bags), f"row {row}: empty bag")
    require(
        all(left.isdisjoint(right) for left, right in combinations(bags, 2)),
        f"row {row}: overlapping bags",
    )
    require(all(bag <= VERTICES for bag in bags), f"row {row}: unknown vertex")
    require(all(is_connected(bag, edges) for bag in bags), f"row {row}: disconnected bag")
    for i, j in combinations(range(7), 2):
        if i == 0 and j in (1, 2):
            continue
        require(are_adjacent(bags[i], bags[j], edges), f"row {row}: missing {i}-{j}")


def main() -> None:
    data = json.loads(CATALOGUE.read_text(encoding="utf-8"))
    require(data.get("format") == "hc7-cross-lobe-rooted-k4-k7vee-v1", "wrong format")
    require(frozenset(data.get("vertices", ())) == VERTICES, "wrong vertex universe")
    raw_certificates = data.get("certificates")
    require(isinstance(raw_certificates, list), "certificates must be a list")

    certificates: dict[str, list[frozenset[tuple[str, str]]]] = {
        contact: [] for contact in CORE
    }
    for row, raw in enumerate(raw_certificates):
        require(isinstance(raw, dict), f"row {row}: not an object")
        contact = raw.get("c_contact")
        require(contact in CORE, f"row {row}: bad contact")
        required = frozenset(edge(*item) for item in raw.get("required_boundary_edges", ()))
        require(any(required <= boundary for boundary in BOUNDARIES), f"row {row}: covers no boundary")
        bags = tuple(frozenset(bag) for bag in raw.get("bags", ()))
        check_bags(bags, base_edges(contact) | required, row)
        certificates[contact].append(required)

    for contact in CORE:
        require(certificates[contact], f"no certificates for {contact}")
        for index, boundary in enumerate(BOUNDARIES):
            require(
                any(required <= boundary for required in certificates[contact]),
                f"uncovered quotient {contact}:{index}",
            )

    print(
        "GREEN: solver-free replay checked "
        f"{len(raw_certificates)} certificates covering all 2048 quotients"
    )


if __name__ == "__main__":
    main()
