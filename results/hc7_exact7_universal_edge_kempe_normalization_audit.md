# Audit of universal-edge Kempe normalization

**Verdict:** GREEN for the exact draft revision identified below.

## Audited revision

The audited file is
`results/hc7_exact7_universal_edge_kempe_normalization.md`.

**Source SHA-256:**
`f2ae7f267ad2026c532b55d29189f4ba097b1c51ed31a702c4b66b4e63c4fb1c`.

The mathematical source was audited at SHA-256
`5a5a5f3333efe63831ed941e07b8e710ece1cc653e697f6b355238972a4d89c0`.
The promoted revision changes only the status line from “separate internal
audit pending” to “separate internal audit GREEN”; restoring the former
line reproduces the audited hash exactly.  No theorem statement,
hypothesis, proof, or trust-boundary text changed.

The verdict covers Theorem 2.1, both uses of the Kriesell--Mohr
pseudoforest theorem, the two shore-colouring gluing arguments, and the
explicit `K_7`-minus-one-edge model.  It does not assert that any of the
three residual cases in Section 3 is closed.

## 1. Minimum boundary colour count

In every six-colouring of `G-pq`, the endpoints `p,q` have one common
colour `alpha`; otherwise the deleted edge could be restored.  Since each
is adjacent to every vertex of the five-cycle `C`, `alpha` is absent from
`C`.  Properness of the odd cycle gives `3<=m(c)<=5`.

If `m(c)=5`, the five roots on `C` have distinct colours.  For every edge
`xy` of the complementary five-cycle `D`, a Kempe interchange would lower
`m(c)` unless `x,y` lie in one component of their two colour classes.
Restricting the host to the five root-colour classes removes the extra
`alpha` class and retains all these connections.  Kriesell--Mohr Theorem 5
applies because `D` is connected with one cycle.  It returns five disjoint
connected rooted sets adjacent along the edges of `D`.  Every nonedge of
`D` is an edge of the literal cycle `G[C]`, so root edges supply all the
remaining adjacencies.  The five sets form a rooted `K_5` model and avoid
`p,q`; adjoining the adjacent universal singletons `{p},{q}` gives a
`K_7` model.  Thus `m(c)` is three or four.

## 2. Absent-colour shore paths and gluing

Let `beta` be absent from the boundary.  On a closed shore, if `p,q` lie
in different `{alpha,beta}` components after deleting `pq`, switching the
component containing `p` changes no boundary vertex except `p`: `beta` is
absent from `S`, while `alpha` occurs there only at `p,q`.  Restoring `pq`
then gives a proper colouring of that closed shore and splits the boundary
block `{p,q}`.

If both shores admitted that switch, the two closed-shore colourings would
induce the same equality partition and could be aligned by a permutation
of six colour names.  They would glue to a six-colouring of `G`.
Consequently at least one shore contains the stated bichromatic `p-q`
path.  No internal vertex of such a path is in `S`, since `p,q` are the
only boundary vertices with either palette colour, so all internal
vertices lie in one open shore.

When `m(c)=3`, the boundary uses `alpha` and three cycle colours, leaving
exactly two absent colours.  If no shore carried both corresponding paths,
each path would occur on exactly one shore and the two occurrences would
be opposite.  Switching at `p` with the other absent colour on each shore
again gives the same boundary equality partition: `p,q` become distinct
singleton blocks and the partition on `C` is unchanged.  The colour names
at `p` may differ, but equality partitions agree, which is precisely what
the gluing argument requires.  Item 3 is therefore correct.

## 3. Four-colour case and rooted triangle

A proper four-colouring of a five-cycle repeats exactly one colour, on a
nonadjacent pair.  This is one edge `x_0x_1` of `D`; the other three roots
`x_2,x_3,x_4` have pairwise distinct colours occurring nowhere else on
the boundary.  If either demanded pair `x_2x_3` or `x_3x_4` were separated
in its bichromatic graph, a component switch would identify the two root
colours on `C` and lower `m(c)` to three.  Both connections are therefore
present.  Their interiors avoid `S` and each lies in one shore.

Kriesell--Mohr Theorem 5 also applies to the two-edge demand path
`x_2x_3x_4`.  It gives disjoint rooted connected sets `D_2,D_3,D_4`
adjacent along that path.  The pair `x_2x_4` is not an edge of `D`, hence
is an edge of `G[C]`, and completes the rooted `K_3` model.

## 4. Explicit near-complete seven-branch-set model

If both demanded paths use the same open shore, say `L`, the rooted sets
may be confined to `L union {x_2,x_3,x_4}`.  The seven proposed sets

\[
 \{p\},\ \{q\},\ D_2,\ D_3,\ D_4,\ R\cup\{x_0\},\ \{x_1\}
\]

are disjoint and connected.  The universal boundary vertices `p,q` meet
every other set.  The three `D_i` are pairwise adjacent.  Full boundary
attachment of `R` makes `R union {x_0}` adjacent to all six other sets.
In the literal five-cycle, `x_1` is adjacent to `x_3,x_4`, so it meets
`D_3,D_4`; its only unsupported adjacency is to `D_2`.  Thus the displayed
sets form exactly the asserted `K_7`-minus-one-edge model.  The construction
is symmetric when both paths use `R`.

## 5. Scope

The theorem does not prove that the two absent-colour paths in the
three-colour case are disjoint, does not combine paths lying in opposite
shores in the four-colour case, and does not repair the final missing
adjacency in the same-shore case.  It produces no common boundary partition
beyond the two contradiction arguments explicitly used in the proof.

## Unresolved assumptions or gaps

None for the statements at the audited hash.
