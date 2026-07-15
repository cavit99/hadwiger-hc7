#!/usr/bin/env python3
"""Exact six-terminal-kernel decoder for the overlap-two order-five cell.

Labels are fixed throughout::

    A = {0,1,2,3,4,5},       I = A cap X = {0,1},
    X = {0,1,6,7},           p = 8, q = 9,
    T = {2,3,4,5,6,7,8,9}.

The five six-support relations are ``A`` and ``(A-i)+p/q`` for ``i`` in
``I``.  The two sets ``X+p`` and ``X+q`` are literal K5 cliques.  After
removing a common rooted-K4 outcome, the experiment reserves a labelled
pair ``r,s`` in ``T`` and adds every carrier in the complete audited
six-terminal kernel catalogue on ``T-{r,s}``.

For an order-seven kernel, its unique nonterminal may be absorbed into
any adjacent terminal bag.  A reserved pair succeeds only when every one
of the 142 order-six carriers and every one of the 780 order-seven
kernels composes to a literal K7 model (with the absorbing owner chosen
adaptively for an order-seven kernel).

No unspecified original edge is completed, and no label is identified.
"""

from __future__ import annotations

import argparse
import collections
import hashlib
import itertools

import hc7_cross_arm_overlap_three_kernel_decoder as decoder
import hc7_overlap_three_six_terminal_kernel_verify as kernel


N = 10
A = (0, 1, 2, 3, 4, 5)
I = (0, 1)
X = (0, 1, 6, 7)
P, Q = 8, 9
T = (2, 3, 4, 5, 6, 7, 8, 9)
SUPPORTS = (
    A,
    (1, 2, 3, 4, 5, 8),
    (1, 2, 3, 4, 5, 9),
    (0, 2, 3, 4, 5, 8),
    (0, 2, 3, 4, 5, 9),
)
LITERAL_FIVES = (X + (P,), X + (Q,))


def assert_exact_cell() -> None:
    """Guard the literal labels and every set entering the finite claim."""

    assert A == tuple(range(6))
    assert set(I) == set(A) & set(X)
    assert set(A) | set(X) | {P, Q} == set(range(N))
    assert set(T) == set(range(N)) - set(I)
    assert len(SUPPORTS) == 5 and all(len(set(support)) == 6 for support in SUPPORTS)
    expected = {frozenset(A)}
    expected.update(
        frozenset((tuple(vertex for vertex in A if vertex != omitted) + (root,)))
        for omitted in I
        for root in (P, Q)
    )
    assert {frozenset(support) for support in SUPPORTS} == expected
    assert {frozenset(five) for five in LITERAL_FIVES} == {
        frozenset(X + (P,)),
        frozenset(X + (Q,)),
    }
    assert all(len(set(five)) == 5 for five in LITERAL_FIVES)


def joined_states():
    """Join the five exact six-support relations and two literal cliques."""

    pairs = tuple(itertools.combinations(range(N), 2))
    pair_index = {edge: index for index, edge in enumerate(pairs)}
    constraints = [decoder.global_patterns(support, pair_index) for support in SUPPORTS]
    fixed_ones = 0
    for five in LITERAL_FIVES:
        for edge in itertools.combinations(five, 2):
            fixed_ones |= 1 << pair_index[edge]
    # The two K5s overlap in the literal K4 on X: 10+10-6=14 edges.
    assert fixed_ones.bit_count() == 14
    states: set[tuple[int, int]] = set()

    def visit(done: frozenset[int], ones: int, zeros: int) -> None:
        if ones & zeros:
            return
        if len(done) == len(constraints):
            states.add((ones, zeros))
            return
        selected = -1
        compatible = None
        for index, patterns in enumerate(constraints):
            if index in done:
                continue
            options = [
                pattern
                for pattern in patterns
                if not (pattern[0] & zeros or pattern[1] & ones)
            ]
            if compatible is None or len(options) < len(compatible):
                selected, compatible = index, options
        assert compatible is not None
        seen = set()
        for local_ones, local_zeros in compatible:
            new = (ones | local_ones, zeros | local_zeros)
            if new in seen:
                continue
            seen.add(new)
            visit(done | {selected}, *new)

    visit(frozenset(), fixed_ones, 0)
    return pairs, pair_index, states


def category_automorphisms():
    """All relabellings preserving I, A-I, X-I, and {p,q}."""

    for pi_i in itertools.permutations(I):
        for pi_a in itertools.permutations((2, 3, 4, 5)):
            for pi_x in itertools.permutations((6, 7)):
                for pi_pq in itertools.permutations((8, 9)):
                    image = list(range(N))
                    image[0:2] = pi_i
                    image[2:6] = pi_a
                    image[6:8] = pi_x
                    image[8:10] = pi_pq
                    yield tuple(image)


