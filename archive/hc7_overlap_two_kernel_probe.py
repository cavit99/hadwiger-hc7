#!/usr/bin/env python3
"""Explore bounded rooted-kernel carriers in the rigid overlap-two cells.

This is a falsifier/proof-discovery script.  It joins the exact local
relations but does not promote a theorem by itself.
"""

from __future__ import annotations

import argparse
import collections
import functools
import itertools

import hc7_cross_arm_overlap_three_kernel_decoder as relation
import hc7_overlap_three_six_terminal_kernel_verify as six_kernel


class FastK7:
    """Exact K7-minor detector for a quotient of order at most eleven."""

    def __init__(self, order, pairs, pair_index):
        self.order = order
        self.pairs = pairs
        self.pair_index = pair_index
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
        for i, (left, right) in enumerate(self.pairs):
            if edges >> i & 1:
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

        # A seven-bag model on at most eleven objects has at least three
        # singleton bags.  Enumerate their clique, then search exactly for
        # the remaining pairwise adjacent connected bags.  Unused objects
        # are allowed.
        for core_size in range(7, 2, -1):
            bag_count = 7 - core_size
            for core_vertices in itertools.combinations(
                range(self.order), core_size
            ):
                if any(
                    not (adj[left] >> right & 1)
                    for left, right in itertools.combinations(
                        core_vertices, 2
                    )
                ):
                    continue
                if bag_count == 0:
                    return True
                core = sum(1 << vertex for vertex in core_vertices)
                remainder = self.full ^ core
                candidates = []
                subset = remainder
                while subset:
                    if connected(subset) and all(
                        touches(subset, 1 << vertex)
                        for vertex in core_vertices
                    ):
                        candidates.append(subset)
                    subset = (subset - 1) & remainder

                def search(start, chosen, used):
                    if len(chosen) == bag_count:
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


def build_cell(arm_order: int):
    common = (0, 1)
    a = tuple(range(6))
    if arm_order == 5:
        n = 10
        x = common + (6, 7)
        p, q = 8, 9
    elif arm_order == 6:
        n = 11
        x = common + (6, 7, 8)
        p, q = 9, 10
    else:
        raise ValueError(arm_order)
    terminals = tuple(v for v in range(n) if v not in common)
    supports_six = [a]
    literal_fives = []
    if arm_order == 5:
        literal_fives.extend((x + (p,), x + (q,)))
    else:
        supports_six.extend((x + (p,), x + (q,)))
    for omitted in common:
        base = tuple(v for v in a if v != omitted)
        supports_six.extend((base + (p,), base + (q,)))
    return (
        n,
        a,
        common,
        x,
        p,
        q,
        terminals,
        tuple(supports_six),
        tuple(literal_fives),
    )


def global_patterns(support, pair_index):
    local_pairs = tuple(itertools.combinations(range(6), 2))
    indices = tuple(
        pair_index[relation.pair(support[u], support[v])]
        for u, v in local_pairs
    )
    return tuple(
        (
            sum(1 << indices[i] for i in range(15) if ones >> i & 1),
            sum(1 << indices[i] for i in range(15) if zeros >> i & 1),
        )
        for ones, zeros in relation.LOCAL_SIX
    )


def joined_states(arm_order: int):
    cell = build_cell(arm_order)
    n, _a, _common, _x, _p, _q, _terminals, supports, literal = cell
    pairs = tuple(itertools.combinations(range(n), 2))
    pair_index = {edge: i for i, edge in enumerate(pairs)}
    constraints = [global_patterns(support, pair_index) for support in supports]
    fixed_ones = 0
    for five in literal:
        for edge in itertools.combinations(five, 2):
            fixed_ones |= 1 << pair_index[edge]
    states = set()

    def visit(done, ones, zeros):
        if ones & zeros:
            return
        if len(done) == len(constraints):
            states.add((ones, zeros))
            return
        selected = None
        compatible = None
        for i, patterns in enumerate(constraints):
            if i in done:
                continue
            options = tuple(
                pattern
                for pattern in patterns
                if not (pattern[0] & zeros or pattern[1] & ones)
            )
            if compatible is None or len(options) < len(compatible):
                selected, compatible = i, options
        seen = set()
        for pattern_ones, pattern_zeros in compatible:
            new = ones | pattern_ones, zeros | pattern_zeros
            if new in seen:
                continue
            seen.add(new)
            visit(done | {selected}, *new)

    visit(frozenset(), fixed_ones, 0)
    return cell, pairs, pair_index, states


