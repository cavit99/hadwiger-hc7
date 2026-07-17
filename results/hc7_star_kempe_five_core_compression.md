# A star-Kempe colouring compresses the adjacent-pair residue to a tight five-chromatic core

**Status:** written proof; separate internal audit GREEN.  This is a conditional
structural theorem inside the adjacent-pair programme.  It does not prove
`HC_7`.

## 1. Setup

Let `G` be a graph such that

1. `chi(G)=7`;
2. every proper minor of `G` is six-colourable; and
3. `G` has no `K_7` minor.

Let `zu` be an edge, put `H=G-{z,u}`, and suppose `chi(H)=6`.  Let `phi`
be a proper six-colouring of `H` with the following adjacent-pair palette
properties.  There is a colour `alpha` such that

- its colour class `A` is nonempty and anticomplete to `{z,u}`; and
- each of `z,u` has a neighbour in every colour different from `alpha`.

Assume in addition the **star-Kempe condition**

\[
             H[A\cup V_\gamma]\text{ is connected}
             \qquad(\gamma\ne\alpha),                 \tag{1.1}
\]

where `V_gamma` is the `gamma`-colour class.  Thus (1.1) concerns the
entire two-colour graph, not merely the component containing the pole
neighbours.

Fix `beta != alpha`, and write

\[
 X=A\cup B,\qquad B=V_\beta,\qquad
 R=H-X,\qquad Q=G-X.                                  \tag{1.2}
\]

In particular, `Q` contains the two adjacent vertices `z,u`, while `R`
is the subgraph induced by the other four colour classes.
For a set outside `Q`, such as `A` or `B`, write
`N_Q(B)=N_G(B)\cap V(Q)`.

## 2. Tight-core compression theorem

### Theorem 2.1

Under the setup above, the following hold for every choice of `beta`.

1. `X` is a connected dominating subgraph of `G`: every vertex of `Q`
   has a neighbour in `X`.
2. `chi(R)=4`, `chi(Q)=5`, the contraction `G/X` is exactly
   six-chromatic, and `Q` has no `K_6` minor.
3. In every proper five-colouring of `Q`, the set `R` uses all five
   colours.  The set `N_Q(B)` also uses all five colours.
4. Both `Q-z` and `Q-u` are five-chromatic.
5. There are two explicit oppositely oriented near-`K_7` models:
   - five branch sets `{u},M_1,...,M_4` form a `K_5` model in `Q-z`,
     and the seven sets

     \[
                    \{z\},\ \{u\},\ X,\ M_1,\ldots,M_4             \tag{2.1}
     \]

     are pairwise adjacent except possibly for pairs `({z},M_i)`;
   - symmetrically, five branch sets `{z},M'_1,...,M'_4` form a
     `K_5` model in `Q-u`, and

     \[
                    \{u\},\ \{z\},\ X,\ M'_1,\ldots,M'_4          \tag{2.2}
     \]

     are pairwise adjacent except possibly for pairs `({u},M'_i)`.

Consequently, if the outside pole in either (2.1) or (2.2) contacts all
four remaining branch sets, those seven sets are an explicit `K_7`
minor model in `G`.

### Proof

Every colour class of `phi` is nonempty because `chi(H)=6`.  The graph
`H[A\cup B]` is connected by (1.1), so `X` is connected.

Let `v` be a vertex of `R`, and let `gamma` be its colour.  The induced
two-colour graph `H[A\cup V_gamma]` is connected and contains the two
nonempty independent sets `A` and `V_gamma`.  Hence `v` is not isolated
in that graph and has a neighbour in `A\subseteq X`.  Each of `z,u` has a
`beta`-coloured neighbour, which belongs to `B\subseteq X`.  Thus every
vertex of `Q`, whose vertex set is `V(R)\cup\{z,u\}`, has a neighbour in
`X`, proving item 1.

The displayed colouring gives `chi(R)\leq4`.  If `R` were three-colourable,
use three colours on `R` and two disjoint new colours on the bipartite
graph `H[X]`; this would five-colour `H`, contrary to `chi(H)=6`.  Hence

\[
                              \chi(R)=4.                \tag{2.3}
\]

Contract the connected set `X` to one vertex `x`.  Because `X` dominates
`Q`, the vertex `x` is universal in the resulting proper minor, and hence

\[
                         \chi(G/X)=\chi(Q)+1.           \tag{2.4}
\]

