#!/usr/bin/env python3
"""Check the atomic fan residue after Dirac and Rolek--Song input.

The parent process runs the seven completed-core rows in fresh child
processes.  This keeps the exact minor detector's deletion/contraction
cache bounded without introducing a non-standard dependency.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]


def load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


D = load(
    "six_terminal_decoder",
    ROOT / "results/hc7_disjoint_k6minus_six_terminal_crossing_decoder.py",
)
B = load(
    "two_fan_barrier",
    ROOT / "barriers/hc7_repaired_contact_two_fan_barrier.py",
)

W = 14
C = 12
BASE_NEIGHBOURS = frozenset((D.A0, D.B0, C))
CANDIDATES = tuple(sorted(set(range(14)) - BASE_NEIGHBOURS))

PATTERN_A = frozenset((D.A1, D.A2, D.A3, D.B1, D.B2))
PATTERN_X = frozenset((D.A1, D.A2, D.X, D.B1, D.B2))
EXPECTED_DEGREE_EIGHT = frozenset((PATTERN_A, PATTERN_X))

NAMES = (
    "a0", "a1", "a2", "a3", "x", "y",
    "b0", "b1", "b2", "r", "p", "q", "c", "d", "w",
)


def edge(left: int, right: int) -> tuple[int, int]:
    return tuple(sorted((left, right)))


def literal_atomic_graph(case_index: int) -> frozenset[tuple[int, int]]:
    """Replace the first filled rail edge by the literal two-edge rail."""

    _, completed = B.completed_core(*B.CASES[case_index])
    graph = {edge(*pair) for pair in completed}
    graph.remove(edge(D.A0, D.B0))
    graph.update(edge(W, vertex) for vertex in BASE_NEIGHBOURS)
    return frozenset(graph)


def augmented(
    graph: frozenset[tuple[int, int]], extras: frozenset[int]
) -> frozenset[tuple[int, int]]:
    return graph | frozenset(edge(W, vertex) for vertex in extras)


def has_k7(graph: frozenset[tuple[int, int]]) -> bool:
    return D.has_k7_minor(15, graph)


def independence_number(
    vertices: frozenset[int], graph: frozenset[tuple[int, int]]
) -> int:
    for size in range(len(vertices), 0, -1):
        if any(
            all(edge(u, v) not in graph for u, v in itertools.combinations(choice, 2))
            for choice in itertools.combinations(sorted(vertices), size)
        ):
            return size
    return 0


def disjoint_core_paths(
    graph: frozenset[tuple[int, int]],
    neighbourhood: frozenset[int],
    first_pair: tuple[int, int],
    second_pair: tuple[int, int],
) -> tuple[tuple[int, ...], tuple[int, ...]]:
    adjacency = {vertex: set() for vertex in range(15)}
    for u, v in graph:
        adjacency[u].add(v)
        adjacency[v].add(u)
    forbidden = neighbourhood | frozenset((W,))

    def shortest_path(
        ends: tuple[int, int], removed: frozenset[int]
    ) -> tuple[int, ...] | None:
        left, right = ends
        queue = [(left,)]
        seen = {left}
        for path in queue:
            current = path[-1]
            if current == right:
                return path
            for following in sorted(adjacency[current]):
                if following in seen or following in removed:
                    continue
                if following != right and following in forbidden:
                    continue
                seen.add(following)
                queue.append(path + (following,))
        return None

    first_left, first_right = first_pair
    answer: tuple[tuple[int, ...], tuple[int, ...]] | None = None

    def visit(path: tuple[int, ...]) -> bool:
        nonlocal answer
        current = path[-1]
        if current == first_right:
            second = shortest_path(second_pair, frozenset(path))
            if second is not None:
                answer = (path, second)
                return True
            return False
        for following in sorted(adjacency[current]):
            if following in path:
                continue
            if following != first_right and following in forbidden:
                continue
            if visit(path + (following,)):
                return True
        return False

    assert visit((first_left,)) and answer is not None
    return answer


def analyse_case(case_index: int) -> dict[str, object]:
    graph = literal_atomic_graph(case_index)
    completed = subprocess.run(
        [sys.executable, __file__, "--negative-four", str(case_index)],
        check=True,
        capture_output=True,
        text=True,
    )
    negative_four = frozenset(
        frozenset(choice) for choice in json.loads(completed.stdout)
    )
    assert negative_four
    assert all(
        independence_number(BASE_NEIGHBOURS | extras, graph) == 3
        for extras in negative_four
    )

    possible_five = tuple(
        extras
        for choice in itertools.combinations(CANDIDATES, 5)
        for extras in (frozenset(choice),)
        if all(extras - {vertex} in negative_four for vertex in extras)
    )
    negative_five = frozenset(
        extras for extras in possible_five if not has_k7(augmented(graph, extras))
    )
    assert negative_five == EXPECTED_DEGREE_EIGHT
    assert all(
        independence_number(BASE_NEIGHBOURS | extras, graph) == 3
        for extras in negative_five
    )

    # Every six-set contains a four-set already verified positive.  Hence
    # every degree-at-least-nine core-contained neighbourhood is positive.
    assert all(
        any(frozenset(subset) not in negative_four for subset in itertools.combinations(choice, 4))
        for choice in itertools.combinations(CANDIDATES, 6)
    )

    path_certificates = []
    for extras, target in ((PATTERN_A, D.A3), (PATTERN_X, D.X)):
        local = augmented(graph, extras)
        neighbourhood = BASE_NEIGHBOURS | extras
        for index, mate in ((1, D.B1), (2, D.B2)):
            first, second = disjoint_core_paths(
                local,
                neighbourhood,
                (D.A0, mate),
                (target, D.B0),
            )
            path_certificates.append(
                {
                    "pattern": "a3" if target == D.A3 else "x",
                    "trace": index,
                    "paths": (
                        tuple(NAMES[vertex] for vertex in first),
                        tuple(NAMES[vertex] for vertex in second),
                    ),
                }
            )

    return {
        "case": case_index,
        "negative_degree_seven": len(negative_four),
        "negative_degree_eight": tuple(
            tuple(NAMES[vertex] for vertex in sorted(extras))
            for extras in sorted(negative_five, key=lambda item: tuple(sorted(item)))
        ),
        "path_certificates": tuple(path_certificates),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--case", type=int)
    parser.add_argument("--negative-four", type=int)
    args = parser.parse_args()
    if args.negative_four is not None:
        graph = literal_atomic_graph(args.negative_four)
        negative = [
            tuple(choice)
            for choice in itertools.combinations(CANDIDATES, 4)
            if not has_k7(augmented(graph, frozenset(choice)))
        ]
        print(json.dumps(negative))
        return
    if args.case is not None:
        print(json.dumps(analyse_case(args.case), sort_keys=True))
        return

    rows = []
    for case_index in range(len(B.CASES)):
        completed = subprocess.run(
            [sys.executable, __file__, "--case", str(case_index)],
            check=True,
            capture_output=True,
            text=True,
        )
        rows.append(json.loads(completed.stdout))

    payload = json.dumps(rows, sort_keys=True, separators=(",", ":"))
    print("rows", len(rows))
    print("degree_seven_negative_counts", tuple(row["negative_degree_seven"] for row in rows))
    print("degree_eight_negative_counts", tuple(len(row["negative_degree_eight"]) for row in rows))
    print("rolek_core_path_pairs", sum(len(row["path_certificates"]) for row in rows))
    print("certificate_digest", hashlib.sha256(payload.encode()).hexdigest())
    print("GREEN: atomic Dirac residues and internal Rolek path pairs verified")


if __name__ == "__main__":
    main()
