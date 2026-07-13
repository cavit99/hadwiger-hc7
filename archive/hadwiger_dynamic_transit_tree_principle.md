# Dynamic transit trees: split, rotation, or an apex-pinned owner corridor

## Status and main point

This note proves a uniform theorem for an induced tree which is simultaneously

* a branch bag of a fixed labelled clique model;
* the whole minimal list obstruction obtained from one contraction; and
* a transit bag carrying two neighbourhood feet.

The new fact is that the perfectly matched list core does not merely give
unrelated edge witnesses.  It gives one **canonical aligned colouring of
every edge deletion**.  Around every nonmatching tree edge whose label is not
the apex colour, the two adjacent matching-edge operations have the same
marked state on the two ends of the edge.  If their two shores were separated,
the crossed-transition theorem would colour the original graph.  Therefore
the edge has an ambient bypass.  A bypass either rotates the branch bag while
preserving every old label, or has a first hit in a named foreign bag.

The only internal edge label which can evade this argument is the colour of
the apex.  Simultaneously contracting the two adjacent matching edges then
gives a sharp replacement: a clean rerouting, or a lock whose colour is
repeated between the apex and the two-vertex gate.  Thus an arbitrary
full tree core either rotates cleanly, transits a named foreign bag, or is
an end-locked path labelled
\(\alpha,\delta,\alpha,\delta,\ldots,\alpha\).  Portal Helly then reduces
the split-free society to an owner gate on this same two-colour path.  A
centred gate with two non-apex-coloured lobes already forces a rotation or
foreign transit, because those lobes have the same unpinned singleton
marked state.

This is a genuine infinite-family reduction.  It is not yet the complete
rooted-model theorem.  The remaining alternating corridor is real: the
fixed-model family in
`hadwiger_fixed_model_contraction_portal_alignment_audit.md` realizes its
smallest member.  Consequently a theorem claiming an unconditional split
from the matched core is false.  Section 11 closes the spanning-singleton
corridor.  Section 12 reduces the nonspanning singleton corridor, under the
connectivity available in \(HC_7\), to a clean rotation even with arbitrary
unused shadow vertices.  Terminating those rotations is part of core
exchange; interaction with two or more complex bags is the other residue.

## 1. Setup

Let \(r\ge 3\).  Let \(G\) be non-\(r\)-colourable and suppose that every
proper minor of \(G\) is \(r\)-colourable.  Fix \(v\in V(G)\), put

\[
                         H=G-v,
\]

and let

\[
                    \mathcal B=(T,B_2,\ldots,B_r)       \tag{1.1}
\]

be a fixed \(K_r\)-model in \(H\).  In this note \(T\) is an induced tree
with at least one edge, and \(T\cap N_G(v)\ne\varnothing\).  Contract
\(T\) to \(z\), choose an
\(r\)-colouring \(c\) of \(G/T\), and write

\[
                         c(z)=\alpha,\qquad c(v)=\delta . \tag{1.2}
\]

The edge \(vz\) gives

\[
                              \alpha\ne\delta.           \tag{1.3}
\]

For \(x\in V(T)\), define the expansion list

\[
 L(x)=[r]\setminus c\bigl(N_G(x)-V(T)\bigr).             \tag{1.4}
\]

Every list contains \(\alpha\), and \(T\) is not \(L\)-colourable.  The
main theorem below uses the following **full-core hypothesis**:

> no proper induced subtree of \(T\) is non-\(L\)-colourable.              \(\tag{FC}\)

This hypothesis cannot simply be dropped.  If a selected minimal core is a
proper subtree, arbitrary portal societies can be put in the hanging parts;
see Section 8.

By the minimal-tree obstruction theorem there is a proper edge-colouring

\[
                         \lambda:E(T)\longrightarrow[r] \tag{1.5}
\]

such that

\[
 L(x)=\{\lambda(e):e\ni x\},                             \tag{1.6}
\]

and the \(\alpha\)-edges form a perfect matching \(M_\alpha\) of \(T\).

For a branch bag \(B_j\), its portal class in \(T\) is

\[
 P_j=\{x\in V(T):N_G(x)\cap B_j\ne\varnothing\}.          \tag{1.7}
\]

We also write \(P_0=T\cap N_G(v)\) for the foot class.  All the statements
below work for an arbitrary family of protected portal classes, not only
the classes in (1.7).

## 2. Canonical edge transitions and tree-convex states

The existence part below is implicit in the matched-tree theorem.  The
uniqueness and convexity are useful additional facts.

### Theorem 2.1 (canonical aligned edge-transition family)

For every edge \(e\in E(T)\), there is a unique \(L\)-colouring
\(\varphi_e\) of \(T-e\).  The two ends of \(e\) both receive
\(\lambda(e)\).  Keeping \(c\) on \(G-T\) and using \(\varphi_e\) on
\(T\) gives a proper \(r\)-colouring \(c_e\) of \(G-e\).

All the colourings \(c_e\) agree literally on \(G-T\).  More explicitly,
for \(x\in V(T)\), let \(h_e(x)\) be the first edge on the path from \(x\)
to \(e\), taking \(h_e(x)=e\) when \(x\) is an end of \(e\).  Then

\[
                             c_e(x)=\lambda(h_e(x)).       \tag{2.1}
\]

#### Proof

Minimality of \(T\) says that the two components of \(T-e\) are
list-colourable.  The minimal-tree obstruction theorem says that in every
such colouring each end of \(e\) is forced to \(\lambda(e)\).

Root either component of \(T-e\) at its end of \(e\).  Let \(y\) be a
nonroot vertex and let \(f\) be the edge from \(y\) toward the root.  The
restriction of a colouring to the component of \(T-f\) lying beyond \(y\)
is a list-colouring of that component.  The same forced-end assertion for
\(f\) gives \(c_e(y)=\lambda(f)\).  Induction away from the root proves
(2.1) and uniqueness.

The lists ensure properness on every edge from \(T\) to \(G-T\), and
\(\varphi_e\) is proper on every tree edge except \(e\).  Since \(T\) is
induced, there is no further internal edge to check.  This proves that
\(c_e\) colours \(G-e\). \(\square\)

For \(x\in V(T)\) and an incident edge \(h\), let \(E(x,h)\) consist of
\(h\) and all edges in the component of \(T-x\) reached through \(h\).
Equation (2.1) gives

\[
 \{e:c_e(x)=\lambda(h)\}=E(x,h).                         \tag{2.2}
\]

Thus each named colour state of one vertex is an edge-subtree.

### Corollary 2.2 (exact state cells are tree-convex)

Let \(X\subseteq V(T)\), and let \(q:X\to[r]\) be a named colour vector.
Then

\[
 \mathcal C_X(q)=\{e\in E(T):c_e|_X=q\}                  \tag{2.3}
\]

is empty or the edge set of a connected subtree of \(T\).

If \(C\) is a component of \(T-X\) containing an edge, then
\(c_e|_X\) is independent of the choice of \(e\in E(C)\).

#### Proof

By (2.2), (2.3) is an intersection of connected edge-subtrees of a tree,
and hence is connected when nonempty.  For the second assertion, the first
edge on the path from a fixed \(x\in X\) to an edge of \(C\) is independent
of the edge chosen in \(C\).  Apply (2.1) at every \(x\in X\). \(\square\)

Only **named** state cells are asserted to be convex.  Equality partitions
need not be convex; Section 8 gives the smallest counterexample.

## 3. Same-state lobes rotate or colour-glue

For a colouring \(d\) of \(G-e\), recall the marked state at an adhesion
\(X\subseteq V(H)\):

\[
 \sigma_X(d)=\bigl(\Pi_X(d),P_X(d)\bigr),\qquad
 P_X(d)=\{x\in X:d(x)=d(v)\}.                            \tag{3.1}
\]

The crossed-transition theorem says that edge operations on opposite open
shores cannot have the same marked state.

### Lemma 3.1 (canonical lobe exchange)

Let \(X\subseteq V(T)\), and let \(C,D\) be distinct components of
\(T-X\), each containing an edge.  Choose \(e\in E(C)\) and
\(f\in E(D)\).  If

\[
                              c_e|_X=c_f|_X,              \tag{3.2}
\]

then \(C\) and \(D\) lie in the same component of \(H-X\).

#### Proof

If they lay in different components, group the component containing \(C\)
on one side of a separation of \(H\) with adhesion \(X\), and group the
component containing \(D\) on the other.  The edges \(e,f\) are strictly
on opposite shores.  The colourings \(c_e,c_f\) agree on \(X\), agree at
\(v\), and are proper colourings of the corresponding edge-deleted graphs.
Crossing their side restrictions colours \(G\), a contradiction. \(\square\)

Let

