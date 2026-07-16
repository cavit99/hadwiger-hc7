#!/usr/bin/env python3
"""Test the exact eight-terminal bundle on the last positive-overlap cell.

The complete noncommon relation has 8,845,350 forced-edge masks.  Minor
existence is monotone in those edges, and the relation factors across the
two disjoint support modules.  Consequently it is enough to test the
132,000 products of module-minimal masks.  Quotienting first by S5 and S4
and then by the simultaneous interchange of p and q leaves 142 cases.

This is an active proof-producing computation.  The structural
eight-terminal kernel theorem is a separate input.
"""

from __future__ import annotations

import argparse
import collections
import functools
import hashlib
import itertools
import shutil
import subprocess
import time

N = 12
A_PRIVATE = (1, 2, 3, 4, 5)
X_PRIVATE = (6, 7, 8, 9)
P, Q = 10, 11
TERMINALS = tuple(range(1, 12))
A = tuple(range(6))
I = (0,)
X = (0, 6, 7, 8, 9)
SUPPORTS = (
    A,
    X + (P,),
    X + (Q,),
    A_PRIVATE + (P,),
    A_PRIVATE + (Q,),
)
PAIRS = tuple(itertools.combinations(range(N), 2))
PAIR_INDEX = {edge: index for index, edge in enumerate(PAIRS)}
ABSTRACT_PAIRS = tuple(itertools.combinations(range(8), 2))
ABSTRACT_PAIR_INDEX = {
    edge: index for index, edge in enumerate(ABSTRACT_PAIRS)
}


def pair(left: int, right: int) -> tuple[int, int]:
    return (left, right) if left < right else (right, left)


def local_allowed_six() -> tuple[tuple[int, int], ...]:
    local_pairs = tuple(itertools.combinations(range(6), 2))
    answer = []
    for edges in range(1 << 15):
        def adjacent(left, right):
            return bool(edges >> local_pairs.index(pair(left, right)) & 1)

        exact_state = False
        for left, right in local_pairs:
            if not adjacent(left, right):
                continue
            core = tuple(
                vertex for vertex in range(6) if vertex not in (left, right)
            )
            if all(
                adjacent(first, second)
                for first, second in itertools.combinations(core, 2)
            ) and all(
                adjacent(left, vertex) or adjacent(right, vertex)
                for vertex in core
            ):
                exact_state = True
                break
        literal_five = any(
            all(
                adjacent(left, right)
                for left, right in itertools.combinations(five, 2)
            )
            for five in itertools.combinations(range(6), 5)
        )
        if exact_state and not literal_five:
            answer.append((edges, ((1 << 15) - 1) ^ edges))
    assert len(answer) == 375
    return tuple(answer)


LOCAL_SIX = local_allowed_six()


def patterns(support: tuple[int, ...]):
    positions = tuple(
        PAIR_INDEX[pair(support[left], support[right])]
        for left, right in itertools.combinations(range(6), 2)
    )
    return tuple(
        (
            sum(1 << positions[index] for index in range(15) if ones >> index & 1),
            sum(1 << positions[index] for index in range(15) if zeros >> index & 1),
        )
        for ones, zeros in LOCAL_SIX
    )


def partitions(items: tuple[int, ...], block_count: int):
    blocks: list[list[int]] = []

    def visit(position: int):
        if position == len(items):
            if len(blocks) == block_count:
                yield tuple(tuple(block) for block in blocks)
            return
        item = items[position]
        for block in blocks:
            block.append(item)
            yield from visit(position + 1)
            block.pop()
        if len(blocks) < block_count:
            blocks.append([item])
            yield from visit(position + 1)
            blocks.pop()

    yield from visit(0)


def mask_connected(edges: int, vertices: tuple[int, ...]) -> bool:
    reached = {vertices[0]}
    while True:
        old = len(reached)
        reached.update(
            right
            for left in tuple(reached)
            for right in vertices
            if right not in reached
            and edges >> PAIR_INDEX[pair(left, right)] & 1
        )
        if len(reached) == old:
            return len(reached) == len(vertices)


def mask_touches(edges: int, left, right) -> bool:
    return any(
        edges >> PAIR_INDEX[pair(first, second)] & 1
        for first in left
        for second in right
    )


