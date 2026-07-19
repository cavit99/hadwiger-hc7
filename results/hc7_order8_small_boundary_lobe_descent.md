# Small-boundary lobe descent at an order-eight interface

**Status:** written proof; separate internal audit GREEN in
[`hc7_order8_small_boundary_lobe_descent_audit.md`](hc7_order8_small_boundary_lobe_descent_audit.md).
This statement is not a proof of `HC_7`.

## Theorem 1 (small-boundary lobe descent)

Let `G` be a seven-connected graph satisfying

\[
 \chi(G)=7,\qquad K_7\not\preccurlyeq G,
 \qquad \chi(M)\le6\text{ for every proper minor }M\text{ of }G.
 \tag{1.1}
\]

Let `S` have order eight, let `C` be a component of `G-S`, and suppose
that `G-S` has a component other than `C`.  Let `L` be a nonempty connected
proper subset of `C` such that

\[
                 |N_{G[C]}(L)|+|N_G(L)\cap S|\le8.       \tag{1.2}
\]

Then at least one of the following holds.

1. `G` has an actual separation of order seven.
2. With `T=N_G(L)`, one has `|T|=8`, the graph `G-T` has exactly two or
   three components, every one of those components is adjacent to every
   literal vertex of `T`, and `L` is one of them.

In outcome 2, `|L|<|C|`, and deleting any edge between `L` and `T` gives a
proper six-colouring in which the two ends of the deleted edge have the
same colour.

### Proof

Because `C` is a component of `G-S`, every neighbour of `L` outside `C`
lies in `S`.  Hence the two terms in (1.2) are disjoint and

\[
                        T=N_G(L),\qquad |T|\le8.          \tag{1.3}
\]

The set `T` is a genuine separation boundary.  The side `L` is nonempty,
and a component of `G-S` other than `C` lies outside `L\cup T`.  Therefore
seven-connectivity gives `|T|\ge7`.

If `|T|=7`, conclusion 1 holds.  Assume `|T|=8`.  Since `T=N_G(L)`, the
set `L` is a component of `G-T`.  It is a strict descent because
`L\subsetneq C`.

Let `D` be any component of `G-T`.  If `D` is not adjacent to some vertex
of `T`, then `|N_G(D)|\le7`.  This is again a genuine separation boundary:
`D` is not `L`, because `N_G(L)=T`, while `L` lies on the opposite side.
Seven-connectivity forces `|N_G(D)|=7`, giving conclusion 1.  Thus, if
conclusion 1 does not hold, every component of `G-T` is full to `T`.

There are at least two components.  There are not four: the promoted
four-full-component order-eight closure says that, under (1.1), four
components all full to an eight-vertex boundary force either an explicit
`K_7`-minor model or a proper six-colouring of `G`.  Hence `G-T` has
exactly two or three components, proving conclusion 2.

Finally, delete an edge `xy` with `x\in L` and `y\in T`.  Such an edge
exists because `T=N_G(L)`.  The graph `G-xy` is a proper minor and is
six-colourable by (1.1).  Its ends have the same colour in every such
colouring, since otherwise restoring `xy` would six-colour `G`. \(\square\)

## Corollary 2 (two-separator residue)

Assume in addition that `G-S` has exactly three `S`-full components
`C,Q_0,Q_1`, that `G[S]` contains a triangle, and that `G[C]` is
two-connected.  Let `X={x,y}` be a two-vertex cut of `G[C]`.

For every component `L` of `G[C]-X`, either `L` is adjacent to at least
seven vertices of `S`, or Theorem 1 gives an actual order-seven separation
or a strict boundary-full order-eight descent.

Moreover, in the absence of a `K_7` minor, at most one component of
`G[C]-X` is adjacent to all eight vertices of `S`.  Consequently, if no
outcome of Theorem 1 occurs, then every component of `G[C]-X`, except
possibly one `S`-full component, has exactly seven neighbours in `S`.

### Proof

Two-connectivity forces every component `L` of `G[C]-X` to have a
neighbour of both `x` and `y`: if, for example, it had no neighbour of
`x`, then deleting `y` would separate `L` from the rest of `G[C]`.
Therefore

\[
                         N_{G[C]}(L)=X.                  \tag{2.1}
\]

If `L` has at most six neighbours in `S`, then (1.2) holds and Theorem 1
applies.  This proves the first assertion.

If two distinct components `L_1,L_2` of `G[C]-X` were both `S`-full,
then `L_1,L_2,Q_0,Q_1` would be four pairwise disjoint connected subgraphs
full to `S`.  Together with a triangle in `G[S]`, the standard
four-full-subgraph construction gives an explicit `K_7`-minor model.  Thus
at most one such component is `S`-full.  Combining this with the first
assertion gives the final statement. \(\square\)

## Exact gain and trust boundary

Theorem 1 is a reusable host-level descent criterion independent of a
particular boundary colouring or branch-set labelling.  Corollary 2 reduces
the non-three-connected selected component to a sharply constrained
residue: every lobe behind every two-cut sees seven of the eight boundary
vertices, apart from at most one full lobe.

The result does not eliminate that nearly-full two-separator residue.  It
does not preserve an inherited boundary equality partition, demand pairs,
minor-model labels, or compatible colourings at a returned order-seven
separation.  A two-component order-eight return remains terminal for this
descent.

## Dependencies

- elementary separation facts in a two-connected graph;
- the promoted four-full-component order-eight closure; and
- the promoted four-full-connected-subgraph plus boundary-triangle minor
  construction.
