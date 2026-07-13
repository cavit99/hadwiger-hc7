# The double-Moser edge witness and the two-carrier capacity state

## 1. Setting

Let (G) be a hypothetical proper-minor-minimal non-six-colourable,
(K_7)-minor-free graph.  Use the cut-irreducible singleton re-root from
`hadwiger_double_moser_two_component_closure.md`.  Thus (G) is
seven-connected, (u,v) are adjacent vertices of degree seven, and

\[
 X=\{x_1,x_2,x_3,x_4\},\qquad
 A=\{a,b\},\qquad P=\{p,q\},
\]

\[
 N(u)=\{v\}\mathbin{\dot\cup}X\mathbin{\dot\cup}P,
 \qquad
 N(v)=\{u\}\mathbin{\dot\cup}X\mathbin{\dot\cup}A.       \tag{1.1}
\]

Put (H_1=\{x_1,x_2\}) and (H_2=\{x_3,x_4\}).  Besides the two
stars at (u,v), the fixed double-Moser edges are

\[
 x_1x_2, x_3x_4, ab, pq,
\]

\[
 ax_1,ax_2,bx_3,bx_4,
 \qquad qx_1,qx_2,px_3,px_4.                    \tag{1.2}
\]

The sole exterior of (N[u]) is (C=A\mathbin{\dot\cup}R), where
(R=C-A) is connected.  Unless a new exact seven-cut has already been
found,

\[
              N_G(R)=A\cup X\cup P.             \tag{1.3}
\]

The purpose of this note is threefold.

1. It gives the complete, exact trace of every edge-deletion colouring of
   (G-uv), including the exterior paths which that colouring really
   supplies.
2. It proves that, unless an exact seven-cut occurs, the one body (R)
   always has a genuine two-carrier split joining (A) to (P).
3. It gives an explicit (K_7)-certificate as soon as those two carriers
   have cross-capacities ((2,1)) or ((1,2)).  This reduces the geometric
   residue to six low-capacity states.

The last six states are not eliminated here.

## 2. What edge criticality forces

### Lemma 2.1 (five Kempe chains)

Let (c) be any proper six-colouring of (G-uv).  Then

1. (c(u)=c(v));
2. each of (u,v) has a neighbour of every other colour; and
3. for every colour (gamma\ne c(u)), the vertices (u,v) lie in the
   same \(\{c(u),\gamma\}\)-component of (G-uv).

#### Proof

If the ends had different colours, restoring (uv) would six-colour
(G).  If, say, (u) missed a colour different from (c(v)), recolouring
(u) with it and restoring (uv) would again colour (G).  Finally, if
(u,v) lay in different bichromatic components, switch the component
containing (u).  Their colours become different, so (uv) can again be
restored.  Each conclusion contradicts the choice of (G).  \(\square\)

Relabel colours so that (c(u)=c(v)=0), and let

\[
                         r=|c(X)|.
\]

### Theorem 2.2 (the exact (r=3/r=4) census)

Exactly one of the following occurs.

1. **Three-colour core.**  We have (r=3).  One colour is repeated on a
   missing cross-edge (x_ix_j), with one end in each of (H_1,H_2).
   The two edges (ab) and (pq) both use, bijectively, the two colours
   absent from (X).
2. **Rainbow core.**  We have (r=4).  There is a unique nonzero colour
   (	au) absent from (X).  Each of (ab,pq) has one end of colour
   (	au), while its other end repeats one colour on (X).  If (a)
   repeats a root colour, that root lies in (H_2); if (b) repeats one,
   it lies in (H_1).  The analogous statement holds for (q,p),
   respectively.

In either case, the trace on each of (N(u)) and (N(v)) uses all six
colours and has exactly one independent pair as its nonsingleton block.

#### Proof

At (u), the six neighbours different from (v) are (X\cup P).  They
must contain all five nonzero colours, and the ends of (pq) have distinct
colours.  Hence

