# Independent audit: two-pole contact trichotomy

**Audited source:**
[`hc7_atomic_two_pole_contact_trichotomy.md`](hc7_atomic_two_pole_contact_trichotomy.md)

**Source SHA-256:**
`6bce1f570c12a93a7d1830f53905cb1e033bd2e40abed948a70a21ce5100c03d`

## Verdict

**GREEN after the precision corrections incorporated in the source.**
The contact-forcing constructions, the uses of the one-hole height gap,
the rooted row split, the actual-separator and exact-seven-fullness
conclusions, and the contact-increasing transfer are literal.  The
icosahedral guardrail is also correct and independently reproducible.

The result is local.  In particular, contact order five does not yet give
a strict `S1` handoff, and an order-seven separator from the row split does
not carry an attained equality state or a noncycling rank merely by being
an actual adhesion.

## 1. Setup and spanning extension

In the atomic application, `chi(G-{z,u})=6` and `HC_6` give a `K_6`
minor in `G-{z,u}`.  Seven-connectivity of `G` implies that deleting the
two poles leaves a connected graph.  Starting from any `K_6` model, every
unused component can therefore be assigned along a path to an adjacent
existing branch bag.  Repeating this extends the model to a spanning one
without losing any branch-set adjacency.  Thus the spanning hypothesis
used by the contact counts is justified.

## 2. Audit of Lemma 2.1

All three constructions have seven pairwise disjoint connected bags.

1. If every row is contacted jointly, `{z,u}` is connected through the
   literal edge `zu` and is adjacent to all six rows.
2. Five common rows together with the singleton poles give seven bags;
   `zu` is the pole--pole edge.
3. With four common rows and distinct exclusive rows `F_a,F_b`, the union
   `F_a union F_b` is connected because two rows of a `K_6` model are
   adjacent.  It contacts `z` through `F_a`, contacts `u` through `F_b`,
   and remains adjacent to all four common rows.  Together with the two
   poles this gives a literal `K_7` model.

The contrapositives `r<=5`, `c<=4`, and the prohibition on exclusive rows
on both sides when `c=4` are exact.  If one pole is absorbed into one row
while the other remains a singleton, the absorbed pole must contact its
recipient row and the singleton must contact the other five rows.  Hence
this alternative already has `r=6`; it creates no omitted contact-order
cell.

## 3. Audit of Lemmas 3.1 and 3.2

When `r=5`, the connected centre `{z,u}` meets exactly five foreign rows,
so it is an exact one-hole centre of order two and `mu<=2`.  If `mu=2`,
the audited
[`one-hole height-gap theorem`](hc7_near_k7_one_hole_height_gap.md)
would require every one-hole centre to have order at least three.  The
displayed order-two centre contradicts that requirement.  Since centres
are nonempty, `mu=1`.

This numerical conclusion does not construct a move from the displayed
pair-centred model to a singleton minimizer.  The minimizer may use a
different six-row frame.  At `mu=1`, the height-gap theorem gives no
orientation, and the audited single-gate rotations can be exact
involutions.  Moreover `{z,u}` itself cannot be the atomic fixed-pair
terminal: its deletion contains the displayed `K_6` minor and hence a
`K_5` minor.  Therefore Lemma 3.1 correctly withholds a strict `S1`
handoff.

When `r=4`, the same pair centre misses exactly two rows, giving an exact
two-hole model of order two.  The three refinements in Lemma 3.2 follow
directly from the definition of `mu`.  If one pole contacts all four
jointly contacted rows, that singleton itself is an exact two-hole centre
on the same frame.  None of these observations orients a reversible
two-hole rotation component.

The source now defines `mu` only when the near-model family is nonempty;
the hypotheses `r=5` and `r=4` ensure nonemptiness in the two uses.

## 4. Audit of Lemma 4.1

Choose a spanning tree of `G[F_h]`.  Deleting an edge on its `x`--`y`
path leaves two nonempty connected vertex sets, containing `x` and `y`
respectively, and the deleted edge makes them adjacent.  This proves the
claimed rooted partition.

If both pieces contact all five foreign rows, the two pole-rooted bags

\[
                 \{z\}\cup X_z,\qquad \{u\}\cup X_u
\]

are connected, disjoint, and adjacent through `zu`.  Each contacts every
retained row, and those five rows remain a clique model, so the seven bags
form a literal `K_7` model.

