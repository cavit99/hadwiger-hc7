#!/usr/bin/env python3
"""Independent exact verifier for the order-five/overlap-one rigid cell.

This does not import the exploratory overlap-one probe.  It independently
regenerates the local six-support relation, joins the three displayed
supports, computes the monotone minima and their category orbits, and tests
the complete audited seven-terminal kernel catalogue.  Every positive K7
decision returns branch sets which are checked directly.
"""

from __future__ import annotations

import collections
import functools
import hashlib
import itertools

from hc7_overlap_two_order_six_adaptive_kernel_probe import (
    exact_order_eight_families,
    minimal_order_seven_carriers,
)


N = 11
A = tuple(range(6))
I = (0,)
X = (0, 6, 7, 8)
P, Q = 9, 10
T = tuple(range(1, 11))
SUPPORTS = (A, (1, 2, 3, 4, 5, P), (1, 2, 3, 4, 5, Q))
LITERAL_FIVES = (X + (P,), X + (Q,))
PAIRS = tuple(itertools.combinations(range(N), 2))
PAIR_INDEX = {edge: index for index, edge in enumerate(PAIRS)}
LOCAL_PAIRS = tuple(itertools.combinations(range(6), 2))
LOCAL_INDEX = {edge: index for index, edge in enumerate(LOCAL_PAIRS)}


def pair(left: int, right: int) -> tuple[int, int]:
    return (left, right) if left < right else (right, left)


@functools.lru_cache(maxsize=1)
def local_six_relation() -> tuple[tuple[int, int], ...]:
    """All irredundant six-vertex supports of a spanning K5 model."""

    full = (1 << len(LOCAL_PAIRS)) - 1
    answer = []
    for edges in range(1 << len(LOCAL_PAIRS)):
        def adjacent(left: int, right: int) -> bool:
            return bool(edges >> LOCAL_INDEX[pair(left, right)] & 1)

        exact = False
        for left, right in LOCAL_PAIRS:
            if not adjacent(left, right):
                continue
            core = tuple(v for v in range(6) if v not in (left, right))
            if all(
                adjacent(u, v) for u, v in itertools.combinations(core, 2)
            ) and all(
                adjacent(left, root) or adjacent(right, root)
                for root in core
            ):
                exact = True
                break
        literal = any(
            all(adjacent(u, v) for u, v in itertools.combinations(five, 2))
            for five in itertools.combinations(range(6), 5)
        )
        if exact and not literal:
            answer.append((edges, full ^ edges))
    assert len(answer) == 375
    return tuple(answer)


def lifted_patterns(support: tuple[int, ...]) -> tuple[tuple[int, int], ...]:
    image = tuple(
        PAIR_INDEX[pair(support[left], support[right])]
        for left, right in LOCAL_PAIRS
    )
    answer = []
    for local_ones, local_zeros in local_six_relation():
        ones = 0
        zeros = 0
        for index, global_index in enumerate(image):
            if local_ones >> index & 1:
                ones |= 1 << global_index
            if local_zeros >> index & 1:
                zeros |= 1 << global_index
        answer.append((ones, zeros))
    return tuple(answer)


def joined_states() -> set[tuple[int, int]]:
    fixed = 0
    for five in LITERAL_FIVES:
        for edge in itertools.combinations(five, 2):
            fixed |= 1 << PAIR_INDEX[edge]

    # A fixed-order natural join, deliberately distinct from the recursive
    # minimum-domain join in the exploratory probe.
    states = {(fixed, 0)}
    for patterns in map(lifted_patterns, SUPPORTS):
        next_states = set()
        for ones, zeros in states:
            for add_ones, add_zeros in patterns:
                if add_ones & zeros or add_zeros & ones:
                    continue
                next_states.add((ones | add_ones, zeros | add_zeros))
        states = next_states
    return states


def set_partitions(items: tuple[int, ...], count: int):
    blocks: list[list[int]] = []

    def visit(index: int):
        if index == len(items):
            if len(blocks) == count:
                yield tuple(tuple(block) for block in blocks)
            return
        item = items[index]
        for position in range(len(blocks)):
            blocks[position].append(item)
            yield from visit(index + 1)
            blocks[position].pop()
        if len(blocks) < count:
            blocks.append([item])
            yield from visit(index + 1)
            blocks.pop()

    yield from visit(0)


def connected(edges: int, vertices: tuple[int, ...]) -> bool:
    reached = {vertices[0]}
    while True:
        old = len(reached)
        reached.update(
            right
            for left in tuple(reached)
            for right in vertices
            if left != right
            if edges >> PAIR_INDEX[pair(left, right)] & 1
        )
        if len(reached) == old:
            return len(reached) == len(vertices)


def touches(edges: int, left, right) -> bool:
    return any(
        edges >> PAIR_INDEX[pair(u, v)] & 1 for u in left for v in right
    )


