# Audit of the cycle-boundary completion theorem

**Verdict:** GREEN.

**Source audited:** `results/hc7_cycle_boundary_completion.md`.  The cold
audit checked the mathematical revision at SHA-256
`f5b21faab19767e7bc7d415745856e1d7181900a1cd437a118d668be4b3bbce5`.
Promotion changed only the status line; the promoted source is SHA-256
`f87ddcf7e4bd33b0fc107033033d9a8ebb2f6e32533b1b9c4538c0bf4bd137db`.

**Audit class:** separate internal cold audit.  This is not external peer
review.

## 1. External theorem

The Martinsson--Steiner statement is quoted with the correct hypotheses
and conclusion.  Lemma 3.1 of *Strengthening Hadwiger's conjecture for
4- and 5-chromatic graphs* applies to a 3-connected graph `F`, a root set
of order at least four which is spread out across every order-three
separation, and the absence of a rooted `K_4`; it concludes that adjoining
one vertex complete to the root set gives a planar graph.  The definitions
of spread out and rooted model in the draft agree with the source.

## 2. Shore connectivity for an arbitrary rim length

Deleting `p,q` from a 7-connected graph leaves the graph `H`
5-connected.  Fix `Z subseteq V(F_A)` with `|Z|<=2`.  If a component of
`F_A-Z` missed `C-Z`, it would lie in `A`; because `A,B` are distinct
components outside the displayed boundary, its entire neighbourhood in
`H` would lie in `Z`, contradicting 5-connectivity.

If `Z` meets `A`, at most one rim vertex is deleted.  A cycle minus at
most one vertex is connected, so every component meeting `C-Z` is the
same component.  If `Z subseteq C`, the connected shore `A` is untouched
and has a neighbour at every remaining rim vertex.  It therefore joins
all components of `C-Z`, including when two nonadjacent rim vertices are
deleted.  Thus `F_A-Z` is connected for every `|Z|<=2`.  Since the rim has
order at least four and the shore is nonempty, the order convention for
3-connectivity is also satisfied.  The proof for `F_B` is identical.

For an order-three separation `(U,W)` of `F_A`, if `C subseteq U`, then
the nonempty set `W-U` lies in `A`.  It has no edge to `B`, and the
separation excludes edges to `U-W`; hence its neighbourhood in `H` is
contained in the three-set `U intersect W`.  This contradicts
5-connectivity.  The symmetric alternatives prove exactly that `C` is
spread out in both shore graphs.

## 3. Rooted model lift

If `M_1,...,M_4` form a `C`-rooted `K_4` model in one shore graph, then

\[
 M_1,M_2,M_3,M_4,\quad B,\quad\{p\},\quad\{q\}
\]

are seven disjoint connected branch sets.  The first four are pairwise
adjacent.  Each meets a rim vertex, so the opposite full shore and both
vertices `p,q` are adjacent to it.  Full attachment makes the opposite
shore adjacent to `p,q`, and `pq` supplies the final adjacency.  Thus all
21 edges of the branch-set clique are present.

## 4. Wheel-face and gluing arguments

After applying Martinsson--Steiner, the added vertex together with the
induced cycle is a wheel in a planar embedding.  The connected open shore,
which is disjoint from the wheel vertices, lies in one face of this plane
wheel: a path inside the shore cannot cross from one wheel face to another.
It cannot lie in a triangular face incident with the hub.  Such a face has
only two rim vertices on its boundary, whereas the shore has a neighbour
at every rim vertex and the hub has no neighbours in the shore.  This
argument remains valid when the rim has its minimum allowed order four.

Therefore the shore lies in the unique wheel face on the side of the rim
opposite the hub.  Deleting the hub yields a planar disc embedding with
the induced cycle as boundary.  Reflecting one of the two shore discs and
identifying their boundary cycles embeds `H` on the sphere; there are no
cross-shore edges to add.  This contradicts the assumed `K_5` minor because
planarity is minor-closed.

## 5. Scope

The argument proves the theorem for every induced cycle of length at least
four under the stated connectedness and full-attachment hypotheses.  It
does not infer full attachment from seven-connectivity when the displayed
boundary has order greater than seven, and the theorem correctly assumes
that condition explicitly.  No unresolved gap was found.
