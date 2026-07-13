# Audit: critical private portal columns

## Verdict

**GREEN AS STRENGTHENED.**  Anti-domination and the three-column theorem
are correct.  The claimed sharp threshold at three was not: every
four-set antichain also satisfies Hall.  The note now includes the sharp
four-column theorem and the first failure at five sets.

For nonadjacent `x,y`, inclusion `N(x) subseteq N(y)` lets a colouring of
`G-x` extend by giving `x` the colour of `y`; this proves the critical
neighbourhood antichain.  Equal internal profiles therefore make the
outside profiles incomparable.  Nonemptiness follows when there are at
least two such vertices (the original unrestricted statement needed this
qualification).

For an antichain of order at most four, every subfamily satisfies Hall:
an antichain of three sets needs a ground set of order at least three, and
an antichain of four sets needs one of order at least four.  Five of the
six two-subsets of a four-element set give the sharp failure.

The Gate A application is correctly limited.  A triple on one side of a
`K_{3,3}` block exports three distinct first neighbours, but their labels,
continuations, and compatibility with an exact-seven boundary state are
not controlled.

`critical_private_columns_verify.py` reports:

```text
antichains of order at most four checked: 182
five-set threshold counterexample: [[0, 1], [0, 2], [0, 3],
                                    [1, 2], [1, 3]]
Mycielski K3: 4-vertex-critical; three outside profiles on three endpoints
rooted K4 exists but carries no prescribed state labels
```

The exact state-forcing completion and the vertex-critical warning are in
`hadwiger_critical_capacity_three_state_forcing.md`.

## Atomic three-pair linkage audit

Theorem 3.2 of that note is **GREEN AS SCOPED**.  After contracting the
three disjoint connected two-vertex sources, set-Menger either gives three
disjoint source-to-distinct-target paths or a separator of order at most
two.  A separator containing zero contracted sources lifts with order at
most two; one containing one source lifts with order at most three.  In
both cases unremoved sources and targets certify a genuine disconnection,
contradicting four-connectivity.  The only possibility is the two-source
separator, whose inverse image is exactly four vertices.

When `H=G-Q`, deleting the neutral triangle as well lifts this to the exact
seven-vertex separator `Q union C_i union C_j`.  This is a structural
exact-seven state, not yet a common colour-extension state.

The linkage outcome also needs one further check before Theorem 3.1 can
be invoked: its three paths may consume vertices of the intended
`Q`-full reservoir branch `B_0`.  Four-connectivity protects the three
source pairs and targets but does not reserve `B_0`.  Thus Theorem 3.2
substantially narrows the atomic block to columns or an exact seven-cut,
while reservoir preservation and proper-minor state synchronization remain
the exact two gaps.
