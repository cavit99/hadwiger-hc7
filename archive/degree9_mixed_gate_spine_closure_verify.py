#!/usr/bin/env python3
"""Dependency-free audit of Lemma 2.1's non-protected split model.

The quotient keeps only adjacencies explicitly forced in the proof.  The
certificate is checked for disjointness, connectivity, and all 21 pairwise
contacts.  The protected split with r5 and 5 on the same side is already
audited in hadwiger_degree9_complementary_lobe_ownership_audit.md.
"""

from itertools import combinations


VERTICES = (
    "v", "h", "1", "2", "3", "4",
    "K", "D", "L0", "R0", "X", "Y",
)
EDGES = set()


def add(a, b):
    EDGES.add(frozenset((a, b)))


# Moser frame, with 6 represented by D, 5 by Y, and r5 by X.
for z in ("h", "1", "2", "3", "4", "D", "Y"):
    add("v", z)
for z in ("1", "2", "3", "4", "K", "L0", "R0", "X"):
    add("h", z)
add("1", "2"); add("3", "4")
for z in ("K", "D", "L0"):
    add(z, "1"); add(z, "2")
for z in ("R0", "X", "Y"):
    add(z, "3"); add(z, "4")

# Only the model/split contacts used by the certificate.
for a, b in (
    ("K", "D"), ("K", "X"), ("K", "Y"), ("X", "Y"),
    ("X", "L0"), ("D", "L0"), ("L0", "R0"),
    ("D", "Y"),
):
    add(a, b)


CERTIFICATE = (
    {"h"}, {"1"}, {"2"}, {"L0"}, {"K", "X"},
    {"v", "3", "R0"}, {"4", "D", "Y"},
)


def connected(bag):
    seen = {next(iter(bag))}
    while True:
        nxt = seen | {
            y for x in seen for y in bag
            if frozenset((x, y)) in EDGES
        }
        if nxt == seen:
            return seen == bag
        seen = nxt


assert set().union(*CERTIFICATE) == set(VERTICES)
assert sum(map(len, CERTIFICATE)) == len(VERTICES)
assert all(connected(bag) for bag in CERTIFICATE)
assert all(
    any(frozenset((x, y)) in EDGES for x in a for y in b)
    for a, b in combinations(CERTIFICATE, 2)
)
print("mixed_split_certificate=PASS")
print("bags=", CERTIFICATE)
print("pairwise_contacts=21")
