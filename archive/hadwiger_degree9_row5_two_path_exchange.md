# The sharp degree-nine row-five residue: one-path absorption and the true web cell

## 1. Setting

Use the exact type-2 state of
`hadwiger_degree9_type2_cutvertex_closure.md`.  Fix the split shore

\[
                         C_i=P\mathbin{\dot\cup}Q,
\]

write (F=F_i=N_N(C_i)), and assume

\[
                         R=N_N(P),\qquad |R|=5.                 \tag{1.1}
\]

Thus

\[
                         D=F-R=\{d_1,d_2\}.                    \tag{1.2}
\]

Lemma 6.1 of the cited note supplies disjoint paths (L_1,L_2) in
(G[Q\cup D]), where (L_h) starts at (d_h), ends at a distinct
vertex (i_h\in I=N_Q(P)), and has all internal vertices in (Q).

The purpose of this note is to identify what those two paths genuinely
buy.  They do not by themselves force the required (N)-meeting
(K_6), but absorbing either path raises the complementary obstruction
from interface order two to interface order three, unless an exact
seven-cut occurs.

## 2. The one-path absorption theorem

Put

\[
                         W_h=V(L_h)-\{d_h\}\subseteq Q.         \tag{2.1}
\]

### Theorem 2.1 (minor, exact cut, or three-interface web)

Fix (h\in\{1,2\}), and let (k\ne h).  Define

\[
                         A_h=P\cup W_h,                         \tag{2.2}
\]

and let (K_k) be the component of (Q-W_h) containing (W_k).
Then (A_h,K_k) are disjoint connected sets, (A_h) contacts
(R\cup\{d_h\}), and (K_k) contacts (d_k).  Moreover at least one
of the following holds.

1. (G) contains an (N)-meeting (K_6)-model, and hence (G)
   contains a (K_7)-minor after adding (v).
2. The set

   \[
      X_k=N_F(K_k)\cup N_{A_h}(K_k)                         \tag{2.3}
   \]

   is a proper exact seven-cut.
3. We have

   \[
   |N_F(K_k)|\le5,qquad
   |N_{A_h}(K_k)|\ge 8-|N_F(K_k)|.                          \tag{2.4}
   \]

   In particular, if the complementary component still has row five,
   it has at least three distinct attachments to the absorbed side.

#### Proof

The set (A_h) is connected: (W_h) is a path segment and its terminal
(i_h) has an edge to (P).  It contacts (d_h) through the first edge
of (L_h), and retains every contact in (R).  The other path is
vertex-disjoint from (L_h), so (W_k\subseteq Q-W_h) and lies in one
component (K_k).  Thus (K_k) contacts (d_k).  Its terminal (i_k)
has an edge to (P\subseteq A_h), so (N_{A_h}(K_k)\ne\varnothing).

If (|N_F(K_k)|\ge6), then both (A_h) and (K_k) have at least six
contacts in (F), and their rows cover (F): (A_h) contains
(R\cup\{d_h\}), while (K_k) contains (d_k).  Together with the
other two exact exterior components, these are the four pieces in Lemma
2.1 of the cited note.  That lemma gives outcome 1.

Suppose therefore that (|N_F(K_k)|\le5).  Distinct components of
(Q-W_h) are anticomplete, and (C_i) has no neighbours outside
(F\cup C_i).  Consequently

\[
                         N_G(K_k)=X_k.                         \tag{2.5}
\]

The other exterior components and (v) lie beyond this neighbourhood.
Seven-connectivity gives (|X_k|\ge7).  Equality is outcome 2.  Outside
that equality case, integrality gives (|X_k|\ge8), which is exactly
(2.4).  \(\square\)

Applying Theorem 2.1 in both orientations gives two nested web cells.
Thus the sharp non-cut residue is not merely the original pair of
interfaces (i_1,i_2): after either missing-label path is absorbed, the
component carrying the other path has three or more attachments back to
the connected absorbed side.

### Corollary 2.2 (removable path closes immediately)

If, for one (h), the graph (Q-W_h) has a connected component which
contains (W_k) and has at least six boundary contacts, then (G)
contains the desired (N)-meeting (K_6)-model.

