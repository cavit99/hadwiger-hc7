# Audit of the edge-critical balanced order-eight lemmas

**Verdict:** GREEN as a collection of conditional lemmas.

**Audited source:**
[`hc7_balanced_order8_edge_critical_completion.md`](hc7_balanced_order8_edge_critical_completion.md)

**Current source SHA-256:**
`e3f0247d611e4f1528d9b287f4f5529acba390fd9f8c0dcbee5e043ef8185780`

**Pre-promotion source SHA-256:**
`c6ea52bcfea3b443139b49844bf66e3513b4bd8132a195b821835b53a828c45c`

**Original audited revision SHA-256:**
`fc7eceadd5cd9935dbdb9d8c97eb770e47c2c50d1e5f36c58ae115466cc60bdc`

The current source differs from the original audited revision only in its
opening status paragraph and, after promotion from `active/` to `results/`,
in the relative paths of two links to results in the same directory and
one link back to the active balanced-order-eight frontier.
Mechanically restoring the original seven-line title/status block and the
three pre-promotion link paths while leaving the theorem text unchanged
reproduces the original audited SHA-256 exactly.  The intermediate
pre-promotion revision has the separately recorded hash above.  No setup
assumption, lemma, proof, corollary, or scope claim changed.  The GREEN
verdict therefore rebinds to the current source hash above.

This audit does not claim that the remaining balanced order-eight case,
the support-six programme, or `HC_7` is proved.

## 1. Setup and dependency boundary

The source explicitly assumes that the open component called `C` contains
both omitted vertices `ell_e,ell_f` of the original five-clique, and cites
the placement of every vertex of `Y-S` in the opposite component `D`.
These are legitimate orientations of the two open components in the
canonical order-eight branch, supplied by Theorem 3.2 of
[`hc7_star_order_eight_rooted_web.md`](hc7_star_order_eight_rooted_web.md).
They are not consequences of boundary fullness alone.  The proofs audited
below correctly import this placement and the labelled defect-edge
contacts in Section 1.

## 2. Lemma 2.1

The proof is correct.

- Deleting `ell_e ell_f` gives a proper minor and hence a six-colouring.
  Its endpoints must be monochromatic; otherwise restoring the edge would
  give a six-colouring of `G`.
- The other three vertices of the five-clique use three distinct colours,
  all different from the common leaf colour.  Hence exactly two of the six
  colour names are absent from the five vertices in the edge-deleted
  colouring.
- If the two leaves lay in different components of either relevant
  two-colour subgraph, swapping those two colours on the component
  containing one leaf would preserve properness and separate the leaf
  colours.  The deleted edge could then be restored, a contradiction.

The same argument actually works for every colour distinct from the common
leaf colour; the stated two absent colours are the two connections not
already witnessed by a two-edge path through a vertex of `R`.

## 3. Promoted split-edge completion

Section 3 cites the separately promoted theorem rather than duplicating
its proof.  I independently rechecked its seven branch sets and all 21
pairwise adjacencies.

There are three adjacencies among the singleton vertices of `R`, twelve
between those three singleton sets and the other four branch sets, and six
among the other four branch sets.  In particular:

- collective adjacency of `e` to `R` is sufficient for the three
  `V(e)`--`R` branch-set adjacencies; no common endpoint is required;
- the two leaf vertices give the `P`--`R`, `Q`--`R`, and `P`--`Q`
  adjacencies;
- boundary fullness of the opposite component gives its contacts with
  `R`, `V(e)`, and `x`; and
- splitting the endpoints of `f` gives both connectivity of the two
  enlarged branch sets and their mutual adjacency.

No individual endpoint-to-all-of-`R` contact is used.  The cited theorem is
therefore valid under the stated collective-contact hypotheses.

## 4. Theorem 4.1 and Corollaries 4.2--4.3

The neighbourhood identity

\[
 N_G(A)=(N_G(A)\cap S)\mathbin{\dot\cup}
        (N_G(A)\cap\{\ell_e,\ell_f\})
\]

is exact: different components of `C-{ell_e,ell_f}` are anticomplete,
and distinct components of `G-S` are anticomplete.  Connectedness of `C`
ensures `t(A)>=1`.

