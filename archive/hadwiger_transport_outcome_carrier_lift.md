# Lifting perfect and singly exposed transport through complex shores

## 1. Relative refinement capacity

Let

\[
                 \mathcal B=(B_1,\ldots,B_r)       \tag{1.1}
\]

be a clique minor model, and let `W` be a disjoint connected set adjacent
to every `B_i`.  For each `i`, let `P_{ij} subseteq B_i` be the portal set
from `B_i` to `B_j`, and let `P_{iW}` be its portal set to `W`.

Call a partition

\[
              B_i=B_i^1\dot\cup\cdots\dot\cup B_i^{q_i} \tag{1.2}
\]

a **full `q_i`-refinement** if its parts are nonempty, connected, pairwise
adjacent, and every part meets every portal class

\[
             P_{iW},\quad P_{ij}\ (j\ne i).         \tag{1.3}
\]

Thus every refined part remains adjacent to `W` and to every **unrefined**
branch bag.  Refinements in two different bags are called **compatible**
if every part of either refinement is adjacent to every part of the other.
This extra condition is essential: meeting the old portal set to a whole
bag does not identify which refined part contains the other end of a
portal edge.

### Theorem 1.1 (refinement-capacity completion)

If pairwise compatible full refinements can be chosen in distinct branch
bags and

\[
                    \sum_i(q_i-1)\ge s,             \tag{1.4}
\]

then the bags and `W` contain a `K_{r+1+s}` model.

#### Proof

Replace every refined `B_i` by its `q_i` parts.  The definition preserves
all adjacencies to unrefined bags and to `W`, and requires all adjacencies
among parts of the same refined bag.  Parts arising from different refined
bags are adjacent by compatibility.
The resulting clique model has

\[
        r+\sum_i(q_i-1)
\]

bags; adjoining `W` and discarding surplus bags proves the claim.
\(\square\)

The theorem is label-free and arbitrary-order.  It identifies the exact
internal capacity needed after the two-layer matching dichotomy.

## 2. Failure of duplication has one Helly torso

A branch bag is **duplicable** when it has a full `2`-refinement.  Regard
the portal sets in (1.3) as roots inside `B_i`; a connected subgraph is
rainbow when it meets every one of them.

### Theorem 2.1 (duplicate or rooted Helly core)

For every branch bag `B_i`, one of the following structural alternatives
holds; in particular, failure of the first forces the second.

1. `B_i` is duplicable.
2. In every tree decomposition of `B_i`, some bag meets every connected
   subgraph which is rainbow for the portal family (1.3).  In a Tutte
   decomposition this common bag is a gate of order at most two, a cycle
   torso, or a 3-connected torso; every component outside it misses a
   portal class and attaches through at most two torso vertices.

#### Proof

If two vertex-disjoint rainbow connected subgraphs exist, contract them,
take a spanning tree of `B_i`, and cut an edge on the path between their
images.  Lifting gives a connected adjacent bipartition; both sides remain
rainbow, so it is a full `2`-refinement.

If no two such subgraphs are disjoint, the inclusion-minimal rainbow
connected subgraphs are pairwise intersecting.  Project them to any tree
decomposition.  Their projections are pairwise intersecting subtrees, so
subtree Helly gives one common decomposition bag.  The adhesion and torso
conclusions are Theorem 1.1 and Corollary 2.1 of
`hadwiger_rainbow_torso_helly_core.md`. \(\square\)

This is stronger than saying that a shore “does not split”: all arbitrary
internal block trees and 2-separation chains collapse to one named rooted
torso.

## 3. Application to the two transport outcomes

Use Theorem 3.1 of
`hadwiger_flat_full_host_matching_dichotomy.md` with `n` connected
two-shore carriers and the connected boundary reserve

\[
                         W=\{b,c\}.                 \tag{3.1}
\]

### 3.1 Perfect transport

