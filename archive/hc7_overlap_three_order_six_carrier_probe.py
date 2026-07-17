#!/usr/bin/env python3
"""Probe rooted peripheral carriers in the order-six-arm overlap-three cell.

This is an exploratory, proof-producing finite layer.  It works only with
literal edges forced by the nine irredundant six-support constraints.  The
three carrier tests add rooted-bag adjacencies only after the original
relation has been joined.
"""

from __future__ import annotations

import argparse
import collections
import functools
import itertools

import hc7_cross_arm_overlap_three_kernel_decoder as decoder


def category_automorphisms():
    """Automorphisms preserving I, A-I, X-I, and the private-root pair."""

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
    for position, (u, v) in enumerate(pairs):
        if mask >> position & 1:
            answer |= 1 << pair_index[decoder.pair(image[u], image[v])]
    return answer


def canonical_key(ones, zeros, pairs, pair_index, automorphisms):
    return min(
        (
            transformed_mask(ones, image, pairs, pair_index),
            transformed_mask(zeros, image, pairs, pair_index),
        )
        for image in automorphisms
    )


def cyclic_orders(vertices):
    first = vertices[0]
    for tail in itertools.permutations(vertices[1:]):
        order = (first,) + tail
        if order[1] < order[-1]:
            yield order


def cycle_mask(order, pair_index):
    return sum(
        1 << pair_index[decoder.pair(order[i], order[(i + 1) % len(order)])]
        for i in range(len(order))
    )


def induced_mask(mask, selected, old_pairs):
    image = {old: new for new, old in enumerate(selected)}
    new_pairs = tuple(itertools.combinations(range(len(selected)), 2))
    new_index = {edge: position for position, edge in enumerate(new_pairs)}
    answer = 0
    for position, (u, v) in enumerate(old_pairs):
        if mask >> position & 1 and u in image and v in image:
            answer |= 1 << new_index[decoder.pair(image[u], image[v])]
    return answer


def all_cofacial_closes(ones, terminals, pair_index, specs):
    """For every facial order, some terminal can absorb the remainder."""

    tested = 0
    for order in cyclic_orders(terminals):
        tested += 1
        cycle = cycle_mask(order, pair_index)
        if not any(
            decoder.has_k_minor(
                ones
                | cycle
                | sum(
                    1 << pair_index[decoder.pair(centre, other)]
                    for other in terminals
                    if other != centre
                ),
                specs,
            )
            is not None
            for centre in terminals
        ):
            return False, order, tested
    return True, None, tested


def placed_split_mask(
    ones,
    old_pairs,
    common,
    boundary,
    off_face,
    singleton,
    order,
):
    """Quotient for one exact on-face/off-face placement of bad roots.

    ``singleton`` is kept outside the connected peripheral bag.  Every other
    off-face root is absorbed by that bag, so its literal incident edges are
    legitimate contacts of the carrier.
    """

    absorbed = tuple(vertex for vertex in off_face if vertex != singleton)
    retained = tuple(common) + tuple(boundary) + (singleton,)
    base = induced_mask(ones, retained, old_pairs)
    carrier = len(retained)
    order_n = carrier + 1
    expanded_pairs = tuple(itertools.combinations(range(order_n), 2))
    expanded_index = {edge: position for position, edge in enumerate(expanded_pairs)}
    mask = sum(
        1 << expanded_index[edge]
        for position, edge in enumerate(itertools.combinations(range(carrier), 2))
        if base >> position & 1
    )
    retained_image = {old: new for new, old in enumerate(retained)}
    boundary_labels = tuple(retained_image[old] for old in boundary)
    singleton_label = retained_image[singleton]

    mask |= cycle_mask(tuple(retained_image[old] for old in order), expanded_index)
    mask |= 1 << expanded_index[decoder.pair(carrier, singleton_label)]
    mask |= sum(
        1 << expanded_index[decoder.pair(carrier, vertex)]
        for vertex in boundary_labels
    )
    old_index = {edge: position for position, edge in enumerate(old_pairs)}
    for old in retained:
        if any(
            ones >> old_index[decoder.pair(old, absorbed_root)] & 1
            for absorbed_root in absorbed
        ):
            mask |= 1 << expanded_index[
                decoder.pair(carrier, retained_image[old])
            ]
    return mask, minor_specs(order_n)


