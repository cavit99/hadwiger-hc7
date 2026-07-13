# Preliminary audit of the fixed-\(C\), order-seven sparse search

> **Superseded.**  The later kappa-only 853-type computation, audited in
> hadwiger_k34_c7_kappa_audit.md, uses the same frozen solver with both the
> sparse-total and conditional-Dirac switches disabled and is independently
> certified UNSAT on every connected seven-vertex \(C\).  It therefore
> eliminates these sparse cells a fortiori.  The pending language below
> records the state of this narrower audit before that stronger certificate.

## Audit state

The logical encoding in k34_c7_sparse_fixed.py has been checked against the
exceptional-cell hypotheses.  This preliminary audit applies to file
SHA-256

    efd2721b5c7e3b3e026fcf7b76f5e9a9f5f5caced94fd814b99ab5ea0a8e4c3c

and finds no unsound reduction.

This note does **not yet certify the 221 solver outcomes**.  Certification
of run coverage is deliberately deferred until the complete terminal
output, final counts, and digests from the run of this exact file are
available.  An UNSAT result for every fixed \(C\), with no timeout/unknown
result, would eliminate both sparse order-seven cells for the sufficient
two-helper certificate.  A SAT or unknown result would not.

## 1. Graph-atlas coverage

NetworkX's graph atlas contains all graph isomorphism classes of order at
most seven.  Filtering by

* order seven,
* connectedness, and
* \(e(C)\in\{12,13\}\)

returns exactly

\[
126\quad\text{classes with }e(C)=12,\qquad
95\quad\text{classes with }e(C)=13,
\]

for 221 classes in total.

This coverage was independently checked without trusting just those two
atlas counts.  Direct enumeration of the \(\binom{21}{q}\) labelled edge
sets gives

\[
290,745\quad(q=12),\qquad 202,755\quad(q=13)
\]

connected labelled graphs.  For every atlas representative, its
automorphism group was computed by all \(7!\) permutations, and the orbit
sizes \(7!/|\operatorname{Aut}(C)|\) were summed.  The two orbit sums are
again 290,745 and 202,755.  Thus the 126 and 95 atlas rows are pairwise
nonisomorphic and exhaustive for the two fixed edge counts.

Using one representative of each \(C\)-orbit is safe: after transporting
an arbitrary incidence pattern along an isomorphism to that representative,
the \(A\)- and \(B\)-incidence variables remain completely free.  The
script performs no additional quotient by \(\operatorname{Aut}(C)\).

The graph-code digest computed independently in atlas order is

    e9cc59585d83825c03de308caa6f775350e548e18e89342acadefbee03caf760

which matches EXPECTED_GRAPH_ID_DIGEST in the audited file.

## 2. Sparse \((p,q)\) mapping and degree constraints

The two sparse density cells are

\[
(p,q)=(25,12),(24,13),
\qquad p=e(C,N),\quad q=e(C).
\]

The code maps \(q=12\) to \(p=49-24=25\), and \(q=13\) to
\(p=50-26=24\).  Although the conditional expression is stylistically
unusual, the mapping is correct.

The 21 \(A\)-incidence and 28 \(B\)-incidence Booleans are all the possible
edges between \(C\) and \(N=A\dot\cup B\).  Their total is constrained to
equal \(p\).  Every \(A\)-row has order at least four, and every \(B\)-row
has order at least three, exactly as minimum degree requires in the
\(K_3\dot\cup K_4\) neighbourhood.

For \(x\in C\), there is no edge \(xv\), and every neighbour of \(x\) is
in \(C\cup A\cup B\).  Hence

\[
d_G(x)=d_C(x)+d_A(x)+d_B(x).
\]

The pseudo-Boolean constraint

\[
d_A(x)+d_B(x)\ge7-d_C(x)
\]

therefore encodes \(d_G(x)\ge7\) exactly.

As a useful consistency check, for \((p,q)=(25,12)\),
\(p+2q=49\), so all seven \(C\)-vertices have degree exactly seven.  For
\((24,13)\), \(p+2q=50\), so precisely one unit of degree surplus exists:
one \(C\)-vertex has degree eight and the other six degree seven.

The monotone ordering constraints on the three \(A\)-row codes and four
\(B\)-row codes are harmless.  The fixed cliques make each family
internally symmetric, and every later constraint, including the helper
quantification, is invariant under those row permutations.

## 3. The 127 connectivity consequences

For each nonempty \(X\subseteq C\), the code computes

\[
\partial_C X=N_C(X)\setminus X
\]

as the union of the fixed \(C\)-neighbourhoods of vertices of \(X\), minus
\(X\).  It then uses seven indicators, one for each vertex of \(A\cup B\),
which record whether that boundary vertex has at least one neighbour in
\(X\).  Thus the encoded inequality is exactly

\[
|\partial_C X|+|N_N(X)|\ge7.
\]

The external neighbourhood of \(X\) separates \(X\) from \(v\), so this
is a necessary consequence of \(\kappa(G)\ge7\).  All
\(2^7-1=127\) nonempty subsets, including \(X=C\), are checked.

These inequalities do not encode full seven-connectivity of the
15-vertex host.  That omission is safe for an UNSAT proof: they define a
weaker superset of the counterexample-derived incidence states.  If even
this weaker system is UNSAT after imposing no helpers, then no genuinely
seven-connected obstruction exists.  A SAT model would merely be
inconclusive unless its full connectivity were separately checked.

## 4. Conditional Dirac neighbourhood constraints

