# Bipartite-contraction rooted near-cliques

## Status

This note proves a uniform rooted-model principle in every least-parameter
Hadwiger counterexample.  An arbitrary nontrivial connected induced
bipartite subgraph can be prescribed inside one branch bag of a
`K_{k-1}`-model.  The statement holds for subgraphs of unbounded order and
in particular for every induced path.  It is stronger than the usual
edge-contraction witness, but it does not split the prescribed bag and
therefore does not by itself prove Hadwiger.

## 1. Exact chromatic order after bipartite contraction

### Theorem 1.1 (bipartite contraction stays on the chromatic wall)

Let `G` be proper-minor-minimal subject to not being `(k-1)`-colourable,
and let `T` be a vertex set of order at least two such that `G[T]` is
connected and bipartite.  Contract all of `T` to one vertex `z`, and call
the resulting simple graph `Q=G/T`.  Then

\[
                              \chi(Q)=k-1.                 \tag{1.1}
\]

#### Proof

The graph `Q` is a proper minor, so it is `(k-1)`-colourable.  Suppose it
has a colouring `c` with at most `k-2` colours, and write
`c(z)=alpha`.  Let

\[
                         V(T)=U\mathbin{\dot\cup}W
\]

be a bipartition.  Retain `c` on `G-T`, colour every vertex of `U` with
`alpha`, and colour every vertex of `W` with one new colour `beta`.
Every external neighbour of `T` is adjacent to `z` in `Q`, and hence has
colour different from `alpha`; the colour `beta` occurs nowhere outside
`T`.  Bipartiteness deals with all internal edges of `G[T]`.  This is a
proper colouring of `G` with at most `k-1` colours, a contradiction.
Thus (1.1) holds.  \(\square\)

The proof uses the *induced* graph `G[T]`: contracting a merely bipartite
spanning subgraph would forget possible same-side chords and would not
justify the expansion colouring.

### Corollary 1.2 (exact minor order at the least failing parameter)

Assume additionally that `k` is the least parameter for which Hadwiger's
Conjecture fails and that `G` has no `K_k` minor.  Then

\[
                            \eta(G/T)=k-1.                \tag{1.2}
\]

#### Proof

The already valid `HC_{k-1}`, applied to (1.1), gives a `K_{k-1}` minor
in `G/T`.  A `K_k` minor there would lift through the contraction to one
in `G`, so the order is exactly `k-1`.  \(\square\)

## 2. The rooted-model consequence

### Theorem 2.1 (uniform bipartite co-rooting)

Under Corollary 1.2, there is a `K_{k-1}`-model in `G` with a branch bag
containing all of `T`.

Consequently, for every two distinct vertices `a,b`, choosing a shortest
`a-b` path shows that some `K_{k-1}`-model has `a,b` in one common branch
bag.  More generally, every prescribed induced tree is contained in one
branch bag of such a model.

#### Proof

Proper-minor minimality makes `G` connected: otherwise its proper
components could be `(k-1)`-coloured separately.  Contracting the connected
set `T` preserves connectedness, so `Q` is connected.

Take a `K_{k-1}`-model in `Q`.  If its union misses `z`, join `z` to the
model union by a shortest path and absorb that path into the first bag it
meets.  This gives a model

\[
                         (R,C_1,\ldots,C_{k-2}),
                         \qquad z\in R.                 \tag{2.1}
\]

Replace `z` in `R` by `T`.  Every component of `R-z` which met `z` in
`Q` has an edge in `G` to some vertex of `T`; connectedness of `T` joins
all these pieces.  Thus

\[
                  B=(R-\{z\})\cup T,
                  \quad C_1,\ldots,C_{k-2}              \tag{2.2}
\]

is a `K_{k-1}`-model in `G`, and its first bag contains `T`.
A shortest path is induced, and every tree is bipartite, giving the two
stated special cases.  \(\square\)

This is a co-rooting theorem, not a rooted-transversal theorem: it puts
all prescribed vertices in one bag.  The missing operation is to split
that bag while preserving its named adjacencies.

## 3. Minimum root bags and the split obstruction

Choose (2.1) so that `|R|` is minimum among all `z`-rooted
`K_{k-1}`-models in `Q`.  The zero-delete/one-rotate theorem in
`hadwiger_uniform_contraction_split_warehouse.md` applies verbatim.  In
particular, every nonempty `z`-detachable `X subseteq R-\{z\}` satisfies

