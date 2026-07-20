# Two-column absorption in a pentagonal-bipyramid expansion

**Status:** written proof; [separately audited GREEN](hc7_pentagonal_bipyramid_two_column_absorption_audit.md).  The displayed
fourteen-vertex application is checked by
[`hc7_pentagonal_bipyramid_two_column_absorption_verify.py`](hc7_pentagonal_bipyramid_two_column_absorption_verify.py).

This note isolates a label-preserving `K_5` construction which is not a
split of one column and is not one of the adjacent-rim Two Paths outcomes.
Two omitted columns may instead be divided between two neighbouring rim
branch sets.  The construction applies to columns of arbitrary order.

## 1. Setup

Let `P` be the pentagonal bipyramid, with nonadjacent poles `a,b` and rim

\[
                         r_0r_1r_2r_3r_4r_0.
\]

Let a graph contain seven pairwise disjoint connected columns

\[
                         C_a,C_b,C_0,C_1,C_2,C_3,C_4
\]

whose contact graph is exactly `P`.  Let `R_0,R_1` be disjoint connected
subgraphs outside the columns, adjacent to one another and each adjacent
to every column.

## 2. The absorption construction

### Theorem 2.1 (two-column absorption)

Suppose there are vertex-disjoint subgraphs `X_1,X_2` contained in

\[
                              C_a\cup C_0
\]

such that

\[
                         D_1=C_1\cup X_1,
                         \qquad D_2=C_2\cup X_2              \tag{2.1}
\]

are connected, and

\[
 E(D_1,C_3)\ne\varnothing,\qquad
 E(D_1,C_4)\ne\varnothing,\qquad
 E(D_2,C_4)\ne\varnothing.                                  \tag{2.2}
\]

Then the graph contains an explicit `K_7`-minor model.

### Proof

Consider the five sets

\[
                         C_b,\quad D_1,\quad D_2,\quad C_3,\quad C_4.
                                                                    \tag{2.3}
\]

They are pairwise disjoint: the four anchor columns are distinct, while
`X_1,X_2` are disjoint and lie in the two omitted columns `C_a,C_0`.
They are connected by the hypotheses and by connectedness of the columns.

The pole column `C_b` is adjacent to the other four sets through their
whole rim columns `C_1,C_2,C_3,C_4`.  Among those four rim anchors, the
three old consecutive rim edges

\[
                         C_1C_2,\qquad C_2C_3,\qquad C_3C_4
\]

supply three adjacencies.  The only missing pairs are

\[
                         D_1C_3,\qquad D_1C_4,\qquad D_2C_4,
\]

and these are precisely the three contacts in (2.2).  Thus the five sets
in (2.3) are branch sets of a `K_5` model.

Every branch set contains a different whole old column.  Consequently
both `R_0` and `R_1` are adjacent to all five branch sets.  The two roots
are adjacent to one another, so they and the five sets in (2.3) form seven
pairwise disjoint, connected and pairwise adjacent branch sets.  This is
an explicit `K_7`-minor model. \(\square\)

The statement is invariant under cyclic relabelling and reversal of the
rim, and under interchange of the two poles.

## 3. The combined-negative fourteen-vertex core

There is a five-connected nonplanar expansion on two vertices per column
which has no four-label alternating path cut and for which all five
adjacent-rim Two Paths instances are negative.  Those two local tests do
not make it a surviving host configuration: it satisfies Theorem 2.1.

Use numeric labels `0,1` for the poles and `2,3,4,5,6` for the cyclic rim.
Write

\[
                         C_x=\{(x,0),(x,1)\}.
\]

For the edge set recorded in the verifier, put

\[
\begin{aligned}
 X_1&=\{(0,1),(2,0)\},\\
 X_2&=\{(0,0),(2,1)\}.
\end{aligned}                                                  \tag{3.1}
\]

Take

\[
 a=0,\quad b=1,\quad
 (r_0,r_1,r_2,r_3,r_4)=(2,3,4,5,6).
\]

Both `X_i` are connected.  The five branch sets from (2.3) are therefore

\[
 C_1,\quad
 C_3\cup\{(0,1),(2,0)\},\quad
 C_4\cup\{(0,0),(2,1)\},\quad
 C_5,\quad C_6.                                               \tag{3.2}
\]

They partition all fourteen vertices and form a `K_5` model.  Hence this
finite combined-negative expansion is already excluded after the two
universal root branch sets are restored; contraction-critical colouring
responses are not needed for this particular graph.

## 4. Dynamic interpretation and trust boundary

The theorem gives a precise additional terminal pattern for a dirty Kempe
response path.  A response calculation is terminal if it can divide one
omitted pole column and one omitted rim column into two disjoint connected
pieces satisfying (2.1)--(2.2), even when neither single column admits an
alternating split and all five adjacent-rim linkage tests fail.

Nothing here proves that operation-selected Kempe paths always create those
two pieces.  In particular, a path may first enter the wrong named column,
different response paths may reuse the same literal vertices, and a
proper-minor colouring may return only an equality partition on a larger
boundary.  The remaining host-level theorem must therefore force one of:

1. the two disjoint absorbable pieces in Theorem 2.1;
2. a full order-seven separation carrying the same boundary partition on
   both closed shores; or
3. a strict descent preserving the selected proper-minor response.

The fourteen-vertex core proves that the first outcome is genuinely more
general than either previously isolated local positive mechanism.  It does
not prove the three-outcome host theorem or `HC_7`.
