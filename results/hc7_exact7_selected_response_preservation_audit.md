# Independent audit of exact preservation of a selected separator response

**Verdict:** **GREEN** for Theorem 1.1, Corollary 2.1, Lemma 3.1 and
Corollary 5.1 at the exact source revision below.

**Audited source:**
`results/hc7_exact7_selected_response_preservation.md`

**Audited source SHA-256:**

```text
94c154ce0d8d9bebaaff2ff97df66beb3e2381bb242378df38d9620ed8ec36e0
```

The theorem and proof are unchanged from the independently checked revision;
the refreshed hash records only the source status-line update.

This is a separate internal mathematical audit, not external peer review.
The contextual descriptions in Section 4 are retained as trust-boundary
motivation; the verdict concerns the named theorem, corollaries and lemma.

## 1. Exact response reflection

The sets `Z_i=V(P_i) union B_i` are pairwise disjoint: the `P_i` are
pairwise disjoint in the open shore, the blocks `B_i` partition the
remaining boundary vertices, and open-shore vertices are disjoint from the
boundary.  Each `Z_i` is connected by hypothesis.  Because both `P_i` and
`B_i` are nonempty, contracting a spanning tree of `Z_i` contracts at least
one open-shore--boundary edge.  The resulting minor is therefore proper.

The contracted images `z_i`, together with the literal vertices in `U`,
form a clique with exactly one vertex for every block of `Pi`.  The three
carrier conditions supply respectively connectivity, adjacency between
different contracted blocks, and adjacency to `U`; the vertices of `U`
are mutually adjacent by hypothesis.  A proper `q`-colouring of the minor
therefore gives distinct colours to all boundary blocks.

Expansion is valid on the untouched closed shore.  Give every vertex of
`B_i` the colour of `z_i`.  The block is independent, and every edge from
it to an untouched vertex maps to an edge incident with `z_i` in the
minor.  The clique of representatives prevents any two different blocks
from receiving the same colour, so the resulting boundary equality
partition is exactly `Pi`, not merely a coarsening.

The original colouring on the other closed shore has the same equality
partition.  Its boundary colours can be matched block by block and the
resulting injection extended to a permutation of the full palette.  The
two proper colourings then agree on the separator and glue because there
are no edges between the open shores.  This proves Theorem 1.1.

The independent minor-model assertion is also correct.  When
`m+|U|=q+1`, the connected sets `Z_i` and the singleton vertices in `U`
are pairwise disjoint and pairwise adjacent, hence are branch sets of a
`K_{q+1}` minor without any colouring assumption.

## 2. Two boundary-full subgraphs and one duty subgraph

In Corollary 2.1 assign the duty-meeting subgraph `Z` to the selected block
`D` and the two boundary-full connected subgraphs to the other two blocks
among `M,{x},{y}`.  Boundary fullness makes each assigned block union
connected, supplies all pairwise adjacencies between the three block
unions, and supplies every required adjacency to `K` except possibly for
the block assigned to `Z`.  For that block, a missing boundary edge to a
vertex `k in K` is exactly why `k` is included in the duty set
`D_K(D)`, and the stipulated contact of `Z` supplies the missing adjacency.
Thus the three subgraphs form precisely the carrier system required by
Theorem 1.1.  No palette colour is being identified with a model label.

## 3. Failed-edge placement and demand

After expanding the simultaneous contraction, the only possibly improper
edges are the two named failed edges, whose endpoints are monochromatic.
A raw restriction to a closed shore is therefore proper exactly when that
shore contains neither failed edge.  The three placement cases in Lemma
3.1 follow immediately and keep the two shore orientations distinct.

For the demand inequality, choose a maximum clique `U` among the vertices
which are singleton blocks of `Pi`.  The number of remaining blocks is

```text
d_{G[S]}(Pi)=|Pi|-|U|.
```

If this number were at most the number of disjoint boundary-full connected
subgraphs on the same coloured shore, assigning one such subgraph to each
remaining block would give the carrier system of Theorem 1.1 and hence a
six-colouring of the host.  This proves the strict inequality in the
hypothetical-counterexample setting.

Theorem 1.1 assumes at least one non-`U` block.  A parameter-free statement
would therefore need to mention the degenerate value `d=0` separately.  In
Corollary 5.1 the setting is an exact seven-vertex boundary with `q=6`, so
at most six boundary blocks are available and at least one block is
non-singleton.  Hence `d>=1` there automatically, and no `d=0` gap occurs.

## 4. The oriented exact-seven conclusions

For Corollary 5.1(1), the maximum-clique choice above and the automatic
positivity of the demand put the situation exactly within Theorem 1.1.

For item 2, let `I` be any nonempty independent subset of the seven-vertex
boundary.  Every component of either open shore is adjacent to every
literal boundary vertex: otherwise its full neighbourhood would have
order at most six and would separate it from the nonempty opposite shore,
contrary to seven-connectivity.  Contracting one such component together
with `I` gives a proper minor.  Restrict a six-colouring of that minor to
the opposite closed shore and expand `I`.  Fullness makes the contracted
vertex adjacent to every boundary vertex outside `I`, so `I` is an exact
block of the resulting boundary partition.  Reversing the shores proves
that both extension languages meet every exact-block cylinder.  The
audited split-boundary synchronization theorem applies because
`chi(G[S])<=4=6-2`, and excludes a split boundary.  This verifies both the
proper-minor expansion and the shore orientations.

Item 3 is exactly the contrapositive of Corollary 2.1 on the same coloured
shore: if any connected subgraph disjoint from the two fixed full
subgraphs met every vertex of one duty set, the selected partition would
reflect and the host would be six-colourable.

## 5. Trust boundary

The audit proves that a partition-specific connected-subgraph certificate
is sufficient to reflect one exact boundary response.  It does not prove
that a first-hit rank deficiency supplies that certificate, that the two
boundary-full subgraphs survive after an arbitrary new separator is
chosen, or that a simultaneous-contraction assignment is proper on a
closed shore containing one of its failed edges.  It also does not make
the two differently oriented response partitions coincide.

Within the theorem's explicit orientation, exact-seven and carrier-system
hypotheses, no unresolved gap was found.
