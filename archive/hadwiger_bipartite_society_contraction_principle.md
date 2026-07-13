# The bipartite-society contraction principle

## Status

This note extends the one-edge contraction programme to every connected
induced bipartite society.  In a proper-minor-minimal counterexample at the
least failing Hadwiger parameter, contracting any such society is tight:
it has chromatic and Hadwiger number exactly one below the counterexample.
Consequently every induced path or tree can be placed wholly inside one
branch set of a `K_{k-1}`-model.

After minimizing that society-rooted bag, the uniform warehouse theorem
applies verbatim.  Every hanging piece monopolizes at least two labels not
contacted directly by the society.  It is either charged by an actual
society edge or lies behind a full adhesion; across the adhesion, the
society-contraction states and all opposite proper-minor states are
disjoint.  One reference colouring also gives a simultaneous saturation
certificate on both bipartition shores.

If the society has at most one direct model defect, that defect also has
two distinct root-bag portals.  Hence every model label participates in one
common all-label portal system: a common tree edge gives the target clique
minor outright, and otherwise only the disjoint-pair and three-arm frames
remain.

This is a uniform rooted-model principle.  It does not prove that the
society bag splits into the two additional branch sets needed for a target
clique minor.

## 1. Every bipartite society contraction is chromatically tight

Let `G` be proper-minor-minimal subject to not being `(k-1)`-colourable.
Thus `chi(G)=k` and every proper minor is `(k-1)`-colourable.  Let
`S subseteq V(G)` have at least two vertices and suppose that `G[S]` is
connected and bipartite, with fixed bipartition

\[
                              S=A\mathbin{\dot\cup}B.     \tag{1.1}
\]

Contract `S` to one vertex `z`, deleting loops and parallel edges, and
write `H=G/S`.

### Theorem 1.1 (bipartite contraction equality)

One has

\[
                              \chi(G/S)=k-1.              \tag{1.2}
\]

#### Proof

The contraction is proper, so minimality gives `chi(G/S)<=k-1`.
Suppose that `G/S` has a `(k-2)`-colouring `c`, and put `c(z)=alpha`.
Every external neighbour of `S` becomes adjacent to `z`; hence none has
colour `alpha`.

Introduce one fresh colour `beta`.  Keep `c` outside `S`, colour every
vertex of `A` with `alpha`, and every vertex of `B` with `beta`.  Edges
inside `S` cross its bipartition.  External edges at `A` avoid `alpha`,
and the old colouring uses no `beta` at all.  This is a proper
`(k-1)`-colouring of `G`, a contradiction.  QED.

Connectedness is what makes identifying `S` a legitimate connected-branch
contraction and hence a graph minor.  Bipartiteness is what makes the
two-colour expansion valid.  (The colouring argument by itself would also
work for a disconnected induced bipartite set, but that identification is
not a minor operation.)

### Theorem 1.2 (two-shore saturation in one reference colouring)

Let `c` be any `(k-1)`-colouring of `G/S`, and put `c(z)=alpha`.  For every
colour `beta ne alpha`, each bipartition shore has an external neighbour of
colour `beta`:

\[
 \begin{aligned}
   &E_G(A,c^{-1}(\beta)-S)\ne\varnothing,\\
   &E_G(B,c^{-1}(\beta)-S)\ne\varnothing.                \tag{1.3}
 \end{aligned}
\]

In particular, each shore has at least `k-2` distinct external neighbours,
while every external neighbour of `S` avoids `alpha`.

#### Proof

The last assertion follows from the edge to `z` after contraction.  If,
say, `B` had no external neighbour of colour `beta`, keep `c` outside `S`,
colour `A` with `alpha`, and colour `B` with `beta`.  This is a proper
`(k-1)`-colouring of `G`, contrary to the choice of `G`.  Interchanging
`A,B` proves the other assertion.  Distinct colours require distinct
neighbour vertices.  QED.

For `S=\{x,y\}` this is exactly the familiar fact that both ends of a
contracted edge see every colour other than their common contraction
colour.  Theorem 1.2 shows that endpoint saturation was the first member of
a society-wide phenomenon, not an isolated edge trick.

## 2. Hadwiger equality and a model containing the whole society

Now assume that `k` is the least parameter for which Hadwiger's conjecture
fails and that `G` is a proper-minor-minimal counterexample at parameter
`k`.  Hadwiger's conjecture holds at parameter `k-1`.  Theorem 1.1 gives

\[
                              \chi(G/S)=k-1.              \tag{2.1}
\]

