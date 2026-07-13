# Audit: full state-shore bi-Helly theorem

## Verdict

**GREEN.**  The cross-Helly argument is valid and the full-row condition
really does force a perfect two-by-two contact matching between every pair
of split carriers.

If the two minimal carrier families have no disjoint cross pair, every
left trace subtree intersects every right trace subtree.  When the left
traces are pairwise intersecting, ordinary subtree Helly gives one common
bag.  Otherwise two disjoint left traces determine a joining path, and
every connected right trace meeting both contains that whole path.  Thus
one bag meets every carrier of one state half.  Every nonminimal carrier
contains a minimal one, so the conclusion extends to the full families.

The component/adhesion assertion is also sound: all bag subtrees of one
component outside the common bag lie in one component of the
decomposition tree minus that node, and every neighbour in the common bag
lies in the first adhesion on that branch.

For two extracted shore pairs, each shore in `D_i` meets the portal row
`N_{D_i}(D_j)`, so it has a neighbour in one shore of `D_j`.  Applying the
same fact from `D_j` makes all four vertices of the `2 by 2` contact graph
nonisolated.  Such a bipartite graph has a perfect matching.  The internal
shore adjacency and all state rows are exactly those required by the
connected-shore cocycle theorem.

The scope remains precise: a cycle or 3-connected common torso is a
rooted obstruction, not automatically a literal gate or rural disk.
Virtual edges require expansion through their named lobes.

