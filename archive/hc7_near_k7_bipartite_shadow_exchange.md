# Bipartite split shadow exchange

## Status

This note isolates and resolves the **state** part of the sole apex-shadow
which remains after total contraction of a spanning induced bipartite
complex bag.  The result is uniform in the palette size.

For `HC_7` it gives the following sharp outcome.  Either the bilateral
split already gives `K_7`, or a second noncontact singleton gives a
literal common two-block operation state, or the apex has a unique
noncontact singleton and the graph contains a forced three-path crossed
frame.  A rainbow member of that theta gives an explicit `K_7`; failure
of the theta gives an exact cut of order at most six.  Thus the only
remaining geometric object is a **non-rainbow crossed theta**, not an
unidentified colour carrier.

The note does not prove that every forced crossed theta has a rainbow
member.  That is a labelled path-exchange statement and is the exact
remaining gap in this cell.

## 1. Spanning singleton setup

Let `r>=3`.  Let `G` be non-`r`-colourable, fix `v in V(G)`, and put
`H=G-v`.  Suppose

\[
 V(H)=V(B)\mathbin{\dot\cup}S,
 \qquad S=\{b_1,\ldots,b_{r-1}\},                         \tag{1.1}
\]

where `S` is a clique, `G[B]` is nontrivial, connected, induced and
bipartite, and

\[
                  (B,\{b_1\},\ldots,\{b_{r-1}\})          \tag{1.2}
\]

is a spanning `K_r`-model in `H`.  Thus every

\[
                         P_i=N_B(b_i)                       \tag{1.3}
\]

is nonempty.  Assume also that the foot set

\[
                         F=N_B(v)                           \tag{1.4}
\]

is nonempty.

Contract `B` to a vertex `z`, and let `c` be an `r`-colouring of the
proper minor `G/B`.  Since `z,b_1,...,b_{r-1}` induce `K_r`, rename the
colours so that

\[
             c(z)=\alpha,\qquad c(b_i)=p_i.                \tag{1.5}
\]

The edge `vz` excludes `alpha`.  Hence

\[
                   c(v)=p_j\quad\hbox{and}\quad vb_j\notin E(G) \tag{1.6}
\]

for some `j`.  Write

\[
                       C=S-\{b_j\}.                         \tag{1.7}
\]

The vertex `b_j` is the singleton shadowed by the apex in this state.

Apply the bipartite bilateral full-palette theorem of
`../results/hc7_near_k7_bipartite_total_contraction.md` to any spanning
tree of `G[B]`.  It returns a partition

\[
                         B=A\mathbin{\dot\cup}D             \tag{1.8}
\]

such that `G[A]` and `G[D]` are connected, they are adjacent, and both
sets see every colour other than `alpha` in the one fixed state `c`.

## 2. The apex is the only possible misalignment

### Theorem 2.1 (literal four-row alignment and one shadow)

For every `i!=j`, both `A` and `D` meet `P_i`.  Each of `A,D` meets
`P_j union F`.

Consequently either

1. `G` contains a `K_{r+1}` minor; or
2. after interchanging `A,D`,

   \[
             A\cap P_j=\varnothing,\quad A\cap F\ne\varnothing,
             \quad D\cap P_j\ne\varnothing.                \tag{2.1}
   \]

#### Proof

Outside `B`, the colour `p_i`, for `i!=j`, occurs only at `b_i`.
The full-palette conclusion for each shore therefore forces a literal
edge from each shore to `b_i`.  The colour `p_j` occurs outside `B`
only at the two nonadjacent vertices `b_j,v`, so each shore meets
`P_j union F`.

The whole bag `B` meets `P_j`.  If both shores meet `P_j`, then

\[
              A,\ D,\ \{b_1\},\ldots,\{b_{r-1}\}           \tag{2.2}
\]

are `r+1` pairwise adjacent connected branch sets.  Otherwise exactly
one shore misses `P_j`; it must meet `F`, giving (2.1).  \(\square\)

Thus palette-to-label noncommutation has only one coordinate in the
spanning singleton cell.

## 3. The shadow is an exact one-coordinate state switch

