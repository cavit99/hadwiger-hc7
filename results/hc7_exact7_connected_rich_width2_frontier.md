# Connected-rich width-two frontier

**Status:** Sections 1--6 are proved and independently audited.  Section 7
isolates the remaining literal carrier theorem; it is not claimed.

This note replaces the four labelled maximal failures seen by the first
small-core probe with one label-free obstruction theorem.  Two of those
four graphs already contain the relevant deeper near model; the shallow
core test simply did not find it.

## 1. Covering a connected rich shore by two packets

Let `R` be connected and let `P_0,Q_0` be disjoint connected subgraphs of
`R`.

### Lemma 1.1 (adjacent connected cover)

There is a partition

\[
                         V(R)=P\mathbin{\dot\cup}Q
\]

such that `R[P]` and `R[Q]` are connected, `P_0 subseteq P`,
`Q_0 subseteq Q`, and there is a `P-Q` edge.  In particular, if `P_0,Q_0`
are `S`-full, then so are `P,Q`.

#### Proof

Contract `P_0` and `Q_0` to two distinct roots and take a spanning tree of
the resulting connected graph.  Delete any edge on the unique path between
the roots.  The two components of the deleted tree edge give the desired
partition after the two contractions are expanded.  The deleted edge is
the required cross-edge.  \(\square\)

Thus a connected rich shore containing two disjoint full packets gives a
literal three-packet quotient: the thin full packet `L`, and adjacent full
packets `P,Q` covering the rich shore.

## 2. Exact static near-model characterization

Write `K_4^vee` for `K_4` with two incident edges deleted.  Equivalently,
it is a triangle with a pendant vertex.  Let `H` be an arbitrary graph on
a literal seven-set `S`.  Form `J(H)` by adding three vertices `l,p,q`,
each complete to `S`, with `pq` as the sole edge among them.

### Theorem 2.1 (three-packet `K_7^vee` criterion)

\[
 J(H)\succeq K_7^\vee
 \quad\Longleftrightarrow\quad
 \left(
 H\succeq K_4
 \quad\hbox{or}\quad
 (\exists x\in S)\ H-x\succeq K_4^\vee
 \right).                                               \tag{2.1}
\]

#### Proof

If `H` has a `K_4` model, use its four bags together with the three
singleton packet bags `l,p,q`.  The only missing bag adjacencies are
`lp,lq`, so these seven bags form a `K_7^vee` model.

If `H-x` has a `K_4^vee` model, use its four bags together with

\[
                           \{l,x\},\quad\{p\},\quad\{q\}.
\]

The three packet bags form a clique: `x` supplies both edges incident with
the first bag and `pq` supplies the third.  Packet fullness supplies every
cross-adjacency.  The only two possible missing edges are the two incident
missing edges of the boundary `K_4^vee` model.

Conversely, let `M` be a `K_7^vee` model in `J(H)`, and let `r` be the
number of its bags that contain at least one of `l,p,q`.  The other `7-r`
bags lie wholly in `S`.

If `r<=2`, there are at least five boundary-only bags.  Select four and
choose a literal `x` from a fifth.  The four selected bags inherit at most
two mutually incident missing adjacencies from `M`, and hence form a
`K_4^vee` model in `H-x`.

Suppose `r=3`.  There are exactly four boundary-only bags.  If a packet bag
contains a literal `x in S`, those four bags again give a `K_4^vee` model
in `H-x`.  Otherwise the three packet bags are precisely the singleton
bags `l,p,q`.  Their two nonedges `lp,lq` already exhaust the permitted
two-edge star of nonadjacencies.  The four boundary-only bags are therefore
pairwise adjacent and form a `K_4` model in `H`.  This proves (2.1).
\(\square\)

This is the near-model analogue of the audited static `K_7` quotient
characterization.  It is exact and does not assume that boundary bags are
singletons or have bounded order.

## 3. The elementary `K_4^vee` obstruction

### Lemma 3.1

A graph is `K_4^vee`-minor-free if and only if each of its connected
components is a tree or a cycle.

#### Proof

