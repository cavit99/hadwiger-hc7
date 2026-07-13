# Audit of the expert-round synthesis

## Verdict

The mathematical gains and residuals in
hadwiger_expert_round_synthesis.md agree with the underlying notes.  In
particular:

* the order-seven density split is arithmetically exact;
* both local counterexamples have the connectivity, degree, colouring,
  and minor properties attributed to them;
* the order-six computer-assisted conclusion is reported with its correct
  scope; and
* degree eight and degree nine are untreated possibilities allowed by the
  known minimum-degree bound, not cases proved to occur.

Three sentences were patched to avoid drawing an unnecessarily exclusive
conclusion from the counterexamples.  The examples prove that their listed
local data are insufficient; they do not prove that one particular extra
hypothesis is the only possible repair.  The final degree sentence was
also rewritten so that “can be eight or nine” cannot be misread as an
existence assertion.

## 1. The order-seven density split

For \(|C|=7\), put

\[
p=e(C,N),\qquad q=e(C).
\]

The boundary degree bounds give \(p\ge24\), and summing the degree-seven
lower bound over the seven vertices of \(C\) gives

\[
p+2q\ge49.
\]

The rooted density theorem applies at

\[
p+q\ge4|C|+10=38.
\]

Failure of this threshold means \(p+q\le37\).  Combining the three integer
inequalities gives \(p\le25\).  If \(p=24\), then
\(q\ge\lceil(49-24)/2\rceil=13\) and \(q\le13\), so \(q=13\).  If \(p=25\),
then \(q\ge12\) and \(q\le12\).  Hence the only possibilities are exactly

\[
(p,q)=(24,13),(25,12).
\]

This arithmetic split remains correct as an intermediate observation.
It has since been superseded by the independently certified 853-type
kappa-only computation, which eliminates every connected seven-vertex
\(C\) without using the sparse totals or the conditional Dirac constraints.

For nonempty \(X\subseteq C\), its external neighbourhood separates it
from \(v\).  Seven-connectivity therefore gives

\[
|N_C(X)\setminus X|+|N_N(X)|\ge7.
\]

Since \(|N_C(X)\setminus X|\le7-|X|\), it follows that
\(|N_N(X)|\ge|X|\).  Thus the stated Hall condition for the
\(C\)-to-\(N\) incidence graph is also valid.

## 2. The colour-preserving removable-path counterexample

The synthesis accurately summarizes the graph from
hadwiger_kempe_removable_round.md:

\[
H=K_2\vee\overline{C_8},
\]

with the specified seven-vertex neighbourhood \(N\) and a new apex \(v\).
The verified properties are

\[
\chi(H)=6,\quad\chi(G)=7,\quad
\kappa(H)=\kappa(G)=7,\quad\delta(G)=7,
\]

and

\[
\overline{G[N]}=\{bc,de\}.
\]

The two perfect matchings of the cycle give the only two accessible
boundary colour patterns.  Each leaves a one-edge missing graph, and in
each pattern every repeated-pair path deletes a vertex of the unique
required bichromatic path.  Thus CP--RP really fails for both accessible
pairs.

The graph is correctly excluded from the genuine counterexample class:
the seven bags displayed in the underlying note give a \(K_7\)-minor
already in \(H\), and deletion of the edge \(pb\) leaves \(G\) seven
chromatic, so the graph is not edge-critical.

The original synthesis said that a repair “must use” either
\(\eta(G)=6\) or proper-minor criticality.  The example proves only that
the listed local connectivity and Kempe data do not suffice.  Conceivably
another global counterexample property could also exclude it.  The patched
wording now says that additional global input is required and gives minor
exclusion and criticality as examples.

The subsequent two-linkage and web summary matches
hadwiger_one_edge_web_round.md: a disjoint
\((x,y),(r,s)\)-linkage gives the six bags directly, while the
Robertson--Seymour--Thomas alternative leaves a three-separation/disk web
obstruction.  The synthesis does not claim that the web has been
eliminated.

## 3. The \(K_2\vee I\) counterexample

For the icosahedral graph \(I\),

\[
\kappa(I)=5,\qquad \delta(I)=5,\qquad \eta(I)=4.
\]

The last equality follows because \(I\) is planar and contains a
\(K_4\)-minor.  Joining two adjacent universal vertices therefore gives

\[
\kappa(K_2\vee I)=7,\qquad
\delta(K_2\vee I)=7,\qquad
\eta(K_2\vee I)=6.
\]

The seven branch sets in hadwiger_near_k7_split_round.md are disjoint,
connected, spanning, and have only the \(t\)-\(b\) adjacency missing.
The deficient singleton has seven attachments into five other bags, with
three attachments in the large icosahedral bag.  Since the host has
Hadwiger number six, no connectivity-only splitting conclusion can be
valid.

As with CP--RP, the example refutes the local implication but does not
logically prove that critical colouring is the only conceivable additional
input.  The synthesis was patched to state the precise negative conclusion
and to identify contraction-critical colouring as the mechanism isolated
by the underlying note.

## 4. Degree-eight and degree-nine scope

For a minor-minimal \(\mathrm{HC}_7\) counterexample, the audited bounds are

\[
7\le\delta(G)\le9.
\]

Choosing a minimum-degree vertex therefore yields degree seven, eight, or
nine.  All of the repeated-pair, five-root, and exceptional
\(K_3\dot\cup K_4\) work in the synthesis assumes that the chosen vertex
has degree exactly seven.  If the minimum degree were eight or nine, none
of those degree-seven reductions would apply directly.

The former wording that the minimum degree “can also be eight or nine”
could be read as claiming examples.  No such counterexample is known or
constructed.  The patched text now says only that the known bounds permit
those two untreated possibilities.

## 5. Other synthesis claims

The remaining sections also match their sources:

* full accessibility follows from the triple contraction and holds for
  every edge of \(Q\);
* the only seven-vertex all-hard deletion graph is \(K_{3,4}\);
* the two boundary-state families have all singleton states, disjoint
  higher states, and a higher-state cover on each side;
* the red/blue Moser systems show that these abstract state axioms alone
  do not close the two-component cell;
* the six-vertex exceptional cell is eliminated under the original lower
  bounds by the audited exhaustive certificate; and
* the exact surviving order bound there is now \(|C|\ge8\), not a closure of
  the whole exceptional cell.

No further factual overstatement was found.
