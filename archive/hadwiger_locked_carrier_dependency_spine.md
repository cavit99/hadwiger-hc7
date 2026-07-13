# A label-free dependency spine for a locked rooted carrier

## 1. Abstract portal system

Let \(T\) be a connected graph with a distinguished prescribed terminal
\(t\).  Let

\[
 R,\ F,\ Q_1,\ldots,Q_q\subseteq V(T)
\]

be nonempty portal sets.  Here \(R\) consists of vertices hit from the
root-side region, \(F\) is the portal class of the free carrier to be
absorbed by a detachable arm, and the \(Q_j\)'s are the helper classes
which the residue containing \(t\) must retain.

A **detachable rooted carrier** is a partition

\[
 T=A\mathbin{\dot\cup}B
\]

into nonempty connected adjacent sets such that

\[
 A\cap R\ne\varnothing,\quad A\cap F\ne\varnothing,\quad
 t\in B,\quad B\cap Q_j\ne\varnothing\quad(j\in[q]).
\tag{1.1}
\]

This definition contains no Moser labels and no reference to the order of
the portal classes.  For the clean \(K_{2,4}\) gate, \(q=4\): the residue
must retain the other free carrier and the three other terminal carriers.
The bypass theorems in hadwiger_clean_gate_minimal_bypass.md show that
(1.1) opens the contact lock.

## 2. The dependency-spine theorem

Choose any spanning tree \(\mathcal T\) of \(T\), rooted at \(t\).
For an edge \(e\) of \(\mathcal T\), let \(D_e\) be the component of
\(\mathcal T-e\) not containing \(t\).  Call \(e\) **mixed** when

\[
 D_e\cap R\ne\varnothing,\qquad D_e\cap F\ne\varnothing .
\tag{2.1}
\]

For each \(j\), let \(b_j\) be the lowest common ancestor in
\(\mathcal T\) of all vertices in \(Q_j\).  If \(Q_j\) is a singleton,
\(b_j\) is that vertex.

### Theorem 2.1 (bounded dependency spine)

If \(T\) has no detachable rooted carrier, then every mixed edge belongs
to

\[
 \Sigma=\bigcup_{j=1}^q t\mathcal T b_j .          \tag{2.2}
\]

More precisely, for every mixed edge \(e\) there is a helper class
\(Q_j\) with

\[
                 Q_j\subseteq D_e .               \tag{2.3}
\]

Consequently, after suppressing unmarked degree-two vertices, the subtree
\(\Sigma\) has at most \(q\) leaves and at most \(q-1\) branch vertices.
Every component of \(\mathcal T-V(\Sigma)\) contains portals of at most
one of the two types \(R,F\).

#### Proof

The two components \(D_e\) and \(V(T)-D_e\) are connected in
\(\mathcal T\), hence in \(T\), and are adjacent through \(e\).  The
second contains \(t\).  If it met every \(Q_j\), then (2.1) would make
this edge partition a detachable rooted carrier.  Therefore it misses
some \(Q_j\), which is exactly (2.3).

For a rooted tree, \(Q_j\subseteq D_e\) holds precisely when \(e\) lies
on the root-to-\(b_j\) path: all vertices of \(Q_j\) lie below \(e\) if
and only if their lowest common ancestor lies below \(e\).  This proves
(2.2).

The union of \(q\) paths with a common initial vertex is a tree with at
most \(q\) leaves and at most \(q-1\) vertices of degree at least three.
Finally, if a component off \(\Sigma\) contained both an \(R\)-portal and
an \(F\)-portal, the first edge of that component away from \(\Sigma\)
would be mixed but would not belong to \(\Sigma\), a contradiction.
\(\square\)

### Corollary 2.2 (the \(2\)-by-\(4\) lock has four stems)

For a clean \(K_{2,4}\) gate, every terminal carrier which resists the
bypass towards a specified free carrier has all of its root/free mixed
tree edges on the union of four dependency stems.  This remains true for
every spanning tree of the carrier.

Thus the infinite part of the simultaneous lock is not arbitrary portal
geometry.  Long chains can occur only as subdivisions of a tree with at
most four leaves and three branch vertices.  The icosahedral sharpness
example is the one-stem extreme.

### Corollary 2.3 (zero-spine outcome is only a tree separation)

