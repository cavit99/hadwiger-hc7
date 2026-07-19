# A two--three allocation theorem for the ordered order-eight interface

**Status:** written proof; separate internal audit GREEN in
[`hc7_order8_ordered_two_three_allocation_audit.md`](hc7_order8_ordered_two_three_allocation_audit.md).  This is an
unbounded conditional reduction inside the connected order-eight interface.
It does not prove `HC_7`, and none of the separations returned below is
asserted to carry compatible colourings on its two closed shores.

## 1. Setting

Let `G` be a seven-connected graph satisfying

\[
 \chi(G)=7,\qquad K_7\not\preccurlyeq G,
 \qquad \chi(M)\le 6\text{ for every proper minor }M\text{ of }G. \tag{1.1}
\]

Suppose

\[
 V(G)=L\mathbin{\dot\cup}S\mathbin{\dot\cup}R,
 \qquad E_G(L,R)=\varnothing,
\]

where `G[L]` and `G[R]` are connected and

\[
 S=\{d,e,x_d,y_d,x_e,y_e,x_0,y_0\}.
\]

Assume that `d,e` are nonadjacent and that `G[S]` contains the two
vertex-disjoint triangles

\[
                     d x_d y_d d,
               \qquad e x_e y_e e.                 \tag{1.2}
\]

Suppose `G[R]` contains disjoint connected subgraphs `P_0,P_1`, each
adjacent to every literal vertex of `S`, with an edge between them.  Suppose
`G[L]` contains disjoint adjacent connected subgraphs `A_d,A_e` such that

\[
 S-\{d\}\subseteq N_G(A_d)\cap S,
 \qquad
 S-\{e\}\subseteq N_G(A_e)\cap S.                 \tag{1.3}
\]

Fix a proper six-colouring of `G[L\cup S]` in which `d,e` have one common
colour `alpha`.  Assume that it supplies three `d`--`e` paths

\[
                         K_1,K_2,K_3                \tag{1.4}
\]

with interiors in `L`, where `K_i` uses exactly the colours
`{alpha,beta_i}` and the three colours `beta_i` are distinct.  Thus every
common vertex of two different paths has colour `alpha`.  This is precisely
the conclusion of the audited merged-root Kempe-path theorem in the intended
application.  We also retain its palette convention: the six colours are
`alpha`, the two distinct colours on `x_d,y_d`, and
`beta_1,beta_2,beta_3`.

Finally assume that

\[
                     H=G[L\cup\{d,e\}]              \tag{1.5}
\]

contains two internally vertex-disjoint `d`--`e` paths.  The complementary
local-connectivity-one case is handled by the separate ordered-series
reduction.

## 2. An induced two-part normalization of `L`

### Lemma 2.1

There is a partition

\[
                         L=E\mathbin{\dot\cup}D      \tag{2.1}
\]

such that `G[E]` and `G[D]` are connected and adjacent,
`A_e\subseteq E`, `A_d\subseteq D`, and

\[
 N_G(E)\cap S=S-\{e\},
 \qquad
 N_G(D)\cap S=S-\{d\}.                             \tag{2.2}
\]

#### Proof

Choose spanning trees of `A_e,A_d` and one edge between them.  Their union
is a tree, which extends to a spanning tree `T` of the connected graph
`G[L]`.  Delete the selected `A_e`--`A_d` edge from `T`, and let `E,D` be
the vertex sets of the two resulting components, with `A_e\subseteq E`.
The induced graphs on `E,D` are connected and the deleted edge joins them.
The inclusions in (1.3) are preserved.

It remains to prove the two missing contacts in (2.2).  If `E` had a
neighbour at `e`, then `G[E]` would be a connected subgraph adjacent to both
`d,e` and disjoint from `A_d`.  The audited ordered-defect crossing theorem
would give an explicit `K_7`-minor model, contrary to (1.1).  Hence `E`
misses `e`.  The symmetric argument shows that `D` misses `d`.  This proves
(2.2). \(\square\)

For a boundary vertex `s`, put

\[
                         P_s=N_G(s)\cap E,
\]

and put

