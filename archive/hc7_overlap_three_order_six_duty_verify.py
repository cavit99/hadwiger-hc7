#!/usr/bin/env python3
"""Duty-carrier certificate for the order-six-arm overlap-three cell.

The checker never enumerates K7 branch partitions.  It extracts the exact
three-core contact duties from the joined support relation and tests only
the reusable exterior target: a K4 model every bag of which is complete in
duty to the three-core.  Original terminal edges and virtual facial/carrier
edges are kept separate until this final K4 test.
"""

from __future__ import annotations

import itertools
from collections import Counter

import hc7_cross_arm_overlap_three_kernel_decoder as decoder


CELL, PAIRS, PAIR_INDEX, STATES = decoder.joined_states(6)
N, A, I, X, P, Q, T, SUPPORTS, LITERAL_FIVES = CELL
L = (3, 4, 5)
Z = (6, 7)
ROOTS = (8, 9)
TERMINAL_PAIRS = tuple(itertools.combinations(T, 2))
TERMINAL_INDEX = {edge: index for index, edge in enumerate(TERMINAL_PAIRS)}
UNKNOWN_TERMINAL_PAIRS = {
    decoder.pair(left, right) for left in L for right in Z
} | {decoder.pair(*ROOTS)}


def live_states():
    return tuple(
        state
        for state in STATES
        if decoder.common_rooted_k4(state[0], N, A, I, P, Q) is None
    )


def duty_vector(ones: int) -> tuple[int, ...]:
    """Return each terminal's three-bit neighbourhood trace on I."""
    return tuple(
        sum(
            1 << position
            for position, core in enumerate(I)
            if ones >> PAIR_INDEX[decoder.pair(core, terminal)] & 1
        )
        for terminal in T
    )


def terminal_mask(ones: int) -> int:
    return sum(
        1 << TERMINAL_INDEX[edge]
        for edge in TERMINAL_PAIRS
        if ones >> PAIR_INDEX[edge] & 1
    )


def terminal_edges(mask: int, vertices: set[int] | None = None) -> set[tuple[int, int]]:
    return {
        edge
        for index, edge in enumerate(TERMINAL_PAIRS)
        if mask >> index & 1
        and (vertices is None or edge[0] in vertices and edge[1] in vertices)
    }


def cycles(vertices: tuple[int, ...]):
    first = vertices[0]
    for tail in itertools.permutations(vertices[1:]):
        order = (first,) + tail
        if order[1] > order[-1]:
            continue
        rim = {
            decoder.pair(order[index], order[(index + 1) % len(order)])
            for index in range(len(order))
        }
        yield order, rim


_MEETING_SPECS: dict[tuple[int, int], tuple] = {}


def meeting_specs(order: int, good_order: int):
    key = (order, good_order)
    if key not in _MEETING_SPECS:
        _MEETING_SPECS[key] = tuple(
            (bags, internal, cross)
            for bags, internal, cross in decoder.partition_specs(order, 4)
            if all(any(vertex < good_order for vertex in bag) for bag in bags)
        )
    return _MEETING_SPECS[key]


def has_good_meeting_k4(
    edges: set[tuple[int, int]],
    objects: tuple[int, ...],
    good: tuple[int, ...],
) -> bool:
    """Test for a K4 model whose every bag contains a good terminal."""
    assert objects[: len(good)] == good
    relabel = {vertex: index for index, vertex in enumerate(objects)}
    local_pairs = tuple(itertools.combinations(range(len(objects)), 2))
    local_index = {edge: index for index, edge in enumerate(local_pairs)}
    mask = sum(
        1 << local_index[decoder.pair(relabel[u], relabel[v])]
        for u, v in edges
        if u in relabel and v in relabel
    )
    return any(
        all(mask & cross_mask for cross_mask in cross)
        and all(any(mask & tree == tree for tree in trees) for trees in internal)
        for _, internal, cross in meeting_specs(len(objects), len(good))
    )