\[
 U_T=H-\bigcup_{j=2}^rV(B_j)                              \tag{3.3}
\]

be the model-clean region for the transit bag.

### Lemma 3.2 (rotation or named foreign transit)

Under the hypotheses of Lemma 3.1, at least one of the following holds.

1. A path in \(U_T-X\) joins the two tree lobes.  Two consecutive visits
   of a shortest such path to \(T\) give a \(T\)-path \(Q\) whose interior
   avoids every old branch bag.  Adding \(Q\) to \(T\) and deleting an
   edge on the old tree path between its ends is a label-preserving clean
   rotation of the branch bag.
2. Every \(X\)-avoiding path in \(H\) between the two lobes meets a named
   foreign bag \(B_j\).  A shortest path gives a first-hit foreign-transit
   certificate.

#### Proof

Lemma 3.1 supplies an \(X\)-avoiding ambient path.  If the two lobes are
connected in (3.3), choose a shortest path and take a subpath between two
consecutive visits to \(T\).  Its interior avoids \(T\) and every foreign
bag.  Its union with \(T\) contains one cycle; delete any old tree edge on
the corresponding tree interval.  The resulting transit bag is connected,
disjoint from all other bags, and retains every old portal vertex and every
old interbag edge.  This is outcome 1.

If the lobes are disconnected in (3.3), every ambient path supplied by
Lemma 3.1 leaves (3.3), and hence meets one of the named bags deleted in
(3.3).  First-hit truncation gives outcome 2. \(\square\)

This is the promised exact split between geometry and colouring: a repeated
canonical state cannot hide behind a model-relative cut.  It either rotates
the model cleanly or identifies the foreign bag through which it transits.

## 4. The opposite-mate bypass theorem

Let \(h=xy\) be a non-\(\alpha\) edge of \(T\), and write

\[
                         \lambda(h)=\beta.                \tag{4.1}
\]

Let \(e_x=xx'\) and \(e_y=yy'\) be the unique \(\alpha\)-matching edges
incident with \(x,y\), respectively.  They are distinct and
vertex-disjoint.

### Theorem 4.1 (every non-apex-coloured core edge has a bypass)

If \(\beta\ne\delta\), then \(x'\) and \(y'\) lie in the same component
of

\[
                              H-\{x,y\}.                  \tag{4.2}
\]

Consequently there is an \(x\)-to-\(y\) detour in \(H-h\).  Relative to
the fixed model, this detour gives either

1. a label-preserving clean rotation replacing \(h\); or
2. a named first hit in a foreign branch bag.

#### Proof

Apply Theorem 2.1 to the two matching edges.  On \(X=\{x,y\}\), formula
(2.1) gives

\[
 (c_{e_x}(x),c_{e_x}(y))=(\alpha,\beta),\qquad
 (c_{e_y}(x),c_{e_y}(y))=(\beta,\alpha).                 \tag{4.3}
\]

Both equality partitions consist of two singleton blocks.  By
(1.3) and the hypothesis \(\beta\ne\delta\), neither state is pinned to
the apex.  Therefore

\[
                         \sigma_X(c_{e_x})=
                         \sigma_X(c_{e_y}).               \tag{4.4}
\]

If \(x',y'\) belonged to different components of (4.2), the separation
with adhesion \(X\) would put \(e_x,e_y\) on opposite open shores.
Equation (4.4) and the crossed-transition theorem would colour \(G\), a
contradiction.  This proves the first assertion.

Join \(x'\) to \(y'\) in (4.2), and add the two matching edges
\(xx',yy'\).  The result is an \(x\)-to-\(y\) path avoiding \(h\).  Apply
the clean-region argument of Lemma 3.2 to obtain the last two alternatives.
\(\square\)

The point is the marked-state swap in (4.3): names \(\alpha,\beta\) are
interchanged, but the equality partition and the unpinned apex block are
identical.  This is precisely why exact named-state convexity alone was not
enough.

### Theorem 4.2 (a matching edge with two clean flanks has a bypass)

Let \(g=uv\in M_\alpha\).  Suppose \(h_u=ux\) and \(h_v=vy\) are edges in
the two components of \(T-g\), and write

\[
                         \lambda(h_u)=\beta,qquad
                         \lambda(h_v)=\gamma.
\]

If \(\beta,\gamma\ne\delta\), then \(x,y\) lie in the same component of
\(H-\{u,v\}\).  Hence \(g\) has an ambient detour and gives a clean
label-preserving rotation or a named foreign transit.

#### Proof

Use the canonical deletion colourings of \(h_u,h_v\).  Formula (2.1) gives
on \(X=\{u,v\}\)

\[
 (c_{h_u}(u),c_{h_u}(v))=(\beta,\alpha),\qquad
 (c_{h_v}(u),c_{h_v}(v))=(\alpha,\gamma).                \tag{4.5}
\]

Both equality partitions have two singleton blocks, and both states are
unpinned because \(\alpha,\beta,\gamma\ne\delta\).  If \(x,y\) lay in
different components of \(H-X\), the two edge operations would lie on
opposite shores with the same marked state, contradicting crossed
transition splicing.  An \(x\)-to-\(y\) path in \(H-X\), together with
\(h_u,h_v\), is a detour around \(g\).  Clean/foreign first-hit
classification is Lemma 3.2. \(\square\)

Since incident edge labels are distinct, a matching owner edge which evades
Theorem 4.2 is end-locked on one side, or has a unique \(\delta\)-labelled
flank there.  This already rules out a matching bridge with two genuinely
branching non-apex sides.

### Theorem 4.3 (global collapse of a rotation-rigid full core)

Under (FC), at least one of the following holds.

1. The transit tree has a label-preserving clean rotation.
2. There is a named foreign-bag transit.
3. The whole tree \(T\) is a path and its edge labels are

   \[
                         \alpha,\delta,\alpha,\delta,
                         \ldots,\alpha.                  \tag{4.6}
   \]

#### Proof

Suppose first that some vertex \(q\) has degree at least three.  Exactly one
incident edge is in the \(\alpha\)-perfect matching, and at most one other
incident edge has label \(\delta\).  Hence two incident edges \(e,f\) have
labels different from \(\delta\).  In the canonical colourings
\(c_e,c_f\), the singleton adhesion \(\{q\}\) has the same marked state:
one block, unpinned.  If the two corresponding lobes of \(T-q\) were
distinct components of \(H-q\), crossed transition splicing would colour
\(G\).  Otherwise an ambient \(q\)-avoiding path gives outcome 1 or 2 by
Lemma 3.2.

We may therefore assume, in the absence of outcomes 1 and 2, that
\(\Delta(T)\le2\).  The connected tree \(T\) is a path.  Its
\(\alpha\)-edges form a perfect matching, so the path alternates between
matching and nonmatching edges and both end edges have label \(\alpha\).
If a nonmatching edge had a label different from \(\delta\), Theorem 4.1
would again give outcome 1 or 2.  Every nonmatching edge is consequently
\(\delta\)-labelled, proving (4.6). \(\square\)

Thus the dynamic edge-transition family collapses **every** full tree core,
of arbitrary size and branching, to the one end-locked two-colour path
which the static counterexample already predicted.

## 5. The apex-colour exception and rainbow lock capacity

When \(\beta=\delta\), the marked blocks in (4.3) are opposite singleton
blocks, so Theorem 4.1 cannot be applied.  The simultaneous two-operation
theorem gives a sharp replacement.

We first record the counting lemma in its useful general form.

### Lemma 5.1 (rainbow lock capacity)

Let \(f\) be a proper \(r\)-colouring of a graph with one edge
\(e=ab\) deleted, where \(f(a)=f(b)=\theta\).  Let \(W\) be a marked gate.
Suppose that for every \(\gamma\ne\theta\), the two
\(\{\theta,\gamma\}\)-components containing \(a,b\) are distinct and
both meet \(W\).  If \(n_\eta(W)\) is the number of vertices of colour
\(\eta\) in \(W\), then

\[
                         n_\theta(W)+n_\gamma(W)\ge2
                    \quad(\gamma\ne\theta).              \tag{5.1}
\]

Let \(W=R\mathbin{\dot\cup}P\), where \(R\) is rainbow, and put
\(C=f(R)\).  The exact shadow requirements on \(P\) are as follows.

* If \(\theta\in C\) and \(P\) has no \(\theta\)-vertex, then \(P\)
  contains every colour in \([r]-C\).
* If \(\theta\notin C\) and \(P\) has no \(\theta\)-vertex, then \(P\)
  contains a second copy of every colour in \(C\), and at least two copies
  of every colour in \([r]-(C\cup\{\theta\})\).
* If \(\theta\notin C\) and \(P\) has exactly one \(\theta\)-vertex,
  then \(P\) contains every colour in
  \([r]-(C\cup\{\theta\})\).
