#!/usr/bin/env python3
"""Verify the 3K2 + 2K1 exact-block/reconfiguration barrier."""

from __future__ import annotations

from itertools import combinations


ORDER = 8
EDGES = {tuple(sorted(edge)) for edge in ((0, 4), (1, 3), (5, 6))}


def canonical(blocks):
    return tuple(sorted(tuple(sorted(block)) for block in blocks if block))


def set_partitions(limit=5):
    answer = set()
    blocks = []

    def visit(vertex):
        if len(blocks) > limit:
            return
        if vertex == ORDER:
            answer.add(canonical(blocks))
            return
        for block in blocks:
            block.add(vertex)
            visit(vertex + 1)
            block.remove(vertex)
        blocks.append({vertex})
        visit(vertex + 1)
        blocks.pop()

    visit(0)
    return answer


def independent(vertices):
    vertices = set(vertices)
    return not any(u in vertices and v in vertices for u, v in EDGES)


def proper(partition):
    return all(independent(block) for block in partition)


def one_vertex_adjacencies(partitions):
    index = {partition: i for i, partition in enumerate(partitions)}
    answer = set()
    for i, partition in enumerate(partitions):
        blocks = [set(block) for block in partition]
        for source, block in enumerate(blocks):
            for vertex in tuple(block):
                for target, other in enumerate(blocks):
                    if source == target or not independent(other | {vertex}):
                        continue
                    changed = [set(old) for old in blocks]
                    changed[source].remove(vertex)
                    changed[target].add(vertex)
                    j = index[canonical(changed)]
                    if i != j:
                        answer.add(tuple(sorted((i, j))))
                if len(block) >= 2 and len(blocks) < 5:
                    changed = [set(old) for old in blocks]
                    changed[source].remove(vertex)
                    changed.append({vertex})
                    j = index[canonical(changed)]
                    answer.add(tuple(sorted((i, j))))
    return answer


def main():
    partitions = sorted(partition for partition in set_partitions() if proper(partition))
    index = {partition: i for i, partition in enumerate(partitions)}
    adjacencies = one_vertex_adjacencies(partitions)

    independent_sets = {
        frozenset(vertices)
        for size in range(1, ORDER + 1)
        for vertices in combinations(range(ORDER), size)
        if independent(vertices)
    }
    maximum = {vertices for vertices in independent_sets if len(vertices) == 5}

    left = {i for i, partition in enumerate(partitions) if len(partition) == 5}
    for stable_set in maximum:
        complement = set(range(ORDER)) - set(stable_set)
        partition = canonical([stable_set] + [{vertex} for vertex in complement])
        left.add(index[partition])

    right = {
        i
        for i, partition in enumerate(partitions)
        if len(partition) <= 3
        and all(tuple(sorted((i, j))) not in adjacencies for j in left)
    }

    assert left.isdisjoint(right)
    assert all(len(partitions[i]) == 5 for i in left if i not in {
        index[canonical([stable_set] + [{v} for v in set(range(ORDER)) - set(stable_set)])]
        for stable_set in maximum
    })
    assert all(len(partitions[i]) < 5 for i in right)
    assert not any(
        (a in left and b in right) or (a in right and b in left)
        for a, b in adjacencies
    )

    for stable_set in independent_sets:
        block = tuple(sorted(stable_set))
        assert any(block in partitions[i] for i in left)
        assert any(block in partitions[i] for i in right)

    assert len(partitions) == 1834
    assert sum(len(partition) == 5 for partition in partitions) == 674
    assert len(maximum) == 8
    assert len(left) == 682
    assert len(right) == 300
    assert len(independent_sets) == 107
    assert len(adjacencies) == 20232

    print(
        "PASS "
        f"partitions={len(partitions)} "
        f"full={sum(len(partition) == 5 for partition in partitions)} "
        f"maximum_independent={len(maximum)} "
        f"left={len(left)} right={len(right)} "
        f"anchors={len(independent_sets)} adjacencies={len(adjacencies)}"
    )


if __name__ == "__main__":
    main()
