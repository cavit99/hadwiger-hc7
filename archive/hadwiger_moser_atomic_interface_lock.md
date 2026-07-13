# Atomic interface locks at a two-shore Moser adhesion

## 1. Setting

Let \(G\) be seven-connected and \(K_7\)-minor-free.  Let \(S\) be a
seven-cut inducing the pure Moser spindle

\[
E(G[S])=\{01,02,03,04,12,16,26,34,35,45,56\}.
\]

Let \(D,D^*\) be two connected full shores of \(G-S\), with \(D\) a
minimum fragment.  Suppose a crossed cyclic hull in \(D\) has been
extended to a covering connected split

\[
D=X\mathbin{\dot\cup}Y,
\]

where \(X,Y\) are nonempty, connected and adjacent.  Put

\[
P_X=N_S(X),\quad P_Y=N_S(Y),\quad
T_X=N_Y(X),\quad T_Y=N_X(Y).
\]

Assume the split is **bad**: contracting \(X,Y,D^*\) to adjacent
vertices \(x,y\) and a full vertex \(h\), respectively, gives no
\(K_7\)-minor.

Minimum-fragment atomicity gives

\[
|P_X|+|T_X|\ge8,\qquad |P_Y|+|T_Y|\ge8.            \tag{1.1}
\]

## 2. The near-full quotient lemma

Put

\[
W=\{1,2,3,4\};
\]

the spindle induced by \(W\) is \(2K_2\), with edges \(12,34\).

### Lemma 2.1

Suppose \(P,Q\subseteq S\), \(P\cup Q=S\), and
\(|P|,|Q|\ge6\).  If the quotient consisting of

* the Moser graph on \(S\);
* adjacent vertices \(x,y\) with boundary rows \(P,Q\); and
* a vertex \(h\) complete to \(S\)

has no \(K_7\)-minor, then

\[
P=S-\{a\},\qquad Q=S-\{b\}
\]

for distinct \(a,b\in W\).

### Proof

Each row has defect at most one.  If a row is full, delete one surplus
incidence so that the two resulting one-vertex defects are distinct and
not both in \(W\).  Thus it is enough to prove that every defect pair
not contained in \(W\) is \(K_7\)-positive.

The automorphism group of the labelled spindle has five orbits on such
unordered pairs.  Representatives and explicit branch sets are shown
below.  A symbol such as \(2h\) denotes the bag \(\{2,h\}\).

\[
\begin{array}{c|c}
\text{defects of }(x,y)&\text{seven branch sets}\\ \hline
(0,1)&3\mid4\mid5\mid x\mid y\mid2h\mid016\\
(0,5)&1\mid2\mid6\mid x\mid y\mid3h\mid045\\
(1,5)&0\mid3\mid4\mid x\mid y\mid2h\mid156\\
(1,6)&0\mid3\mid4\mid x\mid y\mid2h\mid156\\
(5,6)&0\mid1\mid2\mid x\mid y\mid3h\mid456
\end{array}                                       \tag{2.1}
\]

The three-digit bags are connected by the displayed Moser edges.  In
each row the three singleton roots form a triangle, the \(h\)-bag is
connected, and direct inspection of the spindle edges shows that all
seven bags are pairwise adjacent.  The five representatives cover all
defect pairs having at least one member outside \(W\).  Hence a negative
quotient must have the asserted two distinct defects in \(W\).
\(\square\)

The point of the lemma is the invariant \(W\), not the five-line check:
all near-full negative splits concentrate both defects in one induced
\(2K_2\).

### Lemma 2.2 (the (W)-residue is genuine)

Every one of the six quotients with distinct defects

\[
 \{a,b\}\in\binom{\{1,2,3,4\}}2
\]

is (K_7)-negative.  Thus Lemma 2.1 cannot be sharpened by deleting a
positive suborbit.  Under the Moser automorphism group the six pairs have
two orbits,

\[
 \{12,34\},qquad \{13,14,23,24\},                \tag{2.2}
\]

and both are negative.

