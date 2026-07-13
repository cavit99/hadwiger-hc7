# A nested-triangle rooted-model principle for the near-`K_7` lock

## 1. The theorem

The following is independent of the Moser labels, the size of an expanded
piece, and any retained-tree decomposition.

### Theorem 1.1 (nested neutral triangle: `K_7` or coherent two-apex)

Let `G` be a seven-connected graph and let

\[
                         Q=\{q_1,q_2,q_3\}
\]

induce a triangle.  Put `H=G-Q`.  Suppose, after permuting the three
vertices, that

\[
 N_H(q_3)\subseteq N_H(q_1)\cap N_H(q_2).          \tag{1.1}
\]

Then at least one of the two conclusions needed in the near-clique route
holds:

\[
 \boxed{G\text{ has a }K_7\text{ minor}}
 \quad\text{or}\quad
 \boxed{G-\{q_1,q_2\}\text{ is planar}}.           \tag{1.2}
\]

In the second outcome the same two apex vertices work globally; there is
no annulus-by-annulus choice.

#### Proof

The graph `H` is four-connected.  Indeed, a separator of `H` of order at
most three, together with the three vertices of `Q`, would be a separator
of `G` of order at most six.

Let

\[
                           A=N_H(q_3).
\]

Since `G` is seven-connected, `d_G(q_3)>=7`.  The other two vertices of
the triangle account for only two neighbours, so

\[
                              |A|\ge5.              \tag{1.3}
\]

Choose any four distinct vertices `x_1,x_2,x_3,x_4` of `A`.  The rooted
`K_4` theorem of Fabila-Monroy and Wood (Theorem 6) says that a
four-connected graph has a `K_4` model rooted at these four vertices
unless the graph is planar and the four roots lie on a common face.

If the rooted model exists, write its bags as `B_1,...,B_4`, with
`x_i in B_i`.  By (1.1), every `x_i` is adjacent to all three vertices of
`Q`.  Hence

\[
             \{q_1\},\{q_2\},\{q_3\},B_1,B_2,B_3,B_4
                                                               \tag{1.4}
\]

are seven pairwise adjacent disjoint connected bags, a `K_7` model.

If any four-element subset of `A` has such a rooted model, the preceding
bags give the first outcome.  Hence assume that no four-element subset
has one.  The rooted theorem now implies that `H` is planar and **every**
four-element subset of `A` lies on a common face in its unique plane
embedding.  Fix four vertices `x_1,x_2,x_3,x_4 in A`
and a face `F` containing them.  Every other `x in A` lies on `F`: the
four vertices `x_1,x_2,x_3,x` lie on some face `F_x`, and two distinct
faces of a three-connected plane graph share at most two vertices.  Since
`F` and `F_x` share `x_1,x_2,x_3`, they are the same face.  Thus

\[
                              A\subseteq V(F).        \tag{1.5}
\]

Place `q_3` inside `F` and join it to all vertices of `A`.  These are all
of its neighbours after `q_1,q_2` are deleted, so this extends the plane
drawing of `H` to a plane drawing of `G-{q_1,q_2}`.  This is the second
outcome in (1.2).  QED.

### Corollary 1.2 (portal-set form)

In a seven-connected `K_7`-minor-free graph, every triangle `Q` satisfying
(1.1) is a certified coherent two-apex triangle: deleting the two vertices
with the larger portal neighbourhoods leaves a planar graph.

Equivalently, a non-two-apex target-free graph must satisfy the exact
anti-nesting condition

\[
 N_H(q_k)\not\subseteq N_H(q_i)\cap N_H(q_j)
 \quad\text{for every }\{i,j,k\}=\{1,2,3\}.          \tag{1.6}
\]

Thus for every `k` it has a literal private portal

\[
 z_k\in N_H(q_k)-\bigl(N_H(q_i)\cap N_H(q_j)\bigr). \tag{1.7}
\]

This is vertex-level portal placement.  Merely knowing that every
contracted owner class meets every `q_i` does not imply (1.1).

### Corollary 1.3 (minimal-counterexample anti-nesting)

Let `G` be a `K_7`-minor-free minimal counterexample to `HC_7`.  For every
triangle `Q={q_1,q_2,q_3}` and every permutation `{i,j,k}={1,2,3}`,

