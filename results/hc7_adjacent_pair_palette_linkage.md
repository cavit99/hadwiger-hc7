# Palette-permutation linkage at a non-double-critical adjacent pair

**Status:** written proof; separately audited.  The result is a
uniform strengthening of the adjacent-pair `K_6`-model analysis.  It does
not prove `HC_7`: the separator returned by the branch-set split need not
have order seven, and the profiles with at most two common-contact branch
sets remain open.

## 1. Setup

Let `G` be a seven-connected, seven-chromatic graph such that every proper
minor is six-colourable.  Let `zu` be an edge and put

\[
                         H=G-\{z,u\}.
\]

Assume `chi(H)=6`, as occurs for a non-double-critical edge in the active
application.  Let

\[
                         \mathcal M=(F_1,\ldots,F_6)    \tag{1.1}
\]

be a spanning `K_6`-minor model in `H`, and put

\[
 C_z=\{i:N_G(z)\cap F_i\ne\varnothing\},\qquad
 C_u=\{i:N_G(u)\cap F_i\ne\varnothing\}.              \tag{1.2}
\]

The known contact constructions say that a `K_7` minor already exists if

\[
 |C_z\cap C_u|\ge5,                                   \tag{1.3}
\]

or if the intersection has order four and both poles have an exclusive
branch set.  The result below adds the colouring information which was
absent from that contact count.

## 2. The edge-deletion palette

### Lemma 2.1 (five saturated colours)

There is a proper six-colouring `phi` of `G-zu` and a colour `alpha` such
that

1. `phi(z)=phi(u)=alpha`;
2. neither pole has an `alpha`-coloured neighbour in `H`; and
3. for each of the other five colours `beta`, each of `z,u` has a
   `beta`-coloured neighbour in `H`.

Moreover `alpha` occurs on a vertex of `H`.

#### Proof

The edge deletion is a proper minor, so it has a six-colouring.  Its two
ends must have one common colour `alpha`; otherwise the colouring would
also colour `G`.  Properness gives item 2.

If, say, `z` had no neighbour of another colour `beta`, recolouring `z`
with `beta` would make the restored edge `zu` proper and would six-colour
`G`.  This proves item 3 for both poles.

Finally, if `alpha` did not occur in `H`, the restriction of `phi` to `H`
would use only the other five colours, contrary to `chi(H)=6`. \(\square\)

The last assertion is the exact difference from the double-critical
case: the sixth colour survives in the two-vertex deletion but is
anticomplete there to both poles.

### Lemma 2.2 (Kempe connectivity through the surviving colour)

Let `T` be any nonempty set of colours not containing `alpha`.  In the
subgraph of `G-zu` induced by the colours `T union {alpha}`, the vertices
`z` and `u` belong to the same component.  In particular, for every
`beta ne alpha` there is a `z`--`u` path whose vertices use only
`alpha,beta`.

#### Proof

Suppose that the component `K` containing `z` did not contain `u`.
Choose `beta in T` and interchange `alpha` and `beta` on `K`.  This is a
proper Kempe change: every neighbour of `K` outside `K` has a colour not
in `T union {alpha}`.  The change gives `z` colour `beta`, leaves `u`
with colour `alpha`, and therefore remains proper after restoring the
edge `zu`.  It would six-colour `G`, a contradiction. \(\square\)

For distinct colours `beta,gamma ne alpha`, paths supplied by the last
sentence can intersect internally only at `alpha`-coloured vertices.
This records exactly where simultaneous colour-preserving linkage can
fail: the surviving colour class may act as a common bottleneck.

## 3. Five disjoint paths with a palette permutation

### Theorem 3.1 (palette-permutation linkage)

For every colour `beta ne alpha`, choose

\[
 a_\beta\in N_G(z)\cap V_\beta(H),\qquad
 b_\beta\in N_G(u)\cap V_\beta(H),                    \tag{3.1}
\]

where `V_beta(H)` is the `beta`-colour class under `phi`.  Then `H`
contains five pairwise vertex-disjoint paths joining

