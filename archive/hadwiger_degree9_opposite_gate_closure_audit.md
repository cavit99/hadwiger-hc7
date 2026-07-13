# Adversarial audit: opposite complementary gate closure

## Verdict

The four models in Theorem 2.1 of
`hadwiger_degree9_opposite_gate_closure.md` are **GREEN**.  The portal
counts in Theorem 3.1 are also valid, and the symmetric ordinary-bag
bound uses only the primary potential \(|L_0|+|R_0|\).

There is one invalid citation in the final step.  The terminal-clean
crossed-path theorem in
`hadwiger_degree9_two_carrier_capacity_exchange.md` assumes the fixed
contacts \(K L_0\) and \(J R_0\).  In the double-complementary cell the
hypotheses are exactly \(K\not\sim L_0\) and \(J\not\sim R_0\).
Therefore that theorem cannot be invoked with the stated labels.

The gap is repairable by a direct seven-bag model, independent of all four
carrier-allocation choices.  Consequently the opposite-gate closure
itself remains GREEN after this local repair.

## 1. The four \(KJ\) models

Write

\[
 L_6=K\dot\cup D,qquad R_5=J\dot\cup C,qquad
 6\in D,quad5\in C.
\]

The forced contacts in the complementary cells are

\[
 KD, JC, DC, DL_0, CR_0, L_0R_0,               \tag{1.1}
\]

where \(DC\) is witnessed by \(65\).  The two allocation choices are

\[
 KR_0\text{ or }DR_0,qquad JL_0\text{ or }CL_0.    \tag{1.2}
\]

Assume \(KJ\).  The models (2.1)--(2.4) in the source note were checked
as follows.

### Allocation \(DR_0,CL_0\)

Use

\[
 \{v\},\{h\},\{1\},\{2\},C\cup L_0,D\cup R_0,
 \{3\}\cup K\cup J.
\]

The three large bags meet through \(DC\), \(CJ\), and \(DK\).
They see \(v\) through \(5,6,3\), respectively.  Their contacts to
\(h,1,2\) use the root of \(L_0\), the vertex \(6\) plus the root of
\(R_0\), and the root of \(K\).

### Allocation \(DR_0,JL_0\)

Use

\[
 \{h\},\{1\},\{2\},L_0,K\cup J,
 \{3\}\cup D\cup C,\{v,4\}\cup R_0.
\]

The six contacts among the four large bags are

\[
 L_0J,quad L_0D,quad L_0R_0,quad KD,quad J4,quad v6.
\]

Connectivity of \(3\cup D\cup C\) uses \(65\) and \(35\);
connectivity of \(v4\cup R_0\) uses the right root--\(4\)--\(v\)
path.

### Allocation \(KR_0,CL_0\)

Use

\[
 \{h\},\{1\},\{2\},K,L_0\cup R_0,
 \{v,3\}\cup J,\{4\}\cup D\cup C.
\]

The six large-bag contacts are

\[
 KR_0,quad KJ,quad KD,quad R_03,quad L_0C,quad JC.
\]

### Allocation \(KR_0,JL_0\)

Use

\[
 \{h\},\{1\},\{2\},K,J\cup L_0,
 \{3\}\cup D\cup C,\{v,4\}\cup R_0.
\]

The six large-bag contacts are

\[
 KJ,quad KD,quad KR_0,quad L_0D,quad L_0R_0,quad v6.
\]

In the last three models, every large bag sees \(h,1,2\): use a left
root, a right root together with \(6\) or \(v\), and the displayed
literal vertices.  The singleton bags induce the triangle \(h12\).
No carrier or boundary vertex appears twice.  Thus all four allocations
are valid.

## 2. The clean-cross repair

If \(KJ\) is absent, the two portal bounds imply

\[
                         K C\ne\varnothing,qquad J D\ne\varnothing.
                                                               \tag{2.1}
\]

Indeed, the universal portal bound gives at least three portals in
\(R_5\cup R_0\), while the ordinary-bag theorem permits at most one in
\(R_0\).  Hence at least two \(K\)-portals lie in \(R_5\).  Since
\(KJ\) is absent, all of them lie in \(C=R_5-J\).  Symmetrically, at
least two \(J\)-portals lie in \(D=L_6-K\).  The direct model below
needs only one edge of each kind.  Thus the argument includes the exact
seven-adhesion equality; the strict-surplus estimate of three outer
portals is not needed.

Use the seven bags

\[
 \boxed{
 \{v\},\quad\{h\},\quad\{1\},\quad\{2\},\quad
 D\cup J,quad K\cup C,quad \{3\}\cup L_0\cup R_0.}
                                                               \tag{2.2}
\]

Their connectivity is literal:

* \(D\cup J\) is connected by the edge \(JD\);
* \(K\cup C\) is connected by the edge \(KC\); and
* \(3\cup L_0\cup R_0\) is connected through the right root of
  \(R_0\) and the old edge \(L_0R_0\).

The three large bags are pairwise adjacent through

\[
       (D\cup J)(K\cup C): KD\text{ (also }JC\text{)},
\quad (D\cup J)(3\cup L_0\cup R_0):DL_0,
\quad (K\cup C)(3\cup L_0\cup R_0):CR_0.          \tag{2.3}
\]

They see \(v\) through \(6,5,3\), respectively.  They see \(h,1,2\)
through the right root in \(J\) together with \(6\), the left root in
\(K\), and the vertex \(v\) or the left root in \(L_0\), as
appropriate.  The four singleton bags induce a clique on
\(\{v,h,1,2\}\).  Hence (2.2) is a \(K_7\)-model.

This proof uses only the contacts forced by complementarity; it is
independent of the choices in (1.2).  The conservative quotient verifier
`degree9_complementary_star_probe.py` returns exactly (2.2) in all four
allocations.

## 3. Potential audit

The ordinary-bag multiplicity theorem on the left uses, in its proof,
only exchanges from \(R_0\) into \(L_6\) and \(R_5\).  Both strictly
decrease \(|L_0|+|R_0|\).  Its symmetric image uses exchanges from
\(L_0\) into \(R_5\) and \(L_6\), which decrease the same primary
potential.  Thus the simultaneous inequalities

\[
 |N_{R_0}(K)|\le1,qquad |N_{L_0}(J)|\le1
\]

do not require incompatible secondary tie-breaks.

With the direct replacement (2.2), Theorem 3.1 and the complete
elimination of the double-complementary cell are GREEN, including the
exact seven-adhesion equality.
