# Reserved-component completion and the three-label order-eight normal form

**Status:** written proof; separate internal audit GREEN in
[`hc7_reserved_component_linkage_completion_audit.md`](hc7_reserved_component_linkage_completion_audit.md).
The parameter-uniform theorem gives an explicit `K_7`-minor model whenever
all but one member of a minimal family of lost branch-set adjacencies can be
restored while reserving one connected subgraph adjacent to the six other
model branch sets.  Its three-label specialization also gives the complete
literal normal form at the resulting eight-vertex boundary.  It does not
prove `HC_7`.

## 1. Setting

Let `G` be a seven-connected graph such that

\[
 \chi(G)=7,\qquad K_7\not\preccurlyeq G,
 \qquad \chi(M)\le 6\text{ for every proper minor }M\text{ of }G.
 \tag{1.1}
\]

Use the spanning labelled `K_7`-minus-one-edge model

\[
                 X,Y,D,U,F_1,F_2,F_3,                  \tag{1.2}
\]

whose only possible missing branch-set adjacency is `X-Y`, and the
branch-set split

\[
                 U=W\mathbin{\dot\cup}U',              \tag{1.3}
\]

from the multi-label transfer theorem.  Thus `W` and `U'` are nonempty and
connected.  The fixed response data include an edge `c_1u_1` with
`c_1 in D` and `u_1 in U'`.  Define the complete owner set by

