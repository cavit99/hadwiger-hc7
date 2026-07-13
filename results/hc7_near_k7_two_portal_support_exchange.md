# Two-portal support exchange

## Status

This is a protected portal-peel lemma for the bounded carrier bottleneck
in `../results/hc7_near_k7_literal_shore_completion.md`.  It closes the
subfamily in which a crossing support has four distinct terminals as in
(1.1), is two-connected, and has two protected literal portals to the
concentrated row.  Its failure
returns an exact cutvertex obstruction inside the support.  That
cutvertex is not asserted to be a small separator of the whole host.

## Setting

Let `P` have a fixed cut into nonempty connected path sides `L,R`, with
an `LR` edge.  Let `Q` be a connected foreign row disjoint from `P`.
Let `K` be a connected old exterior piece, disjoint from `P`, `Q`, and
all other foreign bags.

Choose four distinct vertices

\[
                         l,r,x,y\in V(K)                 \tag{1.1}
\]

such that `l` has a neighbour in `L`, `r` has a neighbour in `R`, and
`x,y` each have a neighbour in `Q`.  Call `(l,r)` the side terminals and
`(x,y)` the protected `Q`-portals.

### Theorem 1 (protected two-portal exchange)

Exactly one of the following assertions holds.

1. There are two vertex-disjoint paths in `K` linking the set `{l,r}`
   to the set `{x,y}` and using both vertices of each set.
2. There is a vertex `z in V(K)` such that `K-z` contains no path from
   `{l,r}-{z}` to `{x,y}-{z}`.  Thus `z` separates the two terminal sets
   in the order-two set-linkage problem.

In outcome 1, let `P_L` be the path beginning at `l` and `P_R` the path
beginning at `r` (the pairing with `x,y` is immaterial).  Then

\[
                         L^+=L\cup P_L,qquad
                         R^+=R\cup P_R                 \tag{1.2}
\]

are disjoint connected shores, are adjacent through the old `LR` edge,
and are each adjacent to the unchanged connected row `Q`.

Moreover the exchange is protected: it uses no vertex of any foreign
bag.  Hence any pairwise disjoint families of other old exterior pieces
already assigned to the two shores remain disjoint from (1.2), and all
their literal row contacts survive.

The same construction duplicates an entire row profile: if both `x`
and `y` have a neighbour in every member of a family of foreign rows
`mathcal Q`, then both shores in (1.2) are adjacent to every row in
`mathcal Q`.

#### Proof

Apply the vertex form of Menger's theorem to the two disjoint terminal
sets `{l,r}` and `{x,y}` inside `K`, in the convention in which a
separator `Z` may meet the terminal sets and separation means that
`K-Z` has no path from `{l,r}-Z` to `{x,y}-Z`.  Either there are two
disjoint set-to-set paths saturating both two-element terminal sets, or a
vertex set of order at most one separates them.  The empty separator would say
that the connected graph `K` has no path between the nonempty terminal
sets, which is impossible.  Thus failure gives one vertex `z`, proving
the dichotomy.

In the linkage outcome, name the path incident with `l` by `P_L` and
the other by `P_R`.  The paths are disjoint.  The edge from `l` to `L`
and the connectedness of `L` make `L^+` connected; similarly `R^+` is
connected.  The two shores are disjoint because `L,R` and the two paths
are pairwise disjoint.  Their old path-cut edge remains, so they are
adjacent.  Each linkage path ends at a different member of `{x,y}`, and
each such vertex has a literal edge to `Q`; consequently both shores
see the same unchanged row `Q`.  If the two portals share the larger
profile `mathcal Q`, the identical argument applies row by row.

If a one-vertex separator existed in the linkage outcome, at most one of
the two disjoint paths would meet it; the other path, including both of
its distinct terminal ends, would survive.  Thus the two displayed
outcomes are mutually exclusive as well as exhaustive.

All vertices used outside `P` lie in `K`.  Since an old exterior piece
is disjoint from every foreign bag and from every other old exterior
piece, the asserted protection and preservation are immediate.
\(\square\)

### Corollary 2 (two-connected support closure)

Under (1.1), if `K` is two-connected, outcome 1 of Theorem 1 holds.
Consequently, whenever the other literal deficit rows are covered by
two mutually disjoint helper families outside `K`, each family already
attached to its assigned path side and disjoint from `K`, adjoining those
families to the two shores preserves connectedness and supplies the
corresponding row-duplication requirement.  If all five rows of
the one-missing branch are thereby covered, Lemma 1 of
`../results/hc7_near_k7_literal_shore_completion.md` gives a literal
`K_7` model.

#### Proof

No single vertex separates two disjoint two-element terminal sets in a
two-connected graph.  Theorem 1 therefore gives the linkage.  The last
assertion is exactly the protected-composition clause of Theorem 1
followed by literal shore completion. \(\square\)