If there is no mixed edge and neither \(R\) nor \(F\) contains \(t\),
then no component of \(\mathcal T-t\) meets both \(R\) and \(F\).
This is a statement about the chosen spanning tree only; it does not
imply that \(t\) separates the two portal types in the original carrier
\(T\).

#### Proof

If a component of \(\mathcal T-t\) met both types, its first edge at
\(t\) would be mixed. \(\square\)

The distinction is essential.  Non-tree edges may join different
components of \(\mathcal T-t\).  For a counterexample with disjoint
portal sets, let

\[
 V(T)=\{t,r,f,q\},\qquad
 E(T)=\{tr,tf,rf,rq,fq\},
\]

take \(R=\{r\}\), \(F=\{f\}\), \(Q_1=\{q\}\), and choose the spanning
tree \(tr,tf,rq\).  There is no detachable rooted carrier.  Its arm
would have to contain \(r,f\); if it omits \(q\), the residue
\(\{t,q\}\) is disconnected, while if it contains \(q\), the residue
misses \(Q_1\).  No tree edge is mixed, yet \(T-t\) contains the edge
\(rf\).  Thus even in a locked portal system, spine order zero is not an
ordinary one-vertex gate.  Positive spine order still confines all
*tree* root/free mixing to at most \(q\) ordered stems, but conversion
to a graph separator requires control of non-tree bridges.

### Corollary 2.4 (simultaneous two-free-carrier lock)

Apply Theorem 2.1 in both directions, once with free class \(F_1\) and
required classes \(F_2,Q_1,\ldots,Q_{q-1}\), and once with \(F_2\) and
required classes \(F_1,Q_1,\ldots,Q_{q-1}\).  If neither detachable arm
exists, every edge whose far subtree meets \(R\) and either free class
lies in the union of the root-to-LCA paths for the \(q+1\) helper
classes

\[
             F_1,F_2,Q_1,\ldots,Q_{q-1}.
\]

For the clean \(K_{2,4}\) lock this is a common five-stem spine (the two
free carriers and three other terminal carriers), rather than two
unrelated four-stem systems.

## 3. Contraction and lifting

The dependency spine is compatible with label-preserving contractions.

### Lemma 3.1 (a detachable split lifts through an unmarked edge)

Let \(uv\) be an edge of \(T\) such that no prescribed label is lost by
identifying \(u,v\): in particular \(t\) is retained and the portal
membership of the new vertex is the union of the memberships of
\(u,v\).  If \(T/uv\) has a detachable rooted carrier, then \(T\) has
one.

#### Proof

Let \(w\) be the contracted vertex.  Expand \(w\) by putting both
\(u,v\) into whichever side contains \(w\).  That side stays connected
because \(uv\) is an edge; the other side is unchanged.  All portal
incidences are retained under union of labels, and adjacency of the two
sides is retained. \(\square\)

Therefore every label-respecting contraction of a locked carrier remains
locked.  In a contraction-critical host it nevertheless produces a
proper minor with a six-colouring.  Hence each such contraction carries a
strict one-step colouring state somewhere outside the purely combinatorial
portal system.  This is the precise point at which minor-criticality must
shorten or identify a long dependency stem; the portal geometry itself
has already been reduced to at most four stems.

## 4. Kempe detours on a dependency edge

Let \(xy\) be an unmarked edge on a dependency stem, and suppose the
component \(D_{xy}\) away from \(t\) traps \(Q_j\) as in (2.3).  In a
six-colouring of \(G-xy\), put

\[
 c(x)=c(y)=\alpha .
\]

For every other colour \(\gamma\), edge-criticality supplies an
\(\alpha/\gamma\) \(x\)-\(y\) detour.

### Lemma 4.1 (helper-first detour opens the stem)

Suppose the far side \(D_{xy}\) is used as the prospective arm and the
only helper class missing from the root-side residue is \(Q_j\).  If one
of the five detours, read from the residue endpoint, reaches the carrier
represented by \(Q_j\) before meeting any other reserved branch set or
fixed capture path, then the contact lock opens.

#### Proof

The prefix to its first \(Q_j\)-vertex is a clean path from the residue
to that helper carrier.  Absorb its internal vertices into the residue.
This restores the sole missing helper adjacency while remaining disjoint
from every reserved branch.  The edge partition now satisfies (1.1),
and the terminal-arm bypass theorem constructs the improved model.
\(\square\)

The one-helper statement has a stronger simultaneous form.  Different
Kempe prefixes are allowed to meet, and even to use the same second
colour, because all of them will be absorbed into the same residue branch.

