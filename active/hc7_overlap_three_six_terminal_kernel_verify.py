#!/usr/bin/env python3
"""Full six-terminal kernel test for the order-six overlap-three residue.

For a reserved terminal ``r``, four-connectivity of ``H`` makes ``H-r``
three-connected.  The audited terminal-legal contraction theorem reduces
the other six terminals to a rooted kernel of order six or seven.  This
script enumerates the complete bounded carrier guarantee:

* all 142 labelled edge-minimal three-connected graphs on six terminals;
* all 780 labelled terminal-irreducible three-connected kernels with one
  nonterminal.

The nonterminal may be absorbed into any adjacent terminal bag.  Carrier
edges are added only after the original nine support relations are joined.
"""

from __future__ import annotations

import collections
import functools
import argparse
import hashlib
import itertools

import hc7_cross_arm_overlap_three_kernel_decoder as decoder


def category_automorphisms():
    """Relabellings preserving I, A-I, X-I, and the private-root pair."""

    for pi_i in itertools.permutations((0, 1, 2)):
        for pi_a in itertools.permutations((3, 4, 5)):
            for pi_x in itertools.permutations((6, 7)):
                for pi_r in itertools.permutations((8, 9)):
                    image = list(range(10))
                    image[0:3] = pi_i
                    image[3:6] = pi_a
                    image[6:8] = pi_x
                    image[8:10] = pi_r
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


def pair_data(order: int):
    pairs = tuple(itertools.combinations(range(order), 2))
    return pairs, {edge: index for index, edge in enumerate(pairs)}


def adjacency(mask: int, order: int, pairs) -> tuple[int, ...]:
    answer = [0] * order
    for index, (left, right) in enumerate(pairs):
        if mask >> index & 1:
            answer[left] |= 1 << right
            answer[right] |= 1 << left
    return tuple(answer)


def connected_on(adj: tuple[int, ...], remaining: int) -> bool:
    reached = remaining & -remaining
    while True:
        old = reached
        frontier = reached
        neighbours = 0
        while frontier:
            bit = frontier & -frontier
            neighbours |= adj[bit.bit_length() - 1]
            frontier -= bit
        reached |= neighbours & remaining
        if reached == old:
            return reached == remaining


def three_connected(mask: int, order: int, pairs) -> bool:
    adj = adjacency(mask, order, pairs)
    if min(map(int.bit_count, adj)) < 3:
        return False
    full = (1 << order) - 1
    return all(
        connected_on(
            adj,
            full & ~sum(1 << vertex for vertex in deleted),
        )
        for size in range(3)
        for deleted in itertools.combinations(range(order), size)
    )


@functools.lru_cache(maxsize=1)
def minimal_six_terminal_carriers() -> tuple[int, ...]:
    pairs, _ = pair_data(6)
    carriers = []
    for mask in range(1 << len(pairs)):
        if mask.bit_count() < 9 or not three_connected(mask, 6, pairs):
            continue
        if any(
            three_connected(mask & ~(1 << index), 6, pairs)
            for index in range(len(pairs))
            if mask >> index & 1
        ):
            continue
        carriers.append(mask)
    carriers = tuple(carriers)
    assert len(carriers) == 142
    assert collections.Counter(mask.bit_count() for mask in carriers) == {
        9: 70,
        10: 72,
    }
    return carriers


def contract_extra_into(mask: int, owner: int) -> int:
    """Contract vertex 6 into terminal ``owner`` and return a six-mask."""

    pairs7, index7 = pair_data(7)
    pairs6, index6 = pair_data(6)
    answer = 0
    for left, right in pairs6:
        present = bool(mask >> index7[(left, right)] & 1)
        if left == owner:
            present |= bool(mask >> index7[decoder.pair(6, right)] & 1)
        if right == owner:
            present |= bool(mask >> index7[decoder.pair(6, left)] & 1)
        if present:
            answer |= 1 << index6[(left, right)]
    return answer


