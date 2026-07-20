# Minimum-degree alignment in one canonical pole--rim type-5 enlargement

**Status:** written proof; separately audited **GREEN** in
[`hc7_pentagonal_bipyramid_type5_minimum_degree_alignment_audit.md`](hc7_pentagonal_bipyramid_type5_minimum_degree_alignment_audit.md).
This is a finite label-preserving theorem about the displayed canonical orbit of
Hegde--Thomas type-5 enlargements of the pentagonal bipyramid.  It is not a
theorem about every pole--rim type-5 enlargement, is not a relative-minor
theorem, and does not prove the live paired-rooted `K_5` target.

## 1. The displayed canonical orbit

Write the pentagonal bipyramid as the join of the rim cycle

\[
 c_0c_1c_2c_3c_4c_0
\]

and two nonadjacent poles `a,b`.  Split the adjacent old vertices `a,c_0`
into

\[
 \{a_0,a_1\},\qquad \{d_0,d_1\},
\]

respectively.  The canonical pole--rim type-5 enlargement `H_0` has vertex
set

\[
 \{a_0,a_1,d_0,d_1,b,c_1,c_2,c_3,c_4\}
\]

and the following edges:

\[
\begin{aligned}
 &a_0a_1, d_0d_1, a_0d_0, a_1d_1,\\
 &a_0c_4, a_1c_1, a_1c_2, a_1c_3,\\
 &bd_1, bc_i\ (1\le i\le4),\\
 &d_0c_1, d_1c_4,\\
 &c_1c_2, c_2c_3, c_3c_4.
\end{aligned}                                                    \tag{1.1}
\]

The seven labelled parts are

\[
 \{a_0,a_1\},\ \{b\},\ \{d_0,d_1\},\
 \{c_1\},\ \{c_2\},\ \{c_3\},\ \{c_4\}.                    \tag{1.2}
\]

Contracting each part gives the pentagonal bipyramid.  A
**part-respecting supergraph** of `H_0` is a simple graph `H` on the same
vertex set, containing every edge in (1.1), in which an added edge may join
vertices in the same part or in two parts whose old pentagonal-bipyramid
labels are adjacent.  Thus the contact graph of the seven parts remains
exactly the pentagonal bipyramid.

Let `A,B` be two vertex sets such that

\[
 \{b,c_1,c_2,c_3,c_4\}\subseteq A\cap B,                       \tag{1.3}
\]

and each of `A,B` contains exactly one vertex of `\{a_0,a_1\}` and
exactly one vertex of `\{d_0,d_1\}`.  These are all sixteen possible
ordered choices of one root in each labelled part.

All assertions below concern this displayed labelled graph and its
part-respecting supergraphs.  Relabellings obtained from this graph by an
automorphism of the pentagonal bipyramid or by exchanging the two vertices
inside a split part are covered by the same proof.  No assertion is made
here that these relabellings exhaust all pole--rim type-5 enlargements.

## 2. One forced edge closes every endpoint choice

### Theorem 2.1

If `H` is a part-respecting supergraph of `H_0` with minimum degree at
least five, then `H` contains a `K_5`-minor model every branch set of which
meets both `A` and `B`, for every choice of `A,B` satisfying (1.3).

In particular, the conclusion holds when `H` is five-connected.

### Proof

In `H_0`, the neighbours of `c_2` are

\[
                         a_1,b,c_1,c_3.                         \tag{2.1}
\]

The old label `c_2` is adjacent in the pentagonal bipyramid only to
`a,b,c_1,c_3`.  All of the corresponding parts except the split `a`-part
are singletons, and their possible edges to `c_2` already occur in (2.1).
Consequently the only edge incident with `c_2` which a part-respecting
supergraph can add is

\[
                              a_0c_2.                           \tag{2.2}
\]

Since `d_H(c_2)>=5`, edge (2.2) is forced.

Now take the five sets

\[
 \{b\},\qquad
 \{d_0,d_1\},\qquad
 \{c_1\},\qquad
 \{a_0,c_2\},\qquad
 \{a_1,c_3\}.                                                 \tag{2.3}
\]

They are pairwise disjoint.  They are connected: the only nontrivial
point not already in (1.1) is `a_0c_2`, which is (2.2).  They are pairwise
adjacent, as witnessed by

\[
\begin{array}{c|cccc}
 &\{d_0,d_1\}&\{c_1\}&\{a_0,c_2\}&\{a_1,c_3\}\\ \hline
\{b\}&bd_1&bc_1&bc_2&bc_3\\
\{d_0,d_1\}&&d_0c_1&d_0a_0&d_1a_1\\
\{c_1\}&&&c_1c_2&c_1a_1\\
\{a_0,c_2\}&&&&a_0a_1
\end{array}                                                     \tag{2.4}
\]

(The edge `c_2c_3` gives another witness in the last entry.)  Hence (2.3)
is a `K_5`-minor model.

The singleton bags `\{b\}` and `\{c_1\}` meet `A\cap B`.  The bag
`\{d_0,d_1\}` contains the selected root from the split `c_0`-part for
each of `A,B`.  Finally, `\{a_0,c_2\}` and `\{a_1,c_3\}` meet `A\cap B`
at `c_2,c_3`, independently of which vertices were selected in the split
`a`-part.  Thus every bag in (2.3) meets both `A` and `B`.  This proves the
theorem. \(\square\)

## 3. Meaning of the finite count `35`

There are nine missing edges that may be added to `H_0` without changing
the contact graph of the seven parts:

\[
\begin{gathered}
 bd_0, a_0c_1, d_1c_1, a_0c_2, a_0c_3,\\
 a_1c_4, d_0c_4, a_0d_1, a_1d_0.                            \tag{3.1}
\end{gathered}
\]

Thus there are `2^9=512` part-respecting supergraphs on the same nine
vertices.  The
[`deterministic verifier`](hc7_pentagonal_bipyramid_type5_minimum_degree_alignment_verify.py)
exhausts them and finds exactly `35`
whose vertex-connectivity is at least five.  Each of those `35` contains
`a_0c_2`, as the proof already forces, and the single model (2.3) works
for all sixteen ordered root choices.  The count is redundant finite
evidence; Theorem 2.1 is proved directly and does not depend on it.

## 4. Exact trust boundary

This theorem closes only the displayed canonical orbit at the fixed
nine-vertex level.  It does not cover all pole--rim type-5 enlargements.
Indeed, exact generation gives forty labelled pole--rim instances in two
degree-multiset classes of twenty:

\[
 (3,3,4,4,4,4,4,5,5)
 \quad\hbox{and}\quad
 (3,4,4,4,4,4,4,4,5).
\]

The graph in (1.1) belongs to the first class.  The degree multiset is
invariant under graph isomorphism, so automorphisms of the pentagonal
bipyramid, reversal of the rim, and renaming of split ends cannot turn the
second class into the displayed graph.  This observation records the exact
scope boundary; it does not open a new case programme here.

Hegde--Thomas's enlargement theorem, moreover, supplies an enlargement
**minor** of a five-connected nonplanar graph.  Its split vertices may be
branch sets, and the extra connectivity which forces (2.2) at the
nine-vertex level may be represented in the host by a path whose interior
meets other labelled branch sets.  The theorem also does not identify the
enlargement's seven parts with the seven originally prescribed columns or
preserve the two sets of literal root neighbours.

The remaining unbounded step is therefore relative: convert the host path
which replaces the forced edge `a_0c_2` into a label-preserving branch-set
exchange, or show that its failure exposes the required order-seven
separation with compatible boundary colourings.  No such relative lifting
is claimed here.
