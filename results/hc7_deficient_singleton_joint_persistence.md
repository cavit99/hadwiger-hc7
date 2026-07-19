# Joint deletion at the singleton end of a missing model adjacency

**Status:** written proof; separate internal audit GREEN in
[`hc7_deficient_singleton_joint_persistence_audit.md`](hc7_deficient_singleton_joint_persistence_audit.md).

This note puts the common endpoint of the model-preserving two-edge
deletion at the most useful possible vertex: the singleton branch set at
one end of the unique missing adjacency of a spanning near-clique model.
The proof is a deletion-capacity count across the other branch sets.  It is
parameter-uniform and uses no colouring argument.

## 1. Uniform theorem

Let `t>=3`, let `F=K_t-rs`, and let `G` be a `t`-connected graph with no
`K_t` minor.  Suppose

\[
                 \mathcal M=(B_y:y\in V(F))                 \tag{1.1}
\]

is a spanning labelled `F`-minor model in `G` and

\[
                            B_r=\{x\}.                       \tag{1.2}
\]

For every label

\[
                y\in V(F)-\{r,s\},
       \qquad n_y=|N_G(x)\cap B_y|.                         \tag{1.3}
\]

### Theorem 1.1 (deficient-singleton joint persistence)

The following statements hold.

1. `B_s` is anticomplete to `x`, every `n_y` is positive, and

   \[
          d_G(x)=\sum_{y\in V(F)-\{r,s\}}n_y.              \tag{1.4}
   \]

2. A set `Z` of edges incident with `x` can be deleted while the same
   branch sets in (1.1) remain a spanning labelled `F`-model if and only
   if, for every `y in V(F)-{r,s}`, fewer than `n_y` members of `Z` end in
   `B_y`.
3. The maximum number of edges incident with `x` which can be deleted
   simultaneously while preserving the same spanning labelled model is

   \[
                             d_G(x)-(t-2).                    \tag{1.5}
   \]

   In particular, there are two such edges.
4. If a prescribed edge `xu`, with `u in B_y`, is individually persistent
   for this model, then it belongs to a maximum set in item 3.
   If it is not persistent, then

   \[
                         N_G(x)\cap B_y=\{u\}.                \tag{1.6}
   \]

Moreover, at least three edges incident with `x` are individually
persistent, and the pairs of persistent edges which are not jointly
persistent form a matching.  Each such forbidden pair is exactly the two
edges from `x` into one branch set with `n_y=2`.

#### Proof

If `x` had a neighbour in `B_s`, the displayed branch sets would realize
every edge of `K_t`, contrary to the exclusion of a `K_t` minor.  Since
the model is spanning and `B_r={x}`, every neighbour of `x` therefore lies
in one of the `t-2` branch sets indexed by `V(F)-{r,s}`.  The model requires
the adjacency `r y` for every such label `y`, and the singleton condition
forces `n_y>=1`.  This proves item 1.

Deleting edges incident with `x` does not affect the connectivity of any
branch set.  The only required model adjacency which such a deletion can
destroy is the adjacency from `B_r={x}` to a branch set `B_y`.  It survives
exactly when at least one of the `n_y` edges remains.  This proves item 2.

Call

\[
                              c_y=n_y-1                         \tag{1.7}
\]

the deletion capacity at label `y`.  Connectivity gives `d_G(x)>=t`, so
item 1 yields

\[
       \sum_y c_y=d_G(x)-(t-2)\ge2.                            \tag{1.8}
\]

At each label `y`, retain one of the `n_y` incident edges and delete the
other `c_y`.  Item 2 shows that all
`d_G(x)-(t-2)` selected edges may be deleted simultaneously.  Conversely,
every model-preserving deletion must retain at least one edge at each of
the `t-2` required labels, so no larger incident set can be deleted.  This
proves item 3.

The prescribed edge `xu` is persistent exactly when `n_y>=2`.  In that
case retain a different edge at label `y`, retain one arbitrary edge at
every other label, and delete every remaining incident edge.  This is a
maximum set from item 3 and contains `xu`.  If `xu` is not persistent,
then `n_y=1`, which is exactly (1.6).  This proves item 4.

