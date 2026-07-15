#!/usr/bin/env python3
"""Verify the minimal-forest noncritical-image counterarchitecture."""

from __future__ import annotations


def add_edge(adj: dict[str, set[str]], x: str, y: str) -> None:
    assert x != y
    adj[x].add(y)
    adj[y].add(x)


def induced(adj: dict[str, set[str]], keep: set[str]) -> dict[str, set[str]]:
    return {v: adj[v] & keep for v in keep}


def quotient(
    adj: dict[str, set[str]], blocks: list[set[str]], names: list[str]
) -> dict[str, set[str]]:
    assert len(blocks) == len(names)
    flat = set().union(*blocks)
    assert flat == set(adj)
    assert sum(map(len, blocks)) == len(flat)
    owner = {v: names[i] for i, block in enumerate(blocks) for v in block}
    out = {name: set() for name in names}
    for x in adj:
        for y in adj[x]:
            bx, by = owner[x], owner[y]
            if bx != by:
                out[bx].add(by)
    return out


def contract_pairs(
    adj: dict[str, set[str]], pairs: list[tuple[str, str, str]]
) -> dict[str, set[str]]:
    used: set[str] = set()
    blocks: list[set[str]] = []
    names: list[str] = []
    for x, y, z in pairs:
        assert x not in used and y not in used and y in adj[x]
        used.update((x, y))
        blocks.append({x, y})
        names.append(z)
    for v in sorted(set(adj) - used):
        blocks.append({v})
        names.append(v)
    return quotient(adj, blocks, names)


def k_colourable(adj: dict[str, set[str]], k: int) -> bool:
    vertices = list(adj)
    colour: dict[str, int] = {}

    def search() -> bool:
        if len(colour) == len(vertices):
            return True
        uncoloured = [v for v in vertices if v not in colour]
        v = max(
            uncoloured,
            key=lambda x: (
                len({colour[y] for y in adj[x] if y in colour}),
                len(adj[x]),
            ),
        )
        forbidden = {colour[y] for y in adj[v] if y in colour}
        for c in range(k):
            if c not in forbidden:
                colour[v] = c
                if search():
                    return True
                del colour[v]
        return False

    return search()


def chromatic_number(adj: dict[str, set[str]]) -> int:
    if not adj:
        return 0
    for k in range(1, len(adj) + 1):
        if k_colourable(adj, k):
            return k
    raise AssertionError("unreachable")


def is_clique(adj: dict[str, set[str]], vertices: set[str]) -> bool:
    return all(y in adj[x] for x in vertices for y in vertices if x != y)


def connected(adj: dict[str, set[str]], vertices: set[str]) -> bool:
    if not vertices:
        return False
    seen = {next(iter(vertices))}
    stack = list(seen)
    while stack:
        x = stack.pop()
        for y in (adj[x] & vertices) - seen:
            seen.add(y)
            stack.append(y)
    return seen == vertices


def build() -> tuple[dict[str, set[str]], set[str], set[str], set[str]]:
    s = {f"s{i}" for i in range(1, 5)} | {f"t{i}" for i in range(1, 5)}
    a_shore = {"a", "x", "y", "z"}
    b_shore = {"b"}
    vertices = s | a_shore | b_shore
    adj = {v: set() for v in vertices}

    s_clique = {f"s{i}" for i in range(1, 5)}
    for x in s_clique:
        for y in s_clique:
            if x < y:
                add_edge(adj, x, y)
    for x in s_clique:
        add_edge(adj, "a", x)

    add_edge(adj, "x", "y")
    add_edge(adj, "y", "z")
    add_edge(adj, "x", "z")
    q = {"a", "s1", "s2", "s3", "s4"}
    for x in ("x", "y", "z"):
        for y in q - {"s1"}:
            add_edge(adj, x, y)

    for j in range(1, 5):
        add_edge(adj, "a", f"t{j}")
    for x in s:
        add_edge(adj, "b", x)
    return adj, s, a_shore, b_shore


def main() -> None:
    g, s, a_shore, b_shore = build()
    assert len(g) == 13 and len(s) == 8
    assert connected(g, a_shore) and connected(g, b_shore)
    assert not any(y in g[x] for x in a_shore for y in b_shore)
    assert all(g[x] & a_shore and g[x] & b_shore for x in s)
    assert chromatic_number(induced(g, s)) == 4

    k7 = {"x", "y", "z", "a", "s2", "s3", "s4"}
    assert is_clique(g, k7)
    assert chromatic_number(g) == 7

    rest = sorted(set(g) - {"x", "y", "z"})
    k = quotient(g, [{"x", "y", "z"}] + [{v} for v in rest], ["w"] + rest)
    h1 = contract_pairs(g, [("x", "y", "xy")])
    h2 = contract_pairs(g, [("y", "z", "yz")])
    assert chromatic_number(k) == 5
    assert chromatic_number(h1) == 6
    assert chromatic_number(h2) == 6
    assert chromatic_number(induced(k, set(k) - {"w"})) == 5

    # F0 is contained in the displayed spanning tree of A.
    tree_edges = {frozenset(e) for e in [("x", "y"), ("y", "z"),
                                         ("a", "x")]}
    assert len(tree_edges) == len(a_shore) - 1
    tree_adj = {v: set() for v in a_shore}
    for edge in tree_edges:
        x, y = tuple(edge)
        assert y in g[x]
        add_edge(tree_adj, x, y)
    assert connected(tree_adj, a_shore)

    # Explicit failures of the full hypothetical-HC7 kernel.
    assert min(map(len, g.values())) == 2
    assert chromatic_number(induced(g, set(g) - {"b"})) == 7

    print("vertices=13 boundary=8 boundary_chi=4")
    print("shores=connected,anticomplete,S-full")
    print("chi(G)=7 chi(G/F0)=5 predecessor_chi=(6,6)")
    print("image_deletion=5 literal_K7=yes min_degree=2 minor_critical=no")


if __name__ == "__main__":
    main()
