# Oriented portal locks and the forced nonlaminar web in the (C_6) core

**Audit/supersession notice.**  Lemma 1.1 below is valid.  The proposed
global ordering in Sections 2--4 is not valid for arbitrary portal
multiplicity: each rail lock orders selected representatives, while
different locks may select different vertices of the same portal class.
Consequently the former Lemma 3.1 and Corollary 3.2 are retracted as
general statements.  The sound replacement is the compatible-opposite-
crossing and exact ownership theorem in
hadwiger_c6_opposite_crossing_dichotomy.md.

## 1. A stronger escape repair

Retain the representative notation of
`hadwiger_c6_crossing_portal_lock.md`: the missing cycle is

\[
0,4,2,3,1,5,0,
\]

(X,Y) are adjacent disjoint connected crossing pieces with

\[
 X\text{ touching }0,5,qquad Y\text{ touching }1,3,
\]

and (H) is the contracted opposite full shore.

### Lemma 1.1 (outer-bridge escape)

Suppose there is a connected set (R\subseteq D-(X\cup Y)) which

* is adjacent to both (X) and (Y); and
* touches both outward boundary vertices (2) and (4).

Then (G) contains a (K_7)-minor.

#### Proof

Use the seven bags

\[
 \{0\},\quad\{1\},\quad\{2\},\quad\{6\},\quad H,
 \quad X\cup\{4,5\},\quad R\cup Y\cup\{3\}.       \tag{1.1}
\]

The sixth bag is connected because (X) touches (5) and (45) is a
boundary edge.  The seventh is connected because (R) is adjacent to
(Y), and (Y) touches (3).  The last two bags are adjacent through an
(R)-(X) edge.  The contacts of (R) at (2,4), the crossing contacts,
the fullness of (H), and the boundary edges not listed in the missing
cycle verify every remaining adjacency. \(\square\)

This strictly strengthens the one-contact repairs: it allows the two
outward portals to live in a third bridge rather than in the prescribed
crossing pieces.

## 2. Selected-representative order of one tight lock

Write the missing cycle abstractly as

\[
C=(c_0,c_1,c_2,c_3,c_4,c_5).
\]

Frame (i) omits (c_i,c_{i+1}), and its crossing pieces connect

\[
 X_i:c_{i-2}\leftrightarrow c_{i-1},qquad
 Y_i:c_{i+2}\leftrightarrow c_{i+3}.               \tag{2.1}
\]

The two outward repairs are an (X_i)-contact at (c_i) and a
(Y_i)-contact at (c_{i+1}).  In a (K_7)-minor-free graph the mutual
separator lock says

\[
 Y_i\text{ separates }X_i\text{ from all }c_i\text{-portals},
 \qquad
 X_i\text{ separates }Y_i\text{ from all }c_{i+1}\text{-portals}. \tag{2.2}
\]

Call the selected lock **tight** if it also has no outer bridge as in
Lemma 1.1.
After selecting the four crossing portals and one portal in each outward
class, a tight lock has the chain order

\[
 c_{i+1} < \{c_{i-2},c_{i-1}\} <
 \{c_{i+2},c_{i+3}\} < c_i.                     \tag{2.3}
\]

Here the notation records only the order of the selected representatives
in this one rail system.  A bridge which reverses this selected order
gives a one-contact repair or an outer-bridge escape.  It is not a linear
order on all of \(D\), and it does not order an entire portal class when
that class has several representatives.

## 3. Retracted global-order extrapolation

### Retracted Claim 3.1 (valid only under coherent singleton portals)

If every boundary class has one common representative used by every lock,
then no common acyclic precedence relation on those six representatives
can extend the chain orders of two distinct tight frame locks.

#### Proof

In the chain for frame (i), the class (c_i) is last, so in particular

\[
 c_j<c_i\qquad(j\ne i).                             \tag{3.1}
\]

In the chain for a distinct frame (j), the class (c_j) is last, giving

\[
 c_i<c_j.                                           \tag{3.2}
\]

Equations (3.1)--(3.2) are a directed two-cycle. \(\square\)

The calculation is correct under the added coherent-representative
hypothesis.  That hypothesis is not forced in an arbitrary full shore.
With portal multiplicity, two locks may use different representatives of
\(c_i\) and \(c_j\), so the displayed symbolic two-cycle need not be a
two-cycle between graph separations.

### Retracted Corollary 3.2

It remains true that one shore supplies several frame crossings.  It does
not follow from the selected orders alone that their graph separations
cross.  A valid replacement needs either coherent portal representatives
or a label-preserving theorem comparing the actual separator sets.  The
opposite-crossing ownership theorem cited in the audit notice is the
currently proved multiframe statement.

## 4. Selected-representative experiment (not an arbitrary-shore theorem)

The script `c6_multiframe_portal_probe.py` tests the selected-portal model
on all connected graphs with six portal representatives.  There is exactly
one graph which supports all six frame crossings while admitting none of
the outward absorptions: the triangular prism

\[
 012,\quad345,\quad03,14,25.                        \tag{4.1}
\]

It is the exception in the selected-single-representative model.  Adding
one extra portal incidence unlocks a frame unless the incidence is along
one of the matching pairs (03,14,25).  Even after all such matching
incidences and the universal boundary contact are allowed, every vertex of
the six-vertex prism skeleton has total degree at most six; hence the exact
skeleton cannot occur in a minimum-degree-seven counterexample.

The computation motivates, but does not prove for arbitrary shores, the
following possible theorem:

> **Crossing-lock web lemma.** Two nonlaminar tight rail locks in a
> two-connected full shore either have an outer-bridge escape, or the shore
> admits a prism-web decomposition in which every nontrivial substituted
> piece is separated from the opposite shore by at most six vertices.

If proved with full portal multiplicity, the escape outcome would be
Lemma 1.1.  Seven-connectivity would eliminate every
nontrivial substituted piece in the web outcome, leaving the degree-at-most-
six prism skeleton (4.1).  Thus such a lemma would close the sole six-edge
contact core.  Unlike an arbitrary rooted-minor assertion, it is a
two-rail, six-portal splitter statement with an explicitly identified
sharp skeleton.

The missing step is to prove this crossing-lock web lemma for arbitrary
portal multiplicity.  The finite prism calculation shows both why a purely
acyclic argument is insufficient and exactly what the nonlaminar exception
must look like.