def every_bad_placement_closes(ones, old_pairs, common, good, bad):
    """Test every possible nonempty set of bad roots lying off the face."""

    failures = []
    tested = 0
    for off_count in range(1, len(bad) + 1):
        for off_face in itertools.combinations(bad, off_count):
            boundary = tuple(good) + tuple(v for v in bad if v not in off_face)
            for order in cyclic_orders(boundary):
                tested += 1
                if not any(
                    decoder.has_k_minor(
                        *placed_split_mask(
                            ones,
                            old_pairs,
                            common,
                            boundary,
                            off_face,
                            singleton,
                            order,
                        )
                    )
                    is not None
                    for singleton in off_face
                ):
                    failures.append((off_face, order))
                    return False, failures, tested
    return True, failures, tested


@functools.lru_cache(maxsize=1)
def minimal_hamiltonian_three_connected_extensions():
    """Chord sets minimal for making one labelled C7 three-connected."""

    vertices = tuple(range(7))
    pairs = tuple(itertools.combinations(vertices, 2))
    pair_index = {edge: position for position, edge in enumerate(pairs)}
    cycle_edges = {
        decoder.pair(i, (i + 1) % len(vertices)) for i in vertices
    }
    cycle = sum(1 << pair_index[edge] for edge in cycle_edges)
    chords = tuple(edge for edge in pairs if edge not in cycle_edges)
    minimal = []
    for count in range(len(chords) + 1):
        for chosen in itertools.combinations(chords, count):
            chord_mask = sum(1 << pair_index[edge] for edge in chosen)
            if any(old & chord_mask == old for old in minimal):
                continue
            if decoder.is_three_connected(cycle | chord_mask, vertices, pair_index):
                minimal.append(chord_mask)
    return tuple(
        tuple(edge for edge in chords if mask >> pair_index[edge] & 1)
        for mask in minimal
    )


def terminal_kernel_closes(ones, terminals, pair_index, specs):
    """Test the exact order-seven/order-eight terminal-kernel carriers."""

    bad_cycles = []
    bad_hamiltonian_kernels = []
    bad_charged_cycles = []
    bad_bicliques = []
    extension_templates = minimal_hamiltonian_three_connected_extensions()
    for order, carrier in decoder.cycle_masks(terminals, pair_index):
        if decoder.has_k_minor(ones | carrier, specs) is not None:
            continue
        bad_cycles.append(order)

        for template in extension_templates:
            extension = sum(
                1 << pair_index[decoder.pair(order[u], order[v])]
                for u, v in template
            )
            if decoder.has_k_minor(ones | carrier | extension, specs) is None:
                bad_hamiltonian_kernels.append((order, template))

        for charged_positions in itertools.combinations(range(7), 4):
            charged = tuple(order[position] for position in charged_positions)
            if not any(
                decoder.has_k_minor(
                    ones
                    | carrier
                    | sum(
                        1 << pair_index[decoder.pair(centre, other)]
                        for other in charged
                        if other != centre
                    ),
                    specs,
                )
                is not None
                for centre in charged
            ):
                bad_charged_cycles.append((order, charged))

    for sides, carrier in decoder.k34_masks(terminals, pair_index):
        if decoder.has_k_minor(ones | carrier, specs) is None:
            bad_bicliques.append(sides)
    return (
        bad_cycles,
        bad_hamiltonian_kernels,
        bad_charged_cycles,
        bad_bicliques,
    )


def reserved_five_terminal_fan_strategy(ones, old_pairs, common, terminals):
    """Find a reserved root and omitted root for a universal rooted F5 lift.

    The carrier theorem is applied in ``H-r`` to the five selected terminals;
    the seventh terminal is deliberately unused because a rooted bag may
    absorb it.
    """

    for reserved in terminals:
        for omitted in terminals:
            if omitted == reserved:
                continue
            fan_roots = tuple(
                terminal
                for terminal in terminals
                if terminal not in (reserved, omitted)
            )
            retained = tuple(common) + (reserved,) + fan_roots
            base = induced_mask(ones, retained, old_pairs)
            local_pairs = tuple(itertools.combinations(range(len(retained)), 2))
            local_index = {
                edge: position for position, edge in enumerate(local_pairs)
            }
            local_roots = tuple(range(len(common) + 1, len(retained)))
            specs = minor_specs(len(retained))
            if all(
                decoder.has_k_minor(base | carrier, specs) is not None
                for _, carrier in decoder.fan_masks(local_roots, local_index)
            ):
                return reserved, omitted
    return None


