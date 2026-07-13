# Tree-pole rotation exchange for a rural carrier

**Status:** proved and independently audited.
It replaces a vague "rotation obstruction" by two literal disjoint
carriers joining alternating attachment occurrences.  It is local: it does
not assert that the rest of a terminal shore is planar, and it does not by
itself turn the two carriers into a `K_7` model or a common colour state.

## 1. Occurrence societies

Let `T` be a tree and let there be at least one attachment occurrence.
An **attachment occurrence** `omega` has a specified
base `b(omega) in V(T)`.  Different occurrences may have the same base.
Let

\[
                  \Omega=(\omega_1,\ldots,\omega_m)             \tag{1.1}
\]

be a cyclic ordering of the occurrences.  Form the occurrence expansion
`widehat T` by adjoining, for every `omega`, a new leaf `ell_omega` at
`b(omega)`.  A disk realization of `(T,Omega)` means a drawing of
`widehat T` in a closed disk whose intersection with the disk boundary is
exactly the set of occurrence leaves, which occur there in the cyclic
order (1.1).

For an edge `e` of `T`, the two components of `T-e` induce a bipartition
of the occurrences according to their bases.  Call this an **edge split**.
A part of an edge split is a **circular interval** if its occurrences are
consecutive in (1.1), allowing wraparound.

## 2. Exact circular-split criterion

### Theorem 2.1 (tree-pole rotation dichotomy)

Exactly one of the following outcomes occurs.

1. `(T,Omega)` has a disk realization.
2. There are four occurrences in cyclic order

   \[
                         a,b,c,d                              \tag{2.1}
   \]

   and an edge `e in E(T)` such that the bases of `a,c` lie in one
   component of `T-e`, while the bases of `b,d` lie in the other.
   Consequently the unique `b(a)-b(c)` path and the unique
   `b(b)-b(d)` path in `T` are vertex-disjoint.

Equivalently, outcome 1 holds if and only if every edge split of `T` is a
circular interval of `Omega`.

#### Proof

First suppose a disk realization exists.  If an edge split were not a
circular interval, there would be occurrences `a,b,c,d` in cyclic order
with `a,c` based in one component of `T-e` and `b,d` in the other.  The
two corresponding paths in `widehat T` are disjoint arcs in the disk
joining alternating boundary points.  This is impossible by the Jordan
curve theorem.  Hence every edge split is a circular interval.

Conversely, suppose every edge split is a circular interval.  Delete from
`widehat T` every vertex and edge outside the minimal subtree spanning the
occurrence leaves, and suppress unlabelled vertices of degree two.  These
operations neither change the edge-split condition nor the disk-realization
question.  We induct on the number of remaining internal vertices.

If there is at most one internal vertex, the tree is a star and its leaf
edges can be drawn radially in the prescribed order.  Otherwise choose an
internal vertex `u` farthest from an arbitrary internal root.  All but one
of the edges at `u` lead directly to occurrence leaves; let `B` be this
nonempty set of leaves.  The edge from `u` toward the root separates `B`
from all other occurrence leaves, so `B` is a circular interval.  Replace
the whole pendant star at `u` by one temporary occurrence leaf occupying
that interval.  Every edge split of the smaller tree is still a circular
interval in the contracted cyclic order.  By induction the smaller tree
has a disk realization.  In a small boundary neighbourhood of the
temporary leaf, replace it by the star at `u`, putting the leaves of `B`
in their original consecutive order.  This gives the desired realization
of `widehat T`.

Finally, if an edge split is not a circular interval, choose two
occurrences of that part separated in the cyclic order by occurrences of
the other part.  They give (2.1).  Their two unique base-to-base paths lie
in different components of `T-e`, and are therefore vertex-disjoint.
This proves the dichotomy. \(\square\)

The paths are allowed to have length zero when two occurrences have the
same base.  In that event the corresponding one-vertex connected carrier
is still literal and remains disjoint from the path on the other side of
`e`.

## 3. Connected poles

### Corollary 3.1 (rotation failure gives two literal carriers)

Let `X` be a connected subgraph used as one contracted pole of a plane
quotient, and assign every quotient edge at that pole to its literal end
in `X`.  Let `rho` be the rotation of those edge occurrences in the
quotient.  Choose an edge-minimal connected subgraph `T` of `X` containing
all attachment bases.  Then `T` is a tree, and exactly one of the
following occurs.

1. The chosen pole connector `T`, together with all attachment stubs, can
   replace the quotient pole locally while respecting `rho`.
2. There are two vertex-disjoint connected subgraphs of `X`, each joining
   a pair of literal attachment bases, and the four corresponding quotient
   edge occurrences alternate in `rho`.

#### Proof

Edge-minimal connectivity makes `T` a tree.  Apply Theorem 2.1 to the
attachment occurrences based on `T`.  Its disk outcome is precisely the
local substitution in item 1.  In its other outcome, take the two unique
tree paths.  They are literal vertex-disjoint connected subgraphs of `X`
and have the stated alternating endpoints. \(\square\)

Extra host edges inside `X` are irrelevant to this connector statement:
the selected connected subgraph is what is expanded.  Accordingly item 1
does **not** prove that the whole induced graph on `X` is disk-embeddable.
This distinction is essential for the fixed two-apex endgame.

## 4. Application to the exact-six rural page

In the literal two-pole planar quotient of
`../active/hc7_exact7_rural_bilateral_endgame.md`, apply Corollary 3.1
separately to
the poles

\[
                         A\cup B,\qquad L.                    \tag{4.1}
\]

There is no longer an unspecified rotation obstruction.  For either pole,
one obtains a compatible local connector or two disjoint literal carriers
whose attachment pairs alternate in the fixed selected block-terminal rib
rotation.  Thus the remaining constructive HC7 step has the following
exact input:

> **Alternating-carrier conversion.**  In the exact-six Moser cell, turn
> the two disjoint carriers returned by Corollary 3.1 into a labelled
> carrier peel, an admissible-rank promotion, a literal `K_7` model, or a
> boundary state reproducible on the opposite shore.

This target uses actual paths and literal attachment ends.  It has no
palette-to-label lift and no choice among incompatible web completions.
It still needs the Moser/core incidences to convert the two carriers into a
terminal outcome.
