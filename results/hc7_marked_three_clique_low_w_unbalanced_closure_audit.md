# Cold audit of the unbalanced `|W|=0,1` closure

**Verdict:** GREEN after the capacity normalization was weakened from an
equality to the correct inequality.

Audited source:
[`hc7_marked_three_clique_low_w_unbalanced_closure.md`](hc7_marked_three_clique_low_w_unbalanced_closure.md).

Source SHA-256:

```text
4b28d2332cda5ac92c2f314115964000bc6a3bc0bc207dd0edd43804a9d9fd7d
```

The deficient-row separator, every symmetric-difference separator, the
opposite-shore witnesses, the marked-vertex placement, the capacity
arithmetic, and the `w=1` uniqueness argument are valid.  No predecessor
split is used.

## 1. Exact input and the deficient row

The proof uses the audited Mader data:

* `H` is six-connected;
* every six-separator contains the three prescribed marks;
* the auxiliary rows `A_i` are disjoint, contain `L_i-W`, and have
  `B_i` equal to their vertices in large traces;
* a nonempty tail `A_i-B_i` is separated from the other rows by
  `W union B_i`;
* the row bounds and cell budget stated in Section 1 of the source hold;
  and
* all named-clique vertices in a cell belong to its trace.

If an unbalanced vector had no row of order `5-w`, every integer row order
would be at least `6-w`, and the sum upper bound would make all three equal
to `6-w`.  Thus the deficient row `h` exists.

If its tail were nonempty, `W union B_h` would have order five.  The tail
is one nonempty open side.  At least one of the other two disjoint
five-cliques has a vertex outside `W`; that vertex lies in another disjoint
row and supplies the opposite side.  Hence this is a genuine forbidden
separator, so `A_h=B_h`.

The containment `L_h-W subseteq B_h` and `|B_h|=5-w` then force

\[
                         W\subseteq L_h,\qquad B_h=L_h-W.       \tag{1.1}
\]

This reasoning also proves uniqueness when `w=1`: a second order-four row
would force the same nonempty singleton `W` into a second disjoint
five-clique.

## 2. The symmetric-difference shore is literal

For a large trace `X` of order `2f+1`, put

\[
 r=|B_h\cap X|,\qquad
 T=W\cup(B_h\mathbin\triangle X),\qquad
 Z=(B_h\cap X)\cup(Y-X).
\]

The inclusion `N_H(Z) subseteq T` is exact.

* A vertex of `Y-X` can leave its cell only through `W`.
* An edge from `B_h cap X` to another cell survives deletion of
  cell-internal edges.  Its endpoint lies in the same auxiliary row
  `A_h=B_h`, hence in `B_h-X`.
* Edges remaining inside the cell end in `Z` or `X-B_h subseteq T`.

The boundary order is

\[
                         |T|=6+2(f-r).             \tag{2.1}
\]

If `r>f`, then `Z` is nonempty and `|T|<=4`.  A five-clique outside row
`h` has a vertex outside `T`; the Mader terminal condition prevents that
vertex from lying in `Y-X`, and disjointness from `L_h` prevents it from
lying in `B_h cap X`.  It is therefore genuinely outside `Z union T`.
This would be a separator below order six, proving `r<=f`.

If `r=f`, then `Z` is again nonempty and `|T|=6`.  The two outside
five-cliques have ten disjoint vertices, so a six-set cannot contain both.
Choose a named-clique vertex outside `T`; the same terminal and row
disjointness checks keep it outside `Z`.  Thus `T` is a genuine
six-separator.

By (1.1), neither outside marked vertex belongs to `W union B_h`.  The
marked-cut law consequently puts both in `X-B_h`.  Since distinct traces
are disjoint, at most one large cell can be tight (`r=f`).

## 3. Capacity and number of cells

Write

\[
 C=\sum_{j:\ X_j\text{ large}}f_j\le6-w,
 \qquad r_j=|B_h\cap X_j|.
\]

The large traces partition `B_h`, so `sum_j r_j=5-w`.  With `r_j<=f_j`,

\[
 0\le s:=\sum_j(f_j-r_j)=C-(5-w)\le1.             \tag{3.1}
\]

If `s=0`, every large cell is tight and the preceding uniqueness gives
`m<=1`.  If `s=1`, exactly one cell has slack one and the other `m-1`
cells are tight; hence `m-1<=1`.  Uniformly,

\[
                              m\le2.                \tag{3.2}
\]

The source correctly does not assume budget equality.  The total order of
the large traces is

\[
  \sum_{j:\ X_j\text{ large}}|X_j|=2C+m
       \le2(6-w)+m\le14-2w.                       \tag{3.3}
\]

## 4. Final contradictions

For `w=0`, the three disjoint rows have total order at least fifteen,
while (3.3) leaves at most fourteen vertices in all large traces.

For `w=1`, the deficient row has order four and is unique.  The other two
integer row orders are therefore at least five, so the rows occupy at
least fourteen large-trace vertices.  Equation (3.3) permits at most
twelve.  Both cases are impossible.

## 5. Scope

The theorem closes exactly the low-`W` unbalanced outcomes of the marked
Mader certificate.  It does not itself construct a clique minor or prove
the preceding Mader reduction.  Combined with those already audited
reductions and the predecessor decoders, it removes the final low-`W`
certificate residue in the actual minimal-three-contraction branch.
