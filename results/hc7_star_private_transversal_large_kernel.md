# The five- and six-support star kernels

**Status:** written proof; independently audited in
[`hc7_star_private_transversal_large_kernel_audit.md`](hc7_star_private_transversal_large_kernel_audit.md).
This note works inside the star alternative of the promoted
private-transversal kernel theorem.  It does not prove the two-vertex
transversal theorem or Hadwiger's conjecture for `t=7`.

## 1. Setup

Let `G` be a seven-connected graph with no `K_7` minor, and let

\[
             \mathcal C=\{A_1,\ldots,A_m\}
\]

be as in Theorem 2.1 of
[`../results/hc7_private_transversal_graph_kernel.md`](../results/hc7_private_transversal_graph_kernel.md).
Assume its chosen private transversals form the star

\[
 P_i=\{p,\ell_i\},\qquad
 L=\{\ell_1,\ldots,\ell_m\},                         \tag{1.1}
\]

so that

\[
       p,\ell_i\notin A_i,
       \qquad L-\{\ell_i\}\subseteq A_i.              \tag{1.2}
\]

Every `A_i` is the support of a spanning `K_5` model on six
vertices.  The five-vertex members of the underlying set family are
exactly the vertex sets of literal `K_5` subgraphs.

## 2. Literal cliques in the two largest star kernels

### Lemma 2.1

If `m=6`, every literal `K_5` subgraph of `G` contains `p`.

If `m=5`, every literal `K_5` subgraph either contains `p` or has vertex
set exactly `L`.  In particular, `L` is the only possible literal
`K_5` avoiding `p`.

#### Proof

Let `K` be a literal `K_5` avoiding `p`.  Since every
`P_i={p,ell_i}` meets every literal `K_5`, the set `V(K)` contains every
leaf `ell_i`.  This is impossible when there are six leaves.  When there
are five leaves, it forces `V(K)=L`. \(\square\)

The remainder of Sections 2--3 treats the nontrivial `m=5` subcase in
which `L` is a literal `K_5`.

### Lemma 2.2 (normal form relative to a fixed four-clique)

Let `J` be a graph on six vertices, let `Q` be a literal four-clique in
`J`, and suppose that `J` has a spanning `K_5` model but no literal
`K_5`.  If `V(J)-Q={x,y}`, then

1. `xy` is an edge; and
2. for every `q in Q`, at least one of `qx,qy` is an edge.

Thus `Q` and the edge-bag `{x,y}` are themselves a spanning `K_5`
model in `J`.

#### Proof

Let `{a,b}` be the two-vertex bag of a spanning `K_5` model and let
`R=V(J)-{a,b}` be its four singleton bags.  Thus `R` is a four-clique,
`ab` is an edge, and `{a,b}` is collectively adjacent to every vertex of
`R`.

If `{a,b}={x,y}`, the conclusion is immediate.  Suppose first that the
two pairs are disjoint.  Then `x,y in R`, so `xy` is an edge.  The two
vertices of `Q-R` are `a,b`.  If, say, neither `x` nor `y` were adjacent
to `a`, collective adjacency of the model bag `{a,b}` to each of `x,y`
would make `b` adjacent to both.  Since `b` is also adjacent to the two
vertices of `Q cap R`, the five-set `R union {b}` would be a literal
`K_5`, a contradiction.  Thus each of `a,b` has a neighbour in `{x,y}`.
Together with the clique edges from `x,y` to `Q cap R`, this says exactly
that `{x,y}` is collectively adjacent to `Q`.

It remains that the pairs share one vertex.  Relabel so that
`{a,b}={q,x}`, where `q in Q` and `x notin Q`; write
`V(J)-Q={x,y}`.  Then

\[
                         R=(Q-\{q\})\cup\{y\}.
\]

