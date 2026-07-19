# Independent audit of persistent incident edges with several protected singletons

**Verdict:** **GREEN.**  The theorem and both numerical bounds are correct
under their exact stated hypotheses.

**Audited source:** `results/hc7_multi_protected_persistent_model_edge.md`,
SHA-256

```text
db70c8487c0561ab88d88cf08efc96c63c11c645f79ddd634a50c3505ee7d161
```

After the GREEN audit, the source was moved from `active/` to `results/`
and only its status line was changed to link this audit.  Its mathematical
statement and proof are unchanged; this audit is repinned to the resulting
source hash above.

This is a separate internal mathematical audit, not external peer review.
It checks the displayed source revision only.  Before the hash was pinned,
one purely terminological phrase was changed from a foreign branch set
"meets `Z`" to "is adjacent to `Z`"; the proof was otherwise unchanged.

## 1. Protected vertices and the admissible model class

Nonemptiness of the protected model class forces the fixed vertices
`x_a`, for `a in A`, to be pairwise distinct and different from `v`.
Indeed, distinct labelled branch sets are disjoint, while `v` belongs to
the root branch set.  Thus, with

\[
                 X=\{x_a:a\in A\},\qquad S=\{v\}\cup X,
\]

one has `|S|=1+|A|<=t-1`.

Protected vertices may have common neighbours, and a root component may
be adjacent to several of them.  Their direct adjacencies are constrained
by the labelled model: `x_ax_b` is present whenever `ab` is an edge of
`F`; if `ab` is the unique nonedge of `F`, then `x_ax_b` is absent because
such an edge would complete the displayed branch sets to a `K_t`-minor
model.  None of these possibilities affects the transfer argument.

For every component `Z` of `G[R]-v` and every protected label `a`, the
edge `vx_a` puts `v` in `N_G(B_a) cap R`.  Since `v` does not belong to
`Z`, the label `a` is not in `Lambda(Z)`.  Consequently

\[
                         \Lambda(Z)\subseteq\Gamma-A.          \tag{A.1}
\]

## 2. Empty-monopoly component and the separator

Fix a component `Z` of `G[R]-v`.  The set `R-Z` is connected: it contains
`v`, and every other component of `G[R]-v` has an edge to `v` because
`G[R]` is connected.

Suppose `Lambda(Z)` is empty and `Z` has no neighbour in an unprotected
foreign branch set.  Every edge from `Z` to `R-Z` then ends at `v`, by the
definition of the components of `G[R]-v`.  Every neighbour of `Z` outside
`R` lies in a protected branch set, and those branch sets are precisely
the singletons in `X`.  Hence

\[
                              N_G(Z)\subseteq S.                \tag{A.2}
\]

There are `t-1` foreign labels and at most `t-2` protected labels, so an
unprotected foreign label `b` exists.  Its nonempty branch set `B_b` is
disjoint from both `Z` and `S`.  Equation (A.2) therefore puts `Z` and
`B_b` in different components of `G-S`.  Since `|S|<=t-1`, this contradicts
`t`-connectivity.  Thus an empty-monopoly component is adjacent to some
unprotected foreign branch set.

Moving all of `Z` into such a branch set preserves its connectivity,
keeps `R-Z` connected, and leaves every protected singleton unchanged.
No required root adjacency is lost because `Lambda(Z)` is empty.  Every
foreign--foreign adjacency survives by inclusion.  If the transfer creates
the sole missing labelled adjacency, the replacement sets form a
`K_t`-minor model; otherwise they form an admissible spanning labelled
`F`-model with smaller root branch set.  Both conclusions contradict a
hypothesis.

The audited source correctly describes the selected foreign branch set as
being adjacent to `Z`.  Labelled branch sets are disjoint from `R`, so the
relation is adjacency rather than intersection.

## 3. Singleton monopoly and the two-label lower bound

If `Lambda(Z)={y}`, equation (A.1) gives `y notin A`.  Transfer `Z` from
`R` to `B_y`.  A `v-Z` edge supplies the required adjacency between the
new root set and `B_y union Z`; every other required root adjacency remains
because its label is not monopolized by `Z`.  Protected singleton branch
sets and all old foreign--foreign adjacencies remain unchanged.  The same
`K_t`-minor-or-smaller-root dichotomy gives a contradiction.

It follows that every root component satisfies

