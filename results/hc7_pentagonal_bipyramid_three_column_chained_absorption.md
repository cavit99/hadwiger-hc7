# Three-column chained absorption in a pentagonal-bipyramid expansion

**Status:** written proof; [separately audited **GREEN**](hc7_pentagonal_bipyramid_three_column_chained_absorption_audit.md).
This is a sufficient paired-rooted construction, not an exhaustive structural
theorem.  The audit is internal, not external peer review.

## 1. Setup

Let `F` have a vertex partition into nonempty connected columns

\[
             C_a,C_b,C_0,C_1,C_2,C_3,C_4
\]

whose contact graph is the pentagonal bipyramid: `a,b` are nonadjacent,
both poles are adjacent to every rim label, and the rim labels occur in the
cycle `0,1,2,3,4,0`.  Rim subscripts below are modulo five.  Let
`A,B` be vertex sets meeting every column.

## 2. The construction

### Theorem 2.1 (three-column chained absorption)

Fix a rim index `i`.  Suppose there are nonempty vertex sets

\[
\begin{array}{lll}
 P_b,Q_b\subseteq V(C_b),&
 P_1,Q_1\subseteq V(C_{i+1}),&
 Q_2,Z_2\subseteq V(C_{i+2})
\end{array}
\]

such that

\[
 P_b\cap Q_b=P_1\cap Q_1=Q_2\cap Z_2=\varnothing.       \tag{2.1}
\]

Put

\[
\begin{aligned}
 D_1&=P_b\cup P_1,\\
 D_2&=Q_b\cup Q_1\cup Q_2,\\
 D_3&=Z_2\cup V(C_{i+3})\cup V(C_{i+4}).
\end{aligned}                                                \tag{2.2}
\]

Assume that `F[D_1],F[D_2],F[D_3]` are connected, that `D_1,D_2`
each meet both literal root sets `A,B`, and that the following seven
contacts exist:

\[
\begin{gathered}
 E(C_a,D_1),\ E(C_a,D_2),\ E(C_i,D_1),\ E(C_i,D_2),\\
 E(D_1,D_2),\ E(D_1,D_3),\ E(D_2,D_3)\ne\varnothing.
                                                               \tag{2.3}
\end{gathered}
\]

Then `F` has a `K_5`-minor model paired-rooted at `(A,B)`.

### Proof

Use the five branch sets

\[
             V(C_a),\quad V(C_i),\quad D_1,\quad D_2,\quad D_3.
                                                               \tag{2.4}
\]

They are pairwise disjoint by their column locations and (2.1).  The first
two are connected columns and the last three are connected by hypothesis.
All ten pairwise adjacencies have the following exact sources.

| pair | source |
|---|---|
| `C_a,C_i` | the pole--rim quotient contact |
| `C_a,D_1` | hypothesis (2.3) |
| `C_a,D_2` | hypothesis (2.3) |
| `C_a,D_3` | the quotient contact `C_a C_{i+3}` |
| `C_i,D_1` | hypothesis (2.3) |
| `C_i,D_2` | hypothesis (2.3) |
| `C_i,D_3` | the rim contact `C_i C_{i+4}` |
| `D_1,D_2` | hypothesis (2.3) |
| `D_1,D_3` | hypothesis (2.3) |
| `D_2,D_3` | hypothesis (2.3) |

Thus (2.4) is a `K_5`-minor model.  The first two bags meet `A,B` because
they are whole columns, `D_1,D_2` do so by hypothesis, and `D_3` contains
the two whole columns `C_{i+3},C_{i+4}`.  The model is therefore
paired-rooted.  \(\square\)

The theorem is invariant under cyclic permutation and reversal of the rim.
Interchanging `a,b` gives the symmetric version in which `C_b` is the
whole pole anchor and `C_a` supplies `P_b,Q_b` (with those pieces renamed).

The literal root hypotheses on `D_1,D_2` are essential to the stated
conclusion.  Unlike constructions in which five bags contain five distinct
whole columns, (2.4) does not work uniformly for every selection of one
`A`-vertex and one `B`-vertex per column.

## 3. Exact sixteen-vertex application

Use integer vertices `2x+s` for `(x,s)` in the fourteen-vertex graph from
the [four-colourable combined-negative barrier](../barriers/hc7_pentagonal_bipyramid_four_colour_combined_negative.md).
Add vertex `14` to pole column `C_1`, initially adjacent exactly to

\[
                   N_{F-15}(14)=\{2,3,6,7,8\},              \tag{3.1}
\]

and then add vertex `15` to rim column `C_3`, adjacent exactly to

\[
                         N(15)=\{2,3,5,6,14\}.                \tag{3.2}
\]

To distinguish the barrier's numeric labels from the theorem notation,
write its columns temporarily as `hat C_0,...,hat C_6` and set

\[
 C_a=\widehat C_0,\quad C_b=\widehat C_1,\quad
 (C_0,C_1,C_2,C_3,C_4)
   =(\widehat C_2,\widehat C_3,\widehat C_4,
     \widehat C_5,\widehat C_6).
\]

Apply the theorem with `i=0` and choose

\[
\begin{array}{lll}
 P_b=\{2\},&Q_b=\{3\},&P_1=\{7\},\\
 Q_1=\{15\},&Q_2=\{8\},&Z_2=\{9\}.
\end{array}
\]

The five bags in (2.4) are

\[
 \{0,1\},\quad \{4,5\},\quad \{2,7\},\quad
 \{3,8,15\},\quad \{9,10,11,12,13\}.                       \tag{3.3}
\]

Their ten adjacencies are witnessed, in the order of the table in the
proof, by

\[
 04,\ 07,\ 08,\ 0\,11,\ 5\,2,\ 5\,15,\ 4\,12,\
 2\,3,\ 2\,10,\ 8\,9.                                      \tag{3.4}
\]

Here a juxtaposition denotes an edge, with spaces inserted for two-digit
vertices.

For the disjoint minimal root sets

\[
 A=\{0,3,4,7,8,10,12\},\qquad
 B=\{1,2,5,9,11,13,15\},                                   \tag{3.5}
\]

each set contains exactly one vertex of every column, and every bag in
(3.3) meets both sets.  This is a concrete paired-rooted application of
Theorem 2.1.  The adjacent
[singleton-web-cell barrier](../barriers/hc7_pentagonal_bipyramid_singleton_web_cell_barrier.md)
records the exact limits of this certificate and its independent verifier.
