# First incompatible rotation: two rooted pages

## 1. The rotation calculation

Let `X={x_1,x_2,x_3,x_4}`.  A cycle containing `X` induces a cyclic
order on `X`, considered up to reversal.  There are three such orders.

### Lemma 1.1 (two-cycle rotation exchange)

Let `C_0,C_1` be cycles in a graph such that

* `V(C_0) cap V(C_1)=X`; and
* each cycle contains all four vertices of `X`.

If the cyclic orders induced by `C_0` and `C_1` are different, then
`C_0 union C_1` contains an `X`-rooted `K_4` minor.

#### Proof

For `epsilon in {0,1}`, shorten every `X`--`X` arc of `C_epsilon` to
one edge, without contracting either end.  This produces two Hamilton
cycles on the same labelled four-vertex set `X`.  The cyclic orders are
different, so the Hamilton cycles are different.  A Hamilton cycle in
`K_4` omits one perfect matching, and two different Hamilton cycles omit
different perfect matchings.  Their union is therefore all of `K_4`.
All contractions used only internal vertices of the cycle arcs, so the
four vertices of `X` remain in distinct branch sets.  QED.

The hypothesis is exact for the bare frame.  If the orders agree, the
union of the two cycles is planar and has `X` on a face.  Before
identifying the roots, the corresponding object is a subdivision of the
four-prism: two consistently ordered cycles joined by four matching
edges.

### Corollary 1.2 (literal columns preserve the labels)

Let `W_0,W_1` be disjoint graphs, with distinct roots

\[
             p^epsilon_1,p^epsilon_2,p^epsilon_3,p^epsilon_4
             \quad(epsilon=0,1).
\]

Let `Q_i` be four pairwise vertex-disjoint paths from `p^0_i` to
`p^1_i`, internally disjoint from `W_0 union W_1`.  Suppose `W_epsilon`
contains a cycle through its four roots.  If the two root orders are
different, the union contains a rooted `K_4` model whose `i`th bag
contains the whole column `Q_i`.

#### Proof

Contract each `Q_i` to a vertex `x_i` and apply Lemma 1.1.  Lift the
rooted model through the four contractions.  The inverse image of the
bag containing `x_i` is connected and contains `Q_i`; inverse images of
different bags are disjoint.  QED.

This is the precise first-incompatible-rotation theorem.  It uses actual
disjoint columns.  Four abstract portal incidences concentrated through
one gate cannot be substituted for them.

## 2. Two four-connected pages always close

The four-connected special case is stronger: even compatible rotations
close.  The useful reason is not rotation uniqueness but the existence
of two disjoint full pages behind the four roots.

### Lemma 2.1 (double-full-page rooted completion)

Let `H` be four-connected and let `X={x_1,x_2,x_3,x_4}`.  Suppose there
are disjoint connected sets `D_0,D_1 subseteq V(H)-X`, each adjacent to
every vertex of `X`.  Then `H` contains an `X`-rooted `K_4` minor.

#### Proof

Assume no such rooted minor exists.  The four-connected case of the
rooted-`K_4` theorem then gives a plane embedding of `H` in which the
four roots occur on one face.  Relabel them in their cyclic facial order
as `x_1,x_2,x_3,x_4`.

Because `D_0` is connected and full to `X`, it contains, together with
two incident edges, an `x_1`--`x_3` path whose internal vertices lie in
`D_0`.  Similarly `D_1` supplies an `x_2`--`x_4` path with interior in
`D_1`.  The paths are internally vertex-disjoint.  Two internally
disjoint paths joining alternating pairs of vertices on one facial
boundary cannot be drawn in the same disk; this is the elementary
Jordan-curve crossing obstruction.  This contradicts the plane
embedding.  QED.

The sets `D_0,D_1` need not be induced, and no cyclic order is prescribed
in the statement.

### Theorem 2.2 (four-column sum of two four-connected torsos)

In the setting of Corollary 1.2, assume that both `W_0` and `W_1` are
four-connected.  Then the union contains a rooted `K_4` model whose
`i`th bag contains `Q_i`, regardless of the two cyclic orders.

#### Proof

Contract the four columns and call the resulting graph `H`; write
`X={x_1,x_2,x_3,x_4}` for the contracted columns.  The two images
`H_0,H_1` are isomorphic to `W_0,W_1`, intersect exactly in `X`, and are
four-connected.

First, `H` is four-connected.  After deleting at most three vertices,
each `H_epsilon` remains connected and at least one vertex of `X`
remains; that vertex joins the two surviving connected subgraphs.

