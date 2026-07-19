# Independent internal audit: reflection across an order-eight boundary with two one-defect supports

**Verdict:** GREEN for the theorem, the explicit minor-model construction,
and the stated strict-reversal corollary.  This is an internal mathematical
audit, not external peer review.

## Audited revision

This audit checks the complete source file
[`hc7_order8_two_defect_clique_oct_reflection.md`](hc7_order8_two_defect_clique_oct_reflection.md)
at SHA-256

```text
69a63c7899081defb83a15d838e636d6eb5dc96cdc1b0bf5a66ee029c0beafd7
```

No unresolved assumption or gap remains in the displayed statements.  The
result has only the scope stated in its trust boundary and does not prove
`HC_7`.

This is a promotion re-pin of the previously GREEN source revision at
SHA-256

```text
019426eb7dd71cd2ce60faff0626c2e998c258f11dc519943311c363dd1fb8e4
```

The note moved from `active/` to `results/`; its status, adjacent-audit link,
and repository-relative dependency links were adjusted accordingly.  A
line-by-line comparison confirms that the hypotheses, conclusions, proofs,
and trust boundary are mathematically unchanged.  The audit below therefore
continues to apply to the promoted source at the current hash.

## 1. Odd-cycle forcing

Deleting `d,e` leaves a bipartite boundary graph, so every odd cycle in the
boundary meets `{d,e}`.  Two vertex-disjoint odd cycles therefore meet that
two-set in the two distinct singleton sets.  Removing `d` from its odd cycle
leaves an odd-length path between two neighbours of `d`; those neighbours
belong to opposite classes of the chosen bipartition.  The same argument
applies to `e`.  Thus both bipartition classes are nonempty and each of
`d,e` has a neighbour in both classes, exactly as required later.

## 2. The two contraction constructions

For the first closed-shore colouring, `A_d union X` and `A_e union Y` are
disjoint connected sets.  Each contains an edge, so contracting a spanning
tree of each produces a proper minor.  Their images are adjacent, and both
images are adjacent to each of `d,e`; together with the edge `de` they form
a four-clique.  Consequently the two images and the two singleton boundary
vertices have four distinct colours.

Expanding only onto the untouched closed shore is legitimate.  The vertices
of `X` receive the first image colour and those of `Y` receive the second.
There are no edges inside either bipartition class, every edge from one of
those boundary vertices to the retained shore was represented at its
contraction image, and the four-clique makes the four displayed blocks
pairwise colour-distinct.  Hence the induced equality partition is exactly

```text
X | Y | {d} | {e}.
```

The reverse contraction is equally valid.  Boundary-fullness makes
`Q_1 union X` and `Q_2 union Y` connected; nonemptiness of `X,Y` supplies
an edge between their contraction images; and both images are adjacent to
`d,e`.  The resulting proper-minor colouring expands to the same exact
boundary partition on the other closed shore.  A permutation of six colour
names can align the four distinct boundary colours, after which the two
colourings glue because the open shores are anticomplete.

## 3. Short-cycle minor model

A cycle of order three or four has a `K_3` minor whose three nonempty branch
sets use exactly its vertices.  Since the cycle avoids `d,e`, at least two
other boundary vertices remain as distinct anchors.  The seven branch sets
displayed in the source are pairwise disjoint and connected.

Every required adjacency is present:

- the two boundary-full subgraphs meet one another through the opposite
  anchor and meet every cycle branch set;
- both anchors avoid `d,e`, so each anchored full subgraph is adjacent to
  both one-defect subgraphs;
- each one-defect subgraph meets every cycle branch set because the cycle
  avoids its missed vertex;
- the two one-defect subgraphs are adjacent by hypothesis; and
- the three cycle branch sets are pairwise adjacent.

Thus the construction is an explicit `K_7`-minor model.  The count remains
valid in the tight four-cycle case, where exactly two anchors remain.

## 4. Strict-reversal application

The repaired corollary states the full counterexample hypotheses and assumes
exactly three `S`-full components.  For `b <= k < a`, the two path sides

```text
P[0,k]  and  P[k+1,m]
```

are nonempty, disjoint, connected and adjacent.  The first contains the
left one-defect tail and has no neighbour at `d` because `k<a=ell(d)`; the
second contains the right one-defect tail and has no neighbour at `e`
because it starts after `k>=b=r(e)`.  The other two components supply the
two boundary-full subgraphs.  This verifies the short-cycle lemma literally,
including every endpoint case.

The cited three-component classification applies: two full components give
the boundary chromatic upper bound; a clique odd-cycle transversal would
six-colour the host; and a `K_4` minor surviving deletion of two boundary
vertices would lift to a `K_7` minor.  Under the corollary's counterexample
hypotheses the boundary is therefore one of the classified residual types,
each of which contains two vertex-disjoint odd cycles.  These cycles justify
the final use of the common-partition theorem when the six remaining
boundary vertices induce a bipartite graph and `de` is an edge.

## 5. Trust boundary

The audit does not infer anything for a five- or six-cycle in
`G[S-{d,e}]`, for a nonbipartite remaining boundary of girth at least five,
or for the nonadjacent defect pair.  It also does not claim that an arbitrary
order-eight interface has the induced-path strict-reversal form.
