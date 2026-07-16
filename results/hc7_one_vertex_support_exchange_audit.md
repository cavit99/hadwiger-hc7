# Independent audit: one-vertex support exchange

**Verdict:** GREEN.

**Audited source:**
`results/hc7_one_vertex_support_exchange.md`.

**Source SHA-256:**
`d2a9410cdd33b3a6a6b6544303f8709faa70e29da5bb0029c38832445787ef1f`.

After the mathematical audit, the source was moved from `active/` to
`results/` and only its status and adjacent-audit link were updated.  The
hash above binds the audit to that exact promoted revision; the audited
mathematical content is unchanged.

This audit checks Theorems 1.1 and 2.1 and Corollary 3.1, including the
strengthened equality `tau(H)=2` and the canonical exchange core.  The
arguments are finite set-system arguments once the small `K_5`-model
supports have been supplied.  No computational claim is used.

## 1. The exact transversal number of the deleted family

Put

\[
 \mathcal H=\mathcal F_5(G)\cup(\mathcal C-\{A\}).
\]

Inclusion-minimality of `C` gives `tau(H)<=2`.  If `H` had a transversal
`R` of order at most one, then either `R` met `A`, in which case it already
transversed `H union {A}`, or it avoided `A`, in which case adjoining one
vertex of `A` would give a transversal of `H union {A}` of order at most
two.  Both outcomes contradict

\[
             \tau(\mathcal F_5(G)\cup\mathcal C)>2.
\]

Hence `tau(H)=2` exactly.  In particular, the family `T(H)` of two-vertex
transversals used in Theorem 2.1 is nonempty, and every transversal of
`H` of order at most two belongs to `T(H)`.  No enlargement of a
one-vertex transversal is hidden in the canonical-core argument.

## 2. The one-vertex dichotomy

If `tau(H union {A'})>2`, finiteness permits an inclusion-minimal
subfamily `C'` of `(C-{A}) union {A'}` witnessing this inequality.  It
must contain `A'`: otherwise `F_5(G) union C'` is a subfamily of `H`, whose
transversal number is two.  This proves alternative 1 exactly.

If instead `tau(H union {A'})<=2`, choose a transversal `R_0` of order at
most two.  Since it is also a transversal of `H`, Section 1 gives
`|R_0|=2`.  It cannot meet `A`, because then it would meet all of
`H union {A}`.  It must meet `A'`; using

\[
                     A-A'=\{y\},\qquad A'-A=\{w\},
\]

this forces `w in R_0`.  Thus `R=R_0` has every property in (1.6), with
no choice of an auxiliary enlargement vertex.

Because `R` meets every member of `F_5(G)`, the graph `G-R` has no
five-vertex `K_5` model, and `mu_G(R)>=6`.  The support `A` is disjoint
from `R` and supplies a six-vertex model in `G-R`, so `mu_G(R)=6`.
Finally, `tau(F_6(G))>2` says that every two-set misses some support in
`F_6(G)`, whence `mu_G(P)<=6` for every pair `P`.  Therefore `R` is
globally maximizing, as claimed.

For the final assertion of Theorem 1.1, the relation
`A' subseteq A union {w}` shows that a pair avoiding `A union {w}` also
avoids `A'`.  Its transversal property for `H` is unchanged.  Meeting
`F_5(G)` gives support height at least six, while the surviving support
`A'` gives height at most six.  Thus the same pair remains private and
globally support-maximal after rebasing.

## 3. The canonical exchange core

Define

\[
 Z_{\mathcal H}=V(G)-\bigcup_{R\in\mathcal T(\mathcal H)}R.
\]

Every `R in T(H)` avoids `A`; otherwise it would be a two-vertex
transversal of `H union {A}`.  Hence `A subseteq Z_H`.

Suppose a five-set `K subseteq Z_H` induced a literal `K_5`.  Then
`K in F_5(G) subseteq H`, so every member of `T(H)` must meet `K`.  But
the definition of `Z_H` makes every member of `T(H)` disjoint from `K`, a
contradiction.  Therefore `G[Z_H]` contains no literal `K_5`.

Let `A' subseteq Z_H` be any six-vertex `K_5`-model support.  Every
transversal of `H` of order at most two is a member of `T(H)` and hence
avoids all of `Z_H`, including `A'`.  Thus no such set transverses
`H union {A'}`, and

\[
                         \tau(\mathcal H\cup\{A'\})>2.
\]

Choosing an inclusion-minimal witness inside `(C-{A}) union {A'}` gives
the stated legal rebasing, and the same argument as in Section 2 forces
that witness to contain `A'`.  Every pair in `T(H)` continues to meet all
of `H` while avoiding `A'`, so every one remains a private transversal.

Conversely, if `w notin Z_H`, its definition supplies a pair
`R in T(H)` containing `w`.  The inclusion `A subseteq Z_H` makes `R`
disjoint from `A`.  The support-height argument of Section 2 gives

\[
                     \mu_G(R)=6=\max_{|P|=2}\mu_G(P).
\]

This verifies all four items of Theorem 2.1.  In particular, the theorem
does not infer a literal `K_5` from a six-vertex model and does not confuse
membership in a transversal with adjacency in the host graph.

## 4. The length-two replacement

For the `3+1` support, `Q={a_0,a_1,a_2,a_3}` is a clique,
`a_3w,wx` are edges, and `x` is adjacent to `a_0,a_1,a_2`.  Therefore

\[
 \{a_0\},\{a_1\},\{a_2\},\{a_3\},\{w,x\}
\]

are five disjoint pairwise adjacent connected branch sets.  Likewise,
`a_0,a_1,a_2,x` form a clique and the connected set `{a_3,w}` is adjacent
to all four, proving the second labelled model.  Since `w` lies outside
the original support,

\[
                         A-A'=\{y\},\qquad A'-A=\{w\},
\]

so Theorem 1.1 applies exactly.  Corollary 3.1 does not assert that the
replacement preserves any external linkage that has not been named.

## 5. Exact scope

The source proves a genuine stable exchange region: every exact-six
support contained in `Z_H` can replace `A` while preserving every
two-vertex transversal of `H`, and every first vertex outside `Z_H`
already belongs to a globally support-maximal private pair.

It does not prove that:

- repeated replacements inside `Z_H` terminate;
- `G[Z_H]` is planar or has bounded treewidth;
- a private pair containing an outside vertex preserves a selected
  six-linkage, nonadjacency, or labelled minor model;
- every repaired contact has only one internal vertex; or
- the support-six transversal theorem or `HC_7` follows.

The source states these limitations accurately.
