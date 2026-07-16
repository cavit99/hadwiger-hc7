# Barrier: the exact eight-terminal kernel bundle does not close overlap one

## Scope

This note records a counterexample to a proposed **composition lemma**, not
to `HC_7`.  The host data are the normalized twelve-object quotient in the
order-six-arm, overlap-one cell.  Adding an arbitrary rooted
three-connected eight-terminal kernel is not enough, by itself, to force a
`K_7` minor.

The deterministic generator and checker are
`../active/hc7_overlap_one_order_six_full_orbit_closure.py`.  Its structural
kernel input is the separate exact eight-terminal kernel theorem.  The
script itself is self-contained: it rebuilds the finite order-eight
catalogue with nauty `geng`, runs its own exact minor detector, and (in audit
mode) invokes Z3 only as an independent second negative checker.

## Exact reduction of the full relation

Write

```text
A = {0,1,2,3,4,5},       X = {0,6,7,8,9},
p = 10,                  q = 11.
```

The five six-object supports are

```text
A, X+p, X+q, {1,2,3,4,5,p}, {1,2,3,4,5,q}.
```

The joined relation factors into an `A` module with 8,055 states and an
`X` module with 1,635 states.  Exactly 5,410 `A`-module states lack the
previously audited common rooted-`K_4` outcome.  Hence the complete
noncommon relation contains

```text
5,410 * 1,635 = 8,845,350
```

distinct forced-edge masks.

Minor existence is monotone in forced edges.  Inclusion minima factor over
the two edge-disjoint modules: there are 400 minima on the `A` side and 330
on the `X` side, hence 132,000 global minima.  Their edge-count profile is

```text
28:100, 29:300, 30:3200, 31:900,
32:12300, 33:10800, 34:104400.
```

Quotienting first by `S_5` on `{1,...,5}` and `S_4` on `{6,...,9}`, then by
the simultaneous interchange of `p,q`, leaves 142 minimal orbits.  The
digest of the ordered orbit records is

```text
a81e4e2ca170878db8c96a0b3102e93c03091536d22d85f886e05b8d682e30de
```

## First minimal orbit: a complete obstruction

The first orbit already falsifies the universal composition.  Its
forced-edge mask is

```text
decimal 1438900359865595843
hex     0x13f80040f0f877c3
```

with literal present edges

```text
01 02 07 08 09 0A 0B
13 14 15 1A 1B
23 24 25 2A 2B
34 35 45
67 68 69 6A 6B
78 79 89
```

(`A` and `B` in this display denote vertices 10 and 11.)  All cross edges
between `{1,...,5}` and `{6,...,9}`, and edge `10 11`, are absent in the
tested completion.

On the five supports, the induced local fifteen-bit masks are respectively

```text
0x7fc3, 0x17fe, 0x17fe, 0x17fe, 0x17fe.
```

Each is one of the 375 audited local six-object states, and the quotient has
no common rooted-`K_4` outcome.  Thus this is a literal member of the
normalized relation, not an abstract mask outside it.

The category-preserving stabilizer of this state has order 144.

### Fixed deletion of the overlap vertex

If vertex `0` is deleted first and three further vertices are reserved,
there are 165 reserve triples.  Every one fails: for each triple, some
labelled edge-minimal three-connected graph on the other eight objects has
a union with the displayed state containing no `K_7` minor.  The 165
triples form 28 stabilizer orbits.

### Stronger arbitrary-four-reserve rescue

The same obstruction survives the stronger rule suggested after the first
failure.  Allow **any** four of the twelve objects to be reserved, leaving
the other eight as terminals.  All `C(12,4)=495` choices fail already at
kernel order eight.  They form 71 stabilizer orbits.

For each of those 71 representatives, the checker records one exact
edge-minimal three-connected carrier and verifies that its union with the
state has no `K_7` minor.  The ordered witness-record digest is

```text
a812ea793d2c188ab426b8a0a87b0e3901e773ab8e18340669da5fc819e848a3
```

The exact order-eight catalogue has 18 unlabelled and 196,976 labelled
members.  Its fixed-width digest is

```text
2191c87cc229cbf109b19bf66badb40c115838c5b1350709c64fd9a2ec2f020d
```

## Independent negative audit

The primary detector exhausts every seven-bag model on twelve objects.  A
model using at most twelve vertices has at least two singleton bags; the
detector enumerates every possible exact singleton core of size two through
seven and then every remaining connected, disjoint, pairwise adjacent bag.

Every one of the 71 representative negative graphs was also checked by an
independent Z3 encoding.  It uses seven nonempty disjoint vertex sets,
rank-decreasing parent constraints for connectivity, and one literal edge
between every pair of sets.  Ordering the least vertex of each set only
breaks bag-label symmetry.  All 71 formulas were unsatisfiable.  Therefore
the negative conclusion does not depend on the singleton-core detector.

The audited run reports

```text
reserve_four_orbits 71
reserve_four_weight 495
exact_detector_cache 9456
independent_smt_unsat 71
```

## Consequence

Terminate the proposed rung

> choose reserved objects, apply an arbitrary exact eight-terminal kernel,
> and compose solely from the resulting terminal carrier.

It fails even after allowing four arbitrary reserves and even on the first
minimal orbit of the normalized relation.  The separate eight-terminal
rooted-carrier theorem is unaffected.  A successful continuation must
retain additional information from the ambient graph or from the
contraction sequence (for example owner/attachment data not present in the
terminal quotient), or use a different global invariant.
