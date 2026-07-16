# Independent audit of the five- and six-support star kernels

**Verdict:** GREEN for the exact revision audited.

## Audited revision

- theorem file: `results/hc7_star_private_transversal_large_kernel.md`
- SHA-256: `6c87044bf4c4e4c45b583a1e91cdd030897cebe6c6f6ee61f186419e99a43ba9`

This audit covers Lemmas 2.1--2.2, Theorems 2.3--2.4,
Proposition 3.1, Proposition 4.1, and the limitation statement.  It also
checks the exact uses of the promoted private-transversal kernel,
small-`K_6` lifting, the Niu--Zhang three-clique theorem, and the promoted
one-split/two-clique composition theorem.

## Checks performed

### 1. Star-kernel data and literal cliques

The cited private-transversal theorem gives distinct pairs
`P_i={p,ell_i}` which avoid `A_i`, while every other leaf belongs to
`A_i`.  Because every `P_i` transverses `F_5(G)`, a literal `K_5` avoiding
`p` contains all `m` leaves.  This is impossible for `m=6`, and for `m=5`
it forces the clique to be exactly `L`.  Lemma 2.1 follows.

The use of `tau(F_5(G) union C)>2` later is also exact: any two-apex set
would meet every support in both families, since the complement is planar
and hence `K_5`-minor-free.

### 2. Six-vertex normal form

A spanning `K_5` model on six vertices consists of one edge-bag and four
singleton vertices forming a four-clique.  The proof of Lemma 2.2 treats
all three possible intersections between its edge-bag and the fixed
outside pair `{x,y}`.

- If the pairs agree, the conclusion is immediate.
- If they are disjoint, `x,y` lie in the singleton four-clique.  Failure
  of either model-bag endpoint to see both of them forces the other
  endpoint to complete the singleton four-clique to a forbidden literal
  `K_5`.  Hence the edge `{x,y}` collectively sees the fixed four-clique.
- If the pairs meet once, the other outside vertex lies in the singleton
  four-clique.  Its adjacency to the fixed-clique endpoint of the model
  bag would create a literal `K_5`; collective model adjacency therefore
  forces its edge to the outside endpoint instead.  This gives both the
  edge `xy` and every required contact.

As an independent finite check, all labelled six-vertex graphs containing
the fixed four-clique were enumerated: among the 50 graphs having a
spanning `K_5` model but no literal `K_5`, none violates the conclusion.

### 3. The five-support reduction and its explicit minor model

For `m=5`, equation (1.2) and `|A_i|=6` leave exactly two vertices outside
`L` in each support.  Lemma 2.2 makes them an edge `e_i` collectively
adjacent to `L-{ell_i}`.  If either endpoint saw `ell_i`, then the five
singleton leaves and `e_i` would be a `K_6` model on seven vertices.
Lemma 4.3 of the cited separated-support theorem applies verbatim and
would lift this to `K_7`; thus the claimed anticompleteness is valid.

Distinctness of the five edges follows because `e_j` must collectively
see `ell_i` when `i!=j`, whereas `e_i` is anticomplete to it.  If the five
distinct edges had no disjoint pair, the standard edge-family
classification makes them a star (the only non-star pairwise-intersecting
simple edge family is the three-edge triangle).  Its common centre is
anticomplete to `L`, so each other endpoint `u_i` sees exactly every leaf
except `ell_i` among the adjacencies needed in the proof.

Deleting `L` from a seven-connected graph leaves a two-connected graph;
deleting the star centre from that graph leaves it connected.  A shortest
path between two distinct `u` vertices has no other `u` internally.  The
two proposed nonsingleton branch sets are therefore disjoint and
connected.  Each sees all five leaves, and they see each other through
the edge from the centre to a path endpoint.  Together with the five
singleton leaves these are seven pairwise adjacent branch sets.  The
contradiction in Theorem 2.3 is a valid explicit `K_7`-minor model.

### 4. The second clique in the five-support branch

Corollary 2.2 of the private-transversal theorem supplies, for every leaf
pair, a literal `K_5` through `p` avoiding that pair.  Each such clique
meets `L` in at most three vertices.  If two selected cliques met in at
most three vertices, those two together with `L` would satisfy all three
intersection hypotheses of Niu--Zhang Theorem 1.10.  The host is
seven-connected and, as checked above, non-two-apex.  The theorem would
give `K_7`, so the selected family is pairwise four-intersecting.

The auxiliary clique-family argument is correct.  Two distinct
five-cliques meeting in four vertices have nonadjacent exclusive vertices,
or their union is a literal `K_6`.  Any further five-clique meeting both
in four vertices must contain their common four-clique; otherwise it must
contain both nonadjacent exclusive vertices.  Thus either all selected
cliques coincide or they share a fixed four-clique `X`.

In the first case the common clique avoids every leaf.  In the second,
the common four-clique contains `p` and avoids every leaf.  If all fifth
vertices were leaves, at least three distinct leaves would occur (one or
two leaves can themselves be selected as a forbidden pair).  Those three
leaves, being a clique and each complete to `X`, would induce `K_7`.
Hence one completion lies outside `L`, proving Theorem 2.4 exactly.

### 5. Three-connectivity and the paired-linkage obstruction

The graph `H=G-L` is two-connected.  If `{s,t}` separated it, every
component behind that pair would have neighbourhood contained in the
seven-set `L union {s,t}`.  Another component exists, so
seven-connectivity forces equality.  Two distinct components, augmented
respectively by `s` and `t`, are disjoint connected subgraphs, each sees
all of `L`, and they are adjacent because the first component has a
neighbour at `t`.  With the five singleton leaves they form a `K_7`
model.  Thus `H` is three-connected.

If the two connected repairs in (3.1) existed, each would see all five
leaves.  A shortest path between two nonadjacent repairs may be absorbed
into one repair without destroying disjointness, making the two repairs
adjacent.  They and the leaf singletons would again be a valid `K_7`
model.  Proposition 3.1 follows.

### 6. Six-support contraction and composition

For `m=6`, each support contains five leaves and one nonleaf.  Therefore
the four singleton bags of any spanning `K_5` model include at least three
leaves, while its edge-bag includes at least one leaf.  For two leaf
singletons `a,b`, Corollary 2.2 returns the asserted literal clique.

If that clique contains at most one endpoint of the edge-bag, contraction
is injective on its five vertices, so its image remains a literal `K_5`.
It contains at most two vertices of the singleton four-clique (it avoids
`a,b`) and at most the one contracted edge vertex.  Its intersection with
the image of the chosen split model is therefore at most three.  Two
cliques satisfying the additional pairwise image-intersection hypothesis
meet every assumption of the promoted one-split/two-clique composition
theorem.  Its three conclusions are reproduced accurately in Proposition
4.1, including preservation of the original support and both cliques in
the exact-seven separation outcome.

## Scope and unresolved assumptions

No gap remains within the stated reductions.  The note correctly leaves
open both the paired-linkage obstruction in the five-support case and the
existence of two compatible clique witnesses in the six-support case.  It
does not claim that the common star centre meets every support-six model or
that either residual branch is closed.

The Niu--Zhang theorem is used as published external input.  The promoted
private-transversal, separated-support, and one-split composition results
were checked for exact hypothesis matching here; their full earlier proofs
were not re-audited from first principles.
