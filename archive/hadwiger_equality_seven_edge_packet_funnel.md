# The nonsplit seven-edge equality gate is a rooted packet obstruction

## 1. Scope

Let `G` be a seven-connected, proper-minor-minimal non-six-colourable,
`K_7`-minor-free graph.  Let `S` be a seven-cut with exactly two full
components `D_0,D_1`, and put

\[
                         J=G[S],\qquad Q=\overline J.             \tag{1.1}
\]

Assume

\[
                              |E(Q)|=7.                           \tag{1.2}
\]

The exact-block theorem makes `Q` nonsplit.  Contracting the two shores
to nonadjacent full helpers gives a minor (proper unless both shores are
already singleton vertices), so the nine-vertex quotient
`J vee overline(K_2)` has no `K_7` minor.

The preceding repeated-root theorem proves that at least three boundary
labels have degree at most four in `J`, and two of them repeat in one
shore.  This note combines that fact with every cyclic-hull crossing.  It
does not close the entire seven-edge layer, but reduces it to one uniform
rooted matching-packet obstruction.

## 2. The compatibility graph

Put

\[
                    L(Q)=\{s\in S:d_Q(s)\ge2\}.                  \tag{2.1}
\]

For distinct `a,b in L(Q)`, call `ab` **split-positive** when the
following finite condition holds.  For every pair of rows

\[
 P_X\cup P_Y=S,qquad \{a,b\}\subseteq P_X\cap P_Y,             \tag{2.2}
\]

the graph obtained from `J` by adjoining

* adjacent vertices `x,y` with boundary rows `P_X,P_Y`; and
* a vertex `h` complete to `S`

contains a `K_7` minor.  Let `A(Q)` be the graph on `L(Q)` whose edges
are the split-positive pairs.

This definition is label-free.  It records exactly which two repeated
portal classes make *every* connected covering split liftable.

### Theorem 2.1 (nonbipartite compatibility closes or descends)

If `A(Q)` is nonbipartite, then `G` contains a `K_7` minor or the
repeated-root splitter exposes a nested exact seven-cut.

#### Proof

For every `s in L(Q)`, minimum degree and fullness give

\[
          |N_{D_0}(s)|+|N_{D_1}(s)|
             \ge 7-d_J(s)=1+d_Q(s)\ge3.            \tag{2.3}
\]

Assign `s` one of the shores in which it has at least two neighbours.
If `A(Q)` is nonbipartite, this two-colouring has a monochromatic edge
`ab`, say in `D_0`.

Apply the double-root splitter to the two portal classes in `D_0`.  Its
first outcome is a connected covering split satisfying (2.2); its
quotient is `K_7`-positive by the definition of `A(Q)` and lifts to `G`.
In its cutvertex outcome, Theorem 3.1 of
`hadwiger_equality_repeated_root_split.md` gives either a nested exact
seven-cut or a full/full connected split.  The latter is another instance
of (2.2) and is likewise positive.  These are all outcomes. \(\square\)

Thus a survivor carries an actual proper two-colouring of `A(Q)` by
portal-multiplicity shores.  This turns a portal count into a finite
compatibility obstruction rather than an arbitrary choice of repeated
roots.

## 3. Cyclic packets

A **packet demand** is an unordered pair

\[
                      \{e,f\},                                  \tag{3.1}
\]

where `e,f` are vertex-disjoint pairs of boundary labels which occur as
the two alternating pairs of some cyclic hull of `J`.  Let `P(Q)` be the
graph whose vertices are the boundary pairs occurring this way and whose
edges are the packet demands.

### Lemma 3.1 (every packet edge has a shore owner)

For every edge `{e,f}` of `P(Q)`, one of `D_0,D_1` contains two
vertex-disjoint connected carriers for `e,f`.

#### Proof

Choose the cyclic hull witnessing `{e,f}`.  If both shore societies were
crossless for its alternating terminal tuple, the two-shore web-gluing
theorem would four-colour the planar part and use two fresh colours on
the bipartite omitted boundary, six-colouring `G`.  Therefore one shore
is crossed.  Deleting the artificial terminals gives the two required
carriers. \(\square\)

The owner need not be unique, and packet edges need not have coherent
owners.  This is important: assigning all packet edges independently to
the two shores is an overapproximation, not a theorem that their path
systems are simultaneously realizable.

### Definition 3.2 (matching-packet triangle)

Let `e_1,e_2,e_3` be three pairwise vertex-disjoint missing boundary
edges.  They form a matching-packet triangle when all three pairs

\[
       \{e_1,e_2\},\qquad\{e_1,e_3\},\qquad\{e_2,e_3\}           \tag{3.2}
\]

are edges of `P(Q)`.

Suppose one shore contains a simultaneous `e_1,e_2,e_3` linkage.  Join
the three disjoint path carriers by a minimal connector in that shore and
absorb the connector so that their adjacency graph is a tree.  There are
only three possible centres.  Contracting the carriers and the opposite
full shore gives an eleven-vertex quotient.

Call the triangle **fully positive** if that quotient contains `K_7` for
all three possible centres.  Call it **centre-locked** if exactly one
centre is negative.

### Lemma 3.3 (fully positive triangles are pairwise-but-not-triple)

In a `K_7`-minor-free gate, neither shore contains a simultaneous
three-linkage for a fully positive packet triangle.  Nevertheless every
one of its three two-linkages occurs in at least one shore.

#### Proof

The two-linkages are Lemma 3.1.  A simultaneous three-linkage gives one
of the three connector trees described above, and full positivity lifts
the certified `K_7` model. \(\square\)

