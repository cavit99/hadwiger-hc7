# Independent audit: intersecting repaired paths

**Verdict:** GREEN for Lemmas 2.1--2.3, Theorem 2.4, Corollary 2.5, and
Proposition 3.1 at the exact revisions below.  The deterministic checker
passes after a correction described in Section 6.  These results do not
close the exceptional repaired-contact configuration or prove `HC_7`.

**Audited source:**
`results/hc7_repaired_contact_intersection.md`.

**Source SHA-256:**
`46c2498ac436cb63a0d7bbd127c65e13deaca721db359fdd2ad430aabb5b801e`.

**Audited checker:**
`results/hc7_repaired_contact_intersection.py`.

**Checker SHA-256:**
`4cfdc795a87d658734214192b5e120cae35725eafc676dbc38ef77d199ad9f8f`.

After the mathematical audit, the source and checker were moved from
`active/` to `results/`; only status, adjacent-audit links, cross-reference
metadata, and the documented checker invocation changed in the source.
The hashes above bind this audit to those exact promoted revisions; the
audited mathematical content and checker logic are unchanged.

## 1. Four-end attachment models

For `z=q`, the seven sets in (2.2) are disjoint and connected after the
six prescribed linkage paths are contracted.  The branch containing
`D,a3,p` reaches `q` through `D`; the branch containing
`a0,a1,a2,x,y` reaches the five singleton right endpoints through the
corresponding linkage edges.  Its remaining contacts come from the two
endpoint-side cliques and the listed left-side edges.  The same check,
with `x,q` and `a3` exchanged between the last two large branch sets,
validates (2.3) for `z=p`.

If two paths have intersecting interiors, the union of their interiors is
connected, avoids the normalized vertices and linkage paths, and is
adjacent to their four distinct ends.  Thus it is a valid instance of the
first part of Lemma 2.1.

## 2. Exceptional endpoint and linkage-path attachments

An additional attachment at `p` or `q` invokes Lemma 2.1 directly.  By
the simultaneous symmetry on `a0,a1,a2` and `b0,b1,b2`, (2.6) covers any
additional `a_i` attachment.  Formula (2.7) covers attachment to all three
`b_i`.  Direct checking confirms connectivity, disjointness, and all
twenty-one adjacencies in each model.

For an attachment at an internal vertex of `P_i`, `i=0,1,2`, splitting
that path at the attachment gives the seven branch sets in (2.8).  The
edge across the split supplies the only non-obvious adjacency between the
two split branches, and the four compulsory attachments of `D` supply the
remaining exceptional contacts.  The cases on the `a3`--`p` and
`x`--`q` paths are valid contraction lifts: contracting the segment from
the attachment to the right endpoint makes `D` adjacent to `p` or `q`,
respectively, after which Lemma 2.1 applies.  The resulting minor model
lifts to the original graph.

Seven-connectivity forces at least seven distinct skeleton neighbours of
an off-skeleton component.  The four compulsory normalized endpoints and
at most two exceptional `b_i` endpoints account for at most six, so an
interior attachment is forced.  Lemmas 2.2--2.3 correctly confine every
such attachment to the `y`--`r` path in a `K7`-minor-free host.

## 3. Exact-seven separation

Let `U` be the union of `C` and the interior of the `y`--`r` path.  It is
connected because at least one of the forced interior attachments exists.
Suppose a path in `G-X_7` joins `U` to one of the first three linkage
paths.  Trimming it after its last vertex in `U` and before its first
later skeleton contact gives a path whose first end is in the interior of
the `y`--`r` path and whose interior avoids the complete linkage skeleton.

If the next skeleton contact is on one of the first three paths, the
audited clean-augmentation theorem applies.  If it is on the
`a3`--`p` path, connectedness of `C` gives an `r`--`a3` path with
interior in `C`; similarly one obtains an `r`--`x` path for a contact on
the `x`--`q` path.  This use of the crossed-bridge theorem is valid:

- the trimmed path has no internal vertex in `U`, hence none in `C`;
- the second path has all internal vertices in `C`;
- their four endpoints are distinct because `r,a3,x` lie in `X_7`; and
- on the two oriented linkage paths, the endpoint orders are opposite.

Thus the two bridge paths are genuinely vertex-disjoint, not merely two
routes through the same connected component.  Every possible return is
closed, so `X_7` separates the nonempty sets `U` and `T`.  Placing the
seven vertices of `X_7` on both sides gives an actual order-seven
separation; seven-connectivity rules out a smaller boundary.

## 4. Packing numbers on the exact-seven boundary

The separation obtained in Theorem 2.4 has literal boundary `X_7` of
order seven and both open shores nonempty.  With the additional hypothesis
in Corollary 2.5, the host is seven-connected, `K7`-minor-free, and every
proper minor is six-colourable, exactly as required by the independently
audited exact-seven full-packet packing theorem.

The vertices `r,b0,b1,b2` belong to `X_7` and induce a `K4`, since they
are among the vertices of the normalized `K6-pq`.  If `nu_1,nu_2` are the
two full-subgraph packing numbers, the cited theorem gives

```text
4 <= omega(G[X_7]) <= 6-(nu_1+nu_2).
```

Every component of either nonempty shore is `X_7`-full by
seven-connectivity, so both packing numbers are positive.  The inequality
forces their sum to be at most two, and hence `nu_1=nu_2=1`.  The source
states this as a packing-number conclusion; it does not infer uniqueness
of the full connected subgraph, a small transversal, or a recursive
colouring reduction.

## 5. Negative certificates

The low-degree deletion--contraction recurrence used by the imported
detector is exact.  A vertex of degree below six cannot be a singleton
branch set of a `K7` model; if it is used in a larger connected branch
set, some incident edge lies in that branch set and may be contracted;
otherwise the vertex may be deleted.

For each of the seven exceptional endpoint sets, the checker also returns
an elimination ordering of filled width at most five.  Such an ordering
is an independent treewidth-at-most-five certificate and therefore
excludes a `K7` minor.  The three parallel-repair graphs are independently
tested by the exact recurrence.

## 6. Checker correction and replay

In the prior script revision with SHA-256
`f2b97b7117ac6509f3ebc5e549fa24b59b112f36d198240e4736ed665aba8f5e`,
the connectivity and pairwise-adjacency assertions intended for
`verify_bags` appeared after the unconditional `return` in
`elimination_width`.  They were therefore unreachable, so that revision
did not actually verify the displayed positive branch sets.  The current
revision moves those assertions into `verify_bags` and removes the dead
code.  Replaying it gives:

```text
positive_intersection_certificates 5
negative_central_r 1
exceptional_r_endpoint_attachment_sets 7
exceptional_r_treewidth_upper_bound 5
interior_rail_outcomes (True, True, True, True, True, False)
negative_parallel_repair_graphs 3
GREEN: all repaired-contact intersection checks passed
```

The repaired checker therefore verifies nonemptiness, disjointness,
connectivity, and all pairwise adjacencies of each displayed positive
model, all 256 endpoint-attachment subsets, all six linkage-path
locations, and the stated negative examples.

## 7. Remaining gap

The exact-seven separation is obtained only when a single off-skeleton
component is adjacent to `a3,x,y,r`.  The result does not force a
colour-critical simultaneous bypass to avoid the linkage skeleton or to
meet the second residual path in such a component.  It also does not
resolve the resulting order-seven separation.  The source does not claim
any of these stronger conclusions.
