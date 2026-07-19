# Audit of opposite colouring responses forced by an unresolved two-cut

**Verdict:** GREEN.

**Audited source:**
`results/hc7_order8_two_cut_opposite_response.md`

**Audited SHA-256:**
`6e835cf883366f6a2c06095cbf28d9e621dc9e2920f62ddef7f74cb7d9d50671`

**Promoted source SHA-256:**
`d7bf19ae1f0575a0580215c56d9fcb253263dfd57a0964971f97c4dea10b3f51`

The promoted revision changes only the status line and adds the audit link;
the theorem and proof audited below are unchanged.

**Audit type:** independent internal mathematical audit.  This is not
external peer review and does not prove `HC_7`.

## Findings

Two-connectivity does force each of the two lobes to have neighbours at
both cut vertices.  If a cut vertex sees `d`, adjoining it to `L_d`
repairs the sole missing boundary contact and gives a full connected
subgraph adjacent to `L_e`.  One of two disjoint odd cycles avoids `e` and
has order three or five.  There is another boundary vertex outside that
cycle and distinct from `e`, so the full subgraph may be assigned that
artificial defect.  The short-cycle branch-set lemma applies exactly.
Symmetry excludes every cut-vertex contact to either `d` or `e`.

It follows that assigning the two cut vertices to opposite lobes gives
disjoint connected adjacent subgraphs covering `C`, with exact boundary
neighbourhoods `S-{d}` and `S-{e}`.  Neither cut vertex can repair a defect.

If deletion of `d,e` leaves a nonbipartite boundary, a shortest odd cycle
on the remaining six vertices has order three or five, so the same
short-cycle lemma gives a `K_7` minor.  In the bipartite case, both disjoint
odd cycles must meet `{d,e}`.  Their disjointness forces one to contain only
`d` and the other only `e`; deleting the distinguished vertex leaves an
odd-length path.  Thus both bipartition classes are nonempty and each of
`d,e` sees both classes.

If `de` is present, every hypothesis of the promoted adjacent-defect
reflection theorem holds and `G` is six-colourable.  If `de` is absent,
the promoted opposite-response theorem applies with open shores `C` and
`Q_0 union Q_1`.  Since `G` is not six-colourable, the response sets are
opposite singletons.  The bichromatic-path statement and its orientation
are correct.  When the `Q_0 union Q_1` shore has the unequal response, the
promoted localization theorem forces each such path to meet that union
internally.

The phrase “every colouring of the second type” is understood in the
precise sense defined by the cited response theorem: every colouring in
the prescribed response family, with the two bipartition classes
monochromatic and distinct and the roots avoiding those two colours.  It
does not quantify over arbitrary colourings of the closed shore.

## Dependency checks

The audit checked the exact hypotheses of:

- the short-cycle lemma in the strict-reversal completion;
- the adjacent-defect reflection theorem; and
- the opposite-response and path-localization theorems.

No palette colour is identified with a branch-set label.

## Trust boundary

The theorem reaches but does not eliminate the opposite-response normal
form.  It does not split a full component at a forced path's first hits,
produce compatible response types, or return an order-seven separation.
Within the stated conditional two-lobe setting, no mathematical gap was
found.  Safe to promote with the source hash above.
