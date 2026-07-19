# Cycle completion from adjacent defect-one and boundary-full pairs

**Status:** written proof; separate internal audit GREEN in
[`hc7_adjacent_full_pair_cycle_completion_audit.md`](hc7_adjacent_full_pair_cycle_completion_audit.md).
This is a
reusable branch-set construction.  It is not asserted that the current
live opposite-response branch supplies all four connected subgraphs below,
and the theorem does not prove `HC_7`.

## 1. Setting

Let `S` be an eight-vertex set in a graph `G`, and let `d,e` be distinct
vertices of `S`.  Suppose that

\[
                   A_d,\quad A_e,\quad Q_0,\quad Q_1                 \tag{1.1}
\]

are pairwise vertex-disjoint connected subgraphs of `G-S` with the
following properties:

1. `A_d,A_e` are adjacent and

   \[
    N_G(A_d)\cap S=S-\{d\},\qquad
    N_G(A_e)\cap S=S-\{e\};                           \tag{1.2}
   \]

2. each of `Q_0,Q_1` is adjacent to every literal vertex of `S`; and
3. `Q_0,Q_1` are adjacent.

No colouring hypothesis is imposed.

## 2. Cycle completion

### Theorem 2.1

If `G[S-{d,e}]` contains a cycle, then `G` contains a `K_7` minor.

#### Proof

Let `C` be a cycle in `G[S-{d,e}]`.  Partition its cyclic order into
three nonempty consecutive arcs, and let their vertex sets be
`M_1,M_2,M_3`.  Each `M_i` is connected, and the three sets are pairwise
adjacent through the three transition edges of the cycle.

Consider

\[
 Q_0,\quad Q_1,\quad
 V(A_d)\cup\{e\},\quad V(A_e)\cup\{d\},\quad
 M_1,\quad M_2,\quad M_3.                             \tag{2.1}
\]

These seven sets are pairwise disjoint and connected.  The first two are
adjacent by hypothesis.  Each `Q_j` is adjacent to each of the remaining
five sets: use its boundary contact at `e` or `d` for the two defect-one
sets, and boundary fullness for the three cycle arcs.  The two defect-one
sets are adjacent because `A_d,A_e` are adjacent.  Equation (1.2) makes
each of them adjacent to every `M_i`, because the cycle avoids `d,e`.
Finally the three `M_i` are pairwise adjacent.  Thus (2.1) is an explicit
`K_7`-minor model. \(\square\)

### Corollary 2.2 (forest normalization)

If `G` has no `K_7` minor, then `G[S-{d,e}]` is a forest.

The adjacency of `Q_0,Q_1` is essential to this exact construction.  If
they are separate components of `G-S`, the earlier short-cycle construction
uses an unused boundary vertex to create their missing adjacency and only
handles cycles of order at most five.  The present theorem also covers a
six-cycle.

### Corollary 2.3 (two rooted paths in the forest)

Assume additionally that `G[S]` contains two vertex-disjoint odd cycles.
If `G` has no `K_7` minor, then, after interchanging the two cycles if
necessary, one contains `d` but not `e`, the other contains `e` but not
`d`, and deleting the respective root leaves two vertex-disjoint
odd-length paths in the forest `G[S-{d,e}]`.  The ends of the first path
are distinct neighbours of `d`, and the ends of the second are distinct
neighbours of `e`.

#### Proof

By Corollary 2.2, no cycle is contained in `S-{d,e}`.  Each of the two
vertex-disjoint odd cycles therefore contains a member of `{d,e}`.
Disjointness forces one root into each cycle and prevents either cycle
from containing the other root.  Deleting the root leaves a path between
two distinct neighbours.  If that path has `ell` edges, its original
cycle has `ell+2` edges, so `ell` is odd.  The two paths remain
vertex-disjoint. \(\square\)

## 3. Exact scope

The theorem extends the earlier cycle construction only when the two
boundary-full connected subgraphs are adjacent.  The maximal-cover normal
form supplies such an adjacent pair on the connected **split-response**
shore.  It does not supply adjacent defect-one subgraphs on the opposite
merged-response shore.  The now-closed two-cut branch does supply adjacent
defect-one pieces, but its two full subgraphs are separate components and
its response orientation is different.  Thus this theorem is reusable but
is not an immediate dependency of the current active target.

## 4. Dependency

- [the earlier cycle construction through order five](hc7_order8_strict_reversal_completion.md),
  cited for comparison; the proof above is self-contained.
