# Independent audit: pure-Moser crossing carrier

## Verdict

**GREEN after two editorial precision repairs listed in Section 7.**

This audit covers Sections 1--4 of
`results/hc7_moser_crossing_carrier.md`: the crossed rooted `K_4`,
Theorem 2.1, Lemma 2.2, Lemma 3.1, Proposition 3.2, Theorem 4.1,
Corollary 4.2, and Proposition 4.3.  It confirms the stated residual rural
outcome only; it does **not** claim that outcome is closed.

## 1. Crossed frame and rooted bags

For the Moser labelling, `U={0,2,4,5,6}` induces the cycle
`0-2-6-5-4-0`.  The hypotheses of the audited guarded cyclic-shore theorem
hold with guards `{v,1,3}` and shores `C_1,C_2`.  Its crossless outcome is
planar after deleting those three actual vertices, so the audited
three-apex theorem forces a `K_7`; hence a `K_7`-free counterexample has a
crossed shore.

The two terminal-clean crossing paths join opposite pairs of four roots
which alternate on the frame.  Together with the four intervening frame
arcs they form a literal subdivision of `K_4`.  Deleting one selected edge
from each of its six subdivided edges leaves four disjoint connected root
components, and every deleted edge witnesses the corresponding pairwise
bag adjacency.  Since the frame has five vertices, the unselected fifth
root lies on exactly one frame arc; choosing the cut on either side of it
puts it in either incident root bag.  Thus all five vertices of `U` are in
the four bags and each bag contains a neighbour of `v`.

No shore vertex, artificial terminal, or colour-class label is silently
identified with a branch bag in this construction.

## 2. Literal two-row completion

The seven bags in Theorem 2.1 are

`{v}, B_1,B_2,B_3,B_4, {a} union X, {b} union Y`.

They are disjoint and connected.  The `B_i` form a clique model; `v` meets
them and meets the last two bags through `va,vb`; an `X-Y` edge joins the
last two bags.  A direct `a-B_i` edge handles `i` outside `I_a`, and an
actual `X-r_i` edge handles `i` in `I_a`; the `b` row is identical.  Hence
all 21 bag pairs have literal witnessing edges.

Lemma 2.2 is valid: choose a shortest path between the two disjoint
connected sets, truncated so its internal vertices avoid both sets, and
assign all internal vertices to one end set.  The last path edge supplies
adjacency while connectedness and disjointness are preserved.

## 3. Moser duty bounds and the duty-free lift

The two boundary neighbourhoods are exactly

`N_U(1)={0,2,6}` and `N_U(3)={0,4,5}`.

Every rooted bag contains a distinct selected root.  A bag missed by `1`
therefore has its selected root in `{4,5}`, and a bag missed by `3` has its
selected root in `{2,6}`.  This proves both bounds in Lemma 3.1.  The two
sets are disjoint because their possible selected-root sets are disjoint.
The conclusion remains true after assigning the fifth root to one bag.

If the `1` row is duty-free, use `{1}` and `{3} union Y`, where a connected
subgraph `Y` of the full shore meets portals of `1`, `3`, and all roots of
the missing `3` duties.  The portal of `1` joins the two row bags; the
portal of `3` connects the second bag; the selected duty portals repair
its missing contacts.  Together with `{v}` and the four rooted bags, these
are the seven literal clique bags.  The symmetric case is identical.

## 4. Four-port linkage or rural disk

Theorem 4.1 uses the generalized Two Paths theorem within its audited
scope.  In the crossed outcome, terminal-clean alternating paths become
the required two disjoint actual paths after replacing artificial ends by
root portal edges (or a copied terminal edge by the corresponding literal
boundary edge).

In the crossless outcome, consider the original shore vertices `X` in an
inserted facial clique.  Frame terminals are rib vertices, so `X` is the
whole inserted interior of that clique.  Its represented boundary
neighbours correspond to at most the three vertices of the facial
triangle; its only other possible boundary neighbours are the three
unrepresented vertices of `S`.  Since `D` is a component of `G-S`, there
are no further neighbours outside the shore.  Thus `|N_G(X)|<=6`, and this
set separates nonempty `X` from the assumed nonempty far side, contrary to
seven-connectivity.  Every original shore vertex is consequently in the
planar rib.

After deleting all completion-only edges, replace each retained artificial
terminal edge by its literal root edge.  This produces the induced closed
shore in a disk with boundary order `p_0,p_1,p_2,p_3` (up to reversing the
disk orientation).  Edges among the four roots were copied into the
terminal graph, so none is omitted.

## 5. One duty on each row

With ordered tuple `(1,3,r,s)`, the crossed linkage consists of a `1-r`
path and a `3-s` path.  The duty definitions exclude the direct edges
`1r` and `3s`, so both interiors are nonempty connected subsets of `C_2`.
They are disjoint; Lemma 2.2 enlarges them to adjacent disjoint connected
carriers without losing their endpoint contacts.  Theorem 2.1 then gives
the literal `K_7` model audited above.  Otherwise the disk order is exactly
`1,3,r,s`.

For the favourable roots `{0,2,5,4}`, assigning the omitted vertex `6` to
the bag rooted at `5` leaves precisely the duties `r=4` for row `1` and
`s=2` for row `3`.  The opposite-shore cycle

`1-0-3-4-P_{42}-2-1`

is simple because the path interior lies in `C_1`; its four marked
vertices occur in the order `1,3,4,2`.  This agrees with, rather than
contradicts, the rural disk order.  The note is therefore correct not to
claim closure from an order mismatch.

## 6. Exact trust boundary

The green result proves:

* a literal rooted `K_4` in one shore;
* a literal `K_7` whenever the opposite shore has the stated two carriers;
* unconditional closure when one row is duty-free; and
* in the one-duty-per-row cell, either that carrier completion or one
  exact four-port rural disk.

It does not prove that the rural disk is globally planar after three
deletions, does not close cases with two duties on a row, and does not
derive a labelled carrier from a proper-minor colour alone.

Corollary 3.3, added after this audit, is independently checked in Section 9
of `hc7_exact_seven_packet_packing_audit.md`.  Two disjoint `N`-full
packets in `C_2` satisfy every literal portal requirement of Theorem 2.1
after Lemma 2.2 makes them adjacent, so the surviving carrier shore has
packet number exactly one.

## 7. Precision repairs

1. In Theorem 2.1, replace “`D` is ... disjoint from all six of those
   sets” by “`D` is disjoint from `{v,a,b}` and from all four `B_i`.”
   There are seven displayed sets/vertices, not six.  The Moser
   application satisfies the corrected condition.
2. In Lemma 2.2, replace the sentence about adding “all internal vertices,
   except the end in `Y_0`” by: “Choose a shortest path
   `x_0...x_k` with `x_0 in X_0`, `x_k in Y_0`; its internal vertices may
   be chosen outside `X_0 union Y_0`.  Add `x_1,...,x_{k-1}` to `X_0`.”
   The present phrase is grammatically inconsistent because an endpoint is
   not an internal vertex; the intended proof and lemma are correct.

For maximum precision in Theorem 4.1, “replace an artificial terminal
among those triangle vertices” should be read as “replace **each** such
artificial terminal by its corresponding actual root.”  This is already
the operation used in the neighbour count and does not change the proof.
