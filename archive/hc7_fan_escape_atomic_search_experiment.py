#!/usr/bin/env python3
"""Explore one-vertex escapes from the completed two-fan obstruction.

This is a research script.  It compares the filled adhesion triangle used
in the clique-sum barrier with the literal subdivided linkage path, where
the artificial edge a0-b0 is absent.
"""

from __future__ import annotations

import importlib.util
import itertools
from pathlib import Path


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

NAMES = (
    "a0", "a1", "a2", "a3", "x", "y",
    "b0", "b1", "b2", "r", "p", "q", "c", "d",
)


def negative_sets(
    case: tuple[int, int, int], *, keep_filled_a0b0: bool, extra_count: int = 4
) -> tuple[tuple[str, ...], ...]:
    order, edges = B.completed_core(*case)
    assert order == 14
    graph = set(edges)
    if not keep_filled_a0b0:
        graph.discard(B.edge(D.A0, D.B0))

    w = order
    graph.update(
        {
            B.edge(w, D.A0),
            B.edge(w, D.B0),
            B.edge(w, 12),  # first fan centre c
        }
    )
    candidates = sorted(set(range(order)) - {D.A0, D.B0, 12})
    negative: list[tuple[str, ...]] = []
    for choice in itertools.combinations(candidates, extra_count):
        augmented = frozenset(graph | {B.edge(w, vertex) for vertex in choice})
        if not D.has_k7_minor(order + 1, augmented):
            negative.append(tuple(NAMES[vertex] for vertex in choice))
    return tuple(negative)


def neighbourhood_independence(
    case: tuple[int, int, int], choice_names: tuple[str, ...], *, filled: bool
) -> int:
    _, edges = B.completed_core(*case)
    graph = set(edges)
    if not filled:
        graph.discard(B.edge(D.A0, D.B0))
    inverse = {name: index for index, name in enumerate(NAMES)}
    neighbours = {D.A0, D.B0, 12, *(inverse[name] for name in choice_names)}
    maximum = 0
    for size in range(1, len(neighbours) + 1):
        for subset in itertools.combinations(neighbours, size):
            if all(B.edge(u, v) not in graph for u, v in itertools.combinations(subset, 2)):
                maximum = size
    return maximum


def induced_hit_sequences(
    left: int,
    right: int,
    allowed: tuple[int, ...],
    core_edges: set[tuple[int, int]],
) -> tuple[tuple[int, ...], ...]:
    answer = []
    for size in range(len(allowed) + 1):
        for internal in itertools.permutations(allowed, size):
            sequence = (left, *internal, right)
            if all(
                B.edge(sequence[i], sequence[j]) not in core_edges
                for i in range(len(sequence))
                for j in range(i + 2, len(sequence))
            ):
                answer.append(internal)
    return tuple(answer)


