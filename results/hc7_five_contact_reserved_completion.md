# Completing a near-clique model from two connected subgraphs with five outside contacts

**Status:** written proof; separate internal audit GREEN in
[`hc7_five_contact_reserved_completion_audit.md`](hc7_five_contact_reserved_completion_audit.md).

This note sharpens the reserved-component construction used in the
degree-seven programme.  A connected remainder need not be adjacent to all
six outside branch sets.  Five outside contacts suffice except for two
sharp quotient geometries: the two new connected subgraphs may miss the
two ends of the unique absent outside adjacency in opposite orientations,
or they may miss two distinct outside branch sets disjoint from that absent
pair.

The result is an explicit minor-model construction.  It does not produce
the required connected remainder or prove `HC_7`.

## 1. Five-contact completion

### Theorem 1.1

Let `G` contain six pairwise disjoint connected subgraphs

\[
                       X,Y,D,F_1,F_2,F_3
\tag{1.1}
\]

such that every two of them are adjacent except possibly `X,Y`.  Let `A`
and `C` be two further connected subgraphs, disjoint from one another and
from all six subgraphs in (1.1), and suppose that `A` is adjacent to `C`.

Assume that each of `A,C` is adjacent to at least five of the six subgraphs
in (1.1).  Then `G` contains a `K_7` minor unless both have a unique missed
outside label and, up to interchanging `A,C`, one of the following holds.

1. The missed labels are `X,Y` in opposite orientations:

\[
 E_G(A,X)=\varnothing,\qquad E_G(C,Y)=\varnothing.
\tag{1.2}
\]

2. The missed labels are two distinct members of
   `\{D,F_1,F_2,F_3\}`.

More precisely, choose labels `R_A,R_C` from the six labels in (1.1) so
that

\[
 A\text{ is adjacent to every outside subgraph except possibly }R_A,
\qquad
 C\text{ is adjacent to every outside subgraph except possibly }R_C.
\tag{1.3}
\]

If at least one of `A,C` has all six outside contacts, choose its displayed
possible missed label to agree with the other one's possible missed label.
With that convention, if

\[
 R_A=R_C
 \quad\text{or}\quad
 |\{R_A,R_C\}\cap\{X,Y\}|=1,
\tag{1.4}
\]

then seven explicit branch sets can be obtained as in the proof.

#### Proof

First suppose `R_A=R_C=R`.

If `R` is `X` or `Y`, discard `R`.  The remaining five outside subgraphs
are pairwise adjacent and are each adjacent to both `A` and `C`.  Together
with `A,C` they form seven branch sets of a `K_7`-minor model.

If `R` is one of `D,F_1,F_2,F_3`, replace the two outside subgraphs `X,R`
by their union `X\cup R`.  This union is connected because `X` and `R`
are adjacent.  It is adjacent to `Y` through the old `R-Y` adjacency, and
it is adjacent to every other outside subgraph.  Both `A` and `C` are
adjacent to `X\cup R` through `X`, since their only possible missed label
is `R`.  Thus

\[
 A,\ C,\ X\cup R,\ Y,
 \quad\text{and the three members of }
 \{D,F_1,F_2,F_3\}-\{R\}
\tag{1.5}
\]

are seven pairwise disjoint connected branch sets with all required
adjacencies.

Now suppose `R_A\ne R_C`.  Condition (1.4) says that exactly one of them is
`X` or `Y`; in particular the two outside subgraphs `R_A,R_C` are adjacent.
Replace them by their connected union
`R_A\cup R_C`.  The set `A` is adjacent to this union through `R_C`, and
`C` is adjacent to it through `R_A`.  Each of `A,C` is adjacent to the four
unchanged outside subgraphs.  The merged outside subgraph and those four
unchanged subgraphs are pairwise adjacent: any required adjacency to the
merged subgraph is supplied by at least one of its two old members, and the
only possibly absent outside pair was `X,Y`, and one end of that pair lies
in the merged subgraph together with a vertex adjacent to its other end.
Hence

\[
 A,\ C,\ R_A\cup R_C,
 \quad\text{and the four unchanged outside subgraphs}
\tag{1.6}
\]