Hence `G/S` contains a `K_{k-1}` minor.  It cannot contain a `K_k` minor,
since minors lift through contraction and `G` is `K_k`-minor-free.  Thus

\[
                        \eta(G/S)=\chi(G/S)=k-1.          \tag{2.2}
\]

### Theorem 2.1 (society-rooted clique model)

There is a `K_{k-1}`-model in `G/S` whose union contains `z`.  Expanding
the z-bag gives a `K_{k-1}`-model in `G` with the whole vertex set `S`
contained in one branch bag.

#### Proof

Start with any `K_{k-1}`-model in `G/S`.  If `z` is outside its union,
adjoin a shortest path from `z` to the union to the first bag it meets.
The path has no internal vertex in another bag, so all model properties are
preserved.

Let `T` be the bag now containing `z`.  Its preimage

\[
                              \widehat T=(T-\{z\})\cup S  \tag{2.3}
\]

is connected: all incidences at `z` lift to vertices of the connected set
`S`.  Every other bag and every model adjacency lifts unchanged.  QED.

### Corollary 2.2 (every induced path or tree lies in a tight model bag)

Every vertex set inducing a nontrivial path or tree in `G` is contained in
one branch set of some `K_{k-1}`-model of `G`.

This is existential and model-dependent: models obtained from different
societies need not have compatible external bags.

### Corollary 2.3 (uniform two-root co-location)

For every two distinct vertices `p,q in V(G)`, there is a
`K_{k-1}`-model of `G` having one branch set which contains both `p` and
`q`.

#### Proof

Proper-minor minimality makes `G` connected: otherwise all of its proper
components would be `(k-1)`-colourable and their colourings could be
combined.  Take a shortest `p-q` path.  It is induced and bipartite, so Corollary 2.2
places its whole vertex set, and hence both prescribed roots, in one branch
bag.  QED.

The conclusion is co-location, not a model with `p,q` in two prescribed
distinct bags.  It therefore does not itself supply the extra branch set
needed for a `K_k` minor.

### Theorem 2.4 (a maximal society double-contacts every boundary vertex)

Choose `S=A dotcup B` inclusion-maximal among vertex sets inducing a
nontrivial connected bipartite subgraph of `G`.  Every vertex
`w in V(G)-S` which has a neighbour in `S` has neighbours in both shores:

\[
                         N_G(w)\cap A\ne\varnothing,
                         \qquad N_G(w)\cap B\ne\varnothing. \tag{2.4}
\]

#### Proof

If all neighbours of `w` in `S` lay in `A`, then adjoining `w` to `B`
would leave the induced graph connected and bipartite.  This contradicts
maximality.  The case in which all such neighbours lie in `B` is symmetric.
QED.

### Corollary 2.5 (direct model labels are bi-supported)

Use a society-rooted model (3.1) for a maximal society.  If
`E_G(S,C_i)` is nonempty, then both `A` and `B` are adjacent to `C_i`.

#### Proof

Take the endpoint `w in C_i` of an `S-C_i` edge.  It lies outside `S`, so
Theorem 2.4 gives one neighbour in each shore.  QED.

Thus every label outside the defect set `Delta_S` of (3.4) already has two
literal society contacts, one on each bipartition shore.  The warehouse
theorem below says that the remaining labels occur in charges of order at
least two.  This is genuine colour-to-model contact alignment.

It still does not make `A` and `B` branch sets: the two independent shores
may be disconnected.  For each direct label one may select a portal pair
`a_i in A,b_i in B` with a common neighbour in `C_i`.  A connected
two-piece split of the expanded society bag which
separates every selected pair automatically retains all direct labels on
both sides.  The unresolved geometric problem is a connected
pair-separating split, together with retention of the warehouse labels in
`Delta_S`.

## 3. Minimum society bag and multi-label warehouses

Write a z-rooted model in `G/S` as

\[
                         (T,C_1,\ldots,C_{k-2}),          \tag{3.1}
\]

and choose one minimizing `|T|` among all z-rooted models.  For a nonempty
set `X subseteq T-{z}` such that both `X` and `T-X` induce connected
subgraphs, put

\[
 \Lambda_T(X)=
   \{i:E_{G/S}(T-X,C_i)=\varnothing\}.                  \tag{3.2}
\]

### Theorem 3.1 (society-bag warehouse theorem)

Every such detachable set satisfies

\[
                             |\Lambda_T(X)|\ge2.          \tag{3.3}
\]

Moreover,

