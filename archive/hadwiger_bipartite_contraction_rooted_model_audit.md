# Adversarial audit: bipartite-contraction rooted near-cliques

**Verdict: GREEN AS PATCHED for the co-rooting theorem and inherited
warehouse/state consequences.**  The central result is sound: in a
least-parameter proper-minor-minimal counterexample, every nontrivial
connected induced bipartite subgraph is contained in one branch bag of
some `K_{k-1}`-model.  In particular, every pair of vertices can be
co-rooted by contracting a shortest path.

The original final paragraph overstated the classification after
expansion: block geometry internal to an arbitrary prescribed set `T`
need not descend from a lobe of the minimum root bag in `G/T`.  That
paragraph has been repaired.  The inherited warehouses are bounded, but
the intrinsic `T`-core split obstruction remains an additional live
object.

This is an internal proof audit, not external peer review or a novelty
determination.

## 1. Exact chromatic order

Let `Q=G/T`, where `|T|>=2` and the **induced** graph `G[T]` is connected
and bipartite.

* `Q` is a proper minor, so proper-minor minimality gives
  `chi(Q)<=k-1`.
* If `Q` had a `(k-2)`-colouring and `z` had colour `alpha`, colour one
  side of the bipartition of `G[T]` by `alpha` and the other by one new
  colour `beta`.  Every outside neighbour of either side is adjacent to
  `z` in `Q`, hence avoids `alpha`, while `beta` is absent outside `T`.
  All internal edges cross the bipartition.  This gives a `(k-1)`-
  colouring of `G`, a contradiction.

Thus `chi(G/T)=k-1`.  The inducedness condition is essential: contracting
a bipartite spanning subgraph would suppress possible same-side chords of
`G[T]`, and the expansion colouring could fail.  Connectivity is also
essential both to make contraction a single branch operation and to join
the lifted root bag.

No hidden assumption that `G[T]` is an induced *component* is present.
It may have arbitrary neighbours outside `T`; those neighbours are all
seen by `z` in the quotient, exactly as the colouring proof requires.

## 2. Exact minor order and least-parameter induction

At the least failing parameter, `HC_{k-1}` is available.  Since
`chi(Q)=k-1`, its contrapositive gives a `K_{k-1}` minor in `Q`.  Since
`Q` is itself a minor of the `K_k`-minor-free graph `G`, it has no `K_k`
minor.  Hence `eta(Q)=k-1` exactly.

This application is not circular: it uses only the strictly smaller
parameter.  Proper-minor minimality also makes `G` connected (otherwise
its proper components can be coloured separately), and contraction of
connected `T` makes `Q` connected.  The source now states this before
using a shortest path from `z` to the model union.

## 3. Rooting and lifting the model

Starting with any `K_{k-1}`-model in connected `Q`, a shortest path from
`z` to its union can be absorbed into the first met bag.  Its internal
vertices avoid all old bags, so this creates a legitimate `z`-rooted
model without any spanning assumption.

Replace `z` in the root bag `R` by all of `T`.  Every component of `R-z`
has a `Q`-edge to `z`; that edge lifts to an edge from the component to
some vertex of `T`.  Since `G[T]` is connected, `(R-z) union T` is
connected.  A root-to-external-bag edge incident with `z` similarly lifts
to a `T`-to-bag edge, while every other adjacency is unchanged.  Thus all
branch bags remain connected, disjoint, and pairwise adjacent.

This proves the stated co-rooting theorem.  It is deliberately weaker
than a rooted transversal: all prescribed vertices occupy the **same**
bag.

## 4. All-path and induced-tree consequences

For distinct vertices `a,b`, connectedness supplies a shortest `a-b`
path.  Its vertex set induces a path—any chord would shorten it—and is
therefore connected and bipartite.  Contracting it and applying the lift
puts both endpoints, indeed the whole path, into one branch bag.  The
same proof applies to any prescribed vertex set whose induced graph is a
tree.  It does not apply merely because the ambient graph contains a
non-induced tree on that vertex set.

## 5. Minimum root bags and inherited charges

Minimize `|R|` among the `z`-rooted quotient models.  The audited
zero-delete/one-rotate theorem applies in `Q`: every detachable subset of
`R-z` monopolizes at least two named labels, all of them direct defects at
`z`.  Minimal rooted block lobes are disjointly charged, giving at most
`floor((k-2)/2)`.

After expansion, these lobes remain vertex sets in `B-T`; hence their
charge can be tested against the entire prescribed set `T`.  If such a
lobe has no edge to `T`, an inclusion-minimal separator between the two
connected sets is a genuine ambient cut.  Every separator vertex sees
both distinguished components, and `s`-connectivity forces adhesion order
at least `s`.  This argument does not require the model to be spanning or
`T` to be induced beyond the already stated connectivity hypothesis.

## 6. State splice

At an uncharged lobe adhesion, the `T` contraction is wholly in the open
shore opposite the lobe and leaves the lobe's closed shore literal.  A
boundary-faithful warehouse operation wholly inside the lobe shore leaves
the closed `T` shore literal.  If their colourings induced the same
equality partition on the adhesion, a palette permutation would align
the boundary colours; taking the faithful shore from each colouring would
then colour all of `G`.  There are no edges between the open shores.

Therefore the two operation-state sets are disjoint.  The conclusion
would not be justified for a contraction meeting the boundary, or for a
warehouse operation deleting/contracting boundary data; the theorem
correctly restricts both operations to the open shores.

## 7. Scope defect repaired during audit

The quotient root bag `R` and the prescribed expanded core `T` carry
different kinds of geometry.  Lobes of `R-z` survive as inherited
warehouses and obey the charge/adhesion theorem.  But cutvertices or block
branches lying **inside `T`** collapse to the single quotient vertex `z`
and are invisible to that theorem.  Consequently the source could not
validly claim that every failed split of arbitrary `T` was exhausted by
the edge-contraction root-torso trichotomy plus inherited warehouses.

The final section now states the exact conclusion:

1. every prescribed induced path/tree has a co-rooted near-clique;
2. at most `floor((k-2)/2)` inherited minimum-root warehouses survive,
   each `T`-charged or behind a full state-incompatible adhesion; and
3. an additional uniform label-preserving split theorem is still needed
   for the intrinsic block/portal geometry of arbitrary bipartite `T`.

For `k=7`, “at most two” applies to the inherited quotient lobes, not to
an arbitrary number of branches internal to the prescribed tree.

## 8. Frontier consequence

The theorem is the strongest clean uniform rooted-model principle in the
current package: the search may prescribe any induced path, induced tree,
or other connected induced bipartite subgraph and obtain a
`K_{k-1}`-model whose one branch bag contains it.  This lets future
arguments choose a path or tree adapted to a desired two-path/web exchange
*before* selecting the clique model.

It does not yet provide two branch bags, a prescribed distribution among
bags, or a split of the co-rooted bag.  The next genuine theorem must use
the bipartition, path order, or tree branching to force a
label-preserving split, or else convert its failure into a full adhesion
with a common operation state.  That is the precise bridge from this
co-rooting principle to `HC_7` and, potentially, to general `k`.
