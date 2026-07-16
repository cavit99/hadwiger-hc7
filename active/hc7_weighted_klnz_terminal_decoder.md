# Weighted decoder for the disjoint three-clique terminal cell

## Status

Proved and independently audited.  This is a conditional decoder for the
terminal equality cell in the Kawarabayashi--Luo--Niu--Zhang three-clique
argument.  It does not assert that weighted connectivity alone reaches that
cell.

The conclusion is exact: either one of the standard KLNZ cuts expands to an
actual order-seven separator in the original graph, or the entire incidence
matrix is the single diagonal-special pattern displayed in Theorem 2.1.

## 1. Setup

Let `H` contain three pairwise disjoint literal cliques

\[
                         L_1,L_2,L_3\cong K_5,
\]

and choose distinguished vertices `z_i in L_i`.  Give each `z_i` weight
two and every other vertex weight one.  Thus

\[
                 w(T)=|T|+|T\cap\{z_1,z_2,z_3\}|.
\]

Assume that every vertex separator of `H` has weight at least seven.  This
is precisely the separator law obtained by contracting a matching of three
split bags in a seven-connected graph.

Suppose there are pairwise disjoint five-sets `X_1,X_2,X_3` with

\[
 L_1\mathbin{\dot\cup}L_2\mathbin{\dot\cup}L_3
   =X_1\mathbin{\dot\cup}X_2\mathbin{\dot\cup}X_3                 \tag{1.1}
\]

and

\[
             a_{ij}:=|L_i\cap X_j|\in\{1,2\}.                    \tag{1.2}
\]

Every row and every column of the matrix `A=(a_ij)` has sum five, so every
row and column is a permutation of `(1,2,2)`.

Finally assume the separator conclusion furnished by KLNZ 3.2.16 after
the published argument has reached its terminal equality cell
`W=Z=emptyset`:

\[
 C_{ij}:=X_j\mathbin\triangle L_i
 \quad\hbox{is a vertex separator whenever }a_{ij}=2.             \tag{1.3}
\]

Since both sets in the symmetric difference have order five,

\[
                         |C_{ij}|=6                               \tag{1.4}
\]

for every pair covered by (1.3).

For the shore description in Section 3 we also retain the side conclusion
of KLNZ 3.2.16: in `H-C_ij`, the set `X_j cap L_i` is separated from every
vertex of `(L_1 union L_2 union L_3)-L_i-C_ij`.  Before the terminal cell,
the published cut is

\[
             (X_j\mathbin\triangle L_i)\cup W\cup Z,
\]

not merely `C_ij`.  Theorem 2.1 itself uses only the explicit assumption
(1.3); the added side conclusion is used only in Section 3.

## 2. Exact decoder

### Theorem 2.1 (terminal-cell weighted decoder)

Under the hypotheses in Section 1, exactly one of the following outcomes
holds.

1. Some standard separator `C_ij` has weight seven.
2. After independently relabelling the three cliques and the three cells,

   \[
                L_i\cap X_i=\{z_i\}\quad(i=1,2,3),                \tag{2.1}
   \]

   and

   \[
                |L_i\cap X_j|=2\quad(i\ne j).                    \tag{2.2}
   \]

In the second outcome every separator in (1.3) has weight eight and
contains exactly two of the three distinguished vertices.

### Proof

For a fixed column `j`, put

\[
                  Z_j=X_j\cap\{z_1,z_2,z_3\},
                  \qquad t_j=|Z_j|.
\]

If `a_ij=2`, then direct inspection of the symmetric difference gives

\[
 |C_{ij}\cap\{z_1,z_2,z_3\}|
  = {\bf 1}_{z_i\notin X_j}
    +|Z_j-\{z_i\}|.                                                \tag{2.3}
\]

First suppose `t_j=0`.  Formula (2.3) equals one for either of the two
rows with `a_ij=2`.  Hence `w(C_ij)=7`.

Next suppose `t_j=2`.  The column has two entries equal to two and one
entry equal to one.  At least one of the two distinguished vertices in
`Z_j` belongs to a row `i` with `a_ij=2`.  For that row, (2.3) again
equals one, and `w(C_ij)=7`.

Thus outcome 1 holds whenever some `t_j` is zero or two.  It also holds
when some `t_j` is larger than two only after using another column: since

\[
                            t_1+t_2+t_3=3,                         \tag{2.4}
\]

a value `t_j=3` forces a different column to have value zero.  Likewise,
the distribution `(2,1,0)` contains both cases already handled.
Consequently failure of outcome 1 forces

\[
                            t_1=t_2=t_3=1.                         \tag{2.5}
\]

Let `z_i` be the unique distinguished vertex in `X_j`.  If `a_ij=2`,
then (2.3) is zero.  Equations (1.3)--(1.4) would make `C_ij` a separator
of weight six, contrary to weighted connectivity.  Therefore the unique
distinguished vertex in each column lies in that column's unique
intersection of size one.

The three size-one entries of `A` occupy distinct rows as well as distinct
columns, because every row and column has pattern `(1,2,2)`.  Relabel the
columns so that the size-one entry in row `i` is in column `i`.  Its
intersection consists of the unique distinguished vertex of that column,
and hence is exactly `{z_i}`.  This proves (2.1); the row and column sums
give (2.2).

