# Excess-one nested descent with literal boundary data

**Status:** written conditional theorem; adjacent internal audit GREEN.  The theorem
closes every excess-one nested descent whose new order-seven boundary is a
split graph, classifies the only possible five-chromatic new boundary, and
records the exact labelled order-eight obstruction when ordinary nested
descent fails.  It does not eliminate a nonsplit four-colourable boundary or
the boundary-full order-eight obstruction, and therefore does not prove
`HC_7`.

## 1. Excess-one setup

Let `G` be seven-connected and `K_7`-minor-free, and suppose that every
proper minor of `G` is six-colourable.  Let `R` be a nonempty connected
vertex set, put

\[
                         X=N_G(R),\qquad |X|=8,             \tag{1.1}
\]

and assume that `G-(R\cup X)` is nonempty.  Thus `R` is a component of
`G-X`, and its literal separator excess is one.

For a separation with boundary `Y`, an **extension language** means the set
of equality partitions of the literal vertices of `Y` induced by proper
six-colourings of the corresponding closed side.  No quotient vertex is
treated as a literal boundary vertex.

## 2. Exact order-seven descent

### Theorem 2.1 (split descended boundaries synchronize)

Let `C` be a component of `G-X` other than `R`.  If `C` misses a vertex
`x in X`, then

\[
                         N_G(C)=X-\{x\}=:Y.                \tag{2.1}
\]

In particular, `Y` is the boundary of an actual order-seven separation.
For every nonempty independent set `I\subseteq Y`, each of the two closed
shores has a proper six-colouring in which `I` is an exact boundary colour
class.

If `G[Y]` is a split graph, the two closed shores have a common equality
partition on `Y`.  Consequently, if `G` is not six-colourable, every
order-seven boundary obtained by (2.1) is nonsplit.

#### Proof

Every neighbour of `C` lies in `X`.  Since `C` misses `x`, its neighbourhood
has order at most seven.  It separates `C` from the nonempty component `R`.
Seven-connectivity therefore gives

\[
                         7\le |N_G(C)|\le7,
\]

which proves (2.1).  The separation is actual because `C` and `R` lie in
different nonempty components after deleting `Y`.

Both open sides contain a connected subgraph adjacent to every literal
vertex of `Y`: use `C` on its own side and `R` on the other.  Fix a nonempty
independent set `I\subseteq Y`.  Contract a spanning tree of

\[
                         C\cup I.                          \tag{2.2}
\]

The set in (2.2) is connected because `C` has a neighbour at every vertex
of `I`.  It contains an edge and at least two vertices, so the contraction
is a proper minor.  In a six-colouring of that minor, its representative is
adjacent to every vertex of `Y-I`, because `C` is `Y`-full.  Restrict the
colouring to the unchanged closed side containing `R`, and give every
literal vertex of `I` the representative's colour.  This pullback is proper:
`I` is independent, every edge from `I` to an unchanged vertex became
incident with the representative, and the representative is adjacent to
every member of `Y-I`.  Hence `I` is one exact boundary colour class, not
merely part of a larger class.  Contracting a spanning tree of `R\cup I`
gives the symmetric statement for the closed side containing `C`.  This
proves the exact-block assertion, with both contractions and both pullbacks
literal.

Now suppose that `G[Y]` is split.  Write

\[
    Y=Q\mathbin{\dot\cup}J,           \tag{2.3}
\]

where `Q` is a clique and `J` is independent.  The set `J` is nonempty:
otherwise the seven literal vertices of `Y` form a `K_7` subgraph.  Apply the
preceding exact-block construction with `I=J` on both sides.  If `|Q|=6`,
the contraction representative and the six literal vertices of `Q` form a
`K_7` in a proper minor.  Equivalently, exactness would require seven
different boundary colours in a six-colouring.  This is already a
contradiction, so assume `|Q|<=5`.

In any proper
boundary partition having `J` as an exact block, every vertex of the clique
`Q` is a singleton block, and distinct vertices of `Q` have distinct
colours.  Thus both contractions return the same equality partition

\[
                         J\mid\{q\}\ (q\in Q).             \tag{2.4}
\]

After a permutation of the six colour names, the two closed-side colourings
agree at every literal vertex of `Y`.  There is no edge between the two open
sides, so they glue to a proper six-colouring of `G`.  This proves the last
assertion.  \(\square\)

