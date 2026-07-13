# The exact seven-cut boundary threshold for two carrier gates

## Status

This note gives a rigorous first closure of the exact order-seven adhesion

\[
                 S=Q\mathbin{\dot\cup}Z_D\mathbin{\dot\cup}Z_E,
                 \qquad |Q|=3,\quad |Z_D|=|Z_E|=2,              \tag{0.1}
\]

from Theorem 3.4 of `hadwiger_qfull_carrier_adhesion_lift.md`.
It classifies the labelled equality-state universe in terms of the
missing-edge graph, proves a proper-minor **private block** transition for
every independent boundary block, and closes every boundary with at most
four missing edges.  In particular, if both displayed gate pairs are
independent, at least three further boundary nonedges are forced.

The final section gives a sharp qualitative static survivor: the icosahedron joined
with `K_2` realizes this exact triangle-plus-two-gates geometry with
missing-edge graph `C_5`.  It is seven-connected and `K_7`-minor-free but
is coherently two-apex.  Thus the threshold theorem reaches a
genuine rural state; excluding it requires the proper-minor state
transition, not more static gate counting.

## 1. Fullness and the exact state universe

Let `G` be seven-connected and let `S` be a seven-vertex cut.  Write

\[
                         J=G[S],\qquad F=\overline J.             \tag{1.1}
\]

### Lemma 1.1 (every open shore is full)

Every component `C` of `G-S` satisfies

\[
                              N_G(C)=S.                           \tag{1.2}
\]

#### Proof

The neighbourhood of `C` is contained in `S` and separates the nonempty
component `C` from every other component of `G-S`.  Seven-connectivity
gives `|N(C)|>=7`, while `|S|=7`.  Hence equality holds in (1.2).
\(\square\)

### Lemma 1.2 (equality states are clique partitions of `F`)

An equality partition `Pi` of `S` is proper for `J` if and only if every
block of `Pi` induces a clique in `F`.  It is a possible six-colour
boundary state only if it has at most six blocks.  If `Q subseteq S`
induces a triangle in `J`, every block contains at most one vertex of
`Q`.

#### Proof

A colour block is precisely an independent set of `J`, equivalently a
clique of its complement `F`.  Distinct vertices of the triangle `Q`
are adjacent in `J` and therefore cannot share a block.  \(\square\)

This is the complete equality-state classification up to palette
permutation: the labels of the blocks matter, but colour names do not.
The extension family of a closed shore is a subfamily of these clique
partitions.

## 2. The proper-minor private-block witness

Assume now that `G` is not six-colourable and every proper minor of `G`
is six-colourable.  Let `C` be a component of `G-S`, and let

\[
                    H_C=G-C                                      \tag{2.1}
\]

retain all seven labelled boundary vertices.

### Theorem 2.1 (full-shore private block transition)

For every nonempty independent set `P subseteq S`, the extension family
of `H_C` contains a state in which `P` is one exact colour block: all
vertices of `P` have one colour and no vertex of `S-P` has that colour.

Equivalently, for every clique `P` of the missing-edge graph `F`, a
proper minor operation on the opposite full shore produces a labelled
boundary state having `P` as a private block.

#### Proof

By Lemma 1.1, `C` is connected and every `p in P` has a neighbour in
`C`.  Hence

\[
                             C\cup P                              \tag{2.2}
\]

is connected.  Contract it to one vertex `z`.  This is a proper minor of
`G`, so it has a six-colouring.  Restrict the colouring to the vertices
outside `C` and expand every member of `P` with the colour of `z`.

The expansion is proper.  There is no edge inside `P`, and every edge
from a member of `P` to a retained vertex became an edge incident with
`z` under the contraction.  Moreover `z` is adjacent to every vertex of
`S-P`, because the full component `C` has a neighbour at each such
boundary vertex.  Thus no vertex of `S-P` has the colour of `z`, proving
that `P` is an exact private block.  \(\square\)

The theorem is stronger than static colour saturation.  It supplies a
separate proper-minor witness for every independent boundary block.  It
does not assert that the remaining blocks of the resulting states are the
same for two different shores; equality of those residual blocks is the
precise gluing issue.

### Corollary 2.2 (one-block full-adhesion gluing)

