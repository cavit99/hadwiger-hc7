# The exact portal lock in the sole six-edge contact core

## 1. Boundary and frame

Let (S=\{0,\ldots,6\}), and suppose

\[
 \overline{G[S]}=C_6\mathbin{\dot\cup}K_1,
 \qquad
 C_6=0,4,2,3,1,5,0.                         \tag{1.1}
\]

Let (D,D') be the two connected full shores.  The relaxed frame

\[
 R=(0,1,5,3),\qquad Z=\{2,4,6\}                   \tag{1.2}
\]

has one alternating crossing, joining (0) to (5) and (1) to (3).
The graph (G[Z]) is the path (2-6-4).  Thus, by relaxed-frame web
gluing, either this crossing occurs in one shore or (G) is
six-colourable.

Suppose the crossing occurs in (D).  Enlarge its two disjoint path
interiors along a shortest connector and split the connector at an edge.
This gives adjacent disjoint connected sets (X,Y\subseteq D), where

\[
 X\text{ touches }0,5,qquad Y\text{ touches }1,3. \tag{1.3}
\]

Contract (D') to a full helper (H).

## 2. Two explicit one-contact repairs

### Lemma 2.1

If (X) also touches (4), or (Y) also touches (2), then (G)
contains a (K_7)-minor.

#### Proof

If (X) touches (4), use

\[
 \{0\},\ \{1\},\ \{6\},\ H,\ \{2,5\},\
 X\cup\{4\},\ Y\cup\{3\}.                         \tag{2.1}
\]

If (Y) touches (2), use

\[
 \{0\},\ \{1\},\ \{2\},\ \{6\},\ H,\
 Y\cup\{3\},\ X\cup\{4,5\}.                    \tag{2.2}
\]

The bags in (2.1) and (2.2) are connected: (X,Y) contain their stated
crossing contacts, (25,45\in E(G[S])), and the additional contact is
the hypothesis.  The (X)- and (Y)-bags are adjacent through the split
connector.  The full helper sees every boundary-containing bag.  Comparing
the remaining pairs with the six nonedges in (1.1) verifies all 21 bag
adjacencies. \(\square\)

The contacts in Lemma 2.1 are the two **outward portals** of this frame:
the (05)-piece reaches across the adjacent missing edge (04), or the
(13)-piece reaches across the adjacent missing edge (23).

## 3. Exact irreparable ownership

There are ten optional contacts beyond (1.3): (X) may additionally
touch (1,2,3,4,6), and (Y) may additionally touch (0,2,4,5,6).
The exact quotient atlas has 227 negative patterns among the (2^{10}=1024)
possibilities.  Their seven inclusion-maximal contact pairs are

\[
\begin{array}{c|c}
N_S(X)&N_S(Y)\\ \hline
01356&0135\\
012356&0136\\
02356&01346\\
0135&01356\\
012356&13456\\
01256&013456\\
0356&013456.
\end{array}                                                   \tag{3.1}
\]

Here, for example, (01356) denotes the set
(\{0,1,3,5,6\}).  Every negative pattern is coordinatewise contained
in one row of (3.1).  In particular, every row has

\[
 4\notin N_S(X),\qquad 2\notin N_S(Y),              \tag{3.2}
\]

and these two omissions are forced in every (K_7)-minor-free crossing.
The dependency-free verifier `c6_bad_crossing_contact_atlas.py` enumerates
all support partitions of the ten-vertex quotient, replays every positive
model, reports `227` and `7`, and independently returns the branch sets in
(2.1)--(2.2).

## 4. The geometric lock before contraction

For (s\in S), put (P_s=N_D(s)).  The quotient condition (3.2) has the
following stronger uncontracted form.

### Lemma 4.1 (mutual separator lock)

In a (K_7)-minor-free realization of the crossing (1.3),

1. (Y) separates (X) from every vertex of (P_4) in (D); and
2. (X) separates (Y) from every vertex of (P_2) in (D).

#### Proof

If there were an (X)-to-(P_4) path in (D-Y), adjoin a shortest such
path to (X).  The enlarged set remains connected and disjoint from (Y),
retains its adjacency to (Y), and now touches (4).  Lemma 2.1 gives a
(K_7)-minor.  The second assertion is symmetric. \(\square\)

Thus it is not enough that the shore has the two outward portal classes.
Their placement is forced to be reversed across the two crossing pieces.
Wrong-side contacts, even both of them simultaneously, need not repair the
quotient; (3.1) is the exact list of how much wrong-side contact can survive.

## 5. Six cyclic copies

Write the missing cycle as

\[
 C=(c_0,c_1,c_2,c_3,c_4,c_5)=(0,4,2,3,1,5)
\]

and indices modulo six.  For each (i), omit
(c_i,c_{i+1}) (and (6)); the remaining four vertices are a relaxed
frame.  Its crossing pieces join the missing pairs

\[
 c_{i-2}c_{i-1}\quad\text{and}\quad
 c_{i+2}c_{i+3}.                                    \tag{5.1}
\]

The cyclic form of Lemmas 2.1 and 4.1 says that the first piece must be
separated from every (c_i)-portal by the second piece, and the second
piece must be separated from every (c_{i+1})-portal by the first.  If
either ownership is reversed, the corresponding explicit rotation of
(2.1) or (2.2) is a (K_7)-model.

Consequently a hypothetical survivor must assign a crossed shore to each
of the six frames and realize all assigned crossings with these mutually
reversed portal separations.  This is the exact structural residual after
the quotient and relaxed-web information; it is strictly stronger than
merely saying that a crossing quotient fails.
