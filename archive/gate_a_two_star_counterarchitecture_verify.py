#!/usr/bin/env python3
"""Audit the two-star combined-gate counterarchitecture from Gate A."""

from itertools import combinations

import networkx as nx


LABELS = (1, 2, 3)


def build():
    g = nx.Graph()
    portals = {side: {label: set() for label in LABELS} for side in ("d", "e")}
    counts = {
        "d": {1: 3, 2: 3, 3: 1},
        "e": {1: 1, 2: 3, 3: 3},
    }
    for side in ("d", "e"):
        centre = side
        for label in LABELS:
            for i in range(counts[side][label]):
                leaf = f"{side}{label}_{i}"
                portals[side][label].add(leaf)
                g.add_edge(centre, leaf)
    for x in portals["d"][1]:
        for y in portals["e"][2]:
            g.add_edge(x, y)
    for x in portals["d"][2]:
        for y in portals["e"][3]:
            g.add_edge(x, y)
    g.add_node("L")
    g.add_node("R")
    for x in portals["d"][1] | portals["d"][2]:
        g.add_edge("L", x)
    for y in portals["e"][2] | portals["e"][3]:
        g.add_edge(y, "R")
    return g, portals


def connected_subset(g, subset):
    return bool(subset) and nx.is_connected(g.subgraph(subset))


def has_typed_shores(g, portal):
    vertices = tuple(g)
    universe = set(vertices)
    # It is enough for this small star to audit all bipartitions.
    for size in range(1, len(vertices)):
        for left_tuple in combinations(vertices, size):
            left = set(left_tuple)
            right = universe - left
            if not connected_subset(g, left) or not connected_subset(g, right):
                continue
            if not any(g.has_edge(x, y) for x in left for y in right):
                continue
            rows_left_0 = all(left & portal[i] for i in (1, 2))
            rows_left_1 = all(left & portal[i] for i in (1, 3))
            rows_right = all(right & portal[i] for i in (2, 3))
            if rows_right and (rows_left_0 or rows_left_1):
                return True
    return False


def main():
    g, portals = build()
    d = g.subgraph({"d"} | set().union(*portals["d"].values())).copy()
    e = g.subgraph({"e"} | set().union(*portals["e"].values())).copy()
    assert not has_typed_shores(d, portals["d"])
    assert not has_typed_shores(e, portals["e"])

    core = g.copy()
    core.remove_nodes_from(("d", "e", "L", "R"))
    profiles = []
    for component in nx.connected_components(core):
        profile = {
            label
            for label in LABELS
            if component
            & (portals["d"][label] | portals["e"][label])
        }
        profiles.append((len(component), profile, nx.check_planarity(core.subgraph(component))[0]))
    assert {frozenset(profile) for _, profile, _ in profiles} == {
        frozenset((1,)), frozenset((1, 2)),
        frozenset((2, 3)), frozenset((3,))
    }
    assert {
        (size, frozenset(profile)) for size, profile, _ in profiles if size > 1
    } == {(6, frozenset((1, 2))), (6, frozenset((2, 3)))}
    assert all(not planar for size, _, planar in profiles if size == 6)

    cut = nx.minimum_node_cut(g, "L", "R")
    assert len(cut) == 6, cut

    # Every Q-full connected subgraph must contain d or e: after deleting
    # them every component has a proper portal profile.  Hence at most two
    # such subgraphs can be disjoint, while D and E themselves witness two.
    assert all(profile != set(LABELS) for _, profile, _ in profiles)

    print("typed shore pairs: none in either star")
    print("combined lobe profiles:", sorted((size, sorted(profile)) for size, profile, _ in profiles))
    print("combined L-R separator order:", len(cut))
    print("nonplanar straddling systems:", sum(not planar for size, _, planar in profiles if size > 1))


if __name__ == "__main__":
    main()
