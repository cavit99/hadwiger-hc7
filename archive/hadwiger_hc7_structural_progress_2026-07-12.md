# HC7 structural progress after the simultaneous-star breakthrough

## Status

This package does **not** prove \(HC_7\).  It records the theorem-level
progress which survived independent audit, and separates it from finite
discovery probes and from the remaining conjectural exchanges.

## 1. Uniform simultaneous-star theorem

Let every proper minor of a non-\(k\)-colourable graph \(G\) be
\(k\)-colourable.  If \(uv\in E(G)\) and a set

\[
 W\subseteq N(u)\cap N(v)
\]

is the disjoint union of two nonempty independent sets, then

\[
\begin{array}{ll}
 |W|\le d-k+2,&d(u)=d(v)=d,\\
 |W|\le\max\{d(u),d(v)\}-k+1,&d(u)\ne d(v).
\end{array}
\]

The proof contracts both independent stars in one minor, deletes the two
centres before expanding the independent leaves, and uses the exact Hall
condition for the two residual colour lists.  This is audited in
`hadwiger_simultaneous_star_adversarial_audit.md`.

For a \(t\)-connected, \(K_t\)-minor-free, minor-minimal
non-\((t-1)\)-colourable graph, an edge with endpoint degrees \(t\) and
at most \(t+1\) consequently has at most \(t-3\) common neighbours; at
equality all common-set nonedges form a nonempty star.  This is a uniform
general-\(t\) consequence, although it does not prove Hadwiger.

## 2. Pure-Moser consequences

For a degree-seven vertex \(v\) with pure-Moser neighbourhood, let \(h\)
be its unique four-contact hub.

1. The simultaneous-star theorem gives \(d(h)\ge9\).
2. For every value of \(d(h)\), the residual colour classes at \(h\)
   are four-saturating after the double-star contraction.  Strong HC4
   therefore gives a \(K_4\)-model rooted in neighbours of \(h\) outside
   the two stars; adding \(\{h\}\) gives a controlled \(K_5\)-model.
3. If \(d(h)=9\), the four exterior hub neighbours are rainbow in every
   double-star colouring and completely pairwise Kempe-connected.
4. Still at degree nine, every exterior hub neighbour is complete to one
   of the two literal Moser edges.  Combining this portal theorem with
   the rooted \(K_4\) gives \(K_7\) except for a balanced lock with two
   left bags, two right bags, \(6\) trapped in one left bag, and \(5\)
   trapped in one right bag.
5. In a spanning rooted model, splitting either locked bag gives \(K_7\)
   unless its root component is missing a precise attachment class.  A
   cross-half contact gives \(K_7\) explicitly, so the component has
   exactly four fixed local neighbours.  Seven-connectivity then gives
   either an exact seven-adhesion or at least four actual protected
   portals across the gate.
6. With flexible portal endpoints, a vertex-capacitated linkage theorem
   turns the same-bag surplus into either the required cross-side peel or
   one literal bottleneck vertex.  The remaining non-adhesion outcome is
   a three-class bypass through the locked bag on the opposite side.
7. The bottleneck lobes themselves now satisfy a peel-or-transfer
   theorem.  Except for one root-bearing lobe containing every portal,
   they either give \(K_7\), an exact seven-cut, or transfer the lock to
   at least three distinct portals in the adjacent gate piece.
8. The two symmetric bypasses close immediately when they can be
   uncrossed into disjoint label-preserving connections.  With
   \(D_L=L_6-K_L\) and \(D_R=R_5-K_R\), the seven bags are

   \[
   \{v\},\{h\},\{1\},\{2\},
   D_L\cup K_R, K_L\cup D_R,
   \{3\}\cup L_0\cup R_0.
   \]

9. The label-preserving bypass and original exact-cut branches are now
   sharper.  Terminal-clean opposite paths give (K_7) even when they
   intersect; a width-five quotient shows why paths which consume the
   opposite terminal bag do not suffice.  A monotone two-carrier
   capacity exchange continues through every later exact
   seven-neighbourhood and terminates in (K_7) or the root-bearing
   lobe.  Separately, the
   *original* exact cut
   (\{q,h,1,2,3,4,6\}) from Theorem 4.6 is eliminated completely.
   If the ordinary-left root is on the far side, the model is immediate.
   If it is on the locked side, a root exchange handles any (3,4)
   contact in the (K)-component; otherwise retaining the old
   (L_6R_0,L_0R_5,L_0R_0) carrier edges gives the explicit model

   \[
   \{v\},\{h\},\{3\},\{4\},R_5,
   D_0\cup R_0, X\cup P\cup\{1\}.
   \]

10. The later exact equality from the portal-lobe transfer has a sharp
    dichotomy.  With boundary
    (\{h,1,2,6,q,d_1,d_2\}), a mixed split of (D) to its two right
    target classes gives an explicit (K_7)-model.  Failure forces the
    common transversal to be the literal vertex (6).  Absorbing the
    (d_1,d_2)-components then gives

    \[
      N(U)=\{h,1,2,6,q\}\mathbin{\dot\cup}P_Q,
      \qquad |P_Q|\ge2,
    \]

    with equality another exact seven-cut and strict surplus at least
    three.  A width-five construction retaining all old model edges and
    two distinct (P_Q)-portals realizes the equality statically.  The
    alternating exchange nevertheless continues with two portals, so
    this equality either grows again or terminates in the root-bearing
    (Q)-lobe.  Thus the next missing input is genuinely the terminal
    root-lobe order, not contact count, exactness, or carrier ownership.
