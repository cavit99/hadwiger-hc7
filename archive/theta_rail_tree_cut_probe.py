#!/usr/bin/env python3
"""Exact quotient probe for CLEAN theta crossbar rail contacts only.

Fixed bags 3, 6 and the opposite full shore reduce K7 detection to K4
in the displayed rail/boundary quotient.  The component k contains a
4-portal, may absorb either bad arm (the 0-arm of the 05 rail and the
1-arm of the 12 rail), and may have an additional 2- or 5-portal.

This deliberately retains every arm not explicitly assigned to k.  It is
not a verifier for an arbitrary component of C-{cL,cM}: such a component
can absorb entire useful arms, and `theta_rail_component_absorption_verify.py`
shows that the broader median-cut inference is false.
"""

from __future__ import annotations

from itertools import combinations

import networkx as nx

from contact_order7_sixedge_web_probe import generic_minor_model


MISSING = {
    tuple(sorted(edge))
    for edge in ((0, 1), (0, 2), (0, 5), (1, 2), (1, 5), (2, 4), (4, 5))
}


def edge_set(graph: nx.Graph) -> set[tuple[int, int]]:
    labels = {vertex: index for index, vertex in enumerate(graph)}
    return {
        tuple(sorted((labels[u], labels[v]))) for u, v in graph.edges()
    }


def exact_model(graph: nx.Graph, k: int = 4) -> tuple[int, ...] | None:
    labels = {vertex: index for index, vertex in enumerate(graph)}
    edges = edge_set(graph)
    model = generic_minor_model(len(graph), edges, k)
    if model is None:
        return None

    adjacency = {index: set() for index in range(len(graph))}
    for u, v in edges:
        adjacency[u].add(v)
        adjacency[v].add(u)
    bag_sets = tuple(
        {vertex for vertex in range(len(graph)) if mask >> vertex & 1}
        for mask in model
    )
    assert len(bag_sets) == k
    assert all(bag_sets[i].isdisjoint(bag_sets[j]) for i, j in combinations(range(k), 2))
    assert all(nx.is_connected(nx.Graph(graph.subgraph([v for v, i in labels.items() if i in bag])))
               for bag in bag_sets)
    assert all(
        any(v in adjacency[u] for u in bag_sets[i] for v in bag_sets[j])
        for i, j in combinations(range(k), 2)
    )
    return model


def quotient(
    absorbed_bad_arms: frozenset[int],
    median_neighbours: frozenset[str],
    target: int | None,
    zero_arms: frozenset[str] = frozenset(),
) -> nx.Graph:
    graph = nx.Graph()
    boundary = (0, 1, 2, 4, 5)
    graph.add_nodes_from(boundary)
    for u, v in combinations(boundary, 2):
        if tuple(sorted((u, v))) not in MISSING:
            graph.add_edge(u, v)

    # Minimal three-terminal rail trees, joined at l--m.  A named arm in
    # zero_arms is contracted all the way to its rail median.
    for name, portal, median, boundary_label in (
        ("0", "p0", "cL", 0),
        ("5", "p5", "cL", 5),
        ("1", "p1", "cM", 1),
        ("2", "p2", "cM", 2),
    ):
        if name in zero_arms:
            graph.add_edge(median, boundary_label)
        else:
            graph.add_edges_from(((median, portal), (portal, boundary_label)))
    left_joint = "cL" if "l" in zero_arms else "l"
    right_joint = "cM" if "m" in zero_arms else "m"
    if left_joint != "cL":
        graph.add_edge("cL", left_joint)
    graph.add_edge(left_joint, right_joint)
    if right_joint != "cM":
        graph.add_edge(right_joint, "cM")

    graph.add_edge("k", 4)
    for median in median_neighbours:
        graph.add_edge("k", median)
    if target is not None:
        graph.add_edge("k", target)

    # Contract a bad arm into k when the component contains that arm.
    for label, portal in ((0, "p0"), (1, "p1")):
        if label in absorbed_bad_arms and portal in graph:
            median = "cL" if label == 0 else "cM"
            graph.remove_node(portal)
            graph.add_edge("k", label)
            graph.add_edge("k", median)
    return graph


def has_k4(graph: nx.Graph) -> bool:
    return exact_model(graph, 4) is not None


def useful_hit_quotient(
    rail_edge: tuple[str, str],
    at_endpoint: bool,
    absorbed_bad_arms: frozenset[int] = frozenset(),
    median_neighbours: frozenset[str] = frozenset({"cL"}),
    zero_arms: frozenset[str] = frozenset(),
) -> nx.Graph:
    graph = quotient(absorbed_bad_arms, median_neighbours, None, zero_arms)
    near, far = rail_edge
    if far not in graph:
        raise ValueError("the useful arm has length zero")
    if at_endpoint:
        graph.add_edge("k", far)
    else:
        graph.remove_edge(near, far)
        graph.add_edges_from(((near, "x"), ("x", far), ("k", "x")))
    return graph


