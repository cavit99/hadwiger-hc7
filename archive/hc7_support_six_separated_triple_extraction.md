# Separated triples of six-vertex `K_5`-model supports

**Status:** proved draft awaiting independent audit.  This is a global
set-system extraction theorem for exact six-vertex model supports.  It does
not yet compose the extracted three models into a `K_7` or a common
two-vertex transversal.

## 1. Model-support family

For a graph `G`, let `S_6(G)` be the family of six-element sets `X` for
which `G[X]` contains a `K_5` model whose five branch sets have union
exactly `X`.  Necessarily its bag-size multiset is

\[
                         (2,1,1,1,1).                  \tag{1.1}
\]

Write `tau(S_6(G))` for the minimum order of a vertex set meeting every
member of this family.

## 2. An elementary six-uniform dichotomy

### Lemma 2.1 (separated triple or two tight clusters)

Let `F` be a family of six-element sets with `tau(F)>2`.  Then at least one
of the following holds.

1. There are `A_1,A_2,A_3 in F` such that

   \[
                   |A_i\cap A_j|\le4
                     \qquad(1\le i<j\le3).             \tag{2.1}
   \]
2. The family is the disjoint union `F=F_A dotunion F_B`, where every two
   members of each `F_A,F_B` intersect in at least five elements.  At least
   one of these two subfamilies consists of all seven six-subsets of one
   fixed seven-element set.

#### Proof

First record the elementary classification of a pairwise five-intersecting
six-uniform family `C`.  Fix distinct `A,B in C` and write

\[
                         B=A-\{a\}+\{b\},\qquad b\notin A. \tag{2.2}
\]

Every other member differing from `A` has the form
`A-{c}+{d}`.  Two such sets have intersection only four if both their
removed elements and their added elements differ.  Relative to the fixed
set `B`, every member must therefore either remove `a` or add `b`.  A
member of the first kind which adds a value other than `b` and a member of
the second kind which removes a value other than `a` would themselves
intersect in only four elements.  Hence one of the two alternatives holds
for the whole family: all members contain the same five-set `A-{a}`, or
all are contained in the same seven-set `A union {b}`.  The first family
has a common vertex;
the second is met by any two vertices of that seven-set.  Therefore

\[
            \text{pairwise five-intersecting and six-uniform}
                     \quad\Longrightarrow\quad \tau(C)\le2. \tag{2.3}
\]

Now suppose outcome 1 fails.  Formula (2.3) and `tau(F)>2` give sets
`A,B in F` with `|A intersect B|<=4`.  Every `C in F` satisfies

\[
                  |C\cap A|\ge5\quad\hbox{or}\quad|C\cap B|\ge5, \tag{2.4}
\]

for otherwise `A,B,C` would satisfy (2.1).

If `A intersect B` contained two vertices, that pair would meet every set
in (2.4), contradicting `tau(F)>2`.  Hence

\[
                             |A\cap B|\le1.             \tag{2.5}
\]

Let `F_A` and `F_B` consist of the sets satisfying the first and second
inequalities in (2.4), respectively.  They cover `F`.  They are disjoint:
a six-set containing five elements of each of `A,B` would force
`|A intersect B|>=4`, contrary to (2.5).

Each subfamily is pairwise five-intersecting.  Indeed, if
`C,D in F_A` had intersection at most four, then (2.5) and
`|C intersect A|,|D intersect A|>=5` would give

\[
                         |B\cap C|,|B\cap D|\le2.
\]

The triple `B,C,D` would satisfy (2.1), contrary to the standing
assumption.  The proof for `F_B` is symmetric.

Apply the classification preceding (2.3) to both clusters.  If both had a
common vertex, one vertex from each would form a two-element transversal
of `F`.  Thus one cluster has empty total intersection.  It cannot be of
the common-five-set type.  In the seven-set type, a proper subfamily of the
seven possible six-subsets omits fewer than all seven vertices and hence
has nonempty total intersection.  Therefore the cluster with empty
intersection consists of all seven six-subsets of its seven-set.  This is
outcome 2.  \(\square\)

## 3. The top cluster is impossible in the target host

### Lemma 3.1 (seven-vertex top closure)

Let `J` be a graph on seven vertices.  Suppose that for every vertex `v`,
the six-set `V(J)-{v}` belongs to `S_6(J)`.  Then `J` contains a spanning
`K_6` model.

#### Proof

