#!/usr/bin/env python3
"""Exact quotient for the two symmetric same-bag gate alternatives."""

from pure_moser_degree9_model_occupancy_probe import has_k7


ELIMINATION_ORDER = (
    "U", "1", "2", "V", "3", "4", "v", "h", "D", "C", "L0", "R0",
)


def build(extra=()):
    vertices = (
        "v","h","1","2","3","4",
        "U","D","V","C","L0","R0",
    )
    edges = set()
    def add(a,b):
        edges.add(frozenset((a,b)))
    for x in ("h","1","2","3","4","D","C"):
        add("v",x)
    for x in ("1","2","3","4","U","L0","V","R0"):
        add("h",x)
    add("1","2"); add("3","4")
    for x in ("U","D","L0"):
        add(x,"1"); add(x,"2")
    for x in ("V","C","R0"):
        add(x,"3"); add(x,"4")

    # Two gates, outer edge, and same-bag strict portal allocations.
    for a,b in (
        ("U","D"),("V","C"),("D","C"),
        ("U","L0"),("V","R0"),
        ("D","R0"),("C","L0"),("L0","R0"),
    ):
        add(a,b)
    for a,b in extra:
        add(a,b)
    return vertices,edges


def verify_width_five_completion(vertices, edges):
    """Verify the explicit width-five elimination certificate.

    Filling the later neighbours of each eliminated vertex produces a
    chordal supergraph.  An elimination width at most five therefore
    proves treewidth at most five and rules out a K7 minor independently
    of the exhaustive branch-set search.
    """
    assert set(vertices) == set(ELIMINATION_ORDER)
    adjacency = {x: set() for x in vertices}
    for edge in edges:
        x, y = edge
        adjacency[x].add(y)
        adjacency[y].add(x)
    bags = []
    for x in ELIMINATION_ORDER:
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


if __name__ == "__main__":
    base = build()
    bags = verify_width_five_completion(*base)
    print("base",has_k7(*base))
    print("elimination_width", max(len(bag) - 1 for _, bag in bags))
    print("crossed_terminal_paths", ("U", "D", "C"), ("V", "C", "D"))
    print("direct_crosses",has_k7(*build((("U","C"),("V","D")))))
