#!/usr/bin/env python3
"""Superseded classifier for rural-reflection closures across Moser C5 frames."""

from itertools import combinations

import networkx as nx


S = tuple(range(7))
EDGES = {
    (0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (1, 6),
    (2, 6), (3, 4), (3, 5), (4, 5), (5, 6),
}
H = nx.Graph()
H.add_nodes_from(S)
H.add_edges_from(EDGES)


def cycle_order(vertices):
    start = min(vertices)
    order = [start]
    previous = None
    current = start
    while len(order) < len(vertices):
        choices = sorted(set(H.neighbors(current)) & set(vertices) - {previous})
        nxt = next(x for x in choices if x not in order or len(order) + 1 == len(vertices))
        order.append(nxt)
        previous, current = current, nxt
    assert H.has_edge(order[-1], order[0])
    return order


def partitions(items):
    items = tuple(items)
    labels = [0]

    def rec(index, maximum):
        if index == len(items):
            blocks = [set() for _ in range(maximum + 1)]
            for item, label in zip(items, labels):
                blocks[label].add(item)
            yield tuple(frozenset(block) for block in blocks)
            return
        for label in range(maximum + 2):
            labels.append(label)
            yield from rec(index + 1, max(maximum, label))
            labels.pop()

    yield from rec(1, 0)


def independent(block):
    return not any(H.has_edge(x, y) for x, y in combinations(block, 2))


def reflectable(left, right):
    outside = set(S) - set(left) - set(right)
    for partition in partitions(sorted(outside)):
        if not all(independent(block) for block in partition):
            continue
        possible = False
        for star in partition:
            remainder = [block for block in partition if block != star]
            if not all(len(block) == 1 for block in remainder):
                continue
            literals = [next(iter(block)) for block in remainder]
            if not all(H.has_edge(x, y) for x, y in combinations(literals, 2)):
                continue
            if not all(any(H.has_edge(q, x) for x in left) for q in literals):
                continue
            if not all(any(H.has_edge(q, x) for x in right) for q in literals):
                continue
            possible = True
            break
        if not possible:
            return False
    return True


def main():
    frames = []
    for left, right in combinations(S, 2):
        if H.has_edge(left, right):
            continue
        remaining = set(S) - {left, right}
        if all(H.subgraph(remaining).degree(x) == 2 for x in remaining):
            frames.append((left, right, cycle_order(remaining)))
    print("frames", frames)

    for a, b, cycle in frames:
        print(f"FRAME {a}{b} cycle={cycle}")
        for omitted_index, omitted in enumerate(cycle):
            roots = cycle[omitted_index + 1 :] + cycle[:omitted_index]
            # The four roots are in cyclic order; crossing pairs are 0-2,1-3.
            # The omitted vertex lies on the frame arc roots[-1]--roots[0].
            outcomes = []
            for owner in (roots[-1], roots[0]):
                traces = [{root} for root in roots]
                traces[roots.index(owner)].add(omitted)
                duties_a = [i for i, trace in enumerate(traces) if not any(H.has_edge(a, x) for x in trace)]
                duties_b = [i for i, trace in enumerate(traces) if not any(H.has_edge(b, x) for x in trace)]
                closures = []
                if len(duties_a) == len(duties_b) == 1 and duties_a != duties_b:
                    for c in traces[duties_a[0]]:
                        for d in traces[duties_b[0]]:
                            left, right = {a, b}, {c, d}
                            if len(right) < 2 or not independent(right):
                                continue
                            ears = H.has_edge(a, d) and H.has_edge(b, c)
                            if ears and reflectable(left, right):
                                closures.append((c, d, tuple(sorted(right))))
                outcomes.append((owner, duties_a, duties_b, closures))
            print(" omitted", omitted, "cross", (roots[0], roots[2]), (roots[1], roots[3]), outcomes)


if __name__ == "__main__":
    main()
