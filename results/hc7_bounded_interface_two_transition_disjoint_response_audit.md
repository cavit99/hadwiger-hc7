# Independent audit: two-transition disjoint opposite-shore response

**Verdict:** **GREEN** for the exact source revision

```text
5b4a03822ba54efba3a71a3cdabb9f9a8a227d72bed4293ea24081d5cc5d549a  results/hc7_bounded_interface_two_transition_disjoint_response.md
```

This is a separate internal mathematical cold audit, not external peer
review.  Any change to the theorem, proof, operation provenance, or trust
boundary requires renewed audit.

## 1. Exact-block bootstrap

The first failed lift of a shortest exact-singleton transition has a path
through the literal component `C`.  Its two boundary ends lie in distinct
components of one boundary two-colour graph and hence form a boundary
nonedge `e`.  It is therefore valid to use the two vertices of `e` as the
fixed independent block in a second exact-block transition.

The proof fixes a final `B`-extension before applying the canonical
last-interchange dichotomy and the pole normal form.  Every move of the
second transition avoids the fixed colour on `e`.  Consequently every
endpoint of the returned pole-free last path lies in `S-e`; its pair `f`
is disjoint from `e`.  This quantifier is literal and does not rely on the
separately anchored endpoint-response families.

## 2. Path disjointness and localization

The first path has no internal boundary vertex and has interior in `C`.
The second has no internal boundary vertex and has interior in
`B-(S union {u})`.  The endpoint pairs are disjoint, and the two open
sides are disjoint and anticomplete, so the complete paths are
vertex-disjoint.  The localization bound for the second path is exactly the
one already proved in the exact-block reduction: at most three other
components of `G-N[u]`, each meeting at least `|S|-2` boundary vertices.
No arbitrary residual component is treated as a restart.

## 3. Explicit minor lift

A `K_6` model in `G[S]+e+f` can use either added edge within one branch set
or between two branch sets.  Replacing each virtual edge by its literal
path is compatible because the two paths and their four ends are disjoint.
Every resulting branch set retains a vertex of `S`.  The singleton `{u}`
is disjoint from and adjacent to all six branch sets, giving an explicit
`K_7` model.  Thus the asserted residual exclusion
`K_6 not minor G[S]+e+f` follows under the hypothetical-counterexample
hypotheses.

## 4. Trust boundary

The paths arise from two exact-block transitions, not one colouring
operation.  Their existence is nonterminal when the augmented boundary is
`K_6`-minor-free.  The theorem correctly retains as the other alternatives only the
common complete partition, the exact aligned smaller component, and the
tight pole residue; it does not promote a fresh response or arbitrary
separator to a recursive outcome.