* Two \(\theta\)-vertices in \(P\) satisfy all the pair inequalities by
  themselves.

In particular, if \(P=\varnothing\) and

\[
                            0<|R|<r,                      \tag{5.2}
\]

the assumed lock is impossible.

#### Proof

For fixed \(\gamma\), the two components are disjoint.  Each of their
vertices in \(W\) has colour \(\theta\) or \(\gamma\), so two distinct
gate vertices with those colours are necessary.  This is (5.1).

Write (5.1) using the one-or-zero contribution of the rainbow set \(R\).
If \(\theta\in C\), either a shadow repeats \(\theta\), or every colour
absent from \(C\) must occur in \(P\).  If \(\theta\notin C\), zero, one,
or at least two shadow copies of \(\theta\) give exactly the three cases
listed.  Finally, when \(P\) is empty, a colour missing from a proper
rainbow set violates (5.1) if \(\theta\in C\), while any colour of the
nonempty set \(C\) violates it if \(\theta\notin C\). \(\square\)

There is also a geometric package behind (5.1).  Choose first-hit paths
from \(a\) and \(b\) to \(W\) in every bichromatic layer.  The unions on
the two sides are connected.  Different layers can meet across the two
sides only at \(\theta\)-vertices.  Such a meeting concatenates to an
\(a\)-to-\(b\) multicolour detour; if there is no meeting, the two unions
are disjoint connected carriers adjacent through \(e\).  Thus (5.1) is a
literal two-carrier capacity condition, not only a numerical count.

### Corollary 5.2 (three-vertex gate)

If \(r\ge4\), \(|W|=3\), and the lock in Lemma 5.1 occurs, then

\[
                             n_\theta(W)\ge2.              \tag{5.3}
\]

#### Proof

Sum (5.1) over all \(\gamma\ne\theta\).  Since \(|W|=3\),

\[
 (r-1)n_\theta(W)+3-n_\theta(W)\ge2(r-1),
\]

or

\[
                         (r-2)n_\theta(W)\ge2r-5.
\]

For \(r\ge4\), this excludes \(n_\theta(W)\le1\). \(\square\)

### Corollary 5.3 (rainbow two-shore gates reroute)

Let two vertex-disjoint edges lie on opposite shores of a separation, and
obtain the common colouring \(f\) by contracting both edges and expanding
their contraction vertices.  Put \(W=X\cup\{v\}\).  If \(W\) is rainbow
under \(f\) and

\[
                              0<|W|<r,                    \tag{5.4}
\]

then at least one of the two operated edges has a bichromatic endpoint
detour.

#### Proof

The double-operation repair exclusion selects a side with no repair while
the common state on \(W\) is fixed.  If none of its bichromatic layers joins
the two endpoints, the Kempe-lock dichotomy gives the hypotheses of
Lemma 5.1 with \(R=W\) and \(P=\varnothing\), contrary to (5.2). \(\square\)

### Theorem 5.4 (the apex-coloured edge has a rotation or a pinned shadow)

Assume \(r\ge4\), and let \(h=xy\) in Section 4 satisfy
\(\lambda(h)=\delta\).  At least one of the following holds.

1. There is an \(x\)-to-\(y\) detour in \(H-h\), hence a clean rotation
   or a named foreign transit.
2. One of the matching edges \(e_x,e_y\) has a bichromatic detour, hence a
   clean rotation of that matching edge, a named foreign transit, or a
   first hit at the apex \(v\).
3. The sets containing \(x'\) and \(y'\) are separated in
   \(H-\{x,y\}\), and a simultaneous two-edge contraction produces a
   no-repair side whose locked colour \(\theta\) occurs twice on

   \[
                              W=\{x,y,v\}.                \tag{5.5}
   \]

   Since \(xy\) is an edge, \(f(x)\ne f(y)\); consequently \(v\) has
   colour \(\theta\) together with exactly one of the two gate vertices.
   This is an apex-pinned shadow state.

#### Proof

If \(x',y'\) lie in the same component of \(H-\{x,y\}\), the path used in
Theorem 4.1 gives outcome 1, without using the label of \(h\).

Otherwise \(X=\{x,y\}\) is an actual adhesion between the two matching
edges.  Contract both \(e_x,e_y\), colour the proper minor, and expand the
two contraction vertices.  By the double-operation repair exclusion, at
least one of the two monochromatic edge defects cannot be repaired while
the common state on \(X\cup\{v\}\) is fixed.  Apply the Kempe-lock
dichotomy to that edge.  If the two endpoints lie in the same bichromatic
component, that component gives outcome 2.
Indeed, a shortest endpoint detour either lies in the model-clean region
\(U_T\), when it replaces the operated tree edge, or its first forbidden
vertex lies in a named foreign bag or is \(v\).
If there is no such component, both endpoint components in every other
colour layer meet \(W\), so Corollary 5.2 gives (5.3).  The edge \(xy\)
survives the two contractions and makes the colours of \(x,y\) distinct.
Thus the repeated locked colour uses \(v\) and one gate vertex, proving
outcome 3. \(\square\)

This theorem identifies, rather than conceals, the failure of the unpinned
exchange: the only surviving two-vertex gate has an apex-colour shadow.

## 6. Portal Helly and the dynamic corridor normal form

For a nonempty portal class \(P\subseteq V(T)\), let \(K(P)\) be its
minimal spanning subtree.  If \(|P|=1\), its edge set is empty.

### Lemma 6.1 (portal-tree split criterion)

For portal classes \(P_1,\ldots,P_m\), there is an edge \(g\) such that
both components of \(T-g\) meet every \(P_i\) if and only if

\[
                         g\in\bigcap_{i=1}^m E(K(P_i)).    \tag{6.1}
\]

If the intersection in (6.1) is empty, then either some \(P_i\) is a
singleton, or one of the following two mutually compatible certificates
exists.

1. All portal hulls contain one common vertex \(q\), but no edge incident
   with \(q\) belongs to every hull.  This is a centred Helly/star gate.
2. Two portal hulls are vertex-disjoint; their unique connector is a
   nontrivial path.

#### Proof

An edge belongs to the hull of \(P_i\) exactly when deleting it separates
two vertices of \(P_i\).  This proves the first assertion.

Apply the ordinary vertex-Helly theorem to the connected hulls.  If they
are pairwise vertex-intersecting, they have a common vertex \(q\).  The
failure of (6.1) says that no edge at \(q\) is common to all of them, giving
the centred gate.  If they are not pairwise intersecting, two are
vertex-disjoint and the tree has a unique nontrivial path between them.
\(\square\)

The centred alternative is essential.  On a three-leaf star, the three
leaf-to-leaf hulls pairwise share an edge and have the centre in common,
but no edge belongs to all three.  Thus edge sets of tree hulls do **not**
have the Helly property.

In the fixed-model application, if all \(r-1\) model portal classes occur
on both sides of \(g\), the two components of \(T-g\), together with the
other \(r-1\) old bags, form a \(K_{r+1}\)-model.  If the foot class also
occurs on both sides, both new pieces are adjacent to \(v\) as well.

### Theorem 6.2 (dynamic transit-corridor normal form)

Assume (FC), \(r\ge4\), and that (6.1) is empty for the protected portal
classes.  Then one of the following holds.

1. A protected label has a unique portal, or the hull family has a centred
   Helly/star gate \(q\).  In the latter case, the canonical operation
   states of the components of \(T-q\) are pairwise distinct at \(q\): the
   lobe through an incident edge \(e\) has state \(\lambda(e)\).  These
   states exhaust \(L(q)\), and every colour outside \(L(q)\) occurs on an
   external neighbour of \(q\).  Thus this is a saturated, named
   portal-owner/multilobe capacity gate.  If two incident labels differ
   from \(\delta\), it also gives a clean rotation or a named foreign
   transit.  Hence a rotation-free, transit-free centred residue has degree
   at most two; in degree two its incident labels are exactly
   \(\alpha,\delta\).  It is a literal apex-pinned cutvertex owner gate.

In every remaining case, choose two vertex-disjoint portal hulls and denote
their unique nontrivial connector by \(P\).  One of the following then
holds.

2. Some nonmatching edge of \(P\) has label different from \(\delta\), and
   Theorem 4.1 gives a label-preserving clean rotation or a named foreign
   transit.
3. Some \(\delta\)-labelled nonmatching edge of \(P\) gives one of the two
   rotations/dirty hits in Theorem 5.4.
