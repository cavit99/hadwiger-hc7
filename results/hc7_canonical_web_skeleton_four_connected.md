# Four-connectivity of the canonical web skeleton

**Status:** written proof, independently audited in
[`hc7_canonical_web_skeleton_four_connected_audit.md`](hc7_canonical_web_skeleton_four_connected_audit.md).
This is a structural consequence of the hypotheses in the promoted canonical
rooted-web theorem.  It applies independently of the order-two and
order-three list-critical residues, but it does not complete either one.

## 1. Statement

Let `W` be a plane graph whose outer face has boundary

\[
                         a b c d a.                    \tag{1.1}
\]

Assume that every bounded face of `W` is a triangle and every triangle of
`W` is facial.  Form a web completion `W^+` as follows: for any facial
triangle `T`, an optional clique `X_T` may be added, complete to `T` and
with no neighbours in `W^+-(T\cup X_T)`.

Let `Q` be a spanning subgraph of `W^+`.  Assume:

1. `Q` has no vertex cut of order at most two; and
2. every vertex cut of order three in `Q` contains both `c` and `d`.

In the application from
[`../results/hc7_star_order_eight_rooted_web.md`](../results/hc7_star_order_eight_rooted_web.md),
the labels are

\[
 a=\ell_e,\qquad b=\ell_f,\qquad c=z_e,\qquad d=z_f.
\]

Thus `c,d` are the contracted images of the two deficient boundary edges,
and (1.1) is the canonical outer order.

### Theorem 1.1

Under these hypotheses, `W` is four-connected.  Neither diagonal `ac` nor
`bd` belongs to `W`.  Adding either one in the outer face gives a simple
four-connected plane triangulation.

## 2. Separators of the skeleton remain separators of the completion

### Lemma 2.1

If `U\subseteq V(W)` and `W-U` is disconnected, then `W^+-U` is
disconnected.  Consequently `Q-U` is disconnected.

### Proof

Let `C_1,C_2` be distinct components of `W-U`.  Consider an attachment
clique `X_T`.  If `T-U` is nonempty, then all vertices of `T-U` belong to
one component of `W-U`, because they are pairwise adjacent.  The vertices
of `X_T` can therefore attach to at most that one component.  If
`T\subseteq U`, then `X_T` has no remaining neighbour in `W-U` and cannot
join two components of `W-U`.

No attachment clique joins `C_1` to `C_2`, so `W^+-U` is disconnected.
Since `Q` is a spanning subgraph of `W^+`, deleting `U` also disconnects
`Q`. \(\square\)

### Corollary 2.2

The graph `W` is three-connected, and every three-vertex cut of `W`
contains `c,d`.

### Proof

Lemma 2.1 would turn a cut of `W` of order at most two into such a cut of
`Q`, contrary to hypothesis 1.  It likewise turns every three-vertex cut
of `W` into a three-vertex cut of `Q`, to which hypothesis 2 applies.
\(\square\)

## 3. Proof of Theorem 1.1

First, neither outer diagonal belongs to `W`.  Suppose, for example, that
`ac\in E(W)`.  The two triangles `abc` and `acd` would both be facial.
They fill the closed disk bounded by the outer four-cycle, so `W` would
have no other vertex and would equal the four-cycle plus the diagonal
`ac`.  The set `{a,c}` separates `b` from `d`, contrary to Corollary 2.2.
The argument for `bd` is symmetric.

Draw the edge `ac` in the outer face and call the resulting plane graph
`M`.  Every face of `M` is a triangle, so `M` is maximal planar.

We use the elementary separator property of maximal planar graphs: every
three-vertex cut is the vertex set of a separating triangle.  For
completeness, take a component behind such a cut.  Three-connectivity
forces it to have all three cut vertices as neighbours.  In a plane
triangulation, the boundary between that component and the rest is
therefore the three-cycle on the cut vertices.  Vertices occur on both
sides of this cycle, so it is separating.  Conversely, deleting a
separating triangle plainly disconnects the graph.  In particular, a
facial triangle is not a three-vertex cut.

Suppose now that `U` is a three-vertex cut of `W`.  By Corollary 2.2,

\[
                         U=\{c,d,x\}                  \tag{3.1}
\]

for some vertex `x`.  Because the added edge `ac` has an endpoint in `U`,

\[
                         M-U=W-U.                     \tag{3.2}
\]

Thus `U` is a three-vertex cut of the maximal planar graph `M` and must be
a separating triangle.

There are three possibilities.  If `x=a`, the triangle `acd` is one of
the two new facial triangles formed in the outer face.  If `x=b`, then
`U` is not a triangle because `bd\notin E(M)`.  If
`x\notin\{a,b\}`, then the triangle `cdx` already belongs to `W`; it is
facial by hypothesis, and adding `ac` in the outer face does not change
that face.  None of the three possibilities is a separating triangle of
`M`, contradicting (3.1)--(3.2).

Therefore `W` has no three-vertex cut.  Together with Corollary 2.2 this
proves that `W` is four-connected.  Adding an edge cannot lower vertex
connectivity, so both planar triangulations `W+ac` and `W+bd` are also
four-connected. \(\square\)

## 4. Exact trust boundary

Theorem 1.1 concerns the plane skeleton `W`, not the original quotient
`Q`.  The graph `Q` is only a spanning **subgraph** of the web completion:
it may omit edges of `W`, and it may contain vertices in attachment
cliques which are not vertices of `W`.  Nothing above proves that `Q` is
four-connected.

Thomassen proved that every four-connected planar graph is
Hamiltonian-connected: C. Thomassen, *A theorem on paths in planar
graphs*, Journal of Graph Theory **7** (1983), 169--176,
[doi:10.1002/jgt.3190070205](https://doi.org/10.1002/jgt.3190070205).
It follows that `W` has a Hamilton path between every prescribed pair of
its vertices.  This does not give a path in `Q`, because such a Hamilton
path may use skeleton edges omitted from `Q`.

Nor does Hamiltonian-connectedness supply the missing labelled linkage.
The absent linkage joins `a` to `c` and `b` to `d`; these pairs alternate
on the outer face of `W`, so two vertex-disjoint paths joining them cannot
exist in the planar skeleton.  Finally, Hamiltonian-connectedness carries
no boundary-colouring data and therefore gives no proper-minor colouring
response by itself.

Thus the theorem is a reusable structural simplification, but a further
label-preserving mechanism would still have to replace every virtual
skeleton edge it uses by an actual path or colouring transition in `Q`.
