# Three-anchor capacity--web composition

## Status

This note proves the global composition step for a certified
three-anchor interface.  It uses three audited ingredients:

1. the exact arc trichotomy (two-point transversal, three disjoint
   spans, or a minimal cyclic cover);
2. the guarded cyclic-shore web exchange; and
3. the opposite six-partition carrier splice.

The new three-apex lifting theorem makes a planar remainder after deleting
**three** actual vertices terminal.  Consequently the cyclic and
two-transversal branches now have the same endgame.

The theorem below is deliberately stated in terms of actual vertices,
actual open shores, and actual equality blocks.  It does not identify a
palette colour with a model-bag label.  Its remaining applicability edge
is local: extracting the certified spans from a raw nonsingleton
`K_3 join C_4` carrier.

## 1. Three guards force a cross

### Lemma 1 (three-guard cross forcing)

Let `G` be seven-connected, `chi(G)>=7`, and `K_7`-minor-free.  Suppose

\[
 V(G)=A\mathbin{\dot\cup}R\mathbin{\dot\cup}D_1
                         \mathbin{\dot\cup}D_2,           \tag{1.1}
\]

where

* `|A|<=3`;
* `G[R]` contains a spanning cycle `C`;
* `D_1,D_2` are nonempty, connected, and anticomplete; and
* every vertex of `R` has a neighbour in each `D_j`.

Form the two ordered artificial-terminal societies on `C` exactly as in
the guarded cyclic-shore theorem.  Then at least one society is crossed.

#### Proof

If neither society is crossed, the guarded cyclic-shore theorem gives a
plane drawing of `G-A`.  Hence `chi(G-A)<=4`.  The uniform clique-apex
lifting theorem with `(r,s)=(4,3)` then gives a `K_7` minor in `G`, a
contradiction.  \(\square\)

This removes the former extra hypothesis that `G[A]` be bipartite when
`|A|=3`.

### Lemma 1.4 (one-defect six-frame repair)

Let

\[
                 V(G)=S\mathbin{\dot\cup}D_1
                          \mathbin{\dot\cup}D_2,          \tag{1.2}
\]

where the open shores are nonempty and anticomplete.  Let

\[
                             \Pi=(P_1,\ldots,P_6)         \tag{1.3}
\]

be a partition of `S` into nonempty independent blocks.  Assume its
block-adjacency quotient is `K_6` with at most the one edge `P_2P_3`
missing.

For each `j in {1,2}`, suppose there are pairwise disjoint connected
sets `X_i^j subseteq D_j` for every nonsingleton `P_i`, with
`X_i^j union P_i` connected.  Retain a singleton `P_i` itself when no
carrier is needed.  Write

\[
 B_i^j=X_i^j\cup P_i
 \quad\hbox{when a carrier is used},\qquad
 B_i^j=P_i\quad\hbox{otherwise}.                         \tag{1.4}
\]

If `P_2P_3` is absent from the quotient, suppose in addition that the
span geometry on shore `j` supplies one connected **defect packet**
`Y^j subseteq D_j`, disjoint from all selected block carriers, such that

\[
                         Y^j\sim B_2^j,B_3^j.             \tag{1.5}
\]

Then the two shores realize the same six-block equality partition `Pi`,
and the opposite partition-carrier splice six-colours `G`.

If instead only one shore, say `D_1`, has these carriers and defect
packet, while `D_2` is connected and full to `S`, then `G` has a literal
`K_7` minor.

#### Proof

If `P_2P_3` is absent, absorb `Y^j` into `B_2^j` on shore `j`.  This
preserves connectedness, disjointness and every old block adjacency, and
(1.5) repairs the absent quotient edge to `B_3^j`.  If `P_2P_3` is
present, make no absorption.  In either case the six resulting bags are
connected, disjoint and pairwise adjacent.  They therefore satisfy the
audited six-partition carrier theorem for the exact partition `Pi`.
Doing this on both shores and applying the opposite-carrier splice gives
a six-colouring of `G`.