Let `(A,B)` be the separation obtained by putting at least one component
of `G-S` on each side.  If an independent set `P subseteq S`, `|P|>=2`,
has the property that `J[S-P]` is a clique, then `G` is six-colourable.

#### Proof

Contract a full component on the `A`-side together with `P`.  In the
resulting six-coloured proper minor, the contracted image and the
`|S-P|` boundary singletons form a clique: fullness supplies all edges
from the image, and `J[S-P]` supplies the remaining edges.  Since
`|S|=7` and `|P|>=2`, this clique has at most six vertices.  Expanding
gives a colouring of the closed `B`-side with the exact state

\[
              P\mid\{x\}\quad(x in S-P).                         \tag{2.3}
\]

The symmetric contraction on the `B`-side gives the same exact state on
the closed `A`-side.  Align the palette on the two copies of (2.3) and
glue across `S`, contradicting non-six-colourability.  \(\square\)

No completeness between `P` and `S-P` is needed: the contracted full
shore supplies it in the proper minor.  This is the exact strengthening
of the ordinary one-block adhesion lemma available at a full cut.

### Corollary 2.3 (the missing graph is nonsplit)

In a minor-minimal non-six-colourable `K_7`-minor-free graph in the
seven-connected counterexample setting, the missing-edge graph
`F=overline{G[S]}` of a full exact seven-adhesion is not a split graph.
Consequently `F` contains an induced `2K_2`, `C_4`, or `C_5`.

#### Proof

Suppose `F` has a split partition `S=P dotunion R`, where `P` is a clique
and `R` is independent.  Since Corollary 3.2 below gives
`tau(F)>=3`, and `P` itself is a vertex cover of `F`, we have
`|P|>=3`.  In the original boundary graph `J`, the set `P` is
independent and `J[R]` is a clique.  Corollary 2.2 therefore six-colours
`G`, a contradiction.

For completeness, the standard split-graph characterization says that a
finite graph is split exactly when it has no induced `2K_2`, `C_4`, or
`C_5`.  Applying its contrapositive gives the last assertion. \(\square\)

This is the first structural rather than enumerative description of the
four-defect residue.  The induced `2K_2` and `C_4` alternatives are the
nonrural exchange candidates; the induced `C_5` is realized sharply by
the coherent two-apex example in Section 6.

## 3. Two full shores repair every boundary with at most three defects

The next result is purely a labelled minor theorem and does not use
colour criticality.

### Theorem 3.1 (two-shore boundary completion)

Let `S` have order seven, let `A,B` be disjoint connected sets outside
`S`, and suppose each is adjacent to every vertex of `S`.  Put
`F=overline{G[S]}`.  If either

1. `F` has a vertex cover of order at most two; or
2. `F` consists of three pairwise disjoint edges and one isolated vertex,

then `G[S union A union B]` contains a labelled `K_7` minor.

#### Proof

First suppose a set `{x,y}` covers every edge of `F`; if a smaller cover
exists, enlarge it arbitrarily to two distinct vertices.  Then
`S-{x,y}` induces a `K_5`.  Use the seven branch sets

\[
               A\cup\{x\},\quad B\cup\{y\},\quad
               \{s\}\ (s in S-\{x,y\}).                         \tag{3.1}
\]

The first two sets are connected.  They are adjacent through an edge from
`A` to `y`, and both are adjacent to every singleton through fullness.
The five singleton bags form a clique.  Hence (3.1) is a `K_7` model.

Now suppose

\[
 E(F)=\{x_1y_1,x_2y_2,x_3y_3\},\qquad
 S=\{x_1,y_1,x_2,y_2,x_3,y_3,r\}.                              \tag{3.2}
\]

Use

\[
 \{x_1\},\ \{x_2\},\ \{x_3\},\ \{r\},\ A,\
 \{y_1,y_2\},\ B\cup\{y_3\}.                                \tag{3.3}
\]

The bag `{y_1,y_2}` is connected because its two vertices belong to
different missing pairs.  The last bag is connected by fullness.  The
four boundary singletons form a clique; `{y_1,y_2}` sees each `x_i`
through the endpoint belonging to a different missing pair; and every
remaining adjacency involving `A` or `B` follows from fullness.  Thus
all seven bags in (3.3) are pairwise adjacent.  \(\square\)

