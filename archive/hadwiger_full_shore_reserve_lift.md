# A uniform reserve lift for full shores

## Theorem 1 (full-shore reserve lift)

Let `m,q>=1`.  Let `C_1,...,C_m` be pairwise disjoint, pairwise anticomplete connected
subgraphs of a graph `G`, and let `X` be disjoint from them.  Assume every
`C_i` is collectively full to `X`: every vertex of `X` has a neighbour in
`C_i`.

Choose distinct vertices

\[
                         x_2,\ldots,x_m\in X.
\]

If `G[X-\{x_2,...,x_m\}]` contains a `K_q` model, then `G` contains a
`K_{q+m}` minor.

### Proof

Let `Q_1,...,Q_q` be the bags of the model in the residual boundary.  Use
the additional bags

\[
                         C_1,\qquad
                         C_i\cup\{x_i\}\quad(2\le i\le m). \tag{1.1}
\]

They are disjoint and connected.  The bag `C_1` is adjacent to every
other bag in (1.1) through an edge from `C_1` to its reserved vertex.
For distinct `i,j>=2`, an edge from `C_i` to `x_j` joins the corresponding
two bags.  Hence the `m` bags in (1.1) are pairwise adjacent.

Every `Q_a` contains a boundary vertex not among the reserves.  Fullness
therefore joins every bag in (1.1) to every `Q_a`.  The `Q_a` are already
pairwise adjacent.  These `q+m` bags form the required clique model.  QED.

The branch-set audit is literal:

* there are exactly `m+q` bags;
* the `m` shore bags are connected and mutually disjoint because the
  shores and reserves are mutually disjoint;
* the residual model avoids every reserve, so it is disjoint from all
  shore bags;
* shore--shore adjacency uses an edge from `C_i` to `x_j`, with `x_j`
  placed in the other bag;
* shore--core adjacency uses fullness at any vertex of the relevant core
  bag; and
* no edge between two original shores is assumed or used.

## Corollary 2 (one-reserve bilateral lift)

For two full shores `C,R`, if some `x in X` satisfies

\[
                         \eta(G[X-x])\ge q,
\]

then `G` has a `K_{q+2}` minor.  Thus a `K_{q+2}`-minor-free bilateral
gate satisfies `eta(G[X-x])<=q-1` for every boundary vertex `x`.

For the forced `HC_7` exact-eight gate, `q=5`: every seven-vertex deletion
of the adhesion is `K_5`-minor-free.  This includes, simultaneously, the
three deletions that reserve one of the three internal cut vertices.

## Corollary 3 (uniform `HC_t` reserve obstruction)

Let `1<=m<=t-1`, and suppose an adhesion `X` has `m` pairwise
anticomplete connected full shores.  If there is a reserve set

\[
                         Z\subseteq X,
                         \qquad |Z|=m-1,
\]

for which `G[X-Z]` contains a `K_{t-m}` model, then `G` contains a
`K_t` minor.

Equivalently, in every `K_t`-minor-free realization of such a full
`m`-shore gate,

\[
                         \eta(G[X-Z])\le t-m-1       \tag{3.1}
\]

for every `(m-1)`-element reserve set `Z subseteq X`.

### Proof

Order the vertices of `Z` as `x_2,...,x_m` and apply Theorem 1 with
`q=t-m`.  This proves the first statement; its contrapositive is (3.1).
QED.

## Corollary 4 (two-full-shore chromatic gate)

Assume `HC_{t-2}` and let `G` be `K_t`-minor-free.  If an adhesion `X`
has two anticomplete connected full shores, then

\[
                         \chi(G[X])\le t-2.           \tag{4.1}
\]

If equality holds, `G[X]` is `(t-2)`-vertex-critical.  If additionally

\[
                         |X|\le2t-6,                  \tag{4.2}
\]

then Gallai's small-critical-graph theorem makes `G[X]` a nontrivial
join of smaller critical graphs.

In particular, an order-`t+1` bilateral gate satisfies (4.2) for every
`t>=7`.  Its only top-chromatic residue is therefore a coherent join
core; otherwise `chi(G[X])<=t-3`.

### Proof

Take `m=2` in Corollary 3.  For every `x in X`,

\[
                         \eta(G[X-x])\le t-3.
\]

By `HC_{t-2}`, every `G[X-x]` is `(t-3)`-colourable.  Adding `x` proves
(4.1).  Equality makes every vertex deletion lower the chromatic number,
so the boundary is `(t-2)`-critical.  Gallai applies because
`2(t-2)-2=2t-6`; finally `t+1<=2t-6` exactly when `t>=7`.  QED.

## Theorem 5 (order-`t+1` bilateral gates lose a full colour)

Assume `HC_{t-2}`, let `t>=7`, and let `G` be `K_t`-minor-free.  If an
adhesion `X` of order `t+1` has two anticomplete connected full shores,
then

\[
                         \chi(G[X])\le t-3.           \tag{5.1}
\]

### Proof

Put `k=t-2`.  Corollary 4 gives `chi(G[X])<=k`.  Suppose equality held.
Then `H=G[X]` is `k`-critical, has

\[
                         |H|=k+3,                    \tag{5.2}
\]

and, by the reserve obstruction,

\[
                         \eta(H-x)\le k-1
                         \qquad(x\in H).              \tag{5.3}
\]

Since `k>=5`, Gallai decomposes `H` nontrivially as a join of smaller
critical graphs.  Repeatedly apply Gallai to every factor to which it
applies.  For a critical factor `J`, call

\[
                         epsilon(J)=|J|-\chi(J)
\]

its excess.  Excess is additive under joins, so the terminal factors
have total excess three.

No critical graph has excess one.  Indeed, if an `r`-critical graph had
order `r+1`, minimum degree at least `r-1` would make its complement a
matching.  Chromatic number `r` forces that matching to have exactly one
edge, but deleting an endpoint leaves `K_r`, contradicting criticality.
Also, an excess-zero critical graph is the complete graph of its
chromatic order.

It follows that one terminal factor has excess three and every other
factor has excess zero: a sum `2+1` is impossible.  The excess-three
factor cannot have chromatic number at least five, since then its order
`r+3` is at most `2r-2` and Gallai would decompose it further.  It cannot
have chromatic number one or two, whose only critical graphs are `K_1`
and `K_2`; nor chromatic number three, whose critical graphs are odd
cycles and therefore have even excess.  Hence it is a 4-critical graph
`Y` on seven vertices.  Combining all excess-zero factors gives

\[
                         H=K_{k-4}\vee Y.             \tag{5.4}
\]

Lemma 1.1 of `hadwiger_exact8_critical_core_elimination.md` supplies a
vertex `y in Y` such that `Y-y` contains a `K_4` model.  Joining that
model to the `k-4` singleton clique bags in (5.4) gives a `K_k` model in
`H-y`, contradicting (5.3).  Therefore equality is impossible and
(5.1) follows.  QED.

The only finite ingredient is the seven-vertex 4-critical-core lemma;
all dependence on `t` is absorbed by Gallai join decomposition and the
additive excess invariant.

## Scope

This is a label-free rooted-model lift.  It uses collective fullness, not
complete bipartite adjacency of individual shore vertices.  It does not
assert that the residual boundary has the needed clique minor; in the
exact-eight application, forcing that core model from the three
proper-minor transition choices is the remaining exchange problem.
