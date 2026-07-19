# Leaf-block descent at a boundary-full order-eight separation

**Status:** written proof; separate internal audit GREEN in
[`hc7_order8_leaf_block_descent_audit.md`](hc7_order8_leaf_block_descent_audit.md).
This statement is not a proof of `HC_7`.

## Theorem (leaf-block descent)

Let `G` be a seven-connected graph satisfying

\[
 \chi(G)=7,\qquad K_7\not\preccurlyeq G,
 \qquad \chi(M)\le 6\text{ for every proper minor }M\text{ of }G.
 \tag{1}
\]

Let `S` have order eight.  Suppose that `G-S` has exactly three
components

\[
                         C,Q_0,Q_1,                    \tag{2}
\]

each adjacent to every literal vertex of `S`, and suppose that `G[S]`
contains a triangle.  If `G[C]` has a cutvertex, then at least one of the
following holds.

1. `G` has an actual separation of order seven.
2. There is a nonempty connected proper set `L\subsetneq C` such that,
   with

   \[
                             T=N_G(L),                 \tag{3}
   \]

   one has `|T|=8`, the graph `G-T` has exactly two or three components,
   and every component of `G-T` is adjacent to every literal vertex of
   `T`.

In outcome 2, every edge `xy` with `x\in L` and `y\in T` gives a fresh
operation-specific response at the smaller selected component: `G-xy`
has a proper six-colouring in which `x` and `y` have the same colour, and

\[
                              |L|<|C|.                 \tag{4}
\]

Thus outcome 2 is a strict host-level descent to another boundary-full
order-eight interface, with two or three complementary components; it
does not claim to preserve an older boundary partition or branch-set
labelling.

## Proof

Consider the block-cutvertex tree of the connected graph `G[C]`.  Since
`G[C]` has a cutvertex, this tree has at least two leaf blocks.  For a leaf
block `B`, let `z` be its unique cutvertex in `G[C]`, and put

\[
                              L_B=V(B)-\{z\}.           \tag{5}
\]

The set `L_B` is nonempty and connected.  Moreover,

\[
                         N_{G[C]}(L_B)=\{z\}.           \tag{6}
\]

Indeed, a two-connected block remains connected after deleting `z`, while
a bridge leaf block leaves its other end.  An interior vertex of a leaf
block has no neighbour in another block: otherwise it would belong to two
blocks and hence would be a cutvertex of `G[C]`.  This proves (5)--(6).
Interiors of distinct leaf blocks are disjoint.

We first show that not all leaf-block interiors are adjacent to every
vertex of `S`.  Choose two distinct leaf blocks with interiors `L_1,L_2`.
If both were `S`-full, then the four pairwise disjoint connected subgraphs

\[
                           L_1,L_2,Q_0,Q_1              \tag{7}
\]

would all be adjacent to every vertex of `S`.  Fix a triangle
`s_1s_2s_3` in `G[S]` and choose three further distinct vertices
`t_1,t_2,t_3\in S-\{s_1,s_2,s_3\}`.  The seven sets

\[
 L_1,\quad L_2\cup\{t_1\},\quad Q_0\cup\{t_2\},
 \quad Q_1\cup\{t_3\},\quad
 \{s_1\},\{s_2\},\{s_3\}                             \tag{8}
\]

are pairwise disjoint and connected.  Full adjacency supplies every
adjacency involving one of the first four sets, and the final three are a
triangle.  Hence (8) is a `K_7`-minor model, contrary to (1).

Choose a leaf block `B` whose interior `L=L_B` is not `S`-full, and retain
its cutvertex `z`.  Since `C` is a component of `G-S`, equations (5)--(6)
give the exact full neighbourhood

\[
                        N_G(L)=\{z\}\mathbin{\dot\cup}
                                 (N_G(L)\cap S).        \tag{9}
\]

This is the boundary of a genuine separation: `L` is nonempty, while
`Q_0` and `Q_1` lie outside `L\cup N_G(L)`.  Seven-connectivity and the
fact that `L` is not `S`-full yield

\[
             7\le |N_G(L)|=1+|N_G(L)\cap S|\le 8.     \tag{10}
\]

If equality holds on the left, outcome 1 holds.  We may therefore assume

\[
                              |T|=|N_G(L)|=8.           \tag{11}
\]

The set `L` is a component of `G-T`; it is a proper subset of `C` because
`z\notin L`.  Also `G-T` has another component, since it contains vertices
of `Q_0` and `Q_1`.

Let `D` be any component of `G-T`.  If `D` misses some vertex of `T`, then

\[
                              |N_G(D)|\le7.             \tag{12}
\]

Its full neighbourhood is a genuine separator.  Indeed, if `D\ne L`, the
component `L` lies on the other side; and `D=L` cannot occur in (12)
because `N_G(L)=T`.  Seven-connectivity therefore forces
`|N_G(D)|=7`, which is outcome 1.  Hence, if outcome 1 does not hold,
every component of `G-T` is adjacent to every literal vertex of `T`.

There cannot be four such components.  The audited four-full-component
order-eight closure applies to `T`: under (1), four components all full to
an eight-vertex boundary yield either an explicit `K_7`-minor model (when
the boundary has a triangle) or a common three-colour boundary partition
and hence a proper six-colouring of `G` (when it is triangle-free).  Both
contradict (1).  Thus `G-T` has exactly two or three components.  This is
outcome 2, and (4) follows from `L\subsetneq C`.

Finally choose an edge `xy` from `L` to `T`.  It exists by (3).  Edge
deletion is a proper minor, so `G-xy` has a proper six-colouring.  Its ends
must have the same colour; otherwise restoring `xy` would six-colour `G`.
This proves the response assertion. \(\square\)

## Corollary (well-founded reduction of the non-two-connected case)

Repeatedly apply the theorem while the returned interface still has three
components and its selected component has a cutvertex.  At every such
three-component return, the audited boundary classification for the
standing hypothetical-counterexample hypotheses implies that a
nonterminal boundary is one of the residual 82 types and hence contains a
triangle.  Thus the theorem's triangle hypothesis is restored at every
iteration.  The selected component order decreases strictly at each
order-eight return.

Consequently the iteration terminates in an actual order-seven separation,
a two-component order-eight interface, or a three-component order-eight
interface whose selected component has no cutvertex.  In the last case the
selected component may be a singleton, an edge, or a two-connected graph.
The audited induced-path completion can be invoked for the edge only if its
additional demand-pair and overlapping-interval hypotheses are separately
re-established; the fresh edge-deletion response supplied here does not by
itself preserve those data.

## Trust boundary

The theorem eliminates the entire cutvertex family by a strict unbounded
descent until either the number of complementary components drops to two or
the selected component becomes cutvertex-free.  It does not handle a
two-connected selected component, an edge or singleton selected component,
the two-component order-eight interface, or colour compatibility at a
returned order-seven separation.  The order-eight restart obtains a fresh
edge-deletion response but does not preserve the old boundary partition,
the inherited minor-model labels, or the demand/interval data required by
the induced-path completion theorem.

## Dependencies

- the block-cutvertex tree of a connected graph;
- the audited four-boundary-full-subgraph triangle construction;
- the audited four-full-component order-eight closure; and
- the audited three-component order-eight boundary classification (for the
  iterated corollary only).