\[
 N_{G-Q}(q_k)\not\subseteq
 N_{G-Q}(q_i)\cap N_{G-Q}(q_j).                    \tag{1.8}
\]

Indeed, the minor outcome of Theorem 1.1 is excluded, while its other
outcome makes `G` two-apex.  A two-apex graph is six-colourable: four-colour
the planar remainder and give the two deleted vertices two fresh colours.
Thus the second outcome is also incompatible with a counterexample.

For any displayed near-clique triangle this produces three literal
vertex-level witnesses of (1.7); they cannot all be hidden in a quotient
statement saying merely that each owner is contacted.

### Corollary 1.4 (common-core weakening)

Put

\[
 A_\cap=N_H(q_1)\cap N_H(q_2)\cap N_H(q_3).
\]

If `|A_cap|>=4`, then either `G` has a `K_7` minor, or `H` is planar and
all vertices of `A_cap` lie on one face.  In the latter outcome, if every
remaining `q_3`-portal also lies on that face, then
`G-{q_1,q_2}` is planar.

#### Proof

Apply the Fabila-Monroy--Wood theorem to every four-subset of `A_cap`.
A rooted model gives `K_7` exactly as in (1.4).  Otherwise `H` is planar,
and every four-subset is cofacial.  For more than four vertices, fix three
and use the fact that distinct faces of a three-connected plane graph
share at most two vertices; for exactly four there is nothing more to
prove.  If all `q_3`-neighbours lie on that face, insert `q_3` there as in
the proof of Theorem 1.1. QED.

This is the strongest immediate portal-set weakening.  Model-level class
incidence alone does not put the private `q_3`-portals on the common face.
A spanning near-`K_7` application may therefore replace literal nesting
by two separately proved assertions: a four-vertex common portal core and
cofaciality of every private `q_3` attachment.  Without the second
assertion the coherent two-apex conclusion does not follow.

## 2. Why this is the right sharp obstruction

Take the homogeneous exceptional three-piece word `(c,c,a)` and split
the first piece into adjacent vertices `U,V` with rows

\[
\begin{aligned}
 U&\sim a,b,q_1,q_2,q_3,X_2,\\
 V&\sim q_1,q_2,q_3,X_2.
\end{aligned}                                      \tag{2.1}
\]

Keep all other edges of the near-`K_7` quotient.  The resulting
ten-vertex graph is

\[
                              K_3\vee T,             \tag{2.2}
\]

where the universal `K_3` is `q_1q_2q_3` and `T` is the following
seven-vertex 2-tree.  Start with the triangle `bX_2X_3`, add `U` on the
edge `bX_2`, add `a` and `V` on the edge `UX_2`, and add `c` on the edge
`bX_3`.

Consequently the graph has no `K_7` minor.  Indeed `T` is
`K_4`-minor-free, and for every graph `R`

\[
                         \eta(K_3\vee R)=3+\eta(R).  \tag{2.3}
\]

It is also not two-apex.  It has 35 edges.  Each `q` has degree nine, and
a direct check in the displayed 2-tree gives maximum joined degree eight,
attained only at `X_2`.  Thus deleting any pair other than two `q`
vertices leaves eight vertices and more than 18 edges, hence a nonplanar
graph.  Deleting two `q` vertices leaves a subdivision of
`K_{3,3}`: suppress the degree-two vertex `b`, and use bipartition

\[
                         \{a,V,X_3\}\mid\{U,X_2,q\}. \tag{2.4}
\]

The graph has connectivity five.  Deleting fewer than five vertices
either leaves a universal `q`, or deletes all three `q` vertices and at
most one vertex of the 2-connected 2-tree, so it leaves the graph
connected.  On the other hand

\[
                         \{q_1,q_2,q_3,X_2,U\}       \tag{2.5}
\]

separates `V`.  Thus it does not contradict Theorem 1.1.  Rather, it
shows sharply what seven-connectivity has to destroy: the local
series-parallel core behind the neutral triangle.

The same architecture occurs in the inclusion-maximal negative rows of
the cross-split atlas.  The cross is not defeated by adding arbitrary
portal incidences; it is defeated only when the incidences either create
a rooted `K_4` meeting the neutral triangle or align into the cofacial
outcome of Theorem 1.1.

