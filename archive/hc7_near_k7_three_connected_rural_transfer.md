# Three-connected rural transfer: linkage or a shallow full society

## Status

This note extends the off-face transfer mechanism from four-connected
carriers to carriers which are already known to be planar and
three-connected.  It closes every such locked carrier unless the whole
external adhesion lies on one coherent face.  At minimum degree seven the
remaining page is quantitatively shallow: if the coherent face has length
`f` and there are `h` vertices off it, then

\[
                              1\le h\le f-6.              \tag{0.1}
\]

This is a rural terminal, not by itself a global two-apex conclusion.
Nonplanar three-connected carriers and carriers with connectivity at most
two are outside the theorem.

## 1. Setting

Use the coherent one-missing spanning model and the deficient-bag
minimality class of
`../results/hc7_near_k7_offface_transfer_closure.md`.  Thus the deficient
bag `A` consists of the fixed path core `P` and pairwise anticomplete
connected pieces attached to `P`, and `|A|` is minimum among the labelled
spanning models retaining the fixed path data and missed twin.

Fix a path cut `P=L dotunion R`, a connected crossing piece `K`, and two
distinct retained rows `H,Q`.  Put

\[
 A_L=N_K(L),\quad A_R=N_K(R),\quad
 P_H=N_K(H),\quad P_Q=N_K(Q).                             \tag{1.1}
\]

Assume these four portal families have a full system of distinct
representatives.  Suppose `G[K]` is planar and three-connected.

## Theorem 1 (three-connected rural transfer)

Exactly one of the following conclusions is forced.

1. `K` contains two vertex-disjoint paths, one joining `A_L` to `P_H`
   and the other joining `A_R` to `P_Q`.
2. `G[K]` has its unique plane embedding with a face `F` such that

   \[
       A_L\cup A_R\cup P_H\cup P_Q\subseteq V(F),        \tag{1.2}
   \]

   and every vertex of `K-V(F)` has no neighbour outside `K`.

In outcome 2 every literal attachment of the carrier to the rest of the
spanning model lies on `F`.

### Proof

Assume the protected linkage in outcome 1 does not exist.  For any full
SDR `(l,r,h,q)`, an `{l,r,h,q}`-rooted `K_4` model would give the linkage:
use the `l,h` rooted branch sets and their model edge for one path, and
the disjoint `r,q` branch sets and their model edge for the other.
Therefore no SDR image has a rooted `K_4`.

The SDR facial-coherence theorem applies to a planar three-connected
graph as well as to a four-connected graph.  It gives one face containing
every portal vertex occurring in a full SDR.  By the one-swap SDR lemma,
every member of the union of the four portal families occurs in some full
SDR, proving (1.2).

Suppose now that `w in K-V(F)` has a neighbour outside `K`.  Since `K` is
three-connected, `K-w` is connected.  All four portal families lie on
`F`, so `K-w` retains all of them and remains attached to the fixed path
core.  The off-face transfer lemma from the cited source applies verbatim:
`w` cannot meet `P`, `H`, or `Q`, cannot meet the fixed missed twin, and
cannot meet a different old exterior piece.  It therefore meets one of
the three common retained rows.  Moving `w` into that row preserves all
labelled model adjacencies and the comparison class while decreasing
`|A|`, a contradiction.  Hence no such `w` exists, proving outcome 2.
\(\square\)

## Theorem 2 (Euler shallowness)

Retain outcome 2 and assume `delta(G)>=d>=7`.  Put

\[
 f=|V(F)|,\qquad h=|V(K)-V(F)|.
\]

Then

\[
                         (d-6)h\le f-6.                  \tag{2.1}
\]

In particular, at the `HC_7` value `d=7`,

\[
                              1\le h\le f-6,             \tag{2.2}
\]

so `f>=7`.  Consequently every planar three-connected locked carrier
whose coherent portal face has length at most six has the protected
linkage.

### Proof

Every vertex off `F` has no external neighbour by Theorem 1, and hence
has degree at least `d` in `G[K]`.  Every vertex on `F` has carrier degree
at least three.  If `n=f+h` and `m=|E(G[K])|`, then

\[
                         2m\ge 3f+dh.                    \tag{2.3}
\]

Taking `F` as the outer face, the simple planar outer-face bound gives

\[
                         2m\le 6n-6-2f=4f+6h-6.          \tag{2.4}
\]

Comparison of (2.3) and (2.4) gives (2.1).

It remains only to justify the lower bound `h>=1`.  If `h=0`, all
vertices of the three-connected planar graph `G[K]` lie on one face, so
the graph is outerplanar.  Every finite simple outerplanar graph has a
vertex of degree at most two, contradicting three-connectivity.  Thus
`h>=1`; at `d=7`, (2.1) is exactly (2.2).  \(\square\)

## Exact use and residual

The theorem turns the planar three-connected part of the former
“not-four-connected” residue into the intended web object: a single
coherent society whose entire adhesion is on its outer face.  Such a page
can be used in a port-labelled disk expansion, and (2.1) bounds its depth
by its boundary length.  What remains unproved is the global composition:
different rural pages must still be shown to use one compatible rotation
and one common apex pair, or an interface must yield the labelled rooted
model.

The theorem says nothing about a nonplanar three-connected torso.  It
also does not turn a two- or three-vertex separator inside the carrier
into an ambient separator of the host.
