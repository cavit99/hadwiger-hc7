# Independent audit: two-rail bridge overlap

Audited file: `results/hc7_exact7_two_rail_bridge_overlap.md`.

## Verdict

* **Theorem 2.1 — GREEN.**  The displayed reversed-rung construction is
  a literal `xy|qp` linkage, and the cited linkage equivalence and
  generalized pair-carrier peel preserve the labels exactly.
* **Corollary 2.2 — YELLOW as worded; GREEN after one explicit
  qualification.**  Add that the four selected attachments are distinct
  and that “reversed order” means the strict orders in (2.1).  The proof
  itself already invokes this condition.  Without it, two distinct
  `C`-bridges may share `x` or `y`, so their selected paths need not be
  vertex-disjoint.
* **Theorem 3.1 — GREEN.**  Humeau--Pous is used with its exact
  same-vertex web-completion conclusion.  Four-connectivity eliminates
  every nonempty inserted clique cell, and Whitney uniqueness then
  synchronizes all the pairwise outer frames into one facial society.
* **Lemma 4.1 and Corollary 4.2 — GREEN.**  The complement of the selected
  lobe is connected, both marked sides survive, and the trace and target
  labels are preserved.

There are two prose overstatements which should not be promoted with the
theorems.  Lines 105--109 do not establish a monotone order for *all*
bridge incidences: one `C`-bridge can contain many mutually intersecting
cross-rail paths.  Likewise the last row of the box in Section 5 controls
only those three-cut components which avoid `x,y` and meet `Q`; it does
not declare every lobe of every three-cut label-pure.  The exact repaired
statements are recorded below.

## 1. Reversed-rung linkage

The strict orders are

\[
 x,u_1,q,u_2,y\quad\hbox{on }R_Q,
 \qquad x,v_2,p,v_1,y\quad\hbox{on }R_P.
\]

Consequently the two rail portions of

\[
 X_{xy}=xR_Pv_2\,D_2\,u_2R_Qy
\]

are disjoint from the two rail portions of

\[
 X_{qp}=qR_Qu_1\,D_1\,v_1R_Pp.
\]

All four rung ends are internal vertices of the two rails and are
pairwise distinct.  The interiors of `D_1,D_2` avoid the cycle, while the
rungs themselves are vertex-disjoint.  Thus the two displayed paths are
vertex-disjoint, including at their ends.

The carrier is three-connected and `x,y,q,p` are distinct.  Lemma 2.2 of
the connected-pair linkage equivalence therefore converts this
linkage into a nonseparating `x-y` path avoiding `q,p`.  The vertex `q` is
a literal portal to its named target block, and omission of
`p in P_0 subseteq P` means that this path does not contain all of `P`.
The generalized clause following Theorem 4.1 of
`results/hc7_exact7_five_attachment_carrier_peel.md` gives precisely the
claimed labelled peel.  No completion edge or unnamed colour contact is
used.

For distinct `C`-bridges, internally off-`C` paths with four distinct
attachments are vertex-disjoint because distinct bridges intersect only
on `C`.  This proves Corollary 2.2 after inserting the stated
qualification.

The stronger sentence after the corollary is not justified.  A wheel with
rim `C` gives the clean obstruction: its hub component is one `C`-bridge
and supports cross-rail paths for attachment pairs in every order, but any
two such paths through the hub intersect.  Theorem 2.1 says nothing about
that single-bridge incidence pattern.  The valid consequence is only:

> a locked carrier has no label-spanning reversed pair of **distinct**
> `C`-bridges witnessed by internally off-`C` paths with four distinct
> attachments.

It is not valid to infer one global monotone order for all attachments
without an additional bridge-splitting or stable-bridge theorem.

## 2. Four-connected multi-frame synchronization

For fixed `q in Q_0` and `p in P_1`, the four vertices
`x,q,y,p` are pairwise distinct.  A crossing of the tuple
`(x,q,y,p)` is exactly a pair of vertex-disjoint paths joining `x-y` and
`q-p`.  Hence the hypothesis makes this tuple crossless.

Humeau--Pous, *On the Two Paths Theorem and the Two Disjoint Paths
Problem*, Theorem 1.5, says that the maximally crossless graphs for a
tuple are exactly the webs with that frame.  Equivalently, as the paper
states immediately after the theorem and in its definition of web
completion, every crossless graph has a completion obtained by adding
edges but no vertices to a web with that frame.  No connectivity,
independence, or induced-cycle hypothesis on the four terminals is being
silently added here.