For the final assertion, the six repaired bags on `D_1 union S` form a
`K_6` model.  The connected full shore `D_2` is disjoint from them and
adjacent to each, because every bag contains a nonempty boundary block.
It is the seventh branch bag of a literal `K_7` model. \(\square\)

In the lobe-median `K_3 join C_4` carrier there are exactly two natural
orientations of (1.3): merge one absent rim diagonal into one equality
block.  The block quotient then misses precisely the **other** rim
diagonal.  Thus (1.5), rather than a complete boundary quotient, is the
exact adjacency which a separated span must supply.

At an exact seven-cut with two full shores, the previously audited
independent-pair plus clique-complement closure is the special case in
which the complete quotient itself is already terminal.  No new state
mechanism is claimed for that subcase.

## 2. Unconditional extraction inside a lex-minimal common row

The composition theorem needs actual spans rather than row names.  The
following normalization extracts them from every common row of the
`K_3 join C_4` carrier.  Unlike (C1)--(C2), it is unconditional.

Let `R` be one of the three common row bags and let `Q_1,...,Q_6` be its
six neighbouring model bags.  In the permitted labelled comparison
class, first minimize the number of absent bag pairs and then minimize
`|R|`.  Models need not be spanning.  A vertex `x in R` **owns** duty
`i` when every actual `R-Q_i` edge has its `R`-end at `x`.

### Theorem 1.6 (noncut-root normalization)

Exactly one of the following holds.

1. `R` is a singleton, and that actual vertex meets all six neighbouring
   bags.
2. `G[R]` is an induced path.  Each endpoint owns at least two duties,
   the two owner sets are disjoint, and at most two duties have a portal
   anywhere other than their unique owning endpoint.
3. `G[R]` has exactly three noncutvertices `z_1,z_2,z_3`.  They own a
   partition of the six duties into three pairs, and for every duty all
   of its actual `R-Q_i` edges have their `R`-end at the corresponding
   `z_h`.  Every block of `G[R]` is an edge or a triangle; there is at
   most one triangle block.  If there is no triangle, `G[R]` is a
   subdivision of a claw.  If there is a triangle, deleting that one
   triangle leaves at most three edge paths, each ending at one of the
   `z_h` not already in the triangle.

Thus an unbounded row has only the following literal geometry: one path
with at most two mobile portal classes, or three pair-labelled arms
joined through one actual cutvertex or one actual triangle packet.

#### Proof

Assume first that `|R|>=2`.  If `x` is a noncutvertex of `G[R]`, then
`R-x` is connected.  If `x` owns no duty, omit it from the model.  If it
owns exactly one duty, say `i`, move `x` from `R` into `Q_i`.  The
enlarged `Q_i` is connected through an actual `x-Q_i` edge; an edge from
`x` to `R-x` restores the `R-Q_i` adjacency; and every other row duty
survives.  No old bag adjacency is lost.  The move either repairs an old
absent pair or preserves the defect set and decreases `|R|`, contrary to
the choice of the model.  Hence every noncutvertex owns at least two
duties.

Owner sets of distinct noncutvertices are disjoint.  Indeed, the
nonempty set of all `R-Q_i` edge-ends cannot be contained in two distinct
singletons.  There are only six duties, so `G[R]` has at most three
noncutvertices.  Every connected graph on at least two vertices has at
least two noncutvertices.

We next show that every block `B` of `G[R]` has at most three vertices.
For each cutvertex `b` of `G[R]` lying in `B`, the component of the
block--cutvertex tree leaving `B` through `b` contains a leaf block and
hence a noncutvertex of `G[R]`.  Choices made at different cutvertices
of `B` lie in disjoint branches.  Together with the noncutvertices which
already lie in `B`, this injects `V(B)` into the set of all
noncutvertices of `G[R]`.  Therefore `|B|<=3`.  A block of order two is
an edge, and a simple 2-connected block of order three is a triangle.

