# Adversarial audit: low-owner descent and terminal base

## Verdict

The verdict has two parts.

1. **GREEN (local theorem).**  The low-owner finite-or-descent theorem
   is sound after the complete-portal-set clarification now inserted in
   Lemma 4.1.  A low-owner Moser shore either has order at most five or
   contains a strictly smaller connected exact seven-fragment.
2. **RED (automatic recursion claim).**  The new exact cut has an
   arbitrary seven-vertex boundary and need not retain the Moser
   boundary, three-shore geometry, or ownership state.  Therefore the
   theorem cannot simply be reapplied to its smaller fragment.  Strict
   inclusion makes any chain terminate if a separate theorem produces
   such a chain, but the owner-descent theorem alone produces only its
   first step.

The terminal computation is also GREEN as a finite check.  Its original
UNSAT output was not a proof certificate.  It is now independently
replaced by the facial lemma and ten-row table in
hadwiger_moser_three_shore_small_face_certificate.md.

## 1. Low-owner selection

There are sixteen optimal Moser partitions.  Unique ownership assigns
each partition to exactly one of the three shores, so the three owner
counts sum to sixteen.  One shore owns at most

\[
\left\lfloor16/3\right\rfloor=5
\]

and is a non-owner for at least eleven partitions.  This argument does
not require the singleton multiplicity calculation.  The displayed
multiplicities \(4,2,2,2,2,2,2\) are nevertheless correct.

The dependency-free ownership verifier correctly:

* enumerates the sixteen matchings;
* quotients all circular orders by rotation and reversal; and
* computes seven as the maximum number of globally pairwise-alternating
  matching states.

The hand proof needs even less: for each fixed singleton, one facial
six-point order has a unique antipodal perfect matching.  Thus at most
one non-owner state occurs per singleton, regardless of whether the
six-point orders for different singletons are compatible.

## 2. Hall and three-web synchronization

For every omitted singleton \(s\), the other six complete portal
classes have an SDR unless the shore has at most five vertices.  The
Hall-deficiency cut has order at most six and another full shore remains
on the far side.

For an unowned partition, all three pair demands are crossless.  The
same-vertex Two Paths Theorem and seven-connectivity make their webs
bare, giving three faces \(F_{12},F_{13},F_{23}\) in the unique
embedding of a three-connected shore.

In the all-distinct-face case, it is essential to use complete portal
sets, not only one selected SDR.  If \(A_i=\{x,y\}\), then
\(P_x,P_y\) lie in both faces whose indices contain \(i\), hence in
their intersection.  The two SDR representatives occupy the two ends
of its unique shared edge.  Therefore the union of the six complete
portal sets has exactly six vertices.  This quantifier repair is now
explicit in the source.

If vertices remain outside that six-set, a component has neighbourhood
contained in the six vertices plus the omitted singleton.  An untouched
shore is on the far side, so seven-connectivity forces an exact
seven-cut.  If no vertex remains, the three shared edges and facial
cycles force the triangular prism; extra prism chords have no face in
which to lie.  Its vertices have degree at most six, contrary to the
minimum-degree hypothesis.

Thus, absent exact descent, every unowned partition puts all six portal
classes on one face.  For a fixed singleton, two such partitions use
the same face and the same fixed six-class SDR.  The facial order has
only one antipodal perfect matching.  Hence a three-connected shore
without descent is a non-owner at most seven times, contradicting the
eleven non-owner states of a low-owner shore.

No seven-class SDR is needed in the repaired proof.

## 3. Cutvertex ownership

Lemma 6.1 is GREEN.

If \(q\) is a cutvertex, every component \(C\) of \(D-q\) has

\[
N_G(C)\subseteq S\cup\{q\}.
\]

It attaches to \(q\), and seven-connectivity gives at least six
boundary contacts.  In any \(2,2,2,1\) partition it therefore fully
contacts at least two pair blocks.  Two components supply two
two-element choice sets, from which distinct blocks can always be
chosen.  The carriers \(C_1\cup\{q\}\) and \(C_2\) are disjoint,
connected, and adjacent through an edge from \(q\) to \(C_2\).
Therefore a cutvertex shore owns every partition and cannot be the
low-owner shore.

## 4. Two-cut descent

Lemma 6.2 is GREEN.

For a two-cut \(\{p,q\}\), two-connectivity makes every component
\(R_j\) of \(D-\{p,q\}\) attach to both \(p\) and \(q\).
Seven-connectivity then gives at least five boundary contacts.

For one partition not owned by \(D\), let \(\mathcal F_j\) be the
nonempty set of pair blocks fully contacted by \(R_j\).  If two
components admitted distinct choices, then

