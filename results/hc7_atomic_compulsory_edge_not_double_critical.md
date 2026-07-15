# The atomic compulsory edge is not double-critical

**Status:** proved and independently audited.

## 1. Setup

Use the frozen connected-bipartite atomic kernel

\[
 V(G)=A\mathbin{\dot\cup}S\mathbin{\dot\cup}R,
 \qquad S=W\mathbin{\dot\cup}\{u\},\qquad |S|=7,
\]

where `G` is a minimal `HC_7` counterexample, `zu` is the unique edge
from `A` to `u`, there is no `A-R` edge, `A` is connected and `S`-full,
`G[S]` is connected and bipartite, and `R` contains two disjoint connected
`S`-full packets.  Assume also that `A-z` is nonempty, connected and
`W`-full.  In particular `G` is 7-chromatic and vertex-critical, while
the audited unordered asymmetric carrier theorem applies to connected
adjacent partitions of `A`.

## 2. A colourwise common-neighbour lemma

### Lemma 2.1

Let `xy` be an edge of a `k`-chromatic graph `F`.  If

\[
                         \chi(F-\{x,y\})\le k-2,
\tag{2.1}
\]

then every proper `(k-2)`-colouring of `F-{x,y}` has, in every colour,
a vertex adjacent to both `x` and `y`.

### Proof

First enlarge a colouring using fewer than `k-2` colours by adding unused
colour names.  Fix one colour `i` and suppose that no vertex of colour `i`
is a common neighbour of `x,y`.

Recolour every colour-`i` neighbour of `x` with one new colour `*`, give
`x` colour `i`, and give `y` colour `*`.  The recoloured neighbours of
`x` are pairwise nonadjacent because they formerly had one colour.  None
is adjacent to `y`, by the assumption that there is no colour-`i` common
neighbour.  All other edges retain their old proper colour pair.  This is
a proper `(k-1)`-colouring of `F`, contrary to `chi(F)=k`.  Thus every
colour has a common neighbour.  Distinct colours give distinct common
neighbours.  \(\square\)

## 3. Non-double-criticality

### Theorem 3.1

\[
                          \chi(G-\{z,u\})=6.
\tag{3.1}
\]

Consequently `G-{z,u}` contains a `K_6` minor.

### Proof

Vertex-criticality gives a six-colouring of `G-z`, and hence

\[
                          \chi(G-\{z,u\})\le6.
\tag{3.2}
\]

It is at least five: a colouring with at most four colours, followed by
two fresh colours on the adjacent vertices `z,u`, would six-colour `G`.

Assume for a contradiction that it equals five.  Apply Lemma 2.1 with
`k=7` to a five-colouring of `G-{z,u}`.  It gives five distinct common
neighbours of `z,u`, one in each colour.

Every such common neighbour lies in `W`.  It cannot lie in `R`, because
`z in A` and there is no `A-R` edge.  It cannot lie in `A`, because
`zu` is the unique `A-u` edge.  It is neither `z` nor `u`, so the only
remaining location is `S-{u}=W`.

Thus the singleton carrier `{z}` contacts `u` and at least five distinct
vertices of `W`, so

\[
                         |N_S(z)|\ge6.                 \tag{3.3}
\]

The carrier `A-z` is connected and `W`-full, hence also has old-boundary
support at least six.  The two carriers `{z}` and `A-z` are nonempty,
connected and adjacent and cover `A`; name the singleton as the carrier
containing the compulsory root.  The audited unordered asymmetric
carrier theorem now six-colours `G`, a contradiction.  Therefore the
value in (3.2) is six.

Hadwiger's conjecture is known for parameter six.  Applied to the
6-chromatic graph `G-{z,u}`, it supplies a `K_6` minor avoiding both
literal vertices `z,u`.  \(\square\)

### Corollary 3.2

\[
                         |N_G(z)\cap N_G(u)|\le4.       \tag{3.4}
\]

Hence, in any six-colouring of `G/e` lifted to `G-e`, at least one of the
five bichromatic `z-u` locks has no length-two `z-u` path.

### Proof

Five common neighbours would all lie in `W` by the location argument in
the proof of Theorem 3.1.  The carriers `{z}` and `A-z` would again have
support profile at least `(6,6)`, so the asymmetric carrier theorem would
close.

