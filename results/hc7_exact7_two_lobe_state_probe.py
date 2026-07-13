#!/usr/bin/env python3
"""Falsify/test a boundary-only two-lobe state principle.

Enumerates labelled triangle-free graphs H on S=[7] with no admissible
one-block partition, and contact sets A,B of size at least four.  It asks
whether the anticomplete lobe carriers with contacts A,B can fund an
admissible two-block state via Lemma 3.1 of the thin-shore exchange.

This deliberately ignores gate portals.  A counterexample therefore
shows that lobe contact existence alone cannot close the c=2 gate cell.
"""

from itertools import combinations

N = 7
ALL = (1 << N) - 1
PAIRS = [(i, j) for i in range(N) for j in range(i + 1, N)]


def is_clique(mask, adj):
    vs = [i for i in range(N) if mask >> i & 1]
    return all(adj[u] >> v & 1 for u, v in combinations(vs, 2))


def is_independent(mask, adj):
    return all((adj[v] & mask) == 0 for v in range(N) if mask >> v & 1)


def no_one_block(adj):
    for q in range(1 << N):
        i = ALL ^ q
        if i.bit_count() >= 2 and is_independent(i, adj) and is_clique(q, adj):
            return False
    return True


def has_two_block_state(adj, A, B, carriers_adjacent=False):
    # Ordered I1 for A, I2 for B; Q is the remainder.
    sub = A
    while sub:
        I1 = sub
        sub = (sub - 1) & A
        if I1.bit_count() < 2 or not is_independent(I1, adj):
            continue
        available = B & ~I1
        sub2 = available
        while sub2:
            I2 = sub2
            sub2 = (sub2 - 1) & available
            if I2.bit_count() < 2 or not is_independent(I2, adj):
                continue
            Q = ALL ^ (I1 | I2)
            if not is_clique(Q, adj):
                continue
            # If the carriers are anticomplete, a boundary edge must supply
            # adjacency after the independent blocks are absorbed.
            if (not carriers_adjacent and
                    not any(adj[v] & I2 for v in range(N) if I1 >> v & 1)):
                continue
            ok = True
            for q in range(N):
                if not (Q >> q & 1):
                    continue
                if not (A >> q & 1) and not (adj[q] & I1):
                    ok = False
                if not (B >> q & 1) and not (adj[q] & I2):
                    ok = False
            if ok:
                return (I1, I2, Q)
    return None


def main():
    contact_sets = [m for m in range(1 << N) if m.bit_count() >= 4]
    triangle_masks = []
    for tri in combinations(range(N), 3):
        em = 0
        for uv in combinations(tri, 2):
            em |= 1 << PAIRS.index(tuple(sorted(uv)))
        triangle_masks.append(em)

    checked_h = checked_pairs = 0
    for emask in range(1 << len(PAIRS)):
        if any((emask & tm) == tm for tm in triangle_masks):
            continue
        adj = [0] * N
        for k, (u, v) in enumerate(PAIRS):
            if emask >> k & 1:
                adj[u] |= 1 << v
                adj[v] |= 1 << u
        if not no_one_block(adj):
            continue
        checked_h += 1
        for A in contact_sets:
            for B in contact_sets:
                checked_pairs += 1
                if (A | B) != ALL:
                    continue
                if has_two_block_state(adj, A, B, carriers_adjacent=True) is None:
                    print("COUNTEREXAMPLE")
                    print("edges", [PAIRS[k] for k in range(len(PAIRS)) if emask >> k & 1])
                    print("A", [v for v in range(N) if A >> v & 1])
                    print("B", [v for v in range(N) if B >> v & 1])
                    print("checked_h", checked_h, "checked_pairs", checked_pairs)
                    return
    print("NO COUNTEREXAMPLE", checked_h, checked_pairs)


if __name__ == "__main__":
    main()
