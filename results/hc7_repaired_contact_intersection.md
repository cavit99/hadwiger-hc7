# Intersecting repaired paths in the exceptional `3+1` configuration

**Status:** written lemmas with a deterministic finite checker;
independently audited in
[`hc7_repaired_contact_intersection_audit.md`](hc7_repaired_contact_intersection_audit.md).
The negative examples below are barriers to local
path-intersection claims, not counterexamples satisfying the global `HC_7`
hypotheses.

## 1. Setup

Use the normalized sets and six disjoint linkage paths from
[`hc7_disjoint_k6minus_six_terminal_crossing_decoder.md`](hc7_disjoint_k6minus_six_terminal_crossing_decoder.md).
Thus `A={a0,a1,a2,a3,x,y}`, the vertices `a0,a1,a2,a3` induce a clique,
`xy,a3y,xa0,xa1,xa2` are edges, and

\[
 B=\{b_0,b_1,b_2,r,p,q\}
\]

induces `K6-pq`.  The linkage paths join `ai` to `bi` for `i=0,1,2`,
`a3` to `p`, `x` to `q`, and `y` to `r`.

Let `R=a3-w-x` be internally disjoint from this linkage system.  It is the
one-vertex repaired contact from the adjacent repaired-contact note.

## 2. A four-attachment component

### Lemma 2.1

Let `z` be `p` or `q`.  Suppose there is a connected subgraph `D`, disjoint
from the normalized vertices and the interiors of the six linkage paths,
which has a neighbour in each of

\[
                         \{a_3,x,y,z\}.               \tag{2.1}
\]

Then `G` contains a `K7` minor.

In particular, suppose `S` is a `y`--`z` path and `K` is an `a3`--`x`
path, both with interiors avoiding the normalized vertices and the linkage
paths.  If their interiors intersect, then `G` contains a `K7` minor.

#### Proof

Contract the six linkage paths to their labelled endpoint edges.  Also
contract, inside the union of `D` and four paths from `D` to the vertices
in (2.1), until one connected branch remains adjacent to all four named
vertices.  Call this branch `D` again.

If `z=q`, the following are seven branch sets:

\[
 \{b_0\},\ \{b_1\},\ \{b_2\},\ \{r\},\ \{q\},
 \quad D\cup\{a_3,p\},
 \quad\{a_0,a_1,a_2,x,y\}.                            \tag{2.2}
\]

Here the set containing `a3,p` includes the contracted `a3`--`p` linkage
path.  It is connected through `a3`, contacts `q` through `D`, and contacts
the last branch set through the attachments of `D` at `x` or `y`.
All remaining adjacencies follow from the clique on `B` and the stated
edges in `A`.

If `z=p`, use instead

\[
 \{b_0\},\ \{b_1\},\ \{b_2\},\ \{r\},\ \{p\},
 \quad D\cup\{x,q\},
 \quad\{a_0,a_1,a_2,a_3,y\}.                         \tag{2.3}
\]

The sixth branch set includes the contracted `x`--`q` linkage path.  Its
attachment through `D` at `p` supplies its contact with the singleton
`p`, while the attachments at `a3` or `y` supply its contact with the last
branch set.  Again all pairs of branch sets are adjacent.

For the final assertion, the union of the interiors of `S` and `K` is
connected when those interiors intersect, and it has a neighbour at each
of their four distinct ends.  Apply the first assertion.  \(\square\)

The conclusion is deliberately false for `z=r`; the endpoint `r` is
already the mate of `y` in the original six-path system, and the above
branch-set constructions then lose a required adjacency.

### Lemma 2.2 (the exceptional `r` attachment pattern)

Suppose a connected subgraph `D`, disjoint from the normalized vertices
and linkage-path interiors, is adjacent to all four vertices
`a3,x,y,r`.  Let `E` be the subset of the other eight normalized vertices
to which `D` is also adjacent.  Then `G` contains a `K7` minor whenever

\[
 E\not\subseteq\{b_0,b_1,b_2\}
 \quad\hbox{or}\quad
 E=\{b_0,b_1,b_2\}.                                  \tag{2.4}
\]

