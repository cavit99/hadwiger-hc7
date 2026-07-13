#!/usr/bin/env python3
"""Dependency-free audit of the simultaneous-star extension.

After the two contractions, only the colours on
zu,zv,a,b,p,q matter for extending the colouring back to u,v.  This
exhausts all 6^6 assignments satisfying the forced quotient edges and
checks that the two residual lists have distinct representatives.
"""

from itertools import product


PALETTE = frozenset(range(6))


def main() -> None:
    admissible = 0
    for alpha, beta, a, b, p, q in product(range(6), repeat=6):
        # zu-zv; each old/new outer vertex sees both contracted stars;
        # and ab,pq are literal edges.
        if alpha == beta:
            continue
        if a in (alpha, beta) or b in (alpha, beta) or a == b:
            continue
        if p in (alpha, beta) or q in (alpha, beta) or p == q:
            continue
        admissible += 1
        list_u = PALETTE - {alpha, beta, p, q}
        list_v = PALETTE - {alpha, beta, a, b}
        assert len(list_u) == len(list_v) == 2
        assert any(cu != cv for cu in list_u for cv in list_v)

    # 6*5 choices for alpha,beta; then 4*3 independently for each outer
    # edge.
    assert admissible == 6 * 5 * (4 * 3) ** 2
    print(f"verified all {admissible} admissible contracted-core colourings")


if __name__ == "__main__":
    main()