If there are exactly two noncutvertices, no triangle block can occur:
the injection just used would already consume three of them.  Hence all
blocks are bridges, `G[R]` is a tree, and a tree with exactly two
noncutvertices is a path.  Its endpoints own disjoint sets of at least
two duties, so at least four of the six portal sets are those endpoint
singletons.  This proves item 2.

If there are three noncutvertices, their three disjoint owner sets have
order at least two and live in a six-element set.  Equality is forced:
each owner set is a pair and the three pairs partition all duties.  Thus
every row portal is one of `z_1,z_2,z_3`, as asserted.  If a triangle
block `B` occurs, the injection above is a bijection.  Each branch of the
block--cutvertex tree leaving `B` therefore contains exactly one global
noncutvertex; a second triangle anywhere in such a branch would create
another noncutvertex or another leaf branch.  Hence `B` is the unique
triangle and all its branches are edge paths to the remaining `z_h`.
With no triangle all blocks are bridges, so the row is a tree with three
leaves, namely a subdivision of a claw.  This proves item 3.  Finally,
if `|R|=1`, its sole vertex carries every required row edge, giving
item 1.  \(\square\)

### Corollary 1.7 (the three-root cell is literally finite)

Keep outcome 3.  Assume the comparison class is closed under absorbing
an unused connected component into any foreign bag which it meets.  If
`G` is seven-connected, then

\[
                              G[R]\cong K_3.             \tag{1.6}
\]

In particular the three-arm residue is not an unbounded Steiner tree:
it is the literal `2+2+2` triangle-owner cell.

#### Proof

Let `C` be an unused component meeting a foreign bag `Q_i`.  Absorb `C`
into `Q_i`.  This preserves connectedness and `|R|`, loses no model
adjacency, and can only repair an absent pair.  If `C` also had a
neighbour in `R-Z`, a repaired pair would contradict primary defect
minimality; otherwise the new model is equally optimal.  In that new
model the unique root which formerly
owned duty `i` would no longer own it.  It would still own its other
paired duty and could own no third duty, because the other five original
portal sets still end at their assigned roots.  It would therefore be a
noncutvertex with exactly one owned duty, contradicting the first
paragraph of Theorem 1.6 for this equally optimal model.  Hence every
unused component which meets a foreign bag has all its `R`-neighbours in
`Z`.  Absorb all such components.  Every component still unused now has
neighbours in `R` only.

Let `Z={z_1,z_2,z_3}` and let `E` be `R` together with all remaining
unused components.  Every edge from `E-Z` to a foreign model bag is
impossible: the unused components are `R`-private, while Theorem 1.6
says every `R-Q_i` edge ends in `Z`.  Hence any nonempty component of
`G[E-Z]` is separated from the six nonempty foreign bags by the
three-vertex set `Z`, contrary to seven-connectivity.  Thus `E=Z`.
All three vertices of the connected graph `G[R]` are noncutvertices, so
`G[R]` is the triangle.  \(\square\)

Corollary 1.7 is the promised infinite-family closure.  Arbitrarily long
median arms cannot survive the actual HC7 connectivity hypotheses.  The
only unbounded common-row geometry is outcome 2: one induced path with
four or more singleton endpoint duties and at most two literal mobile
portal spans.  Every internal path edge is an actual one-clique row
adhesion; failure to lift it to a whole-graph adhesion must be carried by
one of those two mobile portal classes or by an `R`-private component.
Those objects are the concrete packets/spans to which the guarded web or
opposite-state theorem applies.

### Corollary 1.8 (a long path has literal mobile capacity)

In outcome 2 write the path endpoints as `a,b`.  Assume the same
absorption closure as in Corollary 1.7 and first absorb every unused
component which meets a foreign bag.  Any repair contradicts primary
defect minimality; otherwise the row `R` is unchanged, the resulting
model is equally optimal, and Theorem 1.6 applies again.  Let
`M` be its at most two duties not owned by an endpoint, and put

