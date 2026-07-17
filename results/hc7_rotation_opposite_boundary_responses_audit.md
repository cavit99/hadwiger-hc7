# Audit of oppositely oriented boundary-colouring responses

**Verdict:** GREEN for the exact source revision identified below.

This is a separate internal mathematical audit.  It verifies the conditional
boundary-colouring statements in the source note; it is not external peer
review and it does not prove that the two response languages intersect.

## Audited revision

The audited file is
`results/hc7_rotation_opposite_boundary_responses.md`.

**Source SHA-256:**
`54ea0c2223982b6f1a3d980e6f0042275b0a783b9ca1e3615efc309a18f638c8`.

The promoted source has SHA-256
`ce7c762b58ca4e109d31d8baa07b11ac73b5349439f4dd9b7f60d8f26ec0af0c`.
It differs from the audited revision only in the opening status line,
which records this GREEN verdict; no theorem statement, proof, dependency,
or scope claim changed.

## 1. Derivation from the connected-subgraph trichotomy

In the mutually unavoidable branch of the connected
one-missing-adjacency trichotomy, the selected detachable side is either
`Z_s` or `Z_r`.  Interchanging the names `r,s` when necessary makes it
`Z_s`.  The residual set `W` is then exactly the component of `G[U-s]`
containing `r`, while `Z=U-W` is the connected opposite side supplied by
Lemma 1.2 of the trichotomy.  The near-complete-model outcome assumes this
chosen side meets `R` and has a nonempty lost-label set `Omega`.  Thus the
setup in Section 1 is precisely a conditional instance of that construction;
it does not add an unproved conclusion.

The seven displayed sets in (1.6) have exactly the stated possible missing
adjacencies.  The set `A union Z` is connected because `Z` contains the
selected neighbour `s` of `A`; it meets every fixed branch set through `A`
and meets `R` through `Z`.  The set `W` meets `A union Z` across the donor
split.  For a fixed branch set `H`, it loses its old `U-H` adjacency exactly
when the whole portal set `P_H` lies in `Z`, which is exactly
`H in Omega`.

## 2. The one-vertex donor interface

Since `W` is a component of the induced graph `G[U-s]`, it has no edge in
`G[U-s]` to another component.  Every edge from `W` to `U-W` therefore ends
at `s`.  Connectedness of `G[U]`, together with `s notin W`, forces at least
one such edge.  Hence

\[
                         N_U(W)=\{s\}.
\]

The contacts with `A` follow directly from `r,s in N_G(A)`, and the selected
edge `sw` exists.  This proves Lemma 2.1.  The source correctly calls `s` a
unique **donor-side attachment vertex**; it does not claim that `s` is a
cutvertex of `G` or of the closed shore.

For `S=N_G(W)`, the induced subgraphs
`C=G[W union S]` and `O=G-W` cover every vertex and edge of `G`, intersect
in `G[S]`, and have no edge between their open sides.  Thus they form a
separation.  Its `W`-side is nonempty.

If `H in Omega`, the old `K_6` model supplies an edge `t_H f_H` from `U` to
`H`, and every possible `U`-end of such an edge lies in `Z`.  Moreover `W`
is anticomplete to `H`, so `f_H` lies outside both `W` and `S=N_G(W)`.  It
therefore witnesses a nonempty opposite open side.  Both ends of
`t_H f_H` lie in `O`.  Since `f_H` lies outside `W union S`, this edge is not
in the induced subgraph `C`, including in the case `t_H=s`.  Finally,
`S intersect Z=\{s\}` follows from `S intersect U=N_U(W)=\{s\}`.  All claims
of Lemma 2.2 are valid.

## 3. The two set-difference inclusions

Every displayed edge deletion is a proper minor, so minor-criticality makes
its response language nonempty.

For a six-colouring of `G-sw`, the closed graph `O` is unchanged because it
does not contain `w`.  Its boundary partition therefore lies in
`Ext(O,S)`.  If it also extended to the unmodified `C`, equality of the
labelled boundary partitions would give a bijection between the colours
used on `S`; this bijection extends to a permutation of all six colour
names.  After applying that permutation, the two shore colourings agree
literally on `S` and glue to a six-colouring of `G`.  Hence the partition is
not in `Ext(C,S)`.

For a six-colouring of `G-t_Hf_H`, the graph `C` is unchanged because the
deleted edge is not in `C`.  The same colour-alignment argument shows that
its boundary partition lies in `Ext(C,S)` but not in `Ext(O,S)`.  This proves
both inclusions in (3.1), with no assumption that the boundary uses all six
colours: the bijection between its used colours extends arbitrarily to a
permutation of the unused names.

If a deleted edge had differently coloured ends, restoring it would preserve
properness and six-colour `G`.  Thus its ends have a common colour in every
deletion colouring.  Colourings of `G-e` with equal endpoint colours are in
canonical bijection with colourings of `G/e`.  For `sw`, exactly the endpoint
`s` lies in `S`; for `t_Hf_H`, the endpoint `f_H` is outside `S` and `t_H`
is either `s` or outside `S`.  Consequently at most one endpoint is a
boundary vertex, and retaining its contracted image preserves every literal
boundary label.  The deletion and contraction response languages in (3.2)
are therefore exactly equal.

The two response languages occupy opposite set differences, so their
intersection is empty.  Conversely, a forced common partition would glue an
unmodified colouring of `C` from the far-edge response to an unmodified
colouring of `O` from the donor-interface response, proving Corollary 3.2.

## 4. Colour-restricted paths

For either deleted edge, if its equal-coloured endpoints were in different
components of the subgraph on their common colour and another colour, a
Kempe interchange on one component would give them different colours.  The
edge could then be restored, contradicting the non-six-colourability of
`G`.  Thus all five asserted bichromatic connections exist.

For `sw`, a path from `w in W` to `s notin W` has a first vertex outside
`W`; that vertex belongs to `N_G(W)=S`, and every earlier internal vertex is
in `W`.  The five entrances need not be distinct, and the source does not
claim that they are.  Corollary 3.3 is correct.

## 5. Trust boundary

The audited source proves only the following host-level addition to the
connected-subgraph trichotomy: every mutually unavoidable rotation outcome
has a boundary on which the donor-interface edge and every newly lost
foreign contact edge produce nonempty, oppositely oriented deletion and
contraction response languages, together with five colour-restricted paths
for each response.

It does **not** prove that opposite response languages intersect, that their
Kempe paths are disjoint or aligned with branch-set labels, that the boundary
has order seven, that a common equality partition exists, or that the
rotation is a valid well-founded descent.  No unresolved assumption remains
inside Lemmas 2.1--2.2, Theorem 3.1, or Corollaries 3.2--3.3 at the audited
source hash.