def absorbed_omitted_fan_mask(
    ones,
    old_pairs,
    retained,
    omitted,
    host,
    carrier,
):
    """Add contacts inherited when ``omitted`` lies in rooted bag ``host``."""

    base = induced_mask(ones, retained, old_pairs)
    local_pairs = tuple(itertools.combinations(range(len(retained)), 2))
    local_index = {edge: position for position, edge in enumerate(local_pairs)}
    old_index = {edge: position for position, edge in enumerate(old_pairs)}
    retained_image = {old: new for new, old in enumerate(retained)}
    inherited = 0
    for old in retained:
        local = retained_image[old]
        if local == host:
            continue
        if ones >> old_index[decoder.pair(omitted, old)] & 1:
            inherited |= 1 << local_index[decoder.pair(host, local)]
    return base | carrier | inherited


def rooted_kernel_mask(
    ones,
    old_pairs,
    common,
    reserved,
    selected,
    omitted,
    terminal_edges,
    extra_neighbors,
    host,
):
    """Build one literal quotient of a spanning five-terminal kernel.

    ``extra_neighbors`` is ``None`` for a five-vertex kernel.  Otherwise an
    unrooted sixth kernel bag is appended and joined to the indicated
    selected terminal labels.  ``host`` records the kernel bag containing
    the omitted sixth terminal.
    """

    retained = tuple(common) + (reserved,) + tuple(selected)
    base = induced_mask(ones, retained, old_pairs)
    order_n = len(retained) + (extra_neighbors is not None)
    expanded_pairs = tuple(itertools.combinations(range(order_n), 2))
    expanded_index = {edge: position for position, edge in enumerate(expanded_pairs)}
    mask = sum(
        1 << expanded_index[edge]
        for position, edge in enumerate(itertools.combinations(range(len(retained)), 2))
        if base >> position & 1
    )
    image = {old: new for new, old in enumerate(retained)}
    mask |= sum(
        1 << expanded_index[decoder.pair(image[u], image[v])]
        for u, v in terminal_edges
    )
    extra = len(retained) if extra_neighbors is not None else None
    if extra is not None:
        mask |= sum(
            1 << expanded_index[decoder.pair(extra, image[root])]
            for root in extra_neighbors
        )

    old_index = {edge: position for position, edge in enumerate(old_pairs)}
    host_label = extra if host == "extra" else image[host]
    for old in retained:
        local = image[old]
        if local == host_label:
            continue
        if ones >> old_index[decoder.pair(omitted, old)] & 1:
            mask |= 1 << expanded_index[decoder.pair(host_label, local)]
    return mask, minor_specs(order_n)


def five_terminal_kernel_outcomes(selected):
    """Minimal labelled outcomes of the audited five-terminal kernel proof."""

    selected = tuple(selected)
    # Five-vertex kernel: its complement is a matching.  The edge-minimal
    # instances are K5 minus a matching of order two.
    for unmatched in selected:
        rest = tuple(root for root in selected if root != unmatched)
        first = rest[0]
        for mate in rest[1:]:
            remaining = tuple(root for root in rest if root not in (first, mate))
            missing = {decoder.pair(first, mate), decoder.pair(*remaining)}
            terminal_edges = tuple(
                edge
                for edge in itertools.combinations(selected, 2)
                if edge not in missing
            )
            yield terminal_edges, None

    # Six-vertex wheel kernel: a terminal C5 and a universal extra bag.
    for order in cyclic_orders(selected):
        terminal_edges = tuple(
            decoder.pair(order[i], order[(i + 1) % len(order)])
            for i in range(len(order))
        )
        yield terminal_edges, selected

    # Exceptional six-vertex kernel: y and the extra bag see all four
    # remaining roots, while those four roots contain a perfect matching.
    for y in selected:
        rest = tuple(root for root in selected if root != y)
        first = rest[0]
        for mate in rest[1:]:
            remaining = tuple(root for root in rest if root not in (first, mate))
            terminal_edges = tuple(
                [decoder.pair(y, root) for root in rest]
                + [decoder.pair(first, mate), decoder.pair(*remaining)]
            )
            yield terminal_edges, rest


