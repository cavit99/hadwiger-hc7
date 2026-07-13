# The sparse seven-vertex \(K_3\dot\cup K_4\) cell

> **Superseded by a stronger certificate.**  The independently audited
> kappa-only computation in hadwiger_k34_c7_kappa_audit.md eliminates all
> 853 connected seven-vertex choices for \(C\) without imposing the sparse
> totals or the conditional Dirac constraints.  This note remains as the
> narrower route which led to that computation.

This note records a provisional computer-assisted elimination of the two
sparse incidence cases with \(|C|=7\).  It uses actual Lemma 1.1 bags:
a bag may contain either one or two vertices of \(A\).  It does **not**
assert that seven-connectivity alone forces the stronger one-root-per-bag
certificate, and it does not claim \(\mathrm{HC}_7\).

The finite computation has been run once.  It should be independently
audited and rerun before being installed as a proved lemma.

## 1. Hypotheses and target

Let

\[
 N=A\dot\cup B,\qquad G[A]\cong K_3,\quad G[B]\cong K_4,
 \quad E(A,B)=\varnothing,
\]

and let \(C\) be the sole component outside \(N[v]\), with \(|C|=7\).
For \(X\subseteq C\), write \(N_N(X)=N_G(X)\cap N\).

The finite lemma assumes:

1. \(C\) is connected;
2. \(|N_C(a)|\geq4\) for \(a\in A\) and
   \(|N_C(b)|\geq3\) for \(b\in B\);
3. every \(x\in C\) has
   \(d_C(x)+d_N(x)\geq7\);
4. for every nonempty \(X\subseteq C\),

   \[
   |N_C(X)-X|+|N_N(X)|\geq7;                         \tag{1.1}
   \]

5. if \(d_G(x)=7\) for \(x\in C\), then
   \(\alpha(G[N_G(x)])\leq2\); and
6. with \(p=e(C,N)\), \(q=e(C)\), either

   \[
   (p,q)=(25,12)\quad\text{or}\quad(p,q)=(24,13).    \tag{1.2}
   \]

Condition (1.1) is a direct consequence of \(\kappa(G)\geq7\):
\(N_G(X)\) separates \(X\) from \(v\).  Condition 5 is the standard
degree-seven neighbourhood lemma for a contraction-critical minimal
counterexample.  In the first case of (1.2), all seven vertices of
\(C\) have degree exactly seven; in the second, six have degree seven
and one has degree eight.

The target is two disjoint sets \(J_1,J_2\subseteq C\cup A\) such that

* each \(J_i\) is connected;
* each \(J_i\) meets \(A\); and
* every \(b\in B\) has a neighbour in each \(J_i\).

The A-parts of the bags are only required to be nonempty and disjoint.
Thus the allowed allocations are singleton/singleton or
singleton/complementary-pair.

## 2. Why the earlier \(\kappa=5\) model is not an obstruction

The first one-root search produced

\[
\begin{split}
 E(C)=\{&01,06,14,16,23,25,26,35,36,46,56\},\\
 N_C(a_0)=N_C(a_1)&=\{0,1,4,6\},\\
 N_C(a_2)&=\{2,3,5,6\},\\
 N_C(b_0)&=\{0,1,4\},\qquad N_C(b_1)=\{2,3,5\},\\
 N_C(b_2)&=\{0,2,3,4,5\},\qquad
 N_C(b_3)=\{0,1,2,3,4,5\}.
\end{split}                                           \tag{2.1}
\]

It has no two helpers of the restricted form
\(P\cup\{a_i\},Q\cup\{a_j\}\).  Nevertheless, the actual bags

\[
 J_1=\{a_0,a_2,0,2\},
 \qquad
 J_2=\{a_1,1,3,6\}                                   \tag{2.2}
\]

are disjoint, connected, A-rooted, and adjacent to all four vertices
of \(B\).  Thus (2.1) is not an obstruction to Lemma 1.1.  Any valid
search must allow a bag to use two A-roots.

