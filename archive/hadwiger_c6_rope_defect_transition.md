# The exact defect transition along a locked \(C_6\) rope

> **Scope notice.**  This note is conditional on the prior existence of
> two locked end vertices and an \(xy\)-numbering between them.  The
> former SPQR-orientation argument producing those two ends has been
> retracted.  Consequently this note is not used in the proof of the
> \(C_6\dot\cup K_1\) closure; the orientation-free leaf-singleton and
> cycle-leaf arguments supersede it.

## 1. Setting

Let \(D\) be a full shore on

\[
 S=\{z,c_0,\ldots,c_5\},
\]

where \(c_0c_1\cdots c_5c_0\) is the missing cycle. Let \(x,y\) be the
two locked end vertices of the rope. Because \(D\) is two-connected,
an \(xy\)-numbering gives an ordering

\[
 x=v_1,v_2,\ldots,v_n=y
\]

in which every proper prefix and every complementary suffix induces a
connected subgraph. (If \(xy\notin E(D)\), add \(xy\), take a standard
st-numbering, and then discard the added edge; it joins only the first
and last vertices and is not needed by a proper prefix or suffix.)
Thus put

\[
 \{x\}=X_0\subsetneq X_1\subsetneq\cdots
 \subsetneq X_m=D-\{y\},
\tag{1.1}
\]

where the \(X_i\) are the nonempty proper prefixes. Put

\[
 P_i=S-N_S(X_i),\qquad Q_i=S-N_S(D-X_i).
\tag{1.2}
\]

Assume the ambient two-shore graph is \(K_7\)-minor-free, so every one
of these connected splits belongs to the exact bad-split atlas.

Assume the two end vertices have the exact degree-two locks

\[
\begin{aligned}
P_0&=N_C(a),& Q_0&=\{a\},\\
P_m&=\{b\},& Q_m&=N_C(b),
\end{aligned}
\tag{1.3}
\]

where \(C=c_0c_1\cdots c_5c_0\). These are exactly the end locks forced
for the two leaves of the residual common-face SPQR rope.

## 2. End labels

### Lemma 2.1

The labels \(a,b\) are distinct and adjacent on \(C\).

#### Proof

Defects are monotone along (1.1):

\[
 P_m\subseteq P_i\subseteq P_0,\qquad
 Q_0\subseteq Q_i\subseteq Q_m.
\tag{2.1}
\]

Thus \(b\in P_0=N_C(a)\) and \(a\in Q_m=N_C(b)\). Hence \(a,b\) are
adjacent. They cannot coincide because a cycle has no loop. \(\square\)

Rotate the labels so that \(a=c_0\) and \(b=c_1\). Then

\[
\begin{aligned}
(P_0,Q_0)&=(\{c_5,c_1\},\{c_0\}),\\
(P_m,Q_m)&=(\{c_1\},\{c_0,c_2\}).
\end{aligned}
\tag{2.2}
\]

## 3. The three-state transition

### Theorem 3.1 (forced transition order)

Every bad split in the chain has one of exactly the following three
defect pairs:

\[
\begin{array}{ccl}
L&=&(\{c_5,c_1\},\{c_0\}),\\
M&=&(\{c_5,c_1\},\{c_0,c_2\}),\\
R&=&(\{c_1\},\{c_0,c_2\}).
\end{array}
\tag{3.1}
\]

Moreover the word of states along the rope has the form

\[
 L^{\,*}M^{\,*}R^{\,*},
\tag{3.2}
\]

with the first and last runs nonempty. In particular, the \(c_2\)
defect can enter the right coordinate only before or simultaneously
with the departure of the \(c_5\) defect from the left coordinate; the
reverse order is impossible.

#### Proof

By monotonicity and (2.2), the only four set-theoretically possible
pairs are \(L,M,R\), and

\[
 Z=(\{c_1\},\{c_0\}).
\tag{3.3}
\]

The exact low-defect atlas says that a bad pair whose two coordinates
have order at most two must have both coordinates nonempty and, after
possibly reversing them, must dominate either

\[
 \{v\}\mid N_C(v)
\quad\text{or}\quad
 M_j\mid M_k\quad(j\ne k),
\tag{3.4}
\]

where the \(M_j\) are the three antipodal matching edges of \(C\).
The pair \(Z\) has two singleton coordinates and dominates neither
pattern, so it is positive and would give a \(K_7\)-minor. Hence \(Z\)
cannot occur.

