# Tight vertices give exact order-nine singleton responses

**Status:** written proof; separate internal audit GREEN in
[`hc7_order9_tight_vertex_singleton_response_audit.md`](hc7_order9_tight_vertex_singleton_response_audit.md).

This note records an unconditional operation-specific consequence of a
tight vertex at the order-nine, six-colour boundary endpoint.  The new
boundary need not be `K_5`-minor-free, connected to the opposite side in
any prescribed way, or carry the old minor-model labels.  Accordingly the
result is a strict one-step reduction in the order of the rejected open
side, not a recursive closure of the paired-kernel endpoint.

## 1. Setting

Let `G` be a seven-chromatic graph such that every proper minor is
six-colourable.  Suppose

\[
             V(G)=A\mathbin{\dot\cup}B\mathbin{\dot\cup}D,
             \qquad E_G(A,D)=\varnothing,             \tag{1.1}
\]

where `A,D` are nonempty, `|B|=9`, and `phi` is a proper colouring of
`G[B]` using all six colours.  Fix `Z in {A,D}` and put

\[
 L(v)=[6]\setminus\phi(N_G(v)\cap B),
 \qquad
 \varepsilon(v)=d_{G[Z]}(v)-|L(v)|,
 \qquad
 \rho(v)=|N_G(v)\cap B|-|\phi(N_G(v)\cap B)|.          \tag{1.2}
\]

Assume that `G[Z]` is vertex-minimal subject to not being colourable from
the lists `L`, and that every vertex of `Z` has degree at least nine in
`G`.  A vertex `v in Z` is **tight** when `epsilon(v)=0`.

The hypotheses are exactly the local part of the live order-nine spanning
list-critical endpoint.  They imply the degree identity

\[
                         d_G(v)=6+\varepsilon(v)+\rho(v). \tag{1.3}
\]

## 2. Exact singleton response

### Theorem 2.1

Let `v in Z` be tight.  Then:

1. `d_G(v)=9`.  The set `S=N_G(v)` is the boundary of a nontrivial
   separation with singleton open side `{v}`.
2. For every edge `vx` and every proper six-colouring `c` of `G-vx`,

   \[
        c(v)=c(x),\qquad
        c^{-1}(c(x))\cap S=\{x\},                    \tag{2.1}
   \]

   and every one of the other five colours occurs on `S-{x}`.
3. Consequently `c|S` uses all six colours.  It extends through the
   outside closed side `G-v` and through the edge-deleted singleton side
   `G[S union {v}]-vx`, but its equality partition is rejected by the
   intact singleton side `G[S union {v}]`.

Thus every tight vertex returns an exact order-nine, full-six-colour
singleton response.

#### Proof

Write the six nonempty colour classes of `phi` on `B` as
`C_1,...,C_6`.  Since their orders sum to nine,

\[
                         \sum_{i=1}^6(|C_i|-1)=3.      \tag{2.2}
\]

For any shore vertex `u`, if `n_i=|N_G(u)\cap C_i|`, then

\[
 \rho(u)=\sum_i\max\{0,n_i-1\}
          \le\sum_i(|C_i|-1)=3.                      \tag{2.3}
\]

Tightness, (1.3), and `d_G(v)\ge9` give `rho(v)\ge3`.
Hence `rho(v)=3` and (1.3) gives `d_G(v)=9`.
Equality in (2.3) also forces
`|N_G(v)\cap C_i|=|C_i|` for every nonsingleton class `C_i`.

The opposite shore in (1.1) is nonempty and anticomplete to `v`.  It is
therefore contained in `G-N_G[v]`.  Hence `S=N_G(v)` is an actual
separation boundary, its singleton side is nonempty, and its outside side
is nonempty.  This proves item 1.

Fix `x in S` and a proper six-colouring `c` of `G-vx`, which exists by
proper-minor six-colourability.  If `c(v)\ne c(x)`, restoring `vx` gives a
proper six-colouring of `G`, a contradiction.  Put
`alpha=c(v)=c(x)`.  Every vertex of `S-{x}` remains adjacent to `v` in
`G-vx`, so none has colour `alpha`.  This proves the second equality in
(2.1).