\[
                         P_D=N_G(D)\cap E.           \tag{2.3}
\]

All of `P_d,P_{x_d},P_{y_d},P_{x_e},P_D` are nonempty.

### Lemma 2.2 (three distinct first portals)

The set `P_d` contains at least three vertices.  The set `P_D` contains at
least two vertices.

#### Proof

The first internal vertex of each `K_i` is adjacent to `d`.  It lies in
`E`: it cannot lie in `D`, because `D` has no neighbour at `d`, and `E,D`
partition `L`.  Its colour is `beta_i`, so the three first vertices are
distinct.  Thus `|P_d|\ge3`.

If `P_D=\{q\}`, every `d`--`e` path in `H` must contain `q`: it starts in
`E`, because `D` misses `d`, and eventually enters `D`, because `E` misses
`e`; every `E`--`D` edge then has its `E`-end at `q`.  This contradicts the
two internally disjoint paths assumed after (1.5).  Hence `|P_D|\ge2`.
\(\square\)

## 3. The positive two--three allocation

### Lemma 3.1 (the branch-set construction)

Suppose `G[E]` contains a connected subgraph `J` and
`G[E\cup\{x_e\}]` contains a connected subgraph `T`, with `J,T`
vertex-disjoint, such that

1. `J` meets both `P_d` and `P_D`;
2. `x_e\in T`, and `T` meets `P_{x_d},P_{y_d}`; and
3. an edge joins `J` and `T`.

Then `G` contains a `K_7` minor.

#### Proof

The following are seven pairwise disjoint connected vertex sets:

\[
 P_0,\quad P_1,\quad \{x_d\},\quad \{y_d\},\quad
 T,\quad D\cup\{e\},\quad J\cup\{d\}.             \tag{3.1}
\]

The first two sets are adjacent and are adjacent to every later set through
its displayed boundary vertex.  The sets `\{x_d\},\{y_d\},J\cup\{d\}`
are pairwise adjacent through the triangle `d x_d y_d d`.  The subgraph
`T` supplies the contacts from its branch set to `x_d,y_d`, while `D`
supplies the corresponding contacts from `D\cup\{e\}`.  The edge
`x_e e` joins the fifth and sixth sets.  The assumed `J`--`T` edge joins
the fifth and seventh sets, and the contact of `J` with `P_D` joins the
last two sets.  Thus (3.1) is an explicit `K_7`-minor model. \(\square\)

We use the five-terminal completion appearing in the audited
[two--three linkage reduction](../results/hc7_order8_three_portal_two_three_reduction.md).
For distinct terminals

\[
                  a_1,a_2,a_3,b_1,b_2
\]

in a graph `F`, its **Xie completion** adds the seven virtual edges

\[
 b_1b_2,
 \qquad a_i b_j\quad(i\in\{1,2,3\},\ j\in\{1,2\}). \tag{3.2}
\]

The cited result records the external theorem used here: if this completion
is six-connected, the original graph `F` contains disjoint connected
subgraphs containing respectively the terminal triple and terminal pair.
Virtual edges are used only in the connectivity test.

### Lemma 3.2 (six-connected completion)

Suppose there are distinct vertices

\[
 p\in P_d,\qquad q\in P_D,
 \qquad a\in P_{x_d},\qquad b\in P_{y_d}.           \tag{3.3}
\]

Let `F=G[E\cup\{x_e\}]`, and take the terminal triple
`(a,b,x_e)` and terminal pair `(p,q)`.  If the Xie completion of `F` is
six-connected, then `G` contains a `K_7` minor.

#### Proof

The two--three linkage theorem gives disjoint connected subgraphs `T,J_0`
of the original graph `F`, where

\[
 \{a,b,x_e\}\subseteq T,
 \qquad \{p,q\}\subseteq J_0.                     \tag{3.4}
\]

Because `x_e\in T`, the subgraph `J_0` lies in `E`.  Also
`T\cap E` is nonempty, since it contains `a,b`.  In the connected graph
`G[E]`, choose a shortest path from `J_0` to `T\cap E`.  Absorb into `J_0`
all vertices of this path except its endpoint in `T`.  The resulting
connected subgraph `J` is disjoint from and adjacent to `T`; it still meets
`P_d,P_D`.  The seven sets

