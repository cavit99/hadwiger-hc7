# Audit: bipartite total-contraction split states

## Verdict

**GREEN in the stated scope.**  The theorem applies to a connected vertex
set whose induced graph is bipartite.  It does not align palette colours
with arbitrary model bags.

## Checks

1. If the total contraction had too few colours, one contraction colour
   plus fresh colours on the remaining bipartition classes would expand to
   a forbidden colouring of the original graph.
2. In the list proof every list contains the contraction colour.  Orienting
   a spanning-tree edge toward a side whose list intersection is that
   singleton is sound.  If a vertex has no outgoing edge, each tree branch
   shares a secondary colour; colouring one global bipartition class with
   the contraction colour and the other class branch-by-branch is proper,
   including on non-tree edges.
3. Hence some tree edge has two poor sides, and both connected sides see
   every secondary colour in the same contraction colouring.
4. Separately contracting the two sides makes them adjacent and forces both
   to the contraction colour under the old exterior state, so the localized
   state incompatibility is genuine.  The `|X|>=3` qualification correctly
   ensures this is a proper minor.
5. The rooted shortest-path corollary separates its two prescribed ends and
   retains literal connected branch sets.

The remaining palette-to-label conversion is not part of this result.