Suppose instead that a piece `Y` is anticomplete to a foreign row `F_j`.
The row `F_j` is nonempty and lies outside `Y union N_G(Y)`.  Hence
`N_G(Y)` separates `Y` from `F_j`; this is an actual vertex cut, not only
a model-relative portal set.  Seven-connectivity gives `|N_G(Y)|>=7`.

If equality holds and a component `C` of `G-N_G(Y)` misses a literal
boundary vertex `s`, then

\[
                        N_G(C)\subseteq N_G(Y)-\{s\}.
\]

There is at least one other component of `G-N_G(Y)`: the proof already
exhibits the separated `Y` and `F_j` sides.  Consequently deleting
`N_G(C)` disconnects `C` from that other component.  This would be a cut
of order at most six, contradicting seven-connectivity.  Every component
therefore has a neighbour at every one of the seven literal boundary
vertices.  The asserted exact-seven fullness is valid.

This conclusion supplies an actual exact-seven interface only.  It does
not itself supply an attained proper-minor state or orient the next
handoff, as the source correctly emphasizes.

## 5. Audit of the transfer and multiplicity bounds

The degree bounds (5.1) follow because the spanning rows partition every
neighbour of either pole other than the other pole, while
seven-connectivity gives each pole degree at least seven.  Summing them
gives (5.2) by the pigeonhole principle.  These inequalities count
literal portals but do not label row duties.

For the transfer (5.3):

* `F_i-Y` remains connected and `F_j union Y` is connected through a
  literal `Y-F_j` edge;
* the cut edge between `Y` and `F_i-Y` supplies the new donor--recipient
  adjacency;
* old `F_j` supplies every recipient--foreign-row adjacency;
* condition 3 preserves every donor duty not replaced by that cut edge;
* condition 4 preserves all old pole contacts at the donor; and
* because `j` was uncontacted and `Y` meets a pole, the recipient gains a
  new pole contact.

The resulting six bags remain disjoint, span the same vertex set, and
form a `K_6` model with strictly larger joint contact.  Thus a
contact-maximal model admits no such transfer.

## 6. Audit of the icosahedral guardrail

The dependency-free checker
[`../active/hc7_atomic_two_pole_contact_trichotomy_verify.py`](../active/hc7_atomic_two_pole_contact_trichotomy_verify.py)
whose SHA-256 is
`4a81379c2ae4dc5cb127d2c2192b50f4296ed581a9d54f12622bf17d4dfda71b`,
verifies that the six displayed rows partition the host minus the two
poles, are connected and pairwise adjacent, and have contact sets

\[
 C_{u_3}=\{1,3,4,5,6\},\qquad
 C_{u_4}=\{1,4,5,6\}.
\]

Thus their joint contact is exactly five.  Directly, `u_3` contacts five
rows and misses only `{u_1}`, so it is a singleton one-hole centre and
`mu=1` in this host.

For `G_0=K_2 vee I`, deletion of at most six vertices leaves a universal
join vertex unless both are deleted; in the latter case at most four
vertices were deleted from the five-connected icosahedron.  Hence `G_0`
is seven-connected.  A hypothetical `K_7` model would, after removing at
most two bags containing the join vertices, leave at least five
pairwise-adjacent connected bags in the planar icosahedron, a forbidden
`K_5` minor.  Thus `G_0` is `K_7`-minor-free.

The exact balanced singleton one-hole two-cycle in this same host is
proved in
[`../barriers/hc7_near_k7_rotation_involution_barrier.md`](../barriers/hc7_near_k7_rotation_involution_barrier.md)
and independently audited beside it.  This establishes failure of a raw
height/contact orientation.  It does not refute the possible existence of
a fixed-pair theorem: this host actually has the coherent pair `{p,q}`.
Accordingly the corrected source says only that the contact-five model
does not identify that pair and does not orient the rotation.

## 7. Exact scope retained

The promoted theorem proves the following usable alternatives for the
regenerated spanning frame:

* immediate literal clique models at the contact thresholds of Lemma 2.1;
* exact one-/two-hole model states when `r=5` or `r=4`;
* a literal `K_7` or an actual separator from a same-row rooted split; and
* strict model augmentation whenever the contact-increasing transfer is
  available.

It does **not** turn a separator into a state-carrying descent, orient a
near-model rotation component, or decode the remaining row-duty lock.
Those are precisely the response-matched twin-lock obligations left in
the active theorem.
