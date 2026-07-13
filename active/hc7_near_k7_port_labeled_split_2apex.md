# Port-labelled near-(K_7): planar expansion or an alternating cross

## 1. Why the apex pair cannot be prescribed

The connectivity-only example from
`../archive/hadwiger_near_k7_two_complex_bag_round.md` is sharper than merely showing
that a bag need not split.  Let

\[
                         G=K_2\vee I,
\]

where (I) is the icosahedron and the two universal vertices are (p,q).
In the displayed spanning (K_7^-)-model, the deficient singleton pair is
(u_0,u_2).  Deleting that pair does **not** make (G) planar: the five
vertices

\[
                         p,q,t,u_3,u_4
\]

induce a (K_5).  On the other hand, deleting (p,q) leaves the planar
icosahedron.

Thus even when the graph really is two-apex, the two apex vertices need not
be the deficient model vertices.  Any correct near-clique theorem must say

\[
             \text{(K_7)-minor or *some* two-apex pair},       \tag{1.1}
\]

not prescribe that pair from one selected model.  The example is
seven-connected, has minimum degree seven, and is (K_7)-minor-free.  It
also shows why a connectivity-only proof cannot distinguish a locked bag
from a planar expansion.  What it lacks is seven-criticality.

## 2. Expansion societies

Let (Q) be a plane graph and let (din V(Q)).  Remove a small open disk
around (d).  The incident edge ends occur on the boundary circle in a
cyclic order

\[
                         \Omega_d=(e_1,\ldots,e_m).              \tag{2.1}
\]

Suppose (d) is the contraction image of a connected subgraph (D) of an
uncontracted graph (H).  Every occurrence (e_i) has a specified
attachment vertex (alpha_iin V(D)).  Call

\[
                         (H[D];\alpha_1,\ldots,alpha_m)         \tag{2.2}
\]

the **expansion society** at (d).  Repetitions among the
(alpha_i) are allowed.

The society is **rural in the prescribed rotation** when (H[D]) has an
embedding in a closed disk in which the attachment occurrences lie on the
boundary in the cyclic order (2.1).  Edges of (H[D]) may otherwise meet
the boundary only at their ends.

### Theorem 2.1 (port-labelled disk expansion)

Let (D_1,\ldots,D_s) be pairwise disjoint connected subgraphs of a graph
(H).  Contract each (D_i) to (d_i), and suppose the resulting graph
(Q) has a plane embedding.  If every expansion society at (d_i) is
rural in the rotation induced by that embedding, then (H) is planar.

The same conclusion holds with a prescribed face (F): if selected
vertices or attachment occurrences of every society are required to lie
on the boundary arc exposed to (F), then after expansion all selected
objects lie on the boundary of the corresponding face of (H).

#### Proof

Choose pairwise disjoint closed disks around the vertices (d_i), each
meeting (Q) only in the radial ends of its incident edges.  Delete the
interiors of these disks.  In the (i)-th disk place the rural embedding
of the society, matching its boundary occurrences to the radial edge ends
in their prescribed cyclic order.  No two inserted drawings meet because
the disks are disjoint, and no inserted drawing crosses an old edge because
old edges lie outside their interiors.  This produces a plane drawing of
(H).  The face-preserving assertion follows by choosing the distinguished
boundary arc on the side incident with (F).  \(\square\)

This elementary theorem is the exact step missing from an argument which
only proves that a **contracted** quotient is planar.

## 3. Complete characterization for a tree bag

The rotation obstruction is especially transparent for the locked Steiner
trees obtained by minimizing a near-clique bag.

Let (T) be a tree with attachment occurrences
(e_1,\ldots,e_m).  Form an augmented tree (widehat T) by adding a new
leaf (lambda_i) at the attachment vertex of (e_i).  For an edge
(fin E(T)), the two components of (widehat T-f) partition the set of
attachment leaves.

### Theorem 3.1 (tree interval criterion)

The tree society has a rural embedding with boundary order
(Omega=(e_1,\ldots,e_m)) if and only if, for every edge (fin E(T)),
the attachment leaves in either component of (widehat T-f) form a cyclic
interval of (Omega).

If the condition fails, there are an edge (f), two attachments
(r_1,r_2) on one side of (T-f), and two attachments (s_1,s_2) on the
other side, which occur alternately:

\[
                         r_1,s_1,r_2,s_2                         \tag{3.1}
\]

around the contracted vertex.  Call (3.1) an **alternating port cross**.

#### Proof

Necessity follows from the outer-face walk of a plane tree.  Deleting the
drawing of one tree edge separates the two subtrees in the cyclic leaf
order: all boundary leaves belonging to either subtree occur consecutively.

For sufficiency, induct on the number of edges of (T).  Delete an edge
(f).  By hypothesis the attachment orders of the two resulting subtrees
occupy complementary cyclic intervals.  The same interval condition holds
recursively inside each interval for every remaining tree edge.  Embed the
two augmented subtrees in disjoint subdisks by induction and join their
copies of (f) across the common boundary arc.  Repeating this construction
gives an embedding of the augmented tree with the required leaf order;
deleting the auxiliary leaves gives the required society embedding.

