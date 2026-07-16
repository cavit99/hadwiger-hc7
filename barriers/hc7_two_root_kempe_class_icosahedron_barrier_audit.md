# Audit of the two-root Kempe-class icosahedron barrier

**Status:** separate internal audit

**Verdict:** **GREEN**
**Audit date:** 2026-07-16

## Revision audited

- theorem note:
  `hc7_two_root_kempe_class_icosahedron_barrier.md`
- theorem-note SHA-256:
  `a43cc0939aedd91b741fff43f08b3695cf5556f66c26e6c4e5458d4d9a525a94`
- deterministic checker:
  `hc7_two_root_kempe_class_icosahedron_barrier_verify.py`
- checker SHA-256:
  `64493ba2de21bd99a4ab388097dd0fff6f12cdd9d3840944cb6610b72dc45000`

Any mathematical change to the theorem note or checker requires a new
audit.

## Statement audited

The note gives an explicit graph

\[
 J=K_2\vee I,
 \qquad
 G=K_2\vee(I+\{a,b\}),
\]

where `I` is the displayed icosahedral graph and the adjacencies of the
nonadjacent roots `a,b` inside `I` are prescribed.  It claims that the
following conditions do not force the two exclusive root-dominating
orientations to lie in one Kempe class:

1. `J` is six-chromatic and `K_7`-minor-free;
2. every proper six-colouring of `J` makes at least one root adjacent to
   every colour class, and both exclusive orientations occur;
3. `J` has a spanning five-branch-set `K_5` model whose branch sets are all
   adjacent to both roots;
4. `G` is seven-connected; and
5. contracting any edge incident with either root leaves a six-colourable
   graph.

More precisely, the ten unordered six-colouring partitions of `J` are ten
different Kempe components: four have only `a` colour-dominating and six
have only `b` colour-dominating.  The note also expressly limits the
example: `G` has both a `K_7` minor and an actual order-seven separation,
so it does not refute the proposed three-outcome theorem or `HC_7`.

## Audit method

I used two checks.

1. I inspected the written deductions and the committed checker line by
   line.
2. I independently reimplemented the graph from the displayed adjacency
   lists, using a different backtracking order and different graph data
   structures.  That independent calculation:

   - enumerated all 240 labelled proper four-colourings of `I`;
   - recovered ten unordered partitions, with orientation split `4+6`;
   - checked all two-block induced subgraphs for all ten partitions;
   - checked five-connectivity of `I+{a,b}` and seven-connectivity of `G`;
   - directly six-coloured all fourteen contractions of root-incident
     edges, including the four root--apex edges handled only in prose by
     the committed checker;
   - checked both displayed minor models; and
   - checked the displayed order-seven neighbourhood cut.

The committed checker itself ran to completion with its documented output
and ended with `ALL CHECKS PASSED`.

## Detailed findings

### 1. Icosahedral graph and notation — GREEN

The twelve displayed adjacency lists are symmetric, every vertex has
degree five, and they give exactly thirty edges.  The checker finds twenty
triangular faces, every edge lies in exactly two of them, every vertex link
is a cycle, and the resulting connected closed surface has Euler
characteristic two.  This verifies the intended spherical icosahedral
embedding.  Exhaustive deletion of fewer than five vertices verifies
five-connectivity.

No adjacency-list entry is malformed or missing.  The checker's mixed-label
edge normalisation orders endpoints lexicographically by their string
representations; this is unusual but harmless here because it is applied
consistently to every derived edge set.  The purely integer face check uses
ordinary numerical ordering consistently.

The notation `I+{a,b}` is explained immediately before its use as adding
the two roots with the displayed neighbourhoods; it is not being used as
an unqualified graph-join identity.

### 2. Connectivity of the ambient graph — GREEN

Adding a vertex having at least five neighbours to a five-connected graph
preserves five-connectivity: after deleting at most four vertices, the old
graph remains connected and at least one neighbour of the new vertex
remains.  Applying this successively to `a` and `b` proves that
`F=I+{a,b}` is five-connected.