### Theorem 4.2 (Kempe colour-reuse repair)

Let \(T=A\dot\cup B\) be a prospective detachable partition with
\(t\in B\), \(A\cap R\ne\varnothing\), and
\(A\cap F\ne\varnothing\).  Let

\[
 \mathcal M=\{Q_j:B\cap Q_j=\varnothing\}
\]

be the helper classes missing from the residue.  Fix the two root-side
capture paths, the far-side carrier path, and the final connector used by
the terminal-arm bypass theorem.

Choose an interface edge \(xy\), with \(x\in A,y\in B\), and a
six-colouring of \(G-xy\), where \(c(x)=c(y)=\alpha\).  Form a bipartite
graph \(\mathcal H\) with left side \(\mathcal M\) and right side the five
colours \(\gamma\ne\alpha\).  Join \(Q_j\) to \(\gamma\) when some
\(\alpha/\gamma\) \(y\)-to-\(x\) detour has an initial
\(B\)-to-\(Q_j\)-carrier subpath whose interior:

* avoids \(A\), every reserved helper branch, and the apex \(v\);
* avoids all four fixed capture/connector paths; and
* meets its endpoint helper carrier for the first time at its last
  vertex.

If every vertex of \(\mathcal M\) has a neighbour in \(\mathcal H\),
then the contact lock opens.  No matching condition is needed.

#### Proof

For every \(Q_j\in\mathcal M\), choose any neighbouring colour
\(\gamma_j\), a witnessing prefix, and stop it at first entry into the
helper carrier.  The same colour may be chosen for several helpers:
choose the witnessing paths independently.  Absorb the union of all
prefix interiors into \(B\).

This union is connected to \(B\), because every prefix starts in \(B\).
Intersections between two prefixes, including prefixes using the same
two-colour component, cause no conflict: all are assigned to the same
enlarged branch.  Their interiors avoid every other branch set, the apex,
and the already fixed bypass paths.  The enlarged residue gains an
adjacency to every member of \(\mathcal M\); all nonmissing helper
adjacencies were already present.
Thus the enlarged residue satisfies (1.1), and the bypass theorem applies.
\(\square\)

### Corollary 4.3 (zero-access helper and defect star)

For a missing helper \(Q\), form its **usable repair graph** by retaining
\(B\), the external \(Q\)-carrier, and every unassigned vertex, while
deleting:

* the prospective arm \(A\);
* the apex \(v\);
* every other reserved branch set; and
* the four fixed capture/connector paths, apart from vertices already in
  \(B\) or in the target \(Q\)-carrier.

When the target carrier itself is one of the fixed prospective rooted
carriers, retaining it takes priority over the deletion list; paths are
stopped on first entry into it.

Call \(Q\) path-accessible if this graph contains a path from \(B\) to
the \(Q\)-carrier.  Let

\[
 \mathcal Z=\{Q\in\mathcal M:Q\text{ is not path-accessible}\}.
\tag{4.1}
\]

If the contact lock survives, then \(\mathcal Z\ne\varnothing\).
Moreover all helpers in \(\mathcal M-\mathcal Z\) can be repaired
simultaneously, leaving six connected rooted carriers whose only possible
missing clique edges join the residue to members of \(\mathcal Z\).

#### Proof

For every path-accessible helper choose a usable path, stop at first
entry into its helper carrier, and absorb all path interiors into \(B\).
The union is connected to \(B\).  Different paths may intersect, because
they are assigned to the same enlarged branch, and by construction none
meets another reserved branch, the arm, the apex, or a fixed capture
path.  If \(\mathcal Z\) were empty, the bypass theorem would open the
lock.  Otherwise replaying the construction leaves only the displayed
residue--helper nonedges. \(\square\)

In the \(HC_7\) application all four terminal residues keep their old
roots and the two new carriers contain the two captured roots.  Adjoining
the singleton apex \(v\) therefore gives

\[
             K_7-K_{1,|\mathcal Z|}
\]

as a minor, with the defect star centred at the residue branch.  In
particular, \(|\mathcal Z|=1\) gives a \(K_7^-\)-minor with a prescribed
non-apex deficient pair.

