# Tight Gallai blocks at the order-nine paired-kernel endpoint

**Status:** written proof; separate internal audit GREEN in
[`hc7_order9_tight_gallai_block_separator_audit.md`](hc7_order9_tight_gallai_block_separator_audit.md).

This note isolates the strongest consequence presently forced by the
degree identity at the order-nine spanning list-critical endpoint.  It is a
literal boundary statement: no colour is identified with a branch-set label.

## 1. Setting and notation

Let `G` be a seven-connected graph with a partition

\[
             V(G)=A\mathbin{\dot\cup}B\mathbin{\dot\cup}D,
             \qquad E_G(A,D)=\varnothing,
\tag{1.1}
\]

where `A,D` are nonempty and `|B|=9`.  Let `phi` be a proper six-colouring
of `G[B]` which uses all six colours.  For `Z in {A,D}` and `v in Z`, put

\[
 L(v)=[6]\setminus\phi(N_G(v)\cap B),
\]

and suppose `G[Z]` is vertex-minimal subject to not being colourable from
these lists.  Define

\[
 \varepsilon(v)=d_{G[Z]}(v)-|L(v)|,
 \qquad
 \rho(v)=|N_G(v)\cap B|-|\phi(N_G(v)\cap B)|.
\tag{1.2}
\]

List-criticality gives `epsilon(v)>=0`.  Direct counting gives

\[
                         d_G(v)=6+\varepsilon(v)+\rho(v).
\tag{1.3}
\]

Call `v` **tight** if `epsilon(v)=0`, and let `T` be the subgraph of
`G[Z]` induced by the tight vertices.  The standard degree-choosability
argument says that `T` is a Gallai forest: each of its blocks is a complete
graph or an odd cycle.

The live paired-kernel endpoint additionally excludes a singleton-side
response of boundary order seven or eight.  Equivalently for the argument
below, every vertex of `A union D` has degree at least nine.

## 2. Literal saturation of repeated-colour blocks

### Theorem 2.1 (tight-vertex boundary saturation)

Under the hypotheses above, every tight vertex `v in Z` is adjacent to
every literal vertex of every nonsingleton colour class of `phi` on `B`.
Moreover,

\[
             \rho(v)=3,
             \qquad d_G(v)=9.                         \tag{2.1}
\]

The list `L(v)` consists exactly of the colours of the singleton boundary
vertices missed by `v`, and

\[
 d_{G[Z]}(v)=|L(v)|
 =|\{b\in B:\{b\}\text{ is a colour class of }\phi,
                    \ vb\notin E(G)\}|.               \tag{2.2}
\]

#### Proof

Let the six nonempty colour classes on `B` be
`C_1,...,C_6`.  Since `|B|=9`,

\[
                         \sum_{i=1}^6(|C_i|-1)=3.       \tag{2.3}
\]

For every `v in Z`,

\[
 \rho(v)=
 \sum_{i=1}^6
 \max\{0,\,|N_G(v)\cap C_i|-1\}
 \le \sum_{i=1}^6(|C_i|-1)=3.                         \tag{2.4}
\]

If `v` is tight, then (1.3) and `d_G(v)>=9` give
`rho(v)>=3`.  Hence equality holds throughout (2.4).  For every
nonsingleton `C_i`, equality in its summand is possible only when
`C_i subseteq N_G(v)`.  Thus `v` is adjacent to every literal vertex in
every nonsingleton colour class.  Equations (1.3) and (2.4) give (2.1).

It follows that a colour is absent from `phi(N_G(v) cap B)` precisely when
its colour class is a singleton `{b}` and `vb` is not an edge.  This proves
the description of `L(v)`, and tightness gives (2.2).  \(\square\)

This conclusion is stronger than saying that `v` sees each repeated
colour: it sees every literal boundary vertex carrying such a colour.

## 3. A common missed set for every nontrivial tight block

Fix a nontrivial block `H` of the Gallai forest `T`.  Colour
`G[Z]-V(H)` from the lists `L`; this is possible by vertex-minimality.
Fix one such colouring `psi` and put

\[
 M_H(v)=L(v)\setminus
        \psi(N_{G[Z]}(v)-V(H))
 \qquad(v\in V(H)).                                  \tag{3.1}
\]

### Theorem 3.1 (block palette and full-neighbourhood formula)

The graph `H` is not colourable from the lists `M_H`, and

\[
                         |M_H(v)|\ge d_H(v)            \tag{3.2}
\]

for every `v in V(H)`.  Consequently one of the following holds (with
`K_3` taken under the first alternative).

1. `H=K_r` for some `r>=2`, and all the lists `M_H(v)` are one common
   set `P` of `r-1` colours.
2. `H` is an odd cycle, and all the lists `M_H(v)` are one common set `P`
   of two colours.

Every colour in `P` is carried by a unique singleton vertex of `B`.  Let
`P_B` be this literal set of boundary vertices, and define

\[
 \Lambda_H=B-N_G(H),
 \qquad
 A_H=N_{G[Z]}(H)-V(H).                               \tag{3.3}
\]

Then

\[
 P_B\subseteq\Lambda_H,
 \qquad
 N_G(H)=A_H\mathbin{\dot\cup}(B-\Lambda_H),          \tag{3.4}
\]

and hence

\[
 |N_G(H)|=|A_H|+9-|\Lambda_H|.                       \tag{3.5}
\]

In particular seven-connectivity gives

\[
                         |A_H|\ge|\Lambda_H|-2.       \tag{3.6}
\]

Equality in (3.6) is exactly the case in which `N_G(H)` is an order-seven
separator.  If `|N_G(H)|>=9`, then

