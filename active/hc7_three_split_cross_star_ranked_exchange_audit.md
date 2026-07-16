# Cold audit: cross-star and three-split ranked exchange

**Verdict:** **GREEN** for Sections 2--4, 7, and 8 of
[`hc7_three_split_cross_star_ranked_exchange.md`](hc7_three_split_cross_star_ranked_exchange.md).
Section 5 remains explicitly unproved and was not promoted.

**Audited source SHA-256:**
`c7876b9eec10cf6083b659114975165ae249f4b15ff6eae312b0ce470025c534`.

**Current source SHA-256:**
`2872cdf6015aa49b345bdf98a45440a7d1a561208220ee823d551dd0734da577`.
The only post-audit change was the status line recording this audit.

The cold audit checked the following load-bearing points.

* The complement of an irredundant support-six model has exactly two
  representation-invariant nontrivial star components.  Its possible
  two-vertex bags are precisely the choices of a one-cover from each.
* A support crossing a separation does so through exactly one of those
  defect stars.  An independent enumeration reproduced all 50 defect
  patterns and 440 valid shore placements, with zero failures and the
  digest printed in the source.
* Meet and join preserve fixed literal roots and the declared side of
  every named model.  Submodularity and connectivity force both corners
  to retain exact order, so rooted open-shore order is a strict rank for
  nonnested oriented shores.
* In the three-predecessor theorem, every replacement six-cut contains all
  three contraction images.  The three lifts are therefore synchronized,
  and pairwise disjoint named supports rule out a two-vertex transversal
  before any pullback is attempted.
* For the punctured cube, matching is exactly what keeps every
  noncontracted row proper.  The three-, four-, and five-colour
  recolourings are valid.  Strong contraction-criticality is genuinely
  required for the multi-edge contraction colourings and for the upper
  bound on `chi(G-F)`.

The audit does not claim the anchored cross-star exchange target in
Section 5, does not compose the three synchronized predecessor states,
and does not turn the punctured cube into its missing all-proper state.
