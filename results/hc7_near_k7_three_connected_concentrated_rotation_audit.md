# Audit: 3-connected concentrated rotation

## Verdict

**GREEN for Theorem 2.**  Corollary 3 is a correct localization statement
and explicitly does not lift virtual torso edges.

## Checks

1. The `st`-numbering lemma is used safely after adding a possible
   artificial `st` edge.  That edge crosses every proper prefix/suffix
   cut and is internal to neither side, so it is not needed for the
   asserted connectivity in the original graph.
2. The theorem now states its exact local hypothesis: `G[U-r]` is
   2-connected and `r` has at least two actual neighbours inside `U`.
   The prefix cut puts one such neighbour on each side, yielding both
   required core-to-piece edges.  Three-connectivity of `G[U]` is a valid
   sufficient condition.
3. The two moved parts contain distinct selected neighbours of `X`, while
   `{r}` contains a third.  Thus all connectivity and rooting hypotheses
   of the one-donor rotation theorem are literal.
4. A moved part missing a twin has a whole connected far bag outside the
   part and its open neighbourhood, so the separator output is actual.
   No internal connectivity of the complement is assumed.
5. Outside that separator branch, both parts meet both twins and can be
   assigned in either order.  The six bags in (2.6) are pairwise adjacent:
   `X` uses the two selected roots for the new twin contacts and its old
   contacts for `V_i`; every other edge is inherited from the old `K_6`
   model.
6. The singleton core meets the enlarged twins through the two partition
   cut edges and meets `X` through the protected root.  It can lose only
   the three untouched neutral rows, exactly as claimed.
7. A one-missing model is admissible as a `K_7^vee` comparison by leaving
   a second centre spoke unprescribed.  Hence either one or two losses
   contradict the global deficient-centre minimum `mu>=2`.  The current
   full shore `X` need not itself be the originally minimizing bag; this
   makes the statement applicable after whole-lobe transport.
8. If all three rows are lost, any untouched neutral bag witnesses a far
   side of `N_G(r)`.  Seven-connectivity/fullness are applied correctly.
9. The result does not cover a non-3-connected donor or prove that one
   selected 3-connected torso contains all four roots.  Those are exactly
   the adhesion-two/web composition outputs retained in Corollary 3.
   Its sharper local corollary correctly says only that every surviving
   selected root fails one of the two explicit hypotheses.