\[
 P_0,\ P_1,\ \{x_d\},\ \{y_d\},\ T,
 D\cup\{e\},\ J\cup\{d\}
\]

are exactly the sets checked in Lemma 3.1, with `T` itself as the fifth
set because it already contains `x_e`.  They form a `K_7`-minor model.
\(\square\)

## 4. Failure of distinct representatives

Consider the four portal sets

\[
                       P_d,\quad P_D,\quad
                       P_{x_d},\quad P_{y_d}.        \tag{4.1}
\]

### Lemma 4.1 (Hall collapse)

If the four sets in (4.1) have no system of distinct representatives, then
at least one of the following holds.

1. `G` has an actual separation of order at most seven.
2. `|E|=3`.
3. There is a vertex `v\in E` such that

   \[
                         P_{x_d}=P_{y_d}=\{v\}.      \tag{4.2}
   \]

#### Proof

Hall's theorem supplies a deficient subfamily `I`.  Put

\[
                         Z=\bigcup_{P\in I}P,
 \qquad |Z|\le |I|-1.                              \tag{4.3}
\]

Suppose first that `P_D\in I`, and let `J` be the set of boundary labels
among `d,x_d,y_d` whose portal sets belong to `I`.  Thus
`|I|=|J|+1` and `|Z|\le |J|`.  If `E-Z` is nonempty, let `C` be a component
of the induced graph `G[E-Z]`.  Every neighbour of `C` in `E` lies in `Z`.
Because `P_D\subseteq Z`, the component has no neighbour in `D`; because
the portal set of every member of `J` lies in `Z`, it has no neighbour at
those boundary vertices.  It also has no neighbour at `e`, by (2.2).
Consequently

\[
 N_G(C)\subseteq Z\cup\bigl(S-(\{e\}\cup J)\bigr),
 \qquad |N_G(C)|\le |J|+(7-|J|)=7.                 \tag{4.4}
\]

This is an actual separation: `C` is nonempty and `R` survives outside
`C\cup N_G(C)`.  This gives outcome 1.  If `E=Z`, then
`|E|\le |I|-1\le3`; Lemma 2.2 gives `|E|\ge3`, so outcome 2 holds.

It remains that `P_D\notin I`.  A deficient subfamily containing `P_d` is
impossible, because `|P_d|\ge3` whereas `|I|-1\le2`.  No singleton
subfamily is deficient because every portal set is nonempty.  Hence
`I=\{P_{x_d},P_{y_d}\}` and its union has order at most one.  Both sets are
nonempty, so (4.2) follows. \(\square\)

The common-portal outcome has one immediate closure which does not use the
Xie completion.

### Lemma 4.2 (a common portal also adjacent to `x_e`)

Assume (4.2).  If `v\in P_{x_e}`, then `G` contains a `K_7` minor.

#### Proof

The colours on `x_d,y_d` are distinct in the fixed proper colouring, so
the colour of their common neighbour `v` is neither of those colours.  It
is therefore `alpha` or one of `beta_1,beta_2,beta_3`.

If `v` has colour `beta_j`, choose `i\ne j`.  Then `K_i` avoids `v`, since
its colours are `alpha,beta_i`.  If `v` has colour `alpha`, one of the two
internally disjoint `d`--`e` paths in `H` avoids `v`.  In either case there
is a `d`--`e` path `Q` avoiding `v`.

Take the segment of `Q` from its first vertex in `E` through its last
vertex in `E` before the path first enters `D`.  Its vertex set is a
connected subgraph `J_0\subseteq E-v` meeting `P_d` and `P_D`.  Such a
first entry into `D` exists because `E` misses `e`.  In the connected graph
`G[E]`, absorb into `J_0` a shortest path to `v`, excluding `v` itself.
This produces a connected `J` disjoint from and adjacent to the connected
subgraph `T=G[\{v,x_e\}]`.  The subgraph `T` contains `x_e` and meets
`P_{x_d},P_{y_d}`, so Lemma 3.1 applies.
\(\square\)

