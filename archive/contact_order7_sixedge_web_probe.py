#!/usr/bin/env python3
"""Classify six-missing-edge two-shore quotients and test web frames.

For a missing-edge graph F on a seven-vertex adhesion S, the quotient is
(K7-F) plus two nonadjacent vertices complete to S.  We first test for a
K7 minor exactly.  For every quotient exception, we then seek an induced
cycle C in J=K7-F such that Z=S-C is bipartite and every crossing of the
cyclic terminal order gives a K7 after adding two adjacent path pieces in
one shore and one full opposite-shore helper.
"""

import itertools

import contact_order7_five_edge_verify as base


S = tuple(range(7))
PAIRS = tuple(itertools.combinations(S, 2))
H1, H2 = 7, 8


def partitions_7_of_9():
    vertices = tuple(range(9))
    answer = []
    # Seven used vertices: all singleton bags.
    for used in itertools.combinations(vertices, 7):
        answer.append(tuple(1 << x for x in used))
    # Eight used vertices: one pair and six singletons.
    for unused in vertices:
        used = tuple(x for x in vertices if x != unused)
        for pair in itertools.combinations(used, 2):
            rest = tuple(x for x in used if x not in pair)
            answer.append(((1 << pair[0]) | (1 << pair[1]),)
                          + tuple(1 << x for x in rest))
    # All vertices: one triple, or two pairs.
    for triple in itertools.combinations(vertices, 3):
        rest = tuple(x for x in vertices if x not in triple)
        answer.append((sum(1 << x for x in triple),)
                      + tuple(1 << x for x in rest))
    for four in itertools.combinations(vertices, 4):
        a, b, c, d = four
        for p1, p2 in (((a, b), (c, d)),
                       ((a, c), (b, d)),
                       ((a, d), (b, c))):
            rest = tuple(x for x in vertices if x not in four)
            answer.append(((1 << p1[0]) | (1 << p1[1]),
                           (1 << p2[0]) | (1 << p2[1]))
                          + tuple(1 << x for x in rest))
    return tuple(answer)


PARTITIONS = partitions_7_of_9()


def adjacency_from_edges(n, edges):
    adjacency = [0] * n
    for x, y in edges:
        adjacency[x] |= 1 << y
        adjacency[y] |= 1 << x
    return adjacency


def connected(mask, adjacency):
    reached = mask & -mask
    while True:
        expanded = reached
        todo = reached
        while todo:
            low = todo & -todo
            todo ^= low
            expanded |= adjacency[low.bit_length() - 1] & mask
        if expanded == reached:
            return reached == mask
        reached = expanded


def adjacent(a, b, adjacency):
    todo = a
    while todo:
        low = todo & -todo
        todo ^= low
        if adjacency[low.bit_length() - 1] & b:
            return True
    return False


def quotient_model(missing_mask):
    edges = base.quotient_edges(missing_mask)
    adjacency = adjacency_from_edges(9, edges)
    for bags in PARTITIONS:
        if not all(connected(bag, adjacency) for bag in bags):
            continue
        if all(adjacent(bags[i], bags[j], adjacency)
               for i in range(7) for j in range(i)):
            return bags
    return None


def components(edges):
    adjacency = {x: set() for x in S}
    for x, y in edges:
        adjacency[x].add(y)
        adjacency[y].add(x)
    answer = []
    unseen = set(S)
    while unseen:
        root = min(unseen)
        stack = [root]
        comp = set()
        while stack:
            x = stack.pop()
            if x in comp:
                continue
            comp.add(x)
            stack.extend(adjacency[x] - comp)
        unseen -= comp
        answer.append(tuple(sorted(comp)))
    return tuple(sorted(answer, key=lambda x: (len(x), x)))


def cycle_order(vertices, j_edges):
    vertices = set(vertices)
    nbr = {x: sorted(y for y in vertices if y != x
                    and tuple(sorted((x, y))) in j_edges)
           for x in vertices}
    if any(len(nbr[x]) != 2 for x in vertices):
        return None
    start = min(vertices)
    order = [start]
    prev = None
    cur = start
    while True:
        nxts = [x for x in nbr[cur] if x != prev]
        nxt = min(nxts) if prev is None else nxts[0]
        if nxt == start:
            break
        if nxt in order:
            return None
        order.append(nxt)
        prev, cur = cur, nxt
    return tuple(order) if len(order) == len(vertices) else None


