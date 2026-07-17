# Audit: two-shore rooted-model lift

**Audit status:** GREEN.

**Audited source revision SHA-256:**
`050f0312e98c082a8414f7f01b047e59519802457eca715ddfc8f876b3d48b7a`

This is a separate internal audit, not external peer review.

## Verdict

**GREEN.**  The theorem displays all branch bags explicitly.  Its exact
two-component corollaries use only the already audited pointwise-full
expanded boundary.

## Branch-set audit

The old `K_r` bags lie in `W subseteq S`.  The new bags `A union {u}` and
`B` are disjoint from them and from each other.  The former is connected
through an `A-u` edge; the latter is connected by hypothesis.  An `u-B`
edge joins the two new bags.  For every old bag and each shore, any
boundary vertex in that bag supplies the required shore edge.  These are
all pairwise adjacencies, so the conclusion is literal.

In the minimal bad contraction residue, every expanded boundary atom has
an individual neighbour in each of the two components.  Therefore all
hypotheses apply with `r=5`.  A named footprint with all four core
vertices in the quotient cut expands to a six-vertex boundary `K_5`
model, leaving at least two unused boundary atoms.  It is consequently
forbidden.  No claim is made when the rooted model uses an open-shore
vertex.