def common_rooted_k4(edges: int):
    for root in I:
        available = tuple(vertex for vertex in A if vertex != root)
        for support_size in (4, 5):
            for support in itertools.combinations(available, support_size):
                for bags in partitions(support, 4):
                    if not all(mask_connected(edges, bag) for bag in bags):
                        continue
                    if not all(
                        mask_touches(edges, left, right)
                        for left, right in itertools.combinations(bags, 2)
                    ):
                        continue
                    if all(
                        all(
                            any(
                                edges >> PAIR_INDEX[pair(named, vertex)] & 1
                                for vertex in bag
                            )
                            for bag in bags
                        )
                        for named in (root, P, Q)
                    ):
                        return root, bags
    return None


def images():
    categories = (A_PRIVATE, X_PRIVATE, (P, Q))
    for permutations in itertools.product(
        *(tuple(itertools.permutations(category)) for category in categories)
    ):
        image = list(range(N))
        for category, permutation in zip(categories, permutations):
            for old, new in zip(category, permutation):
                image[old] = new
        yield tuple(image)


def transform(mask: int, image: tuple[int, ...]) -> int:
    answer = 0
    for index, (left, right) in enumerate(PAIRS):
        if mask >> index & 1:
            answer |= 1 << PAIR_INDEX[pair(image[left], image[right])]
    return answer


def join(supports: tuple[tuple[int, ...], ...]) -> set[tuple[int, int]]:
    states = {(0, 0)}
    for choices in map(patterns, supports):
        states = {
            (ones | present, zeros | absent)
            for ones, zeros in states
            for present, absent in choices
            if not (present & zeros or absent & ones)
        }
    return states


def inclusion_minima(values) -> tuple[int, ...]:
    answer: list[int] = []
    for value in sorted(set(values), key=lambda mask: (mask.bit_count(), mask)):
        if not any(value & old == old for old in answer):
            answer.append(value)
    return tuple(answer)


def category_image(category, permutation) -> tuple[int, ...]:
    image = list(range(N))
    for old, new in zip(category, permutation):
        image[old] = new
    return tuple(image)


def quotient(values: tuple[int, ...], category: tuple[int, ...]):
    images = tuple(
        category_image(category, permutation)
        for permutation in itertools.permutations(category)
    )
    canonical = {
        value: min(transform(value, image) for image in images)
        for value in values
    }
    representatives = tuple(sorted(set(canonical.values())))
    weights = collections.Counter(canonical.values())
    return canonical, representatives, weights


def minimal_orbits():
    a_supports = (
        A,
        A_PRIVATE + (P,),
        A_PRIVATE + (Q,),
    )
    x_supports = (
        X + (P,),
        X + (Q,),
    )
    a_states = join(a_supports)
    x_states = join(x_supports)
    assert len(a_states) == 8_055
    assert len(x_states) == 1_635

    common_projection = sum(
        1 << PAIR_INDEX[edge]
        for edge in itertools.combinations(A + (P, Q), 2)
    )

    @functools.lru_cache(maxsize=None)
    def common(projected: int) -> bool:
        return common_rooted_k4(projected) is not None

    a_noncommon = tuple(
        ones
        for ones, _zeros in a_states
        if not common(ones & common_projection)
    )
    assert len(a_noncommon) == 5_410
    a_minima = inclusion_minima(a_noncommon)
    x_minima = inclusion_minima(ones for ones, _zeros in x_states)
    assert len(a_minima) == 400
    assert len(x_minima) == 330

    a_canonical, a_representatives, a_weights = quotient(
        a_minima, A_PRIVATE
    )
    x_canonical, x_representatives, x_weights = quotient(
        x_minima, X_PRIVATE
    )
    assert len(a_representatives) == 8
    assert len(x_representatives) == 27

    swap = list(range(N))
    swap[P], swap[Q] = Q, P
    swap = tuple(swap)
    a_index = {mask: index for index, mask in enumerate(a_representatives)}
    x_index = {mask: index for index, mask in enumerate(x_representatives)}
    a_swap = tuple(
        a_index[a_canonical[transform(mask, swap)]]
        for mask in a_representatives
    )
    x_swap = tuple(
        x_index[x_canonical[transform(mask, swap)]]
        for mask in x_representatives
    )

    answer = []
    seen = set()
    total_weight = 0
    for a_position, a_mask in enumerate(a_representatives):
        for x_position, x_mask in enumerate(x_representatives):
            pair = (a_position, x_position)
            mate = (a_swap[a_position], x_swap[x_position])
            representative = min(pair, mate)
            if representative in seen:
                continue
            seen.add(representative)
            weight = a_weights[a_mask] * x_weights[x_mask]
            if mate != pair:
                weight += (
                    a_weights[a_representatives[mate[0]]]
                    * x_weights[x_representatives[mate[1]]]
                )
            total_weight += weight
            answer.append((a_mask | x_mask, weight, representative))
    assert len(answer) == 142
    assert total_weight == 132_000
    return tuple(answer)


