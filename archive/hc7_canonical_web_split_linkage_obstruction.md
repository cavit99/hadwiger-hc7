# The split-edge linkage is crossed in the canonical web

**Status:** written proof; not yet separately audited.  This note identifies
an obstruction to using the split-edge completion theorem as a purely
geometric continuation of the canonical rooted-web theorem.  It is not a
counterexample to `HC_7` and does not eliminate the balanced order-eight
configuration.

## 1. Setup

Use the notation and hypotheses of
[`../results/hc7_star_order_eight_rooted_web.md`](../results/hc7_star_order_eight_rooted_web.md).
Thus `Q` is a spanning subgraph of an

\[
             (\ell_e,\ell_f,z_e,z_f)\text{-web }H^+,
\]

and the image of the second five-clique lies behind the facial triangle

\[
                         T=\{z_e,z_f,x\}
\]

incident with the virtual outer edge `z_e z_f`.  The graph `Q-T` has
exactly two components.  Denote by `A_Q` the one containing
`ell_e,ell_f`, and by `A` its literal preimage before the two defect edges
are contracted.

The hypotheses of the rooted-web theorem include that every three-vertex
cut of `Q` contains both `z_e,z_f`.

## 2. No attachment clique occurs on the leaf side

### Lemma 2.1

In the web completion `H^+`, every nonempty attachment set `X_U` is
supported by `U=T`.  In particular, every vertex of `A_Q` is a vertex of
the planar skeleton `H`.

### Proof

Let `U` be a facial triangle of `H` and suppose `X_U` is nonempty.  No
vertex of `X_U` has a neighbour outside `U union X_U`.  Since `Q` is
connected and spans `H^+`, deleting `U` separates a vertex of `X_U` from
an outer-frame vertex outside the three-set `U`.  Hence `U` is a
three-vertex cut of `Q`.

Every such cut contains `z_e,z_f`.  In the plane skeleton there is only
one internal facial triangle incident with the outer edge `z_e z_f`,
namely `T`.  Therefore `U=T`.

The rooted-web localization theorem says that the component of `Q-T`
opposite `A_Q` is contained in `X_T`.  Consequently `A_Q` contains no
attachment vertex and lies in the planar skeleton. \(\square\)

## 3. The two candidate linkages are impossible

### Theorem 3.1 (canonical crossing obstruction)

The literal leaf shore `A` does not contain vertex-disjoint connected
subgraphs `P,Q` satisfying

\[
 \ell_f\in V(P),\qquad P\text{ adjacent to }x,
 \qquad
 \ell_e\in V(Q),\qquad Q\text{ adjacent to }V(e).       \tag{3.1}
\]

It also does not contain the symmetric configuration

\[
 \ell_e\in V(P),\qquad P\text{ adjacent to }x,
 \qquad
 \ell_f\in V(Q),\qquad Q\text{ adjacent to }V(f).       \tag{3.2}
\]

### Proof

The outer face of the planar skeleton has boundary

\[
                 \ell_e\ell_f z_e z_f\ell_e.
\]

The internal face incident with its edge `z_e z_f` is the triangle
`z_e z_f x`.  Replacing that outer edge by the other two sides of this
triangle gives the simple cycle

\[
              C=\ell_e\ell_f z_e x z_f\ell_e.           \tag{3.3}
\]

The component `A_Q` lies in the closed disk bounded by `C`; the attachment
set `X_T` lies on the other side of the path `z_e x z_f`.  By Lemma 2.1,
every edge with both ends in `A_Q union T` is represented in this planar
disk.

Suppose (3.1) holds.  Inside `P`, take a path from `ell_f` to a vertex
having a neighbour at `x`, and add the final edge to `x`.  Inside `Q`,
take a path from `ell_e` to a vertex having a neighbour at an endpoint of
the literal edge `e`, and add that final edge.  Contracting `e` maps the
second path to an `ell_e-z_e` path in `Q`.  The two resulting paths are
vertex-disjoint: the original subgraphs `P,Q` are disjoint and lie in the
open shore, while `x` and the endpoints of `e` lie in the boundary.

On the boundary cycle (3.3), the four ends occur in the cyclic order

\[
                         \ell_e,\ell_f,z_e,x.
\]

Thus an `ell_e-z_e` path and an `ell_f-x` path would join alternating
pairs in a disk.  The Jordan curve theorem excludes two vertex-disjoint
such paths.  This contradicts (3.1).

For (3.2), contraction of `f` would instead give disjoint paths joining
`ell_e` to `x` and `ell_f` to `z_f`.  Their four ends occur on `C` in the
cyclic order

\[
                         \ell_e,\ell_f,x,z_f,
\]

so the same alternating-pairs argument gives a contradiction. \(\square\)

## 4. Consequence for the active proof route

The explicit branch-set construction in
[`../results/hc7_star_order_eight_split_edge_completion.md`](../results/hc7_star_order_eight_split_edge_completion.md)
remains correct.  Theorem 3.1 shows, however, that neither of its two
candidate linkages can be forced from the localized rooted-web geometry:
the linkages are precisely the two planar crossings excluded by that
geometry.  Keeping the four literal endpoints of the two defect edges
does not change this conclusion, because contracting the relevant edge
maps any literal witness to the forbidden linkage while preserving
disjointness.

Accordingly, a positive continuation must use an additional host-level
effect which is absent from the static web description, such as a
proper-minor colouring transition that destroys the web description,
produces a common boundary colouring, or exposes an actual order-seven
separation.  Seven-connectivity and endpoint splitting alone do not
provide the proposed paths.

The web definition and the prescribed-linkage obstruction used here are
from R. Fabila-Monroy and D. R. Wood, *Rooted K4-Minors*, Electronic
Journal of Combinatorics 20(2) (2013), P64, especially Lemma 2 and the
definition immediately preceding it.
