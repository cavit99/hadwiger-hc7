#!/usr/bin/env python3
"""Verify the K_{2,6} one-sided full-trace/static-anchor barrier."""

from itertools import product


N = 8
A = frozenset((6, 7))
B = frozenset(range(6))
EDGES = {tuple(sorted((a, b))) for a in A for b in B}


def canonical(blocks):
    return tuple(sorted((tuple(sorted(block)) for block in blocks)))


def set_partitions(items, limit=5):
    out = set()

    def rec(pos, blocks):
        if len(blocks) > limit:
            return
        if pos == len(items):
            out.add(canonical(blocks))
            return
        v = items[pos]
        for i in range(len(blocks)):
            blocks[i].add(v)
            rec(pos + 1, blocks)
            blocks[i].remove(v)
        blocks.append({v})
        rec(pos + 1, blocks)
        blocks.pop()

    rec(0, [])
    return out


def independent(vertices):
    vertices = set(vertices)
    return not any(u in vertices and v in vertices for u, v in EDGES)


def proper(partition):
    return all(independent(block) for block in partition)


def b_blocks(partition):
    return sum(bool(set(block) & B) for block in partition)


def a_joined(partition):
    return any(set(block) == A for block in partition)


def cut_key(j):
    j = frozenset(j)
    other = B - j
    return min(tuple(sorted(j)), tuple(sorted(other))), max(
        tuple(sorted(j)), tuple(sorted(other))
    )


def block(*vertices):
    return frozenset(vertices)


ALL = {p for p in set_partitions(tuple(range(N))) if proper(p)}
FULL = {p for p in ALL if len(p) == 5}

DISTINGUISHED = cut_key({0})
CUTS = {
    cut_key(j)
    for size in range(1, 6)
    for j in __import__("itertools").combinations(B, size)
}


def cut_partition(joined, key):
    j, other = map(frozenset, key)
    if joined:
        return canonical((A, j, other))
    return canonical((block(6), block(7), j, other))


LEFT = {p for p in FULL if a_joined(p)}
RIGHT = {p for p in FULL if not a_joined(p)}

LEFT.add(canonical((A, B)))
RIGHT.add(canonical((block(6), block(7), B)))

for key in CUTS:
    if key == DISTINGUISHED:
        LEFT.add(cut_partition(False, key))
        RIGHT.add(cut_partition(True, key))
    else:
        LEFT.add(cut_partition(True, key))
        RIGHT.add(cut_partition(False, key))

RIGHT.add(canonical((A, block(0), block(1), block(2, 3, 4, 5))))


def has_k5_minor():
    subsets = [
        frozenset(i for i in range(N) if mask & (1 << i))
        for mask in range(1, 1 << N)
    ]

    def connected(s):
        reached = {next(iter(s))}
        while True:
            fresh = {
                v
                for v in s - reached
                if any(tuple(sorted((v, u))) in EDGES for u in reached)
            }
            if not fresh:
                return reached == set(s)
            reached |= fresh

    connected_sets = [s for s in subsets if connected(s)]

    def adjacent(s, t):
        return any(tuple(sorted((u, v))) in EDGES for u in s for v in t)

    def search(chosen, start):
        if len(chosen) == 5:
            return True
        for i in range(start, len(connected_sets)):
            candidate = connected_sets[i]
            if any(candidate & old for old in chosen):
                continue
            if any(not adjacent(candidate, old) for old in chosen):
                continue
            if search(chosen + [candidate], i + 1):
                return True
        return False

    return search([], 0)


def orientation(colouring):
    return len({colouring[v] for v in A})


def main():
    assert not has_k5_minor()
    assert LEFT <= ALL and RIGHT <= ALL and LEFT.isdisjoint(RIGHT)

    independent_sets = [
        frozenset(i for i in range(N) if mask & (1 << i))
        for mask in range(1, 1 << N)
        if independent(i for i in range(N) if mask & (1 << i))
    ]
    for language in (LEFT, RIGHT):
        for query in independent_sets:
            assert any(query in map(frozenset, partition) for partition in language)

    full_colourings = []
    for colouring in product(range(5), repeat=N):
        if len(set(colouring)) != 5:
            continue
        if any(colouring[u] == colouring[v] for u, v in EDGES):
            continue
        partition = canonical(
            ({v for v in range(N) if colouring[v] == colour} for colour in range(5))
        )
        side = orientation(colouring)
        assert (partition in LEFT) == (side == 1)
        assert (partition in RIGHT) == (side == 2)
        full_colourings.append(colouring)

    full_set = set(full_colourings)
    moves = 0
    for colouring in full_colourings:
        old_side = orientation(colouring)
        counts = [colouring.count(colour) for colour in range(5)]
        for vertex in range(N):
            old = colouring[vertex]
            if counts[old] == 1:
                continue
            for new in range(5):
                if new == old:
                    continue
                candidate = list(colouring)
                candidate[vertex] = new
                candidate = tuple(candidate)
                if candidate not in full_set:
                    continue
                moves += 1
                assert orientation(candidate) == old_side

    print(
        "PASS "
        f"partitions={len(ALL)} full_partitions={len(FULL)} "
        f"left={len(LEFT)} right={len(RIGHT)} "
        f"anchors={len(independent_sets)} "
        f"full_colourings={len(full_colourings)} moves={moves}"
    )


if __name__ == "__main__":
    main()
