# Audit of the fixed-trace edge-rotation barrier

**Verdict:** GREEN.  The unbounded odd-cycle construction, its fixed-trace
claims, and its stated limitation are correct.  The deterministic verifier
passes and correctly checks the smallest member `n=7`.

**Audited source:**
[`hc7_fixed_trace_edge_rotation_barrier.md`](hc7_fixed_trace_edge_rotation_barrier.md)

**Source SHA-256:**
`0305e20528bf3dccc829a5f9c654f17353f375a69526fdf0277c47610564803d`

The mathematical text is the revision audited originally; the hash above
also includes the later status-only promotion of this audit from pending to
GREEN.

**Audited verifier:**
[`hc7_fixed_trace_edge_rotation_barrier_verify.py`](hc7_fixed_trace_edge_rotation_barrier_verify.py)

**Verifier SHA-256:**
`83ca6a33979b32235856a0b3d0f4428e194b0727ccfcb11fc76bcbdf345d0d7d`

This is a separate internal mathematical audit, not external peer review.

## 1. Construction, connectivity, and chromatic number

The boundary graph is the disjoint union of a four-clique `K` and three
isolated vertices `J`.  The induced odd cycle `R=C_n` is complete to all
seven boundary vertices, while the extra vertex `a` is complete to the
boundary and anticomplete to `R`.  Thus deleting `S=K union J` separates
the two nonempty connected open shores `{a}` and `R`, and each shore is
adjacent to every literal boundary vertex.

After deleting at most six vertices, at least one boundary vertex and at
least one cycle vertex remain.  Every surviving cycle component is joined
through every surviving boundary vertex; all surviving boundary vertices
are joined through a surviving cycle vertex; and `a`, if present, reaches
that connected subgraph through the boundary.  The remainder is connected.
Deleting all seven boundary vertices disconnects `a` from `R`, so
`kappa(G)=7` exactly.

The graph induced by `S union R` is the complete join of `G[S]` and the odd
cycle.  Its chromatic number is therefore

\[
                 \chi(G[S])+\chi(C_n)=4+3=7.
\]

The vertex `a` can reuse a cycle colour because it has no neighbour in `R`,
so `chi(G)=7`.

## 2. Every cycle-edge deletion and contraction

Deleting any cycle edge turns `C_n` into a path on `n` vertices.  Since `n`
is odd, this path has even length, and its two ends belong to the same side
of its bipartition.  Giving the four blocks of `Sigma` four colours and the
path the two remaining colours yields a six-colouring with exact boundary
partition `Sigma`; every such six-colouring makes the deleted-edge ends
equal because the complete join forces the path to use exactly two colours.

The joined subgraph `G[S] vee (C_n-e)` needs at least `4+2=6` colours, so the
deletion is exactly six-chromatic.  Contracting a cycle edge turns `C_n`
into the even cycle `C_{n-1}`.  Its complete join with `G[S]` likewise has
chromatic number `4+2=6`.  The extra vertex `a` does not increase either
number.

In the original closed shore `G[R union S]`, an exact `Sigma` trace consumes
four colours on `S`; none can appear on the complete-to-`S` odd cycle, which
requires three more.  Hence the selected partition has no six-colour
extension through that shore.

## 3. Fixed-list critical kernel and Kempe saturation

Fixing `Sigma` on `S` leaves every cycle vertex the same two-element list.
The odd cycle is not colourable from that list.  Every proper induced
subgraph is a disjoint union of paths and is two-colourable, so the whole
cycle is the unique vertex-minimal induced non-list-colourable subgraph.
This object is independent of which cycle edge is deleted to produce a
response; changing that edge therefore gives no strict kernel-order descent.

Each cycle edge is also Kempe-saturated in its six-colouring response.  If
its equal-coloured ends were separated in the two-colour graph for some
alternate colour, switching the component of one endpoint would make the
edge proper; restoring it would six-colour `G`, contradicting
`chi(G)=7`.  Thus the saturation item in the consequence list is valid.

## 4. Spanning labelled `K_7` model

For

\[
 e=r_{n-1}r_0,\qquad e'=r_3r_4,
\]

the two paths `D={r_0,r_1,r_2,r_3}` and
`U={r_4,...,r_{n-1}}` are nonempty and connected for every odd `n>=7`.
The set `B={a,j_0,j_1,j_2}` is connected through `a`.  Together with the
four singleton vertices of `K`, these are seven disjoint connected sets
partitioning `V(G)`.

All branch-set adjacencies are literal:

* `D` and `U` meet `B` through the complete `R`--`J` join;
* both paths meet every `K` singleton through the complete `R`--`S` join;
* `B` meets every `K` singleton through an edge from `a`;
* the four `K` singletons form a clique; and
* exactly the two cycle edges `e,e'` run between `D` and `U`.

Deleting either of those last two edges preserves the other and hence
preserves the same spanning labelled `K_7`-minor model.  Both deletions have
the same exact `Sigma` response by the previous section.

## 5. Verifier review

The verifier constructs the `n=7` member with 15 vertices and 69 edges:
six edges in `K_4`, seven in `C_7`, 49 in the complete `R`--`S` join, and
seven from `a` to `S`.  Its exhaustive connectivity and backtracking
colourability routines check connectivity seven, chromatic number seven,
and exact chromatic number six after every cycle-edge deletion and
contraction.  Fixing the seven boundary colours explicitly checks the exact
`Sigma` trace and equal deleted-edge endpoints for every deletion.

The contraction routine correctly suppresses the contracted loop and
parallel edges.  The branch-set checks verify disjoint coverage,
connectedness, every pairwise adjacency, and preservation after deletion of
either selected `D`--`U` edge.  The list-kernel check verifies that `C_7` is
not two-colourable and that every single-vertex deletion is; colourability is
hereditary under further vertex deletion, so this suffices for all proper
induced subgraphs.

Running

```text
python3 barriers/hc7_fixed_trace_edge_rotation_barrier_verify.py
```

produces exactly the five documented GREEN lines.

## 6. Exact scope

The example deliberately contains the displayed `K_7` minor.  Contracting
its seven branch sets gives a proper seven-chromatic minor, so the graph is
not minor-minimal among seven-chromatic graphs.  It therefore does not
refute `HC_7`, a `K_7`-minor-free exchange theorem, or a terminal-aware
theorem which permits an explicit `K_7`-minor outcome.

What it does refute is the inference that fixed-trace attainment, repeated
model contact, seven-connectivity, and rotation of the failed edge alone
must strictly shrink the fixed-trace kernel or synchronize the two shore
colourings.  The conclusion that `K_7`-minor exclusion must participate in
any stronger exchange argument is accurately stated.

## Final audit conclusion

Every unbounded claim follows uniformly for odd `n>=7`, and the independent
smallest-instance verifier agrees with the hand proof.  No unresolved
mathematical assumption remains in the stated barrier.  The source and
verifier are GREEN at the pinned hashes above.
