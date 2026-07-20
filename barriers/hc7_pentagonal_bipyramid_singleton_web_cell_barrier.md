# A singleton web cell need not yield a named PB allocation

**Status:** barrier/counterexample to an intermediate structural claim;
[separately audited **GREEN**](hc7_pentagonal_bipyramid_singleton_web_cell_barrier_audit.md).
The audit is internal, not external peer review.  Computer-assisted finite
checks are reproduced by the
[`structural verifier`](hc7_pentagonal_bipyramid_singleton_web_cell_barrier_verify.py)
and the
[`root-placement sweep`](hc7_pentagonal_bipyramid_singleton_root_sweep_verify.py).
It is not a counterexample to the paired-rooted target.

## 1. Sufficient bridge exhaustion refuted

The following formally stated component-aware bridge theorem is false.

> **Four-outcome bridge exhaustion.**  Let `F,A,B` satisfy all hypotheses of
> [Conjectural Theorem 3.1](../active/hc7_pentagonal_bipyramid_paired_rooted_target.md).
> For every rim index `i`, put
> \(U_i=N_F(V(C_a))\cap V(C_i)\) and
> \(W_i=N_F(V(C_b))\cap V(C_i)\).  Suppose that, for every shortest
> `U_i`--`W_i` path `R` in `F[C_i]`, no component of
> `F[C_i]-V(R)` contacts both adjacent rim columns.  Then at least one of the
> following holds:
>
> 1. some column has the connected bipartition and four alternating contacts
>    specified in
>    [Corollary 2.2](../results/hc7_pentagonal_bipyramid_adjacent_rim_linkage.md#corollary-22-alternating-connected-column-split);
> 2. some adjacent pair of rim columns contains vertex-disjoint connected
>    subgraphs `X,Y` satisfying (2.1) of
>    [the adjacent-rim linkage theorem](../results/hc7_pentagonal_bipyramid_adjacent_rim_linkage.md#theorem-21-adjacent-rim-linkage-completion);
> 3. after an element of the full pentagonal-bipyramid symmetry group
>    \(D_5\mathbin{\times}C_2\), there are vertex-disjoint subgraphs
>    `X_1,X_2` in \(C_a\cup C_0\) for which the sets `D_1,D_2` defined in
>    (2.1) of the
>    [two-column absorption theorem](../results/hc7_pentagonal_bipyramid_two_column_absorption.md#theorem-21-two-column-absorption)
>    are connected and all three contacts in its (2.2) exist; or
> 4. `F` is four-colourable.

This theorem would imply Conjectural Theorem 3.1: a failure of its residual
hypothesis gives the proved off-path component transfer, each of its first
three conclusions gives a paired-rooted `K_5` model, and its last conclusion
is the chromatic outcome.  The graph below satisfies the residual hypothesis
but none of the four conclusions.

It also refutes the more local assertion that a singleton-terminal web cell
with at least three neighbours in its one owner column must yield one of the
three named positive mechanisms or a cut of order at most four.  Its valid
terminal is instead the new three-column chained absorption in Section 5, so
it is not a counterexample to the paired-rooted target itself.

## 2. Construction

Start with the fourteen-vertex
[four-colourable combined-negative PB core](hc7_pentagonal_bipyramid_four_colour_combined_negative.md),
using integer `2x+s` for its vertex `(x,s)`.  Add vertex `14` to pole
column `C_1`, adjacent to

\[
                         2,3,6,7,8,                            \tag{2.1}
\]

and add vertex `15` to rim column `C_3`, adjacent to

\[
                         2,3,5,6,14.                           \tag{2.2}
\]

Thus the seven columns are

\[
 \{0,1\},\ \{2,3,14\},\ \{4,5\},\ \{6,7,15\},\
 \{8,9\},\ \{10,11\},\ \{12,13\}.                          \tag{2.3}
\]

All new intercolumn edges respect old pentagonal-bipyramid adjacencies, so
the quotient remains exact.  Adding a vertex with at least five neighbours
to a five-connected graph preserves five-connectivity: after deleting at
most four vertices, the new vertex retains a neighbour in the connected old
graph.  Apply this first to `14` and then to `15`.  Conversely, the five
vertices in `N(15)` separate `15`, so the resulting connectivity is exactly
five.

The vertices

\[
                         \{2,3,6,14,15\}                       \tag{2.4}
\]

induce `K_5`.  In particular, this graph is not four-colourable.

With the root sets in (5.1), each column contains exactly one vertex of each
root set.  Since every column in (2.3) is connected, every column contains a
literal `A`--`B` path.  Thus the example satisfies every hypothesis of
Conjectural Theorem 3.1.

## 3. Literal singleton web cell

Take poles `0,1`, rim order `(2,3,4,5,6)`, and adjacent carrier

\[
                             Q=C_2\cup C_3.
\]

Write the four artificial terminals in outer order as

\[
                         t_0,t_6,t_1,t_4,                      \tag{3.1}
\]

corresponding to owner columns `C_0,C_6,C_1,C_4`.  Before inserting vertex
`15`, a plane rib has carrier vertices `4,5,6,7`, carrier edges

\[
                         45,67,46,47,56,                       \tag{3.2}
\]

and terminal neighbourhoods

\[
\begin{aligned}
 N(t_0)&=\{4,7\},&N(t_6)&=\{4,5\},\\
 N(t_1)&=\{5,6,7\},&N(t_4)&=\{7\}.
\end{aligned}                                                  \tag{3.3}
\]

Adding only the completion edges of the outer cycle, its ten inner faces
are

\[
\begin{gathered}
 465,\ 476,\ 4t_0 7,\ 4t_6t_0,\ 45t_6,\\
 56t_1,\ 5t_1t_6,\ 67t_1,\ 7t_0t_4,\ 7t_4t_1.
                                                               \tag{3.4}
\end{gathered}
\]

The frame is the outer face `t_0t_6t_1t_4`.  Every triangle of the rib is
one of the displayed faces.

Vertex `15` fills the facial gate `t_1,5,6`.  Its edges to `5,6` are
literal carrier edges of `F`.  The artificial edge `15t_1` is already in
the auxiliary graph because `15` has the three literal owner contacts

\[
                         15\,2,\quad15\,3,\quad15\,14.         \tag{3.5}
\]

It is not a web-completion edge.  The only completion-only edges in this
display are the four outer-frame edges between artificial terminals.  Thus
`X={15}` is exactly a singleton-terminal cell with two carrier gate
vertices and three distinct literal neighbours in its owner column `C_1`.

The resulting auxiliary graph is a `4`-web, so the prescribed crossing
paths are absent.  The verifier also checks this directly.

## 4. Exact negative mechanisms

The verifier exhausts every connected bipartition of every column and finds
no alternating split.  It exhausts the two connected subgraphs in all five
adjacent-rim carriers and finds no adjacent-rim linkage.  Finally, it checks
every cyclic orientation, rim reversal, and pole interchange of the audited
two-column absorption theorem and finds no absorption.

Independently, it enumerates all six shortest pole-portal paths across the
five rim columns and verifies the universal residual condition directly: no
component off such a path contacts both neighbouring rim columns.

Since the graph is five-connected, it has no cut of order at most four.
This proves the counterexample claimed in Section 1.

The failure is not explained by a disguised five-owner construction.  An
exhaustive allocation of vertices outside five nominated whole columns
checks `137,376` assignments and finds no `K_5` model with five distinct
whole-column owner bags.  The maximum number of branch sets admitting
distinct whole-column owners is four: the following model attains four,
while the exhaustive five-owner check proves the upper bound:

\[
 (1,48,3458,12288,16908),                                    \tag{4.1}
\]

or, as vertex sets,

\[
 \{0\},\ \{4,5\},\ \{1,7,8,10,11\},\ \{12,13\},\
 \{2,3,9,14\}.                                               \tag{4.2}
\]

The four owner columns are `C_2,C_5,C_6,C_1`, respectively after matching
them to the appropriate bags.

## 5. The surviving paired-rooted mechanism

This graph is positive for a more flexible allocation.  For

\[
 A=\{0,3,4,7,8,10,12\},\qquad
 B=\{1,2,5,9,11,13,15\},                                    \tag{5.1}
\]

the five sets

\[
 \{0,1\},\ \{4,5\},\ \{2,7\},\ \{3,8,15\},\
 \{9,10,11,12,13\}                                          \tag{5.2}
\]

form a paired-rooted `K_5` model.  Each root set has exactly one vertex in
every column.  This is the application of the separately stated
[three-column chained absorption theorem](../results/hc7_pentagonal_bipyramid_three_column_chained_absorption.md).

The same bags do not work for arbitrary endpoint choices: the last three
bags contain no five distinct whole-column owners and must literally meet
the chosen root sets.  The exact finite root sweep therefore enumerates all

\[
 (2\cdot3\cdot2\cdot3\cdot2\cdot2\cdot2)^2=82,944
\]

ordered choices of one `A`-vertex and one `B`-vertex in every column,
including all `1,152` choices that are columnwise disjoint.  It independently
enumerates all twenty oriented PB frames and verifies every hypothesis of the
three-column theorem for each candidate.  Exactly `98` distinct chained
models result, and between four and ninety-eight of them cover every root
placement.  A separate compact certificate of three fixed `K_5` models also
covers all `82,944` placements.

Consequently this fixed graph has the paired-rooted outcome for **every**
admissible root sets `A,B`: choose one vertex of each set in every column,
use the certified model for those minimal choices, and then apply
monotonicity.  This is a computer-assisted finite result, not an unbounded
theorem.

The example is therefore not a target counterexample for any root placement.
It shows instead that the first irreducible singleton cell already requires
more than the three older local mechanisms.  It decisively falsifies the
sufficient four-outcome bridge exhaustion in Section 1 and exposes a fifth,
reusable terminal mechanism: a root-sensitive multi-column allocation such
as (5.2).  The remaining alternatives are a compatible whole-graph
web/colouring argument or a strict colour-extending reduction.
