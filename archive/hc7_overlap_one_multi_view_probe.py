#!/usr/bin/env python3
"""Probe whether several adverse eight-terminal views close abstractly.

This is a discovery experiment, not a proof.  It imports the exact
overlap-one obstruction and, for each stabilizer orbit of four reserves,
selects the first adverse order-eight carrier used by the audited barrier.
It then asks whether unions of two such terminal-edge views already force
``K_7`` on the twelve-object quotient.

Even a positive answer would still require a simultaneous rooted-carrier
uncrossing theorem: rooted models obtained from different deletions may
overlap outside their terminals, so their terminal-edge masks cannot simply
be united in the host graph.
"""

from __future__ import annotations

import collections
import hashlib
import itertools

import hc7_overlap_one_order_six_full_orbit_closure as base


def main() -> None:
    state = base.minimal_orbits()[0][0]
    carriers = tuple(
        sorted(
            base.order_eight_carriers(),
            key=lambda mask: (mask.bit_count(), mask),
        )
    )
    stabilizer = base.state_stabilizer(state)
    reserve_orbits = base.subset_orbits(stabilizer, range(base.N), 4)
    detector = base.ExactK7()

    records = []
    for reserve, weight in reserve_orbits:
        bad = base.first_bad_order_eight(state, reserve, carriers, detector)
        assert bad is not None
        carrier_index, abstract_carrier, lifted_carrier = bad
        records.append(
            (reserve, weight, carrier_index, abstract_carrier, lifted_carrier)
        )

    pair_profile = collections.Counter()
    pair_by_reserve_intersection = collections.Counter()
    open_pairs = []
    first_closed = None
    for left, right in itertools.combinations(range(len(records)), 2):
        graph = state | records[left][4] | records[right][4]
        closed = detector(graph)
        pair_profile[closed] += records[left][1] * records[right][1]
        pair_by_reserve_intersection[
            (len(set(records[left][0]) & set(records[right][0])), closed)
        ] += 1
        if closed and first_closed is None:
            first_closed = (left, right, graph)
        if not closed:
            open_pairs.append((left, right, graph))

    triple_profile = collections.Counter()
    first_open_triple = None
    for left, right, graph in open_pairs:
        for third in range(right + 1, len(records)):
            closed = detector(graph | records[third][4])
            triple_profile[closed] += 1
            if not closed and first_open_triple is None:
                first_open_triple = (left, right, third)

    digest = hashlib.sha256(
        "\n".join(
            f"{','.join(map(str, reserve))}:{weight}:{index}:{abstract}:{lifted}"
            for reserve, weight, index, abstract, lifted in records
        ).encode()
    ).hexdigest()

    print("reserve_orbits", len(records))
    print("record_digest", digest)
    print("pair_orbit_count", len(records) * (len(records) - 1) // 2)
    print("pair_profile", dict(sorted(pair_profile.items())))
    print(
        "pair_by_reserve_intersection",
        dict(sorted(pair_by_reserve_intersection.items())),
    )
    print("open_pair_orbits", len(open_pairs))
    print("first_closed_pair", first_closed)
    print("tested_extensions_of_open_pairs", sum(triple_profile.values()))
    print("triple_extension_profile", dict(sorted(triple_profile.items())))
    print("first_open_triple", first_open_triple)


if __name__ == "__main__":
    main()
