# A tree-society split-versus-two-apex theorem for a near-\(K_7\) model

## 1. Scope

This note treats a genuinely infinite near-clique cell.  It does not assume
that a planar contracted quotient automatically expands to a planar graph.
All portal occurrences and their rotations are retained.

Let \(G\) be seven-connected and suppose that it has a spanning
\(K_7^-\)-model

\[
 \{a\},\{c\},\{q_1\},\{q_2\},\{q_3\},D,E,             \tag{1.1}
\]

where \(ac\) is the only non-required pair.  When \(G\) is
\(K_7\)-minor-free, \(a\) and \(c\) are in fact nonadjacent.  Assume in
this note that \(G[D]\) and \(G[E]\) are trees.  No bound is put on their
orders or on the number of edges between them.

Delete two of the neutral singleton vertices, say \(q_1,q_2\), and put

\[
                         H=G-\{q_1,q_2\}.              \tag{1.2}
\]

Contracting the five remaining model bags gives the planar graph
\(K_5^-\).  Retaining every interbag edge gives a multigraph whose
underlying simple graph is \(K_5^-\).  A **compatible quotient rotation**
means a plane rotation of this multigraph in which the orders at the two
ends of every parallel bundle are mutually compatible.  At a tree bag,
the incident edge occurrences, with repetitions, form its expansion
society.  Such a quotient rotation always exists: start with a plane
embedding of \(K_5^-\) and draw each parallel bundle in a narrow strip
about its representative edge.

## 2. The exact planar alternative

### Lemma 2.1 (compatible rural expansion)

If the two tree societies \(D,E\) are rural in one compatible quotient
rotation, then \(H\) is planar.  Consequently \(G\) is two-apex.

#### Proof

Take a plane drawing of the quotient multigraph and small pairwise
disjoint disks about its five vertices.  Delete the interiors of the two
disks corresponding to \(D,E\), and insert in them the two prescribed
rural drawings, matching every portal occurrence in its prescribed
rotation.  The compatibility condition makes the two ends of every
interbag edge match.  The singleton societies require no expansion.
This gives a plane drawing of every edge of \(H\), not merely of one
representative edge for each model adjacency.  Hence deleting
\(q_1,q_2\) makes \(G\) planar. \(\square\)

The qualification about all interbag edges is essential.  Planarity of
the simple contracted \(K_5^-\) alone does not imply planarity of \(H\).

### Lemma 2.2 (tree interval certificate)

Fix a compatible quotient rotation.  If the society of \(D\) is not
rural, there is an edge \(xy\in E(D)\) such that the two components
\(P,R\) of \(D-xy\) carry alternating portal occurrences.  Equivalently,
the occurrences on one side of \(xy\) are not a cyclic interval in the
quotient rotation.  The same assertion holds for \(E\).

#### Proof

Add one auxiliary leaf at the endpoint in the tree of every portal
occurrence.  A tree admits a disk embedding with a prescribed cyclic
order of its attachment leaves if and only if the leaves on either side
of every tree edge form a cyclic interval.  Necessity follows from the
outer-face walk.  Sufficiency follows inductively by cutting a tree edge
and embedding its two interval subtrees in adjacent subdisks.  Failure of
the interval condition supplies two occurrences on either side in
alternating order. \(\square\)

Thus an all-tree model has an exact, label-preserving alternative: a
two-apex expansion, or a named tree edge carrying an alternating port
cross.  If the two societies prefer incompatible orders for a parallel
\(DE\)-bundle, then every compatible quotient rotation makes at least
one of them nonrural and hence returns such an edge.  The next lemma
identifies when the cut is already a split, rather than merely a rotation
obstruction.

## 3. A balanced cross is a \(K_7\)-certificate

### Lemma 3.1 (balanced common-deficient peel)

Let \(D=P\mathbin{\dot\cup}R\), where \(P,R\) are nonempty connected
sets with an edge between them.  If

\[
 P\sim a,c,
 \qquad
 R\sim c,q_1,q_2,q_3,E,                              \tag{3.1}
\]

