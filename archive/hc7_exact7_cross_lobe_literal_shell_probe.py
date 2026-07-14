#!/usr/bin/env python3
"""Probe the rooted-K4 handoff quotients for a literal K6-minus shell.

This is a discovery probe, not a proof artifact.  A positive result for all
minimal quotients would feed the audited literal-shell extraction theorem.
"""

from __future__ import annotations

import importlib.util
from itertools import combinations
from pathlib import Path


SOURCE = (
    Path(__file__).parent.parent
    / "results"
    / "hc7_exact7_cross_lobe_rooted_k4_handoff_verify.py"
)
SPEC = importlib.util.spec_from_file_location("rooted_handoff", SOURCE)
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def adjacent(left: str, right: str, edges: frozenset[tuple[str, str]]) -> bool:
    return MODULE.edge(left, right) in edges


def literal_shell(edges: frozenset[tuple[str, str]]):
    vertices = MODULE.VERTICES
    for core in combinations(vertices, 4):
        if not all(adjacent(x, y, edges) for x, y in combinations(core, 2)):
            continue
        common = [
            vertex
            for vertex in vertices
            if vertex not in core
            and all(adjacent(vertex, root, edges) for root in core)
        ]
        if len(common) >= 2:
            return core, tuple(common[:2])
    return None


def main() -> None:
    failures = []
    for c_contact in MODULE.CORE:
        base = MODULE.fixed_edges(c_contact)
        for index, boundary in enumerate(MODULE.BOUNDARIES):
            edges = base | boundary
            if literal_shell(edges) is None:
                failures.append((c_contact, index, sorted(boundary)))
                if len(failures) == 10:
                    break
        if len(failures) == 10:
            break
    if failures:
        print(f"literal shell fails in at least {len(failures)} quotients")
        for failure in failures:
            print(failure)
        raise SystemExit(1)
    print("all 2048 quotients contain a literal K6-minus shell")


if __name__ == "__main__":
    main()
