#!/usr/bin/env python3
"""Enumerate which terminal/w contacts repair a conservative Moser crossing."""

from __future__ import annotations

import itertools

from reserved_terminal_specific_web_quotient_verify import e, minor_model


MOSER = {
    e(x, y)
    for x, y in {
        (0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (1, 6),
        (2, 6), (3, 4), (3, 5), (4, 5), (5, 6),
    }
}
U = {0, 2, 4, 5, 6}
ORDER = (0, 2, 6, 5, 4)


def main() -> None:
    a, b, w, v, h, x, y = 1, 3, 7, 8, 9, 10, 11
    base = MOSER | {e(v, z) for z in range(7)}
    for crossed_terminal, opposite_terminal in ((a, b), (b, a)):
        side = "a" if crossed_terminal == a else "b"
        common = base | {e(h, z) for z in U | {w, opposite_terminal}}
        optional = (e(x, crossed_terminal), e(y, crossed_terminal), e(x, w), e(y, w))
        for i, r, j, s in itertools.combinations(range(5), 4):
            first, second = (ORDER[i], ORDER[j]), (ORDER[r], ORDER[s])
            graph = common | {e(x, y)} | {e(x, z) for z in first} | {e(y, z) for z in second}
            minimal = []
            for q in range(1, 5):
                for subset in itertools.combinations(optional, q):
                    if any(set(old).issubset(subset) for old in minimal):
                        continue
                    if minor_model(12, graph | set(subset), 7) is not None:
                        minimal.append(subset)
            print(side, first, second, "repairs", [tuple(optional.index(z) for z in ss) for ss in minimal])


if __name__ == "__main__":
    main()
