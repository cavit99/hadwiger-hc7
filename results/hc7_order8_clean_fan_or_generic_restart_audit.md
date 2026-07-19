# Independent internal audit of the order-eight fan-or-restart theorem

**Verdict:** GREEN for the exact source revision

```text
ea3fce6948917b3cee0829421424752777f224f84834196323ef471b74b4080c
```

of
[`hc7_order8_clean_fan_or_generic_restart.md`](hc7_order8_clean_fan_or_generic_restart.md).
This is a separate internal audit, not external peer review.

## 1. Scope checked

The audit checked the exact output of the operation-coupled order-eight
theorem, the new full-neighbourhood separation, the nonempty opposite
shore, the selected edge-deletion response, and the minimum-shore
inequality.

## 2. Findings

The cited theorem places the returned connected nonempty set `A` inside
`C_0-({v} union Z)`, so `A` is a literal proper subset of `C_0`.  It gives
`Y=N_G(A)` and `|Y|=7`.  A far component `C_i`, `i>0`, has no edge to
`A subseteq C_0`; hence it is disjoint from `Y` and remains wholly in the
opposite open shore.

Every boundary vertex has an `A`-neighbour by the definition of the full
neighbourhood.  Deleting any crossing edge produces a proper minor and
therefore a six-colouring.  Its endpoints must have one colour, or the
edge could be restored.  This is exactly the selected response required by
the generic-interface definition.

Under the explicit hypothesis `C_0 subsetneq A_0`, the returned shore has

\[
                         |A|<|C_0|<|A_0|,
\]

contradicting global minimum generic-shore order.  Thus the clean-fan
conclusion follows without preserving old labels or an old partition.

## 3. Trust boundary

The theorem applies only to the already normalized operation-coupled
two- or three-component interface and the stated containment in a minimum
generic shore.  It does not allocate the clean paths to distinct model
labels, retain a connected residual, or complete a `K_7` model.  No
unresolved assumption remains in the stated result.
