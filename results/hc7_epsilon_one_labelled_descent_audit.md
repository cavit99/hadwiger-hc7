# Independent audit: excess-one descent with literal boundary data

**Verdict:** **GREEN under the exact stated hypotheses.**  The contractions
used in the order-seven branch are proper minors, the pulled-back boundary
blocks are exact, and a split descended boundary gives either an immediate
contradiction or the same boundary partition on both closed shores.  The
seven-vertex complement argument has exactly the stated exceptional graph
`K_2\vee C_5`.  The order-eight alternative and the placement of all old
labels are literal host-graph statements.  The icosahedral example has the
claimed connectivity and minor exclusion and is scoped only as a barrier to
connectivity-only descent.

**Audited source:**
`results/hc7_epsilon_one_labelled_descent.md`.

**Source SHA-256:**
`6108e6992e1ef069e3a44abac7f0202fbbe38df3659182f091ef416a5475b42f`.

This promoted revision differs from the line-by-line audited source at
`2dae0270401300b50b3856dbe6fc4b63afe66ee5048c77e62eb6efe54e960e4b`
only in its status metadata: “internal audit pending” was replaced by
“adjacent internal audit GREEN.”  The theorem statements, proofs, explicit
construction, and trust boundary are unchanged.  I rechecked that
promotion-only change before repinning this audit.

This audit certifies the displayed conditional theorems.  It does not assert
that every hypothetical counterexample reaches their path-residual setup,
that a nonsplit order-seven boundary synchronizes, or that a boundary-full
order-eight interface closes.  In particular, it does not prove `HC_7`.

## 1. Setup and actual separation

Because `X=N_G(R)`, the connected set `R` is a component of `G-X`.  The
assumed nonempty far side supplies a second component.  If another component
`C` misses `x\in X`, then

\[
 N_G(C)\subseteq X-\{x\}.
\]

This neighbourhood separates `C` from `R`.  Seven-connectivity gives the
reverse order bound, so `N_G(C)=X-\{x\}` and this is an actual order-seven
separation.  No quotient vertex is used in this deduction.

## 2. Proper-minor exact-block construction

Let `Y=N_G(C)` and let `I\subseteq Y` be a nonempty independent set.  Since
`C` is adjacent to every vertex of `Y`, the graph on `C\cup I` is connected
and contains an edge.  Contracting a spanning tree therefore strictly
reduces the vertex count and is a proper minor.  Its representative is
adjacent to every vertex of `Y-I` through `C`.

On pulling a six-colouring back to the opposite closed side:

* all vertices of `I` receive the representative's colour;
* independence of `I` makes the pullback proper inside `I`;
* every edge from `I` to an unchanged vertex was incident with the
  representative after contraction; and
* every boundary vertex in `Y-I` differs from the representative.

Thus `I` is exactly one boundary colour class, not merely a subset of one.
The same argument with `R\cup I` is valid because `R` is also `Y`-full.  It
produces the symmetric exact block on the other closed shore.  Each
contraction changes only the side later discarded, so the two restricted
colourings cover complementary open sides with the same literal boundary.

If `G[Y]` is split as `Y=Q\mathbin{\dot\cup}J`, then `J` is nonempty; otherwise
`Y` itself is a `K_7`.  When `|Q|=6`, contracting `C\cup J` produces a
`K_7` consisting of its representative and the six clique vertices, an
immediate contradiction.  When `|Q|\le5`, exactness of the `J` block and the
clique property force precisely

\[
 J\mid\{q\}\quad(q\in Q)
\]

on both shores.  This uses at most six colours.  A colour permutation aligns
the literal boundary values, and the absence of edges between the open
shores makes the glued colouring proper.

## 3. Seven-vertex exceptional boundary

The critical-subgraph proof of Proposition 2.2 is complete.

* A vertex-critical graph of chromatic number at least six and order at most
  seven contains `K_6`.  At order seven its complement is a matching; the
  sole noncomplete six-chromatic possibility, `K_7-e`, is not
  vertex-critical.
* A five-critical graph cannot have order six.  Its complement would be a
  matching, and the only five-chromatic case is again noncritical.
* If the critical subgraph has order five, the two unused vertices of `H`
  combine with the two nonadjacent join vertices exactly as displayed to
  give seven connected pairwise adjacent branch sets.
* In the remaining order-seven case, for `F=\overline H` one has
  `\Delta(F)\le2`.  A triangle in `F` either combines with a disjoint edge
  to make `H` four-colourable or, with no further edge, contradicts
  five-criticality after a triangle vertex is deleted.  Hence `F` is
  triangle-free.
