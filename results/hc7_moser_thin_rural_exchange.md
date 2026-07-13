# A near-full split exchange in the pure-Moser rural shore

## Status

This proved and independently audited note closes an unbounded part of the exact one-duty-per-row rural
residue in `../results/hc7_moser_crossing_carrier.md`.  Its main theorem is
literal: if the rural component can be divided into two adjacent connected
pieces, each missing at most one of the seven boundary vertices, then the
already-crossed page and the Moser boundary give a `K_7` model.  No equality
state, palette-to-label identification, or bounded-transversal assertion is
used.

Consequently a surviving rural component has at least three vertices and is
2-connected.  In particular every tree shore and every shore with a bridge
is eliminated, regardless of order.  A second argument closes every rural
cycle of length at least four.  Thus the only cactus shore not eliminated by
this note is a single triangle.

## 1. Fixed crossed-page input

Use the pure-Moser labelling

\[
 E(M)=\{01,02,03,04,12,16,26,34,35,45,56\}.             \tag{1.1}
\]

The favorable crossing in `C_1` contains two internally boundary-disjoint
paths, one from `0` to `5` and one from `2` to `4`.  Only the latter is needed
below.  Fix a `2`--`4` path

\[
                         Q=2\,Q^\circ\,4                 \tag{1.2}
\]

whose non-boundary vertices lie in `C_1`.  Thus `Q` is disjoint from the
rural component `C_2`, from `v`, and from `N-\{2,4\}`.

The ordinary carrier completion from the cited note uses the two duty pairs

\[
                         A=\{1,4\},\qquad B=\{3,2\}.     \tag{1.3}
\]

Namely a connected rural piece meeting both labels of `A` can be attached to
row `1`, and a disjoint adjacent piece meeting both labels of `B` can be
attached to row `3`.  The point of Section 2 is to close the two exceptional
same-pair defect patterns for which neither orientation works.

## 2. Two alternative five-carrier frames

For a path `Q` with ends `2,4`, the notation `Q-2` denotes the connected
subpath obtained by deleting the end `2`, and similarly for `Q-4`.
For `Z\subseteq C_2`, put

\[
                         D(Z)=N-N_G(Z).                   \tag{2.0}
\]

### Lemma 2.1 (the `14`-defect frame)

The following five sets are disjoint connected pairwise adjacent branch
sets:

\[
 \{0\},\quad \{2\},\quad \{1,6\},\quad \{3,v\},\quad
                         (V(Q)-\{2\})\cup\{5\}.          \tag{2.1}
\]

Moreover, every connected set `Z\subseteq C_2` with
`D(Z)\subseteq\{1\}` or `D(Z)\subseteq\{4\}` is adjacent to all five sets
in (2.1).

#### Proof

Connectivity follows from the edges `16`, `3v`, and `45`; the last edge adds
`5` to the connected path `Q-2`, which contains `4`.  Disjointness follows
from (1.2).

For pairwise adjacency, the first four sets use the Moser edges `02,01,03,
12,26` and the edges from `v` to all of `N`.  The set `\{0\}` meets the last
bag through `04`; `\{2\}` meets it through the first edge of `Q`; `\{1,6\}`
meets it through `65`; and `\{3,v\}` meets it through `34` (also through the
edges from `v` to `4,5`).

A rural set missing `1` still contacts `0,2,6,3,4,5`, and a rural set missing
`4` still contacts `0,2,1,6,3,5`.  In either case these literal boundary
contacts meet every displayed bag.  \(\square\)

### Lemma 2.2 (the `23`-defect frame)

The following five sets are disjoint connected pairwise adjacent branch
sets:

\[
 \{0\},\quad \{4\},\quad \{3,5\},\quad \{1,v\},\quad
                         (V(Q)-\{4\})\cup\{6\}.          \tag{2.2}
\]

Moreover, every connected set `Z\subseteq C_2` with
`D(Z)\subseteq\{2\}` or `D(Z)\subseteq\{3\}` is adjacent to all five sets
in (2.2).

#### Proof

The last bag is connected because `Q-4` contains `2` and `26` is an edge.
The other nonsingleton bags use `35` and `1v`.  The pairwise contacts are
witnessed by

\[
 04,03,01,02;\qquad 43,45,4v;\qquad 3v,56;\qquad 16,
\]

together with the last edge of `Q`, which joins `\{4\}` to `Q-4`.  These
contacts cover every pair of displayed bags.

