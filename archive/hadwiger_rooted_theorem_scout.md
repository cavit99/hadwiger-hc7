# Rooted-minor theorem scout for the audited \(\mathrm{HC}_7\) residual

## 0. Executive conclusion

No theorem located below closes the degree-seven cell or upgrades the
Norin--Totschnig near-clique by itself.  Two useful conclusions do emerge.

1. The most promising degree-seven target is not a generic nonseparating
   rooted-\(K_5\) theorem.  Such a theorem is false at exactly the available
   connectivity.  The right target is a **colour-preserving removable-path
   lemma**: find an \(a\)-\(b\) path whose deletion preserves the particular
   bichromatic connections used by the Kriesell--Mohr certificate.
2. A connectivity-only splitting lemma for a spanning \(K_7^-\) or
   \(K_7^\vee\) model is also false.  Any successful near-clique proof has to
   use contraction-critical colour witnesses, not merely seven-connectivity,
   minimum degree, the absence of a \(K_7\)-minor, or a large number of
   portals.

The two concrete mechanisms recommended in Sections 7 and 8 are therefore:

* combine Rolek--Song's exterior bichromatic paths with the
  Du--Li--Xie--Yu critical-feasibility machinery, keeping an \(a\)-\(b\)
  path disjoint from a Kriesell--Mohr certificate; and
* minimize a near-clique model and use colourings of contractions of edges
  in a multiply-hit bag to force a duplicate portal or a valid pendant
  transfer.

All statements marked **established** below are published or explicitly
identified preprints/theses.  Statements marked **target** are not known
theorems.

## 1. The exact degree-seven object

Let \(G\) be a proper-minor-minimal counterexample to \(\mathrm{HC}_7\), let
\(v\) have degree seven, and put

\[
 H=G-v,\qquad N=N_G(v).
\]

Then

\[
 \kappa(G)\ge 7,\qquad \kappa(H)\ge 6,\qquad |N|=7,
 \qquad \alpha(G[N])=2.
\]

Fix a six-colouring arising by contracting a nonedge \(\{a,b\}\subseteq N\)
together with \(v\).  After expansion to \(H\), \(a,b\) have the repeated
colour and

\[
 U=N-\{a,b\}=\{u_1,\ldots,u_5\}
\]

has five distinct colours.  Put

\[
 F=\overline{H[U]}.
\]

The graph \(F\) is triangle-free and has at most six edges.  Every edge
\(u_i u_j\in E(F)\) has its ends in the same \((i,j)\)-bichromatic
component.  Kriesell--Mohr therefore gives a rooted \(K_5\)-model on \(U\),
but it need not leave \(a\) and \(b\) in the same complementary component.

The desired outcome can be phrased as a coloured rooted \(K_6\)-model with
terminal partition

\[
 \{u_1\},\{u_2\},\{u_3\},\{u_4\},\{u_5\},\{a,b\}.             \tag{1.1}
\]

This is stronger than a rooted \(K_5\) and different from ordinary
six-linkage.

## 2. The theorem registry

### 2.1 Rolek--Song: contraction-critical exterior Kempe paths

**Established.**  Rolek and Song, *Coloring Graphs with Forbidden Minors*,
JCTB 127 (2017), Lemma 1.7.

In the form relevant here, let \(x\) have degree \(k+s\) in a
\(k\)-contraction-critical graph, let
\(S\subseteq N(x)\) be an independent set of order \(s+2\), and suppose
\(\alpha(N(x))=s+2\).  After contracting \(S\cup\{x\}\), the vertices of
\(N(x)-S\) receive distinct colours.  Specified missing edges grouped into
stars have paths whose internal vertices lie outside \(N[x]\); path groups
with disjoint terminal sets are mutually vertex-disjoint.  In the current
arXiv statement the grouping is subject to

\[
 \sum_i r_i+m\le k-2,
\]

where the \(i\)-th star has \(r_i\) edges and there are \(m\) stars.
In particular, paths for a matching of missing edges are pairwise disjoint.

For \(k=7,s=0,x=v,S=\{a,b\}\), this applies exactly to missing edges of
\(H[U]\), and every path has its interior in \(G-N[v]\).

