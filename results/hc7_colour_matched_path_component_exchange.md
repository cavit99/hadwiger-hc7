# Incorporating a colour-matched path through residual branch-set components

**Status:** written proof; separate internal audit GREEN.  This is a conditional
exchange criterion and an exact description of its obstruction.  It does
not prove `HC_7`.

## 1. Setup

Use the setup of the audited colour-matched path theorem, and assume that
`D_4` is the unique branch set of the contact-maximal `S`-rooted `K_4`
model which misses `T`.  Write

\[
 C=C_4,
 \qquad
 \mathcal K=\{X,D_1,D_2,D_3\}.
\]

Fix `s in D_4 cap S`, put `gamma=phi(s)`, and let `P` be the path supplied
by that theorem.  Thus `P` has one end in `C`, its other end in `T`, its
internal vertices avoid `C union T`, and

\[
       Y=\{u\}\cup(V(P)-C)
\]

is connected, disjoint from `C`, and adjacent to `C`.

For every `K in mathcal K`, put

\[
                         I_K=V(P)\cap K.               \tag{1.1}
\]

The path lies in `H[A union V_gamma]`, whereas `X=A union V_beta` and the
three `D_i` lie in the four-colour graph `R`.  In particular,
`gamma != beta`.  Therefore

\[
             I_X\subseteq A,
 \qquad
             I_{D_i}\subseteq V_\gamma\quad(1\le i\le3),             \tag{1.2}
\]

and every set in (1.2) is independent.

## 2. Component-transversal exchange

### Theorem 2.1

For every `K in mathcal K`, let `mathcal C_K` be the set of components of
`G[K-I_K]`.  Suppose one can choose

\[
                         L_K\in\mathcal C_K
                         \qquad(K\in\mathcal K)        \tag{2.1}
\]

such that:

1. every `L_K` is adjacent to both `C` and `z`; and
2. the four chosen subgraphs `L_K` are pairwise adjacent.

Then `G` contains a `K_7` minor.

#### Proof

The seven sets

\[
                   C,\quad Y,\quad\{z\},\quad
                   (L_K:K\in\mathcal K)               \tag{2.2}
\]

are pairwise disjoint and connected.  The set `C` is adjacent to `Y` by
the first edge of `P` leaving `C`, and `z` is adjacent to both `C` and
`Y` (to `C` because `D_4` meets `S`, and to `Y` through the edge `zu`).
The hypotheses give every adjacency among `C`, `z`, and the four `L_K`,
as well as every adjacency between two of the `L_K`.

It remains only to check adjacency to `Y`.  If `I_K` is nonempty, every
component of the connected graph `G[K]` after deleting `I_K` has an edge
to `I_K`, which is contained in `Y`.  If `I_K` is empty, then
`L_K=K`.  The set `X` is adjacent to `u`, and each `D_i` with `i<=3`
meets `T` because `D_4` is the unique deficient branch set.  Hence in
this case `L_K` is again adjacent to `u in Y`.  Thus (2.2) is an explicit
`K_7`-minor model.  \(\square\)

## 3. Exact separator produced by local failure

### Proposition 3.1

Let `K in mathcal K` and let `L` be a component of `G[K-I_K]`.  Then

\[
 N_G(L)=N_{I_K}(L)\mathbin{\dot\cup}N_{G-K}(L).        \tag{3.1}
\]

If `L` is nonadjacent to one of

\[
                    C,\quad\{z\},\quad
                    \mathcal K-\{K\},                \tag{3.2}
\]

then `N_G(L)` is the boundary of an actual separation with nonempty open
sides.  Its order is

\[
               |N_{I_K}(L)|+|N_{G-K}(L)|.             \tag{3.3}
\]

Consequently (3.3) is at least seven.  If it is at most seven for any
such `L`, it is exactly seven.

#### Proof

No vertex of `L` has a neighbour in a different component of
`G[K-I_K]`; this proves the disjoint identity (3.1).  The set `L` is one
open side of the separation with boundary `N_G(L)`.  A set in (3.2) to
which `L` is nonadjacent lies wholly outside `L union N_G(L)`, so the
other open side is nonempty.  Seven-connectivity gives the lower bound,
and the final assertion follows immediately.  \(\square\)

