# Independent audit of the persistent support-class refinement

**Verdict:** GREEN for the theorem, the common-label `HC_7` consequences,
and the stated trust boundary at the pinned source revision.

**Audited source:** `hc7_persistent_support_class_refinement.md`, SHA-256

```text
4218dea7a7d02c571078dd7b2f1fc34e0fad1abab57dcc4e0f14e6503afa3629
```

After the GREEN audit, the source was moved from `active/` to `results/`
and only its status paragraph was changed to link this audit.  The theorem
statement and proof are unchanged; this audit is repinned to the resulting
promoted source hash above.

This is a separate internal mathematical audit, not external peer review.
The audit independently reconstructed the exact count and every
simultaneous-deletion case.  It also replayed the cited deterministic
barrier.  No source or ledger file was changed during the audit.

This verdict supersedes the earlier audit of source SHA-256 `ba1defd8...`.
The strengthened revision adds the `K_6`-minor analysis of complete graphs
minus matchings and its degree consequences; those additions are checked in
Section 4 below.

The proof uses the rooted persistence theorem at source SHA-256

```text
05548e80573736ea1f56b23db7372b2487eacdcda32dd5633a0af63be65212b7
```

whose Theorems 2.1 and 2.2 have a separate GREEN audit.  The present verdict
also rechecked the particular label count and degree identity used here.

## 1. Exact quantitative identity

The rooted theorem gives

\[
 2(k_0+k_1)+\ell+q\le m,
 \qquad d_G(v)=k_0+\ell+p(v).
\]

Thus

\[
 s=m-\bigl(2(k_0+k_1)+\ell+q\bigr)
\]

is a nonnegative integer and

\[
 \ell=m-2k_0-2k_1-q-s.
\]

Substitution into the degree identity gives exactly

\[
 p(v)=d_G(v)-m+k_0+2k_1+q+s.
\]

If `p(v)=0`, then there is neither a component with at least two
`v`-attachments nor a foreign label receiving a persistent external edge;
in particular `k_1=q=0`.  The displayed label count then gives
`d_G(v)=k_0+ell<=m<=t-1`, contrary to `t`-connectivity.  Hence `p(v)>0`, so
either `k_1>0` or `q>0`.  Therefore

\[
 k_0+2k_1+q+s\ge1
\]

and the claimed bound

\[
 p(v)\ge d_G(v)-m+1
\]

is valid.  No equality has been substituted for the rooted theorem's label
inequality: the slack variable `s` records the exact difference.

## 2. Pairwise simultaneous deletion

Every persistent incident edge belongs to exactly one stated support class:
an internal class determined by a component of `G[R]-v`, or an external
class determined by a foreign branch-set label.

The simultaneous-deletion analysis is complete.

- For two different internal classes, deleting one edge from each leaves at
  least one `v`-attachment to each affected component of `G[R]-v`.
- For an internal and an external class, the first deletion only concerns
  connectivity of `R`, while the second only removes one realization of a
  required inter-branch-set adjacency.  Their backup edges are of different
  types and cannot coincide.
- For two different external classes, each required label retains its own
  backup contact.
- Inside a class of order at least three, deleting any two incident edges
  leaves a third incident edge with the same support.
- Inside a two-edge external class, the pair is jointly persistent exactly
  when some further, possibly nonincident, `R`--foreign-bag edge realizes
  the required adjacency.  Inside a two-edge internal class, deleting both
  incident edges disconnects that component from `v` in `G[R]`.

Consequently, every nonedge of `J_v` is the sole pair in a support class of
order two.  Since support classes partition the persistent incident edges,
such pairs are vertex-disjoint.  Hence

\[
                         \overline{J_v}\text{ is a matching}.
\]

The argument concerns survival of the **same** labelled branch sets, exactly
as required by the definition; it does not rely on reselecting a model after
the two deletions.

## 3. Common-label `HC_7` consequences

For `t=7` and a root label not incident with the missing model edge, `m=6`,
so the quantitative identity gives

\[
                         p(v)\ge d_G(v)-5.
\]

If `d_G(v)=7`, then `N_G(v)` has order seven.  Unless `G=N_G[v]`, it is the
boundary of an actual separation with open sides `{v}` and
`V(G)-N_G[v]`.  In the exceptional case `G=N_G[v]`, the graph has eight
vertices; seven-connectivity forces it to be `K_8`, contrary to the
`K_7`-minor exclusion.  Therefore absence of every actual order-seven
separation implies `d_G(v)>=8`, and hence `p(v)>=3`.  The further implication
`d_G(v)>=9 => p(v)>=4` is immediate.

