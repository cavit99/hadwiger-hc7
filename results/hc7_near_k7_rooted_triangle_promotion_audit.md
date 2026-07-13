# Independent audit: uniform rooted row promotion

## Verdict

**GREEN after the incorporated Hall-scope and helper clarifications.**
The rewritten absorption theorem is simpler and strictly stronger than
the former median-tree construction.  Its `p+s` branch sets, simultaneous
carrier absorption, path-side application and Hall reduction are exact.

## 1. Uniform absorption theorem

The proposed branch sets are

\[
 R_1,\ldots,R_p,
 F'_1=F_1\cup K_1,\ldots,F'_s=F_s\cup K_s.
\]

There are exactly `p+s` of them.  Every `F'_i` is connected through a
literal `F_i-K_i` edge.  Pairwise root disjointness and pairwise carrier
disjointness, together with carrier-root disjointness, make all displayed
branch sets disjoint.

Their clique adjacencies are also literal:

* the `R_j` retain every old `R_jR_k` edge;
* `F'_i,F'_h` retain an old `F_iF_h` edge;
* `F'_i` sees every `R_j` through an edge from `K_i` to `R_j`.

No edge between different carriers is required.  Absorbing an entire
carrier into its matched row preserves all old vertices and adjacencies
of that row and leaves every unselected carrier untouched.

Corollary 2 is the case `p=2,s=1`: `X,Y` remain unchanged and the row
becomes `Z union K`.  This handles coincident portal locations and
cutvertices automatically because no internal split of `K` is made.

## 2. Path-side application

For a crossing path piece `K`, the two path sides `L,R` are disjoint
connected adjacent roots and `K` has a literal edge to each.  If `K`
also meets the foreign row `Q`, replacing `Q` by `Q union K` makes that
single connected row adjacent to both unchanged shores.  The old
path-cut edge still joins the shores, and all old foreign-row
adjacencies survive because the enlarged row still contains `Q`.

To compose other helpers, preserving their contacts is insufficient by
itself.  The corrected statement requires mutually disjoint helper
families outside `K` with every helper piece already attached to its
assigned path side.  Adjoining those pieces then preserves shore
connectedness, disjointness and all literal row contacts needed by the
shore-completion theorem.

## 3. Hall certificate

Corollary 4 now explicitly inherits the complete root setting of
Theorem 1: the `R_j` and `F_i` are disjoint connected clique families,
and every candidate carrier is disjoint from all roots and adjacent to
every `R_j`.  A row-saturating matching selects distinct carriers, one
incident with each `F_i`; these are exactly the hypotheses of Theorem 1,
so they give a `K_{p+s}` model.

If no such matching exists, Hall's theorem gives a nonempty row set `S`
with `|N(S)|<|S|`.  In the one-missing `HC_7` path state, `p=2,s=5`, so
the model has exactly seven bags.  The Hall neighbourhood counts whole
carrier pieces, not vertices, and no ambient separator follows merely
from the inequality.

## 4. Minimal Hall deficiency

Let `S` be inclusion-minimal deficient.  Every proper subset `T` obeys
Hall's inequality.  For each `Q in S`, Hall therefore matches `S-{Q}`
into `N(S)`, proving `|N(S)|>=|S|-1`; deficiency gives equality.  The
matching is consequently a bijection from `S-{Q}` onto `N(S)`.

If `|S|>=2`, minimality makes the singleton `{Q}` nondeficient, so
`N(Q)` is nonempty.  For any chosen `K in N(Q)`, the bijection assigns
that same carrier to some `H in S-{Q}`.  Thus, relative to the
near-perfect assignment, `K` supports both the matched row `H` and the
unmatched row `Q`, while every other matched row has its own distinct
assigned carrier.  This is exactly a two-row assignment collision.  It
does **not** say that `K` has incidence degree two or that `H,Q` have
unique support; the corrected source makes that quantifier boundary
explicit.

If `|S|=1`, deficiency says its neighbourhood is empty, so the sole row
has no crossing carrier at that cut.

## 5. Exact limitation

Whole-carrier absorption promotes one row only.  The ordered path

\[
 L\text{-attachment},\ Q\text{-portal},\
 R\text{-attachment},\ H\text{-portal}
\]

has no disjoint `L-H` and `R-Q` paths, so a carrier simultaneously needed
for those two directional duties cannot be resolved by choosing which
row absorbs it.  The remaining theorem must address that fixed two-path
linkage or return a coherent web.  No portal multiplicity, cutvertex
peel, decreasing recursion or global rural conclusion is proved here.
