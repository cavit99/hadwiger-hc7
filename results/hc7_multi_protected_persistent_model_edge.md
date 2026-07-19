# Persistent incident edges with several protected singleton branch sets

**Status:** written proof; separate internal audit GREEN in
[`hc7_multi_protected_persistent_model_edge_audit.md`](hc7_multi_protected_persistent_model_edge_audit.md).

This note strengthens the rooted persistent-edge theorem by preserving a
family of named singleton branch sets simultaneously.  The statement is
parameter-uniform; its intended use is to retain several literal boundary
or model labels while reselecting a spanning near-complete minor model.

## Theorem

Let `t>=3`, let `F=K_t-e`, and let

\[
                    \mathcal M=(B_y:y\in V(F))
\]

be a spanning labelled `F`-model in a `t`-connected, `K_t`-minor-free graph
`G`.  Fix a label `r`, a vertex `v\in B_r`, and put

\[
 \Gamma=\{y\in V(F)-\{r\}:ry\in E(F)\},\qquad m=|\Gamma|.
\]

Let `A\subseteq\Gamma` satisfy `|A|<=t-2`.  For every `a\in A`, fix a
vertex `x_a` and require

\[
                         B_a=\{x_a\},\qquad vx_a\in E(G).       \tag{1}
\]

Suppose the class of spanning labelled `F`-models satisfying these
requirements is nonempty.  Among that class choose a model for which
`R=B_r` has minimum order.  Then:

1. at least `t-m+1` distinct edges incident with `v` are
   deletion-persistent for this same labelled model; and
2. the number of components of `G[R]-v` satisfies

\[
              c(G[R]-v)\le\left\lfloor\frac{m-|A|}{2}\right\rfloor. \tag{2}
\]

Here an edge is deletion-persistent when deleting it leaves the same
branch sets as a spanning labelled `F`-model.

## Proof

Use the notation and counting argument of the rooted incident-edge
persistence theorem.  For each component `Z` of `G[R]-v`, let

\[
 \Lambda(Z)=\{y\in\Gamma:N_G(B_y)\cap R\ne\varnothing
                         \text{ and }N_G(B_y)\cap R\subseteq Z\}.
                                                               \tag{3}
\]

The sets `\Lambda(Z)` are pairwise disjoint.  Moreover, no protected label
belongs to any of them: for `a\in A`, the protected edge `vx_a` puts `v`
in `N_G(B_a)\cap R`, whereas `v\notin Z`.  Thus

\[
                         \Lambda(Z)\subseteq\Gamma-A.           \tag{4}
\]

We claim that every such component satisfies

\[
                              |\Lambda(Z)|\ge2.                 \tag{5}
\]

Put `R'=R-Z`.  It is nonempty and connected: it consists of `v` together
with the other components of `G[R]-v`, each joined to `v`.

Suppose first that `\Lambda(Z)=\varnothing`.  Then `Z` has a neighbour in
an unprotected foreign branch set.  Otherwise every neighbour of `Z`
outside `R` would be one of the protected singleton vertices `x_a`, and
every edge from `Z` to `R-Z` has endpoint `v`; hence

\[
                             N_G(Z)\subseteq\{v\}\cup\{x_a:a\in A\}. \tag{6}
\]

The right side has order at most `t-1`.  Since `|A|<=t-2`, at least one of
the `t-1` foreign labels is not protected; its nonempty branch set lies
outside `Z` and outside the set in (6).  Therefore the set in (6) would
separate the nonempty set `Z` from that branch set, contradicting
`t`-connectivity.  Choose an unprotected label `y` whose branch set is
adjacent to `Z`, replace `R` by `R'`, and replace `B_y` by `B_y\cup Z`.
All protected singletons remain fixed.  Because no required label is
monopolized by `Z`, all required adjacencies from `R'` survive.  The
remaining labelled adjacencies also survive.  The replacement therefore
either repairs the
sole missing pair and yields a `K_t`-minor model, or gives an allowed
spanning labelled `F`-model with smaller rooted branch set.  Both outcomes
are impossible.

Suppose next that `\Lambda(Z)=\{y\}`.  By (4), `y\notin A`.  Move the whole
component `Z` from `R` into `B_y`.  The edge from `v` to `Z` restores the
required adjacency between `R'` and `B_y\cup Z`; every other required
root adjacency remains because its label is not monopolized by `Z`.
Again the result is either a `K_t`-minor model or an allowed model with
smaller `R`, a contradiction.  This proves (5).

The persistent-edge count now repeats verbatim.  Let `k_0` be the number
of components `Z` with one `v-Z` edge, `k_1` the number with at least two,
`\ell` the number of nonpersistent edges from `v` to foreign branch sets,
and `q` the number of foreign labels receiving a persistent edge from
`v`.  If `p` is the number of deletion-persistent incident edges, the
pairwise disjoint monopoly sets, the private labels of the `\ell` edges,
and the `q` persistent external labels give

\[
                         2(k_0+k_1)+\ell+q\le m.         \tag{7}
\]

Spanning gives the exact degree identity

\[
                                  d_G(v)=k_0+\ell+p.     \tag{8}
\]

If `p=0`, (7)--(8) imply `d_G(v)<=m<=t-1`.  If `p>0`, then a persistent
internal edge gives `k_1>0`, or a persistent external edge gives `q>0`;
hence `k_0+2k_1+q>=1`.  Under the contrary assumption `p<=t-m`, equations
(7)--(8) give

\[
 d_G(v)\le m+p-(k_0+2k_1+q)\le m+p-1\le t-1.
\]

Both cases contradict `t`-connectivity.  Therefore `p>=t-m+1`.

Finally, by (4)--(5), the monopoly sets are pairwise disjoint subsets of
the `m-|A|` labels in `\Gamma-A`, each of order at least two.  Their number
is exactly `c(G[R]-v)`, proving (2).  \(\square\)

## `HC_7` consequences and limitation

When `t=7` and `r` is a common label of `K_7-e`, one has `m=6`.  Protecting
three singleton required neighbours of `v` forces `G[R]-v` to be connected
or empty; protecting five forces `R=\{v\}`.  The persistence conclusion
still supplies at least two distinct incident deletion-persistent edges.

The theorem does not produce the protected singleton branch sets.  It is
useful only when a model-selection or contraction argument has already
provided them.  It also does not place a persistent edge in a prescribed
shore or list-critical subgraph and does not align a minor colouring with
a boundary trace.
