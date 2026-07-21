# Independent audit of the strengthened dirty two-bridge-chain barrier

**Status:** separate internal audit GREEN, 21 July 2026.

This is an internal mathematical and computational audit, not external peer
review.  The auditor did not author the barrier or its verifier.

## Revisions audited

- strengthened barrier:
  [`hc7_atomic_dirty_two_bridge_chain_barrier.md`](hc7_atomic_dirty_two_bridge_chain_barrier.md)
- barrier SHA-256:
  `6f2bd5bc1412475906ae8c932370eea89e550f831c4e15a7f7a95dd082d12cf4`
- simplified retained verifier:
  [`hc7_atomic_dirty_two_bridge_chain_barrier_verify.py`](hc7_atomic_dirty_two_bridge_chain_barrier_verify.py)
- verifier SHA-256:
  `7334fd62e0dc25ec4fae4109714e24e155d0b0d972325449461fa80603d9af8b`

The promoted barrier differs from the audited strengthened revision only in
its status metadata: `separate internal audit pending for this strengthened
revision` became `separate internal audit GREEN`.  Its promoted SHA-256 is
`cc52fd1f9fc08d31f28ab9ccd2191028eb06f719d32326d6c6225f0bc54ee918`.
No mathematical or computational content changed.

The previously GREEN revisions had barrier SHA-256
`8e5bd1998a40b765b0180e88cac43bba3c0ad0986c4559c1266441db5e6c8d2a`
and verifier SHA-256
`5037c1e198eefe3be17873f0a3ea50ab632d7a729f9ff417520a02ebff41370c`.
The exact revision diff leaves the graph construction, width-five/Helly
exclusion, clique-model oracle, connectivity and colouring calculation,
Kuratowski parser, and saturation section mathematically unchanged.  It
replaces the 78 vertex-pair checks and the 14-vertex icosahedral embedding
search by the stronger 1,036 vertex-or-edge-object deletion theorem and its
general subdivision-to-two-apex argument.

## Verdict

GREEN.  Every one of the 1,036 object-deletion cases is represented exactly
once and has a validated literal Kuratowski subdivision.  The written lift
from deletion of at most two host vertices to deletion of at most two source
objects is correct for arbitrary subdivisions and arbitrary host order.
The strengthened theorem therefore excludes a subdivision of `D_*` from
every two-apex graph, not only from the standard `K_2`-joined icosahedron.

The verifier was independently rerun with

```text
.venv/bin/python -B barriers/hc7_atomic_dirty_two_bridge_chain_barrier_verify.py
```

and returned

```text
GREEN atomic dirty two-bridge-chain barrier
object_deletion_nonplanar=yes objects=45 cases=1036 kuratowski={'TK3,3': 587, 'TK5': 449}
two_apex_subdivision_exclusion=yes
```

It also reproduced the prior 92 connectivity checks, width-five `K_6`
exclusion, and all five exact saturation profiles.

## Checks performed

1. **Exact object universe.**  The graph has thirteen vertex objects and
   thirty-two edge objects.  Strings represent vertices and two-element
   frozensets represent edges, so the two types are disjoint and all 45
   objects are distinct.  The loops for deletion sizes zero, one, and two
   cover exactly

   \[
     1+45+\binom{45}{2}=1036
   \]

   cases.  Broken down by type, these are one empty deletion, 13 single
   vertices, 32 single edges, 78 vertex pairs, 416 mixed vertex-edge pairs,
   and 496 edge pairs.

2. **Deletion semantics.**  Vertex objects are removed first and edge
   objects second.  If a selected edge is incident with a selected vertex,
   the second deletion is redundant, exactly as it is in `D_*-Z`; NetworkX
   safely ignores the already absent edge.  Unordered frozenset iteration
   is harmless because the graph is undirected.

3. **All 1,036 planarity outcomes.**  In every case `check_planarity` returns
   nonplanar and supplies a counterexample.  The total certificate count is
   1,036, split into 449 subdivisions of `K_5` and 587 subdivisions of
   `K_{3,3}`.  These counts agree between the note and the retained run.

4. **Certificate parser.**  For every returned counterexample, the verifier
   first checks that every certificate vertex and edge is literally present
   in the deletion remainder and that the certificate is connected.  It
   identifies as branch vertices exactly those of degree different from
   two, then walks each unused edge through degree-two vertices to the next
   branch vertex.  Each edge is removed exactly once.  A return to the same
   branch vertex is rejected, repeated suppressed branch pairs are rejected,
   and no unused edge may remain.  The resulting simple core is checked by
   graph isomorphism to `K_5` or `K_{3,3}`.  Thus the program validates a
   literal Kuratowski subdivision rather than trusting only the Boolean
   planarity result.

5. **Subdivision-to-object map.**  Let `S` be any subdivision of `D_*` in a
   host `J`, and delete at most two host vertices.  A deleted vertex outside
   `S` records no source object.  A deleted branch image records its unique
   vertex object.  A deleted internal vertex lies on exactly one subdivided
   edge route and records that edge object.  Two deleted internal vertices
   on the same route record the same object only once.  Therefore the
   recorded set `Z` has order at most two.

6. **The remaining subdivision.**  Remove from `S` every recorded branch
   image and all its incident routes, and remove every route whose edge
   object was recorded.  No unrecorded route contains a deleted internal
   vertex, because subdivision routes are internally vertex-disjoint and
   avoid all branch images.  The surviving subgraph is a subdivision of
   `D_*-Z` and lies in the planar host remainder.  Proposition 4.1 says
   `D_*-Z` is nonplanar, and subdivision preserves nonplanarity, giving the
   required contradiction.

7. **Two-apex and joined-planar consequences.**  The preceding argument
   uses only that some set of at most two host vertices leaves a planar
   graph, so it proves exclusion from every two-apex host.  In particular,
   deleting the complete-factor vertices from `K_2\vee P` leaves planar
   `P`.  If `P` is five-connected, the join is at least seven-connected:
   after fewer than seven deletions either a universal factor vertex remains
   or at most four vertices were removed from `P`.  It is `K_7`-minor-free
   because discarding the at most two branch sets containing the factor
   vertices from a hypothetical model would leave a `K_5` minor in planar
   `P`.

8. **Previously audited sections.**  The width-five decomposition and Helly
   case split proving `D_*` has no `K_7` minor are unchanged.  The
   connectivity-three and four-colouring witnesses are unchanged.  The
   fifteen positive saturation models, five simultaneous negative covers,
   and exact spanning-partition checks are unchanged.  I compared these
   sections against the prior GREEN revisions and reran the simplified
   verifier; their earlier audit conclusions remain valid.

## Trust boundary

No unresolved assumption remains within the strengthened barrier.  The
finite graph itself is three-connected and four-chromatic, so it still does
not satisfy the full hypotheses of a hypothetical counterexample to
`HC_7`.  The theorem excludes exact subdivisions of this canonical graph
from all two-apex hosts; it does not classify weaker dirty-path patterns or
arbitrary one-sided bridge chains that fail to contain such a subdivision.
