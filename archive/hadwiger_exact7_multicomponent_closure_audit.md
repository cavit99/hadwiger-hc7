# Adversarial audit: exact-seven multicomponent closure

## Verdict

**GREEN after local wording repairs.**  Fullness, every displayed
\(K_7\)-packing, the repeated-portal pigeonhole argument, the use of the
double-root split-or-cutvertex theorem, and the component restrictions are
all valid.  Combined with the independently audited full-shore block
gluing, every seven-cut in an HC7 minimal counterexample has at most three
components.

## Fullness and elementary packings

For a component \(D_i\) of \(G-S\), a missed root \(s\in S\) gives
\(N(D_i)\subseteq S-\{s\}\), a separator of order at most six from any
other component.  Thus every component is full.

For seven components, the bags \(D_i\cup\{s_i\}\) are pairwise adjacent:
\(D_i\) sees the anchor \(s_j\) of every other bag.  The same argument
with six anchored components and one unused singleton proves the
six-component case.  With five components and a boundary edge \(uv\),
the endpoints are singleton bags and the five components use the other
five roots as anchors.  All seven bags are connected, disjoint and
pairwise adjacent.

## Repeated portals and the five-shore split

When the five-shore boundary is independent, each root has at least seven
neighbours distributed positively among five components.  Hence each root
has a repeated portal class in at least one component.  Assigning seven
roots to five components forces one component to have repeated classes
for two distinct roots.

The double-root theorem gives either a connected adjacent split whose
rows both retain the two roots, or a one-vertex portal separator.

In the split case the two rows cover \(S\).  One row therefore contacts
some \(c\notin\{a,b\}\); anchor it at \(c\) and anchor the other at
\(b\).  The original draft's more informal anchor sentence was replaced
by this exact assignment.  The other four full components use the four
remaining roots, and \(a\) is the seventh singleton bag.

In the cutvertex case, every component \(C\) of \(R-q\) has
\(N(C)\subseteq S\cup\{q\}\).  An untouched full component supplies a
far side, so seven-connectivity gives \(|N_S(C)|\ge6\).  Two portal-side
components therefore have a common boundary set of order at least five.
Choose a common singleton root, two further common anchors, and use the
remaining four roots on the other four full components.  Cross-adjacency
of the two cutvertex pieces is supplied by their common anchors; every
other adjacency follows from fullness.

## Four and three shores

Four full shores plus a boundary triangle give four anchored shore bags
and three singleton bags.  Three full shores plus a boundary \(K_4\)
give three anchored shore bags and four singleton bags.  Hence a surviving
four-shore boundary is triangle-free and a surviving three-shore boundary
is \(K_4\)-free.

The new triangle-split and triangle-cutvertex lemmas are also valid.  In a
split row pair sharing a boundary triangle, row coverage and nonempty
outside contacts give distinct representatives among the other four
roots.  In the cutvertex case, two six-contact pieces have a common set of
at least five roots; a triangle in that intersection leaves two common
anchors.  These assignments give the four component-derived bags needed
beside three singleton triangle bags.

## Full-shore block gluing

Theorems 1.1--1.3 of `hadwiger_full_shore_block_gluing.md` are sound.
Opposite full shores make each selected colour block connected; the
contracted block images form the required clique.  An \(r\)-colouring of
the proper minor expands over the retained side, because every edge from
a boundary block to that side survives incident with its contracted
image.  Identical labelled equality partitions align by a palette
permutation and glue across pairwise anticomplete components.

The singleton and clique-residual variants require \(m\ge2\), now stated
explicitly.  The support-efficient minor theorem is valid for
\(p,q\ge1\): one full component is left unanchored, the other \(q-1\)
use distinct roots outside the support of the boundary model.

Every triangle-free graph on at most seven vertices is three-colourable.
The proof by induction is complete: at minimum degree at least three, a
shortest odd cycle is an induced \(C_5\); the two remaining vertices must
be adjacent and have disjoint independent pairs of cycle neighbours,
leaving one cycle vertex of degree two.

Consequently the four-shore branch is impossible.  In the three-shore
branch, a three-colouring has no singleton class, and the four-chromatic
small-support argument reduces the boundary to the Moser spindle and its
one-edge extension.  The extension has the proper five-block partition

\[
25\mid46\mid0\mid1\mid3,
\]

whose singleton residue is the triangle \(013\); clique-residual block
gluing excludes it.  Thus the only four-chromatic three-shore boundary is
the pure Moser spindle.

The exact finite verifier `exact7_multicomponent_quotient_atlas.py`
independently confirms the reductions.  Among the quotient-negative
\(K_4\)-free boundaries, all clique-residual block colourings leave nine
three-chromatic types and exactly one four-chromatic type, the pure Moser
spindle.  This computation is a diagnostic confirmation; the four-
chromatic theorem itself uses the audited seven-vertex small-support
classification.
