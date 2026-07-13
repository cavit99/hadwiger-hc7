# Expert-guided Hadwiger round: audited gains and exact residuals

## Status

This round does not prove Hadwiger's Conjecture, or even all of
\(\mathrm{HC}_7\).  It turns several suggested routes into precise lemmas,
rejects two attractive but false local principles, and closes one finite
exceptional cell by a reproducible computer-assisted proof.

The standing local setup is a proper-minor-minimal counterexample to
\(\mathrm{HC}_7\), a vertex \(v\) of degree seven,
\(H=G-v\), \(N=N_G(v)\), and

\[
 Q=\overline{G[N]}.
\]

Then \(Q\) is a nonempty triangle-free graph on seven vertices, and every
six-colouring of \(H\) uses all six colours on \(N\).

## 1. Every neighbourhood nonedge is accessible

For every \(xy\in E(Q)\), contract the connected set \(\{v,x,y\}\) to
\(q\).  The proper minor obtained has chromatic number exactly six.  In each
of its six-colourings, the five vertices
\(U=N-\{x,y\}\) avoid the colour of \(q\) and use the other five colours
bijectively.  Expanding the contraction gives a six-colouring of \(H\) in
which \(x,y\) are precisely the repeated pair on \(N\).

Thus repeated pairs can be prescribed along every edge of \(Q\); they are
not merely an unknown subset of the neighbourhood nonedges.

For such a pair, the missing-edge graph on the five unique roots is
\(F=Q-\{x,y\}\).  A seven-vertex argument then gives the exact dichotomy:

* some edge \(xy\) has \(F\) a pseudoforest; or
* \(Q=K_{3,4}\), equivalently \(G[N]=K_3\mathbin{\dot\cup}K_4\).

The proof of the exceptional alternative uses constant endpoint degree sum:
if every endpoint deletion leaves \(K_{2,3}\), then the connected graph
\(Q\) is regular or bipartite semiregular, and the only integral possibility
on seven vertices is \(K_{3,4}\).

## 2. What the two-component boundary states really force

If \(G-N[v]\) has two components \(C_1,C_2\), let
\(\mathcal E_i\) be the matchings of \(Q\) which occur as equality classes
on \(N\) in a six-colouring of \(G[N\cup C_i]\).  The following are proved:

1. every singleton \(\{e\}\), \(e\in E(Q)\), belongs to both families;
2. no matching of size two or three belongs to their intersection; and
3. for every \(e\) and each side \(i\), some matching
   \(R\in\mathcal E_i\) has \(e\in R\) and \(2\le |R|\le3\).

For (3), contract \(\{v,x,y\}\) for \(e=xy\) and contract the other
exterior component.  The two contracted vertices have distinct colours and
are both complete to the five remaining boundary vertices, forcing a second
boundary equality on the retained side.

Kempe swaps additionally give a no-reversal rule for exclusive support and
a commuting-swap rule for three disjoint pairs.  These abstract conditions
alone do not finish the Moser cells: explicit red/blue state systems satisfy
them.

A new two-anchor contraction does use the missing minor-critical information.
If \(ab,cd\) are disjoint neighbourhood nonedges and the other three
boundary vertices form a triangle, contract \(\{v,a,b\}\) and, for the
opposite side, \(C_j\cup\{c,d\}\).  On each retained side this forces the
same five-block boundary partition
\(ab\mid cd\mid x\mid y\mid z\).  The two side colourings then glue and the
sixth colour extends to \(v\), a contradiction.  In the classified
one-edge extension \(M+13\), the nonedges \(25,46\) leave the triangle
\(013\).  Hence that extension is impossible: the **pure Moser spindle is
the only remaining two-component degree-seven neighbourhood**.

For pure Moser, choosing repeated pair \(13\) leaves the missing-edge cycle
\(05,52,24,46,60\) on the five unique roots.  Confining all five
bichromatic connections to one exterior component would close the cell by
Kriesell--Mohr.  Four connections forming a spanning tree are not enough:
they yield only \(K_5-e\), so the corrected finite target is full \(C_5\)
confinement or an explicit mixed-pattern repair preserving the sixth bag.

## 3. Two local principles rejected by concrete graphs

### 3.1 Colour-preserving removable paths

There is an explicit graph
\(H=K_2\vee\overline{C_8}\), with a degree-seven apex neighbourhood
chosen inside it, for which

\[
 \kappa(H)=\kappa(G)=7,
\]

both relevant repeated pairs are genuinely accessible, and the five-root
missing graph has one edge, yet the proposed colour-preserving removable
path statement fails for both pairs.  The graph already has a \(K_7\)-minor
and is not edge-critical.  Therefore connectivity and accessible Kempe
data alone are insufficient.  Any repair must use additional global
counterexample information absent from this graph, for example
\(\eta(G)=6\) or proper-minor criticality.

