# Collapse of the unbalanced marked three-clique rows

**Status:** proved and independently audited.  This note closes the
unbalanced counting branch in the marked Mader reduction.  It uses no
predecessor graph and constructs no clique minor; its only conclusion is
that the three row sizes are forced into the balanced equality cell.

## Lemma (unbalanced-row collapse)

Let `H` be six-connected.  Let `L_1,L_2,L_3` be pairwise disjoint
five-vertex cliques with marked vertices `z_i in L_i`, and suppose that
every six-separator of `H` contains all three marked vertices.  In the
notation of the Mader certificate in
[`hc7_marked_three_clique_cut_reduction.md`](../active/hc7_marked_three_clique_cut_reduction.md),
put `w=|W|` and suppose

\[
  2\le w\le5,\qquad
  |B_i|\ge5-w\quad(i=1,2,3),\qquad
  \sum_{i=1}^3|B_i|\le3(6-w).                 \tag{1}
\]

Here the three rows `A_i`, and hence the `B_i`, are pairwise disjoint,
`L_i-W subseteq A_i`, and a nonempty row tail `A_i-B_i` is separated from
the other rows by `W union B_i`.

Then

\[
                         |B_1|=|B_2|=|B_3|=6-w.                \tag{2}
\]

### Proof

It is enough to exclude a row of order `5-w`.  Indeed, after that every
row has order at least `6-w`, and the sum bound in (1) forces equality in
all three rows.

Suppose, therefore, that

\[
                             |B_h|=5-w.                         \tag{3}
\]

The tail `A_h-B_h` is empty.  Otherwise `W union B_h` is a separator of
order five, contrary to six-connectivity.  Since
`L_h-W subseteq A_h=B_h`, we have

\[
  5-|W\cap L_h|=|L_h-W|\le |B_h|=5-w.
\]

Thus `|W cap L_h|>=w`; because `|W|=w`, this says

\[
                             W\subseteq L_h.                    \tag{4}
\]

In fact `B_h=L_h-W`, although only (4) is needed below.  The named
cliques are disjoint, so a row satisfying (3) is unique, and for each
`j ne h`

\[
              W\cap L_j=\varnothing,qquad L_j\subseteq A_j.   \tag{5}
\]

Fix `j ne h`.  If `A_j-B_j` is empty, (5) gives

\[
                              |B_j|\ge5.                         \tag{6}
\]

If `A_j-B_j` is nonempty, six-connectivity first gives
`|W union B_j|>=6`, hence `|B_j|>=6-w`.  Equality cannot hold.  For if
`|B_j|=6-w`, then `W union B_j` is a six-separator.  Let `k` be the third
row.  By (4), `W` is contained in `L_h`; by disjointness of the rows and
the named cliques, the mark `z_k` belongs to neither `W` nor `B_j`.
Consequently this six-separator omits `z_k`, contrary to the marked-cut
hypothesis.  Therefore every nonempty tail outside row `h` satisfies

\[
                              |B_j|\ge7-w.                       \tag{7}
\]

There are now three possibilities for the two rows different from `h`.
If both have tails, (3) and (7) give

\[
  \sum_i|B_i|\ge(5-w)+2(7-w)=19-3w>18-3w.
\]

If exactly one has a tail, (3), (6), and (7) give

\[
  \sum_i|B_i|\ge(5-w)+(7-w)+5=17-2w>18-3w,
\]

where the strict inequality is `w>1`.  If neither has a tail, (3) and
(6) give

\[
  \sum_i|B_i|\ge(5-w)+10=15-w>18-3w,
\]

where the strict inequality is `2w>3`.  Each conclusion contradicts the
upper bound in (1).  Hence no row has order `5-w`, and (2) follows.
\(\square\)

## Consequence and trust boundary

Together with the audited counting inequalities in the source reduction,
the lemma shows that every marked Mader certificate in the range
`2<=|W|<=5` automatically lies in the balanced equality cell.  In
particular, there is no separate unbalanced branch to be handled by the
predecessor decoders.

Combining this collapse with the audited balanced decoders eliminates the
entire range `2<=|W|<=5` in the actual minimal-three-contraction route.
The `|W|=6` branch was already excluded, while the balanced `|W|<=1`
branch was already closed.  Thus the only outcomes of this Mader route not
yet eliminated are the **unbalanced** `|W|=0,1` outcomes.

The lemma does **not** eliminate the balanced cells by itself, close those
remaining low-`W` outcomes, prove the marked three-clique theorem, prove
the global support-six theorem, or prove `HC_7`.
