#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = ["networkx>=3.4"]
# ///
"""Classify shortest ordinary-profile list obstructions in removable fans."""

from __future__ import annotations

import itertools
from collections import Counter, deque

from moser_fan_list_atlas import PALETTE, rows
from moser_safe_transition_state_probe import NONEDGES, kind, matching
from wheel_safe_transition_search import ABSTRACT_TO_PHYSICAL, boundary_colours


def main() -> None:
    residual = [
        es for q in (2, 3) for es in itertools.combinations(NONEDGES, q)
        if matching(es) and kind(es) != "decorated-T trace"
    ]
    ordinary = rows()[:5]
    types = Counter()
    examples = {}
    no_obstruction = 0
    for es in residual:
        for wc in range(6):
            colours = boundary_colours(es, wc)
            for hc in range(6):
                lists = []
                for name, profile, extras in ordinary:
                    physical = {ABSTRACT_TO_PHYSICAL[i] for i in profile}
                    forbidden = {hc, *(colours[x] for x in physical | set(extras))}
                    lists.append(PALETTE - forbidden)
                queue = deque()
                seen = set()
                for i, ls in enumerate(lists):
                    state = frozenset(ls)
                    queue.append((state, (i,)))
                    seen.add(state)
                found = None
                while queue and found is None:
                    state, word = queue.popleft()
                    if not state:
                        found = word
                        break
                    for i, ls in enumerate(lists):
                        nxt = frozenset(c for c in ls if any(d != c for d in state))
                        if not nxt:
                            found = word + (i,)
                            break
                        if nxt not in seen:
                            seen.add(nxt)
                            queue.append((nxt, word + (i,)))
                if found is None:
                    no_obstruction += 1
                    continue
                profiles = [ordinary[i][1] for i in found]
                root_union = frozenset().union(*profiles)
                key = (len(found), len(root_union), tuple(len(lists[i]) for i in found),
                       len(set(found)))
                types[key] += 1
                examples.setdefault(key, (es, wc, hc,
                    [(ordinary[i][0], tuple(sorted(lists[i]))) for i in found]))
    print("no ordinary obstruction", no_obstruction, "types", len(types))
    for key, count in sorted(types.items()):
        print(count, key, examples[key])


if __name__ == "__main__":
    main()
