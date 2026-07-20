# Internal audit of the component-aware off-path bridge draft

**Verdict:** **GREEN** for every claim stated as proved, at the exact source
revision below.  The overall bridge-chain theorem remains unproved, so the
campaign outcome is `no_result` rather than a promoted result.

**Audited source:**
[`hc7_pentagonal_bipyramid_off_path_bridge_draft.md`](hc7_pentagonal_bipyramid_off_path_bridge_draft.md)

**Audited source SHA-256:**
`42fdeea559db6ac4618ee25f3ab0c52a437c2a9d99fa45b2b1a65bb2e069bf9f`

**Finite probe:**
[`hc7_pb_bridge_mechanism_probe.py`](hc7_pb_bridge_mechanism_probe.py),
SHA-256
`7f092b991b4c7ef9ab231217c087bf569a300cf32d9a5cc8ba6165a0595d6d40`,
committed as `b7844a1`.

**Audit type:** separate internal mathematical and computational cold audit.
This is not external peer review and does not prove Conjectural Theorem 3.1
or `HC_7`.

## Mathematical verdicts

- **Lemma 2.1: GREEN.**  The five branch sets are pairwise disjoint and
  connected.  Each of the ten required adjacencies has a literal edge
  witness, and each bag contains a whole column meeting both root sets.  The
  proof correctly needs neither shortestness nor five-connectivity.
- **Lemma 3.1: GREEN.**  Contracting the two prescribed connected subgraphs,
  deleting an edge of their path in a spanning tree, and expanding gives the
  claimed connected bipartition.
- **Lemma 3.2 and Corollaries 3.3--3.4: GREEN.**  Both directions of the exact
  equivalence among a two-sided off-path component for some pole path, the
  prescribed Two Paths linkage, and an alternating connected bipartition are
  present.  Consequently the genuine negative hypothesis quantifies over all
  pole paths, not merely a chosen shortest path.
- **Proposition 4.1: GREEN.**  The six-vertex path with the two displayed
  bridge vertices has crossing attachment intervals, exactly the stated
  shortest pole paths, and no prescribed disjoint linkage.  Thus interval
  crossing alone is not sufficient.
- **Lemma 4.2: GREEN.**  Replacing the closed attachment segment by an
  off-path bridge route releases a literal disjoint open segment and validly
  invokes Lemma 3.2.
- **Theorem 5.1: GREEN as an application of the cited theorem.**  The four
  artificial terminals are distinct, and Humeau--Pous Definition 1.2 and
  Theorem 1.5 yield the stated same-vertex framed `4`-web completion.  The
  proof never treats completion edges as host edges.
- **Lemma 5.2 and Corollary 5.3: GREEN.**  The translation from a web cell to
  literal host neighbours, the five-connectivity lower bound, the exclusion
  of opposite frame terminals, and the connected-complement argument are
  sound.  The surviving cells have exactly the stated singleton or
  consecutive-terminal forms.
- **Proposition 5.4: GREEN.**  Independent reconstruction confirmed the exact
  pentagonal-bipyramid quotient, displayed web completions, unbounded owner
  boundaries, and connectivity after every deletion of at most four vertices
  in both construction families.
- **Section 6 and Propositions 6.1--6.2: GREEN.**  The deletion, contraction,
  and reassignment criteria assert only the invariants actually proved.
  Independent reconstruction confirmed the connectivity, colouring,
  quotient, contraction/deletion, and displayed paired-model claims.  These
  examples are mechanism barriers, not counterexamples to the target.

The imported audited sources were checked at their recorded revisions:

- adjacent-rim linkage:
  `8c7882e2897cedda5cb768ba34f9691a4f23f45a3482d55deae1874ab83e8e79`;
- two-column absorption:
  `2759a37d6d3e6b93022c5fb58744dffbcd2e1d32b7263fdac201c77f07a39cff`;
- single-bridge span-inference barrier:
  `1f9d4adf3900fb9fae3f5c2d8060514c7d564c5139bb6cdf7f9a0f4c619f1343`;
- split/linkage/planarity barrier:
  `dddd2eeafd34cca51199fdbcdfa760332ab3272b071086797a4fee05eca05ec8`.

## Computational audit

The cold audit compiled the three retained scripts, reran the full bridge
probe, reran the two imported barrier verifiers and the absorption verifier,
and independently reconstructed the graphs in Propositions 5.4, 6.1 and
6.2.  The full probe reproduced:

- 2,920 frames and 15,320 shortest paths;
- 3,020 transfer paths;
- 2,300 alternating-split frames;
- 1,540 adjacent-linkage frames;
- 802 two-column-absorption frames;
- 2,480 whole-Two-Paths-positive but bridge-local-negative cases;
- 6,320 laminar attachment sets that are not host separators; and
- zero bridge pairs, with at most one owner-column bridge on every tested
  shortest path.

The probe is semantically consistent with the written definitions and labels
all of these counts as computer-assisted finite evidence.  In particular,
the frozen corpus cannot confirm or refute a theorem about pairs of crossing
or laminar bridge intervals.

## Scope and unresolved inference

The audit agrees with the draft's `no_result` boundary.  The corrected
component-aware transfer and exact one-column closure are proved; crossing
order by itself is falsified; the negative Two Paths theorem is decoded down
to its exact local web-cell residue; and automatic deletion, contraction, and
reassignment reductions are ruled out.

What remains is a theorem coupling the five negative adjacent-carrier webs
while preserving literal column ownership, external edge bundles, paired
branch-set allocation, and the four-colouring conclusion.  Its first
irreducible local form is a cell behind `{t_x,z_1,z_2}` with at least three
literal neighbours in the single owner column.  Neither the cited web theorem
nor five-connectivity supplies the required global allocation.  No complete
bridge theorem, full-hypothesis target counterexample, whole-host planar
outcome, or strict same-form reduction is asserted.

After the cold audit, two nonmathematical edits were made: the reduction gate
was weakened to the logically exact conclusion-level colour pullback, and the
status header was linked to this audit.  The cold auditor explicitly confirmed
that the GREEN verdict transfers to the exact source hash recorded above.