\[
                    P=\bigcup_{i\in M}N_R(Q_i).          \tag{1.7}
\]

Then either the whole `R`-private envelope is contained in
`P union {a,b}`, or

\[
                         |P\cup\{a,b\}|\ge7.             \tag{1.8}
\]

In particular, if `|R|>=7`, at least five internal vertices of the path
are actual portals for the at most two mobile duties; one mobile duty has
at least three distinct internal portal vertices.

#### Proof

Let `E` be `R` together with every component still unused.  All row
edges to endpoint-owned duties end at `a` or `b`, and every other foreign
edge from `R` ends in `P`.  Thus a nonempty component of

\[
                         G[E-(P\cup\{a,b\})]
\]

has no neighbour outside `P union {a,b}`.  If that set has order at most
six, seven-connectivity excludes the component.  This proves the first
dichotomy.  If `|R|>=7`, the containing set must itself contain at least
seven vertices, five of them different from the two endpoints.  They all
belong to `P`; pigeonhole over `|M|<=2` gives the final assertion.
\(\square\)

## 3. Certified capacity--web interfaces

Let `G` be seven-connected and proper-minor-minimal non-six-colourable.
A **certified three-anchor capacity--web interface** consists of the
following data.

### (C0) One fixed base guard and a rural torso tree

There is a fixed set `A_0` of at most one actual vertex such that
`G-A_0` has a facial clique-tree presentation.  Every failure of the
ordinary planar capacity condition is an overfull adhesion triangle.

There is a finite cyclically ordered set `Gamma` of at least four actual vertices and a
finite family `mathcal F` of nonempty proper **cyclic intervals** in
`Gamma`.  Thus every member of `mathcal F` is the actual vertex set of
one contiguous proper arc of the cyclic order.  Each overfull triangle
`T` is assigned an interval `I(T) in mathcal F` satisfying

\[
                              I(T)\subseteq V(T).         \tag{2.1}
\]

Every member of `mathcal F` is assigned to at least one overfull
triangle.  Thus an actual vertex set hitting every interval hits every
overfull triangle.  Transversals below are subsets of `Gamma`; no
nonvertex point of a geometric circle is allowed.

### (C1) Cyclic-cover realization

For every inclusion-minimal subfamily `mathcal C subseteq mathcal F`
whose union is `Gamma`, its page union has an actual realization

\[
 V(G)=A_{\mathcal C}\mathbin{\dot\cup}R_{\mathcal C}
       \mathbin{\dot\cup}D_1^{\mathcal C}
       \mathbin{\dot\cup}D_2^{\mathcal C}                \tag{2.2}
\]

with all hypotheses of Lemma 1 and `|A_{mathcal C}|<=3`.  Here
`R_{mathcal C}=Gamma` as actual vertex sets, with the cyclic order used
in (C0).  Moreover every
cross in either artificial-terminal society lifts, before contraction,
to one of the following:

* two disjoint repair packets for the two missing diagonals of the
  lobe-median `K_3 join C_4` carrier; or
* four distributed rooted sectors satisfying the audited row-promotion
  hypotheses.

In either case the lifted cross gives a literal `K_7` model.

### (C2) Separated-span equality frame

Whenever `mathcal F` contains three pairwise disjoint intervals, choose
three such intervals.  The actual common adhesion has a partition

\[
 S=P_1\mathbin{\dot\cup}P_2\mathbin{\dot\cup}P_3
   \mathbin{\dot\cup}\{s_4\}\mathbin{\dot\cup}\{s_5\}
   \mathbin{\dot\cup}\{s_6\},                            \tag{2.3}
\]

where every `P_i` is nonempty and independent.  The six blocks in (2.3)
have quotient `K_6` with at most the edge `P_2P_3` absent.  This is the
exact orientation obtained by putting one absent rim diagonal of
`K_3 join C_4` into one equality block: the other diagonal is the sole
possible quotient defect.