\[
                         |c(X)\cup c(P)|=5,
\]

so (r\ge3).  Since (|X|=4), (r\le4).  The same equation holds with
(A) in place of (P).

If (r=3), both exclusive edges must use exactly the two colours absent
from (X).  A proper three-colouring of (2K_2=G[X]) repeats one colour
on a cross nonedge and has two singleton colours.

If (r=4), each exclusive edge contributes the unique fifth colour and
repeats one root colour.  Properness locates the repeated mate: (a) is
adjacent to (H_1), so a root of its colour must be in (H_2); the other
three assertions follow from (1.2).  Adding the colour-zero neighbour
(v), or (u), proves the final trace assertion.  \(\square\)

## 3. The chains localize inside the one body

### Lemma 3.1 (exclusive-colour localization)

Let (gamma) be a nonzero colour absent from (X).  There is a path

\[
              z_P\;R\;z_A                         \tag{3.1}
\]

from the unique (gamma)-coloured vertex (z_P\in P) to the unique
(gamma)-coloured vertex (z_A\in A), whose internal vertices lie in
(R).  More precisely, (3.1) is obtained by deleting (u,v) from a
shortest (0,gamma)-coloured (u)-(v) path.

For the two absent colours in the (r=3) case, the resulting paths pair
the two vertices of (P) bijectively with the two vertices of (A).  Two
such paths can meet only at vertices of colour zero.

#### Proof

Lemma 2.1 supplies a (0,gamma)-path from (u) to (v).  Choose it
shortest.  Its first vertex after (u) is the unique (gamma)-coloured
member of (P), and its last vertex before (v) is the unique such member
of (A).  No vertex of (X) has colour (0) or (gamma), and the other
vertices of (A\cup P) have neither colour.  All remaining internal
vertices therefore lie outside both displayed closed neighbourhoods,
hence in (R).  Paths for distinct absent colours have disjoint nonzero
colour sets, so an intersection can only have colour zero.  \(\square\)

The (r=3) trace has one further safe exchange.

### Lemma 3.2 (rainbowize or obtain two core carriers)

Suppose (r=3), and let (x,y\in X) be the equal-coloured cross pair,
of colour (gamma).  For either colour (delta) absent from (X), one
of the following holds.

1. A global (gamma,delta)-Kempe switch in (G-uv) produces another
   edge-deletion colouring with (r=4); or
2. there is a (gamma,delta)-coloured path joining (x) to (y).

Consequently, if no switch produces the rainbow case, both absent colours
give actual bichromatic (x)-(y) carriers.

#### Proof

If (x,y) lie in different (gamma,delta)-components, switch the one
containing (x).  No other root of (X) lies in it: (x,y) are the only
(gamma)-coloured roots and no root has colour (delta).  Thus (X)
gains one colour.  The colours of (u,v) are unchanged because neither
switched colour is zero.  If the two roots lie in one component, a shortest
path in it gives outcome 2.  Apply this independently to the two absent
colours.  \(\square\)

Lemma 3.2 is a real Kempe exchange, but Section 6 below shows why the
resulting carriers do not by themselves make a (K_7)-minor.

## 4. A two-carrier split or an exact seven-cut

The following is independent of the colouring and uses the new one-body
topology.

### Theorem 4.1 (two-carrier Menger dichotomy)

In the setting of Section 1, at least one of the following holds.

1. There is an exact seven-cut of (G).
2. The connected exterior (C=A\cup R) has a partition

   \[
                         C=C_a\mathbin{\dot\cup}C_b              \tag{4.1}
   \]

   into connected sets with (a\in C_a), (b\in C_b), such that
   (C_a,C_b) are adjacent and each has a neighbour in (P).  In fact
   the two sides can be chosen to meet distinct vertices of (P).

#### Proof

Work in

\[
                         F=G[A\cup R\cup P].                     \tag{4.2}
\]

