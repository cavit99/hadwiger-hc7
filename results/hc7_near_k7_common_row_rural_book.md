# A common missing row becomes a third bag or an ordered rural page

## Status

This is an **audited proof-spine theorem**.  The independent audit is
stored beside it in `hc7_near_k7_common_row_rural_book_audit.md`.
It is the label-preserving replacement for the false assertion that every
4-connected rotation connector supplies three of four abstract demands.

For overlapping two-hole states

\[
                       D=\{a,b\},\qquad E=\{a,c\},       \tag{0.1}
\]

the common row `a` can be packaged as a third non-row branch set.  The two
remaining private demands then form an ordinary rooted Two Paths problem.
If that private linkage is absent in a 4-connected connector, the classical
Two Paths Theorem gives one coherent, port-labelled rural page rather than
another finite list of portal patterns.

## 1. Literal three-carrier completion

Use the exact rotation datum of
`../results/hc7_near_k7_rotation_edge.md`: the old centre is `X`, the new
centre is `W`, the connected connector is `Z`, the five fixed clique-model
rows are `F_1,...,F_5`, and `XW` is a literal edge.  Assume (0.1), so `X`
misses `F_a,F_b`, `W` misses `F_a,F_c`, and `Z` meets all three rows.

## Theorem 1 (common-row third-bag completion)

Suppose `Z` contains pairwise vertex-disjoint connected subgraphs `K,L,R`
such that

\[
\begin{array}{lll}
 E(K,F_a)\ne\varnothing, & E(K,L)\ne\varnothing,
                          & E(K,R)\ne\varnothing,\\
 E(L,X)\ne\varnothing,   & E(L,F_b)\ne\varnothing,\\
 E(R,W)\ne\varnothing,   & E(R,F_c)\ne\varnothing.
\end{array}                                                   \tag{1.1}
\]

Then `G` contains a literal `K_7` model.

### Proof

Use the seven branch sets

\[
        X\cup L,\qquad W\cup R,\qquad F_a\cup K,
                \qquad F_i\quad(i\ne a).                \tag{1.2}
\]

They are pairwise disjoint and connected.  The first two are adjacent
through the literal `XW` edge.  Their edges to the third bag are the
`LK` and `RK` edges.  The first bag retains all old centre--row edges
except `F_a,F_b`, gains `F_b` through `L`, and does not need a direct edge
to `F_a` because `F_a union K` is already the third branch set.  The
second bag is symmetric, using `R-F_c`.  Finally `F_a union K` is adjacent
to each unchanged fixed row through the old fixed-row clique model, and
the four unchanged rows remain pairwise adjacent.  Thus every pair in
(1.2) is adjacent. \(\square\)

### Corollary 1.1 (singleton common portal)

If `P_a=N_Z(F_a)={p}`, it suffices that `Z-p` contain disjoint connected
subgraphs `L,R` satisfying

\[
\begin{array}{lll}
 E(L,X)\ne\varnothing, & E(L,F_b)\ne\varnothing,
                        & E(L,p)\ne\varnothing,\\
 E(R,W)\ne\varnothing, & E(R,F_c)\ne\varnothing,
                        & E(R,p)\ne\varnothing.
\end{array}                                                   \tag{1.3}
\]

Indeed take `K={p}` in Theorem 1.  This is the exact two-shore capacity
problem left by a singleton common portal; it is stronger than merely
finding an `X-F_b` path disjoint from a `W-F_c` path.

## 2. The common demand drops out of the `K_7^-` shadow

For the next result, a connected subgraph of `Z` is `X`-rooted if it
meets `N_Z(X)`, and similarly for `W`.  Put

\[
                       P_i=N_Z(F_i).                      \tag{2.1}
\]

## Lemma 2 (private-linkage augmentation)

Assume `P_a` is nonempty.  If `Z` contains disjoint connected subgraphs
`L,R` such that

\[
 L\text{ is `X`-rooted and meets }P_b,qquad
 R\text{ is `W`-rooted and meets }P_c,                   \tag{2.2}
\]

then one of the following two rooted carrier splits exists:

1. an `X`-rooted carrier meeting `P_a,P_b`, disjoint from the
   `W`-rooted `P_c`-carrier; or
2. the `X`-rooted `P_b`-carrier, disjoint from a `W`-rooted carrier
   meeting `P_a,P_c`.

Thus two private rooted paths already cover three of the four occurrences
in the demand multiset `D dotcup E`.

### Proof

Choose `p in P_a`.  If `p` lies in `L` or `R`, the corresponding
conclusion is immediate.  Otherwise take a shortest path from `p` to
`L union R`.  Its internal vertices avoid both carriers and its last
vertex lies in exactly one of them.  Add the path, except for its last
vertex if desired, to that carrier.  The enlarged carrier remains
connected and disjoint from the other carrier, and now meets `P_a`.
This gives conclusion 1 or 2 according to which carrier the path first
reaches. \(\square\)

### Corollary 2.1 (no-`K_7^-` private unlinkage)

If `G` has no `K_7^-` minor, then no private linkage (2.2) exists.

### Proof

Either outcome of Lemma 2 supplies two rooted carriers covering three of
the four demand occurrences.  The robust four-demand theorem in
`../results/hc7_near_k7_rotation_edge.md` then gives a `K_7^-` minor.
\(\square\)

This is the decisive difference between the legitimate overlapping-pair
state and the disjoint-pair counterexamples: after retaining the actual
row labels, the common demand is absorbed for free at the `K_7^-` shadow
level.

## 3. Four-connected connectors have one ordered rural page

We use the following standard 4-connected form of the Two Paths Theorem.