**Applicability.**  This is the strongest theorem found that explicitly
uses the contraction colouring and operates in the correct exterior
region.  It does not say that all paths within one star are internally
disjoint, nor that the whole certificate avoids a prescribed
\(a\)-\(b\) path.  Those are precisely the missing packing assertions.

Source: <https://arxiv.org/abs/1606.05507>.

### 2.2 Kriesell--Mohr: property \((*)\) on five vertices

**Established.**  Kriesell and Mohr, *Kempe Chains and Rooted Minors*,
Theorem 7.

Every graph on five vertices with at most six edges has property \((*)\).
Consequently, if the ends of every edge of such a graph \(F\) are joined
by the corresponding bichromatic component, there are disjoint connected
root bags realizing all edges of \(F\).  Direct edges between roots can be
added to obtain the rooted \(K_5\) used above.

**Applicability.**  It proves the five-bag part of (1.1).  It has no
avoidance or nonseparation clause.  Applying it in \(H\) and then invoking
six-connectivity does not control the union of its five bags.

Source: <https://arxiv.org/abs/1911.09998>.

### 2.3 Du--Li--Xie--Yu: critical feasibility and removable paths

**Established.**  Du, Li, Xie and Yu, *Linkages and Removable Paths
Avoiding Vertices*, JCTB 169 (2024), Theorems 1.2 and 1.5.

For an \(m\)-rooted graph

\[
 \mathcal G=(J,\{x_1,\ldots,x_m\},p,q),
\]

call \(\mathcal G\) feasible if there is a \(p\)-\(q\) path \(P\) such
that all \(x_i\) lie in one component of \(J-P\).  For a terminal set
\(T=\{x_1,\ldots,x_m,p,q\}\), a \(T\)-collection is a collection
\(\mathcal X\) of subsets of \(V(J)-T\) such that

\[
 N[X_1]\cap X_2=\varnothing
 \quad\text{for distinct }X_1,X_2\in\mathcal X.
\]

The graph \(J/\mathcal X\) is obtained by deleting every \(X\in\mathcal X\)
and completing \(N_J(X)\) to a clique.  The augmented rooted graph
\(\mathcal G/\mathcal X\) additionally receives every edge among the
terminals except \(pq\).

Theorem 1.2 says that either \(\mathcal G\) is feasible or there is a
\(T\)-collection \(\mathcal X\) with

\[
 |N_J(X)|\le m+1 \quad(X\in\mathcal X)                       \tag{2.1}
\]

and

\[
 e(\mathcal G/\mathcal X)
 \le (m+1)v(J/\mathcal X)-\frac{m^2}{2}-\frac{3m}{2}-1.       \tag{2.2}
\]

Corollary 1.3 and Theorem 1.5 imply that every
\((2m+2)\)-connected graph is \((2,m)\)-linked and has a \(p\)-\(q\)
path avoiding the \(m\) nominated vertices whose deletion leaves the graph
connected.

#### Exact specialization to D7

Take \(J=H\), \(m=5\), roots \(U\), and \(p=a,q=b\).  Every member
\(X\) of the collection is disjoint from \(T=N(v)\).  If it were nonempty
and \(|N_H(X)|\le6\), then \(N_H(X)\) would separate \(X\) from \(v\) in
\(G\), since \(v\) has no neighbour in \(X\).  This contradicts
\(\kappa(G)\ge7\).  Hence the collection in the infeasible outcome must be
empty.  Writing

\[
 H^+=H+\{xy:x,y\in N,\ xy\ne ab\},
\]

Theorem 1.2 yields the clean alternative

\[
 \boxed{\begin{array}{l}
 \text{there is an }a\text{-}b\text{ path }P\text{ with }U
 \text{ in one component of }H-P,\\[2mm]
 \text{or }e(H^+)\le6|H|-21.
 \end{array}}                                                \tag{2.3}
\]

This is genuine progress, but not closure.  A feasible path only leaves
the five roots in one connected component; it does not preserve their
bichromatic connections and does not put a rooted \(K_5\) in that
component.

