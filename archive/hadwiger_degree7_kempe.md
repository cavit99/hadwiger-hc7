# The degree-seven residual: a rooted (K_5) core and the exact sixth-bag gap

This note treats only the corrected minimum-degree-seven cell for a
minor-minimal counterexample to (mathrm{HC}_7).  It proves a stronger
Kempe-rooted conclusion than the earlier pseudoforest argument, but it does
**not** eliminate the cell.

## 1. Standing hypotheses

Let (G) be a proper-minor-minimal graph with

\[
 \chi(G)=7,\qquad \eta(G)=6,
\]

and let (v) be a vertex of degree seven.  Put

\[
 H=G-v,\qquad N=N_G(v),\qquad |N|=7.
\]

The standard contraction-critical reductions give

\[
 \kappa(G)\ge 7,\qquad \kappa(H)\ge6,
 \qquad \alpha(G[N])=2.                                      \tag{1}
\]

Indeed Dirac's bound gives (alpha(G[N])\le d(v)-7+2=2), while
(alpha(G[N])=1) would make (N) a (K_7).  Every proper six-colouring
of (H) uses all six colours on (N), since otherwise the missing colour
could be assigned to (v).

More is supplied by edge contraction.  For every (w\in N), colour the
proper minor (G/vw) with six colours and expand the colouring to (H).
The colour of the contracted vertex occurs on (w), and on no vertex of
(N-\{w\}).  Thus (N) is colour-saturating and no proper subset of (N)
is colour-saturating.

Write

\[
 Q:=\overline{G[N]}.
\]

By (1), (Q) is triangle-free.

## 2. The exact repeated-pair Kempe structure

Fix any proper six-colouring (c) of (H).  Since all six colours occur
on the seven vertices of (N), exactly one colour, say colour (0), occurs
twice.  Write its two vertices as (a,b), and write the five vertices with
unique colours as

\[
 U=\{u_1,\ldots,u_5\},\qquad c(u_i)=i.
\]

Necessarily (ab\notin E(G)).

### Lemma 2.1 (unique roots are completely Kempe-connected)

For every (i\ne j), (u_i) and (u_j) belong to one component of
(H[c^{-1}(\{i,j\})]).

**Proof.**  If they belonged to different components, interchange colours
(i,j) on the component containing (u_i).  The vertex (u_i) is the only
colour-(i) vertex of (N), and the unique colour-(j) vertex (u_j) is
not in that component.  The resulting proper six-colouring therefore omits
colour (i) on (N), contrary to saturation.  (square)

### Lemma 2.2 (attachment to the repeated pair and Kempe pivot)

For each (u_i\in U), its ((0,i))-Kempe component contains at least one
of (a,b).  If it contains (a) but not (b), interchanging colours
(0,i) on that component gives another proper six-colouring whose repeated
pair on (N) is ({u_i,b}).  Symmetrically, if it contains (b) but not
(a), the new repeated pair is ({u_i,a}).

**Proof.**  If the component containing (u_i) contained neither (a) nor
(b), swapping it would remove the unique colour (i) from (N).  In the
one-end case the claimed colour multiplicities follow immediately after the
swap.  The new repeated pair is nonadjacent because the swapped colouring
is proper.  (square)

Let (R) be the graph on (N) whose edges are the pairs which occur as the
repeated pair in at least one six-colouring of (H).  Then (R\subseteq Q).
The contraction colouring associated with (w) has its repeated pair in
(N-\{w\}).  Consequently, for every (w\in N), (R) has an edge not
incident with (w).  In particular,

\[
 \nu(R)\ge2.                                                \tag{2}
\]

To see (2), if a triangle-free graph has matching number at most one, all
of its nonempty edges have a common endpoint (the only other pairwise-
intersecting family of two-sets is a triangle).  Taking that endpoint as
(w) contradicts the preceding property.  In particular (Q) has a
two-edge matching, and (G[N]) is five-colourable.

## 3. An unconditional rooted (K_5) core

We use the following theorem of Kriesell and Mohr, *Kempe Chains and Rooted
Minors* (2022), Theorem 7:

> Every graph on five vertices with at most six edges has property ((*)).

In the form used here, if (F) is such a graph on a rainbow transversal
(U), and the ends of every edge of (F) are in a common bichromatic
component, then the host has pairwise disjoint connected bags rooted at
(U), adjacent for every edge of (F).

### Theorem 3.1 (five unique roots always root a (K_5))