4. Every nonmatching edge of \(P\) is \(\delta\)-labelled and carries the
   apex-pinned shadow state of Theorem 5.4.  Since both colour classes are
   matchings, the connector is an alternating

   \[
                               \alpha,\delta,
                               \alpha,\delta,\ldots       \tag{6.2}
   \]

   corridor.  A one-edge \(\alpha\)-connector is either rotated (or has a
   foreign transit) by Theorem 4.2, or it is end-locked/uniquely
   \(\delta\)-flanked on at least one side.

#### Proof

Apply Lemma 6.1.  A singleton hull or a centred Helly gate is outcome 1.
For a centred gate, formula (2.1) makes the state at \(q\) of an operation
in a given lobe equal to the label of its incident edge.  Properness of
\(\lambda\) makes those states distinct, (1.6) says they exhaust \(L(q)\),
and (1.4) supplies every missing colour externally.
At most one incident edge has label \(\delta\).  Whenever two incident
edges \(e,f\) have labels different from \(\delta\), in their
canonical deletion colourings, the singleton adhesion \(\{q\}\) has the
same marked state: its equality partition is the unique one-block partition
and it is unpinned.  The crossed-transition theorem therefore forbids the
two corresponding lobes from being distinct components of \(H-q\).
An ambient \(q\)-avoiding path between them gives a clean rotation or a
first foreign-bag hit exactly as in Lemma 3.2.  If no such pair exists,
properness of \(\lambda\) leaves at most one \(\delta\)-edge and at most one
other edge at \(q\).  The common colour \(\alpha\) occurs on the unique
matching edge at \(q\), proving the stated \(\alpha\delta\) residue.
Otherwise choose the two vertex-disjoint hulls supplied by the lemma and
let \(P\) be their nontrivial connector.  Every \(\alpha\)-edge belongs to
the perfect matching
\(M_\alpha\), so two such edges are never consecutive.  Hence a connector
of length at least two contains a nonmatching edge.

Apply Theorem 4.1 to every nonmatching edge whose label is not \(\delta\),
and Theorem 5.4 to every nonmatching \(\delta\)-edge.  If none returns a
rotation, a foreign transit, or an apex hit, every nonmatching edge has
label \(\delta\) and the pinned-shadow outcome occurs.  Properness of
\(\lambda\) makes the
\(\delta\)-edges a matching too, so the two labels alternate.  The only
connector not inspected by a nonmatching edge is a single matching edge;
apply Theorem 4.2 to its two flanks when they exist.  If it does not apply,
one side has no flank or its only available flank has label \(\delta\).
\(\square\)

This is the promised uniform structural reduction.  Arbitrary portal order
does not survive.  The residues are a low-degree centred owner gate, or a
two-colour alternating owner corridor with an explicit dynamic state at
every second edge.

### Corollary 6.3 (a pure alternating core is end-locked)

Suppose the whole core \(T\) is a path whose labels alternate
\(\alpha,\delta,\alpha,\delta,\ldots,\alpha\).  Then every internal vertex
has list \(\{\alpha,\delta\}\), while each end has list \(\{\alpha\}\).
Consequently

\[
                         N_G(v)\cap V(T)
                         \subseteq\{\text{the two ends of }T\}.           \tag{6.3}
\]

If \(T\) is a double-foot bag, its feet are therefore exactly its two ends.
Moreover every internal vertex has an external neighbour in every colour
outside \(\{\alpha,\delta\}\), and each end has an external neighbour in
every colour other than \(\alpha\).

#### Proof

Equation (1.6) makes a vertex list equal to its incident edge labels.  The
asserted lists follow from the alternating path.  A neighbour \(v\) of
colour \(\delta\) would exclude \(\delta\) from the list, so no internal
vertex is a foot.  Finally, the definition (1.4) says that every colour
absent from a list occurs on an external neighbour. \(\square\)

Thus the path residue is not an arbitrary comb: it is forced into the same
end-locked geometry as the sharp family in Section 8, with full external
palette saturation at every internal vertex.

## 7. Contact-maximality turns failed rotations into owners

The following elementary rotation is the precise way in which the
double-foot hypothesis interacts with contact maximality.

### Lemma 7.1 (safe foot transfer)

Assume \(T\) contains distinct feet \(a,b\in N_G(v)\).  Let \(g\in E(T)\)
separate \(T\) into \(A,C\), with \(a\in A\) and \(b\in C\).  Let
\(B_j\) be a noncontact bag.  If

\[
 C\sim B_j,
 \qquad
 A\sim B_k\quad\text{for every }k\ne j,                 \tag{7.1}
\]

then replacing

\[
                         T\longmapsto A,qquad
                         B_j\longmapsto B_j\cup C         \tag{7.2}
\]

is a \(K_r\)-model with one more contact bag.

#### Proof

The two new bags are connected and adjacent through \(g\).  The enlarged
\(B_j\) retains all its old adjacencies to the other bags.  Condition (7.1)
retains every adjacency from the residual transit bag \(A\).  The old bag
\(T\) remains contact through \(a\), while the formerly noncontact bag
\(B_j\cup C\) becomes contact through \(b\). \(\square\)

### Corollary 7.2 (owner interval at a maximal model)

If (1.1) is contact-maximal, every root-side lobe \(C\) which meets a
noncontact portal class \(P_j\) wholly contains another portal class
\(P_k\), for some \(k\ne j\).  Equivalently, the complementary side has
already lost the protected label \(k\).

On the \(a\)-to-\(b\) path, project every portal class to its interval of
attachment positions.  Let \(j\) be a noncontact label whose right endpoint
is maximal, say \(R\).  If \(R=0\), the noncontact class is concentrated at
the \(a\)-end and gives a named endpoint-owner gate.  If \(R>0\), the
\(b\)-tail beginning at \(R\) either

1. safely transfers the foot to \(B_j\), contradicting contact maximality;
2. wholly owns a contact portal class; or
3. wholly owns a different noncontact portal class whose projection is the
   singleton \(\{R\}\).

#### Proof

The first assertion is the contrapositive of Lemma 7.1, written in portal
language.  The case \(R=0\) is immediate from the definition of projection.
For \(R>0\), the \(b\)-tail beginning at \(R\)
meets \(P_j\).  A blocking class \(P_k\) lies wholly in that tail, so its
left endpoint is at least \(R\).  If \(k\) is noncontact, maximality of the
right endpoint of \(P_j\) forces both endpoints of the projection of
\(P_k\) to equal \(R\). \(\square\)

Thus in a contact-maximal counterexample the alternating corridor of
Theorem 6.2 is not merely a drawing obstruction.  It is simultaneously an
owner chain: every forbidden foot rotation traps an entire labelled portal
class.  Eliminating this owner/pinned-state chain is the exact remaining
uniform step.

## 8. Sharp obstructions and audit boundaries

### 8.1 The apex-colour exception is attained

The family \(F_r\) in
`hadwiger_fixed_model_contraction_portal_alignment_audit.md` has transit
path

\[
                         x_1x_2x_3x_4
\]

with lists

\[
 \{\alpha\},\quad\{\alpha,p_1\},\quad
 \{\alpha,p_1\},\quad\{\alpha\},
\]

edge labels

\[
                         \alpha,p_1,\alpha,
\]

and \(c(v)=p_1\).  It has a double foot and a fixed labelled clique model,
but all model portals are concentrated at one end and no label-preserving
split exists.  Thus its only nonmatching edge is exactly the exceptional
\(\delta\)-edge of Theorem 5.4.  The family is not minor-minimal and has the
target minor through another model, so it does not refute dynamic closure;
it proves that the \(\delta\)-corridor cannot be deleted from the theorem.

### 8.2 Marked-state cells are not convex

Take the four-vertex minimal path core with edge labels

\[
                              \alpha,\beta,\alpha.
\]

For its three edge operations, the colour pairs on the two middle vertices
are

\[
                         (\alpha,\beta),\quad
                         (\beta,\beta),\quad
                         (\beta,\alpha).                 \tag{8.1}
\]

If the apex colour is different from \(\alpha,\beta\), the first and last
operations have the same marked state--two singleton blocks, unpinned--but
the middle operation does not.  Hence marked-state preimages need not be
intervals.  Corollary 2.2 deliberately asserts convexity only for named
colour vectors.  The disconnected repetition in (8.1) is precisely what
drives Theorem 4.1.

### 8.3 Hanging parts are uncontrolled

If the minimal core \(R\) is a proper subtree of the contracted tree
\(T\), the canonical colouring of \(R-e\) need not extend through
\(T-R\).  Arbitrary portal trees can be attached outside \(R\) without
changing its minimal obstruction.  Therefore neither Theorem 4.1 nor the
portal-Helly synthesis can be asserted for a selected proper core.

The next required theorem is a **core exchange theorem**: optimize over all
minimal contraction cores and prove that a portal-bearing hanging lobe can
replace a matched leaf, or else its attachment is an ambient adhesion whose
opposite operation states agree.  No such theorem is proved here.