@functools.lru_cache(maxsize=1)
def irreducible_seven_vertex_kernels():
    """Enumerate every labelled kernel with terminals 0,...,5 and extra 6."""

    pairs7, index7 = pair_data(7)
    pairs6, _ = pair_data(6)
    kernels = []
    profile = collections.Counter()
    for mask in range(1 << len(pairs7)):
        if mask.bit_count() < 11:
            continue
        adj = adjacency(mask, 7, pairs7)
        if min(map(int.bit_count, adj)) < 3:
            continue

        # Wu's charge conclusion is a necessary fast filter for a
        # terminal-irreducible vertex; irreducibility is still checked
        # directly below.
        if sum(
            bool(adj[6] >> terminal & 1) and adj[terminal].bit_count() == 3
            for terminal in range(6)
        ) < 4:
            continue
        if not three_connected(mask, 7, pairs7):
            continue
        if any(
            three_connected(contract_extra_into(mask, owner), 6, pairs6)
            for owner in range(6)
            if adj[6] >> owner & 1
        ):
            continue

        terminal_mask = sum(
            1 << index
            for index, edge in enumerate(pairs6)
            if mask >> index7[edge] & 1
        )
        neighbours = adj[6] & ((1 << 6) - 1)
        kernels.append((terminal_mask, neighbours))
        profile[
            (
                neighbours.bit_count(),
                tuple(sorted(adj[t].bit_count() for t in range(6))),
            )
        ] += 1

    kernels = tuple(kernels)
    assert len(kernels) == 780
    assert profile == collections.Counter(
        {
            (4, (3, 3, 3, 3, 3, 3)): 180,
            (5, (3, 3, 3, 3, 3, 4)): 360,
            (6, (3, 3, 3, 3, 3, 3)): 60,
            (6, (3, 3, 3, 3, 4, 4)): 180,
        }
    )
    return kernels


def noncommon_orbits():
    cell, pairs, pair_index, states = decoder.joined_states(6)
    n, a, core, _x, p, q, terminals, *_ = cell
    automorphisms = tuple(category_automorphisms())
    assert len(automorphisms) == 144
    representatives = {}
    weights = collections.Counter()
    noncommon_states = set()
    for ones, zeros in states:
        if decoder.common_rooted_k4(ones, n, a, core, p, q) is not None:
            continue
        noncommon_states.add((ones, zeros))
        key = canonical_key(
            ones, zeros, pairs, pair_index, automorphisms
        )
        representatives.setdefault(key, (ones, zeros))
        weights[key] += 1

    assert len(states) == 60162
    assert len(noncommon_states) == 7878
    assert len(representatives) == 140
    for key, (ones, zeros) in representatives.items():
        orbit = {
            (
                transformed_mask(
                    ones, image, pairs, pair_index
                ),
                transformed_mask(
                    zeros, image, pairs, pair_index
                ),
            )
            for image in automorphisms
        }
        assert orbit <= noncommon_states
        assert len(orbit) == weights[key]

    noncommon = tuple(
        (*representatives[key], weights[key])
        for key in sorted(representatives)
    )
    assert len(noncommon) == 140
    assert sum(weight for _ones, _zeros, weight in noncommon) == 7878
    return cell, pairs, pair_index, noncommon


