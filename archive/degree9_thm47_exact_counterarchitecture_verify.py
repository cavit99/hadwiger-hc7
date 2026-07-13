#!/usr/bin/env python3
"""Width-five counterarchitecture for the later Theorem 4.7 adhesion."""

ORDER = (
    "q", "p1", "p2", "d1", "d2", "3", "4", "W", "1", "2",
    "v", "h", "6", "Q", "R5", "R0",
)
BOUNDARY = {"h", "1", "2", "6", "q", "d1", "d2"}


def build():
    vertices = (
        "v", "h", "1", "2", "3", "4", "6", "q", "d1", "d2",
        "W", "p1", "p2", "Q", "R5", "R0",
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
    for left in ("W", "Q"):
        for x in ("h", "1", "2"):
            add(left, x)
    for right in ("R5", "R0"):
        for x in ("h", "3", "4"):
            add(right, x)
    for x in ("6", "q", "d1", "d2"):
        add("W", x)
    # D={6,d1,d2}: 6 is the literal bottleneck to both right bags;
    # d1,d2 transfer the shore to two distinct actual Q-portals.
    for d, p in (("d1", "p1"), ("d2", "p2")):
        add(d, "6"); add(d, p); add(p, "Q")
    add("6", "R5"); add("6", "R0")
    add("q", "Q")
    add("Q", "R5"); add("Q", "R0"); add("R5", "R0")
    return vertices, edges


def components_after(vertices, edges, deleted):
    remaining = set(vertices) - set(deleted)
    adjacency = {x: set() for x in remaining}
    for edge in edges:
        x, y = edge
        if x in remaining and y in remaining:
            adjacency[x].add(y); adjacency[y].add(x)
    answer = []
    while remaining:
        root = next(iter(remaining)); seen = {root}; stack = [root]
        while stack:
            x = stack.pop()
            for y in adjacency[x] - seen:
                seen.add(y); stack.append(y)
        answer.append(seen); remaining -= seen
    return answer


def main():
    vertices, edges = build()
    assert {y for edge in edges if "W" in edge for y in edge - {"W"}} == BOUNDARY
    components = components_after(vertices, edges, BOUNDARY)
    assert {frozenset(c) for c in components} == {
        frozenset({"W"}),
        frozenset({"v", "3", "4", "p1", "p2", "Q", "R5", "R0"}),
    }
    far = next(c for c in components if "v" in c)
    for x in BOUNDARY:
        assert any(frozenset((x, y)) in edges for y in far)

    # After absorbing the d1,d2 components, the transferred shore has
    # the later exact boundary {h,1,2,6,q,p1,p2}.
    absorbed = {"W", "d1", "d2"}
    transferred_boundary = {
        y for edge in edges if edge & absorbed
        for y in edge - absorbed
    }
    assert transferred_boundary == {"h", "1", "2", "6", "q", "p1", "p2"}

    adjacency = {x: set() for x in vertices}
    for edge in edges:
        x, y = edge
        adjacency[x].add(y); adjacency[y].add(x)
    width = 0
    for x in ORDER:
        later = set(adjacency[x]); width = max(width, len(later))
        for a in later:
            for b in later:
                if a != b:
                    adjacency[a].add(b)
        for a in later:
            adjacency[a].remove(x)
        del adjacency[x]
    assert width <= 5
    print("PASS: exact boundary, full far shore, all old allocations, width", width)


if __name__ == "__main__":
    main()
