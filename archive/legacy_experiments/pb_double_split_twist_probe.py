#!/usr/bin/env python3
"""Classify paired safe vertex splits of adjacent PB vertices."""

from itertools import product
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "active" / "runtime" / "deps"))
sys.path.insert(0, str(ROOT / "results"))

import networkx as nx

from hc7_pentagonal_bipyramid_vertex_split_classifier_verify import (
    BOTH,
    X,
    Y,
    exact_k5_minor,
    has_crossing,
    pb_edges,
)


VERTICES = ("p", "q", "c0", "c1", "c2", "c3", "c4")
ROTATION = {
    "p": ("c0", "c1", "c2", "c3", "c4"),
    "q": ("c4", "c3", "c2", "c1", "c0"),
    "c0": ("c1", "p", "c4", "q"),
    "c1": ("c2", "p", "c0", "q"),
    "c2": ("c3", "p", "c1", "q"),
    "c3": ("c4", "p", "c2", "q"),
    "c4": ("c0", "p", "c3", "q"),
}


def double_split(
    first: str,
    second: str,
    first_assignment: dict[str, int],
    second_assignment: dict[str, int],
    crossed: bool,
) -> tuple[list[str], set[tuple[str, str]]]:
    old_edges = pb_edges()
    vertices = [v for v in VERTICES if v not in (first, second)]
    f0, f1, s0, s1 = f"{first}0", f"{first}1", f"{second}0", f"{second}1"
    vertices += [f0, f1, s0, s1]
    edges = {edge for edge in old_edges if first not in edge and second not in edge}
    edges |= {tuple(sorted((f0, f1))), tuple(sorted((s0, s1)))}
    for neighbour, mark in first_assignment.items():
        if mark in (X, BOTH):
            edges.add(tuple(sorted((f0, neighbour))))
        if mark in (Y, BOTH):
            edges.add(tuple(sorted((f1, neighbour))))
    for neighbour, mark in second_assignment.items():
        if mark in (X, BOTH):
            edges.add(tuple(sorted((s0, neighbour))))
        if mark in (Y, BOTH):
            edges.add(tuple(sorted((s1, neighbour))))
    if crossed:
        edges |= {tuple(sorted((f0, s1))), tuple(sorted((f1, s0)))}
    else:
        edges |= {tuple(sorted((f0, s0))), tuple(sorted((f1, s1)))}
    return vertices, edges


def full_word(vertex: str, other: str, assignment: dict[str, int]) -> tuple[int, ...]:
    return tuple(BOTH if neighbour == other else assignment[neighbour] for neighbour in ROTATION[vertex])


def census(first: str, second: str) -> None:
    first_other = [v for v in ROTATION[first] if v != second]
    second_other = [v for v in ROTATION[second] if v != first]
    checked = planar = k5 = exceptional = 0
    examples = []
    for left_word in product((X, Y, BOTH), repeat=len(first_other)):
        left = dict(zip(first_other, left_word))
        if has_crossing(full_word(first, second, left)):
            continue
        for right_word in product((X, Y, BOTH), repeat=len(second_other)):
            right = dict(zip(second_other, right_word))
            if has_crossing(full_word(second, first, right)):
                continue
            for crossed in (False, True):
                vertices, edges = double_split(first, second, left, right, crossed)
                checked += 1
                graph = nx.Graph()
                graph.add_nodes_from(vertices)
                graph.add_edges_from(edges)
                is_planar = nx.check_planarity(graph)[0]
                model = exact_k5_minor(vertices, edges)
                if is_planar:
                    planar += 1
                    assert model is None
                elif model is not None:
                    k5 += 1
                else:
                    exceptional += 1
                    if len(examples) < 5:
                        examples.append((left_word, right_word, crossed, edges))
    print(
        first,
        second,
        f"checked={checked}",
        f"planar={planar}",
        f"k5={k5}",
        f"nonplanar_k5free={exceptional}",
    )
    for example in examples:
        print("EXCEPTION", example)


def main() -> None:
    census("p", "c0")
    census("c0", "c1")


if __name__ == "__main__":
    main()