class FastK7:
    """Exact ``K_7``-minor detector on the ten labelled quotient objects."""

    def __init__(self, pairs, pair_index):
        self.pairs = pairs
        self.pair_index = pair_index
        self.order = 10
        self.full = (1 << self.order) - 1
        self.vertices = {
            mask: tuple(v for v in range(self.order) if mask >> v & 1)
            for mask in range(1, 1 << self.order)
        }
        self.pair_mask = {
            mask: sum(
                1 << pair_index[decoder.pair(u, v)]
                for u, v in itertools.combinations(vertices, 2)
            )
            for mask, vertices in self.vertices.items()
        }
        self.cores = {
            size: tuple(
                mask
                for mask in self.vertices
                if mask.bit_count() == size
            )
            for size in (4, 5, 6, 7)
        }
        self.cache = {}

    def adjbits(self, edges):
        answer = [0] * self.order
        for (left, right), index in self.pair_index.items():
            if edges >> index & 1:
                answer[left] |= 1 << right
                answer[right] |= 1 << left
        return tuple(answer)

    def connected(self, adj, mask):
        return connected_on(adj, mask)

    @staticmethod
    def touches(adj, left, right):
        frontier = left
        while frontier:
            bit = frontier & -frontier
            if adj[bit.bit_length() - 1] & right:
                return True
            frontier -= bit
        return False

    def full_to_core(self, adj, bag, core):
        return all(
            self.touches(adj, bag, 1 << vertex)
            for vertex in self.vertices[core]
        )

    def __call__(self, edges):
        cached = self.cache.get(edges)
        if cached is not None:
            return cached
        answer = self._test(edges)
        self.cache[edges] = answer
        return answer

    def _test(self, edges):
        adj = self.adjbits(edges)

        for core in self.cores[7]:
            if edges & self.pair_mask[core] == self.pair_mask[core]:
                return True

        for core in self.cores[6]:
            if edges & self.pair_mask[core] != self.pair_mask[core]:
                continue
            remainder = self.full ^ core
            bag = remainder
            while bag:
                if (
                    bag.bit_count() >= 2
                    and self.connected(adj, bag)
                    and self.full_to_core(adj, bag, core)
                ):
                    return True
                bag = (bag - 1) & remainder

        for core in self.cores[5]:
            if edges & self.pair_mask[core] != self.pair_mask[core]:
                continue
            remainder = self.full ^ core
            left = (remainder - 1) & remainder
            while left:
                if left.bit_count() >= 2 and self.connected(adj, left):
                    available = remainder ^ left
                    right = available
                    while right:
                        if (
                            right.bit_count() >= 2
                            and left < right
                            and self.connected(adj, right)
                            and self.full_to_core(adj, left, core)
                            and self.full_to_core(adj, right, core)
                            and self.touches(adj, left, right)
                        ):
                            return True
                        right = (right - 1) & available
                left = (left - 1) & remainder

        for core in self.cores[4]:
            if edges & self.pair_mask[core] != self.pair_mask[core]:
                continue
            remaining = self.vertices[self.full ^ core]
            first = remaining[0]
            for mate in remaining[1:]:
                rest = tuple(v for v in remaining if v not in (first, mate))
                second = rest[0]
                for mate2 in rest[1:]:
                    last = tuple(v for v in rest if v not in (second, mate2))
                    bags = (
                        (1 << first) | (1 << mate),
                        (1 << second) | (1 << mate2),
                        (1 << last[0]) | (1 << last[1]),
                    )
                    if (
                        all(self.touches(adj, bag, bag) for bag in bags)
                        and all(
                            self.full_to_core(adj, bag, core)
                            for bag in bags
                        )
                        and all(
                            self.touches(adj, left, right)
                            for left, right in itertools.combinations(bags, 2)
                        )
                    ):
                        return True
        return False


def lift_six_mask(mask, labels, global_index):
    pairs6, _ = pair_data(6)
    return sum(
        1 << global_index[decoder.pair(labels[left], labels[right])]
        for index, (left, right) in enumerate(pairs6)
        if mask >> index & 1
    )


def owner_quotient(terminal_mask, neighbours, owner):
    pairs6, index6 = pair_data(6)
    answer = terminal_mask
    for other in range(6):
        if other != owner and neighbours >> other & 1:
            answer |= 1 << index6[decoder.pair(owner, other)]
    return answer


def catalogue_digest(six_carriers, seven_kernels):
    digest = hashlib.sha256()
    for mask in six_carriers:
        digest.update(b"6")
        digest.update(mask.to_bytes(2, "little"))
    for terminal_mask, neighbours in seven_kernels:
        digest.update(b"7")
        digest.update(terminal_mask.to_bytes(2, "little"))
        digest.update(neighbours.to_bytes(1, "little"))
    return digest.hexdigest()


def state_digest(states):
    digest = hashlib.sha256()
    for ones, zeros, weight in states:
        digest.update(ones.to_bytes(6, "little"))
        digest.update(zeros.to_bytes(6, "little"))
        digest.update(weight.to_bytes(2, "little"))
    return digest.hexdigest()


