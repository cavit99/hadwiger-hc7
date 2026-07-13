# Independent audit of the dark-bag split and its edge transition

## Verdict

The static structural chain through the potential-maximal lobe theorem is
sound:

* Theorem 3.3 (dark cluster/light donor): **GREEN**.
* Lemma 5.1 (mixed off-core lobe peel): **GREEN**.
* Lemma 6.1 (no mixed lobe at maximum potential): **GREEN**.

The final paragraph of Corollary 6.2 has two different assertions which
must not be conflated:

* every actual edge of the host is chromatically edge-critical: **GREEN**;
* the proposed “first edge” exists and represents the terminal-order lock
  in a form which a Kempe detour can repair: **RED**.

No valid argument currently turns failure of all repairs into a cut of at
most six vertices.  The exact missing input is branch-set-aligned avoidance,
not another path count.

## 1. Audit of Theorem 3.3

Let \(T=A\) (the other case is symmetric), and let \(U_T\) be the union
of all rooted bags anticomplete to \(A\).

1. The dark bags are pairwise adjacent branch sets, so their union is
   connected.
2. Neither \(h\) nor \(r\) belongs to a dark bag, since each sees both
   \(A\) and \(C\).  Thus \(d\) has no neighbour in \(U_T\).
3. The only boundary neighbours available to \(U_T\) are \(b,1,2\), and
   every other neighbour lies in a light rooted bag.  Hence
   \[
      N(U_T)\subseteq\{b,1,2\}\cup
      \bigcup_{K_j\notin\mathcal D_T}K_j.
   \]
4. A vertex of the excluded group \(A\) lies outside
   \(U_T\cup N(U_T)\), so \(N(U_T)\) is a genuine separator.
5. If each of the at most three light bags supplied at most one neighbour,
   this separator would have order at most six.  Seven-connectivity rules
   this out.

This proves both existence of a light donor and two **distinct actual
vertices** in it adjacent to the dark cluster.  The two edges may end in
different dark bags, exactly as the note states.

## 2. Audit of Lemma 5.1

For a component \(L\) of \(K_j-W\), the residual \(K_j-L\) is connected:
it contains connected \(W\), and every other component of \(K_j-W\)
has an edge to \(W\).  The selected terminals in \(W\) retain

* the prescribed \(b\)-root;
* the two other rooted-bag adjacencies;
* a \(K_0\)-edge; and
* every old group incidence of the donor.

If \(L\sim K_0\), then \(K_0\cup L\) is connected.  The two replacement
bags are disjoint, have the same union as before, and retain every pairwise
model adjacency.  The recipient gains the desired group contact.  Thus the
lemma is valid, including its spanning assertion.

## 3. Audit of Lemma 6.1

The potential

\[
 \Phi=\sum_i(\mathbf1[K_i\sim A]+\mathbf1[K_i\sim C])
\]

is maximized over a finite family of spanning rooted models with the same
four prescribed roots.  A mixed lobe transfer from Lemma 5.1 gives the
recipient one previously absent incidence, while the protected core keeps
all donor incidences.  No other summand falls.  Therefore \(\Phi\) rises
strictly, which is impossible.  The lemma and its pure-lobe consequence
are sound.

## 4. Why the “specified critical edge” is not yet specified

### 4.1 The proposed edge need not exist

In the unique-essential-portal outcome, the unique \(T\)-portal and the
retained \(K_0\)-portal may be the **same vertex**.  This is permitted,
for example when \(h\in K_j\) is both the sole \(A\)-contact of the bag
and an endpoint of a \(K_0K_j\)-edge.  The minimal route then has length
zero and has no first edge.

Even when the two portals are distinct, their minimal route may be the
single boundary edge \(hr\).  There is then no “first subsequent
boundary--shore edge” to which the fixed boundary atlas can be moved.

### 4.2 A path edge need not be a bag separator

A first edge on a shortest route need not separate the two portal types in
the donor.  A three-vertex triangle in the protected core already shows
this: choose the two terminal portals at two vertices and take their direct
edge.  Deleting it leaves the two-edge route through the third vertex.
Choosing a spanning tree of the core does not repair the inference, because
an edge of that chosen tree need not be a bridge of the induced donor bag.

Thus the edge is chromatically critical merely because every edge of the
minor-minimal non-six-colourable host is critical.  It has not been proved
to be structurally critical for the terminal order.

