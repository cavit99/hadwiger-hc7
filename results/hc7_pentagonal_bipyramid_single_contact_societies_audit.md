# Independent audit of the single-contact pentagonal-bipyramid theorem

**Verdict:** **GREEN** for the exact source revision identified below.

**Audited source:**
[`hc7_pentagonal_bipyramid_single_contact_societies.md`](hc7_pentagonal_bipyramid_single_contact_societies.md)

**Audited SHA-256:**
`1751b8ca3d1531d157299c6d8d44970156deeb0b70afe6030adfbeeadd44996c`

This is an internal mathematical audit, not external peer review.  The
source proves a conditional unbounded theorem for a spanning expansion of
the pentagonal bipyramid by four-connected columns with one literal edge
per quotient edge and distinct portal endpoints at each column.  It does
not prove that arbitrary columns satisfy those hypotheses.

## 1. Entry into the local column theorem

For a fixed column `L_x`, every neighbour label `y` has exactly one portal
vertex `q_{xy}`.  The distinct-end hypothesis makes these portal vertices
pairwise distinct as `y` varies.  They therefore form a matching of order
`d_P(x)`, which is five for a pole and four for a rim vertex.  The audited
four-connected-column theorem applies at every column.

If that theorem returns a rooted `K_4`, its own completion lemma already
gives the claimed explicit `K_7` model.  Otherwise `L_x` is planar and all
its portal vertices lie on one face.  Four-connectivity implies
two-connectivity, so the boundary of that face is a cycle `C_x`; no facial
boundary walk with a repeated portal occurrence is being treated as a
cycle.

## 2. Outside cycles and the order-mismatch contraction

The cycles in Lemma 2.1 are correct in both vertex orbits of the
pentagonal bipyramid.

* For a pole, deleting it leaves the other pole joined to the rim, and the
  rim `C_5` contains all five neighbours in their rotation order.
* For a rim vertex `c_0`, its neighbours occur in the order
  `c_4,a,c_1,b` up to reversal, and `c_4-a-c_1-b-c_4` is a cycle in
  `P-c_0` with precisely that order.

For four portal vertices, an order mismatch is already the whole mismatch.
For the five portals at a pole, two cyclic orders that agree up to reversal
on every four-subset agree globally; hence a global mismatch has the
four-portal witness selected in Lemma 2.2.

Contracting an external column `L_y` to one vertex is legitimate because
the column is connected.  For a selected neighbour label, the unique
`L_x`--`L_y` edge then joins that contracted vertex to `q_{xy}`; contracting
this edge identifies no two selected roots.  The outside cycle `D_x`
therefore becomes a cycle through the same four literal roots as `C_x`.
Apart from those roots its vertices come from external columns, whereas
`C_x` lies in `L_x`, so the two lifted cycles have disjoint interiors.

Suppressing the intervals between consecutive selected roots preserves the
two cyclic orders.  The audited two-cycle exchange lemma then gives a
`K_4` minor rooted at the four selected `q_{xy}`.  In the contraction
preimage, the branch set rooted at `q_{xy}` contains the entire contracted
column `L_y`.  An unselected column or an unselected interval used while
suppressing a cycle is assigned to one of these four bags and is not used
again below.  Thus lifting preserves connectivity, pairwise disjointness,
and one whole selected external column in every rooted bag.

## 3. The fifth branch set in both quotient orbits

The completion is correct for both possibilities for `x`.

* If `x` is a pole, the four selected labels are four rim vertices.  The
  other pole column is absent from both cycles, hence disjoint from all four
  rooted bags, and is adjacent to every selected rim column.
* If `x=c_0` is a rim vertex, the four selected labels are exactly
  `a,b,c_4,c_1`.  The two unused labels are the consecutive rim vertices
  `c_2,c_3`.  Consequently `L_{c_2}\cup L_{c_3}` is connected, is disjoint
  from the two cycles, contacts both selected pole columns, contacts
  `L_{c_1}` through `L_{c_2}`, and contacts `L_{c_4}` through `L_{c_3}`.

In either case the fifth bag contains a whole column and the first four bags
each contain a distinct whole selected column.  Both fixed root branch sets
are adjacent to all five bags, are disjoint and connected, and are adjacent
to one another by the inherited setup.  The seven displayed bags are
therefore a valid `K_7`-minor model.

## 4. Global planar embedding

In the nonminor branch, every column has a plane embedding with all portals
on one facial cycle.  Lemma 2.2 forces its portal order to agree, up to
reversal, with the unique rotation of the corresponding vertex of `P`.
Reflecting each column drawing independently makes all seven orders agree
with one fixed plane embedding of `P`.

Put each column drawing in a disjoint vertex-disc with its portal face as
the outer face.  There is exactly one literal edge for every quotient edge
and no edge for a nonedge of `P`.  The edge can therefore be drawn in the
corresponding edge-corridor.  The compatible rotations prevent crossings
inside the vertex-discs, and one edge per corridor leaves no endpoint-order
condition to coordinate along a corridor.  The discs and corridor interiors
can be chosen disjoint.  This gives a plane embedding of the complete union
`F`, not merely of a selected spanning subgraph.

In the stated spanning-root specialization, a four-colouring of `F`, one
new common colour on the nonadjacent vertices `v,w`, and a sixth colour on
`p` is proper.  Possible edges from the roots into `F` cause no conflict
because the root colours are fresh; `vp,pw` are proper and `vw` is absent.

## 5. Trust boundary

The distinct portal endpoints and single intercolumn contact are both used
essentially.  The proof supplies no order coupling for an edge bundle,
does not raise portal matching rank when several labels share a portal,
and does not decompose an internally separated column.  Subject to the
stated hypotheses, however, every contraction, lift, fifth-bag completion,
and embedding step is valid.  There are no unresolved assumptions in the
conditional theorem.  **GREEN.**
