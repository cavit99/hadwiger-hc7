#!/usr/bin/env python3
"""Replay the maximally terminal/w-portalized crossing quotients."""

from __future__ import annotations

import itertools

from reserved_terminal_specific_web_quotient_verify import e, minor_model


def main() -> None:
    moser = {
        e(x, y) for x, y in {
            (0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (1, 6),
            (2, 6), (3, 4), (3, 5), (4, 5), (5, 6),
        }
    }
    u = {0, 2, 4, 5, 6}
    a, b, w, v, h, x, y = 1, 3, 7, 8, 9, 10, 11
    order = (0, 2, 6, 5, 4)
    base = moser | {e(v, z) for z in range(7)}
    # It suffices to check crossings on the a-side.  The automorphism
    # (1 3)(2 4)(5 6) gives the b-side cases.
    common = base | {e(h, z) for z in u | {w, b}}
    checked = 0
    for i, r, j, s in itertools.combinations(range(5), 4):
        first, second = (order[i], order[j]), (order[r], order[s])
        graph = (
            common | {e(x, y)}
            | {e(x, z) for z in set(first) | {a, w}}
            | {e(y, z) for z in set(second) | {a, w}}
        )
        assert minor_model(12, graph, 6) is not None
        assert minor_model(12, graph, 7) is None
        checked += 1
        print(first, second, "eta=6")
    assert checked == 5
    print("verified five maximally portalized crossings; the other five are symmetric")


if __name__ == "__main__":
    main()
