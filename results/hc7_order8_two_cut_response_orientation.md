# The equality response is excluded on the two-cut component

**Status:** written proof; separate internal audit GREEN in
[`hc7_order8_two_cut_response_orientation_audit.md`](hc7_order8_two_cut_response_orientation_audit.md).
This statement does not prove `HC_7`.

## Theorem (orientation of the two-cut response)

Assume the hypotheses and notation of the audited
[two-cut opposite-response theorem](hc7_order8_two_cut_opposite_response.md).
Thus `S` has order eight, `G-S` has the three boundary-full components
`C,Q_0,Q_1`, and

\[
 C=L_d\mathbin{\dot\cup}L_e\mathbin{\dot\cup}\{x,y\}.
\]

The sets `L_d,L_e` are the two components of `G[C]-{x,y}`; they miss
exactly `d,e` from `S`, respectively; and neither `x` nor `y` is adjacent
to `d` or `e`.  Moreover,

\[
 S-\{d,e\}=P\mathbin{\dot\cup}R
\]

is a bipartition, `de` is absent, and the two physical shores `C` and
`Q_0 union Q_1` have opposite singleton response sets for

\[
 \Pi_=P\mid R\mid\{d,e\},
 \qquad
 \Pi_{\ne}=P\mid R\mid\{d\}\mid\{e\}.               \tag{1}
\]

Then:

1. each closed component-side \(G[Q_i\cup S]\) has a proper six-colouring
   inducing \(\Pi_=\) on `S`;
2. the closed `C`-side realizes only \(\Pi_{\ne}\), while the closed
   \(Q_0\cup Q_1\)-shore realizes only \(\Pi_=\); and
3. every colouring in the prescribed \(\Pi_{\ne}\) response family on the
   closed `C`-side has a bichromatic `d`--`e` path whose internal vertices
   lie in `C`.  Every such path starts in `L_e`, ends in `L_d`, and meets
   `{x,y}`.  If it meets both cut vertices, its `x`--`y` subpath is either
   the edge `xy` or has all internal vertices in one of `L_d,L_e`; and
4. \(\chi(G[C])\ge4\).

## Proof

The proof of the two-cut opposite-response theorem shows that both `P,R`
are nonempty, that each of `d,e` has a neighbour in both classes, and that
`G[S]` contains two vertex-disjoint odd cycles.  Each odd cycle meets
`{d,e}`.  Deleting its distinguished member of `{d,e}` leaves a nontrivial
odd-length path in the bipartite graph `G[S-{d,e}]`.  In particular,

\[
                         E_G(P,R)\ne\varnothing.       \tag{2}
\]

Fix `i in {0,1}` and let `j=1-i`.  In a proper minor of `G`, contract
spanning trees of the following three pairwise disjoint connected sets:

\[
 Q_j\cup\{d,e\},\qquad L_d\cup P,\qquad L_e\cup R.   \tag{3}
\]

All three sets contain edges.  The first is connected because `Q_j` is
adjacent to every boundary vertex.  The other two are connected because
`L_d` meets every vertex of `P` and `L_e` meets every vertex of `R`.

The three contraction images form a triangle.  Boundary-fullness of `Q_j`
gives its two adjacencies to the other images, and (2) gives the adjacency
between the last two images.  Six-colour the proper minor and restrict the
colouring to the untouched closed side \(G[Q_i\cup S]\).  Expanding the
three contracted boundary blocks gives a proper colouring inducing exactly
\(\Pi_=\).  This proves assertion 1 for both values of `i`.

Suppose the closed `C`-side also realized \(\Pi_=\).  Choose that colouring
and the two colourings from assertion 1, permute colour names so that all
three agree on the three blocks of \(\Pi_=\), and glue them across `S`.
The three components of `G-S` are pairwise anticomplete, so this would be a
proper six-colouring of `G`, a contradiction.  Hence the closed `C`-side
does not realize \(\Pi_=\).  The opposite-response theorem says that the two
physical response sets are nonempty opposite singletons.  It follows that
`C` realizes only \(\Pi_{\ne}\) and \(Q_0\cup Q_1\) realizes only
\(\Pi_=\).  This
proves assertion 2.

If `G[C]` were three-colourable, colour the three independent blocks of
\(\Pi_=\) with three colours and colour `C` with the other three.  This is
a proper colouring of the closed `C`-side inducing \(\Pi_=\).  Together
with assertion 1 it would again give three aligned closed-side colourings
and hence a proper six-colouring of `G`.  Thus \(\chi(G[C])\ge4\), proving
assertion 4.

The bichromatic-path conclusion of the opposite-response theorem now
applies on the closed `C`-side and supplies the path in assertion 3.  Since
`L_d`, `x`, and `y` all miss `d`, every neighbour of `d` in `C` lies in
`L_e`.  Symmetrically every neighbour of `e` in `C` lies in `L_d`.
Consequently the path starts in `L_e`, ends in `L_d`, and must meet the
cut `{x,y}`.  If a simple path meets both cut vertices, the internal
vertices of its `x`--`y` subpath avoid the cut and therefore lie in one
component of `G[C]-{x,y}`, unless that subpath is the edge `xy`.  This is
the final assertion. \(\square\)

## Exact gain and trust boundary

The theorem fixes the physical orientation of the opposite responses and
places every forced unequal-response path across the two literal lobes.
It does not produce a connected boundary-block subgraph disjoint from that
path, split either lobe into labelled branch sets, or return a compatible
order-seven separation.  Those are the remaining exchange obligations.

## Dependencies

- the audited two-cut opposite-response theorem; and
- proper-minor six-colourability from minor minimality.