then \(G\) has a \(K_7\)-minor.  The same holds with \(a,c\)
interchanged, or with \(P,R\) interchanged.

#### Proof

Use the seven bags

\[
 \{a\}\cup P,\quad \{c\},\quad
 \{q_1\},\{q_2\},\{q_3\},\quad R,\quad E.          \tag{3.2}
\]

The first bag is connected and becomes adjacent to \(c\) through the
\(Pc\)-edge, repairing the unique deficient pair.  It meets \(R\)
through the cut edge and meets \(E\) through the old \(aE\)-edge.
The set \(R\) retains all adjacencies in (3.1), and all remaining pairs
are old model adjacencies.  Hence (3.2) is a \(K_7\)-model. \(\square\)

In the plane \(K_5^-\) rotation at \(D\), the classes \(a,c\) are
opposite and the two other classes \(q_3,E\) are opposite.  Therefore a
class-level alternating cross naturally produces a side meeting both
deficient roots.  Lemma 3.1 says precisely which reserve contacts must
remain on the other side; it does not silently assume them.

## 4. Every failed balanced cut has amplified opposite-bag capacity

For a connected side \(P\) of a tree edge of \(D\), let

\[
 m(P)=|\{s\in\{a,c,q_1,q_2,q_3\}:P\not\sim s\}|.     \tag{4.1}
\]

### Lemma 4.1 (defect amplification)

Every such side satisfies

\[
                         |N_E(P)|\ge m(P)+1.          \tag{4.2}
\]

The analogous inequality holds with \(D,E\) interchanged.

#### Proof

Let \(xy\) be the tree edge, with \(x\in P\), and let \(R\) be its
other side.  Since the model is spanning, every neighbour of \(P\)
lies among the one vertex \(y\), the five singleton vertices which see
\(P\), and \(E\).  If \(m(P)\ge1\), a missed singleton lies beyond
this neighbourhood, so seven-connectivity gives

\[
 7\le |N_G(P)|
   \le 1+(5-m(P))+|N_E(P)|,
\]

which is (4.2).  If \(m(P)=0\), the desired conclusion is merely
\(|N_E(P)|\ge1\).  If it failed, then
\(N(P)\subseteq\{y,a,c,q_1,q_2,q_3\}\), while the nonempty bag \(E\)
lies beyond this set, contradicting seven-connectivity.  This proves the
remaining case. \(\square\)

### Theorem 4.2 (tree-society split/2-apex/owner trichotomy)

Under (1.1), at least one of the following occurs.

1. \(G\) is two-apex.
2. \(G\) has a \(K_7\)-minor by the balanced peel of Lemma 3.1.
3. For every choice of two neutral singleton apices and every compatible
   quotient rotation, some tree society has a named alternating edge cut
   which is **unbalanced**: either neither side meets both deficient roots,
   or every common-deficient orientation traps at least one reserve label
   needed in (3.1).  Every side missing \(m\) singleton labels has at
   least \(m+1\) distinct portals into the opposite tree bag.

#### Proof

Choose the deleted neutral pair and a quotient rotation.  If it is
compatible and both societies are rural, Lemma 2.1 gives outcome 1.  If
one is not rural, Lemma 2.2 returns a named alternating tree edge.  If an
orientation of its two sides satisfies (3.1), Lemma 3.1 gives outcome 2.
Otherwise the failure is exactly the trapped reserve label in outcome 3,
and Lemma 4.1 gives the asserted quantitative capacity.  Repeating for
the three choices of the retained neutral vertex and all compatible
orders of the parallel bundles proves the universal form of outcome 3.
\(\square\)

The theorem closes the entire compatible, rural all-tree family and every
balanced alternating family, for trees of arbitrary size.  The residue is
not “a complicated bag”: it is either an owner cut with a measured portal
surplus into the other bag, or a conflict in the order of the shared
\(DE\)-ports.  Both are two-shore states and can be fed directly into a
capacity-state exchange; no further enumeration of tree shapes is needed.

## 5. The degree-seven singleton endpoint: a controlled completion

