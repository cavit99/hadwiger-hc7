# The canonical `K_6` model after deleting the outer-edge pair

**Status:** written proof; separately audited.  This note shows that
the spanning `K_6` model obtained after deleting the unique leaf--endpoint
edge in the canonical balanced order-eight branch is already forced by the
previous spanning `K_7`-minus-one-edge normalization.  Joint pole-contact
maximization therefore has value exactly five in a `K_7`-minor-free host and
leads to an explicit reversible one-hole exchange, not to the low-contact
branch-set obstruction.  The note does not align a six-colouring with the
six branch sets and does not prove `HC_7`.

## 1. Setup

Let `G` contain an eight-vertex separator

\[
 S=R\mathbin{\dot\cup}V(e)\mathbin{\dot\cup}V(f)
      \mathbin{\dot\cup}\{x\},\qquad |R|=3,
\tag{1.1}
\]

such that `G-S` has exactly two connected components `C,D`, each adjacent
to every literal vertex of `S`.  Assume the following balanced-boundary
properties.

1. `R` is a clique.
2. The sets `V(e),V(f)` induce two disjoint anticomplete edges, and each
   edge is collectively adjacent to every vertex of `R`.
3. The component `C` contains adjacent vertices `ell_e,ell_f`, both
   complete to `R`.
4. The edge `e` is anticomplete to `ell_e`, and `f` is anticomplete to
   `ell_f`.
5. The graph

   \[
                         H=C-\{\ell_e,\ell_f\}
   \tag{1.2}
   \]

   is connected and is met by each of `ell_e,ell_f,x`.
6. Every endpoint of `e` and `f` has a nonempty set of nonneighbours in
   `R`, and the two such sets belonging to either edge are disjoint.
7. The vertex `ell_f` is nonadjacent to `x` and has a unique neighbour
   `a` in `V(e)`.

Put

\[
                         z=\ell_f,\qquad u=a.
\tag{1.3}
\]

Thus `zu` is the canonical outer-edge pair.  Hypotheses 1--6 are the
standard-language hypotheses of the already proved simultaneous
singletonization theorem; hypothesis 7 is the endpoint equality exposed by
the canonical outer-edge argument.

For an endpoint `v` of `e` or `f`, put

\[
                         M_R(v)=R-N_R(v).
\tag{1.4}
\]

An endpoint is **admissible** if `|M_R(v)|<=1`.  Each of `e,f` has an
admissible endpoint, since the two nonempty endpoint nonneighbour sets are
disjoint subsets of a three-set.  Under hypothesis 6 an admissible endpoint
has exactly one nonneighbour in `R`.

## 2. The spanning near-complete model

Choose an admissible endpoint `q` of `e` and an admissible endpoint `b` of
`f`; write `q'` and `b'` for their mates, and write

\[
                         M_R(q)=\{r_q\},\qquad
                         M_R(b)=\{r_b\}.
\tag{2.1}
\]

For `r in R`, define

