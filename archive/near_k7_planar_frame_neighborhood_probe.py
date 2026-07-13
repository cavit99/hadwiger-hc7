#!/usr/bin/env python3
"""Finite probe for degree-seven vertices in the rooted-triangle frame.

Vertices 0,1 are the two adjacent triangle neighbours and 2,...,6 are
the five neighbours in the planar remainder.  The latter induced graph
must be outerplanar.  We retain exactly the boundary graphs with
independence number at most two and with no K5-model using at most six
vertices (such a model plus the full sole exterior closes K7).
"""

from itertools import combinations, permutations

import networkx as nx


V = tuple(range(7))
W = tuple(range(2, 7))
PAIRS = tuple(combinations(V, 2))
INDEX = {e: i for i, e in enumerate(PAIRS)}


def bit(a, b):
    if a > b:
        a, b = b, a
    return 1 << INDEX[a, b]


def clique(mask, xs):
    return all(mask & bit(a, b) for a, b in combinations(xs, 2))


def alpha_at_most_two(mask):
    return all(any(mask & bit(a, b) for a, b in combinations(xs, 2))
               for xs in combinations(V, 3))


def has_k5_on_at_most_six(mask):
    for xs in combinations(V, 5):
        if clique(mask, xs):
            return True
    for xs in combinations(V, 6):
        for pair in combinations(xs, 2):
            if not mask & bit(*pair):
                continue
            singles = tuple(x for x in xs if x not in pair)
            if not clique(mask, singles):
                continue
            if all(any(mask & bit(p, s) for p in pair) for s in singles):
                return True
    return False


def outerplanar_w_masks():
    answer = set()
    wpairs = tuple(combinations(W, 2))
    for local in range(1 << len(wpairs)):
        graph = nx.Graph()
        graph.add_nodes_from(W)
        graph.add_node(7)
        graph.add_edges_from((7, w) for w in W)
        mask = 0
        for i, e in enumerate(wpairs):
            if local >> i & 1:
                graph.add_edge(*e)
                mask |= bit(*e)
        if nx.check_planarity(graph)[0]:
            answer.add(mask)
    return answer


def relabel(mask, perm):
    out = 0
    for a, b in PAIRS:
        if mask & bit(a, b):
            out |= bit(perm[a], perm[b])
    return out


def canonical_rooted(mask):
    # Preserve the unordered pair {0,1}; freely permute W.
    best = None
    for swap in (False, True):
        for p in permutations(W):
            perm = list(V)
            perm[0], perm[1] = ((1, 0) if swap else (0, 1))
            for old, new in zip(W, p):
                perm[old] = new
            image = relabel(mask, perm)
            best = image if best is None else min(best, image)
    return best


def main():
    outer = outerplanar_w_masks()
    cross = tuple((q, w) for q in (0, 1) for w in W)
    survivors = set()
    labelled = 0
    for wmask in outer:
        for cmask in range(1 << len(cross)):
            mask = wmask | bit(0, 1)
            for i, e in enumerate(cross):
                if cmask >> i & 1:
                    mask |= bit(*e)
            if not alpha_at_most_two(mask):
                continue
            if has_k5_on_at_most_six(mask):
                continue
            labelled += 1
            survivors.add(canonical_rooted(mask))

    by_edges = {}
    for mask in survivors:
        by_edges[mask.bit_count()] = by_edges.get(mask.bit_count(), 0) + 1
    print("outerplanar W masks", len(outer))
    print("labelled survivors", labelled)
    print("rooted isomorphism types", len(survivors))
    print("types by total edge count", sorted(by_edges.items()))
    for mask in sorted(survivors, key=lambda x: (x.bit_count(), x)):
        edges = [e for e in PAIRS if mask & bit(*e)]
        print(mask.bit_count(), edges)


if __name__ == "__main__":
    main()
