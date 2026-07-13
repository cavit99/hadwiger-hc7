# Maximal bad splits force essential portal vertices

## 1. A label-free peel lemma

Let (S) be a fixed boundary, let (D) be a connected open shore, and
let

\[
                         D=A\mathbin{\dot\cup}B                 \tag{1.1}
\]

be a partition such that (G[A]) and (G[B]) are connected and there is
an (A)--(B) edge.  Its contact rows are

\[
                         R_A=N_S(A),\qquad R_B=N_S(B).           \tag{1.2}
\]

Fix a target clique order (h).  Call the row pair **positive** if the
quotient obtained from (G[S]) by adding adjacent vertices (a,b) with
neighbourhoods (R_A,R_B), respectively, has a (K_h)-minor.  Positivity
is monotone under coordinatewise enlargement of the two rows.

### Lemma 1.1 (maximal-bad portal peel)

Suppose ((R_A,R_B)) is maximal among the row pairs of realized connected
splits which are not positive.  Let (z\in B) satisfy

\[
 N_A(z)\ne\varnothing,\qquad B-\{z\}\ne\varnothing,qquad
 G[B-z]\text{ is connected}.                                  \tag{1.3}
\]

If (z) carries a contact missing from the (A)-row, then it is the
unique (B)-portal of some boundary label:

\[
 N_S(z)\nsubseteq R_A
 \quad\Longrightarrow\quad
 N_S(z)\nsubseteq N_S(B-z).                                    \tag{1.4}
\]

The symmetric assertion holds for a vertex movable from (A) to (B).

#### Proof

Move (z) across the split:

\[
                         A'=A\cup\{z\},\qquad B'=B-\{z\}.
\]

Condition (1.3) says that this is again a connected split.  If the
conclusion of (1.4) failed, every boundary contact carried by (z) would
remain represented in (B-z).  Hence

\[
 R_{B'}=R_B,qquad R_{A'}=R_A\cup N_S(z)\supsetneq R_A.          \tag{1.5}
\]

The new realized row pair strictly dominates the old one.  Maximality
makes it positive.  Contracting (A',B') lifts its quotient
(K_h)-model to the original graph, contradicting the assumption that
the split was a surviving target-minor obstruction.  Therefore some
label in (N_S(z)) has no other neighbour in (B), which is exactly
(1.4). (square)

This lemma uses no colouring, planarity, Moser labels, or connectivity
number.  It converts maximality of a finite bad-split relation into an
actual structural statement: every useful movable frontier vertex is
portal-essential.  The only other possibilities are that the vertex adds
no new contact or that it is a cutvertex of its current side.

## 2. Singleton re-root specialization

Use the double-pure-Moser overlap in
`hadwiger_singleton_reroot_classification_audit.md`.  Let (D=A\dot\cup
B), with (5\in A,6\in B), be a realized quotient-negative split chosen
maximal by its contact rows.  The exact atlas
`singleton_reroot_split_atlas.py` says that its state lies below one of
the ten maximal negative rows in (8.2) of that audit.

Apply Lemma 1.1 with (h=7).  Every vertex which can be peeled from the
(6)-side to the (5)-side and which reaches one of the missing portal
classes of the (5)-side is either

1. a cutvertex of the (6)-side; or
2. the unique (6)-side portal of at least one boundary label.

The same holds with the sides interchanged.  Thus failure of the
cross-saturated split is not an arbitrary absence of linkage.  At a
maximal bad split all possible cross-contact improvements are locked by
cutvertices or uniquely charged portal vertices.

Seven-connectivity supplies the complementary numerical pressure.  For
every nonempty proper (Y\subset D),

\[
 |N_D(Y)-Y|+|N_S(Y)|\ge7.                                  \tag{2.1}
\]

For example, the maximal bad rows with a four-element contact side force
at least three distinct internal frontier vertices on that side; a
five-contact side forces at least two.  Combining this multiplicity with
the essential-portal conclusion is the precise next uncrossing target:
either two frontier vertices can exchange without losing a row, giving
the (K_7) split, or their distinct portal charges expose a nested exact
seven-adhesion.

No latter uncrossing theorem is claimed here.  Lemma 1.1 is the rigorous
bridge from the finite ten-row atlas to that label-free structural task.
