# Order-eight exceptional cell: bounded probe status

This note records the bounded \(|C|=8\) probe and its exact stopping
point.  It proves neither the order-eight helper lemma nor a
counterexample, and it makes no claim about \(\mathrm{HC}_7\).

## 1. Predicate searched

The discovery script `k34_c8_probe.py` has Boolean variables for all
edges of the eight-vertex graph \(C\) and all A/C and B/C incidences.
It imposes:

* \(C\) connected;
* every A-row has order at least four and every B-row at least three;
* \(d_C(x)+d_A(x)+d_B(x)\geq7\) for every \(x\in C\); and
* no two actual Lemma 1.1 helpers.

For the last condition, a helper may use any nonempty root set
\(R\subseteq A\), including two A-vertices.  For every nonempty
\(P\subseteq C\), the encoding uses the exact equivalence

\[
 P\cup R\text{ connected}
 \iff
 \text{every component of }C[P]\text{ has a neighbour in }R.
\]

It also requires \(P\) to meet all four B-rows, then forbids every pair
with disjoint C-parts and disjoint nonempty A-parts.

The 255 necessary seven-connectivity inequalities

\[
 |N_G(X)|\geq7\qquad(\varnothing\neq X\subseteq C)     \tag{1.1}
\]

are added lazily whenever a model violates one.

## 2. First no-helper model

Before adding (1.1), the qffpbv run found

\[
\begin{split}
E(C)=\{&02,05,06,07,17,25,26,27,34,37,47,56,57,67\},\\
N_C(a_0)=N_C(a_1)=N_C(a_2)&=\{1,3,4,7\},\\
N_C(b_0)&=\{0,1,2,3,4,5\},\\
N_C(b_1)&=\{0,2,6\},\\
N_C(b_2)&=\{1,5,6\},\\
N_C(b_3)&=\{0,1,2,3,4,5,6\}.
\end{split}                                           \tag{2.1}
\]

This model is not a connectivity counterexample.  It violates (1.1)
on the masks

\[
 5,24,37,69,97,100,101.                               \tag{2.2}
\]

In particular, its three identical tight A-rows illustrate the
tight-row covering obstruction from Lemma 4.1 of
`hadwiger_k34_c7_kappa_audit.md`.

## 3. Lazy-boundary trace

Successive SAT models produced the following new violated masks:

\[
\begin{array}{c|l|c}
\text{stage}&\text{new masks}&\text{cumulative}\cr
1&5,24,37,69,97,100,101&7\cr
2&3,9,10,11,180&12\cr
3&13,21,25,28,29&17\cr
4&12,35,132,136,140&22\cr
5&40,56,72,88,96,104,112,120&30.
\end{array}                                           \tag{3.1}
\]

For reference, the first seventeen masks in set notation are

\[
\begin{gathered}
\{0,2\},\{3,4\},\{0,2,5\},\{0,2,6\},
\{0,5,6\},\{2,5,6\},\{0,2,5,6\},\\
\{0,1\},\{0,3\},\{1,3\},\{0,1,3\},\{2,4,5,7\},\\
\{0,2,3\},\{0,2,4\},\{0,3,4\},\{2,3,4\},
\{0,2,3,4\}.
\end{gathered}                                        \tag{3.2}
\]

Because control messages crossed while the solver was running, the
17-mask solve was not the final interrupted solve: it returned SAT and
the run advanced through the 22-mask SAT model.  The solve with all 30
masks in (3.1) was then manually interrupted after the agreed bounded
checkpoint and returned `unknown`.  Thus `unknown` records interruption,
not a solver-derived timeout or a mathematical third outcome.

## 4. Exact remaining gap

The next computational question is:

> Are the connectedness, row, degree, exact no-helper, and **all 255**
> inequalities (1.1) jointly satisfiable?

The current trace enforces only 30 of the 255 inequalities, so it does
not answer that question.

* If SAT, the complete incidence model must be extracted and the full
  sixteen-vertex host checked for \(\kappa(G)\geq7\).  The shore
  inequalities are necessary but not by themselves a certificate of
  full connectivity.
* If UNSAT, the computation would give a finite order-eight helper
  lemma, but only after a frozen exhaustive run, preserved records, and
  an independent encoding audit comparable to the order-seven audit.

The conceptual alternative remains to uncross the tight seven-boundary
shores in the tight-cover obstruction: one must prove that they and the
tight A4/B3 rows cannot cover every non-cutvertex of \(C\).  No such
uncrossing proof was obtained in this bounded round.