def reserved_full_five_terminal_kernel_strategy(
    ones, old_pairs, common, terminals
):
    """Test every kernel outcome and every host of the omitted terminal."""

    for reserved in terminals:
        for omitted in terminals:
            if omitted == reserved:
                continue
            selected = tuple(
                terminal
                for terminal in terminals
                if terminal not in (reserved, omitted)
            )
            closes = True
            for terminal_edges, extra_neighbors in five_terminal_kernel_outcomes(
                selected
            ):
                hosts = selected + (("extra",) if extra_neighbors is not None else ())
                if any(
                    decoder.has_k_minor(
                        *rooted_kernel_mask(
                            ones,
                            old_pairs,
                            common,
                            reserved,
                            selected,
                            omitted,
                            terminal_edges,
                            extra_neighbors,
                            host,
                        )
                    )
                    is None
                    for host in hosts
                ):
                    closes = False
                    break
            if closes:
                return reserved, omitted
    return None


def reserved_spanning_five_fan_strategy(ones, old_pairs, common, terminals):
    """Use a spanning rooted F5 model and retain the omitted root's contacts."""

    for reserved in terminals:
        for omitted in terminals:
            if omitted == reserved:
                continue
            fan_roots = tuple(
                terminal
                for terminal in terminals
                if terminal not in (reserved, omitted)
            )
            retained = tuple(common) + (reserved,) + fan_roots
            local_pairs = tuple(itertools.combinations(range(len(retained)), 2))
            local_index = {
                edge: position for position, edge in enumerate(local_pairs)
            }
            local_roots = tuple(range(len(common) + 1, len(retained)))
            specs = minor_specs(len(retained))
            if all(
                decoder.has_k_minor(
                    absorbed_omitted_fan_mask(
                        ones,
                        old_pairs,
                        retained,
                        omitted,
                        host,
                        carrier,
                    ),
                    specs,
                )
                is not None
                for _, carrier in decoder.fan_masks(local_roots, local_index)
                for host in local_roots
            ):
                return reserved, omitted
    return None


def two_reserved_rooted_triangle_strategy(ones, old_pairs, common, terminals):
    """Find two reserved roots and a rooted-triangle quotient forcing K7.

    After reserving ``r,s``, four-connectivity leaves a two-connected graph.
    Any chosen three of the five other terminals therefore root a K3 model
    avoiding ``r,s``.  The two unchosen terminals are deliberately unused.
    """

    for reserved in itertools.combinations(terminals, 2):
        available = tuple(
            terminal for terminal in terminals if terminal not in reserved
        )
        for triangle_roots in itertools.combinations(available, 3):
            retained = tuple(common) + tuple(reserved) + triangle_roots
            base = induced_mask(ones, retained, old_pairs)
            local_pairs = tuple(itertools.combinations(range(len(retained)), 2))
            local_index = {
                edge: position for position, edge in enumerate(local_pairs)
            }
            triangle_labels = tuple(range(len(common) + 2, len(retained)))
            triangle = sum(
                1 << local_index[edge]
                for edge in itertools.combinations(triangle_labels, 2)
            )
            if decoder.has_k_minor(
                base | triangle, minor_specs(len(retained))
            ) is not None:
                return reserved, triangle_roots
    return None


def reserved_six_terminal_cycle_strategy(ones, old_pairs, common, terminals):
    """Find a root whose deletion leaves a universally closing rooted C6.

    A proposed structural theorem says that six prescribed terminals in a
    three-connected graph always root a C6.  Since the cyclic label order is
    not prescribed, every labelled C6 order must close for the chosen
    reserved root.
    """

    for reserved in terminals:
        cycle_roots = tuple(
            terminal for terminal in terminals if terminal != reserved
        )
        retained = tuple(common) + (reserved,) + cycle_roots
        base = induced_mask(ones, retained, old_pairs)
        local_pairs = tuple(itertools.combinations(range(len(retained)), 2))
        local_index = {
            edge: position for position, edge in enumerate(local_pairs)
        }
        local_roots = tuple(range(len(common) + 1, len(retained)))
        specs = minor_specs(len(retained))
        if all(
            decoder.has_k_minor(base | carrier, specs) is not None
            for order in cyclic_orders(local_roots)
            for carrier in (cycle_mask(order, local_index),)
        ):
            return reserved
    return None


