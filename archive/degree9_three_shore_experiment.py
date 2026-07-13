#!/usr/bin/env python3
"""Exploratory oracle for the degree-nine/three-shore quotient.

This is deliberately not a proof certificate.  It tests whether the
anchor-gluing mechanism that closes the degree-eight three-shore cell can
plausibly close the next degree-nine cell.  Each of three anticomplete
shore vertices misses a prescribed two-set of a nine-vertex boundary.
"""

from itertools import combinations, permutations, product
import random


N = 9
SHORES = (9, 10, 11)
TOTAL = 12


def canonical_multigraph(edges):
    vertices = sorted(set(x for e in edges for x in e))
    relabel = {x: i for i, x in enumerate(vertices)}
    normalized = tuple((relabel[a], relabel[b]) for a, b in edges)
    return min(tuple(sorted(tuple(sorted((p[a], p[b]))) for a, b in normalized))
               for p in permutations(range(len(vertices))))


def miss_types():
    states = {()}
    for _ in range(3):
        nxt = set()
        for edges in states:
            used = len(set(x for e in edges for x in e))
            additions = list(combinations(range(used), 2))
            additions += [(x, used) for x in range(used)]
            additions += [(used, used + 1)]
            for e in additions:
                nxt.add(canonical_multigraph(edges + (e,)))
        states = nxt
    return tuple(sorted(states, key=lambda x: (len(set(sum(x, ()))), x)))


MISS_TYPES = miss_types()


def boundary_partitions():
    answer = []
    blocks = []

    def visit(selected, pos):
        if pos == len(selected):
            if len(blocks) == 6:
                answer.append(tuple(tuple(b) for b in blocks))
            return
        if len(blocks) + len(selected) - pos < 6:
            return
        x = selected[pos]
        for block in blocks:
            block.append(x)
            visit(selected, pos + 1)
            block.pop()
        if len(blocks) < 6:
            blocks.append([x])
            visit(selected, pos + 1)
            blocks.pop()

    for size in range(6, N + 1):
        for selected in combinations(range(N), size):
            visit(selected, 0)
    return tuple(answer)


PARTITIONS = boundary_partitions()


def adjacency(edges, misses):
    adj = [0] * TOTAL
    for x, y in edges:
        adj[x] |= 1 << y
        adj[y] |= 1 << x
    for i, shore in enumerate(SHORES):
        for x in range(N):
            if x not in misses[i]:
                adj[shore] |= 1 << x
                adj[x] |= 1 << shore
    return adj


def connected(mask, adj):
    reached = mask & -mask
    frontier = reached
    while frontier:
        bit = frontier & -frontier
        frontier -= bit
        x = bit.bit_length() - 1
        new = adj[x] & mask & ~reached
        reached |= new
        frontier |= new
    return reached == mask


def adjacent(left, right, adj):
    while left:
        bit = left & -left
        left -= bit
        if adj[bit.bit_length() - 1] & right:
            return True
    return False


def find_model(edges, misses):
    adj = adjacency(edges, misses)
    for partition in PARTITIONS:
        base = [sum(1 << x for x in block) for block in partition]
        for placement in product(range(-1, 6), repeat=3):
            bags = base[:]
            for i, target in enumerate(placement):
                if target >= 0:
                    bags[target] |= 1 << SHORES[i]
            if not all(connected(b, adj) for b in bags):
                continue
            if all(adjacent(bags[i], bags[j], adj)
                   for i in range(6) for j in range(i + 1, 6)):
                return bags
    return None


def has_edge(edges, left, right):
    edge_set = {frozenset(e) for e in edges}
    return any(x != y and frozenset((x, y)) in edge_set
               for x in left for y in right)


def anchor(edges, misses, extra_singletons):
    """Find star + two-shore blocks + 0, 1, or 2 singleton blocks."""
    for singletons in combinations(range(N), extra_singletons):
        rest = tuple(x for x in range(N) if x not in singletons)
        for colors in product(range(3), repeat=len(rest)):
            if set(colors) != {0, 1, 2}:
                continue
            blocks = tuple(tuple(x for x, c in zip(rest, colors) if c == k)
                           for k in range(3))
            if any(has_edge(edges, block, block) for block in blocks):
                continue
            good = True
            for retained in range(3):
                other = tuple(i for i in range(3) if i != retained)
                side_good = False
                for first, second in (other, other[::-1]):
                    if set(blocks[1]) & set(misses[first]):
                        continue
                    if set(blocks[2]) & set(misses[second]):
                        continue
                    if not (any(x not in misses[first] for x in blocks[2])
                            or any(x not in misses[second] for x in blocks[1])
                            or has_edge(edges, blocks[1], blocks[2])):
                        continue
                    if any(not (w not in misses[first]
                                   or has_edge(edges, (w,), blocks[1]))
                           for w in singletons):
                        continue
                    if any(not (w not in misses[second]
                                   or has_edge(edges, (w,), blocks[2]))
                           for w in singletons):
                        continue
                    # Every boundary singleton sees the star image through v.
                    if any(not has_edge(edges, (x,), (y,))
                           for x, y in combinations(singletons, 2)):
                        continue
                    side_good = True
                    break
                if not side_good:
                    good = False
                    break
            if good:
                return blocks + tuple((w,) for w in singletons)
    return None


def alpha_at_most_four(edges):
    edge_set = {frozenset(e) for e in edges}
    return all(any(frozenset(e) in edge_set for e in combinations(five, 2))
               for five in combinations(range(N), 5))


def random_boundary():
    while True:
        p = random.uniform(.25, .75)
        edges = [(x, y) for x in range(N) for y in range(x + 1, N)
                 if random.random() < p]
        if alpha_at_most_four(edges):
            return edges


def main():
    print("miss types", len(MISS_TYPES), "boundary partitions", len(PARTITIONS))
    for trial in range(100):
        edges = random_boundary()
        for misses in MISS_TYPES:
            if anchor(edges, misses, 0) is not None:
                continue
            if anchor(edges, misses, 1) is not None:
                continue
            if anchor(edges, misses, 2) is not None:
                continue
            model = find_model(edges, misses)
            if model is None:
                print("COUNTEREXAMPLE", misses, edges)
                return
        if trial % 10 == 0:
            print("checked", trial)
    print("no random counterexample")


if __name__ == "__main__":
    main()
