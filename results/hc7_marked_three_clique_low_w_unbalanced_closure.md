# Closure of the unbalanced `|W|=0,1` marked rows

**Status:** proved and independently cold-audited in
[`hc7_marked_three_clique_low_w_unbalanced_closure_audit.md`](hc7_marked_three_clique_low_w_unbalanced_closure_audit.md).

This note closes the two low-`W` outcomes left by the audited marked
three-clique reduction.  The mechanism is a capacity argument over all
large Mader cells.  A row of minimum possible order has total capacity
defect at most one.  Every capacity-tight cell would give a six-cut and
must therefore contain both outside marked vertices.  Since the cells are
disjoint, there can be at most one such tight cell, leaving too little
total cell capacity for the three rows.

No predecessor splitting is used in this lemma.

## 1. Setup

Let `H` be six-connected.  Let `L_1,L_2,L_3` be pairwise disjoint
five-vertex cliques, with marked vertices `z_i\in L_i`, and suppose that
every six-separator of `H` contains all three marks.

Use a maximal Mader certificate and the notation of
[`hc7_marked_three_clique_cut_reduction.md`](../active/hc7_marked_three_clique_cut_reduction.md).
Put `w=|W|\in\{0,1\}`.  Every nonempty `X`-cell has odd order, and the
Mader budget gives

\[
                  \sum_j\left\lfloor {|X_j|\over2}\right\rfloor\le6-w.
                                                                    \tag{1.1}
\]

Call a cell **large** when `|X_j|\ge3`, and write

\[
                         |X_j|=2f_j+1\qquad(f_j\ge1)               \tag{1.2}
\]

for the large cells.  Singleton cells make no contribution to (1.1).  Put

\[
                         C:=\sum_{j\text{ large}}f_j\le6-w.       \tag{1.3}
\]

The three disjoint Mader rows satisfy

\[
                         |B_i|\ge5-w,qquad
                         \sum_i|B_i|\le3(6-w),                    \tag{1.4}
\]

and each `B_i` is contained in the union of the large `X_j`.
We also retain the defining cell properties

\[
 N_H(Y_j-X_j)\subseteq W\cup Y_j,
 \qquad
 Y_j\cap(L_1\cup L_2\cup L_3)\subseteq X_j,                    \tag{1.5}
\]

and the auxiliary graph defining `A_i` is obtained from `H-W` by deleting
every edge internal to a cell.  Thus the cross-cell argument used below is
literal, not an assumed cell adjacency.

Suppose the row vector is unbalanced.  Integrality and (1.4) give an
index `h` with

\[
                              |B_h|=5-w.                           \tag{1.6}
\]

Indeed, if every row had order at least `6-w`, equality would hold in all
three rows.

## 2. The deficient row and its cell capacities

### Lemma 2.1 (the deficient row is a named clique remainder)

The row tail `A_h-B_h` is empty and

\[
                         W\subseteq L_h,qquad B_h=L_h-W.          \tag{2.1}
\]

### Proof

If the tail were nonempty, the source row separation would make
`W\cup B_h` a separator of order five.  The tail is one nonempty open
side.  At least one of the two named cliques different from `L_h` has a
vertex outside `W`; its row is disjoint from `A_h`, so the opposite open
side is also nonempty.  This contradicts six-connectivity.

Thus `A_h=B_h`.  Since `L_h-W\subseteq A_h`,

\[
             5-|W\cap L_h|=|L_h-W|\le |B_h|=5-w.
\]

It follows that `|W\cap L_h|\ge w=|W|`, and hence `W\subseteq L_h`.
All displayed inequalities are then equalities, proving
`B_h=L_h-W`.  \(\square\)

For a large cell `X_j`, put

\[
                         r_j=|B_h\cap X_j|.                       \tag{2.2}
\]

### Lemma 2.2 (at most one unit of slack and at most two cells)

For every large cell,

\[
                              r_j\le f_j.                         \tag{2.3}
\]

Moreover,

\[
                  0\le\sum_j(f_j-r_j)=C-(5-w)\le1,               \tag{2.4}
\]

and at most one large cell satisfies `r_j=f_j`.  Consequently the number
`m` of large cells satisfies

\[
                              m\le2.                              \tag{2.5}
\]

### Proof

