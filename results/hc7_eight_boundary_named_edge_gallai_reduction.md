# Named-edge normal forms in the eight-boundary Gallai--Edmonds decomposition

**Status:** written proof with a separate GREEN internal audit in
[`hc7_eight_boundary_named_edge_gallai_reduction_audit.md`](hc7_eight_boundary_named_edge_gallai_reduction_audit.md).
This is a boundary-structure theorem, not a colouring-transfer theorem and
not a proof of `HC_7`.

## 1. Statement

For graphs on disjoint vertex sets, `G \vee H` denotes their join.  Let `J`
be a graph on eight vertices, put `F=\overline J`, and suppose

\[
                 I_2\vee J\not\succcurlyeq K_7.       \tag{1.1}
\]

Assume that four distinct named vertices `x_1,x_2,y_1,y_2` induce exactly
the two independent edges

\[
                 x_1x_2,\quad y_1y_2                 \tag{1.2}
\]

in `J`.  Equivalently, these four vertices induce the cycle `K_{2,2}` in
`F`, with bipartition
`\{x_1,x_2\}\mathbin{\dot\cup}\{y_1,y_2\}`.

Suppose also that `F` has no perfect matching.  Write

\[
                 V(F)=D\mathbin{\dot\cup}A\mathbin{\dot\cup}C
\]

for its Gallai--Edmonds decomposition, let `D_1,\ldots,D_q` be the
components of `F[D]`, and use the four possible pairs

\[
 (|A|,q)\in\{(0,2),(0,4),(1,3),(2,4)\}               \tag{1.3}
\]

from the canonical eight-boundary theorem.

Then the following conclusions hold.

1. The type `(|A|,q)=(0,4)` is impossible.

2. If `(|A|,q)=(2,4)`, then `C=\varnothing`, the component orders of
   `F[D]` are `3,1,1,1`, and every `J[D_i]` is independent.  Moreover,
   `A` consists of exactly two of the four named vertices.  More precisely:

   - if `A=\{x_1,x_2\}` or `A=\{y_1,y_2\}`, the endpoints of the other
     named edge lie in two distinct components of `F[D]`;
   - if `A` contains one endpoint of each named edge, the other two named
     vertices lie together in the unique three-vertex component of `F[D]`.

3. If `(|A|,q)=(1,3)`, then `C=\varnothing`, the component orders of
   `F[D]` are `5,1,1`, every `J[D_i]` is triangle-free, and `J[C]` is
   independent (the last assertion being vacuous after `C=\varnothing`).
   Either all four named vertices lie in the five-vertex component of
   `F[D]`, or the unique vertex of `A` is named and the other three named
   vertices lie in that component.

4. If `(|A|,q)=(0,2)`, all four named vertices lie in one component of
   `F[D]` or all four lie in `C`.  In addition,

   \[
        \omega(J[D_i])\le3\quad(i=1,2),\qquad
        \omega(J[C])\le2.                              \tag{1.4}
   \]

Thus the named-edge data remove the `(0,4)` alternative and reduce the
`(2,4)` and `(1,3)` alternatives to the displayed component orders and
placements.  No assertion is made here that the canonical set `A` meets
every `K_5`-minor model or that a Gallai--Edmonds alternating path changes
an attained boundary colouring.

## 2. A clique bound

We first record the common calculation used throughout the proof.

### Lemma 2.1

The graph `J` has no clique of order five.  Consequently,

\[
        \omega(J[D_i])\le 5-q\quad(1\le i\le q),
        \qquad
        \omega(J[C])\le 4-q.                           \tag{2.1}
\]

### Proof

If `Q` were a five-vertex clique of `J`, choose `w\in V(J)-Q` and denote
the two vertices of `I_2` by `u,v`.  Then

\[
              \{u,w\},\quad\{v\},\quad\{z\}\ (z\in Q)
\]

are seven pairwise adjacent connected branch sets in `I_2\vee J`, contrary
to (1.1).  Hence `\omega(J)\le4`.

There is no `F`-edge between distinct components of `F[D]`, and there is
no `F`-edge between `D` and `C`.  Thus, in `J`, distinct `D_i` are complete
to one another and every `D_i` is complete to `C`.  A clique in `J[D_i]`,
together with one vertex from each of the other `q-1` components, is a
clique of `J`; this gives

\[
                 \omega(J[D_i])+(q-1)\le4.
\]