Thus the simultaneous multi-charge lock reduces rigorously to one or more
**zero-access helpers**.  For each such helper, none of the five
bichromatic edge detours has a clean residue-to-helper prefix (otherwise
the helper would be path-accessible).  Detours
for two different second colours can meet only at vertices of colour
\(\alpha\); their failure is now an avoidance/gate statement for one
fixed helper, not a compatibility problem among four helpers.

### Corollary 4.4 (zero access gives a genuine portal adhesion)

Fix \(Q\in\mathcal Z\), and let \(U\) be the component of its usable
repair graph containing \(B\).  Put

\[
                         P=N_G(U).                 \tag{4.2}
\]

Then \(P\) is contained entirely in the deleted reserved objects and is a
genuine separator in \(G\), separating \(U\) from the nonempty external
\(Q\)-carrier.  In a seven-connected graph,

\[
                         |P|\ge7.                  \tag{4.3}
\]

If equality holds, \(P\) is an exact seven-adhesion.  In a
six-minor-critical graph it is state-active: every proper operation
strictly inside \(U\), leaving all vertices of \(P\) distinct, creates a
boundary equality state compatible with
the unchanged opposite side and not extendible over the original
\(U\)-side.  If (4.3) is strict, all surplus attachment vertices lie in
the finite family of reserved carrier/path objects.

#### Proof

By the definition of a component, every neighbour of \(U\) outside \(U\)
was deleted when the usable graph was formed; hence \(P\) lies in the
listed objects.  The \(Q\)-carrier is retained but lies in another
component, so deleting \(P\) separates two nonempty sets.  This proves
(4.3).

For the state assertion, perform any proper operation on the \(U\)-side
and colour the resulting proper minor.  Its state on \(P\) extends over
the modified side and the unchanged complement.  If it extended over
the original \(U\)-side, the two colourings could be permuted blockwise
and glued to colour \(G\), a contradiction. \(\square\)

### Corollary 4.4A (capacity routes every exact zero-helper adhesion)

Suppose equality holds in (4.3), and let \(m\) be the number of
components of \(G-P\).  Every component is full to \(P\).  For an
optimal colouring of \(G[P]\), let \(b\) be the number of non-singleton
colour blocks.  The shore-capacity theorem gives

\[
                         m\le b\le3.               \tag{4.4}
\]

Consequently \(m\le3\).  If \(m=3\), then \(b=3\), and the only possible
block-size patterns on seven vertices are

\[
                         (3,2,2),\qquad(2,2,2,1).
\]

The first is eliminated by
hadwiger_three_shore_block_capacity.md, Theorem 5.1; the audited
seven-vertex support classification then makes the second boundary the
pure Moser spindle.  If \(m=2\), the exact adhesion lies in the
two-full-shore cyclic-hull/bad-split theory.

#### Proof

Fullness follows from minimality of the seven-cut: if a cut vertex missed
one component, the other six vertices would still separate it.  Apply
Corollary 2.2 of hadwiger_shore_capacity_hall.md to obtain \(b\ge m\).
Since each of the \(b\) blocks contains at least two of the seven boundary
vertices, \(b\le3\).

When \(m=3\), equality forces exactly three non-singleton blocks.  With
three colour blocks their sizes are \(3,2,2\); with four colour blocks
they are \(2,2,2,1\).  Five or more blocks would require at least eight
vertices.  The cited closure and classification give the last claims.
\(\square\)

Thus an exact adhesion produced by a zero-access helper is no longer an
unclassified recursion point.  It is either the already normalized
two-shore bad-split state or the single pure-Moser three-shore state.

### Corollary 4.5 (defect size controls spine width)

Absorb the clean prefixes for every helper in
\(\mathcal M-\mathcal Z\) into the residue, as in Corollary 4.3, and
contract that connected protected residue to one terminal.  Choose a
spanning tree of the resulting quotient carrier.  The only helper classes
still required on the protected residue side are the members of
\(\mathcal Z\).  If no detachable rooted carrier containing the protected
residue results, Theorem 2.1 applied in the quotient with these classes
shows that all root/free mixed edges lie on at most
\(|\mathcal Z|\) dependency stems.  Every resulting split lifts by
expanding the protected residue.

Hence the prescribed \(K_7^-\) outcome \(|\mathcal Z|=1\) has a
**one-stem tree lock**: every mixed edge of the selected spanning tree
lies on the single root-to-LCA path of the unique zero-access helper.
At spine order zero, Corollary 2.3 separates the portal types only in
that tree.  Non-tree bridges may still join its branches, so neither a
one-vertex graph gate nor a linear ordering of every root-to-free path
has been proved.  More generally the defect-star size bounds the width
of the mixed part of a chosen spanning tree, not the topological width
of the full residual carrier.

