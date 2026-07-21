#!/usr/bin/env python3
"""Classify every two-attachment bridge on the atomic ``H_0`` frame.

Let ``H_0=(K_7-{ab,cd})+{xa,xb,xc,xd}``.  An attachment at a branch
vertex ``v`` has support ``{v}``; an attachment in the interior of the
subdivided route ``uv`` has support ``{u,v}``.  The checker proves, for all
488 unordered canonical placements of one bridge path, that the augmented
frame has a ``K_7`` minor exactly when the two supports cross ``ab`` or
``cd``.

The positive cases are checked with an exact spanning connected-partition
minor oracle.  Every negative case is checked twice: the same oracle
exhausts all spanning seven-bag models, and deleting one of ``ef,eg,fg``
leaves a graph with a valid planar rotation certificate.  Suppressing
degree-two vertices reduces arbitrary route lengths to the canonical
placements built here.  An attachment next to an incident branch vertex,
or two consecutive attachments on one route, only creates a parallel path;
for simple clique minors that degenerate placement reduces to the
unaugmented frame, which is one of the checked survivors.

Run from the repository root with

    .venv/bin/python -B active/hc7_atomic_h0_single_bridge_falsifier.py

Expected final line:

    criterion: K7 iff the attachment supports cross ab or cd
"""

from __future__ import annotations

from collections import Counter
from functools import lru_cache
from itertools import combinations
from typing import Hashable

import networkx as nx


Node = Hashable
Attachment = tuple[str, str | tuple[str, str]]

BRANCHES = ("a", "b", "c", "d", "e", "f", "g", "x")
CORE_BRANCHES = BRANCHES[:-1]
DEFECTS = {frozenset(("a", "b")), frozenset(("c", "d"))}
APEX_PAIRS = (("e", "f"), ("e", "g"), ("f", "g"))


def pair(left: str, right: str) -> tuple[str, str]:
    return tuple(sorted((left, right)))


ROUTES = tuple(
    sorted(
        pair(left, right)
        for left, right in combinations(CORE_BRANCHES, 2)
        if frozenset((left, right)) not in DEFECTS
    )
    + [("a", "x"), ("b", "x"), ("c", "x"), ("d", "x")]
)
ROUTES = tuple(sorted(ROUTES))


def branch_attachment(vertex: str) -> Attachment:
    return ("branch", vertex)


def route_attachment(route: tuple[str, str]) -> Attachment:
    return ("route", route)


def attachment_support(attachment: Attachment) -> frozenset[str]:
    kind, payload = attachment
    if kind == "branch":
        assert isinstance(payload, str)
        return frozenset((payload,))
    assert isinstance(payload, tuple)
    return frozenset(payload)


def crosses_defect(left: Attachment, right: Attachment) -> bool:
    return any(
        frozenset((u, v)) in DEFECTS
        for u in attachment_support(left)
        for v in attachment_support(right)
    )


def placement_cases() -> tuple[tuple[Attachment, Attachment], ...]:
    attachments = tuple(map(branch_attachment, BRANCHES)) + tuple(
        map(route_attachment, ROUTES)
    )
    distinct = tuple(combinations(attachments, 2))
    same_route = tuple(
        (route_attachment(route), route_attachment(route)) for route in ROUTES
    )
    cases = distinct + same_route
    assert len(cases) == 488
    return cases


def atomic_frame() -> nx.Graph:
    graph = nx.Graph()
    graph.add_nodes_from(BRANCHES)
    graph.add_edges_from(ROUTES)
    assert len(graph) == 8 and graph.number_of_edges() == 23
    return graph


def bridge_augmentation(left: Attachment, right: Attachment) -> nx.Graph:
    """Return the suppressed canonical graph for one bridge placement."""

    graph = atomic_frame()
    if left[0] == "route" and right[0] == "branch":
        left, right = right, left

    if left[0] == right[0] == "branch":
        graph.add_edge(left[1], right[1])
        return graph

    if left[0] == "branch":
        branch = left[1]
        route = right[1]
        assert isinstance(branch, str) and isinstance(route, tuple)
        u, v = route
        graph.remove_edge(u, v)
        if branch not in route:
            attachment = ("p", u, v)
            graph.add_edges_from(
                ((u, attachment), (attachment, v), (branch, attachment))
            )
        else:
            # The interval vertex represents a nonempty route segment between
            # the incident branch and the attachment.  If that segment is
            # empty, the added bridge is parallel and has no effect on minors.
            other = v if branch == u else u
            interval = ("interval", branch, other)
            attachment = ("p", branch, other)
            graph.add_edges_from(
                (
                    (branch, interval),
                    (interval, attachment),
                    (attachment, other),
                    (branch, attachment),
                )
            )
        return graph

    first_route, second_route = left[1], right[1]
    assert isinstance(first_route, tuple) and isinstance(second_route, tuple)
    if first_route != second_route:
        first_attachment = ("p", *first_route)
        second_attachment = ("q", *second_route)
        for route, attachment in (
            (first_route, first_attachment),
            (second_route, second_attachment),
        ):
            u, v = route
            graph.remove_edge(u, v)
            graph.add_edges_from(((u, attachment), (attachment, v)))
        graph.add_edge(first_attachment, second_attachment)
        return graph

    # Two distinct attachments on one route.  Reversing their order gives an
    # isomorphic graph.  Consecutive attachments again add only a parallel
    # path, so the displayed nonempty interval is the strongest placement.
    u, v = first_route
    first_attachment = ("p", u, v)
    interval = ("interval", u, v)
    second_attachment = ("q", u, v)
    graph.remove_edge(u, v)
    graph.add_edges_from(
        (
            (u, first_attachment),
            (first_attachment, interval),
            (interval, second_attachment),
            (second_attachment, v),
            (first_attachment, second_attachment),
        )
    )
    return graph


