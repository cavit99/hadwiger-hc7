"""Reproduce the full |C|=6 balanced-helper certificate.

This is a finite, computer-assisted certificate for the following statement.

* C is a connected graph on six vertices.
* Three A-vertices have at least four neighbours each in C.
* Four B-vertices have at least three neighbours each in C.
* Every x in C has d_C(x)+d_A(x)+d_B(x) >= 7.

Then C has a balanced partition P,Q into triples and distinct A-roots ai,aj
such that P+ai and Q+aj are connected and both P,Q meet every B-neighbourhood.

The checker uses only the Python standard library.  It constructs all 112
unlabelled connected graphs on six vertices (rather than trusting an external
atlas), then checks all C(22+3-1,3)=2024 multisets of three A-neighbourhoods
of sizes 4, 5, or 6 for each graph.

Why B need not be enumerated
----------------------------
There are ten balanced partitions.  Call one A-compatible when its two sides
can be attached to distinct A-roots.  A B-neighbourhood of size at least three
can fail to meet one side of a 3+3 partition only when it is *exactly* the
opposite triple.  Thus one B-vertex forbids at most one partition.  If there
are at least five A-compatible partitions, four B-vertices cannot forbid all.

If q <= 4 compatible partitions remain and no helper exists, q distinct
B-vertices must have exact three-neighbourhoods, one orienting each partition.
To maximize every C-vertex's possible B-degree, make each of the remaining
4-q B-vertices complete to C.  The checker tries all at most 2^q orientations.
If even this coordinatewise maximal relaxation leaves some x with total degree
below seven, no genuine choice of the four B-neighbourhoods is feasible.

The output asserts that this happens in every low-compatible state.  Hence the
zero surviving states are exactly the model-to-helper conclusion above.
"""

from collections import Counter
from itertools import combinations, combinations_with_replacement, permutations


N = 6
FULL = (1 << N) - 1
VERTICES = tuple(range(N))
EDGES = tuple(combinations(VERTICES, 2))
EDGE_INDEX = {edge: i for i, edge in enumerate(EDGES)}
A_ROWS = tuple(mask for mask in range(1 << N) if mask.bit_count() >= 4)
PARTITIONS = tuple(
    (1 | sum(1 << x for x in tail), FULL ^ (1 | sum(1 << x for x in tail)))
    for tail in combinations(range(1, N), 2)
)

EXPECTED_SUMMARY = {
    (5, 4, -3): 2,
    (5, 4, -2): 2,
    (6, 2, -1): 4,
    (6, 4, -3): 4,
    (6, 4, -2): 19,
    (7, 2, -1): 2,
    (7, 4, -2): 22,
    (8, 4, -2): 7,
    (9, 4, -2): 1,
}


def adjacency(edge_mask: int) -> tuple[int, ...]:
    """Return the six adjacency bitmasks of a labelled graph."""
    ans = [0] * N
    for i, (u, v) in enumerate(EDGES):
        if edge_mask >> i & 1:
            ans[u] |= 1 << v
            ans[v] |= 1 << u
    return tuple(ans)


def connected(edge_mask: int) -> bool:
    """Test connectivity by bitset breadth-first search."""
    adj = adjacency(edge_mask)
    seen = 1
    while True:
        reached = seen
        for x in VERTICES:
            if seen >> x & 1:
                reached |= adj[x]
        if reached == seen:
            return seen == FULL
        seen = reached


def permutation_maps() -> tuple[tuple[int, ...], ...]:
    """For every vertex permutation, map each input edge bit to its output bit."""
    maps = []
    for permutation in permutations(VERTICES):
        output_bits = []
        for u, v in EDGES:
            image = tuple(sorted((permutation[u], permutation[v])))
            output_bits.append(1 << EDGE_INDEX[image])
        maps.append(tuple(output_bits))
    return tuple(maps)


def relabel(edge_mask: int, output_bits: tuple[int, ...]) -> int:
    ans = 0
    for i, output_bit in enumerate(output_bits):
        if edge_mask >> i & 1:
            ans |= output_bit
    return ans


def connected_unlabelled_graphs() -> tuple[int, ...]:
    """Construct one representative of each connected six-vertex graph orbit."""
    unseen = {mask for mask in range(1 << len(EDGES)) if connected(mask)}
    assert len(unseen) == 26704  # known labelled count, also checked directly here
    maps = permutation_maps()
    representatives = []
    while unseen:
        representative = min(unseen)
        representatives.append(representative)
        orbit = {relabel(representative, mapping) for mapping in maps}
        unseen.difference_update(orbit)
    assert len(representatives) == 112
    return tuple(representatives)


