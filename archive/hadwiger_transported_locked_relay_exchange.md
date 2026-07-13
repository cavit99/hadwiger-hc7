# The transported locked relay has a literal detour exchange

## 1. Setting

Use Sections 4--5 of `hadwiger_transported_degree8_leaf_closure.md`.
Thus `u` has degree eight, its neighbourhood is

\[
 U=P\dot\cup\{w\}\dot\cup\{y_s:s\in S-P\},
\]

the old boundary satisfies
`\overline {G[S]}=C_6\dot\cup K_1`, and the two components outside
`N[u]` are `F` and `R`, with

\[
 N_U(F)=U-\{w\},\qquad U-N_U(R)=\{p\}\quad(p\in P).
\tag{1.1}
\]

Assume that an old-boundary four-clique `T` contains `P`.  Put

\[
 Q=T-P,\qquad Y_0=\{y_s:s\in S-T\}.
\tag{1.2}
\]

The locked state is

\[
 N_U(p)\cap(Y_0\cup\{w\})=\varnothing,
 \qquad N_U(p)\cap\{y_q:q\in Q\}\ne\varnothing.
\tag{1.3}
\]

The point of the exchange below is that the private relay `y_q` cannot
simply be peeled from the canonical bag `\{q,y_q\}`: the leftover
singleton `q` is not a member of `U`.  Instead one replaces `y_q` by a
private relay from the opposite prism triangle.

## 2. The detour exchange

### Theorem 2.1 (locked-relay closure)

Under (1.1)--(1.3), `G-u` contains a `U`-meeting `K_6`-model.
Consequently `G` contains a `K_7`-minor.

### Proof

Write the old boundary as the triangular prism on six vertices together
with its universal vertex `z`.  Every old-boundary four-clique is one
prism triangle together with `z`.  Hence

\[
                     S-T
\]

is the other prism triangle.  Choose `q in Q` such that `py_q` is an
edge, as supplied by (1.3).  There is a vertex `r in S-T` adjacent to
`q`: if `q=z`, every choice works; if `q` belongs to the prism triangle
in `T`, take its matching neighbour in the opposite prism triangle.

Replace the canonical relay bag `\{q,y_q\}` by

\[
                         C_q=\{q,r,y_r\}.          \tag{2.1}
\]

This is connected, since both `qr` and `ry_r` are edges, and it meets
`U` at `y_r`.  Keep the canonical bags

\[
 \{\{x\}:x\in P\}\ \cup
 \{\{x,y_x\}:x\in Q-\{q\}\}.                    \tag{2.2}
\]

Together with `C_q`, these are four pairwise adjacent bags: use their
representatives in the clique `T`.  Notice that `r` is outside `T`, so
no trace in (2.2) has been reused.

Choose any `a in S-T-\{r\}`; there are two choices.  In the transported
partition `F` is exactly the component induced by `H union(S-P)` (there
are no hidden vertices or further components inside `F`).  Put

\[
 A'=F-(Q\cup\{r\}),\qquad
 B_A=A'\cup\{y_a\},\qquad
 B_R=R\cup\{y_q\}.                                \tag{2.3}
\]

The graph `A'` is connected.  Indeed it contains the connected old full
shore `H`, and every remaining old-boundary vertex in
`S-P-(Q\cup\{r\})` has a neighbour in `H`.  It contains `a`, so
`B_A` is connected through the edge `ay_a`; it meets `U` at `y_a`.
The bag `B_R` is connected because `R` sees `y_q` by (1.1), and it
meets `U` at `y_q`.

We check all remaining adjacencies.

* `B_A` is adjacent to each of the four row bags through the full
  contacts of `H` with the representative in `T`.
* `B_R` is adjacent to every unchanged row bag other than `\{p\}`
  because `R` sees every member of `U-\{p\}`.  It is adjacent to
  `\{p\}` through the edge `py_q`.
* `B_R` is adjacent to `C_q` through the edge `qy_q` (and also through
  an `R-y_r` edge).
* Finally `B_A` and `B_R` are adjacent because `R` sees `y_a`.

Thus the four row bags in (2.1)--(2.2), together with `B_A,B_R`, are
six pairwise adjacent, disjoint, connected bags, and every bag meets
`U`.  They form a `U`-meeting `K_6`-model in `G-u`.  Adding the
singleton bag `\{u\}` gives a `K_7`-model.  QED.

## 3. Consequence and exact remaining row

Theorem 2.1 eliminates the whole locked four-clique residue of Section 5
of the transported-leaf note.  This is independent of the orders and
internal structures of both exterior components.

The only transported two-shore row not covered by that note and this
exchange is therefore the antipodal row: `P` contains a matching edge of
the prism and is not contained in an old-boundary four-clique.  That row
is genuinely different, because the four vertices outside its
three-clique form only two crossed relay pairs; there is no opposite
three-vertex clique from which to take the detour (2.1).