def digest_orbits(orbits) -> str:
    stream = "\n".join(
        f"{ones}:{weight}:{positions[0]}:{positions[1]}"
        for ones, weight, positions in orbits
    ).encode()
    return hashlib.sha256(stream).hexdigest()


def fixed_width_digest(items, width: int) -> str:
    digest = hashlib.sha256()
    for item in sorted(items):
        digest.update(int(item).to_bytes(width, "big"))
    return digest.hexdigest()


def reserve_order(ones: int, all_four: bool = False):
    choices = tuple(
        itertools.combinations(range(N) if all_four else TERMINALS, 4 if all_four else 3)
    )
    return tuple(
        sorted(
            choices,
            key=lambda reserve: (
                -sum(
                    bool(
                        ones
                        >> PAIR_INDEX[pair(left, right)]
                        & 1
                    )
                    for left, right in itertools.combinations(reserve, 2)
                ),
                -(0 in reserve),
                -sum(vertex in A_PRIVATE for vertex in reserve),
                reserve,
            ),
        )
    )


class ExactK7:
    """Exact K7 detector on at most twelve quotient objects."""

    def __init__(self):
        self.cache = {}

    def __call__(self, edges: int) -> bool:
        answer = self.cache.get(edges)
        if answer is None:
            answer = self.test(edges)
            self.cache[edges] = answer
        return answer

    @staticmethod
    def test(edges: int) -> bool:
        adjacency = [0] * N
        for index, (left, right) in enumerate(PAIRS):
            if edges >> index & 1:
                adjacency[left] |= 1 << right
                adjacency[right] |= 1 << left

        @functools.lru_cache(maxsize=None)
        def connected(mask: int) -> bool:
            reached = mask & -mask
            while True:
                old = reached
                scan = reached
                neighbours = 0
                while scan:
                    bit = scan & -scan
                    neighbours |= adjacency[bit.bit_length() - 1]
                    scan -= bit
                reached |= neighbours & mask
                if reached == old:
                    return reached == mask

        @functools.lru_cache(maxsize=None)
        def touches(left: int, right: int) -> bool:
            scan = left
            while scan:
                bit = scan & -scan
                if adjacency[bit.bit_length() - 1] & right:
                    return True
                scan -= bit
            return False

        full = (1 << N) - 1
        # Any seven-bag model on at most twelve used objects has at least
        # two singleton bags.  Choose its exact singleton core; every bag
        # left outside that core then has size at least two.
        for core_size in range(7, 1, -1):
            bag_count = 7 - core_size
            for core_vertices in itertools.combinations(range(N), core_size):
                if any(
                    not (adjacency[left] >> right & 1)
                    for left, right in itertools.combinations(core_vertices, 2)
                ):
                    continue
                if bag_count == 0:
                    return True
                core = sum(1 << vertex for vertex in core_vertices)
                remainder = full ^ core
                maximum_bag_size = remainder.bit_count() - 2 * (bag_count - 1)
                candidates = []
                subset = remainder
                while subset:
                    if (
                        2 <= subset.bit_count() <= maximum_bag_size
                        and connected(subset)
                        and all(
                            touches(subset, 1 << vertex)
                            for vertex in core_vertices
                        )
                    ):
                        candidates.append(subset)
                    subset = (subset - 1) & remainder

                def search(start: int, chosen: tuple[int, ...], used: int) -> bool:
                    missing = bag_count - len(chosen)
                    if missing == 0:
                        return True
                    if (remainder & ~used).bit_count() < 2 * missing:
                        return False
                    for position in range(start, len(candidates)):
                        candidate = candidates[position]
                        if candidate & used:
                            continue
                        if all(touches(candidate, old) for old in chosen) and search(
                            position + 1,
                            chosen + (candidate,),
                            used | candidate,
                        ):
                            return True
                    return False

                if search(0, (), 0):
                    return True
        return False