The dependency-free verifier
`moser_nearfull_W_defect_verify.py` proves the statement directly.  The
quotient has ten vertices, so a (K_7)-model uses between seven and ten
vertices.  For each size the verifier enumerates every chosen vertex set
and every canonical partition into seven nonempty bags, then checks bag
connectivity and all 21 bag adjacencies.  It prints all six pairs as
negative.  There are consequently no positive (W)-suborbits for which
branch-set certificates could be supplied; the next invariant really
must retain portal placement or boundary state.

## 3. Atomic two-edge lock

### Theorem 3.1

Let

\[
m=|E_G(X,Y)|.
\]

Then \(m\ge2\).  If \(m=2\), there are distinct \(a,b\in W\) such that

\[
P_X=S-\{a\},\qquad P_Y=S-\{b\},                    \tag{3.1}
\]

and the two interface edges form a matching: they have two distinct
ends in \(X\) and two distinct ends in \(Y\).

### Proof

Since every vertex of \(T_X\) is incident with an interface edge,
\[
|T_X|\le m,\qquad |T_Y|\le m.                     \tag{3.2}
\]

If \(m=1\), (1.1)--(3.2) make both \(P_X,P_Y\) equal to \(S\).
The quotient is \(K_7\)-positive by Lemma 2.1 (or directly by the first
model in (2.1), after deleting surplus incidences), contradicting
badness.  Hence \(m\ge2\).

Let \(m=2\).  Equations (1.1)--(3.2) give
\[
|P_X|,|P_Y|\ge6.
\]
Lemma 2.1 gives (3.1).  In particular both rows have order exactly six.
Equations (1.1)--(3.2) now force
\[
|T_X|=|T_Y|=2.
\]
The two interface edges therefore have distinct ends on both sides,
which says exactly that they form a matching. \(\square\)

This eliminates every bridge interface and replaces all two-edge
interfaces by one label-free geometry: a matching across two almost-full
pieces, with both defects in the same boundary \(2K_2\).

## 4. State geometry on the two-edge lock

Now suppose \(G\) is also six-minor-critical.  Write the interface
matching as

\[
e_1=x_1y_1,\qquad e_2=x_2y_2,
\quad x_i\in X,\ y_i\in Y.
\]

### Corollary 4.1

For \(i=1,2\), every six-colouring \(c_i\) of \(G-e_i\) has the
following properties.

1. \(c_i(x_i)=c_i(y_i)=\alpha_i\).
2. The other interface edge is proper.
3. The induced boundary state extends the unchanged opposite shore and
   the split shore with \(e_i\) deleted, but not the original split
   shore.
4. For at least four of the five colours
   \(\gamma\ne\alpha_i\), the
   \(\alpha_i/\gamma\)-components containing \(x_i\) and \(y_i\) are
   distinct and each has an actual colour-\(\alpha_i\) or
   colour-\(\gamma\) boundary anchor in \(S\).

### Proof

Items 1 and 3 are the standard edge-critical and exact-state-transfer
conclusions.  Item 2 holds because \(e_{3-i}\) remains present.

For a colour \(\gamma\ne\alpha_i\), the interface exchange lemma gives
either an \(\alpha_i/\gamma\) path from \(x_i\) to \(y_i\) inside
\(D-e_i\), or the two anchored components in item 4.  Every path of the
first type must cross the sole remaining interface edge \(e_{3-i}\).
Its two ends have fixed, distinct colours in \(c_i\), so at most one
choice of \(\gamma\) can use that edge in an
\(\alpha_i/\gamma\)-subgraph.  At least four colours therefore have the
two-anchor outcome. \(\square\)

Thus an atomic Moser bad split has only two possible forms:

* at least three actual interface edges, each deletion preserving the
  covering split while creating a strict opposite-shore state; or
* the matching lock (3.1), in which each of the two deletion witnesses
  carries four simultaneous two-sided boundary anchors.

The remaining exchange problem is now exact.  One must either use those
four anchored colours to split one almost-full piece again, or realize
the two-edge lock as a smaller rooted side with the same extension
family.  The theorem does not yet perform that last exchange.

## 5. Common-state holonomy is an XOR rectangle

The two matching edges also admit a purely state-theoretic
classification which is independent of the Moser labels.

### Lemma 5.1 (cross-intersecting two-coordinate relations)

Let \(\Omega\) be a finite set, and let
\({\cal A},{\cal B}\subseteq\Omega^2\) be nonempty.  Assume

