#!/usr/bin/env python3
"""Verify all root placements on the retained 16-vertex PB barrier.

This is computer-assisted finite evidence, not an unbounded theorem.  There
are 288 ways to choose one root from each of the seven fixed columns and
therefore 82,944 ordered choices of ``(A,B)``, with equality allowed inside a
column.  For every placement this script constructs and checks a literal
instance of the audited three-column chained-absorption theorem, hence a
paired-rooted ``K_5`` minor model.

The implementation is dependency-free.  Vertices, columns, pieces and branch
sets are represented by integer bit masks.  It independently enumerates all
20 oriented pentagonal-bipyramid frames and every admissible choice of the
six nonempty, within-column-disjoint pieces in the theorem.

For reproducibility, a placement's canonical chain certificate minimizes
``(number of supported vertices, sorted branch-set masks)`` within the full
98-certificate catalogue.  This is not a claim of global minimality among
all possible ``K_5`` minor models.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from hashlib import sha256
from itertools import combinations, product


BASE_CROSS = (
    (1, 0, 2, 1), (0, 0, 4, 0), (0, 0, 4, 1), (0, 1, 4, 0),
    (0, 1, 4, 1), (3, 1, 4, 0), (1, 0, 5, 0), (0, 0, 3, 1),
    (1, 1, 4, 0), (1, 1, 4, 1), (0, 0, 6, 0), (2, 0, 3, 0),
    (2, 0, 3, 1), (2, 1, 3, 0), (0, 0, 2, 0), (4, 1, 5, 0),
    (2, 0, 6, 0), (2, 1, 6, 0), (2, 1, 6, 1), (5, 0, 6, 1),
    (5, 1, 6, 0), (5, 1, 6, 1), (0, 0, 5, 1), (0, 1, 5, 0),
    (0, 1, 5, 1), (1, 0, 6, 1), (1, 0, 3, 0), (1, 0, 3, 1),
    (1, 1, 3, 0), (1, 1, 3, 1),
)

COLUMNS = (
    (0, 1), (2, 3, 14), (4, 5), (6, 7, 15),
    (8, 9), (10, 11), (12, 13),
)
RIM = (2, 3, 4, 5, 6)
ORDER = 16

EDGES = {frozenset((2 * column, 2 * column + 1)) for column in range(7)}
EDGES.update(
    frozenset((2 * left + i, 2 * right + j))
    for left, i, right, j in BASE_CROSS
)
EDGES.update(frozenset((14, vertex)) for vertex in (2, 3, 6, 7, 8))
EDGES.update(frozenset((15, vertex)) for vertex in (2, 3, 5, 6, 14))

ADJACENCY = tuple(
    sum(
        1 << other
        for other in range(ORDER)
        if other != vertex and frozenset((vertex, other)) in EDGES
    )
    for vertex in range(ORDER)
)
COLUMN_MASKS = tuple(sum(1 << vertex for vertex in column) for column in COLUMNS)

NEIGHBOURS = [0] * (1 << ORDER)
for _mask in range(1, 1 << ORDER):
    _bit = _mask & -_mask
    NEIGHBOURS[_mask] = (
        NEIGHBOURS[_mask ^ _bit] | ADJACENCY[_bit.bit_length() - 1]
    )


def connected(mask: int) -> bool:
    if not mask:
        return False
    reached = mask & -mask
    frontier = reached
    while frontier:
        bit = frontier & -frontier
        frontier ^= bit
        new = ADJACENCY[bit.bit_length() - 1] & mask & ~reached
        reached |= new
        frontier |= new
    return reached == mask


def touches(left: int, right: int) -> bool:
    return bool(NEIGHBOURS[left] & right)


def valid_model(bags: tuple[int, ...]) -> bool:
    return (
        len(bags) == 5
        and all(connected(bag) for bag in bags)
        and not any(bags[i] & bags[j] for i, j in combinations(range(5), 2))
        and all(touches(bags[i], bags[j]) for i, j in combinations(range(5), 2))
    )


def ordered_disjoint_nonempty_pieces(column: int):
    """Yield all ordered nonempty disjoint pairs of subsets of ``column``."""
    first = column
    while first:
        available = column ^ first
        second = available
        while second:
            yield first, second
            second = (second - 1) & available
        first = (first - 1) & column


@dataclass(frozen=True)
class ChainCertificate:
    """One literal instance of the chained-absorption theorem."""

    whole_pole: int
    supplier_pole: int
    rim: tuple[int, int, int, int, int]
    pb: int
    qb: int
    p1: int
    q1: int
    q2: int
    z2: int

    @property
    def d1(self) -> int:
        return self.pb | self.p1

    @property
    def d2(self) -> int:
        return self.qb | self.q1 | self.q2

    @property
    def d3(self) -> int:
        return self.z2 | COLUMN_MASKS[self.rim[3]] | COLUMN_MASKS[self.rim[4]]

    @property
    def theorem_bags(self) -> tuple[int, ...]:
        return (
            COLUMN_MASKS[self.whole_pole],
            COLUMN_MASKS[self.rim[0]],
            self.d1,
            self.d2,
            self.d3,
        )

    @property
    def bags(self) -> tuple[int, ...]:
        return tuple(sorted(self.theorem_bags))

    @property
    def support(self) -> int:
        return sum(bag.bit_count() for bag in self.bags)

    def encoding(self) -> str:
        fields = (
            self.whole_pole, self.supplier_pole, *self.rim,
            self.pb, self.qb, self.p1, self.q1, self.q2, self.z2,
            *self.bags,
        )
        return ",".join(map(str, fields))


def audit_certificate(certificate: ChainCertificate) -> None:
    """Check every set-location, connectedness and adjacency hypothesis."""
    ca = COLUMN_MASKS[certificate.whole_pole]
    cb = COLUMN_MASKS[certificate.supplier_pole]
    ci, c1, c2, _, _ = map(COLUMN_MASKS.__getitem__, certificate.rim)

    assert {certificate.whole_pole, certificate.supplier_pole} == {0, 1}
    assert set(certificate.rim) == set(RIM)
    assert all(
        certificate.rim[(position + 1) % 5]
        in (RIM[(RIM.index(label) + 1) % 5], RIM[(RIM.index(label) - 1) % 5])
        for position, label in enumerate(certificate.rim)
    )

    pieces = (
        (certificate.pb, certificate.qb, cb),
        (certificate.p1, certificate.q1, c1),
        (certificate.q2, certificate.z2, c2),
    )
    for first, second, owner in pieces:
        assert first and second
        assert not (first & second)
        assert not ((first | second) & ~owner)

    d1, d2, d3 = certificate.d1, certificate.d2, certificate.d3
    assert all(connected(bag) for bag in (d1, d2, d3))
    required_contacts = (
        (ca, d1), (ca, d2), (ci, d1), (ci, d2),
        (d1, d2), (d1, d3), (d2, d3),
    )
    assert all(touches(left, right) for left, right in required_contacts)
    assert valid_model(certificate.theorem_bags)


def enumerate_chain_certificates() -> tuple[ChainCertificate, ...]:
    certificates = []
    for whole_pole, supplier_pole in ((0, 1), (1, 0)):
        for start in range(5):
            for direction in (1, -1):
                rim = tuple(
                    RIM[(start + direction * offset) % 5]
                    for offset in range(5)
                )
                for pb, qb in ordered_disjoint_nonempty_pieces(
                    COLUMN_MASKS[supplier_pole]
                ):
                    for p1, q1 in ordered_disjoint_nonempty_pieces(
                        COLUMN_MASKS[rim[1]]
                    ):
                        for q2, z2 in ordered_disjoint_nonempty_pieces(
                            COLUMN_MASKS[rim[2]]
                        ):
                            certificate = ChainCertificate(
                                whole_pole, supplier_pole, rim,
                                pb, qb, p1, q1, q2, z2,
                            )
                            d1, d2, d3 = (
                                certificate.d1,
                                certificate.d2,
                                certificate.d3,
                            )
                            if not all(connected(bag) for bag in (d1, d2, d3)):
                                continue
                            ca = COLUMN_MASKS[whole_pole]
                            ci = COLUMN_MASKS[rim[0]]
                            if not all(
                                touches(left, right)
                                for left, right in (
                                    (ca, d1), (ca, d2), (ci, d1), (ci, d2),
                                    (d1, d2), (d1, d3), (d2, d3),
                                )
                            ):
                                continue
                            audit_certificate(certificate)
                            certificates.append(certificate)

    # Each certificate happens to produce a distinct normalized model here.
    assert len({certificate.bags for certificate in certificates}) == len(certificates)
    return tuple(certificates)


ROOT_TUPLES = tuple(product(*COLUMNS))
ROOT_MASKS = tuple(sum(1 << vertex for vertex in roots) for roots in ROOT_TUPLES)
ROOT_COUNT = len(ROOT_MASKS)


def root_choice_mask(bags: tuple[int, ...]) -> int:
    """Return the 288-bit set of one-per-column root choices hitting all bags."""
    result = 0
    for index, roots in enumerate(ROOT_MASKS):
        if all(bag & roots for bag in bags):
            result |= 1 << index
    return result


def counter_text(counter: Counter[int]) -> str:
    return ",".join(f"{key}:{counter[key]}" for key in sorted(counter))


def main() -> int:
    assert len(EDGES) == 47
    assert ROOT_COUNT == 288
    assert len(set(ROOT_MASKS)) == ROOT_COUNT
    assert set().union(*map(set, COLUMNS)) == set(range(ORDER))
    assert sum(map(len, COLUMNS)) == ORDER
    assert all(connected(column) for column in COLUMN_MASKS)

    expected_contacts = {
        frozenset((pole, rim)) for pole in (0, 1) for rim in RIM
    } | {
        frozenset((RIM[index], RIM[(index + 1) % 5]))
        for index in range(5)
    }
    actual_contacts = {
        frozenset((left, right))
        for left, right in combinations(range(7), 2)
        if touches(COLUMN_MASKS[left], COLUMN_MASKS[right])
    }
    assert actual_contacts == expected_contacts

    certificates = enumerate_chain_certificates()
    assert len(certificates) == 98
    displayed_model = tuple(
        sorted(
            sum(1 << vertex for vertex in bag)
            for bag in (
                (0, 1), (4, 5), (2, 7), (3, 8, 15),
                (9, 10, 11, 12, 13),
            )
        )
    )
    assert displayed_model in {certificate.bags for certificate in certificates}

    compact_models = tuple(
        tuple(
            sorted(sum(1 << vertex for vertex in bag) for bag in model)
        )
        for model in (
            ((0, 1), (4, 5), (3, 6, 8, 9), (10, 11, 12),
             (2, 7, 13, 14, 15)),
            ((0, 1), (4, 5), (3, 7, 9, 10, 11), (12, 13),
             (2, 6, 8, 14, 15)),
            ((0, 1), (4, 5), (3, 7), (2, 10, 11),
             (6, 8, 9, 14)),
        )
    )
    assert all(valid_model(model) for model in compact_models)
    compact_choice_sets = tuple(root_choice_mask(model) for model in compact_models)
    compact_coverage = sum(
        any(
            choices & (1 << a_index) and choices & (1 << b_index)
            for choices in compact_choice_sets
        )
        for a_index in range(ROOT_COUNT)
        for b_index in range(ROOT_COUNT)
    )
    assert compact_coverage == 82_944

    ordered = tuple(sorted(certificates, key=lambda item: (item.support, item.bags)))
    choice_sets = tuple(root_choice_mask(certificate.bags) for certificate in ordered)

    root_coverage_sizes = Counter(mask.bit_count() for mask in choice_sets)
    certificate_supports = Counter(certificate.support for certificate in ordered)
    overlap_totals: Counter[int] = Counter()
    overlap_chained: Counter[int] = Counter()
    canonical_supports: Counter[int] = Counter()
    canonical_usage: Counter[int] = Counter()
    coverage_multiplicities: Counter[int] = Counter()
    witness_table = []

    for a_index, a_roots in enumerate(ROOT_MASKS):
        for b_index, b_roots in enumerate(ROOT_MASKS):
            overlap = (a_roots & b_roots).bit_count()
            overlap_totals[overlap] += 1
            covering = tuple(
                index
                for index, choices in enumerate(choice_sets)
                if choices & (1 << a_index) and choices & (1 << b_index)
            )
            if not covering:
                print("CHAIN_COVERAGE_FAILURE")
                print(f"A={list(ROOT_TUPLES[a_index])}")
                print(f"B={list(ROOT_TUPLES[b_index])}")
                return 1

            witness = covering[0]
            certificate = ordered[witness]
            # This is the literal paired-root check for this placement.
            assert all(bag & a_roots and bag & b_roots for bag in certificate.bags)
            overlap_chained[overlap] += 1
            canonical_supports[certificate.support] += 1
            canonical_usage[witness] += 1
            coverage_multiplicities[len(covering)] += 1
            witness_table.append(certificate.encoding())

    assert overlap_totals == overlap_chained
    assert overlap_totals[0] == 1_152
    assert sum(overlap_totals.values()) == 82_944
    assert min(coverage_multiplicities) == 4
    assert max(coverage_multiplicities) == 98

    catalogue = "\n".join(certificate.encoding() for certificate in ordered)
    witness_encoding = "\n".join(witness_table)
    used_certificates = sum(1 for count in canonical_usage.values() if count)

    print(
        "PB singleton root-assignment sweep: PASS "
        "placements=82944 chained=82944 arbitrary_only=0 negative=0 "
        f"disjoint={overlap_totals[0]} certificates={len(ordered)} "
        f"canonical_chain_certificates_used={used_certificates} "
        f"compact_models={len(compact_models)} compact_covered={compact_coverage}"
    )
    print(f"placements_by_root_overlap={counter_text(overlap_totals)}")
    print(f"chained_by_root_overlap={counter_text(overlap_chained)}")
    print(f"certificate_supports={counter_text(certificate_supports)}")
    print(f"certificate_root_choice_counts={counter_text(root_coverage_sizes)}")
    multiplicity_encoding = counter_text(coverage_multiplicities)
    print(
        "chain_certificate_multiplicity=4..98 "
        "histogram_sha256="
        f"{sha256(multiplicity_encoding.encode()).hexdigest()}"
    )
    print(f"canonical_chain_support_by_placement={counter_text(canonical_supports)}")
    print(f"certificate_catalogue_sha256={sha256(catalogue.encode()).hexdigest()}")
    print(
        "canonical_chain_witness_table_sha256="
        f"{sha256(witness_encoding.encode()).hexdigest()}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