A perfect cross-nonedge matching is the compatible transport state.  One
of the two labelled layers already gives a `K_n` model, and `W` is full to
it.  Apply Theorem 1.1 with `r=n` and `s=2`.

Hence either one layer bag has a full 3-refinement, or two layer bags have
compatible full duplications, and the graph contains `K_{n+3}`.  If
neither occurs, then either

* at most one layer bag is duplicable, so all other layer bags have the
  gate/cycle/3-connected rooted Helly core of Theorem 2.1; or
* at least two layer bags are individually duplicable, but every pair of
  duplications has an explicit cross-compatibility failure.

Thus a target-free perfect-transport state is not an arbitrary collection
of complex bags.  It is a family of rooted indecomposable torsos with at
most one capacity exception, or it exposes a literal incompatibility
between two otherwise valid full splits.  That incompatibility is itself
a labelled transport obstruction; it cannot be erased by counting only
the old whole-bag portal sets.

### 3.2 Singly exposed favourable transport

If the cross-nonedge matching has order `n-1`, a minimum vertex cover
leaves `n+1` pairwise adjacent connected shores; these form a labelled
`K_{n+1}` model.  With `W`, this is a `K_{n+2}` model.  The favourable
unmatched shore is the type-zero `X` shore or type-one `Y` shore exposed
in Theorem 3.1.

Here Theorem 1.1 needs only `s=1`.  Therefore:

* if **any** branch bag of this `K_{n+1}` model is duplicable relative to
  the other `n` bags and `W`, the graph contains `K_{n+3}`;
* otherwise every one of its `n+1` branch bags has one rooted
  gate/cycle/3-connected Helly core, and every off-core lobe has a named
  missing portal class and adhesion at most two.

This is the weakest purely internal minor condition: a single full
duplication closes the singly exposed state, while its failure yields a
bounded-adhesion rooted obstruction rather than another portal list.

## 4. Colour and coherent-apex lifts

The two remaining nonminor mechanisms require information not contained
in the transport graph alone.

### Faithful colour lift

Fix a quotient colour state.  For each rooted torso and each incident
adhesion, record the relation of boundary colour assignments which extend
through the attached lobe.  If the selected perfect or singly exposed
transport state belongs to every such relation, relational composition
along the torso/adhesion tree gives proper colourings of all branch bags;
because the state also checks every interbag edge, their union is a global
`(n+2)`-colouring.

This “membership in every extension relation” is the exact weakest colour
hypothesis.  Abstract equality partitions are insufficient, as shown by
the leaf expansion in the cocycle note; the attachment relations must be
portal-faithful.

### Coherent rural lift

Suppose instead that every rooted Helly core has the rural alternative:
its portal occurrences admit a disk embedding in the cyclic order induced
by one common outerplane quotient, and all neighbours of one fixed neutral
vertex occur on the distinguished outer face.  The port-labelled disk
expansion theorem then embeds the whole remainder in the plane after two
fixed neutral vertices are deleted.  The graph is coherently two-apex and
therefore `(n+2)`-colourable in the `HC_7` case.

The word **common** is essential.  Independent rural embeddings with
incompatible rotations do not assemble; their first incompatibility must
be converted into a crossing, and hence into a full refinement or rooted
minor.

## 5. Exact remaining uniform lemma

The perfect and singly exposed transport outcomes have now been reduced
to the same statement.

> **Rooted-torso transport lift.**  For a family of portal-indecomposable
> gate/cycle/3-connected Helly cores carrying one common perfect or singly
> exposed transport state, either the extension relations contain that
> state, all rural rotations assemble around one fixed apex pair, or the
> first incompatible adhesion/rotation creates one full duplication.

The first outcome colours, the second is two-apex, and the third gives
`K_{n+3}` by Theorem 1.1.  This is an arbitrary-order carrier theorem;
it no longer mentions Moser labels, carrier size, or a finite portal
enumeration.  Proving it is the precise remaining lift from the now-closed
literal edge cell to the general normalized `K_7^vee` model.
