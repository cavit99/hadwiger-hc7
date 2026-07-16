# Closure of the balanced `|W|=2` marked three-clique cell

**Status:** proved and independently cold-audited in
[`hc7_marked_three_clique_w2_closure_audit.md`](hc7_marked_three_clique_w2_closure_audit.md).
This note closes exactly the `|W|=2` branch left in Section 4 of
[`hc7_marked_three_clique_cut_reduction.md`](hc7_marked_three_clique_cut_reduction.md).
It does not address the branches `3<=|W|<=5` or prove the marked
three-clique theorem by itself.

## 1. Standing cell

Let `H` be a six-connected, `K_7`-minor-free graph containing pairwise
disjoint cliques

\[
                         L_1,L_2,L_3\cong K_5
\]

with prescribed vertices `z_i in L_i`.  Assume the marked-cut law

\[
 T\text{ a six-separator of }H
 \quad\Longrightarrow\quad
 \{z_1,z_2,z_3\}\subseteq T.                       \tag{1.1}
\]

Use the maximal Robertson--Seymour--Thomas/Mader certificate and the
notation `W`, `Y_j`, `X_j`, `A_i`, `B_i` from the cut-reduction note.
Suppose its balanced equality branch has `|W|=2`.  Section 4 of that note
then gives, after relabelling,

\[
\begin{gathered}
 W=\{z_2,z_3\},\qquad m=4,\qquad
 |X_1|=\cdots=|X_4|=3,\qquad |B_i|=4,              \tag{1.2}\\
 A_2=B_2=L_2-z_2,\qquad A_3=B_3=L_3-z_3,           \tag{1.3}\\
 A_1-B_1\ne\varnothing,\qquad z_1\in B_1,         \tag{1.4}
\end{gathered}
\]

and the four large cells partition the three rows:

\[
 X_1\mathbin{\dot\cup}\cdots\mathbin{\dot\cup}X_4
 =B_1\mathbin{\dot\cup}B_2\mathbin{\dot\cup}B_3. \tag{1.5}
\]

The remaining nonempty `X`-sets, if any, are singletons.  This follows
directly from the Mader budget: the four three-sets already contribute all
four units left after `|W|=2`.

## 2. The exact row--cell incidence

### Lemma 2.1

For every `i in {1,2,3}` and `j in {1,2,3,4}`,

\[
                            |B_i\cap X_j|=1.         \tag{2.1}
\]

Moreover, `Y_j=X_j` for each of the four large cells.

### Proof

Since `|W union X_j|=5<6`, the Mader separation axiom and
six-connectivity imply `Y_j=X_j`: if `Y_j-X_j` were nonempty, then
`W union X_j` would separate it from the other cells.

Fix `i,j`, and put `r=|B_i cap X_j|`.  Suppose `r>=2`.  The set

\[
                    T=W\cup(B_i\mathbin\triangle X_j)             \tag{2.2}
\]

separates

\[
              (B_i\cap X_j)\cup(A_i-B_i)                         \tag{2.3}
\]

from a vertex of another row outside `X_j`.  Here is the direct check,
so no claw-free source conclusion is being imported.  An edge from a
vertex of `B_i cap X_j` to outside `X_j` survives in the auxiliary graph
obtained by deleting cell-internal edges, and hence stays inside `A_i`.
The vertices of `B_i-X_j` are deleted by `T`.  Every vertex of
`A_i-B_i` belongs to a singleton cell: all large cells occur in (1.5).
That singleton cell equals its `X`-set, since its union with `W` has order
three.  Thus every edge from such a vertex outside `W` again survives in
the auxiliary graph and stays inside `A_i`.  This proves the asserted
separation.  Its first side is nonempty because `r>=2`; its second side is
nonempty because a different four-vertex row has a vertex outside the
three-set `X_j`.

But

\[
 |T|=|W|+|B_i|+|X_j|-2r=2+4+3-2r\le5,             \tag{2.4}
\]

contrary to six-connectivity.  Therefore `r<=1`.  Each `B_i` has four
vertices and, by definition and (1.5), is contained in the union of the
four cells.  Hence equality holds for every `i,j`.  \(\square\)

Write

\[
                         B_i\cap X_j=\{x_{ij}\}.    \tag{2.5}
\]

There is a unique index `j_0` such that

\[
                              x_{1j_0}=z_1.          \tag{2.6}
\]

## 3. Marked minimum degree forces the needed contacts

### Lemma 3.1

The following literal edges exist:

1. every vertex of `W` is adjacent to every vertex of `B_2 union B_3`;
2. `z_1x_{2j_0}` and `z_1x_{3j_0}` are edges; and
3. `x_{2j}x_{3j}` is an edge for every `j ne j_0`.

### Proof

Take `x=x_{2j}`.  Since `Y_j=X_j`, an edge from `x` to outside `X_j`
survives in the auxiliary graph and its other end belongs to the same
auxiliary component, hence to `A_2`, unless that end lies in `W`.
Using (1.3) and Lemma 2.1 gives

