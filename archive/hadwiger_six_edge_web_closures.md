# Six missing boundary edges: exact atlas and three unbounded web closures

## 1. Exact quotient atlas

Let \(S=\{0,\ldots,6\}\), let \(F=\overline{G[S]}\) have six edges,
and add two nonadjacent helpers, each complete to \(S\).  The
dependency-free script contact_order7_six_edge_atlas.py checks all

\[
 \binom{21}{6}=54264
\]

labelled graphs \(F\).  It enumerates all possible seven-bag partitions
of the nine quotient vertices (support orders seven, eight, or nine),
replays every positive branch-set model, and reruns every negative
isomorphism representative through the slower arbitrary-connected-set
minor search.  Exactly 11697 labelled instances fail, in twelve
isomorphism types.  Representatives are:

\[
\begin{array}{c|l}
0&01,06,15,23,24,34\\
1&05,06,12,16,25,34\\
2&01,05,15,23,24,34\\
3&04,05,13,15,23,24\\
4&02,06,15,23,24,34\\
5&03,06,13,15,23,24\\
6&03,04,05,12,14,23\\
7&01,03,05,12,14,23\\
8&01,03,04,12,14,23\\
9&01,02,05,12,14,23\\
10&01,02,04,12,13,23\\
11&01,02,03,12,13,23.
\end{array}                                                   \tag{1}
\]

Every edge in (1) is a nonedge of \(G[S]\).  Types 0, 1, and 4 admit
unbounded hand closures.

## 2. A reusable web-template lemma

### Lemma 2.1

Let \(G\) be seven-connected, let \(|S|=7\), and suppose \(G-S\) has
exactly two connected components \(D_1,D_2\), each with neighbourhood
\(S\).  Let \(Q\subseteq S\), with \(4\le |Q|\le7\), and cyclically
order \(Q\) so that every edge of \(G[Q]\) joins consecutive vertices
of the displayed cycle.  Some frame edges may be absent from \(G[Q]\);
there are no nonconsecutive chords.
Put \(O=S-Q\), and suppose \(G[O]\) is bipartite.

For \(j=1,2\), form the \(Q\)-terminal society from \(G[D_j]\), using
the cyclic order on \(Q\).  Suppose, moreover, that every crossing in
either society, after its two disjoint shore paths are enlarged to
adjacent connected sets \(X,Y\), has an explicit \(K_7\)-model using
\(X,Y\), the boundary \(S\), and the opposite shore.

Then \(G\) contains a \(K_7\)-minor or is six-colourable.

#### Proof

If a society is crossed, use its assumed model.  Otherwise both are
crossless.  The generalized Two Paths Theorem completes each, by adding
edges only and no vertices, to a web with frame \(Q\).

If a nonempty inserted facial clique has vertex set \(Z\subseteq D_j\),
then in the original graph its neighbours lie among the three vertices
of its facial triangle and the omitted boundary \(O\).  Thus

\[
 |N_G(Z)|\le3+|O|\le6.
\]

This separates \(Z\) from the opposite shore, contrary to
seven-connectivity.  Hence both webs are bare planar ribs.  Add any
missing frame edges, and glue their disk embeddings along that frame
cycle.  The result is a planar supergraph of \(G-O\), so \(G-O\) is
planar.
Four-colour \(G-O\), and two-colour \(G[O]\) with two fresh colours.
All cross edges are automatically proper, giving a six-colouring.
\(\square\)

## 3. Crossing certificates

In the following table, \(H\) denotes the opposite full shore.  The two
crossing paths in the active shore are enlarged to disjoint adjacent
connected sets \(X,Y\); a notation such as \(X2\) means
\(X\cup\{2\}\).  Each row lists seven branch bags.

### Type 0

Here

\[
 F=P_4\dot\cup K_3
 =\{01,06,15\}\dot\cup\{23,24,34\}.
\]

Take

\[
 Q=(0,2,6,3),\qquad O=\{1,4,5\}.
\]

Then \(G[Q]\) is a chordless four-cycle and \(G[O]\) is the path
\(1-4-5\).  The sole crossing joins \(0\) to \(6\) and \(2\) to \(3\).
Its model is

\[
 \{0\},\{2\},\{5\},H,\{1,4\},X6,Y3.                 \tag{2}
\]

### Type 1

Here

\[
 F=C_5\dot\cup K_2
 =\{05,06,12,16,25\}\dot\cup\{34\}.
\]

Take

\[
 Q=(0,1,5,6,2),\qquad O=\{3,4\}.
\]

The omitted pair is independent in \(G\).  The five possible crossings
and their models are:

\[
\begin{array}{c|c|l}
\text{\(X\)-pair}&\text{\(Y\)-pair}&\text{seven bags}\\ \hline
05&16&\{1\},\{3\},\{5\},H,\{2,4\},X0,Y6\\
05&12&\{0\},\{1\},\{3\},H,\{4,6\},X5,Y2\\
06&12&\{0\},\{2\},\{3\},H,\{4,5\},X6,Y1\\
06&52&\{2\},\{3\},\{6\},H,\{1,4\},X0,Y5\\
16&52&\{3\},\{5\},\{6\},H,\{0,4\},X1,Y2.
\end{array}                                                   \tag{3}
\]

### Type 4

Here

\[
 F=\{02,06,15,23,24,34\}.
\]

Take

\[
 Q=(0,3,6,4),\qquad O=\{1,2,5\}.
\]

The omitted graph is the path \(1-2-5\).  The sole crossing joins
\(0\) to \(6\) and \(3\) to \(4\), with model

\[
 \{0\},\{1\},\{3\},H,\{2,5\},X6,Y4.                 \tag{4}
\]

