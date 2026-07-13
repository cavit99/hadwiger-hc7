# Decisive results from the current Hadwiger continuation

## 1. Scope and status

These results do not prove Hadwiger's Conjecture, and they do not yet prove
all of \(\mathrm{HC}_7\).  They give two new rigorous advances requested in
the continuation:

1. a reusable model-meeting theorem for almost-complete shores, with sharp
   new exterior-component bounds at degree eight and degree nine; and
2. a finite-boundary theorem which forces a two-sided bichromatic connection
   in the remaining pure-Moser two-component cell.

The higher-degree package has survived an independent adversarial audit.
The pure-Moser finite calculations have dependency-free verifiers, while the
displayed arguments below are the mathematical proofs.

## 2. Uniform two-defect shore packing

### Theorem 2.1

Let \(m\geq 3\), let \(N\) be a vertex set with \(|N|\geq m+2\), and let
\(C_1,\ldots,C_m\) be pairwise vertex-disjoint, pairwise anticomplete
connected subgraphs.  Suppose
that each \(C_i\) is adjacent to all but at most two vertices of \(N\).
Then there are distinct vertices \(x_i\in N\) such that

\[
   C_i\cup\{x_i\}\qquad(1\leq i\leq m)
\]

are the branch sets of an \(N\)-meeting \(K_m\)-model.

### Proof

Choose \(X\subseteq N\) with \(|X|=m+2\).  Enlarge the set of vertices of
\(X\) missed by \(C_i\), if necessary, to a two-element set \(e_i\).
It is enough to use the following incidence-free representative lemma.

> If a loopless multigraph has \(m\) labelled edges on \(m+2\) vertices,
> then its edges have distinct representatives \(f(e)\) such that
> \(f(e)\notin e\), and no two edges \(e,g\) satisfy both
> \(f(e)\in g\) and \(f(g)\in e\).

The lemma is proved by induction in
`hadwiger_degree8_degree9_exterior_bounds.md`.  Briefly, an isolated vertex
is assigned to any deleted edge.  Otherwise a degree-one vertex \(p\) and
its edge \(pq\) are deleted.  The only obstruction to assigning one of the
two unused representatives is that the edge represented by \(q\) is exactly
the pair of unused vertices; a three-edge rotation then resolves that
configuration.  The base case \(m=3\) is explicit.

Apply the lemma to \(e_1,\ldots,e_m\), and put \(x_i=f(e_i)\).  Every
\(C_i\cup\{x_i\}\) is connected.  If the bags for \(i,j\) had no cross-edge,
then \(C_i\) would miss \(x_j\) and \(C_j\) would miss \(x_i\), so
\(x_j\in e_i\) and \(x_i\in e_j\), contrary to the representative lemma.
Thus the bags are pairwise adjacent. \(\square\)

This is a genuine partial solution of the uniform model-meeting problem:
it converts nearly complete boundary contact into an integral rooted clique
model, rather than merely producing paths or a fractional contact system.

### Theorem 2.2 (uniform \(q\)-defect extension)

More generally, if the \(m\) shores each miss at most \(q\) vertices of
\(N\) and

\[
|N|\ge m+q^2,
\]

then they contain an \(N\)-meeting \(K_m\)-model.  Greedily choose a
representative \(x_i\) outside its miss set \(S_i\), the previously used
vertices, and every earlier \(S_j\) for which \(x_j\in S_i\).  If there
are \(h\) such earlier representatives, the forbidden union has size at
most

\[
(i-1)+q-h+hq\le i-1+q^2<|N|.
\]

The resulting representatives have no mutual incidence, so their shore
bags are pairwise adjacent.  The full proof and an explicit example showing
that the tempting bound \(m+q\) is false for \(q=3\) are in
`hadwiger_uniform_q_defect_shores.md`.  Theorem 2.1 remains sharper for
\(q=2\).

## 3. Consequences at degrees eight and nine for \(\mathrm{HC}_7\)