Equivalently, among endpoint-attachment sets, the only local patterns not
forcing the minor are

\[
 E\subseteq\{b_0,b_1,b_2\},\qquad |E|\le2.           \tag{2.5}
\]

#### Proof

Attachments at `p` or `q` reduce to Lemma 2.1.  By the symmetry which
simultaneously permutes `a0,a1,a2` and `b0,b1,b2`, it remains to give one
model when `D` attaches to `a0`, and one when it attaches to all three of
`b0,b1,b2`.

In the first case, after the standard linkage contractions, take

\[
 \{b_0\},\ \{b_1\},\ \{b_2\},\ \{r\},
 \quad\{x,y,q\},\quad\{a_3,p\},
 \quad D\cup\{a_0,a_1,a_2\}.                         \tag{2.6}
\]

In the second case take

\[
 D\cup\{y\},\quad \{b_0\},\ \{b_1\},\ \{b_2\},
 \quad\{r\},\quad\{a_0,a_1,a_2,x,q\},
 \quad\{a_3,p\}.                                    \tag{2.7}
\]

The linkage paths represented by a two-vertex string are absorbed into
that branch set.  Direct inspection proves connectivity and all pairwise
adjacencies.  Adding further attachments cannot destroy either model.
The exact negative assertions in (2.5) are verified in Proposition 3.1.
\(\square\)

There is a useful seven-connectivity consequence.  Let `C` be a component
outside the six-path linkage skeleton which attaches to `a3,x,y,r`.
Seven-connectivity gives at least seven distinct skeleton attachments for
`C`.  If all those attachments were among the twelve normalized endpoints,
then `C` would have at least three additional endpoint attachments, and
Lemma 2.2 would give a `K7` minor.  Hence, in a seven-connected
`K7`-minor-free host, such a component must attach to the interior of at
least one of the six linkage paths.  This conclusion does not yet say on
which path or on which side of its attachment the necessary rerouting lies.

### Lemma 2.3 (all interior attachments except on the `y`--`r` path)

Under the hypotheses of Lemma 2.2, suppose `D` has an attachment at an
internal vertex of any linkage path other than the path joining `y` to
`r`.  Then `G` contains a `K7` minor.

#### Proof

By symmetry take `i=0` and let `v` be the attachment vertex.  Split the
`a0`--`b0` path at `v`.  Absorb its `a0`-side together with `v` and `D`
into one branch set, and absorb its open `b0`-side into the branch set
containing `b0`.  After contracting the other five linkage paths, the
seven branch sets are

\[
 P_0[v,b_0]-\{v\},
 \quad\{b_1\},\quad\{b_2\},\quad\{r\},
 \quad\{x,y,q\},\quad\{a_3,p\},
 \quad D\cup P_0[a_0,v]\cup\{a_1,a_2\}.              \tag{2.8}
\]

In (2.8), the first displayed path expression simply means the connected
`b0`-side of the split path; the edge across the split gives its contact
with the last branch set.  The attachments of `D` at `a3,x,y,r` give all
remaining contacts not already supplied by the two endpoint cliques.
Thus these are the branch sets of a `K7` minor.

It remains to consider the paths from `a3` to `p` and from `x` to `q`.
If `v` is an internal attachment on the first path, contract its
`v`--`p` segment into `p`.  The image of `D` is now adjacent to `p`, so
Lemma 2.1 with `z=p` gives a `K7` minor.  If `v` lies on the second path,
contract its `v`--`q` segment into `q` and apply Lemma 2.1 with `z=q`.
Since a minor of a minor is a minor, both conclusions lift to `G`.
\(\square\)

Combining Lemmas 2.2 and 2.3 gives a more precise residue.  In a
seven-connected `K7`-minor-free host, a component outside the linkage
skeleton which attaches to `a3,x,y,r` can have no further normalized
endpoint attachment except at at most two of `b0,b1,b2`, and can have no
attachment in the interior of any linkage path except the path joining
`y` to `r`.  Since the four compulsory endpoints and at most two
exceptional `b_i` endpoints account for at most six attachments, at least
one attachment in the interior of the `y`--`r` path is forced.  Thus the
exceptional return is aligned with that one labelled path; arbitrary
return to any of the other five paths is already closed.