Finally, the individually persistent edges are precisely all edges at
labels with `n_y>=2`.  Subject to (1.8), their number is at least three:
either some `n_y>=3`, or at least two labels have multiplicity at least
two.  Edges belonging to distinct labels are jointly persistent.  Within
one label, every pair is jointly persistent when `n_y>=3`, while the two
edges at a label with `n_y=2` are not.  No persistent edge belongs to two
exceptional pairs because the label classes partition the incident edges.
\(\square\)

## 2. Colouring consequence for `HC_7`

Assume now `t=7`, `chi(G)=7`, and every proper minor of `G` is
six-colourable.  Theorem 1.1 gives a model-preserving set of exactly
`d_G(x)-5` incident edges.  In particular, there are at least two.  Choose
two of them and write them as

\[
                             xa,\qquad xb.                     \tag{2.1}
\]

The graph `H=G-{xa,xb}` is a proper subgraph, hence six-colourable, and it
contains the same spanning labelled `K_7`-minus-one-edge model with the
deficient singleton `{x}`.

- If `ab` is absent, contracting the induced two-edge star on `x,a,b`
  gives a six-colouring of `H` whose colour class on `N_G(x)` is exactly
  `{a,b}`.  The audited saturation-or-bypass theorem applies.
- If `ab` is present, the three vertices form a critical triangle.  The
  audited jointly persistent incident-edge colouring theorem gives two
  exclusive one-edge response families.  They are either Kempe-separated,
  or a first transition exposes a common-coloured actual separator or a
  connected dominating bipartite subgraph with five-chromatic,
  `K_6`-minor-free complement.

Thus both outer endpoints of the common deletion now lie in named branch
sets adjacent to the deficient singleton.  No internal rooted support
class remains in this normalization.

If `d_G(x)=7`, then `N_G(x)` is the boundary of an actual order-seven
separation: one open side is `{x}`, while the nonempty branch set `B_s`
lies outside `N_G[x]`.  If additionally the maximum deleted pair `xa,xb`
has nonadjacent outer endpoints, the exact contraction colouring has one
remaining neighbour of `x` in each of the five common branch sets, and
those five neighbours receive the five alternate colours bijectively.
Indeed, every missing alternate colour at `N_G(x)` would permit recolouring
`x` and restoring both deleted edges, contrary to `chi(G)=7`.

Consequently, after excluding an actual order-seven separation one has
`d_G(x)>=8` and at least three incident edges can be deleted simultaneously
while preserving the same labelled model.

There is a sharper dense-alternative bound at this deficient singleton.
Let `P` be the set of outer endpoints of the individually persistent
edges.  If every jointly persistent pair has adjacent outer endpoints,
then

\[
                           G[P]=K_p-M',                        \tag{2.2}
\]

where `p=|P|` and `M'` is a (possibly proper) submatching of the pairs of
vertices at labels with `n_y=2`.  In a `K_7`-minor-free host this forces

\[
                           p\le6,
               \qquad     d_G(x)\le8.                        \tag{2.3}
\]

Consequently degree at least nine forces two jointly persistent incident
edges with nonadjacent outer endpoints, and hence the exact star-
contraction trace.

To prove these claims, note first that edges from different repeated label
classes are jointly persistent, as is every pair within a class of order
at least three.  Under the displayed dense alternative, all corresponding
outer endpoints are adjacent.  Only the two endpoints of a class of order
two may be nonadjacent.  The actually missing pairs therefore form the
matching `M'`, proving (2.2).

If `p>=8`, the graph `K_p-M'` has a `K_6` minor; the explicit constructions
for all matching orders are recorded in the audited
[support-class theorem](../results/hc7_persistent_support_class_refinement.md).
Together with the adjacent singleton `{x}`, that minor would form a
`K_7` model.  If `p=7`, the matching has order at most two: three classes
of order two already account for six persistent edges, and any further
persistent edge either enlarges one of those classes, removing one missing
pair, or belongs to another class of order at least two, making `p>=8`.
But `K_7` minus a matching of order at most two also has a `K_6` minor.
Thus `p<=6`.

