# Fresh-colour linkages across an exact order-seven separation

**Status:** written proof; separate internal audit in
[`hc7_exact7_fresh_colour_linkage_audit.md`](hc7_exact7_fresh_colour_linkage_audit.md).

This note couples the edge-deletion colouring and the opposite-shore
contraction colouring returned by the order-eight fan-or-separator
reduction.  A spare boundary colour converts them into either a path across
an arbitrary boundary nonedge or two vertex-disjoint, colour-separated
obstruction paths.  It also gives an actual eight-boundary transition with
no deleted-edge ambiguity.  Nothing here proves `HC_7`.

## 1. Setting

Let `G` be seven-connected, `K_7`-minor-free and not six-colourable.  Let

\[
                         V(G)=A\mathbin{\dot\cup}Y
                                  \mathbin{\dot\cup}B,  \tag{1.1}
\]

where `A` is nonempty and connected, `|Y|=7`, `N_G(A)=Y`, and there are no
edges from `A` to `B`.  Let `p in B`, `v in Y`, and `e=pv in E(G)`.

Assume that:

1. `d` is a proper six-colouring of `G-e`, with

   \[
                            d(p)=d(v)=\alpha;            \tag{1.2}
   \]

2. `J=d^{-1}(alpha) cap Y` has order at least two; and
3. `h` is a proper six-colouring of `G-A` whose boundary colour class
   `h^{-1}(alpha) cap Y` is exactly the same literal set `J`.

Put

\[
                              F=G[Y-J].                  \tag{1.3}
\]

The application from the prescribed-spoke separator theorem has precisely
these data.  Its live case also makes `F` noncomplete.

## 2. Freeing a colour or obtaining a chord path

### Theorem 2.1 (fresh colour or a shore-supported nonedge path)

Assume that `F` is noncomplete, and fix any nonedge `xy` of `F`.  Then one
of the following holds.

1. In one of the two colourings `d,h`, the corresponding two-colour graph
   contains an `x`--`y` path whose internal vertices lie in one component
   of `G-Y`.
2. By Kempe interchanges and independent palette permutations fixing
   `alpha`, the colourings can be replaced by `d',h'` such that

   \[
   \begin{aligned}
      &d'(p)=d'(v)=\alpha,\\
      &(d')^{-1}(\alpha)\cap Y=(h')^{-1}(\alpha)\cap Y=J,\\
      &\text{one common colour }\beta\ne\alpha
        \text{ is absent from }Y\text{ in both colourings}.          \tag{2.1}
   \end{aligned}
   \]

#### Proof

Consider first the trace of either colouring on `F`.  If fewer than all five
colours other than `alpha` occur there, one non-`alpha` colour is already
absent from all of `Y`.  Otherwise all five occur, so `|F|=5` and the trace
is injective.  Let `rho,sigma` be the
colours of `x,y`.  These colours occur on `Y` only at `x,y`, respectively.
If `x,y` belong to one full `rho`--`sigma` component in the domain of the
colouring, a shortest such path has no other boundary vertex internally.
Its interior consequently lies in one component of `G-Y`, giving outcome
1.

Otherwise interchange `rho,sigma` on the full component containing `x`.
It meets `Y` only at `x`; the interchange therefore gives `x,y` one colour
and frees the other colour on `Y`.  It does not alter `J`.  In the colouring
`d`, neither `p` nor `v` changes, because both have colour `alpha`.

Apply this independently to `d` and `h`.  If neither application gives
outcome 1, each resulting colouring has a non-`alpha` colour absent on
`Y`.  Permute the two palettes independently, fixing `alpha`, so that both
absent colours have the common name `beta`.  This proves outcome 2.
\(\square\)

## 3. Two disjoint obstruction paths

### Theorem 3.1 (fresh-colour disjoint-linkage alternative)

In outcome 2 of Theorem 2.1, either `G` is six-colourable or there are
vertex-disjoint paths `P,Q` such that:

1. `Q` is an `alpha`--`beta` path from `p` to `v` in `G-e`, and

   \[
                              V(Q)\cap Y\subseteq J;     \tag{3.1}
   \]

2. `P` joins two distinct bichromatic components of `F`, all its internal
   vertices lie in `A`, and it uses two colours outside
   `{alpha,beta}` in the relevant lifted colouring.

#### Proof

The noncomplete graph `F` has at most five vertices and is
three-degenerate: a graph of degeneracy at least four on at most five
vertices contains `K_5`.  By the Las Vergnas--Meyniel theorem, all proper
four-colourings of `F` using the palette

\[
                       [6]-\{\alpha,\beta\}             \tag{3.2}
\]

belong to one Kempe class.  Choose a sequence from the trace of `d'` to the
trace of `h'`, keeping `J` fixed in colour `alpha` and `beta` absent from
`Y`.

Start with the restriction of `d'` to `G[A union Y]` and lift the boundary
interchanges in order.  If every interchange lifts, the final colouring on
this closed shore agrees with `h'` on `Y`; gluing it to `h'` on `G-A`
six-colours `G`.

Otherwise consider the first failed interchange, using colours
`gamma,delta` from (3.2) on one component `W` of the boundary two-colour
graph.  In the current closed-shore extension, the full
`gamma`--`delta` component containing `W` must meet another boundary
component; otherwise interchanging the full component would lift the move.
A shortest path between the two boundary components has every internal
vertex in `A`.  Call this path `P`.