def spanning_k7_model(graph: nx.Graph) -> tuple[frozenset[Node], ...] | None:
    """Return an exact spanning ``K_7`` model, or certify none exists.

    Every clique-minor model in a connected graph extends to a spanning one:
    absorb components outside the model one at a time into an adjacent bag.
    Restricted-growth recursion therefore examines a complete set of models.
    """

    vertices = tuple(graph)
    index = {vertex: position for position, vertex in enumerate(vertices)}
    rows = [0] * len(vertices)
    for u, v in graph.edges:
        left, right = index[u], index[v]
        rows[left] |= 1 << right
        rows[right] |= 1 << left

    @lru_cache(maxsize=None)
    def connected(mask: int) -> bool:
        reached = mask & -mask
        while True:
            old_reached = reached
            pending = reached
            while pending:
                bit = pending & -pending
                pending ^= bit
                reached |= rows[bit.bit_length() - 1] & mask
            if reached == old_reached:
                return reached == mask

    blocks: list[list[int]] = []

    def search(position: int) -> tuple[frozenset[Node], ...] | None:
        if position == len(vertices):
            if len(blocks) != 7:
                return None
            masks = tuple(sum(1 << vertex for vertex in block) for block in blocks)
            if not all(connected(mask) for mask in masks):
                return None
            for left, right in combinations(range(7), 2):
                neighbourhood = 0
                pending = masks[left]
                while pending:
                    bit = pending & -pending
                    pending ^= bit
                    neighbourhood |= rows[bit.bit_length() - 1]
                if not neighbourhood & masks[right]:
                    return None
            return tuple(
                frozenset(vertices[position] for position in block)
                for block in blocks
            )

        if len(blocks) + len(vertices) - position < 7:
            return None
        for block in blocks:
            block.append(position)
            model = search(position + 1)
            block.pop()
            if model is not None:
                return model
        if len(blocks) < 7:
            blocks.append([position])
            model = search(position + 1)
            blocks.pop()
            if model is not None:
                return model
        return None

    return search(0)


def verify_k7_model(
    graph: nx.Graph, model: tuple[frozenset[Node], ...]
) -> None:
    assert len(model) == 7
    assert set().union(*map(set, model)) == set(graph)
    assert sum(map(len, model)) == len(graph)
    assert all(nx.is_connected(graph.subgraph(branch_set)) for branch_set in model)
    for left, right in combinations(model, 2):
        assert any(graph.has_edge(u, v) for u in left for v in right)


def planarizing_apex_pair(graph: nx.Graph) -> tuple[str, str] | None:
    """Return and validate a planar rotation certificate after two deletions."""

    for apex_pair in APEX_PAIRS:
        remainder = graph.subgraph(set(graph) - set(apex_pair)).copy()
        planar, embedding = nx.check_planarity(remainder, counterexample=False)
        if not planar:
            continue
        assert set(embedding) == set(remainder)
        assert all(embedding.has_edge(u, v) for u, v in remainder.edges)
        embedding.check_structure()
        return apex_pair
    return None


def route_pair_signature(
    left: Attachment, right: Attachment
) -> tuple[int, int]:
    first = attachment_support(left)
    second = attachment_support(right)
    intersection = len(first & second)
    defect_crosses = sum(
        frozenset((u, v)) in DEFECTS for u in first for v in second
    )
    return intersection, defect_crosses


def main() -> None:
    outcome_counts: Counter[tuple[str, bool]] = Counter()
    apex_counts: Counter[tuple[str, str]] = Counter()
    route_pair_counts: Counter[tuple[int, int, bool]] = Counter()

    for left, right in placement_cases():
        graph = bridge_augmentation(left, right)
        model = spanning_k7_model(graph)
        predicted = crosses_defect(left, right)
        assert (model is not None) == predicted

        kind = left[0][0] + right[0][0]
        outcome_counts[kind, predicted] += 1
        if left[0] == right[0] == "route":
            route_pair_counts[*route_pair_signature(left, right), predicted] += 1

        if model is not None:
            verify_k7_model(graph, model)
        else:
            apex_pair = planarizing_apex_pair(graph)
            assert apex_pair is not None
            apex_counts[apex_pair] += 1

    assert outcome_counts == Counter(
        {
            ("bb", True): 2,
            ("bb", False): 26,
            ("br", True): 24,
            ("br", False): 160,
            ("rr", True): 70,
            ("rr", False): 206,
        }
    )
    assert route_pair_counts == Counter(
        {
            (1, 1, True): 12,
            (1, 0, False): 99,
            (0, 2, True): 2,
            (0, 1, True): 56,
            (0, 0, False): 84,
            (2, 0, False): 23,
        }
    )
    assert apex_counts == Counter(
        {("e", "f"): 361, ("e", "g"): 26, ("f", "g"): 5}
    )

    print("GREEN atomic H0 single-bridge classification")
    print("H0: branches=8 routes=23")
    print(
        "placements: total=488 branch-branch=28 "
        "branch-route=184 route-route=276"
    )
    print(
        "terminal K7: total=96 branch-branch=2 "
        "branch-route=24 route-route=70"
    )
    print(
        "two-apex survivors: total=392 branch-branch=26 "
        "branch-route=160 route-route=206"
    )
    print("planarizing certificates: ef=361 eg=26 fg=5")
    print("criterion: K7 iff the attachment supports cross ab or cd")


if __name__ == "__main__":
    main()