def transformed_mask(mask, image, pairs, pair_index):
    answer = 0
    for position, (left, right) in enumerate(pairs):
        if mask >> position & 1:
            answer |= 1 << pair_index[decoder.pair(image[left], image[right])]
    return answer


def canonical_key(ones, zeros, pairs, pair_index, automorphisms):
    return min(
        (
            transformed_mask(ones, image, pairs, pair_index),
            transformed_mask(zeros, image, pairs, pair_index),
        )
        for image in automorphisms
    )


def noncommon_orbits():
    pairs, pair_index, states = joined_states()
    automorphisms = tuple(category_automorphisms())
    assert len(automorphisms) == 192
    representatives = {}
    weights = collections.Counter()
    noncommon_states = set()
    for ones, zeros in states:
        if decoder.common_rooted_k4(ones, N, A, I, P, Q) is not None:
            continue
        noncommon_states.add((ones, zeros))
        key = canonical_key(ones, zeros, pairs, pair_index, automorphisms)
        representatives.setdefault(key, (ones, zeros))
        weights[key] += 1

    # Verify that the abstract symmetry used for compression preserves the
    # joined relation exactly, and that every recorded weight is the full
    # orbit size rather than a partial stabilizer count.
    for key, (ones, zeros) in representatives.items():
        orbit = {
            (
                transformed_mask(ones, image, pairs, pair_index),
                transformed_mask(zeros, image, pairs, pair_index),
            )
            for image in automorphisms
        }
        assert orbit <= noncommon_states
        assert len(orbit) == weights[key]

    noncommon = tuple(
        (*representatives[key], weights[key]) for key in sorted(representatives)
    )
    assert sum(weight for _ones, _zeros, weight in noncommon) == len(noncommon_states)
    return pairs, pair_index, states, noncommon


def state_digest(states):
    digest = hashlib.sha256()
    for ones, zeros, weight in states:
        digest.update(ones.to_bytes(6, "little"))
        digest.update(zeros.to_bytes(6, "little"))
        digest.update(weight.to_bytes(2, "little"))
    return digest.hexdigest()


def literal_state_digest(states):
    digest = hashlib.sha256()
    for ones, zeros in sorted(states):
        digest.update(ones.to_bytes(6, "little"))
        digest.update(zeros.to_bytes(6, "little"))
    return digest.hexdigest()


def certificate_digest(states, valid_pairs):
    """Hash the complete orbit representatives and valid reserved pairs."""

    digest = hashlib.sha256()
    for (ones, zeros, weight), pairs_for_state in zip(states, valid_pairs, strict=True):
        digest.update(ones.to_bytes(6, "little"))
        digest.update(zeros.to_bytes(6, "little"))
        digest.update(weight.to_bytes(2, "little"))
        digest.update(len(pairs_for_state).to_bytes(1, "little"))
        for left, right in pairs_for_state:
            digest.update(bytes((left, right)))
    return digest.hexdigest()


def exact_edges(mask, pairs):
    return tuple(edge for index, edge in enumerate(pairs) if mask >> index & 1)


