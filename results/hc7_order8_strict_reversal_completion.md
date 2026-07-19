# Completion of the strict-reversal path configuration at an order-eight boundary

**Status:** written proofs; separate internal audit GREEN in
[`hc7_order8_strict_reversal_completion_audit.md`](hc7_order8_strict_reversal_completion_audit.md).
This note closes the strict-reversal branch of the audited induced-path
normal form when the other two components are adjacent to every boundary
vertex.  It does not treat a shared portal at an end of the path and does
not prove `HC_7`.

Throughout, a connected subgraph disjoint from `S` is **`S`-full** if it
has a neighbour at every literal vertex of `S`.

## 1. A boundary cycle gives an explicit minor model

### Lemma 1.1

Let `S` have order eight and let `d,e` be distinct vertices of `S`.
Suppose that `Q_0,Q_1,A_d,A_e` are pairwise vertex-disjoint connected
subgraphs of `G-S` such that:

1. `Q_0,Q_1` are `S`-full;
2. `A_d` is adjacent to every vertex of `S-\{d\}`;
3. `A_e` is adjacent to every vertex of `S-\{e\}`; and
4. `A_d` and `A_e` are adjacent.

If `G[S-\{d,e\}]` contains a cycle of order at most five, then `G`
contains a `K_7` minor.

### Proof

Let `C` be such a cycle.  Since `S-\{d,e\}` has order six, choose

\[
                       w\in S-(V(C)\cup\{d,e\}).       \tag{1.1}
\]

Contract edges of `C` into three nonempty connected pairwise adjacent
sets `M_1,M_2,M_3`.  Consider

\[
 Q_0\cup\{w\},\quad Q_1,\quad
 A_d\cup\{e\},\quad A_e\cup\{d\},\quad
 M_1,\quad M_2,\quad M_3.                             \tag{1.2}
\]

These seven sets are pairwise disjoint and connected.  The first two are
adjacent through an edge from `Q_1` to `w`.  Each of them is adjacent to
`A_d\cup\{e\}` through `e` and to `A_e\cup\{d\}` through `d`.
The two one-defect sets are adjacent by hypothesis.  Both `Q_i` are
adjacent to every `M_j` by boundary fullness, while both one-defect sets
are adjacent to every `M_j` because `C` avoids `d,e`.  Finally the three
sets obtained from the cycle are pairwise adjacent.  Thus (1.2) is an
explicit `K_7`-minor model. \(\square\)

In particular, if `G[S-\{d,e\}]` is nonbipartite, it contains an odd
cycle of order three or five, and Lemma 1.1 applies.

## 2. A three-block colouring when the defects are nonadjacent

### Theorem 2.1

Assume that every proper minor of `G` is six-colourable and that

\[
             G-S=P\mathbin{\dot\cup}Q_0\mathbin{\dot\cup}Q_1       \tag{2.1}
\]

is the decomposition into exactly three components.  Suppose `Q_0,Q_1`
are `S`-full and `P` is three-colourable.  Let `d,e` be distinct
nonadjacent vertices of `S`, and let

\[
                    S-\{d,e\}=X\mathbin{\dot\cup}Y                 \tag{2.2}
\]

be a bipartition with `X,Y` nonempty.  Suppose `P` is the disjoint union
of connected subgraphs `A_d,A_e` which are adjacent and satisfy

\[
 N_G(A_d)\cap S=S-\{d\},
 \qquad
 N_G(A_e)\cap S=S-\{e\}.                              \tag{2.3}
\]

Then `G` is six-colourable.

### Proof

Let

\[
                         \Pi=X\mid Y\mid\{d,e\}.       \tag{2.4}
\]

This is a proper three-block partition of `G[S]`.

First colour the closed `P`-side directly.  Give the three blocks of
`\Pi` three distinct colours, and colour `P` properly with three other
colours.  Because the two palettes are disjoint, every edge between `P`
and `S` is proper.  This gives a proper six-colouring of `G[P\cup S]`
which induces exactly `\Pi`.

