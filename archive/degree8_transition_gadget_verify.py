#!/usr/bin/env python3
"""Independent replay of the order-at-most-two transition exclusion.

This verifier intentionally does not import the discovery program or its
state list.
"""

from itertools import combinations, product


N = 8
Z = 8
X = tuple(range(9))
BOUNDARY_EDGES = {
    tuple(sorted(edge)) for edge in (
        (0, 1), (0, 7), (1, 7),
        (2, 4), (4, 5), (3, 5), (3, 6), (2, 6),
        (2, Z),
    )
}


def partitions():
    blocks = []

    def rec(pos):
        if pos == len(X):
            if len(blocks) <= 6:
                partition = tuple(tuple(block) for block in blocks)
                if sum(any(x < N for x in block) for block in partition) <= 5:
                    yield partition
            return
        x = X[pos]
        for i in range(len(blocks)):
            blocks[i].append(x)
            yield from rec(pos + 1)
            blocks[i].pop()
        if len(blocks) < 6:
            blocks.append([x])
            yield from rec(pos + 1)
            blocks.pop()

    yield from rec(0)


def state_list():
    result = []
    for partition in partitions():
        if any(tuple(sorted(edge)) in BOUNDARY_EDGES
               for block in partition for edge in combinations(block, 2)):
            continue
        colors = [0] * len(X)
        for color, block in enumerate(partition):
            for x in block:
                colors[x] = color
        result.append(tuple(colors))
    return tuple(result)


STATES = state_list()
ALL = (1 << len(STATES)) - 1


def avail(neighbors, colors):
    mask = 0b111111
    for x in neighbors:
        mask &= ~(1 << colors[x])
    return mask


def make_family(test):
    result = 0
    for index, colors in enumerate(STATES):
        if test(colors):
            result |= 1 << index
    return result


def one_vertex_signature(neighbors):
    neighbors = frozenset(neighbors)
    base = make_family(lambda c: bool(avail(neighbors, c)))
    results = [ALL]
    for x in sorted(neighbors):
        reduced = neighbors - {x}
        results.append(make_family(lambda c, r=reduced: bool(avail(r, c))))
        results.append(make_family(
            lambda c, x=x: all(c[y] != c[x] for y in neighbors if y != x)
        ))
    return base, tuple(result & ~base for result in results)


def two_vertex_signature(left, right):
    left, right = frozenset(left), frozenset(right)

    def edge_extension(colors, a=left, b=right):
        aa, bb = avail(a, colors), avail(b, colors)
        return bool(aa and bb and not (
            aa == bb and aa & (aa - 1) == 0
        ))

    base = make_family(edge_extension)
    results = [
        make_family(lambda c: bool(avail(right, c))),
        make_family(lambda c: bool(avail(left, c))),
        make_family(lambda c: bool(avail(left, c) and avail(right, c))),
        make_family(lambda c: bool(avail(left | right, c))),
    ]

    for own_left, own, other in ((True, left, right), (False, right, left)):
        for x in sorted(own):
            reduced = own - {x}

            def deleted(colors, reduced=reduced, own_left=own_left):
                a, b = ((reduced, right) if own_left
                        else (left, reduced))
                aa, bb = avail(a, colors), avail(b, colors)
                return bool(aa and bb and not (
                    aa == bb and aa & (aa - 1) == 0
                ))

            results.append(make_family(deleted))

            def contracted(colors, own=own, other=other, x=x):
                if any(colors[y] == colors[x] for y in own if y != x):
                    return False
                return bool(avail(other, colors) & ~(1 << colors[x]))

            results.append(make_family(contracted))

    return base, tuple(result & ~base for result in results)


def candidate_signatures(required):
    required = tuple(required)
    signatures = []

    base, transitions = one_vertex_signature(required)
    if all(transitions):
        signatures.append((base, transitions))

    seen = set()
    for choices in product((1, 2, 3), repeat=len(required)):
        left = frozenset(x for x, choice in zip(required, choices)
                         if choice & 1)
        right = frozenset(x for x, choice in zip(required, choices)
                          if choice & 2)
        key = min((tuple(sorted(left)), tuple(sorted(right))),
                  (tuple(sorted(right)), tuple(sorted(left))))
        if key in seen:
            continue
        seen.add(key)
        base, transitions = two_vertex_signature(left, right)
        if all(transitions):
            signatures.append((base, transitions))
    return tuple(signatures)


def transitions_hold(piece, other1, other2):
    base, changes = piece
    common_missing = other1[0] & other2[0] & ~base
    return bool(common_missing) and all(change & common_missing
                                        for change in changes)


def main():
    branch_required = tuple(x for x in X if x not in (0, 1))
    d_required = tuple(x for x in range(N) if x != 0)
    branches = candidate_signatures(branch_required)
    exteriors = candidate_signatures(d_required)

    assert len(STATES) == 2355
    assert len(branches) == 215
    assert len(exteriors) == 156

    checked = 0
    for first in branches:
        for second in branches:
            if not (first[0] & second[0]):
                continue
            for third in exteriors:
                checked += 1
                if first[0] & second[0] & third[0]:
                    continue
                assert not (
                    transitions_hold(first, second, third)
                    and transitions_hold(second, first, third)
                    and transitions_hold(third, first, second)
                ), "transition-satisfying triple found"

    assert checked == 7_211_100
    print("low exact states verified:", len(STATES))
    print("individually critical signatures:", len(branches), "branch +",
          len(exteriors), "exterior")
    print("compatible triples exhausted:", checked)
    print("no order-at-most-two transition architecture")


if __name__ == "__main__":
    main()