A rural set missing `2` still meets the last bag at `6`, while one missing
`3` still meets the third bag at `5`; all other displayed bags contain a
different literal boundary vertex.  Hence either type of rural set contacts
all five bags.  \(\square\)

The use of the crossed path `Q` is essential in both frames: it supplies the
otherwise absent `2`--`4` adjacency without identifying a quotient vertex
with a literal boundary vertex.

## 3. The near-full split theorem

### Theorem 3.1 (near-full rural split closes)

Suppose

\[
                         C_2=X\mathbin{\dot\cup}Y         \tag{3.2}
\]

where `X,Y` are nonempty connected sets with an edge between them, and

\[
                         |D(X)|\le1,\qquad |D(Y)|\le1.    \tag{3.3}
\]

Then `G` contains a literal `K_7` model.

#### Proof

First suppose one can orient the two pieces so that one, say `X`, contacts
both `1,4` and the other contacts both `3,2`.  Use `X` as the row-`1`
carrier and `Y` as the row-`3` carrier in Theorem 2.1 of
`../results/hc7_moser_crossing_carrier.md`.  The two sets are already
adjacent, so its seven displayed bags give a literal `K_7`.  The same applies
with the roles of `X,Y` reversed.

Assume neither orientation works.  Since `C_2` is full to `N`, no boundary
label belongs to both `D(X)` and `D(Y)`.  The elementary two-pair alternative
is then exact:

\[
                         \{D(X),D(Y)\}=\{\{1\},\{4\}\}
 \quad\hbox{or}\quad
                         \{D(X),D(Y)\}=\{\{3\},\{2\}\}. \tag{3.4}
\]

Indeed, if the first orientation fails because `X` misses a member of `A`,
then the reverse orientation can fail only because `Y` misses the other
member of `A`; the defects are distinct.  If `X` does not miss `A`, the first
failure forces `Y` to miss `B`, and the reverse failure forces `X` to miss
the other member of `B`.  An empty defect cannot survive both orientation
tests.

In the first case of (3.4), Lemma 2.1 gives five clique carriers and says
that each of `X,Y` is adjacent to all five.  The old `XY` edge makes `X,Y`
adjacent, so these five sets together with `X,Y` are seven disjoint connected
pairwise adjacent branch sets.  Lemma 2.2 gives the identical conclusion in
the second case.  \(\square\)

This theorem uses only the literal crossed path and full-neighbourhood
geometry.  In particular Corollary 3.3 (packet-thinness) of the source note
is compatible with, but not needed for, this closure.

## 4. Consequences for the rural shore

### Corollary 4.1 (no cutvertex)

In the counterexample-derived setup, `C_2` has no cutvertex.

#### Proof

Suppose `z` is a cutvertex, and let `K` be a component of `C_2-z`.  Since
`C_2-z` has at least two components, put

\[
                         X=V(K),\qquad Y=V(C_2)-V(K).     \tag{4.1}
\]

Both sets are connected, and every edge from `K` to the rest of `C_2` ends
at `z`, so they are adjacent.  Also

\[
                         N_G(K)\subseteq N\cup\{z\}.     \tag{4.2}
\]

If `K` contacted at most five boundary vertices, those vertices together
with `z` would be a cut of order at most six separating the nonempty set
`K` from the opposite exterior component (and from `v`).  Seven-connectivity
therefore gives `|N_N(X)|\ge6`.

Choose a second component `K'` of `C_2-z`.  The same argument gives
`|N_N(K')|\ge6`; since `K'\subseteq Y`, also `|N_N(Y)|\ge6`.  Theorem 3.1
applies.  \(\square\)

### Corollary 4.2 (no bridge, including the two-vertex shore)

The component `C_2` has no bridge.

#### Proof

If `xy` is a bridge, its deletion divides `C_2` into connected sets `X,Y`,
with `x\in X,y\in Y`.  Every external neighbour of `X` lies in `N\cup\{y\}`.
Seven-connectivity therefore gives `|N_N(X)|\ge6`; symmetrically
`|N_N(Y)|\ge6`.  The bridge is an `XY` edge, so Theorem 3.1 applies.  This
argument includes `C_2=K_2`.  \(\square\)

### Corollary 4.3 (the singleton shore is impossible)

The component `C_2` is not a singleton.

#### Proof

If `C_2=\{x\}`, full attachment gives

\[
                         N_G(x)=N=N_G(v).                 \tag{4.3}
\]

The vertices `x,v` are nonadjacent.  A six-colouring of the proper minor
`G-x` exists by vertex-criticality.  Giving `x` the colour of `v` then
extends it to a six-colouring of `G`, because `x` and `v` have the same open
neighbourhood.  This is impossible.  \(\square\)