Finally, a subset of a cyclic order is not an interval exactly when two of
its members and two members of its complement alternate.  Applying this to
the failed edge cut gives (3.1).  \(\square\)

The theorem is label-preserving.  It identifies the actual tree edge whose
two sides carry the crossing portal classes; it does not merely say that
some abstract planar embedding fails.

## 4. The rooted-triangle quotient and its exact four outcomes

The following packages the strongest valid part of the near-(K_7)
two-complex-bag route.  Let (T=\{q_1,q_2,q_3\}) be a triangle, put
(J=G-T), and suppose (G) is seven-connected.  Then (J) is
four-connected.

Let (a,cin V(J)) be complete to (T), and let (D,Esubseteq V(J))
be disjoint connected sets, each collectively adjacent to all three
vertices of (T).  Contract (D,E) to (d,e), obtaining

\[
                         Q=J/D/E.                               \tag{4.1}
\]

### Theorem 4.1 (port-labelled rooted-triangle dichotomy)

At least one of the following holds.

1. (G) contains a (K_7)-minor.
2. The quotient (Q) has a separator of order at most three containing
   (d) or (e).  Its lift is the exact two-carrier adhesion described in
   `../archive/hadwiger_triangle_carrier_contraction_dichotomy.md`.
3. The quotient (Q) is planar with (a,c,d,e) on one face, but at least
   one of the two expansion societies is not rural in the induced rotation.
   If its selected portal core is a tree, Theorem 3.1 returns an explicit
   alternating port cross.
4. The quotient has such a plane embedding and both societies are rural;
   hence (J) is planar.  Moreover:
   * if all neighbours in (J) of some (q_i) lie on one face, then (G)
     is two-apex; and
   * if every common neighbour of (T) lies on one face, then
     (chi(G)\le6).

#### Proof

If (Q) is not four-connected, Lemma 2.1 of
`../archive/hadwiger_triangle_carrier_contraction_dichotomy.md` says that every
separator of order at most three contains (d) or (e), giving outcome
2.

Assume (Q) is four-connected.  Apply the rooted-(K_4) theorem to the
roots (a,c,d,e).  A rooted (K_4)-model lifts through the contractions
to four pairwise adjacent branch sets in (J), each adjacent to all three
singleton bags of (T).  These seven bags give outcome 1.  In the other
case the rooted theorem gives a plane embedding of (Q) with the four
roots on one face.

If a society is not rural, this is outcome 3; for a tree society Theorem
3.1 supplies its explicit cross.  If both are rural, Theorem 2.1 expands
the embedding to a plane embedding of (J).  If all neighbours of (q_i)
lie on one face, insert (q_i) in that face.  Deleting the other two
members of (T) leaves a planar graph, proving the first assertion of
outcome 4.  The second assertion is exactly the cofacial common-neighbour
palette-recycling theorem in
`../archive/hadwiger_planar_triangle_palette_recycling.md`.  \(\square\)

Outcome 2 is deliberately not called an ordinary seven-cut: a contracted
carrier in the quotient separator may lift to arbitrarily many vertices.
The first contraction edge has the sharper alternative that its lift is an
exact seven-cut, but later accumulated contractions require a state
invariant.

## 5. How contraction-criticality enters at a cross

Let (xy) be the tree edge returned by Theorem 3.1.  In a hypothetical
seven-critical graph, every six-colouring of (G-xy) gives (x,y) the
same colour, and for each of the other five colours there is an
(x)-(y) bichromatic path.  Thus the alternating port cross comes with
five edge-critical detours which are absent in (K_2\vee I).

This is useful but not yet a split.  A detour may pass through the other
reserved branch sets, and paths of different secondary colours may meet at
vertices of the common colour.  The exact missing lemma is therefore:

> **Rotation-repair Kempe lemma.**  For the edge (xy) of a minimal
> locked bag whose two sides support alternating prescribed portal classes,
> either one edge-critical detour can replace (xy) while keeping the four
> reserved portal classes on the correct sides, or the five detours expose
> a two-carrier adhesion whose lifted boundary is colour-gluable.

Without the word *edge-critical*, this is false by the icosahedral join.
Without the avoidance requirement, it is merely the elementary Kempe-path
lemma and does not repair the model.

## 6. Corrected near-(K_7) target

The rigorous near-clique route now has the following form.

\[
\boxed{
\begin{array}{c}
\text{rooted }K_4\Rightarrow K_7,\\
\text{rural port societies}\Rightarrow\text{planar expansion}
  \Rightarrow\text{two-apex or six-colourable},\\
\text{non-rural locked tree}\Rightarrow\text{an explicit alternating
port cross},\\
\text{failed quotient connectivity}\Rightarrow\text{a two-carrier
adhesion}.
\end{array}}
\]

Thus the broad connectivity-only statement has two defects: it cannot
prescribe the apex pair, and it cannot expand a planar quotient without
checking portal rotations.  The corrected contraction-critical target is
to convert the explicit alternating cross into a label-preserving split or
a colour-gluable adhesion.  This is strictly narrower than asking for an
arbitrary port-labelled splitter theorem and is falsified by a concrete
architecture as soon as edge-criticality is removed.