\[
R_i\cup\{p\},\qquad R_j\cup\{q\}
\]

would be disjoint adjacent carriers for those blocks.  Therefore all
\(\mathcal F_j\) are the same singleton.  Each \(R_j\) must miss one
root from each of the other two blocks and no other root, so

\[
|N_S(R_j)|=5,\qquad
N_G(R_j)=N_S(R_j)\cup\{p,q\}.
\]

Every \(R_j\) is a proper connected exact seven-fragment.

## 5. What “well-founded” does and does not mean

The produced fragment \(C\) is a strict subset of \(D\), so cardinality
is a valid decreasing measure.  The conditional statement in Theorem
1.1 is correct: if the selected low-owner shore itself is an
inclusion-minimal fragment among all exact seven-cuts, the descent
outcome is impossible.

What is not justified is selecting an arbitrary Moser cut and then
assuming its low-owner shore is globally minimum.  Nor is ownership
shown to transfer to the new cut.  In particular, after replacing
\(S\) by \(N(C)\):

* \(G[N(C)]\) need not be Moser;
* \(G-N(C)\) need not have three components; and
* even in a new three-shore Moser state, \(C\) need not be its
  low-owner shore.

Thus the descent is a genuine structural export to the general exact-cut
problem, not a closure of that problem.

## 6. Audit of the terminal CEGIS encoding

For a fixed internal graph \(D\), the Boolean variables are exactly the
\(7|D|\) root-contact incidences.

* Fullness is encoded by one disjunction per root.
* The degree inequality is exactly
  \(d_D(v)+|N_S(v)|\ge7\).
* For every nonempty proper \(X\subset D\), the script computes the
  actual disjoint sets \(N_D(X)-X\) and \(N_S(X)\), and imposes
  \[
  |N_D(X)-X|+|N_S(X)|\ge7.
  \]
  The omitted case \(X=D\) is exactly fullness of the seven roots.
* Connected masks enumerate every nonempty connected carrier because
  atlas vertices are relabelled \(0,\ldots,|D|-1\).
* A matching is owned exactly when two distinct pair blocks have
  disjoint connected supporting masks.  Adjacency need not be encoded:
  a shortest connector in the connected shore can be divided between
  the two masks.
* The sum of the sixteen exact owner expressions is constrained to at
  most five.

The atlas coverage is complete: all connected types of orders one to
three and all three-connected types of orders four to six are tested.
The latter counts are \(1,3,17\).  Every order-four-to-six instance is
UNSAT before the optional minor CEGIS loop, so correctness of the
\(K_7\)-minor enumerator is irrelevant to that claim.

The script now asserts:

* candidate counts \(1,1,2,1,3,17\);
* the unique full-singleton survivor;
* zero CEGIS iterations for all twenty-four UNSAT types; and
* SHA-256
  \(d74287d353e0f3d49b1f24c90f42938b08ba40e3543cad5070348a908d75576b\).

A digest verifies replay consistency, not logical UNSAT.  The next
section supplies the transparent proof.

## 7. Transparent terminal certificate

For any fixed allegedly unowned partition in a three-connected shore,
the three bare webs give faces \(F_{12},F_{13},F_{23}\).  Put
\[
\begin{aligned}
I_1&=F_{12}\cap F_{13},\\
I_2&=F_{12}\cap F_{23},\\
I_3&=F_{13}\cap F_{23}.
\end{aligned}
\]
Fullness makes all \(I_i\) nonempty.  If \(m(v)\) is the number of
these intersections containing \(v\), complete-portal-set containment
gives
\[
|N_S(v)|\le1+2m(v).
\]
Thus every vertex must satisfy
\[
d_D(v)+1+2m(v)\ge7.                               \tag{7.1}
\]

The complete atlas contains ten planar three-connected types on four
to six vertices.  Enumerating only triples of their facial cycles gives
respectively
\[
20,35,56,30,56,50,77,70,104,88
\]
triples with all \(I_i\ne\varnothing\), and zero satisfying (7.1).
Every nonplanar type is excluded by the first bare web.  This proves
that every three-connected shore of orders four to six owns every
partition.

Orders two and three have direct carrier proofs, recorded in
hadwiger_moser_three_shore_small_face_certificate.md.  The only bounded
low-owner survivor is a single vertex complete to all seven roots.

Eliminating that singleton uses the separate pure-Moser
degree-seven/two-exterior theorem.  Consequently:

> Every three-shore Moser cut in the counterexample setting contains a
> proper nested exact seven-fragment,

conditional on that independently installed two-exterior theorem.
This is the exact closure strength.  It does not eliminate the exported
arbitrary-boundary exact cut.