The surplus theorem in
`hadwiger_singleton_triangle_exact7_transport.md` gives the following
additional data in the zero-optional singleton endpoint.  The vertices
\(d,b\) are adjacent, \(d\) has degree seven, the four common neighbours
\(a,c,1,2\) split into independent pairs, and with

\[
                         E_b=N_O(b)
\]

there is an \(E_b\)-rooted \(K_4\)-model
\(\mathcal R=(R_1,R_2,R_3,R_4)\) avoiding
\(\{d,b,a,c,1,2\}\).  In particular \(\{b\},R_1,\ldots,R_4\)
is a controlled \(K_5\)-model.

The next elementary certificate converts a genuinely distributed portal
state into the missing \(K_7\).

### Lemma 5.1 (root-distributed reserved-connector completion)

Suppose, after possibly interchanging \(1,2\), that every \(R_i\)
contains a root \(e_i\in E_b\) satisfying

\[
 e_i\sim\{a,1\}\quad\hbox{in at least one place},
 \qquad
 e_i\sim\{c,2\}\quad\hbox{in at least one place}.       \tag{5.1}
\]

If there is a \(c\)-\(2\) path \(P\) whose interior avoids

\[
 \{d,b,a,1\}\cup\bigcup_{i=1}^4R_i,                    \tag{5.2}
\]

then \(G\) has a \(K_7\)-minor.

#### Proof

Use the seven bags

\[
 R_1,R_2,R_3,R_4,\quad
 \{b\},\quad \{d,a,1\},\quad V(P).                    \tag{5.3}
\]

The first four form a clique model.  The singleton \(b\) sees them at
their roots and sees the last two bags through its edges to
\(d,a,1,c,2\).  The sixth bag is connected through the star at \(d\),
and the last bag is connected by definition.  They are adjacent through
an edge from \(d\) to \(c\) or \(2\).  Finally (5.1) makes every
\(R_i\) adjacent to each of the last two bags.  The avoidance in (5.2)
gives disjointness.  Thus (5.3) is a \(K_7\)-model. \(\square\)

There are three symmetric versions, using the other independent-pair
partition or reserving the other pair connector.  Consequently a
\(K_7\)-minor-free singleton endpoint has an exact lock: every rooted
\(K_4\) certificate whose four roots are cross-distributed as in (5.1)
meets every connector for the opposite independent pair.  This couples
the new simultaneous-star rooted core to the near-clique portal-splitting
programme; it is stronger than the statement that four unordered portals
exist.

The rooted-core theorem actually yields a clean state dichotomy.  In its
proof, let \(J\) be the four-colour graph and define

\[
 X_{a1\mid c2}=\{e\in E_b:
       N(e)\cap\{a,1\}\ne\varnothing\ne
       N(e)\cap\{c,2\}\}.                              \tag{5.4}
\]

### Theorem 5.2 (cross-state or locked rooted core)

At least one of the following holds.

1. There is a proper four-colouring of \(J\) in which some colour is
   absent from \(X_{a1\mid c2}\).
2. There is an \(X_{a1\mid c2}\)-rooted \(K_4\)-model, and every
   \(c\)-\(2\) path satisfying the boundary avoidance in (5.2) meets
   that model.
3. \(G\) contains a \(K_7\)-minor.

The same trichotomy holds for the other independent-pair partition and
with the reserved pair interchanged.

#### Proof

If outcome 1 fails, every proper four-colouring of \(J\) uses all four
colours on the fixed set \(X_{a1\mid c2}\).  The proved four-colour case
of Strong Hadwiger therefore gives an
\(X_{a1\mid c2}\)-rooted \(K_4\)-model.  If a reserved connector avoids
it, Lemma 5.1 gives outcome 3.  Otherwise the model has the locking
property in outcome 2. \(\square\)

The low state in outcome 1 is not vacuous: the larger set \(E_b\) is
four-colour-saturating by the simultaneous-star theorem.  Hence the
missing colour is still represented in \(E_b\), but only on portals
which are one-sided with respect to the ordered pair state.  This is the
same polarity (cross state versus locked connector) that occurs at the
two-shore cut.

