# Adversarial audit: canonical two-block full-shore states

## Verdict

**GREEN AS PATCHED.**  The simultaneous full-shore contraction forces the
claimed exact boundary partition, the two-state exact-block inference is
valid, and the theta residue has exactly the two displayed forced-opposite
state pairs.  The verifier passes under `.venv/bin/python` after being
strengthened with a fixed partition manifest and assertions for both
possible relative orientations.

One mathematical sentence was false and has been corrected.  If two
two-state exact-block constraints share the **same** canonical state, their
orientations must agree, not vary independently.  Relative freedom occurs
only for constraints with two different canonical states, as in the theta
application.

This is an internal correctness audit, not external peer review or a
novelty determination.

## 1. Simultaneous contraction

The sets

```text
D_A union P,   D_B union Q
```

are disjoint and connected.  Each boundary vertex in `P` has a neighbour
in connected `D_A`, and symmetrically for `Q`.  Each set has at least two
vertices because its shore and boundary block are both nonempty, so the
minor operation is proper.

The two contracted images are adjacent: fullness of `D_A` supplies an
edge from it to every vertex of `Q`.  Each vertex of `R` is adjacent to
both images through the two full shores, and `G[R]` is complete.  Thus the
two images together with the literal vertices of `R` form a clique of
order `|R|+2`.

Every `r`-colouring of the proper minor therefore gives these clique
vertices pairwise distinct colours.  Expanding the first image only on
the boundary vertices `P`, and the second only on `Q`, yields:

* one exact colour block `P`;
* one exact colour block `Q`; and
* a distinct singleton block for every vertex of `R`.

Independence of `P,Q` is what makes those expanded boundary blocks proper;
completeness of `R` prevents singleton mergers; fullness prevents either
contracted colour from reappearing on `R`.  No planarity or spanning-shore
hypothesis is used.  The bound `|R|+2<=r` places the forced clique inside
the available palette.

## 2. Two-state orientation

The exact-block theorem supplies disjoint shore-extension families
`E_A,E_B`, and each family meets `Omega(P)`.  If

```text
Omega(P)={Pi_{P,Q}, Pi'},
```

then neither family can contain both states because the other family must
also meet this two-element set and the families are disjoint.  Hence one
state belongs to exactly one shore family and the other belongs to exactly
the other.  Neither extends both shores.

The canonical contraction state `Pi_{P,Q}` therefore defines one genuine
orientation bit: which shore extends it.

If a second two-state constraint `Omega(Q)` contains this **same** state,
the common vertex of the two Property-B edges has one colour.  Both
constraints necessarily orient it toward the same shore, and their two
other states lie together in the opposite shore.  The former claim that
these orientations could disagree was incompatible with the definition
of a state and with Property B.  It is repaired in the source.

This agreement does not relate constraints with different canonical
states.  Their relative bits can remain free.

## 3. Theta partitions

For graph6 type `FwJG?`, the missing boundary edges are

```text
01,02,05,12,15,24,45.
```

Hence `012` and `015` are independent boundary blocks.  After deleting
`012`, the only missing edge among `3,4,5,6` is `45`; a proper partition
containing exact block `012` can therefore either leave all four vertices
single or merge exactly `45`.  This gives exactly

```text
012|3|4|5|6
012|3|45|6.
```

Likewise, deleting `015` leaves `24` as the sole missing edge and gives
exactly

```text
015|2|3|4|6
015|24|3|6.
```

For `(P,Q)=(012,45)` and `(015,24)`, the remainder is `{3,6}`, which is a
clique in the boundary graph.  Theorem 1.1 therefore forces the two merged
canonical states

```text
012|3|45|6
015|24|3|6.
```

Each is opposite its unmerged partner in every exact-block Property-B
colouring.  They are distinct canonical states, so their relative
orientation is not determined by the shared-state argument of Section 2.

## 4. Executable spectrum audit

The command

```text
.venv/bin/python equality_gate_exact_block_state_spectra.py
```

