# Three bridge corollaries for the degree-seven one-spoke problem

**Status:** written proof; separate internal audit GREEN for the stated
claims.  These corollaries are conditional inputs to the
one-missing-adjacency problem.  They do not prove `HC_7` or repair the
missing adjacency.

## 1. Setup

Let `G` be a seven-connected graph such that

\[
 \chi(G)=7,\qquad K_7\not\preccurlyeq G,
\]

and every proper minor of `G` is six-colourable.  Let `u` be a vertex of
degree seven and put

\[
 S=N_G(u),\qquad C=G-N_G[u],\qquad H=G[S],\qquad F=\overline H.
\]

The promoted degree-seven anti-neighbourhood theorem makes `C` nonempty and
connected.  Put

\[
 A=G-u=G[C\cup S],\qquad B=G[N_G[u]].
\]

The exact matching-language theorem gives

\[
 \mathcal M(A)=\{\{e\}:e\in E(F)\},\qquad
 \mathcal M(B)=\{M:M\text{ is a matching of }F, |M|\ge2\}. \tag{1.1}
\]

## 2. Spanning enhancement

### Lemma 2.1 (spanning extension of a clique-minor model)

Let `J` be connected and let `D_1,...,D_t` be pairwise disjoint connected
branch sets whose union is connected.  They may be enlarged, without
changing their labels, to branch sets `D'_1,...,D'_t` which partition
`V(J)`.  Every old branch-set adjacency remains present.

#### Proof

Let `W=\bigcup_iD_i`.  Every component `Q` of `J-W` has an edge to `W`,
because `J` is connected.  Choose one such edge with its end in `D_i` and
add all of `Q` to `D_i`.  The enlarged set is connected.  Components of
`J-W` are pairwise disjoint and have no edges between them, so making one
choice for every component gives disjoint branch sets covering `V(J)`.
Enlargement cannot destroy an old adjacency.  \(\square\)

### Corollary 2.2 (spanning aligned near-`K_7` model)

Every boundary-labelled `K_7^-`- or `K_7^\vee`-model supplied by the
degree-seven aligned-near-clique theorem can be chosen with branch sets
partitioning `V(G)`, while keeping `{u}`, the singleton deficient centre,
and every displayed boundary root in its named branch set.

Here `K_7^\vee` denotes `K_7` with two adjacent edges deleted.

#### Proof

Fix the complement edge `ab` used in the construction.  Seven-connectivity
implies that

\[
                         J=G-\{u,a,b\}
\]

is connected.  The five rooted `K_5` branch sets in `J` have connected
union, so Lemma 2.1 extends them to a partition of `V(J)` without moving
their five boundary roots.  Insert `u,a,b` into the seven branch sets
exactly as in the promoted aligned-near-clique construction.

All adjacencies present in that construction remain present.  Enlargement
can only add one or both deficient centre adjacencies.  If it adds every
missing adjacency, the enlarged sets form a `K_7` model, contrary to the
setup.  Otherwise they form a spanning boundary-labelled `K_7^-` or
`K_7^\vee` model with the same singleton centre and named boundary roots.
\(\square\)

Absorption may turn a two-missing-adjacency model into a
one-missing-adjacency model.  It does not preserve colour-class purity of
the rooted bags: unused vertices, including vertices of the sixth colour,
may be absorbed.  Consequently neither the orders of the spanning bags nor
the number of absorbed vertices is a valid descent parameter by itself.
Only the original rooted submodel retains the matching and Kempe-chain
provenance used in its construction.

## 3. Proper-minor response beyond the pole shore

### Theorem 3.1 (off-pole-shore edge response)

Let `h=xy` be any edge which is not an edge of `B`; equivalently, at least
one endpoint of `h` lies in `C`.  Then every proper six-colouring of `G-h`
has the following properties.

1. `x` and `y` are monochromatic.
2. Its equality partition on `S` is encoded by a matching of `F` of order
   two or three.
3. For each of the five colours different from the common colour of `x,y`,
   the vertices `x,y` lie in one component of the corresponding
   bichromatic subgraph of `G-h`.

