# Three interface edges force a packet or one exact portal pattern

## 1. Setting

Let \(G\) be seven-connected and let \(S\) be a seven-cut with full
shores \(D,D^*\). Choose \(D\) as a minimum fragment and suppose a
covering bad split has

\[
 D=X\mathbin{\dot\cup}Y,
\]

with \(X,Y\) connected and with exactly three interface edges. Put

\[
 P_X=N_S(X),\quad P_Y=N_S(Y),\quad
 T_X=N_Y(X),\quad T_Y=N_X(Y).
\]

Minimum-fragment atomicity gives

\[
 |P_X|+|T_X|\ge8,\qquad |P_Y|+|T_Y|\ge8.          \tag{1.1}
\]

Fix a four-block matching state

\[
 S=A\mathbin{\dot\cup}B\mathbin{\dot\cup}C
   \mathbin{\dot\cup}\{r\},\qquad |A|=|B|=|C|=2. \tag{1.2}
\]

A pair block \(Q\in\{A,B,C\}\) is **full in a piece** when
\(Q\subseteq P_X\), or respectively \(Q\subseteq P_Y\). Since a piece
is connected, a full pair block has a carrier in that piece.

## 2. Packet-or-split-row theorem

### Theorem 2.1

At least one of the following holds.

1. Two distinct pair blocks have disjoint carriers, one in \(X\) and
   one in \(Y\).
2. After permuting \(A,B,C\), there are labellings
   \(B=\{b_1,b_2\}\), \(C=\{c_1,c_2\}\) such that

   \[
   \begin{aligned}
    P_X&=A\cup\{b_1,c_1,r\},\\
    P_Y&=A\cup\{b_2,c_2,r\},                     \tag{2.1}
   \end{aligned}
   \]

   and the three interface edges form a matching: they have three
   distinct ends in \(X\) and three distinct ends in \(Y\).

Thus the packet-free three-edge branch has one label-free form: both
pieces redundantly carry the same pair block, while each of the other
two pair blocks is split one root to each side.

#### Proof

There are at most three interface endpoints in either piece, so
\(|T_X|,|T_Y|\le3\). Equation (1.1) gives

\[
 |P_X|,|P_Y|\ge5.                                \tag{2.2}
\]

Any five-element subset of the seven-element set in (1.2) contains
both vertices of at least one of \(A,B,C\). Hence each piece has a
full pair block.

If \(Q\) is full in \(X\) and a different block \(R\) is full in \(Y\),
the connected sets \(X,Y\) are disjoint \(Q\)- and \(R\)-carriers,
giving outcome 1. Assume this never happens. The collections of full
pair blocks in the two pieces are nonempty and their union therefore
consists of one block, say \(A\).

For \(A\) to be the only full block in \(X\), the row \(P_X\) must miss
at least one vertex of each of \(B,C\). By (2.2) it misses exactly two
vertices, one in each block, and contains \(r\). The same holds for
\(Y\). Since the split is covering,

\[
 P_X\cup P_Y=S,
\]

the missed vertices are complementary within both \(B\) and \(C\).
Relabel their vertices to obtain (2.1).

Finally \(|P_X|=|P_Y|=5\). Equation (1.1) forces
\(|T_X|=|T_Y|=3\). Three interface edges can have three distinct ends
on each side only when they form a matching. \(\square\)

## 3. Why this is the geometric replacement for relation counting

The abstract hypercube relation in
hadwiger_multi_interface_hypercube_obstruction.md shows that deletion
and simultaneous-contraction states alone do not force state diversity.
Theorem 2.1 uses the information absent from that counterexample:
minimum-fragment surplus and actual portal rows.

In outcome 1 the state has genuine two-block capacity. In outcome 2,
the residual has three additional simultaneous structures:

1. two vertex-disjoint carriers of the same block \(A\), one in each
   piece;
2. a three-edge interface matching; and
3. complementary one-root defects on \(B\) and \(C\).

If the state extends the opposite shore but not \(D\), packet transfer
makes that opposite shore packet-deficient for all three pairs of
blocks. Its three failed packets therefore synchronize into the common
hexagram web (or expose an exact seven-cut). The exact remaining
three-edge theorem is consequently not a general Hamming-family lemma:
it is an exchange between the duplicated \(A\)-carrier in (2.1) and
the opposite common hexagram.

This identifies a concrete structural target:

> **Duplicated-carrier/hexagram exchange.** A packet-free common
> hexagram on one shore cannot coexist, in a six-minor-critical
> \(K_7\)-minor-free graph, with the complementary split rows (2.1)
> and a three-edge matching on the opposite shore.

An exchange proof may use one \(A\)-carrier to split the two \(A\)-roots
and reserve the other to reroute one of the two crossing pair demands
in the hexagram. Failure of that rerouting must expose a separator in
the hexagram shore; minimum-fragment atomicity then supplies the exact
cut exit.