The five alternate-colour locks all contain `z,u`.  A length-two path in
one lock uses a common neighbour, and paths belonging to distinct alternate
colours use different common neighbours.  Bound (3.4) therefore leaves at
least one lock without a length-two path. \(\square\)

## 4. Exact use in the twin-seam decoder

The theorem permits the six-row model to be **regenerated after choosing
the compulsory edge**, instead of transporting one fixed `K_7^vee`
model through every gate rotation.  If

\[
                         \mathcal M=(F_1,\ldots,F_6)
\]

is such a model, the named edge `zu` lies wholly outside its bags.
The graph `G-{z,u}` is connected (indeed five-connected), so the model may
be enlarged to a spanning six-bag model by assigning every unused component
successively to an adjacent bag.  In the separating twin-seam response,
the complementary path `Q_0` contains `zu`; deleting that edge leaves a
`z`-end segment and a disjoint `u`-end segment.  Their first hits on the
spanning model are distinct literal vertices, but they may lie in the same
row.  Thus even this response supplies two distinct rows only after a
label-faithful same-row split has been proved.

The connected set `{z,u}` cannot contact all six bags, since it would then
be a seventh branch set of a `K_7` model.  Likewise neither endpoint alone
can contact all six bags.  These are only upper bounds: even a spanning
model need not distribute the two endpoint neighbourhoods among distinct
rows.

This does not by itself label the six bags.  Nor do two response-matched
`d-t` bypasses force a split of the bag or bags containing their first
hits: the paths may be concentrated inside one branch bag and all five
row portals of that bag may remain behind one internal bottleneck.  The
next valid promotion has to prove a labelled branch-set split, or obtain
the fixed-pair terminal when that split fails.  Palette colours cannot be
identified with the six rows of `mathcal M`.

## 5. Exact two-pole row constraints

The regenerated model nevertheless gives a useful literal target which
does not mention colours.  For a `K_6` model
`mathcal M=(F_1,...,F_6)` disjoint from `z,u`, put

\[
 C_z=\{i:E(z,F_i)\ne\varnothing\},\qquad
 C_u=\{i:E(u,F_i)\ne\varnothing\}.
\tag{5.1}
\]

### Lemma 5.1 (two-pole contact threshold)

If either

1. `|C_z cap C_u|>=5`; or
2. `|C_z cap C_u|>=4` and there are distinct rows
   `a in C_z-C_u`, `b in C_u-C_z`,

then `G` contains a literal `K_7` minor.

### Proof

In the first case use the singleton bags `{z},{u}` and any five model
bags contacted by both.  They are seven pairwise adjacent bags, with the
`z-u` edge supplying the only pair not internal to the `K_6` model.

In the second case retain four common-contact rows.  The union

\[
                              F_a\cup F_b
\]

is connected because the two model bags are adjacent.  It contacts `z`
through `F_a`, contacts `u` through `F_b`, and is adjacent to every
retained common row.  Together with `{z},{u}` and the four retained rows
it gives seven pairwise adjacent connected disjoint bags.  \(\square\)

### Corollary 5.2

In a `K_7`-minor-free host,

\[
                           \min\{|C_z|,|C_u|\}\le4.
\tag{5.2}
\]

Indeed, if both contact at least five of the six rows, then either their
intersection has order at least five, invoking Lemma 5.1(1), or it has
order four and each contact set has a distinct exclusive row, invoking
Lemma 5.1(2).

### Lemma 5.3 (the exact same-row split target)

Suppose `z` and `u` have literal neighbours in the same row `F_h`, and
`F_h` has disjoint connected subgraphs `X_z,X_u` such that

* `z` is adjacent to `X_z` and `u` is adjacent to `X_u`; and
* each of `X_z,X_u` is adjacent to every row `F_i`, `i ne h`.

Then `G` contains a literal `K_7` minor.

### Proof

Use

\[
       \{z\}\cup X_z,\quad \{u\}\cup X_u,
       \quad F_i\ (i\ne h).
\]

The first two bags are connected and adjacent through the literal edge
`zu`.  Each meets every one of the other five bags by hypothesis, and
those five retain their clique-model adjacencies.  \(\square\)

Lemma 5.3 is the exact labelled promotion which a same-row first-hit of
the five-rung bundle would have to fund.  Two internally disjoint paths
inside `F_h` are not enough: both resulting shores must retain all five
foreign-row duties.  This identifies the remaining obstruction as a
row-duty split, not path disjointness.
