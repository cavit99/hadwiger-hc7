# Independent audit: same-vertex shared-hub saturation

**Verdict:** GREEN.

The written theorem, its five one-edge certificates, the automorphism
transfer, the minimum-degree forcing step, and the final two-edge
certificate are correct.  No unresolved assumption or gap remains within
the stated fixed-vertex theorem.

## 1. Audited revision

This audit checks exactly:

- [`hc7_atomic_shared_hub_same_vertex_saturation.md`](hc7_atomic_shared_hub_same_vertex_saturation.md),
  SHA-256
  `d315456f5189af245f2249d52aa6cd84d9eb35fedfbc0cc4e81ccb432dbad303`;
  and
- [`hc7_atomic_shared_hub_same_vertex_saturation_verify.py`](hc7_atomic_shared_hub_same_vertex_saturation_verify.py),
  SHA-256
  `ba17649fa24c8abceae189d4566ca145d996c247f73d203b4759741c86186e3d`.

The audit is internal and independent of the authoring pass.  It is not
external peer review.

Relative to the revision first checked, the theorem source changed only its
status from “audit pending” to “audit GREEN.”  I rechecked the resulting
source hash and reran the unchanged verifier; the theorem statement, proof,
certificates, and trust boundary are unchanged.

## 2. Reconstruction of the base graph

The graph description gives the claimed order and size.

- `K_7-{ab,cd}` has nineteen edges, and the four edges from `x` give
  twenty-three.
- Subdividing each of `ac,bd,ad,bc` and adding its anchor edge has net
  edge gain two, giving thirty-one edges.
- Replacing `fg` by `f-h-g` and adding `eh,hx` has net gain three, giving
  thirty-four edges.
- The four route vertices and `h`, added to the eight vertices of `H_0`,
  give thirteen vertices.

Direct reconstruction also gives

\[
 N_{G_*}(p_{ad})=\{a,d,g\},\qquad
 N_{G_*}(p_{bc})=\{b,c,g\}.                            \tag{2.1}
\]

Thus each named vertex has degree three and nine nonneighbours, exactly as
listed in the theorem.

## 3. The five one-edge certificates

For each of the five rows in Theorem 2.1, I checked all of the following
against the independently reconstructed graph after adding the displayed
edge.

1. The seven sets are nonempty, pairwise disjoint, and their union is all
   thirteen vertices.
2. Every non-singleton set induces a connected subgraph.
3. Every one of the twenty-one unordered pairs of branch sets has a host
   edge between it.

All five rows pass.  In particular, the certificates establish a `K_7`
minor after adding any one of

\[
 p_{ad}b,quad p_{ad}c,quad p_{ad}p_{ac},quad
 p_{ad}p_{bd},quad p_{ad}p_{bc}.                      \tag{3.1}
\]

The verifier checks these as literal spanning branch-set partitions; it
does not rely on a heuristic minor oracle.

## 4. Automorphism and degree forcing

The permutation

\[
 (a\ b)(c\ d)(p_{ac}\ p_{bd})(p_{ad}\ p_{bc})          \tag{4.1}
\]

preserves every edge class of `G_*`:

- it preserves the two absent core pairs `ab,cd`;
- it exchanges the subdivided `ac` and `bd` routes and their two
  `f`-anchors;
- it exchanges the subdivided `ad` and `bc` routes and their two
  `g`-anchors; and
- it fixes `e,f,g,h,x` and the edges of the subdivided `fg` route together
  with `eh,hx`.

Therefore it transfers each certificate in (3.1) to a certificate at
`p_bc`.  This is a transfer between two labelled copies of the same base
graph; it does not require the supergraph `Q` itself to be invariant under
the permutation.

If `Q` is `K_7`-minor-free, none of the five edges in (3.1) can occur.
The only remaining possible new neighbours of `p_ad` are

\[
                              e,f,h,x.                  \tag{4.2}
\]

Since its base degree is three, the condition `delta(Q)>=7` forces all
four edges in (4.2), in particular `hp_ad`.  The transferred argument at
`p_bc` forces `hp_bc`.  The forcing uses only edge-monotonicity of minor
containment and the exact degree count; there is no hidden maximality
assumption.

## 5. The final two-edge certificate

After adding `hp_ad` and `hp_bc`, the seven displayed bags have sizes

\[
                         1,1,3,2,2,2,2
\]

and partition all thirteen vertices.  Their internal spanning edges are

\[
 ag, ap_{ac}, hp_{ad}, bp_{bc}, dp_{bd}, cx.       \tag{5.1}
\]

The contact table in the theorem contains exactly the twenty-one unordered
pairs of bags.  Every listed contact is present in the augmented graph and
has one endpoint in each named bag.  The two forced edges have distinct
roles: `hp_ad` connects the `H` bag internally, while `hp_bc` supplies the
`H`--`B` contact.  Hence the table is a complete explicit `K_7`-minor
certificate.

The last consequence is also valid: a seven-connected graph on thirteen
vertices has minimum degree at least seven, so the fixed-vertex theorem
excludes a seven-connected `K_7`-minor-free supergraph of `G_*`.

## 6. Reproduction

I reran

```text
.venv/bin/python -B results/hc7_atomic_shared_hub_same_vertex_saturation_verify.py
```

and obtained exactly

```text
GREEN atomic shared-hub same-vertex saturation
host: vertices=13 edges=34 degree(p_ad)=3 degree(p_bc)=3
automorphism: p_ad<->p_bc verified
one_edge_K7_models: p_ad-b,p_ad-c,p_ad-p_ac,p_ad-p_bd,p_ad-p_bc
remaining_incident_edges: p_ad-e,p_ad-f,p_ad-h,p_ad-x
forced_edges: h-p_ad,h-p_bc
two_edge_K7_model: branch_sets=7 contact_edges=21 verified
conclusion: same_vertex_minimum_degree_7_K7_free_supergraph=no
```

Source inspection confirms that the checker validates the complete edge
set under the automorphism, exact neighbour and nonneighbour sets, spanning
and disjointness of every model, connectedness of every bag, all pairwise
model adjacencies, and all twenty-one named final contacts.

## 7. Trust boundary

The GREEN verdict is limited to the theorem as stated: supergraphs on the
same thirteen vertices.  Adding new vertices can raise the two degree-three
vertices to degree seven without adding the forced edges used in the proof.
The result therefore does not close an unbounded seven-connected host, does
not use contraction-critical colouring responses, and does not prove the
atomic collision theorem.
