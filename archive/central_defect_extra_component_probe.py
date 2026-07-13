#!/usr/bin/env python3
"""Test whether one extra component closes a central portal-swap defect row."""

from itertools import combinations


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
        nxt = seen | {y for x in seen for y in block if norm(x, y) in edges}
        if nxt == seen:
            return len(seen) == len(block)
        seen = nxt


def adjacent(a, b, edges):
    return any(norm(x, y) in edges for x in a for y in b)


def find_model(vertices, edges):
    for size in range(7, len(vertices) + 1):
        for used in combinations(vertices, size):
            for model in partitions(used, 7):
                if all(connected(bag, edges) for bag in model) and all(
                    adjacent(a, b, edges) for a, b in combinations(model, 2)
                ):
                    return model
    return None


def find_near_model(vertices, edges):
    for size in range(7, len(vertices) + 1):
        for used in combinations(vertices, size):
            for model in partitions(used, 7):
                if not all(connected(bag, edges) for bag in model):
                    continue
                missing = [
                    (a, b) for a, b in combinations(model, 2)
                    if not adjacent(a, b, edges)
                ]
                if len(missing) <= 1:
                    return model, missing
    return None


def graph(d, defect):
    S = ("h", "1", "2", "5", "6", "y", "z")
    boundary = S + ("v",)
    U = tuple(x for x in S if x != d)
    vertices = boundary + ("R", "D", "E")
    edges = {norm(a, b) for a, b in (
        ("h", "1"), ("h", "2"), ("1", "2"),
        ("1", "6"), ("2", "6"), ("5", "6"),
        ("v", "h"), ("v", "1"), ("v", "2"),
        ("v", "5"), ("v", "6"),
    )}
    edges |= {norm("R", x) for x in U + ("v",)}
    edges |= {norm("D", x) for x in U + (d,)}
    edges |= {norm("E", x) for x in boundary if x != defect}
    return vertices, edges


def main():
    for d in ("1", "2", "6"):
        failures = []
        for defect in (None, "h", "1", "2", "5", "6", "y", "z"):
            if defect == "v":
                continue
            vertices, edges = graph(d, defect)
            model = find_model(vertices, edges)
            if model is None:
                failures.append(defect)
            else:
                print("d", d, "defect", defect, "model", model)
        print("d", d, "failures", failures)

    for d in ("1", "2", "6"):
        vertices, edges = graph(d, None)
        vertices = tuple(x for x in vertices if x != "E")
        edges = {e for e in edges if "E" not in e}
        print("portal-swap K7- d", d, find_near_model(vertices, edges))


if __name__ == "__main__":
    main()
