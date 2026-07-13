# Minor-normalizing an arbitrary `K_7^vee` model

## 0. Spanningness costs nothing in a connected host

### Lemma 0.1 (spanning extension of a minor model)

Let `G` be connected and let `M_1,...,M_s` be the branch sets of any
minor model in `G`.  The branch sets can be enlarged, without changing
their labels or losing any model adjacency, so that they partition
`V(G)`.

#### Proof

Put `U=union_i M_i`.  Every component `C` of `G-U` has an edge to `U`:
otherwise `C` would be a component of the connected graph `G` disjoint
from the nonempty set `U`.  Choose one edge from `C` to a branch set
`M_i` and replace `M_i` by `M_i union C`.  This set is connected, remains
disjoint from all other branch sets, and retains every old model edge.
Doing this independently for all components of `G-U` gives the required
spanning model.  QED.

Consequently Theorem 1.1 below applies to an arbitrary `K_7^vee` minor
in a connected graph.  In particular, it applies to the near-clique
minor supplied in a hypothetical minor-minimal counterexample to
`HC_7`; no additional spanning-model theorem is needed.

## 1. The weakest unconditional normalization

Write `K_7^vee` for `K_7` with the two incident edges `ab,ac`
deleted.  Its other four vertices will be called neutral.

### Theorem 1.1 (one-complex-bag `Q`-full normalization)

Let `G` contain a spanning `K_7^vee` model with branch sets

\[
 A,B,C,U_1,U_2,U_3,U_4,                         \tag{1.1}
\]

where the only adjacencies not required by the model are `AB` and `AC`.
Fix any `j in {1,2,3,4}` and put

\[
 Q_j=\{U_i:i\ne j\}.
\]

Choose any retained label

\[
 X\in\{A,B,C,U_j\}.                               \tag{1.2}
\]

There is a minor `G_{j,X}` of `G` with the
following properties.

1. Six model bags are literal singletons

   \[
       r_1,r_2,r_3,q_1,q_2,q_3,                   \tag{1.3}
   \]

   where the three `q_i` are the images of `Q_j` and the three `r_i`
   are the other labels in `{A,B,C,U_j}-{X}`.
2. `Q_j={q_1,q_2,q_3}` is a triangle, and each of `r_1,r_2,r_3` is adjacent
   to every member of `Q_j`.
3. The vertices not in the six singleton bags induce the old connected
   bag `X`; call it `D_{j,X}`.  It is collectively adjacent to every
   member of `Q_j`, so it is `Q_j`-full.  It retains every adjacency to
   the `r_i` required by `K_7^vee`; an adjacency corresponding to `AB` or
   `AC` is not asserted.
4. Partition `D_{j,X}` into the maximum possible number of nonempty
   connected `Q_j`-full sets.  If `R_{j,X}` is the quotient whose other
   three vertices are the singleton `r_i`, then either `G` has a `K_7`
   minor or

   \[
                              R_{j,X}
   \quad\hbox{is `K_4`-minor-free and has treewidth at most two}. \tag{1.4}
   \]

Thus every target-free spanning model gives **sixteen** one-complex
normalizations: four choices of the neutral triangle and four choices of
the retained complementary bag.  In particular every one of the seven
original branch bags is retained, rather than contracted, in at least one
normalization.

#### Proof

Inside each of the six bags other than `X`, contract a spanning tree to
one vertex.  Do not contract an edge of `X`.  Because the original model
is spanning, these are all the vertices of the resulting minor except
those of `D_{j,X}=X`.

Every required model adjacency survives contraction.  The three selected
neutral vertices therefore form the triangle `Q_j`; the images `r_i`
are literal common neighbours of it; and `D_{j,X}` remains connected and
collectively adjacent to `Q_j`.  Every other required model adjacency is
also retained.  This proves items 1--3.  Extra edges corresponding to
`AB` or `AC`, if present in the original model, only help and need not be
deleted.

The one-part partition `{D_{j,X}}` is `Q_j`-full, so a partition with the
maximum number of parts exists.  Apply the `Q`-full quotient lifting
theorem in `hadwiger_q_full_quotient_rooted_k4.md`.  A `K_4` minor in
`R_{j,X}` lifts to four disjoint pairwise adjacent connected sets, each
adjacent to all of `Q_j`; the three singleton bags of `Q_j` complete a
`K_7` model in `G_{j,X}`, and hence in `G`.  If no such target exists,
`R_{j,X}` is `K_4`-minor-free.  The standard characterization of
`K_4`-minor-free graphs makes it a partial 2-tree.  QED.

