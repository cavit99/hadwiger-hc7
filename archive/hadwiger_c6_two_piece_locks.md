# The \(C_6\dot\cup K_1\) boundary: two-piece defect locks

## 1. Setting and exact two-piece atlas

Let \(G\) be seven-connected and \(K_7\)-minor-free.  Let

\[
 S=W\mathbin{\dot\cup}\{c\},\qquad |W|=6,
\]

where \(c\) is complete to \(W\), and let the missing-edge graph on
\(W\) be the cycle

\[
 F=0\,4\,2\,3\,1\,5\,0.                              \tag{1.1}
\]

Thus \(G[W]\) is the triangular prism: its two triangles are

\[
 P=\{0,1,2\},\qquad Q=\{3,4,5\},
\]

and its three cross-edges are the antipodal pairs

\[
 M_0=\{0,3\},\qquad M_1=\{1,4\},\qquad M_2=\{2,5\}. \tag{1.2}
\]

Suppose \(G-S\) has exactly two connected full shores \(D,D'\).  If
\(D=X\dot\cup Y\) is a connected bipartition with an \(X\)-\(Y\) edge,
put

\[
 d_X=S-N_S(X),\qquad d_Y=S-N_S(Y).
\]

Contract \(X,Y,D'\) to adjacent helpers \(x,y\) and a full helper \(h\).
An exact enumeration of all \(3^7\) contact covers gives 28 maximal
negative contact pairs.  In defect form they are:

\[
\begin{array}{ll}
\varnothing\mid P,\quad \varnothing\mid Q,
  &\varnothing\mid(W-M_i)\quad(i=0,1,2),\\
\{v\}\mid N_F(v) &(v\in W),\\
M_i\mid M_j &(i\ne j),
\end{array}                                             \tag{1.3}
\]

together with all reversals.  Here \(N_F(v)\) is the pair of neighbours
of \(v\) on the missing cycle.  Every other negative pair is obtained
by enlarging both displayed defects, subject to \(d_X\cap d_Y=\varnothing\).

This is a finite quotient statement: any connected split whose defect
pair does not dominate a pair in (1.3) gives an explicit \(K_7\)-minor
after expanding the three contracted helpers.  The exact certificate is
c6_two_piece_contact_atlas.py.  It enumerates all 11,880 possible
seven-bag partitions of supports of order seven through ten, checks all
\(3^7\) contact covers, and asserts the counts 762 and 28 before
printing the defect list (1.3).

## 2. First internal-connectivity consequence

### Lemma 2.1

Every nonsingleton full shore is two-connected.  In particular, shore
order two is impossible.

### Proof

If an edge of \(D\) is a bridge with connected sides \(X,Y\), then
\(N_S(X)\), together with the endpoint of the bridge on the other side,
separates \(X\) from \(D'\).  Seven-connectivity gives

\[
 |N_S(X)|,|N_S(Y)|\ge6.                              \tag{2.1}
\]

Thus \(|d_X|,|d_Y|\le1\).  No pair in (1.3) has both coordinates of
order at most one, so the split gives a \(K_7\)-minor.

If \(z\) is a cutvertex and \(C_1,C_2\) are two components of \(D-z\),
then

\[
 |N_S(C_i)|\ge6                                      \tag{2.2}
\]

because \(N_S(C_i)\cup\{z\}\) is a cut in \(G\).  The connected split
\(C_1\mid(D-C_1)\) has both sides six-full, and the same atlas
contradiction applies.  Hence \(D\) has no cutvertex.  A two-vertex
shore consists of a bridge and was already excluded.

### Lemma 2.2

A nonsingleton full shore has order at least four.

### Proof

By Lemma 2.1, a shore of order three would be a triangle
\(D=\{x_1,x_2,x_3\}\).  Put

\[
 d_i=S-N_S(x_i).
\]

The set \(N_S(x_i)\cup(D-\{x_i\})\) separates \(x_i\) from the opposite
shore.  Seven-connectivity therefore gives \(|N_S(x_i)|\ge5\), so
\(|d_i|\le2\).  Fullness says

\[
 d_1\cap d_2\cap d_3=\varnothing.                   \tag{2.3}
\]

For each \(i\), the connected split \(x_i\mid(D-x_i)\) has defect pair

\[
 \left(d_i,d_j\cap d_k\right),\qquad
 \{i,j,k\}=\{1,2,3\}.                               \tag{2.4}
\]

Lemma 4.1 below (which is a direct reading of the atlas (1.3)) says
that both coordinates of every low-defect negative pair are nonempty.
Thus \(d_1,d_2,d_3\) are pairwise intersecting.  Together with (2.3)
and \(|d_i|\le2\), this forces

\[
 d_1=\{b,c\},\qquad d_2=\{a,c\},\qquad
 d_3=\{a,b\}                                        \tag{2.5}
\]

for distinct \(a,b,c\).  Applying the singleton/pair alternative in
Lemma 4.1 to (2.4) gives

\[
 \{b,c\}=N_F(a),\qquad \{a,c\}=N_F(b),\qquad
 \{a,b\}=N_F(c),
\]

which makes \(a,b,c\) a triangle in the missing cycle \(F=C_6\), an
impossibility.

## 3. Every individual portal row is locked

### Lemma 3.1

Let \(D\) be nonsingleton and \(x\in D\).  Put

\[
 d_x=S-N_S(x),\qquad e_x=S-N_S(D-x).
\]

Then \(|e_x|\le1\), and at least one of the following holds:

1. \(P\subseteq d_x\) or \(Q\subseteq d_x\);
2. \(W-M_i\subseteq d_x\) for some \(i\in\{0,1,2\}\);
3. \(e_x=\{v\}\) for some \(v\in W\), and
   \(N_F(v)\subseteq d_x\).

Consequently, if \(D-x\) is full to \(S\), then

\[
 N_S(x)\subseteq
 P\cup\{c\},\quad Q\cup\{c\},\quad\text{or}\quad
 M_i\cup\{c\}                                        \tag{3.1}
\]

for some \(i\).  In general \(|N_S(x)|\le5\); the five-contact
alternative is possible only when \(x\) is the unique shore portal of
the vertex \(v\) in item 3.

### Proof

By Lemma 2.1, \(D-x\) is connected.  The set

\[
 \{x\}\cup N_S(D-x)
\]

separates \(D-x\) from the opposite shore, so seven-connectivity gives
\(|N_S(D-x)|\ge6\), equivalently \(|e_x|\le1\).

Apply the exact list (1.3) to the connected split
\(\{x\}\mid(D-x)\).  If the second defect is empty, only the first line
of (1.3) can be dominated, giving items 1 or 2.  If it is the singleton
\(\{v\}\), the additional possibility is the second line of (1.3),
which is item 3.  Taking complements gives (3.1) and the size claims.

## 4. Two-cuts have exactly two components

### Lemma 4.1 (low-defect form of a negative split)

Suppose \(|d_X|,|d_Y|\le2\).  If the split is negative, then both
defects are nonempty and, after possibly reversing them, either

\[
 \{v\}\subseteq d_X,\qquad N_F(v)=d_Y                \tag{4.1}
\]

for some \(v\in W\), or

\[
 d_X=M_i,\qquad d_Y=M_j,\qquad i\ne j.               \tag{4.2}
\]

This is immediate from (1.3), since the empty-coordinate patterns there
have their other coordinate of order at least three.

### Theorem 4.2

If \(Z=\{z_1,z_2\}\) is a two-cut of a full shore \(D\), then \(D-Z\)
has exactly two components.

### Proof

Two-connectivity implies that every component \(C\) of \(D-Z\) meets
both \(z_1,z_2\).  Moreover,

\[
 |N_S(C)|+|Z|\ge7,\qquad\text{so}\qquad
 |S-N_S(C)|\le2.                                    \tag{4.3}
\]

Suppose there are at least three components \(C_1,C_2,C_3\).  Fold the
two cutvertices and all further components into a fourth piece \(R\).
Write

\[
 d_i=S-N_S(C_i)\quad(i=1,2,3),\qquad
 d_0=S-N_S(R).
\]

For every \(i\), the split \(C_i\mid(D-C_i)\) is connected, and its
defect pair is

\[
 \left(d_i,\ e_i\right),\qquad
 e_i=d_j\cap d_k\cap d_0,\quad\{i,j,k\}=\{1,2,3\}.   \tag{4.4}
\]

Both coordinates have order at most two.  Lemma 4.1 says in particular
that every \(e_i\) is nonempty.  Hence the three sets \(d_1,d_2,d_3\),
each of order at most two, are pairwise intersecting.

Suppose they have a common intersection \(K\ne\varnothing\).  If
\(|K|=2\), then all three sets equal \(K\), and the nonemptiness of any
\(e_i\) gives \(d_0\cap K\ne\varnothing\).  If \(K=\{w\}\), then at
least one pair intersection is exactly \(\{w\}\): otherwise the
order-two bound would make all three sets the same two-element set.
The corresponding \(e_i\) then forces \(w\in d_0\).  In either case
this contradicts fullness of \(D\), which says

\[
 d_0\cap d_1\cap d_2\cap d_3=\varnothing.            \tag{4.5}
\]

Thus three pairwise-intersecting sets of order at most two have the
form

\[
 d_1=\{y,z\},\qquad d_2=\{x,z\},\qquad
 d_3=\{x,y\}                                        \tag{4.6}
\]

for distinct \(x,y,z\).  Equation (4.4) gives
\(e_1=\{x\},e_2=\{y\},e_3=\{z\}\).  Lemma 4.1 now forces

\[
 \{y,z\}=N_F(x),\qquad
 \{x,z\}=N_F(y),\qquad
 \{x,y\}=N_F(z).                                    \tag{4.7}
\]

Thus \(x,y,z\) induce a triangle in \(F\), contrary to \(F=C_6\).
Therefore a two-cut has only two components.

### Corollary 4.3 (the surviving two-cut lock)

For either component \(C\) of \(D-Z\), the defect pair of
\(C\mid(D-C)\) is locked into (4.1) or (4.2).  Thus every surviving
two-cut has exactly two components and exposes either a
cycle-neighbour singleton/pair defect or two distinct antipodal-pair
defects.  The coarse contact atlas alone does not eliminate these
two-component locks; portal-edge and coloring-transition information is
the next required input.
