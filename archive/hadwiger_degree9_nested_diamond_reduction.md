# The nested degree-nine residue is a rooted-diamond problem

## 1. Setting

Use the terminal notation of
`hadwiger_degree9_terminal_root_swap.md`.  Thus

\[
 U=Z\cup J,
\]

where (Z,J) are connected and adjacent, (e_6\in Z) and
(e_0\in J) are the two left roots, (D) is the connected carrier
containing (6), and (s\in S) is the unique bottleneck through which
the root lobe (J) meets the target side (S).  The right bags are
(R_5,R_0), with (5\in R_5).  In particular

\[
 D\sim R_5,R_0,qquad S\sim R_5,R_0,qquad R_5\sim R_0,
\]

and the four prescribed roots give the usual contacts to the two
triangles (h12) and (h34).

The terminal capacity statement is

\[
 N_G(U)=\{h,1,2,s\}\mathbin{\dot\cup}P_D(U)
              \mathbin{\dot\cup}C_{34}(J),
 \qquad |P_D(U)|+|C_{34}(J)|\ge3.                 \tag{1.1}
\]

Here (P_D(U)=N_D(U)) and
(C_{34}(J)=N_{\{3,4\}}(J)).

## 2. Two literal exits close immediately

### Lemma 2.1 (double-literal closure)

If (J) has a neighbour at both (3) and (4), then (G) contains a
(K_7)-minor.

#### Proof

Use the seven branch sets

\[
 \{v\},\quad \{h\},\quad \{3\},\quad \{4\},\quad
 R_5,\quad D\cup R_0,\quad \{1\}\cup J\cup S.     \tag{2.1}
\]

They are disjoint and connected.  For the last set, use the edge from
the ordinary left root (e_0\in J) to (1), the connectivity of
(J), the (J)-(s) edge, and the connectivity of (S).  The sixth
set is connected through the old (D)-(R_0) carrier edge.

The first four sets form a clique.  The right-root contacts make (R_5)
and (R_0\subseteq D\cup R_0) adjacent to (h,3,4), while (v5) and
(v6) give their contacts to (v).  The last set sees (v,h) through
(1), sees (3,4) through the two assumed literal contacts, sees
(R_5) through an (S)-(R_5) portal, and sees (D\cup R_0) through
an (S)-(R_0) portal.  Finally (R_5\sim D\cup R_0) through (56)
(or the old right-bag contact).  This audits all twenty-one pairs.
\(\square\)

Consequently every minor-free terminal state satisfies

\[
 |C_{34}(J)|\le1,
 \qquad |P_D(U)|\ge2.                              \tag{2.2}
\]

If there is no literal exit, the second inequality improves to three.

## 3. A weaker target than the two-root bipartition

Let (H=G[U\cup D\cup\{s\}]).  A **rooted diamond model** in (H)
means four pairwise disjoint connected sets

\[
 A,B,C,Q                                                   \tag{3.1}
\]

such that

\[
 e_6\in A,qquad e_0\in B,qquad D\subseteq C,qquad s\in Q, \tag{3.2}
\]

and every pair among (A,B,C,Q) is adjacent except that no
(C)-(Q) adjacency is required.  Thus the required quotient is
(K_4^-), with the missing pair the two carrier sides.

### Theorem 3.1 (rooted-diamond lift)

If (H) has the rooted diamond model (3.1)--(3.2), then (G) contains
a (K_7)-minor.

#### Proof

Take

\[
 \{h\},\quad\{1\},\quad\{2\},\quad A,\quad B,\quad
 C\cup R_5,\quad Q\cup\{v,3\}\cup S\cup R_0.       \tag{3.3}
\]

These sets are disjoint.  The sixth is connected because (D\subseteq C)
contains (6), (R_5) contains (5), and (56\in E(G)).  The last is
connected because (s\in Q\cap S), (S\sim R_0), the right root in
(R_0) is adjacent to (3), and (3v\in E(G)).

The sets (A,B,C\cup R_5), and the last set form a clique.  Five of
their six contacts are exactly the five required edges of the rooted
diamond.  The omitted carrier-side contact is supplied by (6v).
The roots (e_6,e_0) make (A,B) adjacent to each of (h,1,2).
The set (C\cup R_5) sees (1,2) through (6) and (h) through the
right root in (R_5).  The last set sees all three through (v).
Since (h12) is a triangle, (3.3) is a (K_7)-model. \(\square\)

The connected bipartition requested in Section 6 of the terminal note
is a special case: take (A=E), (B=T), (C=D), and (Q=\{s\}).
Theorem 3.1 is strictly more permissive.  It allows the two carrier
branch sets to absorb vertices of (U), so the live obstruction is not
the failure of one particular spanning split but the absence of this
rooted (K_4^-)-minor.

## 4. Exact remaining structural target

By (2.2), a surviving nested shore has at least two distinct
(D)-portal vertices and at most one literal exit.  It must nevertheless
exclude a rooted diamond with roots

\[
                         e_6,e_0,D,s.                       \tag{4.1}
\]

This is the appropriate interface for a Two Paths/rooted-minor theorem.
A useful next dichotomy is therefore:

> either (G[U\cup D\cup\{s\}]) contains the rooted diamond of
> Theorem 3.1, or the rooted-diamond obstruction exposes a separation
> which, after restoring the fixed vertices (h,1,2) and the at most
> one literal exit, has order at most six.

Unlike the earlier two-root split, the positive outcome here is closed
under absorption into either carrier bag.  Thus a web or separator
theorem need not preserve a prescribed partition of every vertex of
(U); it need only preserve the four labelled root sets in (4.1).