Let `r_0` be the number of common labels with multiplicity at least two.
Every other one of the five labels contributes exactly one nonpersistent
edge, so

\[
                          d_G(x)=p+5-r_0.                      \tag{2.5}
\]

If `r_0>=2`, then (2.5) and `p<=6` first give `d_G(x)<=9`.  If
`r_0=1` and `p=6`, the six persistent endpoints form a clique, again
giving a `K_6` minor adjacent to `x`; hence `p<=5` and again
`d_G(x)<=9`.  Equality in this provisional degree bound is possible only
for `(r_0,p)=(1,5)` or `(2,6)`.  The corresponding multiplicities are

\[
                       (5,1,1,1,1)
       \quad\hbox{or}\quad(4,2,1,1,1).                       \tag{2.4}
\]

In the second pattern, the two endpoints `u,v` of the order-two class
must be nonadjacent, since otherwise all six persistent endpoints form a
clique.  Let `A` be the four endpoints in the order-four class.  Then `A`
is a clique, and both `u` and `v` are adjacent to every vertex of `A`.
The graph obtained from `G` by deleting `{x} union A` is connected (in
fact, it is two-connected), because `G` is seven-connected.  It therefore
contains a `u`--`v` path avoiding `{x} union A`.  Split this path at any
edge into two connected sets, one containing `u` and one containing `v`.
Together with `{x}` and the four singleton sets indexed by `A`, these two
sets are seven pairwise adjacent branch sets: each contains an endpoint
adjacent to `x` and to all four members of `A`, and the two sets are
adjacent across the chosen path edge.  This is a `K_7`-minor model, a
contradiction.

In the first pattern, the five persistent endpoints `P` lie in one class
of order five and hence induce a clique.  Choose the unique neighbour `y`
of `x` in any one of the other four common branch sets.  The graph `G-x`
is six-connected.  By the Fan Lemma it contains five internally disjoint
paths from `y` to the five distinct vertices of `P`, meeting pairwise only
at `y`.  The union of these paths with their endpoints in `P` removed is
a connected set `T`, disjoint from `{x} union P`, adjacent to every vertex
of `P`, and adjacent to `x` through `xy`.  Thus

\[
                         \{x\},\quad T,
                 \quad \{p\}\ (p\in P)
\]

are seven pairwise adjacent branch sets, again a `K_7`-minor model.  Both
degree-nine equality patterns are impossible.  Hence (2.3) holds, and
degree at least nine forces a jointly persistent pair with nonadjacent
outer endpoints.

## 3. Trust boundary

The theorem aligns a maximum common model-preserving deletion at the deficient
singleton and can include any prescribed incident edge which is already
persistent.  Failure of prescribed-edge persistence is the exact unique-
contact statement (1.6).

It does not repair the missing adjacency `B_rB_s`, assign palette colours
to the other branch-set labels, force the two critical-triangle response
families into one Kempe component, upper-bound a returned separator by
seven, or prove `HC_7`.  In particular, the two outer endpoints may lie in
branch sets whose internal geometry prevents a clean first-hit transfer.
The dense alternative is now confined to degree eight.  The possible
degree-eight contact multiplicities, and in particular their remaining
label-allocation obstruction, are not resolved here.

## 4. Dependencies

- The labelled-model definitions used in
  [rooted incident-edge persistence](../results/hc7_rooted_persistent_model_edge.md).
- [Bichromatic saturation or bypass](../results/hc7_shared_interface_bichromatic_bypass.md).
- [Colouring fork for a jointly persistent incident pair](../results/hc7_joint_persistent_incident_colour_fork.md).
- [Persistent support-class refinement](../results/hc7_persistent_support_class_refinement.md),
  for the complete-graph-minus-matching minor constructions.
