#!/usr/bin/env python3
"""Dependency-free audit of the four mixed-contact K7 certificates.

This checks displays (5.5)--(5.8) in
hadwiger_degree9_two_carrier_capacity_exchange.md.  It is a certificate
checker, not evidence for the unproved exact-adhesion colour alignment.
"""


def check(vertices, edges, model):
    edges = {frozenset(e) for e in edges}
    assert len(model) == 7
    used = set()
    for bag in model:
        bag = set(bag)
        assert bag and not (used & bag) and bag <= set(vertices)
        used |= bag
        reached = {next(iter(bag))}
        while True:
            nxt = reached | {
                y for x in reached for y in bag
                if frozenset((x, y)) in edges
            }
            if nxt == reached:
                break
            reached = nxt
        assert reached == bag, ("disconnected", bag)
    for i in range(7):
        for j in range(i + 1, 7):
            assert any(
                frozenset((x, y)) in edges
                for x in model[i] for y in model[j]
            ), ("nonadjacent", i, j, model[i], model[j])


def common(add, *, dnode, lnode):
    vertices = ("v", "h", "1", "2", "3", "4",
                "Z", dnode, lnode, "X", "Y", "R5", "R0")
    edges = set()

    def edge(x, y):
        edges.add((x, y))

    for x in ("h", "1", "2", "3", "4", dnode, "R5"):
        edge("v", x)
    for x in ("1", "2", "3", "4", "Z", lnode, "R5", "R0"):
        edge("h", x)
    edge("1", "2"); edge("3", "4")
    for x in ("Z", dnode, lnode):
        edge(x, "1"); edge(x, "2")
    for x in ("R5", "R0"):
        edge(x, "3"); edge(x, "4")
    edge("R5", "R0")
    for x, y in add:
        edge(x, y)
    return vertices, edges


def active_q(r5_side, r0_side):
    add = [
        ("Z", "D"), ("Z", "X"), ("Z", "Y"), ("X", "Y"),
        ("D", "R5"), ("D", "R0"),
        (r5_side, "R5"), (r0_side, "R0"),
    ]
    return common(add, dnode="D", lnode="Y")


def active_d(r5_side, r0_side):
    add = [
        ("Z", "X"), ("Z", "Y"), ("X", "Y"), ("Z", "Q"),
        ("Y", "R5"), ("Q", "R5"), ("Q", "R0"),
        (r5_side, "R5"), (r0_side, "R0"),
    ]
    return common(add, dnode="Y", lnode="Q")


def main():
    # (5.5): X--R5, root side Y--R0.
    check(*active_q("X", "Y"), [
        ["h"], ["1"], ["2"], ["Z"], ["Y"],
        ["D", "R0"], ["v", "X", "R5"],
    ])
    # (5.6): root side Y--R5, X--R0.
    check(*active_q("Y", "X"), [
        ["h"], ["1"], ["2"], ["Z"], ["Y"],
        ["D", "R5"], ["v", "3", "X", "R0"],
    ])
    # (5.7): X--R5, 6-side Y--R0.
    check(*active_d("X", "Y"), [
        ["h", "3", "4"], ["v", "R5"], ["1"], ["2"],
        ["Z", "X"], ["Y", "R0"], ["Q"],
    ])
    # (5.8): 6-side Y--R5, X--R0.
    check(*active_d("Y", "X"), [
        ["h"], ["1"], ["2"], ["Z"], ["Q"],
        ["3", "Y", "R5"], ["v", "4", "X", "R0"],
    ])

    # (5.9): after a source-component absorption with a 3-contact.
    vertices, edges = common([
        ("Z", "3"), ("Z", "D"), ("Z", "Q"),
        ("D", "R5"), ("D", "R0"),
        ("Q", "R5"), ("Q", "R0"),
    ], dnode="D", lnode="Q")
    check(vertices, edges, [
        ["v"], ["h"], ["1"], ["2"], ["Z", "3"],
        ["D", "R5"], ["4", "Q", "R0"],
    ])

    print("PASS: four mixed-contact and cross-absorption K7 certificates")


if __name__ == "__main__":
    main()
