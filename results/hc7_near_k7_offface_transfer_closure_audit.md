# Independent audit: off-face transfer at a marked two-duty carrier

## Verdict

**GREEN after correction to linkage-or-descent.**  The vertex-transfer
lemma preserves the full marked two-duty certificate, including all four
portal families, one fixed SDR, and every disjoint helper.  A
four-connected rural carrier therefore gives either the protected fixed
linkage or a strictly smaller marked carrier.  Iteration is finite and
terminates at a linkage or a non-four-connected carrier.

The source now states exactly this descent and expressly does not call
the family closed.  No preservation of four-connectivity after the
transfer is asserted or needed.

## 1. The transfer comparison is label-faithful

Let `w` be the off-face vertex returned in the rural outcome.  Full-SDR
facial coherence puts the entire union

\[
                 A_L\cup A_R\cup P_H\cup P_Q
\]

on `F`.  Hence `w` belongs to none of those four sets.  Deleting `w`
therefore leaves every portal family literally unchanged, not merely
nonempty.  The old SDR remains an SDR, `K-w` remains attached to both
path sides, and the two named duties `H,Q` remain present.

Four-connectivity of the original `G[K]` makes `K-w` connected.  It is
still disjoint from every selected helper; moving `w` into a foreign row
does not move or consume a helper vertex.  Every helper's old attachment
to its assigned path side and row also survives.  Thus the marked
certificate really is preserved.

## 2. The target row exists

Every neighbour of `w` outside `K` is in `P` or a foreign bag, because
distinct old exterior pieces are anticomplete.  An edge to `P`, `H`, or
`Q` would put `w` in one of the four locked portal families on `F`.
There is no edge to the fixed missed twin `D`.  The degree-escape vertex
has an external neighbour, so it meets one of the other three retained
rows.

Choosing `E` whenever it is available is the correct rule.  If `E` is
one of the named duties, then all its `K`-portals lie on `F`, so the
off-face `w` does not meet it.  Hence the proof works for any two
distinct retained duties `H,Q`; they need not both be neutral rows.

## 3. Every model adjacency survives

With

\[
                         A'=A-\{w\},\qquad T'=T\cup\{w\},
\]

the target `T'` is connected through a literal `wT` edge.  The bag `A'`
is connected because `K-w` is connected and retains its path
attachments.  An edge from `w` to `K-w` gives the new `A'T'` adjacency.

The old foreign clique survives inside the enlarged target.  The four
`A'U_i` endpoint edges on `P` survive.  If `T=E`, the `w(K-w)` edge
restores `A'E`; if `T!=E`, then `w` had no `E`-neighbour, so the old
`AE` adjacency was not removed.  Finally `A'D` remains absent because
`A' subseteq A`.  The bag union is unchanged, so spanning and
disjointness are preserved.

These checks validate Lemma 1 completely.

## 4. Descent and termination

The transfer may destroy four-connectivity, and the corrected theorem
handles this exactly.  Apply it only while the current marked carrier is
four-connected.  In the non-linkage outcome its order decreases by one
and all marked data survive.  A finite sequence cannot decrease order
indefinitely.  Hence it ends either with a linkage or at a carrier to
which the four-connected theorem no longer applies.

The audited statement is:

> **Four-connected transfer descent.**  A marked rank-four two-duty
> carrier which is four-connected either has the protected fixed linkage,
> or there is another spanning labelled near-`K_7` model with the same
> path core, missed twin, named duties, SDR, and disjoint helpers, whose
> marked carrier has smaller order.

Corollary 3 says exactly this.  It invokes shore completion only in the
linkage outcome and retains the non-four-connected descendant as the
remaining case.  Thus there is no induction or minimization gap in the
revised source.

## 5. Scope

To infer a literal `K_7` from every initial collision, one must still
close the resulting lower-connectivity carrier.  Rank-at-most-three
portal systems and failures of the disjoint-helper certificate also
remain outside the theorem.

No palette-to-label inference, virtual torso edge, or ambient separator
counting issue occurs; the sole defect is the lost four-connectivity in
the descent.