@functools.lru_cache(maxsize=None)
def minor_specs(order_n):
    return decoder.partition_specs(order_n, 7)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--test-carriers",
        action="store_true",
        help="test the all-cofacial and exact off-face-placement carriers",
    )
    parser.add_argument(
        "--test-reserved-f5",
        action="store_true",
        help="test a five-root fan in H-r with one further terminal omitted",
    )
    parser.add_argument(
        "--test-two-reserved-k3",
        action="store_true",
        help="test a rooted K3 in H-{r,s}, with two further roots omitted",
    )
    parser.add_argument(
        "--test-combined-reserved",
        action="store_true",
        help="test reserved F5 first, then the two-reserved rooted K3",
    )
    parser.add_argument(
        "--test-reserved-c6",
        action="store_true",
        help="test every labelled rooted C6 in H-r for some reserved root",
    )
    parser.add_argument(
        "--test-spanning-reserved-f5",
        action="store_true",
        help="test rooted F5 after assigning the omitted root to every bag",
    )
    parser.add_argument(
        "--test-full-five-kernel",
        action="store_true",
        help="test every outcome of the full five-terminal irreducible kernel",
    )
    parser.add_argument(
        "--test-kernel-carriers",
        action="store_true",
        help="test every exact seven-terminal irreducible-kernel carrier",
    )
    parser.add_argument("--start", type=int, default=0)
    parser.add_argument("--stop", type=int)
    args = parser.parse_args()

    cell, pairs, pair_index, states = decoder.joined_states(6)
    n, a, common, x, p, q, terminals, supports, literal_fives = cell
    automorphisms = tuple(category_automorphisms())
    assert len(automorphisms) == 144
    orbit_weights = collections.Counter()
    representatives = {}
    noncommon_states = set()
    for ones, zeros in states:
        if decoder.common_rooted_k4(ones, n, a, common, p, q) is not None:
            continue
        noncommon_states.add((ones, zeros))
        key = canonical_key(ones, zeros, pairs, pair_index, automorphisms)
        orbit_weights[key] += 1
        representatives.setdefault(key, (ones, zeros))

    assert len(states) == 60162
    assert len(noncommon_states) == 7878
    assert len(representatives) == 140
    for key, (ones, zeros) in representatives.items():
        orbit = {
            (
                transformed_mask(ones, image, pairs, pair_index),
                transformed_mask(zeros, image, pairs, pair_index),
            )
            for image in automorphisms
        }
        assert orbit <= noncommon_states
        assert len(orbit) == orbit_weights[key]

    specs = decoder.partition_specs(n, 7)
    live = []
    direct_weight = 0
    for key, (ones, zeros) in representatives.items():
        if decoder.has_k_minor(ones, specs) is not None:
            direct_weight += orbit_weights[key]
            continue
        good = tuple(
            terminal
            for terminal in terminals
            if all(
                ones >> pair_index[decoder.pair(i, terminal)] & 1
                for i in common
            )
        )
        live.append((ones, zeros, good, orbit_weights[key]))

    good_weight = collections.Counter()
    good_orbits = collections.Counter()
    overlap_profile = collections.Counter()
    for _, _, good, weight in live:
        good_weight[len(good)] += weight
        good_orbits[len(good)] += 1
    for ones, _, good, weight in live:
        i_edges = sum(
            ones >> pair_index[edge] & 1
            for edge in itertools.combinations(common, 2)
        )
        overlap_profile[(len(good), i_edges)] += weight
    assert direct_weight == 1242
    assert len(live) == 110
    assert sum(good_weight.values()) == 6636
    assert good_weight == {4: 3663, 5: 1677, 6: 1296}
    assert good_orbits == {4: 45, 5: 35, 6: 30}
    assert overlap_profile == {
        (4, 3): 2592,
        (5, 3): 336,
        (4, 2): 1071,
        (5, 2): 1341,
        (6, 2): 1296,
    }

    print(
        "joined=60162",
        f"noncommon_orbits={len(representatives)}",
        f"direct_weight={direct_weight}",
        f"live_orbits={len(live)}",
        f"live_weight={sum(weight for _, _, _, weight in live)}",
    )
    print(
        "good_size_weight",
        sorted(good_weight.items()),
        "good_size_orbits",
        sorted(good_orbits.items()),
        "overlap_profile",
        sorted(overlap_profile.items()),
    )

    if (
        not args.test_carriers
        and not args.test_kernel_carriers
        and not args.test_reserved_f5
        and not args.test_two_reserved_k3
        and not args.test_combined_reserved
        and not args.test_reserved_c6
        and not args.test_spanning_reserved_f5
        and not args.test_full_five_kernel
    ):
        return

    selected_live = live[args.start : args.stop]
    if args.test_reserved_f5:
        no_strategy = []
        strategies = collections.Counter()
        for index, (ones, zeros, good, weight) in enumerate(selected_live, 1):
            strategy = reserved_five_terminal_fan_strategy(
                ones, pairs, common, terminals
            )
            if strategy is None:
                no_strategy.append((good, weight))
            else:
                strategies[strategy] += weight
            if index % 10 == 0:
                print(
                    f"reserved_f5_tested={index}/{len(selected_live)}",
                    f"no_strategy={len(no_strategy)}",
                    flush=True,
                )
        print("reserved_f5_no_strategy", len(no_strategy), no_strategy[:10])
        print("reserved_f5_strategies", sorted(strategies.items()))

    if args.test_two_reserved_k3:
        no_strategy = []
        strategies = collections.Counter()
        for index, (ones, zeros, good, weight) in enumerate(selected_live, 1):
            strategy = two_reserved_rooted_triangle_strategy(
                ones, pairs, common, terminals
            )
            if strategy is None:
                no_strategy.append((good, weight, ones, zeros))
            else:
                strategies[strategy] += weight
            if index % 10 == 0:
                print(
                    f"two_reserved_k3_tested={index}/{len(selected_live)}",
                    f"no_strategy={len(no_strategy)}",
                    flush=True,
                )
        print("two_reserved_k3_no_strategy", len(no_strategy), no_strategy)
        print("two_reserved_k3_strategies", sorted(strategies.items()))

    if args.test_combined_reserved:
        no_strategy = []
        mechanism_weight = collections.Counter()
        for index, (ones, zeros, good, weight) in enumerate(selected_live, 1):
            fan = reserved_five_terminal_fan_strategy(
                ones, pairs, common, terminals
            )
            if fan is not None:
                mechanism_weight["reserved_f5"] += weight
                continue
            triangle = two_reserved_rooted_triangle_strategy(
                ones, pairs, common, terminals
            )
            if triangle is not None:
                mechanism_weight["two_reserved_k3"] += weight
                continue
            i_edges = tuple(
                edge
                for edge in itertools.combinations(common, 2)
                if ones >> pair_index[edge] & 1
            )
            no_strategy.append(
                {
                    "good": good,
                    "weight": weight,
                    "i_edges": i_edges,
                    "ones": ones,
                    "zeros": zeros,
                }
            )
        print("combined_reserved_no_strategy", len(no_strategy), no_strategy)
        print("combined_reserved_mechanism_weight", sorted(mechanism_weight.items()))

    if args.test_reserved_c6:
        no_strategy = []
        strategies = collections.Counter()
        for index, (ones, zeros, good, weight) in enumerate(selected_live, 1):
            strategy = reserved_six_terminal_cycle_strategy(
                ones, pairs, common, terminals
            )
            if strategy is None:
                no_strategy.append((good, weight, ones, zeros))
            else:
                strategies[strategy] += weight
            if index % 10 == 0:
                print(
                    f"reserved_c6_tested={index}/{len(selected_live)}",
                    f"no_strategy={len(no_strategy)}",
                    flush=True,
                )
        print("reserved_c6_no_strategy", len(no_strategy), no_strategy)
        print("reserved_c6_strategies", sorted(strategies.items()))

    if args.test_spanning_reserved_f5:
        no_strategy = []
        strategies = collections.Counter()
        for index, (ones, zeros, good, weight) in enumerate(selected_live, 1):
            strategy = reserved_spanning_five_fan_strategy(
                ones, pairs, common, terminals
            )
            if strategy is None:
                no_strategy.append((good, weight, ones, zeros))
            else:
                strategies[strategy] += weight
            if index % 10 == 0:
                print(
                    f"spanning_reserved_f5_tested={index}/{len(selected_live)}",
                    f"no_strategy={len(no_strategy)}",
                    flush=True,
                )
        print("spanning_reserved_f5_no_strategy", len(no_strategy), no_strategy)
        print("spanning_reserved_f5_strategies", sorted(strategies.items()))

    if args.test_full_five_kernel:
        no_strategy = []
        strategies = collections.Counter()
        for index, (ones, zeros, good, weight) in enumerate(selected_live, 1):
            strategy = reserved_full_five_terminal_kernel_strategy(
                ones, pairs, common, terminals
            )
            if strategy is None:
                no_strategy.append((good, weight, ones, zeros))
            else:
                strategies[strategy] += weight
            if index % 10 == 0:
                print(
                    f"full_five_kernel_tested={index}/{len(selected_live)}",
                    f"no_strategy={len(no_strategy)}",
                    flush=True,
                )
        print("full_five_kernel_no_strategy", len(no_strategy), no_strategy)
        print("full_five_kernel_strategies", sorted(strategies.items()))

    if args.test_kernel_carriers:
        cycle_bad = []
        hamiltonian_kernel_bad = []
        charged_cycle_bad = []
        biclique_bad = []
        for index, (ones, zeros, good, weight) in enumerate(selected_live, 1):
            (
                bad_cycles,
                bad_hamiltonian_kernels,
                bad_charged_cycles,
                bad_bicliques,
            ) = terminal_kernel_closes(ones, terminals, pair_index, specs)
            if bad_cycles:
                cycle_bad.append((good, bad_cycles[0], len(bad_cycles), weight))
            if bad_bicliques:
                biclique_bad.append(
                    (good, bad_bicliques[0], len(bad_bicliques), weight)
                )
            if bad_hamiltonian_kernels:
                hamiltonian_kernel_bad.append(
                    (
                        good,
                        bad_hamiltonian_kernels[0],
                        len(bad_hamiltonian_kernels),
                        weight,
                    )
                )
            if bad_charged_cycles:
                charged_cycle_bad.append(
                    (
                        good,
                        bad_charged_cycles[0],
                        len(bad_charged_cycles),
                        weight,
                    )
                )
            if index % 10 == 0:
                print(
                    f"kernel_tested={index}/{len(selected_live)}",
                    f"cycle_bad={len(cycle_bad)}",
                    f"hamiltonian_kernel_bad={len(hamiltonian_kernel_bad)}",
                    f"charged_cycle_bad={len(charged_cycle_bad)}",
                    f"biclique_bad={len(biclique_bad)}",
                    flush=True,
                )
        print("cycle_bad", len(cycle_bad), cycle_bad[:10])
        print("hamiltonian_kernel_bad", len(hamiltonian_kernel_bad), hamiltonian_kernel_bad[:10])
        print("charged_cycle_bad", len(charged_cycle_bad), charged_cycle_bad[:10])
        print("biclique_bad", len(biclique_bad), biclique_bad[:10])

    if not args.test_carriers:
        return

    cofacial_bad = []
    split_bad = []
    cofacial_orders = 0
    placement_orders = 0
    for index, (ones, zeros, good, weight) in enumerate(selected_live, 1):
        closes, order, tested = all_cofacial_closes(
            ones, terminals, pair_index, specs
        )
        cofacial_orders += tested
        if not closes:
            cofacial_bad.append((good, order, weight))
        bad = tuple(terminal for terminal in terminals if terminal not in good)
        closes, failure, tested = every_bad_placement_closes(
            ones, pairs, common, good, bad
        )
        placement_orders += tested
        if not closes:
            split_bad.append((good, failure, weight))
        if index % 5 == 0:
            print(
                f"tested={index}/{len(selected_live)}",
                f"cofacial_bad={len(cofacial_bad)}",
                f"split_bad={len(split_bad)}",
                flush=True,
            )

    print("cofacial_bad", len(cofacial_bad), cofacial_bad[:10])
    print("split_bad", len(split_bad), split_bad[:10])
    print(
        "tested_orders",
        f"cofacial={cofacial_orders}",
        f"off_face_placements={placement_orders}",
    )


if __name__ == "__main__":
    main()
