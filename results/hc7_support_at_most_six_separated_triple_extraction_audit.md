# Audit of the small-support separated-triple theorem

**Verdict:** **GREEN after a second, independently assigned line-by-line
audit.**  The second audit reconstructed the mixed-size classification,
the two-cluster extraction, the complement argument on seven vertices and
the final connectivity lift without relying on the first audit.  The
theorem is an extraction result only; it does not prove the support-six
transversal theorem.

## 0. Independent verdict and attempted failure points

The independent audit tried to break precisely the four transitions most
likely to hide a uniform-family assumption.

1. For a five-set and a six-set, near-identity means that the five-set is
   literally contained in the six-set.  Consequently a six-set
   near-identical to two distinct five-sets must be their six-element union;
   no mixed-size exception is missing from Lemma 2.1.
2. If the two non-near-identical seeds have two common vertices, those two
   vertices meet every set near-identical to either seed.  Hence the
   transversal hypothesis really forces seed intersection at most one.
   This makes the two clusters in Lemma 3.1 disjoint and makes each cluster
   pairwise near-identical.
3. For a spanning `K_5` model on six vertices, the complement consists of
   at most two nontrivial stars: the four singleton bags are complement-
   independent, the two edge-bag endpoints are complement-nonadjacent, and
   no singleton is complement-adjacent to both endpoints.  The proof uses
   only this forward implication.  Applying it after every vertex deletion
   gives exactly the star-component analysis in Lemma 4.2.
4. In the seven-vertex support case, a component of `G-W`, where `W` is
   the support, has all seven support vertices as neighbours.  Otherwise its
   neighbourhood, of order at most six, is a separator.  Thus the extra
   component is a literal seventh branch set; no connectivity of the whole
   complement is being assumed.

No counterexample was found, and no graph-minor operation is shared across
the three extracted models.  That last fact is why the result is sound as
an extraction theorem but cannot yet invoke a three-clique theorem.

## 1. Set-family classification

The mixed-size threshold

\[
 |A\cap B|\ge\max\{|A|,|B|\}-1
\]

is essential.  In particular, a near-identical five-/six-set pair means
literal containment of the five-set.  This makes every mixed case in
Lemma 2.1 exact rather than an appeal to a uniform-family analogy.

The pairwise near-identical classification was checked by splitting into:

1. two distinct five-sets, whose intersection has order four;
2. exactly one five-set, which is contained in every six-set; and
3. six-sets only, the usual star/top classification in the Johnson graph.

In case 1, any six-set must contain both selected five-sets and is therefore
their six-element union.  Empty total intersection in the contained-six-
set case forces each of the six possible omitted vertices to occur, hence
all six five-subsets.  In case 3, the same argument forces all seven
six-subsets.  There is no missing mixed family with empty intersection.

## 2. Extraction logic

For non-near-identical seeds `A,B`, failure of a separated triple says
that every member is near-identical to at least one seed.  If
`|A intersect B|>=2`, any two common vertices hit every member, because a
near-identical member omits at most one literal seed vertex.  Thus the
transversal hypothesis correctly gives `|A intersect B|<=1`.

A member near-identical to both seeds would force at least three common
seed vertices.  The exact minimum is attained for three five-sets:
two subsets of order at least four inside a five-set meet in at least
three vertices.  Hence the two clusters are disjoint.

If `C` is near-identical to `A`, then `|B intersect C|<=2` in each of the
four size combinations.  Therefore a non-near-identical pair in the same
cluster, together with the opposite seed, would be a separated triple.
This proves that both clusters are pairwise near-identical.  If both had a
common vertex, those two vertices would form a transversal; thus one is a
full family from Lemma 2.1.

## 3. Graph realization of the full families

For a five-element support, all five branch sets are singletons.  Hence a
full family of the six five-subsets of `U` makes every such subset a
literal `K_5`, and every pair of vertices of `U` is an edge.  The resulting
`K_6` is literal.

For the seven-set family, each deletion graph has a *spanning* `K_5`
model.  Taking complements converts such a model into at most two star
components.  This implication is deliberately one-way: the complement
`K_{1,5}` is a union of one star but its original graph is `K_5` plus an
isolated vertex and has no spanning model.  A nonstar component has a
triangle or a three-edge path, both
surviving some vertex deletion.  Three nontrivial components retain three
chosen independent edges after deletion of the seventh vertex.  These are
the only two possible failures of the at-most-two-star condition.

The one-star `K_{1,6}` complement needs separate treatment: deleting a
leaf gives `K_{1,5}`, whose complement is `K_5` plus an isolated vertex and
has no spanning `K_5` model.  Otherwise an isolated complement vertex is
available as the second endpoint of the spanning `K_6` edge-bag.  Thus all
complement cases in Lemma 4.2 are covered.

Finally, the lift of a `K_6` model supported on seven vertices does not
assume `G-W` connected.  Seven-connectivity forces every component of
`G-W` to have all seven support vertices in its neighbourhood, so any one
component supplies the seventh branch set.  For support at most six,
connectivity and minimum degree give the same conclusion.

## 4. Scope checks

The proof uses only seven-connectivity and exclusion of a `K_7` minor.  It
does not use contraction-criticality, colourings, a selected near-`K_7`
model, or exact-seven adhesion terminology.

The conclusion is not a minor-composition theorem.  In particular:

* contracting the split edge of one six-support may reduce connectivity;
* that edge can meet or merge two named rows of another model;
* the Niu--Zhang theorem applies directly only when all three supports are
  literal five-cliques; and
* the theorem does not return a common two-vertex transversal.

These are the exact remaining gaps and prevent any inference of `HC_7` or
even `tau(S_{<=6}(G))<=2` from this result alone.

The irredundant reduction in Corollary 1.2 is safe because only supersets
of existing family members are removed.  It does not assert that every
spanning model on that six-set has the same edge-bag.  It only fixes one
such model; absence of a contained literal `K_5` makes both deficiency sets
for that chosen edge-bag nonempty, while model adjacency makes them
disjoint.  The four displayed patterns are then exhaustive arithmetic on
the four singleton rows.