### Theorem 2.4 (the exceptional intersection yields an exact-seven separation)

Suppose `G` is seven-connected and has no `K7` minor.  Let `C` be a
component outside the six-path linkage skeleton which is adjacent to
`a3,x,y,r`.  Then

\[
                 X_7=\{a_3,x,y,r,b_0,b_1,b_2\}       \tag{2.9}
\]

is the boundary of an actual order-seven separation.  One open side
contains `C` and the interior of the `y`--`r` linkage path; the other
contains vertices of the three paths from `ai` to `bi`,
`i in {0,1,2}`.

#### Proof

Lemmas 2.2--2.3 show that, outside `X_7`, every attachment of `C` to the
linkage skeleton lies in the interior of the `y`--`r` path, and at least
one such attachment exists.  Hence

\[
 U=V(C)\cup\bigl(V(P_5)-\{y,r\}\bigr)
\]

is nonempty and connected in `G-X_7`.  Put

\[
 T=\bigcup_{i=0}^{2}V(P_i-b_i).
\]

The set `T` is nonempty and disjoint from `U`.

Suppose that `G-X_7` contains a path from `U` to `T`.  Shorten such a path
at its last vertex in `U` and then at its first later contact with the
linkage skeleton.  Its first end lies in the interior of `P5`: if it lay
in `C`, its next exit from the component `C` would be another vertex of
`U`, contradicting the shortening.  Its interior avoids the entire
linkage skeleton.

If its other end lies on one of `P0-b0,P1-b1,P2-b2`, it is a clean
augmenting path of Theorem 2.1 in the
[bridge-augmentation theorem](../results/hc7_disjoint_k6minus_support6_bridge_augmentation.md),
which gives a `K7` minor.

Otherwise its first later skeleton contact lies on `P3-a3` or `P4-x`.
Suppose first that it lies on `P3-a3`.  Because `C` is connected and is
adjacent to both `r` and `a3`, it contains the interior of an
`r`--`a3` path.  This path is disjoint from the shortened path.  Along
`P5`, the end of the shortened path precedes `r`, while along `P3`, `a3`
precedes its other end.  These are two crossed bridges between `P5` and
`P3`; Theorem 4.1 of the same bridge-augmentation theorem gives a `K7`
minor.  The case in which the first contact lies on `P4-x` is identical,
using an `r`--`x` path through `C` and the crossed bridges between `P5`
and `P4`.

Every possible first contact therefore contradicts the absence of a
`K7` minor.  Thus `X_7` separates `U` from `T`.  Taking the union of the
components of `G-X_7` meeting `U` gives an actual separation of order at
most seven with both open sides nonempty.  Seven-connectivity forces its
boundary to have order exactly seven, and hence to equal `X_7`.
\(\square\)

### Corollary 2.5 (both full-subgraph packing numbers equal one)

Assume in addition that `G` is strongly seven-contraction-critical:

\[
 \chi(G)=7\quad\text{and every proper minor of }G\text{ is
 six-colourable}.
\]

For the separation in Theorem 2.4, each open shore has `X_7`-full packing
number one: it contains a connected subgraph adjacent to every vertex of
`X_7`, but it contains no two vertex-disjoint such subgraphs.

#### Proof

The vertices `r,b0,b1,b2` induce a clique of order four in `G[X_7]`.
Apply the exact-seven full-packet packing theorem to the separation from
Theorem 2.4.  If `nu_1,nu_2` are the two maximum packing numbers, that
theorem gives

\[
 4\le \omega(G[X_7])\le 6-(\nu_1+\nu_2).
\]

Every component of either nonempty open shore is `X_7`-full by
seven-connectivity, so `nu_1,nu_2>=1`.  The displayed inequality gives
`nu_1+nu_2<=2`, and hence `nu_1=nu_2=1`. \(\square\)

