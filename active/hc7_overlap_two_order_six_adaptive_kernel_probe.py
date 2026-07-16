#!/usr/bin/env python3
"""CEGAR probe for the adaptive seven-terminal kernel rung.

For each orbit of the normalized order-six-arm/overlap-two relation, seek a
reserved pair for which both of the following universal checks hold:

* every labelled edge-minimal three-connected order-seven carrier closes;
* every exact order-eight terminal-irreducible kernel closes after its unique
  nonterminal is absorbed into some adjacent terminal bag.

The order-eight catalogue is *exact*.  In particular, this script does not
quantify over arbitrary cycle/charged-four pairs, many of which cannot occur
in a three-connected terminal-irreducible kernel.

This is the canonical finite verifier for the audited local closure theorem.
"""

from __future__ import annotations

import argparse
import collections
import functools
import hashlib
import itertools
import time

import hc7_overlap_three_six_terminal_kernel_verify as connectivity
import hc7_cross_arm_overlap_three_kernel_decoder as relation


LOCAL_PAIRS, LOCAL_INDEX = connectivity.pair_data(7)
EIGHT_PAIRS, EIGHT_INDEX = connectivity.pair_data(8)


def build_cell():
    n = 11
    a = tuple(range(6))
    common = (0, 1)
    x = (0, 1, 6, 7, 8)
    p, q = 9, 10
    terminals = tuple(vertex for vertex in range(n) if vertex not in common)
    supports = [a, x + (p,), x + (q,)]
    for omitted in common:
        base = tuple(vertex for vertex in a if vertex != omitted)
        supports.extend((base + (p,), base + (q,)))
    return n, a, common, x, p, q, terminals, tuple(supports)


def global_patterns(support, pair_index):
    local_pairs = tuple(itertools.combinations(range(6), 2))
    indices = tuple(
        pair_index[tuple(sorted((support[left], support[right])))]
        for left, right in local_pairs
    )
    return tuple(
        (
            sum(
                1 << indices[index]
                for index in range(15)
                if local_ones >> index & 1
            ),
            sum(
                1 << indices[index]
                for index in range(15)
                if local_zeros >> index & 1
            ),
        )
        for local_ones, local_zeros in relation.LOCAL_SIX
    )


def joined_states():
    cell = build_cell()
    n, _a, _common, _x, _p, _q, _terminals, supports = cell
    pairs = tuple(itertools.combinations(range(n), 2))
    pair_index = {edge: index for index, edge in enumerate(pairs)}
    constraints = tuple(global_patterns(support, pair_index) for support in supports)
    states = set()

    def visit(done, ones, zeros):
        if ones & zeros:
            return
        if len(done) == len(constraints):
            states.add((ones, zeros))
            return
        selected = None
        compatible = None
        for index, patterns in enumerate(constraints):
            if index in done:
                continue
            options = tuple(
                pattern
                for pattern in patterns
                if not (pattern[0] & zeros or pattern[1] & ones)
            )
            if compatible is None or len(options) < len(compatible):
                selected, compatible = index, options
        seen = set()
        for pattern_ones, pattern_zeros in compatible:
            new = ones | pattern_ones, zeros | pattern_zeros
            if new in seen:
                continue
            seen.add(new)
            visit(done | {selected}, *new)

    visit(frozenset(), 0, 0)
    return cell, pairs, pair_index, states


def category_automorphisms():
    categories = ((0, 1), (2, 3, 4, 5), (6, 7, 8), (9, 10))
    for images in itertools.product(
        *(tuple(itertools.permutations(category)) for category in categories)
    ):
        image = list(range(11))
        for category, permuted in zip(categories, images):
            for old, new in zip(category, permuted):
                image[old] = new
        yield tuple(image)


def transformed_mask(mask, image, pairs, pair_index):
    return sum(
        1 << pair_index[tuple(sorted((image[left], image[right])))]
        for index, (left, right) in enumerate(pairs)
        if mask >> index & 1
    )