\[
\forall a\in{\cal A},\ \forall b\in{\cal B},\qquad
a_1=b_1\ \hbox{or}\ a_2=b_2.                       \tag{5.1}
\]

Suppose there is a cross-pair sharing only its first coordinate and a
cross-pair sharing only its second coordinate.  Then exactly one of the
following holds.

1. One of \({\cal A},{\cal B}\) is a singleton; the other is contained
   in the union of the row and column through that point.
2. There are distinct \(p,r\in\Omega\) and distinct \(q,s\in\Omega\)
   such that, after possibly interchanging the families,
   \[
   {\cal A}=\{(p,q),(r,s)\},\qquad
   {\cal B}=\{(p,s),(r,q)\}.                        \tag{5.2}
   \]

### Proof

If one family is a singleton, (5.1) gives item 1.  Assume both have at
least two elements.  Neither family can lie in one row: two members with
the same first coordinate and different second coordinates force every
member of the other family into that row, contrary to the second-only
cross-pair.  The same argument excludes one column.

Thus \({\cal A}\) has two members
\[
(p,q),(r,s),\qquad p\ne r,\ q\ne s.
\]
The points which share a coordinate with both are exactly
\[
(p,s),(r,q).
\]
Condition (5.1) puts \({\cal B}\) inside this two-point set; since
\(|{\cal B}|\ge2\), equality holds.  Reversing the argument puts
\({\cal A}\) inside \(\{(p,q),(r,s)\}\), proving (5.2).
\(\square\)

### Theorem 5.2 (distinct states or star/XOR lock)

Keep the atomic two-edge lock, but the statement below only needs a
two-edge matching between connected pieces \(X,Y\).  Let
\(\Phi\) be an exact boundary state which extends the unchanged
opposite shore and both \(D-e_1\) and \(D-e_2\), but not \(D\).

For a labelled colouring of the boundary representing \(\Phi\), let
\({\cal A}_\Phi\) be the ordered pairs
\[
\bigl(c(x_1),c(x_2)\bigr)
\]
which occur in extensions over \(X\), and define
\({\cal B}_\Phi\) from \(y_1,y_2\) symmetrically.  Then the two relations
have exactly one of the star/XOR forms in Lemma 5.1.

Consequently, for the two transition-state sets
\[
{\cal T}_i=
\bigl({\cal E}_6(D-e_i,S)-{\cal E}_6(D,S)\bigr)
\cap{\cal E}_6(D^*,S),                             \tag{5.3}
\]
either

1. \({\cal T}_1\cap{\cal T}_2=\varnothing\), so the two interface
   deletions force genuinely distinct transition states; or
2. every state in the intersection makes one piece terminal-pair
   rigid or induces the XOR rectangle (5.2).

### Proof

Fix \(\Phi\in{\cal T}_1\cap{\cal T}_2\) and align one labelled boundary
colouring representing it.  Because the only \(X\)-\(Y\) edges are
\(x_1y_1,x_2y_2\), an \(X\)-extension with pair \(a\) and a
\(Y\)-extension with pair \(b\) glue over \(D\) exactly when
\[
a_1\ne b_1,\qquad a_2\ne b_2.
\]
The state does not extend \(D\), so (5.1) holds.

The state extends \(D-e_1\).  In every such extension the deleted edge
has equal-coloured ends, while the retained edge is proper.  Hence
there is a cross-pair with equality only in coordinate 1.  The
extension over \(D-e_2\) gives equality only in coordinate 2.
Lemma 5.1 applies.  The final dichotomy is immediate from whether the
intersection in (5.3) is empty. \(\square\)

The XOR rectangle is not a vague compatibility condition.  It is the
unique two-coordinate parity gadget:

\[
(p,q),(r,s)\quad\hbox{versus}\quad(p,s),(r,q).
\]

Thus the two-edge residue can no longer hide behind arbitrary extension
families.  Its remaining obstruction is one of:

* transition-state diversity, which feeds the Moser matching-holonomy
  theorem;
* a forced terminal pair on one rooted piece; or
* a literal XOR relation which must be destroyed by an internal minor
  transition or by a portal split.

Eliminating the star and XOR relations using the four anchored colours
of Corollary 4.1 would complete the two-edge atomic cell.
