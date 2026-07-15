#!/usr/bin/env python3
"""Certificate for the order-five-arm, overlap-three decoder.

The local relation and branch-model routines are imported from the adjacent
generic overlap-three decoder.  Both files use only Python's standard
library.  Original support edges and virtual rooted-carrier edges remain
separate until the final model test.
"""

from __future__ import annotations

import itertools

import hc7_cross_arm_overlap_three_kernel_decoder as decoder


def residuals():
    cell, pairs, pair_index, states = decoder.joined_states(5)
    n, a, common, x, p, q, terminals, supports, literal_fives = cell
    specs = decoder.partition_specs(n, 7)
    completed = set(decoder.completions(states, len(pairs)))
    common_states = []
    direct_states = []
    live = []
    for edges in completed:
        if decoder.common_rooted_k4(edges, n, a, common, p, q) is not None:
            common_states.append(edges)
        elif decoder.has_k_minor(edges, specs) is not None:
            direct_states.append(edges)
        else:
            live.append(edges)
    assert (len(states), len(completed), len(common_states), len(direct_states), len(live)) == (
        435,
        6960,
        6576,
        312,
        72,
    )
    return cell, pairs, pair_index, specs, live


def main() -> None:
    cell, pairs, pair_index, specs, live = residuals()
    n, a, common, x, p, q, terminals, supports, literal_fives = cell

    # Every residue has one bad left terminal.  The other five terminals
    # are complete to all three common-core vertices.
    data = []
    deficit_hist: dict[int, int] = {}
    for edges in live:
        bad = tuple(
            t
            for t in terminals
            if any(not (edges >> pair_index[decoder.pair(i, t)] & 1) for i in common)
        )
        assert len(bad) == 1 and bad[0] in (3, 4, 5)
        b = bad[0]
        good = tuple(t for t in terminals if t != b)
        assert all(
            edges >> pair_index[decoder.pair(i, t)] & 1
            for i in common
            for t in good
        )
        missed = sum(
            not (edges >> pair_index[decoder.pair(i, b)] & 1) for i in common
        )
        assert missed in (2, 3)
        deficit_hist[missed] = deficit_hist.get(missed, 0) + 1
        data.append((edges, b, good))
    assert deficit_hist == {2: 54, 3: 18}

    # If all six terminals lie on one face, the four-connected carrier
    # theorem gives the fixed facial cycle with any prescribed universal
    # terminal.  One of those six fan choices always has a K7 certificate.
    cycles = tuple(decoder.cycle_masks(terminals, pair_index))
    assert len(cycles) == 60
    for order, cycle in cycles:
        for edges, _, _ in data:
            witnesses = []
            for centre in terminals:
                fan = cycle
                for t in terminals:
                    if t != centre:
                        fan |= 1 << pair_index[decoder.pair(centre, t)]
                model = decoder.has_k_minor(edges | fan, specs)
                if model is not None:
                    witnesses.append((centre, model))
            assert witnesses, (order, edges)

    # In the five-good cofacial branch, a literal edge between two good
    # terminals must be a boundary-cycle edge.  Twenty-four residues are
    # therefore impossible.  Every feasible residue has one facial order,
    # the literal good-terminal graph is P5, and the bad-terminal wheel is
    # the exact survivor.  Any one of the five absent rim chords repairs it.
    impossible = feasible = wheel_survivors = repairs = expanded_closures = 0
    expanded_pairs = tuple(itertools.combinations(range(10), 2))
    expanded_index = {edge: index for index, edge in enumerate(expanded_pairs)}
    expanded_specs = decoder.partition_specs(10, 7)
    for edges, bad, good in data:
        literal_good = {
            edge
            for edge in itertools.combinations(good, 2)
            if edges >> pair_index[edge] & 1
        }
        facial_orders = []
        first = good[0]
        for tail in itertools.permutations(good[1:]):
            order = (first,) + tail
            if order[1] > order[-1]:
                continue
            rim = {
                decoder.pair(order[i], order[(i + 1) % 5]) for i in range(5)
            }
            if literal_good <= rim:
                facial_orders.append((order, rim))
        if not facial_orders:
            impossible += 1
            continue
        feasible += 1
        assert len(facial_orders) == 1
        assert len(literal_good) == 4
        assert sorted(
            sum(vertex in edge for edge in literal_good) for vertex in good
        ) == [1, 1, 2, 2, 2]
        _, rim = facial_orders[0]
        wheel = 0
        for terminal in good:
            wheel |= 1 << pair_index[decoder.pair(bad, terminal)]
        for edge in rim:
            wheel |= 1 << pair_index[edge]
        assert decoder.has_k_minor(edges | wheel, specs) is None
        wheel_survivors += 1
        for chord in set(itertools.combinations(good, 2)) - rim:
            assert decoder.has_k_minor(
                edges | wheel | (1 << pair_index[chord]), specs
            ) is not None
            repairs += 1
        # Preserve b as a singleton and replace the collapsed b-hub by the
        # connected remainder D=(H-b)-C.  D is universal to the five rim
        # bags and adjacent to b.  Label D by 9 in this finite layer.
        expanded_edges = {
            edge for edge in pairs if edges >> pair_index[edge] & 1
        }
        expanded_edges.update(rim)
        expanded_edges.update(decoder.pair(9, terminal) for terminal in good)
        expanded_edges.add(decoder.pair(9, bad))
        expanded_mask = sum(1 << expanded_index[edge] for edge in expanded_edges)
        assert decoder.has_k_minor(expanded_mask, expanded_specs) is not None
        expanded_closures += 1
    assert (impossible, feasible, wheel_survivors, repairs) == (24, 48, 48, 240)
    assert expanded_closures == 48

    print("order-five-arm overlap-three decoder: verified")
    print("joins=435 completions=6960 common=6576 direct=312 live=72")
    print("unique bad terminal: two missed core contacts=54, three=18")
    print("all-six cofacial: every one of 60 orders closes with some fan centre")
    print("five-good cofacial: impossible=24, P5-wheel=48, chord repairs=240")
    print("preserved b + peripheral D: all 48 wheel states close")


if __name__ == "__main__":
    main()
