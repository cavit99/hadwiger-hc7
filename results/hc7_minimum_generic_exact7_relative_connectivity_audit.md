# Independent internal audit of the minimum-shore relative-connectivity theorem

**Verdict:** GREEN for the exact source revision

```text
71af2fc88f52e32388fe13b140faf69978ca6faf226433610da2aadd806fddcb
```

of
[`hc7_minimum_generic_exact7_relative_connectivity.md`](hc7_minimum_generic_exact7_relative_connectivity.md).
This is a separate internal audit, not external peer review.

## 1. Scope checked

The audit checked:

1. that an order-seven full neighbourhood of a proper connected subset of
   the chosen shore gives a genuine smaller generic response interface;
2. the passage from connected subsets to arbitrary subsets;
3. every component argument in the boundary-completed graph;
4. the case in which all seven boundary vertices are deleted; and
5. the order-eight boundary-full corollary.

## 2. Findings

The old opposite shore is anticomplete to the selected shore.  It therefore
remains outside every proper connected subset and its full neighbourhood,
so each displayed separation has a nonempty opposite side.  If that
neighbourhood had order seven, deletion of any crossing edge gives a
six-colouring with equal endpoint colours and hence a smaller generic
exact-seven interface.  This verifies the strict minimum-shore
contradiction.

For an arbitrary proper subset, a component of its induced graph has no
edge to the other components, so its full neighbourhood is contained in
the neighbourhood of the whole subset.  This proves the general bound.

In the boundary-completed graph, any component not containing a surviving
boundary vertex lies inside the selected shore and has all actual host
neighbours in the deleted set.  It is a proper subset, so the eight-neighbour
bound excludes it.  If all boundary vertices are deleted, exactly the
seven boundary vertices were deleted and the connected shore remains.

For the order-eight corollary, connectedness of the selected shore and the
properness of `K` ensure that `T=N_G(K)` meets `A-K`.  Thus every component
of `G-T` contained in `A` is a proper subset of `A`; its neighbourhood is
contained in the eight-set `T` and has order at least eight, forcing
equality.

## 3. Trust boundary

The auxiliary clique edges inside the seven-vertex boundary prove only
connectivity of the completed graph and are never treated as host edges.
The theorem gives no opposite-side fullness, colouring synchronization,
separator trimming, or labelled minor-model completion.  No unresolved
assumption remains in the stated result.
