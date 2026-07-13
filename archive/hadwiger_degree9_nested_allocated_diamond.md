# The nested degree-nine shore: allocated peeling and the full-core diamond

## 1. Setting

Use the terminal notation of
`hadwiger_degree9_terminal_root_swap.md`.  Put

\[
 T_0=\{h,1,2\},\qquad U=Z\cup J,
 \qquad r=e_6\in Z,\qquad t=e_0\in J.
\]

The sets \(Z,J,D,S,R_5,R_0\) are connected in the roles recorded
there, \(6\in D\), \(5\in R_5\), and

\[
 Z\sim J,D,\qquad J\sim S,\qquad
 D,S\sim R_5,R_0,\qquad R_5\sim R_0.             \tag{1.1}
\]

Both \(r,t\) see the triangle \(T_0\).  The terminal neighbourhood is

\[
 N(U)=T_0\mathbin{\dot\cup}\{s\}
       \mathbin{\dot\cup}P_D(U)
       \mathbin{\dot\cup}C_{34}(J),
 \qquad |P_D(U)|+|C_{34}(J)|\ge3.                \tag{1.2}
\]

The double-literal model in
`hadwiger_degree9_nested_diamond_reduction.md` proves that a
minor-free terminal state has

\[
 |C_{34}(J)|\le1,qquad |P_D(U)|\ge2.             \tag{1.3}
\]

## 2. The weakest split is an allocated one-sided peel

The split (6.3)--(6.4) in the terminal note asks both root sides to
meet \(D\) and \(S\).  The \(Z\)-side already meets \(D\), and each
literal \(3,4\) can be assigned to either of the two carrier bags.
This gives a strictly weaker certificate.

### Theorem 2.1 (allocated one-sided peel)

Let \(X\subseteq\{3,4\}\).  Suppose that \(J\) has a connected
bipartition

\[
                         J=W\mathbin{\dot\cup}K              \tag{2.1}
\]

such that

\[
\begin{aligned}
 &t\in K,\qquad W\sim Z,\\
 &W\sim S\cup(\{3,4\}-X),\\
 &K\sim D\cup X,\qquad K\sim S\cup(\{3,4\}-X).
                                                               \tag{2.2}
\end{aligned}
\]

Then \(G\) contains a \(K_7\)-minor.

#### Proof

Put \(E=Z\cup W\).  It is connected, contains \(r\), and is
adjacent to \(K\).  It sees \(D\) through the old \(Z\)-\(D\)
contact, so no second \(D\)-portal in \(W\) is required.

If \(X\ne\{3,4\}\), use the carrier bags

\[
 A=D\cup R_5\cup X,qquad
 B=S\cup R_0\cup\{v\}\cup(\{3,4\}-X).            \tag{2.3}
\]

The first is connected through \(65\), and the second is connected
through any literal in \(\{3,4\}-X\), the right root in \(R_0\),
and \(v\).  If \(X=\{3,4\}\), instead use

\[
 A=D\cup R_0\cup\{3,4\},qquad
 B=S\cup R_5\cup\{v\};                            \tag{2.4}
\]

now \(B\) is connected through \(v5\).  In either case \(A,B\)
are disjoint and adjacent through \(v6\) (also through the old right
bag contact).  The four sets \(E,K,A,B\) form a clique by (2.2), the
\(Z\)-\(D\) edge, and the edge between the two sides of (2.1).
Each is adjacent to all of \(T_0\): use \(r,t,6,v\), respectively,
and the right root included in \(A\) for its \(h\)-contact.  Hence

\[
                  \{h\},\{1\},\{2\},E,K,A,B       \tag{2.5}
\]

is a \(K_7\)-model. \(\square\)

All four choices of \(X\) and all twenty-one adjacencies are checked
independently by `degree9_nested_allocated_peel_verify.py`.

Theorem 2.1 is the weakest connected *bipartition of the existing
shore* needed by the displayed carrier construction.  A still weaker
positive object may absorb vertices into either carrier; that object is
the rooted diamond of the preceding note.

## 3. The whole four-connected core already contains the prescribed roots

The absence of a diamond is not the live global obstruction.

### Theorem 3.1 (four-terminal diamond forced in the full core)

Let

\[
                         F=G-T_0,qquad
                         R=\{r,t,6,s\}.             \tag{3.1}
\]

If \(G\) is seven-connected and \(K_7\)-minor-free, then \(F\)
contains a diamond on \(R\).  Moreover, for every \(x\in R\), it
contains such a diamond in which \(x\) is one of the two degree-three
terminals.

#### Proof

The graph \(F\) is four-connected: a separator of order at most three
in \(F\), together with \(T_0\), would be a separator of order at
most six in \(G\).