\[
 |\Lambda_R(X)|\ge2,
 \qquad
 \Lambda_R(X)\subseteq
 \Delta_z:=\{i:zC_i\notin E(Q)\}.                       \tag{3.1}
\]

The inclusion-minimal rooted block lobes have disjoint monopoly sets, so
their number is at most

\[
                         \left\lfloor{k-2\over2}\right\rfloor. \tag{3.2}
\]

After expansion, put `B=(R-z) union T`.  If there is a partition

\[
                           B=X\mathbin{\dot\cup}Y        \tag{3.3}
\]

into adjacent connected sets such that both `X` and `Y` are adjacent to
every `C_i`, then

\[
                         X,Y,C_1,\ldots,C_{k-2}
\]

is a `K_k`-model.  Hence a counterexample forces every connected split of
the prescribed bipartite branch bag to lose at least one named label.

The point of (3.1) is that an off-root lobe cannot account for only one
lost label: it can then be rotated into that label bag, reducing `R`.
Every genuine hanging obstruction therefore owns at least two labels,
uniformly in `k`.

## 4. A full adhesion or an actual charge to the prescribed set

### Theorem 4.1 (`T`-charge or full adhesion)

Assume `G` is `s`-connected.  Let `K` be a rooted block lobe of the
minimum bag `R`, viewed after expansion as a subset of `B-T`.  Then either

1. `K` has an edge to `T`; or
2. there is an inclusion-minimal separator `Z`, disjoint from
   `K union T`, separating `K` from `T`, such that `|Z|>=s`; the
   components containing `K` and `T` are both full to `Z`.

#### Proof

If the first outcome fails, the open neighbourhood of `K` separates it
from the connected set `T`.  Choose an inclusion-minimal separator `Z`
between those two sets.  Connectivity gives `|Z|>=s`.  For every
`q in Z`, minimality gives a `K-T` path avoiding `Z-{q}`; its two sides
show that `q` has a neighbour in each distinguished component of `G-Z`.
No component has a neighbour outside itself and `Z`, proving fullness.
\(\square\)

### Theorem 4.2 (reference-state disjointness)

Suppose `G` is proper-minor-minimal non-`r`-colourable and outcome 2 of
Theorem 4.1 gives a separation `(P,Q')` with boundary `Z`, where
`K subseteq P-Z` and `T subseteq Q'-Z`.  No `r`-colouring of `G/T` and
no `r`-colouring of a boundary-faithful proper minor operated strictly in
`P-Z` induce the same equality partition on `Z`.

#### Proof

If two such colourings had the same equality partition, permute one
palette so that they agree literally on `Z`.  Use the `G/T` colouring on
the closed `P`-shore; the contraction lies strictly on the other side, so
this shore is represented faithfully.  Use the warehouse-operation
colouring on `Q'-Z`; that operation lies strictly in `P-Z`, so the second
closed shore is faithful.  There is no edge between the open shores.
The two restrictions therefore splice to an `r`-colouring of the original
graph `G`, a contradiction.  \(\square\)

Thus every prescribed induced bipartite contraction supplies, in one
object, a rooted near-clique, bounded multi-label warehouses, and a family
of operation states disjoint across any uncharged warehouse adhesion.

## 5. Exact frontier consequence

The theorem changes the uniform target.  A least counterexample cannot
merely fail to possess a convenient near-clique: **every induced path and
every induced tree already sits in a branch bag of one**.  What has been
proved for the part inherited from the minimum root bag is:

1. at most `floor((k-2)/2)` multi-label warehouse lobes, each charged
   directly to the prescribed bipartite set or lying behind a full
   adhesion; and
2. at every such uncharged adhesion, a warehouse-operation spectrum
   disjoint from the contraction spectrum.

There is also an intrinsic split obstruction inside the expanded
`T`-containing core.  For a single contracted edge the root-torso theorem
reduces that obstruction to endpoint/internal pins or an ordered
two-label corridor.  For an arbitrary bipartite `T`, however, its own
cutvertices and block geometry need not descend from lobes of `R`; this
note does not yet give an exhaustive torso classification for them.

For `k=7` there are at most two minimal *inherited* warehouse lobes.  A
completion must both eliminate those dynamic objects and prove a
label-preserving split principle for the arbitrary induced bipartite core.
No additional density estimate is hidden in that target, but the present
note does not assert the split.