Let \(G\) be a hypothetical minor-minimal counterexample to
\(\mathrm{HC}_7\), let \(v\in V(G)\), and put \(N=N_G(v)\).  The graph is
seven-connected.  Hence every component \(C\) of \(G-N[v]\) satisfies

\[
   |N_G(C)|\geq 7,                                      \tag{3.1}
\]

because \(N_G(C)\subseteq N\) separates \(C\) from \(v\).

### Theorem 3.1

If \(d(v)=8\), then \(G-N[v]\) has at most three components.

### Proof

Otherwise choose four components.  Each misses at most one of the eight
vertices of \(N\).  The union \(M\) of their missed vertices has order at
most four.  Dirac's inequality gives \(\alpha(G[N])\leq3\), so
\(N-M\) contains adjacent vertices \(y,z\).  On the six-element set
\(N-\{y,z\}\), choose four distinct incidence-free representatives for
the four one-element miss sets (or use the explicit cyclic allocation in
the full note).  The four component bags and the singleton bags
\(\{y\},\{z\}\) form an \(N\)-meeting \(K_6\)-model.  Adding \(\{v\}\)
gives a \(K_7\)-minor. \(\square\)

### Theorem 3.2

If \(d(v)=9\), then \(G-N[v]\) has at most four components.

### Proof

Suppose that five components exist, and enlarge their miss sets to five
two-element sets, regarded as the edges of a multigraph \(F\) on \(N\).
If \(F\) has an isolated vertex \(y\), Theorem 2.1 gives five pairwise
adjacent component bags and \(\{y\}\) is adjacent to all of them.  These
six bags, followed by \(\{v\}\), give \(K_7\).

If \(F\) has no isolated vertex, its five edges cover all nine vertices,
so

\[
   F\cong P_3\mathbin{\dot\cup}3K_2.
\]

Some leaf \(y\) of \(F\) has a neighbor \(x\) in \(G[N]\) outside its
unique incident miss edge \(yz\).  Otherwise every edge of \(G[N]\) would
belong to \(F\), forcing
\(\alpha(G[N])\geq\alpha(F)=5\), contrary to Dirac's bound
\(\alpha(G[N])\leq4\).  If \(C_i\) has miss edge \(yz\), use
\(C_i\cup\{x\}\) as one bag.  Apply Theorem 2.1 to the other four shores
on the six vertices \(N-\{x,y,z\}\).  Their four bags, the special bag,
and \(\{y\}\) form an \(N\)-meeting \(K_6\)-model; add \(\{v\}\).
\(\square\)

The detailed proof and independent audit are in
`hadwiger_degree8_degree9_exterior_bounds.md`.

## 4. The two-component pure-Moser boundary theorem

Assume now that \(d(v)=7\), that

\[
 G-N[v]=C_1\mathbin{\dot\cup}C_2,
\]

and that \(G[N]\) is the pure Moser spindle with

\[
E(M)=\{01,02,03,04,12,16,26,34,35,45,56\}.
\]

The previously classified one-edge extension is excluded by the two-anchor
contraction in `hadwiger_moser_two_anchor_elimination.md`; hence this is the
only remaining two-component degree-seven neighborhood.

Choose the exact trace with repeated pair \(13\).  On the five unique roots
\(U=\{0,2,4,5,6\}\), the missing edges are the cycle

\[
 05,25,24,46,06.                                       \tag{4.1}
\]

For a missing edge, record whether its bichromatic connection is supported
inside \(C_1\), inside \(C_2\), or inside both; write \(1,2,B\).

### Theorem 4.1

Every purely binary mixed support word is impossible.  More precisely, up
to dihedral symmetry and interchange of the components, the following five
of the fourteen mixed ternary support orbits are impossible:

\[
11112,\quad11122,\quad11212,\quad1121B,\quad1212B.       \tag{4.2}
\]

Consequently every surviving mixed trace has a missing edge supported in
both exterior components.

### Proof mechanism

For each cycle edge \(e_i\), let \(D_i=\{13,e_i\}\).  When \(e_i,e_j\)
are vertex-disjoint, let \(T_{ij}=\{13,e_i,e_j\}\).  Three facts hold:

1. no \(D_i\) or \(T_{ij}\) extends to both sides, since the two side
   colorings would glue and use at most five colors on \(N\);
2. the two-anchor contraction forces, on each side, one of \(D_i\) or the
   two possible triples extending it; and
3. if a side does not support \(e_i\), a Kempe swap puts \(D_i\) on that
   side; two unsupported disjoint edges give \(T_{ij}\) by commuting
   swaps.

The disjointness graph of the five cycle edges is another \(C_5\).  If a
side owns \(D_i\) and both triples incident with \(i\), exclusivity leaves
the other side no state allowed by item 2.  Repeated propagation gives
(4.2).  The complete hand propagation and the independent verifier are in
`hadwiger_moser_pentagon_boundary_lemma.md` and
`moser_pentagon_state_verify.py`.

### Theorem 4.2 (binary-support cut criterion)

The preceding argument is neighborhood-independent.  In any
two-component degree-seven exact trace, let \(P_r\) be the graph whose
vertices are missing edges among the five unique roots, adjacent when the
two missing edges are vertex-disjoint.  For a purely binary support
assignment, let \(K_r\) be the cut subgraph of \(P_r\) joining differently
supported edges.  The boundary-state axioms are feasible if and only if
every component of \(K_r\), including isolated vertices, contains a cycle.

Indeed, a cut edge's triple state can be assigned to at most one side.
Orient it toward the endpoint whose supporting side receives that state.
Two-anchor coverage is exactly the requirement that every vertex have
positive indegree.  Such an orientation exists precisely when every
component contains a cycle.

In particular, if \(P_r\) has no even cycle, then either one component
supports every missing edge (which already yields the confined rooted
model), or some edge is supported by both components.

For the ten exact traces of the pure Moser spindle,

\[
\begin{array}{c|c}
r&P_r\\ \hline
05,06&C_6\\
13,14,23,24&C_5\\
15,25,36,46&P_5.
\end{array}
\]

Thus eight of the ten traces force a two-sided edge unless the minor is
already obtained.  In the \(05,06\) traces, the only purely binary
survivors are the two alternating colorings of the disjointness \(C_6\).

## 5. Two closures in the pure-Moser four-plus-one cell

Continue with repeated pair \(13\) and the missing cycle (4.1).  Suppose
\(C_1\) supports four cycle edges and misses only \(e=xy\).  The four
supported edges give rooted bags \((B_u:u\in U)\) which form
\(K_5-e\).

First, if the other component \(C_2\) contains disjoint paths joining
\(1\) to \(3\) and \(x\) to \(y\), split the latter path between
\(B_x,B_y\) and use the former as the sixth bag.  This is an explicit
\(N\)-meeting \(K_6\)-model.

Two entire subfamilies can be closed without assuming that linkage:

* If \(e=05\), vertex \(3\) is adjacent to both ends.  Absorb \(3\) into
  \(B_0\), and use \(C_2\cup\{1\}\) as the sixth bag.  If \(e=06\), use
  \(1\) and \(C_2\cup\{3\}\) symmetrically.
* If \(C_2\) has a cutvertex \(z\), split it into adjacent connected
  shores \(D,E\).  Seven-connectivity forces each shore to meet at least
  six vertices of \(N\).  Delete one endpoint bag of \(e\), leaving four
  mutually adjacent rooted bags.  Two distinct anchors from
  \(\{1,3,o\}\), where \(o\) is the deleted root, can always be assigned
  to \(D,E\) so that the resulting shore bags meet and are adjacent to all
  four rooted bags.  The finite anchor table is checked by
  `moser_cutvertex_assignment_verify.py`.

The full proof is `hadwiger_moser_4plus1_closures.md`.  Its exact residual
is now:

\[
e\in\{25,24,46\},
\]

the minority component is connected and cutvertex-free (without silently
excluding components of order one or two), at least one majority edge is
bi-supported there, and it is a two-disjoint-paths obstruction for terminal
pairs \((1,3)\) and the ends of \(e\).