In the global colouring `d'` of `G-e`, the vertices `p,v` lie in one
`alpha`--`beta` component.  Otherwise a Kempe interchange on the component
containing one endpoint would give them different colours, after which the
edge `e` could be restored and `G` would be six-coloured.  Let `Q` be an
`alpha`--`beta` path between them.  Since `beta` is absent from `Y` and the
boundary `alpha`-class is exactly `J`, (3.1) follows.

Every successful lifted interchange before the failure uses only colours
in (3.2).  Thus the set of vertices of `A` having colour `alpha` or `beta`
is unchanged from `d'`.  The path `P` uses two colours from (3.2), whereas
`Q` uses only `alpha,beta`; their internal vertices are disjoint.  Their
boundary vertices are disjoint as well: those of `P` lie in `Y-J`, while
every boundary vertex of `Q` lies in `J`.  Also `p notin V(P)`.  Hence
`P,Q` are vertex-disjoint. \(\square\)

## 4. Kempe connectivity on at most eight vertices

### Lemma 4.1

If `R` is a `K_7`-minor-free graph of order at most eight, then all proper
six-colourings of `R` belong to one Kempe class.

#### Proof

If `R` is five-degenerate, apply Las Vergnas--Meyniel.  Otherwise `R`
contains a subgraph of minimum degree at least six.  A seven-vertex such
subgraph is `K_7`, so `|R|=8` and the subgraph is spanning.  Its missing
edges, and therefore the missing edges of `R`, form a matching `M`.
Thus

\[
                              R=K_8-M.                  \tag{4.1}
\]

If `|M|<=1`, `R` contains a `K_7` subgraph.  If `|M|=2`, say the missing
edges are `a_1b_1,a_2b_2`, contracting `a_1a_2` gives a `K_7` minor.
Consequently `|M|>=3`.

Regard `R` as a complete multipartite graph whose nonsingleton parts are
the pairs in `M`.  Every colour is confined to one part.  If a two-vertex
part is split between two colours, its two vertices are isolated components
of the corresponding two-colour graph; interchange one singleton component
to make the part monochromatic.  Repeating this makes every part
monochromatic.  There are at most five parts, so one of the six colours is
unused.  That colour acts as a buffer: a singleton part is recoloured in one
Kempe interchange, and a two-vertex part is recoloured one vertex at a time.
This connects all monochromatic-part colourings.  Reversing the initial
merges reaches any target colouring. \(\square\)

## 5. An actual augmented-boundary transition

### Theorem 5.1

Retain outcome 2 of Theorem 2.1 and put

\[
                              X=Y\cup\{p\}.             \tag{5.1}
\]

Then at least one of the following holds.

1. `G` is six-colourable.
2. There is a connected component `D` of `G-X` whose full neighbourhood has
   order seven.  Thus `N_G(D)=X-\{x\}` for one `x in X`, and this is an
   actual order-seven separation.  The gaining-side colouring and a named
   bichromatic obstruction path are retained on that side.
3. There is a connected component `D` of `G-X` with

   \[
                              N_G(D)=X.                  \tag{5.2}
   \]

Only the selected component in outcome 3 is asserted to be `X`-full.

#### Proof

Starting from `d'`, recolour `p` alone from `alpha` to the fresh colour
`beta`.  This properly colours `G[A union X]`: there are no edges from `p`
to `A`, `beta` is absent on `Y`, and the restored edge `pv` now has
different endpoint colours.  The colouring `h'` properly colours `G-A`.
Their restrictions are proper six-colourings of the actual boundary graph
`G[X]`.

By Lemma 4.1 those restrictions lie in one Kempe class.  For a boundary
colouring record whether it extends to the closed `A`-side and whether it
extends to `G-A`.  A colouring extending to both sides would glue to a
six-colouring of `G`.  If there is no such colouring, take a Kempe path from
the first trace to the second.  At the first loss of left extension, the
usual full-component argument gives a bichromatic obstruction path with
interior in `A`.  At the first gain of right extension, read the move
backwards.  Because `pv` is an edge of the actual boundary graph `G[X]`,
two distinct boundary two-colour components cannot be joined merely by
that edge.  The obstruction path therefore has nonempty interior in one
component `D` of `G-X` on the right.

Now `N_G(D) subseteq X`.  Seven-connectivity gives

\[
                             |N_G(D)|\in\{7,8\}.         \tag{5.3}
\]

Order seven gives outcome 2 and order eight gives (5.2). \(\square\)

The order-seven output is numerically smaller on the selected right shore,
but the theorem does not prove a state-preserving recursive descent: its
boundary can omit `p` or `v`, and restricting the operated boundary move
need not remain a Kempe move on that seven-set.

## 6. Exact scope

Theorem 3.1 is a label-free but genuinely simultaneous conclusion: the two
paths arise from the same pair of proper-minor colourings and are disjoint
for a colour-theoretic reason, not by independent path selection.  Theorem
5.1 removes the direct-edge flaw that occurs if `pv` is deleted from the
comparison boundary.

The results do not allocate `P,Q` among the five inherited minor-model
branch sets.  Outcome 3 of Theorem 5.1 gives one full component, not an
all-components-full order-eight interface.  Outcome 2 does not yet carry a
common full equality partition.  A further rooted-model or separator-
colouring theorem is still required.

## 7. Dependencies

- [prescribed spokes or a coloured exact-seven separator](hc7_order8_prescribed_spoke_reduction.md)
- M. Las Vergnas and H. Meyniel, *Kempe classes and the Hadwiger
  Conjecture*, J. Combin. Theory Ser. B 31 (1981), 95--104.
