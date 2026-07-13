# Independent audit addendum: packet deficiency and four-connected discharge

## Scope and verdict

This addendum audits only Section 6 of
`hc7_contact_transversal_amplification.md`; the adjacent audit covers
Sections 1--5.

**GREEN.**  All three scope repairs in Section 5 have been applied and
rechecked.  Lemma 4 is a correct exact packet-label criterion.  Lemma 5
now states the literal off-core, disjoint preassignment hypotheses needed
for its correct application of the audited four-set rural theorem.  Its
second outcome is accurately limited to one local rural page, not a
coherent disk for an entire adhesion.

## 1. Lemma 4: packet assignment criterion

Let `D` be the set of corner--row duties for which the direct
`Q_i-F_j` edge is absent.  A valid packet assignment in the sense of the
distributed-row theorem assigns each used packet one row label.  Hence,
for every `(i,j) in D`, it must select a packet adjacent to both `Q_i`
and `F_j`; and a packet selected for two duties can serve both only when
their row indices agree.  This is exactly (6.2)--(6.3).

Conversely, choices satisfying (6.2)--(6.3) give every selected packet
a unique row label.  Multiple packets may receive the same label, and
one packet may repair arbitrarily many corners of its one row.  The
packets are already pairwise disjoint and off the seven cores, so
Theorem 1.5 applies.  Thus the equivalence in Lemma 4 is correct; it is
not a hidden matching-capacity assumption.

The prose immediately after the proof needs one logical qualification.
Failure can occur because some missing duty has
`N(i,j)=emptyset`, in which case no complete choice exists at all.  Only
after every `N(i,j)` is known nonempty is failure equivalent to: every
complete selection assigns one packet to duties from two different
rows.  Calling the latter the unique exact failure makes the empty-
support branch disappear vacuously.

## 2. Lemma 5: exact set-rooted Two Paths use

The portal-set ordering in (6.4) is correct.  Apply the audited theorem
with its variables

\[
                  (A,B,P,Q)=(A,B,P,R).
\]

Its linkage outcome is a pair of disjoint paths joining `A` to `P` and
`B` to `R`.  Their vertex sets are disjoint connected sets.  Because
the first contains a vertex adjacent to `Q_i` and one adjacent to
`F_j`, it is an eligible row-`j` packet; the second is analogously an
eligible row-`k` packet.  Extra portal contacts on either path are
harmless because each packet receives only its designated row label.

The other outcome makes `G[L]` planar and puts all four sets on one
facial cycle in the exact block order

\[
                             A,R,P,B
\]

up to reflection.  This is the labelled alternating order for the
demands `A-P` and `B-R`.  Four-connectivity and the assumed nonempty,
pairwise disjoint portal sets are precisely the hypotheses of the
set-root theorem; no stronger connectivity is being smuggled in.

## 3. Missing disjointness needed for the packet conclusion

The phrase “the sole failure ... is concentrated in one connected
packet region `L`” has no formal definition in Lemma 4 and is not enough
to invoke the distributed-row theorem.  The intended sufficient
hypothesis should be stated literally:

* `L` is disjoint from the seven core bags;
* there is an already labelled family `K_0` of pairwise disjoint
  connected packets, disjoint from `L` and from the cores;
* direct edges together with `K_0` repair every duty other than
  `(i,j)` and `(h,k)` (or every duty other than those two and at most one
  explicitly retained `K_7^-` defect); and
* `L` supports the four nonempty portal sets in (6.4).

Under these hypotheses, replace `L` by the two paths returned by the
linkage outcome.  They are disjoint from `K_0` because they lie in `L`,
so the enlarged packet family meets every hypothesis of Theorem 1.5.
If all other duties were repaired, the conclusion is actually `K_7`;
if one separately declared duty remains unrepaired, it is `K_7^-`.

Without `K_0 cap L=emptyset`, an already used witness for a third duty
may meet every returned path.  The paths still solve the local linkage,
but they do not form a pairwise disjoint global packet family.  Thus the
omitted hypothesis is necessary for the claimed handoff, not merely
cosmetic.

## 4. Spine boundary of the rural outcome

The rural alternative is useful and reusable: it turns one locked
two-row collision in one 4-connected lobe into a single labelled facial
page.  It does not by itself prove that both open shores share a common
disk order, that pages across 1/2-adhesions glue, or that deleting two
fixed vertices makes the host planar.  Those require the separate
torso-tree/guarded-cycle composition step.

Accordingly, the applicability paragraph should say “one local rural
page ready for the rural composition branch,” not “one common rural
web” if the latter is meant as a completed adhesion-level outcome.  The
listed residuals--overlapping portal classes, a cutvertex/2-adhesion,
and multiple collisions--are otherwise accurate.

## 5. Repairs applied and verified

1. After Lemma 4, distinguish an empty support set `N(i,j)` from a
   genuine cross-row collision among complete packet choices.
2. In Lemma 5, replace “sole failure concentrated in `L`” by the formal
   off-core and disjoint preassigned-family hypotheses of Section 3.
   State the rural block order explicitly as `A,R,P,B`.
3. Describe outcome 2 as one **local** rural page which feeds, but does
   not complete, the torso/adhesion gluing branch.

All three changes now appear in the source note.  Section 6 is GREEN and
can inherit the theorem note's audited status.
