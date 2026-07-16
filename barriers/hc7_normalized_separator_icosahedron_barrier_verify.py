#!/usr/bin/env python3
"""Verify the normalized-separator structure in the icosahedral join."""

from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from results.hc7_join_near_clique_dichotomy_verify import (
    G_ADJ,
    G_EDGES,
    G_VERTICES,
    adjacent_sets,
    connected,
    edge_key,
)


roots = {0, 2}
J = set(G_VERTICES) - roots
T1 = {4}
T2 = {"p", "q"}
T3 = {3, 6, 5}
T4 = {11}
T5 = {10}
model = [T1, T2, T3, T4, T5]

assert all(connected(branch, G_ADJ) for branch in model)
assert sum(map(len, model)) == len(set().union(*model))
for i, earlier in enumerate(model):
    for later in model[i + 1 :]:
        assert all(
            any(edge_key(x, y) in G_EDGES for x in earlier)
            for y in later
        )

cycle = [3, 6, 5, 11, 10]
cycle_edges = {
    edge_key(cycle[i], cycle[(i + 1) % len(cycle)])
    for i in range(len(cycle))
}
induced_edges = {
    edge_key(x, y)
    for i, x in enumerate(cycle)
    for y in cycle[i + 1 :]
    if edge_key(x, y) in G_EDGES
}
assert induced_edges == cycle_edges

S = T2 | set(cycle)
assert len(S) == 7
remaining_J = J - S
assert 8 in remaining_J and 4 in remaining_J
assert not connected(remaining_J, G_ADJ)
assert not (G_ADJ[4] & (remaining_J - {4}))

remaining_G = set(G_VERTICES) - S
assert not connected(remaining_G, G_ADJ)
assert not (G_ADJ[4] & (remaining_G - {4}))

colour_classes = [{0, 2, 4}, {1, 3, 7}, {5, 8, 10}, {6, 9, 11}]
for colour_class in colour_classes:
    for x in colour_class:
        for y in colour_class:
            if x < y:
                assert edge_key(x, y) not in G_EDGES

root_colour_sets = []
colour_of = {
    vertex: colour
    for colour, colour_class in enumerate(colour_classes)
    for vertex in colour_class
}
colour_of.update({"p": 4, "q": 5})
for root in (0, 2):
    root_colour_sets.append({colour_of[x] for x in G_ADJ[root] & J})
assert all(0 not in colours for colours in root_colour_sets)

print("normalized dominating K5 model verified")
print("induced cycle and order-seven separator verified")
print("universal two-root colouring cover failure verified")
print("ALL CHECKS PASSED")
