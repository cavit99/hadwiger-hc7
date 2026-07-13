# Rooted wqo and linked-annulus pumping: rigorous audit

## 1. Executive verdict

Both proposed mechanisms have valid forms, but they have sharply
different force.

1. **Rooted wqo is valid but non-effective.**  For fixed numbers of
   colours and roots, every side of a separation in a minor-critical
   graph belongs to a finite set of rooted-minor-minimal obstruction
   graphs.  Hence a finite size bound exists.  One must fix the graph
   induced by the roots before applying rooted wqo, because deleting a
   root--root edge on only one side does not glue to the unchanged
   opposite side.  No monotonicity of colour extension under
   contraction is needed: minimal elements of *every* subset of a wqo
   form a finite antichain.
2. **Linked-annulus pumping is valid and explicit.**  If two nested
   adhesions have the same inward extension family and a clean
   label-preserving linkage joins their roots, delete everything in
   the intervening annulus except the linkage and contract each linkage
   path.  The retained inner graph then has exactly the repeated
   extension family on the outer roots.  Gluing it to the unchanged
   outer context gives a proper minor with the same colourability
   obstruction, contradicting minor-criticality.

The important caveat in item 2 is that path contraction can create
edges between roots.  Consequently one must not assert that the pumped
rooted graph is isomorphic to the old inward side.  The extension-set
argument remains correct: all restrictions caused by transported inner
root edges are already encoded in the repeated inner extension family.
In the HC7 pentagonal application the cyclic linkage transports a
(C_5) to the same (C_5), so even this caveat disappears after
extraneous annular cross-edges are deleted.

## 2. Boundary extension notation

An ordered `k`-rooted graph is a graph `L` with distinct distinguished
vertices

\[
 S=(s_1,\ldots,s_k).
\]

For a positive integer `r`, define

\[
 {\cal E}_r(L,S)
 =\{\phi:S\to[r]:\phi\text{ extends to a proper
 }r\text{-colouring of }L\}.                       \tag{2.1}
\]

If `G=L union_S M` is a proper separation, then

\[
 G\text{ is }r\text{-colourable}
 \quad\Longleftrightarrow\quad
 {\cal E}_r(L,S)\cap {\cal E}_r(M,S)\ne\varnothing.
                                                               \tag{2.2}
\]

The colour names are symmetric.  Thus (2.1) is equivalently encoded
by the equality partitions of `S` into at most `r` colour blocks which
occur in extensions.

Call `G` **r-minor-critical** if `G` is not r-colourable but every
proper minor of `G` is r-colourable.

## 3. The correct rooted-minor order

Fix a graph `T` on the ordered root set.  Let

\[
 {\mathfrak G}_{k,T}
\]

be the class of finite ordered k-rooted graphs whose root-induced graph
is exactly `T`.

A rooted minor model preserves every root label: the branch set for
root `s_i` contains the original root `s_i`, the k root branch sets are
distinct, and no two roots are identified.  Nonroot vertices may be
absorbed into a root branch set.  Within
`mathfrak G_(k,T)`, such a model can always be realized while retaining
all edges of `T` between roots.

The last restriction matters.  If a boundary edge is deleted from one
side while the same edge remains in the opposite side, gluing the two
rooted graphs restores the edge and does not realize the claimed side
minor.  Fixing `T` avoids this problem.

### Lemma 3.1 (fixed-boundary rooted wqo)

For every fixed `k` and `T`, the class
`mathfrak G_(k,T)` is well-quasi-ordered by root-preserving minors.

#### Proof

Use the labelled form of the Graph Minor Theorem.  Give root `s_i` its
own label `i` and give nonroots the empty label.  The finite label set,
with labels required to be preserved, is a wqo.  In a labelled minor
model of one k-rooted graph in another, the branch set representing
root `i` must contain the uniquely labelled original root `i`.
Disjointness and the presence of all k root labels prevent two roots
from entering one branch set or a root from being discarded.