passes for all ten packet residues.  The state universe consists of every
partition of the seven labels into at most six nonempty blocks, filtered
so that each block is independent in the boundary graph.  For every
nonempty independent block, the corresponding NAE hyperedge is exactly
the set of states containing that block.

The satisfiability recursion is exhaustive in `main()`; the capped
`enumerate_nae()` diagnostic is not used for the theorem assertions.
Fixing one queried state to colour zero loses no solutions because global
red/blue complementation is a symmetry.  Thus the same/opposite tests for
every state pair are exact.

The strengthened script now asserts:

* no forced-same state pair occurs in any of the ten types;
* the nine non-theta residues have no forced-opposite pair;
* the theta type has exactly the two manifested pairs above;
* its `Omega(012)` and `Omega(015)` spectra equal the displayed pairs; and
* the two merged canonical states are satisfiable both with equal and
  with opposite Property-B colours.

As an independent check, all Property-B colourings of the 19-state theta
instance were brute-forced with one global colour fixed.  There are 12,987
such colourings.  Their only forced-opposite pairs are the two displayed
pairs, and the XOR of the two merged-state colours takes both values.

## 5. Exact consequence and remaining gap

The theta packet core now carries two explicit, operation-generated
orientation bits rather than two arbitrarily selected states.  Abstract
exact-block data force each bit internally but allow both relative
orientations between the two distinct canonical states.

This is not a contradiction and does not close the theta type.  A closing
argument must use the actual `45` and `24` packet carriers, or faithful
shore operations, to correlate the two bits.  It must show that one
relative orientation yields a `K_7` packet while the other yields a common
opposite-shore state or a nested exact seven-cut.  The present result
identifies the two states that such an exchange must compare; it does not
perform that exchange.

## 6. Audit of the merge-pair and theta-bridge geometry

**GREEN.**  Theorem 5.1 uses an exact Kempe switch.  In the unmerged
state, the two singleton colours occur nowhere else on the boundary.  If
their bichromatic components were distinct, switching the component of
one singleton merges exactly those two blocks and changes no other block.
In the merged state, any boundary-absent colour similarly splits exactly
the merged pair.  A shortest path in the resulting bichromatic component
has no internal boundary vertex, so it is an external shore path.

For the theta states, the boundary bichromatic graph of `012|45` has
components `0-4-1` and `2-5`; switching one component produces
`015|24` literally.  The unmerged pair has components `{0}`, `{1}` and
`2-5`, and the same switch gives the other unmerged state.  Thus crossed
bits really force the two stated bridge types in each shore.  The paths
may arise from different colourings and no disjointness is inferred.

## 7. Audit of the crossbars and eight branch-set certificates

**GREEN.**  Both crossbar partitions have complete block-adjacency
quotient.  Cyclic-packet ownership supplies at least one shore containing
the two disjoint carriers.  One-way packet transfer then makes the exact
crossbar state extend the opposite shore.  If both shores owned the
crossbar, that state would extend both and the colourings would glue;
hence the owner is unique and rejects the state.  This membership comes
from actual transfer, not from an arbitrary red/blue Property-B entry.

The command

```text
.venv/bin/python equality_gate_theta_two_bit_verify.py
```

passes.  Its independent model checker verifies, for every row in (6.4),
seven nonempty disjoint connected bags and an edge between every bag
pair.  The abstract helper vertex lifts to the opposite connected full
shore, the two rail vertices lift to the disjoint adjacent owner carriers,
and the bridge vertex lifts to the carrier assumed disjoint from both
rails.  Thus all eight displayed `K_7` certificates are valid.

The invocation of the uniform three-demand theorem in Corollary 6.3 is
also legitimate although the demand systems `05,12,45` and `15,02,24`
repeat one boundary label.  The theorem's basic portal-set formulation
explicitly allows overlapping portal classes and handles their absorption
through its capture outcome.  Only its later connectivity refinement
assumes six distinct labels; Corollary 6.3 does not invoke that refinement.

