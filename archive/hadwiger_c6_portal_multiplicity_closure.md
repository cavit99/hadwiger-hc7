# Portal multiplicity in the (C_6\dot\cup K_1) shore

## 1. The high-owner shore has six distinct portals

Retain the two-full-shore setting with boundary

\[
 S=\{c_0,\ldots,c_5,z\},
\]

where the missing edges on the first six vertices form the cycle
\(c_0c_1\cdots c_5c_0\).  For a shore \(D\), put

\[
 P_i=N_D(c_i).
\]

Every \(P_i\) is nonempty.  The frame-ownership theorem gives one shore
which owns at least two opposite pairs of frames; call it the high-owner
shore.

### Theorem 1.1 (multiplicity closure)

In a seven-connected, minimum-degree-seven, (K_7)-minor-free
realization satisfying the audited frame and split locks, the six portal
sets of the high-owner shore have a system of six distinct
representatives.

### Proof

The hand part is Hall's theorem plus the ambient cut.  If Hall fails for
a label set (I\subseteq\{0,\ldots,5\}), put

\[
 U=\bigcup_{i\in I}P_i,qquad |U|<|I|.              \tag{1.1}
\]

If (D-U\ne\varnothing), every component (C) of it satisfies

\[
 N_G(C)\subseteq
 U\cup\{c_j:j\notin I\}\cup\{z\}.
\]

The right side has order at most

\[
 (|I|-1)+(6-|I|)+1=6,
\]

contrary to seven-connectivity.  Hence (D=U), and (1.1) gives
\(|D|\le5\).

Every nonsingleton shore is two-connected and has order at least four,
so only orders four and five remain.  The exact finite certificates in
Section 2 eliminate both orders under the high-owner hypotheses.  Thus
the shore has order at least six, Hall's condition holds, and the six
distinct representatives exist. \(\square\)

This theorem proves existence of one global transversal.  It does not
assert that independently chosen linkage witnesses use those six
vertices.

## 2. Complete finite base

The programs

* `c6_order4_portal_exhaustive.cpp`, and
* `c6_order5_portal_exhaustive.cpp`

enumerate the finite base.  Both independently generate all labelled
graphs of the relevant order, canonically quotient by vertex
permutations, and assert that the retained hard-coded list is exactly
the complete list of two-connected unlabelled graphs: three at order
four and ten at order five.

For every graph they enumerate all six nonempty portal classes, modulo
the automorphism group of the shore and a dihedral rotation taking a
minimum-cardinality class to label zero.  For every assignment they
check:

1. at least two opposite frame pairs are owned;
2. every owned frame is tight against the two outward absorptions;
3. all three antipodal two-linkages are absent;
4. both alternating three-linkages are absent;
5. every connected bipartition of the shore is negative in the exact
   two-piece atlas;
6. some nonempty (z)-portal set makes every shore vertex have ambient
   degree at least seven.

At order five the Hall cut above adds the necessary condition that every
proper subfamily of portal classes satisfies Hall and the union of all
six is the five-vertex shore.  This condition is checked incrementally
during enumeration.

The exact outputs are:

\[
\begin{array}{c|r|r|r}
|D|&\text{unlabelled type}&\text{linkage survivors}&\text{actual survivors}\\
\hline
4&C_4&0&0\\
4&K_4-e&0&0\\
4&K_4&90&0\\
\hline
5&38&0&0\\
5&43&0&0\\
5&44&14&0\\
5&46&14&0\\
5&47&0&0\\
5&48&0&0\\
5&49&0&0\\
5&50&0&0\\
5&51&0&0\\
5&52=K_5&0&0
\end{array}                                         \tag{2.1}
\]

Here “linkage survivor” means that items 1--4 and the proper Hall
conditions hold; “actual survivor” additionally means that items 5--6
hold for some (z)-portal set.  Thus the final zero column is the
relevant certificate.  The separate program
`c6_k5_portal_exhaustive.cpp` gives an independent (K_5) cross-check:
among 41,566,880 symmetry-reduced assignments, 360 satisfy its raw
linkage filter, but none also satisfies the proper Hall circuit.

The enumeration uses connected vertex masks, not merely incidence
counts.  Consequently its path tests retain the internal graph of every
shore type, and its split tests range only over bipartitions whose two
induced sides are connected.

## 3. What multiplicity closure does and does not give

Theorem 1.1 removes the tetrahedral obstruction and every other bounded
failure of Hall.  The remaining high-owner shore has six distinct
selected roots and three simultaneous Yu (X)-ladder descriptions.

Two further synchronization issues remain:

1. a connected set realizing one missing edge may meet its two portal
   classes at the same shore vertex, even though a distinct transversal
   exists elsewhere; and
2. a merely two-connected shore may realize its three crossless web
   embeddings using different flips across its exact two-cuts.

The corrected `c6_circular_witness_smt.py` retains within-piece portal
coincidences.  It produces a satisfiable order type immediately, so the
earlier four-distinct-occurrence version cannot be used as a closure.
The next valid target is therefore a portal-splitting lemma: replace a
collapsed occurrence by distinct representatives without destroying the
two disjoint path pieces, or project the failure to one of the exact
two-cut rope locks.