The clique `R` makes `y` adjacent to every vertex of `Q-{q}`.  The
model makes `y` adjacent to at least one of `q,x`.  If `qy` were an
edge, then `Q union {y}` would be a literal `K_5`, contrary to the
hypothesis.  Hence `xy` is an edge.  Finally `xq` is the model-bag edge,
so the edge `{x,y}` is collectively adjacent to all of `Q`. \(\square\)

### Theorem 2.3 (five-clique star reduction)

Assume `m=5` and `L` is a literal `K_5`.  For every `i` there is an edge

\[
                         e_i=x_i y_i\subseteq G-L       \tag{2.1}
\]

such that

\[
 A_i=(L-\{\ell_i\})\cup\{x_i,y_i\},                   \tag{2.2}
\]

the edge `e_i` is collectively adjacent to every vertex of
`L-{ell_i}`, and `e_i` is anticomplete to `ell_i`.

The five edges `e_1,...,e_5` are distinct and contain two
vertex-disjoint edges.

#### Proof

Equation (1.2), `|A_i|=6`, and `|L|=5` give (2.2) for two vertices
`x_i,y_i` outside `L union {p}`.  The graph `G[A_i]` contains no literal
`K_5`: by Lemma 2.1 such a clique would have to be `L`, but `ell_i` is
not in `A_i`.  Apply Lemma 2.2 to the fixed four-clique
`Q=L-{ell_i}` in `G[A_i]`.  This proves that `e_i=x_i y_i` is an edge
collectively adjacent to `L-{ell_i}`.

If an endpoint of `e_i` were adjacent to `ell_i`, the five singleton
vertices of `L`, together with `e_i` as a sixth branch set, would be a
`K_6` model supported on the seven-set `L union V(e_i)`.  Lemma 4.3 of
[`../results/hc7_support_at_most_six_separated_triple_extraction.md`](../results/hc7_support_at_most_six_separated_triple_extraction.md)
would lift it to a `K_7` minor.  Therefore `e_i` is anticomplete to
`ell_i`.

The edges are distinct.  Indeed, if `e_i=e_j` for distinct `i,j`, then
the common edge is anticomplete to `ell_i` by the preceding paragraph,
but its role as `e_j` makes it collectively adjacent to `ell_i`, since
`i != j`.

Suppose, for a contradiction, that the five distinct edges are pairwise
intersecting.  A pairwise-intersecting family of five distinct edges is a
star, so write

\[
                         e_i=v u_i\qquad(1\le i\le5),   \tag{2.3}
\]

where the `u_i` are distinct.  Since `v` lies in every `e_i` and `e_i`
is anticomplete to `ell_i`, the vertex `v` is anticomplete to `L`.
Consequently (2.3) and the collective adjacency of `e_i` give

\[
        u_i\ell_i\notin E(G),
        \qquad u_i\ell_j\in E(G)\quad(j\ne i).         \tag{2.4}
\]

Put `H=G-L`.  Deleting the five vertices of `L` from a seven-connected
graph leaves a two-connected graph, so `H-v` is connected.  Among all
paths in `H-v` whose distinct ends belong to
`{u_1,...,u_5}`, choose a shortest one, say `P` has ends `u_a,u_b`.
No internal vertex of `P` is another `u_i`, by minimality.

Choose distinct `c,d` outside `{a,b}`.  The two subgraphs

\[
                         P,
             \qquad G[\{u_c,v,u_d\}]                  \tag{2.5}
\]

are connected and vertex-disjoint.  Each is adjacent to every vertex of
`L` by (2.4), and they are adjacent to each other through the edge
`vu_a`.  Together with the five singleton vertices of the clique `L`,
they are the seven branch sets of a `K_7` model.  This contradiction
proves that two of the `e_i` are vertex-disjoint. \(\square\)

### Theorem 2.4 (a second disjoint literal clique)

Under the hypotheses of Theorem 2.3, there is a literal `K_5` subgraph
vertex-disjoint from `L`.  It may be written

\[
                         X\cup\{w\},                   \tag{2.6}
\]

where `X` is a four-clique, `p in X`, and
`(X union {w}) cap L` is empty.

#### Proof