Corollary 6.4 is exact.  The six missing pairs across
`{0,1,4}|{2,5}` consist of the two owned crossbar demands and precisely
the four closing pairs in Lemma 6.2.  Hence a bridge whose interior avoids
the rails either duplicates an owned demand or supplies one of the eight
models.  Boundary endpoints themselves never lie in the open-shore rails.

## 8. The proposed rail-median strengthening is false

**RED for the broad component statement; GREEN only for clean retained-
rail first hits.**  A first attempt retained rail arms after contracting
a median-deleted component which had actually absorbed them.  That gives
fictitious branch capacity.  The more faithful verifier

```text
.venv/bin/python theta_rail_component_absorption_verify.py
```

enumerates zero-length arms, absorbed arm components, median contacts and
extra `2`/`5` portal contacts.  It reports 5,488 negative useful-arm rows
and 4,564 negative target-portal rows.  Therefore neither “the component
reaches a useful arm” nor “the component has a `2`/`5` portal” forces
`K_7`, and the two medians need not bound a seven-cut.

There is an additional centre-only capture not covered by any statement
quantifying over a `4`-portal component of the median-deleted shore: all
`4`-portals may be the two medians themselves.  The remainder may be one
component full to `S-{4}`.  Its natural boundary has order eight, and the
static quotient can remain `K_7`-minor-free.  This is an atomic two-gate
operation-state lock, not an eliminated case.

Accordingly, Sections 5 through 6.4 are GREEN; Warning 6.5 correctly
records the falsification.  The remaining valid target is dynamic:
faithful operations across the two full shores must force a clean bridge,
a common boundary state, or a smaller owner core.  More static rail
enumeration cannot supply that implication.

## 9. The singleton-triangle descent bypasses the rail lock

**GREEN.**  New Theorem 6.6 does not revive the false rail claim.  It
uses the whole nonowner shore and the already audited arbitrary-order
singleton-triangle web theorem.

For the `05|12` crossbar the exact identification is

```text
P={0,5},  Q={1,2},  R={3,4,6}.
```

Both pair blocks are independent, `R` is a triangle, and their five-block
quotient is complete.  The three only potentially hidden block edges are
`25`, `04`, and `14`, all present in the theta boundary.  Lemma 6.1 gives
one actual packet owner and one actual packet-free nonowner, exactly the
input to the web theorem.

The theta-specific crossed-two-cut certificates were replayed
independently.  For complementary `P` defects they are

```text
{1}|{3}|{4}|{6}|L0|2L5|5E,
```

and for complementary `Q` defects they are

```text
{0}|{3}|{4}|{6}|L1|5L2|2E.
```

Here `E` is the opposite full shore.  Every bag is connected and all bag
pairs are adjacent.  Hence the strict-relative-boundary branch is a
three-connected bare web.

The audited curvature theorem gives at least six tagged outer vertices,
each seeing all of `R` and one root from each of `P,Q`.  Any two split a
spanning tree of the web.  Together with the two owner carriers, the
seven bags

```text
3|4|6|P+XP|Q+XQ|W0|W1
```

are a literal `K_7` model.  This uses neither a rail median nor a retained
arm.  The singleton nonowner is also impossible: it has degree seven and
neighbourhood `S`, where `012` is independent, contradicting Dirac's
`alpha(N(v))<=2` bound for a degree-seven vertex of a
7-contraction-critical graph.

The command

```text
.venv/bin/python equality_gate_theta_singleton_triangle_descent_verify.py
```

passes the five-block check, both crossed-cut models, and all sixteen tag
pairs.  Therefore every theta crossbar nonowner exposes a proper nested
exact seven-cut.  This is a genuine arbitrary-order elimination of the
atomic theta core, including centre-only and absorbed-arm architectures.
It is a descent theorem, not by itself a proof that changing boundary
types cannot continue indefinitely.