def lift(mask: int, labels: tuple[int, ...]) -> int:
    return sum(
        1 << PAIR_INDEX[pair(labels[left], labels[right])]
        for index, (left, right) in enumerate(ABSTRACT_PAIRS)
        if mask >> index & 1
    )


def first_bad_order_eight(ones, reserve, carriers, detector):
    universe = range(N) if len(reserve) == 4 else TERMINALS
    labels = tuple(vertex for vertex in universe if vertex not in reserve)
    assert len(labels) == 8
    for index, abstract_carrier in enumerate(carriers):
        carrier = lift(abstract_carrier, labels)
        if not detector(ones | carrier):
            return index, abstract_carrier, carrier
    return None


def state_stabilizer(ones: int):
    return tuple(
        image
        for image in images()
        if transform(ones, image) == ones
    )


def subset_orbits(stabilizer, universe, size):
    live = set(itertools.combinations(universe, size))
    answer = []
    while live:
        representative = min(live)
        orbit = {
            tuple(sorted(image[vertex] for vertex in representative))
            for image in stabilizer
        }
        assert orbit <= live | (set(itertools.combinations(universe, size)) - live)
        answer.append((representative, len(orbit)))
        live -= orbit
    return tuple(answer)


def abstract_adjacency(mask: int):
    adjacency = [0] * 8
    for index, (left, right) in enumerate(ABSTRACT_PAIRS):
        if mask >> index & 1:
            adjacency[left] |= 1 << right
            adjacency[right] |= 1 << left
    return tuple(adjacency)


def connected_after_removal(adjacency, removed: int) -> bool:
    remaining = 0xFF & ~removed
    if not remaining:
        return True
    reached = remaining & -remaining
    while True:
        old = reached
        frontier = reached
        neighbours = 0
        while frontier:
            bit = frontier & -frontier
            neighbours |= adjacency[bit.bit_length() - 1]
            frontier -= bit
        reached |= neighbours & remaining
        if reached == old:
            return reached == remaining


def three_connected_mask(mask: int) -> bool:
    adjacency = abstract_adjacency(mask)
    return all(
        connected_after_removal(
            adjacency, sum(1 << vertex for vertex in removed)
        )
        for size in range(3)
        for removed in itertools.combinations(range(8), size)
    )


def edge_minimal_three_connected(mask: int) -> bool:
    if not three_connected_mask(mask):
        return False
    return all(
        not three_connected_mask(mask & ~(1 << index))
        for index in range(28)
        if mask >> index & 1
    )


def graph6_adjacency(line: bytes) -> tuple[int, ...]:
    data = line.strip()
    assert data and data[0] != ord(">")
    order = data[0] - 63
    assert order == 8
    bits = []
    for value in data[1:]:
        value -= 63
        bits.extend((value >> shift) & 1 for shift in range(5, -1, -1))
    adjacency = [0] * order
    position = 0
    for right in range(1, order):
        for left in range(right):
            if bits[position]:
                adjacency[left] |= 1 << right
                adjacency[right] |= 1 << left
            position += 1
    return tuple(adjacency)


def adjacency_mask(adjacency: tuple[int, ...]) -> int:
    return sum(
        1 << ABSTRACT_PAIR_INDEX[(left, right)]
        for left, right in ABSTRACT_PAIRS
        if adjacency[left] >> right & 1
    )


def relabel_abstract(mask: int, image: tuple[int, ...]) -> int:
    return sum(
        1 << ABSTRACT_PAIR_INDEX[pair(image[left], image[right])]
        for index, (left, right) in enumerate(ABSTRACT_PAIRS)
        if mask >> index & 1
    )


