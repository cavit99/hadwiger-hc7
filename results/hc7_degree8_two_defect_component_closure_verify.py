#!/usr/bin/env python3
"""Verify the degree-eight at-most-two-defect four-bag allocation.

Run from the repository root with nauty's ``geng`` on PATH:

    geng -q 8 | python3 results/hc7_degree8_two_defect_component_closure_verify.py
"""

from __future__ import annotations

import hashlib
from itertools import combinations, product

from hc7_degree8_nonedge_bipartition_classification_verify import (
    catalogue_lines,
    has_independent_four,
)
from hc7_order8_three_component_boundary_verify import (
    decode_g6,
    encode_g6,
    has_compact_k4,
)


ORDER = 8
S = tuple(range(ORDER))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


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


def first_canonical_certificate(
    adjacency: tuple[int, ...],
    missed_left: frozenset[int],
    missed_right: frozenset[int],
) -> tuple[tuple[int, ...], tuple[int, int]] | None:
    """Return one certificate for a canonically ordered missed-set pair."""

    for first, second in combinations(S, 2):
        if not edge(adjacency, first, second):
            continue

        available = tuple(
            vertex for vertex in S if vertex not in {first, second}
        )
        eligible_left = tuple(
            anchor
            for anchor in available
            if anchor not in missed_left
            and (
                first not in missed_left
                or edge(adjacency, anchor, first)
            )
            and (
                second not in missed_left
                or edge(adjacency, anchor, second)
            )
        )
        eligible_right = tuple(
            anchor
            for anchor in available
            if anchor not in missed_right
            and (
                first not in missed_right
                or edge(adjacency, anchor, first)
            )
            and (
                second not in missed_right
                or edge(adjacency, anchor, second)
            )
        )

        for left_anchors in combinations(eligible_left, 2):
            for right_anchors in combinations(eligible_right, 2):
                anchors = left_anchors + right_anchors
                if len(set(anchors)) < 4:
                    continue
                if all(
                    bags_adjacent(
                        adjacency,
                        missed_left,
                        left_anchor,
                        missed_right,
                        right_anchor,
                    )
                    for left_anchor in left_anchors
                    for right_anchor in right_anchors
                ):
                    return anchors, (first, second)
    return None


def valid_certificate(
    adjacency: tuple[int, ...],
    missed_e: frozenset[int],
    missed_f: frozenset[int],
    certificate: tuple[tuple[int, ...], tuple[int, int]],
) -> bool:
    anchors, singletons = certificate
    first, second = singletons
    missed = (missed_e, missed_e, missed_f, missed_f)
    return (
        len(anchors) == 4
        and len(set(anchors + singletons)) == 6
        and all(anchors[index] not in missed[index] for index in range(4))
        and edge(adjacency, first, second)
        and all(
            bags_adjacent(
                adjacency,
                missed[left],
                anchors[left],
                missed[right],
                anchors[right],
            )
            for left in range(2)
            for right in range(2, 4)
        )
        and all(
            bag_sees_singleton(
                adjacency, missed[index], anchors[index], singleton
            )
            for index in range(4)
            for singleton in singletons
        )
    )


def sorted_vertices(vertices: frozenset[int]) -> tuple[int, ...]:
    return tuple(sorted(vertices))


def main() -> None:
    total = 0
    compact = 0
    tested_orientations = 0
    certificate_count = 0
    certificate_digest = hashlib.sha256()
    failures: list[str] = []
    missed_sets = tuple(
        frozenset(vertices)
        for size in range(3)
        for vertices in combinations(S, size)
    )

    for line in catalogue_lines():
        adjacency = decode_g6(line)
        if not adjacency:
            continue
        total += 1
        if has_independent_four(adjacency) or has_compact_k4(adjacency):
            continue
        compact += 1
        source_code = encode_g6(adjacency)
        instance_cache: dict[
            tuple[frozenset[int], frozenset[int]],
            tuple[tuple[int, ...], tuple[int, int]] | None,
        ] = {}

        for missed_e, missed_f in product(missed_sets, repeat=2):
            tested_orientations += 1
            key_e = sorted_vertices(missed_e)
            key_f = sorted_vertices(missed_f)
            if key_e <= key_f:
                cache_key = (missed_e, missed_f)
                swapped = False
            else:
                cache_key = (missed_f, missed_e)
                swapped = True

            if cache_key not in instance_cache:
                instance_cache[cache_key] = first_canonical_certificate(
                    adjacency, *cache_key
                )
            found = instance_cache[cache_key]
            if found is not None and swapped:
                anchors, singletons = found
                found = (anchors[2:] + anchors[:2], singletons)

            prefix = f"{source_code}|{key_e}|{key_f}"
            if found is None:
                failures.append(prefix)
                continue
            require(
                valid_certificate(adjacency, missed_e, missed_f, found),
                f"invalid certificate for {prefix}: {found}",
            )
            certificate_count += 1
            certificate_digest.update(
                f"{prefix}|{found[0]}|{found[1]}\n".encode()
            )

    require(total == 12_346, f"expected 12346 order-eight graphs, got {total}")
    require(compact == 185, f"expected 185 compact boundaries, got {compact}")
    require(len(missed_sets) == 37, "incorrect missed-set catalogue")
    require(
        tested_orientations == 253_265,
        f"expected 253265 orientations, got {tested_orientations}",
    )
    require(
        certificate_count == tested_orientations,
        f"only {certificate_count} of {tested_orientations} cases certified",
    )
    if failures:
        raise RuntimeError(f"first failed orientation: {failures[0]}")

    print(f"order8_graphs {total}")
    print(f"compact_boundaries {compact}")
    print(f"missed_sets {len(missed_sets)}")
    print(f"tested_missed_set_orientations {tested_orientations}")
    print(f"anchor_certificates {certificate_count}")
    print(f"anchor_certificate_sha256 {certificate_digest.hexdigest()}")
    print(f"failures {len(failures)}")
    print("PASS degree8_two_defect_component_closure")


if __name__ == "__main__":
    main()
