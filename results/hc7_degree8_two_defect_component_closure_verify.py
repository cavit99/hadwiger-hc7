#!/usr/bin/env python3
"""Verify the degree-eight two-defect four-bag anchor allocation.

Run from the repository root with nauty's ``geng`` on PATH:

    geng -q 8 | python3 results/hc7_degree8_two_defect_component_closure_verify.py
"""

from __future__ import annotations

import hashlib
from itertools import combinations, permutations, product

from hc7_degree8_nonedge_bipartition_classification_verify import (
    aligned_nonedges,
    catalogue_lines,
    has_independent_four,
    is_k1_join_c7,
)
from hc7_order8_three_component_boundary_verify import (
    decode_g6,
    encode_g6,
    has_compact_k4,
)


ORDER = 8
S = tuple(range(ORDER))
I = (0, 1, 2)
T = (3, 4, 5)


def independent(adjacency: tuple[int, ...], vertices: tuple[int, ...]) -> bool:
    return all(
        not ((adjacency[left] >> right) & 1)
        for left, right in combinations(vertices, 2)
    )


def aligned_partitions(
    adjacency: tuple[int, ...], p: int, q: int
) -> list[tuple[tuple[int, ...], tuple[int, ...]]]:
    remainder = tuple(vertex for vertex in S if vertex not in {p, q})
    answer = []
    for first in combinations(remainder, 3):
        second = tuple(vertex for vertex in remainder if vertex not in first)
        if first > second:
            continue
        if independent(adjacency, first) and independent(adjacency, second):
            answer.append((first, second))
    return answer


def relabel_boundary(
    adjacency: tuple[int, ...],
    first: tuple[int, ...],
    second: tuple[int, ...],
    p: int,
    q: int,
) -> tuple[int, ...]:
    old_vertices = first + second + (p, q)
    old_to_new = {old: new for new, old in enumerate(old_vertices)}
    rows = [0] * ORDER
    for old_left, old_right in combinations(old_vertices, 2):
        if not ((adjacency[old_left] >> old_right) & 1):
            continue
        left = old_to_new[old_left]
        right = old_to_new[old_right]
        rows[left] |= 1 << right
        rows[right] |= 1 << left
    return tuple(rows)


def edge(adjacency: tuple[int, ...], left: int, right: int) -> bool:
    return bool((adjacency[left] >> right) & 1)


def bags_adjacent(
    adjacency: tuple[int, ...],
    left_missed: frozenset[int],
    left_anchor: int,
    right_missed: frozenset[int],
    right_anchor: int,
) -> bool:
    return (
        right_anchor not in left_missed
        or left_anchor not in right_missed
        or edge(adjacency, left_anchor, right_anchor)
    )


def bag_sees_singleton(
    adjacency: tuple[int, ...],
    missed: frozenset[int],
    anchor: int,
    singleton: int,
) -> bool:
    return singleton not in missed or edge(adjacency, anchor, singleton)


def first_certificate(
    adjacency: tuple[int, ...],
    missed_e: frozenset[int],
    missed_f: frozenset[int],
) -> tuple[tuple[int, ...], tuple[int, int]] | None:
    missed = (missed_e, missed_e, missed_f, missed_f)
    for anchors in permutations(S, 4):
        if any(anchors[index] in missed[index] for index in range(4)):
            continue
        if any(
            not bags_adjacent(
                adjacency,
                missed[left],
                anchors[left],
                missed[right],
                anchors[right],
            )
            for left in range(2)
            for right in range(2, 4)
        ):
            continue

        unused = tuple(vertex for vertex in S if vertex not in anchors)
        for first, second in combinations(unused, 2):
            if not edge(adjacency, first, second):
                continue
            if all(
                bag_sees_singleton(
                    adjacency, missed[index], anchors[index], first
                )
                and bag_sees_singleton(
                    adjacency, missed[index], anchors[index], second
                )
                for index in range(4)
            ):
                return anchors, (first, second)
    return None


def main() -> None:
    total = 0
    compact = 0
    nonwheel = 0
    aligned_instances = 0
    tested_orientations = 0
    certificates: list[str] = []
    failures: list[str] = []
    missed_pairs = tuple(
        frozenset((left, right)) for left, right in product(I, T)
    )

    for line in catalogue_lines():
        adjacency = decode_g6(line)
        if not adjacency:
            continue
        total += 1
        if has_independent_four(adjacency) or has_compact_k4(adjacency):
            continue
        compact += 1
        if is_k1_join_c7(adjacency):
            continue
        nonwheel += 1
        source_code = encode_g6(adjacency)

        for p, q in aligned_nonedges(adjacency):
            for first, second in aligned_partitions(adjacency, p, q):
                aligned_instances += 1
                boundary = relabel_boundary(adjacency, first, second, p, q)
                for missed_e, missed_f in product(missed_pairs, repeat=2):
                    tested_orientations += 1
                    found = first_certificate(boundary, missed_e, missed_f)
                    prefix = (
                        f"{source_code}|{p},{q}|{first}|{second}|"
                        f"{tuple(sorted(missed_e))}|{tuple(sorted(missed_f))}"
                    )
                    if found is None:
                        failures.append(prefix)
                    else:
                        certificates.append(f"{prefix}|{found[0]}|{found[1]}")

    assert total == 12_346
    assert compact == 185
    assert nonwheel == 184
    assert aligned_instances == 1_207
    assert tested_orientations == 97_767
    assert len(certificates) == tested_orientations
    assert not failures

    certificate_text = "\n".join(certificates) + "\n"
    certificate_digest = hashlib.sha256(certificate_text.encode()).hexdigest()

    print(f"order8_graphs {total}")
    print(f"compact_boundaries {compact}")
    print(f"nonwheel_compact_boundaries {nonwheel}")
    print(f"aligned_labelled_instances {aligned_instances}")
    print(f"tested_missed_pair_orientations {tested_orientations}")
    print(f"anchor_certificates {len(certificates)}")
    print(f"anchor_certificate_sha256 {certificate_digest}")
    print(f"failures {len(failures)}")
    print("PASS degree8_two_defect_component_closure")


if __name__ == "__main__":
    main()