If (4.2) holds, `v\notin P_{x_e}`, and `|E|\ge4`, choose

\[
 q\in P_D-\{v\},\qquad
 p\in P_d-\{v,q\},\qquad
 w\in E-\{p,q,v\}.                                \tag{4.5}
\]

These choices exist by Lemma 2.2.  The Xie completion in
`F=G[E\cup\{x_e\}]` with terminal triple `(v,w,x_e)` and pair `(p,q)` is
called the **common-portal completion**.  If it is six-connected, the proof
of Lemma 3.2 applies verbatim: the returned triple subgraph contains `v`
and `x_e`, hence meets the three required portal classes, while the pair
subgraph meets `P_d,P_D`.  Thus a `K_7` minor results.  The filler terminal
`w` has no further role.  Notice that six-connectivity can occur only when
`|E\cup\{x_e\}|\ge7`; the cases of smaller order are not eliminated by
this observation.

## 5. The exact residue of a non-six-connected completion

The next statement applies either to the completion in Lemma 3.2 or to the
common-portal completion following Lemma 4.2.

### Lemma 5.1 (completion cut)

Assume `|E|\ge6` and that the selected Xie completion is not
six-connected.  Then there are a set

\[
                         K\subseteq E\cup\{x_e\},
 \qquad |K|\le5,                                   \tag{5.1}
\]

and a nonempty connected proper set `C\subset E` such that

\[
 N_E(C)\subseteq K\cap E,                          \tag{5.2}
\]

and

\[
 N_G(C)=N_E(C)\mathbin{\dot\cup}N_D(C)
             \mathbin{\dot\cup}(N_G(C)\cap S),
 \qquad e\notin N_G(C).                           \tag{5.3}
\]

The completed-graph separation can be chosen in one of two terminal forms:

1. `C` contains none of the five nominated terminals; or
2. the two nominated pair terminals belong to `K`, and surviving triple
   terminals occur in components on both sides of `K`.

In either case `B=N_G(C)` is the boundary of an actual separation of `G`.

#### Proof

The completion has at least seven vertices.  Since it is not
six-connected, it has a separation with separator `K` of order at most
five and two nonempty open sides.

The virtual edges on the five terminals have the following elementary
consequence.  If terminals occur in both open sides, both pair terminals
must lie in `K`; otherwise a surviving pair terminal is virtually adjacent
to every other surviving terminal.  Surviving triple terminals must then
occur in both sides.  If terminals occur in at most one open side, at least
one open side is terminal-free; this includes the case in which all five
terminals belong to `K`.

In the latter case choose a component `C` of a terminal-free open side.  In the
former case choose a component containing a surviving triple terminal on a
side not containing the literal terminal `x_e`; such a side exists because
the triple terminals are split.  If `x_e\in K`, choose either surviving
triple-terminal side.  Thus in all cases `C\subset E`.

No original edge of `G[E\cup\{x_e\}]` joins `C` to the other side, so
(5.2) holds.  The partition (2.1), the absence of `L`--`R` edges, and
(2.2) give the disjoint decomposition (5.3).  A vertex in the other open
side and the nonempty set `R` lie outside `C\cup N_G(C)`, so `N_G(C)` is
an actual separation boundary.  The terminal description follows from the
choice of `C`. \(\square\)

### Corollary 5.2 (small boundary or positive excess)

With `B=N_G(C)` as in Lemma 5.1, at least one of the following holds.

1. `|B|=7`, so `G` has an actual order-seven separation.
2. `|B|=8`, and the audited small-boundary lobe theorem gives either an
   actual order-seven separation or a strict order-eight boundary-full
   lobe descent.
3. `|B|\ge9`, and

   \[
    |N_D(C)|+|N_G(C)\cap S|
       \ge 9-|N_E(C)|
       \ge 9-|K|
       \ge4.                                       \tag{5.4}
   \]

#### Proof

The set `B` is an actual separator, so seven-connectivity gives
`|B|\ge7`.  Outcome 1 is immediate.  If `|B|=8`, then `C` is a nonempty
connected proper subset of the component `L` of `G-S`, and (5.3) gives

