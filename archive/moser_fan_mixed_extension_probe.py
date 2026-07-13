#!/usr/bin/env python3
"""Can mixed forced ordinary fan chains occur in a full crossless portal word?"""

from __future__ import annotations

import itertools

from moser_fan_list_atlas import PALETTE, rows
from moser_safe_transition_state_probe import NONEDGES, kind, matching
from wheel_safe_transition_search import (
    ABSTRACT_TO_PHYSICAL, PRESENT_PROFILES, TRIPLE_PROFILES,
    boundary_colours, circular_crossless,
)


def exact(word):
    if set().union(*word) != set(range(5)):
        return False
    for i, triple in enumerate(TRIPLE_PROFILES):
        if triple in word and sum((i + 3) % 5 in p for p in word) != 1:
            return False
    return circular_crossless(word)


def extendable(chain):
    alphabet = tuple(frozenset({i}) for i in range(5)) + PRESENT_PROFILES + TRIPLE_PROFILES
    for q in range(0, 6):
        for outside in itertools.product(alphabet, repeat=q):
            if exact(chain + outside):
                return outside
    return None


def main() -> None:
    residual = [
        es for q in (2, 3) for es in itertools.combinations(NONEDGES, q)
        if matching(es) and kind(es) != "decorated-T trace"
    ]
    ordinary = rows()[:5]
    candidates = set()
    for es in residual:
        for wc in range(6):
            colours = boundary_colours(es, wc)
            for hc in range(6):
                lists = []
                for _name, profile, extras in ordinary:
                    physical = {ABSTRACT_TO_PHYSICAL[i] for i in profile}
                    lists.append(PALETTE - {hc, *(colours[x] for x in physical | set(extras))})
                for start, ls in enumerate(lists):
                    if len(ls) != 1:
                        continue
                    c0 = next(iter(ls))
                    stack = [(c0, (start,), frozenset({c0}))]
                    while stack:
                        force, word, seen = stack.pop()
                        for j, lj in enumerate(lists):
                            nxt = lj - {force}
                            new_word = word + (j,)
                            if not nxt:
                                profiles = tuple(ordinary[i][1] for i in new_word)
                                if circular_crossless(profiles):
                                    candidates.add(profiles)
                            elif len(nxt) == 1:
                                colour = next(iter(nxt))
                                if colour not in seen:
                                    stack.append((colour, new_word, seen | {colour}))
    print("forced chains", len(candidates))
    feasible = []
    for chain in sorted(candidates, key=lambda w: (len(w), tuple(map(tuple, w)))):
        outside = extendable(chain)
        print(tuple(map(tuple, chain)), "outside", None if outside is None else tuple(map(tuple, outside)))
        if outside is not None:
            feasible.append(chain)
    print("full-word feasible", len(feasible))


if __name__ == "__main__":
    main()