## 9. Exact contribution and remaining gap

The proved uniform output is

\[
\boxed{
\begin{array}{c}
\text{portal split;}\\
\text{or a low-degree centred portal-Helly owner gate;}\\
\text{or a label-preserving clean rotation;}\\
\text{or a named foreign-bag transit or apex hit;}\\
\text{or an alternating }\alpha\delta\text{ owner corridor}\
\text{with an apex-pinned minor-transition state at every}\ \delta\text{-edge.}
\end{array}}
\tag{9.1}
\]

This combines the whole-tree list expansion, portal-tree Helly, and the
opposite-edge transition gate without identifying model labels with list
colours.  The anti-portal rule remains respected throughout.

To turn (9.1) into the full rooted-model principle, two points remain.

1. **Core exchange:** force the full-core hypothesis dynamically, or absorb
   every portal-bearing hanging lobe.
2. **Multi-complex-bag allocation:** when a bypass first hits another
   nonsingleton bag, distribute the resulting carriers without destroying
   that bag's labelled portals.  Section 11 solves the spanning singleton
   corridor, while Section 12 leaves only a clean-rotation outcome in the
   nonspanning singleton case.

The fixed-model counterexample shows that one contraction state cannot do
either job.  The all-edge minor-transition family and contact maximality are
the genuinely new data still available for closing them.

## 10. Gallai-society extension

The singleton-gate argument is not restricted to tree blocks.  We record
the exact extension because it identifies the non-tree residue.

Let \(S\) be a connected induced society contracted to one vertex in a
colouring \(c\).  Assume \(S\cap N_G(v)\ne\varnothing\), write \(\alpha\)
for the contraction colour and \(\delta=c(v)\), so
\(\alpha\ne\delta\).  Suppose \(S\) itself is a minimal unexpandable
equality core: \(|L(x)|=d_S(x)\) for every \(x\).  Then \(S\) is a Gallai tree.  Use
its standard block palettes \(C_K\): clique blocks have a common palette of
size \(|K|-1\), odd-cycle blocks have a common two-colour palette, and at a
cutvertex the incident block palettes are pairwise disjoint and their union
is its list.

### Theorem 10.1 (Gallai cutvertices have one non-apex side)

Let \(q\) be a cutvertex of \(S\).  If two incident blocks \(K,L\) both
satisfy

\[
                        C_K-\{\delta\}\ne\varnothing,
                \qquad C_L-\{\delta\}\ne\varnothing,     \tag{10.1}
\]

then the corresponding block lobes are joined in \(H-q\).  A shortest such
path gives a model-clean block bypass or a named foreign-bag transit.

Consequently, in a bypass-free, transit-free equality core, every cutvertex
belongs to at most two blocks.  If it belongs to two, one of them has the
singleton palette \(\{\delta\}\).

#### Proof

Choose edges \(e=qx\in E(K)\) and \(f=qy\in E(L)\), and choose
\(\theta\in C_K-\{\delta\}\), \(\eta\in C_L-\{\delta\}\).  The aligned
Gallai transition construction colours \(S-e\) with \(q,x\) both
\(\theta\), and colours \(S-f\) with \(q,y\) both \(\eta\); it agrees with
\(c\) outside \(S\) in both cases.  For a clique block, prescribe the common
endpoint colour and use the other block colours bijectively.  For an odd
cycle, delete the edge and swap the two colours on the resulting even path
if necessary.  The usual outward block-tree extension then colours every
other block.  Hence these are proper colourings of \(G-e,G-f\).

At the singleton adhesion \(\{q\}\), both marked states are the unique
one-block state and are unpinned.  Opposite block lobes therefore cannot be
different components of \(H-q\), by crossed transition splicing.  The
clean/foreign conclusion follows as in Lemma 3.2.

In a rigid core, at most one incident block palette can contain a colour
different from \(\delta\).  Every other nonempty palette would have to be
\(\{\delta\}\).  Incident block palettes are pairwise disjoint, so there is
at most one such block.  This gives the final assertion. \(\square\)

### Corollary 10.2 (surplus, bypass, or an \(\alpha/\delta\) Gallai web)

For an arbitrary whole minimal induced contraction core \(S\), at least one
of the following holds.

1. Some vertex has strict internal list surplus
   \(d_S(x)>|L(x)|\).
2. A cutvertex gate has a model-clean bypass or a named foreign transit.
3. Equality holds everywhere, and after suppressing the internally
   two-connected \(\alpha\)-blocks, all remaining block-tree edges are
   \(K_2\)-blocks with palette \(\{\delta\}\).

#### Proof

Minimality always gives \(|L(x)|\le d_S(x)\).  A strict inequality is
outcome 1.  In the equality case the degree-choosability theorem makes
\(S\) a Gallai tree.  Apply Theorem 10.1 at every cutvertex.  If it ever
returns a bypass/transit, obtain outcome 2.  Otherwise the
\(\alpha\)-block cover and the argument in the following paragraph give
outcome 3. \(\square\)

Thus the non-tree equality residue is an \(\alpha\)-block Gallai web joined
through isolated \(\delta\)-palette bridges.  Indeed, because \(\alpha\)
belongs to every vertex list and incident palettes are disjoint, the blocks
whose palettes contain \(\alpha\) are vertex-disjoint and cover all
vertices.  At a vertex of any other block, its incident \(\alpha\)-block
already supplies a non-\(\delta\) palette; Theorem 10.1 forces the other
palette to be \(\{\delta\}\), so that block is a \(K_2\).  Arbitrary
branching at a
cutvertex is eliminated.  Branching can remain only inside a clique or
odd-cycle block at distinct cutvertices.  Closing those block hubs, and
exchanging a proper core through portal-bearing hanging parts, are the two
non-tree versions of the pinned-corridor gap.

## 11. The end-locked path closes in the spanning singleton cell

The alternating residue is completely eliminable when every other model bag
is a singleton and there are no unused vertices outside the complex bag.
This is the first full infinite cell closed by the dynamic principle.

Assume

\[
 V(H)=V(T)\mathbin{\dot\cup}\{b_1,\ldots,b_{r-1}\},       \tag{11.1}
\]

where the \(b_i\) form a clique and
\((T,\{b_1\},\ldots,\{b_{r-1}\})\) is the fixed model.  Retain the quotient
colouring

\[
 c(T)=\alpha,qquad c(b_i)=p_i,qquad c(v)=p_j=\delta.   \tag{11.2}
\]

Write \(P_i=N_T(b_i)\) and \(F=N_T(v)\).
Assume throughout this section that \(|F|\ge2\), as in the double-foot
application.

### Theorem 11.1 (spanning singleton corridor closure)

If \(T\) is the full alternating path in (4.6), then \(G\) contains a
\(K_{r+1}\)-minor.

#### Proof

The expansion lists have no shadow terms:

\[
 L(x)=\{\alpha\}\cup
 \{p_i:x\notin P_i\text{ and }(i\ne j\text{ or }x\notin F)\}.             \tag{11.3}
\]

By Corollary 6.3, every internal path vertex has list
\(\{\alpha,\delta\}\), both ends have list \(\{\alpha\}\), and the two
ends are precisely the feet.  Equation (11.3) now gives

\[
 \begin{array}{ll}
 \text{every vertex of }T\text{ lies in }P_i,& i\ne j;\\
 P_j\subseteq\{\text{the two ends of }T\},&P_j\ne\varnothing.
 \end{array}                                             \tag{11.4}
\]

Suppose first that \(|T|\ge4\).  Choose an end \(a\in P_j\), and denote
the other end by \(b\).  The three sets

\[
       C_1=\{a,b_j\},\qquad
       C_2=\{b,v\},\qquad
       C_3=V(T)-\{a,b\}                                  \tag{11.5}
\]

are nonempty, connected, and pairwise adjacent: use respectively the two
end edges of the path and the edge \(av\).  By (11.4), each is adjacent to
every singleton \(b_i\), \(i\ne j\); for \(C_1\), the clique edges from
\(b_j\) provide the same conclusion as well.  Therefore

\[
 C_1,C_2,C_3,\{b_i\}\ (i\ne j)                           \tag{11.6}
\]

are the \(r+1\) branch sets of a clique model.

It remains that \(T=ab\) is one matching edge.  If both ends lie in
\(P_j\), the two singleton sides of \(T-ab\) meet every portal class, and
the usual alpha-bridge construction gives a \(K_{r+1}\)-model.

Assume exactly one end lies in \(P_j\).  If \(b_j\) is the only noncontact
singleton, then \(v\) is adjacent to every \(b_i\), \(i\ne j\), and

\[
                 \{v\},\quad\{a,b_j\},\quad\{b\},
                 \quad\{b_i\}\ (i\ne j)                 \tag{11.7}
\]