Let `U` be the set of other endpoints of the persistent incident edges.  If
no jointly persistent pair has nonadjacent endpoints, then every nonedge of
`G[U]` corresponds to a nonedge of `J_v`.  The preceding section shows that
these nonedges form a matching and that each lies in one nonjoint two-edge
support class.  Thus the statement

\[
                         G[U]=K_{p(v)}-M
\]

for some matching `M` is correct.  In particular, endpoints from distinct
support classes are adjacent, and the endpoints in every support class of
order at least three form a clique.

## 4. Complete graphs minus matchings

Continue under the common-label `HC_7` hypotheses and the assumption that
there is no jointly persistent pair with nonadjacent outer endpoints.  Then
Section 3 gives `G[U]=K_p-M`, where `p=p(v)` and `M` is a matching.

If `p>=8`, restrict to any eight vertices of `U`.  The resulting graph is
`K_8` minus a matching of order at most four.  It has a `K_6` minor in every
case:

- for matching order at most two, choose a clique of six singleton branch
  sets;
- for matching order three, choose one endpoint from each missing pair and
  the two unmatched vertices as five mutually adjacent singleton branch
  sets, then join two of the three unused mates into a connected sixth
  branch set; each singleton has an edge to this branch set;
- for a perfect matching, choose one endpoint from each missing pair as four
  singleton branch sets and partition the four unused mates into two pairs,
  each using vertices from different missing pairs.  Those two pairs are
  connected branch sets, are adjacent to one another, and each is adjacent
  to all four singleton branch sets.

Because `v` is adjacent to every vertex of `U`, adjoining `{v}` to any of
these `K_6` models gives a `K_7` model in `G`.  The `K_7`-minor exclusion
therefore proves `p<=7` in the dense alternative.

When `p=7`, a matching of order zero or one leaves a six-vertex clique.  For
matching order two, take one endpoint from each missing pair and all three
unmatched vertices as five singleton branch sets; the two unused mates form
a connected sixth branch set adjacent to all five.  Hence `K_7-M` has a
`K_6` minor whenever `|M|<=2`.  Since a matching on seven vertices has order
at most three, survival of the dense alternative with `p=7` forces
`|M|=3`, exactly as claimed.  An independent exhaustive enumeration of
branch-set partitions confirms that `K_7-3K_2` has no `K_6` minor, so the
stated residual is sharp at this quotient level.

Finally, the quantitative bound `p>=d_G(v)-5` and `p<=7` give

\[
                             d_G(v)\le12.
\]

If equality holds, then `p>=7`, hence `p=7`, and the preceding paragraph
forces `G[U]=K_7-3K_2`.  If instead `d_G(v)>=13`, the dense alternative is
impossible, so two jointly deletion-persistent incident edges have
nonadjacent outer endpoints.  These deductions do not require the separate
no-order-seven-separation assumption.

## 5. Barrier replay and scope

The deterministic command

```text
PYTHONPATH=active/runtime/deps python3 barriers/hc7_persistent_induced_star_barrier_verify.py
```

completed with the expected output

```text
verified persistent induced-star barrier
```

at verifier SHA-256

```text
c56d29fec3fb0f23d6fe08b25137bac069a21fc2d178150d290f06c3d7b47a4a
```

The construction is a seven-connected, `K_7`-minor-free graph with a
spanning labelled `K_7`-minus-one-edge model.  The root has degree eight,
its exactly three persistent incident edges are pairwise jointly persistent,
and their other endpoints form a triangle.  The `K_7`-minor exclusion follows
because at least five branch sets of any hypothetical `K_7` model avoid the
two universal vertices and would give a `K_5` minor in the planar remainder.

The example also has an actual order-seven separation: the two universal
vertices together with the five neighbours in the planar remainder of a
degree-five vertex separate that vertex.  It therefore refutes only the
induced-star inference from persistence multiplicity plus the other listed
static hypotheses.  It does not refute an induced-star theorem that
essentially assumes the absence of actual order-seven separations.

## 6. Trust boundary

The audited result is a structural theorem about persistent incident edges.
It does not force a persistent edge into a prescribed shore, align palette
colours with branch-set labels, synchronize colourings across a separation,
or split a branch set.  It proves the induced-star conclusion at degree at
least thirteen, but not at degrees eight through twelve even with the
additional no-order-seven-separation hypothesis.  No conclusion beyond this
scope is covered by the GREEN verdict.