### Verification of the displayed models

Every ordinary two-vertex bag in (2)--(4) is an edge because its pair is
absent from the corresponding list \(F\).  Each \(X\)- or \(Y\)-bag is
connected through the appropriate crossing endpoint.  The \(X\)- and
\(Y\)-bags are adjacent by the split connector.  The opposite shore
\(H\) sees every boundary-containing bag.  Comparing the remaining bag
pairs with the six listed nonedges checks all 21 adjacencies in each
row.  The script six_edge_web_template_search.py independently
reconstructs and exactly replays these models.

Lemma 2.1 now proves:

### Theorem 3.1

None of types 0, 1, or 4 in (1) occurs as an order-seven
counterexample-derived contact separator.

## 4. Type 5

Type 5 has

\[
 F=\{03,06,13,15,23,24\}.
\]

Take

\[
 Q=(0,1,3,5),\qquad O=\{2,4,6\}.
\]

Every actual edge of \(G[Q]\) is a frame edge (the frame edge \(13\) is
simply absent), and \(G[O]\) is the path \(2-6-4\).  The sole crossing
joins \(0\) to \(3\) and \(1\) to \(5\).  Its explicit model is

\[
 \{0\},\{4\},\{5\},H,\{2,6\},X3,Y1.                 \tag{5}
\]

The pair \(26\) is an edge, the crossing contacts connect the last two
anchored bags, \(X,Y\) are adjacent after splitting a connector, and
comparison with \(F\) checks all remaining adjacencies.  Lemma 2.1
handles the crossless case.

### Theorem 4.1

Type 5 in (1) cannot occur as a counterexample-derived contact
separator.

## 5. Allowing missing frame edges: types 6, 7, 8, and 9

The strengthened form of Lemma 2.1, which permits absent consecutive
frame edges, gives four more closures.  The following choices all have
bipartite omitted graph and no nonconsecutive edge in \(G[Q]\):

\[
\begin{array}{c|c|c}
\text{type}&Q&O\\ \hline
6&(1,2,4,3)&\{0,5,6\}\\
7&(1,2,4,3)&\{0,5,6\}\\
8&(0,1,3,4,2)&\{5,6\}\\
9&(1,2,4,3)&\{0,5,6\}.
\end{array}                                                   \tag{9}
\]

For types 6, 7, and 9 there is one crossing.  Its explicit models are

\[
\begin{array}{c|c|l}
\text{type}&(X\text{-pair}\mid Y\text{-pair})&
 \text{seven bags}\\ \hline
6&14\mid23&\{1\},\{3\},\{5\},\{6\},H,X4,Y\cup\{0,2\}\\
7&14\mid23&\{3\},\{4\},\{5\},\{6\},H,X1,Y2\\
9&14\mid23&\{3\},\{4\},\{5\},\{6\},H,X1,Y2.
\end{array}                                                   \tag{10}
\]

In the first row, \(02\in E(G[S])\), so the last bag is connected
through the \(Y\)-contact at \(2\).

Type 8 has five crossings:

\[
\begin{array}{c|c|l}
X\text{-pair}&Y\text{-pair}&\text{seven bags}\\ \hline
03&14&\{3\},\{4\},\{5\},\{6\},H,Y1,X\cup\{0,2\}\\
03&12&\{2\},\{5\},\{6\},H,\{3,4\},X0,Y1\\
04&12&\{2\},\{4\},\{5\},\{6\},H,X0,Y\cup\{1,3\}\\
04&32&\{2\},\{4\},\{5\},\{6\},H,X0,Y3\\
14&32&\{3\},\{4\},\{5\},\{6\},H,X1,Y2.
\end{array}                                                   \tag{11}
\]

As before, the displayed path contacts make the anchored bags connected;
the split connector makes \(X,Y\) adjacent; \(H\) is full; and direct
comparison with the corresponding row of (1) verifies every remaining
bag adjacency.  Thus every crossing in (9) gives a \(K_7\)-minor, while
Lemma 2.1 six-colours the crossless alternative.

### Theorem 5.1

Types 6, 7, 8, and 9 in (1) cannot occur as counterexample-derived
contact separators.

## 6. Exact residual after the first six-edge web round

The web search by itself leaves types (2,3,10,11).  The last two,
however, are split graphs in the missing-edge representation
(F=\overline{G[S]}): for type 10 take clique
(\{0,1,2\}) and independent set (\{3,4,5,6\}), and for type 11
take clique (\{0,1,2,3\}) and independent set (\{4,5,6\}).
Corollary 4.1 of `hadwiger_exact_block_hypergraph.md` proves that the
missing-edge graph at a full-shore adhesion is nonsplit.  Hence types
10 and 11 cannot occur (and the same observation independently excludes
the already web-closed type 9).

Before applying two-piece shore surgery, the genuine nonsplit quotient
types are exactly

\[
 2,3.                                               \tag{12}
\]

They are (2K_3\dot\cup K_1) and (C_6\dot\cup K_1), respectively.
The exhaustive search permits missing consecutive frame edges.  These
two nonsplit types have no chordless-frame template with bipartite
omitted graph and all crossing models of the elementary two-path form.
The unbounded theorem in `hadwiger_k331_two_piece_closure.md` eliminates
type 2 by forcing four-connectivity inside each shore and then opposite
rooted triangles.  Consequently the sole remaining six-edge type is

\[
 3=C_6\dot\cup K_1.                                \tag{13}
\]

Closing (13) requires simultaneous portal constraints from several
frames, controlled boundary chords in the web disks, or a different
colour-gluing decomposition.