## 3. Exact finite predicate

For a nonempty \(P\subseteq C\) and a nonempty
\(R\subseteq A\), the induced graph \(G[P\cup R]\) is connected if
and only if every component of \(C[P]\) has a neighbour in \(R\).
This equivalence uses that \(A\) is a clique.

Accordingly, for every \(P\) and every one of the seven nonempty root
subsets \(R\subseteq A\), the checker defines

\[
 h(R,P)\iff
 \begin{cases}
 \text{every component of }C[P]\text{ meets }N_C(R),\ 
 \text{and}\\
 P\cap N_C(b)\neq\varnothing\quad\text{for every }b\in B.
 \end{cases}                                          \tag{3.1}
\]

It asserts the absence of helpers by imposing

\[
 \neg\bigl(h(R,P)\wedge h(S,Q)\bigr)                 \tag{3.2}
\]

for every disjoint nonempty \(P,Q\subseteq C\) and every disjoint
nonempty \(R,S\subseteq A\).  Hence (3.2) forbids exactly the branch
sets sought above, not merely the simple one-root certificate.

The degree, boundary, and conditional neighbourhood constraints are
then literal translations of items 2--6 in Section 1.  In particular,
for each degree-seven \(x\) and each triple \(y,z,w\) of possible
neighbours, the checker asserts

\[
 xy,xz,xw\in E(G)\quad\Longrightarrow\quad
 E(G[\{y,z,w\}])\neq\varnothing.                     \tag{3.3}
\]

## 4. Exhaustion by the fixed graph \(C\)

There are 126 unlabelled connected seven-vertex graphs with 12 edges
and 95 with 13 edges.  The checker fixes each of these 221 possibilities
in turn and leaves only the 49 A/C and B/C incidences Boolean.

As a separate orbit-coverage check, summing
\(7!/|\operatorname{Aut}(C)|\) over the displayed atlas
representatives gives

\[
 290{,}745\quad(q=12),\qquad
 202{,}755\quad(q=13)                                  \tag{4.1}
\]

labelled graphs.  The checker now computes and asserts these two sums;
this guards against silently omitting an isomorphism class.

The first completed run returned

\[
 \boxed{221\ \mathrm{UNSAT},\quad0\ \mathrm{SAT},\quad0\ \mathrm{UNKNOWN}}.
                                                               \tag{4.2}
\]

The graph identifiers and their statuses, in atlas order, have digest

```text
graph6-id SHA256:
e9cc59585d83825c03de308caa6f775350e548e18e89342acadefbee03caf760

graph6-id/status SHA256:
ff15c316a703c69235124ce7431d8e01914c05881c04fb6dbd5be0f8aa562e42

checker-file SHA256:
aea1de233d30568694208458ea44a415c64f6c7637531c4438299f69b572a5fb
```

The reproducible program is `k34_c7_sparse_fixed.py`.  It uses
NetworkX only to obtain the standard graph atlas and induced components,
and Z3 for the 49-variable incidence problems.  It uses a 20-second
per-instance timeout, treats any timeout as `unknown`, asserts all counts
and both digests, and fails unless every instance is `unsat`.

## 5. Provisional consequence

Subject to independent audit of the encoding and rerun of (4.2), the
finite lemma says that hypotheses 1--6 force the two bags \(J_1,J_2\).
The four singleton bags on \(B\), together with \(J_1,J_2\), form an
\(N(v)\)-meeting \(K_6\)-model: the B-bags form a clique; each sees
both helpers; and the helpers see one another through the A-clique.
Adding \(\{v\}\) gives a \(K_7\)-minor.

Thus the sparse pairs (1.2) are computationally eliminated from the
seven-vertex exceptional cell.  This conclusion uses more than
seven-connectivity alone: it also uses contraction-critical
neighbourhood condition (3.3) and the sparse edge counts.  The dense
\(|C|=7\) branch is not addressed here.