For each `epsilon`, choose a component `D_epsilon` of
`H_epsilon-X`.  It is nonempty, since a four-connected graph has at
least five vertices.  Its neighbourhood in `H_epsilon` is all of `X`.
Indeed, the neighbourhood is contained in `X`; if it had order at most
three, deleting it would separate `D_epsilon` from at least one root in
`X`, contradicting four-connectivity.  The two selected components are
disjoint.  Lemma 2.1 now gives an `X`-rooted `K_4` minor in `H`.

Lift this model through the column contractions as in Corollary 1.2.
Each lifted root bag contains its named column.  QED.

Thus a target-free carrier system joined by four genuine columns has at
most one four-connected rooted torso.  A surviving multi-torso system
must lose a column, pass through a one/two-vertex gate, or use a genuinely
three-connected web torso.  In particular, incompatible rotations are
not the remaining issue in the four-connected cell.

### Corollary 2.3 (partial-`2` quotient with literal cross edges)

Let an ambient carrier quotient be a partial `2`-tree, and replace two
of its vertices by disjoint four-connected rooted torsos.  The single
quotient adjacency between those two carrier vertices records only
nonempty contact.  Assume, more strongly, that its expansion contains
four pairwise independent literal label-preserving edges

\[
                         p^0_i p^1_i\quad(1\le i\le4),
\]

then the expanded graph contains a rooted `K_4` whose `i`th bag contains
`p^0_i p^1_i`.

#### Proof

Use the four literal edges as the paths `Q_i` in Theorem 2.2.  The other
quotient vertices and edges may be deleted before taking the minor.  In
particular, their partial-`2`-tree structure is not needed once the four
literal columns exist.  QED.

### Theorem 2.4 (the exact planar three-connected residue)

Let `W_0,W_1` be planar three-connected graphs with four roots on one
face, and join corresponding roots by four disjoint columns as in
Corollary 1.2.  Then at least one of the following holds.

1. The column union contains the column-rooted `K_4` model.
2. After contracting the columns, the union has a separation of order
   exactly three.
3. In one of the two torsos, no component left after deleting its four
   roots is adjacent to all four roots.

Moreover, if the two facial root orders are different, outcome 1 holds.

#### Proof

The boundary of a face in a three-connected plane graph is a cycle, so
different orders give outcome 1 by Corollary 1.2.

Assume the orders agree and contract the columns to `X`.  The resulting
union `H` is three-connected: after deleting at most two vertices, both
torso images remain connected and at least two common roots remain.  If
`H` is not four-connected, it therefore has a separation of order three,
which is outcome 2.

If `H` is four-connected and outcome 3 fails, choose one `X`-full
component in each torso.  They are disjoint, so Lemma 2.1 gives outcome
1.  QED.

Thus the first incompatible rotation is completely eliminated even at
three-connectivity.  A compatible target-free pair is forced into a
literal three-separator or a portal-deficient lobe; these are exactly
the objects on which the state-shore/two-gate and colour-gluing
mechanisms must operate.

## 3. Direct `K_7` lift

The preceding rooted model composes with the two-pool completion without
any unlabelled inference.

### Corollary 3.1 (biportal four-column completion)

In Theorem 2.2, suppose there are further disjoint sets `B,T,R,U`, also
disjoint from the torsos and the columns, such that

1. `B,R,U` are connected and `T` is nonempty;
2. `R` is adjacent to every vertex of `B union T`;
3. every column `Q_i` is adjacent to `B`, to `T`, and to `U`; and
4. `U` is adjacent to both `B` and `T`.

Then the ambient graph contains a `K_7` minor.

#### Proof

Let `F_1,...,F_4` be the lifted rooted bags from Theorem 2.2.  They are
pairwise adjacent, and `F_i` contains `Q_i`; hence the named column
edges make `F_i` adjacent to `B,T,U`.  The seven bags

\[
                  F_1,F_2,F_3,F_4,U,B,R union T
\]

are connected, disjoint and pairwise adjacent, exactly as in Theorem
1.1 of `hadwiger_biportal_rooted_k4_web_exchange.md`.  QED.

The same proof works when the three contacts occur on any protected
part of the lifted `i`th bag, not necessarily on the literal path
`Q_i`.  What is essential is that those contacts survive in the named
root bag.

## 4. Coherent disk gluing: the missing hypothesis