def common_state(edges: int) -> bool:
    roots = (0, P, Q)
    available = tuple(vertex for vertex in A if vertex != I[0])
    for size in (4, 5):
        for support in itertools.combinations(available, size):
            for bags in set_partitions(support, 4):
                if not all(connected(edges, bag) for bag in bags):
                    continue
                if not all(
                    touches(edges, left, right)
                    for left, right in itertools.combinations(bags, 2)
                ):
                    continue
                if all(
                    all(touches(edges, (root,), bag) for bag in bags)
                    for root in roots
                ):
                    return True
    return False


def category_generators():
    categories = ((1, 2, 3, 4, 5), (6, 7, 8), (P, Q))
    for category in categories:
        for left, right in zip(category, category[1:]):
            image = list(range(N))
            image[left], image[right] = image[right], image[left]
            yield tuple(image)


def transform(mask: int, image: tuple[int, ...]) -> int:
    answer = 0
    for index, (left, right) in enumerate(PAIRS):
        if mask >> index & 1:
            answer |= 1 << PAIR_INDEX[pair(image[left], image[right])]
    return answer


def minima_and_orbits(noncommon: set[tuple[int, int]]):
    masks = sorted({ones for ones, _ in noncommon}, key=lambda x: (x.bit_count(), x))
    minima = []
    for mask in masks:
        if not any(old & mask == old for old in minima):
            minima.append(mask)
    minimum_set = set(minima)
    generators = tuple(category_generators())
    live = set(minima)
    orbits = []
    while live:
        representative = min(live)
        orbit = {representative}
        frontier = [representative]
        while frontier:
            old = frontier.pop()
            for image in generators:
                new = transform(old, image)
                assert new in minimum_set
                if new not in orbit:
                    orbit.add(new)
                    frontier.append(new)
        orbits.append((representative, orbit))
        live -= orbit
    assert set().union(*(orbit for _, orbit in orbits)) == minimum_set
    return minima, orbits


class WitnessK7:
    """Exact K7 detector on the eleven-object quotient, returning its bags."""

    def __init__(self):
        self.full = (1 << N) - 1
        self.cache: dict[int, tuple[int, ...] | None] = {}

    def __call__(self, edges: int) -> tuple[int, ...] | None:
        if edges not in self.cache:
            self.cache[edges] = self._find(edges)
        answer = self.cache[edges]
        if answer is not None:
            self.validate(edges, answer)
        return answer

    @staticmethod
    def adjacency(edges: int) -> tuple[int, ...]:
        answer = [0] * N
        for index, (left, right) in enumerate(PAIRS):
            if edges >> index & 1:
                answer[left] |= 1 << right
                answer[right] |= 1 << left
        return tuple(answer)

    @staticmethod
    def is_connected(mask: int, adjacency: tuple[int, ...]) -> bool:
        reached = mask & -mask
        while True:
            old = reached
            frontier = reached
            while frontier:
                bit = frontier & -frontier
                reached |= adjacency[bit.bit_length() - 1] & mask
                frontier -= bit
            if reached == old:
                return reached == mask

    @staticmethod
    def sets_touch(left: int, right: int, adjacency: tuple[int, ...]) -> bool:
        while left:
            bit = left & -left
            if adjacency[bit.bit_length() - 1] & right:
                return True
            left -= bit
        return False

    def _find(self, edges: int) -> tuple[int, ...] | None:
        adjacency = self.adjacency(edges)
        # Seven nonempty disjoint bags on eleven objects have at least three
        # singleton bags.  This enumerates all possible singleton cores.
        for singleton_count in range(7, 2, -1):
            other_count = 7 - singleton_count
            for vertices in itertools.combinations(range(N), singleton_count):
                if any(
                    not (adjacency[left] >> right & 1)
                    for left, right in itertools.combinations(vertices, 2)
                ):
                    continue
                singleton_bags = tuple(1 << vertex for vertex in vertices)
                if other_count == 0:
                    return singleton_bags
                core = sum(singleton_bags)
                remainder = self.full ^ core
                candidates = []
                subset = remainder
                while subset:
                    if self.is_connected(subset, adjacency) and all(
                        self.sets_touch(subset, bag, adjacency)
                        for bag in singleton_bags
                    ):
                        candidates.append(subset)
                    subset = (subset - 1) & remainder

                def choose(start: int, chosen: tuple[int, ...], used: int):
                    if len(chosen) == other_count:
                        return chosen
                    for position in range(start, len(candidates)):
                        candidate = candidates[position]
                        if candidate & used:
                            continue
                        if all(
                            self.sets_touch(candidate, old, adjacency)
                            for old in chosen
                        ):
                            answer = choose(
                                position + 1,
                                chosen + (candidate,),
                                used | candidate,
                            )
                            if answer is not None:
                                return answer
                    return None

                chosen = choose(0, (), 0)
                if chosen is not None:
                    return singleton_bags + chosen
        return None

    def validate(self, edges: int, bags: tuple[int, ...]) -> None:
        adjacency = self.adjacency(edges)
        assert len(bags) == 7 and all(bags)
        assert all(not (left & right) for left, right in itertools.combinations(bags, 2))
        assert all(self.is_connected(bag, adjacency) for bag in bags)
        assert all(
            self.sets_touch(left, right, adjacency)
            for left, right in itertools.combinations(bags, 2)
        )