def bipartite(vertices, j_edges):
    colour = {}
    for root in vertices:
        if root in colour:
            continue
        colour[root] = 0
        stack = [root]
        while stack:
            x = stack.pop()
            for y in vertices:
                if y == x or tuple(sorted((x, y))) not in j_edges:
                    continue
                if y not in colour:
                    colour[y] = 1 - colour[x]
                    stack.append(y)
                elif colour[y] == colour[x]:
                    return False
    return True


def generic_minor_model(n, edges, k=7):
    adjacency = adjacency_from_edges(n, edges)
    connected_sets = [mask for mask in range(1, 1 << n)
                      if connected(mask, adjacency)]
    connected_sets.sort(key=lambda x: (x.bit_count(), x))

    def rec(chosen, candidates, used):
        if len(chosen) == k:
            return tuple(chosen)
        needed = k - len(chosen)
        if len(candidates) < needed:
            return None
        for pos, bag in enumerate(candidates):
            if bag & used:
                continue
            nxt = [other for other in candidates[pos + 1:]
                   if not other & (used | bag)
                   and adjacent(bag, other, adjacency)]
            if len(nxt) >= needed - 1:
                result = rec(chosen + [bag], nxt, used | bag)
                if result is not None:
                    return result
        return None

    return rec([], connected_sets, 0)


def crossing_forces(j_edges, order):
    xpiece, ypiece, helper = 7, 8, 9
    witnesses = []
    for i, r, j, s in itertools.combinations(range(len(order)), 4):
        first = (order[i], order[j])
        second = (order[r], order[s])
        edges = set(j_edges)
        edges.add((xpiece, ypiece))
        edges.update((helper, z) for z in S)
        edges.update((xpiece, z) for z in first)
        edges.update((ypiece, z) for z in second)
        edges = {tuple(sorted(edge)) for edge in edges}
        model = generic_minor_model(10, edges)
        if model is None:
            return None
        witnesses.append((first, second, model))
    return tuple(witnesses)


def web_frames(missing_mask):
    missing = {edge for i, edge in enumerate(PAIRS)
               if missing_mask >> i & 1}
    j_edges = set(PAIRS) - missing
    answer = []
    for size in range(4, 8):
        for frame in itertools.combinations(S, size):
            order = cycle_order(frame, j_edges)
            if order is None:
                continue
            omitted = tuple(x for x in S if x not in frame)
            if not bipartite(omitted, j_edges):
                continue
            witnesses = crossing_forces(j_edges, order)
            if witnesses is not None:
                answer.append((order, omitted, witnesses))
    return tuple(answer)


def main():
    failures = []
    for missing in itertools.combinations(PAIRS, 6):
        mask = base.edge_mask(missing)
        if quotient_model(mask) is None:
            failures.append(mask)

    # Quotient by all vertex relabellings.
    covered = set()
    representatives = []
    for mask in failures:
        if mask in covered:
            continue
        orb = base.orbit(mask)
        representatives.append(mask)
        covered |= orb

    assert set(failures) <= covered
    print("labeled quotient exceptions", len(failures))
    print("unlabeled quotient exceptions", len(representatives))
    for number, mask in enumerate(representatives, 1):
        missing = tuple(edge for i, edge in enumerate(PAIRS)
                        if mask >> i & 1)
        degrees = tuple(sorted((sum(x in edge for edge in missing)
                                for x in S), reverse=True))
        frames = web_frames(mask)
        print("TYPE", number,
              "missing", missing,
              "degrees", degrees,
              "components", components(missing),
              "web_frames", len(frames))
        for order, omitted, witnesses in frames:
            print(" frame", order, "omitted", omitted,
                  "crossings", len(witnesses))


if __name__ == "__main__":
    main()
