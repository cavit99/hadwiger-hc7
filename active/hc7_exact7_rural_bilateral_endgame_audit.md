# Independent audit: rural bilateral endgame

Audited file: `active/hc7_exact7_rural_bilateral_endgame.md`.

This audit supersedes the earlier audit of the pre-repair version of
Lemma 4.1.  The source now states a genuinely local disk-substitution
criterion and expressly limits its application to the selected quotient
subgraph.

## Verdict

* **Theorem 2.1 — GREEN**, under the inherited induced-carrier and
  rank-first lexicographic-minimality hypotheses.  Its simple quotient
  edge list is exhaustive, including every pole--root edge, and it uses
  the whole literal sets `Q_*` and `P_*`.
* **Theorem 3.1 — GREEN.**  The two disk drawings glue along the same
  literal five-cycle, and the two deleted vertices receive two fresh
  colours.
* **Lemma 4.1 — GREEN.**  It is now exactly an if-and-only-if statement
  about replacement inside a fixed disk.  Both directions follow by
  radial insertion and restriction to that disk.
* **The selected-pole application — GREEN at its stated scope.**  The
  companion tree-pole rotation theorem gives the claimed dichotomy for a
  selected connector.  It does not embed an induced pole society or any
  omitted shore vertex.
* **Section 5's spanning-quotient citation — GREEN.**  The cited theorem
  removes the former nonspanning-quotient gap by returning either a
  literal obstruction certificate or a quotient containing every shore
  vertex.
* **The rural endgame as a whole remains open.**  Its exact remaining
  obligations are occurrence multiplicity at contracted poles, expansion
  of each induced pole society, and conversion of a literal obstruction
  certificate while preserving the attained decorated-state duty.

Thus the repaired note contains no false lemma identified by this audit.
It is a correct conditional endgame, not yet a closure theorem for the
rural branch.

## 1. Literal two-pole quotient

The two contracted vertex sets are disjoint and connected: `L` is the
fixed connected locked region, while `A union B` is connected through the
literal `A-B` core adjacency.  The second pole is `L`, not the earlier
decorated set `W={w} union L`; this is appropriate for the selected graph
after `w` is deleted.  The source no longer claims that this selected
quotient already contains the whole closed shore.

Under the induced-carrier convention of
`results/hc7_exact7_block_terminal_web.md`, contraction creates an
`alpha-k` edge exactly when `k in Q_*`, and a `beta-k` edge exactly when
`k in P_*`.  The four possible pole--root edges are precisely the outer
frame edges

\[
 x\alpha,\quad \alpha y,\quad y\beta,\quad \beta x.
\]

The rank-one condition `E(L,A union B)=empty` excludes `alpha-beta`.
All remaining quotient edges are internal carrier edges; edges internal
to a pole become loops and are deleted.  Hence the simple quotient edge
list is exhaustive.

Rank-first carrier minimality legitimately removes nonrib cells.  The
same evacuation argument used in the audited block-terminal theorem
applies to the larger sets `Q_*,P_*`: every member has the universal
capture property, both sets have order at least three, cell vertices meet
neither set, and evacuating a cell lowers the carrier without lowering
either contact rank.  Therefore the lex-optimal three-connected carrier
has no nonrib cell, and the simple quotient is a subgraph of a planar rib.

## 2. Bilateral disk gluing

The phrase “the two closed terminal shores” includes

\[
 J_a\cup J_b=G-\{v,w\},\qquad J_a\cap J_b=U,
\]

together with anticompleteness of their open parts.  Each disk drawing has
the same literal five-cycle `G[U]` on its boundary.  Reflecting one disk if
necessary aligns the cyclic orders.  Identifying equal literal boundary
vertices and edges gives a sphere drawing; there is no unaccounted
cross-shore edge.

The Four Color Theorem colours `G-{v,w}` with four colours.  Giving `v`
and `w` two different fresh colours is proper whether or not `vw` is an
edge.  Theorem 3.1 is therefore exact.

## 3. Repaired Lemma 4.1

The former version spoke about an arbitrary planar extension of `R-z`.
That was too broad: an arbitrary extension need not place the replacement
inside the face and rotation formerly occupied by `z`.

