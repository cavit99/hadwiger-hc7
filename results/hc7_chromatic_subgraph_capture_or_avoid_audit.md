# Audit of chromatic subgraph alignment or separation

**Verdict:** GREEN.

Audited source:
`results/hc7_chromatic_subgraph_capture_or_avoid.md`.

Source SHA-256:
`ac6b2b0a879c6b75dd93ac2f8ada48aa27cf09655c866b2d5eec0a57f74ea97f`.

This was an independent line-by-line audit against Lemma 2.1 and Lemma 2.2
of Girão--Illingworth--Mohar--Norin--Steiner--Tamitegama--Tan--Wood--Yip,
*The Dominating 4-Colour Theorem* (arXiv:2605.10112).

## Checks

1. In Theorem 2.1, reusing the contracted vertex's colour on one colour
   class of `X` is valid: every outside neighbour of `X` is adjacent to the
   contracted vertex in the quotient. The expansion therefore uses at most
   `4+(r-1)=r+3` colours.
2. The ordered-edge case split is exhaustive. If the contracted vertex is
   omitted and the marked neighbour occurs, compatibility puts that
   neighbour in the first branch set; adding the contracted vertex along
   their edge and then lifting is valid.
3. In Theorem 2.2, normalization leaves the first two branch sets fixed and
   shrinks only the final three. It therefore preserves omission of the
   contracted vertex and produces the stated induced cycle. If the first
   branch set and the contracted vertex are in one component after deleting
   the final four branch sets, absorbing that component preserves
   connectedness, disjointness, domination, and the normalized cycle.
4. In Theorem 3.1, the two contracted vertices are adjacent and hence have
   different quotient colours. The two remaining fresh palettes are
   disjoint, so the expansion uses at most
   `4+(r_1-1)+(r_2-1)=r_1+r_2+2` colours. Lifting `Y` and then `X` matches
   Lemma 2.2(b) and Lemma 2.2(a), respectively.
5. The separator assertions follow from the component-absorption argument.
   In the marked version, normalize before applying that argument; omission
   of the marked neighbour is preserved.
6. Corollaries 4.1 and 4.2 follow. Under `chi(J)=6`, a shortest route from
   `a` to `b` through a named branch set has a nonempty internal vertex set
   inducing a path in `J`. In Corollary 4.2, every edge leaving the
   `T_1`-side component of `J-S` goes to `S` or to one of the roots in
   `R_E`; hence `S union R_E` is a proper separator. Seven-connectivity
   gives the stated weighted lower bound, with equality an actual
   order-seven separation.

## Scope

The result does not bound the order of the structured separator, force the
aligned branch set to split, or align the other four dominating-model branch
sets with a pre-existing near-`K_7` model. It is not a proof of `HC_7`.