Let `beta\ne alpha`.  If no vertex of `S-{x}` had colour `beta`, recolour
`v` with `beta` and restore the edge `vx`.  The result would again be a
proper six-colouring of `G`: no neighbour of `v` would have colour `beta`,
and `c(x)=alpha\ne beta`.  This contradiction proves that every one of the
five other colours occurs on `S-{x}`.  Item 2 follows.

The restriction of `c` to `G-v` gives the outside extension, and its
restriction to `G[S union {v}]-vx` gives the edge-deleted singleton-side
extension.  Since all six colours occur on `S`, no colour is available for
`v` in the intact singleton side.  The same is true for every boundary
colouring inducing the same equality partition, after a permutation of
the six colour names.  Thus the intact singleton side rejects the
partition, proving item 3.  \(\square\)

### Theorem 2.2 (fixed-trace rainbow replacement)

Let `v in Z` be tight and let `vw` be an internal shore edge.  Then
`G[Z]-vw` is `L`-colourable.  In every such colouring `lambda`,

\[
                        \lambda(v)=\lambda(w),        \tag{2.4}
\]

and `lambda` restricts to a bijection

\[
                        N_{G[Z]}(v)\longrightarrow L(v). \tag{2.5}
\]

Moreover `B-N_G(v)` consists of one singleton boundary colour class for
each colour in `L(v)`.  Hence (2.5) gives a literal colour-preserving
bijection

\[
                 B-N_G(v)\longrightarrow N_{G[Z]}(v), \tag{2.6}
\]

and the coloured nine-set `N_G(v)` is obtained from the coloured nine-set
`B` by replacing precisely those missed singleton boundary vertices by
their uniquely colour-matched internal neighbours of `v`.

#### Proof

Vertex-minimality gives an `L`-colouring of `G[Z]-v`.  In `G[Z]-vw`, the
vertex `v` has only

\[
                       d_{G[Z]}(v)-1=|L(v)|-1
\]

coloured neighbours, so at least one colour in `L(v)` remains available.
This extends the colouring to `G[Z]-vw`.

Now let `lambda` be any such colouring and put `alpha=lambda(v)`.  If
`lambda(w)\ne alpha`, restoring `vw` would give an `L`-colouring of
`G[Z]`, a contradiction.  Thus (2.4) holds.  Every vertex of
`N_{G[Z]}(v)-{w}` is adjacent to `v` in the edge-deleted graph, so none
has colour `alpha`.  If some `beta in L(v)-{alpha}` were absent from
these neighbours, recolouring `v` with `beta` and restoring `vw` would
again colour `G[Z]` from `L`.  Thus all `|L(v)|-1` other list colours
occur on the `|L(v)|-1` other internal neighbours, each exactly once.
Together with `w`, this proves (2.5).

Equality in (2.3) also gives the literal saturation conclusion: `v` is
adjacent to every vertex in every nonsingleton boundary colour class.  A
colour is therefore in `L(v)` exactly when its boundary colour class is a
singleton missed by `v`.  This identifies the left side of (2.6) with
the colours in `L(v)`, while (2.5) identifies its right side with the same
colours.  The identity on `B\cap N_G(v)` and the bijection (2.6) preserve
every colour class and replace one vertex for one vertex.  Since both sets
have order nine, the final assertion follows.  \(\square\)

## 3. The mixed tight/non-tight forest branch

### Corollary 3.1

Assume additionally that

\[
                  E_Z=\sum_{u\in Z}\varepsilon(u)>0. \tag{3.1}
\]

If the tight-vertex subgraph of `G[Z]` is nonempty (in particular, if it
is a nonempty forest), there is an edge `vw` with `v` tight and `w`
non-tight.  Applying Theorem 2.1 to this edge gives an exact order-nine
singleton response whose rejected open side has order one, strictly less
than `|Z|`.