A further two-cut lemma splits the minority component into two adjacent
shores, each missing at most two boundary vertices.  Explicit multi-anchor
assignments first leave 50 physical defect pairs.  Exhaustive clique-minor
checking in the resulting nine-vertex shore quotient closes another 17,
leaving exactly 11 pairs for each of \(e=25,24,46\).  The complete tables
and branch-set checks are in the same proof note and in
`moser_2cut_assignment_verify.py` and `moser_2cut_quotient_verify.py`.
Those 33 pairs are the only two-cut geometries still needing the mandatory
bi-supported majority path.

## 6. One-step minor transitions

The abstract state system across all ten traces is consistent; the
dependency-free certificate is `moser_all_trace_state_certificate.py`.
Therefore geometry or minor transitions are essential.  The following
additional criticality statement is proved in
`hadwiger_two_side_minor_transition.md`.

If a vertex or edge on side \(i\) is deleted, or an edge on that side is
contracted, every resulting proper-minor coloring induces a boundary
matching state \(R\) of order two or three such that

\[
R\in\mathcal E_{3-i},\qquad R\notin\mathcal E_i,
\]

while \(R\) extends to the modified side.  For an internal deleted edge
\(xy\), its endpoints have the same color in every witness coloring, see
every other color, and lie in one two-color component for every other
color.  This is the exact one-step information absent from the finite
state countercertificate.

## 7. Elimination of the two smallest one-component pure-Moser cells

There is also a certified closure on the one-component side.

### Theorem 7.1 (computer-assisted)

Let \(d(v)=7\), let \(G[N(v)]\) be the pure Moser spindle, and suppose
\(G-N[v]=C\) is connected, \(\delta(G)\ge7\), and \(\kappa(G)\ge7\).
Then \(|C|=4\) implies that \(G\) has a \(K_7\)-minor.

Order four is the first possible order: deleting
\(C\cup\{v,0,6\}\) separates the edge \(12\) from the triangle \(345\),
so seven-connectivity gives \(|C|+3\ge7\).

For \(|C|=4\), there are six connected unlabelled choices for \(G[C]\)
and 28 possible boundary-incidence edges.  A finite Boolean certificate
imposes only the necessary degree and attachment constraints, then records
valid clauses of two types:

* every cut of order at most six requires an optional cross-edge; and
* every explicit seven-bag clique model requires at least one of its
  optional witness edges to be absent in a minor-free completion.

All six resulting systems are unsatisfiable, with respectively

\[
37,40,88,113,154,180
\]

verified clauses.  The independent replay enumerates the six graph types,
checks every cut partition and every branch-set witness, and reruns the final
Z3 unsatisfiability tests.  The proof note is
`hadwiger_moser_one_component_c4.md`; the replay is `moser_c4_verify.py`.
The same certified method also eliminates \(|C|=5\).  It treats all 21
connected unlabelled five-vertex exteriors and all 35 possible boundary
incidences.  The four archived shards contain 25,474 verified cut/minor
clauses in total.  The merged verifier independently enumerates all 21
graph types, checks every clause and seven-bag witness, and reruns every
final UNSAT instance in Z3.  See
`hadwiger_moser_one_component_c5.md` and `moser_c5_verify.py`.

Consequently a one-component pure-Moser residual has

\[
\boxed{|C|\ge6}.
\]

## 8. Exact remaining gaps

The present work meets the continuation's success criteria through both a
new uniform model-meeting lemma and substantial degree-eight/nine progress.
It does not close the full conjecture.  The remaining local gaps include:

* the balanced pure-Moser support orbits and the cutvertex-free
  four-plus-one residual with minority edge \(25,24\), or \(46\);
* the one-component degree-seven rooted-certificate lock with, in the
  pure-Moser cell, exterior order at least six;
* degree eight with at most three exterior components and degree nine with
  at most four; and
* the general contact problem outside the two-defect shore regime.