The density alternative is compatible with all current bounds.  If
\(n=|H|\), Mader's \(K_7\)-minor extremal bound gives

\[
 e(H)=e(G)-7\le5n-17.
\]

Since \(\alpha(H[N])=2\), the complement of \(H[N]\) is triangle-free,
so \(e(H[N])\ge9\).  Thus \(H^+\) adds at most eleven edges and

\[
 e(H^+)\le5n-6,
\]

which is already below \(6n-21\) for \(n\ge15\).  Therefore (2.2) is an
upper bound in the wrong direction for a direct density contradiction.

The graph \(H^+\) is always six-connected.  It need not be
seven-connected.  Its only possible exceptional six-cut not immediately
contradicting seven-connectivity of \(G\) has the form

\[
 U\cup\{z\},
\]

with \(a,b\) on different sides; after deletion of this set, the terminal
remainder is exactly the unique nonedge \(ab\), and \(v\) reconnects the
two sides in \(G\).

Source: <https://arxiv.org/abs/2303.12146>.

### 2.4 Xie's \((2,3)\)-linkage theorem

**Established in a dissertation.**  Shijie Xie, *6-Connected Graphs Are
Two-Three Linked* (Georgia Tech PhD thesis, 2019), Theorem 1.2.1.

For distinct \(a_0,a_1,a_2,b_1,b_2\), if adding \(b_1b_2\) and all six
edges \(a_i b_j\) makes the graph six-connected, then there are two
disjoint connected subgraphs containing \(\{a_0,a_1,a_2\}\) and
\(\{b_1,b_2\}\), respectively.  In particular every six-connected graph
is \((2,3)\)-linked.  The 2024 Du--Li--Xie--Yu paper records the equivalent
removable-path value \(f(3)=6\) as Xie's thesis result.

**Applicability.**  In \(H\), it can protect any chosen triple of \(U\)
while joining \(a,b\), but it cannot protect all five roots.  Iterating the
theorem is not legitimate because deleting the first linkage destroys the
connectivity hypothesis.  It is nevertheless a plausible exchange engine:
for every triple \(T\subset U\), choose a nonseparating \(a\)-\(b\) path
avoiding \(T\), then compare the traces of these paths on \(U-T\).

Source: <https://repository.gatech.edu/items/83a4c974-d776-4648-9620-9c2424e5c7c8>.

### 2.5 Rooted \(K_4\), rooted cycles, and their limits

**Established.**

* Fabila-Monroy and Wood, *Rooted \(K_4\)-Minors*, Theorem 6: in a
  four-connected graph, four nominated vertices root a \(K_4\)-minor
  unless the graph is planar and the four vertices lie on a common face.
  Theorem 9 gives the corresponding three-connected planar statement.
* Robertson--Seymour--Thomas's rooted-\(C_4\) characterization, as quoted
  and used by Du--Li--Yu, implies that a graph with no specified rooted
  \(C_4\)-minor has connectivity at most five.
* Du, Li and Yu, *Rooted \(C_5\)-Minors* (2025), prove in particular that
  ten-connectivity forces a \(C_5\)-minor rooted in any prescribed order.

**Applicability.**  The rooted-\(K_4\) and rooted-\(C_4\) results can settle
four-terminal subconfigurations, but the hard complement
\(F\cong K_{2,3}\) requires six missing adjacencies on five roots.  The
rooted-\(C_5\) theorem needs ten-connectivity, whereas \(H\) is only
six-connected, and even a rooted cycle would supply only the cycle edges of
\(F\).

Sources:

* <https://arxiv.org/abs/1102.3760>;
* <https://arxiv.org/abs/2510.27161>.

### 2.6 Ordinary linkage theorems

**Established.**

* Thomas--Wollan, *The Extremal Function for 3-Linked Graphs*, Theorem
  1.1: a six-connected \(n\)-vertex graph with at least \(5n-14\) edges is
  three-linked.  Corollary 1.2: every ten-connected graph is three-linked.
* Chen--Gould--Kawarabayashi--Pfender--Wei, *Graph Minors and Linkages*,
  Theorems 1.1 and 1.2: six-connectivity plus a \(K_9^-\)-minor forces
  three-linkage, and seven-connectivity plus a \(K_9^-\)-minor forces
  \((2,5)\)-linkage.