Fix `i\in\{0,1\}` and write `j=1-i`.  In a proper minor of `G`, contract
spanning trees of the following three pairwise disjoint connected sets:

\[
              A_d\cup X,\qquad
              A_e\cup Y,\qquad
              Q_j\cup\{d,e\}.                         \tag{2.5}
\]

The first two sets are connected by (2.3), and the third is connected by
boundary fullness.  Their contraction images form a triangle.  The first
two are adjacent because `A_d,A_e` are adjacent.  The first is adjacent to
the third through `e`, and the second through `d`.

Six-colour this proper minor, restrict the colouring to `G[Q_i\cup S]`,
and expand the three contracted boundary blocks.  The three images have
distinct colours, so the resulting proper colouring induces exactly
`\Pi` on `S`.  Doing this for `i=0` and `i=1` gives colourings of both
remaining closed component sides with the same boundary partition.

Permute colour names so that all three closed-side colourings agree on
`S`.  Distinct components of `G-S` are anticomplete, so the colourings
glue to a proper six-colouring of `G`. \(\square\)

## 3. Strict-reversal completion

### Corollary 3.1

Assume that `G` is seven-connected, is not six-colourable, has no `K_7`
minor, and every proper minor of `G` is six-colourable.  Let `S` have order
eight, suppose `G-S` has exactly three `S`-full components, and suppose one
component is the induced path

\[
                              P=p_0p_1\cdots p_m.
\]

In the strict-reversal outcome of the audited overlapping-interval normal
form, an actual order-seven separation is returned.

### Proof

Suppose that none of the three path subintervals in that normal form has
already returned an order-seven separation.  Use its notation `b<a` and
choose `k` with `b<=k<a`.  Put

\[
                         A_d=P[0,k],\qquad A_e=P[k+1,m].             \tag{3.1}
\]

The two subpaths are nonempty, connected, adjacent, cover `P`, and are
respectively adjacent to exactly `S-\{d\}` and `S-\{e\}`.  The other two
components supply the `S`-full subgraphs `Q_0,Q_1`.

The audited three-component boundary classification shows that `G[S]`
contains two vertex-disjoint odd cycles.  If `G[S-\{d,e\}]` is
nonbipartite, Lemma 1.1 gives a `K_7` minor, a contradiction.  Hence it is
bipartite; write its bipartition as `X\mathbin{\dot\cup}Y`.

Both classes are nonempty.  Indeed, each of the two disjoint odd cycles
must meet `\{d,e\}`.  Disjointness lets us orient them so that one contains
`d` but not `e` and the other contains `e` but not `d`.  Removing the
distinguished vertex from either odd cycle leaves a nonempty odd-length
path in `G[S-\{d,e\}]`, whose ends lie in opposite bipartition classes.

If `de` is an edge, the audited adjacent-defect reflection theorem gives a
six-colouring of `G`, a contradiction.  If `de` is not an edge, Theorem
2.1 applies because the induced path `P` is two-colourable, and again gives
a six-colouring.  Thus the supposition that no path subinterval returned
an order-seven separation is impossible. \(\square\)

## 4. Trust boundary

Corollary 3.1 closes the strict-reversal branch only in the exact
three-component, boundary-full, induced-path setting stated above.  It
does not treat a shared portal at an end of `P`, an arbitrary connected
selected component, the two-component order-eight interface, or the
colour compatibility of the order-seven separation it returns.

The proof uses the finite boundary classification only for its audited
universal statement that every surviving boundary contains two
vertex-disjoint odd cycles.  It does not infer an unbounded host theorem
from the 134-case quotient probe.

## 5. Dependencies

- the [overlapping-interval path normal form](hc7_order8_overlapping_interval_normal_form.md);
- the [three-component boundary classification](hc7_order8_three_component_boundary_classification.md); and
- [reflection across adjacent complementary defects](hc7_order8_two_defect_clique_oct_reflection.md).
