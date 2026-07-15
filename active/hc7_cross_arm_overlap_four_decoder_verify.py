#!/usr/bin/env python3
"""Dependency-free verifier for the overlap-four rooted-K4 decoder.

The program does not enumerate arbitrary nine-vertex graphs.  It first
enumerates the 375 complement patterns on six vertices that are exactly
the irredundant spanning-K5 supports.  It then joins eleven copies of this
finite relation on their literal labelled overlaps.

For each choice of the fifth terminal t it verifies the table stated in
results/hc7_cross_arm_overlap_four_rooted_k4_decoder.md:

* either the original graph has the displayed common rooted K4; or
* after adding only the six virtual adjacencies supplied by the exterior
  rooted K4, the complement off t is a perfect matching on I, with at most
  one extra edge from I to z.  The latter has an explicit spanning K7
  model.

Only Python's standard library is used.
"""

from __future__ import annotations

import itertools


N = 9
A = tuple(range(6))
I = tuple(range(4))
LEFT = (4, 5)
Z, P, Q = 6, 7, 8
X = I + (Z,)
TERMINALS = LEFT + (Z, P, Q)

ALL_PAIRS = tuple(itertools.combinations(range(N), 2))
PAIR_INDEX = {pair: index for index, pair in enumerate(ALL_PAIRS)}
LOCAL_PAIRS = tuple(itertools.combinations(range(6), 2))


def pair(u: int, v: int) -> tuple[int, int]:
    return (u, v) if u < v else (v, u)


def original_edge(complement: int, u: int, v: int) -> bool:
    return not (complement >> PAIR_INDEX[pair(u, v)] & 1)


def local_original(complement: int, u: int, v: int) -> bool:
    return not (complement >> LOCAL_PAIRS.index(pair(u, v)) & 1)


def local_exact_six(complement: int) -> bool:
    for x, y in LOCAL_PAIRS:
        if not local_original(complement, x, y):
            continue
        core = tuple(v for v in range(6) if v not in (x, y))
        if all(local_original(complement, u, v) for u, v in itertools.combinations(core, 2)) and all(
            local_original(complement, x, z) or local_original(complement, y, z)
            for z in core
        ):
            return True
    return False


def local_has_literal_k5(complement: int) -> bool:
    return any(
        all(local_original(complement, u, v) for u, v in itertools.combinations(five, 2))
        for five in itertools.combinations(range(6), 5)
    )


LOCAL_ALLOWED = tuple(
    complement
    for complement in range(1 << len(LOCAL_PAIRS))
    if local_exact_six(complement) and not local_has_literal_k5(complement)
)


SUPPORTS = [A, X + (P,), X + (Q,)]
for omitted in I:
    common = tuple(v for v in A if v != omitted)
    SUPPORTS.extend((common + (P,), common + (Q,)))


def global_patterns(support: tuple[int, ...]) -> tuple[tuple[int, int], ...]:
    global_indices = tuple(PAIR_INDEX[pair(support[u], support[v])] for u, v in LOCAL_PAIRS)
    known = sum(1 << index for index in global_indices)
    patterns = []
    for local in LOCAL_ALLOWED:
        ones = sum(
            1 << global_indices[index]
            for index in range(len(LOCAL_PAIRS))
            if local >> index & 1
        )
        patterns.append((ones, known ^ ones))
    return tuple(patterns)


CONSTRAINTS = tuple(global_patterns(support) for support in SUPPORTS)


def joined_states() -> set[tuple[int, int]]:
    """Return all partial complement assignments satisfying the 11 supports."""
    states: set[tuple[int, int]] = set()

    def visit(done: frozenset[int], ones: int, zeros: int) -> None:
        if len(done) == len(CONSTRAINTS):
            states.add((ones, zeros))
            return

        selected = -1
        compatible: list[tuple[int, int]] | None = None
        for index, patterns in enumerate(CONSTRAINTS):
            if index in done:
                continue
            options = [
                pattern
                for pattern in patterns
                if not (pattern[0] & zeros or pattern[1] & ones)
            ]
            if compatible is None or len(options) < len(compatible):
                selected = index
                compatible = options
        assert compatible is not None

        seen: set[tuple[int, int]] = set()
        for pattern_ones, pattern_zeros in compatible:
            new = (ones | pattern_ones, zeros | pattern_zeros)
            if new in seen:
                continue
            seen.add(new)
            visit(done | {selected}, *new)

    visit(frozenset(), 0, 0)
    return states