The same conclusions hold after expanding the contracted vertex in any
six-colouring of `G/h`.

#### Proof

Deleting `h` does not change the induced closed shore `B`, because `h` does
not have both endpoints in `V(B)`.  Restrict a six-colouring of `G-h` to
`B`.  Equation (1.1) says that the induced boundary matching has order at
least two; it has order at most three because it is a matching on seven
vertices.

If `x,y` received different colours, restoring `h` would give a
six-colouring of `G`.  Hence they have one common colour, say `0`.  Fix any
other palette colour `gamma`.  If `x,y` belonged to different components
of the subgraph induced by colours `0,gamma`, interchange those two colours
on the component containing `x`.  The resulting colouring of `G-h` gives
`x,y` different colours, so `h` can again be restored, a contradiction.
Thus they lie in one bichromatic component for every alternate colour.
(In particular no alternate palette colour can be absent.)

A colouring of `G/h` expands by giving `x,y` the colour of the contracted
vertex.  It is then a colouring of `G-h`, so the preceding argument
applies.  \(\square\)

If `h` joins `C` to `S`, these bichromatic paths are global paths in
`G-h`: their interiors need not lie in `C`, avoid `u`, or avoid other
vertices of `S`.  The theorem gives the exact colouring response, not a
pole-free or shore-internal linkage.

## 4. Two centre-preserving orientations

### Corollary 4.1 (dual orientation at a degree-two complement vertex)

Suppose `a` has degree two in `F`, with

\[
                         N_F(a)=\{b,x\}.
\]

Then the aligned-near-clique construction has two orientations with the
same singleton centre `{a}` and pole `{u}`:

1. using the rooted `K_5` model for `ab`, the unique deficient bag is
   `{b}\cup B_x`;
2. using the rooted `K_5` model for `ax`, the unique deficient bag is
   `{x}\cup B_b`.

In both orientations the remaining four bags contain the same four named
boundary roots.  The rooted branch sets in the two models are not asserted
to coincide.

#### Proof

Triangle-freeness of `F` gives `bx\in E(H)`.  For the complement edge
`ab`, take the rooted `K_5` model on `S-\{a,b\}`.  Its bag `B_x` contains
`x`, so `{b}\cup B_x` is connected through the edge `bx`.  The construction
in the aligned-near-clique theorem shows that

\[
 \{u\},\ \{a\},\ \{b\}\cup B_x,\
 (B_t:t\in S-\{a,b,x\})
\]

has every branch-set adjacency except possibly that between `{a}` and
`{b}\cup B_x`.  That adjacency cannot be present, since it would give a
`K_7` model.  This is the first orientation.

Apply the same argument to the complement edge `ax`, interchanging `b` and
`x`.  It gives the second orientation with deficient bag
`{x}\cup B_b`.  Both constructions retain `{u}`, `{a}`, and the four
boundary labels in `S-\{a,b,x\}`.  \(\square\)

## 5. Trust boundary

In the `K_7^-` outcome of Corollary 2.2, the model is a supported
one-missing-adjacency configuration, so the promoted connected
one-missing-adjacency trichotomy applies with deficient centre `{a}`.  The
trichotomy does not directly apply to a `K_7^\vee` outcome.
Theorem 3.1 permits the operation edge to be the first edge entering a
named branch set from `C`, rather than requiring both endpoints in `C`.
Corollary 4.1 gives two orientations but not one simultaneous pair of
rooted models.

None of these facts converts a first-hit collision into a labelled
branch-set split, bounds a returned full-neighbourhood separator by seven,
or synchronizes the two shore colourings.  Those are the remaining tasks.

## Dependencies

- [degree-seven aligned near-`K_7` model](../results/hc7_degree7_aligned_near_k7_model.md)
- [exact matching languages and proper-minor response](../results/hc7_degree7_matching_bridge_bundle.md)
- [connected one-missing-adjacency trichotomy](../results/hc7_connected_one_hole_trichotomy.md)
