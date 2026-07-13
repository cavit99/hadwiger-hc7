#!/usr/bin/env python3
"""Exact K7-minor probe for the bare defect-one tight-Hall quotient.

This deliberately records only consequences proved by Corollary 4.4:
the C6-complement plus universal z boundary, an opposite full shore H,
a component K behind the eight-gate, and a common portal x for a missing
cycle edge i-k.  No unproved pole/boundary contacts are inserted.
"""

def graph(alpha: int, i: int = 0, k: int = 1) -> list[int]:
    # 0,...,5 are cycle labels, 6 is z, 7=x, 8=K, 9=H.
    g = [0] * 10

    def edge(a: int, b: int) -> None:
        g[a] |= 1 << b
        g[b] |= 1 << a
    for a in range(6):
        for b in range(a + 1, 6):
            if (a - b) % 6 not in (1, 5):
                edge(a, b)
    for a in range(6):
        edge(6, a)
    # Old opposite shore.
    for a in range(7):
        edge(9, a)
    # x is the common i,k portal and K is the selected component of C-x.
    edge(7, i)
    edge(7, k)
    edge(7, 8)
    # K sees exactly the old labels not excluded by the defect alpha or k.
    for a in set(range(7)) - {alpha, k}:
        edge(8, a)
    return g


def k_clique_minor_model(adjacency: list[int], target: int = 7):
    order = len(adjacency)
    neighbours = [0] * (1 << order)
    connected = []
    for mask in range(1, 1 << order):
        bit = mask & -mask
        neighbours[mask] = neighbours[mask ^ bit] | adjacency[bit.bit_length() - 1]
        reached = bit
        while True:
            expanded = reached | (neighbours[reached] & mask)
            if expanded == reached:
                break
            reached = expanded
        if reached == mask:
            connected.append(mask)
    connected.sort(key=lambda mask: (mask.bit_count(), mask))

    def recurse(chosen: list[int], candidates: list[int], used: int):
        if len(chosen) == target:
            return tuple(chosen)
        needed = target - len(chosen)
        for position, bag in enumerate(candidates):
            if bag & used:
                continue
            following = [
                other for other in candidates[position + 1:]
                if not other & (used | bag) and neighbours[bag] & other
            ]
            if len(following) >= needed - 1:
                answer = recurse(chosen + [bag], following, used | bag)
                if answer is not None:
                    return answer
        return None

    return recurse([], connected, 0)


def elimination_order(adjacency: list[int], width: int):
    """Return an elimination order whose chordal completion has width <= width."""
    n = len(adjacency)

    def rec(adj, alive, order):
        if not alive:
            return order
        candidates = sorted(
            (v for v in range(n) if alive >> v & 1),
            key=lambda v: (adj[v] & alive).bit_count(),
        )
        for v in candidates:
            nb = adj[v] & alive & ~(1 << v)
            if nb.bit_count() > width:
                continue
            new_adj = adj.copy()
            bits = nb
            while bits:
                bit = bits & -bits
                bits ^= bit
                u = bit.bit_length() - 1
                new_adj[u] |= nb & ~(1 << u)
            answer = rec(new_adj, alive & ~(1 << v), order + [v])
            if answer is not None:
                return answer
        return None

    return rec(adjacency.copy(), (1 << n) - 1, [])


def main() -> None:
    for alpha in (2, 3, 4, 5, 6):
        g = graph(alpha)
        model = k_clique_minor_model(g, 7)
        decoded = None if model is None else [
            ["x" if v == 7 else "K" if v == 8 else "H" if v == 9
             else "z" if v == 6 else f"c{v}" for v in range(10) if bag >> v & 1]
            for bag in model
        ]
        print("alpha", "z" if alpha == 6 else f"c{alpha}", "K7", decoded)
        if model is None:
            print(" width-5 elimination", elimination_order(g, 5))
            repairs = []
            certificates = {}
            for u in range(10):
                for v in range(u + 1, 10):
                    if g[u] >> v & 1:
                        continue
                    h = g.copy()
                    h[u] |= 1 << v
                    h[v] |= 1 << u
                    repaired_model = k_clique_minor_model(h, 7)
                    if repaired_model is not None:
                        repairs.append((u, v))
                        certificates[(u, v)] = repaired_model
            print(" single-edge repairs", repairs)
            target = (2, 7) if alpha == 3 else (5, 7)
            if target in certificates:
                print(" target repair model", [
                    ["x" if v == 7 else "K" if v == 8 else "H" if v == 9
                     else "z" if v == 6 else f"c{v}"
                     for v in range(10) if bag >> v & 1]
                    for bag in certificates[target]
                ])

    # Exact two-path split rows from Lemma 3.1 of the accompanying note.
    # P=8, Q=10.  No other P/Q-to-boundary incidences are inserted.
    for alpha, outward, qlabels in ((3, 2, (4, 5)), (4, 5, (2, 3))):
        adj = graph(alpha) + [0]
        for u in range(10):
            if adj[8] >> u & 1:
                adj[u] &= ~(1 << 8)
        adj[8] = 0

        def add(a, b):
            adj[a] |= 1 << b
            adj[b] |= 1 << a

        add(8, 10)
        add(8, 7)
        add(8, outward)
        for label in qlabels:
            add(10, label)
        model = k_clique_minor_model(adj, 7)
        assert model is not None
        print("hard defect", alpha, "two-path split", [
            ["P" if v == 8 else "Q" if v == 10 else "x" if v == 7
             else "H" if v == 9 else "z" if v == 6 else f"c{v}"
             for v in range(11) if bag >> v & 1]
            for bag in model
        ])


if __name__ == "__main__":
    main()