The dark-bag theorem gives a stronger conclusion when the two completion
groups, rather than an ordered pairing of their members, are retained.
Put

\[
 X_{A\mid C}=\{e\in E_b:
 N(e)\cap A\ne\varnothing\ne N(e)\cap C\},
 \qquad A=\{a,c\},\quad C=\{1,2\}.                    \tag{5.5}
\]

### Corollary 5.3 (a forced dark colour state)

If \(G\) has no \(K_7\)-minor, there is a proper four-colouring of
\(J\) in which some colour is absent from \(X_{A\mid C}\).  The same
colour is present on \(E_b\), and every portal of that colour is
anticomplete to all of \(A\) or to all of \(C\).

#### Proof

If every four-colouring used all four colours on \(X_{A\mid C}\),
Strong HC4 would give an \(X_{A\mid C}\)-rooted \(K_4\)-model.  Every
one of its four bags would meet both completion groups \(A,C\).  The
completion partition

\[
                         A\mid(\{d\}\cup C)
\]

together with those four bags and \(\{b\}\) is then the explicit
\(K_7\)-model from the dark-bag allocation theorem.  Thus a colouring
omitting a colour on \(X_{A\mid C}\) exists.  But \(E_b\) is
four-colour-saturating in \(J\), so that colour occurs on \(E_b\).
Membership in \(E_b-X_{A\mid C}\) means exactly that one of the two
whole completion groups is missed. \(\square\)

This is a colour-state version of the dark-bag conclusion.  It aligns an
actual colour with the owner side and is therefore stronger input for an
edge-deletion or contraction transition than the static assertion that
some branch bag is dark.

## 6. A multiply-hit rooted tree peels to a four-label core

Retain the spanning rooted \(K_4\)-model
\(K_0,K_1,K_2,K_3\) from
`hadwiger_rooted_core_dark_bag_split.md`.  Suppose \(K_0\) contains
neither \(h\) nor \(r\), is anticomplete to \(A=\{a,c\}\), and a
different bag \(T=K_j\) is a tree with at least two distinct
\(K_0\)-portals.  Let \(L,M\) be the other two rooted bags.

Assume first that \(K_0\) is the only bag avoiding \(h,r\) which fails
to meet both \(A\) and \(C=\{1,2\}\).  In particular \(K_0\sim C\).
Choose in \(T\):

* one prescribed \(b\)-root;
* one portal to each of \(L,M\); and
* one portal to \(K_0\).

Let \(W\) be the minimal subtree containing these four selected vertices.

### Lemma 6.1 (off-core mixed branch peel)

If a component \(U\) of \(T-W\) contains both an \(A\)-portal and a
\(K_0\)-portal, then \(G\) contains a \(K_7\)-minor.

#### Proof

Put \(Y=T-U\).  A component of a tree outside a connected subtree has
exactly one edge to the subtree, so \(U,Y\) are connected and adjacent.
The selected \(K_0\)-portal in \(W\) ensures \(Y\sim K_0\); the other
three selected vertices ensure that \(Y\) retains its \(b\)-root and its
edges to \(L,M\).

Replace

\[
                         K_0\longmapsto K_0\cup U,
 \qquad                 T\longmapsto Y.             \tag{6.1}
\]

The first new bag is connected through the \(UK_0\)-edge and now meets
\(A\).  It still meets \(C\) and the other three rooted bags through the
old \(K_0\)-contacts.  The second new bag retains all four rooted-model
requirements by the choice of \(W\), including its edge to the enlarged
first bag.  Thus the four resulting rooted bags all meet both \(A,C\).
Together with \(\{b\}\) and the connected partition

\[
                         A\mid(\{d\}\cup C)
\]

they form the explicit \(K_7\)-model of the dark-bag allocation theorem.
\(\square\)

### Theorem 6.2 (tree gate normal form)

Unless \(G\) has a \(K_7\)-minor, every component of \(T-W\) is
portal-pure with respect to the two classes \(A,K_0\).  Moreover all such
components can be consumed label-preservingly:

* an \(A\)-pure component is absorbed into the connected bag \(A\);
* a \(K_0\)-pure component is absorbed into \(K_0\); and
* an unlabelled component is discarded.

