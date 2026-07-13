#!/usr/bin/env python3
"""Probe contraction-induced rank loss for four exact-seven lobes.

Four two-pole portal rows have rank four before the torso edge 01 is
contracted and rank at most three afterwards.  Up to relabelling and the
static bouquet/unusable-occurrence closures, seven incidence patterns
remain.  For every missed singleton-row profile, search for a K7 model
whose branch bags have order at most three.  A positive output is a guide
for a uniform hand proof; it is not itself used as a theorem.
"""

from __future__ import annotations

import itertools
from collections import Counter


PATTERNS = (
    ((0, 1), (0, 1), (2, 3), (2, 3)),
    ((0, 1), (0, 1), (2, 3), (2, 4)),
    ((0, 1), (0, 1), (2, 3), (4, 5)),
    ((0, 1), (0, 2), (1, 2), (3, 4)),
    ((0, 1), (0, 2), (1, 3), (2, 3)),
    ((0, 2), (0, 2), (1, 3), (1, 3)),
    ((0, 2), (0, 3), (1, 2), (1, 3)),
)


def matching_rank(rows, merge=False, forced=None):
    """Tiny brute-force transversal rank (four rows only)."""
    image = lambda x: 0 if merge and x in (0, 1) else x
    assignments = []
    for index, row in enumerate(rows):
        if forced is not None and index == forced[0]:
            assignments.append((image(forced[1]),))
        else:
            assignments.append(tuple({image(x) for x in row}))
    return max(
        (len(set(choice)) for choice in itertools.product(*assignments)),
        default=0,
    )


def canonical(rows):
    """Relabel all poles except the distinguished contracted pair 01."""
    others = sorted(set().union(*map(set, rows)) - {0, 1})
    answer = None
    for swap in (False, True):
        for permutation in itertools.permutations(range(2, 2 + len(others))):
            relabel = {0: int(swap), 1: int(not swap),
                       **dict(zip(others, permutation))}
            candidate = tuple(sorted(
                tuple(sorted(relabel[x] for x in row)) for row in rows
            ))
            answer = candidate if answer is None else min(answer, candidate)
    return answer


def classify_patterns():
    """Derive, rather than assume, the seven residual incidence types."""
    pairs = tuple(itertools.combinations(range(8), 2))
    residual = set()
    for rows in itertools.combinations_with_replacement(pairs, 4):
        if matching_rank(rows) < 4 or matching_rank(rows, merge=True) >= 4:
            continue
        # Existing static closures: a triple repeated pair, or four rows
        # on at most three poles.
        if max(Counter(rows).values()) >= 3 or len(set().union(*rows)) <= 3:
            continue
        # Existing unusable-occurrence closure: retain only families in
        # which every actual incidence belongs to an SDR.
        if any(matching_rank(rows, forced=(i, x)) < 4
               for i, row in enumerate(rows) for x in row):
            continue
        residual.add(canonical(rows))
    assert residual == set(PATTERNS), (residual, set(PATTERNS))
    return residual


def host(pattern, profile):
    k = 1 + max(max(row) for row in pattern)
    labels = range(k, k + 6)
    lobes = range(k + 6, k + 10)
    edges = {
        (i, j) for i, j in itertools.combinations(labels, 2)
        if (i-k, j-k) not in {(0, 1), (0, 2)}
    }
    edges.add((0, 1))
    for lobe, row, missed in zip(lobes, pattern, profile):
        edges.update(tuple(sorted((lobe, x))) for x in row)
        edges.update(tuple(sorted((lobe, s)))
                     for index, s in enumerate(labels) if index != missed)
    return k + 10, edges


def small_minor(n, edges, max_bag=3):
    adjacency = [0] * n
    for a, b in edges:
        adjacency[a] |= 1 << b
        adjacency[b] |= 1 << a

    candidates = []
    for size in range(1, max_bag + 1):
        for vertices in itertools.combinations(range(n), size):
            mask = sum(1 << x for x in vertices)
            reached = mask & -mask
            while True:
                expanded = reached
                todo = reached
                while todo:
                    low = todo & -todo
                    todo ^= low
                    expanded |= adjacency[low.bit_length() - 1] & mask
                if expanded == reached:
                    break
                reached = expanded
            if reached == mask:
                neighbourhood = 0
                for x in vertices:
                    neighbourhood |= adjacency[x]
                candidates.append((mask, neighbourhood))

    def search(chosen, available, used):
        if len(chosen) == 7:
            return tuple(chosen)
        needed = 7 - len(chosen)
        for pos, (bag, neighbourhood) in enumerate(available):
            if bag & used:
                continue
            next_available = [
                item for item in available[pos+1:]
                if not item[0] & (used | bag) and item[1] & bag
            ]
            if len(next_available) >= needed - 1:
                answer = search(chosen + [bag], next_available, used | bag)
                if answer is not None:
                    return answer
        return None

    return search([], candidates, 0)


def main():
    classify_patterns()
    print("classified residual incidence types", len(PATTERNS))
    counts = []
    for number, pattern in enumerate(PATTERNS):
        failures = []
        for profile in itertools.product(range(6), repeat=4):
            n, edges = host(pattern, profile)
            if small_minor(n, edges) is None:
                failures.append(profile)
        print(number, pattern, "profiles", 6**4,
              "small-model failures", len(failures), failures[:5])
        counts.append(len(failures))
    assert counts == [0, 0, 110, 0, 0, 0, 0], counts


if __name__ == "__main__":
    main()