First, `G` is not two-apex.  A pair whose deletion left a planar graph
would meet every `K_5`-minor model, hence every member of
`F_5(G) union C`, contrary to the defining inequality
`tau(F_5(G) union C)>2`.

For every pair of distinct leaves `ell_i,ell_j`, choose the literal
clique `K_{ij}` supplied by Corollary 2.2 of the private-transversal
kernel theorem.  It contains `p` and avoids `ell_i,ell_j`; consequently

\[
                         |K_{ij}\cap L|\le3.            \tag{2.7}
\]

Any two chosen cliques intersect in at least four vertices.  Otherwise
those two cliques and `L` would be three literal five-cliques with all
pairwise intersections of order at most three.  Theorem 1.10 of
Niu--Zhang, as quoted in
[`../results/hc7_global_literal_k5_transversal.md`](../results/hc7_global_literal_k5_transversal.md),
would give a `K_7` minor in the seven-connected non-two-apex graph `G`.

The graph has no literal `K_6`, since such a clique is a `K_6` model on
six vertices and again lifts to `K_7` by Lemma 4.3 cited above.  We use
the following elementary consequence.  A pairwise four-intersecting
family of literal five-cliques in a `K_6`-subgraph-free graph either has
only one member or has a common four-clique.  Indeed, choose distinct
members `X union {a}` and `X union {b}`.  Their exclusive vertices
`a,b` are nonadjacent, or their union is a `K_6`.  Any further
five-clique missing a vertex of `X` would have to contain `a,b` in order
to meet each chosen clique in four vertices, contradicting `ab notin
E(G)`.

If all the `K_{ij}` coincide, their common five-set avoids every leaf:
each leaf occurs in one of the forbidden pairs.  Choose a four-subset
`X` of this clique containing `p`; the fifth vertex already gives (2.6).

Otherwise the preceding elementary fact supplies a four-clique `X`
contained in every `K_{ij}`.  Since all the chosen cliques contain `p`,
we have `p in X`.  For each leaf `ell_i`, some chosen clique avoids
`ell_i`, so `X cap L` is empty.  Write

\[
                         K_{ij}=X\cup\{w_{ij}\}.
\]

If every `w_{ij}` belonged to `L`, at least three distinct leaves would
occur among them: a set of at most two leaves is itself contained in
some forbidden pair and therefore cannot supply the completion vertex
for that pair.  Three such completion leaves form a triangle in `L` and
are each complete to `X`; together with `X` they induce a literal `K_7`.
This is impossible.  Hence some `w_{ij}` lies outside `L`, and its clique
`X union {w_{ij}}` is disjoint from `L`. \(\square\)

## 3. The exact remaining linkage in the five-clique subcase

### Proposition 3.1

Under the hypotheses of Theorem 2.3, put `H=G-L`.  Then:

1. `H` is three-connected; and
2. if `e_i,e_j` are vertex-disjoint, there do not exist vertex-disjoint
   connected subgraphs `C_i,C_j` of `H` such that

   \[
     e_i\subseteq C_i,\quad e_j\subseteq C_j,
     \quad N_G(\ell_i)\cap C_i\ne\varnothing,
     \quad N_G(\ell_j)\cap C_j\ne\varnothing.          \tag{3.1}
   \]

Thus the unresolved part of this `m=5` branch is a standard prescribed
two-linkage obstruction in a three-connected graph, not an arbitrary
five-support configuration.

#### Proof

We already know that `H` is two-connected.  If `{s,t}` were a two-vertex
cut of `H`, let `D_1,D_2` be distinct components of `H-{s,t}`.  For each
`h`,

\[
                         N_G(D_h)\subseteq L\cup\{s,t\}.
\]

The complement of `D_h` is nonempty, so seven-connectivity forces
`|N_G(D_h)|>=7`.  Equality with the displayed seven-set follows.  In
particular, every `D_h` is adjacent to every vertex of `L` and to both
`s,t`.  The disjoint connected subgraphs

