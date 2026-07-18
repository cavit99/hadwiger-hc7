#!/usr/bin/env python3
"""Check the three explicit K7 models in the minimal three-path quotient."""

from __future__ import annotations

from itertools import combinations


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def edge(left: str, right: str) -> tuple[str, str]:
    return tuple(sorted((left, right)))


def base_edges() -> set[tuple[str, str]]:
    edges: set[tuple[str, str]] = set()

    def add(left: str, right: str) -> None:
        edges.add(edge(left, right))

    for index in range(4):
        add(f"u{index}", f"u{(index + 1) % 4}")
        add(f"u{index}", f"x{index}")
    for index in range(5):
        add(f"x{index}", f"x{(index + 1) % 5}")
        add("v", f"x{index}")
        add("b1", f"x{index}")
        add("b2", f"x{index}")
    for vertex in ("b0", "b1", "b2"):
        add("v", vertex)
    add("b0", "x3")
    add("b0", "x4")

    for terminal in ("u0", "u2", "z0", "z1", "z2"):
        add("aI", terminal)
    for terminal in ("u1", "u3", "z0", "z1", "z2"):
        add("aJ", terminal)
    add("z0", "z1")
    add("z0", "z2")
    for index in range(3):
        add("b1", f"z{index}")
        add(f"z{index}", "u0")
    for left, right in (
        ("b0", "b1"),
        ("b0", "b2"),
        ("b1", "b2"),
        ("b1", "u0"),
        ("b2", "aJ"),
    ):
        add(left, right)
    return edges


MODELS = {
    "b0-z0": (
        {"b0"},
        {"b2"},
        {"u2", "u3", "x0", "x1", "x2", "aI", "aJ", "z0"},
        {"x3"},
        {"x4"},
        {"b1", "z1", "z2"},
        {"v"},
    ),
    "b0-z2": (
        {"u1", "u2", "x0", "x1", "x2", "aI"},
        {"b2"},
        {"x4"},
        {"b1", "z0"},
        {"u3", "x3", "aJ", "z1"},
        {"b0", "z2"},
        {"v"},
    ),
    "b0-z1": (
        {"u0", "x0", "x4", "aJ", "z0"},
        {"b0", "z1"},
        {"b2", "x2"},
        {"x3"},
        {"u2", "u3", "aI"},
        {"b1", "z2"},
        {"u1", "x1", "v"},
    ),
}


def connected(vertices: set[str], edges: set[tuple[str, str]]) -> bool:
    reached = {next(iter(vertices))}
    while True:
        enlarged = reached | {
            other
            for vertex in reached
            for other in vertices
            if edge(vertex, other) in edges
        }
        if enlarged == reached:
            return reached == vertices
        reached = enlarged


def verify_model(
    edges: set[tuple[str, str]], branch_sets: tuple[set[str], ...]
) -> None:
    require(len(branch_sets) == 7, "the certificate must have seven branch sets")
    require(
        all(branch_sets),
        "every branch set must be nonempty",
    )
    require(
        sum(map(len, branch_sets)) == len(set().union(*branch_sets)),
        "branch sets must be pairwise disjoint",
    )
    require(
        all(connected(branch, edges) for branch in branch_sets),
        "every branch set must be connected",
    )
    require(
        all(
            any(edge(left, right) in edges for left in first for right in second)
            for first, second in combinations(branch_sets, 2)
        ),
        "every two branch sets must be adjacent",
    )


def main() -> None:
    for contact, model in MODELS.items():
        edges = base_edges() | {edge(*contact.split("-"))}
        verify_model(edges, model)
        print(f"{contact}: K7 model verified")
    print("GREEN: the three possible b0-to-{z0,z1,z2} contacts are exhausted")


if __name__ == "__main__":
    main()
