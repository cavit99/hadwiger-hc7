# Both-missing normalization: one twin is a `2+1+2` portal path

## Status

In the exact branch left by the endpoint-shadow exchange, the deficient
bag `A` is a nontrivial induced path and is anticomplete to both twins
`B,C`; every exterior component meeting `A` also avoids `B,C`.  This note
gives a second uniform normalization.  After fixing `A` and minimizing
one twin bag, say `B`, the graph induced by `B` is itself a path.  At
least two of its five required row labels occur only at each endpoint,
and at most one row label remains between them.

Thus the both-missing residue contains two anticomplete normalized paths,
not an arbitrary complex twin.  This does not yet produce the three full
shores required for `K_7`.

## 1. Fixed both-missing model

Let

\[
                       A,B,C,U_1,U_2,U_3,U_4             \tag{1.1}
\]

be a labelled, not necessarily spanning, `K_7^vee` model.  The six
foreign bags form a clique model; the only unprescribed pairs are `AB`
and `AC`.  Assume these pairs are genuinely absent and that the vertex
set and normalized path structure of `A` are fixed.

Among all such models with this fixed bag `A`, choose one minimizing
`|B|`.  The comparison class permits deletion of unused vertices and
enlargement of any bag other than `A`, but must preserve both absent
pairs `AB,AC`.

The five required neighbours of `B` are

\[
                         \mathcal R=\{C,U_1,U_2,U_3,U_4\}. \tag{1.2}
\]

For a nonempty proper `X subset B`, call `X` detachable if `G[X]` and
`G[B-X]` are connected, and put

\[
 \Omega_B(X)=\{R\in\mathcal R:
   \text{every `B-R` model edge has its `B`-end in `X`}\}. \tag{1.3}
\]

## Lemma 1 (every detachable part owns two rows)

Every detachable `X subset B` satisfies

\[
                              |\Omega_B(X)|\ge2.          \tag{1.4}
\]

### Proof

If `Omega_B(X)` is empty, replace `B` by `B-X` and omit `X`.  Every
required model adjacency survives, both missing pairs involving `A`
remain absent, and `|B|` decreases.

Suppose `Omega_B(X)={R}`.  Replace

\[
                 B\longmapsto B-X,\qquad R\longmapsto R\cup X.
                                                               \tag{1.5}
\]

The enlarged target is connected through an old `X-R` edge.  The cut
edge between `X` and `B-X` restores the `B-R` model adjacency.  The
residual `B-X` retains every other required row, and the enlarged target
retains all its old model edges.

The fixed missing pair `A(B-X)` remains absent.  If `R=C`, then `A` is
also anticomplete to `X subseteq B`, so enlarging `C` by `X` preserves
the second missing pair `AC`.  If `R=U_i`, the bag `C` is unchanged.
Thus (1.5) stays in the comparison class and decreases `|B|`, a
contradiction.  \(\square\)

## Theorem 2 (the minimized twin is an induced path)

Either `B` is a singleton or `G[B]` is an induced path.

### Proof

Fix a spanning tree `T` of `G[B]`.  Every leaf singleton of `T` is
detachable: deleting it leaves the connected tree `T-x`.  Monopoly sets
of distinct detachable singletons are disjoint, because the nonempty set
of all `B`-ends of the edges to one row cannot be contained in two
disjoint sets.  Lemma 1 gives at least two row labels to every leaf, while
only five labels occur in (1.2).  Hence `T` has at most two leaves.  If
`|B|>=2`, every tree has at least two leaves, so every spanning tree of
`G[B]` is a path.

If `G[B]` had a vertex of degree at least three, three incident edges
could be extended from a forest to a spanning tree in which that vertex
still has degree at least three, a contradiction.  Thus `G[B]` has
maximum degree at most two and, being connected, is a path or a cycle.

A cycle is impossible.  Every singleton vertex of a cycle is detachable,
and three distinct vertices would have disjoint monopoly sets of order at
least two, requiring at least six labels.  Therefore `G[B]` is a path.
Since this is the induced subgraph on the bag, the path is induced in
`G`.  \(\square\)

## Theorem 3 (exact endpoint ownership)

Write a nonsingleton minimized twin as

\[
                              B=b_0b_1\cdots b_n.         \tag{3.1}
\]

There are disjoint sets `mathcal R_0,mathcal R_1 subseteq mathcal R`
such that

\[
       |\mathcal R_0|\ge2,\qquad |\mathcal R_1|\ge2,      \tag{3.2}
\]

and, for every row `R`, if

\[
                 P_R=\{b\in B:E(b,R)\ne\varnothing\},    \tag{3.3}
\]

then

\[
 P_R=\{b_0\}\quad(R\in\mathcal R_0),\qquad
 P_R=\{b_n\}\quad(R\in\mathcal R_1).                    \tag{3.4}
\]

At most one row of `mathcal R` lies outside
`mathcal R_0 union mathcal R_1`.  Moreover, across every edge cut of
the path, at most one of the five portal sets in (3.3) meets both sides.

### Proof

The endpoint singletons are detachable.  Put

\[
       \mathcal R_0=\Omega_B(\{b_0\}),\qquad
       \mathcal R_1=\Omega_B(\{b_n\}).
\]

Lemma 1 gives (3.2), and the two monopoly sets are disjoint.  Membership
in `Omega_B({b_i})` says that every `B-R` edge has its `B`-end at `b_i`;
nonemptiness of each model row then gives (3.4).  Since there are five
rows in total, at most one remains.

For the last assertion, split the path at any edge into connected sides
`X,Y`.  Both are detachable, so their disjoint monopoly sets have order
at least two each.  A row whose portal set meets both sides belongs to
neither monopoly set.  Four of the five labels are already consumed by
the two disjoint monopoly sets, leaving at most one crossing row.
\(\square\)

Equivalently, no path edge lies in the first-to-last portal spans of two
different rows.  Singleton spans in one endpoint bundle may of course
share that endpoint.  At least four rows are locked in the two endpoint
bundles, while at most one row can have a nontrivial span.

## 4. Consequence for the exact branch

Combine this theorem with the independently audited endpoint-shadow
exchange.  Every nontrivial deficient-minimal path has both twins absent,
and every path-meeting exterior lobe avoids both twins.  Fixing that path
and minimizing one twin yields the following literal frame:

* `A` is an induced `2+2` portal path on the four neutral rows;
* `B` is an anticomplete induced `2+(at most 1)+2` portal path on
  `C,U_1,U_2,U_3,U_4`; and
* the six foreign bags still form the old clique model.

This is an unbounded crossed-frame society, but it has only one mobile row
on the second path.  A successful next theorem must use the proper-minor
states of the two actual paths to do one of three things:

1. split one foreign path label-faithfully and obtain `K_7`;
2. match equality partitions across the full adhesion and six-colour; or
3. embed both path societies with one common pair of actual apex vertices.

Static endpoint movement alone cannot shorten `A`: it would create a
third absent spoke.  The result therefore does not claim closure of the
both-missing branch.
