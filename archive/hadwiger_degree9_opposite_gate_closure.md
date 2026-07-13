# The degree-nine Moser lock: opposite complementary gates cannot coexist

## 1. Setting

Retain a balanced spanning rooted model

\[
                         L_6,L_0,R_5,R_0
\]

in the degree-nine pure-Moser lock.  Let \(K\) be the component of
\(L_6-6\) containing the left root, and put \(D=L_6-K\).  Let \(J\)
be the component of \(R_5-5\) containing the right root, and put
\(C=R_5-J\).  Thus

\[
  L_6=K\mathbin{\dot\cup}D,\qquad
  R_5=J\mathbin{\dot\cup}C,                               \tag{1.1}
\]

where all four sets are connected, \(KD,JC\in E(G)\), \(6\in D\),
\(5\in C\), and \(DC\in E(G)\) through the literal edge \(65\).

Assume that both gates are in their complementary attachment cells:

\[
                         K\not\sim L_0,\qquad J\not\sim R_0. \tag{1.2}
\]

The old clique-model adjacencies then force

\[
                         D\sim L_0,\qquad C\sim R_0.        \tag{1.3}
\]

The other two carrier adjacencies have two possible locations each:

\[
  K\sim R_0\text{ or }D\sim R_0,\qquad
  J\sim L_0\text{ or }C\sim L_0.                          \tag{1.4}
\]

No uniqueness is asserted in (1.4); if both alternatives hold, choose
either one.

## 2. A contact between the two root components closes the model

### Theorem 2.1 (opposite-root contact closure)

Under (1.1)--(1.4), if \(K\sim J\), then \(G\) contains a
\(K_7\)-minor.

#### Proof

Choose one alternative in each clause of (1.4).  There are four cases.

If \(D\sim R_0\) and \(C\sim L_0\), use

\[
 \{v\},\ \{h\},\ \{1\},\ \{2\},\
 C\cup L_0,\ D\cup R_0,\ \{3\}\cup K\cup J.             \tag{2.1}
\]

If \(D\sim R_0\) and \(J\sim L_0\), use

\[
 \{h\},\ \{1\},\ \{2\},\ L_0,\ K\cup J,\
 \{3\}\cup D\cup C,\ \{v,4\}\cup R_0.                 \tag{2.2}
\]

If \(K\sim R_0\) and \(C\sim L_0\), use

\[
 \{h\},\ \{1\},\ \{2\},\ K,\ L_0\cup R_0,\
 \{v,3\}\cup J,\ \{4\}\cup D\cup C.                   \tag{2.3}
\]

Finally, if \(K\sim R_0\) and \(J\sim L_0\), use

\[
 \{h\},\ \{1\},\ \{2\},\ K,\ J\cup L_0,\
 \{3\}\cup D\cup C,\ \{v,4\}\cup R_0.                 \tag{2.4}
\]

All displayed sets are disjoint.  Connectivity follows from the
chosen edges in (1.4), the old edge \(L_0R_0\), the assumed edge
\(KJ\), the internal edges \(KD,JC\), the edge \(65\), and the
literal paths through \(3\) or \(4\), as displayed.

For completeness, the nonsingleton bags in (2.1) meet pairwise through
\(DC\) (or \(L_0R_0\)), \(CJ\), and \(DK\).  In (2.2) the four
large bags meet through

\[
 L_0J,\ L_0D,\ L_0R_0,\ KD,\ J4,\ v6,
\]

(with \(JC\) and \(CR_0\) also available for two of those pairs).
In (2.3) they meet through

\[
 KR_0,\ KJ,\ KD,\ R_03,\ L_0C,\ JC,
\]

where \(R_03\) denotes the edge from the root of \(R_0\) to the
displayed vertex \(3\).  In (2.4) the six contacts are

\[
 KJ,\ KD,\ KR_0,\ L_0D,\ L_0R_0,\ v6.
\]

Every nonsingleton bag sees the three singleton bags \(h,1,2\): a
left root supplies all three contacts, a set containing \(6\) uses
\(16,26\) and either \(3h\) or \(4h\), a set containing \(v\) uses
\(v1,v2\), and every displayed right-root piece sees \(h\).  In
(2.1), where \(v\) is also a singleton, the three large bags see it
through \(5,6,3\), respectively.  The literal Moser edges give all
contacts among the singleton bags.  Thus each display is a
\(K_7\)-model. \(\square\)

## 3. Complete elimination of the double-complementary cell

### Theorem 3.1 (opposite-gate closure)

In a globally potential-minimal balanced model, the two complementary
alternatives in (1.2) cannot both hold.  This includes the exact
seven-adhesion equality as well as the strict-surplus residue.

#### Proof

Assume both hold and that \(G\) has no \(K_7\)-minor.  The
ordinary-bag portal theorem in
`hadwiger_degree9_complementary_lobe_ownership.md`, applied on the
left, together with the universal three-portal bound in
`hadwiger_degree9_cross_half_gate.md`, gives

\[
             |N_{R_0}(K)|\le1,\qquad |N_{R_5}(K)|\ge2.      \tag{3.1}
\]

Its left--right image, applied to the right gate, gives

\[
             |N_{L_0}(J)|\le1,\qquad |N_{L_6}(J)|\ge2.      \tag{3.2}
\]

Theorem 2.1 forbids \(K\sim J\).  Hence every contact counted on the
right of (3.1) has its \(R_5\)-endpoint in \(C\), and every contact
counted on the right of (3.2) has its \(L_6\)-endpoint in \(D\).
In particular,

\[
                              K\sim C,\qquad J\sim D.        \tag{3.3}
\]

These are opposite cross-edges between the four disjoint sets
\(K,D,J,C\).  Use the seven branch sets

\[
 \{v\},\quad\{h\},\quad\{1\},\quad\{2\},\quad
 D\cup J,\quad K\cup C,\quad \{3\}\cup L_0\cup R_0.        \tag{3.4}
\]

The fifth and sixth are connected through the two cross-edges in
(3.3), and the last through the old \(L_0R_0\) edge and the
right-root--\(3\) edge.  The three large bags meet pairwise through
\(KD\) (also \(JC\)), the forced edge \(D L_0\), and the forced edge
\(C R_0\).  They see \(v\) through \(6,5,3\), respectively.  Their
contacts to \(h,1,2\) come from the right root in \(J\) together with
\(6\in D\), the left root in \(K\) together with \(5\in C\), and
the left root in \(L_0\) together with \(3v\).  Thus (3.4) is a
\(K_7\)-model, a contradiction. \(\square\)

The proof is independent of the orders and block structures of all four
model bags.  It converts two portal-count lower bounds into a
label-preserving crossed pair, rather than adding another finite contact
table.  Outside the exact equality the lower bounds in (3.1)--(3.2)
improve from two to three, but that extra surplus is not needed.

## 4. Exact remaining consequence

If the left gate is complementary, \(K\not\sim L_0\), then the right
gate must be in the other attachment cell:

\[
                         J\sim R_0,\qquad J\not\sim L_6,L_0. \tag{4.1}
\]

Thus the remaining complementary residue couples at least two
\(K\)-portals in the \(5\)-side \(C\) (at least three outside the
exact equality) to a symmetric same-bag ordered portal spine in
\(R_0\).  The double-complementary family itself is closed completely.