> If `H` is 4-connected and `s_1,t_1,s_2,t_2` are distinct, then either
> `H` contains disjoint `s_1-t_1` and `s_2-t_2` paths, or `H` is planar
> and in its (unique up to reflection) plane embedding the four terminals
> occur in alternating order on one facial cycle.

## Theorem 3 (private linkage or coherent rural page)

Assume `G[Z]` is 4-connected.  Fix distinct attachment roots

\[
                 \alpha\in N_Z(X),\qquad
                 \beta\in N_Z(W),                        \tag{3.1}
\]

and nonempty private portal sets `P_b,P_c` which are pairwise disjoint
and disjoint from `{alpha,beta}`.  Then exactly one of the following
structural alternatives is forced.

1. For some `x in P_b` and `y in P_c`, there are disjoint
   `alpha-x` and `beta-y` paths.  Consequently Lemma 2 supplies a rooted
   three-demand split, and a host with no `K_7^-` minor is impossible.
2. `G[Z]` has a unique plane embedding with one face `F` containing
   `alpha,beta` and every vertex of `P_b union P_c`.  All private portals
   lie on one of the two open `alpha-beta` boundary arcs of `F`.  Orient
   that occupied arc from `alpha` to `beta`.  Every occurrence of `P_c`
   precedes every occurrence of `P_b` on the arc.  (The whole facial
   orientation may be reflected, but the labelled order may not be
   interchanged while `alpha,beta` remain fixed.)

In particular, in the no-`K_7^-` branch every 4-connected shared-row
rotation connector is a single coherent rural page, not an arbitrary
4-connected capacity obstruction.

### Proof

Suppose outcome 1 fails.  For every `x in P_b,y in P_c`, the Two Paths
Theorem applied to the pairs `(alpha,x)` and `(beta,y)` gives planarity
and a facial cycle on which those four vertices alternate.

Fix `x_0 in P_b,y_0 in P_c`.  The resulting plane embedding is unique
because `G[Z]` is 4-connected.  Let `F` be the face containing
`alpha,beta,x_0,y_0`.  For any `y in P_c`, the same theorem gives a face
containing `alpha,beta,x_0,y`.  In a 3-connected plane graph two distinct
facial cycles cannot share three distinct vertices; otherwise their
common boundary would yield a separation of order at most two.  Hence
that face is `F`, so all of `P_c` lies on `F`.  Fixing `y_0` and varying
`x` proves in the same way that all of `P_b` lies on `F`.

For every pair `x in P_b,y in P_c`, the endpoints of the two absent paths
alternate on the boundary cycle of `F`.  Relative to the two occurrences
`alpha,beta`, this forces `x,y` onto the same open boundary arc.  Fixing
one portal in each class shows that every portal lies on that one arc.
Orient the occupied arc from `alpha` to `beta`.  For the prescribed pairs
`(alpha,x)` and `(beta,y)`, alternation gives the labelled order

\[
                     \alpha,\quad y,\quad x,\quad\beta,
\]

for every `x in P_b,y in P_c`.  Hence every `P_c` occurrence precedes
every `P_b` occurrence.  This is outcome 2 and is incompatible with
outcome 1. \(\square\)

## 4. Component concentration around the common core

The three-carrier theorem has an immediate decomposition consequence which
is useful at cutvertices and 2-adhesions.

## Theorem 4 (two-shore component exchange)

Let `K subseteq Z` be a nonempty connected set with an edge to `F_a`.
Call a component `C` of `Z-K`

* **left-live** if it meets both `N_Z(X)` and `P_b`; and
* **right-live** if it meets both `N_Z(W)` and `P_c`.

If a left-live component and a right-live component are distinct, then
`G` contains a `K_7` minor.  Consequently, in a `K_7`-minor-free host,
exactly one of the following holds:

1. neither a left-live nor a right-live component exists;
2. a left-live component exists but no right-live component exists;
3. a right-live component exists but no left-live component exists; or
4. both kinds exist, and there is a unique component `C` which is the
   sole left-live and the sole right-live component.

### Proof

Every component of `Z-K` is adjacent to `K`, since `Z` is connected.
If `C_L,C_R` are distinct live components, take inside `C_L` a connected
subgraph meeting `N_Z(X)` and `P_b`, and inside `C_R` one meeting
`N_Z(W)` and `P_c`.  They are disjoint and, together with `K`, satisfy
Theorem 1.

Now suppose both kinds of live component exist but the `K_7` outcome is
excluded.  Every left-live component must equal every right-live
component.  Fixing one of each shows that there is exactly one component
in each family and that the two are equal. \(\square\)

This is a genuine infinite-family reduction: a target-free common core
cannot feed the two private sides through different lobes.  All useful
traffic is either absent on one side or concentrated in one block.  The
former is a separator/state input; the latter is the single-page input of
Theorem 3 after the relevant rooted connectivity is verified.

## 5. Exact composition residue

Theorems 1--3 close two infinite subfamilies:

* a splittable common core gives a literal `K_7`; and
* a 4-connected private shadow gives a rooted split or one ordered rural
  page.

They do **not** yet prove that rural pages from different rotation edges
use one global apex pair.  The remaining composition edge is now exact:

1. expand adjacent ordered pages with compatible orientation into one
   planar society; or
2. use an orientation conflict to construct the three carriers of
   Theorem 1; or
3. at a cutvertex/2-adhesion between pages, match the proper-minor
   equality state from the critical-pinch theorem.

No conclusion based only on abstract rooted-`K_4` shadows is valid; small
4-connected counterexamples show that two separate rooted-`K_4` models
need not compose into a three-demand carrier.