\[
                         |A_H|\ge|\Lambda_H|.         \tag{3.7}
\]

#### Proof

For `v in V(H)`, tightness gives `|L(v)|=d_{G[Z]}(v)`.  At most
`d_{G[Z]}(v)-d_H(v)` colours are removed in (3.1), so (3.2) follows.  If
`H` were colourable from `M_H`, that colouring and `psi` would combine to
an `L`-colouring of `G[Z]`, a contradiction.

The block `H` is a complete graph or an odd cycle.  For `H=K_r`, an
`M_H`-colouring is a system of distinct representatives.  Since every list
has order at least `r-1`, Hall's condition can fail only on all `r`
vertices, and then the union and every list are the same set of order
`r-1`.  For an odd cycle, the standard degree-list characterization of a
cycle says that lists of order at least two fail to colour it only when all
lists are one common two-element set.  This proves the alternatives.

By Theorem 2.1, every `L(v)` for a tight vertex contains only colours of
singleton boundary classes.  Hence the same is true of `P`.  A colour in
`P subseteq L(v)` is absent from the boundary neighbourhood of every
`v in H`; its unique boundary vertex therefore lies in `Lambda_H`.  This
proves the first part of (3.4).

There are no edges from `Z` to the opposite shore in (1.1), so every
neighbour of `H` lies either in `Z-V(H)` or in `B`.  This gives the second
part of (3.4) and (3.5).  The nonempty opposite shore lies in a component of
`G-N_G(H)` different from `H`, so `N_G(H)` is a separator.  Seven-connectivity
and (3.5) give (3.6).  Equality is equivalent to `|N_G(H)|=7`.

The final assertion is immediate from (3.5).  \(\square\)

### Corollary 3.2 (a smaller response unless attachment excess persists)

Assume additionally that `G` is not six-colourable and every proper minor
of `G` is six-colourable.  For any edge `xy` with `x in V(H)` and
`y in N_G(H)`, a six-colouring of `G-xy` induces a boundary partition on
`N_G(H)` which extends through the edge-deleted `H`-side and through the
opposite closed shore, but is rejected by the intact `H`-side.

Thus (3.6) gives an exact order-seven full-neighbourhood response when
equality holds, and (3.5) gives a strict response-boundary descent from
order nine whenever

\[
                         |A_H|\le|\Lambda_H|-1.        \tag{3.8}
\]

The only nonterminal block case has the literal attachment inequality
`|A_H|>=|Lambda_H|`.

#### Proof

The graph `G-xy` is a proper minor and has a proper six-colouring.  Its
restriction to the two sides of the full-neighbourhood separation gives
the two extensions.  If the same boundary partition extended through the
intact `H`-side, aligning colour names and gluing would six-colour `G`.
Thus the intact side rejects it.  The assertions about boundary order are
immediate from (3.5).  In particular, after excluding boundary orders seven
and eight, `|N_G(H)|>=9`, so Theorem 3.1 gives (3.7).  \(\square\)

### Corollary 3.3 (the cutvertex-free full shore has positive excess)

Suppose `G[Z]` is two-connected and `Z` is full to `B`: every literal
vertex of `B` has a neighbour in `Z`.  Then not every vertex of `Z` is
tight.  Equivalently,

\[
                 \sum_{v\in Z}\varepsilon(v)>0.       \tag{3.9}
\]

#### Proof

If every vertex were tight, then `T=G[Z]`.  Since `T` is a Gallai forest
and `G[Z]` is two-connected, it would consist of one nontrivial block `H`.
Apply Theorem 3.1 with `H=G[Z]` and with the empty colouring of its
complement.  The common set `P` is nonempty, and every vertex of `H` misses
the corresponding nonempty literal set `P_B subseteq B`.  This contradicts
the assumption that `Z` is full to every vertex of `B`.  \(\square\)

## 4. What this does not prove

The theorem applies to every nontrivial block of the tight-vertex Gallai
forest, not merely to a leaf block.  It converts the proposed leaf-block
test into one exact residual inequality: after excluding an order-seven or
order-eight response, a block missing `k` literal boundary vertices has at
least `k` distinct internal attachment vertices.

Combined with the existing cutvertex response descent, Corollary 3.3 also
eliminates the entire all-tight spanning endpoint: each residual
two-connected boundary-full shore must contain a vertex of positive
list-degree excess.  It does not bound the amount or location of that
positive excess.

It does **not** identify the common palette `P` with named branch sets of a
minor model.  It therefore does not by itself yield the cyclic three-pair
contact configuration or a `K_7`-minor model.  Nor does maximal coverage by
two boundary-full connected subgraphs change this issue: that normalization
removes unused shore vertices, but it does not canonically transport
branch-set labels through a split-and-amalgamate move.  The audited
[permutation-holonomy barrier](../barriers/hc7_order8_transfer_holonomy_barrier.md)
records this obstruction.  The valid normalization by an adjacent
connected two-piece cover is already given by
[Lemma 1.1 of the connected-rich width-two frontier](../results/hc7_exact7_connected_rich_width2_frontier.md);
the gauge-invariant colouring-cycle replacement is the
[two-shore Kempe incidence-cycle theorem](../results/hc7_two_shore_kempe_incidence_cycle.md).

The remaining live question is consequently literal and host-level: use
contraction-critical responses at one block satisfying (3.7) either to
allocate its attachment vertices to the required named branch sets, or to
lower the attachment excess in (3.5).  A proof which records only colour
names or an arbitrarily chosen permutation of branch-set roles does not
address that question.