Let `G_2` be the proper minor obtained by contracting `A` and `D`
separately to adjacent vertices `a,d`.  Put

\[
                J_0=\{k:vb_k\notin E(G)\}.                 \tag{3.1}
\]

For every `k in J_0`, the total contraction `G/B` has the colouring
`c_k` obtained from (1.5) by assigning `p_k` to `v`; all other displayed
colours are unchanged.

### Theorem 3.1 (shadow-switch theorem)

Assume (2.1).  For every `k in J_0-\{j\}`, the state `c_k` on
`G-B` extends to an `r`-colouring of `G_2`, explicitly by

\[
                          a=p_j,\qquad d=\alpha.            \tag{3.2}
\]

On the other hand the state `c_j=c` does not extend to `G_2`.
Therefore the pair of operations

\[
                         G/B,\qquad G_2                    \tag{3.3}
\]

has an exact one-coordinate transition spectrum:

\[
 \boxed{
 \begin{array}{c}
 \{v,b_j\}\text{ is rejected by the two-block contraction, while}\\
 \{v,b_k\}\text{ is accepted for every other noncontact }k.
 \end{array}}                                             \tag{3.4}
\]

#### Proof

Because `A cap P_j` is empty, the contracted vertex `a` is nonadjacent
to `b_j`.  In the state `c_k`, where `k!=j`, the only other exterior
vertex of colour `p_j` is absent: `v` now has colour `p_k`.  Thus `a`
may receive `p_j`.  No exterior vertex has colour `alpha`, so `d` may
receive `alpha`.  The two contracted vertices are adjacent and the two
colours are distinct.  Every other exterior adjacency was already proper
under `c_k`.  This proves (3.2).

For `c_j`, full palette exposure says that the only colour available at
each contracted shore is `alpha`; equivalently this is Corollary 2.4 of
the total-contraction theorem.  Since `a,d` are adjacent, the state does
not extend.  \(\square\)

This is stronger than saying that two unrelated proper minors have
different colourings.  Their states agree literally on the entire
exterior `G-B`, and the accepted states are written down explicitly.
At any larger separation in which this spanning cell is one closed shore,
(3.4) is directly usable by ordinary palette-aligned gluing.

### Corollary 3.2 (state closure or unique shadow)

Either Theorem 3.1 supplies an accepted alternative noncontact state, or

\[
                         J_0=\{j\};                         \tag{3.5}
\]

that is, `v` is adjacent to every vertex of `C`.

No trace or Kempe path is needed to prove this dichotomy; it is an exact
consequence of the star of quotient colourings at `v`.

## 4. Unique shadow: a crossed frame or the target minor

Assume (3.5).  In particular

\[
                         v\sim C,\qquad b_j\sim C.          \tag{4.1}
\]

### Lemma 4.1 (double-foot completion)

If `D cap F` is nonempty, then `G` contains a `K_{r+1}` minor.

#### Proof

Use the branch sets

\[
            A,\quad D\cup\{b_j\},\quad\{v\},
            \quad\{b_i\}\ (i\ne j).                      \tag{4.2}
\]

They are connected and disjoint.  The first two are adjacent through an
`A-D` edge; `v` sees `A` by (2.1) and sees the second bag through a foot
in `D`.  Both `v` and `b_j` see all singleton vertices in `C`, each shore
sees all of `C` by Theorem 2.1, and `C` is a clique.  Thus (4.2) is a
`K_{r+1}` model.  \(\square\)

Consequently a target-free unique-shadow cell has the exact crossed
placement

\[
               F\subseteq A,\qquad P_j\subseteq D,
               \qquad A,D\text{ each meet every }P_i\ (i\ne j). \tag{4.3}
\]

## 5. The forced theta and its literal completion

The next lemma separates the connectivity input from the label input.

### Lemma 5.1 (cut-or-three-path frame)

Assume (4.1).  Exactly one of the following holds.

1. There is a `v-b_j` separator `T` in `G-C` with `|T|<=2`.  Then

   \[
                              Z=C\cup T                     \tag{5.1}
   \]

   is a `v-b_j` separator in `G` of order at most `r`.