### Theorem 4.6 (one zero-access helper is a protected Two Paths problem)

Let \(K\) be the unique member of \(\mathcal Z\).  After the clean
repairs, let \(B_0\) be the connected protected residue containing
\(t\) and all already repaired helper contacts.  Contract \(B_0\) to a
single terminal \(\beta\), and let \(Q\) be the set of remaining
vertices adjacent to the external helper carrier \(K\).
Put \(R'=R-V(B_0)\) and \(F'=F-V(B_0)\); these sets are nonempty for
the prospective arm under consideration.

There is a detachable rooted carrier whose residue contains all of
\(B_0\) if and only if the quotient carrier contains two
vertex-disjoint paths

\[
       P_{RF}:R'\longrightarrow F',\qquad
       P_{\beta Q}:\beta\longrightarrow Q,        \tag{4.4}
\]

where a path is allowed to be trivial when its two portal requirements
occur at one vertex.  Apart from that harmless degeneracy, the four ends
are distinct; the path endpoints select the actual portal vertices.

#### Proof

A detachable partition \(A\dot\cup B\) with \(B_0\subseteq B\) contains
an \(R'\)-to-\(F'\) path in \(A\) and, after contracting \(B_0\), a
\(\beta\)-to-\(Q\) path in \(B\), proving necessity.

Conversely, suppose the two paths in (4.4) exist.  If their vertex sets
are not adjacent, take a shortest connector between them.  Its interior
misses both paths; split the connector at any edge and absorb its two
halves into the respective paths.  This gives disjoint connected adjacent
sets \(A_1,B_1\), with \(A_1\) meeting \(R',F'\) and \(B_1\) containing
\(\beta\) and meeting \(Q\).

Contract \(A_1,B_1\) to adjacent vertices and choose a spanning tree
containing their edge.  Deleting that tree edge partitions all remaining
vertices between two connected sides.  Expanding the contractions gives
a partition of the quotient carrier satisfying (1.1), with the sole
required helper \(K\).  Finally expand \(\beta\) back to the connected
set \(B_0\).  It remains wholly on the residue side, so every previously
repaired helper contact is retained. \(\square\)

Therefore the nondegenerate \(|\mathcal Z|=1\) residue lies exactly in
the scope of the Two Paths Theorem.  For fixed choices
\(r\in R',f\in F',q\in Q\) with \(r,f,\beta,q\) distinct, its failure yields
the standard low-order separation or web obstruction with the four
terminals in alternating boundary order.  If the \(R\)- and \(F\)-roles
coincide, the problem reduces to a \(\beta\)-to-\(Q\) path avoiding that
fixed vertex.  If a \(Q\)-role is forced to coincide with an arm role,
that common portal is itself the unsplittable gate.  Thus the degenerate
cases are one-path avoidance or a common-portal obstruction, not an
unmentioned four-terminal linkage.  The remaining HC7 task is no longer
to invent a simultaneous six-bag split: it is to lift that
web/separation through the three repaired terminal carriers and the apex,
using the exact minor-transition boundary state.

### Lemma 4.7 (usable bridges of a maximal web have clique attachment)

Fix distinct terminals \(r,f,\beta,q\).  Let \(W\) be edge-maximal on
its vertex set subject to having no disjoint \(r\)-\(f\) and
\(\beta\)-\(q\) paths.  Let \(X\) be a connected graph disjoint from
\(W\), regarded as usable material which may be absorbed into either
path.  If \(W\cup X\) still has no prescribed two-linkage, then

\[
                    N_W(X)\ \text{is a clique in }W. \tag{4.5}
\]

#### Proof

Suppose two attachments \(u,w\in N_W(X)\) are nonadjacent in \(W\).
By edge-maximality, \(W+uw\) has the prescribed two-linkage.  That
linkage must use the added edge, or it would already exist in \(W\).
Replace \(uw\) by a \(u\)-to-\(w\) path whose interior lies in \(X\).
The other linkage path lies in \(W\) and is vertex-disjoint from
\(u,w\), so the replacement preserves disjointness.  This gives the
forbidden linkage in \(W\cup X\). \(\square\)