For every proper six-colouring (c) of (H), the five unique-colour
vertices (U) are the roots of a (K_5)-model

\[
 \mathcal B=(B_1,\ldots,B_5)
\]

in (H).  Moreover, the bags may be chosen inside the union (W) of the
five unique colour classes.  In particular (a,b\notin\bigcup_iB_i).

**Proof.**  Let

\[
 F=\overline{H[U]}.
\]

As (F\subseteq Q), it is triangle-free.  Mantel's theorem on five vertices
gives (|E(F)|\le\lfloor 5^2/4\rfloor=6).  Lemma 2.1 says that every edge
of (F) has Kempe-connected ends.  Apply the quoted Kriesell--Mohr theorem
to the restriction of (H) to (W), obtaining an (F)-model rooted at
(U).  If (u_iu_j\notin E(F)), then (u_iu_j\in E(H)), and this root edge
joins the corresponding bags.  Thus every two bags are adjacent, so they
form a rooted (K_5)-model.  Since the repeated colour class was deleted
when passing to (W), neither (a) nor (b) is in a bag.  (square)

This removes the earlier exceptional (K_{2,3}) complement case: although
(K_{2,3}) is not a pseudoforest, it is one of the six-edge graphs covered
by the Kriesell--Mohr theorem.

## 4. The exact sixth-bag obstruction

### Lemma 4.1 (connected-complement upgrade)

Let (mathcal B) be a model supplied by Theorem 3.1.  If (a) and (b)
belong to one component (D) of

\[
 H-\bigcup_{i=1}^5B_i,
\]

then (G) has a (K_7)-minor.

**Proof.**  The set (D) is connected and disjoint from the five bags.
For every (i), at least one of (au_i,bu_i) is an edge: otherwise
({a,b,u_i}) would be an independent set in (G[N]), contrary to (1).
Thus (D) is adjacent to every (B_i).  The six bags
(D,B_1,\ldots,B_5) form a (K_6)-model in (H), and every bag meets
(N).  Adding the singleton bag ({v}) gives a (K_7)-model in (G).
(square)

Hence a degree-seven counterexample must satisfy the following sharp
locking condition:

\[
 \boxed{\text{For every six-colouring and every rooted model from
 Theorem 3.1, its five bags separate the repeated vertices }a,b.} \tag{3}
\]

Six-connectivity does not immediately contradict (3): the separator is the
union of five connected bags, not a set of five vertices.  Contracting the
bags first can destroy the original connectivity, so treating the bags as
five separator vertices is invalid.  The unresolved operation is a
**non-separating rooted (K_5)** construction, not the existence of the
rooted (K_5) itself.

## 5. Components outside the closed neighbourhood

Let (mathcal C) be the set of components of (G-N[v]), and put
(m=|\mathcal C|).  Every (C\in\mathcal C) has

\[
 N_G(C)=N.                                                  \tag{4}
\]

Indeed (N_G(C)\subseteq N), and a smaller neighbourhood would be a
separator of order at most six in the seven-connected graph (G).

There is at least one such component.  Otherwise (G) has eight vertices,
and (delta(G)\ge7) makes it (K_8).  There are at most two:

### Lemma 5.1 (three exterior components give the minor)

If (m\ge3), then (G) has a (K_7)-minor.

**Proof.**  By (R(3,3)=6) and (alpha(G[N])=2), choose a triangle
(p_1p_2p_3) in (N).  Choose distinct
(q_1,q_2,q_3\in N-\{p_1,p_2,p_3\}) and distinct components
(C_1,C_2,C_3).  The six sets

\[
 \{p_1\},\{p_2\},\{p_3\},
 \quad C_1\cup\{q_1\},C_2\cup\{q_2\},C_3\cup\{q_3\}
\]

are connected and pairwise adjacent by (4), and all meet (N).  They form
an (N)-meeting (K_6)-model in (H), which extends with ({v}).
(square)

Similarly, if (m=2) and (G[N]) contains a (K_4), four singleton clique
bags and two bags (C_i\cup\{q_i\}) give an (N)-meeting (K_6)-model.
Thus

\[
 m=1,\quad\text{or}\quad m=2\text{ and }\omega(G[N])=3.     \tag{5}
\]

Here (omega(G[N])\ge3) again follows from (R(3,3)=6).  Also
(omega(G[N])\le4): a (K_5\subseteq N), together with (v), is a
(K_6); deleting those six vertices leaves a connected set adjacent to
every vertex of that (K_6), whose contraction gives (K_7).

