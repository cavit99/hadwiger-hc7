# The four-colour reserved-connector gate

## 1. Setting

Use the notation and the audited conclusions of
`hadwiger_palette_deletion_rooted_core.md`.  Thus (G) is a
seven-connected, (K_7)-minor-free, minor-minimal non-six-colourable
graph, (v) is a degree-seven vertex with pure-Moser neighbourhood,
(H=G-v), and an exact (05)-trace gives

\[
 A=c^{-1}(c(0))=c^{-1}(c(5)),\qquad
 B=c^{-1}(c(6)),\qquad J=H-(A\cup B).
\]

Put (X=\{1,2,3,4\}).  The set (X) is four-saturating in the
four-colourable graph (J).  Let (K_0,K_{56}) be the distinct,
anticomplete components of (H[A\cup B]) containing (0) and
\(\{5,6\}), respectively.  Both gate components are adjacent to every
root in (X): vertex (0) sees all four roots, while (6) sees
\(1,2\) and (5) sees (3,4).

The purpose of this note is to replace an arbitrary reserved rooted
(K_4) problem by two disjoint, explicitly typed Kempe blockers.  The
Kempe conclusion below is deliberately stated at its sharp strength:
each connector must cut at least one support, not two.

## 2. Two clean gate connectors

### Lemma 2.1 (two root-avoiding connectors)

There are two (K_0)-(K_{56}) paths (P,Q) such that

1. their interiors are vertex-disjoint;
2. neither interior meets (X); and
3. after trimming, neither interior meets (K_0\cup K_{56}).

#### Proof

The graph (H) is six-connected: deleting (v) from the
seven-connected graph (G) lowers vertex connectivity by at most one.
Choose (a\in K_0) and (b\in K_{56}).  By Menger's theorem there are
six internally vertex-disjoint (a)-(b) paths.  On each path, retain
only the segment from its last vertex in (K_0) to its first subsequent
vertex in (K_{56}).  The resulting gate paths still have pairwise
disjoint interiors and have no internal vertex in the two gate
components.

Only four of these six interiors can meet the four-element set (X).
Choose two of the remaining paths.  \(\square\)

For a clean connector (P), write

\[
                         D(P)=V(P^\circ)\cap V(J).
\]

This set is nonempty.  Indeed, distinct components of the induced
bichromatic graph (H[A\cup B]) cannot be joined by a path whose whole
interior lies in (A\cup B).

### Lemma 2.2 (connector/model alternative)

If (J-D(P)) contains an (X)-rooted (K_4)-model, then (G)
contains a (K_7)-minor.  Consequently, for both connectors supplied by
Lemma 2.1,

\[
                 J-D(P)\text{ has no (X)-rooted (K_4)-minor}.       \tag{2.1}
\]

#### Proof

Let (R_1,R_2,R_3,R_4) be such a model in (J-D(P)).  Absorb into
(K_0) every vertex of (P) except its endpoint in (K_{56}).  This
gives a connected bag (K'_0), disjoint from (K_{56}), and the last
edge of (P) makes these two bags adjacent.  The rooted bags avoid the
vertices of (P) which lie in (J), and all other internal vertices of
(P) lie outside (J), so all six bags are disjoint.

The old gate bag (K_0\subseteq K'_0) is adjacent to every (R_i)
through the boundary edges (0i).  The bag (K_{56}) is adjacent to
(R_1,R_2) through (6), and to (R_3,R_4) through (5).  Hence

\[
                   K'_0,K_{56},R_1,R_2,R_3,R_4
\]

form a (K_6)-model in (H), every bag meeting (N(v)).  Adding the
singleton bag \(\{v\}) gives a (K_7)-model.  \(\square\)

Thus a surviving sole-exterior gate has **two disjoint rooted-(K_4)
transversals** (D(P),D(Q)): every (X)-rooted (K_4)-model in (J)
meets each of them.

## 3. The exact (C_4) Kempe support

In (G[X]) the present edges are (12,34), and its four missing edges
are

\[
                         F=\{13,14,23,24\}\cong C_4.                  \tag{3.1}
\]

For (ij\in F), let (J_{ij}) be the subgraph induced by the two
original colour classes containing (i,j).

### Lemma 3.1 (all four original supports)

For every (ij\in F), the roots (i,j) lie in one component of
(J_{ij}).  Paths for the disjoint pairs (13,24) can be chosen
vertex-disjoint, as can paths for (14,23).

#### Proof

If (i,j) lay in different bichromatic components, switch the two
colours on the component containing (i).  The roots (i,j) would then
have one colour, while the other two roots retain theirs.  This would be
a four-colouring of (J) using at most three colours on (X), contrary
to four-saturation.  The disjointness assertion follows because paths
for vertex-disjoint pairs use disjoint pairs of colour classes.  \(\square\)

For (D\subseteq V(J)-X), define its **surviving support graph**

\[
 F_D=\{ij\in F:i,j\text{ lie in one component of }J_{ij}-D\}.        \tag{3.2}
\]

### Theorem 3.2 (Kempe-support obstruction)

For each clean connector (P) in a (K_7)-minor-free graph,

\[
                         F_{D(P)}\ne F.                             \tag{3.3}
\]

In particular (D(P)) separates at least one of the four bichromatic
root pairs in (3.1).

#### Proof

Suppose instead that (F_{D(P)}=F).  For every edge (ij\in F), choose
an (i)-(j) path in (J_{ij}-D(P)).  The cycle (F=C_4) has property
((\*)) in the Kriesell--Mohr rooted-minor theorem, so these four
bichromatic connections give disjoint rooted bags realizing every edge
of (F).  The two complementary root edges (12,34) already lie in
(G[X]).  Hence the bags form an (X)-rooted (K_4)-model in
(J-D(P)), contradicting Lemma 2.2.  Therefore (3.3) holds.
\(\square\)

This conclusion is stronger than saying that one chosen rooted model meets
the connector: it cuts the fixed four-state Kempe certificate.  It does
**not** imply that two supports are cut.  If exactly one is cut, the other
three Kempe adjacencies together with (12,34) give only a rooted
(K_4^-); property ((\*)) does not repair the fourth edge.  Lemma 2.1
gives two vertex-disjoint sets each cutting at least one support.

### Corollary 3.3 (last-support repair)

If some clean connector (P) leaves all four pairs in (3.1)
bichromatically connected, then (G) contains a (K_7)-minor.  Thus the
geometric target is to repair the last cut support; preserving an arbitrary
preselected rooted (K_4)-model is unnecessary.

## 4. The web/adhesion residue

The preceding theorem identifies the structural residue without further
finite Moser casework.  For each of two disjoint clean connectors (P,Q),
(J-D(P)) and (J-D(Q)) have no rooted (K_4) at (X).  Hence the
Fabila-Monroy--Wood rooted-(K_4) theorem gives the following exact
alternative for each deletion:

* it has vertex connectivity at most three; or
* it is planar and the four roots lie on a common face.

Indeed, if it were four-connected and either nonplanar or had no common
root face, that theorem would give the forbidden rooted model.  Thus the
remaining gate is a pair of **disjoint Kempe-certificate blockers**, each
producing a small internal adhesion or a four-terminal disk web.

This is the correct next exchange target.  A proof must show that two such
blockers cannot coexist with the minor-transition colourings: one blocker
must cross the other's disk web and restore the last missing support in
(3.2) (or directly build the rooted model by another exchange), or a
separator of order at most three must lift, with the two gate colours, to a
colour-gluable adhesion.  Connectivity alone cannot do this, as shown by
(K_2\vee I); the universal trace and one-step minor states must enter at
this final lifting step.