Suppose first that \(F\) has no diamond on \(R\).  Corollary 9.3 of
Hayashi--Kawarabayashi, *Rooted topological minors on four vertices*,
gives a set \(Q\subseteq V(F)-R\) of order four such that no component
of \(F-Q\) contains two vertices of \(R\).  Let
\(C_r,C_t,C_6,C_s\) be the four components containing the four
terminals.  For each \(x\in R\),

\[
                         N_G(C_x)\subseteq T_0\cup Q.         \tag{3.2}
\]

The other three terminal components show that this is a genuine
separator.  Seven-connectivity and \(|T_0\cup Q|=7\) therefore give

\[
                         N_G(C_x)=T_0\cup Q.                 \tag{3.3}
\]

Thus the four terminal components are four disjoint connected shores,
each full to the same seven-vertex boundary.  Enumerate
\(Q=\{q_r,q_t,q_6,q_s\}\).  The seven sets

\[
 \{h\},\quad\{1\},\quad\{2\},\quad
 C_r\cup\{q_r\},\quad C_t\cup\{q_t\},\quad
 C_6\cup\{q_6\},\quad C_s\cup\{q_s\}              \tag{3.4}
\]

are connected and pairwise adjacent: (3.3) supplies every adjacency
involving a nonsingleton set and \(T_0\) is a triangle.  This is a
\(K_7\)-model, a contradiction.  Hence a diamond on \(R\) exists.

Theorem 5.4 of the same paper says that, under its three-fan hypothesis,
the existence of one diamond on four terminals gives, for each terminal,
a diamond in which that terminal has degree three.  Four-connectivity of
\(F\) supplies the required three-fan from every member of \(R\) to
the other three.  This proves the last assertion. \(\square\)

There is also a shorter minor-only strengthening.  The four vertices
\(v,3,4,5\) induce a \(K_4\) in \(F\).  Since \(F\) has vertices
outside this \(K_4\), a planar embedding would place an outside
component in a triangular face of that \(K_4\), making its boundary a
three-cut.  Therefore \(F\) is nonplanar.  The rooted-\(K_4\) theorem
of Fabila-Monroy--Wood now gives a \(K_4\)-minor in \(F\) rooted at
the prescribed four vertices \(r,t,6,s\).

## 4. What this closes, and the central-edge funnel

The six possible missing pairs of a diamond on \(R\) are as follows.
The second column lists the degree-three pair.

\[
\begin{array}{c|c|c}
\text{missing pair}&\text{degree-three pair}&\text{old geometry}\\ \hline
6s&rt&\text{desired carrier-missing diamond}\\
rt&6s&Z\text{--}J\\
ts&r6&J\text{--}s\\
t6&rs&J\text{--}D\text{ if present}\\
rs&t6&Z\not\sim S\text{ (the forbidden direction)}\\
r6&ts&Z\text{--}D.
\end{array}                                                \tag{4.1}
\]

By Theorem 3.1 one may demand that \(r\) have degree three, leaving
only the missing pairs \(6s,ts,t6\).  One may separately demand that
\(t\) have degree three, leaving \(6s,rs,r6\).  Thus, after the two
aligned old-bag directions \(ts\) and \(r6\), the only simultaneous
label obstruction is the crossed pair

\[
       \text{an }(r,s)\text{-branch diamond missing }t6,
       \qquad
       \text{a }(t,6)\text{-branch diamond missing }rs.     \tag{4.2}
\]

This table is a classification, not yet a repair theorem.  The diamonds
in Theorem 3.1 live in the whole core \(F\); they may consume vertices
of \(D,S,R_5,R_0\) needed to make the \(6\)- and \(s\)-rooted bags
collectively adjacent to \(h,1,2\).  Consequently neither the full-core
diamond nor even the full-core rooted \(K_4\) may simply be augmented by
the old carriers.

The broad reserved-carrier formulation is now superseded by Theorem 4.5
of `hadwiger_four_connected_rooted_diamond.md`.  Contracting only the
actual edge \(56\) gives the sharper exhaustive funnel:

1. the full exact adhesion
   \(\{h,1,2,5,6,y,z\}\), with two or three shores, each full to the
   seven boundary vertices; or
2. a rooted \(K_4\)-model at \(56,e_6,e_0,v\) in which every
   \(5\)-to-right-root connector is dirty.

Theorem 2.1 closes either branch whenever its portal surgery produces
the displayed one-sided peel of \(J\).  It does **not** prove that an
arbitrary full-adhesion shore or dirty connector produces that peel.
Thus its exact contribution is a positive exchange certificate, not a
closure of Theorem 4.5.  The no-diamond infinite family and all
four-literal allocation ambiguity have been removed; the remaining
tasks are the two-/three-shore \(56\)-transition in outcome 1 and the
first dirty-hit exchange in outcome 2.
