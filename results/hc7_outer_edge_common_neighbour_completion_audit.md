# Independent audit: common neighbours at a canonical outer edge

**Verdict:** **GREEN** for the exact revision audited.  Lemma 2.1,
Theorem 3.1, and the five-chromatic exclusion in Corollary 4.1 are valid
under their stated hypotheses.  The argument uses only actual edges of the
quotient when it constructs the two skeleton triangles; it never promotes
the virtual edge `z_e z_f` or any other completion edge to an edge of the
host graph.  The result does not eliminate the six-chromatic branch or
align its regenerated spanning `K_6` model with the deleted endpoint pair.

**Audited source:**
`results/hc7_outer_edge_common_neighbour_completion.md`.

**Source SHA-256:**
`d9ceb0e832e55ff659dc701ecefa0974a87058fcd6303443b96cc33ec7864731`.

The independently audited mathematical revision had SHA-256
`4dcb4cbcb8c076c6998dcad82ad0e116b2020f54d2c74af110c366c09248e50f`.
The promoted revision differs only in its status paragraph and in repairing
the relative link to the already promoted chromatic dichotomy.  No theorem
statement or proof step changed.

This is an internal mathematical audit, not external peer review.

## 1. Exact dependency revisions

The proof invokes three separately audited inputs.  Their current source
hashes agree with the hashes in their adjacent audits:

- the canonical rooted-web theorem,
  `d02a82cd15ba652696683f79c171f448d1bbeb9ec71ae5f78fb594dffde5c08f`;
- four-connectivity of the canonical web skeleton,
  `0a0f5db310c6896ba8e3aef9fd81a57c9d9cc697ff3b2cb9dad373f686579c08`;
  and
- the unique leaf--endpoint chromatic dichotomy,
  `8bc8ebcab599fd614afae5075c8e77384408d1f4750da55c5566439bd1c6d36b`.

The first input supplies a web completion `W^+` of the quotient `Q`, the
outer order

\[
                  \ell_e,\ell_f,z_e,z_f,
\]

the facial triangle `T={z_e,z_f,x}`, and exactly two components of `Q-T`.
The second input applies to the same labelled skeleton `W`.  The third
input uses the same orientation: `ell_f` has unique neighbour `a` in the
endpoint set of `e`, and its connected interior is the component denoted
by `C` here after deleting the two leaves.

## 2. Attachment vertices cannot occur on the leaf side

Let `A_Q` be the component of `Q-T` containing `ell_e,ell_f`.  Suppose a
vertex of `A_Q` belonged to an attachment clique `X_U`.  The set `U` is a
facial triangle of the skeleton.  A vertex of `X_U` survives deletion of
`U`, has no neighbour outside `U union X_U`, and is separated from at least
one of the four outer vertices, because a three-set cannot contain all four
outer vertices.  Thus `U` is a three-vertex cut of the spanning subgraph
`Q`.

By the canonical cut hypothesis, `U` contains `z_e,z_f`.  Since these are
consecutive on the outer face, the plane edge `z_e z_f` is incident with a
unique bounded facial triangle, namely `T`.  Hence `U=T`.  But after
deleting `T`, no vertex of `X_T` can be in the component containing
`ell_e,ell_f`, because `X_T` has no neighbour outside `T union X_T`.
This contradiction proves Lemma 2.1.  The argument uses the virtual outer
edge only as an edge of the skeleton; it does not claim that `z_e z_f` is
an edge of `Q`.

## 3. Literal-to-quotient label check

The component `C` lies in `G-S`, whereas both endpoints of `e` belong to
`S`.  Therefore any two vertices

\[
 u,v\in C-\{\ell_e,\ell_f\}
\]

survive contraction of `e` as two distinct vertices, and their images lie
in `A_Q`.  Lemma 2.1 consequently places both in the skeleton `W`.

The edge `ell_f a` is a literal edge of `G`, with `a` an endpoint of `e`.
Contracting `e` turns it into the actual quotient edge `ell_f z_e`.  The
outer order makes this the outer skeleton edge between the second and
third named vertices.  Likewise, if `u` is adjacent in `G` to both
`ell_f` and `a`, then the edges `u ell_f` and `u z_e` are actual edges of
`Q`; the same holds for `v`.

All endpoints of these five quotient edges are skeleton vertices.  A web
completion adds no new edge between two skeleton vertices: such an edge is
an edge of `W`.  Thus the two cycles

\[
                 \ell_f z_e u\ell_f,
                 \qquad
                 \ell_f z_e v\ell_f
\]

are genuine triangles of `W`.  This verifies the most label-sensitive
step of Theorem 3.1.

## 4. The plane-edge contradiction

The separately audited skeleton theorem gives that `W` is four-connected;
in particular no triangle of `W` is separating.  Equivalently here—and
also directly from the definition of the web skeleton—each triangle is
facial.  Neither displayed triangle can bound the outer face, whose
boundary is the four-cycle
`ell_e ell_f z_e z_f ell_e`.

The shared edge `ell_f z_e` lies on that outer four-cycle.  In a plane
embedding it has the outer face on one side and exactly one bounded face on
the other.  It therefore cannot lie in two distinct bounded facial
triangles.  Since `u` and `v` are distinct, the two triangles are distinct,
which proves the asserted common-neighbour bound.

Notice that this contradiction uses the actual outer edge
`ell_f z_e`, not the virtual edge `z_e z_f` singled out elsewhere in the
canonical web theorem.

## 5. Chromatic consequence

Under the hypotheses of Corollary 4.1, the five-chromatic branch of the
unique leaf--endpoint dichotomy gives two distinct common neighbours of
`ell_f,a` in precisely

\[
                         C-\{\ell_e,\ell_f\}.
\]

Theorem 3.1 allows at most one, so that branch is impossible.  The deletion
`G-{ell_f,a}` is consequently six-chromatic.  The cited dichotomy invokes
the established parameter-six case of Hadwiger's conjecture and then
absorbs all vertices outside a `K_6` model, yielding a spanning `K_6`
model.  No additional contact between that model and the deleted vertices
is inferred.

The direct proof of Theorem 3.1 needs only the canonical cut hypotheses and
the skeleton theorem.  Seven-connectivity, exclusion of a `K_7` minor, and
exclusion of the relevant actual order-seven separations are used upstream
to reach exactly that canonical branch.  Restoring those alternatives
makes the last sentence of Corollary 4.1 a valid contrapositive: within the
full upstream reduction, a five-chromatic deletion forces one of the
previously excluded terminal outcomes.

## 6. Scope and editorial note

This audit establishes only the five-chromatic exclusion in the canonical
order-eight branch.  It does not prove that the spanning `K_6` model in the
six-chromatic branch has six branch sets adjacent to `{ell_f,a}`, and it
does not complete a `K_7` model.

The source currently links the chromatic dichotomy by a same-directory
path although that dependency has been promoted to `results/`.  This is a
documentation-link issue only; it does not affect the proof.  If the source
is promoted and its status or link is edited, its hash should be rebound in
this audit without changing the mathematical verdict.
