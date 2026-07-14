# Audit: exact two-carrier clique-OCT obstruction and gate reassignment

**Verdict:** GREEN at frozen source SHA-256
`3cdeea2b434cf9a957d481862671566bca094dd86b52d3532b8dad629d906bec`.

The nonspanning synchronization, exact two-list parity criterion, literal
reassignment criterion, retained-clique duty theorem, automatic-duty
frontier proposition, and final parity obstruction are all correct.  Every
claimed equivalence is confined to the named two-carrier contraction
mechanism where the source says it is.

## 1. Theorem 2.1: nonspanning synchronization

Let `I_i=phi^{-1}(i)`.  Properness of the two-list colouring makes every
`I_i` independent, and the list condition gives every member of `I_i` a
literal neighbour in `C_i`.  Hence `C_i union I_i` is connected.  The two
sets are disjoint because the carriers are disjoint and the `I_i` partition
the literal boundary.

At least one block is nonempty because `S` is nonempty.  Its union with its
nonempty carrier contains a literal carrier-boundary edge, so contracting a
spanning tree produces a proper minor.  If the other block is empty, the
source's instruction to contract `C_i union I_i=C_i` is harmless: a
singleton carrier requires no contraction, a larger connected carrier may
be contracted, and its image is discarded when restricting the colouring.
The properness certificate comes from the nonempty block.

After restriction to `R union S`, only the boundary blocks are expanded.
This is proper because they are independent and every edge incident with a
contracted boundary member was represented at the corresponding image.
When both blocks are nonempty, the literal `C_1-C_2` edge forces their
images to receive distinct colours.  With one nonempty block, exactness is
automatic.  Vertices of `L-(C_1 union C_2)` may indeed be discarded; the
minor colouring need not be lifted through them.

On the opposite side, assigning one distinct full packet to each nonempty
block gives disjoint connected nontrivial contraction sets.  Packet
fullness makes two block images adjacent when both occur.  An empty block
requires no contraction and its unused packet is discarded on restriction
to `L union S`.  Thus both closed-shore colourings induce exactly the same
one- or two-block partition.  Their block colours can be aligned by a
partial palette bijection extended to a permutation, and the colourings
glue because there is no `L-R` edge.

This verifies both the nonspanning restriction and Remark 2.2.

## 2. Theorem 3.1: exact two-list obstruction

For a bipartite connected component `K`, every proper two-colouring is one
of the two orientations

\[
 phi_epsilon(s)=1+(p_K(s)\mathbin{\mathsf{xor}}epsilon).
\]

A singleton list `{c_s}` forces exactly

\[
 epsilon=p_K(s)\mathbin{\mathsf{xor}}(c_s-1),
\]

while a flexible list imposes no condition.  Therefore a component is
list-colourable exactly when all forced vertices prescribe one common
orientation; isolated vertices are included by the same calculation.
Different components may orient independently.

For two forced vertices, disagreement is equivalent to equal singleton
lists at odd bipartite distance, or different singleton lists at even
distance.  If `H` is not bipartite, no proper two-colouring exists at all.
The theorem's two obstructions are therefore necessary and sufficient, and
Corollary 3.2 is exact for the retained two-carrier mechanism.

## 3. Theorem 4.1: one literal reassignment

A legal move preserves nonempty lists.  A boundary vertex not adjacent to
`Z` retains every old contact; a vertex adjacent to `Z` gains or retains a
literal contact with `C'_2=C_2 union Z`.  Formula (4.3) follows directly,
and a list can change only at a literal neighbour of `Z`.

Outside the affected set `A`, `Lambda'=Lambda`.  Thus (4.4) is precisely
the componentwise orientation criterion of Theorem 3.1 applied to the
recomputed lists `Lambda'`; it neither assumes nor invents an abstract
palette change.  When (4.4) holds, Theorem 2.1 legally glues the state.  If
it fails, the new list instance has no proper colouring, so this named
two-carrier mechanism cannot glue.  The source correctly does not infer
that every other minor construction also fails.

The prose about a common unchanged orientation is read existentially when
a component has no unchanged forced vertex, exactly as the displayed
formula states.  Corollary 4.2 is the correct specialization to one changed
vertex.

