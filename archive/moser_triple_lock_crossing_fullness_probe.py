#!/usr/bin/env python3
"""Add the contacts forced when crossing carriers partition a full shore."""

from itertools import product

from moser_triple_lock_opposite_crossing_probe import (
    E, F, FRAMES, U, W, base_edges, find_model, fmt,
)

BTERM = 3


def main():
    for pair in ((0, 5), (6, 0)):
        base, shield = base_edges(pair)
        print("TRIPLE", pair, "shield", shield, flush=True)
        for frame in FRAMES:
            e, f = tuple(frame)
            edges0 = set(base) | {frozenset((E, F))}
            edges0 |= {frozenset((E, z)) for z in e}
            edges0 |= {frozenset((F, z)) for z in f}
            leftover = sorted((U | {W, BTERM}) - set(e) - set(f))
            bad = []
            first = None
            for state in product((1, 2, 3), repeat=len(leftover)):
                # 1=E only, 2=F only, 3=both.
                edges = set(edges0)
                for z, side in zip(leftover, state):
                    if side & 1:
                        edges.add(frozenset((E, z)))
                    if side & 2:
                        edges.add(frozenset((F, z)))
                model = find_model(edges)
                if model is None:
                    bad.append((state, leftover))
                elif first is None:
                    first = (state, fmt(model))
            print(" frame", "E", sorted(e), "F", sorted(f),
                  "left", leftover, "bad", len(bad), "first", first,
                  flush=True)
            if bad:
                print("  bad states", bad, flush=True)
            # For the 05 triple, finish the atlas by adding every optional
            # cross-contact at the four frame endpoints.  Positive states
            # need no refinement (monotonicity); only the bad full-contact
            # states can have maximal bad superstates.
            if pair == (0, 5) and bad:
                endpoint_options = [(E, z) for z in f] + [(F, z) for z in e]
                maximal_rows = []
                for state, _ in bad:
                    exact = set(edges0)
                    for z, side in zip(leftover, state):
                        if side & 1:
                            exact.add(frozenset((E, z)))
                        if side & 2:
                            exact.add(frozenset((F, z)))
                    bad_bits = []
                    for bits in product((0, 1), repeat=4):
                        trial = set(exact)
                        trial |= {
                            frozenset(endpoint_options[i])
                            for i, bit in enumerate(bits) if bit
                        }
                        if find_model(trial) is None:
                            bad_bits.append(bits)
                    maximal = [
                        bits for bits in bad_bits
                        if not any(
                            bits != other and all(x <= y for x, y in zip(bits, other))
                            for other in bad_bits
                        )
                    ]
                    for bits in maximal:
                        row_e = set(e)
                        row_f = set(f)
                        for z, side in zip(leftover, state):
                            if side & 1:
                                row_e.add(z)
                            if side & 2:
                                row_f.add(z)
                        for bit, (helper, z) in zip(bits, endpoint_options):
                            if bit:
                                (row_e if helper == E else row_f).add(z)
                        maximal_rows.append((sorted(row_e), sorted(row_f)))
                print("  maximal bad rows", maximal_rows, flush=True)


if __name__ == "__main__":
    main()