### Corollary 3.2 (four-defect threshold)

If `G` is seven-connected and `K_7`-minor-free, every seven-cut `S`
satisfies

\[
                     |E(\overline{G[S]})|\ge4.                  \tag{3.4}
\]

More precisely, its missing-edge graph has vertex-cover number at least
three and is not `3K_2 dotunion K_1`.

#### Proof

Choose two components of `G-S`; Lemma 1.1 makes them the full sets `A,B`
of Theorem 3.1.  A graph with at most three edges has vertex-cover number
at most two unless its three edges are pairwise disjoint.  The two cases
of Theorem 3.1 therefore exhaust all missing-edge graphs of order at most
three.  \(\square\)

### Corollary 3.3 (two independent gates need three further defects)

In (0.1), suppose both `Z_D` and `Z_E` are independent pairs in `G[S]`.
Then a seven-connected `K_7`-minor-free graph has at least two further
boundary nonedges besides the two gate-pair nonedges by Corollary 3.2,
and in fact at least three by Theorem 3.4 and Corollary 3.5 below.

Thus the clean two-pair boundary and every one- or two-extra-edge repair
of it are eliminated in one statement.

### Theorem 3.4 (every four-defect boundary closes)

Under the hypotheses of Theorem 3.1, if `F` has exactly four edges, then
`G[S union A union B]` contains a labelled `K_7` minor.

#### Proof

If `tau(F)<=2`, apply Theorem 3.1.  Suppose `tau(F)>=3`.  An elementary
component count leaves exactly three isomorphism types (isolated vertices
are suppressed):

\[
                  K_3\dot\cup K_2,\qquad
                  P_4\dot\cup K_2,\qquad
                  P_3\dot\cup2K_2.                \tag{3.5}
\]

Indeed, a connected graph with four edges has vertex-cover number at most
two.  For a `3+1` distribution, the three-edge component must have cover
number two, giving `K_3` or `P_4`; for `2+1+1`, the two-edge component is
`P_3`; `2+2` has cover number two, and four independent edges require
eight vertices.

For `K_3 union K_2`, label the missing triangle `012`, the missing edge
`34`, and the two isolates `5,6`.  The seven bags

\[
 \{0\},\{3\},\{5\},\{6\},A,\{1,4\},B\cup\{2\}   \tag{3.6}
\]

form a `K_7` model.  For `P_4 union K_2`, label the missing path
`0-1-2-3`, the missing edge `45`, and isolate `6`; use

\[
 \{0\},\{2\},\{4\},\{6\},A,\{1,5\},B\cup\{3\}. \tag{3.7}
\]

For `P_3 union 2K_2`, label the missing path `0-1-2` and missing edges
`34,56`; use

\[
 \{0\},\{2\},\{3\},\{5\},A,\{1,4\},B\cup\{6\}. \tag{3.8}
\]

Every displayed two-vertex boundary bag is connected because its pair is
not an edge of `F`; every bag involving a shore is connected by fullness.
Direct inspection of (3.5) shows that the remaining boundary bags are
pairwise adjacent, and all adjacencies involving `A` or `B` follow from
fullness. \(\square\)

### Corollary 3.5 (five-defect threshold)

Every exact seven-cut in a seven-connected `K_7`-minor-free graph
satisfies

\[
                     |E(\overline{G[S]})|\ge5.      \tag{3.9}
\]

Thus the first static nonsplit residues occur at five defects.  Exact
branch-set enumeration at that order has two survivors:
`C_5 union 2K_1` and `K_3 union 2K_2`; the former is the coherent rural
example of Section 6, while the latter is closed by the crossing-or-web
theorem in `hc7_near_k7_exact7_k322_web_closure.md`.

## 4. Equality states at the last three-defect candidate

Although Theorem 3.1 already eliminates it, the state classification of
the extremal candidate records the finite-boundary polarity exactly.
Let

\[
                       F=3K_2\mathbin{\dot\cup}K_1              \tag{4.1}
\]