def category_automorphisms(arm_order: int):
    cell = build_cell(arm_order)
    n, a, common, x, p, q, _terminals, _supports, _literal = cell
    categories = (
        common,
        tuple(v for v in a if v not in common),
        tuple(v for v in x if v not in common),
        (p, q),
    )
    for images in itertools.product(
        *(tuple(itertools.permutations(category)) for category in categories)
    ):
        image = list(range(n))
        for category, permuted in zip(categories, images):
            for old, new in zip(category, permuted):
                image[old] = new
        yield tuple(image)


def category_generators(arm_order: int):
    cell = build_cell(arm_order)
    n, a, common, x, p, q, _terminals, _supports, _literal = cell
    categories = (
        common,
        tuple(v for v in a if v not in common),
        tuple(v for v in x if v not in common),
        (p, q),
    )
    for category in categories:
        for left, right in zip(category, category[1:]):
            image = list(range(n))
            image[left], image[right] = image[right], image[left]
            yield tuple(image)


def transformed_mask(mask, image, pairs, pair_index):
    return sum(
        1 << pair_index[relation.pair(image[left], image[right])]
        for i, (left, right) in enumerate(pairs)
        if mask >> i & 1
    )


def noncommon_orbits(arm_order: int):
    cell, pairs, pair_index, states = joined_states(arm_order)
    n, a, common, _x, p, q, _terminals, _supports, _literal = cell
    generators = tuple(category_generators(arm_order))
    bit_maps = tuple(
        tuple(
            1 << pair_index[relation.pair(image[left], image[right])]
            for left, right in pairs
        )
        for image in generators
    )


def minimal_forced_orbits(arm_order, pairs, pair_index, noncommon):
    """Inclusion-minimal forced-one masks, modulo category symmetry."""

    masks = sorted({ones for ones, _zeros in noncommon}, key=int.bit_count)
    minimal = []
    for mask in masks:
        if not any(old & mask == old for old in minimal):
            minimal.append(mask)
    minimal_set = set(minimal)

    generators = tuple(category_generators(arm_order))
    bit_maps = tuple(
        tuple(
            1 << pair_index[relation.pair(image[left], image[right])]
            for left, right in pairs
        )
        for image in generators
    )

    def transform(mask, bit_map):
        answer = 0
        while mask:
            bit = mask & -mask
            answer |= bit_map[bit.bit_length() - 1]
            mask -= bit
        return answer

    unseen = set(minimal_set)
    representatives = []
    while unseen:
        representative = unseen.pop()
        orbit = {representative}
        stack = [representative]
        while stack:
            current = stack.pop()
            for bit_map in bit_maps:
                image = transform(current, bit_map)
                assert image in minimal_set
                if image not in orbit:
                    orbit.add(image)
                    stack.append(image)
        unseen.difference_update(orbit)
        representatives.append((representative, 0))
    return tuple(minimal), tuple(representatives)

    def fast_transform(mask, bit_map):
        answer = 0
        while mask:
            bit = mask & -mask
            answer |= bit_map[bit.bit_length() - 1]
            mask -= bit
        return answer
    noncommon = {
        state
        for state in states
        if relation.common_rooted_k4(state[0], n, a, common, p, q) is None
    }
    unseen = set(noncommon)
    representatives = []
    while unseen:
        state = unseen.pop()
        orbit = {state}
        stack = [state]
        while stack:
            current = stack.pop()
            for bit_map in bit_maps:
                transformed = (
                    fast_transform(current[0], bit_map),
                    fast_transform(current[1], bit_map),
                )
                if transformed not in orbit:
                    orbit.add(transformed)
                    stack.append(transformed)
        assert orbit <= noncommon
        unseen.difference_update(orbit)
        representatives.append((*state, len(orbit)))
    return (
        cell,
        pairs,
        pair_index,
        tuple(representatives),
    )