* The 2024 graph-minor linkage theorem strengthens the general
  Robertson--Seymour condition: a \(2k\)-connected graph with a
  \(K_{3k}\) minor minus an independent matching of size \(k\) is
  \(k\)-linked.

**Applicability.**  The present graphs have neither the edge lower bound
nor a \(K_9^-\)-model.  A \(K_7^\vee\)-model is substantially too small.
Moreover, three-linkage does not directly realize the five-bag clique
certificate.

Sources:

* <https://thomas.math.gatech.edu/PAP/3link.pdf>;
* <https://doi.org/10.1002/jgt.20067>;
* <https://doi.org/10.1016/j.ejc.2023.103874>.

### 2.7 Knittedness

**Established.**

* Liu--Rolek--Yu, *Minimum Degree Condition for a Graph to Be Knitted*,
  Theorem 2: if \(n\ge2k+3\) and
  \(\delta(J)\ge(n+k)/2-1\), then \(J\) is \(k\)-knitted.
* Kawarabayashi--Yu, *Connectivities for k-Knitted Graphs and for Minimal
  Counterexamples to Hadwiger's Conjecture* (2026), main theorem: every
  \(8\ell\)-connected graph is \(\ell\)-knitted.  The paper explicitly
  corrects a gap in an earlier claimed bound.

**Applicability.**  Partition (1.1) involves seven terminals.  Generic
seven-knittedness would require connectivity 56 from the newest theorem;
the degree theorem requires a global minimum degree close to \(n/2\).
Neither is available.  Even knittedness alone connects prescribed terminal
parts but does not create the ten pairwise adjacencies among the five
singleton parts.

Sources:

* <https://arxiv.org/abs/1811.07482>;
* <https://arxiv.org/abs/2606.01586>.

### 2.8 Nonseparating subdivisions and removable paths

**Established.**

* Kriesell, *Nonseparating \(K_4\)-Subdivisions in Graphs of Minimum
  Degree at Least 4*, Corollary 1: for every vertex \(x\) of a
  four-connected graph, there is a subdivision of \(K_4\) avoiding \(x\)
  whose deletion leaves a connected graph containing \(x\).
* Tutte's path theorem: in a three-connected graph, for prescribed
  \(p,q,r\), there is a \(p\)-\(q\) path avoiding \(r\) whose deletion
  leaves the graph connected.
* The Lovasz path-removal problem is not known at the general connectivity
  level that would preserve a large connected or highly connected
  remainder.  Du--Li--Xie--Yu give the precise modern bound relevant to
  avoiding a fixed number of nominated vertices, discussed above.

**Applicability.**  Kriesell's subdivision is unrooted and has only four
branch vertices.  The theorem cannot prescribe the five vertices \(U\).
Tutte's theorem protects one nominated vertex, not five roots and their
bichromatic components.

Source: <https://arxiv.org/abs/1101.5278>.

### 2.9 Root-preserving compression and vital linkage

**Established.**

* Bohme--Harant--Kriesell--Mohr--Schmidt, *Rooted Minors and Locally
  Spanning Subgraphs*, Theorem 3: if the local connectivity
  \(\kappa_J(X)\ge k\), for \(k\in\{1,2,3,4\}\), then \(J\) has a
  \(k\)-connected \(X\)-minor.  Their Observation 1 gives graphs with
  \(\kappa_J(X)=6\) and no five-connected \(X\)-minor.
* Robertson--Seymour, *Graph Minors XXI: Graphs with Unique Linkages*: a
  graph with a spanning vital linkage of fixed order has treewidth bounded
  by a function of that order.

**Applicability.**  Root-preserving compression can reduce \((H,N)\) to a
four-connected rooted minor but cannot produce the five- or six-connected
rooted core one would want.  The vital-linkage theorem provides a
high-treewidth rerouting versus bounded-treewidth dichotomy; it does not
itself supply the desired rerouting.  The bounded function is far too large
to conflict with \(\chi(H)=6\).

Sources:

* <https://arxiv.org/abs/2003.04011>;
* <https://collaborate.princeton.edu/en/publications/graph-minors-xxi-graphs-with-unique-linkages>.

### 2.10 Connectivity of contraction-critical graphs

**Established.**  Mader gives seven-connectivity for noncomplete
\(k\)-contraction-critical graphs when \(k\ge7\).  Lafferty--Liu--Rolek--Yu
(2025) improve this to connectivity 8 for \(k\ge17\), 9 for \(k\ge29\),
and 10 for \(k\ge41\).

**Applicability.**  At \(k=7\), this stops at \(\kappa(G)=7\) and
\(\kappa(H)=6\).  None of the higher-connectivity linkage or knittedness
thresholds can be invoked.

Source: <https://arxiv.org/abs/2509.07144>.

## 3. Two decisive counterexamples to overbroad target lemmas

### 3.1 Six-connectivity does not give a nonseparating rooted \(K_5\)

Let

\[
 J=K_8-\{45,67\}
\]

on vertices \(0,1,\ldots,7\).  Then \(\kappa(J)=6\): its minimum degree is
six, and deleting the other six vertices leaves either missing pair
disconnected.

Take

\[
 U=\{2,4,5,6,7\},\qquad a=0,\qquad b=1.
\]

The set \(U\) roots a \(K_5\)-model, for example by using vertex 3 to
repair one of the missing root edges and vertex 0 to repair the other.
But every rooted \(K_5\)-model needs two distinct auxiliary vertices: one
to repair the \(45\) adjacency and another to repair the \(67\) adjacency.
Only vertex 3 is outside \(U\cup\{a,b\}\).  Hence every rooted model consumes
at least one of \(a,b\), and no rooted model leaves them in one complementary
component.

Thus the statement

> every \((t+1)\)-connected graph with a rooted \(K_t\)-model has one whose
> complement connects two prescribed vertices

is false already for \(t=5\).  The D7 lemma must use colour saturation and
the contraction witnesses.

### 3.2 Seven-connectivity and multiply-hit bags do not upgrade \(K_7^-\)

Let \(I\) be the icosahedral graph and let

\[
 J=K_2\vee I.
\]

Since \(I\) is five-connected and planar with Hadwiger number four,

\[
 \kappa(J)=7,\qquad \delta(J)=7,
 \qquad \eta(J)=2+4=6.
\]

Thus \(J\) has no \(K_7\)-minor.  In the standard labeling

\[
 t=0,\quad u_0,\ldots,u_4=1,\ldots,5,
 \quad w_0,\ldots,w_4=6,\ldots,10,\quad b=11,
\]

the following are branch sets of a spanning \(K_5^-\)-model in \(I\):

\[
 \{0\},\quad \{1,2,6,7,10\},\quad \{3,8\},
 \quad \{4,5\},\quad \{9,11\};                              \tag{3.1}
\]

the only missing pair is the first and fifth.  Adding the two universal
vertices gives a spanning \(K_7^-\)-model.  The deficient singleton
\(\{t\}\) has seven portal vertices across the other five adjacent bags:
the two universal vertices, \(u_0,u_1\) in the second bag, \(u_2\) in the
third, and \(u_3,u_4\) in the fourth.  In particular the contact
concentration and double-hit conclusions hold, but no upgrade exists.

Therefore no splitting lemma based only on seven-connectivity, minimum
degree seven, exclusion of \(K_7\), and multiply-hit portal counts can be
true.  The example is not seven-contraction-critical; that missing
hypothesis must do real work.

## 4. What the established results genuinely reduce

The literature supports the following exact ladder, with no omitted arrow:

\[
\begin{array}{c}
\text{contraction colouring at }\{v,a,b\}\\
\Downarrow\quad\text{Rolek--Song}\quad\\
\text{exterior bichromatic paths for missing edges of }H[U]\\
\Downarrow\quad\text{Kriesell--Mohr}\quad\\
\text{a rooted }K_5\text{ on }U\\
\not\Downarrow\\
\text{an }a\text{-}b\text{ path disjoint from its bags.}
\end{array}
\]

Du--Li--Xie--Yu supplies a different arrow:

\[
\begin{array}{c}
\text{six-connected }H\text{ with the seven-terminal CE extension}\\
\Downarrow\\
\text{a path leaving }U\text{ connected, or the sparse alternative (2.3),}
\end{array}
\]

but “\(U\) connected” cannot be replaced silently by “\(U\) roots a
\(K_5\) inside that component.”

## 5. The most useful exact target lemma

### Target CP-RP (colour-preserving removable path)

Under the D7 hypotheses, there is a contraction colouring \(c\), with
repeated pair \(a,b\) and unique roots \(U\), and an \(a\)-\(b\) path
\(P\subseteq H-U\) such that, for every

\[
 u_i u_j\in E(\overline{H[U]}),
\]

the vertices \(u_i,u_j\) remain in the same \((i,j)\)-bichromatic component
of \(H-P\).

This lemma immediately closes the degree-seven cell.  Apply
Kriesell--Mohr in \(H-P\) to obtain five rooted clique bags.  The path
\(P\) is a sixth connected bag containing \(a,b\).  For every \(u_i\), at
least one of \(a u_i,b u_i\) is an edge, since otherwise
\(\{a,b,u_i\}\) would be independent in \(G[N]\).  Hence \(P\) is adjacent
to every rooted bag.  The six bags form an \(N\)-meeting \(K_6\)-model in
\(H\), and adjoining \(\{v\}\) gives \(K_7\).

CP-RP is strictly more tailored than the false generic statement in
Section 3.1.  It asks only to preserve the finite set of bichromatic
connections from one contraction colouring.

## 6. A weakest plausible near-clique target

### Target CC-Split

Let \(G\) be seven-contraction-critical and \(K_7\)-minor-free.  Among all
spanning \(K_7^-\)- or \(K_7^\vee\)-models, choose one minimizing the sorted
multiset of branch-set orders.  Suppose a deficient bag \(A\) is genuinely
anticomplete to one or two bags and an unaffected bag \(D\) contains two
vertices of \(N(A)\).  Then either

1. the model can be upgraded to \(K_7\), or
2. it can be replaced by a lexicographically smaller model of the same
   near-clique type.

CC-Split would close both normalized near-clique cases: seven attachments
in five bags for \(K_7^-\), or seven attachments in four bags for
\(K_7^\vee\), force a multiply-hit bag, contradicting minimality.

Section 3.2 proves that “seven-contraction-critical” cannot be weakened to
the currently used connectivity and portal hypotheses.

## 7. Proof mechanism I: path--Kempe certificate exchange

This is the recommended first route toward CP-RP.

1. Fix a contraction colouring of \(G/\{v,a,b\}\).  For every missing
   root edge choose a shortest exterior bichromatic path as in
   Rolek--Song.  Use the constructive cases in Kriesell--Mohr Theorem 7 to
   convert these paths to a five-bag certificate.
2. Simultaneously choose an \(a\)-\(b\) path \(P\subseteq H-U\), minimizing
   first the number of certificate vertices on \(P\), then the total length
   of the certificate, and finally \(|P|\).
3. At a first intersection between \(P\) and an \((i,j)\)-Kempe path,
   attempt the two standard exchanges:
   * reroute the relevant subpath of \(P\) along the Kempe component; or
   * interchange colours on the portion of the Kempe component cut off by
     \(P\), thereby changing the repeated pair through the established
     Kempe-pivot operation.
4. If neither exchange reduces the lexicographic objective, record the
   bridge attachments to \(P\).  Feed this “critical feasibility” data into
   the Du--Li--Xie--Yu proof, rather than using only its final density
   corollary.  Any obstruction set disjoint from \(N(v)\) with boundary at
   most six is forbidden by seven-connectivity of \(G\).
5. Treat the finite complement types separately.  Rolek--Song already
   gives disjoint paths for matching edges and disjoint star groups.  The
   first non-pseudoforest case to isolate is
   \(F=K_{2,3}\); proving CP-RP for this case removes the only six-edge
   complement.

