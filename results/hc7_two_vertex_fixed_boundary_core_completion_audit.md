# Independent audit: two-vertex fixed-boundary core completion

**Audited file:** `results/hc7_two_vertex_fixed_boundary_core_completion.md`
**SHA-256:**
`3a0c9deceea2f88f9a3f5b9d667700f8d1497cadcd8b1b88a2bf050d9ab77109`
**Verdict:** **GREEN.**  The boundary-endpoint selection lemma, the seven
branch sets in Theorem 2.1, and the balanced-order-eight specialization are
correct as stated.  This is an independent internal mathematical audit, not
external peer review.

The promoted source differs from the originally audited revision only in
its status paragraph: the pending-audit wording was replaced by a link to
this GREEN audit.  Reverting that metadata edit reproduces the original
audited SHA-256
`b0c4d8c42aae1b632a0249dd2aa08ea7ce77d78495a46e634863340736729b7d`.
No theorem statement, hypothesis, conclusion, or proof step changed, so the
GREEN verdict transfers to the promoted hash above.

The result eliminates only the two-vertex fixed-boundary critical core in
the surviving balanced order-eight branch.  It does not eliminate the
facial-triangle or positive-slack cores, the whole balanced order-eight
configuration, or `HC_7`.

## 1. Boundary-endpoint selection

Let `M` be the set of vertices of `R` missed by `A`.  Since `A` misses at
most two vertices of `R union e union f` and misses at least one vertex of
`R`, its order is one or two.

If `|M|=2`, those two vertices exhaust all vertices missed by `A`; hence
every endpoint of both `e` and `f` has a neighbour in `A`.  Assign the two
members of `M` to different edges.  Collective adjacency of each edge to
every member of `R` supplies one endpoint of each assigned edge adjacent
to its assigned member of `M`.  Both selected endpoints meet `A`, and the
edges are disjoint, so the two endpoints are distinct and satisfy every
condition on `Z`.

If `M={r}`, at most one endpoint in `e union f` can be missed by `A`.
Collective adjacency gives one candidate endpoint of `e` and one candidate
endpoint of `f` adjacent to `r`.  These candidates are distinct because
the edges are disjoint.  At least one therefore meets `A`; selecting it
gives the required singleton `Z`.

These cases are exhaustive.  No endpoint is assumed individually complete
to `R`, and the proof uses only the collective adjacency appearing in the
lemma.

## 2. The seven branch sets

Write the sets in Theorem 2.1 as

```text
B_e = {ell_e}
B_f = {ell_f}
B_A = V(A) union Z
B_D = V(D) union ((S-R)-Z)
B_r = {r}, for r in R.
```

They are pairwise disjoint: `A`, the two leaves, and `D` are disjoint
subsets of components of `G-S`; `Z` and `(S-R)-Z` partition the used
vertices of `S-R`; and the three vertices of `R` are retained separately.

The sets are connected.  Each selected endpoint in `Z` has a neighbour in
the connected graph `A`, so `B_A` is connected.  Every vertex of
`(S-R)-Z` has a neighbour in the connected boundary-full component `D`, so
`B_D` is connected.  The other five sets are singletons.

All 21 pairwise adjacencies follow from the stated hypotheses:

1. `B_e` and `B_f` are adjacent by the leaf edge.
2. Each leaf is adjacent to `B_A` by its assumed neighbour in `A`.
3. Each leaf is adjacent to all three `R` singletons by item 5.
4. Since `Z` uses at most one endpoint from each defect edge, `B_D`
   retains an endpoint of `f` and an endpoint of `e`.  Completeness of
   `ell_e` to `f` and of `ell_f` to `e` gives the two leaf--`B_D`
   adjacencies.
5. The vertex `x` lies in `B_D`, because `Z` is contained in
   `V(e) union V(f)`.  The assumed `A`--`x` contact gives the
   `B_A`--`B_D` adjacency.
6. Boundary-fullness of `D` gives every `B_D`--`B_r` adjacency.
7. If `A` meets `r`, then `B_A` is directly adjacent to `B_r`; if not,
   Lemma 1.1 puts in `B_A` an endpoint adjacent to `r`.
8. The three `B_r` are pairwise adjacent because `R` is a clique.

Thus the displayed sets are seven disjoint connected pairwise adjacent
branch sets.  Theorem 2.1 constructs an actual `K_7`-minor model and does
not rely on an implicit contraction, a completion edge, or a stronger
connectivity hypothesis.

## 3. Application to the balanced order-eight branch

The corollary uses only previously promoted properties of that branch.
The original five-clique gives the edge `ell_e ell_f` and makes both leaves
adjacent to all of `R`.  The balanced boundary gives the disjoint
anticomplete defect edges and their collective contacts with `R`, while
the opposite open component `D` is boundary-full.

The promoted connected-leaf-side conclusion gives precisely that

- `A=C-{ell_e,ell_f}` is connected;
- each leaf and `x` has a neighbour in `A`;
- `A` contacts both defect edges; and
- `A` misses one or two boundary vertices, including a member of `R`.

It remains to check the complete cross-index endpoint contacts used in
item 5 of Theorem 2.1.  If the critical core is only the leaf edge, the
promoted fixed-boundary theorem gives the two leaves the same singleton
list.  Hence each leaf sees all five other colours at boundary neighbours.
The three vertices of `R` account for three of those colours.  The
distinguished vertex `x` misses both leaves, and each leaf is anticomplete
to its same-index defect edge.  The only remaining possible boundary
neighbours are therefore the two endpoints of the opposite defect edge.
The two colours absent from the original five-clique must occur on those
two endpoints.  Both endpoints are consequently adjacent to the leaf;
because they form an edge, their colours are distinct as required.  Thus
`ell_e` is complete to `f` and `ell_f` is complete to `e`.

Every hypothesis of Theorem 2.1 is now present literally, so its branch-set
model contradicts `K_7`-minor-freeness.  Corollary 3.1 correctly eliminates
the two-vertex core.

## 4. Exact remaining scope

The endpoint selection depends essentially on the near-full boundary
contact of `A`, and the branch-set construction depends on complete
cross-index contact from each leaf to the opposite defect edge.  The latter
comes from the singleton-list conclusion and is not available for the
common two-element lists of the facial-triangle core.  The source therefore
correctly leaves the triangle and positive-slack cases open and draws no
conclusion about `HC_7` as a whole.