def order_eight_carriers() -> tuple[int, ...]:
    """Generate the exact labelled order-eight catalogue using nauty."""

    if shutil.which("geng") is None:
        raise SystemExit("nauty's `geng` executable is required")
    process = subprocess.Popen(
        ["geng", "-cq", "-d3", "8"], stdout=subprocess.PIPE
    )
    assert process.stdout is not None
    bases = []
    for line in process.stdout:
        mask = adjacency_mask(graph6_adjacency(line))
        if edge_minimal_three_connected(mask):
            bases.append(mask)
    if process.wait() != 0:
        raise RuntimeError("geng failed")
    assert len(bases) == 18
    carriers = {
        relabel_abstract(mask, image)
        for mask in bases
        for image in itertools.permutations(range(8))
    }
    assert len(carriers) == 196_976
    return tuple(sorted(carriers))


def smt_has_k7(edges: int) -> bool:
    """Independent labelled-bag encoding, used only for the RED audit."""

    import z3

    edge_list = tuple(
        edge
        for index, edge in enumerate(PAIRS)
        if edges >> index & 1
    )
    adjacency = [set() for _ in range(N)]
    for left, right in edge_list:
        adjacency[left].add(right)
        adjacency[right].add(left)

    solver = z3.Solver()
    member = [
        [z3.Bool(f"member_{vertex}_{bag}") for bag in range(7)]
        for vertex in range(N)
    ]
    root = [
        [z3.Bool(f"root_{vertex}_{bag}") for bag in range(7)]
        for vertex in range(N)
    ]
    rank = [
        [z3.Int(f"rank_{vertex}_{bag}") for bag in range(7)]
        for vertex in range(N)
    ]
    for vertex in range(N):
        solver.add(
            z3.PbLe([(member[vertex][bag], 1) for bag in range(7)], 1)
        )

    root_value = []
    for bag in range(7):
        solver.add(
            z3.PbEq([(root[vertex][bag], 1) for vertex in range(N)], 1)
        )
        root_value.append(
            z3.Sum(
                [
                    vertex * z3.If(root[vertex][bag], 1, 0)
                    for vertex in range(N)
                ]
            )
        )
        for vertex in range(N):
            solver.add(z3.Implies(root[vertex][bag], member[vertex][bag]))
            # The root is the least literal vertex of its bag.  Together
            # with increasing roots this only breaks bag-label symmetry.
            solver.add(
                z3.Implies(
                    root[vertex][bag],
                    z3.And(
                        rank[vertex][bag] == 0,
                        *[
                            z3.Not(member[old][bag])
                            for old in range(vertex)
                        ],
                    ),
                )
            )
            solver.add(
                z3.Implies(
                    member[vertex][bag],
                    z3.And(
                        rank[vertex][bag] >= 0,
                        rank[vertex][bag] < N,
                    ),
                )
            )
            solver.add(
                z3.Implies(
                    z3.And(
                        member[vertex][bag], z3.Not(root[vertex][bag])
                    ),
                    z3.Or(
                        *[
                            z3.And(
                                member[old][bag],
                                rank[old][bag] < rank[vertex][bag],
                            )
                            for old in adjacency[vertex]
                        ]
                    ),
                )
            )
    for bag in range(6):
        solver.add(root_value[bag] < root_value[bag + 1])
    for first in range(7):
        for second in range(first + 1, 7):
            solver.add(
                z3.Or(
                    *[
                        z3.And(member[left][first], member[right][second])
                        for left, right in edge_list
                    ],
                    *[
                        z3.And(member[right][first], member[left][second])
                        for left, right in edge_list
                    ],
                )
            )
    return solver.check() == z3.sat