Consequently, in the case where the tight-vertex subgraph is a forest, the
only alternative not returned by this one-step reduction is that the
tight-vertex subgraph is empty, equivalently

\[
                         \varepsilon(u)\ge1
                         \quad\text{for every }u\in Z. \tag{3.2}
\]

#### Proof

Vertex-minimal non-`L`-colourability makes `G[Z]` connected: otherwise an
uncolourable component would be a proper induced subgraph.  Equation (3.1)
gives a non-tight vertex.  If a tight vertex also exists, connectedness
gives an edge between the union of the tight components and its non-tight
complement.  Choose such an edge `vw`, with `v` tight.

Theorem 2.1 gives the asserted response.  Moreover `|Z|>1`, since a
one-vertex vertex-minimal list obstruction has empty list and internal
degree zero, hence excess zero.  The new singleton rejected side therefore
has strictly smaller order.  If there is no tight vertex, nonnegative
integrality of the excesses gives (3.2).  \(\square\)

For the selected tight--non-tight edge, Theorem 2.2 additionally supplies
the fixed-`phi` rainbow replacement (2.6) inside the operated shore.  This
is local colouring data; because the opposite shore rejects `phi` in the
live paired-kernel application, it is not by itself a six-colouring of the
edge-deleted host.

### Theorem 3.2 (boundary-aligned response at the tight pole)

Assume additionally that `G` is seven-connected and has no `K_7` minor.
For every tight vertex `v`, there are a neighbour `z`, a component `C` of
`G-N_G[v]`, and its full neighbourhood `S=N_G(C)` such that

\[
 z\in S\subseteq N_G(v),\qquad
 7\le |S|\le9,\qquad
 \chi(G-\{v,z\})=6.                                  \tag{3.3}
\]

Every proper six-colouring of `G-vz` gives `v,z` one common colour and
induces on `S` a partition with `{z}` as an exact singleton block.  This
partition extends through `G[C\cup S]` and through the edge-deleted
opposite closed side, but is rejected by the intact opposite closed side.
Moreover `G[S]` is four-colourable.

Consequently one of the following occurs.

1. `|S|` is seven or eight, giving an actual smaller-boundary
   operation-specific response.
2. `|S|=9` and hence `S=N_G(v)`.  In this case `C` and `{v}` are connected
   subgraphs on opposite sides, each adjacent to every literal vertex of
   `S`, and the boundary trace uses all six colours.

#### Proof

Put `H=G[N_G(v)]` and let `T_ext` be the set of neighbours of `v` having
a neighbour outside `N_G[v]`.  The complement
`R=N_G(v)-T_ext` has no exterior neighbour.  Thus `T_ext` separates the
nonempty exterior from `{v} union R`, and seven-connectivity gives
`|T_ext|>=7`.

Suppose for a contradiction that

\[
                 \chi(G-\{v,x\})=5
                 \qquad(x\in T_ext).                 \tag{3.4}
\]

For `x in T_ext`, a five-colouring of `G-{v,x}` and the standard
common-neighbour recolouring show that `x` has at least five neighbours in
`H`.  Indeed, if one of the five colours were absent from the common
neighbourhood of `v,x`, recolour all neighbours of `v` in that colour with
a fresh sixth colour, give `v` the old colour and `x` the fresh colour.
This would six-colour `G`.  For `x in R`, every neighbour of `x` lies in
`N_G[v]`, so seven-connectivity gives `d_H(x)=d_G(x)-1>=6`.  Therefore

\[
                              \delta(H)\ge5.          \tag{3.5}
\]

Contract any component of `G-N_G[v]` to a vertex `c`.  It has at least
seven neighbours in `H`.  Since `|H|=d_G(v)=9`, (3.5) gives
`|E(H)|>=23`.  Unless

\[
 (|E(H)|,d_H(c))\in\{(23,7),(23,8),(24,7)\},         \tag{3.6}
\]

