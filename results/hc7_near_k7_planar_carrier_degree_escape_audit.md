# Independent audit: planar-carrier degree escape

## Verdict

**GREEN.**  The degree lower bound and the outer-face Euler upper bound
are exact and differ by six, so the asserted fully facial attachment
configuration is impossible.  The quantitative version correctly
charges every missing unit of off-face internal degree to a literal
external edge and yields the stated surplus.  Four-connectivity supplies
both the internal degree-four bound and the simple facial-cycle setting.
The old exterior carrier in Corollary 3 has the required induced internal
graph, minimum-degree host, planar embedding, and actual external
boundary.

## 1. Degree lower bound

Write `H=G[K]`.  Since `H` is four-connected, every vertex has degree at
least four in `H`.  For `v in K-V(F)`, condition (1.1) says that every
neighbour of `v` in the host already lies in `K`.  Because `H` is the
induced subgraph on `K`,

\[
                         d_H(v)=d_G(v)\ge6.
\]

Thus the `n-f` vertices off the facial cycle contribute at least six
each and the `f` cycle vertices contribute at least four each.  The
handshake lemma gives exactly

\[
                         2m\ge6(n-f)+4f=6n-2f.
\]

External neighbours of vertices on `F` are irrelevant to this lower
bound; only their internal degree four is used.

## 2. Outer-face bound

The host is simple, so `H` is a simple plane graph.  Four-connectivity
implies in particular that `H` is connected and three-connected; hence
facial boundaries are simple cycles.  The given facial cycle `F` may be
chosen as the outer facial cycle on the sphere, and its boundary length
is therefore `f=|V(F)|`.

Every non-outer face has length at least three.  If `r` is the number of
faces, summing face lengths and using Euler's formula gives

\[
  2m\ge f+3(r-1)
       =f+3(m-n+1),
\]

and hence

\[
                         m\le3n-3-f,
   \qquad 2m\le6n-6-2f.
\]

Together with the lower bound this would require
`6n-2f<=6n-6-2f`, an immediate contradiction.  No triangulation or
maximal-planarity assumption is being smuggled in; the inequality uses
only simplicity and the stated outer facial cycle.

The equivalent formulation is logically exact: for any selected face,
if every carrier vertex with an outside neighbour lay on its boundary,
then every vertex missed by that face would satisfy (1.1), which the
theorem excludes.

## 3. Quantitative external load

For each `v in K-V(F)`, inducedness gives the exact identity

\[
 d_{G[K]}(v)
   =d_G(v)-|E_G(\{v\},V(G)-K)|.
\]

Every external edge counted on the right has exactly one carrier end,
so summing those subtracted terms over all off-face vertices gives
precisely `T_F`, with neither omissions nor double counting.  With
`delta(G)>=d`, while retaining internal degree at least four on `F`,
this yields

\[
                         2m\ge d(n-f)-T_F+4f.
\]

Combining it with `2m<=6n-6-2f` and rearranging gives

\[
 T_F\ge d(n-f)+4f-(6n-6-2f)
      =(d-6)(n-f)+6,
\]

exactly (2.1).  At `d=7`, this is `T_F>=n-f+6`.  In particular
`T_F>0`, so there is at least one off-face vertex; moreover, if every
such vertex had at most one external neighbour then
`T_F<=n-f`, contradicting the strict six-edge surplus.  Hence some
literal off-face carrier vertex has at least two distinct external
neighbours (the graph is simple).

## 4. Application to the old exterior carrier

In the rural outcome of the locked-two-row theorem, the old exterior
carrier is four-connected and has a plane embedding with the coherent
portal face `F`.  Interpreting the carrier as its vertex set, its internal
graph is precisely `G[K]`; the actual adhesion is
`S=N_G(K)`, so a carrier vertex has a neighbour outside `K` exactly when
it has a neighbour in `S`.

A hypothetical `HC_7` counterexample has minimum degree at least seven,
which is stronger than Theorem 1's degree-six hypothesis.  If every
attachment vertex lay on `F`, every `v in K-V(F)` would have
`N_G(v) subseteq K`, contradicting Theorem 1.  Therefore some off-face
carrier vertex has a literal neighbour in the actual adhesion.  Applying
Theorem 2 with `d=7` gives the stronger conclusion that some off-face
carrier vertex has at least two distinct literal neighbours in that
adhesion.  This is exactly the negation of the fully rural attachment
hypothesis in the active-face list-splice theorem.

## Scope

The result forces a literal off-face attachment for every four-connected
planar old exterior carrier.  It does not say that this attachment is a
usable representative of one of the four locked portal families, assign
it a foreign row label, or by itself create the protected linkage.  The
three label/rank possibilities listed in the source note remain the
correct residue.