def audit_first_obstruction(order_eight) -> None:
    ones, weight, positions = minimal_orbits()[0]
    assert weight == 40 and positions == (0, 0)
    local_masks = tuple(
        sum(
            1 << index
            for index, (left, right) in enumerate(
                itertools.combinations(range(6), 2)
            )
            if ones
            >> PAIR_INDEX[pair(support[left], support[right])]
            & 1
        )
        for support in SUPPORTS
    )
    assert local_masks == (0x7FC3, 0x17FE, 0x17FE, 0x17FE, 0x17FE)
    assert all(
        (mask, ((1 << 15) - 1) ^ mask) in LOCAL_SIX
        for mask in local_masks
    )
    assert common_rooted_k4(ones) is None
    stabilizer = state_stabilizer(ones)
    assert len(stabilizer) == 144
    reserve_orbits = subset_orbits(stabilizer, range(N), 4)
    assert len(reserve_orbits) == 71
    assert sum(weight for _reserve, weight in reserve_orbits) == 495

    detector = ExactK7()
    records = []
    for index, (reserve, orbit_weight) in enumerate(reserve_orbits):
        bad = first_bad_order_eight(
            ones, reserve, order_eight, detector
        )
        assert bad is not None
        carrier_index, abstract_carrier, lifted_carrier = bad
        assert edge_minimal_three_connected(abstract_carrier)
        graph = ones | lifted_carrier
        assert not detector(graph)
        assert not smt_has_k7(graph)
        records.append(
            (
                reserve,
                orbit_weight,
                carrier_index,
                abstract_carrier,
                lifted_carrier,
                graph,
            )
        )
        print("AUDIT", index, *records[-1], flush=True)

    digest = hashlib.sha256(
        "\n".join(
            ":".join(
                (
                    ",".join(map(str, reserve)),
                    str(orbit_weight),
                    str(carrier_index),
                    str(abstract_carrier),
                    str(lifted_carrier),
                    str(graph),
                )
            )
            for (
                reserve,
                orbit_weight,
                carrier_index,
                abstract_carrier,
                lifted_carrier,
                graph,
            ) in records
        ).encode()
    ).hexdigest()
    print("obstruction_state", ones)
    print("obstruction_state_hex", hex(ones))
    print("local_masks", tuple(hex(mask) for mask in local_masks))
    print("stabilizer", len(stabilizer))
    print("reserve_four_orbits", len(reserve_orbits))
    print("reserve_four_weight", sum(record[1] for record in records))
    print("witness_digest", digest)
    print("exact_detector_cache", len(detector.cache))
    print("independent_smt_unsat", len(records))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--start", type=int, default=0)
    parser.add_argument("--stop", type=int, default=142)
    parser.add_argument("--reserve-limit", type=int, default=165)
    parser.add_argument("--all-four", action="store_true")
    parser.add_argument("--audit-first-obstruction", action="store_true")
    args = parser.parse_args()

    orbits = minimal_orbits()
    print("minimal_masks 132000", flush=True)
    print("minimal_orbits", len(orbits), flush=True)
    print("orbit_digest", digest_orbits(orbits), flush=True)
    order_eight = tuple(
        sorted(order_eight_carriers(), key=lambda mask: (mask.bit_count(), mask))
    )
    print("order8_carriers", len(order_eight), flush=True)
    catalogue_digest = fixed_width_digest(order_eight, 4)
    assert catalogue_digest == (
        "2191c87cc229cbf109b19bf66badb40c115838c5b1350709c64fd9a2ec2f020d"
    )
    print("order8_digest", catalogue_digest, flush=True)
    if args.audit_first_obstruction:
        audit_first_obstruction(order_eight)
        return

    for orbit_index in range(args.start, min(args.stop, len(orbits))):
        ones, weight, positions = orbits[orbit_index]
        detector = ExactK7()
        started = time.monotonic()
        valid = None
        failures = []
        for reserve in reserve_order(ones, args.all_four)[: args.reserve_limit]:
            bad = first_bad_order_eight(
                ones, reserve, order_eight, detector
            )
            if bad is None:
                valid = reserve
                break
            failures.append((reserve, bad[0], bad[2]))
        print(
            "ORBIT",
            orbit_index,
            "module_positions",
            positions,
            "weight",
            weight,
            "edges",
            ones.bit_count(),
            "reserve",
            valid,
            "tested_reserves",
            len(failures) + (valid is not None),
            "cache",
            len(detector.cache),
            "seconds",
            round(time.monotonic() - started, 3),
            flush=True,
        )
        if valid is None:
            print("FIRST_UNCLOSED", orbit_index, ones, failures, flush=True)
            break


if __name__ == "__main__":
    main()