This is the exact nonseparating-path target: one does not need both paths
to be simultaneously removable.  A single missing-label path whose
deletion leaves a six-contact carrier closes the row-five state.

## 3. Why the two-linkage alone is insufficient

There is a fourteen-vertex conservative quotient satisfying every
conclusion of Lemma 6.1 but having treewidth four.

Take (i=1), so

\[
 F_1=\{2,3,4,5,6,7,8\}.
\]

Use a piece (P), two adjacent vertices (q_7,q_8) forming (Q), and
the other exact pieces (C_2,C_3).  Put

\[
\begin{array}{c|c}
\text{piece}&N_N(\text{piece})\\ \hline
P&\{2,3,4,5,6\}\\
q_7&\{2,3,7\}\\
q_8&\{6,8\}\\
C_2&F_2\\
C_3&F_3,
\end{array}                                                     \tag{3.1}
\]

and add all three edges of the triangle (Pq_7q_8P).  The paths

\[
                         7q_7,qquad 8q_8                         \tag{3.2}
\]

are disjoint label-preserving paths to distinct vertices of
(N_Q(P)).  The split rows cover (F_1).

### Lemma 3.1 (exact counterarchitecture)

The quotient (3.1) has no (K_6)-minor.

#### Proof certificate

`degree9_row5_linkage_counterarchitecture_verify.py` checks (3.1)--(3.2)
and the following width-four tree decomposition.  Write the piece names
literally inside the bags:

\[
\begin{array}{lll}
B_0=\{6,P,q_8,C_2,C_3\},&&B_1=\{6,8,q_8,C_2,C_3\},\\
B_2=\{3,P,q_7,C_2,C_3\},&&B_3=\{3,7,q_7,C_2,C_3\},\\
B_4=\{2,P,q_7,C_2,C_3\},&&B_5=\{2,5,P,C_2,C_3\},\\
B_6=\{4,5,P,C_2,C_3\},&&B_7=\{1,2,C_2,C_3\},\\
B_8=\{0,1,2,C_3\},&&K=\{P,q_7,q_8,C_2,C_3\}.
\end{array}                                                     \tag{3.3}
\]

The decomposition tree has edges

\[
 KB_0,KB_2,KB_4, B_0B_1, B_2B_3,
 B_4B_5,B_4B_7,B_5B_6,B_7B_8.                                 \tag{3.4}
\]

Every bag has order at most five.  The verifier checks edge coverage and
the running-intersection property, so the quotient has treewidth at most
four and therefore no (K_6)-minor.  \(\square\)

This graph is not seven-connected; that is exactly the point.  It proves
that the label-preserving linkage is not the missing static certificate.
Ambient connectivity must be used after one path is absorbed, as in
Theorem 2.1.

## 4. The corrected web-exchange target

The true sharp residue is now the following label-free object.

* (A) and (K) are disjoint connected sets.
* (K) has at most five contacts in a seven-label boundary.
* (K) has at least (8-|N_F(K)|) distinct attachments to (A).
* One prescribed missing boundary label has a path ending at one of
  those attachments.

At row five there are at least three attachments.  Choose a minimal tree
in (A) spanning them.  If a pendant part of that tree can be moved into
(K) while retaining the other two attachments and all five boundary
contacts, the contact row rises to six and Lemma 2.1 closes the state.
If it cannot, the first immovable vertex is either

1. a cutvertex of the relevant side; or
2. the unique portal of one of the five boundary labels.

This is exactly the maximal-bad portal peel mechanism, now with three
interface charges rather than two.  A web theorem must show that three
charges cannot remain cyclically locked: two can be exchanged, or their
first bottlenecks together with the five boundary contacts form the exact
seven-cut (2.3).

The structural theorem still missing is therefore:

> **Three-interface portal exchange.**  In the surplus case of Theorem
> 2.1, either a connected peel produces two six-contact pieces, or the
> portal-essential bottlenecks uncross to a separator of order at most
> six or to an exact seven-adhesion carrying a common six-colour boundary
> state.

Theorem 2.1 proves the minor/exact-cut/numerical part of this statement.
It does **not** prove the common colouring state on an arbitrary exact
seven-cut.  That compatibility is an additional transition-alignment
axiom; identifying the cut set alone is insufficient for gluing two
six-colourings.