### Corollary 1.2 (exact normalized obstruction)

In the target-free branch, every part of the maximal partition of
`D_{j,X}`
is `Q_j`-indecomposable: it cannot be partitioned into two nonempty
connected `Q_j`-full sets.  Moreover every 3-connected block of
`R_{j,X}` of order at least four is absent; equivalently, its
triconnected torsos are only triangular.  Any nontrivial normalization residue is therefore assembled
through one- or two-vertex quotient adhesions containing at least one
`Q_j`-indecomposable carrier.

The conclusion is simultaneous as a family of sixteen statements, but
the minors `G_{j,X}` are different contractions.  Their quotient cuts cannot
be identified or spliced without transporting the contraction maps and
their six-colour operation signatures.

## 2. Why this is not yet the original-graph normalization

The six vertices in (1.3) are literal in the normalized **minor**, not
necessarily literal singleton branch sets of the original graph.  A
branch bag may use different vertices as its indispensable portals to
different model neighbours.  Contracting the bag coalesces those portals;
shrinking it inside `G` need not preserve the model.

This is a real obstruction, not a notational issue.  A subdivision of
`K_7^vee` has a spanning `K_7^vee` model, but its model adjacencies run
through distinct subdivided edge paths.  No choice of the seven original
branch vertices gives the literal near-clique edges before contractions.
Seven-connectivity rules out this thin example, but connectivity alone
does not identify one vertex in each branch bag incident with all required
portal classes.

The sharp high-connectivity warning is the spanning `K_7^-` model in
`K_2` joined with the icosahedron, recorded in
`hadwiger_near_k7_split_round.md`.  It is seven-connected, has minimum
degree seven and no `K_7` minor, yet its essential portal contacts are
distributed across a large branch bag and no connectivity-only split can
repair the deficient pair.  It is two-apex rather than contraction-critical,
which identifies the extra alternatives a valid normalization theorem
must retain.

## 3. Portal-tree normal form for a failed literal shrink

The following elementary certificate describes exactly what prevents a
selected model bag from becoming a singleton in the original graph.

### Lemma 3.1 (essential-leaf portal tree)

Let `X` be a branch set of a minor model and let `Lambda` be the set of
model-neighbour labels whose adjacencies must be retained.  Choose a
connected subgraph `T subseteq G[X]` which meets at least one portal edge
to every label in `Lambda`, first minimizing `|V(T)|` and then deleting
cycle edges.  Then `T` is a tree, and every leaf of `T` is the unique
vertex of `T` meeting the portal class of at least one label in `Lambda`.
Consequently `T` has at most `|Lambda|` leaves.

#### Proof

A minimal connected subgraph contains no cycle.  If a leaf `x` were not
the unique `T`-portal for any required label, deleting `x` would leave a
connected subgraph meeting every required portal class, contrary to the
choice of `T`.  Assign one witnessed label to each leaf.  One label cannot
witness two leaves, because then neither would be its unique portal.
QED.

For a shell bag in (1.1), `|Lambda|<=6`.  Hence failure of literal
normalization is witnessed by a bounded-leaf, but potentially arbitrarily
long, tree whose leaves carry distinct irreplaceable model labels.  This
is the **distributed portal-tree architecture**.  It is the correct
object for a splitter theorem; the mere number of contacts is already
exhausted.

## 4. Exact remaining Gate A

Theorem 1.1 completes normalization at the level of minors and proves
that every target-free normalized quotient is series-parallel.  What is
still missing for `HC_7` is the boundary-faithful lift:

> Given the sixteen maximal partial-2-tree quotients `R_{j,X}`, either
> split an
> essential portal tree in the original spanning model, identify the same
> faithful six-colour state on opposite sides of a one/two-carrier
> adhesion, or realign the model around one globally coherent apex pair.

A quotient separator of order at most two may lift to one or two entire
branch carriers of unbounded order.  It is therefore not an actual cut of
order at most six in `G`.  Contraction-criticality and the labelled
operation signatures must enter precisely at this lift; neither the
unrooted near-clique model nor seven-connectivity alone completes it.