A clique in `J[C]`, together with one vertex from each of the `q`
components `D_i`, similarly gives

\[
                 \omega(J[C])+q\le4.
\]

These are exactly (2.1).  \(\square\)

## 3. Proof of the normal forms

The four named vertices induce a connected four-cycle in `F`.  Recall also
that every `D_i` is factor-critical and hence has odd order, `F[C]` has a
perfect matching, and there is no `F`-edge from `D` to `C` or between
distinct `D_i`.

### Type `(0,4)`

Lemma 2.1 gives `\omega(J[D_i])\le1` for every `i`, so every `J[D_i]` is
independent.  It also gives `\omega(J[C])\le0`, and therefore
`C=\varnothing`.  Because `A=\varnothing`, the connected four-cycle on
the named vertices must lie in one component `D_i`.  But that component
then contains the `J`-edge `x_1x_2` (and also `y_1y_2`), contradicting the
independence of `J[D_i]`.  This proves part 1.

### Type `(2,4)`

Again every `J[D_i]` is independent and `C=\varnothing`.  Since `|D|=6`
is the sum of four positive odd component orders, those orders are

\[
                         3,1,1,1.                     \tag{3.1}
\]

Let `k` be the number of named vertices in `A`; thus `k\le2`.  If `k=0`,
the named `F`-cycle lies in one `D_i`, contradicting the independence of
`J[D_i]`.  If `k=1`, deleting that one vertex from the named `F`-cycle
leaves a connected three-vertex path.  Its vertices lie in one `D_i`, and
they include both endpoints of one of the named `J`-edges, again a
contradiction.  Hence `k=2`, and `A` consists entirely of named vertices.

If those two vertices are the endpoints of one named `J`-edge, the
endpoints of the other named edge cannot lie together in an independent
graph `J[D_i]`; hence they lie in distinct components.  If instead `A`
contains one endpoint of each named edge, the two remaining named vertices
come from different named edges and are adjacent in `F`.  They therefore
lie in one `D_i`, which must be the unique component of order three in
(3.1).  This proves part 2.

### Type `(1,3)`

Lemma 2.1 gives

\[
                  \omega(J[D_i])\le2,
                  \qquad \omega(J[C])\le1.            \tag{3.2}
\]

Thus every `J[D_i]` is triangle-free and `J[C]` is independent.

If the unique vertex of `A` is not named, the connected named `F`-cycle
lies in one component of `F-A`.  It cannot lie in `C`, because it contains
the named `J`-edges while `J[C]` is independent.  Hence all four named
vertices lie in one `D_i`.

If the vertex of `A` is named, the other three named vertices induce a
connected path in `F`.  That path also contains both endpoints of one
named `J`-edge, so it cannot lie in `C`; its three vertices lie in one
`D_i`.  If this component had order three, factor-criticality would force
`F[D_i]=K_3`: after deletion of any vertex the other two must be adjacent.
Then `J[D_i]` would be independent, contradicting the named `J`-edge in
the component.  Therefore the component has odd order at least five.

In either subcase one `D_i` has order at least five.  The other two
factor-critical components have order at least one, while `|A|=1` and the
whole graph has eight vertices.  It follows that `C=\varnothing` and the
three component orders are exactly `5,1,1`.  This proves part 3.

### Type `(0,2)`

Because `A=\varnothing`, the connected named `F`-cycle lies within a
single component of `F`.  There are no edges from `D` to `C` or between
the two components of `F[D]`; hence all four named vertices lie in one
`D_i`, or all four lie in `C`.  The bounds (1.4) are (2.1) with `q=2`.
This proves part 4 and the theorem.  \(\square\)

## 4. Exact contribution and limitation

In the support-six argument, the two named `J`-edges are the two branch
sets that remain split when a minimal bad contraction is expanded to an
eight-vertex separator.  The theorem therefore applies to that exact
boundary whenever the absence of the relevant balanced boundary partition
is expressed as the absence of a perfect matching in `F=\overline J`.

The result is strictly structural.  A Gallai--Edmonds alternating path is
a path in the complement of the boundary graph; it is not automatically a
Kempe chain in either shore and does not preserve the labels of an existing
minor model.  The next step must use the proper-minor colouring transitions,
seven-connectivity at the level of individual vertices, or the specified
branch sets in the one-edge predecessor models.  Static boundary matching
data alone cannot provide that step.