def relevant_complements(
    states: set[tuple[int, int]], omitted: int
) -> set[int]:
    common_vertices = set(A) | {P, Q}
    k7_vertices = set(range(N)) - {omitted}
    relevant_pairs = set(itertools.combinations(sorted(common_vertices), 2)) | set(
        itertools.combinations(sorted(k7_vertices), 2)
    )
    relevant_mask = sum(1 << PAIR_INDEX[p] for p in relevant_pairs)
    answers: set[int] = set()
    for ones, zeros in states:
        unknown = relevant_mask & ~(ones | zeros)
        unknown_bits = [1 << index for index in range(len(ALL_PAIRS)) if unknown >> index & 1]
        for choices in range(1 << len(unknown_bits)):
            extra = sum(bit for index, bit in enumerate(unknown_bits) if choices >> index & 1)
            answers.add((ones | extra) & relevant_mask)
    return answers


def connected(complement: int, vertices: tuple[int, ...]) -> bool:
    reached = {vertices[0]}
    frontier = [vertices[0]]
    while frontier:
        vertex = frontier.pop()
        for other in vertices:
            if other not in reached and original_edge(complement, vertex, other):
                reached.add(other)
                frontier.append(other)
    return len(reached) == len(vertices)


def touch(complement: int, left: tuple[int, ...], right: tuple[int, ...]) -> bool:
    return any(original_edge(complement, u, v) for u in left for v in right)


def partitions(items: tuple[int, ...], block_count: int):
    blocks: list[list[int]] = []

    def visit(index: int):
        if index == len(items):
            if len(blocks) == block_count:
                yield tuple(tuple(block) for block in blocks)
            return
        item = items[index]
        for position in range(len(blocks)):
            blocks[position].append(item)
            yield from visit(index + 1)
            blocks[position].pop()
        if len(blocks) < block_count:
            blocks.append([item])
            yield from visit(index + 1)
            blocks.pop()

    yield from visit(0)


def common_rooted_k4(complement: int) -> bool:
    for root in I:
        available = tuple(v for v in A if v != root)
        roots = (root, P, Q)
        for support_size in (4, 5):
            for support in itertools.combinations(available, support_size):
                for bags in partitions(support, 4):
                    if not all(connected(complement, bag) for bag in bags):
                        continue
                    if not all(touch(complement, left, right) for left, right in itertools.combinations(bags, 2)):
                        continue
                    if all(
                        all(any(original_edge(complement, named, vertex) for vertex in bag) for bag in bags)
                        for named in roots
                    ):
                        return True
    return False


def k7_avoiding(complement: int, omitted: int) -> bool:
    vertices = tuple(v for v in range(N) if v != omitted)
    for deleted in vertices:
        seven = tuple(v for v in vertices if v != deleted)
        if all(original_edge(complement, u, v) for u, v in itertools.combinations(seven, 2)):
            return True
    for x, y in itertools.combinations(vertices, 2):
        if not original_edge(complement, x, y):
            continue
        core = tuple(v for v in vertices if v not in (x, y))
        if all(original_edge(complement, u, v) for u, v in itertools.combinations(core, 2)) and all(
            original_edge(complement, x, z) or original_edge(complement, y, z)
            for z in core
        ):
            return True
    return False


def thin_template(complement: int, omitted: int) -> bool:
    """Perfect matching on I, with zero or one additional I-z nonedge."""
    vertices = tuple(v for v in range(N) if v != omitted)
    actual = {
        p
        for p in itertools.combinations(vertices, 2)
        if complement >> PAIR_INDEX[p] & 1
    }
    for first in itertools.combinations(I, 2):
        rest = tuple(v for v in I if v not in first)
        matching = {pair(*first), pair(*rest)}
        if actual == matching:
            return True
        if any(actual == matching | {pair(vertex, Z)} for vertex in I):
            return True
    return False


def main() -> None:
    assert len(LOCAL_ALLOWED) == 375
    states = joined_states()
    assert len(states) == 387
    for clique in itertools.combinations(TERMINALS, 4):
        omitted = next(vertex for vertex in TERMINALS if vertex not in clique)
        complements = relevant_complements(states, omitted)
        virtual_edges = sum(1 << PAIR_INDEX[p] for p in itertools.combinations(clique, 2))
        surviving_pairs = set(itertools.combinations(tuple(v for v in range(N) if v != omitted), 2))
        surviving_mask = sum(1 << PAIR_INDEX[p] for p in surviving_pairs)

        common_count = 0
        direct_count = 0
        residue: set[int] = set()
        for complement in complements:
            if common_rooted_k4(complement):
                common_count += 1
                continue
            augmented = complement & ~virtual_edges
            assert k7_avoiding(augmented, omitted)
            direct_count += 1
            residue.add(augmented & surviving_mask)

        assert len(residue) == (3 if omitted == Z else 15)
        assert all(thin_template(complement, omitted) for complement in residue)

        print(
            f"clique={clique} omitted={omitted} original_states={len(states)} "
            f"patterns={len(complements)} common={common_count} direct={direct_count} "
            f"projected_direct={len(residue)}"
        )


if __name__ == "__main__":
    main()
