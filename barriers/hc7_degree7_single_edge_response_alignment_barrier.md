# A bond response need not select one aligned edge by matching data alone

**Status:** abstract barrier/counterexample to an intermediate response-
counting claim; [separate internal audit **GREEN**](hc7_degree7_single_edge_response_alignment_barrier_audit.md).
This is a consistent boundary-response table, not a graph claimed to
satisfy all hypotheses of a minor-minimal `HC_7` counterexample.

## Refuted inference

The following inference is false from the exact degree-seven matching
languages and the equality signatures of a two-edge bond alone:

> If deleting two nonseparating layer edges together returns a boundary
> matching containing `e_0,e_1`, then deleting at least one edge alone
> returns a matching containing `e_0,e_1`.

## Response table

Let the boundary complement be

\[
                   F=K_{3,4},qquad H=\overline F=K_3\mathbin{\dot\cup}K_4,
\tag{2.1}
\]

and choose three disjoint edges

\[
                         e_0,e_1,e_2\in E(F).          \tag{2.2}
\]

Let `D=\{h_1,h_2\}` be the two operation edges.  On the common host with
both edges deleted, prescribe the following three response records:

\[
\begin{array}{c|c|c}
 \text{operation}&(h_1,h_2)\text{ endpoint signature}
                  &\text{boundary matching}\\ \hline
 G-h_1&(\mathrm{equal},\mathrm{proper})&\{e_0,e_2\}\\
 G-h_2&(\mathrm{proper},\mathrm{equal})&\{e_0,e_2\}\\
 G-D&(\mathrm{equal},\mathrm{equal})&\{e_0,e_1\}.
\end{array}                                             \tag{2.3}
\]

Here the first two colourings are simply restricted to the common
double-deletion host when their signatures are compared.  Both single-edge
responses omit `e_1`; only the simultaneous response is aligned with the
target pair `e_0,e_1`.

## Checks

The table satisfies every matching-level condition used in the proposed
inference.

1. `F` is triangle-free, while `alpha(H)=2` and `chi(H)=4`.
2. The three selected edges form a matching of order three.  Each response
   matching in (2.3) has order two and therefore belongs to the exact pole-
   shore language.  The intact opposite-shore language may still be all
   singleton matchings of `F`.
3. The equality signatures have the required restoration logic.  The edge
   absent in a single-edge operation is monochromatic; the other edge is
   present and proper.  In the common deletion both are monochromatic.  A
   `(proper,proper)` signature would restore both edges and is deliberately
   absent.
4. For the selected matching `M=\{e_0,e_1,e_2\}`, every graph

   \[
                              H+(M-\{e\}),\qquad e\in M, \tag{2.4}
   \]

   is `K_6`-minor-free.  It consists of the disjoint cliques `K_3,K_4`
   joined by two independent edges.  A `K_6` model on seven vertices would
   use either six singleton bags or five singleton bags and one two-vertex
   bag.  The first case would require a `K_6` subgraph.  In the second,
   contracting one edge still leaves nonadjacent singleton vertices on
   opposite clique sides.  Neither case is possible.

Thus response order, matching choice, edge-restoration signatures and the
finite boundary minor exit do not force a single aligned edge.

## Exact scope

This table is not asserted to be the response relation of one
seven-connected, `K_7`-minor-free, fully minor-critical host.  It does not
encode the five endpoint Kempe locks or the literal rooted `K_5` bags.
Accordingly it does not refute a theorem which genuinely spends those
global data.  It proves only that counting boundary matchings or reselecting
one proper-minor colouring cannot establish the missing existential
quantifier.  A positive proof must couple several operations, their literal
geometry, or the whole rooted-bag cycle.