An especially concrete two-component version is available.  There are at
most two components of \(G-N[v]\), each with all seven neighbours in
\(N(v)\).  Record, for every missing root edge, in which component its
bichromatic connection can be chosen.  If one component supports a full
Kriesell--Mohr certificate, route \(P\) through the other.  The unresolved
case becomes a finite edge-labeling problem on the triangle-free graphs
\(F\) of order five, augmented by the contraction-colouring constraints on
each exterior component.

**Adversarial checkpoint.**  Merely finding an \(a\)-\(b\) path with
\(U\) in one component of its complement is insufficient.  Every missing
edge of \(H[U]\) must retain the right bichromatic connection after the
path is deleted.

## 8. Proof mechanism II: contraction-coloured portal pruning

This is the recommended near-clique route toward CC-Split.

1. In a minimal spanning near-clique model, replace each branch set by a
   minimal tree connecting one retained portal for every required model
   adjacency and every neighbour in the deficient bag.
2. In a multiply-hit unaffected bag \(D\), take the path in that tree
   between two \(A\)-portals.  Cutting an edge of this path produces two
   candidate pieces.  A pendant piece can be merged with \(A\) if the
   residual piece still has one portal for every adjacency demanded of
   \(D\).
3. Whenever the transfer is blocked, the blocking adjacency has a unique
   portal on the pendant side.  Contract an edge immediately behind that
   portal and use a six-colouring of the proper minor.  The intended Kempe
   exchange is to force either a second portal for that adjacency or a path
   through another branch set that allows the portal to be moved.
4. If every edge on the \(A\)-portal path is blocked, the unique portals
   occur in a nested order.  Their attachment sets should give either a
   separator of order at most six, contradicting Mader connectivity, or a
   colouring of the contracted graph that extends to a six-colouring of
   \(G\).

The first finite cell to prove is when the minimal tree for \(D\) is a path
and the two \(A\)-portals are its ends.  Classify the order of the at most
six retained adjacency portals along the path.  The explicit
\(K_2\vee I\) obstruction in Section 3.2 should be used as the adversarial
test: every proposed exchange must point to a contraction-colouring fact
that fails in that graph.

## 9. Lower-priority structural/computational route

The desired configuration is a fixed coloured rooted-minor problem: a
\(K_6\)-model with terminal partition (1.1).  Graph Minors XXI and modern
rooted-minor algorithms give an irrelevant-vertex reduction when the
treewidth is sufficiently large; failure of rerouting can therefore be
reduced to bounded treewidth for this fixed pattern.  One could combine
this with a lean tree decomposition and the fact that \(G\) has no
separating clique.

This is useful for exhaustive falsification and finite-state discovery,
not presently a proof: bounded treewidth does not bound the order, and the
known vital-linkage width bound is vastly larger than the chromatic
threshold six.

## 10. Recommended immediate tests

1. **CP-RP for pseudoforests.**  Prove the colour-preserving removable-path
   lemma when \(F\) is a forest or unicyclic.  Use Rolek--Song's disjoint
   matching/star groups, and audit simultaneous path avoidance.
2. **Hard complement \(K_{2,3}\).**  Enumerate the possible distributions
   of its six bichromatic connections over one or two exterior components.
   Reject any distribution incompatible with a proper contraction
   colouring.
3. **Portal path cell.**  Prove or computationally refute CC-Split when the
   multiply-hit bag has a path as its minimal connector tree.
4. **Counterexample filters.**  Every candidate lemma must survive
   \(K_8-\{45,67\}\) and \(K_2\vee I\); if it does, identify explicitly
   which saturation or contraction-colouring hypothesis excludes those
   graphs.

## 11. Stopping criteria

A route has reached a theorem-strength gap rather than a proof if it asks
for any of the following without a new mechanism:

* every six-connected graph to have a nonseparating rooted \(K_5\);
* every seven-connected graph with \(K_7^-\) or \(K_7^\vee\) to contain
  \(K_7\);
* generic seven-knittedness or five-linkage at connectivity six;
* arbitrary simultaneous disjointness of all Kempe paths;
* a branch-set split justified only by the number of portals.

The next genuine milestone is either CP-RP for all triangle-free
five-vertex complements, or CC-Split with an essential, explicitly used
contraction-colouring hypothesis.

