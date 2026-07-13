# Degree-eight triple locks: the exact crossing split and its web residual

## 1. Setting

Use the pure-Moser labels

\[
 E(M)=\{01,02,03,04,12,16,26,34,35,45,56\},
\]

with repeated pair \(a b=13\), unique roots

\[
 U=\{0,2,4,5,6\},\qquad
 \overline{M[U]}=05,52,24,46,60,
\]

and order-six adhesion \(S=U\dot\cup\{w\}\).  Let \(D\) be the
all-crossless shore on the \(a=1\) side, and let \(D'\) be the opposite
full shore on the \(b=3\) side.

Suppose disk curvature gives a degree-eight triple-lock vertex \(x\in D\)
for the missing pair \(05\).  Thus

\[
 N_L(x)=\{0,4,5,w,1\},\qquad P_4(D)=\{x\},
 \qquad d_D(x)=3.
 \tag{1.1}
\]

Put \(B=D-x\).  Since \(D\) is three-connected, \(B\) is connected.
The relative order-seven cut inequality applied to \(B\), together with
\(P_4(D)=\{x\}\), gives

\[
 N_L(B)=L-\{4\}=\{0,1,2,5,6,w\}.
\tag{1.2}
\]

The opposite shore is full to

\[
 L'=U\dot\cup\{w,3\}.
\tag{1.3}
\]

## 2. A necessary correction to the equality-trace route

Let \(p,q,h\) be the three shore neighbours of \(x\), with \(p,q\)
the two facial neighbours.  As in the curvature note, \(pq\notin E(G)\),
and the singleton shield makes \(\{p,q,4\}\) independent.  Dirac's bound
is tight:

\[
 \alpha(N(x))=3.
\]

Contracting the star on \(\{x,p,q,4\}\) therefore gives a six-colouring
of \(G-x\) in which \(p,q,4\) have one common colour and

\[
 h,0,5,w,1
\]

receive the other five colours bijectively.  Rolek--Song supplies a
bichromatic \(0\)-\(5\) path internally outside \(N[x]\).  The original
apex \(v\) cannot lie on that path, because it is adjacent to both ends
and hence can receive neither of their colours.

This does **not** confine the path to an open shore.  The two remaining
roots \(2,6\) are outside \(N[x]\), and the fixed Moser path

\[
 0-2-6-5                                             \tag{2.1}
\]

is internally outside \(N[x]\).  It can be bichromatic in a colouring
having

\[
 c(0)=c(6),\qquad c(5)=c(2).
\]

This is locally compatible with the entire exact trace: for example use
distinct colours

\[
 c(p)=c(q)=c(4)=0,quad c(0)=c(6)=1,quad
 c(5)=c(2)=2,quad c(1)=c(3)=3,quad c(h)=4,quad c(w)=5.
\tag{2.2}
\]

All displayed Moser edges are proper.  Thus Rolek--Song alone gives no
new routing information in this residual.  The analogous obstruction for
the \(60\) lock is the path \(6-5-4-0\).  Any use of the equality trace
must first prove that the Kempe path avoids the other two roots.

## 3. Enlarging an opposite crossing to a full split

Suppose one Moser frame is crossed in \(D'\).  Its two disjoint connected
supports can be enlarged to adjacent connected sets \(E,F\) which
partition \(D'\).  Indeed, first split a shortest connector between the
two supports to make them adjacent.  Every component left after deleting
them has a neighbour in their union; assign the whole component to one
side it meets.  Connectivity, disjointness and the prescribed endpoint
contacts are preserved.

Consequently

\[
 N_{L'}(E)\cup N_{L'}(F)=L'.                       \tag{3.1}
\]

### Theorem 3.1 (complete full-split atlas for the \(05\) lock)

If a frame is crossed in \(D'\), then either \(G\) has a \(K_7\)-minor,
or, after interchanging the two carriers if necessary,

\[
\begin{aligned}
 &F\text{ supports }05,\qquad
 N_{L'}(F)\subseteq\{0,3,4,5\},\\
 &N_{L'}(E)\subseteq L'-\{3\},\\
 &\{2,4,6,w\}\subseteq N_{L'}(E),qquad
 \{0,3,5\}\subseteq N_{L'}(F).
\end{aligned}                                      \tag{3.2}
\]

In particular \(F\) misses each of \(2,6,w\), while \(E\) misses
terminal \(3\).  The only possible crossed frames in (3.2) are

\[
 (05,24)\quad\hbox{and}\quad(05,46).               \tag{3.3}
\]

#### Verification

Contract \(B,E,F\) to helper vertices and retain \(x,w\) and the seven
Moser vertices.  Every one of the five frames leaves three labels of
\(L'\) not prescribed by its two supported edges.  Each such label lies
in \(E\) only, \(F\) only, or both, giving exactly \(3^3=27\) full-contact
states per frame.  For the two states which remain negative, all
\(2^4\) optional cross-contacts at the four frame endpoints are then
checked.  Monotonicity makes this exhaustive.

The result is:

* the frames \((25,46)\), \((06,24)\), and \((06,25)\) are always
  positive;
* for \((05,24)\), positivity fails only below the maximal rows
  \(N(E)=L'-\{3\}\), \(N(F)=\{0,3,4,5\}\);
* the same maximal pair is the only failure for \((05,46)\).

For every positive state the verifier enumerates all partitions of six
or seven Moser vertices into six nonempty branch bags and all assignments
of \(w,x,B,E,F\).  It checks connectivity and all fifteen bag
adjacencies directly.  The replay is
`moser_triple_lock_crossing_fullness_probe.py`; the underlying model
checker is `moser_triple_lock_opposite_crossing_probe.py`.

Two basic certificates, which also make the positive mechanism
transparent, are as follows.  Here a symbol such as \(E_{46}\) means a
connected carrier meeting both displayed portals.

If the crossing is \((25,46)\), use the six bags

\[
 \{0,w\}\cup B,\quad \{1,x\},\quad
 \{2\}\cup F_{25},\quad \{4\}\cup E_{46},
 \quad\{5\},\quad\{6\}.                            \tag{3.4}
\]

If it is \((06,24)\), use

\[
 \{0\},\quad\{1,w,x\},\quad\{2\},\quad
 \{4\}\cup E_{24},\quad\{5\}\cup B,
 \quad\{6\}\cup F_{06}.                           \tag{3.5}
\]

The Moser edges, (1.1)--(1.2), and the edge \(EF\) verify all pairwise
adjacencies.  Every bag contains a vertex of \(N(v)\), so adjoining
\(\{v\}\) gives \(K_7\).  The remaining rows use rotations of these
two assignments or the extra full-shore contacts; the verifier prints the
actual six bags for each state.

## 4. The exact Two-Paths target inside the unique residual

Assume (3.2).  Make an auxiliary graph \(A_E\) from \(G[E]\) by adding
four independent terminals

\[
 t_F,t_4,t_2,t_6,
\]

adjacent respectively to

\[
 N_E(F),\quad N_E(4),\quad N_E(2),\quad N_E(6),
\]

and order them as

\[
 (t_F,t_4,t_2,t_6).                                \tag{4.1}
\]

### Lemma 4.1 (cross or port-labelled web)

Either \(G\) contains a \(K_7\)-minor, or \(A_E\) embeds in a
four-web with frame (4.1).  Moreover, in the latter case every nonempty
inserted clique containing an actual vertex of \(E\) lies behind a
facial triangle incident with \(t_F\).

### Proof

A crossing of (4.1) consists of disjoint connected carriers \(P,Q\),
where \(P\) meets \(F\) and root \(2\), and \(Q\) meets roots \(4,6\).
If necessary split a shortest connector in connected \(E\) to make
\(P,Q\) adjacent.  Absorb \(P\) into \(F\).  Formula (3.4), with
\(F_{25}\) replaced by the connected set \(F\cup P\) and \(E_{46}\)
replaced by \(Q\), is still a \(K_6\)-model meeting \(N(v)\).  Hence a
cross gives \(K_7\).

If there is no cross, the generalized Two Paths Theorem gives a
same-vertex four-web completion with frame (4.1).

Let \(X\subseteq E\) be a nonempty set of actual vertices in an inserted
clique behind a facial triangle \(T\) not containing \(t_F\).  Since
\(A_E\) is an edge-subgraph of the web, no vertex of \(X\) has a neighbour
in \(F\); otherwise it is adjacent to \(t_F\), whereas clique vertices
behind \(T\) have neighbours outside their clique only in \(T\).
Map any of \(t_2,t_4,t_6\) in \(T\) to its boundary label, and retain
the shore vertices of \(T\).  The only further possible external
neighbours of \(X\) are the omitted labels \(0,5,w\).  Thus \(X\) is
separated from the opposite shore by at most

\[
 |T|+|\{0,5,w\}|\le6
\]

vertices, contrary to seven-connectivity.  Therefore every surviving
inserted clique is incident with \(t_F\).  \(\square\)

The web alternative is substantially narrower than the original
degree-eight cell: all nonplanar clique pockets are concentrated at the
single interface terminal, and the three other portal classes occur on
the web frame in the fixed alternating order.  Closing it requires a
port-labelled peel at \(t_F\): either absorb a \(2\)-portal into \(F\)
while retaining a connected \(4,6\)-carrier, or turn the failure into a
six-cut.  Boundary-state saturation alone has not yet supplied that peel.

### Lemma 4.2 (pocket peel, exact cut, or surplus ear)

Let \(K\) be an inserted clique behind a facial triangle containing
\(t_F\), and let \(X\) be a nonempty component of the graph induced by
the actual vertices of \(K\).  Then

\[
 |N_F(X)|\ge2.                                     \tag{4.2}
\]

Moreover:

1. if \(X\) meets portal \(2\) and some component of \(E-X\) meets
   both portals \(4,6\), then \(G\) has a \(K_7\)-minor;
2. if \(|N_F(X)|=2\), then \(X\) lies behind an exact seven-cut; and
3. if \(|N_F(X)|\ge3\), then \(X\) supplies an \(F\)-ear with at least
   three available attachment vertices.

Consequently, in a \(K_7\)-minor-free graph, every pocket component
which meets portal \(2\) separates the \(4\)- and \(6\)-portal classes:
no component of \(E-X\) meets both.

### Proof

Write the facial triangle as \(\{t_F,p,q\}\).  Replace an artificial
label terminal among \(p,q\) by its actual label and retain an actual
\(E\)-vertex unchanged; call the resulting set \(R\), so \(|R|\le2\).
The unique maximal bad row has no \(E\)-contact at terminal \(3\).  All
original neighbours of \(X\), other than its neighbours in \(F\), are
therefore contained in

\[
 R\cup\{0,5,w\}.
\]

Indeed, the web contains every original edge of the auxiliary society;
an \(E\)-edge leaving the pocket can end only at \(p,q\), and an edge to
one of the selected labels \(2,4,6\) is represented by the corresponding
frame-terminal edge.  Thus

\[
 N_G(X)\subseteq R\cup\{0,5,w\}\cup N_F(X).       \tag{4.3}
\]

This set separates \(X\) from the all-crossless opposite shore.
Seven-connectivity and \(|R|\le2\) prove (4.2).

Suppose next that \(X\) meets portal \(2\), and let \(C\) be a component
of \(E-X\) meeting both portals \(4,6\).  Put

\[
 F^*=F\cup X\cup\!
      \bigcup\{C':C'\text{ is a component of }E-X,\ C'\ne C\}.
\tag{4.4}
\]

The set \(F^*\) is connected.  The edge from \(X\) to \(F\) joins its
first two displayed parts.  Every component of \(E-X\) has an edge to
\(X\): otherwise it has no edge to another component of \(E-X\) and
would be disconnected from \(X\) in connected \(E\).  Equivalently,
contract the components of \(E-X\) and use a spanning tree rooted at the
contracted image of \(X\); assign every branch except the reserved
\(C\)-branch to the \(F^*\)-side.  This also shows that \(F^*\) and
\(C\) are adjacent.

Now \(F^*\) meets \(0,3,5\) through the old \(F\) and meets \(2\)
through \(X\), while \(C\) meets \(4,6\).  Replace the two opposite
carriers in (3.4) by \(F^*\) and \(C\).  The same six bags give an
\(N(v)\)-meeting \(K_6\), and \(\{v\}\) gives \(K_7\).  This proves
item 1 and the final assertion.

If \(|N_F(X)|=2\), the right side of (4.3) has order at most seven.
It is a separator and the graph is seven-connected, so equality holds:
\(|R|=2\), all three effective omitted labels occur, and

\[
 N_G(X)=R\dot\cup\{0,5,w\}\dot\cup N_F(X)
\]

is an exact seven-cut.  This is item 2.  Finally, if
\(|N_F(X)|\ge3\), choose two distinct attachments in \(F\); a path
through connected \(X\) between them is an \(F\)-ear, with a third
attachment available for a subsequent exchange.  This proves item 3.
\(\square\)

Lemma 4.2 is the exact current stopping point.  Two attachments recurse
through a new minimum adhesion; three attachments give genuine surplus,
but do not by themselves preserve the \(4,6\)-carrier needed after the
\(2\)-portal is absorbed.  Treating that surplus as an automatic peel
would reintroduce the portal-placement gap.  This limitation is already
visible in the smallest quotient.  Let one pocket vertex \(y\) meet
portal \(2\), the piece \(F\), and two distinct residual carriers
\(E_4,E_6\) meeting only the displayed portals \(4,6\).  Even if the
edge \(yF\) represents arbitrarily many physical attachments, the
resulting quotient has no \(N(v)\)-meeting \(K_6\).  The exhaustive
23,059,204-assignment replay is
`moser_triple05_separated_pocket_probe.py`.  Thus distinct attachment
placement or a minor-transition state, rather than attachment cardinality,
is indispensable.

## 5. The \(60\) residual

For the degree-eight triple \(\{6,0,2\}\), the minimal crossing atlas is
weaker.  An opposite crossing of \((25,46)\) already closes, with bags

\[
 \{0,3,w,x\},\quad\{1\}\cup B,\quad
 \{2\}\cup F_{25},\quad\{4\}\cup E_{46},
 \quad\{5\},\quad\{6\}.                            \tag{5.1}
\]

The other four minimal frames need extra distributed contacts; their
full-split atlas has several surviving rows.  Thus Theorem 3.1 is a real
asymmetric gain for the \(05\) orbit, not a claimed closure of both
degree-eight locks.