## 3. The exact capacity statement at a society cross

Let `X_1,X_2,X_3` be an exceptional defect-one three-piece path in the
shell

\[
 L=\{a,b,c,q_1,q_2,q_3\},\qquad G[L]=K_6-\{ab,ac\}.
\]

Suppose a distinct-class society cross in `X_t` is extended to a
connected adjacent bipartition

\[
                         X_t=U\mathbin{\dot\cup}V.    \tag{3.1}
\]

For `R in {U,V}`, let `S(R)` be the set of external **owner classes**
seen by `R`: singleton labels in `L` and adjacent original pieces, but not
the other member of `{U,V}`.

The dependency-free verifier
`near_k7_exceptional_cross_split_atlas.py` proves the following exact
quotient lemma.

### Lemma 3.1 (cross-capacity lemma)

1. In each of the six mixed exceptional words
   `(c,q_i,b),(b,q_i,c)`, every distinct-class cross split gives a
   `K_7` minor.
2. In each of the four homogeneous words
   `(c,c,a),(b,b,a),(a,b,b),(a,c,c)`, either the split gives a `K_7`
   minor or, after interchanging `U,V`,

   \[
                              |S(U)|\le5.             \tag{3.2}
   \]

3. If arbitrary owner classes are allowed to have portals on both sides,
   every inclusion-maximal negative row has exactly four common owner
   classes.  In particular five common owner classes force `K_7`.

The computation covers all 480 minimal cross rows and all 12,960 support
pairs with duplicated owner contacts.  For each ten-vertex connected
quotient it enumerates all 5,880 spanning partitions into seven nonempty
bags, verifies connectedness of every bag and all 21 bag adjacencies, and
therefore exhausts all `K_7` models.  A clique model in a connected graph
can always be extended to a spanning model, so this enumeration loses
nothing.

### Corollary 3.2 (actual gate or portal surplus)

Assume the displayed shell and the three pieces are spanning.  In the
`K_7`-free outcome of Lemma 3.1, choose `U` satisfying (3.2).  For every
nonsingleton owner `Y in S(U)`, put

\[
 P_Y=N_Y(U),\qquad P_V=N_V(U).                       \tag{3.3}
\]

The actual external neighbourhood is the disjoint union of the contacted
singleton labels and the portal sets in (3.3).  If every `P_Y` and `P_V`
is a singleton, then

\[
                              |N_G(U)|\le6,           \tag{3.4}
\]

and `N_G(U)` is an explicit separator, contrary to seven-connectivity.
More generally, seven-connectivity forces the exact surplus inequality

\[
 (|P_V|-1)+\sum_{Y\in S(U),\,Y\text{ nonsingleton}}(|P_Y|-1)
                         \ge 6-|S(U)|.                \tag{3.5}
\]

#### Proof

The other cross side contributes the class `V`, in addition to the at
most five classes in `S(U)`.  The full external owner set has order six
for an end piece and seven for the middle piece, so (3.2) also leaves an
uncontacted owner class outside `U union N_G(U)`.  Hence `N_G(U)` is a
genuine separator.  Under the singleton-gate hypothesis its actual
vertices form a set of order at most six, proving (3.4).  In general the right side
of (3.5) is exactly the deficit between the baseline
`1+|S(U)|` and the seven neighbours required by connectivity.  QED.

Thus a first nonrural conflict has now been reduced without contracting
an annular sequence:

\[
 \boxed{K_7}
 \quad\text{or}\quad
 \boxed{\text{an actual cut of order at most six}}
 \quad\text{or}\quad
 \boxed{\text{a nonzero distributed portal surplus}}.       \tag{3.6}
\]

Theorem 1.1 closes the distributed-surplus family whenever the three
neutral portal neighbourhoods become nested; its cofacial conclusion
propagates one fixed pair of apex labels across the whole graph.  Hence
the exact unresolved state is now simultaneous:

* the four-common-owner capacity lock of Lemma 3.1;
* strict portal surplus in (3.5); and
* the three anti-nesting witnesses (1.7).

The last bullet is essential.  The ten-vertex 2-tree join in Section 2
shows that owner-class contact data alone cannot replace the vertex-level
neighbourhood condition (1.1).
