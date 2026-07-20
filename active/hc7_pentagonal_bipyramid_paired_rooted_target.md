# Paired-rooted `K_5` target for the pentagonal-bipyramid core

**Status:** conjectural target with proved terminal reductions.  This file
defines the exact root-alignment conclusion needed in the five-connected
spanning core.  The dichotomy in Theorem 3.1 is not proved.

## 1. Literal root-neighbourhood sets

Let `G` contain two disjoint connected subgraphs `R_0,R_1` which are
adjacent to one another.  Let `F` be a subgraph disjoint from the roots and
put

\[
 A=N_G(R_0)\cap V(F),
 \qquad
 B=N_G(R_1)\cap V(F).                                      \tag{1.1}
\]

A `K_5`-minor model `M_1,...,M_5` in `F` is **paired-rooted at `(A,B)`**
when

\[
                         M_i\cap A\ne\varnothing,
 \qquad
                         M_i\cap B\ne\varnothing
 \quad(1\le i\le5).                                      \tag{1.2}
\]

No matching is prescribed between individual vertices of `A` and `B`.
The same vertex may belong to both sets, and a branch set may meet the two
sets in different original columns.  This is deliberately weaker than
requiring each `M_i` to contain a whole column.

### Lemma 1.1 (paired-rooted completion)

If `F` has a paired-rooted `K_5` model, then `G` has a `K_7` minor.

### Proof

The five branch sets are connected, disjoint and pairwise adjacent.  By
(1.1)--(1.2), each is adjacent to both root subgraphs.  The roots are
connected, disjoint and adjacent to one another.  Hence

\[
                         R_0,R_1,M_1,\ldots,M_5
\]

are seven branch sets of a `K_7` model. \(\square\)

## 2. The spanning pentagonal-bipyramid setup

In the audited spanning-core theorem, the roots are

\[
                         R_0=G[\{v,p\}],
 \qquad
                         R_1=G[\{w\}],
\]

where `vp,pw` are edges and `vw` is a nonedge.  The graph

\[
                         F=G-\{v,p,w\}
\]

is partitioned into seven nonempty connected columns whose contact graph
is the pentagonal bipyramid.  Every column meets both sets `A,B`; indeed,
the original construction retains a path from a neighbour of one root to
a neighbour of the other.

The same theorem proves

\[
                    \kappa(F)\ge4,
 \qquad
                    \chi(F)\ge5,
 \qquad
                    F\text{ is nonplanar}.                   \tag{2.1}
\]

If `F` has a four-cut `X`, then

\[
                         X\cup\{v,p,w\}                       \tag{2.2}
\]

is a full literal order-seven boundary.  The unresolved issue in that
branch is equality-partition compatibility of the two closed-shore
six-colourings.

If there is no four-cut, then `F` is five-connected.  Kelmans--Seymour
gives an unrooted subdivision of `K_5`, but does not ensure (1.2).

## 3. Exact no-four-cut target

### Conjectural Theorem 3.1 (chromatic or paired-rooted `K_5`)

Let `F` be a five-connected graph partitioned into seven nonempty connected
columns whose contact graph is the pentagonal bipyramid.  Let `A,B` be
vertex sets meeting every column, with each column containing an
`A`--`B` path.  Then at least one of the following holds.

1. `F` is four-colourable.
2. `F` contains a `K_5`-minor model paired-rooted at `(A,B)`.

The statement is intentionally chromatic rather than planar.  Finite
combined-negative expansions can be nonplanar and four-colourable.

### Corollary 3.2 (why the target closes the five-connected branch)

Assume Theorem 3.1.  In the spanning-core setup, outcome 1 contradicts
`\chi(F)\ge5`.  Equivalently, one may four-colour `F`, give the nonadjacent
vertices `v,w` one fresh colour, and give `p` a sixth colour, contrary to
`\chi(G)=7`.  Outcome 2 gives a `K_7` minor by Lemma 1.1.  Therefore no
hypothetical counterexample reaches the no-four-cut pentagonal-bipyramid
branch.

## 4. Evidence and exact remaining gap

Two independent fourteen-vertex combined-negative expansions now support
the formulation.

- One has an explicit distributed `K_5` model obtained by absorbing pieces
  of two omitted columns.
- The other has no model whose five bags contain five distinct whole
  columns, but it has the paired-rooted model

  \[
  \begin{aligned}
   &\{(0,0),(0,1)\},\quad \{(2,0),(2,1)\},\\
   &\{(1,0),(3,1)\},\quad \{(5,0),(6,1)\},\\
   &\{(1,1),(3,0),(4,1)\},
  \end{aligned}
  \]

  and is also exactly four-colourable.

These are finite certificates, not a proof of Theorem 3.1.  Hegde--Thomas
enlargements of the abstract pentagonal bipyramid also do not prove the
target by themselves: some type-5 enlargements admit portal assignments
with no paired-rooted `K_5`, although those enlargements have connectivity
only three or four rather than five.

The precise structural gate is therefore:

> use five-connectivity, or the operation-specific contraction-critical
> colouring responses, to eliminate the paired-rooted-negative type-5
> enlargement; otherwise return a full order-seven boundary with compatible
> shore colourings.

No theorem in this file supplies that gate.

