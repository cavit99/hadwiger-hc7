# Defect stars and the branching number of a bad-split atlas

## 1. Defect relation

Use the quotient family \(\mathcal B_k(J)\) from
hadwiger_defect_atlas_connectivity_principle.md, on boundary \(S\).
Write a contact pair in defect form:

\[
 \mathcal R_k(J)=
 \{(P,Q):P,Q\subseteq S,\ P\cap Q=\varnothing,\
       (S-P,S-Q)\in\mathcal B_k(J)\}.                \tag{1.1}
\]

The disjointness condition is exactly the assertion that the two
contact rows cover \(S\).

For \(p\ge0\), a **\(p\)-defect star of order \(m\)** is a tuple

\[
 (P_0;P_1,\ldots,P_m)
\]

such that

\[
 |P_i|\le p\quad(1\le i\le m),\qquad
 \bigcap_{i=0}^{m}P_i=\varnothing,                  \tag{1.2}
\]

and, putting

\[
 Q_i=P_0\cap\bigcap_{j\ne i}P_j,                    \tag{1.3}
\]

one has

\[
 (P_i,Q_i)\in\mathcal R_k(J)\quad(1\le i\le m).     \tag{1.4}
\]

Let \(\sigma_{k,p}(J)\) be the supremum of the possible orders, with
value \(+\infty\) if stars of arbitrarily large order exist.  Repeated
leaf defects are allowed, as repeated attachment types can occur in
different components of a shore.  This is a label-free invariant of the
bad-split family.  The centre \(P_0\) is not size-bounded: it represents
all portal contacts carried by a separator and by pieces not selected as
star leaves.

## 2. Separator branching theorem

### Theorem 2.1

Let \(G\) be \(\lambda\)-connected and \(K_k\)-minor-free.  Let \(S\)
and two connected full shores \(D,D'\) satisfy the hypotheses of the
quotient-lifting lemma.  Suppose \(W\subseteq D\), \(|W|=w\), and
\(D-W\) has components \(C_1,\ldots,C_m\).  Assume

\[
 D-C_i\text{ is connected for every }i.             \tag{2.1}
\]

Put

\[
 p=|S|-\lambda+w.                                   \tag{2.2}
\]

Then

\[
 m\le\sigma_{k,p}(G[S]).                             \tag{2.3}
\]

### Proof

Define

\[
 P_i=S-N_S(C_i)\quad(1\le i\le m),\qquad
 P_0=S-N_S(W).
\]

The external neighbourhood of \(C_i\) is contained in
\(W\cup N_S(C_i)\) and separates \(C_i\) from \(D'\).  Hence

\[
 |N_S(C_i)|\ge\lambda-w,\qquad |P_i|\le p.           \tag{2.4}
\]

Fullness of \(D\) says that every boundary vertex is seen by \(W\) or
by at least one component, equivalently

\[
 \bigcap_{i=0}^{m}P_i=\varnothing.                  \tag{2.5}
\]

For fixed \(i\), contact sets turn unions into unions, and therefore
defects turn unions into intersections:

\[
 S-N_S(D-C_i)
 =P_0\cap\bigcap_{j\ne i}P_j=Q_i.                  \tag{2.6}
\]

By (2.1), \(C_i\mid(D-C_i)\) is a connected bipartition with an edge
between its sides.  Its quotient cannot contain \(K_k\), so
\((P_i,Q_i)\in\mathcal R_k(G[S])\).  Equations
(2.4)--(2.6) form a \(p\)-defect star of order \(m\), proving (2.3).

### Corollary 2.2 (minimal internal separators)

If \(D\) is internally \(w\)-connected and \(W\) is a \(w\)-cut, then
every component of \(D-W\) has neighbourhood exactly \(W\).  Hence, when
\(D-W\) has at least two components, (2.1) holds and Theorem 2.1
applies.

Indeed, a component missing a vertex of \(W\) would be separated by at
most \(w-1\) vertices.  Any other component, together with \(W\), then
connects all of \(D-C_i\).

## 3. The two exact seven-boundary examples

For the \(2K_3\dot\cup K_1\) missing-edge boundary, every maximal bad
contact pair has a three-contact side.  The balanced width theorem is
stronger than the star bound: with \(\lambda=k=7\), it directly makes
each nonsingleton shore four-connected.  Portal locality then places
each vertex row in one cross-triangle, and rooted triangles close the
boundary.

For the \(C_6\dot\cup K_1\) missing-edge boundary,
\(\lambda=k=|S|=7\).  At a two-cut, (2.2) gives \(p=2\).  The hand
defect calculation in hadwiger_c6_two_piece_locks.md proves

\[
 \sigma_{7,2}(J)=2.                                 \tag{3.1}
\]

The key point is structural.  Three leaf defects of order at most two
would either have a common element, contradicting (1.2), or have the
form

\[
 \{y,z\},\quad\{x,z\},\quad\{x,y\}.
\]

The three bad-pair conditions then say that each pair is the
\(C_6\)-neighbourhood of the omitted third vertex, producing a triangle
in the missing cycle.  Thus every two-cut has exactly two components,
without a labelled finite enumeration of cut configurations.

## 4. Balanced transition core

The star number controls branching but not a chain of two-sided
separations.  The remaining information is carried by the **balanced
transition core**

\[
 \mathcal R_k^{\mathrm{bal}}(J;q)=
 \{(P,Q)\in\mathcal R_k(J):
   |S-P|>q,\ |S-Q|>q,\ (P,Q)\text{ is inclusion-minimal}\}.   \tag{4.1}
\]

For \(2K_3\dot\cup K_1\), take \(q=3\).  This core is empty: every
maximal bad contact pair has a cross-triangle side.  This is the exact
abstract property behind the connectivity-to-rooted-triangle closure.

For \(C_6\dot\cup K_1\), take \(q=4\).  The unbalanced empty-defect
pairs then have a contact side of order at most four and are omitted
from (4.1), while the balanced core consists of

\[
 \{v\}\leftrightarrow N_{C_6}(v)
\quad(v\in V(C_6)),\qquad
 M_i\leftrightarrow M_j\quad(i\ne j),                \tag{4.2}
\]

where \(M_0,M_1,M_2\) are the three antipodal pairs.  Thus the failure
of the cross-triangle mechanism is not arbitrary: it is precisely an
oriented cycle-incidence system, together with the directed triangle on
the three antipodal defect types.

This identifies the next uniform lemma:

> **Balanced-core dichotomy.**  For a counterexample-derived full-shore
> adhesion, either the balanced transition core is eliminated by rooted
> portal models, or its transitions orient all tight two-sided
> separations consistently.  Consistent transitions uncross to a
> laminar/web decomposition whose adhesion states agree on both sides
> and hence colour the graph.

Theorem 2.1 supplies the branching half of this target.  What remains is
the chain/uncrossing half: composition of defect transitions along
successive two-sided separations must either leave the bad relation
(giving a positive quotient) or become periodic.  In the periodic case,
the period itself is a boundary cycle order, which is the frame needed
for the two-shore web-gluing theorem.