Let `Delta` be the facial triangle supporting a nonempty inserted clique
cell and let `z` be a vertex in that cell.  Every edge of `J` is also an
edge of its web completion, while a clique-cell vertex has no neighbour
outside its cell and `Delta`.  The four frame vertices lie on the rib;
at least one of them is outside the three-vertex set `Delta`.  Thus
`Delta` separates `z` from that frame vertex already in `J`, contrary to
four-connectivity.  Since the completion is same-vertex, there can be no
nonempty clique cell containing only newly added vertices.  All vertices
of `J` therefore lie in the planar rib, so `J` is planar.

In the rib embedding, `x,q,y,p` occur in alternating order on the outer
face.  Deleting completion edges retains an embedding of `J` and only
merges faces, so these four vertices remain cofacial in that cyclic order.
Because `J` is four-connected, it is three-connected; Whitney uniqueness
identifies all these embeddings up to reflection on the sphere.

Fix the face `F` arising from `(x,q_0,y,p_0)`.  The face arising from
`(x,q_0,y,p)` contains the three distinct vertices `x,q_0,y`.  In a
three-connected plane graph, two distinct facial cycles intersect in at
most one edge, so that face must be `F`.  Hence every `p` lies on `F`.
The symmetric argument with `(x,q,y,p_0)` puts every `q` on `F`.
Alternation with the fixed vertices then puts all of `Q_0` on one open
`x-y` arc and all of `P_1` on the other.  This proves every conclusion of
Theorem 3.1.

The four-connectivity hypothesis is sharp for this proof.  Start with a
four-rib and replace one internal facial triangle by a clique containing
at least two additional vertices.  The resulting web is crossless for
its frame and is three-connected, but the inserted `K_5` cell is
nonplanar and its facial triangle is an actual three-cut.  Thus the
claimed three-cut alternative, rather than unconditional rurality, is
the correct three-connected residue.

## 3. Mixed three-cut lobe

Let `S` be a three-cut and `D` a component of `K-S`.  Since `K` is
three-connected, `N_K(D)=S`: a proper subset would be a cut of order at
most two, and another component of `K-S` supplies a nonempty far side.
The same applies to every component of `K-S`.

Choose one component `D'` other than `D`.  The graph induced by
`D' union S` is connected because `D'` has a neighbour at every vertex of
`S`.  Every remaining component of `K-S` also attaches to `S`.
Consequently `K-D` is connected even when `S` itself has missing edges.
This covers, in particular, a 3-sum in which some or all edges of the
common triangle were deleted.

Now `X=V(D)` and `Y=V(K)-V(D)` are a partition into connected induced
sets.  The whole trace `{x,y}` lies in `Y`; `q in X` has its stipulated
literal edge to the named target block; and the hypothesis that both
sides contain a member of `P_0` ensures that both sides meet the original
marked set `P`.  No vertex of `X` is an adhesion label because the
carrier's exact trace is `{x,y}`.  Hence this is exactly the labelled
peel definition, with both marked contacts and every label preserved.

A wheel or a triangle 3-sum does not refute the lemma.  A wheel lobe cut
off by the hub and two rim vertices has connected complement; if it mixes
a portal with a proper nonempty part of `P_0`, it is itself the peel.
Similarly, a 3-sum lobe is a peel whenever the labels are mixed.  These
examples survive only when each relevant lobe is label-pure, exactly as
Corollary 4.2 states.

The final structural box should therefore replace its third row by the
precise assertion:

> in a three-connected nonrural residue, some three-cut exists, and every
> component of that cut which avoids `x,y` and contains a member of `Q`
> is either disjoint from `P_0` or contains all of `P_0`.

## Trust boundary

This note proves a useful infinite-family exchange: a genuinely disjoint
label-spanning reversed pair peels, four-connectivity synchronizes every
crossless pair into one rural society, and a mixed labelled lobe behind a
three-cut peels.  It does **not** synchronize arbitrary incidences inside
one `C`-bridge, split a wheel hub into disjoint rungs, or classify lobes
which contain a trace root or no movable portal.  Those distinctions are
essential before the result is used as a complete bridge-overlap
dichotomy.