Trees and cycles plainly have no triangle-with-a-pendant minor.  Conversely,
let `F` be a connected graph that is neither a tree nor a cycle, and choose
a cycle `C`.

If a vertex lies outside `C`, take a shortest path from `C` to such a
vertex.  Contract `C` to a triangle while retaining the path attachment,
and contract the nontrivial part of the path to one pendant edge.  This is
a `K_4^vee` minor.

If `C` spans `F`, then `F` has a chord `uv`.  The chord and one `u-v` arc
of `C` contract to a triangle.  Delete the last edge of the other arc at
`v` and contract what remains of that arc to a pendant edge at `u`.
Again one obtains `K_4^vee`.  \(\square\)

## 4. Paired boundaries collapse to two width-two forms

Let

\[
 S=\{c,a_1,t_1,a_2,t_2,a_3,t_3\},\qquad
 B_i=\{a_i,t_i\}.
\]

Assume the paired-state boundary conditions:

1. every `B_i` is independent;
2. `c` has a neighbour in every `B_i`; and
3. every two distinct `B_i,B_j` have a literal edge between them.

These conditions already give six distinct boundary edges.

### Lemma 4.1 (cycle length)

Let `F` be a connected seven-vertex graph such that `F-x` is
`K_4^vee`-minor-free for every `x`.  Every cycle of `F` has length at least
six, and `F` has at most one cycle.

#### Proof

Let `C` be a cycle.  If at least two vertices lie outside `C`, take a
component `D` of `F-C` that attaches to `C`.

If `D` has at least two vertices, retain a vertex of `D` adjacent to `C`
and delete a different vertex of `D`.  The resulting graph still has a
component containing `C` and a vertex outside `C`, contrary to Lemma 3.1.
If every such component is a singleton, delete one outside singleton and
retain another.  The same contradiction results.  Hence at most one
vertex lies outside `C`, and `|C|>=6`.

Suppose that a second cycle exists.  Relative to `C`, it contains a
`C`-path `P` that is not an edge of `C`: the ends of `P` lie on `C` and
its internal vertices and edges lie outside `C`.  (A chord is allowed and
has no internal vertex.)  Since `|C|>=6`, the graph has at most one vertex
outside `C`, and hence `P` has length at most two.  If the two arcs of `C`
between the ends of `P` have lengths `r,s`, then

\[
                         r+s=|C|\le7.
\]

The two cycles formed by `P` and those arcs must also have length at least
six.  Thus `r+|P|>=6` and `s+|P|>=6`, which gives
`r+s+2|P|>=12`.  But the left side is at most `7+4=11`, a contradiction.
Thus the cycle is unique.  \(\square\)

### Theorem 4.2 (uniform static frontier)

Under the paired-state boundary conditions, if `J(H)` has no
`K_7^vee` minor, exactly one of the following structural alternatives
holds:

1. `H` is a connected tree;
2. `H` is a six-cycle with its seventh vertex pendant; or
3. `H` is the disjoint union `K_{1,3} dotcup K_3`.

In particular,

\[
 |E(H)|\le7,qquad \operatorname{tw}(H)\le2,             \tag{4.1}
\]

and there is a clique `U` of order at most one such that `H-U` is
bipartite.  In the connected case `U` may be chosen empty.

#### Proof

Theorem 2.1 says that `H` has no `K_4` minor and that every `H-x` is
`K_4^vee`-minor-free.

First suppose `H` is connected.  Lemma 4.1 says that it is a tree, a
seven-cycle, or a six-cycle with one pendant vertex.  A seven-cycle is
impossible because `c` has three neighbours belonging to the three
distinct pairs, whereas every cycle vertex has degree two.  This gives
alternatives 1 and 2, both bipartite.

Now suppose `H` is disconnected.  No component can contain a `K_4^vee`
minor: deleting a vertex in another component would leave that minor.
By Lemma 3.1 every component is a tree or a cycle.  The component containing
`c` contains `c` and at least one vertex from each `B_i`, so it has at
least four vertices.  It cannot be a cycle because `c` has degree at least
three, and hence it is a tree.  At most three vertices remain, so the only
possible odd-cycle component is a triangle.