To apply the lemma to the reduced planar-web outcome of the Two Paths
Theorem, one must additionally know that the edge-maximal web \(W\) is
realized in the host, or that every artificial completion edge used by
the resulting linkage has a disjoint replacement in the original graph.
Under that **completion-edge realization hypothesis**, (4.5) has order
at most four in the quotient, and normally is a facial triangle.  If the
clique avoids the contracted protected terminal \(\beta\), this is an
actual small attachment.  If it contains \(\beta\), expansion may replace
that one quotient vertex by the whole protected residue; this is a
reserved-carrier attachment, not an order-four cut in \(G\).

Without completion-edge realization, an abstract maximal web may use
added edges elsewhere in the two-linkage, and Lemma 4.7 does not imply a
clique attachment in the original host.

### Corollary 4.7A (a protected web bridge has portal multiplicity)

Under the completion-edge realization hypothesis, suppose a nonempty
bridge interior \(X\) has quotient attachment clique
\(\{\beta\}\cup Z\), where \(Z\) consists of \(s\le3\) actual vertices,
and let

\[
                 P_\beta=N_G(X)\cap B_0
\]

be the actual attachment set in the protected residue represented by
\(\beta\).  If \(X\) has no other neighbour, then seven-connectivity
gives

\[
                         |P_\beta|\ge7-s\ge4.      \tag{4.6}
\]

#### Proof

The actual set \(P_\beta\cup Z\) separates \(X\) from the nonempty far
side of the clean model.  Its two parts are disjoint.  Apply
seven-connectivity. \(\square\)

Thus the only way a quotient facial attachment evades the small-cut
contradiction is by producing at least four distinct actual portals in
one protected carrier.  This is exactly the multiplicity input required
for another detachable-arm/dependency-spine pass; the quotient
contraction does not erase the cost.

### Corollary 4.8 (capacity interpretation)

At an exact adhesion, suppose the \(R,F\) portal roles are the two traces
of one non-singleton equality block and the protected-residue,
zero-helper roles are the traces of a second block (with every vertex of
each block adjacent to its displayed carrier).  Then the two paths in
Theorem 4.6 are exactly a two-packet in the sense of the shore-capacity
family of hadwiger_shore_capacity_hall.md.  Under this explicit trace
hypothesis:

1. the linkage outcome adds one shore-capacity unit and is consumed by
   the shore-capacity gluing theorem whenever the other shores meet its
   packet-cover hypothesis;
2. the failure outcome is an edge-maximal web; for every usable exterior
   component whose completion edges are realized, Lemma 4.7 gives a
   clique attachment of order at most four; and
3. the unresolved bridges are reserved helper carriers and bridges whose
   linkage certificate uses unrealized completion edges.

This is the promised label-free route from a zero-access helper to
“capacity increase or small adhesion”.  The unresolved lift is now
sharply localized: identify the two portal pairs with the same equality
blocks on the opposite shore, or peel a reserved helper while preserving
its old contact.  Without that trace identification, Theorem 4.6 is a
rooted two-carrier packet but not yet an \(\mathcal R_i\)-packet, and the
shore-capacity theorem must not be invoked.

This is a structural input, not a closure claim.  Turning the fivefold
avoidance certificate for one zero-access helper into a state-gluable
adhesion is the exact remaining step.

## 5. What has and has not been achieved

The theorem replaces the label-specific simultaneous lock by a uniform
invariant:

\[
\boxed{\text{detachable rooted carrier}\quad\text{or}\quad
       \text{a bounded helper-dependency spine}.}
\]

For \(HC_7\) each chosen free direction has four dependency stems, and
the simultaneous two-direction lock has one common five-stem spine.
Along every unmarked edge, contraction-criticality supplies five coloured
detours; colour reuse repairs every helper with at least one clean prefix.
Non-tree bridges between the stems remain unrestricted.  A zero-access
helper now yields the genuine portal adhesion \(P=N(U)\).  If
\(|P|=7\), shore capacity normalizes it to a two-shore bad split or the
pure-Moser three-shore state.  The remaining alternatives are:

* strict reserved-portal surplus \(|P|\ge8\);
* equality-block trace identification across the normalized exact
  adhesion; or
* the reserved-helper peel in the one-stem web.

The triangle example following Corollary 2.3 forbids inferring a graph
gate from the tree spine alone, and the icosahedral example shows why the
final ambient peel cannot use portal geometry and seven-connectivity
alone.
