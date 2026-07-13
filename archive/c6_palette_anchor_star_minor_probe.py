"""Exact minor probe for the quotient forced by palette-distinct gate anchors.

The vertex ``a`` represents the connected centre of the rooted star inside
one shore, ``h`` the opposite full shore, and ``q`` the second gate.  Only
edges forced by the C6+K1 boundary and the chosen star anchors are used.
"""

from itertools import combinations

import networkx as nx


RIM = tuple(range(6))
Z = 6


def has_k_minor(g, k=7):
    # A model can be made spanning in a connected graph by absorbing every
    # unused component into an incident bag.  Enumerate the set partitions
    # into exactly k branch bags; S(10,7)=5,880 here.
    vs = list(g)
    blocks = [[vs[0]]]

    def rec(pos):
        if pos == len(vs):
            if len(blocks) != k:
                return None
            sets = [frozenset(b) for b in blocks]
            if not all(nx.is_connected(g.subgraph(b)) for b in sets):
                return None
            if not all(
                any(g.has_edge(x, y) for x in sets[i] for y in sets[j])
                for i in range(k) for j in range(i + 1, k)
            ):
                return None
            return tuple(sets)
        if len(blocks) > k or len(blocks) + len(vs) - pos < k:
            return None
        v = vs[pos]
        for b in blocks:
            b.append(v)
            ans = rec(pos + 1)
            if ans:
                return ans
            b.pop()
        if len(blocks) < k:
            blocks.append([v])
            ans = rec(pos + 1)
            if ans:
                return ans
            blocks.pop()
        return None

    return rec(1)


def host(anchors):
    g = nx.Graph()
    g.add_nodes_from((*RIM, Z, "a", "h", "q"))
    # Boundary complement is C6 plus isolated z.
    for u, v in combinations(RIM, 2):
        if (u - v) % 6 not in (1, 5):
            g.add_edge(u, v)
    for u in RIM:
        g.add_edge(Z, u)
    # Opposite full shore.
    for u in (*RIM, Z):
        g.add_edge("h", u)
    # Palette-star quotient.
    for u in anchors:
        g.add_edge("a", u)
    return g


def main():
    gate = (0, 2, 3, 5, Z, "q")
    for r in range(1, 7):
        positive = []
        negative = []
        for anchors in combinations(gate, r):
            model = has_k_minor(host(anchors))
            (positive if model else negative).append((anchors, model))
        print("r", r, "positive", len(positive), "negative", len(negative))
        if negative:
            print(" negative anchors", [x for x, _ in negative])
        if positive and r <= 4:
            print(" sample", positive[0])


if __name__ == "__main__":
    main()