The proof does not claim that an arbitrary seven-set linkage transports the
old equality blocks.  Such a linkage may send two vertices of the same old
block to adjacent vertices of `Y`.  The split hypothesis avoids that
unjustified step by producing one common partition directly on the literal
new boundary.

### Proposition 2.2 (the unique five-chromatic boundary quotient)

Let `H` be a graph on seven vertices.  If

\[
                    \overline {K_2}\vee H
                    \quad\hbox{has no `K_7` minor},        \tag{2.5}
\]

then either `H` is four-colourable or

\[
                              H\cong K_2\vee C_5.          \tag{2.6}
\]

The exception in (2.6) is sharp: the graph in (2.5) has no `K_7` minor when
`H=K_2\vee C_5`.

Consequently, for the descended boundary `Y` in Theorem 2.1,

\[
       \chi(G[Y])\le4
       \quad\hbox{or}\quad
       G[Y]\cong K_2\vee C_5.                             \tag{2.7}
\]

#### Proof

Assume `\chi(H)\ge5` and choose an induced vertex-critical subgraph `J` with
`\chi(J)\ge5`.  A critical `k`-chromatic graph has minimum degree at least
`k-1`.

If `\chi(J)\ge6`, then `|J|\le7` and the minimum-degree bound shows directly
that `J` contains a `K_6`.  Indeed, at order six it is `K_6`; at order seven
its complement has maximum degree at most one, and a nonempty complementary
matching either lowers the chromatic number to at most five or leaves a
vertex deletion still six-chromatic, contrary to criticality.  One of the
two vertices of `\overline {K_2}` together with that `K_6` is a `K_7`
subgraph, contrary to (2.5).  Hence `J` is five-critical.

If `|J|=5`, then `J=K_5`.  Since `H` has two further vertices, call them
`a,b`, and write `p,q` for the two vertices of `\overline {K_2}`.  The seven
sets

\[
             \{p,a\},\quad \{q,b\},\quad
             \{v\}\quad(v\in V(J))                      \tag{2.8}
\]

are disjoint and connected.  The first two are adjacent through the literal
edges `pb` and `qa`, and both meet every `K_5` singleton through `p` or `q`.
Thus (2.8) is an explicit `K_7`-minor model, a contradiction.

There is no five-critical graph of order six.  To see this, its complement
has maximum degree at most one, so it is `K_6` with a matching removed.
Chromatic number five forces exactly one removed edge, but deleting either
endpoint of that nonedge leaves a `K_5`, contradicting
vertex-criticality.

It remains that `|J|=7`.  Put `F=\overline J`.  Then `\Delta(F)\le2`.  A
colouring of `J` is a clique cover of `F`.  If `F` contains a triangle, its
three vertices already save two colour classes.  Any further edge would
make `J` four-colourable; with no further edge, deleting a triangle vertex
leaves a graph whose clique-cover number is still five, contradicting
five-criticality.  Hence `F` is triangle-free.

For a triangle-free graph of maximum degree two, every clique has order at
most two, and therefore

\[
                     \chi(J)=7-\nu(F),                    \tag{2.9}
\]

where `\nu(F)` is the matching number.  Thus `\nu(F)=2`.  Five-criticality
also gives `\nu(F-v)=2` for every vertex `v`.  Each nontrivial component of a
maximum-degree-two graph is a path or a cycle.  A path or an even cycle has
a vertex whose deletion lowers its matching number; an odd cycle does not.
It follows that the only nontrivial component is an odd cycle.  Triangle
freeness and total matching number two force

\[
                              F\cong C_5\mathbin{\dot\cup}2K_1.
\]

Taking complements gives `J=H\cong K_2\vee C_5`, proving (2.6).

For sharpness, regroup the join as

\[
       \overline {K_2}\vee(K_2\vee C_5)
            =K_2\vee(\overline {K_2}\vee C_5).            \tag{2.10}
\]

The graph in the second parentheses is the planar pentagonal bipyramid, so
it has no `K_5` minor.  If the graph in (2.10) had a seven-branch-set clique
model, discard the at most two branch sets containing the two vertices of
the first `K_2`.  At least five pairwise adjacent branch sets would remain
entirely in the pentagonal bipyramid, giving a `K_5` minor there, a
contradiction.

Finally, contracting one `Y`-full connected subgraph on each side of the
separation in Theorem 2.1, and deleting all unused vertices, gives precisely
`\overline {K_2}\vee G[Y]`: the two representatives are nonadjacent and each
is adjacent to every literal vertex of `Y`.  This proves (2.7).  \(\square\)