What remains valid in the one-edge cell is an ordinary two-linkage
certificate.  If, after deleting the other three unique roots, there are
disjoint \(x\)-\(y\) and \(r\)-\(s\) paths, then splitting the second path
and using the first as a bag gives an \(N\)-meeting \(K_6\)-model.  The
two-disjoint-paths theorem therefore reduces a survivor to a three-sum web
with the four terminals alternating on its disk boundary.  The missing
step is to rule out that web using the double boundary states supplied by
edge-critical colourings.

### 3.2 Connectivity-only branch-bag splitting

The graph \(K_2\vee I\), where \(I\) is the icosahedral graph, has
\(\kappa=7\), minimum degree seven, and Hadwiger number six, but realizes
the locked attachment pattern that a proposed connectivity-only splitting
lemma was meant to forbid.  Thus the near-\(K_7\) route cannot use only
connectivity and many attachments to a branch bag; it needs some further
global input, with contraction-critical colouring information being the
mechanism isolated in the underlying note.

## 4. The exceptional \(K_3\dot\cup K_4\) cell

Write \(N=A\dot\cup B\), where \(G[A]=K_3\), \(G[B]=K_4\), and there
are no \(A\)-\(B\) edges.  The exterior is a single connected component
\(C\).  Minimum degree gives

\[
 |N_C(a)|\ge4\quad(a\in A),\qquad
 |N_C(b)|\ge3\quad(b\in B).
\]

Two disjoint connected sets in \(C\cup A\), each containing a distinct
vertex of \(A\) and each adjacent to every vertex of \(B\), together with
the four singleton \(B\)-bags and \(\{v\}\), form a \(K_7\)-model.

The elementary analysis proves:

* \(|C|\ne4,5\);
* every cutvertex of \(C\) has exactly two sides in the residual; three
  sides give an explicit six-bag rooted model;
* \(G[C\cup A]\) is two-connected; and
* an \(A\)-to-\(A\) st-numbering closes the cell whenever the four
  intervals determined by the \(B\)-neighbourhoods have a common cut.

### Full six-vertex certificate

The case \(|C|=6\) is now eliminated under the original lower bounds, not
only under an equality assumption.  For each balanced partition
\(C=P\dot\cup Q\), record which of the three \(A\)-roots connects each
side.  If at least five partitions admit distinct roots, four
\(B\)-vertices cannot block all of them.  If there are at most four, each
partition requires a different exact three-neighbourhood from \(B\); after
orienting those partitions, making every unused \(B\)-row complete to
\(C\) is a simultaneous coordinatewise maximum for all degree inequalities.

The standard-library verifier constructs all 112 connected unlabelled
six-vertex graphs and all 2024 multisets of three \(A\)-neighbourhoods for
each, for 226,688 states.  Exactly 63 degree-possible states have at most
four compatible partitions, and every orientation has negative minimum
degree slack.  An independent audit also enumerated all 148,995 possible
multisets of four \(B\)-rows for each of those 63 states and again found no
feasible obstruction.

That first certificate gives \(|C|\ge7\).  Order seven is now eliminated
by a stronger finite theorem which does not use its sparse density split.
For each of the 853 connected unlabelled seven-vertex graphs \(C\), the
solver keeps all \(A\)- and \(B\)-incidences free and imposes only the row
lower bounds, the 127 necessary consequences

\[
 |N_C(X)-X|+|N_N(X)|\ge7\qquad
 (\varnothing\ne X\subseteq C),
\]

and the absence of two disjoint \(A\)-rooted, \(B\)-complete helpers.
Helpers may use arbitrary disjoint nonempty subsets of the three-set \(A\),
not merely one root each.

All 853 instances were independently rerun in six shards.  The preserved
records contain 853 UNSAT results and no SAT or UNKNOWN result, cover every
atlas index exactly once, and have merged graph-ID/status digest

    fe854344e1c75336fa01d6bab426e1456e28a2f59ad46c9315dc82c11e72a946

Thus, computer-assistively,

\[
 |C|\ge8
\]

in this exceptional degree-seven cell.  The exact encoding and archived
run certificate are audited in hadwiger_k34_c7_kappa_audit.md.

## 5. Exact remaining scope

Even a complete solution of every cell above would address only a
degree-seven vertex in a hypothetical \(\mathrm{HC}_7\) counterexample.
The known bounds only place a minimum-degree vertex in degrees seven
through nine, so the degree-eight and degree-nine possibilities remain
untreated; this is not an assertion that counterexamples of either degree
exist.  The conjecture for \(t\ge8\) remains behind the uniform rooted-model
obstruction already recorded in `hadwiger_strongest_valid_derivation.md`.

The strongest current degree-seven endpoints are therefore:

1. make a pseudoforest rooted \(K_5\) certificate nonseparating, with the
   one-edge case reduced to edge-critical web elimination;
2. in the now-pure-Moser two-component cell, confine the full missing-edge
   \(C_5\) certificate to one side or resolve its mixed support patterns
   while preserving a sixth connector; or
3. in the exceptional cell with \(|C|\ge8\), construct two disjoint
   \(A\)-rooted, \(B\)-complete helpers (with the rooted-density route
   available only in its density branch).

None of these statements is silently assumed here.
