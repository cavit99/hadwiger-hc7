# Independent internal audit of the concentrated three-owner reduction

**Verdict:** GREEN for the exact source revision

```text
results/hc7_three_owner_order8_exact7_reduction.md
SHA-256 b13976c72c59e4d25a697bc390f6fda92364b0efe945bcf29f466d0e12e088e2
```

This is a separate internal mathematical audit, not external peer review.
The audit checked the fan--Menger separation, every branch-set reassignment,
the relaxed first-hit rank, the all-direct absorption, and the final
singleton contradiction.

## 0. Imported hypotheses

The three imported theorem packages are exact and pinned by their own GREEN
audits.  They supply all facts used in this reduction:

* `U_0=U' union (W-C)` is connected, contains the prescribed donor root,
  and is adjacent to `C` through the internal transversal;
* the complete owner set is exactly the three named owners, so `U'` retains
  every donor contact to a nonowner, while the fixed response edge retains
  the donor contact to `D`;
* all three owner portal sets lie in `C`, and `C` has exactly one boundary
  vertex in each outside branch set;
* the selected model first maximizes the relaxed literal first-hit rank and
  then minimizes donor order among models preserving the roots, boundary
  partition and response subgraph; and
* for each pair of owners, the two-edge corollary supplies contact edges
  whose donor-side ends are distinct vertices of `C`.

These are literal host and branch-set statements.  No step replaces a named
branch-set label by a palette colour.

## 1. Fan failure gives an actual order-seven separation

The component `C` has a neighbour `v` of at least one member `k_1` of the
two-vertex internal transversal.  Only this one edge is needed to connect
the later donor seed to the retained donor `U_0`.

In the induced graph on `C` and the three owner representatives, failure of
a three-fan from `v` gives a vertex set `Z` of order at most two meeting
every path from `v` to those representatives.  If `A` is the component of
`v` after deleting `Z`, no surviving owner representative lies in `A`.
The vertex form of Menger permits `Z` to contain target representatives;
this causes no loss, because `|Z|\le2` leaves at least one of the three
representatives outside `Z`.
Every edge leaving `A` in the host therefore ends either in `Z` or in one
of the other five vertices of the literal eight-boundary.  Hence

\[
 |N_G(A)|\le |Z|+5\le7.
\]

At least one of the three owner representatives survives outside `Z` and
is not adjacent to `A`; it supplies a nonempty opposite side.  Thus
`N_G(A)` is an actual separation boundary.  Seven-connectivity makes its
order exactly seven.  No unlisted neighbour of `A` is possible because
the full host neighbourhood of `C` is the displayed eight-set.

## 2. The three-fan partition is valid

In the fan outcome, truncating at the owner representatives leaves three
paths which meet only at `v` and otherwise lie in `C`.  Their internal
vertex sets are pairwise disjoint connected seeds.  Together with the
donor seed `{v}`, they form a disjoint seed family in `C`.  Every component
of the remaining induced subgraph meets at least one nonempty seed by
connectedness of `G[C]`; assigning it to one adjacent seed therefore gives
a connected partition

\[
 C=C_0\mathbin{\dot\cup}L_1\mathbin{\dot\cup}L_2
                         \mathbin{\dot\cup}L_3,
\]

where empty owner arms remain empty.

The new donor `U_0 union C_0` is connected through the selected edge
`vk_1`.  A nonempty owner arm is joined to its old owner by the last path
edge and to the donor by the first; an empty arm means the fan path is the
direct owner-contact edge.  The complete owner-set definition retains all
nonowner contacts in `U' subseteq U_0`, while the fixed response edge
retains the `D` contact.  The old owner branch sets themselves are never
reduced, so every other labelled adjacency and every prescribed root
survives.  The construction is spanning.  Consequently it either repairs
the old `X-Y` nonadjacency and gives an explicit `K_7`-minor model, or is a
compatible spanning labelled near-complete model.

## 3. Rank preservation and strictness

A ranked first-hit path with terminal label other than `U` avoided the
whole old donor and hence all transferred pieces.  A ranked `U`-path whose
old endpoint is transferred is replaced from its same designated port
inside the fixed connected response subgraph and then across the fixed edge
into `U'`.  This is precisely the audited rank-preserving transfer and does
not alter the selected boundary partition or roots.

If one fan arm has an internal vertex, that nonempty seed remains outside
the new donor.  Thus the donor order strictly decreases, contradicting the
maximum-rank, minimum-donor choice unless the construction already gave a
`K_7` minor.  Therefore every owner arm is direct in a surviving fan.

## 4. The all-direct case and singleton contradiction

When all three arms are direct, `v` is adjacent to all three owner
representatives.  Let `Q` be a component of `C-v`.  Componenthood and the
exact internal neighbourhood of `C` show that, if `Q` met no outside branch
set, then

\[
                         N_G(Q)\subseteq\{v,k_1,k_2\},
\]

contrary to seven-connectivity.  Assign every such component to one outside
branch set which it meets.  The union with that old branch set remains
connected even when several components receive the same label.  Replacing
the donor by `U_0 union {v}` is therefore a spanning, label-preserving
reassignment.  The three direct edges retain all owner contacts; `U_0`
retains every other donor contact; and the same first-hit-rank argument
applies.  If `|C|>1`, the donor strictly decreases.  Hence a surviving fan
would force `C={v}`.

The audited concentration theorem's two-edge corollary supplies, for any
two owner labels, two contact edges with **distinct** endpoints in `C`.
That is impossible for the singleton `C`.  Thus the fan outcome is wholly
excluded and the order-seven separation is unavoidable.

## 5. Trust boundary

The source theorem is an unbounded host-level closure of the concentrated
three-owner boundary-full order-eight branch.  It does not prove that the
two closed shores of the returned order-seven separation induce one common
boundary equality partition.  It also does not show that every remaining
degree-seven configuration enters the concentrated three-owner hypotheses.
The next proof obligation remains operation-specific colour gluing or a
strict state-preserving descent at the returned exact boundary.