The pairs \(L\) and \(R\) are the two end locks. The middle pair \(M\)
dominates \(\{c_1\}\mid N_C(c_1)\), so it is an allowed bad pair.
Finally, the first coordinate can only decrease and the second can only
increase. Therefore all \(L\)-states precede all \(M\)-states, which
precede all \(R\)-states, proving (3.2). \(\square\)

## 4. Scope and next use

The theorem is a statement about actual nested connected shore splits;
it does not compare portal representatives chosen in unrelated
linkages. It is therefore immune to the representative-identification
error that invalidated the earlier symbolic precedence claim.

It reduces an arbitrarily long rope to three constant defect zones and
a directed transition

\[
 L\longrightarrow M\longrightarrow R.
\]

Defect constancy alone does not make a zone colour-gluable. The remaining
step must decorate these three states by the exact boundary extension
relations forced by internal deletion and contraction. A valid closure
would show that a constant zone contains a minor-irrelevant segment, or
that the unique transition torso supplies a positive rooted model.

## 5. Exact portal rows at a state change

Use the (xy)-numbering from Section 1 and suppose the state changes
when the next vertex (u) is added.  Put

[
 A=X_{i-1},qquad B=D-X_i,qquad X_i=Acup{u}.
	ag{5.1}
]

The numbering gives an (A)-neighbour and a (B)-neighbour of (u).
There is also an (A)-(B) edge.  Indeed, (D-u) is connected because
(D) is two-connected; any path in (D-u) from (A) to (B) must
cross such an edge.  This last adjacency is essential in the quotient
certificates below and is not an assumed chord.

In all three possible changes, (A) has defect
(N_C(c_0)={c_5,c_1}) and (B) has defect
(N_C(c_1)={c_0,c_2}).  Monotonicity determines the mandatory row of
(u):

[
egin{array}{c|c|c}
	ext{change}&	ext{mandatory contacts of }u&	ext{mandatory misses of }u\
hline
L	o M&c_2&c_5,c_1,c_0\
M	o R&c_5&c_1,c_0,c_2\
L	o R&c_2,c_5&c_1,c_0.
end{array}                                         	ag{5.2}
]

### Lemma 5.1 (transition-vertex portal lock)

In a (K_7)-minor-free realization,

[
egin{array}{c|c}
L	o M&N_W(u)subseteq{c_2,c_4},quad c_2in N_W(u),\
M	o R&N_W(u)subseteq{c_3,c_5},quad c_5in N_W(u),\
L	o R&N_W(u)={c_2,c_5}.
end{array}                                         	ag{5.3}
]

The contact with (z) is unrestricted by this lemma.

#### Proof

Contract (A), (B), and the opposite full shore to helpers denoted by
the same letters and (H), retain (u), and retain all seven boundary
vertices.  Keep the edges

[
 Au,quad uB,quad AB,                              	ag{5.4}
]

the exact contact rows of (A,B), and the full boundary row of (H).
If (u) touches (c_3) in an (L	o M) transition, the following are
seven branch sets:

[
 {c_0,c_5,H},quad {c_1,c_3},quad {c_2,u},quad
 {c_4},quad{z},quad{A},quad{B}.          	ag{5.5}
]

If (u) touches (c_4) in an (M	o R) transition, use

[
 {c_0,c_3},quad {c_1,c_2,H},quad {c_4},quad
 {c_5,u},quad{z},quad{A},quad{B}.        	ag{5.6}
]

Every displayed set is connected, and direct inspection using the
complement-cycle boundary verifies all pairwise adjacencies.  Thus
(c_3) is forbidden in the first transition and (c_4) in the second.
Combining this with (5.2) proves the first two rows of (5.3).  In a
direct (L	o R) transition, (u) already touches both (c_2,c_5), so
(5.5) excludes (c_3) and (5.6) excludes (c_4), proving the last row.
(square)

The dependency-free exhaustive replay
`c6_rope_direct_transition_quotient.py` checks all 159,027 seven-bag
partitions of this eleven-vertex quotient.  Without the forced (AB)
edge, all coarse rows are negative; with (AB), it reproduces (5.5)
and (5.6).  This guards both against silently assuming an optional
portal and against omitting the two-connectivity adjacency.

The three rows in (5.3) are exactly the three sparse types suggested by
the singleton split atlas: the first lies on one boundary triangle, the
second on the other, and the direct jump lies on an antipodal matching
edge.  Contact existence alone does not eliminate these final rows.