After these operations the rooted model is retained and the tree gate is
exactly \(W\), a minimal Steiner tree for four protected labels and hence
has at most four leaves.  Any failure of a further edge peel is an exact
owner cut inside this four-label tree.

#### Proof

Mixed components are excluded by Lemma 6.1.  If \(U\) is \(A\)-pure,
then \(A\cup U\) is connected through an \(AU\)-edge and remains
anticomplete to \(K_0\); the unique tree edge from \(U\) to \(T-U\)
retains the required \(A\)-gate adjacency.  The proof for a
\(K_0\)-pure component is symmetric.  Removing any component leaves the
subtree \(W\), and therefore the protected \(b,L,M,K_0\) contacts,
inside a connected residual gate.  Components of \(T-W\) have no edges
to one another, so the operations iterate.  Minimality of \(W\) charges
every leaf to a distinct one of its four selected terminal labels, giving
the leaf bound. \(\square\)

This is the precise tree version of the requested labelled peel.  It
closes every off-core mixed placement, of arbitrary size.  The surviving
tree is not an arbitrary bag: all mixing is confined to a four-terminal
Steiner core, and each failed edge orientation names the protected label
which it owns.

## 7. When the dark rooted-core quotient is genuinely two-apex

There is also a sharp, fully checkable two-apex outcome.  Suppose two
distinct rooted bags \(K_A,K_C\) are respectively anticomplete to
\(A\) and to \(C\).  Delete \(d,b\), and contract the six connected
bags

\[
                         A,C,K_0,K_1,K_2,K_3.        \tag{7.1}
\]

The simple contact quotient is a subgraph of \(K_6\) missing the path

\[
                         K_A-A-C-K_C.                \tag{7.2}
\]

The graph \(K_6-E(P_4)\) is planar: start with a plane \(K_4\) on
\(K_A,K_C\) and the other two rooted vertices; insert \(A\) into the
face incident with \(K_C\) and the latter two vertices, and insert \(C\)
into the opposite face incident with \(K_A\) and those two vertices.

### Theorem 7.1 (opposite-dark rural expansion)

Assume that the six bags in (7.1) are trees (the two boundary bags are
the literal edges \(ac\) and \(12\)).  If their societies are rural in
one compatible plane rotation of the full contact multigraph, then
\(G-\{d,b\}\) is planar.  Hence \(G\) is two-apex.

If no such rural rotation exists, the tree interval criterion returns a
named alternating edge in one of the six actual bags.  When that edge is
in the multiply-hit tree \(T\) and has the off-core mixed placement of
Lemma 6.1, it gives the explicit \(K_7\); otherwise it is a labelled
owner cut in its tree society.  All parallel interbag edges are included
in the rotation.

#### Proof

The simple quotient is planar by (7.2), and extra absent contacts only
delete edges.  Draw every parallel bundle in a narrow strip of a plane
quotient embedding and substitute the six rural tree societies in
disjoint vertex disks.  This draws every edge of \(G-\{d,b\}\), proving
the two-apex conclusion.  If substitution fails, apply the tree interval
criterion to a nonrural society in any compatible quotient rotation.  A
mixed off-core cut in \(T\) is Lemma 6.1; in every other case the label
whose retention prevents that peel is recorded as the owner of the cut.
\(\square\)

Thus the all-tree rooted-core singleton cell is closed whenever its
contact defect graph contains the opposite-dark path (7.2) and the
societies are rotation-compatible.  The exact residue is now one of:

1. only one dark type is present;
2. a four-label owner core from Theorem 6.2; or
3. an alternating owner cut returned by Theorem 7.1.

## 8. Exact endpoint

The result is not a proof of \(HC_7\).  It proves a label-preserving
split-versus-two-apex theorem for the all-tree near-\(K_7^-\) cell and an
explicit completion theorem for the new degree-seven rooted \(K_5\).
The remaining near-clique states are now precisely:

* unbalanced owner cuts with the capacity bound (4.2);
* incompatible preferred orders in the \(DE\)-edge bundle, witnessed by
  an unbalanced cut in at least one tree society; and