More precisely,

\[
                 V(G)=S\mathbin{\dot\cup}D_1
                          \mathbin{\dot\cup}D_2,          \tag{2.4}
\]

where `D_1,D_2` are nonempty and anticomplete.  For
each `j in {1,2}` and `i in {1,2,3}` there is a nonempty connected set

\[
                              X_i^j\subseteq D_j           \tag{2.5}
\]

such that, for fixed `j`, the three sets are pairwise disjoint and
`X_i^j union P_i` is connected.  These are the literal packets carried
by the three separated spans.  Put `B_i^j=X_i^j union P_i` for
`i=1,2,3` and retain the three singleton blocks.  If `P_2P_3` is absent,
there is also a connected set

\[
             Y^j\subseteq D_j-\bigcup_{i=1}^3X_i^j       \tag{2.6}
\]

which is adjacent to both `B_2^j` and `B_3^j`; the two sets `Y^1,Y^2`
lie on their respective open shores and hence are disjoint.  Notice that
(2.3)--(2.6) specify actual boundary equality blocks and the literal
packet repairing the one remaining adjacency, not row names.

Conditions (C0)--(C2) are local certificates.  They do not already state
either global conclusion: (C0) only provides a tree of planar torsos with
possibly overfull triangles; (C1) only says how a cyclic cover is
realized; and (C2) only records the three packet connections and the
one-defect boundary quotient.

## 4. Capacity--web theorem

### Theorem 2 (three-anchor capacity--web composition)

Let `G` have a certified three-anchor capacity--web interface.  Then at
least one of the following holds.

1. `G` contains a literal `K_7` minor (and in the capacity branch it is
   supplied by a lifted repair cross).
2. There is one actual set `A` with `|A|<=3` such that `G-A` is planar,
   and hence `chi(G-A)<=4`.
3. The two open shores contain carriers for the **same** six-block
   partition (2.3).  Contracting either shore forces that partition on
   the unchanged opposite closed side; the two colourings glue and `G`
   is six-colourable.

In particular, if `chi(G)>=7`, outcomes 1 and 2 both give a `K_7` minor
by the uniform clique-apex lifting theorem, while outcome 3 contradicts
minor-minimal non-six-colourability.  Thus no `K_7`-minor-free
seven-chromatic graph admits this certified interface.

#### Proof

If `G` already contains a `K_7` minor, outcome 1 holds.  Hence assume it
does not.  Apply the following discrete form of the exact arc trichotomy
to `mathcal F`: either two actual vertices hit every cyclic interval,
three intervals are pairwise disjoint, or an inclusion-minimal subfamily
covers `Gamma`.  Indeed, if the union does not cover `Gamma`, delete an
uncovered vertex and cut the cyclic order there.  The members of
`mathcal F` become intervals of a linearly ordered finite set, for which
the greedy right-endpoint algorithm proves equality of packing and
transversal numbers.  If the union does cover `Gamma`, delete members
until the cover is inclusion-minimal.

**A two-point transversal.**  Suppose a set `Z` of at most two actual
vertices meets every interval.  By (2.1), it meets every overfull adhesion
triangle.  Delete

\[
                                A=A_0\cup Z.              \tag{3.1}
\]

Then `|A|<=3`.  In the facial clique-tree presentation of `G-A_0`, all
formerly overfull triangles now have order at most two.  Every other
triangle had at most two nontrivial incident pages already.  The audited
fixed-hitting-set rural-tree theorem therefore glues all remaining
torsos planarly.  Hence `G-A` is planar, which is outcome 2.

**A minimal cyclic cover.**  Let `mathcal C` be an inclusion-minimal
subfamily covering `Gamma`.  Use its actual realization (2.2).  Lemma 1
forces a crossed terminal society.  Condition (C1) lifts that crossing to
literal repair packets or distributed rooted sectors, and the audited
packet-promotion theorem gives a literal `K_7`.  This is outcome 1.

