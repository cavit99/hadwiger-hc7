# Tight cycles close the full-six-colour order-nine endpoint

**Status:** written proof; separate internal audit GREEN in
[`hc7_order9_full_trace_tight_cycle_completion_audit.md`](hc7_order9_full_trace_tight_cycle_completion_audit.md).

This note treats an unbounded part of the order-nine paired list-critical
endpoint.  It uses the literal boundary colour classes and the two
anticomplete shores; it does not identify a colour with an inherited
minor-model label.

## 1. Setting

Let

\[
             V(G)=A\mathbin{\dot\cup}B\mathbin{\dot\cup}D,
             \qquad E_G(A,D)=\varnothing,
\tag{1.1}
\]

where `A,D` are nonempty.  Let `|B|=9`, and let `phi` be a proper colouring
of `G[B]` which uses exactly six colours.  For `Z in {A,D}` and `v in Z`,
put

\[
 q(v)=|\phi(N_G(v)\cap B)|,
 \qquad
 \rho(v)=|N_G(v)\cap B|-q(v),
\tag{1.2}
\]

and call `v` **tight** when

\[
                    d_{G[Z]}(v)=6-q(v).              \tag{1.3}
\]

Assume that every shore vertex satisfies

\[
 d_{G[Z]}(v)-\bigl(6-q(v)\bigr)+\rho(v)\ge3.
\tag{1.4}
\]

In the live application, (1.4) is the exact degree accounting at the
spanning paired list-critical endpoint after excluding singleton response
boundaries of order seven and eight.

Let `M` be the union of the nonsingleton colour classes of `phi` on `B`.

## 2. Boundary repetition is completely visible from a tight vertex

### Lemma 2.1

One has `|M|>=4`.  Every tight vertex in either shore is adjacent to every
literal vertex of `M`.

### Proof

Write the six nonempty colour classes on `B` as

\[
                         C_1,\ldots,C_6.
\]

Their orders sum to nine, and therefore

\[
                    \sum_{i=1}^6(|C_i|-1)=3.          \tag{2.1}
\]

At least one class is nonsingleton.  For a fixed total excess of three,
the union of the nonsingleton classes has minimum order four, attained by
the size pattern `4,1,1,1,1,1`.  Hence `|M|>=4`.

For any shore vertex `v`, put `n_i=|N_G(v)\cap C_i|`.  Then

\[
 \rho(v)=\sum_{i:n_i>0}(n_i-1)
          \le \sum_{i=1}^6(|C_i|-1)=3.               \tag{2.2}
\]

If `v` is tight, (1.4) gives `rho(v)>=3`, so equality holds throughout
(2.2).  For every nonsingleton `C_i`, equality is possible only when
`n_i=|C_i|`: omitting the class or one of its vertices loses at least one
unit from the right side of (2.1).  Thus `v` is adjacent to every vertex of
every nonsingleton class, which is exactly every vertex of `M`.  \(\square\)

## 3. Two tight cycles give seven branch sets

### Theorem 3.1

If both induced subgraphs on the tight vertices,

\[
               G[T_A]\quad\text{and}\quad G[T_D],
\tag{3.1}
\]

contain a cycle, then `G` contains a `K_7` minor.

### Proof

A cycle contains a `K_3` minor.  Choose three pairwise disjoint connected
branch sets

\[
                         A_1,A_2,A_3\subseteq T_A
\]

forming a `K_3`-minor model in the first tight-vertex subgraph, and choose
similarly

\[
                         D_1,D_2,D_3\subseteq T_D.
\]

By Lemma 2.1, every vertex in all six branch sets is adjacent to every
vertex of `M`.  Choose four distinct vertices

\[
                            m_1,m_2,m_3,m_4\in M.
\]

Consider the seven sets

\[
 A_1,\quad A_2,\quad A_3,\quad
 D_1\cup\{m_1\},\quad D_2\cup\{m_2\},\quad
 D_3\cup\{m_3\},\quad \{m_4\}.                     \tag{3.2}
\]

They are pairwise disjoint and connected.  The three `A_i` are pairwise
adjacent, and the three enlarged `D_i` are pairwise adjacent through the
chosen `K_3` model in `D`.  Every `A_i` is adjacent to every enlarged
`D_j` through the edge from `A_i` to `m_j`.  Finally, the singleton
`{m_4}` is adjacent to every `A_i` and every `D_j` by Lemma 2.1.  Hence
(3.2) is an explicit `K_7`-minor model.  \(\square\)

### Corollary 3.2

If `G` has no `K_7` minor, at least one of `G[T_A],G[T_D]` is a forest.
In particular, if both shores are two-connected and every shore vertex is
tight, then `G` contains a `K_7` minor.

### Proof

The first statement is the contrapositive of Theorem 3.1.  A two-connected
graph has at least three vertices and contains a cycle.  Thus if every
vertex of each two-connected shore is tight, both graphs in (3.1) contain a
cycle and Theorem 3.1 applies.  \(\square\)

## 4. Exact gain and trust boundary

The theorem eliminates the entire full-six-colour endpoint in which both
tight-vertex subgraphs contain cycles.  It is independent of the orders and
internal shapes of the two shores.

It does not treat a fixed boundary trace using fewer than six colours.  It
also does not close the case in which one tight-vertex subgraph is a forest,
or in which non-tight vertices carry all cycles of a shore.  The four
vertices `m_i` are selected from literal boundary colour classes; they are
not asserted to represent four inherited branch-set labels.  No
palette-to-label inference is used.

## 5. Dependency

- [large-boundary singleton-response descent](../results/hc7_large_boundary_singleton_response_descent.md),
  for the live order-nine endpoint and inequality (1.4).
