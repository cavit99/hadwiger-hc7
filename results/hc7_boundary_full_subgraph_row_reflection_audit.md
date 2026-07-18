# Audit of boundary-full-subgraph row reflection

**Verdict:** GREEN.

**Audited source:**
`results/hc7_boundary_full_subgraph_row_reflection.md`

**Audited SHA-256:**
`2073fad6bd81f3d7a82f18720e719d86656e75587d720a1ed3006ae77a52223a`

The exact revision above was independently audited GREEN after correction
of the pullback sentence.  The correction explicitly colours every
unchanged boundary vertex and does not change the theorem statement.

## Checks

1. A proper colouring of the row-trace conflict graph makes every union
   `J_h` independent.  The connected sets `X_h=P_h union J_h` are
   pairwise disjoint, connected, pairwise adjacent and adjacent to `a`.
2. At least one used `J_h` makes the simultaneous contraction a proper
   minor.  The corrected pullback keeps the minor colouring on every
   unchanged vertex of `(R union T)-bigcup_h J_h`, including `a` and all
   singleton traces, and gives `J_h` the representative colour.  Every
   possible edge type is therefore proper.
3. Every row trace is monochromatic in the resulting unchanged-far-shore
   colouring.  A boundary-free row activates the second hypothesis of the
   audited five-row reflection theorem.
4. If a `T`-full connected subgraph exists and all five rows meet `T`, it,
   `{a}` and the five rows are seven valid branch sets.  Hence `K_7`
   exclusion supplies the boundary-free row used in the corollary.
5. The conflict-capacity inequality and all three stated special cases
   follow directly.

## Trust boundary

The theorem assumes the row traces themselves are independent.  If one
contains an edge, no proper colouring can make it monochromatic.  When the
conflict chromatic number exceeds the maximum number of disjoint
boundary-full connected subgraphs, the theorem gives no linkage, split,
transversal or separator.  It does not prove `HC_7`.