The six required paired-state edges give `|E(H)|>=6`.  A disjoint union of
trees and cycles with the `c`-component a tree has at most six edges here.
Consequently equality holds: there are exactly two components, the
`c`-component is the four-vertex tree `K_{1,3}`, and the other component is
`K_3`.  This is alternative 3.  Deleting any one vertex of that triangle
makes the graph bipartite.

All three alternatives have the asserted edge and treewidth bounds.
\(\square\)

Thus the four labelled maximal failures from the shallow core probe were
not the correct invariant.  The exact quotient theorem leaves only a
bipartite width-two boundary or the single `K_3 dotcup K_{1,3}` odd-cycle
cell; both have a clique odd-cycle transversal of order at most one.

## 5. Literal consequences in a hypothetical counterexample

Return to an actual exact-seven `(1,2)` adhesion in a hypothetical minimal
`HC_7` counterexample.  Let `L` be the thin connected `S`-full packet and
let `P,Q` be the adjacent connected `S`-full cover of the connected rich
shore supplied by Lemma 1.1.  Put `H=G[S]`.

### Corollary 5.1 (surplus portal bound)

If the three-packet quotient does not already contain `K_7^vee`, then

\[
 \sum_{s\in S}\bigl(|N_L(s)|+|N_P(s)|+|N_Q(s)|-3\bigr)\ge14. \tag{5.1}
\]

In particular, one of `L,P,Q` has at least twelve literal boundary-contact
edges, and some boundary literal has at least two distinct neighbours in
one packet.

#### Proof

Minimum degree in the counterexample is at least seven.  Theorem 4.2 gives
`|E(H)|<=7`, so

\[
 \sum_{s\in S}d_{G-S}(s)
 =\sum_{s\in S}(d_G(s)-d_H(s))
 \ge49-2|E(H)|\ge35.
\]

Fullness of the three packets accounts for the baseline `21` contacts,
giving (5.1).  One packet therefore has at least
`ceil(35/3)=12` contacts.  The final assertion follows already from the
fourteen surplus incidences.  \(\square\)

The conclusion uses all portal surplus, rather than the false rule that a
single duplicated portal automatically gives a near model.

### Lemma 5.2 (the exact low-state carrier split that closes)

Let `U` be the clique of order at most one from Theorem 4.2 and let
`A,B` be the two independent sides of `H-U`.  Suppose the thin shore
contains disjoint adjacent connected sets `X,Y` such that

\[
 A\subseteq N_S(X),\qquad B\subseteq N_S(Y),            \tag{5.2}
\]

and, for the possible vertex `u in U`, both `X union A` and `Y union B`
are adjacent to `u`.  Then `G` is six-colourable.

#### Proof

Inside the thin shore contract `X union A` and `Y union B`.  The two
representatives are adjacent, and together with the possible singleton
`u` they form a clique.  A six-colouring of this proper minor therefore
restricts to the untouched rich closed shore with exact boundary state

\[
                              A\mid B\mid U.            \tag{5.3}
\]

Inside the rich shore contract `P union A` and `Q union B`.  Fullness and
the `P-Q` edge make these representatives, together with `U`, a clique.
A six-colouring of this proper minor restricts to the untouched thin
closed shore with the same exact state (5.3).  Align the at most three
block colours and glue the two colourings over `S`.  \(\square\)

If `L` were a singleton, it would be a degree-seven vertex with
`N_G(L)=S`.  Dirac's neighbourhood inequality would give
`alpha(H)<=2`, whereas each graph in Theorem 4.2 has an independent set of
order at least three.  Hence the static frontier also proves that the thin
packet is nonsingleton.

## 6. Cutvertices give the first state-aware gate descent

Continue with the low state `A|B|U` of Section 5.  In the connected case
take `U` empty.  In the disconnected `K_{1,3} dotcup K_3` case, take `U`
to be any triangle vertex.  The other two triangle vertices lie on
opposite sides of the bipartition of `H-U`; consequently both `A` and `B`
contain a neighbour of `U`.