For two bare rooted cycles, agreement of the rotations is sufficient for
planar gluing.  It is not sufficient for arbitrary partial-2-tree
interfaces.

### Proposition 4.1 (treewidth two is not terminal rurality)

There is a partial `2`-tree with four named vertices which has no disk
embedding with all four named vertices on the boundary.

#### Proof

Take `K_{2,3}` with bipartition

\[
                         {u,v} mid {a,b,c}
\]

and name `u,a,b,c`.  The graph is series-parallel and hence a partial
`2`-tree.  In every plane embedding, each face is bounded by two of the
three length-two `u`--`v` paths.  Consequently a face contains at most
two of `a,b,c`, so no face contains all four named vertices
`u,a,b,c`.  QED.

Therefore the correct coherent alternative is not merely

\[
        \text{compatible torso rotations + partial-2-tree quotient}.
\]

It must additionally require a **terminal-rural embedding** of every
quotient piece (equivalently, a compatible choice of outer face through
the named adhesion terminals), or an SPQR statement which proves that
all intervening two-separations are nested relative to those terminals.
The `K_{2,3}` example is sharp at the level of minor width: it has no
`K_4` minor, so quotient minor-freeness alone cannot supply the missing
disk order.

### Theorem 4.2 (annular composition)

Let `A` be a graph with two disjoint ordered terminal sets

\[
 P_0=(p^0_1,p^0_2,p^0_3,p^0_4),\qquad
 P_1=(p^1_1,p^1_2,p^1_3,p^1_4).
\]

Assume `A` has an embedding in a closed annulus in which `P_0` and
`P_1` occur, in the prescribed compatible cyclic orders, on the two
different boundary components.  For `epsilon=0,1`, let `W_epsilon` have
a disk embedding with `P_epsilon` on the disk boundary in the same
order.  Suppose

\[
 A cap W_epsilon=P_epsilon,
 \qquad W_0 cap W_1=emptyset.
\]

Then `A union W_0 union W_1` is planar.  Consequently, if these are all
the vertices of a graph `G` except two fixed vertices `alpha,beta`, then
`G` is coherently `{alpha,beta}`-apex.

#### Proof

Glue the boundary circle of the disk containing `W_epsilon` to the
corresponding boundary circle of the annulus, matching the four named
points.  Compatibility of the cyclic orders is exactly what makes both
boundary identifications homeomorphisms.  The annulus capped by the two
disks is a sphere, and the three drawings have disjoint interiors and
agree only at their named boundary vertices.  Their union is therefore
a plane graph.  Deleting `alpha,beta` from `G` leaves precisely this
union.  QED.

For the four literal columns and no other interface edges, `A` is four
disjoint radial arcs, so the annular hypothesis holds exactly when the
two rotations agree.  For a general partial `2`-tree interface the
hypothesis is additional structure, not a consequence of treewidth, as
Proposition 4.1 shows.

## 5. Consequence for the uniform Gate B

The cross-Helly theorem in
`hadwiger_full_state_shore_bihelly.md` changes the scope of this rotation
problem.  If every carrier has a full typed shore pair, both shores keep
every intercarrier portal row.  Every two-by-two contact graph then has
a perfect matching, so the whole system enters the connected-shore
cocycle/matching theorem.  No torso rotation has to be considered in
that branch.

The rotation problem therefore belongs only to the other cross-Helly
outcome: one named gate/cycle/3-connected torso meets every carrier of
one state half, and each off-torso lobe has a named missing state or
intercarrier row.  The marks used below must be **state-forcing** marks
in the sense of Section 4 of that note; arbitrary vertices of the torso
do not retain all neutral portal rows.

The first-incompatible-rotation part is now closed whenever four actual
disjoint columns have been selected:

* different rotations give the rooted model directly by Lemma 1.1;
* if both endpoint torsos are four-connected, all rotations give the
  rooted model by Theorem 2.2;
* compatible rotations can support a coherent rural lift only after the
  quotient pieces are proved terminal-rural, not merely partial
  `2`-trees.

Hence the unresolved Gate B can be stated more narrowly.  It is the
**single-torso selection theorem** which must choose four state-forcing
marks and expand their virtual bridges to four disjoint columns, or else
use a named missing row to exhibit a shared one/two-vertex gate whose
exact extension relation is colour-gluable.  If two obstruction torsos
are reached by four such columns, different rotations close by Lemma
1.1, and two four-connected torsos close by Theorem 2.2 regardless of
rotation.  Once the columns enter two four-connected torsos, there is no
remaining rotation case.