### 4.3 Atlas applicability is narrower than edge criticality

For an edge internal to \(O\), or for deletion of a boundary--\(O\) edge,
the boundary remains labelled and the matching-state atlas applies.  It
does not apply unchanged to deletion of an old boundary edge such as
\(hr\).  Moving from \(hr\) to a later edge requires proof that the new
edge still controls the same owner order; no such proof is present.

## 5. The strongest valid clean-detour statement

The following is the exact positive transition which survives audit.

### Lemma 5.1 (bag-aligned detour raises the potential)

Let \(xy\) be a bridge of the donor bag \(K_j\), with components
\(X\ni x\) and \(Y\ni y\).  Suppose

1. \(X\) contains a portal of a group \(T\) missed by \(K_0\);
2. \(Y\) contains the protected \(b\)-root, the two other rooted-bag
   portals, a retained \(K_0\)-portal, and retained portals for every
   group in \(\{A,C\}\) seen by \(K_j\); and
3. in \(G-xy\) there is an \(x\)-\(y\) path whose interior is contained
   in \(K_0\).

Then replacing

\[
 K_0\longmapsto K_0\cup X\cup\operatorname{int}P,
 \qquad K_j\longmapsto Y
\]

is a spanning rooted \(K_4\)-model with larger \(\Phi\).

#### Proof

The first new bag is connected through the first edge of \(P\), and the
last edge of \(P\) joins it to \(Y\).  It gains the \(T\)-contact in
\(X\).  The second bag retains all selected terminals in (2).  Every
other model adjacency is inherited from \(K_0\) or \(Y\), and the two
new bags have the same union as the three displayed pieces.  Thus no
root, group incidence, or spanning vertex is lost, while \(K_0\) gains
\(T\). \(\square\)

Because the original rooted model is spanning in \(J_0\), “interior is
contained in \(K_0\)” is the precise branch-set avoidance requirement;
an apparently external detour actually belongs to some reserved bag.

At a potential maximum, no Kempe detour can have this clean alignment.
This is a real conclusion, but it does not say where the five detours go.
In particular, it does not handle the unique-essential-\(T\)-portal
outcome: moving that portal would make the recipient gain \(T\) while the
donor loses \(T\), leaving \(\Phi\) unchanged.  A separate lexicographic
secondary potential or a direct completion certificate would be required
there.

## 6. Why the five Kempe detours do not give a six-cut

Delete a valid internal or boundary--shore edge \(xy\), and six-colour
\(G-xy\).  Its endpoints have one common colour and there are five
bichromatic \(x\)-\(y\) detours.  A detour which is not clean may:

* enter either of the other two rooted bags;
* enter both the donor and recipient more than once;
* use a boundary vertex whose label is needed by the fixed state; or
* share common-colour vertices with several other detours.

These obstructions are entire branch bags or colour components, not five
actual vertices.  Selecting one first hit from each detour does not produce
a separator: another detour, or an uncoloured path, may avoid all selected
hits.  Conversely the seven-detour theta architecture from
`hadwiger_near_k7_rotation_kempe_obstruction.md` has all five prescribed
bichromatic detours while remaining treewidth two; its obstruction is a
small adhesion only because that adhesion is visible independently, not
because the Kempe paths manufacture it.

Therefore the implication

\[
 \text{all five detours fail the peel}
 \Longrightarrow \text{a separator of order at most six}
\]

is currently unproved.  Establishing it requires a new theorem coupling
the detour colour labels to the fixed rooted-bag labels.  Without such a
coupling, it is exactly the noncommutation obstruction already identified
in the near-\(K_7\) rotation audit.

## 7. Exact blocker

The audited endpoint is:

1. all inessential mixed lobes have been eliminated at maximum \(\Phi\);
2. a genuine bridge edge with a bag-aligned detour through \(K_0\) raises
   \(\Phi\) and is impossible;
3. the note does not prove that such a bridge edge exists; and
4. for an arbitrary critical edge, failure of all five detours gives
   charged **bags**, not a bounded vertex separator.

The next valid lemma must be a bag-aligned detour-or-vertex-separator
theorem.  It must output either the clean path of Lemma 5.1 or an explicit
set of at most six vertices meeting every route; naming six terminal
classes is insufficient.