def components(side: int, adj: tuple[int, ...]) -> tuple[int, ...]:
    """Return the component masks of the graph induced by ``side``."""
    remaining = side
    answer = []
    while remaining:
        seed = remaining & -remaining
        seen = seed
        while True:
            reached = seen
            for x in VERTICES:
                if seen >> x & 1:
                    reached |= adj[x] & side
            if reached == seen:
                break
            seen = reached
        answer.append(seen)
        remaining &= ~seen
    return tuple(answer)


def root_set(component_masks: tuple[int, ...], a_rows: tuple[int, int, int]) -> int:
    """Bit i is set exactly when side + a_i is connected."""
    answer = 0
    for i, row in enumerate(a_rows):
        if all(row & component for component in component_masks):
            answer |= 1 << i
    return answer


def compatible_partitions(
    partition_components: tuple[tuple[tuple[int, ...], tuple[int, ...]], ...],
    a_rows: tuple[int, int, int],
) -> tuple[tuple[int, int], ...]:
    """List partitions whose two root lists have distinct representatives."""
    answer = []
    for (left, right), (left_components, right_components) in zip(
        PARTITIONS, partition_components, strict=True
    ):
        left_roots = root_set(left_components, a_rows)
        right_roots = root_set(right_components, a_rows)
        if left_roots and right_roots and (left_roots | right_roots).bit_count() >= 2:
            answer.append((left, right))
    return tuple(answer)


def main() -> None:
    graphs = connected_unlabelled_graphs()
    summary: Counter[tuple[int, int, int]] = Counter()
    a_multisets_tested = 0
    degree_possible_states = 0
    low_compatible_states = 0
    feasible_states = []

    for edge_mask in graphs:
        adj = adjacency(edge_mask)
        c_degree = tuple(neighbours.bit_count() for neighbours in adj)
        partition_components = tuple(
            (components(left, adj), components(right, adj))
            for left, right in PARTITIONS
        )

        for indices in combinations_with_replacement(range(len(A_ROWS)), 3):
            a_multisets_tested += 1
            a_rows = tuple(A_ROWS[i] for i in indices)
            a_degree = tuple(sum(row >> x & 1 for row in a_rows) for x in VERTICES)

            # Even four B-vertices complete to C cannot repair this state.
            if any(c_degree[x] + a_degree[x] + 4 < 7 for x in VERTICES):
                continue
            degree_possible_states += 1

            compatible = compatible_partitions(partition_components, a_rows)
            q = len(compatible)
            if q >= 5:
                continue
            low_compatible_states += 1

            best_minimum_slack = -100
            for orientation in range(1 << q):
                exact_b_rows = tuple(
                    partition[orientation >> i & 1]
                    for i, partition in enumerate(compatible)
                )
                b_degree = tuple(
                    (4 - q) + sum(row >> x & 1 for row in exact_b_rows)
                    for x in VERTICES
                )
                minimum_slack = min(
                    c_degree[x] + a_degree[x] + b_degree[x] - 7
                    for x in VERTICES
                )
                best_minimum_slack = max(best_minimum_slack, minimum_slack)

            summary[(edge_mask.bit_count(), q, best_minimum_slack)] += 1
            if best_minimum_slack >= 0:
                feasible_states.append((edge_mask, a_rows, compatible))

    assert len(graphs) == 112
    assert len(A_ROWS) == 22
    assert a_multisets_tested == 112 * 2024 == 226688
    assert degree_possible_states == 186354
    assert low_compatible_states == 63
    assert dict(summary) == EXPECTED_SUMMARY
    assert feasible_states == []

    print("connected unlabelled C graphs:", len(graphs))
    print("A-neighbourhood multisets per graph: 2024")
    print("degree-possible C/A states:", degree_possible_states)
    print("states with at most four A-compatible partitions:", low_compatible_states)
    for key, count in sorted(summary.items()):
        print(f"  (e(C), q, best minimum degree slack)={key}: {count}")
    print("degree-feasible no-helper states:", len(feasible_states))
    print("certificate verified")


if __name__ == "__main__":
    main()
