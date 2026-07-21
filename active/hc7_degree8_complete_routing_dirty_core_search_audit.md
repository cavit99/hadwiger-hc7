# Independent audit: complete-routing dirty-core finite search

**Verdict:** **GREEN** for the exact finite searches and scope statements at
the revision below.  This is a separate internal cold audit, not external
peer review and not an unbounded mathematical result.

## Exact revision audited

```text
17538099fdbada3a7a6ec1b4ac9db0886a509014e48fbe469f06f28716cdcf7e  active/hc7_degree8_complete_routing_dirty_core_search.py
```

Any change to the construction, enumeration, asserted counts, or scope
requires renewed audit.

## Reproduction

I ran

```text
.venv/bin/python active/hc7_degree8_complete_routing_dirty_core_search.py
```

The program completed successfully and returned the asserted histograms.  In
the additive search it found `39` routed patterns, with minimum-defect
histogram `{0: 18, 1: 21}`; the seven patterns retaining the exact literal
root graph all have minimum defect one.  In the balanced atlas it found all
`64` graphs to have a rooted `K_5`, `16` to have a dirty two-defect
certificate, `24` to be five-chromatic with colourful roots, and `9` to be
both dirty and colourful.  All `24` colourful graphs pass all five deletion
colouring and rooted-`K_4` gates.  The deleted-colour contact enumeration
returned the individual-contact histograms `{4: 320}`, `{4: 120}`, and
`{4: 45}` for, respectively, all graphs, the colourful subfamily, and the
dirty-colourful subfamily.  Thus every one of the `320` graph/deleted-root
instances has a residual rooted `K_4` whose four bags all contact the deleted
root.

## Encoding audit

The first search starts from the retained ten-vertex slice, whose displayed
colouring, two dirty paths, rooted bags, and exact defect set `{ae,bc}` are
checked directly.  With the original `D` colour containing only `d`, a
nonliteral `b`--`d` bichromatic path requires another `D`-coloured vertex.
After adjoining it, the six possible `B`--`D` edges give exactly `2^6=64`
patterns.  For each routed pattern, assignment of every nonroot vertex to a
root bag or to no bag exhausts all labelled rooted minor models on that
vertex set.

The second search is an exact atlas only for its stated rigid family: two
vertices in each fixed colour class; literal root edges `ab,cd`; the unique
three-edge bichromatic `P_4` on every nonliteral root pair; and arbitrary
choices of the other three cross-edges on each literal pair.  There are six
such optional edges, hence `64` graphs.  The code checks all ten routes, the
two disjoint length-three shortest paths for `ae,bc`, every allocation of the
five mates to five rooted bags or no bag, and every dirty two-defect
certificate.  The backtracking colouring test exhausts proper colourings,
and the deletion tests exhaust both root collisions in four colourings and
rooted `K_4` allocations.  For each deleted root, the contact routine assigns
each of the four remaining nonroots to one of four fixed rooted bags or to no
bag, checks connectedness and all six quotient contacts, and maximizes the
number of bags meeting the deleted root's residual neighbourhood.  Those
`5^4` assignments exhaust all residual rooted models; returning early at
four is exact because four is the absolute maximum.

The common rooted `K_5` witness is independently valid in every atlas graph:
its bags are

```text
{ra,ma,mc,md}, {rb,me}, {rc}, {rd}, {re,mb}.
```

All their connectedness and pairwise-adjacency claims use mandatory edges,
not any optional edge.  This also independently explains the count `64` for
the same explicit model.

## Trust boundary and research status

The enumeration is finite evidence about two explicitly bounded families.
It does not enumerate all completely routed five-colour cores and proves no
case of the open unbounded five-root property-`(*)` problem.  It also omits
`K_7`-minor exclusion, contraction-criticality, a full degree-eight host,
and an aligned host-level separator or strict reduction.  Since every graph
in the balanced atlas already has a rooted `K_5`, the search supplies no
counterexample.  Its universal contact-four profile is positive finite
evidence for an existential-over-the-deleted-root contact strategy, but does
not prove such a strategy in an arbitrary core.

Accordingly, these results are consistent with, but do not establish, the
current unbounded requirement: obtain a `U`-rooted `K_5` or a literal aligned
host separator/reduction from the special degree-eight hypotheses.  The
script correctly makes no stronger claim.
