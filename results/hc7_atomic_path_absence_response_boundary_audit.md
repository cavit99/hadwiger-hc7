# Independent internal audit of the atomic path-absence response boundary

**Verdict:** GREEN.

This is a separate internal mathematical audit, not external peer review.
No unresolved assumption or proof gap was found within the theorem's stated
scope.

## Audited revision

- theorem note:
  [`hc7_atomic_path_absence_response_boundary.md`](hc7_atomic_path_absence_response_boundary.md),
  SHA-256
  `d6fc8e0024b31439fbdd7fe4f2e20593ba5e01553bef937e2d26aec0032da036`.

I audited the promoted revision after its three precision edits: separators
are explicitly disjoint from their terminals, the two-vertex chromatic
inequality is displayed, and the application says that its boundary is
contained in the named set `Z`.  I did not alter the theorem note.

## 1. Minimal-separator and order checks

Let `S` be an inclusion-minimal `r`--`t` separator and let `A,B` be the
components of `G-S` containing `r,t`.  For each `s in S`, an `r`--`t` path
in `G-(S-{s})` uses `s` and no other member of `S`.  Its two sections show
that `s` has a neighbour in both `A` and `B`.  Componenthood gives
`N_G(A)=S`, and seven-connectivity gives `|S|>=7`; the containing separator
`Z` gives `|S|<=9`.  The displayed separation therefore has two nonempty
open sides and the required literal fullness.

At order seven, take the far open shore in the generic exact-seven response
interface to be all of `V(G)-(A union S)`.  It is nonempty, need not be
connected, is anticomplete to `A`, and the preceding argument gives every
remaining hypothesis of that interface.  Deleting a selected `A`--`S`
edge is a proper minor and hence has a six-colouring.  The automatic
response lemma therefore applies and gives `chi(G[S])<=4`.

At orders eight and nine, the two distinguished components are nonempty,
connected, anticomplete, and individually full to `S`.  These are exactly
the hypotheses of the audited two-full-shore boundary-absorption theorem.
It gives four-colourability except for the stated order-nine graph
`K_2 join C_7`.

## 2. Audit of the order-nine exception

Write the universal edge as `pq` and the induced cycle as
`0,1,...,6`.  If `A,B` are the only components of `G-S`, then

```text
chi(G-{p,q}) >= chi(G)-2 = 5.
```

The established case `HC_5` supplies a `K_5` minor.  The cycle-completion
theorem applies literally: the cycle is induced, `p,q` are adjacent and
complete to it, the remainder has exactly the two connected full
components `A,B`, and the ambient graph is seven-connected.  Its conclusion
contradicts `K_7`-minor-freeness.

If a third component `D` exists, then `N_G(D)` is contained in the
nine-vertex boundary.  A neighbourhood of order at most six would separate
`D` from `A` and `B`, so seven-connectivity gives `|N_G(D)|>=7`.  The list
of missed sets in (1.6) is exhaustive: after interchanging `p,q`, a missed
universal vertex is `p`, and a missed pair of cycle vertices has cyclic
distance one, two, or three.  In every listed case `D` meets `4` and `6`
and also meets at least one of `p,0,1`.

The seven branch sets in (1.7) are disjoint and connected.  A direct contact
audit is:

- `{p,0,1}` meets `{q}`, `A union {2}`, `B union {3}`, `D union {4}`,
  `{5}`, and `{6}` through respectively `pq`, `1-2`, `p-3`, `p-4`,
  `p-5`, and `p-6`;
- `{q}` meets every remaining bag through its universal boundary edges and
  the literal vertices included in those bags;
- `A union {2}` meets `B union {3}` through `2-3`, and meets the last four
  applicable bags through fullness of `A`;
- `B union {3}` meets `D union {4}` through `3-4` and meets `{5},{6}`
  through fullness of `B`; and
- `D union {4}` meets `{5}` through `4-5` and `{6}` through a `D`--`6`
  edge, while `{5}` meets `{6}` through `5-6`.

Thus the displayed sets are indeed a `K_7`-minor model.  The additional
recorded contact of `D` with one of `p,0,1` is true but is not needed for
this particular contact list.

## 3. Exact-block and selected-edge responses

For a nonempty independent `I` in `S`, the graph induced by `B union I`
is connected because `B` is full to `S`.  Contracting it is a proper minor.
When the contracted colour is pulled back to every vertex of `I`, there is
no conflict inside `I`, and every edge from `I` to a retained vertex was
represented by an edge incident with the contraction vertex.  Fullness of
`B` makes that vertex adjacent to every member of `S-I`, so no such member
has the pulled-back colour.  This proves the exact-block assertion on the
`A`-shore.  Contracting `A union I` gives the symmetric far-shore assertion.

For a selected edge `e=as`, the restriction of any six-colouring of `G-e`
to `G-A` is proper and realizes its boundary equality partition.  If the
same partition were realized on `G[A union S]`, a permutation of the six
colour names aligns the colours block by block on `S`; it extends to a
permutation of the unused colour names.  Gluing is proper because the two
exclusive shores are anticomplete.  It would six-colour `G`, a
contradiction.  The argument is symmetric for the `B`-shore.

## 4. Application and trust boundary

In the atomic application, neither `q'` nor `h` belongs to
`Z={a,b,c,d,e,f,g,x,q}`.  Hence absence of a `q'`--`h` path whose internal
vertices avoid the eight branch vertices and `q` is exactly the statement
that `Z` separates `q'` from `h`.  An inclusion-minimal separator contained
in `Z` therefore satisfies Theorem 1.1.  If the first-hit theorem's global
order-seven-separation alternative has already been excluded, its order is
eight or nine.

The proof relies on the established case `HC_5` and on the separately
audited generic exact-seven response, two-full-shore boundary-absorption,
cycle-boundary completion, and arbitrary-subdivision first-hit results.
The computer-assisted finite classification inside the boundary-absorption
dependency remains within that dependency's recorded software trust
boundary; this audit checks its hypotheses and use here rather than rerunning
that census.

The theorem does not align the two closed-shore colourings, reduce an
order-eight or order-nine boundary to order seven, preserve the old atomic
branch-set ownership inside a shore, or establish a strict same-form
reduction.  Those are scope limits, not gaps in the audited claims.
