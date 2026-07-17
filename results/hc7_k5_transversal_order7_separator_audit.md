# Audit of the two-vertex `K_5`-transversal separator theorem

**Verdict:** GREEN (separate internal audit)

**Audited theorem revision:** SHA-256
`069bfa0dd96211d44e762cc49aaa2476a4e655f52ba45e63e492bb6445411023`
of `hc7_k5_transversal_order7_separator.md`.

## Checks performed

Deleting a two-vertex transversal leaves a `K_5`-minor-free graph.  Its
order is at least six, so the sharp bound `e<=3n-6` applies and gives a
vertex of remaining degree at most five.  Restoring the two deleted
vertices gives total degree at most seven, while seven-connectivity gives
the reverse inequality.

The degree-seven vertex cannot be universal.  Proper-minor colourability
and `chi(G)=7` make its deletion exactly six-chromatic; `HC_6` then gives
a `K_6` minor which universality would extend to `K_7`.  A non-neighbour
therefore exists, and the displayed pair has boundary exactly the seven
neighbours and two nonempty open sides.

## Scope

The theorem proves that the fixed-pair outcome implies an actual
order-seven separation.  It does not produce either outcome.  No
unresolved gap remains in the stated implication.
