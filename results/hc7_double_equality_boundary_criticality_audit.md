# Independent audit of boundary-preserving criticality in the simultaneous-equality colouring

**Verdict:** GREEN for the exact revision audited.

This is an independent internal mathematical audit, not external peer
review.  It checks the general boundary-colouring lemmas, their application
to the balanced order-eight configuration, the planar list-critical-core
argument, and every branch-set construction in the labelled first-hit
conclusions.

## Audited revision

- theorem file: `results/hc7_double_equality_boundary_criticality.md`
- SHA-256:
  `bd8aa342a2c6d81f8e34096e8f8fa5c9f993e27284d3f6a95bd2562274f74ba4`
- audit date: 17 July 2026

## 1. Simultaneous-equality trace orientation

The two closed sides cover the host graph and meet exactly in the literal
boundary.  A trace-preserving repair of `e` therefore glues to the displayed
colouring of the opposite side minus `f`, producing a colouring of `G-f`;
the converse follows by restricting such a colouring after a permutation of
colour names on its boundary classes.  The argument for `f` is symmetric.

The asserted signatures are correct.  In a colouring of `G-f`, the restored
edge `e` is proper.  The endpoints of `f` must be equal-coloured, because
otherwise the same colouring would be a colouring of `G`, contrary to the
hypothesis.  Thus the signature is `(proper,equal)`, and symmetrically it is
`(equal,proper)` for `G-e`.  If both trace-preserving repairs existed, the
two closed-side colourings would glue to a colouring of all of `G`.

Using the same equality partition rather than the same literal colour names
is safe: the injective correspondence between the colour classes used on
the boundary extends to a permutation of the full palette.

## 2. Fixed-boundary Kempe certificate

For a fixed alternate colour, equality or inequality of the two named
bichromatic components is an exhaustive dichotomy.  If the components are
distinct and one avoids the boundary, switching that component changes
exactly one endpoint of the missing edge while preserving every boundary
colour.  Restoring the edge then contradicts nonrepairability.  Hence both
components meet the boundary.

Shortest endpoint-to-boundary paths stopped at their first boundary
vertices have boundary-free interiors.  They are vertex-disjoint and have
distinct boundary endpoints because they lie in different bichromatic
components.  If an endpoint had no neighbour of the alternate colour, its
bichromatic component would be a singleton and recolouring that endpoint
would repair the edge.  The claimed neighbour condition and the prohibition
on boundary-disjoint component switches both follow.

The geometric refinement in the common-component case is also valid: a
shortest endpoint path either avoids the boundary internally, meets it first
at distinct vertices from the two directions, or has one common first-hit
vertex with internally disjoint initial segments.

## 3. Minimal list-critical core

The lists delete exactly the colours occurring on boundary neighbours, so
an `L`-colouring of the open side is equivalent to extending the fixed
boundary colouring.  The open side with the edge restored is not
`L`-colourable, whereas deleting the edge admits the restricted displayed
colouring.

A vertex-minimal induced non-`L`-colourable subgraph must contain both
endpoints of the edge; otherwise it is an induced subgraph of the known
`L`-colourable edge-deleted graph.  Minimality gives connectedness and
colourability of every proper induced subgraph.  Colouring `K-w` and trying
to extend to `w` proves

\[
             d_K(w)\ge |L(w)|.
\]

The theorem correctly warns that this is the reverse of the general
degree-assignment hypothesis and does not, by itself, imply that `K` is a
Gallai tree.

## 4. Web-attachment localization and planarity

The application uses the full hypotheses of the separately promoted
canonical rooted-web theorem.  If a web attachment set `X_U` is nonempty,
every one of its vertices has neighbours only in `U union X_U`, even after
passing to the spanning subgraph `Q`.  Deleting the facial triangle `U`
therefore separates `X_U` from an outer root outside `U`, so `U` is a
three-vertex cut of `Q`.

Every such cut contains `z_e,z_f` by the exact rooted-web hypothesis.  Since
the virtual outer edge `z_ez_f` is incident with a unique bounded facial
triangle, the only possible supporting triangle is

