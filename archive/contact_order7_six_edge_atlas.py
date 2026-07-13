#!/usr/bin/env python3
"""Exact quotient atlas for six missing edges on an order-seven boundary."""

import itertools

import contact_order7_five_edge_verify as exact


V = tuple(range(9))


def all_candidate_partitions():
    answer = []
    # Seven used vertices: all singleton bags.
    for support in itertools.combinations(V, 7):
        answer.append(tuple(1 << v for v in support))
    # Eight used vertices: one pair and six singletons.
    for omitted in V:
        support = tuple(v for v in V if v != omitted)
        for pair in itertools.combinations(support, 2):
            pair_set = set(pair)
            answer.append((sum(1 << v for v in pair),) + tuple(
                1 << v for v in support if v not in pair_set
            ))
    # Nine used vertices: one triple or two pairs.
    for triple in itertools.combinations(V, 3):
        triple_set = set(triple)
        answer.append((sum(1 << v for v in triple),) + tuple(
            1 << v for v in V if v not in triple_set
        ))
    for first in itertools.combinations(V, 2):
        rest = tuple(v for v in V if v not in first)
        for second in itertools.combinations(rest, 2):
            if first > second:
                continue
            used = set(first) | set(second)
            answer.append((sum(1 << v for v in first),
                           sum(1 << v for v in second)) + tuple(
                1 << v for v in V if v not in used
            ))
    # Dense helper-anchored partitions tend to succeed; try larger support
    # before clique subgraphs, while retaining a deterministic order.
    answer.sort(key=lambda bags: (-sum(mask.bit_count() for mask in bags), bags))
    assert all(len(bags) == 7 for bags in answer)
    return tuple(answer)


CANDIDATES = all_candidate_partitions()


def fast_k7_model(edges):
    adjacency = [0] * 9
    for a, b in edges:
        adjacency[a] |= 1 << b
        adjacency[b] |= 1 << a

    def connected(mask):
        reached = mask & -mask
        while True:
            expanded = reached
            bits = reached
            while bits:
                low = bits & -bits
                expanded |= adjacency[low.bit_length() - 1] & mask
                bits ^= low
            if expanded == reached:
                return reached == mask
            reached = expanded

    for bags in CANDIDATES:
        if not all(connected(bag) for bag in bags):
            continue
        good = True
        neighbour_unions = []
        for bag in bags:
            union = 0
            bits = bag
            while bits:
                low = bits & -bits
                union |= adjacency[low.bit_length() - 1]
                bits ^= low
            neighbour_unions.append(union)
        for i in range(7):
            if any(not (neighbour_unions[i] & bags[j]) for j in range(i)):
                good = False
                break
        if good:
            return bags
    return None


def edge_list(mask):
    return tuple(edge for index, edge in enumerate(exact.PAIRS)
                 if mask >> index & 1)


def signature(mask):
    edges = edge_list(mask)
    degrees = [0] * 7
    adjacency = [set() for _ in range(7)]
    for a, b in edges:
        degrees[a] += 1
        degrees[b] += 1
        adjacency[a].add(b)
        adjacency[b].add(a)
    components = []
    unseen = set(range(7))
    while unseen:
        root = min(unseen)
        reached = {root}
        while True:
            expanded = reached | {y for x in reached for y in adjacency[x]}
            if expanded == reached:
                break
            reached = expanded
        components.append(len(reached))
        unseen -= reached
    return tuple(sorted(degrees, reverse=True)), tuple(sorted(components, reverse=True))


def main():
    failures = set()
    checked = 0
    for missing in itertools.combinations(exact.PAIRS, 6):
        mask = exact.edge_mask(missing)
        if fast_k7_model(exact.quotient_edges(mask)) is None:
            failures.add(mask)
        checked += 1

    remaining = set(failures)
    types = []
    while remaining:
        seed = min(remaining)
        orb = exact.orbit(seed)
        members = remaining & orb
        assert members
        representative = min(orb)
        types.append((representative, len(members), len(orb)))
        remaining -= members

    types.sort(key=lambda item: (signature(item[0]), item[0]))
    print("labelled six-edge complements checked", checked)
    print("labelled quotient failures", len(failures))
    print("unlabelled failure types", len(types))
    for index, (mask, labelled, orbit_size) in enumerate(types):
        # Independently replay every negative representative with the slower
        # arbitrary-connected-subset search.
        assert exact.k_minor_model(exact.quotient_edges(mask)) is None
        print(index, "edges", edge_list(mask), "signature", signature(mask),
              "labelled", labelled, "orbit", orbit_size)


if __name__ == "__main__":
    main()
