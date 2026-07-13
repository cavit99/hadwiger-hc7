#!/usr/bin/env python3
"""Fast exact K7-minor census for the C6 double-overlap quotients.

The search uses the elementary fact that an 11-vertex graph has a K7
minor exactly when at most four contractions produce a graph containing
a K7 subgraph.  States are partitions into current contracted bags.
"""

from __future__ import annotations

import itertools

import unique_interface_c6_surplus_split_probe as base


def touching(x: int, y: int, adjacency: tuple[int, ...]) -> bool:
    todo = x
    while todo:
        bit = todo & -todo
        todo ^= bit
        if adjacency[bit.bit_length() - 1] & y:
            return True
    return False


def find_k7(edges: set[tuple[int, int]]) -> tuple[int, ...] | None:
    n = 11
    adjacency = [0] * n
    for x, y in edges:
        adjacency[x] |= 1 << y
        adjacency[y] |= 1 << x
    adjacency = tuple(adjacency)
    start = tuple(1 << x for x in range(n))
    failed: set[tuple[int, ...]] = set()

    def clique7(bags: tuple[int, ...]) -> tuple[int, ...] | None:
        # Backtracking is faster than testing every 7-subset.
        def rec(chosen: tuple[int, ...], candidates: tuple[int, ...]):
            if len(chosen) == 7:
                return chosen
            need = 7 - len(chosen)
            if len(candidates) < need:
                return None
            for pos, bag in enumerate(candidates):
                nxt = tuple(other for other in candidates[pos + 1:]
                            if touching(bag, other, adjacency))
                ans = rec(chosen + (bag,), nxt)
                if ans is not None:
                    return ans
            return None
        return rec((), bags)

    def rec(bags: tuple[int, ...], depth: int) -> tuple[int, ...] | None:
        if bags in failed:
            return None
        found = clique7(bags)
        if found is not None:
            return found
        if depth == 4:
            failed.add(bags)
            return None
        # Merge adjacent bags.  Try small bags and helper-containing pairs first.
        pairs = [(i, j) for i in range(len(bags))
                 for j in range(i + 1, len(bags))
                 if touching(bags[i], bags[j], adjacency)]
        pairs.sort(key=lambda ij: (
            (bags[ij[0]] | bags[ij[1]]).bit_count(),
            -bool((bags[ij[0]] | bags[ij[1]]) & 0b11110000000),
            ij,
        ))
        for i, j in pairs:
            merged = bags[i] | bags[j]
            nxt = tuple(sorted((bag for p, bag in enumerate(bags)
                                if p not in (i, j)), key=lambda x: x))
            nxt = tuple(sorted(nxt + (merged,)))
            ans = rec(nxt, depth + 1)
            if ans is not None:
                return ans
        failed.add(bags)
        return None

    return rec(start, 0)


def main() -> None:
    def dihedral_perms():
        out = []
        for reflection in (False, True):
            for shift in range(6):
                p = {0: 0}
                for i in range(6):
                    j = (-i if reflection else i) + shift
                    p[i + 1] = (j % 6) + 1
                out.append(p)
        return out

    def canonical(roots, bits, split_opposite):
        left, right = base.rows(roots, bits)
        encodings = []
        for p in dihedral_perms():
            a = tuple(sorted(p[x] for x in left))
            b = tuple(sorted(p[x] for x in right))
            encodings.append((a, b))
            if split_opposite:
                encodings.append((b, a))
        return min(encodings)

    rows = []
    seen = set()
    multiplicity = {}
    for split_opposite, roots, bits in itertools.product(
        (False, True), itertools.combinations(base.S, 2), range(1 << 5)
    ):
        key = (split_opposite, canonical(roots, bits, split_opposite))
        multiplicity[key] = multiplicity.get(key, 0) + 1
        if key in seen:
            continue
        seen.add(key)
        rows.append((split_opposite, roots, bits, key))
    print("orbit representatives", len(rows), flush=True)
    failures = []
    verified = 0
    for index, (split_opposite, roots, bits, key) in enumerate(rows):
        edges = base.graph_edges(roots, bits, split_opposite)
        model = find_k7(edges)
        name = "opposite" if split_opposite else "arm"
        if model is None:
            failures.append((name, roots, bits, key, multiplicity[key]))
        else:
            verified += multiplicity[key]
        if index % 10 == 9:
            print("processed", index + 1, flush=True)
    print("verified labelled", verified)
    print("negative orbits", len(failures),
          "negative labelled", sum(x[-1] for x in failures))
    for row in failures:
        print(row)


if __name__ == "__main__":
    main()