## 4. Theorem 7.1: retained-clique duty and proper minors

Let `U` be the retained clique and `F=H-U`.  Since `F` is nonempty, at
least one list-colour class `I_i` is nonempty.  Only nonempty blocks are
contracted in this theorem.  For such a block,
`C_i union I_i` is connected and contains a literal carrier-boundary edge,
so the carrier-side minor is proper.  The sets for the two indices are
disjoint; if both occur, the literal carrier edge makes their images
adjacent.

For `u in U`, the image of `C_i union I_i` is adjacent to the retained
singleton `u` exactly when either `u` has a boundary edge to `I_i`, or
`u` has a carrier edge to `C_i`.  Consequently

\[
 D_U(I_i)=I_i\cup
 \{u\in U:N_H(u)\cap I_i=\varnothing\}
 \subseteq N_S(C_i)
\]

is exactly the required representative-to-singleton adjacency condition,
using the already known list contacts for the members of `I_i`.  No duty is
needed for an empty block because it has no representative in the target
state.

The nonempty block images and the literal vertices of `U` form a clique of
order at most `2+|U|<=6`.  Hence every six-colouring of the carrier-side
proper minor induces exactly the nonempty `I_i` blocks plus the singleton
blocks `{u}`.  Unused carriers and all other nonspanning `L` vertices are
simply discarded on restriction.

On the packet side, one distinct full packet per nonempty block supplies
connected proper contractions.  Packet fullness gives all image-image and
image-`U` adjacencies, while `U` supplies the singleton clique.  The same
exact partition is returned, its at most six block colours align, and the
closed shores glue.

The source's necessity statement is scoped correctly: (7.3) is necessary
and sufficient for the named representative-to-singleton adjacency, not
for every conceivable proper-minor realization of the state.

## 5. Proposition 8.1: automatic duty in both frontier forms

If `H` is connected bipartite and `U` is empty, there is no retained duty.

If `H=K_{1,3} dotunion K_3` and `U={u}` is one triangle vertex, write the
remaining triangle edge as `xy`.  Every proper two-colouring of

\[
 F=K_{1,3}\mathbin{\dot\cup}xy
\]

assigns `x,y` different carrier indices.  Thus each nonempty colour class
contains one literal neighbour of `u`, independently of how the claw
component is oriented.  The retained singleton is adjacent to both block
representatives through those boundary edges, so (7.2) adds no duty vertex
to either block.  This remains true after a legal carrier reassignment,
provided the resulting list colouring exists.

The relevant connected frontier has edges, and the exceptional frontier
contains `xy`, so both colour classes are nonempty in the applications.
Corollary 8.2's iff is therefore valid for the explicitly named
clique-OCT state mechanism.  Its disclaimer correctly prevents reading it
as an iff for arbitrary six-colourings or arbitrary proper-minor states.

## 6. Theorem 9.1: exact post-move obstruction

The literal update (9.1) is the restriction of (4.3) to `F`, and
`A_F subseteq N_S(Z) cap V(F)` is correct.  Contacts to `U` may change, but
Proposition 8.1 makes them irrelevant: `U` is empty in the connected form,
and in the exceptional form every proper two-colouring uses the two
neighbours `x,y` in opposite classes.

Both possible graphs `F` are bipartite.  Hence, after the move, failure of
the named clique-OCT state is exactly failure of the recomputed two-list
instance.  Theorem 3.1 makes this equivalent to two forced vertices in one
component prescribing opposite orientation bits, or equivalently equal
singleton lists at odd distance or different singleton lists at even
distance.  Formula (9.3) is the exact mixed old/new version because the
lists agree outside `A_F`.

On the exceptional edge component `xy`, the only failure is indeed that
both endpoints are forced to the same carrier.  Flexible endpoints or
opposite singleton lists admit a proper orientation.

## 7. Trust boundary

The note completely characterizes list-state compatibility once two
literal adjacent carriers and their contact lists are fixed.  It does not
produce a legal geometric reassignment, prove that one must exist, or
exclude other state-producing contractions when its list instance fails.
Those limitations are stated accurately and no stronger iff is used.