### Theorem 3 (flexible attachments and the exact portal arm)

Put

\[
 A_L=N_K(L),\qquad A_R=N_K(R),\qquad X_Q=N_K(Q),          \tag{1.3}
\]

where, for example, `N_K(L)` denotes the vertices of `K` having a
neighbour in `L`.  Assume `A_L,A_R` are nonempty and `|X_Q|>=2`.
Then either

1. there are disjoint paths in `K`, one joining `A_L` to `X_Q` and one
   joining `A_R` to a different vertex of `X_Q`; or
2. there is one vertex `z in K` such that in `K-z` no component meeting
   `X_Q-{z}` contains a vertex of `(A_L union A_R)-{z}`.

In outcome 1 the two paths give the protected row duplication exactly
as in Theorem 1.  In outcome 2 every `Q`-portal lobe behind `z` has no
attachment to either path side.  More precisely, either `z` is a
cutvertex separating such a portal arm, or
`A_L union A_R subseteq {z}`.  The latter is the degenerate side-gate
case in which every attachment to both path sides is concentrated at one
vertex; it need not make `z` a cutvertex of `K`.

#### Proof

Add two new vertices `lambda,rho` to `K`, joining `lambda` to every
member of `A_L` and `rho` to every member of `A_R`.  Apply set-Menger
between the two-element source set `{lambda,rho}` and the target set
`X_Q`.

Two disjoint source-to-target paths necessarily use both source
vertices and two distinct target vertices.  Deleting `lambda,rho` from
them gives outcome 1.  Otherwise a separator of order at most one meets
every source-to-`X_Q` path.  The augmented graph contains at least one
such path and is connected through `K`, so the separator is nonempty.
It cannot be `lambda`: after deleting `lambda`, the vertex `rho` still
has a path through connected `K` from a member of the nonempty set
`A_R` to the nonempty set `X_Q`.  Symmetrically it cannot be `rho`.
Hence it is one vertex `z in K`.

The absence in the augmented graph minus `z` of a source-to-target path
is precisely the component statement in outcome 2.  The linkage-to-
shore construction and its protection are the same as in Theorem 1.
Since `|X_Q|>=2`, the set `X_Q-{z}` is nonempty.  If `K-z` is connected,
the component statement therefore forces
`(A_L union A_R)-{z}` to be empty.  Otherwise `z` is a cutvertex and
every component containing a surviving `Q` portal contains no path-side
attachment.  This proves the asserted refined alternative.
\(\square\)

## Exact residual

In a target-free graph, a support with four distinct terminals as in
Theorem 1 must therefore have a cutvertex `z` separating the two terminal
sets.  In the flexible-attachment form, failure returns either such a
cutvertex portal arm or the exact degenerate gate
`A_L union A_R subseteq {z}`.  The next recursion must treat that
one-vertex side concentration explicitly rather than silently calling it
a block-cut arm.

This is only an **internal** one-vertex adhesion.  A component of
`K-z` may have additional edges to `P` or to foreign rows, so `{z}` is
not necessarily a separator of `G`.  A valid continuation must either
use those additional contacts to perform another protected exchange, or
show that all of them occur in one rural society with the already fixed
global exceptional roles.  Replacing `K` by a quotient vertex would
lose precisely this information.

### Strict descent and its sharp terminal gate

In outcome 2 of Theorem 3, let `K_Q` be `z` together with every
component of `K-z` which contains a vertex of `X_Q-{z}`.  Then `K_Q` is
connected and contains every protected `Q` portal.  It has no path-side
attachment outside `z`.  If `K` has any path-side attachment outside
`z`, then `K_Q` is a proper subgraph of `K`; replacing the support by
this portal core strictly decreases its vertex order.

The descent is sharp.  It can stop with

\[
                         A_L\cup A_R=\{z\}.              \tag{1.4}
\]

For example, take a tree consisting of a gate `z`, an arbitrarily long
arm, and two terminal leaves `x,y`; attach both path sides only at `z`
and attach both `x,y` to `Q`.  The vertex `z` separates every side
attachment from both protected portals, `K_Q=K`, and no two protected
shore arms exist.  If the terminal arm also owns all contacts to a
second foreign row, transferring it into `Q` loses that second literal
role.  Subdividing the constant two-owner arm gives the same obstruction
at arbitrary length.

This portal tree is a counterexample to an ownership-only claim that the
recursion must always decrease.  It is not asserted by itself to be a
seven-connected contraction-critical host.  In the actual host, high
connectivity may be maintained by many contacts from the arm into the
foreign rows, so the internal gate `z` still need not be an ambient small
cut.  Eliminating (1.4) requires the proper-minor state transition or a
global rural expansion; it cannot be obtained from set-Menger and
lexicographic ownership alone.