Apply the vertex form of Menger's theorem between the two-sets (A) and
(P).  If there are no two vertex-disjoint (A)-(P) paths, there is a
set (Z) of order at most one such that (F-Z) has no (A-Z) to (P-Z)
path.  Then

\[
                         X\cup\{u,v\}\cup Z                     \tag{4.3}
\]

separates the remaining member of (A) from the remaining member of
(P) in (G).  If (Z) is empty this is a cut of order six,
contradicting seven-connectivity.  Hence (|Z|=1), and (4.3) is an exact
seven-cut.

Otherwise choose two disjoint (A)-(P) paths.  Trim each path at its last
vertex of (A) and its first subsequent vertex of (P).  Their (A\cup R)
portions are then disjoint connected sets containing exactly one, and
different, vertices of (A), and they see different vertices of (P).
They are adjacent by the edge (ab).  Contract each of these two sets in the connected graph
(C), choose a spanning tree containing the edge between the two
contracted vertices, and delete that tree edge.  The inverse images of
the two tree components give the connected partition (4.1), preserving
the two (P)-contacts.  \(\square\)

This removes the possibility that the one-body obstruction has no genuine
split at all.  What remains is the distribution of its (X)-portals.

## 5. Three cross-portals already give (K_7)

For a split (4.1), define its two cross-capacities by

\[
 \rho_a=|N_X(C_a)\cap H_2|,
 \qquad
 \rho_b=|N_X(C_b)\cap H_1|.                     \tag{5.1}
\]

The contacts of (a,b) guarantee that (C_a) already sees all of
(H_1), while (C_b) already sees all of (H_2).

### Theorem 5.1 (three-cross portal certificate)

Suppose both sides of (4.1) have a neighbour in (P).  If

\[
                    (\rho_a,\rho_b)\ge(2,1)
       \quad\hbox{or}\quad
                    (\rho_a,\rho_b)\ge(1,2),                    \tag{5.2}
\]

then (G) contains a (K_7)-minor.

#### Proof

Assume first that (ho_a=2) and (ho_b\ge1).  By symmetry inside
(H_1), let (C_b) see (x_2).  The seven branch sets are

\[
 C_a,quad C_b,quad \{p,q\},quad \{x_3\},quad \{x_4\},
 \quad \{v,x_1\},quad \{u,x_2\}.             \tag{5.3}
\]

They are connected and disjoint.  The first two are adjacent through
(ab).  Each sees ({p,q}) by hypothesis.  The set (C_a) sees
(x_3,x_4) by (ho_a=2), sees ({v,x_1}) through (a), and sees
({u,x_2}) through (ax_2).  The set (C_b) sees (x_3,x_4) through
(b), sees ({v,x_1}) through (bv), and sees ({u,x_2}) through
its cross-contact at (x_2).

The five boundary bags in (5.3) are pairwise adjacent: use (pq), the
two triangles (q x_1x_2) and (p x_3x_4), the stars at (u,v), and
the edges (uv,x_1x_2,x_3x_4).  Thus (5.3) is a (K_7)-model.

If (ho_b=2) and (ho_a\ge1), interchange the literal halves.  With
(C_a) seeing (x_4), use

\[
 C_a,quad C_b,quad \{p,q\},quad \{x_1\},quad \{x_2\},
 \quad \{v,x_3\},quad \{u,x_4\}.             \tag{5.4}
\]

The same check proves the claim.  \(\square\)

This strictly weakens the earlier cross-saturated endpoint, which asked
both carriers to see all four roots.  Only three cross incidences, with
one row full, are needed.

### Corollary 5.2 (the exact low-capacity residue)

Choose a split from Theorem 4.1 which is maximal in its pair of contact
rows.  Unless a (K_7)-minor or exact seven-cut has already occurred, its
cross-capacity state belongs to

\[
 \boxed{(0,0),(0,1),(0,2),(1,0),(1,1),(2,0).}                   \tag{5.5}
\]