* For triangle-free `F` of maximum degree two, colour classes of `H` are
  precisely singleton vertices and matched pairs in `F`, giving
  `\chi(H)=7-\nu(F)`.  Five-criticality yields
  `\nu(F)=\nu(F-v)=2` for every vertex `v`.  Paths and even cycles have a
  vertex whose deletion lowers their matching contribution; every
  nontrivial component must therefore be an odd cycle.  Triangle-freeness
  and total matching number two leave exactly
  `F=C_5\mathbin{\dot\cup}2K_1`, so `H=K_2\vee C_5`.

As an independent finite check of the conclusion, an exhaustive scan of the
1,044 unlabelled seven-vertex graphs found, among graphs of chromatic number
at least five, exactly one isomorphism type for which
`\overline K_2\vee H` has no `K_7` minor; its degree sequence is
`4,4,4,4,4,6,6`, hence it is `K_2\vee C_5`.  The written proof above does not
depend on this check.

For sharpness,

\[
 \overline K_2\vee(K_2\vee C_5)
 =K_2\vee(\overline K_2\vee C_5).
\]

The graph in parentheses is the planar pentagonal bipyramid.  Any `K_7`
model in the join would leave at least five pairwise adjacent connected
branch sets wholly in that planar graph after discarding branch sets meeting
the outer `K_2`, giving an impossible `K_5` minor.  Contracting the two
nonadjacent boundary-full connected subgraphs in Theorem 2.1 really does
give `\overline K_2\vee G[Y]`, so the classification applies to the literal
descended boundary.

## 4. Boundary-full order-eight alternative

For every component of `G-X`, its whole neighbourhood is a subset of the
eight-set `X` and separates it from another component.  Hence the
neighbourhood has order seven or eight.  This proves the exhaustive and
mutually exclusive alternative: an order-seven full neighbourhood, or every
component is `X`-full.

In the latter case, if `Q\subseteq X` is a clique and `m+|Q|\ge7`, there are
enough distinct components and distinct anchors in `X-Q` to form the branch
sets

\[
 C_i\cup\{x_i\},\qquad \{q\}\ (q\in Q).
\]

Fullness supplies every cross-adjacency, while the singleton branch sets
from `Q` are pairwise adjacent.  Thus the packing inequality
`m+|Q|\le6` is valid.

## 5. Literal placement of the old labels

In the path-residual application,

\[
 X=N_G(R)=(S-\Lambda)\mathbin{\dot\cup}U
\]

is an identity of literal vertex sets, and excess one gives
`|U|=|\Lambda|+1`.  Every component of the opposite open side `B` has
neighbourhood contained in the seven-set `S`; seven-connectivity forces that
neighbourhood to equal `S`.  Since `\Lambda` is nonempty, `B\cup\Lambda` is
connected, is disjoint from `X`, and therefore lies in one component `F` of
`G-X`.  Outcome 2 makes both `R` and `F` adjacent to all eight literal
boundary vertices.

The statements about `C_2` are also exact: because `C_2` lies in the old
open side, `C_2\cap X=C_2\cap U`; and a component of `C_2-X` adjacent to a
lost label in `\Lambda\subseteq F` belongs to the same component `F`.  The
parallel first-entry statement follows from
`N_G(K)=T_K\mathbin{\dot\cup}A_K` by the identical argument.  These facts
locate labels which move into the far component; they do not claim that all
seven old labels remain boundary vertices or that an old equality partition
is preserved.

## 6. Icosahedral sharpness example

The explicit thirty-edge list defines the convention used in Proposition
4.1.  Direct inspection gives:

* `I[S_0]` is the displayed induced six-cycle;
* `I-S_0` has exactly the connected components `R=\{5,6\}` and
  `F=\{7,8,9,10\}`;
* both components are adjacent to all six vertices of `S_0`; and
* `X=S_0\cup\{a,b\}=N_G(R)` and both components of `G-X` are `X`-full.

The join is seven-connected: with one join vertex present all remaining
icosahedral vertices are connected through it; after both are deleted,
fewer than five additional deletions leave the five-connected icosahedron
connected.  Deleting both join vertices and the five neighbours of an
icosahedral vertex gives the matching upper bound on connectivity.

Finally, at most two branch sets of a hypothetical `K_7` model can contain
the join vertices.  Five branch sets would remain entirely in the planar
icosahedron and form a `K_5` minor, a contradiction.  The example is
five-colourable, is not a hypothetical counterexample, and lacks the hard
labelled first-entry data.  It refutes only a strict-descent principle based
on seven-connectivity and `K_7`-minor exclusion alone.

## 7. Trust boundary

The source deliberately leaves two cases open: nonsplit descended
order-seven boundaries and decorated boundary-full order-eight interfaces.
It also correctly warns that an arbitrary seven-path linkage need not carry
the old three- and two-vertex independent blocks to independent sets.  The
GREEN verdict does not promote any such label-preserving transfer.