\[
                         T=\{z_e,z_f,x\}.
\]

The promoted theorem gives exactly two components of `Q-T`, one containing
the two leaf vertices and the other containing a vertex of the image of the
second five-clique in `X_T`.  No vertex of `X_T` can meet a skeleton vertex
after `T` is deleted.  A further component of `Q[X_T]` would create a third
component of `Q-T`; consequently every attachment vertex lies on the
localized-clique side.  The leaf-side component consists entirely of
vertices and edges of the planar skeleton.

The open component `C` is precisely the lift of the component of `Q-T`
containing `ell_e,ell_f`.  Deleting `R` and contracting the two boundary
edges changes no edge with both ends in `C`, so `G[C]=Q[C]` is planar.

## 5. Euler incidence bound and the two-vertex case

For the fixed-boundary critical core in `C`, let `c(w)` count distinct
boundary colours seen by `w`.  The list-degree inequality gives

\[
                       c(w)\ge 6-d_K(w).
\]

For a simple planar graph of order at least three,

\[
 \sum_w c(w)\ge 6|K|-2|E(K)|\ge 12.
\]

No connectivity or face assumption beyond those already proved is missing
from this calculation.

If the core has only the two endpoints of the restored edge, each list is
nonempty because the edge-deleted colouring supplies a list colour.  The
degree inequality makes both lists singletons, and noncolourability of the
edge makes them the same singleton.  It is the common endpoint colour in
the displayed colouring, so each endpoint sees all five other colours on
the literal boundary.

## 6. Labelled first-hit branch-set constructions

In the same-index placement, the two disjoint first-hit paths survive the
contractions of `e,f` and realize the missing
`ell_e-z_e,ell_f-z_f` linkage.  Together with the other two pair-linkages
from the rooted-web theorem, the rooted-`K_4` characterization gives four
rooted branch sets.  Expanding `z_e,z_f` to the literal edges `e,f` preserves
connectivity, disjointness, and all rooted adjacencies.  The three singleton
vertices of `R` complete the `K_7` model: the leaf branch sets are complete
to `R`, each defect edge is collectively adjacent to every vertex of `R`,
and `R` is a clique.

For the two split-edge placements, deleting only the terminal boundary
vertex from each first-hit path leaves two disjoint connected subgraphs in
`C`, with exactly the `x` and defect-edge contacts required by the promoted
split-edge completion theorem.  The second placement is its symmetric
application after interchanging both defect-edge and leaf labels.  The
promoted theorem's audit already verifies all twenty-one adjacencies, and
the present hypotheses match its labels exactly.

## 7. Promotion recheck and nonblocking repository note

The promoted revision makes both clarifications requested in the first
audit: the proof of Lemma 1.1 now explains why the omitted edge remains
equal-coloured, and Corollary 3.3 explicitly identifies `C` with the lifted
component of `Q-T` containing `ell_e,ell_f`.  The remaining changes are
status and audit-link metadata.  None changes a hypothesis, conclusion, or
proof step, so the GREEN verdict transfers to the promoted revision.

The subsequent revision changes only the relative target of the link to
`hc7_balanced_order8_frontier.md`, prefixing it by `../active/` after the
theorem's relocation to `results/`.  The link now resolves correctly.  This
navigation-only change leaves every mathematical statement and proof step
unchanged, so the GREEN verdict transfers to the final hash recorded above.

## 8. Trust boundary

This audit verifies the exact file revision identified above, conditional
on the explicit balanced order-eight hypotheses and the separately audited
canonical rooted-web and split-edge completion theorems.  It does not audit
the entire upstream five-leaf-star reduction anew.

The audited result proves a repair-or-critical-core structure and closes
three labelled first-hit patterns.  It does not force the nonrepairable edge
to lie on the leaf side, force one of those patterns, synchronize the two
closed-shore boundary colourings, produce an order-seven separation or a
two-vertex minor-model transversal, eliminate the balanced order-eight
configuration, prove `HC_7`, or prove Hadwiger's Conjecture.