The repaired statement fixes a closed disk `Delta_z`, keeps the drawing
outside it unchanged, draws all of `X` inside it, and assigns every old
edge end to a specified attachment of `X`.  Under this definition:

* if the occurrence society has the prescribed disk embedding, insert it
  and join corresponding occurrences through a thin radial collar; and
* if a local replacement exists, restriction to `Delta_z` is exactly the
  required occurrence-society disk embedding.

These are inverse descriptions of the same local operation.  The old
star/path counterexample refuted only the superseded arbitrary-extension
formulation and is irrelevant to the repaired lemma.

## 4. Attachment-occurrence multiplicity

Theorem 2.1 deliberately produces a **simple** quotient.  If several
original pole edges have the same quotient endpoints, suppressing
parallel edges forgets their individual edge-end occurrences.  Lemma 4.1,
correctly, requires every old edge end to be assigned to an actual pole
vertex.

This does not threaten quotient planarity.  Before local substitution one
may reinsert all parallel copies in a thin band around the corresponding
simple rib edge.  One must then retain their chosen order as part of the
pole-society data.  The simple rib determines the order of distinct
quotient edges, but not the internal order of suppressed copies.

Accordingly, the selected-pole dichotomy is exact after a full
parallelization has been chosen.  A failed order for one parallelization
does not by itself prove that every possible parallelization fails.  Any
later conversion theorem must either choose an order that expands or show
that all admissible orders yield a literal obstruction.  This is the
remaining **pole-occurrence multiplicity** obligation; it is not a defect
in Lemma 4.1.

## 5. Selected connector versus induced pole

The source now cites the audited companion theorem
`results/hc7_exact7_tree_pole_rotation_exchange.md`.  That theorem is
tailored to an edge-minimal tree connector and handles repeated base
vertices by retaining attachment occurrences.  It gives an exact local
alternative:

1. the selected connector has the required disk rotation; or
2. there are two literal vertex-disjoint carriers joining alternating
   attachment occurrences.

This citation repairs the former unsupported appeal to a generic Two
Paths theorem.  The conclusion is nevertheless limited to the selected
connector.  Vertices and edges of the induced pole outside that connector
may prevent extension of the disk drawing.  Thus “selected connector
expands” must not be read as “the entire induced pole expands.”

## 6. Spanning rural quotient

Section 5 now invokes the independently audited theorem
`results/hc7_exact7_spanning_rural_quotient.md`.  At quotient level it
accounts for every vertex of the relevant shore and returns one of:

* an actual low carrier cut;
* a shared portal;
* a set-terminal cross;
* a proper bilateral three-gated cell; or
* a planar quotient in which every shore vertex belongs to the carrier or
  one of the two poles.

This citation closes the old “selected quotient is nonspanning” gap.  It
does not automatically produce a disk embedding of the original induced
poles, nor does it convert any of the first four outputs into a `K_7`
model or a common equality state.  Those are separate expansion and
conversion steps.

## Exact trust boundary

The audited dependency chain now proves:

\[
\text{rank-first rural core}
\Longrightarrow
\begin{cases}
\text{a literal cut/cross/gate certificate},\\
\text{or a spanning planar two-pole quotient},
\end{cases}
\]

and, for every chosen pole connector,

\[
\text{prescribed local rotation}
\Longrightarrow
\begin{cases}
\text{a valid local expansion},\\
\text{or two literal alternating carriers}.
\end{cases}
\]

What is not yet proved is the final implication from these outputs to a
literal `K_7` model, a common bilateral boundary-colouring state, or the
same fixed pair `{v,w}` with `G-{v,w}` planar (or merely
`K_5`-minor-free).

Any such final implication must simultaneously discharge three named
duties:

1. **occurrence duty:** restore and consistently order every suppressed
   pole-edge occurrence;
2. **induced-pole duty:** expand the whole induced pole society, not only
   one selected tree connector; and
3. **state duty:** preserve the actually attained decorated boundary
   state when converting a cut, cross, gate, or alternating-path output.

Raw contact or an abstract equality pattern is insufficient for the third
duty.  Subject to this trust boundary, the repaired source is internally
sound and aligned with the present proof spine.