Fix a large cell and abbreviate `X=X_j`, `Y=Y_j`, `f=f_j`, and `r=r_j`.
Consider

\[
                         T=W\cup(B_h\mathbin\triangle X).         \tag{2.6}
\]

The standard symmetric-difference shore is

\[
                         Z=(B_h\cap X)\cup(Y-X).                  \tag{2.7}
\]

Because the deficient row has no tail, a direct edge check gives
`N_H(Z)\subseteq T`.  Indeed, a vertex of `Y-X` can leave `Y` only through
`W`, while an edge from `B_h\cap X` to a different cell remains in the
auxiliary graph defining `A_h=B_h` and therefore ends in `B_h-X`.

The boundary order is

\[
 \begin{aligned}
 |T|
   &=w+(5-w)+(2f+1)-2r\\
   &=6+2(f-r).                                                    \tag{2.8}
 \end{aligned}
\]

If `r>f`, then `r>0`, so `Z` is nonempty and (2.8) is at most four.
The opposite side is also nonempty: an order-at-most-four set cannot
contain either of the two five-cliques with label different from `h`, and
a named-clique vertex outside `T` cannot lie in `Y-X` by the Mader terminal
condition.  Thus `T` would be a genuine separator of order below six, a
contradiction.  This proves (2.3).

If `r=f`, the same argument shows that `T` is a genuine six-separator:
`r=f\ge1` makes `Z` nonempty, and a six-set cannot contain both of the two
disjoint outside five-cliques.  The marked-cut law puts `z_a,z_b` in `T`,
where `\{a,b,h\}=\{1,2,3\}`.  By (2.1), neither outside mark lies in
`W\cup B_h`; hence

\[
                              z_a,z_b\in X-B_h.                   \tag{2.9}
\]

Two distinct large cells cannot both satisfy (2.9), because the `X_j`
are disjoint.  Hence at most one cell is tight.

Finally, `B_h` is contained in the union of the large cells, so (1.3),
(1.6), and (2.2) give

\[
             \sum_j(f_j-r_j)=C-(5-w).
\]

The left side is nonnegative by (2.3), while `C\le6-w`; this proves
(2.4).  If it is zero, every cell is tight and hence `m\le1`.  If it is
one, exactly one cell has slack one and every other cell is tight.  Since
at most one cell is tight, in this case `m\le2`.  This proves (2.5).
\(\square\)

## 3. The low-`W` contradiction

### Theorem 3.1 (unbalanced low-`W` closure)

No unbalanced Mader row vector exists for `w\in\{0,1\}` under the standing
hypotheses.

### Proof

The total order of all large cells is, by (1.2)--(1.3),

\[
             \sum_{j:\ X_j\text{ large}}|X_j|
                 =2C+m\le2(6-w)+m\le14-2w.                     \tag{3.1}
\]

The three `B_i` are disjoint subsets of these cells.

If `w=0`, (3.1) gives a total large-cell order at most `12+2=14`.
But (1.4) requires the three disjoint rows to have total order
at least fifteen, a contradiction.

Let `w=1`.  The deficient row `h` is unique.  Indeed, a second row `i`
of order four would have an empty tail by the same genuine five-cut
argument as Lemma 2.1, and then `L_i-W\subseteq B_i` would force
`W\subseteq L_i`.  This is impossible because Lemma 2.1 gives
`W\subseteq L_h`, `W` is nonempty, and the named cliques are disjoint.
Thus the other two rows have order at least five, and

\[
                    \sum_i|B_i|\ge4+5+5=14.                     \tag{3.2}
\]

But the rows are disjoint subsets of the large cells, whose total order
is at most `14-2w=12` by (3.1).  This is a contradiction.  \(\square\)

## 4. Consequence and trust boundary

The theorem eliminates exactly the unbalanced `|W|=0,1` outcomes.  When
combined with the already audited balanced low-`W` decoder, the unbalanced
collapse for `2\le|W|\le5`, the balanced predecessor decoders, and the
`|W|=6` exclusion, it removes every Mader certificate in the actual
minimal-three-contraction branch.

This combination still requires an end-to-end audit of the marked
three-clique reduction before promotion as a closure of that branch.  It
does not address a minimal bad contraction set of order two, the global
support-six theorem, or `HC_7`.