Thus the remaining web exchange has six capacity states, not an
unbounded collection of path patterns.  The maximal-bad portal peel in
`hadwiger_maximal_bad_split_portal_peel.md` additionally says that every
movable vertex which would increase one of these capacities is either a
cutvertex of its side or the unique portal of a boundary label.

## 6. Why the five Kempe chains alone cannot finish

There is a sharp adversarial obstruction to any proof which contracts the
chains to mere exclusive-to-exclusive contacts.

Let (Q_\times) be the ten-vertex double-Moser core on

\[
                 \{u,v\}\cup X\cup A\cup P
\]

and add all four edges between (A) and (P).  It has the following
tree-decomposition:

\[
\begin{array}{c|l}
B_0&\{a,b,p,q,u,v\}\\
B_1&\{x_4,b,p,u,v\}\\
B_2&\{x_3,x_4,b,p,u,v\}\\
B_3&\{x_2,a,q,u,v\}\\
B_4&\{x_1,x_2,a,q,u,v\},
\end{array}                                                     \tag{6.1}
\]

on the tree (B_2-B_1-B_0-B_3-B_4).  Every bag has order at most six,
so (\operatorname{tw}(Q_\times)\le5).  In particular it has no
(K_7)-minor.  Replacing any of the four cross-edges by internally
disjoint paths merely subdivides edges and preserves this conclusion.

Even a dirty common hub does not help.  Add a vertex (h) adjacent to
all four vertices of (A\cup P).  Attach the additional bag

\[
                         \{a,b,p,q,h\}                           \tag{6.2}
\]

to (B_0); (6.1)--(6.2) is still a width-five tree-decomposition.

These obstructions realize the geometry of both trace types.  For
example, in the rainbow case colour

\[
 c(u)=c(v)=c(h)=0,quad
 c(x_i)=i,quad c(b)=1, c(a)=5, c(p)=2, c(q)=5,
\]

and retain only the path (a-h-q).  The five (u)-(v) bichromatic
chains are the four length-two paths through (X) and
(u-q-h-a-v).  In the three-colour case use

\[
 c(x_1)=c(x_3)=1, c(x_2)=2, c(x_4)=3,
 \quad c(a)=c(q)=5, c(b)=c(p)=4,
\]

with either two clean subdivided cross-edges or the common zero-coloured
hub.  This supplies all five required chains but still lies in a
width-five architecture.

The examples are not asserted to satisfy seven-connectivity or
minor-criticality.  Their exact role is to prove that the chain traces,
even with clean disjoint routing or a dirty hub, cannot imply a
(K_7)-minor without using how internal body vertices meet (X).

## 7. Net result and exact remaining exchange

The singleton double-Moser residue now has the following rigorous form.

1. Every edge-deletion witness is in the (r=3/r=4) normal form of
   Theorem 2.2 and supplies the localized carriers of Lemma 3.1.
2. Independently of that witness, the one eight-interface body has two
   disjoint (A)-to-(P) carriers, or it exposes an exact seven-cut
   (Theorem 4.1).
3. Those carriers give a (K_7)-minor as soon as their cross-capacity
   state dominates ((2,1)) or ((1,2)) (Theorem 5.1).
4. Pure exclusive-to-exclusive routing cannot eliminate the six remaining
   states (Section 6).

Accordingly, the exact unproved statement is now the following
capacity-state exchange, inside one connected body rather than across an
enumerated collection of shores.

> **Double-Moser capacity exchange.**  A maximal connected split of the
> cut-irreducible body cannot have one of the six states (5.5): either a
> portal-essential frontier can be exchanged to increase a cross-capacity,
> or its cutvertices and unique portal charges form an exact seven-cut.

This is precisely where a two-path web or a portal-essential uncrossing
theorem is needed.  Proving it would close the singleton crossed-frame
double-Moser cell.  Nothing above claims that final exchange.