* rooted-core certificates locked to every reserved connector.

These are the same two-shore capacity states appearing in the main
portal-exchange route.  Thus the near-clique backup no longer ends at the
vague instruction “split a multiply hit bag”; it reaches the identical
owner/rotation/connector obstruction by an independent normalization.

### Audit boundaries

* No singleton model vertex is treated as universal.  Every completion
  above cites the actual boundary edge or portal which supplies it.
* The two-apex conclusions use the full contact multigraph and every
  induced bag edge.  A planar simple quotient is never expanded without
  the rural-society hypothesis.
* Lemma 6.1 needs the selected \(K_0\)-portal inside \(W\); this is what
  preserves the \(K_0T\)-edge after the peel.
* Rurality of the single multiply-hit tree \(T\) does **not** imply that
  the whole graph is two-apex.  Theorem 7.1 requires all six societies to
  be simultaneously rural.  Dropping this condition would repeat the
  planar-quotient error.
* The unclosed four-label owner core is stated as a residue, not called a
  contradiction.  Eliminating it still requires a contraction-critical
  state transition or a second compatible society.

## 9. Sharp counterexample when rurality or reserve contacts are omitted

The following six-vertex construction shows that both qualifications are
real.  Begin with a planar \(K_5^-\) quotient on
\(a,c,q,e,D\), with deficient pair \(ac\).  Expand \(D\) to the tree
edge \(xy\), put

\[
 x\sim a,c,qquad y\sim q,e,
\]

and retain the five quotient edges

\[
 aq,ae,cq,ce,qe.
\]

Contracting \(xy\) gives back the planar \(K_5^-\).  Before contraction,
however, the graph contains the literal \(K_{3,3}\) with bipartition

\[
                         \{a,c,y\}\mid\{q,e,x\}.
\]

Thus the planar quotient does not expand.  The edge \(xy\) is exactly the
alternating tree cut: its \(x\)-side meets both deficient roots, but its
\(y\)-side retains neither deficient root, so the balanced peel condition
fails.  This is the smallest owner-cut architecture.

Adjoining two adjacent universal vertices produces a spanning
\(K_7^-\)-model.  The six-vertex core has no \(K_5\)-minor (on six
vertices this is checked by deleting one vertex or contracting one edge),
and it has a \(K_4\)-minor, so the join has Hadwiger number six.  Hence
even this expanded near-\(K_7\) graph has no \(K_7\)-minor.  It is only
five-connected and belongs to the two-apex alternative: deleting \(a\)
and \(q\) leaves the join of the two universal vertices with a four-cycle,
namely the planar octahedral graph.  Seven-connectivity and
contraction-critical state exchange are therefore indispensable for
excluding the owner cut.

## 10. Collective compensator lobes give a two-bag exchange

Return to the two-complex-bag model (1.1).  Let \(xy\) be an edge of
the tree \(D\), and let

\[
 D=P\mathbin{\dot\cup}R
\]

be the two components of \(D-xy\), with \(P\sim a,c\).  Put

\[
 T_0=\{c,q_1,q_2,q_3\},
 \qquad M=\{s\in T_0:R\not\sim s\}.                 \tag{10.1}
\]

In the opposite bag \(E\), choose one portal to each vertex of
\(T_0\cup\{a\}\), and let \(W\) be a vertex-minimal connected subgraph
containing the five selected portals.  Let \(\mathcal L_R\) be the set
of components \(L\) of \(E-W\) having an edge to \(R\), and put

\[
                         L^*=\bigcup_{L\in\mathcal L_R}L. \tag{10.2}
\]

### Theorem 10.1 (collective-lobe two-bag exchange)

Assume \(M\ne\varnothing\).  If

\[
             \text{for every }s\in M\text{ some }L\in\mathcal L_R
             \text{ satisfies }L\sim s,              \tag{10.3}
\]

then \(G\) contains a \(K_7\)-minor.

#### Proof

Set

\[
 Z=R\cup L^*,\qquad Y=E-L^*.
\]

