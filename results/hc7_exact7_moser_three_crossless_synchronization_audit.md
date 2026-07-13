# Independent audit: three crossless Moser frames synchronize

Audited source: `../archive/hadwiger_reserved_connector_rank_leaf.md`,
Theorem 5.1, together with
`../archive/moser_c5_crossless_order_probe.py` and
`../archive/moser_c5_three_crossless_exact_probe.py`.

## Verdict

**GREEN under the literal common-face hypotheses stated below.**  The
occurrence-level strengthening is real: overlapping portal sets, multiple
occurrences of one portal label, coincidences between a proposed linkage
occurrence and an SDR occurrence, and a single vertex serving both labels
of one demanded pair are all allowed.  The proof does not make incompatible
one-occurrence choices for the three crossless frames.

The three-connected shore formulation additionally depends on the preceding
relative bare-web theorem and Whitney uniqueness to put all five *full
literal portal sets* on one common facial cycle.  The synchronization
argument does not apply to a two-connected shore with frame-dependent face
choices, to abstract label incidences without literal portal vertices, or
to supports living in different embeddings.

## Promoted theorem

Let `D` be a graph embedded in a closed disk, and let its boundary be a
simple facial cycle `F`.  Let

\[
                         P_0,P_1,P_2,P_3,P_4\subseteq V(F)
\]

be literal portal sets admitting a system of five distinct
representatives.  Portal sets may overlap.  For indices modulo five, define
frame `j` to consist of the two demands

\[
             P_{j+1}\!\longleftrightarrow P_{j+2},
             \qquad
             P_{j+3}\!\longleftrightarrow P_{j+4}.
\]

Call the frame crossless when there are no two vertex-disjoint connected
subgraphs of `D`, one meeting the first two portal sets and the other
meeting the last two.  If any three of the five frames are crossless, then
all five are crossless.

For the intended HC7 corollary, let `D` be the three-connected relative
pure-Moser shore satisfying the seven-boundary fullness/cut inequality.
The Hall argument supplies the five-portal SDR.  Each crossless frame gives
a bare-web embedding with its four full portal sets on one face.  Three
such frame faces coincide by Whitney uniqueness, so the focused theorem
applies.

## 1. Five literal portals have a simultaneous SDR

The Hall proof used earlier for four labels extends verbatim to all five
Moser root labels.  For a subfamily `I`, if the union `R` of its portal
sets has order below `|I|` and `D-R` is nonempty, a component of `D-R` has
at most

\[
                    (|I|-1)+(7-|I|)=6
\]

external neighbours.  This contradicts the installed relative
seven-connectivity inequality.  If `D=R`, then `|D|<=4`, contradicting
`|D|>=6`.  Thus the representatives can be chosen simultaneously and are
literal distinct shore vertices even when the portal sets overlap.

## 2. The three frame faces really coincide

Any two distinct missing-cycle frames share three portal labels.  Choose
the three corresponding representatives from the five-label SDR.  They
are three distinct vertices belonging to both frame faces.  In the unique
embedding of a three-connected planar graph, two distinct faces cannot
share three vertices.  Hence the two faces are equal.  Pairwise comparison
of the three crossless frames produces one common face, and their union of
labels is all five labels.  Consequently every occurrence of every full
portal set lies on that same face.

This is the exact point at which three-connectivity is used.  Merely having
three separate disk certificates is insufficient.

## 3. Crosslessness constrains every occurrence choice

Fix any four facial occurrences `x,y,z,t` for the two demands of a
crossless frame, and suppose no occurrence of the first pair equals an
occurrence of the second pair.

If `x=y`, the singleton `{x}` realizes the first demand.  One of the two
facial `z-t` arcs avoids `x` (or `{z}` realizes the second demand when
`z=t`), giving disjoint supports.  Thus neither within-pair collapse is
possible.  With four distinct occurrences, a nonalternating circular order
gives two vertex-disjoint facial arcs realizing the demands.  Therefore
the four occurrences must alternate.

This conclusion is universal over occurrence choices.  It is not tied to
one representative chosen for a frame.

## 4. A proposed remaining linkage yields one finite weak-order system

Fix the five SDR occurrences.  The three crossless-frame constraints force
their facial order to one of the two pentagram orders

\[
                         0,2,4,1,3
                  \quad\text{or its reverse}.
\]

This is the complete `4!=24` circular-order enumeration reproduced by
`moser_c5_crossless_order_probe.py`.

If a remaining frame were linked, choose one portal occurrence of each
label in its two disjoint connected supports.  The two occurrences within
one support may coincide, but every occurrence chosen from one support is
distinct from every occurrence chosen from the other.  If all four are
distinct, their order is nonalternating by the disk separation theorem.

For each of the three crossless frames, it is enough to impose the universal
constraint from Section 3 on every choice drawn from the five SDR
occurrences and these four support occurrences.  Every real configuration
induces precisely such a weak circular order.  No occurrence outside this
nine-occurrence set is needed for the contradiction.

## 5. Verifier audit

The exact probe has five distinct ordered SDR variables and four additional
support variables.  It deliberately allows:

* equality of the two occurrences within either support;
* equality between a support occurrence and any SDR occurrence; and
* otherwise-unforced equal positions, which only relax the search.

It forbids equality only across the two disjoint supports.  For every
selected occurrence quadruple of every crossless frame, its
`antipodal_forbidden` formula says: if the two pairs are cross-disjoint,
then neither pair collapses and the four positions alternate.  Its
`frame_realized` formula is the complementary necessary disk condition for
the proposed linked frame: cross-disjointness, with either an allowed
within-support collapse or four distinct nonalternating endpoints.

The search covers all ten choices of three crossless frames, both
pentagram orientations, and each of the two remaining candidate linked
frames: forty systems total.  I reran it and obtained

```
checked 40 satisfiable 0
```

The use of integer positions `0,...,8` loses no real configuration: at most
nine selected occurrences exist, and their cyclic weak order can be
compressed into those positions after rotating the representative of label
zero to position zero.  Allowing distinct real vertices to take an equal
integer position is again a relaxation, so unsatisfiability remains sound.

## Trust boundary

The result uses the following equivalent packages:

1. the focused common-face theorem above, retaining the small exhaustive
   verifier as part of the proof; or
2. the three-connected pure-Moser corollary, provided the relative
   bare-web/common-face lemma, five-label Hall SDR, and Whitney uniqueness
   are cited explicitly.

The audit does **not** promote the later rank-one leaf claims, does not
assert a common face in a merely two-connected shore, and does not turn
crosslessness into a colouring state.  The finite part currently trusts the
reported Z3 unsatisfiability and the audited encoding; a fully
dependency-free enumerator or stored proof certificates would narrow that
computational trust boundary but is not needed for the occurrence-level
logical validity.
