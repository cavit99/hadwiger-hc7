# Independent audit: exact singleton-block Kempe exchange

**Verdict:** **GREEN** at the exact source revision below.

**Audited source:** `hc7_exact7_singleton_block_kempe_exchange.md`,
SHA-256

```text
d0157bc10b6f588a7e7fd714b1e5be02faee3da35f2d35ce43cf03f5237c91e2
```

This exact-revision pin supersedes the legacy unpinned form of this audit.
The lemma was reconstructed directly from the two components of the
induced bichromatic graph.  This is a separate internal mathematical audit,
not external peer review.

Let `alpha=c(x)` and `beta=c(y)`.  Since `{x}` and `{y}` are distinct
singleton blocks of the equality partition on `S`, `alpha!=beta`, and no
vertex of `S-{x,y}` has either colour.

In the two-colour graph induced by the `alpha` and `beta` classes, the two
component cases are exhaustive and exclusive for the stated procedure.

* If `x,y` lie in different components, swapping `alpha,beta` on the
  component containing `x` preserves properness.  That component contains
  no boundary vertex other than `x`: it cannot contain `y` by assumption,
  and no other boundary vertex has either colour.  Thus `x` acquires
  `beta`, `y` retains `beta`, and every other literal boundary colour is
  unchanged.  The exact new equality partition is obtained by merging only
  `{x}` and `{y}`.  The hypothesis `xy` is absent is consistent with, and
  necessary for, this merged boundary colouring to remain proper.
* If `x,y` lie in the same component, a shortest path between them uses
  only `alpha,beta`.  No internal vertex can lie in `S`, because every
  internal path vertex has one of those two colours and the only boundary
  vertices with those colours are `x,y`.  Since `xy` is absent, this path
  is nontrivial and has an internal vertex outside `S`.

For `J=G[R union S]`, the second outcome is therefore a literal
bichromatic path whose internal vertices all lie in the open shore `R`.
The audit confirms the stated limitation: the lemma supplies no
disjointness from packets, branch sets, or reserved connectors.

No minor operation occurs in this lemma, so no proper-minor hypothesis is
being used implicitly.

At the pinned revision, the exact scope is also GREEN: the path need not
avoid any preselected full connected subgraphs, branch sets, or connectors.
For a closed shore `J=G[R union S]`, the conclusion that all internal path
vertices lie in `R` uses only `V(J)-S=R`; no connectivity or
minor-criticality hypothesis is hidden.