\[
 N_H(x)\subseteq
 (B_2-\{x\})\cup\{z_2,z_3\}\cup\{x_{1j},x_{3j}\}. \tag{3.1}
\]

The set on the right has order seven.  The clique `L_2` already supplies
the four neighbours

\[
                         (B_2-\{x\})\cup\{z_2\}.    \tag{3.2}
\]

Six-connectivity gives `d_H(x)>=6`.

If `d_H(x)=7`, then `x` sees the entire set in (3.1).  If `d_H(x)=6`,
then `N_H(x)` is a six-separator: deleting it isolates `x`, and vertices
remain outside `N_H[x]` because the three disjoint five-cliques give at
least fifteen vertices.  The marked-cut law (1.1) therefore puts all
three marks in `N_H(x)`.  In particular `xz_3` is an edge.  If `j=j_0`,
it also forces `xx_{1j_0}=xz_1`.  If `j ne j_0`, then `z_1` is not in the
seven-vertex envelope (3.1), so degree six is impossible and `x` has
degree seven.

Consequently `z_3` is complete to `B_2`, every `x_{2j}` sees `x_{1j}`,
and `x_{2j}` sees `x_{3j}` whenever `j ne j_0`.  The vertex `z_2` is
already complete to `B_2` through the clique `L_2`.

The symmetric argument with rows two and three interchanged shows that
`z_2` is complete to `B_3`, every `x_{3j}` sees `x_{1j}`, and
`x_{3j}` sees `x_{2j}` for `j ne j_0`.  The vertex `z_3` is complete to
`B_3` through `L_3`.  This proves all three assertions.  \(\square\)

## 4. Literal `K_7` decoder

### Theorem 4.1

The balanced `|W|=2` cell (1.2)--(1.5) cannot occur under the standing
hypotheses.

### Proof

Put

\[
                              S=W\cup B_1.           \tag{4.1}
\]

This is a six-separator by the source cell axiom because
`A_1-B_1` is nonempty.  The binary-cut corollary in the cut-reduction note
says that `H-S` has exactly two components.  Let `P` be the component
containing a vertex of `A_1-B_1`.  In fact all of `A_1-B_1` lies in `P`:
the source separation puts it on the side opposite the nonempty set
`V(H)-A_1-W` (which contains `B_2 union B_3`), so two different tail
components would give at least three components of `H-S`.  In particular
`P` contains no vertex of `B_2 union B_3`.

The component `P` is `S`-full.  Indeed, `N_H(P)` is contained in `S`; if
it were a proper subset, it would have order at most five and would
separate `P` from the other component of `H-S`, contrary to
six-connectivity.  In particular there is a `z_2-z_3` path `R` whose
internal vertices lie in `P`.  Split `R` across any one of its edges into
two disjoint connected bags `D_2,D_3`, with `z_2 in D_2` and
`z_3 in D_3`.  The two bags are adjacent.

Now define

\[
                             C=B_3\cup\{z_1\}.       \tag{4.2}
\]

This bag is connected: `B_3` is the four-vertex clique `L_3-z_3`, and
Lemma 3.1 gives the edge `z_1x_{3j_0}`.  Consider the following seven
branch sets:

\[
       \{x_{21}\},\ \{x_{22}\},\ \{x_{23}\},\ \{x_{24}\},
       \quad D_2,\quad D_3,\quad C.                  \tag{4.3}
\]

They are pairwise disjoint and connected.  The first four are pairwise
adjacent because `B_2=L_2-z_2` is a clique.  Both `D_2` and `D_3` are
adjacent to every one of them: their respective vertices `z_2,z_3` are
complete to `B_2` by Lemma 3.1.  The bag `C` meets every core singleton:
for `j ne j_0` use the edge `x_{2j}x_{3j}`, and for `j=j_0` use the edge
`x_{2j_0}z_1`.

Finally, `D_2` is adjacent to `C` because `z_2` is complete to `B_3`,
and `D_3` is adjacent to `C` because `z_3` is complete to `B_3` through
the clique `L_3`.  Together with the split edge between `D_2,D_3`, these
are all remaining adjacencies.  Thus (4.3) is a literal `K_7` model,
contrary to the standing assumption.  \(\square\)

## 5. Exact consequence and trust boundary

Combining Theorem 4.1 with the earlier cut reduction removes `|W|=2`
from the balanced equality branch.  Its live range is now

\[
                  3\le |W|\le5,qquad
                  \{z_1,z_2,z_3\}\subseteq W,
\]

with all three row tails nonempty.

The proof used only:

* the exact Mader cell axioms and maximal-certificate arithmetic;
* six-connectivity and the all-three-marks law for six-separators;
* the previously proved binary-cut corollary; and
* the three literal `K_5` cliques.

It did not use claw-freeness, minimum degree seven, contraction-critical
colouring states, or any unproved portal/rerouting assertion.
