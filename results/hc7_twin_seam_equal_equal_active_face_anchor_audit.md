# Independent audit: equal/equal active-face anchor exchange

**Verdict:** **GREEN at the frozen source hash below.**  Lemmas 1.1 and
2.1, Theorems 3.1, 3.3 and 3.5, and Corollaries 3.2, 3.4 and 3.6 are
correct under their stated hypotheses.  In particular, the contraction
in Lemma 2.1 creates no hidden edge into the planar shore, the imported
list-colouring theorems have exactly the required hypotheses, and in the
symmetric packet-one cell each unlocked switch has packet demand at least
two.

**Audited source:**
`results/hc7_twin_seam_equal_equal_active_face_anchor.md`.

**Source SHA-256:**
`d31269d343adc06c6073e51779bb93d1e1eb2ee51981d705c67794f28f180e60`.

## 1. Component switching is literal and boundary-anchored

In Lemma 1.1 the two endpoint components in the `i,j` subgraph are either
the same, giving the named path, or disjoint.  If a distinct component
missed the literal boundary, switching it would change exactly one end of
`e`, preserve every boundary colour, and glue to the fixed left-shore
colouring.  Thus both components meet the boundary.  First-hit paths in
two disjoint components have distinct literal boundary ends and interiors
off the boundary.  No palette colour is identified with a model label.

## 2. The contraction repair has no hidden adjacency

The only delicate point in Lemma 2.1 is the passage from the colouring of
`G_R-e` to one of `G_R/e`.  Every neighbour of either endpoint already
avoids their common colour, so identifying the endpoints preserves
properness inside `G_R`.  Moreover, both endpoints lie in `G_R-S`, while
`D=G_L-S`; shore anticompleteness therefore gives

\[
                         E_G(D,\{a,b\})=\varnothing.
\]

Consequently contraction creates no new edge from its image into `D`.
The lists on the facial cycle have size at least three and all vertices
off that cycle have the full `q`-set, hence size at least five.  Thomassen's
precoloured-outer-edge theorem applies after choosing distinct colours on
one facial edge.  The resulting list-colouring repairs `f` and leaves the
entire opposite closed shore, not merely its boundary state, unchanged.

## 3. Twin-seam specialization

For Theorem 3.1, the equal/equal response supplies the hypotheses of
Lemma 2.1 with `e=zu`, `f=dt` and boundary `Omega_D`.  The repaired
colouring is proper on the `D`-closed side and agrees vertex-for-vertex
with the original response on the `B_D`-closed side.  Lemma 1.1 therefore
gives, for every alternate colour, either a literal `z-u` lock or two
first-hit anchor paths whose interiors lie in `B_D`.  Since `d` is in the
other open shore, none of these paths uses `f`.

## 4. Sharp list obstruction audit

The list cases in Theorem 3.3 are exhaustive after first recording empty
lists and the case of at least three lists of order at most two.

* With no exceptional list, Lemma 2.1 applies.
* With one exceptional nonempty list, that vertex and a facial neighbour
  can be precoloured distinctly, and Thomassen applies.
* With two lists of size at least two, Postle--Thomas Theorem 1.2 applies
  even when the two vertices are nonadjacent.
* With list sizes one and two, Postle--Thomas Theorem 1.3 says precisely
  that failure is equivalent to containment of the directed colouring
  harmonica recorded in outcome 3.
* With two singleton lists, adjacent distinct singletons are covered by
  Thomassen; the same-colour adjacent case and all nonadjacent cases are
  correctly retained.

The primary statements are Theorems 1.1--1.3 of Postle and Thomas,
[*Five-list-coloring graphs on surfaces III. One list of size one and one
list of size two*](https://arxiv.org/abs/1608.05759).  Their outer-cycle,
outer-list and interior-list hypotheses match the note exactly.

For Corollary 3.4, the first step of a harmonica from the singleton end to
the two-list end contains a literal triangle through the singleton end.
The other two triangle vertices are distinct from the terminal two-list
vertex, and the exact harmonica lists give each list size three.  Since
every vertex off `F` has list size six, all three triangle vertices lie on
`F`.  A chord of an outer facial cycle of length at least four would make
its two ends a separator; four-connectivity therefore makes `F` induced.
The triangle is impossible.

## 5. Unlocked switches and demand

In Theorem 3.5, switching either of the two distinct endpoint components
makes `e` proper and changes exactly its nonempty boundary trace.  If the
new trace preserved the old unlabelled equality partition, a palette
permutation would align it with the state-preserving repaired left-shore
colouring and six-colour `G`.  If its induced active-face lists coloured
`D`, that list-colouring would likewise glue to the switched right shore.
Thus each switch changes state and creates one of the sharp obstructions
of Theorem 3.3.

Corollary 3.6's support algebra is exact.  On the two old colour blocks
`I,J`, a switch preserves the unlabelled partition only when its support
is empty or all of `I union J`; Theorem 3.5 excludes both extremes for an
unlocked endpoint switch.

Finally `rho_r` is proper on the original `B_D`-closed side because its
switch repairs `e`.  In the symmetric cell
`nu_{B_D}^{Omega_D}=1`.  If its state had demand at most one, exact packet
reflection in that one full packet would give either a literal `K_7` or a
proper colouring of the opposite `D`-closed side with the same exact
partition.  The kernel excludes the first, while the second palette-aligns
and glues to `rho_r`.  Hence

\[
                 d_{G[\Omega_D]}(\Pi_r)>1,
\]

which is the asserted integer bound at least two.

## 6. Trust boundary

The audited theorem proves a uniform state-preserving repair, five literal
lock-or-anchor alternatives, and two disjointly supported high-demand
state moves whenever one alternate colour is unlocked.  It does **not**
prove that paths for different colours are disjoint, that their ends cover
distinct model duties, that an internal lock is a branch-set row, or that
one of the switched states occurs on the opposite shore.  It therefore
does not yet yield a common state, a literal `K_7`, a coherent fixed pair,
a strict `F_12` handoff, the twin-seam decoder, or `HC_7`.