def crosscheck_fast_detector(
    states,
    terminals,
    pair_index,
    six_carriers,
    seven_kernels,
    has_k7,
):
    """Compare the specialized detector with the generic branch search."""

    generic_specs = decoder.partition_specs(10, 7)
    chosen = next(
        ones
        for ones, _zeros, _weight in states
        if decoder.has_k_minor(ones, generic_specs) is None
    )
    digest = hashlib.sha256()
    tested = 0
    for reserved in terminals[:2]:
        labels = tuple(t for t in terminals if t != reserved)
        for carrier in six_carriers:
            edges = chosen | lift_six_mask(carrier, labels, pair_index)
            fast = has_k7(edges)
            generic = decoder.has_k_minor(edges, generic_specs) is not None
            assert fast == generic
            digest.update(edges.to_bytes(6, "little"))
            digest.update(bytes((fast,)))
            tested += 1
        for terminal_mask, neighbours in seven_kernels:
            for owner in range(6):
                if not (neighbours >> owner & 1):
                    continue
                edges = chosen | lift_six_mask(
                    owner_quotient(terminal_mask, neighbours, owner),
                    labels,
                    pair_index,
                )
                fast = has_k7(edges)
                generic = decoder.has_k_minor(edges, generic_specs) is not None
                assert fast == generic
                digest.update(edges.to_bytes(6, "little"))
                digest.update(bytes((fast,)))
                tested += 1
    assert tested == 8204
    return tested, digest.hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--crosscheck",
        action="store_true",
        help="compare the fast K7 detector with the generic enumerator",
    )
    args = parser.parse_args()
    six_carriers = minimal_six_terminal_carriers()
    seven_kernels = irreducible_seven_vertex_kernels()
    cell, pairs, pair_index, states = noncommon_orbits()
    _n, _a, core, _x, _p, _q, terminals, *_ = cell
    has_k7 = FastK7(pairs, pair_index)

    successes = []
    failure_profile = collections.Counter()
    for orbit, (ones, _zeros, weight) in enumerate(states):
        universal_reserved = []
        first_failures = {}
        for reserved in terminals:
            labels = tuple(t for t in terminals if t != reserved)
            bad = None

            for carrier in six_carriers:
                lifted = lift_six_mask(carrier, labels, pair_index)
                if not has_k7(ones | lifted):
                    bad = ("order6", carrier)
                    break

            if bad is None:
                for terminal_mask, neighbours in seven_kernels:
                    if not any(
                        has_k7(
                            ones
                            | lift_six_mask(
                                owner_quotient(
                                    terminal_mask, neighbours, owner
                                ),
                                labels,
                                pair_index,
                            )
                        )
                        for owner in range(6)
                        if neighbours >> owner & 1
                    ):
                        bad = ("order7", terminal_mask, neighbours)
                        break

            if bad is None:
                universal_reserved.append(reserved)
            else:
                first_failures[reserved] = bad

        if universal_reserved:
            successes.append((orbit, weight, tuple(universal_reserved)))
        else:
            good = tuple(
                t
                for t in terminals
                if all(
                    ones >> pair_index[decoder.pair(i, t)] & 1
                    for i in core
                )
            )
            core_edges = sum(
                ones >> pair_index[edge] & 1
                for edge in itertools.combinations(core, 2)
            )
            failure_profile[(len(good), core_edges)] += weight
            print(
                "FAIL",
                orbit,
                "weight",
                weight,
                "good",
                good,
                "first",
                first_failures,
                flush=True,
            )

    success_orbits = {orbit for orbit, _weight, _r in successes}
    print("six-terminal terminal-legal kernel test")
    print("minimal order6 carriers", len(six_carriers))
    print("labelled irreducible order7 kernels", len(seven_kernels))
    print("catalogue_sha256", catalogue_digest(six_carriers, seven_kernels))
    print("noncommon_state_sha256", state_digest(states))
    print(
        "closed_orbits",
        len(successes),
        "closed_weight",
        sum(weight for _orbit, weight, _r in successes),
    )
    print(
        "failure_orbits",
        140 - len(successes),
        "failure_weight",
        7878 - sum(weight for _orbit, weight, _r in successes),
    )
    print("failure_profile", dict(sorted(failure_profile.items())))
    reserved_weight = collections.Counter()
    for _orbit, weight, reserved in successes:
        reserved_weight[len(reserved)] += weight
    print(
        "universal_reserved_count_weight",
        dict(sorted(reserved_weight.items())),
    )
    print(
        "universal_reserved_count_orbits",
        dict(
            sorted(
                collections.Counter(
                    len(reserved)
                    for _orbit, _weight, reserved in successes
                ).items()
            )
        ),
    )
    print("closed_orbit_indices", sorted(success_orbits))
    if args.crosscheck:
        tested, digest = crosscheck_fast_detector(
            states,
            terminals,
            pair_index,
            six_carriers,
            seven_kernels,
            has_k7,
        )
        print("generic_crosscheck", tested, "sha256", digest)


if __name__ == "__main__":
    main()