\[
 W_r=\{r\}\cup
 \{q':r=r_q\}\cup
 \{b':r=r_b\},
\tag{2.2}
\]

and put

\[
                         V^+=D\cup\{x\}.
\tag{2.3}
\]

The simultaneous singletonization theorem says, and its direct proof
checks, that

\[
 \{q\},\quad \{b\},\quad C,\quad V^+,
                   \quad W_r\ (r\in R)                 \tag{2.4}
\]

are the seven branch sets of a spanning `K_7`-minus-one-edge model.  Its
only missing branch-set adjacency is `\{q\}-\{b\}`.  We retain the explicit
description (2.1)--(2.4), because it makes the two-vertex deletion model
canonical.

## 3. Canonical deletion model and exact contact height

### Theorem 3.1 (canonical deletion model)

The graph `G-{z,u}` has an explicit spanning `K_6` model obtained from
(2.4).  Its six rows may be chosen so that the connected pair `\{z,u\}`
is adjacent to exactly five rows and is anticomplete to the sixth row
`\{b\}`.

More precisely:

1. if `q=u`, the six rows are

   \[
      C-\{z\},\quad V^+,\quad W_r\ (r\in R),\quad\{b\};
   \tag{3.1}
   \]

2. if `q\ne u`, then `q'=u`; delete `u` from the unique row of (2.4)
   containing it and use

   \[
      (C-\{z\})\cup\{q\},\quad V^+,
      \quad W_r-\{u\}\ (r\in R),\quad\{b\}.
   \tag{3.2}
   \]

Exactly one of the three sets `W_r` contains `u`, and removing it leaves
that set nonempty.

#### Proof

First,

\[
                         C-\{z\}=H\cup\{\ell_e\}
\tag{3.3}
\]

is connected: `H` is connected and has a neighbour at `ell_e`.  Deleting
`z` loses none of the five adjacencies from this row to the other rows in
(3.1).  It remains adjacent to every `W_r` through the edge
`ell_e r`; it remains adjacent to `V^+` because `x` has a neighbour in
`H`; and it remains adjacent to `\{b\}` because boundary fullness gives
`b` a neighbour in `C`, while `f` is anticomplete to `z`, so that neighbour
survives in `C-{z}`.  Thus, when `q=u`, deleting the singleton row
`\{q\}=\{u\}` and deleting `z` from the `C` row leaves the six pairwise
adjacent connected rows in (3.1).  They plainly span `G-{z,u}`.

Now suppose `q\ne u`.  Since `V(e)=\{q,u\}`, the deleted vertex `u=q'`
belongs to `W_{r_q}`.  Formula (2.2) and the edge-disjointness leave
`\{r_q\}` together with at most the mate `b'`; that set is connected by
the same collective-adjacency argument used in singletonization.

The vertex `q` has a neighbour in `C` by boundary fullness.  It is not
adjacent to `z`, because `u` is the unique endpoint of `e` adjacent to
`z`, and it is not adjacent to `ell_e`, because `e` is anticomplete to
`ell_e`.  Hence `q` has a neighbour in `H`, and
`(C-{z})\cup\{q\}` is connected.

Removing `u` from its old row loses no adjacency needed among the five
rows other than `\{q\}`: the surviving vertex `r_q` supplies all its old
adjacencies to `C`, `D`, and the other `R`-rooted rows, while `b` meets it
either at `r_q` or through the retained mate `b'`.  Finally absorb the
former singleton `q` into `C-{z}`.  The
row `C-{z}` was already adjacent to all five other rows, so this absorption
cannot lose an adjacency.  The six sets in (3.2) are therefore connected,
pairwise adjacent, disjoint, and spanning.

It remains to calculate the contact of the deleted pair.  The row `\{b\}`
is anticomplete to both `z` and `u`: the first assertion follows from
`f` being anticomplete to `z`, and the second from `e,f` being
anticomplete.  The pair `\{z,u\}` meets every other row:

- `z` meets the modified `C` row through a `z-H` edge;
- `u` meets the modified `D` row through boundary fullness;
- `z` meets every `W_r-\{u\}` at its surviving root `r`; and
- in the second case, `u` also meets the modified `C` row at its mate
  `q`.

Thus the pair contacts exactly five of the six rows and misses precisely
`\{b\}`.  \(\square\)

### Corollary 3.2 (contact maximization has value five)

Assume in addition that `G` has no `K_7` minor.  Among all spanning
`K_6` models in `G-{z,u}`, the maximum number of rows adjacent to the
connected pair `\{z,u\}` is exactly five.

#### Proof

Theorem 3.1 supplies a model with five contacted rows.  A model with all
six rows contacted, together with `\{z,u\}`, would be a `K_7`-minor
model.  Hence no such model exists. \(\square\)

This eliminates the contact-order-four and contact-order-at-most-three
branches from any lexicographically contact-maximal analysis of the
canonical outer-edge pair.  It does not orient the contact-five branch.

### Corollary 3.3 (a common row has distinct pole portals)

In the model of Theorem 3.1, some common-contact row contains distinct
vertices adjacent to the two poles.  Consequently the rooted row-split
theorem gives either a `K_7` minor or an actual vertex separator.

More precisely:

- if `q=u`, then `M_R(u)=\{r_0\}` for some `r_0`, and the row `W_{r_0}`
  contains the distinct pole portals `r_0 in N(z)` and
  `q' in N(u)`;
- if `q` is not `u`, then the modified `C` row contains a vertex of
  `N_H(z)` and the distinct vertex `q in N(u)`.

#### Proof

In the first case, endpoint rigidity makes `M_R(u)` nonempty, while
admissibility makes it a singleton.  Collective adjacency of `e` to
`r_0` puts the edge `q'r_0` in `G`, and (2.1) puts both vertices in
`W_{r_0}`.  The first is adjacent to `u` through the mate edge, while the
second is adjacent to `z` because `z` is complete to `R`.

In the second case, the proof of Theorem 3.1 puts `q` in the modified
`C` row.  The edge `uq` gives its `u`-portal, and a `z-H` edge gives a
different `z`-portal in that row.

Apply the rooted row-duty split theorem to the displayed common row.  A
spanning-tree edge on a path between the two portals partitions the row
into adjacent connected parts.  If both parts retain all five foreign-row
adjacencies they, the two singleton poles, and the five foreign rows give
a `K_7` model.  Otherwise one part has its whole-graph neighbourhood as an
actual separator. \(\square\)

This separator is not automatically an order-seven separator.  In the
branch where all actual order-seven separations have already been excluded,
its order is at least eight.  Counting the five foreign-row duties and the
two pole duties counts terminal **classes**, not literal neighbours, and
therefore gives no valid upper bound on that separator.  This is the exact
point at which a naive seven-duty argument fails.

## 4. The exact reversible obstruction

### Theorem 4.1 (explicit one-hole exchange)

The contact-five model of Theorem 3.1 and the singleton-root model (2.4)
are related by a reversible, label-preserving reassignment with the same
missed row `\{b\}`.

In the model (2.4), the singleton `\{q\}` is adjacent to each of the five
rows

\[
                        C,\quad V^+,\quad W_r\ (r\in R)
\tag{4.1}
\]

and is anticomplete to `\{b\}`.  In the transformed model, the connected
set `\{z,u\}` is adjacent to the five transformed rows corresponding to
(4.1) and is anticomplete to the same singleton row `\{b\}`.

The transformation is reversible: when `q=u`, move `z` between the
`C` row and the centre; when `q\ne u`, also move `q` from the modified
`C` row back to its singleton centre and return `u=q'` to its original
row.

#### Proof

All assertions for the singleton centre `q` are part of (2.4).  The
assertions for the pair centre `\{z,u\}` were checked in Theorem 3.1.
The reverse assignments restore exactly the sets in (2.1)--(2.4).
Connectivity in both directions is witnessed by the edges already used in
the proof of Theorem 3.1: a `z-H` edge, the mate edge `qu` when needed,
and the edge from `u` to its missed `R`-root.  Thus both endpoints of the
reassignment are valid labelled
one-hole near-`K_7` models with the same deficient adjacency. \(\square\)

Consequently the numerical conclusion `mu=1` from the general two-pole
contact-five theorem is not a new, unidentified frame here.  Its
singleton witness is already `q`, and the regenerated deletion model lies
in the explicit reversible exchange component of the old spanning
near-complete model.  Neither branch-set order nor joint contact can be a
strict potential on this exchange.

## 5. What the six-chromatic deletion actually adds

The model in Theorem 3.1 uses no colouring theorem.  Hence the genuinely
new conclusion of the canonical outer-edge argument is only

\[
                         \chi(G-\{z,u\})=6,
\tag{5.1}
\]

not the existence of its spanning `K_6` model.  The following elementary
cover records the exact colouring information available from (5.1).

### Proposition 5.1 (adjacent-root colouring cover)

Let `G` be seven-chromatic and suppose every proper minor of `G` is
six-colourable.  Let `zu` be an edge and put `J=G-{z,u}`.  If
`chi(J)=6`, then for every proper six-colouring `phi` of `J`, with

\[
 A_z=\{\alpha:\alpha\text{ is absent from }\phi(N_J(z))\},
 \qquad
 A_u=\{\alpha:\alpha\text{ is absent from }\phi(N_J(u))\},
\tag{5.2}
\]

at least one of the following holds:

1. `A_z` is empty;
2. `A_u` is empty; or
3. `A_z=A_u=\{alpha\}` for one colour `alpha`.

The third outcome occurs for at least one six-colouring of `J`.

#### Proof

If both missing-colour sets are nonempty and contain distinct colours
`alpha in A_z`, `beta in A_u`, then assigning `alpha` to `z` and `beta`
to `u` extends `phi` to a six-colouring of `G`, a contradiction.  Thus,
when neither set is empty, their union has order one.  Each set is then the
same singleton, proving the cover.

Contract the edge `zu`.  The resulting proper minor has a six-colouring;
it cannot use at most five colours, because its restriction to `J` would
contradict `chi(J)=6`.  Let `alpha` be the colour of the contracted vertex.
On restriction to `J`, the colour `alpha` is absent from both pole
neighbourhoods.  The cover forces both missing-colour sets to equal
`\{alpha\}`. \(\square\)

### Corollary 5.2 (the buffer class and five locks)

There is a six-colouring `phi` of `J` and a colour `alpha` such that:

1. the colour class

   \[
                         I_0=\phi^{-1}(\alpha)
   \tag{5.3}
   \]

   is nonempty and anticomplete to both `z,u`;
2. each pole has a neighbour of every colour `beta ne alpha`; and
3. after assigning `alpha` to both poles in `G-zu`, the two poles belong
   to one `alpha`--`beta` component for every `beta ne alpha`.

#### Proof

Use the common-singleton colouring obtained from `G/zu` in Proposition
5.1.  Its restriction to `J` uses all six colours because `chi(J)=6`, so
`I_0` is nonempty.  The definition of the common missing colour makes it
anticomplete to both poles.

If, say, `z` missed a second colour `beta`, then assigning `beta` to `z`
and `alpha` to `u` would restore the edge and six-colour `G`.  Thus both
poles see every other colour.

Finally assign `alpha` to both poles in the edge-deleted graph.  If the
poles lay in distinct `alpha`--`beta` components, interchange the two
colours on the component containing `z`.  This gives the poles different
colours, after which the edge `zu` can be restored, again six-colouring
`G`.  Hence all five component locks hold. \(\square\)

Five-connectivity of `J` turns the five saturated colour contacts into
five simultaneously vertex-disjoint pole-to-pole paths, by choosing one
neighbour of each non-`alpha` colour at each pole and applying Menger's
theorem to the two resulting five-sets.  This retains a permutation of the
five colours at the path ends, but the paths need not be bichromatic.  The
separate
[palette-permutation linkage note](hc7_adjacent_pair_palette_linkage.md)
records that construction and its exact branch-set consequences.

In the canonical balanced branch, the bichromatic path for the unique
colour absent from the five-clique `R union {ell_e,ell_f}` starts inside
`H`, as proved in the unique leaf--endpoint chromatic theorem.  The other
four locked components do not acquire that localization: three may use
the vertices of `R`, and the fourth may start through `ell_e`.  This is
the precise obstacle to treating the five locks as five paths in the
planar leaf-side society.

This is palette-labelled host information.  It still does not identify a
colour with one of the six rows in Theorem 3.1.  The surviving proof
obligation is therefore a colouring-to-labelled-model transition, not a
further optimization of the unrooted regenerated model.

## 6. Exact contribution

The theorem closes one proposed mechanism and sharpens the next target.

- The spanning `K_6` model after deleting `z,u` is canonical and does not
  require `HC_6`.
- A contact-maximal model has joint contact exactly five, so no
  low-contact branch-set lock survives at the optimum.
- The contact-five model is explicitly and reversibly coupled to the old
  singleton-centred `K_7`-minus-one-edge model.
- Only the six-colouring cover and its Kempe connections are new.  A
  positive continuation must use those colour transitions to produce a
  common boundary partition, an actual order-seven separation with the
  named data, or a model reassignment outside this reversible component.

The standard `K_2`-join-icosahedron example remains consistent with this
conclusion: its contact-five model also lies in a reversible singleton
one-hole component.  The present theorem explains why that guardrail is
structural rather than an accident of the example, while using the
canonical balanced boundary to identify the exchange explicitly.

The existing canonical-web missing-colour-path barrier gives the other
necessary guardrail.  A canonical four-root web can contain a fully locked
outer edge—both nontrivial missing-palette paths and all five ordinary
two-colour locks—while the repairing rooted linkage is absent.  That
example is not minor-critical and does not have the present literal
endpoint distribution, so it does not refute a host-level theorem.
It does show that Corollary 5.2 cannot be decoded by planar web geometry
alone.  The next mechanism must use the proper-minor transition together
with the literal split endpoints, rather than merely the existence of the
five locked components.