**Three separated spans.**  Use the common partition and packets from
(C2).  For fixed `j`, put

\[
 B_i^j=X_i^j\cup P_i\quad(i=1,2,3),\qquad
 B_h^j=\{s_h\}\quad(h=4,5,6).                            \tag{3.2}
\]

The first three sets are connected and pairwise disjoint by (2.5), and
the last three are singleton.  Every pair except possibly
`B_2^jB_3^j` is adjacent through the quotient edges in (2.3).  If that
pair is absent, absorb `Y^j` into `B_2^j`; (2.6) repairs precisely this
last adjacency without meeting another carrier.  Lemma 1.4 now applies
on both open shores for the same actual partition (2.3).  Contracting
the carriers on one shore gives a proper minor whose six-colouring
forces (2.3) on the unchanged opposite side.  Doing this in both
directions and permuting colour names glues the two side colourings.
Hence `G` is six-colourable, which is outcome 3.

At an exact seven-boundary with two full shores, the separately audited
independent-pair plus clique-complement closure gives `K_7` directly;
that already-known terminal does not require synchronized packet
families.

The arc trichotomy is exhaustive, so one outcome holds. \(\square\)

## 5. Application to the lobe-median residue

The audited lobe-median theorem says that every nonsingleton rich-contact
lobe has already terminated in a missing-star model with at most two
spokes, in `K_7^-`, or in the unique carrier

\[
                              K_3\mathbin\vee C_4.        \tag{4.1}
\]

For (4.1), the three common rows are the fixed row triangle and the four
rim bags have two independent missing diagonals.  A terminal-clean cross
is precisely the two-packet promotion in (C1).  Crossless cyclic pages
which satisfy (C0)'s simultaneous port-disk condition are precisely the
web pieces used in the facial clique-tree presentation.
Three separated capacity spans are terminal once their actual trace
blocks satisfy (2.3)--(2.6), by Theorem 2.

Theorems 1.6--1.8 now remove the arbitrary median-arm geometry which
previously preceded this interface.  Every common row is a literal
universal root, an exact `2+2+2` triangle, or an induced path with at
most two mobile portal classes; a long path has at least five actual
mobile portal vertices.  Thus the remaining applicability question is
not another row-support enumeration.  It is the following path-capacity
extraction statement.

> **Capacity certification edge.**  In the actual lobe-median
> `K_3 join C_4` residue after Theorems 1.6--1.8, prove that the at most
> two mobile classes on each surviving path either give the cyclic-cover
> lift in (C1), or three separated path spans determine the same
> one-defect equality frame and defect packet (2.3)--(2.6) on both open
> shores.

This is strictly narrower than the former arbitrary-bag
palette-to-labelled-carrier gap.  It asks for a state exchange on at most
two actual portal spans of an induced path.  The triangle and branching
Steiner-arm families are closed unconditionally by Corollary 1.7.  Once
the displayed path certificates are extracted, Theorem 2 gives the
whole-host terminal without any further row-support cases.

## 6. Trust boundary

The following deductions are unconditional within the stated interface.

* Three omitted actual vertices are now enough in the cyclic-web branch;
  no bipartiteness of the omitted graph is required.
* A two-point span transversal and one fixed base guard produce one
  global three-apex set, not different local apex choices.
* Three separated spans use the same labelled equality partition on both
  actual shores; this is exactly what permits colour gluing.
* A lex-minimal common row has no unbounded block or three-arm geometry:
  the only unbounded cell is one induced path with at most two mobile
  portal classes.

The theorem does **not** infer (C1) or (C2) from abstract row ownership,
from an unrooted `K_6` model, or from arbitrary proper-minor colourings.
Those implications are false without the actual packet and adhesion
data.  The capacity-certification edge above is the sole remaining local
step for this composition route.  A row-internal cutvertex is an actual
clique in the row decomposition, but it is not called a whole-graph
adhesion unless every bypassing mobile packet is placed on a named shore.