def main() -> None:
    for filled in (False,):
        families = []
        for index, case in enumerate(B.CASES[:1]):
            family = negative_sets(case, keep_filled_a0b0=filled, extra_count=6)
            families.append(family)
            print(
                "case", filled, index, "negative6", len(family),
                "alphas6", tuple(neighbourhood_independence(case, item, filled=filled) for item in family),
                flush=True,
            )
            D.has_k7_minor.cache_clear()
        common = set(families[0])
        for family in families[1:]:
            common.intersection_update(family)
        print("filled_a0b0", filled)
        print("negative_counts", tuple(map(len, families)))
        print("common_negative", tuple(sorted(common)))

    case = B.CASES[0]
    _, core_edges = B.completed_core(*case)
    literal_edges = {B.edge(*edge) for edge in core_edges}
    literal_edges.discard(B.edge(D.A0, D.B0))
    patterns = (
        (D.A1, D.A2, D.A3, D.B1, D.B2),
        (D.A1, D.A2, D.X, D.B1, D.B2),
    )
    for pattern in patterns:
        neighbourhood = {D.A0, D.B0, 12, *pattern}
        triples = tuple(
            choice
            for choice in itertools.combinations(sorted(neighbourhood), 3)
            if all(
                B.edge(u, v) not in literal_edges
                for u, v in itertools.combinations(choice, 2)
            )
        )
        print("pattern", tuple(NAMES[v] for v in pattern))
        for independent in triples:
            remainder = neighbourhood - set(independent)
            missing = tuple(
                (NAMES[u], NAMES[v])
                for u, v in itertools.combinations(sorted(remainder), 2)
                if B.edge(u, v) not in literal_edges
            )
            print(" independent", tuple(NAMES[v] for v in independent), "missing", missing)

        w = 14
        graph = set(core_edges)
        graph.discard(B.edge(D.A0, D.B0))
        graph.update(
            {B.edge(w, D.A0), B.edge(w, D.B0), B.edge(w, 12)}
            | {B.edge(w, vertex) for vertex in pattern}
        )
        target = D.A3 if D.A3 in pattern else D.X
        print(
            "equality_target",
            NAMES[target],
            "to_b0_positive",
            D.has_k7_minor(15, frozenset(graph | {B.edge(target, D.B0)})),
        )
        print(
            "disjoint_pair_positive",
            D.has_k7_minor(
                15,
                frozenset(
                    graph
                    | {
                        B.edge(D.A0, D.B1),
                        B.edge(target, D.B0),
                    }
                ),
            ),
        )
        induced_vertices = tuple(sorted(neighbourhood | {w}))
        induced_edges = frozenset(
            graph
            | {
                B.edge(D.A0, D.B1),
                B.edge(target, D.B0),
            }
        )
        induced_order, induced_graph = D.normalize_graph(induced_vertices, induced_edges)
        print(
            "disjoint_pair_induced_positive",
            D.has_k7_minor(induced_order, induced_graph),
        )
        outside = sorted(set(range(14)) - neighbourhood)
        one_hit_negatives = []
        for which in (0, 1):
            for middle in outside:
                first_sequence = (
                    (D.A0, middle, D.B1)
                    if which == 0
                    else (D.A0, D.B1)
                )
                second_sequence = (
                    (target, D.B0)
                    if which == 0
                    else (target, middle, D.B0)
                )
                path_edges = {
                    B.edge(u, v)
                    for sequence in (first_sequence, second_sequence)
                    for u, v in zip(sequence, sequence[1:])
                }
                if not D.has_k7_minor(15, frozenset(graph | path_edges)):
                    one_hit_negatives.append((which, NAMES[middle]))
                D.has_k7_minor.cache_clear()
        print("one_hit_negative_routings", tuple(one_hit_negatives))
        normalized_core_edges = {B.edge(*edge) for edge in graph}
        first_sequences = induced_hit_sequences(
            D.A0, D.B1, tuple(outside), normalized_core_edges
        )
        second_sequences = induced_hit_sequences(
            target, D.B0, tuple(outside), normalized_core_edges
        )
        print(
            "induced_sequence_counts",
            len(first_sequences),
            len(second_sequences),
        )
        sequence_negatives = []
        tested = 0
        for first_internal in first_sequences:
            for second_internal in second_sequences:
                if set(first_internal) & set(second_internal):
                    continue
                tested += 1
                path_edges = {
                    B.edge(u, v)
                    for sequence in (
                        (D.A0, *first_internal, D.B1),
                        (target, *second_internal, D.B0),
                    )
                    for u, v in zip(sequence, sequence[1:])
                }
                if not D.has_k7_minor(15, frozenset(graph | path_edges)):
                    sequence_negatives.append(
                        (
                            tuple(NAMES[v] for v in first_internal),
                            tuple(NAMES[v] for v in second_internal),
                        )
                    )
                    print("first_induced_sequence_negative", sequence_negatives[-1], flush=True)
                    break
                D.has_k7_minor.cache_clear()
            if sequence_negatives:
                break
        print("induced_sequence_pairs", tested)
        print("induced_sequence_negatives", tuple(sequence_negatives))
        D.has_k7_minor.cache_clear()


if __name__ == "__main__":
    main()
