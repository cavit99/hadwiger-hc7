#!/usr/bin/env python3
"""Verify the sharp flexibility example for the seven retained views.

The graph is K7^vee with one private leaf added to each logical vertex; a
logical branch bag consists of the core vertex and its leaf.  Every retained
view is proper.  Each neutral retained view admits both repeated missing-pair
states independently, so arbitrarily selected view colourings have no parity
relation.  Exact search certifies that the graph is K7-minor-free.
"""

from __future__ import annotations

from functools import lru_cache
from itertools import combinations, product

import networkx as nx


LABELS = ("A", "B", "C", "U1", "U2", "U3", "U4")
NEUTRALS = LABELS[3:]


def vertices(label: str) -> tuple[str, str]:
    return (f"{label}0", f"{label}1")


def graph() -> nx.Graph:
    g = nx.Graph()
    for label in LABELS:
        g.add_edge(*vertices(label))
    # All quotient contacts use the core endpoints.  The second endpoint of
    # every branch bag is a private leaf.
    for first, second in combinations(LABELS, 2):
        if required(first, second):
            g.add_edge(f"{first}0", f"{second}0")
    return g


def required(first: str, second: str) -> bool:
    return frozenset((first, second)) not in {
        frozenset(("A", "B")),
        frozenset(("A", "C")),
    }


def view(g: nx.Graph, retained: str) -> tuple[nx.Graph, dict[str, str]]:
    """Contract every bag other than ``retained`` to a named singleton."""
    h = nx.Graph()
    image: dict[str, str] = {}
    for label in LABELS:
        if label == retained:
            for v in vertices(label):
                image[v] = v
                h.add_node(v)
        else:
            image[vertices(label)[0]] = label
            image[vertices(label)[1]] = label
            h.add_node(label)
    for x, y in g.edges:
        ix, iy = image[x], image[y]
        if ix != iy:
            h.add_edge(ix, iy)
    return h, image


def equality_type(colour: dict[str, int], retained: str) -> str:
    boundary = [x for x in LABELS if x != retained]
    equal = {
        frozenset((x, y))
        for x, y in combinations(boundary, 2)
        if colour[x] == colour[y]
    }
    if not equal:
        return "R"
    if equal == {frozenset(("A", "B"))}:
        return "AB"
    if equal == {frozenset(("A", "C"))}:
        return "AC"
    return "other"


def state_set(h: nx.Graph, retained: str) -> set[str]:
    order = sorted(h, key=lambda x: (-h.degree[x], x))
    colours: dict[str, int] = {}
    states: set[str] = set()

    def search(i: int, used: int) -> None:
        if i == len(order):
            states.add(equality_type(colours, retained))
            return
        v = order[i]
        forbidden = {colours[w] for w in h[v] if w in colours}
        # Colour symmetry: introduce at most the next new colour.
        for c in range(min(used + 1, 6)):
            if c in forbidden:
                continue
            colours[v] = c
            search(i + 1, max(used, c + 1))
            del colours[v]

    search(0, 0)
    return states


def exact_treewidth(g: nx.Graph) -> tuple[int, tuple[str, ...]]:
    """Exact elimination-order treewidth by memoization; graph has 14 nodes."""
    names = tuple(g.nodes)
    n = len(names)
    index = {v: i for i, v in enumerate(names)}
    base = [0] * n
    for x, y in g.edges:
        i, j = index[x], index[y]
        base[i] |= 1 << j
        base[j] |= 1 << i

    @lru_cache(maxsize=None)
    def solve(mask: int, rows: tuple[int, ...]) -> tuple[int, tuple[int, ...]]:
        if not mask:
            return 0, ()
        best = n
        best_order: tuple[int, ...] = ()
        bits = mask
        while bits:
            bit = bits & -bits
            bits ^= bit
            v = bit.bit_length() - 1
            neigh = rows[v] & (mask ^ bit)
            width_here = neigh.bit_count()
            if width_here >= best:
                continue
            new_rows = list(rows)
            ns = [i for i in range(n) if neigh >> i & 1]
            for i, j in combinations(ns, 2):
                new_rows[i] |= 1 << j
                new_rows[j] |= 1 << i
            rest_width, rest_order = solve(mask ^ bit, tuple(new_rows))
            width = max(width_here, rest_width)
            if width < best:
                best = width
                best_order = (v,) + rest_order
        return best, best_order

    width, order = solve((1 << n) - 1, tuple(base))
    return width, tuple(names[i] for i in order)


def has_k7_minor(g: nx.Graph) -> tuple[tuple[tuple[str, ...], ...] | None, int]:
    """Exact branch-set partition search after deleting pendant vertices."""
    core = g.copy()
    while True:
        leaves = [v for v in core if core.degree[v] <= 1]
        if not leaves:
            break
        core.remove_nodes_from(leaves)
    names = tuple(core.nodes)
    n = len(names)
    adj = [0] * n
    for x, y in core.edges:
        i, j = names.index(x), names.index(y)
        adj[i] |= 1 << j
        adj[j] |= 1 << i

    @lru_cache(maxsize=None)
    def connected(mask: int) -> bool:
        reached = mask & -mask
        while True:
            expanded = reached
            bits = reached
            while bits:
                bit = bits & -bits
                bits ^= bit
                expanded |= adj[bit.bit_length() - 1] & mask
            if expanded == reached:
                return reached == mask
            reached = expanded

    def partitions(items: tuple[int, ...], k: int):
        blocks: list[list[int]] = []

        def rec(pos: int):
            if pos == len(items):
                if len(blocks) == k:
                    yield tuple(tuple(block) for block in blocks)
                return
            left = len(items) - pos
            if len(blocks) + left < k:
                return
            value = items[pos]
            for block in blocks:
                block.append(value)
                yield from rec(pos + 1)
                block.pop()
            if len(blocks) < k:
                blocks.append([value])
                yield from rec(pos + 1)
                blocks.pop()

        yield from rec(0)

    checked = 0
    for size in range(7, n + 1):
        for support in combinations(range(n), size):
            for blocks in partitions(support, 7):
                checked += 1
                masks = tuple(sum(1 << v for v in block) for block in blocks)
                if not all(connected(mask) for mask in masks):
                    continue
                if all(
                    any(adj[v] & masks[j] for v in blocks[i])
                    for i in range(7)
                    for j in range(i)
                ):
                    return (
                        tuple(tuple(names[v] for v in block) for block in blocks),
                        checked,
                    )
    return None, checked


def main() -> None:
    g = graph()
    for first, second in combinations(LABELS, 2):
        contacts = any(
            g.has_edge(x, y)
            for x, y in product(vertices(first), vertices(second))
        )
        assert contacts == required(first, second), (first, second, contacts)

    expected = {
        "A": {"R"},
        "B": {"R", "AC"},
        "C": {"R", "AB"},
        "U1": {"AB", "AC"},
        "U2": {"AB", "AC"},
        "U3": {"AB", "AC"},
        "U4": {"AB", "AC"},
    }
    actual = {}
    for retained in LABELS:
        h, _ = view(g, retained)
        actual[retained] = state_set(h, retained)
    assert actual == expected, actual

    width, order = exact_treewidth(g)
    model, checked = has_k7_minor(g)
    assert model is None, model
    assert width <= 5, (width, order)
    print("state sets:", actual)
    print("treewidth:", width)
    print("elimination order:", order)
    print("K7 branch-set partitions checked:", checked)


if __name__ == "__main__":
    main()