2. There are three internally vertex-disjoint `v-b_j` paths in `G-C`.

If `T` is inclusion-minimal in outcome 1, then `Z` is inclusion-minimal:
each vertex of `C` has the two-edge path `v-b_i-b_j`, and every vertex of
`T` is essential in `G-C`.  Hence the two distinguished sides are full
to `Z`.

#### Proof

Apply the vertex form of Menger's theorem to `v,b_j` in `G-C`.  It gives
the stated alternatives.  In the separator outcome, adding `C` blocks
all paths which use a deleted clique vertex and gives (5.1).

For minimality, restoring any `b_i in C` restores the path
`v-b_i-b_j`, while minimality of `T` restores a `v-b_j` path in `G-C`.
The standard path witness for an inclusion-minimal separator shows that
each separator vertex has a neighbour in both distinguished components.
\(\square\)

For an `(r+1)`-connected graph, outcome 1 is impossible.  In particular,
for the seven-connected `HC_7` host, deleting the four-clique `C` always
leaves three internally disjoint `v-b_j` paths.

### Lemma 5.2 (rainbow-theta completion)

Let `L_1,L_2,L_3` be internally vertex-disjoint `v-b_j` paths in `G-C`,
and put

\[
                       R_i=V(L_i)-\{v,b_j\}.               \tag{5.2}
\]

If, after relabelling the paths,

\[
                 R_3\cap P_i\ne\varnothing
                 \quad\hbox{for every }i\ne j,             \tag{5.3}
\]

where `P_i` denotes the singleton portal set from (1.3), then `G` has a
`K_{r+1}` minor.

#### Proof

The three branch sets

\[
             Q_1=\{v\}\cup R_1,\qquad
             Q_2=\{b_j\}\cup R_2,\qquad
             Q_3=R_3                                      \tag{5.4}
\]

are nonempty, connected and disjoint.  They are pairwise adjacent:
the last edge of `L_1` joins `Q_1` to `b_j in Q_2`, the first edge of
`L_2` joins `v in Q_1` to `Q_2`, and the first and last edges of `L_3`
join `Q_3` to `Q_1,Q_2`, respectively.

By (4.1), `Q_1,Q_2` are adjacent to every singleton in `C`.  Condition
(5.3) gives the same for `Q_3`.  Therefore

\[
                    Q_1,Q_2,Q_3,\quad \{b_i\}\ (i\ne j)   \tag{5.5}
\]

are `3+(r-2)=r+1` pairwise adjacent connected branch sets.  \(\square\)

The existence of a rainbow connector does not have to be assumed.

### Lemma 5.3 (a rainbow pole connector is forced)

In the unique-shadow setup, there is a `v-b_j` path in `G-C` whose
internal vertex set meets every ordinary portal class `P_i`, `i!=j`.

More precisely, each class of the fixed bipartition of `B` contains a
vertex `x` such that

\[
                 x\sim b_i\quad(i\ne j),
                 \qquad x\sim v\ \hbox{or}\ x\sim b_j.   \tag{5.6}
\]

#### Proof

For `x in B`, let

\[
 L(x)=\{\alpha,p_1,\ldots,p_{r-1}\}
       -c(N_G(x)-B).                                      \tag{5.7}
\]

Every list contains `alpha`, and `B` is not `L`-colourable: such a
colouring would extend the fixed quotient state to `G`.  Let
`U dotcup W` be the bipartition of `B`.  If every vertex of `U` had a
colour in `L(x)-{alpha}`, colour all of `W` with `alpha` and choose one
such secondary colour independently at every vertex of `U`.  This is
proper because both parity classes are independent, and it contradicts
the non-list-colourability.  Thus some `x in U` has `L(x)={alpha}`;
the same argument gives such a vertex in `W`.

At a singleton-list vertex, each ordinary colour `p_i`, `i!=j`, is
blocked by its unique exterior occurrence `b_i`, while `p_j` is blocked
by at least one of `v,b_j`.  This is (5.6).

