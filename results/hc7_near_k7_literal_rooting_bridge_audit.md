# Audit: arbitrary `K_7^vee` source-bag normalization

## Verdict

**GREEN for the stated partial bridge.**  It bounds every two-connected
neutral bag and every family of detachable branches, but does not yet
extract a literal `K_6^-` transversal through a constant-owner corridor.

## Checks

1. Six literal vertices consisting of a `K_4` and two common neighbours
   leave a connected nonempty remainder in a seven-connected graph.
   Deleting the other five roots shows each root has an actual neighbour
   in that remainder.  If the two common neighbours are adjacent, the
   six vertices and the remainder are seven clique bags; otherwise this
   is exactly the singleton-core shell.
2. For a detachable `X subset U_i`, an empty monopoly set permits literal
   deletion of `X` from the model.  A unique monopoly `V_j` permits the
   transfer `X` into `V_j`: connectivity uses an old `X-V_j` edge, and
   the cut edge between `X` and `U_i-X` restores the `U_iV_j` adjacency.
   Lexicographic minimality therefore forces `j<i`.
3. Monopoly sets of disjoint detachable parts are disjoint because the
   nonempty endpoint set for one model label cannot be contained in two
   disjoint parts.  Singleton monopolies use at most the `i-1` earlier
   neutral labels and every other monopoly has order at least two.  This
   yields the bounds `3,3,4,4` for disjoint detachable parts of
   `U_1,...,U_4`.
4. In a two-connected `U_i`, every singleton deletion is detachable.
   Applying the same count bounds its order by `3,3,4,4`.  For `U_1`,
   equality forces exactly three singleton monopoly pairs partitioning
   the six model labels, so the bag is a triangle with a literal
   `2+2+2` portal allocation.
5. Leaf-block interiors are detachable.  Along a rooted block-cut chain,
   the monopoly set of the detached prefix is monotone; every strict
   change adds a model label, so only a bounded number of owner changes
   occurs.  The note correctly leaves a constant-owner corridor open.
6. The icosahedral join shows that shrinking the initially displayed
   bags in place is false, while a global literal realignment exists and
   lands in the coherent two-apex branch.

## Exact caution

Seven-connectivity gives six alternative paths around a corridor bridge,
but it does not by itself make their entire interiors avoid the old
neutral bag.  Only suitably trimmed cross-segments have that property.
Any continuation must retain their actual endpoints and may not call
them six private `x-y` paths outside the source bag.