\[
                              |\Lambda(Z)|\ge2.                 \tag{A.3}
\]

The monopoly sets of different root components are pairwise disjoint:
one nonempty root-side contact set cannot be contained in two disjoint
components of `R-v`.

## 4. Persistence count

Let `k_0` count root components with one `v`-edge and `k_1` those with at
least two.  Every incident edge into a component of the second type is
persistent, and the unique edge into a component of the first type is not.
Let `ell` count nonpersistent external incident edges, let `q` count the
distinct foreign labels receiving persistent external incident edges, and
let `p` be the total number of persistent incident edges.

A nonpersistent external edge is the sole edge between `R` and its
required foreign branch set.  Distinct such edges therefore determine
distinct private labels, none of which belongs to a monopoly set.  A label
counted by `q` has `v` as a root-side contact, is not private, and is in no
monopoly set.  Repeated persistent edges at one label contribute once to
`q`, so there is no label overcount.  Equations (A.3) and pairwise
disjointness give

\[
                      2(k_0+k_1)+\ell+q\le m.                   \tag{A.4}
\]

Spanning and `K_t`-minor exclusion account for every neighbour of `v`:
an external edge into the sole nonneighbour label of `r` would itself
complete a `K_t`-minor model.  Thus

\[
                              d_G(v)=k_0+\ell+p.                 \tag{A.5}
\]

If `p=0`, equations (A.4)--(A.5) give `d_G(v)<=m<=t-1`.  If `p>0`, then
either `k_1>0` or `q>0`, so `k_0+2k_1+q>=1`.  Under the contrary assumption
`p<=t-m`,

\[
 d_G(v)\le m+p-(k_0+2k_1+q)\le m+p-1\le t-1.
\]

Both cases contradict the minimum-degree consequence of
`t`-connectivity.  Therefore

\[
                              p\ge t-m+1.                       \tag{A.6}
\]

## 5. Root-component bound

By (A.1) and (A.3), the pairwise disjoint monopoly sets are subsets of
the `m-|A|` labels in `Gamma-A`, and each has at least two elements.  Their
number is exactly the number of components of `G[R]-v`.  Hence

\[
              c(G[R]-v)\le\left\lfloor\frac{m-|A|}{2}\right\rfloor.
\]

## 6. Independent falsification checks

Two separate adversarial checks concentrated on the separator and on
small parameters.

1. For `t=3`, one has `|A|<=1`; even in the maximal protected case the
   set `S` above has order two and an unprotected foreign branch set
   remains.  Thus the separator proof itself is valid.  Globally the
   setup is vacuous because a `K_3`-minor-free graph is a forest and cannot
   be three-connected.
2. The `t=4` setup is likewise vacuous: a `K_4`-minor-free graph has
   treewidth at most two and cannot be four-connected.  No argument in the
   proof nevertheless requires `t>=5`.
3. The cases `A=emptyset` and `R={v}` are covered without exceptional
   conventions.  In the latter case there are no monopoly sets and the
   external-label count alone proves (A.6).
4. If `r` is an end of the missing edge and `A=Gamma`, then
   `m=t-2` and the component bound forces `R={v}`.  In fact the whole
   extremal configuration is incompatible with `t`-connectivity; this
   causes no false conclusion.
5. If `r` is a common label and `|A|=t-2`, then `m=t-1` and the component
   bound again forces `R={v}`.  The one remaining required foreign branch
   set must receive enough incident edges to meet `d_G(v)>=t`, and at least
   two of those edges are persistent, in agreement with (A.6).
6. Overlapping protected vertices, or a protected vertex equal to `v`,
   are impossible in a nonempty admissible class.  Edges from a root
   component to several protected vertices are all removed by the same
   separator `S`, so they do not defeat (A.2).

No finite or structural counterexample was found.

## 7. Exact scope

The result is conditional on a nonempty class of spanning labelled
`K_t`-minus-one-edge models with every named singleton and every literal
edge `vx_a` already present.  It preserves those branch sets while
minimizing only the rooted branch set.  It does not construct the
protected singleton bags, place a persistent edge in a prescribed shore,
preserve colouring data, align model labels with palette colours, or by
itself construct a `K_t` minor.  The theorem gives individual deletion
persistence; it does not assert that two supplied persistent edges may be
deleted simultaneously.

Subject to this exact scope, there are no unresolved assumptions or proof
gaps at the audited hash.
