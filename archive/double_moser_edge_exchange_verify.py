#!/usr/bin/env python3
"""Dependency-free checks for hadwiger_double_moser_edge_exchange.md.

The script verifies only the finite displayed certificates:

* the width-five decomposition of the complete exclusive-cross skeleton;
* the dirty-hub extension of that decomposition;
* the r=3 and r=4 edge-deletion colourings and their five Kempe paths;
* the two seven-bag models in the three-cross portal certificate.

The Menger and Kempe arguments in the note are hand proofs, not searches.
"""

from collections import defaultdict, deque


def edge(first: str, second: str) -> frozenset[str]:
    return frozenset((first, second))


X = ("x1", "x2", "x3", "x4")
A = ("a", "b")
P = ("p", "q")


def double_moser_core(include_uv: bool = True) -> set[frozenset[str]]:
    edges: set[frozenset[str]] = set()
    if include_uv:
        edges.add(edge("u", "v"))
    for root in X:
        edges.add(edge("u", root))
        edges.add(edge("v", root))
    edges.update(
        {
            edge("u", "p"), edge("u", "q"),
            edge("v", "a"), edge("v", "b"),
            edge("x1", "x2"), edge("x3", "x4"),
            edge("a", "b"), edge("p", "q"),
            edge("a", "x1"), edge("a", "x2"),
            edge("b", "x3"), edge("b", "x4"),
            edge("q", "x1"), edge("q", "x2"),
            edge("p", "x3"), edge("p", "x4"),
        }
    )
    return edges


def connected(vertices: set[str], edges: set[frozenset[str]]) -> bool:
    if not vertices:
        return False
    reached = {next(iter(vertices))}
    while True:
        more = {
            y
            for x in reached
            for y in vertices - reached
            if edge(x, y) in edges
        }
        if not more:
            return reached == vertices
        reached.update(more)


def adjacent(
    first: set[str], second: set[str], edges: set[frozenset[str]]
) -> bool:
    return any(edge(x, y) in edges for x in first for y in second)


def verify_tree_decomposition(
    edges: set[frozenset[str]],
    bags: list[set[str]],
    tree_edges: list[tuple[int, int]],
    width: int,
) -> None:
    vertices = set().union(*edges)
    assert set().union(*bags) == vertices
    assert max(map(len, bags)) - 1 <= width
    assert len(tree_edges) == len(bags) - 1

    tree = defaultdict(set)
    for first, second in tree_edges:
        tree[first].add(second)
        tree[second].add(first)

    reached = {0}
    queue = deque([0])
    while queue:
        current = queue.popleft()
        for nxt in tree[current] - reached:
            reached.add(nxt)
            queue.append(nxt)
    assert len(reached) == len(bags)

    for graph_edge in edges:
        assert any(graph_edge <= bag for bag in bags)

    for vertex in vertices:
        containing = {index for index, bag in enumerate(bags) if vertex in bag}
        start = next(iter(containing))
        seen = {start}
        queue = deque([start])
        while queue:
            current = queue.popleft()
            for nxt in tree[current] & containing - seen:
                seen.add(nxt)
                queue.append(nxt)
        assert seen == containing


def verify_width_five_obstructions() -> None:
    edges = double_moser_core()
    edges.update(edge(left, right) for left in A for right in P)

    bags = [
        {"a", "b", "p", "q", "u", "v"},
        {"x4", "b", "p", "u", "v"},
        {"x3", "x4", "b", "p", "u", "v"},
        {"x2", "a", "q", "u", "v"},
        {"x1", "x2", "a", "q", "u", "v"},
    ]
    tree_edges = [(2, 1), (1, 0), (0, 3), (3, 4)]
    verify_tree_decomposition(edges, bags, tree_edges, width=5)

    hub_edges = set(edges)
    hub_edges.update(edge("h", terminal) for terminal in A + P)
    hub_bags = bags + [{"a", "b", "p", "q", "h"}]
    verify_tree_decomposition(
        hub_edges, hub_bags, tree_edges + [(0, 5)], width=5
    )