For a connected carrier `T subseteq L`, say that `T` **funds** `A` when
`A subseteq N_S(T)` and `T union A` is adjacent to the possible retained
singleton `U`; define funding of `B` symmetrically.  Thus a full carrier
funds both duties.  A carrier missing one literal of `A` funds `B`, one
missing one literal of `B` funds `A`, and a carrier missing only `U` funds
both duties (the boundary edge from each side to `U` repairs the retained
adjacency).

### Theorem 6.1 (thin cutvertex split-or-exact-gate)

Suppose `z` is a cutvertex of the thin packet `G[L]`.  Then either Lemma
5.2 applies, or `L-z` has exactly two components `D_1,D_2` and there are
distinct literals `d_1,d_2` lying in the same one of `A,B` such that

\[
 N_S(D_i)=S-\{d_i\}\quad(i=1,2),\qquad
 zd_1,zd_2\notin E(G).                                 \tag{6.1}
\]

In the latter outcome

\[
                         S_i=(S-\{d_i\})\cup\{z\}       \tag{6.2}
\]

is the literal neighbourhood of `D_i`, and hence is a strictly descending
actual seven-adhesion.

#### Proof

Let `D_1,...,D_k` be the components of `L-z`.  Each has a neighbour at
`z`.  Moreover

\[
                         N_G(D_i)\subseteq S\cup\{z\}.
\]

The nonempty rich shore lies on the other side, so seven-connectivity gives
`|N_S(D_i)|>=6`.  Every lobe therefore has empty or singleton defect
`Delta_i=S-N_S(D_i)`.

Suppose first that `k>=3`.  Choose one lobe `Y=D_j` and put

\[
                  X=\{z\}\cup\bigcup_{i\ne j}D_i.
\]

The carriers `X,Y` are disjoint, connected and adjacent.  If every lobe
has empty defect, choose any `j`; both carriers are full and Lemma 5.2
applies.  If the defects are not all empty and not all the same singleton,
choose `j` so that the union defining `X` contains two lobes with different
defects (an empty defect counts as different).  Then `X` is full.  The
near-full carrier `Y` funds at least one of `A,B`, so assign the other duty
to `X` and apply Lemma 5.2.  If every lobe has the same defect `{d}`,
fullness of `L` forces `zd` to be an edge; hence `X` is again full and the
same conclusion holds.
Thus a survivor has `k=2`.

Write the two defects as `Delta_1,Delta_2`.  If either is empty, its lobe
funds both duties and the other lobe funds at least one, so the two duties
have distinct carriers.  The same is true if one defect is `{u}` with
`u in U`, or if the two defects lie in different sides `A,B`.  Lemma 5.2
closes all these cases using the genuinely adjacent carriers
`D_1 union {z},D_2` (or, after interchanging the indices,
`D_1,D_2 union {z}`).  Adding `z` preserves every duty funded by the raw
lobe, and the component property supplies the edge from `z` to the other
lobe.

The only possible failure therefore has

\[
                  \Delta_1=\{d_1\},\quad
                  \Delta_2=\{d_2\},
\]

with both literals in the same bipartition side.  If `d_1=d_2`, fullness
of `L` forces `zd_1` to be an edge.  Then `D_1 union {z}` is full and is
adjacent to `D_2`, so the split closes.  If the defects are distinct and
`z` sees `d_i`, put `z` with `D_i`; that carrier becomes full and the
other funds the opposite duty.  Hence a survivor has distinct defects and
`z` sees neither, proving (6.1).

Finally, each `D_i` is adjacent to `z`, contacts exactly `S-{d_i}`, and
has no other neighbour outside itself.  Thus `N_G(D_i)=S_i`.  The rich
shore is nonempty and lies outside `D_i union S_i`, so (6.2) is an actual
seven-separator.  Since `D_i` is a proper subset of `L`, it is a strict
shore-order descent.  \(\square\)

This theorem closes every multi-lobe thin articulation at once.  The sole
cutvertex residue is a two-lobe same-duty lock, and it already comes with
two named smaller exact-seven adhesions.  What it does **not** yet prove is
that the low equality state pulls back through either replacement
`d_i -> z`.

