# Internal audit of the full order-eight four-component closure

**Verdict: GREEN.**  This audit checks the exact source revision

```text
1c50f6a2e666c316d99dead9f8e3fbd185c56e87f9bf396229b7b75043994222
```

of
[`hc7_full_order8_four_component_closure.md`](hc7_full_order8_four_component_closure.md).
The theorem is valid under its stated hypotheses.  In particular, the
proper-minor pullback and the final componentwise gluing in Lemma 4 do not
expand any contracted open component and do induce the same exact labelled
partition on the literal eight-vertex boundary.

The source first audited at hash
`f33a241b6b678e92ebd6f8f85f6fe3c4d88f97a5dfcba700453851ab6ac88af9`
was promoted with only its status line changed from “separate audit
pending” to “separate internal audit GREEN.”  The mathematical statement
and proof are byte-for-byte identical after that metadata line, and were
rechecked at the promoted hash.  The only subsequent source changes were
two formatting-only revisions repairing all plain `quad` tokens to `\quad`
in display (3.2).  They leave the seven branch sets and every adjacency
unchanged; the proof was rechecked at the final hash displayed above.

## 1. Hypotheses and component fullness

Let `C` be a component of `G-X`.  By the definition of a component, every
neighbour of `C` outside `C` belongs to `X`.  Hypothesis (1.2) therefore
means exactly that `C` is connected and has a neighbour at every literal
vertex of `X`.  Distinct components of `G-X` are vertex-disjoint and have
no edge between them.  These facts justify every use of a component as a
boundary-full connected subgraph and the final gluing over all components.

The theorem uses the assumption on proper minors only for minors obtained
by contractions and deletions.  The displayed chromatic hypothesis
therefore supplies every six-colouring invoked in the proof.  The
`K_7`-minor exclusion is used only in Lemma 3.

## 2. Audit of the eight-vertex triangle-free lemma

Lemma 2 is correct.  If every component has maximum degree at most three,
Brooks' theorem gives a three-colouring unless the component is complete or
an odd cycle.  A triangle-free complete graph has order at most two, and an
odd cycle is three-colourable, so neither exception causes a problem.

If `d_H(v)>=4`, triangle-freeness makes `N_H(v)` independent.  Since
`|V(H)|<=8`, the set

\[
                       R=V(H)-N_H[v]
\]

has order at most three.  The induced graph `H[R]` is triangle-free and
hence bipartite.  Colouring `N_H(v)` with colour one, `v` with colour two,
and `H[R]` with colours two and three is proper: `v` has no neighbour in
`R`, and every edge from `R` to `N_H(v)` has one endpoint of colour one.
This covers all degree cases and proves `chi(H)<=3`.

## 3. Audit of the triangle lift

In Lemma 3, choose distinct anchors `x_2,x_3,x_4` outside the displayed
triangle.  There are five available vertices, so this choice is possible.
The seven proposed branch sets consist of four component-derived sets and
three triangle singletons.  They are pairwise disjoint and connected.

Every pair of component-derived sets is adjacent: an unanchored component
has an edge to the other set's anchor, and between two anchored sets either
component has an edge to the other's anchor.  Every component-derived set
is adjacent to every triangle singleton by boundary fullness, and the three
singletons are pairwise adjacent by the triangle hypothesis.  Thus all 21
branch-set adjacencies have literal witnesses.  The conclusion is an
explicit `K_7`-minor model, so `G[X]` must be triangle-free.

## 4. Audit of the proper-minor construction in Lemma 4

Fix a proper three-colouring of `H=G[X]` with nonempty colour classes

\[
                       I_1,\ldots,I_p,\qquad 1\le p\le3.
\]

For a target component `C`, at least four components in total guarantee
the existence of `p` distinct components `D_1,...,D_p`, all different from
`C`.  For each `j`, the induced subgraph on `D_j union I_j` is connected:
`D_j` is connected and every vertex of the nonempty set `I_j` has a
neighbour in `D_j`.  These sets are pairwise vertex-disjoint.