with missing pairs `P_1,P_2,P_3` and singleton `r`.  Every proper
equality state has `r` as a singleton block, and independently either
splits or identifies the two vertices of each `P_i`.  A six-colour state
must identify at least one pair.  Hence the labelled state universe is

\[
          \{T:emptyset ne T subseteq \{1,2,3\}\},               \tag{4.2}
\]

where `i in T` means that `P_i` is monochromatic.  Up to permutation of
the three pair labels there are exactly the three weights
`|T|=1,2,3`.

Theorem 2.1 says that the extension family of either closed shore meets
each coordinate star `{T:i in T}`.  Static private witnesses alone could
still polarize two abstract state families; the explicit model (3.3) is
the graph-theoretic transition which closes this cell.

## 5. Critical private contacts

The following standard criticality fact explains what replaces false
twin gate rows after the four-defect threshold.

### Lemma 5.1 (no nested nonadjacent neighbourhoods)

If `G` is vertex-critical with chromatic number seven and `xy` is a
nonedge, then neither

\[
                         N(x)subseteq N(y)
             \quad\hbox{nor}\quad N(y)subseteq N(x)             \tag{5.1}
\]

holds.  Consequently, if `x,y` have identical neighbours inside the
seven-cut `S`, there are vertices outside `S` which distinguish the pair
in both directions.

#### Proof

Six-colour `G-x`.  If `N(x)subseteq N(y)`, the colour of `y` is absent
from `N(y)` and hence from `N(x)`.  Giving `x` that colour six-colours
`G`, a contradiction.  Interchange `x,y` for the other inclusion.  If
the boundary neighbourhoods agree, the two private neighbours supplied
by failure of the inclusions cannot lie in `S`.  \(\square\)

These are actual exterior portal witnesses, not abstract inequality
rows.  Turning them into four disjoint state-forcing columns remains a
linkage question; the lemma does not silently assert their disjointness.

## 6. Sharp coherent-rural survivor

Let `I` be the icosahedral graph, let `u,v` be two adjacent vertices
complete to `I`, and put

\[
                              G_0=I vee K_2.                     \tag{6.1}
\]

The graph is seven-connected and has Hadwiger number six: the icosahedron
is five-connected, planar, has a `K_4` minor and no `K_5` minor, while
joining a universal `K_2` raises connectivity and Hadwiger number by two.

Choose a vertex `0` of `I`.  Its five neighbours induce a cycle; label
them in cyclic order

\[
                           1,5,11,7,8.                          \tag{6.2}
\]

Then

\[
 S=N_I(0)\cup\{u,v\}                                           \tag{6.3}
\]

is a seven-cut.  The two components of `G_0-S` are `{0}` and the
remaining six icosahedral vertices, and both are full to `S`.  Moreover

\[
                         G_0[S]=K_2\vee C_5,
 \qquad \overline{G_0[S]}=C_5\mathbin{\dot\cup}2K_1.           \tag{6.4}
\]

Set

\[
 Q=\{u,v,1\},\qquad Z_D=\{5,7\},\qquad Z_E=\{8,11\}.           \tag{6.5}
\]

Then `Q` is a triangle and both displayed gate pairs are nonedges.  This
static survivor has five boundary defects and is literally cyclic.
Theorem 3.4 shows that it occurs at the first possible static two-shore
defect level.

The boundary equality states are also exact.  The universal adjacent
vertices `u,v` are distinct singleton blocks.  On the remaining `C_5`,
a six-colour boundary state uses either

* four colours: one nonedge pair and three singletons; or
* three colours: two disjoint nonedge pairs and one singleton.

There are five labelled states of each kind, ten in total, and only two
types up to the dihedral symmetry of the cycle.

Finally `G_0-{u,v}=I` is planar.  Hence this graph lies in the coherent
two-apex alternative, not in the clique-minor branch.  It is
six-colourable and is not a minor-critical counterexample.  The example
is therefore sharp in the intended sense: seven-connectivity, two full
shores, the triangle-plus-two-gates boundary, and `K_7`-minor exclusion
already permit the rural `C_5` state.  Any theorem excluding the residue
must use the private proper-minor transitions of Theorem 2.1 (and their
Kempe saturation), or prove that all cyclic rotations assemble around the
same apex pair.
