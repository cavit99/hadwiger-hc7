#!/usr/bin/env python3
"""Probe the literal-K4 crossed 1|2 cutvertex quotient for a K7 model."""

from itertools import combinations


V = ("v", "h", "1", "2", "5", "6", "z", "q", "L1", "L2", "D")


def norm(a, b):
    return tuple(sorted((a, b)))


def partitions(items, k):
    items = tuple(items)
    if not items:
        if k == 0:
            yield ()
        return
    first = items[0]
    for rest in partitions(items[1:], k - 1):
        yield ((first,),) + rest
    for rest in partitions(items[1:], k):
        for i in range(len(rest)):
            yield rest[:i] + ((first,) + rest[i],) + rest[i + 1 :]


def connected(block, edges):
    seen = {block[0]}
    while True:
        nxt = seen | {
            y for x in seen for y in block if norm(x, y) in edges
        }
        if nxt == seen:
            return len(seen) == len(block)
        seen = nxt


def adjacent(a, b, edges):
    return any(norm(x, y) in edges for x in a for y in b)


def find_model(edges):
    for size in range(7, len(V) + 1):
        for used in combinations(V, size):
            for model in partitions(used, 7):
                if all(connected(bag, edges) for bag in model) and all(
                    adjacent(a, b, edges) for a, b in combinations(model, 2)
                ):
                    return model
    return None


def main():
    S = ("v", "h", "1", "2", "5", "6", "z")
    edges = {norm(a, b) for a, b in (
        ("v", "h"), ("v", "1"), ("v", "2"),
        ("h", "1"), ("h", "2"), ("1", "2"),
        ("v", "5"), ("v", "6"), ("1", "6"),
        ("2", "6"), ("5", "6"),
        ("q", "L1"), ("q", "L2"),
    )}
    edges |= {norm("L1", s) for s in S if s != "1"}
    edges |= {norm("L2", s) for s in S if s != "2"}
    edges |= {norm("D", s) for s in S}
    model = find_model(edges)
    print("minimal quotient model:", model)


if __name__ == "__main__":
    main()
