#!/usr/bin/env python3
"""Exact audit of the theta rail-median component contraction.

After deleting the two medians, each nondegenerate terminal arm is one
connected arm component and the two junction arms form one component
(unless both have length zero).  An arbitrary off-rail component can join
any collection of these arm components.  Contracting the whole component
is therefore represented exactly by the quotient below; no clean
first-hit path is assumed.
"""

from __future__ import annotations

from itertools import combinations

import networkx as nx

MISSING = {
    tuple(sorted(edge))
    for edge in ((0, 1), (0, 2), (0, 5), (1, 2), (1, 5), (2, 4), (4, 5))
}
ARM_NAMES = ("0", "5", "j", "1", "2")


def exact_model(
    graph: nx.Graph,
    order: int = 4,
    anchors: tuple[object, ...] = (0, 1, 2, 4, 5),
):
    vertices = list(graph)
    index = {vertex: i for i, vertex in enumerate(vertices)}
    adjacency = [0] * len(vertices)
    for u, v in graph.edges():
        i, j = index[u], index[v]
        adjacency[i] |= 1 << j
        adjacency[j] |= 1 << i
    anchor_mask = sum(1 << index[x] for x in anchors)

    def connected(mask: int) -> bool:
        reached = mask & -mask
        while True:
            expanded = reached
            todo = reached
            while todo:
                low = todo & -todo
                todo ^= low
                expanded |= adjacency[low.bit_length() - 1] & mask
            if expanded == reached:
                return reached == mask
            reached = expanded

    candidates = [
        mask for mask in range(1, 1 << len(vertices))
        if mask & anchor_mask and connected(mask)
    ]
    candidates.sort(key=lambda mask: (mask.bit_count(), mask))

    def adjacent(left: int, right: int) -> bool:
        todo = left
        while todo:
            low = todo & -todo
            todo ^= low
            if adjacency[low.bit_length() - 1] & right:
                return True
        return False

    def search(chosen: list[int], remaining: list[int], used: int):
        if len(chosen) == order:
            return tuple(chosen)
        needed = order - len(chosen)
        for pos, bag in enumerate(remaining):
            if bag & used:
                continue
            nxt = [
                other for other in remaining[pos + 1:]
                if not other & (used | bag) and adjacent(bag, other)
            ]
            if len(nxt) >= needed - 1:
                result = search(chosen + [bag], nxt, used | bag)
                if result is not None:
                    return result
        return None

    masks = search([], candidates, 0)
    if masks is None:
        return None
    bags = tuple(
        frozenset(vertices[i] for i in range(len(vertices)) if mask >> i & 1)
        for mask in masks
    )
    assert all(nx.is_connected(graph.subgraph(bag)) for bag in bags)
    assert all(bags[i].isdisjoint(bags[j]) for i, j in combinations(range(order), 2))
    assert all(
        any(graph.has_edge(x, y) for x in bags[i] for y in bags[j])
        for i, j in combinations(range(order), 2)
    )
    return bags


def quotient(
    zero: frozenset[str],
    absorbed: frozenset[str],
    extra_medians: frozenset[str],
    extra_targets: frozenset[int],
) -> nx.Graph:
    graph = nx.Graph()
    boundary = (0, 1, 2, 4, 5)
    graph.add_nodes_from(boundary)
    for u, v in combinations(boundary, 2):
        if tuple(sorted((u, v))) not in MISSING:
            graph.add_edge(u, v)

    # Four terminal arms, represented by one vertex when nondegenerate.
    for name, portal, median, label in (
        ("0", "p0", "cL", 0),
        ("5", "p5", "cL", 5),
        ("1", "p1", "cM", 1),
        ("2", "p2", "cM", 2),
    ):
        if name in zero:
            graph.add_edge(median, label)
        elif name in absorbed:
            graph.add_edges_from((("w", median), ("w", label)))
        else:
            graph.add_edges_from(((median, portal), (portal, label)))

    # The two junction arms plus their joining edge are one component after
    # the medians are deleted.  If absorbed, contraction gives w both median
    # contacts.  Otherwise retain its one- or two-vertex path.
    left_zero = "l" in zero
    right_zero = "m" in zero
    if "j" in absorbed:
        assert not (left_zero and right_zero)
        graph.add_edges_from((("w", "cL"), ("w", "cM")))
    elif left_zero and right_zero:
        graph.add_edge("cL", "cM")
    elif left_zero:
        graph.add_edges_from((("cL", "m"), ("m", "cM")))
    elif right_zero:
        graph.add_edges_from((("cL", "l"), ("l", "cM")))
    else:
        graph.add_edges_from((("cL", "l"), ("l", "m"), ("m", "cM")))

    graph.add_edge("w", 4)
    graph.add_edges_from(("w", median) for median in extra_medians)
    graph.add_edges_from(("w", target) for target in extra_targets)
    return graph


def main() -> None:
    negative_useful = []
    negative_target = []
    checked = 0
    witnesses = {}
    zero_names = ("0", "5", "l", "1", "2", "m")

    for zero_mask in range(1 << len(zero_names)):
        zero = frozenset(
            name for bit, name in enumerate(zero_names) if zero_mask >> bit & 1
        )
        available = [name for name in ("0", "5", "1", "2") if name not in zero]
        if not ({"l", "m"} <= zero):
            available.append("j")
        for absorbed_mask in range(1 << len(available)):
            absorbed = frozenset(
                name for bit, name in enumerate(available) if absorbed_mask >> bit & 1
            )

            # Automatic median contacts from absorbed arm components.
            automatic = set()
            if absorbed & {"0", "5", "j"}:
                automatic.add("cL")
            if absorbed & {"1", "2", "j"}:
                automatic.add("cM")
            for med_mask in range(4):
                medians = frozenset(
                    median
                    for bit, median in enumerate(("cL", "cM"))
                    if med_mask >> bit & 1
                ) | frozenset(automatic)
                if not medians:
                    # A component of C-{cL,cM} must attach back to C.
                    continue
                for target_mask in range(4):
                    targets = frozenset(
                        target for bit, target in enumerate((2, 5))
                        if target_mask >> bit & 1
                    )
                    checked += 1
                    graph = quotient(zero, absorbed, medians, targets)
                    model = exact_model(graph)
                    key = (tuple(sorted(zero)), tuple(sorted(absorbed)),
                           tuple(sorted(medians)), tuple(sorted(targets)))
                    useful = bool(absorbed & {"5", "2", "j"})
                    if useful and model is None:
                        negative_useful.append(key)
                    if targets and model is None:
                        negative_target.append(key)
                    if model is not None and (useful or targets):
                        witnesses.setdefault(
                            ("useful" if useful else "target", len(zero),
                             tuple(sorted(absorbed & {"5", "2", "j"})),
                             tuple(sorted(targets))),
                            model,
                        )

    print("checked", checked)
    print("negative useful", len(negative_useful))
    print("negative target", len(negative_target))
    if negative_useful:
        print("first negative useful", negative_useful[0])
    if negative_target:
        print("first negative target", negative_target[0])
    print("representative witness classes", len(witnesses))


if __name__ == "__main__":
    main()
