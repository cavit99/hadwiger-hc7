# A small carrier forces capacity or an exact adhesion

## 0. Uniform carrier-size theorem

The counting mechanism is not special to three pairs or to the Moser
boundary.

Let (G) be (k)-connected, let (S) be a (k)-cut, and let (D)
be a component of (G-S), with another component on the other side.
Let

\[
                  A_1,\ldots,A_p\subseteq S
\]

be pairwise disjoint nonempty label blocks.  An (A_i)-carrier is a
connected set in (D) meeting the portal set of every label in (A_i).

### Theorem 0.1 (uniform small-carrier exchange)

Let (X\subseteq D) be an (A_1)-carrier, and suppose that (D-X)
is nonempty.  If

\[
                            |X|\le p-1,             \tag{0.1}
\]

then either

1. (X), together with a disjoint carrier in (D-X), gives a packet
   for (A_1) and some (A_j), (j>1); or
2. (G) has an exact (k)-cut.

If (|X|<p-1), the first outcome is forced.

### Proof

Assume that outcome 1 fails, and fix a component (Y) of (D-X).
For each (j>1), the connected graph (Y) cannot meet every portal
row belonging to (A_j), since it would then contain an
(A_j)-carrier disjoint from (X).  Choose

\[
 s_j\in A_j\quad\text{with}\quad N_Y(s_j)=\varnothing .
\]

The chosen labels are distinct because the blocks are disjoint.  Put
(R=\{s_2,\ldots,s_p\}).  Distinct components of (D-X) are
anticomplete, so

\[
 N_G(Y)\subseteq X\cup(S-R),
 \qquad
 |N_G(Y)|\le |X|+k-(p-1)\le k.                    \tag{0.2}
\]

This set separates (Y) from the other component of (G-S).
(k)-connectivity gives the reverse inequality.  Hence equality holds
in (0.2), producing an exact (k)-cut.  If (|X|<p-1), the upper bound
in (0.2) is strictly below (k), a contradiction.  \(\square\)

This is a genuine all-(t) contact-or-separator statement.  Its threshold
depends on the number of competing non-singleton boundary blocks, not on
the labels or the target clique order.

## 1. Statement

Let (G) be seven-connected, let (S) be a seven-cut, and let (D)
be a component of (G-S).  Assume that (G-S) has another component,
so that (N_G(D)=S).  Partition

\[
 S=A\mathbin{\dot\cup}B\mathbin{\dot\cup}C
   \mathbin{\dot\cup}\{r\},
 \qquad |A|=|B|=|C|=2 .
\tag{1.1}
\]

For a pair block (Q=\{q_1,q_2\}), a **(Q)-carrier** is a
nonempty connected set (X\subseteq D) having a neighbour at both
(q_1,q_2).  Two pair blocks have a packet if they have disjoint
carriers.  Adjacency between the two carriers is not required.

### Theorem 1.1 (small carrier exchange)

Suppose (D-X) is nonempty and (X) is an
(A)-carrier.  If (|X|\le2), then one of the following holds.

1. (D) has an (A,B)-packet or an (A,C)-packet.
2. (G) has an exact seven-cut, namely the external neighbourhood of
   (D-X).

Moreover, if (|X|=1), outcome 1 is forced.  Consequently, if
(|D|\ge3) and neither packet nor a nested exact seven-cut occurs,
every carrier for each of (A,B,C) has at least three vertices.

This is Theorem 0.1 with (k=7) and (p=3); the direct proof below is
retained to make the sharp seven-boundary specialization transparent.

## 2. Proof

Assume that neither packet in outcome 1 exists, and fix a component
(Y) of (D-X).  Since (Y) is connected, it would itself contain a
(B)-carrier if it had a neighbour at both vertices of (B).
Therefore some (b\in B) has no neighbour in (Y):

\[
                         N_Y(b)=\varnothing .      \tag{2.1}
\]

The identical argument for (C) gives a vertex (c\in C) with

\[
                         N_Y(c)=\varnothing .      \tag{2.2}
\]

No vertex outside (D\cup S) has a neighbour in (Y), because (D)
is a component of (G-S), and no other component of (D-X) has an
edge to (Y).  Equations (2.1) and (2.2) therefore give

\[
 N_G(Y)\subseteq X\cup(S-\{b,c\}),
 \qquad |N_G(Y)|\le |X|+5\le7.                    \tag{2.3}
\]

The set in (2.3) separates the nonempty set (Y) from the other
component of (G-S).  Seven-connectivity implies

\[
                         |N_G(Y)|\ge7.             \tag{2.4}
\]

If (|X|=1), (2.3) and (2.4) contradict one another.  Hence a
singleton carrier forces a packet.  If (|X|=2), equality holds
throughout (2.3)--(2.4), and (N_G(Y)) is an exact seven-cut.  This
proves the theorem.

If (|D|\ge3), the complement of every carrier of order at most two is
nonempty.  Applying the proved assertion gives the final consequence.
\(\square\)

## 3. Why this is the first nonstatic common-web exchange

In the common-hexagram outcome of
`hadwiger_three_pair_common_web.md`, all three pair-packets fail.  The
theorem shows that a short portal connection is not another web case:
it either boosts the shore capacity immediately or exports an actual
minimum adhesion.  Thus an atomic common-hexagram shore has the metric
restriction

\[
 \operatorname{dist}_D(P_{q_1},P_{q_2})\ge2
 \quad\text{for }Q\in\{A,B,C\},                   \tag{3.1}
\]

where distance zero or one would give a carrier on one or two vertices.
This conclusion is label-free and uses the full seven-connectivity in
exactly one place.

The order-two threshold is sharp for this counting mechanism.  A
carrier (X) of order three which monopolizes one root of each of the
other two pair blocks only gives

\[
 |X|+|S-\{b,c\}|=8,
\]

so seven-connectivity alone no longer forces a tight cut.  The next
required input at that threshold is precisely a minor-transition state
or a contraction which lowers the carrier order.

## 4. A palette warning

The common hexagram cannot be closed merely by claiming that its
three-colour boundary pattern extends through every planar disk with a
five-colour palette (the sixth colour being reserved for (r)).  Here
is a minimal explicit obstruction.

Take the outer cycle

\[
 u_1u_2u_3u_4u_5u_6u_1
\]

precoloured (1,2,3,1,2,3).  Put a triangle (x_1x_2x_3) inside it,
and add

\[
\begin{aligned}
 N_{\{u_i\}}(x_1)&=\{u_1,u_2,u_3\},\\
 N_{\{u_i\}}(x_2)&=\{u_3,u_4,u_5\},\\
 N_{\{u_i\}}(x_3)&=\{u_5,u_6,u_1\}.
\end{aligned}                                      \tag{4.1}
\]

This has a plane annular drawing.  Every (x_i) sees boundary colours
1,2,3, so a five-colour extension would have to two-colour the inner
triangle with colours 4,5, which is impossible.  Thus any proof of the
full common-web exchange must use seven-connectivity/portal capacity or
the one-step minor transition; planarity and the fixed equality state
alone are insufficient.  Theorem 1.1 is exactly what excludes the
short-carrier version of this obstruction in a counterexample-derived
shore.
