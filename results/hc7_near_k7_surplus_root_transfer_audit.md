# Independent audit: surplus-root transfer and one-donor rotation

## Verdict

**GREEN after correction of the two-donor interaction.**  All transfers
are literal branch-set repartitions.  Two simultaneous transfers root the
old clique model when the residual donors remain adjacent; otherwise one
residual donor has an actual open-neighbourhood separator with the other
on a far side.  The one-donor theorem either roots the model or rotates
the deficient centre.  A spanning-tree partition closes the concentrated
`4+1+1+1` exact-seven distribution modulo an actual adhesion or labelled
near-clique rotation.

## Checks

1. Moving a detachable part `Z` from donor `U` to a met target `T`
   preserves connectedness and disjointness.  The `Z-(U-Z)` cut edge
   restores donor--target adjacency; the monopoly condition retains all
   other donor rows.
2. Transfers from distinct donors to distinct targets do **not** commute
   automatically: a retained donor--old-donor edge can end in the part
   simultaneously removed from the opposite donor.  The corrected
   theorem checks the residual donor--donor edge explicitly.  If it is
   present, old target--target and target--other-row edges survive and
   the transfers commute.  If it is absent, the residual donors are
   connected anticomplete sets, so the open neighbourhood of either is
   an actual separator with the other on a far side.  In the successful
   branch, one moved root per target, one protected root per donor, and
   one old root per untouched bag are literal distinct roots.
3. In a one-donor partition `U_0,Z_B,Z_C`, `U_0` need not retain old
   edges to `B,C`: its cut edges to the pieces now absorbed into those
   targets restore both.  It must retain only the other row contacts.
4. For deficiency rotation, the six foreign bags
   `X,B',C',V_1,V_2,V_3` are pairwise adjacent.  Full boundary roots in
   the moved pieces give `X-B',X-C'`; old path contacts give `X-V_i`;
   all remaining pairs are old foreign-clique edges.  The residual donor
   meets `X` at its protected full root and meets `B',C'` at the two cut
   edges.  Hence exactly the lost untouched-neutral rows are missing
   spokes, so loss orders `0,1,2` give `K_7,K_7^-,K_7^vee`.
5. A connected graph with at least three marks has the required
   three-part partition: delete the two distinct spanning-tree edges at
   two leaves of the minimal marked subtree.  Each leaf component and the
   central component contain a mark, and the deleted edges provide both
   central adjacencies.
6. In the `4+1+1+1` cell, any moved part missing a twin has that entire
   bag beyond its open neighbourhood, so it exposes an actual separator.
   Otherwise both parts support their assigned twins.  If all three other
   neutral contacts are lost jointly, the connected central donor is
   anticomplete to any of those bags and its own open neighbourhood is an
   actual separator.  Every nonseparator case therefore gives target or
   rotation.

## Scope

A rotated `K_7^vee` model is not itself a contradiction; it changes the
deficient centre and must be combined with a well-founded potential,
proper-minor state collision, or global rural coherence.  A separator of
order greater than seven is not automatically full.  These are the exact
remaining composition issues.
