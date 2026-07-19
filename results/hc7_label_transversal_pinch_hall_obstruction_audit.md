# Internal audit of the label-transversal pinch Hall obstruction

**Verdict:** **GREEN** for source revision
`46df0d770db1e4918a53de49e1b911814a378c245690bfdbe1a0c8ff68aad37d`.
This is an internal audit, not external peer review.

## 1. Scope checked

The audit checks only the theorem in
[`hc7_label_transversal_pinch_hall_obstruction.md`](hc7_label_transversal_pinch_hall_obstruction.md).
It checks the orientation of the critical-pinch response, the use of the
adaptive `(1,3)` theorem, and the Hall-neighbour calculation.  It does not
audit the four cited dependency proofs anew.

## 2. Separation and orientation

The retained part of `U` is explicitly assumed nonempty outside `L union
S`, so `S=N_G(L)` is an actual separator.  Since `L` is connected, has
neighbourhood exactly `S`, and has no edge to `R`, it is one open component
of `G-S`.

The critical-pinch response is oriented correctly.  A colouring of
`G-s ell` is proper on the intact opposite closed shore `G[R union S]`,
because the failed edge has its other endpoint in `L`.  The cited theorem
states exactly that the returned partition does not extend through the
intact closed `L`-side.

## 3. Full connected subgraphs and the packing bound

Every component of `G-S` is `S`-full by seven-connectivity.  Hence both
open shores contain a full connected subgraph.  If `R` contained three
disjoint full connected subgraphs, those three together with `L` would
meet the adaptive `(1,3)` theorem.  Its two conclusions contradict the
assumed `K_7`-minor exclusion and seven-chromaticity.  Thus `1<=r<=2`.

No stronger packet vector is asserted.  In particular, the proof does not
assume that the six retained branch-set pieces are connected components or
additional full supports.

## 4. Hall calculation

The transported-partition theorem is applied with its coloured support
shore equal to `R`.  This is essential: `Pi` is legal on `G[R union S]`,
not on `G[L union S]`.  The `P_j` are universal incidence vertices, and a
`W_k` is incident with exactly the blocks whose complete duties it meets.
All displayed disjointness and pairwise-adjacency hypotheses match the
cited theorem.

A saturating matching would reproduce `Pi` on the intact `L`-side and
therefore glue, so Hall supplies

\[
                 r+|N_W(X)|<|X|.
\]

The inequalities in (2.4) follow integrally.  When `d=r+1`, no deficient
set can have order at most `r`, because it already sees all `r` universal
vertices.  Thus the only possible deficient set is the full block family,
and it has no `W`-neighbour.  The two claimed lowest-demand cases are
correct.

## 5. Trust-boundary audit

The final section correctly refuses three unsafe inferences:

1. a branch-set label does not make the retained vertices connected;
2. old model adjacency need not survive after the boundary representative
   is removed; and
3. the pinch entrance paths lie on the shore opposite the one on which
   supports must be contracted to reflect the legal trace.

No palette colour is identified with a branch-set label, and no automatic
common boundary partition is claimed.

The theorem is **GREEN** within its stated scope.
