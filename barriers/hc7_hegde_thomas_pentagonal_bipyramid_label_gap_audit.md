# Audit: Hegde--Thomas pentagonal-bipyramid label gap

**Verdict:** GREEN at the stated finite and literature scope.

**Barrier revision checked:**
`c72ee65b7a596a5de208dce49be8fa89f527b8810856bcbf7d62528a96e4737d`

**Probe revision checked:**
`d53e66678231eca6afc5d298a522f6cddd370b137feb974ee3cd756f7bbbadd3`

## Checks

1. The pentagonal bipyramid is a planar triangulation.  Hence Hegde--Thomas
   enlargement operations 2, 4, 6 and 7 have no instance; the probe correctly
   generates operations 1, 3 and 5.
2. The operation-5 generation is exact.  For every old edge, the program
   identifies its two facial third vertices.  It orients the two conforming
   splits so clone 0 retains the old edge, forces the other clone at each end
   across opposite incident faces, and adds the clone-1 edge.
3. The first displayed failure is a genuine operation-5 split of the edge
   `bc_0`, along its two opposite incident faces.
4. For fixed root sets, every other vertex is assigned either to one of the
   five branch sets or to the unused set.  This exhausts all rooted minor
   models on graphs of order at most nine.
5. For the paired-portal check, the program enumerates every nonempty
   connected vertex set meeting both portal sets and every unordered
   five-tuple of pairwise disjoint, pairwise adjacent such sets.  Thus the
   reported 140 failures among 800 endpoint choices are exact.
6. In the first paired failure, both portal sets are exactly the five unsplit
   vertices together with clone 0 in each split fibre, as asserted.

## Trust boundary

The computation does not refute a theorem using five-connectivity,
seven-chromaticity, contraction-criticality, extra portals, or a dynamic
proper-minor colouring response.  The explicit enlargement is only weakly
four-connected.  It refutes only the inference that the abstract
Hegde--Thomas enlargement, even supplied with one prescribed portal per side
in each old fibre, automatically contains the required paired-rooted
`K_5`-minor model.
