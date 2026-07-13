#!/usr/bin/env python3
"""Search K2 join icosahedron for a spanning K7^vee model with singleton K4 core."""

from itertools import product

import networkx as nx


def icosahedron():
    g = nx.Graph()
    t, b = "t", "b"
    us = [f"u{i}" for i in range(5)]
    ws = [f"w{i}" for i in range(5)]
    g.add_nodes_from([t, b, *us, *ws, "p", "q"])
    for i in range(5):
        g.add_edge(t, us[i])
        g.add_edge(b, ws[i])
        g.add_edge(us[i], us[(i + 1) % 5])
        g.add_edge(ws[i], ws[(i + 1) % 5])
        g.add_edge(us[i], ws[i])
        g.add_edge(us[i], ws[(i - 1) % 5])
    for x in [t, b, *us, *ws]:
        g.add_edge("p", x)
        g.add_edge("q", x)
    g.add_edge("p", "q")
    return g


def adjacent(g, x, y):
    return any(g.has_edge(a, b) for a in x for b in y)


def is_two_connected(g, z):
    return len(z) >= 3 and nx.is_biconnected(g.subgraph(z))


def main():
    g = icosahedron()
    old = [v for v in g if v not in {"p", "q"}]
    first = None
    strong = None
    for uv in g.subgraph(old).edges():
        core = {"p", "q", *uv}
        rem = [v for v in g if v not in core]
        for word in product(range(3), repeat=len(rem)):
            bags = [{rem[i] for i, z in enumerate(word) if z == j} for j in range(3)]
            if any(not z for z in bags):
                continue
            if any(not nx.is_connected(g.subgraph(z)) for z in bags):
                continue
            if any(not all(any(g.has_edge(x, q) for x in z) for q in core) for z in bags):
                continue
            # Relabel so bags[1] and bags[2] are the required B-C adjacent pair.
            for a, b, c in [(0, 1, 2), (1, 0, 2), (2, 0, 1)]:
                if adjacent(g, bags[b], bags[c]):
                    row = (core, bags[a], bags[b], bags[c])
                    first = first or row
                    if is_two_connected(g, bags[b]) and is_two_connected(g, bags[c]):
                        strong = row
                        break
            if strong:
                break
        if strong:
            break
    for name, row in [("first", first), ("both-cross-bags-2connected", strong)]:
        print(name)
        if row is None:
            print("NONE")
            continue
        core, aa, bb, cc = row
        print("core", sorted(core))
        print("A", sorted(aa))
        print("B", sorted(bb))
        print("C", sorted(cc))
        print("cross", next((x, y) for x in bb for y in cc if g.has_edge(x, y)))


if __name__ == "__main__":
    main()
