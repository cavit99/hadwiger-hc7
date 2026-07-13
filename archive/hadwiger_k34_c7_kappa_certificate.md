# A separator-or-two-helpers certificate for \(|C|=7\)

This note records a finite computer-assisted proof of the exact local
statement needed in the seven-vertex \(K_3\dot\cup K_4\) cell.  It is
formulated as a concrete dichotomy: either there are two explicit types of
branch bags, or a set of at most six vertices separates a nonempty subset of
\(C\) from \(v\).

The computation has completed with no solver timeouts.  Because the result is
new and materially stronger than the sparse-cell search, it must receive an
independent encoding audit and rerun before being installed as a theorem.
Nothing here claims \(\mathrm{HC}_7\); only the residual cell with
\(|C|=7\) is addressed.

## 1. Finite lemma

Let \(C\) be a connected graph on seven vertices.  Let

\[
 A=\{a_1,a_2,a_3\},\qquad B=\{b_1,b_2,b_3,b_4\}.
\]

Assume

\[
 |N_C(a)|\geq4\quad(a\in A),\qquad
 |N_C(b)|\geq3\quad(b\in B),                          \tag{1.1}
\]

and

\[
 d_C(x)+d_A(x)+d_B(x)\geq7\quad(x\in C).             \tag{1.2}
\]

Finally suppose that, for every nonempty \(X\subseteq C\),

\[
 |N_C(X)-X|+|N_A(X)|+|N_B(X)|\geq7.                  \tag{1.3}
\]

Then there are disjoint nonempty \(P,Q\subseteq C\) and disjoint
nonempty root sets \(R,S\subseteq A\) such that

* \(G[P\cup R]\) and \(G[Q\cup S]\) are connected; and
* \(P,Q\) both meet \(N_C(b)\) for every \(b\in B\).

The root sets are allowed to have orders \(1,1\) or \(1,2\).  This is
the actual Lemma 1.1 target; imposing one root per bag would be an
unnecessary and false strengthening.

## 2. From seven-connectivity to (1.3)

In the exceptional neighbourhood cell, \(v\) has no neighbour in
\(C\).  For every nonempty \(X\subseteq C\), the set

\[
 S_X=(N_C(X)-X)\cup N_A(X)\cup N_B(X)                \tag{2.1}
\]

separates \(X\) from \(v\).  Hence \(\kappa(G)\geq7\) implies
\(|S_X|\geq7\), which is precisely (1.3).  Notice that the finite
lemma uses only this necessary consequence of seven-connectivity; it
does not need the full collection of cuts of the fifteen-vertex host.

The row bounds (1.1) also follow from minimum degree seven: a vertex
of \(A\) already has \(v\) and its two clique neighbours, while a
vertex of \(B\) has \(v\) and its three clique neighbours.

## 3. Exact branch-bag predicate

For nonempty \(P\subseteq C\) and nonempty \(R\subseteq A\), define

\[
 h(R,P)\iff
 \begin{cases}
 P\cap N_C(b)\neq\varnothing&\text{for every }b\in B,\\
 G[P\cup R]\text{ is connected}.&
 \end{cases}                                          \tag{3.1}
\]

Because \(A\) is a clique, the second line is equivalent to the
following component condition:

\[
 \text{every component of }C[P]
 \text{ has a neighbour in }R.                        \tag{3.2}
\]

Thus (3.1) contains no hidden path or connectivity oracle once \(C\)
is fixed.

The negation of the desired conclusion is exactly

\[
 \neg\bigl(h(R,P)\wedge h(S,Q)\bigr)                 \tag{3.3}
\]

for every pair of disjoint nonempty sets \(P,Q\subseteq C\) and every
pair of disjoint nonempty root sets \(R,S\subseteq A\).  A helper bag
cannot have empty C-part, since there are no A--B edges.  Conversely,
every pair of Lemma 1.1 bags has precisely the form covered by (3.3).

## 4. Exhaustive certificate

There are 853 isomorphism classes of connected seven-vertex graphs.
As an orbit-coverage check,

\[
 \sum_C\frac{7!}{|\operatorname{Aut}(C)|}=1{,}866{,}256,             \tag{4.1}
\]

the number of connected labelled graphs on seven vertices.

For each of the 853 choices of \(C\), the solver leaves only the 49
A/C and B/C incidences Boolean and asserts:

1. the seven row lower bounds (1.1);
2. the seven degree inequalities (1.2);
3. all 127 inequalities (1.3); and
4. all no-helper clauses (3.3), using the component test (3.2).

No density equality, contraction-critical neighbourhood lemma,
colouring constraint, or full-host connectivity constraint is used.

The run was divided by atlas index modulo six.  It returned

\[
 \boxed{853\ \mathrm{UNSAT},\quad0\ \mathrm{SAT},\quad0\ \mathrm{UNKNOWN}}.
                                                               \tag{4.2}
\]

The shard sizes were \(143,142,142,142,142,142\).  In shard order,
the SHA256 digests of the graph6-id/status streams are:

```text
88bd85f9d81e547408ee9ccb5a18eb1c3ad9705e183ae2bdc81c3999e07cb136
fe51bf49c4239069592a28b04edbc2c88d96500cfbd200d3fbd12088be9fac68
c2190fb67ce2035a602128e028690a75c39d6bf24d67b26a28e699f059a8c8b5
01ea845a80461d583d95bf23213fb0b8d8344c2832c3092587191b7d4ec834b4
6aef5ce8017afb1120a0bad7c7a67ec334753430b7d11b961d8ec3397b41764c
26383fc75f1e08e833a28eb6da083ec08555e9856a45b9084bbd550f2054e452
```

The corresponding unsharded all-UNSAT stream has digest

```text
fe854344e1c75336fa01d6bab426e1456e28a2f59ad46c9315dc82c11e72a946
```

The files used are:

```text
k34_c7_sparse_fixed.py
SHA256 aea1de233d30568694208458ea44a415c64f6c7637531c4438299f69b572a5fb

k34_c7_kappaonly_parallel.py
SHA256 36231bad721c4f2ab66c1e92cfbcafc771ffabad66875fdee160dfa0088f0e0a
```

The wrapper calls the fixed-C solver with
`enforce_sparse=False, enforce_dirac=False`; these keyword values are
the reason the certificate proves the connectivity-only statement rather
than merely the earlier sparse lemma.  It gives every instance a
120-second timeout and records a timeout as `unknown`.  The six completed
shards had none.

## 5. Concrete separator/branch-set dichotomy

The finite result can be stated without solver language.  Every incidence
system satisfying (1.1)--(1.2) has one of the following two certificates:

1. disjoint \((P,R)\), \((Q,S)\) satisfying (3.1), hence two concrete
   helper branch sets; or
2. a nonempty \(X\subseteq C\) for which the explicit set \(S_X\) in
   (2.1) has order at most six and separates \(X\) from \(v\).

Indeed, the exhaustive UNSAT statement says that forbidding certificate 1
while forbidding certificate 2 is impossible.  Seven-connectivity excludes
certificate 2, so certificate 1 follows.

Given certificate 1, put

\[
 J_1=P\cup R,\qquad J_2=Q\cup S.
\]

The four singleton bags on \(B\), together with \(J_1,J_2\), form a
\(K_6\)-model: the B-bags form a clique, each is adjacent to both
helpers, and the helpers are adjacent through the A-clique.  All six
bags meet \(N(v)\), so adjoining \(\{v\}\) gives a \(K_7\)-minor.

Subject to independent audit, this eliminates the entire
\(|C|=7\) exceptional cell under \(\kappa(G)\geq7\), with no split into
sparse and dense cases.