\[
 A=\{a_\beta:\beta\ne\alpha\}
       \quad\text{to}\quad
 B=\{b_\beta:\beta\ne\alpha\},                      \tag{3.2}
\]

and every vertex of `A union B` is the end of one of the paths.  Trivial
one-vertex paths are allowed when the chosen sets overlap.

Consequently, after adjoining the pole edges, there are five internally
vertex-disjoint `z`--`u` paths such that the colours on their neighbours
of `z` are the five distinct non-`alpha` colours and the colours on their
neighbours of `u` are also the five distinct non-`alpha` colours.  The
paths therefore induce a permutation of those five colours between their
two ends.

#### Proof

Deleting two vertices from a seven-connected graph leaves a
five-connected graph, so `H` is five-connected.  The sets in (3.2) each
have order five because their vertices have distinct colours.

Put `I=A cap B`.  Use each vertex of `I` as a trivial path and delete `I`.
The graph `H-I` is `(5-|I|)`-connected.  Its two remaining terminal sets
both have order `5-|I|`.  By the vertex form of Menger's theorem there are
`5-|I|` pairwise vertex-disjoint paths between them.  Indeed, a separator
of smaller order would leave a terminal on each side and disconnect
`H-I`.  Truncate each path at its first and last terminal if necessary, so
that no selected terminal occurs internally.  Together with the trivial
paths, these are the five paths asserted in (3.2).

Their endpoints are all distinct on either side and hence use every
selected colour exactly once.  For each linkage path, add the edge from
`z` to its `A`-end and the edge from its `B`-end to `u`.  This produces the
final `z`--`u` paths. \(\square\)

This is stronger than the five edge-critical Kempe connections: those
connections retain their two-colour labels but may intersect one another,
whereas Theorem 3.1 gives simultaneous vertex-disjointness and retains the
complete palettes at both ends.  Its paths need not themselves be
bichromatic.

## 4. Elimination of four common-contact branch sets

We use the following elementary rooted split.  If a common-contact branch
set `F_h` contains distinct vertices

\[
                x\in N(z)\cap F_h,qquad
                y\in N(u)\cap F_h,                    \tag{4.1}
\]

then split a spanning tree of `G[F_h]` across an edge of its `x`--`y`
path.  If both resulting connected parts are adjacent to all five other
model branch sets, they combine with the poles and those five branch sets
to form a `K_7`-minor model.  Otherwise one part `Y` misses a foreign
branch set, and `N_G(Y)` is an actual vertex separator.  This is the
rooted branch-set split proved in the two-pole contact trichotomy.

### Theorem 4.1 (four-common-row reduction)

Suppose in addition that `G` has no `K_7` minor and

\[
                         |C_z\cap C_u|=4.              \tag{4.2}
\]

Then some common-contact branch set contains distinct vertices as in
(4.1).  Consequently `G` contains a `K_7` minor or there is a nonempty
proper connected subset `Y` of one branch set for which `N_G(Y)` is an
actual separator.

#### Proof

If both `C_z-C_u` and `C_u-C_z` were nonempty, four common branch sets and
the union of one exclusive branch set from each side, together with the
two singleton poles, would form a `K_7`-minor model.  Thus, after
interchanging the poles,

\[
                         C_u\subseteq C_z.
\]

It follows from (4.2) that `u` contacts exactly the four common branch
sets.  Since the model is spanning, every neighbour of `u` in `H` belongs
to one of those four sets.

Lemma 2.1 gives neighbours of `u` in five distinct colour classes.
Therefore one common branch set `F_h` contains two distinct neighbours
`y_1,y_2` of `u`.  It also contains some neighbour `x` of `z`.  At least
one of `y_1,y_2` differs from `x`; choose it as `y`.  The rooted split
described before the theorem now gives the claimed `K_7` model or actual
separator. \(\square\)

The conclusion is sharp at the present level.  The two-apex icosahedron
example has four common-contact branch sets and realizes the separator
alternative.  Its separator happens to have order seven, but the proof
above gives no upper bound on `|N_G(Y)|` in an arbitrary host.