11. The terminal lobe has now been sharpened again.  Writing
    (Q=J\cup S) across its bottleneck, a (Z)-(S) contact together
    with either a (J)-(D) or (J)-(\{3,4\}) contact gives an
    explicit (K_7)-model.  If those contacts are absent, the connected
    union (Z\cup J) has at most six external neighbours, contradicting
    seven-connectivity.  Hence (Z\not\sim S): every active portal is
    fully nested in (J).  The exact residual capacity is

    \[
       N(Z\cup J)=\{h,1,2,s\}\mathbin{\dot\cup}P_D
                    \mathbin{\dot\cup}C_{34},
       \qquad |P_D|+|C_{34}|\ge3.
    \]

    A Two Paths/web audit confirms that no portal-saturated
    (S)-side web survives; the remaining object is instead a nested
    double-root shore whose exits all point back into (D,3,4).

The proofs and audit are in
`hadwiger_degree9_hub_rainbow_rooted_k4.md`,
`hadwiger_degree9_hub_portal_lock.md`, and
`hadwiger_degreefree_hub_row5_audit.md`.  A width-five quotient proves
that the balanced lock cannot be eliminated from contracted contact data
alone.

## 3. Degree-nine three-shore obstruction

The only static exact-miss obstruction found in the three-component
degree-nine cell has miss sets

\[
 \{0,1\},\quad\{0,2\},\quad\{1,2\}.
\]

For this type:

1. Every cutvertex shore is eliminated.  Each lobe has at least six
   boundary contacts by seven-connectivity, and 87 independently checked
   contact states all contain an \(N(v)\)-meeting \(K_6\)-model.
2. Portal multiplicity therefore forces a connected double-root split.
3. A side with \(r<7\) contacts has \(7-r\) disjoint paths from all its
   missing labels to distinct opposite interface vertices.
4. In the sharp row-five state, absorbing either of the two paths gives
   the minor immediately if the complementary carrier retains six
   contacts.  Otherwise it exposes an exact seven-cut or a carrier with
   at least three attachments to the absorbed side.

The linkage alone is insufficient: a dependency-free verifier checks a
width-four counterarchitecture containing both prescribed paths.  Thus
the exact residue is a three-interface portal web plus boundary-state
alignment, not another static row enumeration.

Relevant files are `hadwiger_degree9_type2_cutvertex_closure.md` and
`hadwiger_degree9_row5_two_path_exchange.md`.

## 4. General interface and gluing machinery

In a \(k\)-connected graph, if a shore piece contacts \(r<k\) vertices
of a component boundary of order at least \(k\), there are \(k-r\)
vertex-disjoint paths from distinct unused boundary labels to distinct
opposite interface vertices.  The bound is sharp.

For a proper-minor-minimal non-\(q\)-colourable graph, the two sets of
boundary equality partitions at any separation form a minimal
incompatible pair: the original sets are disjoint, while every internal
minor transition makes them intersect.  A common partition glues if it
is represented by rooted clique models on both sides; a connected full
shore also realizes the exact trace of every independent boundary set.

An exact adhesion by itself is not color-gluable.  The missing uniform
step is precisely linkage-to-rooted-clique packaging, or a structural
classification of the incompatible equality states.  See
`hadwiger_uniform_interface_linkage_and_gluing.md`.

## 5. Independently certified component closures

In a hypothetical minimal \(HC_7\) counterexample:

* a degree-eight vertex has at most two components outside \(N[v]\);
* a degree-nine vertex has at most three components outside \(N[v]\).

The maximal-component cases are covered by explicit certificate lists
and short independent verifiers.  These close infinite component-count
families, but not the remaining lower-component degree-eight/nine cells.

## 6. Exact remaining gaps

The new work has not eliminated all degree-seven, degree-eight, or
degree-nine configurations.  The sharpest current subproblems are:

1. **Locked Moser gate:** the original Theorem 4.6 exact cut is closed,
   and the alternating exchange continues through every later exact
   seven-neighbourhood because two active portals suffice.  What remains
   is the fully nested root-bearing bottleneck lobe produced by that
   exchange (and its symmetric mate): it has no contact to the target
   side (S), and the double-root union (Z\cup J) has at least three
   exits into (D\cup\{3,4\}).  No boundary-state gluing is needed
   before that terminal state.
2. **Three-interface type-2 web:** peel a carrier with three attachments
   to six contacts, or uncross its essential portals into a color-gluable
   exact seven-adhesion.
3. **Higher-degree Moser hub:** exploit the degree-free rooted \(K_4\)
   when the four exterior roots are no longer the entire outside
   neighbourhood.
4. **Other degree cells:** finish the remaining one/two-component
   degree-eight and one/two/three-component degree-nine structures.

Until one of these mechanisms closes all relevant cells, \(HC_7\)
remains unproved.  The substantive change is that two major residues are
now expressed by the same reusable object: a full connected side, a
sharp connectivity-budget linkage, and either strict portal surplus or
an exact critical adhesion.