Pass to the subsequence whose root-induced graph is the fixed graph
`T`.  If a labelled minor model creates an extra edge between two root
branch sets which is not in `T`, delete that edge; it arose from the
nonroot part because the original roots have the same nonedge in `T`.
For an edge belonging to `T`, retain the original root--root edge.
Thus the labelled minor relation can be realized without changing the
root graph `T`.  Hence the fixed-boundary class is a wqo. \(\square\)

## 4. Finite rooted obstruction theorem

For a set `F` of labelled r-colourings of the roots, put

\[
 {\cal P}_{r,T,F}
 =\{L\in{\mathfrak G}_{k,T}:
       {\cal E}_r(L,S)\cap F=\varnothing\}.         \tag{4.1}
\]

Notice that (4.1) need not be upward- or downward-closed under minors:
edge contraction can increase chromatic number.  Closure is not needed
for the following argument.

### Theorem 4.1 (rooted finite-boundary obstruction theorem)

For fixed `r,k,T,F`, the set of rooted-minor-minimal graphs in
`P_(r,T,F)` is finite.

Consequently there is a finite number `B(r,k)` such that, whenever an
r-minor-critical graph has a proper separation of order k, each side
has at most `B(r,k)` vertices.

#### Proof

Minimal elements of any subset of a wqo form an antichain.  Lemma 3.1
therefore implies that the minimal elements of (4.1) are finite.

Now let

\[
 G=L\cup_S M
\]

be a proper separation of an r-minor-critical graph, and put

\[
 F={\cal E}_r(M,S),\qquad T=G[S].
\]

Equation (2.2) and non-r-colourability give

\[
 {\cal E}_r(L,S)\cap F=\varnothing,                \tag{4.2}
\]

so `L` belongs to (4.1).

Let `L'` be any proper root-preserving minor of `L` in
`mathfrak G_(k,T)`.  Perform its branch-set deletions and contractions
inside `G`.  A nonroot vertex of `L` has no neighbour in `M-S`, so
absorbing such a vertex into a root creates no unintended edge to the
open side of `M`.  Root edges in `T` are retained.  Therefore

\[
 G'=L'\cup_S M
\]

is a proper minor of `G`.  Minor-criticality makes `G'` r-colourable,
and its boundary state lies in