\[
 |N_{G[L]}(C)|+|N_G(C)\cap S|=8.
\]

The small-boundary lobe theorem applies and gives outcome 2.  The remaining
case is `|B|\ge9`; (5.2)--(5.3) give (5.4). \(\square\)

The order-seven boundary in outcomes 1 and 2 is only structural.  No common
boundary equality partition has been proved there.

### Proposition 5.3 (the retained colouring obstruction)

Let `pi` be the equality partition induced on `B=N_G(C)` by restricting
the fixed merged-root colouring to `G[C\cup B]`.  For every edge
`uv` with `u\in C` and `v\in B`, every six-colouring of `G-uv` satisfies

\[
                              c(u)=c(v),             \tag{5.5}
\]

and its restriction to `G-C` induces on `B` an equality partition different
from `pi`.

#### Proof

The graph `G-uv` is a proper minor and is six-colourable by (1.1).  If one
such colouring assigned different colours to `u,v`, restoring the edge
would six-colour `G`, proving (5.5).

Suppose its restriction to `G-C` induced the partition `pi` on `B`.
Permute its colour names so that it agrees vertexwise on `B` with the fixed
colouring of `G[C\cup B]`.  The two colourings then glue to a proper
six-colouring of `G`: the inner colouring includes every edge from `C` to
`B`, while the outer colouring covers all remaining edges.  This contradicts
`chi(G)=7`.  Hence the two boundary partitions differ. \(\square\)

## 6. Combined reduction and trust boundary

The preceding lemmas prove the following exhaustive reduction for the
locally two-connected ordered branch.

### Theorem 6.1

Under the hypotheses of Section 1, at least one of the following holds.

1. `G` contains an explicit `K_7`-minor model.
2. `G` has an actual separation of order seven.
3. The small-boundary lobe theorem gives a strict order-eight boundary-full
   descent.
4. A selected Xie completion has order at most six.  In particular, this
   includes some configurations with `|E|\le5`.
5. A Hall obstruction has the unresolved small part `|E|=3`.
6. There is a nonempty connected proper set `C\subset E` satisfying
   (5.2)--(5.4), with `|N_G(C)|\ge9`, and the incompatible operation-specific
   boundary responses of Proposition 5.3.

#### Proof

If the four portal sets in (4.1) have distinct representatives, apply
Lemma 3.2.  A six-connected completion gives outcome 1.  A completion of
order at most six gives outcome 4; otherwise Lemma 5.1 and Corollary 5.2
give outcomes 2, 3, or 6.

If the four sets do not have distinct representatives, Lemma 4.1 gives
outcome 2, outcome 5, or the common portal (4.2).  Lemma 4.2 gives outcome
1 when that portal also sees `x_e`.  Otherwise, if `|E|\ge4`, form the
common-portal completion.  Its six-connected and non-six-connected cases
give the same alternatives as above; if the completion has order at most
six, outcome 4 holds.  Finally `|E|\le3`, together with Lemma 2.2, gives
outcome 5. \(\square\)

Outcomes 4--6 are genuine open residues.  In particular:

- no finite argument eliminating the small completion or the three-vertex
  part is asserted here;
- positive excess in (5.4) is not a decreasing induction parameter;
- the returned order-seven separation is not known to carry one equality
  partition extending through both closed shores;
- Proposition 5.3 records incompatible, rather than compatible, boundary
  colourings; and
- the normalization does not prove that a later proper-minor operation
  preserves the labels `E,D,P_0,P_1`.

Thus the theorem closes every six-connected five-terminal completion for
arbitrary `|E|`, but it does not close the non-six-connected completion or
prove `HC_7`.

## 7. Inputs

- [ordered crossings of the two deficient connected
  subgraphs](../results/hc7_order8_ordered_defect_crossing.md);
- [three merged-root Kempe paths](../results/hc7_merged_root_three_kempe_locks.md);
- [the audited two--three linkage reduction and its statement of Xie's
  theorem](../results/hc7_order8_three_portal_two_three_reduction.md); and
- [the small-boundary lobe descent](../results/hc7_order8_small_boundary_lobe_descent.md).
