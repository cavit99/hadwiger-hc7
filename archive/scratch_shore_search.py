#!/usr/bin/env python3
"""Small exhaustive/random search for incidence-free representatives."""

from itertools import combinations, product
from random import Random
import argparse


def has_rep(sets, n):
    """Return one incidence-free injective representative map, or None."""
    m = len(sets)
    allowed = [tuple(x for x in range(n) if x not in sets[i]) for i in range(m)]
    order = sorted(range(m), key=lambda i: len(allowed[i]))
    f = [-1] * m
    used = 0

    def rec(pos):
        nonlocal used
        if pos == m:
            return True
        i = order[pos]
        for x in allowed[i]:
            if used >> x & 1:
                continue
            good = True
            for p in range(pos):
                j = order[p]
                if x in sets[j] and f[j] in sets[i]:
                    good = False
                    break
            if not good:
                continue
            f[i] = x
            used ^= 1 << x
            if rec(pos + 1):
                return True
            used ^= 1 << x
            f[i] = -1
        return False

    return tuple(f) if rec(0) else None


def exhaustive(m, q, spare=None):
    n = m + (q if spare is None else spare)
    edges = [frozenset(c) for c in combinations(range(n), q)]
    first = frozenset(range(q))
    count = 0
    for tail in product(edges, repeat=m - 1):
        sets = (first,) + tail
        count += 1
        if has_rep(sets, n) is None:
            print("COUNTEREXAMPLE", m, q, n, [sorted(s) for s in sets], "after", count)
            return False
    print("NO COUNTEREXAMPLE", m, q, n, "families", count)
    return True


def random_search(m, q, trials, seed, spare=None):
    n = m + (q if spare is None else spare)
    rng = Random(seed)
    for t in range(1, trials + 1):
        sets = tuple(frozenset(rng.sample(range(n), q)) for _ in range(m))
        if has_rep(sets, n) is None:
            print("COUNTEREXAMPLE", m, q, n, [sorted(s) for s in sets], "trial", t)
            return False
    print("NO RANDOM COUNTEREXAMPLE", m, q, n, "trials", trials)
    return True


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("m", type=int)
    ap.add_argument("q", type=int)
    ap.add_argument("--trials", type=int, default=0)
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--spare", type=int)
    args = ap.parse_args()
    if args.trials:
        random_search(args.m, args.q, args.trials, args.seed, args.spare)
    else:
        exhaustive(args.m, args.q, args.spare)