def symmetry_orbit_count(live: tuple[tuple[int, int], ...]) -> int:
    permutations = []
    for image_i in itertools.permutations(I):
        for image_l in itertools.permutations(L):
            for image_z in itertools.permutations(Z):
                for image_roots in itertools.permutations(ROOTS):
                    mapping = dict(zip(I, image_i))
                    mapping.update(zip(L, image_l))
                    mapping.update(zip(Z, image_z))
                    mapping.update(zip(ROOTS, image_roots))
                    permutations.append(mapping)

    def transform(mask: int, mapping: dict[int, int]) -> int:
        answer = 0
        for index, (u, v) in enumerate(PAIRS):
            if mask >> index & 1:
                answer |= 1 << PAIR_INDEX[decoder.pair(mapping[u], mapping[v])]
        return answer

    canonical = {
        min((transform(ones, mapping), transform(zeros, mapping)) for mapping in permutations)
        for ones, zeros in live
    }
    return len(canonical)


def verify_duties(live: tuple[tuple[int, int], ...]):
    assert len(STATES) == 60162
    assert len(live) == 7878
    for ones, zeros in live:
        assert all(
            ones >> PAIR_INDEX[decoder.pair(left, right)] & 1
            for left, right in itertools.combinations(I, 2)
        )
        unknown = {
            edge
            for index, edge in enumerate(PAIRS)
            if not ((ones | zeros) >> index & 1)
        }
        assert unknown == UNKNOWN_TERMINAL_PAIRS

    group_profile = Counter()
    deficit_profile = Counter()
    for ones, _ in live:
        duties = duty_vector(ones)
        good = {terminal for terminal, duty in zip(T, duties) if duty == 0b111}
        group_profile[
            (
                len(good),
                len(good & set(L)),
                len(good & set(Z)),
                len(good & set(ROOTS)),
            )
        ] += 1
        deficit_profile[
            (len(good), tuple(sorted(3 - duty.bit_count() for duty in duties)))
        ] += 1

    assert group_profile == Counter(
        {
            (3, 1, 0, 2): 153,
            (4, 1, 1, 2): 180,
            (4, 2, 0, 2): 3969,
            (5, 1, 2, 2): 162,
            (5, 2, 1, 2): 1956,
            (6, 2, 2, 2): 1458,
        }
    )
    assert all(profile[3] == 2 for profile in group_profile)

    expected_deficits = Counter(
        {
            (3, (0, 0, 0, 1, 1, 1, 1)): 153,
            (4, (0, 0, 0, 0, 1, 1, 1)): 1557,
            (4, (0, 0, 0, 0, 1, 1, 2)): 972,
            (4, (0, 0, 0, 0, 1, 1, 3)): 324,
            (4, (0, 0, 0, 0, 1, 2, 2)): 972,
            (4, (0, 0, 0, 0, 1, 2, 3)): 324,
            (5, (0, 0, 0, 0, 0, 1, 1)): 1782,
            (5, (0, 0, 0, 0, 0, 1, 2)): 108,
            (5, (0, 0, 0, 0, 0, 1, 3)): 36,
            (5, (0, 0, 0, 0, 0, 2, 2)): 108,
            (5, (0, 0, 0, 0, 0, 2, 3)): 72,
            (5, (0, 0, 0, 0, 0, 3, 3)): 12,
            (6, (0, 0, 0, 0, 0, 0, 1)): 1458,
        }
    )
    assert deficit_profile == expected_deficits
    return group_profile, deficit_profile


def unique_cases(live, good_order: int):
    cases = {}
    for ones, _ in live:
        duties = duty_vector(ones)
        good = tuple(terminal for terminal, duty in zip(T, duties) if duty == 0b111)
        if len(good) == good_order:
            cases[(good, terminal_mask(ones))] = True
    return tuple(cases)


