#!/usr/bin/env python3
"""Probe three six-vertex K5 supports over one common five-set.

The supports are U+a, U+p, U+q on eight labelled vertices.  For each
support we enumerate a normalized spanning K5 model (one edge bag and four
singleton bags) and retain only the edges required by that model.  The
script looks for minimal unions with no K7 minor.  It is a falsifier for a
purely local replacement-composition claim, not an HC7 certificate.
"""

from itertools import combinations, product


U = tuple(range(5))
A, P, Q = 5, 6, 7
N = 8
ALL = tuple(combinations(range(N), 2))
EDGE_BIT = {e: 1 << i for i, e in enumerate(ALL)}


def edge(u, v):
    return (u, v) if u < v else (v, u)


def bits(edges):
    value = 0
    for e in edges:
        value |= EDGE_BIT[e]
    return value


def patterns(support, restricted_pairs=None):
    support = tuple(support)
    pairs = tuple(combinations(support, 2))
    if restricted_pairs is not None:
        pairs = tuple(restricted_pairs)
    for x, y in pairs:
        core = tuple(v for v in support if v not in (x, y))
        base = {edge(x, y)}
        base.update(edge(r, s) for r, s in combinations(core, 2))
        for bits in product((0, 1), repeat=4):
            req = set(base)
            for r, bit in zip(core, bits):
                req.add(edge((x, y)[bit], r))
            yield bits_of_req(req), (edge(x, y), bits)


def bits_of_req(required):
    return bits(required)


DELETE_CLIQUES = tuple(
    bits(combinations(tuple(v for v in range(N) if v != omitted), 2))
    for omitted in range(N)
)
CONTRACTION_TESTS = []
for x, y in ALL:
    rest = tuple(v for v in range(N) if v not in (x, y))
    CONTRACTION_TESTS.append(
        (
            EDGE_BIT[(x, y)],
            bits(combinations(rest, 2)),
            tuple(EDGE_BIT[edge(x, r)] | EDGE_BIT[edge(y, r)] for r in rest),
        )
    )


def has_k7_minor(mask):
    # A K7 model on an eight-vertex host either deletes one vertex or
    # contracts exactly one edge.
    for clique_mask in DELETE_CLIQUES:
        if mask & clique_mask == clique_mask:
            return True
    for edge_bit, rest_clique, contact_pairs in CONTRACTION_TESTS:
        if (
            mask & edge_bit
            and mask & rest_clique == rest_clique
            and all(mask & pair for pair in contact_pairs)
        ):
            return True
    return False


def has_literal_k5(mask, support):
    for five in combinations(support, 5):
        required = bits(combinations(five, 2))
        if mask & required == required:
            return True
    return False


def main():
    supports = (U + (A,), U + (P,), U + (Q,))
    # Up to permutations of U, the first split pair either contains A or
    # lies inside U.  Endpoint order is absorbed by the duty bits.
    first_pairs = ((A, 0), (0, 1))
    first = tuple(patterns(supports[0], first_pairs))
    second = tuple(patterns(supports[1]))
    third = tuple(patterns(supports[2]))

    survivor_graphs = set()
    minimum = None
    fixed_x = (0, 1, 2, A)
    outside_x = (3, 4)
    literal_arm_edges = bits(combinations(fixed_x + (P,), 2)) | bits(
        combinations(fixed_x + (Q,), 2)
    )
    literal_arm_survivors = set()
    carrier_failures = set()
    tested = 0
    for req_a, tag_a in first:
        for req_p, tag_p in second:
            partial = req_a | req_p
            for req_q, tag_q in third:
                tested += 1
                mask = partial | req_q
                if any(has_literal_k5(mask, support) for support in supports):
                    continue
                if has_k7_minor(mask):
                    continue
                survivor_graphs.add(mask)
                edge_list = tuple(e for e in ALL if mask & EDGE_BIT[e])
                candidate = (mask.bit_count(), edge_list, tag_a, tag_p, tag_q, mask)
                if minimum is None or candidate[:2] < minimum[:2]:
                    minimum = candidate

                armed = mask | literal_arm_edges
                if any(has_literal_k5(armed, support) for support in supports):
                    continue
                if has_k7_minor(armed):
                    continue
                literal_arm_survivors.add(armed)
                r, s = outside_x
                carrier_ok = bool(armed & EDGE_BIT[edge(r, s)])
                carrier_ok &= all(
                    armed & (EDGE_BIT[edge(r, x)] | EDGE_BIT[edge(s, x)])
                    for x in fixed_x
                )
                carrier_ok &= bool(
                    armed & (EDGE_BIT[edge(P, r)] | EDGE_BIT[edge(P, s)])
                )
                carrier_ok &= bool(
                    armed & (EDGE_BIT[edge(Q, r)] | EDGE_BIT[edge(Q, s)])
                )
                if not carrier_ok:
                    carrier_failures.add(armed)

    print(f"tested={tested} distinct_k7_free_graphs={len(survivor_graphs)}")
    print(
        "fixed_literal_arm_survivors="
        f"{len(literal_arm_survivors)} carrier_failures={len(carrier_failures)}"
    )
    if minimum is not None:
        size, edge_list, tag_a, tag_p, tag_q, mask = minimum
        print(f"minimum_edges={size}")
        print(f"patterns={tag_a},{tag_p},{tag_q}")
        print("edges=" + " ".join(f"{x}{y}" for x, y in edge_list))

        local = U + (A,)
        found = None
        for x_size in (4, 5):
            for x_set in combinations(local, x_size):
                if A not in x_set:
                    continue
                b_support = tuple(x_set) + (P,)
                c_support = tuple(x_set) + (Q,)
                if x_size == 4:
                    b_patterns = ((bits(combinations(b_support, 2)), ("literal",)),)
                    c_patterns = ((bits(combinations(c_support, 2)), ("literal",)),)
                else:
                    b_patterns = tuple(patterns(b_support))
                    c_patterns = tuple(patterns(c_support))
                six_supports = list(supports)
                if len(b_support) == 6:
                    six_supports.extend((b_support, c_support))
                for req_b, tag_b in b_patterns:
                    for req_c, tag_c in c_patterns:
                        completed = mask | req_b | req_c
                        if any(
                            has_literal_k5(completed, support)
                            for support in six_supports
                        ):
                            continue
                        if has_k7_minor(completed):
                            continue
                        found = (x_set, tag_b, tag_c, completed)
                        break
                    if found:
                        break
                if found:
                    break
            if found:
                break
        if found:
            x_set, tag_b, tag_c, completed = found
            completed_edges = tuple(e for e in ALL if completed & EDGE_BIT[e])
            print(f"rigid_arm_local_survivor_X={x_set}")
            print(f"arm_patterns={tag_b},{tag_c}")
            print(
                "completed_edges="
                + " ".join(f"{x}{y}" for x, y in completed_edges)
            )
        else:
            print("minimum survivor has no X-subset rigid-arm completion")


if __name__ == "__main__":
    main()