Choose either saturated vertex `x`.  If `x~v`, take in connected `B` a
path from `x` to any member of the nonempty set `P_j`, then add its two
pole edges.  If `x~b_j`, take a path from any member of the nonempty foot
set `F` to `x` and again add the pole edges.  The resulting `v-b_j` path
has the saturated vertex `x` internally, so its interior meets all the
ordinary portal classes.  \(\square\)

### Corollary 5.4 (a doubly incident saturated vertex closes)

Assume `G` is `(r+1)`-connected.  If a vertex `x` satisfying (5.6) is
adjacent to both `v` and `b_j`, then `G` contains a `K_{r+1}` minor.

#### Proof

Put `K=G-C`.  The standard connectivity inequality gives

\[
                         \kappa(K)\ge3.                    \tag{5.8}
\]

Hence `K-x` is 2-connected and contains two internally vertex-disjoint
`v-b_j` paths.  Together with the length-two path `v-x-b_j`, these form
three internally vertex-disjoint pole paths, one of which is rainbow by
(5.6).  Lemma 5.2 applies.  \(\square\)

Thus a target-free unique-shadow cell contains a rainbow pole connector,
but every such connector fails to extend to a three-path theta.  Moreover
the two list-saturated parity witnesses are **pure**: each touches exactly
one of the two poles.

## 6. Exact surviving counterarchitecture

Combining the preceding results gives the promised sharp theorem.

### Theorem 6.1 (bipartite apex-shadow exchange)

In the spanning setup of Section 1, one of the following holds.

1. `G` contains a `K_{r+1}` minor.
2. There is a second noncontact singleton `b_k`, and the total- and
   two-block contractions have the explicit common exterior state of
   Theorem 3.1.
3. The apex has the unique noncontact singleton `b_j`, and there is a
   full separation of order at most `r` between `v` and `b_j`.
4. The apex has the unique noncontact singleton `b_j`; the crossed frame
   (4.3) holds; a rainbow `v-b_j` connector exists in `G-C`; and there are
   three internally disjoint `v-b_j` paths in `G-C`, but no rainbow
   connector belongs to any such triple.

If `G` is `(r+1)`-connected, outcome 3 is impossible.  Thus the sole
geometric survivor is outcome 4, the **non-rainbow crossed theta**.

#### Proof

Theorem 2.1 gives the target or the single shadow.  Theorem 3.1 and
Corollary 3.2 give outcome 2 or the unique shadow.  Lemma 4.1 gives the
target unless the crossed placement (4.3) holds.  Lemma 5.1 gives outcome
3 or a three-path frame, and Lemma 5.2 gives the target whenever a member
is rainbow.  \(\square\)

For `HC_7`, outcome 4 says exactly this.  Four singleton vertices form a
literal `K_4`; the apex and its unique noncontact singleton are the two
poles of a forced theta after that `K_4` is deleted; the old bipartite bag
split puts every foot on one side and every selected portal on the other;
and every triple of pole-to-pole paths avoids a full four-label carrier.
This is a finite-label path-exchange obstruction.  The colour shadow itself
has been eliminated.

## 7. Audit boundary and next lemma

1. The singleton hypothesis is essential.  It is what converts every
   nonshadow palette occurrence into a literal named portal.
2. The induced bipartite hypothesis is used only to obtain the bilateral
   connected split from one total-contraction state.
3. The recoloured state (3.2) colours the **two-block contraction**, not
   the original graph.  Expanding the two monochromatic contracted shores
   without extra work would be invalid.
4. Three disjoint pole paths alone do not give the target.  One internal
   branch set must meet all four ordinary portal classes.  Treating
   collective contacts on the union of the theta as contacts on one branch
   set would be an invalid allocation step.

The exact next target is therefore label-geometric rather than chromatic:

> **Crossed-theta rainbow exchange.**  In the seven-connected,
> `7`-contraction-critical, `K_7`-minor-free spanning singleton cell,
> the crossed placement (4.3) cannot coexist with a rainbow connector
> which is excluded from every pole theta.  Either reroute the connector
> into a three-path frame,
> or a minimal failed rerouting exposes an order-at-most-six adhesion on
> which the accepted state (3.4) glues to an edge-operation state.

This statement retains all operation data that the static theta lacks and
contains no Moser labels.