Every proper minor of `G` is six-colourable, so (2.4) gives
`chi(Q)\leq5`.  On the other hand, a four-colouring of `Q` together with a
two-colouring of the bipartite graph `H[X]`, using disjoint palettes,
would six-colour `G`.  Therefore `chi(Q)=5`.
Equation (2.4) now also gives `chi(G/X)=6`.

If `Q` contained a `K_6` minor, its six branch sets together with the
connected dominating set `X` would be seven pairwise adjacent branch
sets in `G`.  This would be a `K_7` minor, so `Q` is `K_6`-minor-free.
This proves item 2.

Now let `psi` be any proper five-colouring of `Q`.  Suppose first that a
colour `delta` is absent from `R`.  Colour every vertex of `A` with
`delta` and every vertex of `B` with one new sixth colour.  This is proper:
`A` is anticomplete to `{z,u}`, all its other neighbours outside `X` lie
in `R`, and `delta` is absent there; the sixth colour is new; and the two
sides of `H[X]` receive different colours.  We would obtain a
six-colouring of `G`, a contradiction.  Hence `R` uses all five colours
under `psi`.

Suppose instead that a colour `delta` is absent from `N_Q(B)`.  Give `B`
the colour `delta` and `A` one new sixth colour.  Again this extends `psi`
to a proper six-colouring of `G`, a contradiction.  Thus `N_Q(B)` also
uses all five colours.  This proves item 3.  Notice that the first
assertion can equivalently be read as the colourfulness of `N_Q(A)=R`:
the equality follows from the domination argument and the fact that `A`
is anticomplete to the poles.

If `Q-z` were four-colourable, use such a colouring and give `z` a new
fifth colour.  This is a five-colouring of `Q` in which `R\subseteq Q-z`
uses at most four colours, contrary to item 3.  Hence `chi(Q-z)=5`;
the reverse inequality follows from `chi(Q)=5`.  The same argument gives
`chi(Q-u)=5`, proving item 4.

Choose a five-vertex-critical subgraph `C_u` of `Q-z`.  Since
`C_u\subseteq R\cup\{u\}` and `R` is four-colourable, `u` belongs to
`C_u`.  Martinsson and Steiner proved that, in a five-vertex-critical
graph, any prescribed vertex can be the singleton branch set of a
`K_5` minor.  Apply their theorem to `u`.  We obtain a `K_5` model

\[
                              \{u\},M_1,\ldots,M_4
\]

inside `Q-z`.  The connected set `X` is adjacent to every one of these
five branch sets because it dominates `Q`.  The vertex `z` is adjacent
to `u` and has a neighbour in `B subseteq X`.  Consequently all pairs
among the seven sets in (2.1) are adjacent except possibly
`({z},M_i)`.  Interchanging `z,u` proves (2.2), and the last assertion is
immediate.  This proves item 5. \(\square\)

## 3. Exact contribution and remaining obstruction

The star-Kempe condition does more than supply five pairwise colour
connections.  For every nonbuffer colour it canonically separates the
host into

- one connected dominating bipartite subgraph `X`; and
- one tight five-chromatic, `K_6`-minor-free core `Q` carrying two
  opposite singleton-rooted near-`K_7` models.

Thus the residue can be regenerated without preserving the original
spanning `K_6` model.  In the three-common-branch-set profile, choosing
`beta` absent from the three common portal colours also makes `X` meet
both exclusive branch sets, but that extra fact is not needed for the
theorem.

The theorem does not align the four branch sets `M_i` with the outside
pole.  Closing that row would require a simultaneous two-root version of
the rooted `K_4` mechanism inside a five-critical core, or a
label-preserving exchange between the two opposite models (2.1) and
(2.2).  One application of Strong Hadwiger for four colours roots a model
at one colourful set only and does not provide this synchronization.

This distinction is necessary even abstractly.  Take two copies of `K_4`
and join them by one bridge.  The vertex set of either copy is colourful
in the resulting four-chromatic graph, but no `K_4` minor can have every
branch set meet both copies, because the bridge is a one-vertex-capacity
bottleneck.  The seven-connectivity and contraction-criticality of the
host therefore have to enter a proof that synchronizes the two rows; the
two colourful-set statements alone cannot do it.

## 4. External input

A. Martinsson and R. Steiner,
[*Strengthening Hadwiger's conjecture for 4- and 5-chromatic graphs*](https://doi.org/10.1016/j.jctb.2023.08.009),
Journal of Combinatorial Theory, Series B 164 (2024), 1--16.  We use their
Corollary 1.4, which says that every five-vertex-critical graph has a
`K_5` minor in
which any prescribed vertex is a singleton branch set.
