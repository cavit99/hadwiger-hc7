#!/usr/bin/env python3
"""Verify the five-terminal cycle decoder and its crossed-frame residue.

The original eleven support relations are imported from the corrected
two-edge-layer verifier.  Cycle edges are then added only as virtual bag
adjacencies.  Up to reversal there are twelve cyclic orders on the five
terminals.  Ten close by a common rooted K4 or a K7.  The two crossed
orders have one uniform 27-pattern residue, checked by
``crossed_frame_certificate`` below.
"""

from __future__ import annotations

import itertools

import hc7_cross_arm_overlap_four_decoder_verify as base


FULL_MASK = (1 << len(base.ALL_PAIRS)) - 1


def complete_original_complements() -> set[int]:
    answers: set[int] = set()
    for ones, zeros in base.joined_states():
        unknown = FULL_MASK & ~(ones | zeros)
        bits = [1 << index for index in range(len(base.ALL_PAIRS)) if unknown >> index & 1]
        for choices in range(1 << len(bits)):
            extra = sum(bit for index, bit in enumerate(bits) if choices >> index & 1)
            answers.add(ones | extra)
    return answers


def clique(complement: int, vertices: tuple[int, ...]) -> bool:
    return all(
        base.original_edge(complement, u, v)
        for u, v in itertools.combinations(vertices, 2)
    )


def k7_model(complement: int) -> bool:
    vertices = tuple(range(base.N))

    # Seven singleton bags on a seven-subset.
    for omitted in itertools.combinations(vertices, 2):
        support = tuple(v for v in vertices if v not in omitted)
        if clique(complement, support):
            return True

    # One edge bag and six singleton bags on an eight-subset.
    for omitted in vertices:
        support = tuple(v for v in vertices if v != omitted)
        for x, y in itertools.combinations(support, 2):
            if not base.original_edge(complement, x, y):
                continue
            core = tuple(v for v in support if v not in (x, y))
            if clique(complement, core) and all(
                base.original_edge(complement, x, z)
                or base.original_edge(complement, y, z)
                for z in core
            ):
                return True

    # One three-vertex bag and six singleton bags on all nine vertices.
    for bag in itertools.combinations(vertices, 3):
        core = tuple(v for v in vertices if v not in bag)
        if not clique(complement, core) or not base.connected(complement, bag):
            continue
        if all(
            any(base.original_edge(complement, vertex, z) for vertex in bag)
            for z in core
        ):
            return True

    # Two edge bags and five singleton bags on all nine vertices.
    for four in itertools.combinations(vertices, 4):
        first = min(four)
        for mate in tuple(v for v in four if v != first):
            bag_one = (first, mate)
            bag_two = tuple(v for v in four if v not in bag_one)
            core = tuple(v for v in vertices if v not in four)
            if not base.original_edge(complement, *bag_one) or not base.original_edge(
                complement, *bag_two
            ):
                continue
            if not clique(complement, core):
                continue
            if not all(
                base.original_edge(complement, bag_one[0], z)
                or base.original_edge(complement, bag_one[1], z)
                for z in core
            ):
                continue
            if not all(
                base.original_edge(complement, bag_two[0], z)
                or base.original_edge(complement, bag_two[1], z)
                for z in core
            ):
                continue
            if any(
                base.original_edge(complement, u, v) for u in bag_one for v in bag_two
            ):
                return True
    return False


def perfect_matchings():
    first = base.I[0]
    for mate in base.I[1:]:
        rest = tuple(v for v in base.I if v not in (first, mate))
        yield {base.pair(first, mate), base.pair(*rest)}


def crossed_frame_certificate(complement: int, cycle: tuple[int, ...]) -> bool:
    """Recognize the uniform two-gate residue for a crossed cycle order."""
    left_one, left_two, root_one, z, root_two = cycle
    if (left_one, left_two, z) != (4, 5, base.Z):
        return False

    actual = {
        edge
        for edge in base.ALL_PAIRS
        if complement >> base.PAIR_INDEX[edge] & 1
    }
    fixed = {
        base.pair(left_one, z),
        base.pair(left_one, root_one),
        base.pair(left_two, z),
        base.pair(left_two, root_two),
    }
    for matching in perfect_matchings():
        for vertex in base.I:
            spoke = base.pair(vertex, z)
            allowed_tails = (
                {base.pair(root_one, root_two)},
                {spoke},
                {base.pair(root_one, root_two), spoke},
            )
            if any(actual == fixed | matching | tail for tail in allowed_tails):
                return True
    return False


def canonical_cycles() -> tuple[tuple[int, ...], ...]:
    cycles = []
    for tail in itertools.permutations(base.TERMINALS[1:]):
        cycle = (base.TERMINALS[0],) + tail
        if cycle[1] < cycle[-1]:
            cycles.append(cycle)
    assert len(cycles) == 12
    return tuple(cycles)


def main() -> None:
    originals = complete_original_complements()
    assert len(originals) == 3096
    unresolved_originals = tuple(
        complement for complement in originals if not base.common_rooted_k4(complement)
    )
    assert len(unresolved_originals) == 1080

    bad_orders = {(4, 5, base.P, base.Z, base.Q), (4, 5, base.Q, base.Z, base.P)}
    for cycle in canonical_cycles():
        virtual = sum(
            1 << base.PAIR_INDEX[base.pair(cycle[index], cycle[(index + 1) % 5])]
            for index in range(5)
        )
        augmented = {complement & ~virtual for complement in unresolved_originals}
        survivors = {complement for complement in augmented if not k7_model(complement)}

        if cycle in bad_orders:
            assert len(survivors) == 27
            assert all(crossed_frame_certificate(complement, cycle) for complement in survivors)
            left_one, left_two, root_one, z, root_two = cycle
            gate_defects = (
                base.pair(left_one, z),
                base.pair(left_one, root_one),
                base.pair(left_two, z),
                base.pair(left_two, root_two),
            )
            for defect in gate_defects:
                repair = 1 << base.PAIR_INDEX[defect]
                assert all(k7_model(complement & ~repair) for complement in survivors)
            tail_repairs = (base.pair(root_one, root_two),) + tuple(
                base.pair(vertex, z) for vertex in base.I
            )
            repair = sum(1 << base.PAIR_INDEX[edge] for edge in tail_repairs)
            assert all(k7_model(complement & ~repair) for complement in survivors)
        else:
            assert not survivors

        print(
            f"cycle={cycle} augmented={len(augmented)} "
            f"survivors={len(survivors)}"
        )


if __name__ == "__main__":
    main()