The set `N_G(A)` separates the nonempty set `A` from the nonempty opposite
component `D`.  Seven-connectivity gives order at least seven; if its order
were exactly seven, it would be an actual order-seven separation.  Under
the theorem's exclusion this yields

\[
 |N_G(A)\cap S|+t(A)>=8.
\]

The branch model in (4.2) has exactly seven disjoint connected sets.  All
pairwise adjacencies check.  The potentially delicate ones are valid:

- `V(h) union {ell_e,ell_f}` is connected because `h` contacts the leaf it
  does not omit, and the leaves are adjacent;
- it is adjacent to `V(g)` because `g` also contacts the leaf it does not
  omit;
- `A union {x}` contacts the leaf-containing set because every component
  `A` contacts at least one deleted leaf; and
- collective contacts of `g,h` with `R` are used only for branch-set
  adjacency, where they suffice.

The numerical consequences are exact: for `t(A)=1` the boundary degree is
exactly seven; for `t(A)=2` it is six or seven.  In both cases at least one
missed boundary vertex belongs to `R union {x}`.

Corollary 4.2 correctly places the interior of a simple leaf-to-leaf path
in one component after the leaves are deleted.  Such a path in the
edge-deleted graph is nontrivial, so that component exists and contacts
both leaves.

For Corollary 4.3, a two-leaf component contacting `x` has at least six
boundary neighbours.  At most four of these can lie in `R union {x}`, so
it contacts at least two of the four endpoints of `e,f`, and hence at
least one of the two edges.  Deleting the two artificial terminal vertices
from a linkage in the auxiliary graph produces exactly the two disjoint
connected subgraphs required by the promoted split-edge completion.  The
forbidden-linkage conclusion follows.

## 5. Lemmas 5.1--5.2 and Corollary 5.3

The gluing argument is correct.

- A minor operation internal to `D` and not identifying `D` with `S`
  leaves the closed subgraph `G[C union S]` unchanged.  Its minor colouring
  therefore restricts to a proper colouring of that original closed shore,
  including `ell_e ell_f`.
- The edge-deletion colouring restricts to a proper colouring of the other
  original closed shore `G[D union S]`; the only host edge whose endpoints
  can be monochromatic is `ell_e ell_f`, and neither endpoint lies in this
  closed shore.
- Equality of the induced partitions of `S` gives a bijection between the
  colour names occurring on the boundary.  It extends to a permutation of
  the six colour names, after which the two colourings agree vertex by
  vertex on `S` and glue.

Thus a proper-minor response internal to `D` returning the specified
boundary partition would indeed six-colour `G`.

Lemma 5.2 is the symmetric two-edge version of the same argument and is
also correct.  If `uv` lies wholly in `C` and `yz` wholly in `D`, a
colouring of `G-yz` is proper on the original `C`-shore, while a colouring
of `G-uv` is proper on the original `D`-shore.  Agreement of their boundary
partitions permits the same colour-name alignment and gluing.  Notice that
the lemma does not require either deleted edge to be monochromatic for this
argument.

The count in Corollary 5.3 is exact.  Since `Y` is disjoint from `L`, it
contains no vertex of `R`.  Since `e` and `f` are anticomplete, a clique can
meet endpoints of at most one of them, and it can additionally contain
`x`.  Hence `|Y cap S|<=3`; the cited rooted-web placement puts at least two
vertices of `Y-S` in `D`, where they form an edge.  Lemma 5.2 says that any
six-colourings after deleting this edge and after deleting
`ell_e ell_f` have different boundary partitions.  Applying the Kempe-swap
argument from Lemma 2.1 inside the five-clique `Y` correctly gives two
bichromatic components joining the two deleted-edge endpoints, one for
each colour absent from `Y`.

## 6. Scope notes

No audited statement proves that either Kempe component has a path wholly
inside `C`, that the two required paths are disjoint, or that a proper
minor internal to `D` returns the edge-deletion boundary partition.  These
are correctly left as the host-level obstruction in Section 6.

The final paragraph correctly identifies an open transition problem.  In
particular, the existence of two incompatible edge-deletion partitions
does not itself force a transition between them, and the source does not
claim otherwise.