def main() -> None:
    useful_rows = []
    for edge in (("cL", "p5"), ("cL", "l"), ("cM", "p2"), ("cM", "m")):
        for at_endpoint in (False, True):
            result = has_k4(useful_hit_quotient(edge, at_endpoint))
            useful_rows.append((edge, at_endpoint, result))
    assert all(row[2] for row in useful_rows)
    print("useful-arm first-hit certificates", len(useful_rows))

    useful_names = {
        ("cL", "p5"): "5",
        ("cL", "l"): "l",
        ("cM", "p2"): "2",
        ("cM", "m"): "m",
    }
    names = ("0", "5", "l", "1", "2", "m")
    useful_degenerate_checked = 0
    useful_degenerate_negative = []
    for zero_mask in range(1 << len(names)):
        zero = frozenset(name for bit, name in enumerate(names) if zero_mask >> bit & 1)
        available_bad = tuple(
            label for label, name in ((0, "0"), (1, "1")) if name not in zero
        )
        for edge, arm_name in useful_names.items():
            if arm_name in zero:
                continue
            for arms_mask in range(1 << len(available_bad)):
                arms = frozenset(
                    label for bit, label in enumerate(available_bad) if arms_mask >> bit & 1
                )
                for med_mask in range(1, 4):
                    medians = frozenset(
                        median
                        for bit, median in enumerate(("cL", "cM"))
                        if med_mask >> bit & 1
                    )
                    for at_endpoint in (False, True):
                        useful_degenerate_checked += 1
                        graph = useful_hit_quotient(edge, at_endpoint, arms, medians, zero)
                        if not has_k4(graph):
                            useful_degenerate_negative.append(
                                (tuple(sorted(zero)), edge, at_endpoint,
                                 tuple(sorted(arms)), tuple(sorted(medians)))
                            )
    print("degenerate useful-hit configurations", useful_degenerate_checked)
    print("degenerate useful-hit negatives", tuple(useful_degenerate_negative))
    assert not useful_degenerate_negative

    # Adversarially test the broader (and not assumed) statement that a
    # whole component of C-{cL,cM} reaching a useful arm is sufficient.
    # Two off-rail bridge vertices may connect the 4-portal to that arm
    # only through a bad rail segment.
    broad_counterexamples = []
    base = useful_hit_quotient(("cL", "p5"), True)
    # Undo the direct useful hit, retaining k as the 4-portal component.
    base.remove_edge("k", "p5")
    positions = ("p0", "p5", "l", "p1", "p2", "m")
    useful = {"p5", "l", "p2", "m"}
    for first in positions:
        for second_a in positions:
            for second_b in positions:
                graph = base.copy()
                graph.add_edges_from((("k", first), ("h", second_a), ("h", second_b)))
                reduced = graph.copy()
                reduced.remove_nodes_from(("cL", "cM"))
                component = nx.node_connected_component(reduced, "k")
                if not component & useful:
                    continue
                if not has_k4(graph):
                    broad_counterexamples.append((first, second_a, second_b))
    print("broad component-reach counterexamples", tuple(broad_counterexamples))

    rows = []
    for arms_mask in range(4):
        arms = frozenset(label for bit, label in enumerate((0, 1)) if arms_mask >> bit & 1)
        for med_mask in range(1, 4):
            medians = frozenset(
                median
                for bit, median in enumerate(("cL", "cM"))
                if med_mask >> bit & 1
            )
            for target in (None, 2, 5):
                result = has_k4(quotient(arms, medians, target))
                rows.append((tuple(sorted(arms)), tuple(sorted(medians)), target, result))

    negative_with_target = tuple(row for row in rows if row[2] is not None and not row[3])
    print("configurations", len(rows))
    print("negative with a 2/5 target portal", negative_with_target)
    print("positive with target", sum(row[3] for row in rows if row[2] is not None), "/", 24)

    # Repeat the target-portal test through every topological degeneration
    # obtained by making any subset of the six terminal arms length zero.
    degenerate_negative = []
    checked = 0
    for zero_mask in range(1 << len(names)):
        zero = frozenset(name for bit, name in enumerate(names) if zero_mask >> bit & 1)
        available_bad = tuple(
            label for label, name in ((0, "0"), (1, "1")) if name not in zero
        )
        for arms_mask in range(1 << len(available_bad)):
            arms = frozenset(
                label for bit, label in enumerate(available_bad) if arms_mask >> bit & 1
            )
            for med_mask in range(1, 4):
                medians = frozenset(
                    median
                    for bit, median in enumerate(("cL", "cM"))
                    if med_mask >> bit & 1
                )
                for target in (2, 5):
                    checked += 1
                    graph = quotient(arms, medians, target, zero)
                    if not has_k4(graph):
                        degenerate_negative.append(
                            (tuple(sorted(zero)), tuple(sorted(arms)), tuple(sorted(medians)), target)
                        )
    print("degenerate target configurations", checked)
    print("degenerate negatives", tuple(degenerate_negative))
    assert not negative_with_target
    assert not degenerate_negative


if __name__ == "__main__":
    main()