Contract a spanning tree of every `D_j union I_j`.  At least one literal
component--boundary edge is contracted, so the result is a proper minor;
deleting the unused components is legal but is not needed to establish
properness.  Let `d_j` be the image of `D_j union I_j`.  For `i ne j`,
fullness of `D_i` supplies an edge from `D_i` to any vertex of `I_j`, so
`d_i d_j` is an edge in the minor.  Hence `d_1,...,d_p` form a clique and
receive pairwise distinct colours in every proper six-colouring.

The pullback is made only to the untouched graph `G[C union X]`; no vertex
of any contracted component is expanded.  Give each `x in I_j` the colour
of `d_j` and retain the minor colouring on `C`.  This is proper for the
following exhaustive reasons.

1. Each `I_j` is independent.
2. Vertices in different classes get distinct colours because their
   representatives form a clique.
3. If `x in I_j` is adjacent to `c in C`, the contraction created the edge
   `d_jc`; hence the retained colour of `c` differs from the colour pulled
   back to `x`.

Therefore the boundary equality partition is exactly
`I_1|...|I_p`, not a coarsening.  Repeating the construction separately for
each component gives a proper colouring of every induced closed piece
`G[C union X]` with this same labelled partition.  The injective maps from
the `p` blocks to the six colour names differ only by a partial
permutation, and each partial permutation extends to a permutation of the
six-colour palette.  After these permutations, all component-side
colourings agree vertex by vertex on `X`.  Distinct components of `G-X`
are anticomplete, so their union is a proper six-colouring of all of `G`.
This contradicts `chi(G)=7` and proves Lemma 4.

## 5. Dependency and novelty comparison

The contraction in Lemma 4 is the same local mechanism as the exact packet
reflection lemma in
[`../results/hc7_exact7_adaptive_packet_reflection.md`](../results/hc7_exact7_adaptive_packet_reflection.md),
Lemma 2.1: each independent boundary block is joined to a distinct full
connected subgraph, the block representatives form a clique, and the
colouring is pulled back only to an untouched side.  That promoted lemma is
stated for a seven-vertex boundary and one opposite closed shore.  Its proof
is boundary-size-independent for a partition having at most six blocks,
but its published statement does not itself cover the present eight-vertex
componentwise application.

The promoted exact-seven multishore theorem in
[`../results/hc7_exact7_multishore_state_synchronization.md`](../results/hc7_exact7_multishore_state_synchronization.md)
also reproduces one attained state component by component, but it assumes a
literal seven-boundary and two specified adjacent carriers with additional
contact duties.  It does not imply Lemma 4 verbatim.  The audited theorem is
therefore a genuine order-eight synthesis of the packet-reflection
construction, the elementary triangle lift, and the sharp fact that every
triangle-free graph on at most eight vertices is three-colourable.

The two-full-shore boundary-absorption theorem is compatible with the
conclusion but is not needed: Lemmas 2 and 3 improve its four-colour bound
to a three-colour bound when four full components are present.

The theorem strictly strengthens Corollary 2 of
[`../archive/hadwiger_hc7_minimum_eight_cut_four_shores.md`](../archive/hadwiger_hc7_minimum_eight_cut_four_shores.md).
That archived result assumes an eight-vertex minimum cut with exactly four
components; minimum-cut status both supplies fullness and enters its cut
inequality.  The present theorem assumes literal fullness directly, permits
any number of components at least four, and does not require `X` to be a
minimum cut.  Every archived instance is therefore covered, while a full
order-eight adhesion need not be a minimum cut.  The strengthening is in
separator scope; it does not replace the archived derivation of fullness
from minimum-cut status.

## 6. Exact limitations

The proof spends three components other than each retained target
component.  With only three components, the packet-plus-clique construction
excludes a boundary `K_4`, but it does not exclude a boundary triangle; and
a target component has only two other components available to fund a
boundary partition.  Thus the argument does not close the two- or
three-component interfaces.

The theorem also does not preserve the seven old boundary labels, the two
named connected subgraphs from the exact-seven first-entry construction,
or either inherited equality partition.  It bypasses those data only in
the four-component case by choosing one fixed three-colour partition of
the new boundary and reproducing it independently on every complementary
component.  No analogous state selection or label-preserving descent is
proved for the remaining two- and three-component cases.
