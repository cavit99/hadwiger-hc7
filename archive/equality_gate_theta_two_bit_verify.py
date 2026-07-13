#!/usr/bin/env python3
"""Independent exhaustive certificate for the FwJG? exact-block spectrum.

The script deliberately imports none of the packet-atlas or spectra code.
It constructs all set partitions of the seven boundary labels directly,
filters the proper six-colour states, and checks every Property-B colouring.
"""

from __future__ import annotations

from itertools import combinations


LABELS = tuple(range(7))
MISSING = {
    (0, 1),
    (0, 2),
    (0, 5),
    (1, 2),
    (1, 5),
    (2, 4),
    (4, 5),
}


def canonical(partition: tuple[tuple[int, ...], ...]) -> tuple[tuple[int, ...], ...]:
    return tuple(sorted((tuple(sorted(block)) for block in partition), key=lambda b: b[0]))


def set_partitions(vertices: tuple[int, ...]):
    if not vertices:
        yield ()
        return
    first, *rest = vertices
    for partition in set_partitions(tuple(rest)):
        yield canonical(((first,),) + partition)
        for index in range(len(partition)):
            enlarged = list(partition)
            enlarged[index] = tuple(sorted((first,) + enlarged[index]))
            yield canonical(tuple(enlarged))


def independent(block: tuple[int, ...]) -> bool:
    return all(tuple(sorted(edge)) in MISSING for edge in combinations(block, 2))


def fmt(state: tuple[tuple[int, ...], ...]) -> str:
    return "|".join("".join(map(str, block)) for block in state)


def verify_model(
    edges: set[tuple[int, int]],
    bags: tuple[tuple[int, ...], ...],
) -> None:
    edges = {tuple(sorted(edge)) for edge in edges}
    bag_sets = tuple(set(bag) for bag in bags)
    assert len(bag_sets) == 7 and all(bag_sets)
    assert all(
        bag_sets[i].isdisjoint(bag_sets[j])
        for i, j in combinations(range(7), 2)
    )
    for bag in bag_sets:
        reached = {next(iter(bag))}
        while True:
            expanded = reached | {
                y
                for x in reached
                for y in bag
                if tuple(sorted((x, y))) in edges
            }
            if expanded == reached:
                break
            reached = expanded
        assert reached == bag
    assert all(
        any(tuple(sorted((x, y))) in edges for x in bag_sets[i] for y in bag_sets[j])
        for i, j in combinations(range(7), 2)
    )


def verify_crossbar_models() -> None:
    boundary = set(combinations(LABELS, 2)) - MISSING
    helper = {(7, vertex) for vertex in LABELS}
    systems = (
        (
            ((0, 5), (1, 2)),
            {
                (0, 2): ((0,), (3,), (6,), (7,), (5, 8), (2, 10), (1, 4, 9)),
                (1, 5): ((1,), (3,), (6,), (7,), (2, 9), (5, 10), (0, 4, 8)),
                (2, 4): ((2,), (3,), (6,), (7,), (5, 8), (1, 9), (0, 4, 10)),
                (4, 5): ((3,), (4,), (6,), (7,), (0, 8), (1, 9), (2, 5, 10)),
            },
        ),
        (
            ((1, 5), (0, 2)),
            {
                (0, 5): ((0,), (3,), (6,), (7,), (2, 9), (5, 10), (1, 4, 8)),
                (1, 2): ((1,), (3,), (6,), (7,), (5, 8), (2, 10), (0, 4, 9)),
                (2, 4): ((2,), (3,), (6,), (7,), (5, 8), (0, 9), (1, 4, 10)),
                (4, 5): ((3,), (4,), (6,), (7,), (1, 8), (0, 9), (2, 5, 10)),
            },
        ),
    )
    for (first, second), certificates in systems:
        rail_edges = {
            (8, first[0]),
            (8, first[1]),
            (9, second[0]),
            (9, second[1]),
            (8, 9),
        }
        for bridge, bags in certificates.items():
            edges = boundary | helper | rail_edges | {
                (10, bridge[0]),
                (10, bridge[1]),
            }
            verify_model(edges, bags)


def main() -> None:
    states = sorted(
        {
            partition
            for partition in set_partitions(LABELS)
            if len(partition) <= 6 and all(independent(block) for block in partition)
        }
    )
    assert len(states) == 19
    index = {state: position for position, state in enumerate(states)}

    blocks = tuple(
        tuple(vertex for vertex in LABELS if mask >> vertex & 1)
        for mask in range(1, 1 << len(LABELS))
        if independent(tuple(vertex for vertex in LABELS if mask >> vertex & 1))
    )
    hyperedges = tuple(
        tuple(position for position, state in enumerate(states) if block in state)
        for block in blocks
    )
    assert len(blocks) == 16
    assert all(hyperedges)

    valid_masks = []
    for tail in range(1 << (len(states) - 1)):
        colour_mask = tail << 1  # quotient by global shore interchange
        if all(
            any(colour_mask >> position & 1 for position in edge)
            and any(not (colour_mask >> position & 1) for position in edge)
            for edge in hyperedges
        ):
            valid_masks.append(colour_mask)
    assert len(valid_masks) == 12_987

    relation = {}
    for i, j in combinations(range(len(states)), 2):
        xors = {
            ((mask >> i) ^ (mask >> j)) & 1
            for mask in valid_masks
        }
        relation[i, j] = xors

    a0 = canonical(((0, 1, 2), (3,), (4,), (5,), (6,)))
    a1 = canonical(((0, 1, 2), (3,), (4, 5), (6,)))
    b0 = canonical(((0, 1, 5), (2,), (3,), (4,), (6,)))
    b1 = canonical(((0, 1, 5), (2, 4), (3,), (6,)))
    forced_opposite = {
        tuple(sorted((index[a0], index[a1]))),
        tuple(sorted((index[b0], index[b1]))),
    }
    observed_forced_opposite = {
        pair for pair, xors in relation.items() if xors == {1}
    }
    observed_forced_same = {
        pair for pair, xors in relation.items() if xors == {0}
    }
    assert observed_forced_opposite == forced_opposite
    assert not observed_forced_same

    bit_pairs = {
        ((mask >> index[a1]) & 1, (mask >> index[b1]) & 1)
        for mask in valid_masks
    }
    assert bit_pairs == {(0, 0), (0, 1), (1, 0), (1, 1)}

    witnesses = {}
    for bits in sorted(bit_pairs):
        witness = next(
            mask
            for mask in valid_masks
            if ((mask >> index[a1]) & 1, (mask >> index[b1]) & 1) == bits
        )
        witnesses[bits] = tuple(
            fmt(state) for position, state in enumerate(states) if witness >> position & 1
        )

    print("states", len(states), "exact blocks", len(blocks))
    print("Property-B colourings modulo swap", len(valid_masks))
    print(
        "forced opposite",
        tuple((fmt(states[i]), fmt(states[j])) for i, j in sorted(forced_opposite)),
    )
    print("forced same", ())
    print("canonical orientation pairs", tuple(sorted(bit_pairs)))
    for bits, shore_one in witnesses.items():
        print(" witness", bits, "shore-1 states", shore_one)
    verify_crossbar_models()
    print("all eight crossbar plus free-bridge K7 models verified")
    print("independent theta two-bit audit verified")


if __name__ == "__main__":
    main()