There is a second, genuinely simultaneous obstruction.  Even if every
part `mathcal C_K` has components adjacent to both anchors, the
four-partite graph whose vertices are those components and whose edges
record adjacency in `G` may have no transversal `K_4`.  This is a
component-compatibility obstruction and need not be represented by one
separation of the form (3.1).

## 4. What path minimality proves

Choose `P` to minimize

\[
        |V(P)\cap(X\cup D_1\cup D_2\cup D_3)|         \tag{4.1}
\]

among all paths in `H[A union V_gamma]` with one end in `C`, one end in
`T`, and no internal vertex in `C union T`.  This family is nonempty by
the preceding theorem.
Put

\[
 W=X\cup D_1\cup D_2\cup D_3,
 \qquad I=V(P)\cap W,
\]

and form the pruned bichromatic graph

\[
       B^*=H[A\cup V_\gamma]-(W-I).                  \tag{4.2}
\]

### Proposition 4.1

For every `x in I`, the graph `B^*-x` has no `C`--`T` path.

#### Proof

If such a path existed, trim it at its last vertex in `C` before its first
subsequent vertex in `T`.  The result would be another admissible
colour-matched path.  By (4.2), it could meet `W` only in `I-\{x\}` and
would therefore improve (4.1), a contradiction.  \(\square\)

Thus every intersection with a protected branch set is an individually
unavoidable one-vertex blocker for the `C`--`T` path problem in the pruned
two-colour graph.  An internal member of `I-T`, when both terminal sides
remain nonempty after its deletion, is a one-vertex `C`--`T` separator
there.  This does not give a small separator in `G`: restoring `W-I`, the
other four colour classes, and the two poles can enlarge the full boundary
without bound.

## 5. Minor-critical boundary-colour invariant

### Proposition 5.1

Let `L` be a nontrivial connected proper vertex set of `G`, and suppose
`chi(G)=7` while every proper minor of `G` is six-colourable.  In every
six-colouring of `G/L`:

1. at most five colours occur on `N_G(L)`; and
2. if `chi(G[L])<=r`, at least `7-r` colours occur on `N_G(L)`.

In particular, if `L` is a nontrivial component of `G[X-I_X]`, exactly
five colours occur on its boundary in every six-colouring of `G/L`.

For a singleton `L={v}`, every six-colouring of `G-v` uses all six colours
on `N_G(v)`.

#### Proof

In a six-colouring of `G/L`, the colour on the contracted vertex is absent
from all of its neighbours, proving the first assertion.  If at most
`6-r` colours occurred on `N_G(L)`, at least `r` colours would be absent
there.  Colour `G[L]` with those colours and combine it with the colouring
outside `L`; this would six-colour `G`, a contradiction.  Hence at least
`7-r` boundary colours occur.

Every component of `G[X-I_X]` is bipartite, so `r=2`; the lower and upper
bounds are both five.  Finally, if one of the six colours were absent from
`N_G(v)` in a colouring of `G-v`, assigning that colour to `v` would
six-colour `G`.  \(\square\)

## 6. Exact remaining step

Theorem 2.1 converts the branch-set exchange into a finite four-family
selection problem after a colour-matched path has been chosen.  Proposition
3.1 turns the loss of an anchor, or of adjacency to an entire other
protected branch set, into an actual separator.  Failure of adjacency
between particular selected residual components remains the separate
four-partite compatibility obstruction.  Proposition 5.1 supplies a sharp
five-colour boundary condition for every residual component inside the
bipartite branch set.

What remains open is to prove that the full proper-minor colouring
responses either make one of the local separators have order seven or
force an anchor-complete transversal `K_4` among the residual components.
Neither path minimality nor connectivity alone proves that implication.

## 7. Dependencies

- [colour-matched deficient-branch-set path](../results/hc7_colour_matched_repair_path.md)
- [star--Kempe compression](../results/hc7_star_kempe_five_core_compression.md)
- [deficient-component separator](../results/hc7_maximal_rooted_k4_deficient_component_separator.md)
