#!/usr/bin/env python3
"""Audit the static terminal root-lobe counterarchitecture.

The explicit width-five completion proves that the retained rooted-model
and portal data alone do not force the terminal two-root swap.
"""

ORDER = (
    "p1", "p2", "s", "S", "3", "4", "Z", "1", "2",
    "D", "J", "R0", "R5", "h", "v",
)


def build():
    vertices = ORDER
    edges = set()

    def add(x, y):
        edges.add(frozenset((x, y)))

    # Pure-Moser boundary after 6 and 5 have been retained in D and R5.
    for x in ("h", "1", "2", "3", "4", "D", "R5"):
        add("v", x)
    for x, y in (
        ("h", "1"), ("h", "2"), ("h", "3"), ("h", "4"),
        ("1", "2"), ("1", "D"), ("2", "D"), ("3", "4"),
    ):
        add(x, y)

    # Exterior roots: Z,J are left; R5,R0 are right.
    for left in ("Z", "J"):
        for x in ("h", "1", "2"):
            add(left, x)
    for right in ("R5", "R0"):
        for x in ("h", "3", "4"):
            add(right, x)

    # Terminal lobe and its two distinct active portal endpoints.
    for x in ("p1", "p2"):
        add("Z", x); add("J", x)
    add("J", "s"); add("s", "S")

    # Inactive outer carrier and all six old K4-model adjacencies.
    add("Z", "D")
    add("D", "R5"); add("D", "R0")
    add("S", "R5"); add("S", "R0")
    add("R5", "R0")
    return vertices, edges


def width_certificate(vertices, edges):
    adjacency = {x: set() for x in vertices}
    for edge in edges:
        x, y = edge
        adjacency[x].add(y); adjacency[y].add(x)
    width = 0
    for x in ORDER:
        later = set(adjacency[x])
        width = max(width, len(later))
        assert len(later) <= 5, (x, later)
        for a in later:
            for b in later - {a}:
                adjacency[a].add(b)
        for a in later:
            adjacency[a].remove(x)
        del adjacency[x]
    return width


def check_model(vertices, edges, model):
    used = set()
    for bag in model:
        bag = set(bag)
        assert bag and not (bag & used)
        used |= bag
        reached = {next(iter(bag))}
        while True:
            grown = reached | {
                y for x in reached for y in bag
                if frozenset((x, y)) in edges
            }
            if grown == reached:
                break
            reached = grown
        assert reached == bag, ("disconnected", bag)
    for i in range(len(model)):
        for j in range(i + 1, len(model)):
            assert any(
                frozenset((x, y)) in edges
                for x in model[i] for y in model[j]
            ), ("nonadjacent", i, j)


def audit_swap_certificate():
    vertices = (
        "v", "h", "1", "2", "3", "E", "T", "J", "S",
        "D", "R5", "R0",
    )
    edges = set()

    def add(x, y):
        edges.add(frozenset((x, y)))

    for x in ("h", "1", "2", "3", "D", "R5"):
        add("v", x)
    add("h", "1"); add("h", "2"); add("1", "2")
    for left in ("E", "J"):
        for x in ("h", "1", "2"):
            add(left, x)
    for x in ("1", "2"):
        add("D", x)
    for right in ("R5", "R0"):
        add(right, "h"); add(right, "3")
    for x, y in (
        ("E", "T"), ("E", "D"), ("E", "S"),
        ("T", "J"), ("T", "D"), ("J", "S"),
        ("D", "R5"), ("S", "R0"), ("R5", "R0"),
    ):
        add(x, y)
    check_model(vertices, edges, [
        ["h"], ["1"], ["2"], ["E"], ["T", "J"],
        ["D", "R5"], ["v", "3", "S", "R0"],
    ])


def audit_direct_cross_certificates():
    vertices = (
        "v", "h", "1", "2", "3", "4", "Z", "J", "S",
        "D", "R5", "R0",
    )

    def graph(extra):
        edges = set()

        def add(x, y):
            edges.add(frozenset((x, y)))

        for x in ("h", "1", "2", "3", "4", "D", "R5"):
            add("v", x)
        add("h", "1"); add("h", "2"); add("h", "3"); add("h", "4")
        add("1", "2"); add("3", "4")
        for left in ("Z", "J"):
            add(left, "h"); add(left, "1"); add(left, "2")
        add("D", "1"); add("D", "2")
        for right in ("R5", "R0"):
            add(right, "h"); add(right, "3"); add(right, "4")
        for x, y in (
            ("Z", "J"), ("Z", "D"), ("Z", "S"),
            ("J", "S"), ("D", "R5"), ("S", "R0"),
            ("R5", "R0"),
        ) + tuple(extra):
            add(x, y)
        return edges

    jd_edges = graph((("J", "D"),))
    check_model(vertices, jd_edges, [
        ["h"], ["1"], ["2"], ["Z"], ["J"],
        ["D", "R5"], ["v", "3", "S", "R0"],
    ])
    j3_edges = graph((("J", "3"),))
    check_model(vertices, j3_edges, [
        ["h"], ["1"], ["2"], ["Z"], ["J", "3"],
        ["D", "R5"], ["v", "4", "S", "R0"],
    ])


def audit_nested_split_certificate():
    vertices = (
        "v", "h", "1", "2", "3", "E", "T", "S",
        "D", "R5", "R0",
    )
    edges = set()

    def add(x, y):
        edges.add(frozenset((x, y)))

    for x in ("h", "1", "2", "3", "D", "R5"):
        add("v", x)
    add("h", "1"); add("h", "2"); add("1", "2")
    for root_side in ("E", "T"):
        add(root_side, "h"); add(root_side, "1"); add(root_side, "2")
    add("D", "1"); add("D", "2")
    for right in ("R5", "R0"):
        add(right, "h"); add(right, "3")
    for x, y in (
        ("E", "T"), ("E", "D"), ("E", "S"),
        ("T", "D"), ("T", "S"), ("D", "R5"),
        ("S", "R0"), ("R5", "R0"),
    ):
        add(x, y)
    check_model(vertices, edges, [
        ["h"], ["1"], ["2"], ["E"], ["T"],
        ["D", "R5"], ["v", "3", "S", "R0"],
    ])


def main():
    vertices, edges = build()

    def adjacent(x, y):
        return frozenset((x, y)) in edges

    # Two distinct active Q-portals, both in the root-bearing s-lobe.
    assert adjacent("Z", "p1") and adjacent("Z", "p2")
    assert adjacent("J", "p1") and adjacent("J", "p2")
    assert not adjacent("J", "R5") and not adjacent("J", "R0")
    assert adjacent("J", "s") and adjacent("s", "S")

    # The four spanning bags L6=Z+D, L0=J+p1+p2+s+S, R5, R0
    # retain all six pairwise adjacencies.
    assert adjacent("Z", "D")
    assert adjacent("Z", "p1")
    assert adjacent("D", "R5") and adjacent("D", "R0")
    assert adjacent("S", "R5") and adjacent("S", "R0")
    assert adjacent("R5", "R0")

    width = width_certificate(vertices, edges)
    audit_swap_certificate()
    audit_direct_cross_certificates()
    audit_nested_split_certificate()
    print("PASS: terminal lobe, two active portals, all old allocations, width", width)
    print("PASS: terminal two-root-swap K7 certificate")
    print("PASS: direct J-D and J-3 terminal-cross K7 certificates")
    print("PASS: nested double-root split K7 certificate")


if __name__ == "__main__":
    main()
