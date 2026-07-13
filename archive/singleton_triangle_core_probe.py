#!/usr/bin/env python3
"""Probe the terminal three-vertex protected carrier core."""

from itertools import combinations


V = ("h", "1", "2", "r", "a", "b", "c", "D0", "D1")


def norm(x, y):
    return tuple(sorted((x, y)))


def partitions(items, k):
    items = tuple(items)
    if not items:
        if k == 0:
            yield ()
        return
    x = items[0]
    for rest in partitions(items[1:], k - 1):
        yield ((x,),) + rest
    for rest in partitions(items[1:], k):
        for i in range(len(rest)):
            yield rest[:i] + ((x,) + rest[i],) + rest[i + 1 :]


def connected(block, edges):
    seen = {block[0]}
    while True:
        nxt = seen | {y for x in seen for y in block if norm(x, y) in edges}
        if nxt == seen:
            return len(seen) == len(block)
        seen = nxt


def adjacent(a, b, edges):
    return any(norm(x, y) in edges for x in a for y in b)


def find_model(edges):
    for size in range(7, len(V) + 1):
        for used in combinations(V, size):
            for bags in partitions(used, 7):
                if all(connected(b, edges) for b in bags) and all(
                    adjacent(a, b, edges) for a, b in combinations(bags, 2)
                ):
                    return bags
    return None


def main():
    s = ("h", "1", "2", "r")
    w = ("a", "b", "c")
    base = {norm(x, y) for x, y in combinations(s, 2)}
    base |= {norm("a", "b"), norm("b", "c"), norm("a", "c")}
    base |= {norm("a", "h"), norm("b", "1"), norm("b", "2"), norm("c", "r")}
    base |= {norm(d, x) for d in ("D0", "D1") for x in s}
    failures = []
    for p0 in combinations(w, 2):
        for p1 in combinations(w, 2):
            edges = set(base)
            edges |= {norm("D0", x) for x in p0}
            edges |= {norm("D1", x) for x in p1}
            model = find_model(edges)
            if model is None:
                failures.append((p0, p1))
            else:
                print(p0, p1, model)
    print("failures", failures)


if __name__ == "__main__":
    main()