is a \(K_{r+1}\)-model.  If another singleton \(b_k\) is noncontact, colour
the quotient \(G/T\) with \(v\) receiving \(p_k\).  Both ends belong to
\(P_k\) by (11.4), so the selected \(k\)-portal crosses the matching edge.
For every other colour, endpoint Kempe connectivity across the deleted
matching edge gives the ordinary two-sided portals; equivalently apply the
alpha-bridge contact dichotomy with selected label \(k\).  Its
portal-crossing outcome is a \(K_{r+1}\)-model.  This finishes the final
case. \(\square\)

The construction (11.5) is the missing rooted-triangle mechanism: instead
of trying to make the selected singleton and the apex adjacent, attach each
to a different end and use the nonempty internal path as the third branch
set.  No simultaneous disjointness of Kempe paths is asserted or needed.

### Audit boundary

The spanning hypothesis is doing exact work.  With unused vertices, a
colour \(p_i\) missing from an internal list can be supplied by a shadow
vertex of colour \(p_i\), rather than by the labelled singleton \(b_i\).
Then (11.4) fails and the three bags in (11.5) need not see \(b_i\).  The
next theorem must turn such a shadow into a labelled portal or an ambient
adhesion; endpoint Kempe connectivity alone does not identify it.

## 12. Shadow-to-portal or faithful adhesion beyond the spanning cell

We now retain the full end-locked path and double-foot setup of Section 11
but allow unused vertices.  All bags other than \(T\) are still the
singleton clique

\[
                              S=\{b_1,\ldots,b_{r-1}\}.   \tag{12.1}
\]

Put

\[
                              U=H-(V(T)\cup S).           \tag{12.2}
\]

The following lemma is label-wise and requires no simultaneous choice of
Kempe paths.

### Theorem 12.1 (single-shadow absorption/rotation/adhesion)

Fix an ordinary model label \(i\ne j\), and let \(x\in V(T)-P_i\).  (For
the end-locked path, \(p_i\notin L(x)\).)  In the
quotient colouring, choose a neighbour \(s\in U\) of \(x\) with
\(c(s)=p_i\), and let \(C\) be the component of \(U\) containing \(s\).
At least one of the following holds.

1. **Shadow-to-portal absorption.**  The component \(C\) has an edge to
   \(b_i\).  Replacing \(\{b_i\}\) by \(C\cup\{b_i\}\) preserves the
   labelled clique model and creates an actual \(i\)-portal at \(x\).
2. **Clean transit rotation.**  The component \(C\) has neighbours at two
   distinct vertices of \(T\).  A path through \(C\) between two such
   attachments is a model-clean bypass and gives a label-preserving
   rotation of the transit bag.
3. **Faithful adhesion.**  We have

   \[
        N_T(C)=\{x\},\qquad C\not\sim b_i,               \tag{12.3}
   \]

   and

   \[
        X_C=N_H(C)=\{x\}\cup Q_C,qquad
        Q_C\subseteq S-\{b_i\},qquad |X_C|\le r-1.      \tag{12.4}
   \]

   Thus \((C\cup X_C,H-C)\) is an actual ambient separation, the shadow
   shore omits its own labelled singleton \(b_i\), and its only transit-tree
   gate is the named vertex \(x\).

#### Proof

The missing colour \(p_i\) in \(L(x)\) must occur on an external neighbour.
If that neighbour is not the singleton \(b_i\), it may be chosen in \(U\)
as stated.

If \(C\sim b_i\), then \(C\cup\{b_i\}\) is connected, remains disjoint
from every other branch bag, and retains all clique edges at \(b_i\).
The edge \(xs\) makes it adjacent to \(T\), proving outcome 1.

If \(C\) has two distinct tree attachments, connect corresponding
neighbours inside \(C\).  The resulting \(T\)-path has interior in the
unused component and hence avoids every old bag.  Adding it to \(T\) and
deleting an edge of the old tree interval is outcome 2.

We may therefore assume neither outcome.  The component \(C\) has the one
tree attachment \(x\) and is anticomplete to \(b_i\).  Since \(C\) is a
component of (12.2), every other neighbour lies in \(T\cup S\).  This gives
(12.4), and the bound follows from
\(|S-\{b_i\}|=r-2\). \(\square\)

### Corollary 12.2 (one shadow component gives near-complete portals)

Suppose, for a fixed ordinary label \(i\), all \(p_i\)-coloured unused
neighbours of \(T\) lie in one component \(C_i\) of \(U\).  If neither
absorption nor a clean rotation occurs, then

\[
                              |V(T)-P_i|\le1,             \tag{12.5}
\]

and the unique possible missed portal vertex is the tree gate of the
faithful adhesion (12.4).

#### Proof

Every vertex outside \(P_i\) has a \(p_i\)-coloured unused neighbour by
the expansion-list equation.  Hence it belongs to \(N_T(C_i)\).  Outcome 2
of Theorem 12.1 excludes two distinct such vertices. \(\square\)

### Corollary 12.2A (connectivity kills a nonabsorptive shadow)

If \(H\) is \(r\)-connected, outcome 3 of Theorem 12.1 is impossible.
In particular, in the \(HC_7\) application \(r=6\) and the inherited
six-connectivity of \(H=G-v\) eliminates every nonabsorptive,
single-attachment shadow component.

#### Proof

The far side contains \(b_i\), while the shadow component is nonempty.
Equation (12.4) is a separation of order at most \(r-1\). \(\square\)

### Corollary 12.3 (the adhesion carries a common double-operation state)

In outcome 3, let \(g=xs\), and let \(e\) be a tree edge not incident with
\(x\).  The edges \(e,g\) are vertex-disjoint and lie on opposite shores of
the separation (12.4).  Contracting both and colouring the proper minor
gives one common colouring of \(G-\{e,g\}\).  Therefore the
double-operation repair exclusion applies: either a side has an
operated-edge bichromatic detour (giving a clean rotation/rerouting or a
named dirty hit), or a no-repair side has two
gate-reaching endpoint components in every remaining colour layer.

Thus (12.4) is not merely a static cut.  It is precisely an ambient adhesion
on which opposite operation transitions share a marked state after the
canonical simultaneous contraction.

#### Proof

The edge \(g\) belongs only to the \(C\)-shore because \(s\in C\) and
\(x\in X_C\).  The tree edge \(e\), chosen away from \(x\), belongs only to
the opposite shore.  All assertions are now the double-operation repair
and Kempe-lock theorems. \(\square\)

The qualification on \(e\) is harmless for an end-locked path of at least
four vertices.  The two-vertex core is a separate bounded base.

### Theorem 12.4 (one shadow component per colour closes every long path)

Assume that, for each ordinary label \(i\ne j\), all \(p_i\)-coloured
unused neighbours of \(T\) lie in one component of \(U\).  If

\[
                              |T|\ge6,                    \tag{12.6}
\]

then either the transit bag has a clean rotation or \(G\) contains a
\(K_{r+1}\)-minor.

#### Proof

If a colour component attaches at two missed portal vertices, Theorem 12.1
gives a clean rotation.  Otherwise Corollary 12.2 gives

\[
                              |V(T)-P_i|\le1
                         \quad(i\ne j).                  \tag{12.7}
\]

Let the path be \(x_0x_1\ldots x_{n-1}\), choose
\(a=x_0\in P_j\), and put \(b=x_{n-1}\).  The selected portal exists and,
by the end-locked list equation, lies at an end.  Define

\[
 \begin{aligned}
 D_1&=\{a,b_j\},\\
 D_2&=\{v,b,x_{n-2}\},\\
 D_3&=\{x_1,\ldots,x_{n-3}\}.
 \end{aligned}                                           \tag{12.8}
\]

These sets are nonempty and connected.  They are pairwise adjacent through
\(av\), \(x_0x_1\), and \(x_{n-3}x_{n-2}\), respectively.  The first set
sees every ordinary singleton through the clique edges at \(b_j\).  The
second contains two tree vertices, and the third contains at least three;
(12.7) therefore makes both adjacent to every \(b_i\), \(i\ne j\).
Consequently

\[
                    D_1,D_2,D_3,\{b_i\}\ (i\ne j)       \tag{12.9}
\]

are \(r+1\) pairwise adjacent disjoint connected bags. \(\square\)

No simultaneous allocation of shadow components is used in this proof.
Their only role is to force the one-missed-portal bound (12.7); the final
minor uses the original singleton bags.  The exact bounded residue of the
one-component-per-colour case is therefore \(|T|\in\{2,4\}\).

### A sharp length-four static residue

The bound \(|T|\ge6\) in Theorem 12.4 cannot be replaced by a purely
static near-complete-portal argument.  Let

