# Cyclic three-pair boundary contacts give a `K_7` minor

**Archive note:** unaudited exploratory result retained for provenance; it
is not part of the current proof spine.

**Status:** written proof; independent audit pending.

This note isolates the positive mechanism in a proposed paired
list-critical-kernel example.  List-criticality is not needed for the
minor construction.  What matters is a central connected subgraph, three
adjacent pairs of connected subgraphs, and six literal boundary vertices
whose contacts are complementary to those three pairs.

## 1. Assigned-contact completion

The following is the exact condition needed by the proposed seven branch
sets.  It separates the minor construction from the more symmetric
six-colour hypothesis used later.

### Lemma 1.1

Let `I` be a six-element set partitioned into three pairs.  Suppose `G`
contains pairwise vertex-disjoint nonempty connected subgraphs

\[
                         Z,\qquad U_a\quad(a\in I)
\]

and distinct vertices `b_a` (`a\in I`) outside their union.  Assume:

1. `Z` is adjacent to every `U_a`;
2. `U_a` is adjacent to `b_a` for every `a`;
3. if `a,a'` form one of the three prescribed pairs, then `U_a` and
   `U_{a'}` are adjacent; and
4. if `a,a'` are in different prescribed pairs, then `U_a` is adjacent to
   `b_{a'}` or `U_{a'}` is adjacent to `b_a`.

Then `G` contains a `K_7` minor.

#### Proof

The seven sets

\[
                         Z,\qquad U_a\cup\{b_a\}\quad(a\in I)
\]

are pairwise disjoint and connected.  Hypothesis 1 supplies every
adjacency incident with `Z`; hypothesis 3 supplies the three within-pair
adjacencies; and hypothesis 4 supplies every remaining adjacency.  They
are therefore the branch sets of a `K_7`-minor model. \(\square\)

For these prescribed branch sets, hypotheses 1--4 say exactly where their
connectivity and pairwise adjacencies come from.  This is the useful
minimal formulation; of course another host edge could replace any one of
the stipulated adjacencies.

## 2. Symmetric three-pair contacts

All subscripts in this section are taken modulo three.

### Theorem 2.1

Let `G` contain pairwise vertex-disjoint nonempty connected subgraphs

\[
 Z,\qquad U_i^0,U_i^1\quad(i\in\mathbb Z/3\mathbb Z),
\]

and six distinct vertices

\[
 b_i^0,b_i^1\quad(i\in\mathbb Z/3\mathbb Z)
\]

outside all seven displayed subgraphs.  Assume:

1. `Z` is adjacent to every `U_i^epsilon`;
2. `U_i^0` is adjacent to `U_i^1` for every `i`; and
3. whenever `i != j`, every `U_i^epsilon` is adjacent to both
   `b_j^0` and `b_j^1`.

Then `G` contains a `K_7` minor.

#### Proof

For `i in Z/3Z` and `epsilon in {0,1}`, put

\[
 A_i^\epsilon=U_i^\epsilon\cup\{b_{i+1}^\epsilon\}.
\]

Hypothesis 3 makes every `A_i^epsilon` connected.  The seven sets

\[
 Z,\qquad A_i^\epsilon
      \quad(i\in\mathbb Z/3\mathbb Z,\ \epsilon\in\{0,1\})
\]

are nonempty, connected and pairwise vertex-disjoint.

The set `Z` is adjacent to each of the other six sets by hypothesis 1.
The two sets `A_i^0,A_i^1` are adjacent by hypothesis 2.  It remains to
compare sets with distinct first indices.  If `j=i+1`, then
`b_{j+1}^delta=b_{i+2}^delta` belongs to `A_j^delta` and is adjacent to
`U_i^epsilon` by hypothesis 3.  If `j=i+2`, then
`b_{i+1}^epsilon` belongs to `A_i^epsilon` and is adjacent to
`U_j^delta`, again by hypothesis 3.  Thus all seven sets are pairwise
adjacent and form a `K_7`-minor model. \(\square\)

The assumptions above are a symmetric sufficient condition, rather than a
claim of logical minimality.  For the displayed branch sets, hypothesis 3
can be weakened to the individual cross-adjacencies used in the last
paragraph.  The symmetric form is the one naturally certified by six
boundary colours with unique literal representatives.

## 3. Recognition inside a boundary list obstruction

Let `X={b_i^epsilon : i in Z/3Z, epsilon in {0,1}}`, and let `c` be a
proper six-colouring of `G[X]` which assigns the six colours bijectively to
these six vertices.  Write

\[
 P_i=\{c(b_i^0),c(b_i^1)\}.
\]

For a vertex `v` outside `X`, define its boundary list by

\[
 L(v)=[6]\setminus c(N_G(v)\cap X).
\]

### Corollary 3.1

Suppose `G-X` contains seven distinct vertices

\[
 x,\qquad u_i^0,u_i^1
       \quad(i\in\mathbb Z/3\mathbb Z)
\]

such that:

1. `x u_i^epsilon` is an edge for all `i,epsilon`;
2. `u_i^0u_i^1` is an edge for every `i`; and
3. `L(u_i^epsilon) subseteq P_i` for every `i,epsilon`.

Then `G` contains a `K_7` minor.

#### Proof

For `j != i`, the two colours on `b_j^0,b_j^1` do not belong to `P_i`
and hence do not belong to `L(u_i^epsilon)`.  Because `c` is bijective on
`X`, the definition of the boundary list implies that
`u_i^epsilon` is adjacent to both `b_j^0,b_j^1`.  Theorem 2.1 applies with
`Z={x}` and `U_i^epsilon={u_i^epsilon}`. \(\square\)

In particular, the corollary applies to a three-triangle friendship graph
whose common vertex has list `[6]` and whose two noncentral vertices in the
`i`-th triangle both have list exactly `P_i`.

## 4. Relation to the live paired-kernel branch

The paired rejection-kernel theorem does **not** currently force the
hypotheses of Corollary 3.1.  It supplies, in each shore, only a connected
induced vertex-minimal non-list-colourable subgraph `K` satisfying

\[
 d_K(v)\ge |L(v)|,
\]

with a Gallai forest on its tight vertices.  It does not force:

- a common vertex in three triangle blocks;
- three disjoint two-colour lists partitioning all six colours;
- six singleton boundary colour classes; or
- common literal representatives of repeated boundary colours adjacent to
  all of the required kernel vertices.

The last point is essential.  If one colour occurs at several boundary
vertices, the fact that two kernel vertices both omit that colour from
their lists says only that each has *some* neighbour of that colour.  It
does not give one literal boundary vertex adjacent to both.  Thus the
lemma closes the displayed friendship-kernel subcase, but it does not close
the general distance-at-least-two paired-kernel outcome.