def verify_cofacial_carriers(live):
    carrier_counts = Counter()
    impossible_counts = Counter()
    D = 10

    for good_order in (4, 5, 6):
        for good, mask in unique_cases(live, good_order):
            bad = tuple(terminal for terminal in T if terminal not in good)
            original = terminal_edges(mask)
            for on_order in range(len(bad) + 1):
                for on_face in itertools.combinations(bad, on_order):
                    cycle_vertices = good + on_face
                    off_face = tuple(terminal for terminal in bad if terminal not in on_face)
                    compatible = 0
                    for _, rim in cycles(cycle_vertices):
                        if not terminal_edges(mask, set(cycle_vertices)) <= rim:
                            continue
                        compatible += 1
                        carrier_counts[(good_order, on_order)] += 1
                        if not off_face:
                            # All terminals are on the face.  The peripheral
                            # construction allows any cycle bag to be the hub.
                            assert any(
                                has_good_meeting_k4(
                                    original
                                    | rim
                                    | {
                                        decoder.pair(centre, terminal)
                                        for terminal in cycle_vertices
                                        if terminal != centre
                                    },
                                    good + on_face,
                                    good,
                                )
                                for centre in cycle_vertices
                            )
                        else:
                            # Preserve one off-face terminal b.  The other
                            # off-face terminals are absorbed in D=(H-b)-C.
                            assert any(
                                has_good_meeting_k4(
                                    original
                                    | rim
                                    | {
                                        decoder.pair(D, terminal)
                                        for terminal in cycle_vertices
                                    }
                                    | {decoder.pair(D, b)},
                                    good + on_face + (b, D),
                                    good,
                                )
                                for b in off_face
                            )
                    if compatible == 0:
                        impossible_counts[(good_order, on_order)] += 1

    assert carrier_counts == Counter(
        {
            (4, 0): 342,
            (4, 1): 648,
            (4, 2): 12,
            (5, 0): 624,
            (5, 1): 96,
            (6, 0): 492,
        }
    )
    # In particular, putting every bad terminal on the good facial cycle is
    # incompatible with the already forced literal terminal edges.
    assert all(carrier_counts[(good_order, 7 - good_order)] == 0 for good_order in (4, 5, 6))
    return carrier_counts, impossible_counts


def verify_three_good_handoff(live):
    cases = []
    missing_colour_hist = Counter()
    compatible_all_terminal_cycles = 0
    for ones, _ in live:
        duties = duty_vector(ones)
        good = tuple(terminal for terminal, duty in zip(T, duties) if duty == 0b111)
        if len(good) != 3:
            continue
        assert good[1:] == ROOTS
        bad = tuple(terminal for terminal in T if terminal not in good)
        assert all(duties[T.index(terminal)].bit_count() == 2 for terminal in bad)
        missing = tuple(
            sorted(
                next(position for position in range(3) if not duties[T.index(terminal)] >> position & 1)
                for terminal in bad
            )
        )
        missing_colour_hist[missing] += 1
        mask = terminal_mask(ones)
        cases.append((duties, mask))
        for _, rim in cycles(T):
            if terminal_edges(mask) <= rim:
                compatible_all_terminal_cycles += 1

    assert len(cases) == 153
    assert len(set(cases)) == 153
    assert compatible_all_terminal_cycles == 0
    assert missing_colour_hist == Counter(
        {
            (0, 1, 1, 1): 24,
            (0, 2, 2, 2): 24,
            (0, 0, 0, 1): 24,
            (1, 1, 1, 2): 24,
            (1, 2, 2, 2): 24,
            (0, 0, 0, 2): 24,
            (0, 0, 0, 0): 3,
            (1, 1, 1, 1): 3,
            (2, 2, 2, 2): 3,
        }
    )
    return missing_colour_hist


def main() -> None:
    live = live_states()
    group_profile, deficit_profile = verify_duties(live)
    orbits = symmetry_orbit_count(live)
    assert orbits == 140
    carriers, impossible = verify_cofacial_carriers(live)
    three_good = verify_three_good_handoff(live)

    print("order-six-arm overlap-three duty interface: verified")
    print("joined=60162 noncommon=7878 symmetry_orbits=140")
    print("good-terminal counts:", {k: sum(v for p, v in group_profile.items() if p[0] == k) for k in (3, 4, 5, 6)})
    print("cofacial carrier instances:", dict(sorted(carriers.items())))
    print("every good>=4 carrier has a good-meeting K4")
    print("three-good states=153; all-seven cofacial orders=0")
    print("three-good deficit multisets:", dict(sorted(three_good.items())))


if __name__ == "__main__":
    main()
