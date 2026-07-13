#!/usr/bin/env python3
"""Exact check of both sharp five-edge cores with a two-vertex shore.

The graph consists of the seven-vertex boundary S=C5 join K2, a shore
edge xy, and a contracted opposite full shore d.  Both x and y have at
least six neighbours in S (the consequence of delta(G)>=7 when xy is a
whole component).  The helper d is adjacent to all of S and to neither
x nor y.  For every possible missing S-neighbour of x and y, we search
for an exact K7 branch-set model.
"""

import itertools
C = tuple(range(5))
R = (5, 6)
S = C + R
X, Y, D = 7, 8, 9
V = tuple(range(10))


def boundary_edges(kind):
    if kind == "C5+2K1":
        missing = {
            tuple(sorted((i, (i + 2) % 5))) for i in C
        }
    elif kind == "K3+2K2":
        missing = {(0, 1), (0, 2), (1, 2), (3, 4), (5, 6)}
    else:
        raise AssertionError(kind)
    return {
        edge for edge in itertools.combinations(S, 2) if edge not in missing
    }


def fixed_edges(kind):
    edges = set()
    edges.update(boundary_edges(kind))
    edges.add((X, Y))
    edges.update((s, D) for s in S)
    return {tuple(sorted(e)) for e in edges}


def k_minor_model(edges, k=7):
    adjacency = [0] * len(V)
    for i, j in edges:
        adjacency[i] |= 1 << j
        adjacency[j] |= 1 << i
    neighbour_union = [0] * (1 << len(V))
    connected = []
    for mask in range(1, 1 << len(V)):
        low = mask & -mask
        i = low.bit_length() - 1
        neighbour_union[mask] = neighbour_union[mask ^ low] | adjacency[i]
        reached = low
        while True:
            expanded = reached | (neighbour_union[reached] & mask)
            if expanded == reached:
                break
            reached = expanded
        if reached == mask:
            connected.append(mask)
    connected.sort(key=lambda m: (m.bit_count(), m))

    def adjacent(a, b):
        return not (a & b) and bool(neighbour_union[a] & b)

    def rec(chosen, candidates, used):
        if len(chosen) == k:
            return chosen
        needed = k - len(chosen)
        if len(candidates) < needed:
            return None
        for pos, a in enumerate(candidates):
            if a & used:
                continue
            nxt = [
                b for b in candidates[pos + 1:]
                if not b & (used | a) and adjacent(a, b)
            ]
            if len(nxt) >= needed - 1:
                result = rec(chosen + [a], nxt, used | a)
                if result:
                    return result
        return None

    return rec([], connected, 0)


def as_sets(model):
    return [tuple(i for i in V if mask >> i & 1) for mask in model]


def main():
    choices = (None,) + S
    for kind in ("C5+2K1", "K3+2K2"):
        base = fixed_edges(kind)
        witnesses = {}
        failures = []
        for miss_x, miss_y in itertools.product(choices, repeat=2):
            edges = set(base)
            edges.update((min(X, s), max(X, s)) for s in S if s != miss_x)
            edges.update((min(Y, s), max(Y, s)) for s in S if s != miss_y)
            model = k_minor_model(edges)
            if model is None:
                failures.append((miss_x, miss_y))
            else:
                witnesses[(miss_x, miss_y)] = as_sets(model)

        print(kind, "cases", len(choices) ** 2,
              "K7", len(witnesses), "failures", failures)


if __name__ == "__main__":
    main()
