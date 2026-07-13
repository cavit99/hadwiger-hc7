# A sharp portal-multiplicity obstruction to the simultaneous-prism step

## 1. Why a linkage-only theorem is false

Write the six missing-cycle vertices abstractly as

\[
  c_0,c_1,c_2,c_3,c_4,c_5
\]

in cyclic order.  Let a shore (D) be the tetrahedron

\[
  D=K_4[a,b,d,q]
\]

and give its six portal classes the following sets:

\[
\begin{array}{c|cccccc}
 i&0&1&2&3&4&5\\ \hline
 P_i&\{d,q\}&\{a\}&\{b,q\}&\{d\}&\{a,q\}&\{b\}.
\end{array}                                             \tag{1.1}
\]

For a cycle edge (e_i=c_ic_{i+1}), a shore realization is a connected
set meeting both (P_i) and (P_{i+1}).  Since (D) is complete, two
such realizations form a two-linkage exactly when they can be chosen
disjoint.

### Proposition 1.1

The portal system (1.1) has all of the following properties.

1. It owns all six frames: for every (i), the demands
   (e_{i-2}) and (e_{i+2}) have disjoint realizations.
2. Every owned frame is tight: no such realization can absorb the
   outward class (P_i) on its first side or (P_{i+1}) on its second
   side.
3. None of the three antipodal pairs (e_i,e_{i+3}) has a two-linkage.
4. Neither alternating triple
   ({e_0,e_2,e_4}) or ({e_1,e_3,e_5}) has a three-linkage.
5. There cannot be a six-rooted prism or missing-cycle model in (D),
   because six disjoint nonempty rooted bags cannot fit in four vertices.

#### Proof

Every consecutive pair (P_i,P_{i+1}) is disjoint, so each realization
of (e_i) uses at least two vertices of (D).  Direct inspection gives
the six frame witnesses (in four-bit notation on (a,b,d,q))

\[
 (3,12),(10,5),(5,10),(9,6),(6,9),(12,3).             \tag{1.2}
\]

In each pair the two masks are disjoint and therefore adjacent in the
tetrahedron.  For an antipodal demand pair, inspection of the two possible
minimal masks for each demand shows that every choice intersects.  An
alternating three-linkage would need three disjoint sets of order at least
two, impossible in a four-vertex shore.  The outward-absorption statement
is the same sixteen-subset check with one additional portal-incidence
requirement.  The dependency-free checks are in
`c6_portal_tetrahedron_verify.py` and
`c6_k4_portal_exhaustive.cpp`.  \(\square\)

The example shows exactly why representatives chosen in separate frame
linkages cannot be silently identified.  The odd classes have singleton
representatives, while the even classes reuse the central vertex (q).
The separate pair linkages exist, but there is no six-element portal
transversal.

## 2. It survives every coarse contact test

Return to the standard boundary labels

\[
 (c_0,c_1,c_2,c_3,c_4,c_5)=(0,4,2,3,1,5)
\]

and let (z=6).  Give (a,b,d,q) the boundary contact rows

\[
\begin{aligned}
 N_S(a)&=\{1,4,6\},&N_S(b)&=\{2,5,6\},\\
 N_S(d)&=\{0,3,6\},&N_S(q)&=\{0,1,2,6\}.            \tag{2.1}
\end{aligned}
\]

Their union is all of (S), so (D) is a full shore.  Every nontrivial
bipartition of (K_4) has connected adjacent sides.  For all fourteen
ordered bipartitions, its two contact rows are negative in the exact
two-piece atlas of `hadwiger_c6_two_piece_locks.md`.  Thus the obstruction
survives not only the linkage exclusions but every existing coarse split
test.

There is also an ambient sharpness example.  Take the boundary
(G[S]), the shore (D) with (2.1), and a second shore consisting of one
vertex (h) complete to (S).  There are no (D-h) edges.

### Proposition 2.1

The resulting twelve-vertex graph is six-connected and has no (K_7)
minor.

#### Certificate

`c6_portal_tetrahedron_verify.py` checks six-connectivity and exhausts all
1,899,612 partitions of every support of order (7,ldots,12) into seven
nonempty branch sets.  It tests connectivity of every bag and all 21 bag
adjacencies; none is a (K_7)-model.  The same script independently
replays all linkage and two-piece assertions above.

The degree sequence is

\[
  7,7,7,6,6,6,11,6,6,6,7,7.                       \tag{2.2}
\]

Thus the example misses the counterexample-derived hypotheses by exactly
one unit: it is six-connected rather than seven-connected and has degree-
six vertices.

## 3. Complete tetrahedron classification

The sharpness is not peculiar to the displayed labeling.

### Theorem 3.1 (exact (K_4) portal bound)

Let (D=K_4), and let (P_0,ldots,P_5) be arbitrary nonempty subsets
of (V(D)).  Assume:

1. at least two opposite frame pairs are owned;
2. all three antipodal two-linkages are absent; and
3. both alternating three-linkages are absent.

Then:

* every owned frame is automatically tight;
* every connected split is automatically negative in the exact
  (C_6\dot\cup K_1) two-piece atlas; and
* some vertex of (D) lies in at most two of the six portal classes.

Consequently, even if that vertex also contacts (z), its degree in the
ambient graph is at most

\[
  3+2+1=6.                                           \tag{3.1}
\]

So minimum degree seven eliminates every tetrahedral portal obstruction.

#### Exact certificate

`c6_k4_portal_exhaustive.cpp` enumerates all

\[
  (2^4-1)^6=11,390,625
\]

nonempty portal assignments.  Exactly 624 satisfy the three hypotheses;
all 624 are tight and exact-split negative.  Modulo the dihedral group of
the missing cycle and the (S_4) automorphism group of the tetrahedron,
there are only four types, encoded by

\[
  12492c,quad12582c,quad12592c,quad16834a,          \tag{3.2}
\]

where the six hexadecimal digits are the six four-bit portal masks.  The
maximum, over all survivors, of the minimum number of portal classes at a
shore vertex is two.  The program asserts this final bound and exits with
failure if it ever finds a value at least three.

## 4. Exact implication for the missing theorem

The following proposed statement is false:

> Two-connectivity, fullness, the owned-frame conditions, the forbidden
> nonidentity linkages, and all exact two-piece locks force a coherent
> six-root prism/web.

The tetrahedron is a counterexample.  Therefore a valid simultaneous-web
theorem must use the global seven-connectivity/minimum-degree information
*inside the portal decomposition*, rather than applying a rooted theorem
to representatives selected independently.

The precise remaining structural target is a **multiplicity-resolution
lemma**:

> In the seven-connected (C_6\dot\cup K_1) adhesion, a simultaneous Yu
> three-path obstruction either has a six-element coherent portal
> transversal on which its ladder descriptions agree, or it exposes a
> shore vertex of total degree at most six (equivalently, a globally
> separating adhesion of order at most six).

The tetrahedron is the sharp degree-six equality case.  Yu's obstruction
characterization supplies the unbounded ladder/3-planar decomposition;
Theorem 3.1 identifies the first basic rung that the multiplicity-resolution
lemma must remove.  This is the exact extra hypothesis and mechanism absent
from a purely SPQR or linkage-only argument.