\[
 \Lambda_T(X)\subseteq
 \Delta_S:=\{i:E_G(S,C_i)=\varnothing\}.                \tag{3.4}
\]

#### Proof

If the monopoly set is empty, delete `X` from the root bag.  The connected
set `T-X` retains every labelled adjacency, contradicting minimality.

If `Lambda_T(X)={j}`, all old `T-C_j` contacts have their `T` endpoint in
`X`.  Replace

\[
             T\longmapsto T-X,qquad C_j\longmapsto C_j\cup X. \tag{3.5}
\]

The enlarged `j`-bag is connected, it sees `T-X` through the
`X-(T-X)` edge, and all other bag pairs retain old clique-model edges.
This is a smaller z-rooted model, again a contradiction.

Finally, an edge from `S` to `C_i` becomes an edge `z-C_i` in `G/S`.
Since `z in T-X`, such a label cannot be monopolized by `X`.  This proves
(3.4).  QED.

Root the block--cutvertex tree of `(G/S)[T]` at `z`.  Exactly as in the
one-edge theorem, every non-root lobe is detachable.  Inclusion-minimal
lobes are disjoint, and their monopoly sets are pairwise disjoint: the
nonempty set of all `T` endpoints of `T-C_i` edges cannot lie in two
disjoint lobes.  Therefore:

### Corollary 3.2 (uniform warehouse count)

The number of inclusion-minimal society-bag warehouse lobes is at most

\[
                         \left\lfloor {|\Delta_S|\over2}\right\rfloor
                         \le \left\lfloor{k-2\over2}\right\rfloor. \tag{3.6}
\]

If `|Delta_S|<=1`, the minimized society bag has no non-root block lobe.

### Lemma 3.3 (a lone defect has two distinct root-bag portals)

For a model label `i`, put

\[
 P_i(T)=\{t\in T:E_{G/S}(\{t\},C_i)\ne\varnothing\}. \tag{3.7}
\]

If `|Delta_S|<=1`, then every defect label `i in Delta_S` satisfies

\[
                              |P_i(T)|\ge2.              \tag{3.8}
\]

#### Proof

The set `P_i(T)` is nonempty because `T` and `C_i` are adjacent model
bags.  Since `i` is a society defect, `z notin P_i(T)`.

Suppose that `P_i(T)={q}`.  In the connected graph `(G/S)[T]-q`, let `K`
be the component containing `z`, and put

\[
                              X=T-K.                    \tag{3.9}
\]

The set `X` contains `q`.  It is connected: every component of `T-q`
other than `K` has an edge to `q`, since `T` is connected.  Its complement
`T-X=K` is connected and contains `z`.  Thus `X` is z-detachable.
Moreover, every `T-C_i` edge has its `T` endpoint at `q`, so
`i in Lambda_T(X)`.  Theorem 3.1 gives

\[
                 2\le |\Lambda_T(X)|,
                 \qquad \Lambda_T(X)\subseteq\Delta_S. \tag{3.10}
\]

This is impossible when `|Delta_S|<=1`.  QED.

After expansion, the vertices of `P_i(T)` are unchanged (none is `z`),
so (3.8) gives two distinct portals of the expanded bag to every lone
defect label.  Every direct label already has the two distinct society
portals in (4.3).  Consequently:

### Corollary 3.4 (two portals for every label at defect order at most one)

If `|Delta_S|<=1`, every external model bag has two distinct neighbours
in the expanded root bag `widehat T`.  Direct labels may be represented by
one portal in each society shore; the possible defect label may be
represented by any two distinct vertices of `P_i(T)`.

## 4. Expansion and the still-missing split

Expand `T` to `widehat T` as in (2.3).  Any bipartition

\[
                 \widehat T=X\mathbin{\dot\cup}Y         \tag{4.1}
\]

into nonempty connected adjacent sets for which both sides meet every
external bag `C_i` produces the `K_k`-model

\[
                           X,Y,C_1,\ldots,C_{k-2}.        \tag{4.2}
\]

Such connected adjacent splits always exist geometrically: take any edge
of a spanning tree of `G[widehat T]` and delete it.  If one wants to
separate the ends of a prescribed edge of `G[S]`, choose a spanning tree
containing that edge and delete it.  The unresolved issue is simultaneous
retention of all `k-2` named model labels.

The bipartition `(A,B)` of the society itself generally does not give (4.1):
each shore may be disconnected, and the vertices of `T-{z}` still have to
be assigned.  Theorem 1.2 is a colour-capacity statement, not permission to
treat the two independent shores as connected branch sets.