The paired width-two frontier in fact closes that last lock without a
state pullback.

### Lemma 6.2 (a same-side pair does not cover the frontier)

Let `U,A,B` be chosen as in Section 6.  If distinct `d_1,d_2` lie in the
same one of `A,B`, then

\[
                         E(H-\{d_1,d_2\})\ne\varnothing.       \tag{6.3}
\]

#### Proof

First suppose `H` is connected, so `U` is empty and `A,B` are its
bipartition sides.  Put `c in A` after interchanging the sides.  The three
paired-state contacts from `c` give three distinct neighbours in `B`, so
`|B|>=3`.

Also `|A|>=3`.  Otherwise at most one member `x` of the six-set
`B_1 union B_2 union B_3` lies in `A`; two of the three paired blocks then
lie wholly in `B`.  No edge can join those two blocks in a bipartite graph,
contrary to the paired-state boundary condition.  Thus both bipartition
sides have order at least three.  After deleting two vertices from one
side, a vertex of that side remains.  Connectedness gives it a neighbour
in the untouched opposite side, proving (6.3).

Now suppose `H=K_{1,3} dotcup K_3`.  The retained singleton `U={u}` lies
in the triangle, and the two other triangle vertices lie on opposite sides
of the bipartition of `H-u`.  A same-side pair therefore deletes at most
one of them.  The edge from `u` to the other remains in
`H-{d_1,d_2}`, again proving (6.3). \(\square\)

### Theorem 6.3 (the two-lobe lock has a literal near model)

In the residual outcome (6.1) of Theorem 6.1, `G` contains a labelled
`K_7^vee` minor.

#### Proof

By Lemma 6.2 choose an edge `xy` of `H-{d_1,d_2}` and choose any third
literal

\[
                    t in S-\{d_1,d_2,x,y\}.
\]

Use the seven branch sets

\[
 D_1\cup\{z,d_2\},\quad D_2\cup\{d_1\},\quad
 P,\quad Q,\quad \{x\},\quad\{y\},\quad\{t\}.          \tag{6.4}
\]

They are pairwise disjoint.  The first is connected through the literal
edges `D_1-z` and `D_1-d_2`; the second is connected through
`D_2-d_1`.  The first two bags are adjacent through `z-D_2`.  Together
with the adjacent full packets `P,Q` they form a clique: fullness at
`d_1,d_2` supplies every packet incidence.

All four carrier bags meet each of `x,y,t`.  For `P,Q` this is fullness;
for `D_i` it follows from
`N_S(D_i)=S-{d_i}` and the choice of the three literals outside both
defects.  Finally `xy` is a literal edge.  Hence only the other two pairs
among `{x},{y},{t}` may be absent, and they share `{t}`.  The seven bags
in (6.4) therefore form a labelled `K_7^vee` model. \(\square\)

### Corollary 6.4 (all thin cutvertices leave `S3`)

If the thin packet has a cutvertex, then either the low state reflects by
Lemma 5.2 and `G` is six-colourable, or Theorem 6.3 supplies a labelled
`K_7^vee` handoff to `S1`.  No cutvertex state-pullback residue remains.

## 7. Exact remaining mechanism

The next theorem should not mention the four labelled probe orbits.  The
uniform obligation is:

> **Width-two low-state portal pullback.**  In the setup of Section 5,
> either the thin packet has the duty-faithful `A-B` split of Lemma 5.2,
> or a block-terminal web/gate decomposition produces a strictly smaller
> actual adhesion on which the same two named duties pull back, or the
> portal system gives a spanning labelled `K_7^vee` model.

Theorems 6.1 and 6.3 close every cutvertex geometry.  Thus only a
cutvertex-free thin packet remains on the local side of this frontier.  The
fourteen surplus contacts in (5.1) are the quantitative input to its
block-terminal web theorem.  A single duplicated portal is not enough; the
required theorem must use their distribution or turn concentration into a
canonical gate.  This is now a two-duty, width-two state-transfer theorem,
rather than a four-orbit boundary case analysis.
