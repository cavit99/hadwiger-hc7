# Audit of the double-overlap cyclic-arc lock

This note audits `hadwiger_c6_double_overlap_arc_lock.md` at the two
places where a hidden loss of information was most likely.

## 1. Allocation of genuine overlaps

Let `L,R` be the actual cycle-contact rows.  They cover the cycle and
share chosen roots `a,b`.  For every vertex of
`(L intersection R)-{a,b}`, delete one of its two incidences.  Exclusive
contacts cannot be changed, so the resulting rows still cover the cycle
and meet exactly in `a,b`.  They are genuine subgraphs of the actual
quotient; hence a clique model in any allocation lifts to the actual
graph.

For fixed `a,b`, the two complementary-arc words differ in all four
nonroot coordinates.  Therefore two allocations differing in one
overlap coordinate cannot both be arc words.  It follows that if the
actual quotient is negative, there is no additional cycle overlap.  Its
unique allocation is an arc word.  This justifies the last paragraph of
Theorem 3.1; no assumption that an overlap may be represented twice in
one branch model is made.

The verifier `unique_interface_c6_word_lemma_verify.py` checks all

\[
 \binom62 2^4=240
\]

allocated cycle words.  Its audited output is

```text
binary words 240
covered by 13-row K4 table 204
antipodal full-row K7 certificates 6
complementary-arc residuals 30
```

It independently verifies every displayed four-bag model and both
orientations of the antipodal seven-bag model in both helper geometries.

## 2. Identity of the old interface endpoint

In the arm-split geometry, let the old unique interface be `xy`, with
`x` in the arm being split.  Exactly one of `P,Q` contains `x`; it is
named `P`.  Thus `BP` is retained in the quotient and `BQ` is not added.
The antipodal model (3.3) uses `BP` in precisely this orientation.  The
model (3.4) handles the opposite choice of the small/full contact row
without relabelling away the distinguished endpoint.  The thirteen-row
construction does not use `BP` at all, so its permitted `P,Q`
interchange is harmless.

## 3. External-neighbourhood identities

In the opposite-shore split, anticompleteness of the original shores
gives exactly

\[
 N_G(P)=N_S(P)\dot\cup N_Q(P).
\]

There is no suppressed edge from `P` to an old arm.  In the arm split,
the uniqueness of `xy` gives exactly

\[
 N_G(P)=N_S(P)\dot\cup N_Q(P)\dot\cup\{y\},
 \qquad
 N_G(Q)=N_S(Q)\dot\cup N_P(Q).
\]

The three displayed parts are disjoint because `S`, the two split
pieces, and the other old arm are disjoint.  Each neighbourhood
separates its nonempty piece from the nonempty opposite original shore.
Seven-connectivity therefore gives order at least seven, and equality
is genuinely an exact seven-cut.  If equality fails, integrality raises
the order to at least eight, yielding (4.5).  No stronger connectivity
than seven is used.

## 4. Exact negativity of the arc quotients

`unique_interface_c6_arc_rows_probe.py` tests both helper geometries,
all three cyclic distances, both arc orientations, and all three
nonempty placements of `z`.  All 36 maximal arc quotients are
`K_7`-negative.

The minor test is exact.  In an eleven-vertex graph, a `K_7` model uses
`m<=11` vertices and contracts exactly `m-7<=4` tree edges inside its
branch sets.  Conversely, any sequence of at most four adjacent-bag
merges producing a seven-clique is a `K_7` model.  The fast verifier
enumerates precisely these merge states; vertices outside the model may
remain unused, so no deletion case is omitted.

The two rerun verifiers exited successfully on 2026-07-11.  The audit
therefore supports the exact conclusion claimed in the main note:
static quotient information ends at the complementary-arc lock; the
next valid inputs are the real interface endpoint sets, a nested exact
seven-cut when equality holds, and the minor-critical one-step state
transition when it does not.