\[
                         T=a x_1 x_2 b
\]

and take four singleton labels \(j,q_1,q_2,q_b\) forming a clique.  Add
\(v\) adjacent to \(a,b\), and put

\[
 \begin{array}{c|c}
 \text{label}&\text{neighbours in }T\\ \hline
 j&\{a\}\\
 q_1&\{a,x_2,b\}\\
 q_2&\{a,x_1,b\}\\
 q_b&\{a,x_1,x_2\}.
 \end{array}                                             \tag{12.10}
\]

Thus the three ordinary labels miss respectively \(x_1,x_2,b\).  Add one
unused leaf at each missed vertex and give it the corresponding label
colour.  Every ordinary colour has one shadow component and every portal
set misses at most one tree vertex, but the displayed graph has no
\(K_6\)-minor.  The three leaves are irrelevant to clique minors, and an
exhaustive connected-branch-set check on the nine-vertex leafless core
certifies the assertion; see
`verify_length4_nearcomplete_counterarchitecture.py`.

This graph is deliberately not minor-critical: its shadow leaves have
one-vertex neighbourhoods.  Corollary 12.2A shows exactly which missing
dynamic hypothesis kills it in an \(HC_7\) counterexample.  The example
therefore falsifies the overstrong claim “one missed portal per label
already splits a four-vertex corridor,” while leaving the
shadow-to-adhesion theorem intact.

### Theorem 12.5 (connected shadow allocation closes the corridor)

Assume \(H\) is \(r\)-connected.  Then every end-locked path gives either
a clean transit rotation or a \(K_{r+1}\)-minor.  No
one-component-per-colour hypothesis is needed.

#### Proof

Assume there is no clean rotation.  Every component \(C\) of \(U\) which
has a neighbour in \(T\) consequently has a unique attachment vertex;
write it \(\tau(C)\).  Indeed, two distinct attachments give outcome 2 of
Theorem 12.1.

Fix an ordinary label \(i\ne j\) and a missed portal
\(x\in V(T)-P_i\).  Its required \(p_i\)-coloured shadow neighbour lies in
some component \(C\) with \(\tau(C)=x\).  If \(C\not\sim b_i\), outcome 3
of Theorem 12.1 is a separation of order at most \(r-1\), contrary to the
connectivity of \(H\).  Hence

\[
\boxed{\text{every shadow component at a missed }i\text{-portal is
 adjacent to }b_i.}                                    \tag{12.11}
\]

First suppose \(T=ab\).  Assign every unused component with a tree
attachment to that unique endpoint, and enlarge \(\{a\},\{b\}\) by their
assigned components; call the resulting connected, disjoint sets \(A,B\).
Equation (12.11) makes both sets adjacent to every ordinary singleton
\(b_i\), \(i\ne j\).  Choose the notation so that \(a\in P_j\).  If
\(b\in P_j\) as well, then

\[
                         A,B,\{b_1\},\ldots,\{b_{r-1}\} \tag{12.12}
\]

already form a \(K_{r+1}\)-model.

Otherwise delete

\[
                         \{a\}\cup(S-\{b_j\}),           \tag{12.13}
\]

a set of order \(r-1\).  Connectivity gives a path in the remaining graph
from \(b\) to \(b_j\).  Since \(bb_j\) is not an edge, the path first enters
an unused component.  Distinct components of \(U\) have no edges between
them, and (12.13) removes the other possible transit vertices, so one
component attached at \(b\) has an edge to \(b_j\).  It was assigned to
\(B\), making \(B\sim b_j\).  Hence (12.12) is again the desired model.

We may now assume \(|T|\ge4\).

Partition the path into its first end \(a\in P_j\), its other end \(b\),
and the nonempty internal path.  For each part, absorb **all** unused
components whose unique attachment lies in that part.  Call the resulting
three connected sets \(A_1,A_2,A_3\), in the same order.  They are disjoint,
and the two path end edges retain their consecutive adjacencies.

For every ordinary singleton \(b_i\), each \(A_k\) is adjacent to \(b_i\).
Indeed, choose a tree vertex \(x\) in the underlying part.  If
\(x\in P_i\), use its portal edge.  Otherwise use its shadow component,
which belongs to \(A_k\) and meets \(b_i\) by (12.11).  This argument is
label-wise but the allocation is simultaneous because unused components
are assigned once, according to their unique tree attachment; a component
shared by several colours supplies all of those adjacencies from the same
branch set.

Finally enlarge

\[
                         A_1\longmapsto A_1\cup\{b_j\},
             \qquad     A_2\longmapsto A_2\cup\{v\}.     \tag{12.14}
\]

The first enlargement is connected through the selected portal at \(a\),
and the second through the foot at \(b\).  The two enlarged sets and
\(A_3\) are pairwise adjacent, the first two through \(av\) and the latter
two through the path end edges.  By the preceding paragraph all three see
every \(b_i\), \(i\ne j\).  Together with those \(r-2\) singleton bags they
form a \(K_{r+1}\)-model. \(\square\)

For \(HC_7\), the hypotheses are exactly \(r=6\) and the inherited
six-connectivity of \(H\).  Hence every full-core, one-complex-bag
end-locked path is closed **modulo a clean rotation**, even with arbitrarily
many unused shadow vertices and arbitrarily shared shadow components.  A
global potential or core-exchange theorem is still needed to show that such
rotations terminate in the minor outcome.

### Why the static forcing family does not survive

In the family \(F_r\) from Section 8, the same-colour forcing vertices are
joined through the unused \(\alpha\)-vertex of the reference clique.  Their
unused component therefore attaches to several vertices of the transit
path.  It falls into outcome 2 of Theorem 12.1: the common forcing gadget is
a clean bypass.  This is exactly the dynamic operation which the static
fixed-model audit omitted.  If the forcing vertices are split into
one-attachment components to forbid that bypass, each becomes the faithful
adhesion (12.4), where simultaneous opposite-edge contraction activates the
transition gate.

### Simultaneous-disjointness audit

Corollary 12.2 is deliberately label-wise.  Components \(C_i\) for
different colours may coincide, cross, or attach through the same gate; the
absorbed bags \(C_i\cup\{b_i\}\) need not be disjoint.  Therefore it is
false to infer simultaneous near-complete labelled bags from the individual
alternatives.

A concrete minimal obstruction is obtained from two labels \(i,k\).  Take
an unused path \(u_i-w-u_k\), colour its ends \(p_i,p_k\), colour \(w\)
with a third colour, join both ends to the same tree vertex \(x\), and join
\(w\) to both \(b_i,b_k\).  The whole path is one unused component with the
single tree attachment \(x\).  It may be absorbed with \(b_i\), or with
\(b_k\), but the two absorptions share all three unused vertices and cannot
be performed simultaneously with disjoint branch sets.  (All displayed
edges are proper in the named colouring.)

Theorem 12.1 outputs the correct alternatives one label at a time;
any multi-label upgrade needs a Hall/Rado allocation of unused components,
or else must use the common adhesion state of Corollary 12.3.

## 13. Connectivity absorbs every shadow in the one-complex-bag model

There is a simpler global interpretation of Theorem 12.5.  At the
connectivity threshold used there, a model with only one nonsingleton bag
can always be made spanning in one step.

### Theorem 13.1 (spanning enlargement)

Let \(H\) be \(r\)-connected and suppose

\[
                         (B,\{b_1\},\ldots,\{b_{r-1}\}) \tag{13.1}
\]

is a \(K_r\)-model.  Then \(H-S\) is connected for
\(S=\{b_1,\ldots,b_{r-1}\}\), and

\[
                         (H-S,\{b_1\},\ldots,\{b_{r-1}\}) \tag{13.2}
\]

is a spanning \(K_r\)-model.  Enlarging \(B\) to \(H-S\) preserves every
old contact and may only add contacts.

#### Proof

Deleting the \(r-1\) vertices of \(S\) cannot disconnect the
\(r\)-connected graph \(H\).  The connected graph \(H-S\) contains the old
bag \(B\), is disjoint from the singleton bags, and retains every old edge
from \(B\) to a singleton.  The singleton bags still form a clique, proving
(13.2).  The contact assertion is immediate from containment. \(\square\)

For \(HC_7\), \(r=6\) and \(H\) is six-connected, so this theorem applies
exactly.  Therefore unused shadows are not a permanent obstruction in the
one-complex-bag route: they can all be absorbed into the complex bag.  The
remaining issue is internal **core exchange** inside that spanning bag.  A
minimal unexpandable Gallai/list core may be a proper subgraph and may omit
essential feet or singleton portals.  Sections 11--12 solve the case in
which the spanning bag itself is the full core; Theorem 13.1 shows that
proper-core exchange, rather than external shadow routing, is the sole
remaining obstruction in the one-complex-bag cell.

