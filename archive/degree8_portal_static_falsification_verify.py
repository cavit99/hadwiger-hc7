#!/usr/bin/env python3
"""Verify the explicit obstruction to a coarse static portal dichotomy."""

from itertools import combinations

from degree8_cutvertex_exact_transfer_probe import (
    PARTITIONS, exact_state, find_model, full_adjacency, independent,
    MISS_TYPES,
)


MISS_TYPE = MISS_TYPES[0]  # branch defects 01,01; D defect 0
EDGES = [
    # K3 on 0,1,7 and C5 2-4-5-3-6-2.
    (0, 1), (0, 7), (1, 7),
    (2, 4), (4, 5), (3, 5), (3, 6), (2, 6),
    # The only z--N edge.
    (2, 8),
]


def main():
    n_edges = {tuple(sorted(edge)) for edge in EDGES if edge[1] < 8}
    assert all(any(tuple(sorted(edge)) in n_edges
                   for edge in combinations(four, 2))
               for four in combinations(range(8), 4))

    # Exhaustive quotient-model search: 462 choices of six nonempty
    # boundary traces and 7^4 placements/omissions of z,R1,R2,D.
    assert find_model(EDGES, MISS_TYPE) is None

    # Exhaustive exact-state search over every partition of X=N+z into at
    # most six blocks, with at most five blocks meeting N.
    adj = full_adjacency(EDGES, MISS_TYPE)
    independent_count = sum(independent(partition, adj)
                            for partition in PARTITIONS)
    assert len(PARTITIONS) == 19052
    assert independent_count == 2355
    assert exact_state(EDGES, MISS_TYPE) is None

    print("alpha(N)<=3 verified")
    print("no N-meeting K6 portal-quotient model")
    print("static exact states checked:", len(PARTITIONS),
          "candidate partitions;", independent_count, "independent")
    print("no common complementary realization for R1,R2,D")


if __name__ == "__main__":
    main()
