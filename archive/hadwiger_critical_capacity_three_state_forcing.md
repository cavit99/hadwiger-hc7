# Critical capacity-three blocks: rooted `K_4` and the label gap

## Status

Vertex-criticality gives more than the original three-column note stated:
four locally parallel portals also have four distinct outside
representatives.  Four is the exact threshold forced by the antichain
property alone; at five, an antichain need not have an SDR.

A capacity-three `K_{3,3}` contact block with one common gate already
contains a rooted `K_4` model.  Three **state-forcing** private columns
upgrade that rooted model to four full neutral branch sets and hence a
`K_7` model.  However vertex-critical anti-domination supplies only
distinct outside endpoints, not their portal labels.  A seven-vertex
4-critical Mycielski architecture is the sharp warning: its three locally
parallel vertices export an antichain on exactly three endpoints and have
an unlabelled rooted `K_4`, but no prescribed portal row is replicated
across those branches.

Thus the two-star obstruction is not closed by the SDR alone.  The exact
remaining hypothesis is operation-sensitive: the three representatives
must link disjointly to the missing state row, or failure of that linkage
must be shown to be the same exact-seven boundary state on both sides.

## 1. Correct SDR threshold

Let `2<=m<=4`, and let `x_1,...,x_m` be pairwise nonadjacent and have the same neighbourhood
inside a selected module `U`.  In a vertex-critical graph their outside
neighbour sets form an antichain.

### Theorem 1.1 (four-column critical SDR)

The outside neighbour sets have a system of distinct representatives.
For a family of five sets, the antichain property alone no longer forces
an SDR.

#### Proof

Write `A_i=N(x_i)-U`.  If `A_i subseteq A_j`, equality of the inside
neighbourhoods gives `N(x_i) subseteq N(x_j)`, contrary to critical
anti-domination.  Thus the `A_i` are pairwise incomparable and nonempty.

For any subfamily of one set, the union is nonempty.  Two incomparable
nonempty sets have union of order at least two.  Three incomparable sets
cannot live on a two-element ground set, whose largest antichain has order
two.  Four incomparable sets cannot live on a three-element ground set,
whose largest antichain has order three.  These are all Hall inequalities
for a family of order at most four.

To see the limit of this argument, choose five of the six two-subsets of
a four-element set.  They form an antichain but their union has order
four, so no SDR exists.  This is an abstract antichain example; no claim
is made here that this particular family is realized as the outside
profiles of a vertex-critical graph.
\(\square\)

## 2. A capacity-three block already has a rooted `K_4`

### Lemma 2.1 (three-by-three gate model)

Let `L_1,L_2,L_3,R_1,R_2,R_3,Z` be pairwise disjoint connected sets.
Assume

* every `L_i` is adjacent to every `R_j`; and
* the connected set `Z` is adjacent to every `L_i`.

Then the four branch sets

\[
              Z,\qquad L_i\cup R_i\quad(i=1,2,3)   \tag{2.1}
\]

form a `K_4` model.

#### Proof

Each `L_i union R_i` is connected.  For `i ne j`, the edge class
`L_iR_j` joins the corresponding two branch sets.  The set `Z` meets each
through `L_i`. \(\square\)

This applies directly to either `K_{3,3}` cross-lobe block in the sharp
two-star architecture, with the star centre as `Z`.  Hence nonplanarity
itself is not the missing issue; preservation of all state rows is.

## 3. Exact state-forcing completion

### Theorem 3.1 (three missing-row columns force `K_7`)

Let `Q={q_1,q_2,q_3}` be a triangle.  Suppose a graph disjoint from `Q`
contains four pairwise adjacent connected branch sets

\[
                       B_0,B_1,B_2,B_3.             \tag{3.1}
\]

Assume `B_0` is `Q`-full.  For `i=1,2,3`, let `C_i` be pairwise disjoint
connected sets, disjoint from all `B_j`, such that

* `C_i` is adjacent to `B_i`;
* `B_i union C_i` is adjacent to every member of `Q`; and
* `B_0` remains adjacent to each `B_i union C_i`.

Then the graph contains a `K_7` minor.

#### Proof

The four sets `B_0,B_1 union C_1,B_2 union C_2,B_3 union C_3` are
disjoint connected and pairwise adjacent.  Each is adjacent to all three
singleton bags of `Q`.  These seven bags form a `K_7` model. \(\square\)

Combining Lemma 2.1 with Theorem 3.1 gives the exact capacity-three
closure.  In the `{1,2}` block of the two-star architecture, take
`B_i=L_i union R_i`; the connected remainder containing the two star
centres is the reservoir `B_0`.  Three disjoint columns which give the
`B_i` the missing row 3 produce `K_7`.  The complementary `{2,3}` block
is symmetric.

### Theorem 3.2 (atomic three-pair linkage or exact four-cut)

Let `H` be four-connected, let `T` contain at least three vertices, and
let `C_1,C_2,C_3` be pairwise disjoint connected **two-vertex** sets,
disjoint from `T`.  Then either

1. there are three disjoint connected sets `P_i superseteq C_i`, each
   meeting a different vertex of `T`; or
2. for some distinct `i,j`, the four vertices of `C_i union C_j` form an
   exact separator between the remaining `C_k` and `T`.

