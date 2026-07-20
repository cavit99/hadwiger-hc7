#!/usr/bin/env python3
"""Verify the full five-response pentagonal-bipyramid shell."""

from __future__ import annotations

from itertools import combinations, product
from pathlib import Path
import runpy
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "active" / "runtime" / "deps"))

import networkx as nx


COLUMNS = ("A0", "A1", "R0", "R1", "R2", "R3", "R4")


def has_rooted_k4(graph: nx.Graph, roots: set[str]) -> bool:
    """Exact four-bag census on the seven-vertex contact graph."""
    vertices = list(graph)
    for assignment in product(range(5), repeat=7):
        bags = [
            {vertices[i] for i, label in enumerate(assignment) if label == j}
            for j in range(4)
        ]
        if not all(bags) or not all(len(bag & roots) == 1 for bag in bags):
            continue
        if not all(nx.is_connected(graph.subgraph(bag)) for bag in bags):
            continue
        if all(
            any(graph.has_edge(x, y) for x in bags[i] for y in bags[j])
            for i in range(4)
            for j in range(i + 1, 4)
        ):
            return True
    return False


def build() -> tuple[nx.Graph, nx.Graph, dict[str, set[str]]]:
    pb = nx.Graph()
    pb.add_nodes_from(COLUMNS)
    for apex in COLUMNS[:2]:
        for rim in COLUMNS[2:]:
            pb.add_edge(apex, rim)
    for i in range(5):
        pb.add_edge(COLUMNS[2 + i], COLUMNS[2 + (i + 1) % 5])

    graph = nx.Graph()
    graph.add_edges_from((("p", "v"), ("p", "w")))
    columns: dict[str, set[str]] = {}
    for label in COLUMNS:
        columns[label] = {f"v{label}", f"h{label}", f"w{label}"}
        graph.add_edges_from(
            (
                ("v", f"v{label}"),
                (f"v{label}", f"h{label}"),
                (f"h{label}", f"w{label}"),
                (f"w{label}", "w"),
            )
        )
    for left, right in pb.edges():
        graph.add_edge(f"h{left}", f"h{right}")
    for label in ("A0", "R0", "R1"):
        graph.add_edges_from((("p", f"v{label}"), ("p", f"w{label}")))
    for left in ("A1", "R2"):
        for right in ("A1", "R2"):
            graph.add_edge(f"v{left}", f"w{right}")
    return graph, pb, columns


def main() -> None:
    graph, pb, columns = build()
    fv = {1: "A1", 2: "R2", 3: "A0", 4: "R0", 5: "R1"}
    fw = {1: "A0", 2: "R0", 3: "A1", 4: "R2", 5: "R1"}
    kind = {1: "X", 2: "X", 3: "Y", 4: "Y", 5: "Z"}

    colour = {
        "p": 0, "v": 0, "w": 0,
        "vA0": 3, "hA0": 5, "wA0": 1,
        "vA1": 1, "hA1": 2, "wA1": 3,
        "vR0": 4, "hR0": 1, "wR0": 2,
        "vR1": 5, "hR1": 0, "wR1": 5,
        "vR2": 2, "hR2": 1, "wR2": 4,
        "vR3": 2, "hR3": 3, "wR3": 4,
        "vR4": 3, "hR4": 4, "wR4": 5,
    }

    deleted = graph.copy()
    deleted.remove_edges_from((("p", "v"), ("p", "w")))
    assert set(colour) == set(deleted)
    assert all(colour[x] != colour[y] for x, y in deleted.edges())
    assert colour["p"] == colour["v"] == colour["w"] == 0
    assert len(set(fv.values())) == len(set(fw.values())) == 5
    for i in range(1, 6):
        assert colour[f"v{fv[i]}"] == colour[f"w{fw[i]}"] == i

        bichromatic = deleted.subgraph(
            [x for x in deleted if colour[x] in (0, i)]
        )
        component = next(
            set(block)
            for block in nx.connected_components(bichromatic)
            if "v" in block
        )
        observed = ("p" in component, "w" in component)
        expected = {"X": (False, False), "Y": (True, False), "Z": (True, True)}[
            kind[i]
        ]
        assert observed == expected
        p_component = next(
            set(block)
            for block in nx.connected_components(bichromatic)
            if "p" in block
        )
        if kind[i] == "X":
            assert "w" in p_component and f"w{fw[i]}" in p_component
        elif kind[i] == "Y":
            assert "v" in p_component and "w" not in p_component
            w_component = next(
                set(block)
                for block in nx.connected_components(bichromatic)
                if "w" in block
            )
            assert f"w{fw[i]}" in w_component
        else:
            assert {"p", "v", "w"} <= p_component

    for i in (1, 2):
        for j in (3, 4):
            assert graph.has_edge(f"v{fv[i]}", f"w{fw[j]}")

    contact = nx.Graph()
    contact.add_nodes_from(COLUMNS)
    for left, right in combinations(COLUMNS, 2):
        if any(
            graph.has_edge(x, y)
            for x in columns[left]
            for y in columns[right]
        ):
            contact.add_edge(left, right)
    assert {frozenset(edge) for edge in contact.edges()} == {
        frozenset(edge) for edge in pb.edges()
    }
    assert {fv[i] for i in (3, 4, 5)} | {fw[i] for i in (1, 2, 5)} == {
        "A0", "R0", "R1"
    }
    assert all(
        has_rooted_k4(pb, set(roots))
        for roots in combinations(COLUMNS, 4)
    )

    minor_module = runpy.run_path(
        str(ROOT / "barriers" / "hc7_balanced_order8_two_missing_colour_paths_verify.py")
    )
    assert not minor_module["has_k7_minor"](graph)
    assert nx.node_connectivity(graph) == 2
    greedy = nx.coloring.greedy_color(
        graph, strategy="saturation_largest_first"
    )
    assert max(greedy.values()) < 4

    print("GREEN full five-response PB shell obstruction")


if __name__ == "__main__":
    main()