the resulting eleven-vertex minor has more than `5*11-15` edges and hence
has a `K_7` minor by Mader's bound.  In each case in (3.6), the audited
degree-nine pole completion theorem gives a `K_6`-minor model in `H+c`
whose six branch sets all meet `H`.  The singleton `{v}` is adjacent to
all six sets and completes a `K_7` model.  Both conclusions contradict the
hypothesis.  Thus (3.4) fails for some `z in T_ext`.  Deleting two vertices
lowers chromatic number by at most two, while `G-v` is six-colourable, so
the remaining possibility is `chi(G-{v,z})=6`.

Choose a component `C` of `G-N_G[v]` adjacent to `z` and put `S=N_G(C)`.
Then `z in S subseteq N_G(v)`.  The set `S` separates `C` from `v`, so
seven-connectivity and `d_G(v)=9` give (3.3).

Let `c` be a six-colouring of `G-vz`.  Its ends have one common colour;
otherwise the deleted edge can be restored.  Every member of `S-{z}` is
still adjacent to `v`, so `{z}` is the exact boundary block carrying that
common colour.  The restriction `c|G[C union S]` is proper in the intact
graph because this closed side omits `v`.  If the same equality partition
extended through the intact opposite closed side `G-C`, align the colour
names on its blocks and glue the two closed-shore colourings.  This would
six-colour `G`.  Hence that side rejects the partition, while `c` itself
colours its edge-deleted version.

If `|S|<=8`, outcome 1 holds.  If `|S|=9`, the inclusion
`S subseteq N_G(v)` and `d_G(v)=9` give equality.  The component `C` is
adjacent to every vertex of `S` by the definition of its full
neighbourhood, while the singleton `v` is adjacent to all of `S`.  Finally
Theorem 2.1, applied to the same deleted edge `vz`, says that `c|S` uses all
six colours.  This proves outcome 2.

Finally, the boundary-four-colourability argument in the audited
boundary-aligned low-degree theorem applies verbatim to the connected
`S`-full subgraphs `C` and `{v}`.  At order seven it uses the exact-seven
classification and cycle-boundary completion; at order eight it uses
two-full-shore boundary absorption; and at order nine it eliminates the
sole exceptional boundary `K_2\vee C_7` by the same cycle completion or an
explicit third-component `K_7` model.  Hence `chi(G[S])\le4`.  \(\square\)

## 4. Trust boundary

Theorem 2.1 is a literal host statement and is independent of the order or
internal shape of the original shore.  It does **not** prove a recursive
descent in the paired-kernel class:

- the new boundary `N_G(v)` need not be `K_5`-minor-free;
- `G-N_G[v]` need not be connected, and its components need not be full to
  the new boundary;
- the new boundary trace need not be the old trace `phi` and need not
  retain old branch-set labels; and
- the trace extends through the intact outside side, so it is an
  opposite-response trace rather than a trace rejected by both old shores.

Thus Corollary 3.1 is a strict **one-step response-side reduction**.  It
does not eliminate the mixed branch unless a separate theorem closes or
re-enters the resulting singleton response.  Its exact gain is to isolate
the remaining direct order-nine positive-excess obstruction as either an
all-positive-excess shore or this explicit singleton-response interface.
Theorem 2.2 preserves the old colour names on its local replacement, but
it does not change this trust boundary: its `L`-colouring need not extend
through the opposite shore.

Theorem 3.2 improves the geometry after using seven-connectivity and the
global `K_7`-minor exclusion: it selects one connected outside component
which is full whenever its boundary still has order nine.  It still does
not make every outside component full, preserve the old trace, or produce
a partition extending through both intact closed shores.

## 5. Dependencies

- [degree-nine local completion](../results/hc7_degree9_pole_verifier.md)
- [boundary-aligned low-degree adjacent-pair argument](../results/hc7_low_degree_boundary_edge_alignment.md),
  whose vertex-wise proof is repeated in Theorem 3.2
- Mader's extremal bound for `K_7` minors