#### Proof

Contract each `C_i` to a protected source vertex `c_i`.  If three
disjoint source--`T` paths exist, lifting them gives outcome 1.  Otherwise
the set form of Menger's theorem gives a source--`T` separator `Z` of
order at most two in the contracted graph.  Separators are allowed to
contain source or target vertices; the three protected sources and the
at least three targets are otherwise disjoint.

If `Z` contains no contracted source, it lifts to a separator of `H` of
order at most two.  At least one target and all three source pairs remain,
so this is a genuine disconnection.  If `Z` contains exactly one source,
replacing that source by its two-vertex preimage gives a separator of
order at most three; the other two source pairs and at least two targets
remain.  Both alternatives contradict four-connectivity.  Therefore `Z`
has order two and consists of two contracted sources `c_i,c_j` (and no
target).  Its
inverse image is exactly `C_i union C_j`, of order four, and separates
the third source from `T`.  This is outcome 2. \(\square\)

If `H=G-Q` for a neutral triangle `Q` in a seven-connected graph, the
second outcome lifts to the exact seven-vertex adhesion

\[
                         Q\cup C_i\cup C_j.         \tag{3.2}
\]

Thus an atomic `K_{3,3}` block whose three row-pairs are literal portal
edges has three mutually disjoint continuations to distinct missing-row
targets unless it lands precisely in the four-vertex full-adhesion state.
To invoke Theorem 3.1 one must additionally verify that these
continuations can be assigned without consuming the `Q`-full reservoir
`B_0` (or that `B_0` remains connected and `Q`-full after their target
vertices are reassigned).  Four-connectivity alone does not protect that
reservoir.  For arbitrary connected lobes the protected pairs can also be
large, and the warehouse obstruction reappears; the two-vertex hypothesis
is substantive.

Likewise, (3.2) is the exact **structural** seven-adhesion.  Colour gluing
still requires the proper-minor extension relations induced on that same
seven-vertex boundary to agree on its two sides; Theorem 3.2 does not by
itself synchronize those states.

### Corollary 3.3 (the exact cut is a full adhesion)

If `G` is seven-connected and the second outcome of Theorem 3.2 occurs in
`H=G-Q`, then every component `K` of

\[
             G-(Q\cup C_i\cup C_j)
\]

has neighbourhood exactly `Q union C_i union C_j`.

#### Proof

The neighbourhood of `K` is contained in the displayed seven-set.  If it
were a proper subset, deleting `N_G(K)` would disconnect `K` from the
rest of `G` with at most six vertices, contrary to seven-connectivity.
\(\square\)

Thus the linkage failure does produce the common **structural** boundary
on every side.  What remains operation-sensitive is equality of the
six-colour extension relations on that full boundary.

## 4. What criticality does and does not provide

The three-column theorem gives distinct first neighbours outside the
chosen module.  It does not imply that those neighbours

* lie in the missing neutral portal row;
* have disjoint continuations to that row;
* avoid the reservoir branch set; or
* induce the same proper-minor boundary state on the opposite side of an
  exact seven-cut.

These are precisely the hypotheses of Theorem 3.1 which remain absent.

The gap is real even in an actual critical graph.  Take the Mycielskian
of `K_3`, with original triangle `v_0,v_1,v_2`, independent clone
vertices `u_0,u_1,u_2`, and a vertex `w` adjacent to every clone.  It is
4-vertex-critical.  Relative to

\[
                         U=\{w,u_0,u_1,u_2\},       \tag{4.1}
\]

the three clones are locally parallel and their outside profiles are

\[
 \{v_1,v_2\},\qquad\{v_0,v_2\},\qquad\{v_0,v_1\}. \tag{4.2}
\]

This is a three-set antichain on exactly three outside vertices.  An SDR
exists, but there is no fourth outside column.  The graph even has the
unlabelled rooted model

\[
 \{w\},\quad\{u_0,v_1\},\quad
 \{u_1,v_2\},\quad\{u_2,v_0\}.                    \tag{4.3}
\]

If a required state row is concentrated at `w`, only one of these branch
sets carries it; the rooted model is not state-forcing.  Thus neither the
SDR nor an unlabelled rooted `K_4` supplies the labelled conclusion.

This example refutes a vertex-critical-only capacity-three closure.  It
does not refute a contraction-critical operation theorem: synchronizing
the colour states of deletions/contractions may force the SDR endpoints
to the missing row or to a common exact-seven boundary signature.  That
operation synchronization is the precise additional hypothesis still
needed.

## 5. Exact next theorem

The remaining target can now be stated without portal enumeration.

> **Critical three-column linkage theorem.**  For a capacity-three
> cross-lobe block in a 7-contraction-critical host, the three private
> representatives on one side either have disjoint continuations to the
> block's missing state row, satisfying Theorem 3.1, or a separator of
> order at most two carrying their failed linkage has the same
> proper-minor extension relation on both sides of the surrounding exact
> seven-adhesion.

The first outcome gives `K_7`.  The second is the common boundary state
needed for colour gluing.  Vertex-critical anti-domination proves only the
first edge of each proposed continuation; contraction-criticality must be
used to prove the rest.