class FastK7:
    """Exact K7-minor detector for the eleven-object quotient."""

    def __init__(self, order, pairs, pair_index):
        self.order = order
        self.pairs = pairs
        self.full = (1 << order) - 1
        self.cache = {}

    def __call__(self, edges):
        answer = self.cache.get(edges)
        if answer is None:
            answer = self._test(edges)
            self.cache[edges] = answer
        return answer

    def _test(self, edges):
        adj = [0] * self.order
        for index, (left, right) in enumerate(self.pairs):
            if edges >> index & 1:
                adj[left] |= 1 << right
                adj[right] |= 1 << left

        def connected(mask):
            reached = mask & -mask
            while True:
                old = reached
                frontier = reached
                neighbours = 0
                while frontier:
                    bit = frontier & -frontier
                    neighbours |= adj[bit.bit_length() - 1]
                    frontier -= bit
                reached |= neighbours & mask
                if reached == old:
                    return reached == mask

        def touches(left, right):
            frontier = left
            while frontier:
                bit = frontier & -frontier
                if adj[bit.bit_length() - 1] & right:
                    return True
                frontier -= bit
            return False

        # Seven bags on eleven objects have at least three singleton bags.
        for singleton_count in range(7, 2, -1):
            nonsingleton_count = 7 - singleton_count
            for singleton_vertices in itertools.combinations(
                range(self.order), singleton_count
            ):
                if any(
                    not (adj[left] >> right & 1)
                    for left, right in itertools.combinations(
                        singleton_vertices, 2
                    )
                ):
                    continue
                if nonsingleton_count == 0:
                    return True
                core = sum(1 << vertex for vertex in singleton_vertices)
                remainder = self.full ^ core
                candidates = []
                subset = remainder
                while subset:
                    if connected(subset) and all(
                        touches(subset, 1 << vertex)
                        for vertex in singleton_vertices
                    ):
                        candidates.append(subset)
                    subset = (subset - 1) & remainder

                def search(start, chosen, used):
                    if len(chosen) == nonsingleton_count:
                        return True
                    for position in range(start, len(candidates)):
                        candidate = candidates[position]
                        if candidate & used:
                            continue
                        if all(touches(candidate, old) for old in chosen):
                            if search(
                                position + 1,
                                chosen + (candidate,),
                                used | candidate,
                            ):
                                return True
                    return False

                if search(0, (), 0):
                    return True
        return False


def generic_adjacency(edges, order, pairs):
    answer = [0] * order
    for index, (left, right) in enumerate(pairs):
        if edges >> index & 1:
            answer[left] |= 1 << right
            answer[right] |= 1 << left
    return tuple(answer)


def generic_contract(graph, left, right):
    """Contract one edge in an adjacency tuple and relabel increasingly."""

    assert left < right and graph[left] >> right & 1
    image = tuple(
        left if vertex == right else vertex - (vertex > right)
        for vertex in range(len(graph))
    )
    answer = [0] * (len(graph) - 1)
    for u in range(len(graph)):
        for v in range(u + 1, len(graph)):
            if not (graph[u] >> v & 1):
                continue
            x, y = image[u], image[v]
            if x == y:
                continue
            answer[x] |= 1 << y
            answer[y] |= 1 << x
    return tuple(answer)


@functools.lru_cache(maxsize=None)
def generic_has_k7(graph):
    """Independent exact detector by at most four edge contractions."""

    if any(
        all(
            graph[left] >> right & 1
            for left, right in itertools.combinations(vertices, 2)
        )
        for vertices in itertools.combinations(range(len(graph)), 7)
    ):
        return True
    if len(graph) == 7:
        return False
    return any(
        generic_has_k7(generic_contract(graph, left, right))
        for left in range(len(graph))
        for right in range(left + 1, len(graph))
        if graph[left] >> right & 1
    )


@functools.lru_cache(maxsize=1)
def minimal_order_seven_carriers():
    carriers = []
    for mask in range(1 << len(LOCAL_PAIRS)):
        if mask.bit_count() < 11:
            continue
        if not connectivity.three_connected(mask, 7, LOCAL_PAIRS):
            continue
        if any(
            connectivity.three_connected(
                mask & ~(1 << index), 7, LOCAL_PAIRS
            )
            for index in range(len(LOCAL_PAIRS))
            if mask >> index & 1
        ):
            continue
        carriers.append(mask)
    carriers = tuple(carriers)
    assert len(carriers) == 5495
    assert collections.Counter(map(int.bit_count, carriers)) == {
        11: 5040,
        12: 455,
    }
    return carriers


def lift(mask, labels, global_index):
    return sum(
        1 << global_index[tuple(sorted((labels[left], labels[right])))]
        for index, (left, right) in enumerate(LOCAL_PAIRS)
        if mask >> index & 1
    )


def contract_extra(mask: int, owner: int) -> int:
    answer = 0
    for left, right in LOCAL_PAIRS:
        present = bool(mask >> EIGHT_INDEX[(left, right)] & 1)
        if left == owner:
            present |= bool(mask >> EIGHT_INDEX[tuple(sorted((7, right)))] & 1)
        if right == owner:
            present |= bool(mask >> EIGHT_INDEX[tuple(sorted((7, left)))] & 1)
        if present:
            answer |= 1 << LOCAL_INDEX[(left, right)]
    return answer