form a `K_7`-minor model.

The pairs of distinct missed labels not covered by these constructions are
exactly the two cases listed before (1.2).  At the quotient level their
three absent pairs are, respectively, a four-vertex path and a three-edge
matching.  Neither quotient is forced to have a `K_7` minor, so the stated
hypotheses alone cannot remove these exceptions. \(\square\)

### Proposition 1.2 (sharp quotient exceptions)

The two exceptional quotient graphs in Theorem 1.1 have no `K_7` minor.
Thus neither exception can be removed using only the adjacencies stated in
that theorem.

#### Proof

Take all eight displayed connected subgraphs to be singleton vertices.  In
the distinct-ordinary-label exception the quotient is `K_8` with three
independent edges deleted.  In the crossed `X,Y` exception its complement
is the path

\[
                              A-X-Y-C.
\tag{1.7}
\]

A `K_7`-minor model on an eight-vertex graph either deletes one vertex and
uses seven singleton branch sets, or uses all eight vertices with one
two-vertex branch set and six singleton branch sets.  The first possibility
would leave a `K_7` subgraph.  It is impossible in both quotients because
deleting one vertex leaves at least one missing edge.

In the second possibility, the two vertices in the nonsingleton branch set
must be adjacent and must cover every edge of the complement; moreover,
each remaining vertex must be adjacent in the original graph to at least
one of them.  A three-edge matching has no two-vertex cover.  For the path
in (1.7), its two-vertex covers of minimum order are

\[
                         \{X,Y\},\quad\{A,Y\},\quad\{X,C\}.
\]

The first pair is nonadjacent in the original graph.  The branch set
`A\cup Y` would have no edge to the remaining vertex `X`, and the branch
set `X\cup C` would have no edge to the remaining vertex `Y`.  Hence none
can be the required two-vertex branch set. \(\square\)

## 2. Reserved-component consequence

### Corollary 2.1

Use the setting of Theorem 4.1 or Corollary 4.2 in
[`hc7_reserved_component_linkage_completion.md`](hc7_reserved_component_linkage_completion.md).
Let the connected set formed by the retained donor and a linkage be `A`,
and suppose its sole possible missed outside label is the omitted owner
`R_0`.  Let `C_0` be a nonempty connected residual subgraph, disjoint from
`A`, adjacent to `A`, and adjacent to at least five of the six outside
branch sets.

If `R_0\notin\{X,Y\}`, then `G` contains a `K_7` minor unless `C_0` has
exactly five outside contacts and its unique missed label is a member of

\[
                  \{D,F_1,F_2,F_3\}-\{R_0\}.
\tag{2.1}
\]

#### Proof

Take `R_A=R_0`.  If `C_0` has all six outside contacts, choose
`R_C=R_0`; Theorem 1.1 applies.  Otherwise let `R_C` be its unique missed
label.  The theorem again applies unless `R_C` is a distinct member of
`\{D,F_1,F_2,F_3\}`, which is precisely (2.1). \(\square\)

### Corollary 2.2

In the three-owner reserved-component setting, choose the omitted owner

\[
                         R_0\in I-\{X,Y\}.
\tag{2.2}
\]

Such a choice always exists because `|I|=3`.  If the linkage for
`I-\{R_0\}` leaves a nonempty connected residual subgraph which is
adjacent to the linkage union and to at least five of the six outside
branch sets, then `G` contains a `K_7` minor unless the residual subgraph
misses exactly one outside label and that label is a member of
`\{D,F_1,F_2,F_3\}-\{R_0\}`.

#### Proof

Condition (2.2) and Corollary 2.1 give the assertion. \(\square\)

## 3. Exact trust boundary

The theorem lowers the contact requirement in the reserved-component
construction from six outside branch sets to five except for two exact
quotient geometries.  Choosing the omitted owner away from `X,Y` removes
the crossed `X,Y` exception but not the distinct-ordinary-label exception.
It preserves every branch-set label used in the construction and lists the
actual mergers.

It does not show that a two-owner linkage leaves a nonempty connected
remainder, that such a remainder has five outside contacts, or that a
failure produces a colour-compatible order-seven separation.  Those are
operation-specific host problems.