For a maximal society, Corollary 2.5 gives more.  For every direct label
`i notin Delta_S`, fix a common external neighbour `w_i in C_i` and portal
endpoints

\[
                         a_i\in A\cap N(w_i),\qquad
                         b_i\in B\cap N(w_i).             \tag{4.3}
\]

Let `F` be any spanning tree of `G[widehat T]`, and let `P_i` be the unique
`a_i-b_i` path in `F`.

### Theorem 4.1 (common split edge or a finite portal frame)

The following priority procedure yields one of the three outcomes for the
family `{P_i:i notin Delta_S}`: first test outcome 1, then outcome 2, and
otherwise obtain outcome 3.

1. **Common split edge.**  Some edge `f in E(F)` belongs to every `P_i`.
   The two components of `F-f` give a connected adjacent split of
   `widehat T` which retains every direct label on both sides.
2. **Disjoint pair frame.**  Two named portal paths are edge-disjoint.
3. **Three-arm frame.**  There are three named portal paths and a vertex
   `q in V(F)` with three distinct incident edges `e_1,e_2,e_3` such that,
   locally at `q`, the three paths use respectively

   \[
                         \{e_1,e_2\},\quad
                         \{e_2,e_3\},\quad
                         \{e_1,e_3\}.                    \tag{4.4}
   \]

#### Proof

If the paths have a common edge, delete it.  A portal pair is separated
precisely because its tree path uses the deleted edge.  Each component is
connected, the deleted edge makes them adjacent, and the two endpoints in
(4.3) supply one edge from each component to `C_i`.

Suppose there is no common edge.  If two paths are edge-disjoint, outcome 2
holds.  Otherwise the paths are pairwise edge-intersecting.  Paths are
subtrees of a tree, so the vertex-Helly property gives a common vertex `q`.
For each path record the one or two incident edges which it uses at `q`.
These sets have order at most two and are pairwise intersecting: an edge
intersection in one branch at `q` forces both paths to use that branch's
first edge.  Their total intersection is empty, since a common incident
edge would be a common edge of all the paths.

A pairwise-intersecting family of subsets of order at most two with empty
total intersection has no singleton and contains the three two-sets on
three elements.  These are exactly (4.4).  QED.

### Corollary 4.2 (directly complete societies reduce to two frames)

If `Delta_S` is empty, outcome 1 of Theorem 4.1 gives a `K_k` minor through
(4.2).  Consequently, in a `K_k`-minor-free counterexample, every spanning
tree and every selected direct-portal-pair system has either a disjoint pair
frame or a three-arm frame.

If `Delta_S` is nonempty, the common-edge split still settles every direct
label simultaneously; only the multi-label warehouse charges from Theorem
3.1 remain to be retained.  Thus the infinite tree geometry has been
reduced to two finite frame types plus the already named defect set.

### Corollary 4.3 (all-label frame reduction with at most one defect)

Assume `|Delta_S|<=1`.  For every direct label choose the portal pair
`a_i,b_i` from (4.3), and for the possible defect label choose two portals
given by Lemma 3.3.  In any spanning tree `F` of `G[widehat T]`, let `P_i`
be the tree path joining the selected portals of label `i`.

Then one of the following holds:

1. deleting a common edge of all the `P_i` gives the split (4.1), and
   hence the explicit `K_k`-model (4.2); or
2. two of the all-label portal paths are edge-disjoint; or
3. three of them form the three-arm frame (4.4).

In particular, in a `K_k`-minor-free graph only outcomes 2 and 3 can
occur.  Thus when `|Delta_S|<=1` the defect is not an additional warehouse
residue: it participates in the same two finite tree frames as every
direct label.

#### Proof

Corollary 3.4 supplies a distinct portal pair for every label.  Apply the
pure tree argument of Theorem 4.1 to the resulting family of paths.  If
they have a common edge, the two components of `F-f` are connected and
adjacent, and each contains one portal to every external bag.  These
components together with `C_1,...,C_{k-2}` are exactly the model (4.2).
The other two outcomes are the remaining alternatives in Theorem 4.1.
QED.

The possible defect pair need not lie in `S`.  Therefore its appearance in
a frame authorizes the static all-label reduction above, but not an
automatic society contraction of every subpath of its tree path.  Any
dynamic use of such a subpath must instead choose an induced path or an
edge operation explicitly.

## 5. Society charge or a full adhesion