Combining the three corollaries, a surviving rural component has at least
three vertices and is 2-connected (and 2-edge-connected).  Every forest
shore is therefore closed.

### Lemma 4.4 (cyclic defect split)

Let `n\ge4`, and let `D_0,\ldots,D_{n-1}` be subsets of a set `S`, each of
order at most two, with

\[
                         \bigcap_{i=0}^{n-1}D_i=\varnothing. \tag{4.4}
\]

Either the cyclic order has a division into two nonempty consecutive
intervals `I,J` such that

\[
              \left|\bigcap_{i\in I}D_i\right|\le1,
              \qquad
              \left|\bigcap_{j\in J}D_j\right|\le1,       \tag{4.5}
\]

or there are a two-set `D` and one index `w` such that

\[
                              D_i=D\quad(i\ne w).           \tag{4.6}
\]

#### Proof

Assume (4.5) never occurs.  If some `D_w` has order at most one, use
`\{w\}` as one interval.  The complementary interval must have intersection
of order two, so every one of its sets, all of order at most two, equals one
fixed two-set `D`.  This is (4.6).

We may therefore assume every `D_i` has order two.  They are not all equal
by (4.4), so cyclically relabel to make `D_0\ne D_1`.  The interval
`\{0,1\}` has intersection of order at most one.  Hence its complement has
intersection of order two, which says

\[
                         D_2=D_3=\cdots=D_{n-1}=E          \tag{4.7}
\]

for one two-set `E`.  If `D_1=E`, all but `D_0` already equal `E`.  If
`D_1\ne E`, apply the same argument to the interval `\{1,2\}`.  Its
complement contains `D_0` and copies of `E`, and must have intersection of
order two; therefore `D_0=E`.  Again all but one set equal `E`.  \(\square\)

### Corollary 4.5 (all rural cycles of length at least four close)

The component `C_2` is not a cycle of length at least four.

#### Proof

Write the cycle as `x_0x_1\ldots x_{n-1}x_0` and put

\[
                              D_i=N-N_G(x_i).              \tag{4.8}
\]

Every `x_i` has only its two cycle neighbours outside `N`.  Since the
hypothetical counterexample has minimum degree at least seven,
`|D_i|\le2`.  Full attachment of `C_2` to `N` gives (4.4).

If Lemma 4.4 gives the intervals `I,J`, take the corresponding two cycle
arcs as `X,Y`.  They are nonempty and connected, and the two cut cycle edges
make them adjacent.  The boundary defect of an arc is the intersection of
the defects of its vertices, so (4.5) is exactly the hypothesis of
Theorem 3.1.

It remains to exclude (4.6).  Let `D=\{a,b\}` and let `w=x_w` be the
exceptional cycle vertex.  Every vertex of `C_2-w` misses both `a,b`.
Consequently

\[
                              \{w\}\cup(N-D)               \tag{4.9}

\]

is a set of six vertices separating the nonempty path `C_2-w` from `v` and
the opposite exterior shore: its only cycle contacts outside the path go to
`w`, and all of its boundary contacts lie in `N-D`.  This contradicts
seven-connectivity.  \(\square\)

A cactus with at least two blocks has a cutvertex and is closed by Corollary
4.1.  A one-block cactus is a vertex, an edge, or a cycle.  Corollaries
4.2--4.5 therefore close every cactus rural shore except the single triangle.

## 5. Exact remaining rural problem

The one-duty-per-row residue has now lost every tree, block-chain, pendant
block, cycle of length at least four, and other cutvertex architecture.  What
remains is a 2-connected, packet-thin labelled society with the fixed rural
order `1,3,4,2`; among cactus shores only the triangle remains.

The next constructive step must use that 2-connectivity to obtain one of:

1. two disjoint row carriers, which Theorem 2.1 of the source note completes;
2. another near-full split, which Theorem 3.1 completes;
3. a proper-minor equality state matching one from the crossed shore; or
4. one planar expansion compatible with the crossed page after deleting at
   most three fixed vertices.

Packet packing number one must not be replaced by an unproved bounded
transversal.  This note does not claim that 2-connectivity and rurality alone
close the remaining society.

## Dependencies

1. `../results/hc7_moser_crossing_carrier.md`, especially its Theorem 2.1
   and the literal favorable `2`--`4` crossed path.
2. Seven-connectivity and proper-minor six-colourability of the hypothetical
   minimal `HC_7` counterexample.

No computation is used in the proof.