## 5. The exact three-common-row normal form

### Corollary 5.1

Assume that `G` has no `K_7` minor and that no common-contact branch set
admits the separator outcome in Section 4.  If

\[
                         |C_z\cap C_u|=3,              \tag{5.1}
\]

then the six model branch sets have precisely the following contact
profile.

1. Three branch sets are common contacts.  In each of them, the two pole
   neighbourhoods are the same singleton vertex.
2. There is exactly one branch set contacted only by `z` and exactly one
   branch set contacted only by `u`.
3. The sixth branch set is anticomplete to both poles.
4. Each exclusive branch set contains neighbours of its pole in at least
   two distinct non-`alpha` colour classes.

#### Proof

If a common branch set contained distinct pole neighbours, the rooted
split would give a `K_7` minor or the excluded separator.  Thus, for every
common branch set `F_i`, any member of `N(z) cap F_i` equals any member of
`N(u) cap F_i`.  Both sets are nonempty, so they are the same singleton.
The three common branch sets consequently supply at most three of the five
neighbour colours required at either pole by Lemma 2.1.

Each pole must therefore contact an exclusive branch set.  A
`K_7`-minor-free host has `|C_z union C_u|<=5`, since the connected set
`{z,u}` together with all six rows would otherwise be a `K_7` model.
Starting from the three common rows leaves room for only two contacted
rows.  Hence there is exactly one exclusive row for each pole, and the
last row is uncontacted.

Finally, the three singleton common portals use at most three colours.
Every remaining one of the five saturated colours must occur at a
neighbour in the relevant exclusive row.  There are at least two such
colours for each pole, proving item 4. \(\square\)

### Corollary 5.2 (two palette linkages between the exclusive branch sets)

Under the hypotheses and notation of Corollary 5.1, let `F_z` and `F_u`
be the branch sets contacted exclusively by `z` and `u`, respectively.
Let `T` be the set of non-`alpha` colours not used by the three common
portal vertices.  Then `|T|>=2`, and for every `beta in T`:

1. every `beta`-coloured neighbour of `z` lies in `F_z`, and every
   `beta`-coloured neighbour of `u` lies in `F_u`; and
2. there is an `alpha,beta`-coloured `z`--`u` path whose first vertex in
   `H` lies in `F_z` and whose last vertex in `H` lies in `F_u`.

Moreover, after choosing two distinct colours `beta,gamma in T` and one
corresponding neighbour at each pole, `H` contains two vertex-disjoint
paths from the two chosen vertices in `F_z` to the two chosen vertices in
`F_u` (the pairing may interchange `beta` and `gamma`).

#### Proof

The common pole-neighbourhood in each common branch set is its singleton
portal.  Hence a colour absent from those three portals can occur at a
pole-neighbour only in that pole's exclusive branch set.  There are at
least two such colours by Corollary 5.1.  Lemma 2.2 gives item 2.

For the final assertion, the two selected vertices on each side form
disjoint two-element sets because `F_z` and `F_u` are disjoint.  The
five-connected graph `H` has two vertex-disjoint paths joining these two
sets by Menger's theorem. \(\square\)

## 6. Exact contribution and remaining gap

Theorem 3.1 is a label-free simultaneous linkage attached to every
non-double-critical adjacent pair.  Theorem 4.1 uses the same proper-minor
colouring to eliminate the full four-common-contact family, up to a
genuine graph separator rather than a model-relative cut.  Corollary 5.1
then replaces the next contact count by one exact, uniform portal profile.

What remains is not another contact inequality.  One must either:

- prove that the separator in Theorem 4.1 can be chosen with order seven
  and with a compatible proper-minor colouring;
- use the palette-permutation linkage to split the two exclusive rows in
  Corollary 5.1 while preserving all five model adjacencies; or
- show that failure of those splits identifies one fixed pair meeting
  every `K_5` minor.

The complete-join icosahedron family shows why the third alternative must
remain: geometry alone can lock a branch set, while the two universal
vertices form the coherent terminal pair.
