#!/usr/bin/env python3
"""Verify the literal opposite-decoration Kempe barrier."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "active" / "runtime" / "deps"))

import networkx as nx  # noqa: E402


U = {"0", "2", "4", "5", "6"}
S = U | {"w"}
cycle_edges = [("0", "2"), ("2", "6"), ("6", "5"), ("5", "4"), ("4", "0")]

G = nx.Graph(cycle_edges)
G.add_edges_from(
    [
        ("0", "eL"),
        ("eL", "5"),
        ("2", "fL"),
        ("fL", "4"),
        ("w", "l"),
        ("l", "eL"),
        ("0", "eR"),
        ("eR", "5"),
        ("2", "fR"),
        ("fR", "4"),
        ("w", "r"),
        ("r", "fR"),
    ]
)

left = S | {"eL", "fL", "l"}
right = S | {"eR", "fR", "r"}
assert (left - S).isdisjoint(right - S)
assert not any(G.has_edge(x, y) for x in left - S for y in right - S)

cL = {
    "0": 1,
    "5": 1,
    "l": 1,
    "fL": 1,
    "2": 2,
    "4": 2,
    "w": 2,
    "eL": 2,
    "6": 3,
}
cR = {
    "0": 1,
    "5": 1,
    "w": 1,
    "fR": 1,
    "2": 2,
    "4": 2,
    "r": 2,
    "eR": 2,
    "6": 3,
}


def proper(H: nx.Graph, colouring: dict[str, int]) -> bool:
    return all(colouring[x] != colouring[y] for x, y in H.edges())


assert proper(G.subgraph(left), cL)
assert proper(G.subgraph(right), cR)
assert cL["w"] == cL["2"] == cL["4"]
assert cR["w"] == cR["0"] == cR["5"]


def two_colour_component(
    H: nx.Graph, colouring: dict[str, int], start: str, target_colour: int
) -> set[str]:
    colours = {colouring[start], target_colour}
    T = H.subgraph([v for v in H if colouring[v] in colours])
    return set(nx.node_connected_component(T, start))


CL = two_colour_component(G.subgraph(left), cL, "w", 1)
CR = two_colour_component(G.subgraph(right), cR, "w", 2)
assert {"w", "l", "eL", "0"} <= CL
assert {"w", "r", "fR", "2"} <= CR
assert CL & U
assert CR & U

# Fixed-core geometric decoration sets are opposite and have no overlap.
WL = {"w", "l"}
WR = {"w", "r"}
EL = {"0", "eL", "5"}
FL = {"2", "fL", "4"}
ER = {"0", "eR", "5"}
FR = {"2", "fR", "4"}
assert nx.is_connected(G.subgraph(WL)) and nx.is_connected(G.subgraph(WR))
assert any(G.has_edge(x, y) for x in WL for y in EL)
assert not any(G.has_edge(x, y) for x in WL for y in FL | {"6"})
assert any(G.has_edge(x, y) for x in WR for y in FR)
assert not any(G.has_edge(x, y) for x in WR for y in ER | {"6"})

assert G.number_of_nodes() == 12
assert G.number_of_edges() == 17 < 21

print("GREEN: cL induces Pi_F and its fixed-U Kempe swap fails")
print("GREEN: cR induces Pi_E and its fixed-U Kempe swap fails")
print("GREEN: failure paths merely retrace the opposite fixed decorations")
print("GREEN: 17 host edges exclude a K7 minor")
