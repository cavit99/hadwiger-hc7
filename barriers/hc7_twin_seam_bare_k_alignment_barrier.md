# Barrier: bare common-five-set alignment

**Status:** explicit bounded counterexample, independently constructed and
verified by the adjacent script.

## Claim refuted

Two named proper-minor colour responses on a twin-style common five-set
need not be Kempe-alignable, even when the second contraction adds no edge
inside that five-set and the host is `K_7`-minor-free.

This refutes a bare `K`-normalization lemma.  It does not refute the correct
disjunction **alignment or rooted terminal model**.

## Construction

Let `P={p1,...,p6}` induce `K_6`.  Add `z,u,d,t,k` and the following
neighbourhoods outside the displayed edge `zu` and edge `dt`:

\[
\begin{aligned}
 N(k)\cap P&=\{p_2,p_3,p_4,p_5,p_6\},\\
 N(z)\cap P&=\{p_1,p_2,p_3,p_4,p_5\},\\
 N(u)\cap P&=\{p_1,p_2,p_3,p_4\},\\
 N(d)\cap P&=\{p_1,p_2,p_3,p_4,p_6\},\\
 N(t)\cap P&=\{p_2,p_3,p_4,p_6\}.
\end{aligned}
\]

Put

\[
                         K=\{t,k,p_2,p_3,p_4\}.
\]

On `G-zu`, the assignment

\[
 p_i\mapsto i,\qquad z,u\mapsto6,\qquad d\mapsto5,\qquad t,k\mapsto1
\]

is proper and induces the block `{t,k}` on `K`.  On `G/dt`, contracting
`d` into `t`, the assignment

\[
 p_i\mapsto i,\qquad z\mapsto6,\qquad u,t\mapsto5,\qquad k\mapsto1
\]

is proper and makes all five members of `K` singleton blocks.

The palette `K_6` fixes all six colours up to permutation.  In every
six-colouring of `G/dt`, the vertex `k` must share the missing palette
colour of `p1`, while the contracted `t` must share that of `p5`.  Hence no
six-colouring, and therefore no Kempe sequence, aligns the two states on
`K`.

The contraction is `K`-clean: every neighbour of `d` in `K-{t}` is already
adjacent to `t`.

## Why this is not an `HC_7` obstruction

The graph is only five-connected, is six-colourable, and is not
contraction-critical.  It has no `K_7` minor, but it does have the permitted
`K`-rooted `K_5` model with bags

```text
{t}, {u,k,p5,p1,p6}, {p2}, {p3}, {p4}.
```

Thus the rooted-model branch is indispensable.  The active theorem must
prove **alignment or terminal model** from response-matched lock geometry;
`K`-cleanliness and abstract exact states are insufficient.

The adjacent verifier checks both named colourings, forced nonalignment,
`K`-cleanliness, connectivity five, the rooted bags, full six-colourability,
and exact exclusion of a `K_7` minor.