For `G=K_2\vee F`, deleting at most six vertices either leaves one of the
two universal adjacent vertices, or deletes both and at most four vertices
of `F`.  Hence `G` is seven-connected.  Since `a` has exactly seven
neighbours and deleting them isolates `a` from other surviving vertices,
the connectivity is exactly seven and that neighbourhood is an actual
order-seven separator.  Both the committed and independent exhaustive
checks agree.

### 3. Chromatic and minor claims for `J` — GREEN

The colouring enumeration has no colouring with an unused one of its four
colours, so it also certifies that `I` is not three-colourable.  Since the
listed four-colourings exist, `chi(I)=4`; therefore
`chi(K_2\vee I)=6`.

The proof that `J` is `K_7`-minor-free is sound.  From any hypothetical
seven-branch-set model, discard the at most two branch sets meeting the two
universal vertices.  At least five pairwise adjacent connected branch sets
remain wholly in the planar graph `I`, giving a forbidden `K_5` minor of a
planar graph.  This also covers the cases in which one or both universal
vertices are unused or occur in the same branch set.

### 4. Complete colouring and Kempe-component certificate — GREEN

The committed checker exhausts all proper four-colourings of `I`, not a
preselected list.  It obtains 240 labelled colourings and exactly the ten
unordered partitions printed in the note.  Each partition has four
nonempty classes.  Inspection of the two root neighbourhoods verifies that
exactly one root meets all four classes in every row, with four `a` rows
and six `b` rows.

In `J`, the two universal vertices occupy two additional singleton colour
classes.  For every printed partition, every union of two `I`-classes is
connected.  A union involving either universal singleton is also
connected, as is the union of the two universal singleton classes.
Consequently every bichromatic subgraph is connected, so a Kempe
interchange can only exchange two entire colour classes.  Thus the
unordered partition is invariant.  Conversely, whole-class interchanges
generate all palette permutations.  Each component therefore has
`6!=720` labelled colourings, and the ten partitions are exactly the ten
Kempe components.  The independent enumeration reproduced all of these
structural checks and the `4+6` orientation split.

The deduction `chi(F)=5` is also correct: no four-colouring of `I` extends
to both roots, while assigning the two nonadjacent roots one new common
colour gives a five-colouring.  Hence `chi(G)=chi(F)+2=7`.

### 5. Spanning root-adjacent `K_5` model — GREEN

The five displayed sets are disjoint, partition `V(J)`, induce connected
subgraphs, and are pairwise adjacent.  Each has an edge to each root.  The
committed checker and the independent model check both verify these facts.

### 6. Every root-edge contraction — GREEN

For each of the ten root--icosahedron edges, the committed checker both
finds the stated exact trace in the complete colouring enumeration and
directly four-colours the corresponding contraction inside `F`.  Joining
the contracted graph with `K_2` gives the required six-colouring in `G`.

For the four root--apex edges, the written construction is valid.  After
contracting one such edge, the merged vertex and the other universal vertex
use two colours; an exclusive row of the appropriate opposite orientation
four-colours the remaining `I` plus the other root.  My independent solver
also directly verified six-colourability after all fourteen root-incident
edge contractions.

### 7. Trust boundary — GREEN

The seven displayed branch sets for the `K_7` minor are disjoint,
connected and pairwise adjacent.  Thus `G` is deliberately outside the
`K_7`-minor-free hypothesis of a hypothetical `HC_7` counterexample.  The
displayed neighbourhood of `a` is the actual order-seven separator checked
above.  Since a proper minor sequence reaches a seven-chromatic `K_7`, `G`
also fails the required proper-minor criticality.

The note therefore draws the correct negative conclusion and no stronger
one: universal two-root domination, opposite exclusive witnesses,
seven-connectivity, the spanning root-adjacent model, and every root-edge
contraction trace do not by themselves force an orientation-changing
Kempe sequence.  A valid positive theorem must essentially use exclusion
of the `K_7`-minor/separator outcomes or stronger global proper-minor
criticality.

## Residual assumptions and limitations

There is no mathematical gap in the stated barrier.  Its intended scope is
strictly intermediate: it is not a counterexample to the full proposed
trichotomy, to a theorem assuming the entire proper-minor criticality
package, or to `HC_7`.  The planarity-based proof that `J` is
`K_7`-minor-free is a written mathematical deduction rather than an
exhaustive minor search; that deduction is complete.