## 5. Structural interpretation of persistent planar reroutings

The planar outcomes are part of the intended conclusion, not merely failed
attempts to create another contact.  The audited expansion results establish
the following pattern at increasing levels of generality.

1. A connected split of one column whose four distinct old neighbour labels
   alternate in the plane rotation of the pentagonal bipyramid gives an
   explicit `K_7`-minor model.
2. For tree expansions, one family of compatible portal orders embeds the
   entire core in the plane.  In the single-contact family this is exhaustive:
   a nonconforming split gives `K_7`, while conforming splits give a planar
   core and hence a six-colouring of the host.
3. The same dichotomy holds for four-connected single-contact columns after
   replacing tree-edge intervals by the facial order of the portal vertices.
4. In the first repeated-contact finite laboratory, all five local linkage
   obstructions together with the absence of an alternating split force
   four-colourability.

Thus a persistent sequence of conforming reroutings should be assembled into
one compatible planar expansion and treated as outcome 1 of Conjectural
Theorem 3.1.  The alternative must be a genuinely nonconforming global
attachment, decoded into a paired-rooted `K_5` rather than into one more local
residue.

Existing structure theorems do not perform this labelled assembly
automatically.  Hegde--Thomas produces an abstract nonplanar enlargement but
does not preserve the two root-neighbourhood sets.  Norin--Thomas Lemma (9.8)
starts from a feasible mold on a homeomorphic embedding; complete adjacency
of the two roots to the seven selected minor-model columns supplies neither
that homeomorphic embedding nor the internally disjoint cast required for
mold feasibility.  These are precise missing hypotheses, not reasons to
discard the planar alternative.

## 6. Spanning five-part normalization

The [spanning two-sided packing theorem](../results/hc7_spanning_two_sided_five_partition.md)
removes all ambient leftovers from the target.  Five disjoint connected
subgraphs meeting both `A` and `B` may be chosen first to maximize the number
of edges in their contact graph and then to maximize their covered vertex
set.  They necessarily partition `V(F)`.  If their contact graph is complete,
they give the paired-rooted model immediately.

Consequently a counterexample to Theorem 3.1 may be normalized as a spanning
five-part connected partition, every part meeting both root-neighbourhood
sets, whose contact graph is not complete.  This normalization is
well-founded and unbounded, but it does not force the missing contacts:
nonplanarity and chromatic complexity may remain inside one part.  The next
theorem must use the inherited pentagonal-bipyramid ownership or the
operation-specific proper-minor colourings to turn that internal complexity
into either a new contact, an exact order-seven compatible separation, or a
four-colouring.

## 7. A weaker root allocation already gives a structural exit

Full paired rooting is stronger than necessary.  The
[one-defect two-root theorem](../results/hc7_one_defect_two_root_k5_separator.md)
proves that if all five bags of a `K_5` model meet one of `A,B` and at least
four meet the other, then `G` has a `K_7` minor or a genuine
full-neighbourhood separation.  The latter need not have order seven and no
common boundary colouring is yet known, so it is a structural exit rather
than a terminal colouring conclusion.

The exact type-5 endpoint census sharpens the finite enlargement laboratory.
Of the 340 paired-rooted-negative assignments, 320 have a one-defect model
in one orientation.  The remaining 20 are exactly the **doubly confined**
assignments: both root-neighbourhood sets meet only the retained-edge side in
both split fibres.  Thus type-5 enlargement casework has been compressed to
one label-placement obstruction.  This finite classification does not align
an abstract enlargement minor with the host columns, and the doubly confined
case remains an unbounded label-preserving problem.

## Immediate proved inputs and barriers

- [spanning pentagonal-bipyramid core](../results/hc7_pentagonal_bipyramid_spanning_core.md)
- [seven-column contact-graph structure](../results/hc7_seven_column_contact_structure.md)
- [spanning two-sided five-part normalization](../results/hc7_spanning_two_sided_five_partition.md)
- [one-defect two-root completion or full-neighbourhood separation](../results/hc7_one_defect_two_root_k5_separator.md)
- [exact type-5 paired-root endpoint allocation](../results/hc7_pentagonal_bipyramid_type5_endpoint_allocation.md)
- [exact type-5 one-defect allocation](../results/hc7_pentagonal_bipyramid_type5_one_defect_allocation.md)
- [minimum-degree alignment in one canonical type-5 orbit](../results/hc7_pentagonal_bipyramid_type5_minimum_degree_alignment.md)
- [alternating split and adjacent-rim linkage completions](../results/hc7_pentagonal_bipyramid_adjacent_rim_linkage.md)
- [two-column absorption](../results/hc7_pentagonal_bipyramid_two_column_absorption.md)
- [finite two-vertex path-column four-colour theorem](../results/hc7_pentagonal_bipyramid_two_vertex_path_census.md)
- [local split/linkage tests are not an exhaustive unbounded dichotomy](../barriers/hc7_pentagonal_bipyramid_split_linkage_planarity_barrier.md)
- [abstract enlargement minors do not preserve the two root sets](../barriers/hc7_hegde_thomas_pentagonal_bipyramid_label_gap.md)
- [root-to-column adjacency does not imply mold feasibility](../barriers/hc7_root_contacts_do_not_form_a_feasible_mold.md)