\[
 {\cal E}_r(L',S)\cap F.
\]

Thus every proper fixed-boundary rooted minor of `L` leaves (4.1), and
`L` is a minimal member.  The same argument with the sides reversed
applies to `M`.

There are finitely many root graphs `T` and finitely many possible
families

\[
 F\subseteq[r]^k.
\]

Take the maximum order of the finitely many minimal rooted obstructions
over all these choices.  This is `B(r,k)`. \(\square\)

### Audit qualification

The bound `B(r,k)` is existential and supplies no usable numerical
value.  Indeed the same wqo observation with no boundary says that, for
each fixed `r`, there are only finitely many r-minor-critical graphs in
total.  This does not decide whether one of them violates the desired
clique-minor conclusion.  Thus Theorem 4.1 is rigorous finite-boundary
compactness, not a proof of HC7 or of Hadwiger's Conjecture.

## 5. Clean nested linked adhesions

We now state the explicit pumping theorem.

Let

\[
 (O_i,I_i),\qquad S_i=O_i\cap I_i
 \quad(0\le i\le m)
\]

be nested proper separations of `G`, oriented so that

\[
 O_i\subseteq O_j,qquad I_j\subseteq I_i
 \quad\text{whenever }i<j.                         \tag{5.1}
\]

Every `S_i` is an ordered k-tuple

\[
 S_i=(s_i^1,\ldots,s_i^k).
\]

For `i<j`, a **clean label-preserving linkage** from `S_i` to `S_j`
consists of pairwise vertex-disjoint paths

\[
 P_1,\ldots,P_k,\qquad
 P_a:s_i^a\longrightarrow s_j^a,                  \tag{5.2}
\]

such that the internal vertices of every path lie in the open annulus

\[
 I_i\setminus (O_i\cup I_j),
\]

and the paths meet `S_i union S_j` only at their prescribed ends.
Some paths may be trivial when the corresponding root is literally
the same vertex in both adhesions.  Distinct nontrivial paths avoid all
fixed-root paths.

Define the inward extension family

\[
 {\cal F}_i={\cal E}_r(G[I_i],S_i),                \tag{5.3}
\]

transported to one common ordered label set via (5.2).

## 6. Linked-annulus pumping theorem

### Theorem 6.1 (exact extension-family pumping)

Assume `i<j`, a clean linkage (5.2) exists, and

\[
 {\cal F}_i={\cal F}_j                            \tag{6.1}
\]

under the label identification.  Then `G` has a proper minor `G'`
whose inward extension family at `S_i` is exactly `F_i`, while the
outer graph `G[O_i]` is unchanged.

In particular, if `G` is not r-colourable, neither is `G'`.
Therefore an r-minor-critical graph cannot contain such a repeated
pair of linked inward families.

#### Proof

Start with the subgraph consisting of

1. the unchanged outer graph `G[O_i]`;
2. the unchanged inner graph `G[I_j]`; and
3. the linkage paths `P_1,...,P_k`.

Delete all other annular vertices.  For every nontrivial linkage path,
delete every edge incident with one of its internal vertices except
the edges of the path itself.  In particular delete chords of a path,
edges between different paths, and edges from a path interior to an
unretained annular vertex.  The clean-linkage hypothesis ensures that
this does not delete an edge of `G[O_i]` or `G[I_j]`.

Contract every `P_a` to its outer endpoint `s_i^a`.  The paths are
disjoint, so distinct roots are not identified.  The retained copy of
`G[I_j]` is now rooted at `S_i`, with root `s_j^a` identified with
`s_i^a`.  Call this rooted inner graph `J`.

A labelled colouring of `S_i` extends to `J` if and only if the same
labelled colouring, transported to `S_j`, extends to `G[I_j]`.
Therefore

\[
 {\cal E}_r(J,S_i)={\cal F}_j={\cal F}_i.          \tag{6.2}
\]

The resulting graph is

\[
 G'=G[O_i]\cup_{S_i}J.
\]

It is a minor of `G`.  It is proper because `i<j` leaves a nonempty
annulus: at least one annular vertex is deleted or at least one
nontrivial path edge is contracted.

For every labelled state on `S_i`, extension through the outer context
is unchanged, and (6.2) says extension through the inward side is also
unchanged.  Hence

\[
 G'\text{ is }r\text{-colourable}
 \Longleftrightarrow
 {\cal E}_r(G[O_i],S_i)\cap{\cal F}_i\ne\varnothing
 \Longleftrightarrow
 G\text{ is }r\text{-colourable}.                 \tag{6.3}
\]

If `G` is r-minor-critical and non-r-colourable, (6.3) contradicts
the r-colourability of the proper minor `G'`. \(\square\)

## 7. Edge-creation audit

Contracting the linkage paths can create edges between outer roots.
There are three sources.

1. A cross-edge between two path interiors becomes a root edge.  This
   is harmless only if it is deleted before contraction, as required
   in the proof.
2. An annular edge from a path interior to the wrong root becomes a
   root edge.  It too must be deleted before contraction.
3. An edge between two inner roots in `G[I_j]` becomes an edge between
   the corresponding outer roots.  This edge cannot simply be deleted
   if one wants to preserve the inner extension family.

The third source is the genuine caveat.  It does **not** invalidate
Theorem 6.1.  The transported graph `J` is allowed to have that root
edge, and its restriction on boundary colourings is already part of
`F_j`.  Equality (6.1) says that precisely the same boundary states
extended through the original inward side at `S_i`.  The theorem
claims equality of extension relations, not equality of rooted graphs.

If one wants the root-induced graph itself to remain fixed, one must
add either of the following hypotheses:

* the label bijection sends `G[S_j]` isomorphically to `G[S_i]`; or
* the boundary graph is included as part of the finite state and all
  transported extra root edges are already forced by every state in
  `F_i`.

In the pentagonal HC7 application, the first condition holds: planar
order makes the five-cycle linkage cyclic up to rotation or reflection,
and the two protected roots are fixed.

## 8. Counting extension families

Let

\[
 N(r,k)=\sum_{q=1}^{\min(r,k)} {k\brace q},         \tag{8.1}
\]

where the braces denote Stirling numbers of the second kind.  There are
`N(r,k)` equality partitions of k labelled roots into at most r colour
classes.  An extension family is a subset of these states, so there are
at most

\[
 2^{N(r,k)}                                        \tag{8.2}
\]

different inward extension families.

### Corollary 8.1 (explicit linked depth bound)

In an r-minor-critical graph, a clean nested sequence of linked
k-adhesions has fewer than

\[
 2^{N(r,k)}
\]

annuli.

#### Proof

If there are `d` annuli, there are `d+1` inward extension families.
When `d` is at least the number in (8.2), two families repeat.  Compose
the consecutive label-preserving linkages to obtain a clean linkage
between the repeated adhesions and apply Theorem 6.1. \(\square\)

## 9. HC7 nested pentagonal adhesions

In the four-residual-colour HC7 cell, the adhesion is

\[
 S_i=A\mathbin{\dot\cup}V(C_i),qquad
 A=K_2,qquad C_i=C_5.                             \tag{9.1}
\]

The two vertices of `A` are the same in every adhesion and give two
trivial label paths.  Between two nested pentagons, even when they
share public vertices or edges, ambient 7-connectivity supplies five
disjoint paths in the planar side.  Indeed, a set of at most four
vertices meeting every path between the two pentagons would lift with
`A` to an ambient cut of order at most six.  Set-Menger therefore gives
five paths using every vertex of each pentagon as an endpoint.  A
shared cycle vertex necessarily gives a trivial path; otherwise two
paths would use that vertex.  Truncating the nontrivial paths at their
first and last cycle vertices confines them to the annulus.  Planarity
orders their endpoints cyclically, up to rotation or reflection, so
they give the five label-preserving paths required in Theorem 6.1.

Using the crude universe of all partitions of seven roots into at most
six blocks gives

\[
 N(6,7)=
 {7\brace1}+{7\brace2}+{7\brace3}+{7\brace4}
 +{7\brace5}+{7\brace6}
 =1+63+301+350+140+21=876.                         \tag{9.2}
\]

Thus the requested crude bound is

\[
 \text{nested depth}<2^{876}.                     \tag{9.3}
\]

There is a much sharper bound in the actual boundary graph (9.1).
The two protected vertices are adjacent and complete to the pentagon,
so they form two distinct singleton colour blocks.  The pentagon must
then be partitioned into either three or four independent colour
blocks.  There are

\[
 5
\]

three-block partitions (the 30 labelled proper 3-colourings of a
5-cycle, divided by `3!`) and five four-block partitions (choose the
unique nonadjacent repeated pair).  Hence there are only ten boundary
state orbits and at most

\[
 2^{10}=1024                                      \tag{9.4}
\]

inward extension families.

### Corollary 9.1 (overlap-robust HC7 depth bound)

A noncrossing nested chain of `K_2+C_5` adhesions in a hypothetical
6-minor-critical HC7 counterexample has fewer than 1024 annuli, even
when consecutive pentagons share public vertices or public edges.

This turns the concentric infinite-web obstruction into a bounded-depth
problem.  It does not bound the size or complexity of one annular torso,
and it does not turn a branching laminar family into one chain.  Those
are the exact remaining qualifications.

## 10. Final strategic assessment

The rooted-wqo theorem is fully rigorous but nonconstructive.  The
linked pumping theorem is the stronger operational result: it gives an
explicit state bound, survives the contraction edge-creation audit, and
cuts the HC7 linked pentagonal depth bound from the proposed
`2^876` to `1024` by using the actual boundary graph.

No clean vertex-disjoint subchain extraction is required.  The next
structural step is to control branching in the noncrossing
obstructing-cycle hierarchy and to bound the complexity of an
individual annular torso.  No further colouring theorem is needed for
the pumping step along a chain.