The set \(Z\) is connected because every selected lobe has an edge to
the connected set \(R\).  The set \(Y\) is connected: it contains
connected \(W\), and every unselected component of \(E-W\) has an edge
to \(W\).  Since \(M\ne\varnothing\) in the only nontrivial use of
(10.3), at least one selected lobe exists; its edge to \(W\) gives
\(ZY\ne\varnothing\).

The bag \(Z\) sees every member of \(T_0\): \(R\) supplies the labels
outside \(M\), and (10.3) supplies those in \(M\).  The protected bag
\(Y\) sees all of \(T_0\cup\{a\}\) through its selected portals in
\(W\).  Now use

\[
 \{a\}\cup P\mid\{c\}\mid\{q_1\}\mid\{q_2\}\mid
 \{q_3\}\mid Z\mid Y.                               \tag{10.4}
\]

The first bag is connected and meets \(c\) through \(P\), repairing
the deficient pair.  It meets \(Z\) through the \(PR\)-edge and meets
\(Y\) through the old \(aY\)-edge.  The last two bags are adjacent as
above and both see \(c,q_1,q_2,q_3\).  Every other pair is an old
singleton-model adjacency.  Thus (10.4) is a \(K_7\)-model. \(\square\)

### Corollary 10.2 (common owner label)

In a \(K_7\)-minor-free graph with \(M\ne\varnothing\), there is a
single label \(s^*\in M\) such that

\[
                         L^*\not\sim s^*.             \tag{10.5}
\]

Equivalently, **every** off-core lobe hit by \(R\) is dark to the same
missing label \(s^*\).  This is stronger than assigning a possibly
different failed label to each lobe.

Seven-connectivity simultaneously gives

\[
 |N_E(R)|\ge
 1+|\{s\in\{a,c,q_1,q_2,q_3\}:R\not\sim s\}|.        \tag{10.6}
\]

### Lemma 10.3 (equality is an exact seven-adhesion)

Write

\[
 m_R=|\{s\in\{a,c,q_1,q_2,q_3\}:R\not\sim s\}|.
\]

If equality holds in (10.6), then

\[
 N_G(R)=\{x\}\mathbin{\dot\cup}
        N_{\{a,c,q_1,q_2,q_3\}}(R)
        \mathbin{\dot\cup}N_E(R)                  \tag{10.7}
\]

has order exactly seven, where \(x\) is the endpoint of \(xy\) in
\(P\).  Thus \(R\) is a connected fragment behind an exact seven-cut.
If nested exact seven-fragments have already been excluded by the
transport/descent theorem, then every unbalanced residual instead has
the strict surplus

\[
                         |N_E(R)|\ge m_R+2.          \tag{10.8}
\]

#### Proof

Because \(D\) is a tree, \(x\) is the only neighbour of \(R\) in
\(P\).  Spanningness says that every other neighbour lies in the five
singletons or in \(E\), giving the disjoint equality (10.7).  Exactly
\(5-m_R\) singleton vertices see \(R\); equality in (10.6) therefore
gives

\[
 |N_G(R)|=1+(5-m_R)+(m_R+1)=7.
\]

At least one missed singleton lies beyond the cut in the unbalanced case,
so it is a genuine separation and \(R\) is one of its components.  The
last assertion is the integral strict alternative after equality has been
excluded. \(\square\)

Consequently the unresolved alternative is exact: either the amplified
\(R\)-portals are concentrated inside the five-terminal core \(W\), or
every portal outside it lies in a lobe with the common owner defect
(10.5).  The former is a bounded-terminal order problem; the latter is
the precise state on which a deletion/contraction transition must act.

The theorem uses all compensating lobes simultaneously and therefore
closes families that no one-lobe peel sees.  It does not turn the owner
label in (10.5) into a six-vertex separator: the lobes may have many
distinct neighbours in \(R\) and many attachment vertices in \(W\).

## 11. Strict surplus and all local cut inequalities still permit an owner

The strict alternative (10.8) is not, by itself, enough to split the
opposite tree.  Here is a minimal explicit society demonstrating the
remaining need for contraction-critical state exchange.

Let \(D\) be the path