Put `F=overline J`.  A spanning `K_5` model on six vertices has four
singleton bags forming a clique and one two-vertex edge-bag.  In the
complement, the four singleton vertices are independent, the two vertices
of the edge-bag are nonadjacent, and no singleton is adjacent to both
edge-bag vertices.  Consequently, for every `v`, the graph `F-v` is the
disjoint union of at most two star components and isolated vertices.

We claim that `F` itself has the same form.  If one of its components were
not a star, that component would contain either a triangle or a path with
three edges.  This witness uses at most four vertices, so deleting one of
the other vertices of the seven-set would leave it in `F-v`, impossible
for a union of stars.  Thus every component of `F` is a star.

If `F` had at least three nontrivial components, choose one edge from each.
Those three independent edges use six vertices.  Deleting the seventh
would leave three nontrivial components in `F-v`, again impossible.
Therefore `F` is the union of at most two star components and isolates.

If there are two nontrivial stars, let `x,y` be their centres.  The
remaining five vertices form a clique in `J`; `xy` is an edge of `J`; and
each remaining vertex is adjacent in `J` to at least one of `x,y`.
Contracting `xy` therefore gives a spanning `K_6` model.

If there is exactly one nontrivial star with centre `x`, it cannot have all
six other vertices as leaves.  Indeed, deleting one leaf would leave in
the complement one star with five leaves.  In the corresponding six-vertex
graph, an edge-bag cannot use the star centre with a leaf because they are
nonadjacent, while an edge-bag using two leaves misses the centre from both
ends.  No spanning `K_5` model would exist, contrary to the hypothesis.
Hence the complement has an isolated vertex `y`.  Use `xy` as the
two-vertex branch set; the other five vertices form a clique and every
leaf of `x` is adjacent in `J` to the isolate `y`.  This again gives a
spanning `K_6` model.  With no nontrivial complement component, `J` is
complete and the conclusion is immediate.  \(\square\)

### Lemma 3.2 (no full top in a seven-connected `K_7`-minor-free graph)

If `G` is seven-connected and has no `K_7` minor, then `S_6(G)` cannot
contain all seven six-subsets of one seven-set `U`.

#### Proof

Lemma 3.1 gives a `K_6` model in `G[U]`.  Since a seven-connected graph has
at least eight vertices, `G-U` is nonempty.

If `G-U` is connected, minimum degree at least seven ensures that every
vertex of `U` has a neighbour in it.  If `G-U` is disconnected, every
component `C` has `N(C) subseteq U`; its neighbourhood separates it from
another component, so seven-connectivity gives `N(C)=U`.  In either case
there is a connected subgraph `C subseteq G-U` adjacent to every vertex of
`U`.

The six branch sets supplied by Lemma 3.1, together with `C`, are seven
pairwise adjacent connected branch sets.  This is a `K_7` model, a
contradiction.  \(\square\)

## 4. Global extraction theorem

### Theorem 4.1 (separated support-six triple)

Let `G` be a seven-connected graph with no `K_7` minor.  If

\[
                            \tau(S_6(G))>2,              \tag{4.1}
\]

then there are three exact six-vertex `K_5`-model supports
`A_1,A_2,A_3` satisfying (2.1).

#### Proof

Apply Lemma 2.1 to `S_6(G)`.  Outcome 2 contains a full seven-set top, and
Lemma 3.2 excludes it.  Hence outcome 1 holds.  \(\square\)

The accompanying exhaustive seven-vertex census is
[`hc7_support_six_top_cluster_probe.py`](hc7_support_six_top_cluster_probe.py).
It finds eleven unlabelled top-cluster hosts; all eleven have the `K_6`
minor proved in Lemma 3.1.  The proof does not depend on that census.

## 5. Exact trust boundary

The theorem concerns the exact-six family `S_6(G)`, not the union of
literal five-vertex and exact six-vertex supports.  The literal family and
`S_6(G)` may each have a two-vertex transversal while their union has none.
Thus Theorem 4.1 does not prove

\[
                           \tau_5^{\le6}(G)\le2.
\]

Nor does three supports satisfying (2.1) automatically give a `K_7`:
the published three-clique theorems apply to literal `K_5` subgraphs, and
the three split edges may overlap other model rows.  The next global step
is therefore either a composition theorem for the separated decorated
triple or a compatibility theorem between a transversal of the literal
family and one of `S_6(G)`.