@functools.lru_cache(maxsize=1)
def exact_order_eight_families():
    """Every labelled order-eight terminal-irreducible owner family."""

    cycles = set()
    for tail in itertools.permutations(range(1, 7)):
        order = (0,) + tail
        if order[1] > order[-1]:
            continue
        cycle = sum(
            1 << LOCAL_INDEX[
                tuple(sorted((order[index], order[(index + 1) % 7])))
            ]
            for index in range(7)
        )
        cycles.add(cycle)

    kernels = set()
    for cycle in cycles:
        for charged in range(1 << 7):
            if charged.bit_count() < 4:
                continue
            uncharged = tuple(
                vertex for vertex in range(7) if not (charged >> vertex & 1)
            )
            optional_chords = tuple(
                edge
                for edge in itertools.combinations(uncharged, 2)
                if not (cycle >> LOCAL_INDEX[edge] & 1)
            )
            for choice in range(1 << len(optional_chords)):
                terminal_mask = cycle | sum(
                    1 << LOCAL_INDEX[edge]
                    for index, edge in enumerate(optional_chords)
                    if choice >> index & 1
                )
                terminal_adj = connectivity.adjacency(
                    terminal_mask, 7, LOCAL_PAIRS
                )
                actual_charged = sum(
                    1 << vertex
                    for vertex in range(7)
                    if terminal_adj[vertex].bit_count() == 2
                )
                if actual_charged != charged:
                    continue
                if any(
                    terminal_adj[vertex].bit_count() < 3
                    for vertex in uncharged
                ):
                    continue

                for extras in range(1 << len(uncharged)):
                    neighbours = charged | sum(
                        1 << vertex
                        for index, vertex in enumerate(uncharged)
                        if extras >> index & 1
                    )
                    kernel = sum(
                        1 << EIGHT_INDEX[edge]
                        for index, edge in enumerate(LOCAL_PAIRS)
                        if terminal_mask >> index & 1
                    ) | sum(
                        1 << EIGHT_INDEX[(vertex, 7)]
                        for vertex in range(7)
                        if neighbours >> vertex & 1
                    )
                    if not connectivity.three_connected(
                        kernel, 8, EIGHT_PAIRS
                    ):
                        continue
                    if any(
                        connectivity.three_connected(
                            contract_extra(kernel, owner), 7, LOCAL_PAIRS
                        )
                        for owner in range(7)
                        if neighbours >> owner & 1
                    ):
                        continue
                    kernels.add((terminal_mask, neighbours))

    families = {
        tuple(
            sorted(
                {
                    contract_extra(
                        sum(
                            1 << EIGHT_INDEX[edge]
                            for index, edge in enumerate(LOCAL_PAIRS)
                            if terminal_mask >> index & 1
                        )
                        | sum(
                            1 << EIGHT_INDEX[(vertex, 7)]
                            for vertex in range(7)
                            if neighbours >> vertex & 1
                        ),
                        owner,
                    )
                    for owner in range(7)
                    if neighbours >> owner & 1
                }
            )
        )
        for terminal_mask, neighbours in kernels
    }
    families = tuple(sorted(families))
    assert len(kernels) == 30600
    assert len(families) == 30600
    assert collections.Counter(map(len, families)) == {
        4: 2520,
        5: 10080,
        6: 12600,
        7: 5400,
    }
    return families


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--crosscheck", action="store_true")
    args = parser.parse_args()
    started = time.time()
    cell, pairs, pair_index, states = joined_states()
    n, a, common, _x, p, q, terminals, *_ = cell
    noncommon = {
        (ones, zeros)
        for ones, zeros in states
        if relation.common_rooted_k4(ones, n, a, common, p, q) is None
    }

    # Composition is monotone in the forced-one mask.  It is enough to test
    # the inclusion-minimal masks: every other noncommon state contains one.
    witness = {}
    for ones, zeros in noncommon:
        witness.setdefault(ones, zeros)
    minima = []
    for ones in sorted(witness, key=lambda mask: (mask.bit_count(), mask)):
        if not any(old & ones == old for old in minima):
            minima.append(ones)
    assert all(any(old & ones == old for old in minima) for ones in witness)
    assert len(states) == 762738
    assert len(noncommon) == 148488
    assert len(witness) == 148488
    assert len(minima) == 8220

    automorphisms = tuple(category_automorphisms())
    assert len(automorphisms) == 576
    live_minima = set(minima)
    orbit_masks = []
    covered_minima = set()
    while live_minima:
        representative = min(live_minima)
        orbit = {
            transformed_mask(representative, image, pairs, pair_index)
            for image in automorphisms
        }
        assert orbit <= set(minima)
        orbit &= live_minima
        assert representative in orbit
        orbit_masks.append(representative)
        covered_minima |= orbit
        live_minima -= orbit
    assert covered_minima == set(minima)
    assert len(orbit_masks) == 67

    detector = FastK7(n, pairs, pair_index)
    order_seven = minimal_order_seven_carriers()
    order_eight = exact_order_eight_families()
    reserve_pairs = tuple(itertools.combinations(terminals, 2))

    # Counterexample-guided guard sets.  They only change search order; every
    # accepted pair is still checked against each complete catalogue.
    guards_seven = [797887, 435327, 61244, 120383, 32700, 286396]
    assert set(guards_seven) <= set(order_seven)
    guards_eight = []
    profile = collections.Counter()
    closed_minima = 0
    closure_records = []

    for orbit_index, ones in enumerate(orbit_masks):
        zeros = witness[ones]
        if detector(ones):
            profile["direct"] += 1
            closed_minima += 1
            closure_records.append((ones, "direct"))
            continue

        valid = None
        failures = {}
        for reserved in reserve_pairs:
            labels = tuple(
                terminal for terminal in terminals if terminal not in reserved
            )

            bad_seven = next(
                (
                    carrier
                    for carrier in guards_seven
                    if not detector(ones | lift(carrier, labels, pair_index))
                ),
                None,
            )
            if bad_seven is None:
                bad_seven = next(
                    (
                        carrier
                        for carrier in order_seven
                        if not detector(
                            ones | lift(carrier, labels, pair_index)
                        )
                    ),
                    None,
                )
                if bad_seven is not None and bad_seven not in guards_seven:
                    guards_seven.append(bad_seven)
            if bad_seven is not None:
                failures[reserved] = ("order7", bad_seven)
                continue

            def family_closes(family):
                return any(
                    detector(ones | lift(carrier, labels, pair_index))
                    for carrier in family
                )

            bad_eight = next(
                (family for family in guards_eight if not family_closes(family)),
                None,
            )
            if bad_eight is None:
                bad_eight = next(
                    (
                        family
                        for family in order_eight
                        if not family_closes(family)
                    ),
                    None,
                )
                if bad_eight is not None and bad_eight not in guards_eight:
                    guards_eight.append(bad_eight)
            if bad_eight is not None:
                failures[reserved] = ("order8", bad_eight)
                continue

            valid = reserved
            break

        if valid is None:
            print("ADAPTIVE_FAIL", orbit_index, ones, zeros)
            print("failures", failures)
            print("elapsed", time.time() - started)
            return

        profile[valid] += 1
        closed_minima += 1
        closure_records.append((ones, f"{valid[0]},{valid[1]}"))
        if orbit_index % 10 == 0:
            print(
                "progress",
                orbit_index,
                "of",
                len(orbit_masks),
                "valid",
                valid,
                "guards",
                len(guards_seven),
                len(guards_eight),
                "cache",
                len(detector.cache),
                "elapsed",
                round(time.time() - started, 1),
                flush=True,
            )

    assert closed_minima == 67
    assert profile == collections.Counter(
        {"direct": 21, (2, 3): 45, (2, 9): 1}
    )

    def digest(records):
        answer = hashlib.sha256()
        for record in records:
            answer.update((record + "\n").encode())
        return answer.hexdigest()

    state_digest = digest(
        f"{ones}:{zeros}" for ones, zeros in sorted(noncommon)
    )
    minima_digest = digest(str(mask) for mask in sorted(minima))
    orbit_digest = digest(str(mask) for mask in orbit_masks)
    order7_digest = digest(str(mask) for mask in order_seven)
    order8_digest = digest(
        ",".join(map(str, family)) for family in order_eight
    )
    closure_digest = digest(
        f"{mask}:{outcome}" for mask, outcome in closure_records
    )

    if args.crosscheck:
        cached = tuple(detector.cache.items())
        for index, (edges, answer) in enumerate(cached):
            independent = generic_has_k7(
                generic_adjacency(edges, n, pairs)
            )
            assert independent == answer, (edges, answer, independent)
            if index % 10000 == 0:
                print(
                    "crosscheck_progress",
                    index,
                    "of",
                    len(cached),
                    flush=True,
                )
        print("crosschecked_quotient_masks", len(cached))

    print("adaptive full-kernel probe: no counterstate")
    print(
        "joined",
        len(states),
        "noncommon",
        len(noncommon),
        "unique_one_masks",
        len(witness),
    )
    print(
        "minimal_one_masks",
        len(minima),
        "minimal_orbits",
        len(orbit_masks),
        "closed_minimal_orbits",
        closed_minima,
    )
    print("order7_catalogue", len(order_seven))
    print("order8_exact_families", len(order_eight))
    print("guard_counts", len(guards_seven), len(guards_eight))
    print("profile", dict(profile))
    print("noncommon_sha256", state_digest)
    print("minima_sha256", minima_digest)
    print("orbit_sha256", orbit_digest)
    print("order7_sha256", order7_digest)
    print("order8_sha256", order8_digest)
    print("closure_sha256", closure_digest)
    print("fast_detector_cache", len(detector.cache))
    print("elapsed", time.time() - started)


if __name__ == "__main__":
    main()