\[
 \Omega(W)=\{R\in\{X,Y,F_1,F_2,F_3\}:E_G(U',R)=\varnothing\}. \tag{1.4}
\]

Put

\[
 B=N_G(U')\cap W                                      \tag{1.5}
\]

and, for every branch set `R` which is anticomplete to `U'`, put

\[
 A_R=N_G(R)\cap W.                                    \tag{1.6}
\]

Let `I={R_1,R_2,R_3} subseteq Omega(W)` be an inclusion-minimal deficient family of three
such branch sets.  The audited Rado--Menger theorem supplies a two-vertex
set

\[
                         K=\{k_1,k_2\}\subseteq W       \tag{1.7}
\]

which meets every `B`--`(A_{R_1}\cup A_{R_2}\cup A_{R_3})` path in
`G[W]`, while every proper subfamily of `I` has its full labelled linkage.

Choose a component `C` of `G[W-K]` which contains a vertex of

\[
                 (A_{R_1}\cup A_{R_2}\cup A_{R_3})-K. \tag{1.8}
\]

Assume that no branch set outside `U` contains two distinct neighbours of
`C`, and that

\[
                         |N_G(C)|=8.                    \tag{1.9}
\]

The first assumption is exactly the non-repeated-contact branch of the
audited host-separation theorem.

## 2. Literal boundary normal form

### Theorem 2.1

Put `S=N_G(C)`.  Then all of the following hold.

1. The two internal separator vertices both meet `C`:

   \[
                     N_{G[W]}(C)=K.                    \tag{2.1}
   \]

2. Each of the six branch sets different from `U` contains exactly one
   literal vertex of `S`.  Consequently

   \[
      S=\{k_1,k_2\}\mathbin{\dot\cup}
        \{s_D,s_X,s_Y,s_{F_1},s_{F_2},s_{F_3}\},       \tag{2.2}
   \]

   where `s_R in R` and `s_R` has a neighbour in `C`.
3. `S` is the boundary of an actual separation.  The graph `G-S` has at
   least two components, one of which is `C` and another of which contains
   `U'`.
4. For every component `Q` of `G-S`, either `N_G(Q)=S`, or

   \[
                         N_G(Q)=S-\{s\}                \tag{2.3}
   \]

   for a unique `s in S`; in the latter case `N_G(Q)` is the boundary of an
   actual order-seven separation.
5. If the second outcome in item 4 never occurs, then `G-S` has exactly two
   or three components, every one of them is adjacent to every literal
   vertex of `S`, and

   \[
                         \chi(G[S])\le4.                \tag{2.4}
   \]

#### Proof

The component `C` contains no vertex of `B`.  Indeed, if `b in C cap B`
and `a` is the portal from (1.8), a path from `b` to `a` inside connected
`C subseteq W-K` is a `B`--`A_I` path avoiding `K`, contrary to (1.7).
Since `B=N_G(U') cap W`, it follows that

\[
                         E_G(C,U')=\varnothing.          \tag{2.5}
\]

The construction of `C` also gives

\[
                         N_{G[W]}(C)\subseteq K.        \tag{2.6}
\]

By (2.5), every neighbour of `C` outside `W` lies in one of the six branch
sets different from `U`, because the seven branch sets in (1.2) span `G`.
There is at most one such neighbour in each branch set by hypothesis.
Thus (1.9) and (2.6) give

\[
 8=|N_G(C)|\le |K|+6=8.                                \tag{2.7}
\]

Equality holds at every term.  Hence both vertices of `K` occur in the
neighbourhood and every outside branch set contributes exactly one vertex.
This proves items 1 and 2.

The set `C` is connected and has full neighbourhood `S`.  The retained set
`U'` is nonempty, connected, disjoint from `S`, and anticomplete to `C`.
It therefore lies in a different component of `G-S`.  This proves item 3.

Let `Q` be a component of `G-S`.  If it misses some vertex `s of S`, then

\[
                         N_G(Q)\subseteq S-\{s\}.       \tag{2.8}
\]

Seven-connectivity gives `|N_G(Q)|>=7`; since `|S|=8`, equality holds in
(2.8), and exactly one boundary vertex is missed.  The component `C` or the
component containing `U'` supplies a nonempty opposite side, as appropriate,
so `N_G(Q)` is an actual order-seven boundary.  If no boundary vertex is
missed, then `N_G(Q)=S`.  This proves item 4.

Assume now that item 4 never returns an order-seven boundary.  Every
component of `G-S` is `S`-full.  There are at least two by item 3, and there
cannot be four: the audited order-eight four-component theorem would
contradict (1.1).  Hence there are two or three.  Contracting any two of
them separately gives the two-full-shore boundary-absorption theorem, which
implies (2.4).  This proves item 5. \(\square\)

### Corollary 2.2 (the three-component finite normal form)

Assume the no-order-seven outcome of Theorem 2.1 and that `G-S` has exactly
three components.  Then `G[S]` has neither a
clique odd-cycle transversal nor a `K_4` minor after deleting two boundary
vertices.  Consequently it belongs to the audited list of 82
three-colourable eight-vertex boundary graphs, and it contains two
vertex-disjoint odd cycles.

#### Proof

A clique odd-cycle transversal would synchronize the three full component
colourings, while a `K_4` model after deleting two boundary vertices would
combine with the three full components to give an explicit `K_7` model.
Both conclusions contradict (1.1).  The cited order-eight classification
now applies. \(\square\)

## 3. The rank-two linkage geometry

### Theorem 3.1

For every two-element set `J subset I`, there are two vertex-disjoint paths
in `G[W]`, from distinct vertices of `B` to one portal in each set
`A_R`, `R in J`, such that each path contains exactly one vertex of `K` and
the two paths collectively contain both `k_1,k_2`.

Moreover:

1. after choosing one such linkage for each of the three pairs in `I`, some
   owner label is routed through `k_1` in one linkage and through `k_2` in
   another; and
2. there is a partition

   \[
                          W=L_1\mathbin{\dot\cup}L_2    \tag{3.1}
   \]

   into two nonempty connected sets such that each `L_i` meets `B`, each
   contains a different vertex of `K`, and collectively `L_1,L_2` meet all
   three portal sets `A_{R_1},A_{R_2},A_{R_3}`.

#### Proof

Every proper subfamily of the minimal deficient family has its full
labelled linkage.  Apply this to a pair `J`.  Each of its two paths is a
`B`--`A_I` path and therefore meets `K`.  The paths are vertex-disjoint and
`|K|=2`; hence each contains exactly one vertex of `K` and they use different
vertices.  This proves the first assertion.

Choose one linkage for every pair.  If no owner label were ever routed
through both vertices of `K`, each of the three labels would have one fixed
assigned vertex of `K`.  Two labels would receive the same assignment, but
their mutual linkage routes them through different vertices of `K`, a
contradiction.  This proves item 1.

For item 2, start with a linkage `P_1,P_2` for any two owner labels.  Choose
a vertex `a` in the portal set of the third label.  Since `G[W]` is
connected, take a shortest path `Q` from `a` to `P_1 union P_2`.  Apart from
its last vertex, `Q` is disjoint from both linkage paths.  Add `Q` to the
path it first meets.  The result is two disjoint connected subgraphs, each
meeting `B` and a different vertex of `K`, and together meeting all three
portal sets.  Every component of the remaining induced subgraph has a
neighbour in at least one of the two connected subgraphs, because `G[W]` is
connected.  Assign each such component to one adjacent subgraph.  The two
enlarged sets give (3.1) and retain all stated properties. \(\square\)

The partition (3.1) is the exact static rank-two object.  It is not the
three-part partition needed by the multi-label transfer theorem: one of the
two sets may have to carry two owner labels.

## 4. An explicit `K_7` model when one component can be reserved

The completion mechanism is not special to three owners.  The following
parameter-uniform form returns to the general setting of the audited
multi-label transfer theorem.

### Theorem 4.1 (reserved-component linkage completion)

Let `I=Omega(W)` be an inclusion-minimal deficient complete owner set of
order `m`, where `2<=m<=5`, and let `K subseteq W` be its Rado--Menger
transversal of order `m-1`.  Let `C` be a component of `G[W-K]` which is
anticomplete to `U'` and adjacent to every one of the six branch sets
different from `U`.

If, for some `R_0 in I`, the proper subfamily `I-{R_0}` has a full labelled
portal linkage in `G[W-C]`, then `G` contains a `K_7` minor.

#### Proof

Let `P_1,...,P_{m-1}` be the linkage paths and put

\[
                    A=U'\cup\bigcup_{i=1}^{m-1}V(P_i). \tag{4.1}
\]

Each path starts at a distinct vertex of `B=N_G(U') cap W`, so `A` is
connected.  Every path is a `B`--`A_I` path and hence meets `K`.  The paths
are pairwise disjoint and their number equals `|K|`; consequently each uses
one different vertex of `K` and their union contains all of `K`.

The component `C` has a neighbour in `K`: its neighbourhood in connected
`G[W]` is a nonempty subset of `K`.  Hence `A` and `C` are adjacent.  The
terminal portal edges make `A` adjacent to every owner other than `R_0`;
the definition of the complete owner set makes `U' subseteq A` adjacent to
every nonowner among `X,Y,F_1,F_2,F_3`; and the fixed response edge gives
the `A-D` adjacency.  Thus `A` is adjacent to every outside branch set
except possibly `R_0`, while `C` is adjacent to all six by hypothesis.

If `R_0` is `X` or `Y`, discard that branch set.  The remaining five
outside branch sets already form a clique minor model.  Otherwise merge
the adjacent branch sets `X` and `R_0`.  Their connected union is adjacent
to `Y` through the old `R_0-Y` edge, so it and the other four outside
branch sets form a `K_5` model.  In both cases denote the five resulting
branch sets by `Q_1,...,Q_5`.  Each is adjacent to both `A` and `C`.

Therefore

\[
                         A,C,Q_1,Q_2,Q_3,Q_4,Q_5       \tag{4.2}
\]

are seven pairwise disjoint connected branch sets with all pairwise
adjacencies.  They form an explicit `K_7`-minor model. \(\square\)

### Corollary 4.2 (residual-subgraph completion)

In Theorem 4.1, allow the linkage paths to meet `C`, and define `A` by
(4.1).  The same conclusion holds if \(C-\bigcup_iV(P_i)\) contains a nonempty
connected subgraph `C_0` which is adjacent to `A` and to all six outside
branch sets.

#### Proof

Use `C_0` in place of `C` in the seven branch sets (4.2).  It is disjoint
from `A` by hypothesis, and every adjacency used in the proof of Theorem
4.1 remains available. \(\square\)

### Corollary 4.3 (the three-owner order-eight specialization)

Assume in addition that the complete owner set of `W` is exactly

\[
                         \Omega(W)=I.                   \tag{4.3}
\]

If, for some `R_0 in I`, the two labels in `I-\{R_0\}` have a full labelled
portal linkage whose two paths avoid `C`, then `G` contains a `K_7` minor.

#### Proof

Theorem 2.1 says that `C` is anticomplete to `U'` and adjacent to all six
outside branch sets.  Apply Theorem 4.1 with `m=3`. \(\square\)

### Corollary 4.4 (exact remaining linkage obstruction)

In a `K_7`-minor-free host satisfying (4.3), every full linkage for every
two-owner subfamily meets `C`.  Equivalently, deleting `C` destroys the
rank-two labelled linkage for each of the three pairs.

This is the smallest remaining static linkage statement.  A proof-closing
continuation must use a proper-minor colouring response to do one of the
following:

1. reroute one two-owner linkage off `C`, when Corollary 4.3 is terminal;
2. split the part of `C` used by the linkage while preserving a connected
   remainder adjacent to the five selected outside branch sets; or
3. retain a legal boundary partition and a connected subgraph meeting one
   complete boundary duty at the exact order-seven or order-eight boundary.

The strict gammoid and seven-connectivity alone give none of these three
dynamic conclusions.

## 5. Dependencies and trust boundary

- [multi-owner portal linkage transfer](../results/hc7_multi_owner_portal_linkage_transfer.md)
- [four full components close an order-eight boundary](../results/hc7_full_order8_four_component_closure.md)
- [two full shores force a four-colour boundary](../results/hc7_two_full_shore_boundary_absorption.md)
- [three-component order-eight boundary classification](../results/hc7_order8_three_component_boundary_classification.md)

Theorem 2.1 is a literal host reduction, Theorem 3.1 is a static linkage
normal form, and Theorem 4.1 is a parameter-uniform explicit minor
construction.  The note does not force a linkage avoiding `C`, does not
prove that the complete owner set has order three in the order-eight branch,
and does not synchronize the colourings of two closed shores.