For a degree-seven vertex \(x\) of a 7-contraction-critical graph, Dirac's
neighbourhood bound gives

\[
\alpha(G[N(x)])\le2.
\]

The formula degree_seven is true exactly when

\[
d_A(x)+d_B(x)=7-d_C(x).
\]

The global minimum-degree constraint makes this precisely the event
\(d_G(x)=7\).

The typed candidate list contains all potential neighbours of \(x\):

* all three \(A\)-vertices and all four \(B\)-vertices, guarded by their
  incidence variables; and
* exactly the fixed \(C\)-neighbours of \(x\).

It correctly omits \(v\), which is not adjacent to a vertex of \(C\), and
omits \(x\) itself.

For every candidate triple, the antecedent asserts that all three vertices
are neighbours of \(x\).  The consequent asserts that some pair in the
triple is adjacent.  The helper yz returns:

* true inside the \(A\)-clique and inside the \(B\)-clique;
* false between \(A\) and \(B\);
* the fixed \(C\)-edge value for two \(C\)-vertices; and
* the appropriate incidence variable for an \(A\)-\(C\) or \(B\)-\(C\)
  pair.

Skipping a triple with an identically true internal edge is valid.
When every possible internal edge is identically false, the empty
z3.Or is false, correctly forbidding the independent triple.
Consequently the conditional encoding is equivalent to
\(\alpha(G[N(x)])\le2\) at every degree-seven \(C\)-vertex.

The script does not impose the analogous Dirac consequences at possible
degree-seven vertices of \(A\cup B\).  This again weakens the system and
is safe for an UNSAT conclusion.

## 5. Arbitrary multi-\(A\) helpers

A sufficient helper bag has the form

\[
J=P\cup R,
\qquad \varnothing\ne P\subseteq C,\quad
\varnothing\ne R\subseteq A,
\]

is connected, and is adjacent to every vertex of \(B\).

Because \(A\) is a clique, \(J\) is connected exactly when every component
of \(C[P]\) has a neighbour in at least one root in \(R\).  The helper
predicate computes the fixed components of \(C[P]\) and imposes precisely
these component-contact clauses.  It permits every one of the seven
nonempty subsets \(R\subseteq A\), so a bag may contain one, two, or all
three \(A\)-vertices.  A root in \(R\) need not itself meet \(P\), since it
can attach through another root in the \(A\)-clique; the code correctly
does not impose that unnecessary condition.

Since there are no \(A\)-\(B\) edges, adjacency of \(J\) to every
\(b\in B\) is equivalent to \(P\) meeting every \(B\)-row.  The
b_complete formula is therefore exact.

The script considers every pair of nonempty disjoint \(C\)-sets, once,
using left < right, and every pair of disjoint nonempty root subsets.
Those are exactly the pairs of vertex-disjoint helper bags in \(C\cup A\).
Any such pair is mutually adjacent through an edge between its two disjoint
nonempty root subsets of the \(A\)-clique.  Both helpers meet \(N(v)\);
with the four \(B\)-singletons and \(\{v\}\), they give the required
\(K_7\)-model.

Helpers with an empty \(C\)-part need not be considered: a subset of \(A\)
alone has no edge to any \(B\)-vertex and cannot be \(B\)-complete.
Unused vertices of \(C\) or \(A\) are allowed.

Thus the family of negated pair constraints is exactly the negation of
the sufficient two-helper certificate, even when helpers are allowed
multiple \(A\)-roots.

## 6. Meaning of a fixed-\(C\) UNSAT result

Fix one connected \(C\)-graph with \(q=12\) or 13.  Every incidence state
arising from the sparse exceptional HC7 cell satisfies:

1. the row and total-incidence constraints;
2. all seven \(C\)-vertex minimum-degree constraints;
3. all 127 \(C\)-shore boundary inequalities;
4. the conditional Dirac constraints; and
5. the negated helper-pair constraints if it has no sufficient
   \(K_7\)-model.

Therefore UNSAT for that fixed graph proves that every counterexample-derived
incidence state on that \(C\) has two helpers and hence a \(K_7\)-minor.
Because the encoded structural conditions are necessary rather than
sufficient for a genuine counterexample, weakening full connectivity or
omitting additional criticality constraints cannot invalidate this
direction.

If all 126 twelve-edge types and all 95 thirteen-edge types return UNSAT,
with no SAT, timeout, or unknown result, the two sparse order-seven cells
are eliminated.  This conclusion additionally depends on trusting the Z3
UNSAT results and the graph-atlas/orbit coverage documented above.

## 7. Pending run certificate

The audited file contains two expected digests:

* graph-ID digest
  e9cc59585d83825c03de308caa6f775350e548e18e89342acadefbee03caf760;
* all-UNSAT status digest
  ff15c316a703c69235124ce7431d8e01914c05881c04fb6dbd5be0f8aa562e42.

The second value is the SHA-256 of the 221 atlas graph codes paired with
the literal status string “unsat”; it has been recomputed independently.
It is a useful coverage checksum, not independent evidence that Z3
actually returned UNSAT.

Final certification is pending receipt and comparison of:

* the complete final counts, which must be
  \(\{\mathrm{sat}:0,\mathrm{unsat}:221,\mathrm{unknown}:0\}\);
* both printed digests;
* the success line after all assertions; and
* confirmation that the completed process ran the audited file version
  rather than an earlier in-memory version.

The critical conclusions are guarded by Python assertions.  The documented
run must use ordinary python3 without the -O flag; otherwise assertions
would be disabled.
