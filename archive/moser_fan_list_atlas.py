#!/usr/bin/env python3
"""Exact list atlas for a removable outer fan in the Moser web."""

from __future__ import annotations

import itertools
from collections import Counter

from moser_safe_transition_state_probe import NONEDGES, kind, matching
from pentagram_critical_web_fullprofile_probe import PRESENT, TRIPLES
from wheel_safe_transition_search import A, W, ABSTRACT_TO_PHYSICAL, boundary_colours


PALETTE = frozenset(range(6))


def rows():
    out = []
    for pair in PRESENT:
        out.append(("P" + "".join(map(str, sorted(pair))), pair, frozenset({A, W})))
    for triple, _shield in TRIPLES.items():
        for extras in (frozenset({A}), frozenset({W}), frozenset({A, W})):
            out.append(("T" + "".join(map(str, sorted(triple))) + "/" +
                        "".join("a" if x == A else "w" for x in sorted(extras)),
                        triple, extras))
    return out


def main() -> None:
    residual = [
        es for q in (2, 3) for es in itertools.combinations(NONEDGES, q)
        if matching(es) and kind(es) != "decorated-T trace"
    ]
    atlas = Counter()
    hard = []
    for es in residual:
        for wc in range(6):
            colours = boundary_colours(es, wc)
            for hc in range(6):
                lists = []
                for name, profile, extras in rows():
                    physical = {ABSTRACT_TO_PHYSICAL[i] for i in profile}
                    forbidden = {hc, *(colours[x] for x in physical | set(extras))}
                    lists.append((name, PALETTE - forbidden))
                signature = tuple(sorted(Counter(len(ls) for _, ls in lists).items()))
                atlas[signature] += 1
                if min(len(ls) for _, ls in lists) < 2:
                    hard.append((es, wc, hc, lists))
    print("cells", len(residual) * 6 * 6, "hard", len(hard), "signatures")
    for sig, count in sorted(atlas.items()):
        print(count, sig)
    print("sample hard rows")
    for es, wc, hc, lists in hard[:20]:
        print(es, "w", wc, "h", hc,
              [(name, tuple(sorted(ls))) for name, ls in lists if len(ls) < 2])


if __name__ == "__main__":
    main()
