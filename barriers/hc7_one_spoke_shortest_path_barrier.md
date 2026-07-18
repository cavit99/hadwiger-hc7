# Barrier: the unrestricted centre-to-deficient-bag path is degenerate

**Status:** written barrier to an intermediate proof mechanism.  This does
not refute the degree-seven one-missing-adjacency theorem.

## Refuted mechanism

The proposed mechanism chose a centre-to-deficient-bag path in a spanning
aligned `K_7^-` model and minimized

\[
 (\text{number of common-bag intervals},
   \text{number of common-bag vertices},
   \text{path order}).                                      \tag{1.1}
\]

It then sought a strict improvement from a proper-minor bichromatic
response, or a response reaching the deficient bag before every common
bag.

## Universal obstruction

Write the aligned model as

\[
                       \{c\},D,U_1,\ldots,U_5,              \tag{2.1}
\]

where `cD` is the unique missing adjacency.  In the degree-seven
construction one common branch set is the pole singleton `{u}`, and the
deficient bag contains a boundary vertex `b in N(u)`.  Therefore

\[
                              c-u-b                         \tag{2.2}
\]

is always a centre-to-deficient-bag path.  Its score is one common-bag
interval, one common-bag vertex and three vertices, the absolute minimum
possible because `{c}` and `D` are anticomplete.  Both edges of (2.2) lie
in the unchanged pole shore `G[N[u]]`, so the off-pole-shore edge-response
theorem does not apply to either edge.

There is a second identity.  Spanningness and `cD` anticomplete give

\[
                         N_G(c)\subseteq\bigcup_{i=1}^5U_i.
                                                                  \tag{2.3}
\]

Hence every centre-to-deficient-bag path meets a common branch set on its
first edge.  The proposed outcome “reach `D` before any common bag” is
logically impossible in every intended input.

Thus neither criticality nor additional connectivity can rescue the rank
in (1.1): it is already minimized by the fixed pole shortcut.

## Pole-avoiding repair and its limit

Let `C=G-N[u]`.  Since `C` is connected and adjacent to every vertex of
`N(u)`, a `c-b` path with all internal vertices in `C` exists, and every
edge of such a path is eligible for the off-pole response.  For one fixed
branch-set partition, a legitimate path rank must use connected components
of `U_i intersect C`, not merely repeated branch-set names.

Even that correction is only a normalization inside the fixed model.  A
branch-set rotation changes the trace components, and standard
two-universal-vertex icosahedral examples attain the minimum corrected
path length without producing a geometric improvement.  Those examples
have a terminal two-vertex transversal or an exact separator and are not
hypothetical `HC_7` counterexamples.  They show that strict improvement can
only be one disjunct of a theorem which spends the complete proper-minor
response and permits a terminal outcome.

## Consequence for the active proof

The path rank is not used further.  The proved two-mark branch-set theorem
instead gives, uniformly,

\[
                 K_7\text{ minor}\quad\text{or}\quad
                 \text{an actual full-neighbourhood separation}.
\]

The remaining problem is colour reflection across that separation, not
shortest-path first-hit casework.

## Related committed barriers

- [single branch-set rotations are reversible](hc7_near_k7_rotation_involution_barrier.md)
- [spanning-minimal deficient-tree barrier](hc7_near_k7_spanning_minimal_deficient_tree_barrier.md)
- [two-root Kempe-class icosahedron](hc7_two_root_kempe_class_icosahedron_barrier.md)