This conclusion is stronger than an unclassified order-seven separation,
but it is not a colouring or a strict recursive reduction.  A complete
argument must still compose the two shores with packing number one or
attach a well-founded parameter to the separation.

## 3. Exact local barriers

### Proposition 3.1

For every `z` in `{p,q,r}`, form the bare graph consisting of the normalized
twelve-vertex quotient, the path `a3-w-x`, a path `y-s-z`, and two further
internally disjoint paths `a3-u-x` and `a3-v-x`, with all four new internal
vertices distinct.  This graph has no `K7` minor.

Consequently, even two distinct alternative `a3`--`x` paths which each
avoid both edges `a3w` and `wx`, and which are internally disjoint from the
clean `y`--`z` path, do not force a `K7` minor from the local configuration
alone.  If either alternative has one internal vertex, it does give the
exact-six support rotation already described in Lemma 2.1 of
[`hc7_repaired_contact_exchange.md`](hc7_repaired_contact_exchange.md),
but no strict improvement follows.

There is a second sharp barrier.  Add a vertex `t` adjacent to all four of
`a3,x,y,r`, while retaining `a3-w-x`.  The resulting fourteen-vertex graph
has no `K7` minor.  Thus Lemma 2.1 cannot be extended from `z in {p,q}` to
`z=r`, even when the two paths meet at one internal vertex.

More exactly, if `t` is additionally adjacent to a subset `E` of the
other eight normalized endpoints, exhaustive checking gives no `K7` minor
precisely for the seven sets in (2.5): the empty set, the three singleton
subsets of `{b0,b1,b2}`, and its three two-element subsets.  Every other
choice gives a `K7` minor, in agreement with Lemma 2.2.

For these seven endpoint exceptions the checker also supplies an
independent negative certificate: a vertex-elimination ordering whose
filled width is at most five.  This gives a chordal completion with no
clique larger than six, hence treewidth at most five.  Since treewidth is
minor-monotone and `K7` has treewidth six, none of the seven bare graphs
has a `K7` minor.  The deletion--contraction search is therefore not the
sole verification of the endpoint-exception list.

#### Verification

The adjacent checker verifies the displayed positive branch-set models,
checks all 256 endpoint-attachment subsets from Lemma 2.2, checks the six
possible linkage-path locations from Lemma 2.3, and performs exact
deletion--contraction searches for the negative graphs.  Every vertex
above order twelve selected by the recurrence has degree below six.  In a
`K7` model such a vertex is either unused or shares a branch set with one
of its neighbours, so deletion and contraction give an exact recurrence.

Run from the repository root:

```sh
python3 results/hc7_repaired_contact_intersection.py
```

The examples are not seven-connected and do not encode the two particular
six-colourings supplied by edge-criticality.  They refute only an argument
which forgets those colours and uses the displayed paths as unlabelled
local graph structure.

## 4. Consequence for the two Kempe witnesses

In a `K7`-minor-free host, Lemma 2.1 imposes the following exact condition.
For `z in {p,q}`, every linkage-system-avoiding `a3`--`x` path is internally
disjoint from every linkage-system-avoiding `y`--`z` path.  Therefore, if
the simultaneous edge-bypassing path from Lemma 3.2 of the
[repaired-contact note](hc7_repaired_contact_exchange.md) avoids the
linkage system, it either remains disjoint from the second residual path
or closes the configuration by (2.2) or (2.3).

For `z=r`, an intersection does not by itself close the configuration.
However, if the intersecting path interiors lie in one component outside
the linkage skeleton, Theorem 2.4 gives a complete local dichotomy: either
the forced return to another linkage path combines with the component to
form the crossed-bridge `K7` model, or the seven labelled vertices in
(2.9) are the boundary of an actual order-seven separation.  Thus the
`r` case does not require an unbounded analysis of attachment order along
`P5`; it returns an exact-seven separation suitable for the existing
boundary-colouring machinery.  What is not proved here is that every
edge-deletion Kempe bypass and the residual `y`--`r` path meet in one
component outside the linkage skeleton.