def lift(mask: int, labels: tuple[int, ...]) -> int:
    answer = 0
    for index, (left, right) in enumerate(itertools.combinations(range(7), 2)):
        if mask >> index & 1:
            answer |= 1 << PAIR_INDEX[pair(labels[left], labels[right])]
    return answer


def digest(values) -> str:
    return hashlib.sha256("\n".join(map(str, values)).encode()).hexdigest()


def main() -> None:
    states = joined_states()
    noncommon = {(ones, zeros) for ones, zeros in states if not common_state(ones)}
    minima, orbits = minima_and_orbits(noncommon)
    assert len(states) == 8055
    assert len(noncommon) == 5410
    assert len(minima) == 400
    assert collections.Counter(mask.bit_count() for mask in minima) == {
        29: 10,
        31: 30,
        33: 360,
    }
    assert sorted(len(orbit) for _, orbit in orbits) == [10, 30, 60, 60, 120, 120]

    order_seven = minimal_order_seven_carriers()
    order_eight = exact_order_eight_families()
    assert len(order_seven) == 5495
    assert len(order_eight) == 30600
    detector = WitnessK7()
    guard_seven: list[int] = []
    guard_eight: list[tuple[int, ...]] = []
    certificates = []

    for orbit_index, (ones, orbit) in enumerate(orbits):
        chosen = None
        for reserved in itertools.combinations(T, 3):
            labels = tuple(vertex for vertex in T if vertex not in reserved)
            bad_seven = next(
                (
                    carrier
                    for carrier in guard_seven
                    if detector(ones | lift(carrier, labels)) is None
                ),
                None,
            )
            if bad_seven is None:
                bad_seven = next(
                    (
                        carrier
                        for carrier in order_seven
                        if detector(ones | lift(carrier, labels)) is None
                    ),
                    None,
                )
                if bad_seven is not None and bad_seven not in guard_seven:
                    guard_seven.append(bad_seven)
            if bad_seven is not None:
                continue

            def family_closes(family: tuple[int, ...]) -> bool:
                return any(
                    detector(ones | lift(option, labels)) is not None
                    for option in family
                )

            bad_eight = next(
                (family for family in guard_eight if not family_closes(family)),
                None,
            )
            if bad_eight is None:
                bad_eight = next(
                    (family for family in order_eight if not family_closes(family)),
                    None,
                )
                if bad_eight is not None and bad_eight not in guard_eight:
                    guard_eight.append(bad_eight)
            if bad_eight is None:
                chosen = reserved
                break
        assert chosen is not None, (orbit_index, ones)
        certificates.append((orbit_index, ones, len(orbit), chosen))

    assert [certificate[3] for certificate in certificates] == [
        (1, 2, 9),
        (1, 2, 3),
        (1, 2, 3),
        (1, 2, 3),
        (1, 2, 3),
        (1, 2, 3),
    ]
    state_digest = digest(sorted(noncommon))
    minimum_digest = digest(sorted(minima))
    order7_digest = digest(order_seven)
    order8_digest = digest(order_eight)
    certificate_digest = digest(certificates)
    assert state_digest == "bbcd05839b15cabb5a6d7b2ef1a7e3743154be9d12d3849903a80d479369a907"
    assert minimum_digest == "1f62f3282bb2134f4e422cec810b280c059476a849d474db53f6c69129cf2343"
    assert order7_digest == "16aad7592a7f5412ab7b254434ca7f02b6454b2a8ba644d962f9f283788edec1"
    assert order8_digest == "0189701148e17b1f792e83ec1737f753c23b99dcb52c149808428602f12021e1"
    assert certificate_digest == "384761c399bd17b1c7d574801703236d3d50c8730af018e87458cbfd7511e033"
    print("local_six", len(local_six_relation()))
    print("joined", len(states))
    print("common", len(states) - len(noncommon))
    print("noncommon", len(noncommon))
    print("minimal_one_masks", len(minima))
    print("minimal_profile", dict(sorted(collections.Counter(mask.bit_count() for mask in minima).items())))
    print("minimal_orbits", len(orbits))
    print("orbit_sizes", sorted(len(orbit) for _, orbit in orbits))
    print("kernel_catalogues", len(order_seven), len(order_eight))
    print("certificates", certificates)
    print("state_digest", state_digest)
    print("minimum_digest", minimum_digest)
    print("order7_digest", order7_digest)
    print("order8_digest", order8_digest)
    print("certificate_digest", certificate_digest)
    print("validated_positive_masks", sum(value is not None for value in detector.cache.values()))
    print("cached_negative_masks", sum(value is None for value in detector.cache.values()))
    print("overlap-one order-five seven-terminal-kernel decoder: verified")


if __name__ == "__main__":
    main()