def verify_colouring(
    edges: set[frozenset[str]], colour: dict[str, int]
) -> None:
    assert set().union(*edges) <= colour.keys()
    for first, second in map(tuple, edges):
        assert colour[first] != colour[second]


def verify_alternating_path(path: list[str], colour: dict[str, int]) -> None:
    used = {colour[vertex] for vertex in path}
    assert len(used) == 2
    assert all(colour[x] != colour[y] for x, y in zip(path, path[1:]))


def verify_edge_witness_examples() -> None:
    # Rainbow X: the only nontrivial chain is u-q-h-a-v.
    r4_edges = double_moser_core(include_uv=False)
    r4_edges.update({edge("q", "h"), edge("h", "a")})
    r4_colour = {
        "u": 0, "v": 0, "h": 0,
        "x1": 1, "x2": 2, "x3": 3, "x4": 4,
        "b": 1, "a": 5, "p": 2, "q": 5,
    }
    verify_colouring(r4_edges, r4_colour)
    for root in X:
        verify_alternating_path(["u", root, "v"], r4_colour)
    verify_alternating_path(["u", "q", "h", "a", "v"], r4_colour)

    # Three-colour X: two clean exclusive chains.
    r3_edges = double_moser_core(include_uv=False)
    r3_edges.update(
        {
            edge("p", "h4"), edge("h4", "b"),
            edge("q", "h5"), edge("h5", "a"),
        }
    )
    r3_colour = {
        "u": 0, "v": 0, "h4": 0, "h5": 0,
        "x1": 1, "x2": 2, "x3": 1, "x4": 3,
        "b": 4, "p": 4, "a": 5, "q": 5,
    }
    verify_colouring(r3_edges, r3_colour)
    for root in ("x1", "x2", "x4"):
        verify_alternating_path(["u", root, "v"], r3_colour)
    verify_alternating_path(["u", "p", "h4", "b", "v"], r3_colour)
    verify_alternating_path(["u", "q", "h5", "a", "v"], r3_colour)


def verify_model(
    edges: set[frozenset[str]], bags: list[set[str]]
) -> None:
    used: set[str] = set()
    for bag in bags:
        assert used.isdisjoint(bag)
        used.update(bag)
        assert connected(bag, edges)
    assert all(
        adjacent(bags[first], bags[second], edges)
        for first in range(len(bags))
        for second in range(first)
    )


def verify_three_cross_certificates() -> None:
    # rho_a=2, rho_b>=1, with Cb seeing x2.
    first = double_moser_core()
    first.update(
        {
            edge("Ca", "Cb"),
            edge("Ca", "v"), edge("Ca", "x1"), edge("Ca", "x2"),
            edge("Ca", "x3"), edge("Ca", "x4"), edge("Ca", "p"),
            edge("Cb", "v"), edge("Cb", "x3"), edge("Cb", "x4"),
            edge("Cb", "x2"), edge("Cb", "q"),
        }
    )
    verify_model(
        first,
        [
            {"Ca"}, {"Cb"}, {"p", "q"}, {"x3"}, {"x4"},
            {"v", "x1"}, {"u", "x2"},
        ],
    )

    # rho_b=2, rho_a>=1, with Ca seeing x4.
    second = double_moser_core()
    second.update(
        {
            edge("Ca", "Cb"),
            edge("Ca", "v"), edge("Ca", "x1"), edge("Ca", "x2"),
            edge("Ca", "x4"), edge("Ca", "p"),
            edge("Cb", "v"), edge("Cb", "x3"), edge("Cb", "x4"),
            edge("Cb", "x1"), edge("Cb", "x2"), edge("Cb", "q"),
        }
    )
    verify_model(
        second,
        [
            {"Ca"}, {"Cb"}, {"p", "q"}, {"x1"}, {"x2"},
            {"v", "x3"}, {"u", "x4"},
        ],
    )


def main() -> None:
    verify_width_five_obstructions()
    verify_edge_witness_examples()
    verify_three_cross_certificates()
    print("double-Moser edge exchange certificates verified")


if __name__ == "__main__":
    main()