## 14. A full-core-free finite-state transit theorem

The preceding canonical arguments use the full-core hypothesis in order to
name every edge state explicitly.  There is, however, a coarser transition
principle which needs no list core, no Gallai decomposition, and no selected
contraction colouring.  It applies to every edge of every branch bag.

Let \(X\subseteq V(H)\).  If \(d\) is an \(r\)-colouring of \(G-e\), define
its marked equality state on \(X\) by

\[
 \sigma_X(d)=\text{the equality partition induced by \(d\) on }
                    X\cup\{v\},                         \tag{14.1}
\]

where \(v\) is distinguished.  Equivalently, this is the pair in (3.1):
the equality partition of \(X\), together with the (possibly empty) block
whose colour is \(d(v)\).  Thus the number of abstract states is

\[
                              b_{|X|+1},                 \tag{14.2}
\]

the \((|X|+1)\)-st Bell number.

For a component \(C\) of \(H-X\), let \(\Omega_X(C)\) be the set of marked
states obtained as follows.  Choose an edge \(e\) having at least one end in
\(C\), both ends in \(C\cup X\), and no end in another component of \(H-X\);
then choose any \(r\)-colouring of \(G-e\).  We call such an \(e\) a
\(C\)-operation.  Proper-minor minimality makes every such spectrum nonempty
whenever a \(C\)-operation exists.

### Theorem 14.1 (disjoint state spectra across a separator)

If \(C,D\) are distinct components of \(H-X\), then

\[
                         \Omega_X(C)\cap\Omega_X(D)
                         =\varnothing.                  \tag{14.3}
\]

Consequently at most \(b_{|X|+1}\) components of \(H-X\) contain an
operation.  In particular, if every component has a neighbour in \(X\),
then

\[
                         c(H-X)\le b_{|X|+1}.            \tag{14.4}
\]

#### Proof

Suppose that a \(C\)-operation \(e\), a \(D\)-operation \(f\), and
colourings \(d_e,d_f\) of \(G-e,G-f\), respectively, induce the same state
on \(X\cup\{v\}\).  Partition the components of \(H-X\) into two shores,
putting \(C\) on the first and \(D\) on the second.  The edge \(e\) belongs
only to the first shore and \(f\) only to the second.

Equality of the two marked partitions means that a permutation of the
\(r\) colours makes \(d_e\) and \(d_f\) agree on all of \(X\cup\{v\}\).
After making this permutation, use \(d_f\) on the first shore and \(d_e\)
on the second.  The first restriction is proper on \(e\), because only
\(f\) was deleted from its source graph; symmetrically, the second is proper
on \(f\).  The restrictions agree on \(X\cup\{v\}\), there are no edges
between the open shores, and all edges from \(v\) are checked in their
source colouring.  They therefore splice to an \(r\)-colouring of \(G\), a
contradiction.  This proves (14.3).  The state count gives the remaining
assertions. \(\square\)

The estimate is intentionally a state-capacity statement, not a
connectivity statement.  Its useful rooted-model form concerns components
which are separated only inside a model-clean region.

### Corollary 14.2 (clean lobes: bounded capacity or foreign transit)

Fix a labelled clique model and one branch bag.  Let \(F\) be the union of
the other, foreign, branch bags, and let \(R\) be the component of \(H-F\)
containing the selected bag.  For \(X\subseteq V(R)\), suppose that
\(L_1,\ldots,L_m\) are components of \(R-X\), each joined to \(X\) by an
edge.  Then either

1. \(m\le b_{|X|+1}\); or
2. two of the \(L_i\) are joined in \(H-X\) by a path meeting \(F\).

More precisely, if no path in \(H-X\) between distinct clean lobes meets a
foreign bag, their nonempty state spectra are pairwise disjoint.

#### Proof

For each \(L_i\), an edge from \(L_i\) to \(X\) is an operation.  If two
spectra meet, Theorem 14.1 says that the corresponding lobes cannot be
distinct components of \(H-X\).  A path joining them in \(H-X\) cannot lie
in \(R-X\), by the definition of the \(L_i\), and it cannot leave the
component \(R\) of \(H-F\) without meeting \(F\).  Thus it is a named
foreign transit.  In its absence the spectra are disjoint, and (14.2)
gives the bound. \(\square\)

For a singleton gate the complete state space has only two elements.  This
case is considerably sharper than the Bell-number formulation suggests.

For an edge \(e=qx\), let

\[
 \tau_q(d,e)=
 \begin{cases}
 1,&d(q)=d(v),\\
 0,&d(q)\ne d(v),
 \end{cases}                                             \tag{14.5}
\]

where \(d\) is any \(r\)-colouring of \(G-e\).  Because \(G\) itself is not
\(r\)-colourable, the ends \(q,x\) necessarily have the same colour in
every such \(d\); otherwise \(d\) would also colour the restored edge.
Thus (14.5) says exactly whether the forced defect colour is apex-pinned.

### Corollary 14.3 (the two-shore capacity--state gate)

Let \(q\in V(R)\), with \(R,F\) as in Corollary 14.2.  If there is no named
foreign transit between components of \(R-q\), then:

1. \(R-q\) has at most two components;
2. if it has two components \(L_0,L_1\), every edge \(qx\) with
   \(x\in L_i\), in every \(r\)-colouring of \(G-qx\), has one forced bit
   \(\varepsilon_i\), and
   \(\{\varepsilon_0,\varepsilon_1\}=\{0,1\}\).

#### Proof

The two singleton marked states are precisely the two values in (14.5).
Every component of \(R-q\) has an edge to \(q\), because \(R\) is connected.
Corollary 14.2 therefore bounds their number by two.

If \(L_0,L_1\) are the two components, take the union of the state spectra
of all incident-edge operations in each lobe.  These are nonempty, disjoint
subsets of the two-element state space.  They must consequently be the two
opposite singleton sets. \(\square\)

This is a uniform, full-core-free version of the locked two-shore gate.  It
does not merely select convenient deletion colourings: in the rigid case it
forces **every** deletion witness on one shore to be pinned and **every**
witness on the other to be unpinned.

### Theorem 14.4 (binary collapse on an arbitrary transit tree)

Let \(T_0\) be any tree contained in the selected clean region \(R\).  For
each \(e\in E(T_0)\), choose an arbitrary \(r\)-colouring \(d_e\) of \(G-e\)
and give \(e=xy\) the bit

\[
                 \tau(e)=1\quad\Longleftrightarrow\quad
                 d_e(x)=d_e(y)=d_e(v).                  \tag{14.6}
\]

Then at least one of the following occurs.

1. A vertex \(q\) of \(T_0\) has two incident tree lobes joined by a
   \(q\)-avoiding path in the clean region \(R\).  The path is an ambient
   bypass and permits a spanning-tree rotation while retaining every old
   branch-bag vertex and every old portal.
2. Two such lobes have a \(q\)-avoiding path whose first exit from \(R\)
   meets a named foreign branch bag.
3. \(T_0\) is a path and its chosen edge bits alternate \(0,1,0,1,\ldots\).

#### Proof

If some \(q\) has degree at least three in \(T_0\), two incident edges have
the same bit.  Their other ends lie in two tree lobes.  Applying the direct
splicing argument of Theorem 14.1 with adhesion \(\{q\}\) shows that the
lobes are joined in \(H-q\).  A shortest joining path either stays in \(R\),
giving outcome 1 (take two consecutive visits to \(T_0\) and exchange the
old tree path for that segment), or has a first visit to \(F\), giving
outcome 2.

In the absence of outcomes 1 and 2, \(\Delta(T_0)\le2\), so \(T_0\) is a
path.  If two consecutive edges had the same bit, the identical singleton
argument at their common end would again give outcome 1 or 2.  Consecutive
bits therefore alternate. \(\square\)

### Exact limitation

Theorem 14.4 removes the full-core assumption from the **geometric
collapse**, but it does not by itself terminate outcome 1.  A bypass using
new clean vertices enlarges the selected bag and is monotone.  A bypass
already contained in a 2-connected part of the bag may merely exchange one
spanning tree for another.  To turn the theorem into the desired rooted
model principle one still needs one of the following genuinely new steps:

* a potential which makes every clean basis exchange terminate;
* an owner theorem saying that a terminal-minimal 2-connected block can
  absorb or split every alternating state corridor; or
* a contact-or-small-adhesion theorem which converts a terminal exchange
  failure into a colour-gluable separator.

What is now proved is that all branching outside such a 2-connected owner
block is finite-state.  At every singleton articulation there are at most
two clean shores, and in the two-shore case their entire deletion-witness
families are forced to opposite apex states.  This is the precise uniform
interface on which a web exchange or portal-owner theorem has to act.