The exceptional graph `K_2\vee C_5` is nonsplit.  Proposition 2.2 does not
assert that its two shore extension languages intersect; that would require
an additional proper-minor transition or a labelled minor construction.

## 3. Exact failure of excess-one component descent

### Theorem 3.1 (boundary-full order-eight obstruction)

Under (1.1), exactly one of the following holds.

1. Some component `C` of `G-X` other than `R` satisfies (2.1), so Theorem
   2.1 returns an actual order-seven separation.
2. Every component of `G-X` is adjacent to every literal vertex of `X`.

In outcome 2, if `G-X` has `m` components and `Q` is a clique in `G[X]`,
then

\[
                              m+|Q|\le6.                  \tag{3.1}
\]

This is the exact irreducible configuration for nested **component** descent
at excess one.

#### Proof

For a component `C` of `G-X`, its neighbourhood is contained in `X` and
separates it from another component.  Seven-connectivity gives
`|N_G(C)|\ge7`.  Since `|X|=8`, either `N_G(C)=X` or
`N_G(C)=X-{x}` for one literal `x in X`.  This proves the dichotomy.

For (3.1), first note that `|Q|\le6`, since otherwise seven vertices of
`Q` already form a `K_7` subgraph.  Suppose instead that
`m+|Q|\ge7`.  Choose `7-|Q|` distinct
components `C_i` and the same number of distinct anchors
`x_i in X-Q`.  The seven sets

\[
                 C_i\cup\{x_i\},\qquad \{q\}\ (q\in Q)  \tag{3.2}
\]

are disjoint and connected.  Two component sets are adjacent because each
component has a literal edge to the other set's anchor; every component set
is adjacent to every clique singleton; and the clique singletons are
pairwise adjacent.  Thus (3.2) is an explicit `K_7`-minor model, contrary to
the hypothesis.  \(\square\)

### Proposition 3.2 (placement of the old exact-seven labels)

Assume additionally the path-residual setup of
`../results/hc7_small_path_intersection_lobe.md`.  Thus

\[
 S=D\mathbin{\dot\cup}E\mathbin{\dot\cup}\{r,z\},
 \quad |D|=3,\quad |E|=2,
\]

`C_1,C_2` are the two named disjoint `S`-full connected subgraphs on the
coloured side, a prescribed `r-z` path avoids `C_2`, and

\[
 R=C_1-V(P),\quad
 \Lambda=S-N_G(R),\quad U=N_G(R)-S.
\]

If `\varepsilon(R)=1` and outcome 2 of Theorem 3.1 holds, then all of the
following identities and incidences are literal:

\[
 \begin{aligned}
 X&=(S-\Lambda)\mathbin{\dot\cup}U,\\
 |U|&=|\Lambda|+1,\\
 S\cap X&=S-\Lambda.
 \end{aligned}                                           \tag{3.3}
\]

Moreover, there is one component `F` of `G-X` containing the whole opposite
open side together with all lost boundary vertices:

\[
                              B\cup\Lambda\subseteq F.    \tag{3.4}
\]

Both `R` and `F` are adjacent to every literal vertex of `X`.  Hence every
retained old label in `S-\Lambda` and every external attachment in `U` has a
literal neighbour in each of `R,F`.  The named subgraph `C_2` may meet `X`
through `C_2\cap U`; every component of `C_2-X` which has a neighbour in
`\Lambda` lies in `F`.  Thus (3.3)--(3.4) preserve all seven old labels and
locate exactly where the new boundary can cut the second named subgraph;
they do not silently replace it by a quotient vertex.

#### Proof

The identities in (3.3) are the definitions of `\Lambda,U,X=N_G(R)` and the
equation

\[
                 |X|=|U|+7-|\Lambda|=8.
\]

The separator-excess theorem gives `|\Lambda|\ge2`, so in particular
`\Lambda` is nonempty.

Every component of `G[B]` has all its neighbours in `S` and is separated
from the nonempty side containing `R`.  Seven-connectivity makes each such
component adjacent to every vertex of `S`.  Fix `\lambda\in\Lambda`.  Every
component of `G[B]` has an edge to `lambda`, and every other vertex of
`\Lambda` has an edge to every component of `G[B]`.  Consequently
`B\cup\Lambda` is connected.  It is disjoint from `X` by (3.3), proving
(3.4).  Outcome 2 of Theorem 3.1 makes both `R` and `F` `X`-full.  The last
assertion follows because `C_2\cap X=C_2\cap U`, while any component of
`C_2-X` having a neighbour in `\Lambda\subseteq F` belongs to the same
component `F` of `G-X`.  \(\square\)