def test_reserved_pair(
    ones,
    reserved,
    pair_index,
    has_k7,
    six_carriers,
    seven_kernels,
):
    labels = tuple(terminal for terminal in T if terminal not in reserved)
    assert len(labels) == 6
    for carrier in six_carriers:
        lifted = kernel.lift_six_mask(carrier, labels, pair_index)
        if not has_k7(ones | lifted):
            return ("order6", carrier)
    for terminal_mask, neighbours in seven_kernels:
        if not any(
            has_k7(
                ones
                | kernel.lift_six_mask(
                    kernel.owner_quotient(terminal_mask, neighbours, owner),
                    labels,
                    pair_index,
                )
            )
            for owner in range(6)
            if neighbours >> owner & 1
        ):
            return ("order7", terminal_mask, neighbours)
    return None


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--census-only",
        action="store_true",
        help="join and orbit-reduce the exact relation without testing carriers",
    )
    parser.add_argument(
        "--show-failures",
        action="store_true",
        help="print complete exact edge/nonedge data for failed orbits",
    )
    args = parser.parse_args()

    assert_exact_cell()
    pairs, pair_index, all_states, states = noncommon_orbits()
    assert len(all_states) == 1419
    assert sum(weight for *_rest, weight in states) == 240
    assert len(states) == 9
    assert state_digest(states) == "fda41d193855cc87de35746a5d567f53093a4ec8b2354b0caaadcac0d6d042e8"
    print("overlap-two order-five six-terminal-kernel decoder")
    print("joined_states", len(all_states))
    print("common_states", len(all_states) - sum(weight for *_rest, weight in states))
    print("noncommon_states", sum(weight for *_rest, weight in states))
    print("noncommon_orbits", len(states))
    print("noncommon_state_sha256", state_digest(states))
    unknown_histogram = collections.Counter()
    for ones, zeros, weight in states:
        unknown_histogram[len(pairs) - (ones | zeros).bit_count()] += weight
    print("unknown_edge_histogram", dict(sorted(unknown_histogram.items())))
    if args.census_only:
        return

    six_carriers = kernel.minimal_six_terminal_carriers()
    seven_kernels = kernel.irreducible_seven_vertex_kernels()
    has_k7 = kernel.FastK7(pairs, pair_index)

    # This direct pass deliberately avoids symmetry compression: every
    # one of the 240 literal noncommon states is checked with the same
    # reserved pair {p,q}.  Orbit reduction below remains useful for the
    # stronger all-reserved-pairs diagnostic, but is not needed for the
    # fixed-pair theorem.
    literal_noncommon = tuple(
        (ones, zeros)
        for ones, zeros in all_states
        if decoder.common_rooted_k4(ones, N, A, I, P, Q) is None
    )
    assert len(literal_noncommon) == 240
    assert literal_state_digest(literal_noncommon) == (
        "90f42c0edf0e6b5b6c424810fe19ce31f5e84ef1079feea0fd3a5c1454cf7ef5"
    )
    for ones, _zeros in literal_noncommon:
        assert (
            test_reserved_pair(
                ones,
                (P, Q),
                pair_index,
                has_k7,
                six_carriers,
                seven_kernels,
            )
            is None
        )
    print("fixed_private_pair_all_state_check", len(literal_noncommon))
    print("literal_noncommon_sha256", literal_state_digest(literal_noncommon))

    successes = []
    failures = []
    reserved_profile = collections.Counter()
    for orbit, (ones, zeros, weight) in enumerate(states):
        valid = []
        witnesses = {}
        for reserved in itertools.combinations(T, 2):
            failure = test_reserved_pair(
                ones,
                reserved,
                pair_index,
                has_k7,
                six_carriers,
                seven_kernels,
            )
            if failure is None:
                valid.append(reserved)
            else:
                witnesses[reserved] = failure
        if valid:
            successes.append((orbit, weight, tuple(valid)))
            reserved_profile[len(valid)] += weight
        else:
            failures.append((orbit, ones, zeros, weight, witnesses))
            print("FAIL", orbit, "weight", weight, "first", witnesses, flush=True)

    print("minimal_order6_carriers", len(six_carriers))
    print("irreducible_order7_kernels", len(seven_kernels))
    print("catalogue_sha256", kernel.catalogue_digest(six_carriers, seven_kernels))
    print("closed_orbits", len(successes))
    print("closed_weight", sum(weight for _orbit, weight, _valid in successes))
    print("failure_orbits", len(failures))
    print("failure_weight", sum(record[3] for record in failures))
    valid_pairs = tuple(valid for _orbit, _weight, valid in successes)
    assert not failures
    assert all((P, Q) in valid for valid in valid_pairs)
    assert certificate_digest(states, valid_pairs) == (
        "17ce12fd03734d53af37deae840662b1744ecda8b86ef2fdd9934c5b5fff568a"
    )
    print(
        "fixed_private_pair_pq_valid",
        len(successes) == len(states)
        and all((P, Q) in valid for valid in valid_pairs),
    )
    print("certificate_sha256", certificate_digest(states, valid_pairs))
    print("valid_reserved_pair_count_weight", dict(sorted(reserved_profile.items())))
    print(
        "valid_reserved_pair_count_orbits",
        dict(
            sorted(
                collections.Counter(len(valid) for _orbit, _weight, valid in successes).items()
            )
        ),
    )
    if args.show_failures:
        for orbit, ones, zeros, weight, witnesses in failures:
            print("COUNTERSTATE", orbit, "weight", weight)
            print(" forced_edges", exact_edges(ones, pairs))
            print(" forced_nonedges", exact_edges(zeros, pairs))
            print(" first_failures", witnesses)


if __name__ == "__main__":
    main()
