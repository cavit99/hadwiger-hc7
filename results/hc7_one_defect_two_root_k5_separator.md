# A one-defect two-root `K_5` model gives a full-neighbourhood separation

**Status:** written proof; [separately audited GREEN](hc7_one_defect_two_root_k5_separator_audit.md).

This note weakens the root alignment required from a `K_5` model.  It
combines a spanning normalization with the tree-splitting argument behind
the audited two-mark branch-set split theorem, extended here from a
singleton centre to an arbitrary connected root branch set.  The returned
separation is genuine, but its order is not bounded above and its two shore
colourings are not synchronized.

## Theorem 1 (spanning a `K_7` model with one missing adjacency)

Let `G` be connected.  Suppose it contains pairwise disjoint connected
subgraphs

\[
                 C,D,U_1,U_2,U_3,U_4,U_5
\]

such that these seven sets are pairwise adjacent except possibly for
`C,D`.  Then either `G` contains a `K_7` minor or it has a spanning model of
the same form.

### Proof

Assume that `G` has no `K_7` minor.  Among all models of the displayed form,
choose one maximizing the number of covered vertices.  The pair `C,D` is
then anticomplete, since an edge between them would complete the model.

Suppose `K` is a component outside the seven branch sets, and let
`I_K` be the subfamily of branch sets having a neighbour in `K`.  This
family is nonempty because `G` is connected.

If both `C` and `D` lie in `I_K`, connectedness of `K` gives a `C`--`D`
path whose internal vertices lie in `K`.  Adding its internal vertices to
`D` makes `D` adjacent to `C` without losing any old adjacency, producing
a `K_7` model.  Hence this does not occur.

The only nonadjacent pair among the seven branch sets is `C,D`.  It follows
that `I_K` is a clique in their contact graph.  Choose any `Q in I_K` and
replace `Q` by `Q\cup K`.  The new branch set is connected.  It loses no old
adjacency, and every branch set newly contacted through `K` belongs to
`I_K` and was already adjacent to `Q`.  Thus the same one-defect model covers
strictly more vertices, a contradiction.  No component `K` exists, so the
model spans `G`.  \(\square\)

## Theorem 2 (connected-centre split)

Let `G` be seven-connected and suppose its vertex set is partitioned into
seven nonempty connected sets

\[
                         C,D,U_1,\ldots,U_5
\]

which are pairwise adjacent except that `C` and `D` are anticomplete.  Then
`G` contains a `K_7` minor or has a nonempty proper connected set `X` whose
full neighbourhood is the boundary of an actual separation.  The boundary
has order at least seven and, at equality, every component of its deletion
is adjacent to every boundary vertex.

### Proof

The set `N_G(C)` separates the nonempty connected set `C` from `D`, so
seven-connectivity gives

\[
                         |N_G(C)|\ge7.                 \tag{2.1}
\]

Spanningness and the unique missing adjacency give

\[
                         N_G(C)\subseteq\bigcup_{i=1}^5U_i. \tag{2.2}
\]

Hence some common branch set, say `U_1`, contains two distinct vertices
having neighbours in `C`.

Fix any vertex `rho in U_1`.  In a spanning tree of `G[U_1]`, take the
minimal subtree containing `rho` and every vertex of
`N_G(C)\cap U_1`.  It has a leaf `m in N_G(C)\cap U_1` with `m ne rho`.
Cut the tree edge incident with `m` in that minimal subtree, viewed in the
full spanning tree.  This partitions

\[
                         U_1=Z\mathbin{\dot\cup}W
\]

into nonempty connected adjacent sets, both adjacent to `C`, with
`rho in W`.

If `Z` is anticomplete to `D`, then `N_G(Z)` is the boundary of an actual
separation whose open sides contain `Z` and `D`.  If `W` is anticomplete to
some `U_j` with `j>=2`, then `N_G(W)` analogously separates `W` from
`U_j`.  Otherwise

\[
               C,\quad D\cup Z,\quad W,\quad U_2,U_3,U_4,U_5
\]

are seven disjoint connected pairwise adjacent branch sets.  The old
`D U_1` edge makes `D\cup Z` connected when `Z` is adjacent to `D`; the
tree-cut edge supplies its adjacency to `W`; `D` supplies all contacts from
`D\cup Z` to `U_2,...,U_5`; `W` retains its contacts to those four sets;
and the two marked vertices supply the two contacts from `C`.  This is a
`K_7` model.

The returned full neighbourhood has order at least seven by connectivity.
If its order is seven and a component of its deletion missed one boundary
vertex, that component would have a neighbourhood of order at most six,
contradicting seven-connectivity.  \(\square\)

## Theorem 3 (one-defect two-root completion or separation)

Let `G` be seven-connected.  Let `R_0,R_1` be disjoint adjacent connected
subgraphs, and let

\[
                         M_1,\ldots,M_5
\]

be a `K_5`-minor model disjoint from the roots.  Suppose one root is
adjacent to every `M_i` and the other is adjacent to at least four of them.
Then at least one of the following holds.

1. `G` contains a `K_7` minor.
2. There is a nonempty proper connected vertex set `X` such that `N_G(X)`
   is the boundary of an actual separation with two nonempty open sides.
   Its order is at least seven; if its order is seven, every component of
   `G-N_G(X)` is adjacent to every boundary vertex.

### Proof

If both roots are adjacent to all five model bags, they and the five bags
are a `K_7` model.  Otherwise orient the names so that `R_0` is adjacent to
all five bags, while `R_1` is anticomplete to `M_5` and adjacent to
`M_1,...,M_4`.  The seven sets

\[
               R_1,\quad M_5,\quad R_0,\quad
               M_1,M_2,M_3,M_4
\]

form a `K_7` model with only the `R_1M_5` adjacency missing.  By Theorem 1,
either `G` has a `K_7` minor or such a model may be chosen spanning while
retaining its one missing adjacency.  In the latter case Theorem 2 gives a
`K_7` minor or the stated full-neighbourhood separation. \(\square\)

## Consequence for the pentagonal-bipyramid target

Write

\[
 A=N_G(R_0)\cap V(F),\qquad B=N_G(R_1)\cap V(F).
\]

It is enough to find a `K_5` model in `F` whose five bags meet one of `A,B`
and whose at least four bags meet the other.  Full paired rooting is needed
only to obtain `K_7` immediately; the one-defect conclusion already yields
`K_7` or a genuine separation, with no orientation restriction on the two
connected roots.

This does not finish the live branch.  The separator may have order greater
than seven, and no common equality partition on it has been proved.  The
remaining response-coupling theorem must bound or strictly descend through
that separation, or synchronize the two closed-shore colourings.