def six_terminal_kernel_test(cell, pairs, pair_index, states):
    n, _a, common, _x, _p, _q, terminals, _supports, _literal = cell
    assert n == 10 and len(common) == 2 and len(terminals) == 8
    detector = six_kernel.FastK7(pairs, pair_index)
    carriers = six_kernel.minimal_six_terminal_carriers()
    kernels = six_kernel.irreducible_seven_vertex_kernels()
    successes = []
    failures = []
    direct_weight = 0
    for index, (ones, _zeros, weight) in enumerate(states):
        if detector(ones):
            direct_weight += weight
            continue
        valid_pairs = []
        first_failure = {}
        for reserved in itertools.combinations(terminals, 2):
            labels = tuple(v for v in terminals if v not in reserved)
            bad = None
            for carrier in carriers:
                if not detector(
                    ones
                    | six_kernel.lift_six_mask(carrier, labels, pair_index)
                ):
                    bad = ("order6", carrier)
                    break
            if bad is None:
                for terminal_mask, neighbours in kernels:
                    if not any(
                        detector(
                            ones
                            | six_kernel.lift_six_mask(
                                six_kernel.owner_quotient(
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
                valid_pairs.append(reserved)
            else:
                first_failure[reserved] = bad
        if valid_pairs:
            successes.append((index, weight, tuple(valid_pairs)))
        else:
            failures.append((index, ones, weight, first_failure))
            print(
                "FAIL",
                index,
                "weight",
                weight,
                "missing",
                [edge for i, edge in enumerate(pairs) if not ones >> i & 1],
                "first",
                first_failure,
                flush=True,
            )
    print("direct_weight", direct_weight)
    print(
        "kernel_closed_orbits",
        len(successes),
        "weight",
        sum(item[1] for item in successes),
    )
    print(
        "kernel_failure_orbits",
        len(failures),
        "weight",
        sum(item[2] for item in failures),
    )
    print(
        "valid_reserve_count",
        dict(
            sorted(
                collections.Counter(
                    len(valid) for _index, _weight, valid in successes
                ).items()
            )
        ),
    )


def seven_terminal_light_test(cell, pairs, pair_index, states, limit=None):
    n, _a, _common, _x, _p, _q, terminals, _supports, _literal = cell
    assert n == 11 and len(terminals) == 9
    detector = FastK7(n, pairs, pair_index)
    failures = []
    tested = 0
    direct = 0
    for ones, _zeros in states:
        if detector(ones):
            direct += 1
            continue
        tested += 1
        valid = []
        first_bad = {}
        for reserved in itertools.combinations(terminals, 2):
            labels = tuple(vertex for vertex in terminals if vertex not in reserved)
            bad = None
            carriers = itertools.chain(
                relation.cycle_masks(labels, pair_index),
                relation.k34_masks(labels, pair_index),
            )
            for kind_index, (label, carrier) in enumerate(carriers):
                if not detector(ones | carrier):
                    bad = (
                        "cycle" if kind_index < 360 else "k34",
                        label,
                    )
                    break
            if bad is None:
                valid.append(reserved)
            else:
                first_bad[reserved] = bad
        if not valid:
            failures.append((ones, first_bad))
            print(
                "LIGHT_FAIL",
                "nonedges",
                [edge for i, edge in enumerate(pairs) if not ones >> i & 1],
                "first",
                first_bad,
                flush=True,
            )
            break
        if limit is not None and tested >= limit:
            break
    print("seven_light_direct", direct, "tested", tested)
    print("seven_light_failures", len(failures))


@functools.lru_cache(maxsize=1)
def minimal_seven_terminal_carriers():
    """All labelled edge-minimal three-connected graphs on seven roots."""

    import hc7_seven_terminal_kernel_dichotomy_probe as kernel_probe

    local_pairs, local_index = six_kernel.pair_data(7)
    carriers = set()
    type_count = 0
    for graph in kernel_probe.graphs_of_order(7):
        if kernel_probe.nx.node_connectivity(graph) < 3:
            continue
        minimal = True
        for edge in tuple(graph.edges):
            reduced = graph.copy()
            reduced.remove_edge(*edge)
            if kernel_probe.nx.node_connectivity(reduced) >= 3:
                minimal = False
                break
        if not minimal:
            continue
        type_count += 1
        for image in itertools.permutations(range(7)):
            carriers.add(
                sum(
                    1
                    << local_index[
                        relation.pair(image[left], image[right])
                    ]
                    for left, right in graph.edges
                )
            )
    carriers = tuple(sorted(carriers))
    assert type_count == 5
    assert len(carriers) == 5495
    assert collections.Counter(mask.bit_count() for mask in carriers) == {
        11: 5040,
        12: 455,
    }
    return carriers


def lift_local_mask(mask, labels, pair_index):
    local_pairs, _local_index = six_kernel.pair_data(len(labels))
    return sum(
        1 << pair_index[relation.pair(labels[left], labels[right])]
        for i, (left, right) in enumerate(local_pairs)
        if mask >> i & 1
    )


def seven_terminal_full_order_seven_test(
    cell, pairs, pair_index, states, limit=None
):
    n, _a, _common, _x, _p, _q, terminals, _supports, _literal = cell
    assert n == 11 and len(terminals) == 9
    detector = FastK7(n, pairs, pair_index)
    carriers = minimal_seven_terminal_carriers()
    tested = 0
    failures = []
    for ones, _zeros in states:
        if detector(ones):
            continue
        tested += 1
        valid = []
        first_bad = {}
        for reserved in itertools.combinations(terminals, 2):
            labels = tuple(vertex for vertex in terminals if vertex not in reserved)
            bad = next(
                (
                    carrier
                    for carrier in carriers
                    if not detector(
                        ones
                        | lift_local_mask(carrier, labels, pair_index)
                    )
                ),
                None,
            )
            if bad is None:
                valid.append(reserved)
            else:
                first_bad[reserved] = bad
        if not valid:
            failures.append((ones, first_bad))
            print(
                "ORDER7_FAIL",
                "nonedges",
                [edge for i, edge in enumerate(pairs) if not ones >> i & 1],
                "first_bad_masks",
                first_bad,
                flush=True,
            )
            break
        print("ORDER7_PASS", tested, "valid", valid, flush=True)
        if limit is not None and tested >= limit:
            break
    print("order7_full_tested", tested, "failures", len(failures))


def seven_terminal_charged_cycle_test(
    cell, pairs, pair_index, states, limit=None, fixed_private=False
):
    """Test the exact minimal order-eight kernel carrier guarantee."""

    n, _a, _common, _x, p, q, terminals, _supports, _literal = cell
    assert n == 11 and len(terminals) == 9
    detector = FastK7(n, pairs, pair_index)
    tested = 0
    failures = []
    for ones, _zeros in states:
        if detector(ones):
            continue
        tested += 1
        valid = []
        first_bad = {}
        reserve_pairs = (
            ((p, q),)
            if fixed_private
            else itertools.combinations(terminals, 2)
        )
        for reserved in reserve_pairs:
            labels = tuple(vertex for vertex in terminals if vertex not in reserved)
            bad = None
            for cycle_order, cycle in relation.cycle_masks(labels, pair_index):
                for charge in itertools.combinations(labels, 4):
                    missed = tuple(vertex for vertex in labels if vertex not in charge)
                    # A cycle plus a hub with exactly these four neighbours
                    # is three-connected only if the three missed rim
                    # vertices are independent on the cycle.
                    if any(
                        cycle >> pair_index[relation.pair(left, right)] & 1
                        for left, right in itertools.combinations(missed, 2)
                    ):
                        continue
                    if not any(
                        detector(
                            ones
                            | cycle
                            | sum(
                                1 << pair_index[relation.pair(owner, other)]
                                for other in charge
                                if other != owner
                            )
                        )
                        for owner in charge
                    ):
                        bad = (cycle_order, charge)
                        break
                if bad is not None:
                    break
            if bad is None:
                valid.append(reserved)
            else:
                first_bad[reserved] = bad
        if not valid:
            failures.append((ones, first_bad))
            print(
                "CHARGED_FAIL",
                "nonedges",
                [edge for i, edge in enumerate(pairs) if not ones >> i & 1],
                "first",
                first_bad,
                flush=True,
            )
            break
        print("CHARGED_PASS", tested, "valid", valid, flush=True)
        if limit is not None and tested >= limit:
            break
    print("charged_cycle_tested", tested, "failures", len(failures))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--arm-order", type=int, choices=(5, 6), required=True)
    parser.add_argument("--test-six-kernel", action="store_true")
    parser.add_argument("--test-seven-light", action="store_true")
    parser.add_argument("--test-seven-order7", action="store_true")
    parser.add_argument("--test-seven-order8", action="store_true")
    parser.add_argument("--limit", type=int)
    parser.add_argument("--fixed-private", action="store_true")
    parser.add_argument("--orbits-only", action="store_true")
    parser.add_argument("--minimal-reps", action="store_true")
    args = parser.parse_args()
    cell, pairs, pair_index, states = joined_states(args.arm_order)
    n, a, common, _x, p, q, terminals, supports, literal = cell
    noncommon = [
        state
        for state in states
        if relation.common_rooted_k4(
            state[0], n, a, common, p, q
        )
        is None
    ]
    unknown = {}
    for ones, zeros in noncommon:
        count = len(pairs) - (ones | zeros).bit_count()
        unknown[count] = unknown.get(count, 0) + 1
    print("arm_order", args.arm_order)
    print("terminals", terminals)
    print("supports", len(supports), "literal", len(literal))
    print("joined", len(states), "noncommon", len(noncommon))
    print("unknown_noncommon", sorted(unknown.items()))
    selected_noncommon = noncommon
    if args.minimal_reps:
        minimal, representatives = minimal_forced_orbits(
            args.arm_order, pairs, pair_index, noncommon
        )
        print(
            "minimal_forced",
            len(minimal),
            "minimal_orbits",
            len(representatives),
            "edge_hist",
            dict(sorted(collections.Counter(map(int.bit_count, minimal)).items())),
        )
        selected_noncommon = representatives
    if args.orbits_only:
        _orbit_cell, _orbit_pairs, _orbit_index, orbits = noncommon_orbits(
            args.arm_order
        )
        print(
            "noncommon_orbits",
            len(orbits),
            "weight",
            sum(weight for _ones, _zeros, weight in orbits),
        )
    if args.test_six_kernel:
        if args.arm_order != 5:
            raise ValueError("the six-terminal test is for arm order five")
        orbit_cell, orbit_pairs, orbit_index, orbits = noncommon_orbits(5)
        print("noncommon_orbits", len(orbits))
        assert sum(weight for _ones, _zeros, weight in orbits) == len(noncommon)
        six_terminal_kernel_test(
            orbit_cell, orbit_pairs, orbit_index, orbits
        )
    if args.test_seven_light:
        if args.arm_order != 6:
            raise ValueError("the seven-terminal test is for arm order six")
        seven_terminal_light_test(
            cell, pairs, pair_index, selected_noncommon, args.limit
        )
    if args.test_seven_order7:
        if args.arm_order != 6:
            raise ValueError("the seven-terminal test is for arm order six")
        seven_terminal_full_order_seven_test(
            cell, pairs, pair_index, selected_noncommon, args.limit
        )
    if args.test_seven_order8:
        if args.arm_order != 6:
            raise ValueError("the seven-terminal test is for arm order six")
        seven_terminal_charged_cycle_test(
            cell,
            pairs,
            pair_index,
            selected_noncommon,
            args.limit,
            args.fixed_private,
        )


if __name__ == "__main__":
    main()