This is the same label-free rooted-prism obstruction that emerged in the
closed `C_6` laboratory: all pair packets are available across two
shores, while every integral triple realization is forbidden.

For a centre-locked triangle, the same proof forces the unique negative
carrier to be the centre of every simultaneous realization.  Thus its
failure is an **oriented centre lock**, not an arbitrary three-linkage
failure.

## 4. Complete finite funnel at seven missing edges

The exact verifier `equality_gate_seven_edge_packet_atlas.py` proves the
following finite assertion.  Every minor certificate is replayed as seven
disjoint connected pairwise adjacent bags.

### Theorem 4.1 (31 types reduce to ten packet cores)

Modulo the nested exact-seven-cut outcome of Theorem 2.1, the following
finite reduction holds.

There are exactly 31 unlabelled graphs `Q` satisfying all of:

1. `|V(Q)|=|E(Q)|=7`;
2. `Q` is nonsplit; and
3. `overline(Q) vee overline(K_2)` has no `K_7` minor.

Among them:

1. 18 have a cyclic hull for which every covering crossing quotient is
   `K_7`-positive.  The full-split web theorem closes them.
2. `A(Q)` is nonbipartite for five types.  Two overlap the preceding 18,
   so Theorem 2.1 closes or sends three additional types to a nested
   exact seven-cut.
3. Exactly ten types survive both mechanisms.

Their graph6 codes and missing edges are:

\[
\begin{array}{c|l}
\text{code}&E(Q)\\ \hline
\texttt{FwJG?}&01,02,05,12,15,24,45\\
\texttt{F[JG?}&02,03,05,12,15,24,45\\
\texttt{FhoW?}&01,04,12,14,23,35,45\\
\texttt{FHHGg}&12,15,23,24,36,45,56\\
\texttt{FHOgg}&12,14,23,25,36,45,56\\
\texttt{FIS`G}&12,13,14,25,26,34,56\\
\texttt{Fpq?G}&01,02,04,05,14,23,56\\
\texttt{Fh\_gG}&01,04,12,23,25,45,56\\
\texttt{FhCKG}&01,06,12,23,34,45,56\\
\texttt{F`o\_g}&01,04,14,23,25,36,56.
\end{array}                                                       \tag{4.1}
\]

Seven of these ten have a fully positive matching-packet triangle.  One
certificate matching for each is:

\[
\begin{array}{c|c}
\texttt{F[JG?}&03\mid12\mid45\\
\texttt{FhoW?}&01\mid23\mid45\\
\texttt{FHHGg}&12\mid36\mid45\\
\texttt{FHOgg}&12\mid36\mid45\\
\texttt{FIS`G}&12\mid34\mid56\\
\texttt{Fpq?G}&01\mid23\mid56\\
\texttt{FhCKG}&01\mid23\mid45.
\end{array}                                                       \tag{4.2}
\]

Two further types have centre-locked triangles:

\[
\begin{array}{c|c|c}
\text{code}&\text{matching}&\text{only permitted centre}\\ \hline
\texttt{Fh\_gG}&01\mid23\mid45&45\\
\texttt{F`o\_g}&01\mid23\mid56&01.
\end{array}                                                       \tag{4.3}
\]

The final type `FwJG?` has matching number two.  Its nontrivial component
is a triangulated theta: a `K_4-e` on `0,1,2,5`, with the missing `25`
edge replaced by `2-4-5`, plus two isolated vertices.  Its packet graph
has seven vertices, eight edges, degree sequence

\[
                         3,3,2,2,2,2,2,                           \tag{4.4}
\]

and cycle rank two.  Thus it is itself a theta packet core rather than a
matching-packet triangle.

#### Certification details

The verifier independently:

* regenerates the 31 types from the NetworkX order-seven atlas;
* checks all `3^5` covering rows for every candidate repeated pair;
* verifies the 18 full-split cyclic-hull witnesses;
* computes `A(Q)` and checks the exact nonbipartite set;
* verifies all three connector-tree centres for (4.2)--(4.3); and
* prints explicit branch bags for every positive connector tree.

No conclusion is inferred from a positive edge count alone.

## 5. The reusable remaining invariant

Modulo nested exact seven-cut descent, the entire nonsplit seven-edge
layer has therefore reached one of two label-free objects:

1. a state-decorated rooted matching triangle which is
   pairwise-linkable but not triple-linkable (with two oriented centre
   exceptions); or
2. the rank-two theta packet core.

Every owned packet extends to a connected covering bad split.  Every
boundary-faithful proper-minor operation strictly inside one open shore
produces a strict boundary transition state; for interface-edge deletions,
`hadwiger_bad_split_interface_exchange.md` additionally supplies the
ear-or-two-anchor geometry.  Hence the missing theorem is not another
boundary atlas.  It is the following uniform exchange:

> **State-decorated packet exchange.**  In two full shores behind a
> minimum `k`-cut, a finite packet graph is edge-covered by rooted
> two-linkages.  If every target-positive matching triangle fails to
> lift integrally, then the resulting pairwise-but-not-triple linkage
> obstruction either has a bounded-adhesion rope/ladder decomposition,
> or two operated packet splits accept a common boundary state.

The first outcome is suited to exact-cut descent; the second colour-glues
the two shores.  Proving this statement for a packet triangle and the
theta core would close the entire seven-missing-edge equality layer at
once.  Its formulation does not mention any of the ten graph labels and
is the first uniform rooted-model principle exposed by the full layer,
rather than by one selected boundary case.
