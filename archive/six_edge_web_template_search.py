#!/usr/bin/env python3
"""Search generalized-web closure templates for six-edge quotient exceptions."""

import itertools

import c5_core_k2_shore_verify as exact10


S = tuple(range(7))
X, Y, H = exact10.X, exact10.Y, exact10.D
PAIRS = set(itertools.combinations(S, 2))


EXCEPTIONS = (
    ((0, 1), (0, 6), (1, 5), (2, 3), (2, 4), (3, 4)),
    ((0, 5), (0, 6), (1, 2), (1, 6), (2, 5), (3, 4)),
    ((0, 1), (0, 5), (1, 5), (2, 3), (2, 4), (3, 4)),
    ((0, 4), (0, 5), (1, 3), (1, 5), (2, 3), (2, 4)),
    ((0, 2), (0, 6), (1, 5), (2, 3), (2, 4), (3, 4)),
    ((0, 3), (0, 6), (1, 3), (1, 5), (2, 3), (2, 4)),
    ((0, 3), (0, 4), (0, 5), (1, 2), (1, 4), (2, 3)),
    ((0, 1), (0, 3), (0, 5), (1, 2), (1, 4), (2, 3)),
    ((0, 1), (0, 3), (0, 4), (1, 2), (1, 4), (2, 3)),
    ((0, 1), (0, 2), (0, 5), (1, 2), (1, 4), (2, 3)),
    ((0, 1), (0, 2), (0, 4), (1, 2), (1, 3), (2, 3)),
    ((0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)),
)


def bipartite(vertices, edges):
    vertices = set(vertices)
    colour = {}
    adjacency = {v: set() for v in vertices}
    for a, b in edges:
        if a in vertices and b in vertices:
            adjacency[a].add(b)
            adjacency[b].add(a)
    for root in vertices:
        if root in colour:
            continue
        colour[root] = 0
        stack = [root]
        while stack:
            x = stack.pop()
            for y in adjacency[x]:
                if y not in colour:
                    colour[y] = 1 - colour[x]
                    stack.append(y)
                elif colour[y] == colour[x]:
                    return False
    return True


def quotient_edges(boundary, first_pair, second_pair):
    edges = set(boundary)
    edges.add((X, Y))
    edges.update((s, H) for s in S)
    edges.update(tuple(sorted((X, s))) for s in first_pair)
    edges.update(tuple(sorted((Y, s))) for s in second_pair)
    return {tuple(sorted(edge)) for edge in edges}


def canonical_cycle_orders(subset):
    first = min(subset)
    rest = tuple(v for v in subset if v != first)
    for tail in itertools.permutations(rest):
        order = (first,) + tail
        if order[1] > order[-1]:
            continue
        yield order


def cycle_subgraph(order, boundary):
    order = tuple(order)
    expected = {
        tuple(sorted((order[i], order[(i + 1) % len(order)])))
        for i in range(len(order))
    }
    actual = {edge for edge in boundary
              if edge[0] in order and edge[1] in order}
    # Missing frame edges can be added by the web completion and then
    # discarded; only nonconsecutive boundary chords obstruct disk gluing.
    return actual <= expected


def crossing_safe(order, boundary):
    for i, r, j, s in itertools.combinations(range(len(order)), 4):
        first = (order[i], order[j])
        second = (order[r], order[s])
        if exact10.k_minor_model(
                quotient_edges(boundary, first, second)) is None:
            return False, (first, second)
    return True, None


def main():
    for index, missing_tuple in enumerate(EXCEPTIONS):
        missing = {tuple(sorted(edge)) for edge in missing_tuple}
        boundary = PAIRS - missing
        candidates = []
        near = []
        for size in range(4, 8):
            for subset in itertools.combinations(S, size):
                omitted = set(S) - set(subset)
                if not bipartite(omitted, boundary):
                    continue
                for order in canonical_cycle_orders(subset):
                    if not cycle_subgraph(order, boundary):
                        continue
                    safe, bad = crossing_safe(order, boundary)
                    if safe:
                        candidates.append((order, tuple(sorted(omitted))))
                    else:
                        near.append((order, tuple(sorted(omitted)), bad))
        print(index, "templates", candidates[:20], "count", len(candidates))
        if not candidates:
            print(" near", near[:10], "count", len(near))


if __name__ == "__main__":
    main()