## 5. Colour-state correction: sixteen structures, seven minors

The number sixteen in Theorem 1.1 counts structural `Q`-full views, not
independent colour minors.  For fixed retained label `X in {A,B,C}`, the
four choices of the omitted neutral label contract exactly the same six
bags and produce the same retained-bag minor; only the designation of the
triangle `Q_j` changes.  Together with the four neutral retained-bag
minors, there are only

\[
                 3+4=7
\]

underlying colour minors.

A retained-`X` minor is proper exactly when at least one nonretained bag
is nonsingleton.  Hence all sixteen structural views are proper if and
only if at least two original bags are nonsingleton.  If there is a unique
complex bag `Z`, the structural views retaining `Z` equal `G` and have no
six-colouring in a minimal counterexample; all other retained-bag views
are proper.

The exact singleton equality states and the sharp failure of an
equality-only Helly argument are proved in
`hadwiger_seven_view_state_cocycle_exchange.md`.  In particular, a
`K_7`-minor-free leaf expansion realizes independent `AB/AC` choices in
the four neutral views.  Thus the sixteen structural quotient cuts remain
useful, but colour transport between them must retain portal-labelled
operation data; one must not count them as sixteen independent colour
witnesses.

### Proper-view count

The sixteen views are always minors, but a view need not be a **proper**
minor.  The exact exception is useful and should not be hidden.

### Lemma 5.1 (proper-view count)

Call an original branch bag complex when it has at least two vertices.

1. If at least two branch bags are complex, all sixteen normalization
   views are proper minors.
2. If exactly one bag is complex, precisely the views which retain that
   bag can fail to be proper.  There are four such views when the bag is
   one of `A,B,C`, and one such view when it is neutral.  Thus at least
   twelve of the sixteen views are proper.
3. A non-six-colourable target-free graph cannot have all seven bags
   singleton.

#### Proof

A view contracts all six bags other than its retained bag.  Contracting
a connected bag of order at least two contracts an actual edge and makes
the view proper.  This proves the first two assertions and the stated
counts from the list of retained labels in Theorem 1.1.

If every bag is singleton, spanningness says that `G` has seven vertices.
The required edges give `K_7^vee`.  If both deficient edges are also
present, `G` contains `K_7`; otherwise `G` is a subgraph of `K_7` with an
edge missing and is six-colourable.  QED.

Hence a six-minor-critical counterexample supplies six-colour states on
every proper retained-bag minor.  The sixteen structural designations may
reuse those seven underlying colourings and must not be treated as
independent witnesses.  A state-exchange proof must use only proper views
or handle the one-complex-bag architecture separately.

## 6. The central deficient bag cannot be the sole complex bag

The following standard extension observation closes one of those
one-complex outcomes uniformly.

### Lemma 6.1 (clique extension in a connected host)

Let `k>=2`, and use the standard convention that a `k`-connected graph
has at least `k+1` vertices.  Every `k`-connected graph containing a
`K_{k-1}` subgraph contains a `K_k` minor.

#### Proof

Let `S` be the `(k-1)`-clique and put `D=G-S`.  The order convention and
`k`-connectivity make `D` nonempty and connected.  For each `s in S`, the
graph `G-(S-{s})` is connected, so `s` has a neighbour in `D`.  Thus the
connected bag `D` is adjacent to every singleton bag in `S`, and these
`k` bags form a `K_k` model.
QED.

### Corollary 6.2 (one-complex deficient-centre closure)

In a seven-connected target-free spanning `K_7^vee` model, the deficient
bag `A` cannot be the only complex bag.  Indeed the other six singleton
bags `B,C,U_1,...,U_4` induce `K_6`, so Lemma 6.1 gives `K_7`.

Therefore the nonproper-view exception in Lemma 5.1 is narrower than its
raw count suggests: in a hypothetical counterexample with exactly one
complex branch bag, that bag must be either `B` or `C` (an unaffected bag
in the resulting `K_7^-` view), or one of the four neutral bags.  The former
is the sharp one-complex `K_7^-`/two-apex architecture; the latter is the
one-complex `K_7^vee` portal-splitting architecture.