The same bookkeeping applies to the non-direct first-entry component `K`
of `../results/hc7_exact7_first_entry_bridge_reduction.md`: with

\[
 X=N_G(K)=T_K\mathbin{\dot\cup}A_K,
\]

the old boundary vertices in `T_K` lie literally in `X`, the vertices of
`S-T_K` lie in the far component containing the opposite open shore, and
the named subgraphs `P_1,P_2` meet `X` exactly in their attachment vertices
from `A_K`.  In the irreducible outcome every vertex of `T_K\cup A_K` has
a literal neighbour on both sides.  This is the decorated order-eight
configuration that a label-preserving external-attachment exchange must
close.

## 4. Sharpness of the geometric conclusion

### Proposition 4.1 (seven-connected `K_7`-minor-free full interface)

There is a seven-connected `K_7`-minor-free graph with a connected set `R`
such that `|N_G(R)|=8`, the far side is nonempty, and every component behind
that eight-set is boundary-full.  Hence seven-connectivity and `K_7`-minor
exclusion alone cannot replace outcome 2 of Theorem 3.1 by a strict descent.

#### Construction and proof

Let `I` be the icosahedral graph on `0,...,11` with edge set

```text
01 05 07 08 0-11 12 15 16 18 23 26 28 29 34
36 39 3-10 45 46 4-10 4-11 56 5-11 78 79
7-10 7-11 89 9-10 10-11
```

(Hyphens disambiguate the two-digit vertex labels.)  This is the usual
NetworkX labelling of the planar icosahedral graph.  Let

\[
                              G=\overline {K_2}\vee I,
\]

with nonadjacent join vertices `a,b`.  In `I`, put

\[
 \begin{aligned}
 S_0&=\{0,1,2,3,4,11\},\\
 R&=\{5,6\},\\
 F&=\{7,8,9,10\}.
 \end{aligned}
\]

The graph `I[S_0]` is the six-cycle

\[
                         0,1,2,3,4,11,0.
\]

The sets `R,F` are the two components of `I-S_0`; both are connected and
each is adjacent to every vertex of `S_0`.  Since `a,b` are complete to
`I`, the literal set

\[
                         X=S_0\cup\{a,b\}=N_G(R)          \tag{4.1}
\]

has order eight, and `G-X` has exactly the two `X`-full components `R,F`.

The graph is seven-connected.  If either `a` or `b` remains after deleting
fewer than seven vertices, it joins all remaining icosahedral vertices; if
both are deleted, fewer than five vertices were deleted from the
five-connected graph `I`.  Conversely, deleting `a,b` and the five
neighbours in `I` of one icosahedral vertex isolates that vertex.

Finally, `G` has no `K_7` minor.  In a seven-branch-set clique model, at
most two branch sets contain `a` or `b`.  At least five branch sets would
therefore lie entirely in the planar graph `I`, giving a `K_5` minor in a
planar graph, which is impossible.

This example is deliberately outside the full counterexample hypotheses:
it is six-colourable (indeed, the planar graph `I` uses at most four colours
and `a,b` can share a fifth), it is not strongly seven-contraction-critical,
and it does not realize the complete hard exact-seven `(1,2)` first-entry
data.  It is a sharp counterexample only to a connectivity-and-minor-
exclusion proof of strict component descent.  The missing input is therefore
a literal use of the proper-minor colour responses together with the named
subgraphs, not a stronger separator-order calculation.  \(\square\)

## 5. Exact remaining condition

At excess one, a complete label-preserving theorem must still close exactly
one of the following two host configurations.

1. A descended order-seven boundary `Y=X-{x}` whose graph is nonsplit
   (with `K_2\vee C_5` the unique possible five-chromatic boundary) and whose
   two exact-block-complete extension languages have not yet been shown to
   intersect.
2. The decorated boundary-full order-eight interface of Theorem 3.1 and
   Proposition 3.2, where the seven old labels are placed as in (3.3)--(3.4)
   and a named connected subgraph can be cut by the literal eight-set.

An unpaired seven-path linkage between the old and new boundaries is not
enough: its endpoint permutation need not send the three vertices of `D`
and the two vertices of `E` to independent sets.  The required extra
condition is a block-compatible rooted transfer, or an all-operation
proper-minor transition which directly produces a common equality partition.
No such transfer is asserted here.
