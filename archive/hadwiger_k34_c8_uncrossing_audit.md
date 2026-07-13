# Audit of the order-eight uncrossing example

## Verdict

The boundary-submodularity lemma, the explicit host, the complete tight-shore
list, the two minimal boundary witnesses, and the helper bags in
hadwiger_k34_c8_uncrossing.md are all correct.

Two malformed LaTeX commands in equation (3.2) were repaired.  One scope
sentence was narrowed: the example blocks the proposed
minimal-witness-uncrossing route, but it does not show that every possible
order-eight proof must process the crossing in that particular way.

## 1. Boundary submodularity

For an external vertex boundary \(N(X)\), put
\(\Gamma(X)=X\cup N(X)\).  Then

\[
\Gamma(X\cup Y)=\Gamma(X)\cup\Gamma(Y),\qquad
\Gamma(X\cap Y)\subseteq\Gamma(X)\cap\Gamma(Y).
\]

Cardinality submodularity for the closed neighbourhoods, followed by
subtraction of the modular identity for \(|X|\), gives

\[
|N(X)|+|N(Y)|\ge |N(X\cup Y)|+|N(X\cap Y)|.
\]

When \(X,Y\subseteq C\) are tight and intersect, both sets on the right
are nonempty.  Seven-connectivity supplies a lower bound of seven for
each, while the left side is fourteen.  Hence both are tight.  If two
distinct globally inclusion-minimal tight shores intersected, their tight
intersection would be a proper tight subset of at least one.  Thus the
minimal shores are disjoint.

The use of the host induced by \(A\cup B\cup C\) is harmless: vertices of
\(C\) have no edge to \(v\), so deleting \(v\) does not change their
external boundaries.

## 2. Exhaustive check of the explicit host

The graph described in Section 2 has:

\[
|V(G)|=16,\qquad |E(G)|=72,\qquad
\delta(G)=7,\qquad\kappa(G)=7.
\]

NetworkX independently computed node connectivity seven.  In addition,
all

\[
\sum_{i=0}^{6}\binom{16}{i}=14,893
\]

vertex-deletion sets of order at most six were enumerated, and every
remaining graph was connected.  Since \(d(v)=7\), this proves the claimed
connectivity exactly rather than only testing a lower bound.

The prose proof also survives case analysis.  If one of the five
\(C\)-complete boundary vertices survives, it joins all surviving
components of \(C-S\).  A special \(B\)-vertex could be separated from
that component only by deleting \(v\), the other three \(B\)-vertices,
and all of its at least three \(C\)-neighbours, seven vertices.  If none
of the five complete boundary vertices survives, those five deletions
leave room for at most one more; two-connectivity keeps \(C-S\) connected,
and every surviving special \(B\)-vertex retains at least two
\(C\)-neighbours.

## 3. Tight shores and witnesses

All 255 nonempty subsets of \(C\) were checked directly.  None has boundary
below seven, and exactly eight have boundary seven:

\[
\{y\},\ \{u_2\},\ \{u_1,u_2\},\ \{u_2,u_3\},\
\{y,u_2,u_3\},\ \{u_1,u_2,u_3\},\
\{y,u_1,u_2,u_3\},\ C.
\]

It follows immediately that the globally minimal tight shores are exactly
\(\{y\}\) and \(\{u_2\}\).

Among tight shores having \(x\) in their boundary, the unique
inclusion-minimal one is

\[
X=\{u_1,u_2\}.
\]

Among those having \(y\) in their boundary, the unique minimal one is

\[
Y=\{u_2,u_3\}.
\]

Thus \(X,Y\) intersect at \(u_2\) but neither contains the other.  The
intersection is a globally tight atom, but it is not a witness for either
specified boundary vertex.  This verifies the precise failure of the
naive witness-laminarity argument.

The statement that \(u_2\) remains deletable was also checked directly:
\(C-u_2\) is connected, all row bounds survive, and every one of the 127
nonempty shores in \(C-u_2\) has reduced boundary at least seven.

## 4. Helpers and exact scope

The displayed bags

\[
J_1=\{a_1,r_1\},\qquad J_2=\{a_2,r_2\}
\]

are disjoint and connected.  Both \(r_1,r_2\) see all four vertices of
\(B\), and the helpers are mutually adjacent through \(a_1a_2\).
Together with the four \(B\)-singletons and \(\{v\}\), they give a valid
\(K_7\)-model.

Accordingly, the host is not an obstruction to the helper theorem and not
a counterexample to HC7.  Its exact negative content is only this:
globally minimal tight shores do not preserve a specified boundary
vertex, and inclusion-minimal witness shores need not be laminar even
under the full local row and seven-connectivity hypotheses.  A proof based
on that uncrossing strategy needs an additional conversion lemma; other
order-eight mechanisms are not ruled out.
