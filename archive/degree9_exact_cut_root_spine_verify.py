#!/usr/bin/env python3
"""Certificate checks for the exact-cut root-spine quotient."""

from pure_moser_degree9_model_occupancy_probe import has_k7


ORDER = ("q", "R0", "3", "4", "R5", "v", "h", "1", "2", "6", "Z")
SHARP_ORDER = (
    "q", "r1", "r2", "r3", "R0", "3", "4", "R5", "v",
    "h", "1", "2", "6", "K", "E",
)


def build(q_extra=()):
    vertices = ("v", "q", "h", "1", "2", "3", "4", "6", "Z", "R5", "R0")
    edges = set()

    def add(x, y):
        edges.add(frozenset((x, y)))

    for x in ("h", "1", "2", "3", "4", "6", "R5"):
        add("v", x)
    for x, y in (
        ("h", "1"), ("h", "2"), ("h", "3"), ("h", "4"),
        ("1", "2"), ("1", "6"), ("2", "6"), ("3", "4"),
    ):
        add(x, y)
    add("6", "R5")
    add("R5", "R0")
    add("q", "R0")
    for right in ("R5", "R0"):
        for x in ("h", "3", "4"):
            add(right, x)
    for x in ("q", "h", "1", "2", "3", "4", "6"):
        add("Z", x)
    for x in q_extra:
        add("q", x)
    return vertices, edges


def verify_width_five(vertices, edges):
    assert set(vertices) == set(ORDER)
    adjacency = {x: set() for x in vertices}
    for edge in edges:
        x, y = edge
        adjacency[x].add(y)
        adjacency[y].add(x)
    bags = []
    for x in ORDER:
        later = set(adjacency[x])
        bags.append((x, tuple(sorted(later | {x}))))
        assert len(later) <= 5
        for a in later:
            for b in later:
                if a != b:
                    adjacency[a].add(b)
        for a in later:
            adjacency[a].remove(x)
        del adjacency[x]
    return bags


def build_sharp_root_exchange(extra=()):
    """Two explicit left roots and a tight three-portal root lobe."""
    vertices = (
        "v", "q", "h", "1", "2", "3", "4", "6", "K", "E",
        "r1", "r2", "r3", "R5", "R0",
    )
    edges = set()

    def add(x, y):
        edges.add(frozenset((x, y)))

    for x in ("h", "1", "2", "3", "4", "6", "R5"):
        add("v", x)
    for x, y in (
        ("h", "1"), ("h", "2"), ("h", "3"), ("h", "4"),
        ("1", "2"), ("1", "6"), ("2", "6"), ("3", "4"),
    ):
        add(x, y)
    add("6", "R5"); add("R5", "R0"); add("q", "R0"); add("q", "E")
    for root in ("K", "E"):
        for x in ("h", "1", "2"):
            add(root, x)
    add("K", "6")
    add("E", "3"); add("E", "4")
    for r in ("r1", "r2", "r3"):
        add("K", r); add("E", r)
    for right in ("R5", "R0"):
        for x in ("h", "3", "4"):
            add(right, x)
    for x, y in extra:
        add(x, y)
    return vertices, edges


def build_full_carrier_frame():
    vertices, edges = build_sharp_root_exchange()
    vertices = tuple(vertices) + ("Df", "Lf")
    edges = set(edges)

    def add(x, y):
        edges.add(frozenset((x, y)))

    # Replace the deliberately omitted old-model allocations by H-side
    # carrier pieces: 6--Df--R0 and q--Lf--{R5,R0}.
    add("6", "Df"); add("Df", "R0")
    add("q", "Lf"); add("Lf", "R5"); add("Lf", "R0")
    return vertices, edges


def verify_order(vertices, edges, order):
    assert set(vertices) == set(order)
    adjacency = {x: set() for x in vertices}
    for edge in edges:
        x, y = edge
        adjacency[x].add(y); adjacency[y].add(x)
    width = 0
    for x in order:
        later = set(adjacency[x])
        width = max(width, len(later))
        for a in later:
            for b in later:
                if a != b:
                    adjacency[a].add(b)
        for a in later:
            adjacency[a].remove(x)
        del adjacency[x]
    assert width <= 5
    return width


def check_model(vertices, edges, model):
    edges = set(edges)
    assert len(model) == 7
    used = set()
    for raw in model:
        bag = set(raw)
        assert bag and not bag & used
        used |= bag
        reached = {next(iter(bag))}
        while True:
            new = reached | {
                y for x in reached for y in bag
                if frozenset((x, y)) in edges
            }
            if new == reached:
                break
            reached = new
        assert reached == bag
    for i in range(7):
        for j in range(i + 1, 7):
            assert any(
                frozenset((x, y)) in edges
                for x in model[i] for y in model[j]
            ), (i, j)


def main():
    base = build()
    bags = verify_width_five(*base)
    assert not has_k7(*base)
    print("base_no_K7 width", max(len(bag) - 1 for _, bag in bags))

    for i in ("1", "2"):
        graph = build((i,))
        assert has_k7(*graph)
        check_model(*graph, [
            ["v"], ["h"], ["3"], ["4"], ["R5"],
            ["6", "Z"], ["q", i, "R0"],
        ])
        print("q" + i, "explicit_K7")

    sharp = build_sharp_root_exchange()
    print("sharp_root_spine_no_K7 width", verify_order(*sharp, SHARP_ORDER))
    repaired = build_sharp_root_exchange((("K", "3"),))
    check_model(*repaired, [
        ["v"], ["h"], ["1"], ["2"], ["K", "3"],
        ["6", "R5"], ["4", "E", "q", "R0"],
    ])
    print("root_exchange_K3 explicit_K7")

    full = build_full_carrier_frame()
    check_model(*full, [
        ["v"], ["h"], ["3"], ["4"], ["R5"],
        ["6", "Df", "R0"], ["q", "1", "E", "Lf"],
    ])
    print("full_carrier_exact_cut explicit_K7")


if __name__ == "__main__":
    main()