Let `K` be a rooted lobe of the minimized z-bag `T`.  It avoids `z` and
therefore denotes the same vertex set in `G`.

### Theorem 5.1 (society charge--adhesion dichotomy)

If `G` is `s`-connected, then either

1. **society charge:** `E_G(K,S)` is nonempty; or
2. **full adhesion:** there is an inclusion-minimal `K-S` separator `Z`,
   disjoint from both connected sets, with

   \[
                              |Z|\ge s,                  \tag{5.1}
   \]

   and the components `R_K,R_S` of `G-Z` containing `K,S` satisfy

   \[
                         N_G(R_K)=Z=N_G(R_S).             \tag{5.2}
   \]

#### Proof

If there is no society charge, the open neighbourhood of `K` separates it
from the connected set `S`.  Choose an inclusion-minimal separator.  Its
order is at least `s` by connectivity.  Restoring any one separator vertex
creates a `K-S` path through it, so every separator vertex has a neighbour
in both distinguished components.  The reverse containments in (5.2) are
automatic for components of `G-Z`.  QED.

Thus a society simultaneously charges all warehouses which touch it.  A
noncharged warehouse is not merely hidden behind a cut in the model bag;
it lies behind a genuine ambient full adhesion.

## 6. Society reference states are crossed-state codes

Let `r=k-1`.  In the full-adhesion outcome, take

\[
       P=R_K\cup Z,qquad Q=V(G)-R_K,qquad P\cap Q=Z.   \tag{6.1}
\]

Then `K subseteq P-Z` and `S subseteq Q-Z`.  Let `Sigma_S(Z)` be the set
of equality partitions on `Z` induced by all `r`-colourings of `G/S`.
Let `Sigma_K(Z)` be the union of the partitions induced by all
`r`-colourings of proper minors whose nontrivial operations are supported
in `P-Z` and which retain the closed `Q`-shore literally.

### Theorem 6.1 (society/warehouse state disjointness)

One has

\[
                         \Sigma_S(Z)\cap\Sigma_K(Z)=\varnothing. \tag{6.2}
\]

#### Proof

The contraction branch set `S` lies wholly in `Q-Z`, so `G/S` retains the
closed `P`-shore literally.  Every warehouse-side minor retains the closed
`Q`-shore.  If two colourings induced the same equality partition on `Z`,
permute one palette to make the restrictions agree, take the `G/S`
colouring on `P`, and take the warehouse-minor colouring on `Q-Z`.  Each
original closed shore is coloured faithfully, and no edge joins the two
open shores.  This gives an `r`-colouring of `G`, a contradiction.  QED.

The same proof gives a useful symmetric form.

### Theorem 6.2 (opposite bipartite societies have disjoint states)

Let `(P,Q)` be any separation of `G` with boundary `Z`.  Let
`S_P subseteq P-Z` and `S_Q subseteq Q-Z` induce nontrivial connected
bipartite graphs.  Then the equality-partition sets on `Z` arising from
`r`-colourings of `G/S_P` and `G/S_Q` are disjoint.

Every society contraction is tight by Theorem 1.1, and at the least failing
parameter each also carries a society-rooted `K_{k-1}`-model by Theorem
2.1.  Thus (6.2) is a code on a large family of rooted models, not just on
unrelated deletion colourings.

## 7. Quantitative consequences and exact boundary

For every nontrivial induced tree or path `S`, the proved package supplies:

1. a tight society-rooted `K_{k-1}`-model;
2. two bipartition shores which, in every contraction colouring, each see
   all `k-2` noncontraction colours;
3. for a maximal society, literal bi-support of every direct model label
   and a common-edge split or one of two finite portal frames;
4. at most `floor(|Delta_S|/2)` minimal off-root warehouse lobes;
5. a society charge or a full adhesion of order at least `kappa(G)` at
   every warehouse; and
6. disjoint reference/warehouse state sets at every full adhesion.

For `k=7`, every society contraction has a rooted `K_6`-model, every shore
sees five distinct noncontraction colours, there are at most two minimal
warehouse lobes, and every noncharged warehouse lies behind an adhesion of
order at least seven.

The missing implication is precise.  Colour saturation does not identify
the colour witnesses with the fixed external model labels; a society shore
need not be connected; charged warehouses may concentrate several labels
behind one attachment; and disjoint state sets do not force a common state.
A completion needs a society split/ear exchange which converts the two
saturated shores into connected label-preserving branch sets, or else
forces two opposite society contractions to realize the same full-adhesion
partition.  None of those conclusions is assumed here.