Finally take `i ne j` in this normalization.  The cell `X_j` contains
exactly `z_j`, while `z_i notin X_j`.  Formula (2.3) therefore equals two.
Together with (1.4), this gives `w(C_ij)=8`.  \(\square\)

## 3. Literal expansion and the small-shore form

Suppose `H` is obtained from a graph `G` by contracting three disjoint
edges `x_i y_i` to the vertices `z_i`.  A weight-seven separator in
Theorem 2.1(1) expands to a literal order-seven separator of `G`.  The
component-lifting theorem then retains every named clique carrier in one
closed shore.  In a strongly contraction-critical `HC_7` candidate this
is a model-preserving exact-seven handoff; after fixing literal roots and
the named side map it enters the established anchored uncrossing rank.

The exceptional outcome has an additional useful description.  For
`i ne j`, the separator `C_ij` has weight eight.  Its KLNZ distinguished
open shore is rooted by

\[
                         L_i\cap X_j,                              \tag{3.1}
\]

which is a literal two-vertex clique and contains no contracted image.
The open shore may also contain nonterminal vertices; its intersection
with the named terminal union away from the boundary is exactly the
displayed `K_2`.  All remaining vertices of the named model `L_i` lie in
the separator, while the other two named cliques lie in the opposite
closed shore.  Thus the first irreducible equality case is not an
arbitrary order-eight adhesion: it has a distinguished shore rooted by a
literal two-vertex clique and preserves all three named models under
literal expansion.

This final description uses the side conclusion of KLNZ 3.2.16 explicitly
assumed in Section 1.  It does not claim that either open shore consists
only of named vertices, that the opposite open shore is connected, or that
the order-eight boundary can always be trimmed.

## 4. Where ordinary seven-connectivity remains essential in KLNZ

The theorem above decodes the last counting equality only.  A wholesale
replacement of ordinary connectivity by the weighted separator law is not
valid.  In the published proof ordinary `(k+2)`-connectivity is used at
the following earlier interfaces (specialized here to `k=5`).

1. KLNZ 3.2.8 excludes an empty `X_j` because `W` would be a cut of
   ordinary order at most six.  Weighted connectivity instead returns a
   bundle-bearing separator, possibly of weight seven, eight, or nine.
2. KLNZ 3.2.11(e) and 3.2.19 use fans in `H-W` of ordinary order
   `7-|W|`.  A weight-two vertex in `W` consumes two units of the lifted
   separator but only one ordinary deleted vertex, so the same fan count
   does not follow in `H`.
3. KLNZ 3.2.13--3.2.14 infer `Y_j=X_j` from the ordinary size of
   `W union X_j`.  The correct weighted threshold depends on how many
   distinguished vertices this set contains.
4. KLNZ 3.2.17, 3.2.20 and 3.2.21 use ordinary minimum degree seven.
   A contracted image `z_i` need not have ordinary degree seven even
   though its neighbourhood has separator weight at least seven.
5. KLNZ 3.2.26--3.2.27 finish with ordinary cuts of order six.  Theorem
   2.1 is the exact weighted replacement only in their disjoint terminal
   equality cell.

Accordingly, Theorem 2.1 supplies a real terminal decoder but not an
induction that reaches its hypotheses.  Any continuation must either
carry weighted fans through items 1--4, or arrive at the displayed cell
by the existing minimal-bad-contraction/state machinery.

## 5. Minimal three-edge contractions exclude the whole terminal cell

There is a sharper consequence when all three contractions form an
inclusion-minimal set whose quotient is not seven-connected.  In that
case every separator of `H` of order at most six contains all three
vertices `z_1,z_2,z_3`: if a separator omitted `z_i`, splitting only
`z_i` back into its edge would leave the same separator in the
seven-connected proper predecessor quotient.

### Corollary 5.1 (terminal equality cannot occur at a minimal triple)

Assume, in addition to Section 1, that every separator of `H` of order at
most six contains `z_1,z_2,z_3`.  Then no family `X_1,X_2,X_3` can satisfy
(1.1)--(1.3).

### Proof

In outcome 1 of Theorem 2.1, the order-six separator `C_ij` has weight
seven and therefore contains exactly one distinguished vertex.  In
outcome 2, every such `C_ij` contains exactly two distinguished vertices.
Both alternatives contradict the additional separator property.  \(\square\)

Thus the last disjoint terminal equality in the published three-clique
proof is already closed in the minimal three-contraction quotient.  The
live work is to reach that equality cell, or produce an earlier literal
`K_7`/exact-seven handoff, using the stronger separator property.  This
corollary does not perform that earlier induction.

## 6. Trust boundary

Proved here:

* the exact matrix classification;
* the existence of a weight-seven standard cut outside one canonical
  pattern; and
* the weight-eight and `K_2`-rooted-shore description of that pattern;
* exclusion of both terminal patterns in a minimal three-edge bad
  quotient.

Not proved here:

* that every weighted three-clique obstruction reaches the terminal cell;
* that the exceptional `K_2`-rooted shore forces `K_7`;
* that an order-eight separator automatically descends to order seven; or
* the global support-six transversal theorem.
