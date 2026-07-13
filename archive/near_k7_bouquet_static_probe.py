#!/usr/bin/env python3
"""Exact static K7 probe for the Hall-deficient near-K7 bouquets.

The six literal labels induce K6-ab-ac.  In the two-pole experiment,
three independent lobe vertices see the same two poles and all labels
except their named missed row.  No label--pole or pole--pole edges are
assumed.  A connected torso route between the poles is represented by an
optional extra vertex adjacent to both poles; this is deliberately kept
outside the first, weakest quotient.
"""

from __future__ import annotations

from itertools import product


def partitions(n: int, k: int = 7):
    labels = [0] * n

    def rec(pos: int, maximum: int):
        if pos == n:
            if maximum + 1 == k:
                blocks = [0] * k
                for vertex, label in enumerate(labels):
                    blocks[label] |= 1 << vertex
                yield tuple(blocks)
            return
        if k - (maximum + 1) > n - pos:
            return
        for label in range(min(maximum + 1, k - 1) + 1):
            labels[pos] = label
            yield from rec(pos + 1, max(maximum, label))

    yield from rec(1, 0)


def connected(mask: int, adj: tuple[int, ...]) -> bool:
    reached = mask & -mask
    while True:
        nbrs = 0
        scan = reached
        while scan:
            bit = scan & -scan
            scan ^= bit
            nbrs |= adj[bit.bit_length() - 1]
        expanded = reached | (nbrs & mask)
        if expanded == reached:
            return reached == mask
        reached = expanded


def find_model(adj: tuple[int, ...]):
    n = len(adj)
    conn = [False] * (1 << n)
    nbr = [0] * (1 << n)
    for mask in range(1, 1 << n):
        low = mask & -mask
        v = low.bit_length() - 1
        nbr[mask] = nbr[mask ^ low] | adj[v]
        conn[mask] = connected(mask, adj)
    for blocks in partitions(n):
        if all(conn[b] for b in blocks) and all(
            nbr[blocks[i]] & blocks[j] for i in range(7) for j in range(i)
        ):
            return blocks
    return None


def graph(missed: tuple[int, int, int], pole_edge: bool, route: bool):
    # labels a,b,c,q1,q2,q3; missing ab,ac
    n = 12 if route else 11
    adj = [0] * n

    def add(u: int, v: int):
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    for u in range(6):
        for v in range(u + 1, 6):
            if (u, v) not in {(0, 1), (0, 2)}:
                add(u, v)
    p, q = 6, 7
    if pole_edge:
        add(p, q)
    for i, miss in enumerate(missed):
        d = 8 + i
        add(d, p)
        add(d, q)
        for label in range(6):
            if label != miss:
                add(d, label)
    if route:
        add(11, p)
        add(11, q)
    return tuple(adj)


def names(blocks, route):
    nn = ["a", "b", "c", "q1", "q2", "q3", "p", "q", "D1", "D2", "D3"]
    if route:
        nn.append("r")
    return " | ".join(
        "{" + ",".join(nn[v] for v in range(len(nn)) if block >> v & 1) + "}"
        for block in blocks
    )


def main():
    for pole_edge, route in ((False, False), (True, False), (False, True)):
        negative = []
        witness = None
        for missed in product(range(6), repeat=3):
            model = find_model(graph(missed, pole_edge, route))
            if model is None:
                negative.append(missed)
            elif witness is None:
                witness = (missed, names(model, route))
        print("pole_edge", pole_edge, "route", route, "negative", len(negative))
        print("sample_negative", negative[:20])
        print("sample_positive", witness)


if __name__ == "__main__":
    main()