\[
 p_1p_2p_3p_4p_5z_1z_2z_3z_4,
\]

with \(P=\{p_1,\ldots,p_5\}\) and
\(R=\{z_1,\ldots,z_4\}\).  Every \(p_i\) sees all five singleton
labels.  Every \(z_i\) sees \(a,q_1,q_2,q_3\) and misses \(c\).  Thus
\(m_R=1\).

Let the opposite tree \(E\) have edges

\[
                         uv,\quad vr_1,\quad vr_2.    \tag{11.1}
\]

Give it boundary rows

\[
\begin{array}{c|c}
u&a,c\\
v&q_1,q_2,q_3\\
r_1&a,q_1,q_2,q_3\\
r_2&a,q_1,q_2,q_3.
\end{array}                                           \tag{11.2}
\]

Join every \(p_i\) to \(u,v\), and use the cross rows

\[
\begin{array}{c|c}
z_1&v,r_1\\
z_2&v,r_2\\
z_3&r_1,r_2\\
z_4&v,r_1,r_2.
\end{array}                                           \tag{11.3}
\]

Then

\[
                         N_E(R)=\{v,r_1,r_2\},
 \qquad |N_E(R)|=3=m_R+2.                             \tag{11.4}
\]

All three vertices are anticomplete to \(c\), the common owner label.
The protected five-terminal core is \(W=uv\); the two off-core
\(R\)-lobes are \(r_1,r_2\), and the third amplified portal is trapped
inside \(W\).

The central edge \(uv\) is nonrural in the plane \(K_5^-\) rotation:
its \(u\)-side carries the opposite classes \(a,c\), while its
\(v\)-side carries the opposite classes \(q_3,D\).  Nevertheless no edge
of \(E\) gives the split required by (10.4).  A side meeting both \(c\)
and an \(R\)-portal must contain \(u,v\); its complement is then at most
one of the leaves \(r_i\) and cannot retain all five protected boundary
labels.

This is not merely caused by an exact seven-fragment.  The contact rows
can be chosen, as in (11.2)--(11.3), so that every nonempty proper
connected subset of either tree has at least eight distinct external
neighbours.  For \(E\), the minimum is already visible on the four
singletons:

\[
\begin{aligned}
|N(u)|&=1+2+5=8,\\
|N(v)|&=3+3+3=9,\\
|N(r_i)|&=1+4+3=8.
\end{aligned}
\]

The remaining connected subsets have larger boundary.  Giving every
\(p_i\) the two \(E\)-neighbours \(u,v\), and the cross rows (11.3),
makes the same assertion true for every proper interval of the path
\(D\).  The dependency-free verifier
`near_k7_strict_surplus_tree_counterarchitecture.py` checks every proper
connected subset and every edge split.

Thus the strongest conclusion available from seven-connectivity, strict
portal surplus, rural/nonrural order, and absence of exact seven-cuts is
still the owner state above.  The construction is an interface
counterarchitecture, not a seven-connected \(K_7\)-minor-free host.  To
exclude it in a counterexample one must use the one-step colouring
transition: some deletion or contraction has to create a \(c\)-contact
in an \(R\)-hit lobe or reroute one of the three core portals across
\(uv\).  Static cut inequalities cannot do so.

### Audit correction

The last sentence describes what the listed *static inequalities* fail to
do, but the literal test society is eliminated even before a colouring
transition is used: for any consecutive \(p_i,p_{i+1}\),

\[
 \{a\}\mid\{q_1\}\mid\{q_2\}\mid\{q_3\}
 \mid\{p_i\}\mid\{p_{i+1}\}\mid E
\]

is a \(K_7\)-model.  The first four bags form a clique, both \(p\)-vertices
see all four and each other, and the connected bag \(E\) sees all six.
Thus this example only proves that the selected local cut data do not force
the protected two-bag peel; it is not a \(K_7\)-free portal architecture.
Any use of it as a residual counterexample must retain this qualification.
The operation-critical replacement and the resulting full-row-edge lemma
are recorded in `hadwiger_strict_surplus_operation_states.md`, Sections
6--7.