\[
                         D_1\cup\{s\},
                 \qquad D_2\cup\{t\}
\]

are adjacent and are each adjacent to every vertex of `L`.  With the five
singletons of `L` they give a `K_7` model, a contradiction.  Hence `H`
is three-connected.

Now suppose (3.1) holds.  By Theorem 2.3, `e_i` is collectively adjacent
to `L-{ell_i}`, and `C_i` also contains a neighbour of `ell_i`; hence
`C_i` is adjacent to every vertex of `L`.  The same holds for `C_j`.
If `C_i,C_j` are not already adjacent, take a shortest path between them
in the connected graph `H` and add all its internal vertices to one of
the two subgraphs.  This preserves disjointness and connectedness and
makes the two subgraphs adjacent.  They and the five singleton vertices
of `L` are then a `K_7` model, again a contradiction. \(\square\)

## 4. A row-compatible clique trigger when `m=6`

The six-leaf branch admits a different exact normalization.

### Proposition 4.1

Assume `m=6`.  For each `i`,

\[
                         A_i=(L-\{\ell_i\})\cup\{r_i\} \tag{4.1}
\]

for a vertex `r_i` outside `L union {p}`.  Fix a spanning `K_5` model on
`A_i`, with singleton four-clique `Q_i` and two-vertex edge-bag `f_i`.
Then at least three vertices of `Q_i` are leaves and at least one endpoint
of `f_i` is a leaf.

For any two leaf vertices `a,b in Q_i`, there is a literal `K_5` clique
`K_{ab}` containing `p` and avoiding `a,b`.  If `K_{ab}` does not contain
both endpoints of `f_i`, then after contracting `f_i` its image is a
literal `K_5` whose intersection with the image of the chosen model has
order at most three.

Consequently, if two such cliques can be chosen so that neither contains
both endpoints of `f_i` and their two images intersect in at most three
vertices, Theorem 1.1 of
[`../results/hc7_one_split_two_clique_composition.md`](../results/hc7_one_split_two_clique_composition.md)
returns one of:

1. a `K_7` minor;
2. a two-vertex transversal of every support-at-most-six `K_5` model; or
3. an actual order-seven separation preserving `A_i` and both literal
   cliques.

#### Proof

Equation (4.1) follows from (1.2) and `|A_i|=6`.  Only one vertex of
`A_i` is not a leaf.  The four singleton bags therefore include at least
three leaves, and the two-vertex bag includes at least one leaf.

Corollary 2.2 of the private-transversal kernel theorem supplies the
literal clique `K_{ab}` through `p` and avoiding `a,b`.  By Lemma 2.1 it
also follows directly that every literal clique contains `p`.  If
`K_{ab}` contains at most one endpoint of `f_i`, its image after the
contraction still has five distinct vertices and is a clique.  It meets
`Q_i` in at most two vertices, because it avoids `a,b`, and it meets the
contracted image of `f_i` in at most one more vertex.  Thus the required
intersection has order at most three.

The final assertion is exactly Theorem 1.1 of the cited composition
theorem, applied to the chosen split model and the two returned literal
cliques. \(\square\)

## 5. Exact contribution and limitation

For `m=5`, either `p` meets every literal `K_5`, or the unique literal
clique avoiding `p` converts all five exact supports into five distinct
near-complete edges outside that clique.  The pairwise-intersecting edge
case and every two-separation of the exterior are eliminated by explicit
`K_7` models.  The same hypotheses also force a second literal `K_5`
vertex-disjoint from the leaf clique.  What remains has these two disjoint
literal cliques, two disjoint distinguished defect edges inside a
three-connected exterior, and failure of the precise paired linkage
(3.1).

For `m=6`, the common centre `p` meets every literal `K_5`; Proposition
4.1 identifies a concrete family of row-compatible literal-clique
witnesses and hands every compatible pair to an already proved global
composition theorem.  It does not prove that two compatible witnesses
always exist.  Neither section resolves the branches in which `p` meets
every literal `K_5`.