Theorem 3.1 and (4) give one more exact restriction.  If some exterior
component (C) is disjoint from (\bigcup_iB_i), then
(C\cup\{a,b}) is a connected sixth bag adjacent to all five rooted bags.
Therefore, in a counterexample,

\[
 \boxed{\text{every rooted (K_5) model in Theorem 3.1 meets every
 component of }G-N[v].}                                    \tag{6}
\]

For (m=2), every such model must use both exterior components.  This is a
concrete two-component packing obstruction.

## 6. External Kempe paths supplied by contraction-criticality

The following useful specialization of Rolek--Song's Lemma 1.7 is valid in
the same setting.

### Lemma 6.1 (external missing-edge paths)

Let (S=\{s,t\}\subseteq N) be a nonedge.  For any set (M) of nonedges
of (G[N-S]), there are paths (P_{xy}) for (xy\in M), with ends (x,y)
and all internal vertices in (G-N[v]).  Paths belonging to vertex-disjoint
edges of (M) are vertex-disjoint.  More generally, two star groups whose
sets of terminals are disjoint have mutually disjoint path families.

**Proof.**  Contract the connected set ({v,s,t}) and six-colour the
resulting proper minor.  Give the contracted vertex colour (0).  The five
vertices of (N-S) receive the five other colours bijectively; otherwise a
missing colour can be assigned to (v) after expanding (s,t) with colour
(0).  For a nonedge (xy), a Kempe swap shows that the two distinct-colour
vertices (x,y) have a bichromatic path whose interior avoids (N[v]).
Paths for disjoint terminal pairs use disjoint pairs of colour classes, and
hence are vertex-disjoint.  The same colour-class observation separates
star groups on disjoint terminal sets.  (square)

This lemma supplies substantial exterior linkage, but it does not by itself
make the rooted (K_5) of Theorem 3.1 non-separating.  Paths in different
applications arise from different contraction colourings, and paths within
one star group may intersect.  Combining them as if all were simultaneously
disjoint would be invalid.

## 7. Near-(K_7) information and its precise limitation

Norin--Totschnig's local argument (Claim 4.4 in *Every graph with no
(K_7^{\vee})-minor is (6)-colorable*, 2025) also applies up to its final
contradiction.  If (G[N]) has no (K_4), the Moser-spindle configuration
and a rooted (C_5) construction produce a (K_7^{\vee})-model whose two
missing adjacencies have a common deficient singleton bag.  This is allowed
in a graph assumed only to have no (K_7)-minor.

If an exterior component were disjoint from that particular near-clique
model, it could be absorbed into the deficient singleton bag and would repair
both missing adjacencies, yielding (K_7).  The missing step is exactly the
same as (6): the rooted (C_5) bags may use vertices of every exterior
component.  Absorbing an arbitrary component without proving disjointness
would make branch sets overlap.

## 8. Exact remaining gap in the degree-seven cell

The repeated-pair analysis therefore reaches the following rigorously proved
endpoint.  Every six-colouring supplies

1. a nonadjacent repeated pair (a,b\in N);
2. five unique roots which unconditionally root a (K_5)-model using only
   their five colour classes;
3. collective adjacency of ({a,b}) to every rooted bag;
4. at most two exterior components, each attached to all seven vertices of
   (N); and
5. the external missing-edge paths of Lemma 6.1.

To eliminate the cell it is enough to prove that, for at least one colouring,
the rooted (K_5) bags can be chosen so that they do not separate (a) from
(b).  Equivalently for this route, one must rule out the simultaneous locks
(3) and (6).  Neither six-connectivity, the known property-((*)) theorem,
nor the external path lemma presently proves that non-separating choice.

### Sources used

- M. Rolek and Z.-X. Song, [*Coloring graphs with forbidden minors*](https://sciences.ucf.edu/math/zxsong/wp-content/uploads/sites/13/2018/04/Coloring-graphs-with-forbidden-minors.pdf), JCTB 127 (2017), Lemma 1.7.
- M. Kriesell and S. Mohr, [*Kempe Chains and Rooted Minors*](https://arxiv.org/abs/1911.09998), Theorem 7.
- S. Norin and A. Totschnig, [*Every graph with no (K_7^{\vee})-minor is (6)-colorable*](https://arxiv.org/abs/2507.03244), Claim 4.4.
