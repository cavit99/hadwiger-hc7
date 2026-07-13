#!/usr/bin/env python3
"""Probe the three-lobe exact-state claim on a seven-vertex boundary.

Each of three anticomplete T-lobes contacts a set A_i of at least four
boundary labels and their union is the whole boundary.  The question is
whether the boundary graph admits a proper 3-colouring assigning colour i
only inside A_i.  A colouring gives the exact three-carrier state.
"""

from itertools import product

import networkx as nx


ALL = (1 << 7) - 1
LARGE = [m for m in range(1 << 7) if m.bit_count() >= 4]


def colourable(edge_masks: list[int], a: tuple[int, int, int]) -> bool:
    lists = []
    for v in range(7):
        opts = tuple(i for i in range(3) if a[i] & (1 << v))
        if not opts:
            return False
        lists.append(opts)
    order = sorted(range(7), key=lambda v: len(lists[v]))
    colour = [-1] * 7

    def rec(pos: int) -> bool:
        if pos == 7:
            return True
        v = order[pos]
        for c in lists[v]:
            if all(colour[u] != c for u in range(7) if edge_masks[v] & (1 << u)):
                colour[v] = c
                if rec(pos + 1):
                    return True
                colour[v] = -1
        return False

    return rec(0)


def main() -> None:
    graphs = []
    for g0 in nx.graph_atlas_g():
        if len(g0) != 7:
            continue
        g = nx.convert_node_labels_to_integers(g0)
        if any(c == 3 for c in map(len, nx.enumerate_all_cliques(g))):
            continue
        # A live (1,3) boundary has no admissible one-block state I|Q,
        # where I is independent and Q is a clique (necessarily |Q|<=2).
        has_one_block = False
        for qmask in range(1 << 7):
            q = [v for v in range(7) if qmask & (1 << v)]
            i = [v for v in range(7) if not qmask & (1 << v)]
            if len(i) < 2:
                continue
            if all(g.has_edge(x, y) for x in q for y in q if x < y) and not g.subgraph(i).edges:
                has_one_block = True
                break
        if has_one_block:
            continue
        edge_masks = [sum(1 << u for u in g.neighbors(v)) for v in range(7)]
        graphs.append((g, edge_masks))
    tested = 0
    for g, edge_masks in graphs:
        for a0 in LARGE:
            for a1 in LARGE:
                need = ALL ^ (a0 | a1)
                for a2 in LARGE:
                    if need & ~a2:
                        continue
                    tested += 1
                    a = (a0, a1, a2)
                    if not colourable(edge_masks, a):
                        print("COUNTEREXAMPLE")
                        print("edges=" + repr(sorted(tuple(sorted(e)) for e in g.edges())))
                        print("A=" + repr(tuple([v for v in range(7) if m & (1 << v)] for m in a)))
                        print(f"tested={tested}")
                        return
    print(f"NO_COUNTEREXAMPLE graphs={len(graphs)} tested={tested}")


if __name__ == "__main__":
    main()
