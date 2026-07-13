# Minimum degree forces an off-face attachment in every planar carrier

## Status

This is a uniform Euler-discharge closure for the rural branch of the
locked two-row theorem.  In the `HC_7` host it proves that a
four-connected planar old exterior carrier can never have all of its
external attachment vertices on the one coherent portal face.

## Theorem 1 (planar carrier degree escape)

Let `G` be a graph with minimum degree at least six.  Let `K` be a
vertex set such that `G[K]` is a four-connected planar graph.  Suppose
there is a plane embedding of `G[K]` with facial cycle `F` such that

\[
 N_G(v)\subseteq K\qquad\text{for every }v\in K-V(F).    \tag{1.1}
\]

Then no such configuration exists.  Equivalently, in every plane
embedding of a four-connected planar carrier in `G`, every face misses
at least one carrier vertex having a neighbour outside the carrier.

### Proof

Put `n=|K|`, `m=|E(G[K])|`, and `f=|V(F)|`.  Four-connectivity gives
minimum degree at least four inside `G[K]`.  Every vertex outside `F`
has no external neighbour by (1.1), so its degree in `G[K]` equals its
degree in `G` and is at least six.  Therefore

\[
 2m=\sum_{v\in K}d_{G[K]}(v)
       \ge 6(n-f)+4f=6n-2f.                               \tag{1.2}
\]

On the other hand, take `F` as the outer face.  Every other face of the
simple plane graph has length at least three.  Euler's formula gives the
standard outer-face bound

\[
                         m\le3n-3-f,
\]

and hence

\[
                         2m\le6n-6-2f.                    \tag{1.3}
\]

Inequalities (1.2) and (1.3) say `6n-2f<=6n-6-2f`, an impossibility.
\(\square\)

## Theorem 2 (quantitative off-face load)

In the same plane setting, assume `delta(G)>=d>=6` but do not impose
(1.1).  Let

\[
 T_F=|E_G(K-V(F),V(G)-K)|
\]

count the external edges whose carrier end is strictly off `F`.  Then

\[
                  T_F\ge (d-6)(n-f)+6.                  \tag{2.1}
\]

In particular `T_F>=6`; for the `HC_7` value `d=7`,

\[
                         T_F\ge n-f+6.                  \tag{2.2}
\]

### Proof

Every facial vertex has internal degree at least four.  For a vertex
`v` off `F`,

\[
 d_{G[K]}(v)=d_G(v)-|E_G(v,V(G)-K)|.
\]

Summing and using `delta(G)>=d` gives

\[
 2m\ge d(n-f)-T_F+4f.
\]

Combine this with `2m<=6n-6-2f` and rearrange to obtain (2.1).
\(\square\)

For `d=7`, (2.2) says that the off-face vertices collectively have at
least six more external incidences than their number.  Thus some off-face
carrier vertex has at least two literal external neighbours.

## Theorem 3 (at least three distinct off-face portal vertices)

Retain the plane setting and assume `delta(G)>=7`.  Put

\[
 I=V(K)-V(F),\qquad
 X=\{x\in I:N_G(x)-K\ne\varnothing\}.
\]

Then

\[
                         3|X|\ge |I|+6.                  \tag{3.1}
\]

Consequently `|I|>=3` and `|X|>=3`.  Thus the degree escape supplies at
least three distinct off-face carrier endpoints, in addition to the
edge-incidence bound `T_F>=|I|+6` from Theorem 2.

### Proof

Write `f=|F|`, `h=|I|`, `p=|X|`, and `m=|E(G[K])|`.  Every vertex of
`F` has carrier degree at least four.  Every vertex of `I-X` has no
external neighbour, so its carrier degree equals its degree in `G` and
is at least seven.  Every member of `X` still has carrier degree at least
four by four-connectivity.  Therefore

\[
 2m\ge4f+7(h-p)+4p=4f+7h-3p.                            \tag{3.2}
\]

The outer-face Euler bound is

\[
 2m\le6(f+h)-6-2f=4f+6h-6.                             \tag{3.3}
\]

Comparing (3.2) and (3.3) gives (3.1).  Since `p<=h`, it also gives
`3h>=h+6`, whence `h>=3`; substituting in (3.1) gives `p>=3`.
\(\square\)

## Corollary 4 (forced escape from the locked portal face)

Let `G` be a hypothetical `HC_7` counterexample and let `K` be a
four-connected old exterior carrier in the rural outcome of
`../results/hc7_near_k7_locked_two_row_linkage.md`.  Let `F` be the
coherent face containing every usable representative of the four locked
portal families.  Then some vertex of `K-F` has a literal neighbour in
the actual adhesion `S=N_G(K)`.

In fact, Theorem 2 gives an off-face vertex with at least two distinct
neighbours in `S`, while Theorem 3 gives at least three distinct
off-face attachment vertices.

In particular, the fully rural hypothesis in the active-face list-splice
theorem can never hold for this carrier: its off-face alternative is
forced before any colouring is chosen.

### Proof

A hypothetical counterexample has minimum degree at least seven, hence
at least six.  If every carrier vertex with a neighbour in `S` lay on
`F`, condition (1.1) would hold, contradicting Theorem 1.  \(\square\)

## Exact label residue

There is no Hall-unusable occurrence inside the four locked portal
families.  Suppose `P_1,...,P_4` have a full SDR.  Every vertex
`w in P_1 union ... union P_4` occurs in a full SDR: take any SDR; if its
image omits `w`, choose `i` with `w in P_i` and replace only the
representative of `P_i` by the unused vertex `w`.  Distinctness is
preserved.

The coherent-face theorem therefore puts the entire union

\[
                         A_L\cup A_R\cup P_H\cup P_Q
\]

on `F`.  Every off-face external attachment forced by Corollary 4 has a
genuinely extra literal role.  In the one-missing path-cut cell it cannot
attach to either path side or to the two locked rows `H,Q`; coherent
transport also excludes the fixed missed twin.  Hence it attaches to one
of the three remaining common foreign rows.

Assign each of the at least three vertices in `X` one of its extra row
labels.  Either all three common rows receive an off-face portal, or one
common row receives at least two distinct off-face portal vertices.  In
general some common row has at least `ceil(|X|/3)` such vertices.

The next exchange must spend these extra-row incidences.  At `delta=7`
there are at least `n-f+6` such off-face edges and one off-face vertex has
two distinct external neighbours.  Those two neighbours may still lie in
one nonsingleton foreign bag, so the count does not yet give two literal
row labels.  A valid continuation must split that owner bag
label-faithfully, produce a boundary-state splice, or put the owner
society into the same global apex expansion.
