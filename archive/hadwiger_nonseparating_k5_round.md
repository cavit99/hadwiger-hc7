# Degree seven: the nonseparating rooted-\(K_5\) problem

This note continues only the degree-seven cell in
`hadwiger_degree7_kempe.md`.  It gives two new reductions, a useful
component-support obstruction, and an explicit warning example.  It does
**not** close the degree-seven case.

## 1. Standing hypotheses

Let \(G\) be a proper-minor-minimal counterexample to \(\mathrm{HC}_7\),
let \(v\in V(G)\) have degree seven, and put
\[
 H=G-v,\qquad N=N_G(v),\qquad Q=\overline{G[N]}.
\]
The audited critical-graph reductions give
\[
 \chi(G)=7,\quad \eta(G)=6,\quad \kappa(G)\geq7,
 \quad\kappa(H)\geq6,\quad \alpha(G[N])=2.       \tag{1.1}
\]
In particular, \(Q\) is triangle-free.  Every six-colouring of \(H\)
uses all six colours on \(N\).

If a six-colouring has repeated pair \(x,y\in N\), write
\[
 U=N-\{x,y\}=\{u_1,\ldots,u_5\}
\]
for the five uniquely coloured neighbours, and put
\[
 F_{xy}:=Q[U]=\overline{G[U]} .                  \tag{1.2}
\]

## 2. Every neighbourhood nonedge is an accessible repeated pair

The earlier note only extracted a matching of accessible repeated pairs.
Proper-minor minimality gives the following stronger fact.

### Lemma 2.1 (full accessibility)

For every edge \(xy\in E(Q)\), there is a six-colouring of \(H\) whose
repeated pair on \(N\) is exactly \(\{x,y\}\).  More precisely, let
\(J_{xy}\) be obtained from \(G\) by contracting the connected triple
\(\{x,v,y\}\) to a vertex \(q\).  Then
\[
 \chi(J_{xy})=6,                                      \tag{2.1}
\]
and in every proper six-colouring of \(J_{xy}\), the five vertices of
\(U=N-\{x,y\}\) receive the five colours other than the colour of \(q\),
bijectively.

#### Proof

The graph \(J_{xy}\) is a proper minor, so it is six-colourable.  If it
were five-colourable, expand \(q\) onto \(x,y\) in \(H\), giving both the
colour of \(q\).  This is proper because \(xy\notin E(G)\).  Giving \(v\)
a fresh sixth colour would six-colour \(G\), a contradiction.  Thus
\(\chi(J_{xy})=6\).

In \(J_{xy}\), the vertex \(q\) is adjacent to every vertex of \(U\),
using the edges from \(v\) before contraction.  Hence no vertex of \(U\)
has the colour of \(q\).  If some other colour were absent from \(U\),
expanding \(q\) onto \(x,y\) and assigning that absent colour to \(v\)
would again six-colour \(G\).  The five vertices of \(U\) therefore have
the other five colours bijectively.  Expanding \(q\) gives the asserted
colouring of \(H\). \(\square\)

Thus the accessible repeated-pair graph is not merely a subgraph of
\(Q\): it is all of \(Q\).  Any proposed local counterconfiguration must
survive the rooted-minor test for **every** edge of \(Q\), with the
colourings supplied by the corresponding triple contractions.

### Lemma 2.2 (simultaneous external Kempe paths)

Fix \(xy\in E(Q)\) and a six-colouring obtained from \(J_{xy}\).  Give
\(x,y\) colour \(0\), and give \(u_i\) colour \(i\).  For every
\(u_i u_j\in E(F_{xy})\), there is a \((i,j)\)-alternating
\(u_i\)-\(u_j\) path whose internal vertices lie in
\(G-N[v]\).  Paths for vertex-disjoint edges of \(F_{xy}\) can be chosen
vertex-disjoint.

#### Proof

If the \((i,j)\)-component containing \(u_i\) omitted \(u_j\), swapping
colours \(i,j\) on it would remove colour \(i\) from \(N\).  Colouring
\(v\) with \(i\) would six-colour \(G\), a contradiction.  Hence the two
roots are in one bichromatic component.

No internal vertex of a corresponding path lies in \(N[v]\): the other
five vertices there have colour \(0\) or colours different from
\(i,j\), while \(u_i,u_j\) are the unique boundary vertices with their
two colours.  Finally, paths for disjoint terminal pairs use disjoint
pairs of colour classes and are therefore vertex-disjoint. \(\square\)

This is the precise useful content of the Rolek--Song contraction-colouring
argument in the present cell.

## 3. A path-avoidance reformulation

Let \(c\) be one of the colourings above, and let \(W\) be the union of
the five unique colour classes.  Kriesell--Mohr Theorem 7 applies because
\(F_{xy}\) is triangle-free on five vertices and hence has at most six
edges.  It gives a rooted \(K_5\)-model on \(U\), wholly inside \(H[W]\).

The nonseparating requirement has an equivalent path form.

### Lemma 3.1 (path-avoidance equivalence)

The following are equivalent.

1. There is a rooted \(K_5\)-model \(\mathcal B\) at \(U\) such that
   \(x,y\) lie in one component of
   \(H-\bigcup\mathcal B\).
2. There is an \(x\)-\(y\) path \(P\) in \(H-U\) such that
   \(H-V(P)\) contains a \(K_5\)-model rooted at \(U\).

Either condition gives a \(K_7\)-minor in \(G\).

#### Proof

Under (1), take an \(x\)-\(y\) path in the indicated complementary
component.  This gives (2).  Conversely, a rooted model in \(H-V(P)\)
and the path \(P\) give (1).

For every \(u_i\), at least one of \(xu_i,yu_i\) is an edge, since
otherwise \(\{x,y,u_i\}\) would be an independent triple in \(G[N]\).
Consequently, \(V(P)\) is adjacent to all five rooted bags.  The path and
those bags form a \(K_6\)-model in \(H\), and the singleton \(\{v\}\)
is a seventh bag. \(\square\)

This suggests a sharply stated sufficient lemma.  It is weaker than a
general nonseparating rooted-minor theorem.

### Lemma 3.2 (Kempe-resilient path criterion)

If there is an \(x\)-\(y\) path \(P\subseteq H-U\) such that, for every
edge \(u_i u_j\in E(F_{xy})\), the vertices \(u_i,u_j\) remain in one
\((i,j)\)-component of \(H-V(P)\), then \(G\) has a \(K_7\)-minor.

#### Proof

Apply Kriesell--Mohr property \((*)\) to \(F_{xy}\) in the graph
\(H[W]-V(P)\).  This gives a rooted \(F_{xy}\)-certificate.  Root edges
of \(G[U]\) supply every complementary pair, turning it into a rooted
\(K_5\)-model.  Lemma 3.1 finishes. \(\square\)

Thus a counterexample forces every \(x\)-\(y\) path avoiding \(U\) to
destroy at least one of the finitely many required bichromatic
connections.  Six-connectivity guarantees such paths, but not their
simultaneous avoidance of all bichromatic separators.

## 4. The two-exterior-component support obstruction

Let \(C_1,C_2\) be the two components of \(G-N[v]\).  Seven-connectivity
gives
\[
 N_G(C_1)=N_G(C_2)=N.                                  \tag{4.1}
\]
For \(e=u_i u_j\in E(F_{xy})\), say that \(C_r\) **supports** \(e\) if
there is an \((i,j)\)-path from \(u_i\) to \(u_j\) all of whose internal
vertices lie in \(C_r\).  Lemma 2.2 says every edge has nonempty support.

### Lemma 4.1 (one supporting component closes the cell)

If one of \(C_1,C_2\) supports every edge of \(F_{xy}\), then \(G\) has a
\(K_7\)-minor.

#### Proof

Suppose \(C_1\) supports every edge.  Restrict the five-coloured graph to
\(U\) and those vertices of \(C_1\) in the five unique colour classes.
Every edge of \(F_{xy}\) still has Kempe-connected ends.  By
Kriesell--Mohr Theorem 7 there is a rooted \(F_{xy}\)-certificate in this
restricted graph.  Edges of \(G[U]\) complete it to a rooted
\(K_5\)-model \(\mathcal B\), all of whose vertices lie in
\(U\cup C_1\).

The set
\[
 D=C_2\cup\{x,y\}
\]
is connected by (4.1), is disjoint from the five bags, and is adjacent to
each bag: for the bag rooted at \(u_i\), use one of the edges
\(xu_i,yu_i\), which exists by (1.1).  Hence
\(D\) and the five bags form a \(K_6\)-model in \(H\); add \(\{v\}\).
\(\square\)

### Corollary 4.2 (oppositely exclusive missing edges)

In the two-component cell, for every \(xy\in E(Q)\) and every colouring
of \(J_{xy}\), there are distinct edges \(e,f\in E(F_{xy})\) such that
\[
 e\text{ is supported only by }C_1,qquad
 f\text{ is supported only by }C_2                 \tag{4.2}
\]
after possibly interchanging \(C_1,C_2\).

#### Proof

If \(C_1\) does not support all edges, some edge is supported only by
\(C_2\); if \(C_2\) does not support all edges, some edge is supported
only by \(C_1\).  These edges are distinct because every edge has
nonempty support.  Lemma 4.1 excludes the other alternatives. \(\square\)

This is a concrete strengthening of the earlier statement that every
certificate must meet both exterior components: the obstruction is already
visible in the two-coloured paths before a certificate is assembled.

## 5. A seven-vertex complement lemma

The existence of a pseudoforest choice does not actually require the
Moser-spindle classification.

### Lemma 5.1 (pseudoforest deletion)

Let \(Q\) be a triangle-free graph on seven vertices.  Either

1. some edge \(xy\in E(Q)\) has \(Q-\{x,y\}\) a pseudoforest, or
2. \(Q=K_{3,4}\).

#### Proof

On five vertices, the only triangle-free graph which is not a
pseudoforest is \(K_{2,3}\).  Indeed, a connected non-pseudoforest has at
least six edges and hence is the equality graph in Mantel's theorem; a
disconnected non-pseudoforest would require a triangle-free component on
at most four vertices with at least five edges, which is impossible.

Suppose therefore that
\[
 Q-\{x,y\}\cong K_{2,3}                              \tag{5.1}
\]
for every \(xy\in E(Q)\).  The graph \(Q\) is connected.  To see this,
fix \(xy\).  The five other vertices form a connected graph by (5.1).
If the edge component containing \(x,y\) had no edge to those five,
deleting the ends of an edge in that \(K_{2,3}\) would leave a
disconnected graph, contrary to (5.1).

Writing \(m=|E(Q)|\), equation (5.1) gives, for every edge \(xy\),
\[
 d_Q(x)+d_Q(y)=m-5,                                  \tag{5.2}
\]
because deleting the two endpoints leaves six edges.  In a connected
graph with constant degree-sum on its edges, degrees alternate along
paths.  Hence the graph is regular if it has an odd cycle, and otherwise
it is bipartite semiregular.

The regular case is impossible: if the common degree is \(r\), then
\(m=7r/2\), while (5.2) says
\(2r=7r/2-5\), giving \(r=10/3\).

Thus \(Q\) is bipartite semiregular.  If its bipartition has orders
\(p,q\), deletion of the ends of an edge leaves the unique bipartition
of \(K_{2,3}\), so \(\{p-1,q-1\}=\{2,3\}\), and hence
\(\{p,q\}=\{3,4\}\).  If the two constant degrees are \(r,s\), then
\(3r=4s\), with \(r\leq4\), \(s\leq3\).  Therefore \(r=4,s=3\) and
\(Q=K_{3,4}\). \(\square\)

For the degree-seven problem, the exceptional alternative says
\[
 G[N]=K_3\mathbin{\dot\cup}K_4.                       \tag{5.3}
\]
In the two-exterior-component cell, the \(K_4\) together with the two
universal component helpers already gives an \(N\)-meeting \(K_6\)-model.
Consequently:

### Corollary 5.2

In every unresolved two-exterior-component cell, one can choose an
accessible repeated pair \(xy\) for which \(F_{xy}\) is a pseudoforest.
For every contraction colouring associated with that pair, however,
Corollary 4.2 still forces oppositely exclusive edges.  Thus the remaining
issue is component avoidance, not property \((*)\).

### Lemma 5.3 (leaf-defect restriction in the exceptional one-component cell)

Suppose there is one exterior component \(C\) and
\[
 G[N]=K_3\mathbin{\dot\cup}K_4,
 \qquad A=V(K_3),\quad B=V(K_4).                 \tag{5.4}
\]
Let \(z\) be a cutvertex of \(C\).  For a component \(D\) of \(C-z\),
call \(D\) a *leaf side at \(z\)*.  Then:

1. \(D\) is adjacent to at least six of the seven vertices of \(N\).
2. There cannot be two leaf sides which are both adjacent to all four
   vertices of \(B\).
3. For each \(b\in B\), there cannot be two leaf sides whose unique
   missed boundary vertex is \(b\).

Consequently, at any cutvertex of \(C\), there are at most five leaf
sides: at most one adjacent to all of \(B\), and at most one with each of
the four possible defects in \(B\).

#### Proof

The neighbourhood of \(D\) outside \(D\) is contained in
\[
 \{z\}\cup N.
\]
If \(D\) met at most five boundary vertices, this set would contain at
most six vertices and would separate \(D\) from \(v\), contradicting
\(\kappa(G)\geq7\).  This proves (1).

Suppose first that distinct leaf sides \(D_1,D_2\) are each adjacent to
all of \(B\).  Each is adjacent to at least two vertices of \(A\), by
(1).  Choose distinct \(a_1,a_2\in A\) with \(a_i\) adjacent to \(D_i\).
Then
\[
 X_i=D_i\cup\{a_i\}\quad(i=1,2)
\]
are disjoint connected bags.  They are adjacent through the edge
\(a_1a_2\), and each is adjacent to every singleton bag \(\{b\}\),
\(b\in B\).  Together with the four singleton bags on \(B\), they form
an \(N\)-meeting \(K_6\)-model in \(H\), which extends with \(\{v\}\)
to a \(K_7\)-model.  This proves (2).

Now suppose \(D_1,D_2\) both miss the same \(b\in B\).  By (1), each is
adjacent to every vertex of \(N-\{b\}\).  Again choose distinct
\(a_1,a_2\in A\) adjacent to \(D_1,D_2\), respectively.  Since
\(d_G(b)\geq7\), while \(b\) has only its three neighbours in \(B\) and
the neighbour \(v\) outside \(C\), it has at least three neighbours in
\(C\).  Neither \(D_i\) contains one.  Hence there is a \(b\)-\(z\) path
\(R\) whose internal vertices lie in
\(C-(D_1\cup D_2)\): start with any neighbour of \(b\) in that set and
continue to \(z\) inside its component of \(C-z\) (with the evident
one-edge interpretation if the neighbour is \(z\)).

Use the six bags
\[
 D_1\cup\{a_1\},\quad D_2\cup\{a_2\},\quad
 V(R),\quad \{b'\}\ (b'\in B-\{b\}).             \tag{5.5}
\]
Here \(V(R)\) is the bag rooted at \(b\).  Its endpoint \(z\) is
adjacent into both \(D_1,D_2\), repairing precisely their missing
adjacency to \(b\).  All other required adjacencies follow from the
\(K_4\) on \(B\), the edge \(a_1a_2\), and the fact that each \(D_i\)
meets every vertex of \(B-\{b\}\).  Thus (5.5) is again an
\(N\)-meeting \(K_6\)-model, a contradiction.  This proves (3), and the
count follows. \(\square\)

The count can be sharpened using a two-side consolidation which does not
use the cutvertex.

### Lemma 5.4 (at most two cut sides)

Under the hypotheses of Lemma 5.3, \(C-z\) has at most two components.

#### Proof

Call a side *good* if it is adjacent to all of \(B\).  By Lemma 5.3 there
is at most one good side, and the nongood sides have pairwise distinct
defects in \(B\).

If two nongood sides \(D_i,D_j\) have distinct defects, choose any
\(a\in A\) and set
\[
 X=D_i\cup D_j\cup\{a\}.                            \tag{5.6}
\]
Both sides are adjacent to every vertex of \(A\), so \(X\) is connected.
Moreover, their distinct one-vertex defects imply that their union is
adjacent to every vertex of \(B\).  Thus (5.6) is one connected
\(B\)-complete helper bag rooted in \(N\).

If there are four nongood sides, pair them and use distinct vertices
\(a_1,a_2\in A\) in the two versions of (5.6).  The resulting helper bags
are disjoint and adjacent through \(a_1a_2\).  With the four singleton
bags on \(B\) they give the forbidden \(K_6\)-model.

If there is one good side and at least two nongood sides, consolidate two
nongood sides as in (5.6), and use the good side together with a distinct
vertex of \(A\) as the second helper.  The same construction closes the
case.  Hence four sides are impossible.  With three sides, the presence
of a good one is also impossible, and Lemma 5.3 makes the three remaining
defects distinct.  Write those sides as \(D_1,D_2,D_3\), with respective
defects \(b_1,b_2,b_3\in B\).  Choose distinct vertices
\(c_i\in B-\{b_i\}\) for \(i=1,2,3\); such a choice exists by Hall's
theorem (each of the three allowed sets has order three in the four-set
\(B\)).  The bags
\[
 X_i=D_i\cup\{c_i\}\qquad(i=1,2,3)
\]
are disjoint and connected.  They are pairwise adjacent through the
clique edges \(c_ic_j\), and each is adjacent to all three singleton
bags on \(A\), because a side with a unique defect in \(B\) meets every
vertex of \(A\).  These are six pairwise adjacent, \(N\)-meeting bags,
giving the forbidden \(K_6\)-model in \(H\).  Hence three sides are
impossible as well. \(\square\)

This lemma does not eliminate the exceptional cell.  Its first unresolved
block-tree pattern has two leaf sides with *different* defects
\(b_1,b_2\in B\).  Both routes from the deficient side to the missing
\(B\)-root pass through the same cutvertex \(z\), so assigning \(z\) to
one repairing bag can block the other.  Treating the two repairs as
disjoint without resolving this shared vertex would be invalid.

## 6. Specialisation to the two Moser-spindle neighbourhoods

Use the labelling
\[
 V(M)=\{a,b,c,d,e,p,q\},
\]
\[
 E(M)=\{ab,ac,bc,bp,cp,ad,ae,de,dq,eq,pq\}.
\]
The audited two-component reduction leaves \(G[N]=M\) or \(M+bd\), up
to symmetry.

A direct deletion check gives the following useful finite table.

* For \(G[N]=M\), choosing any nonedge except \(ap\) or \(aq\) as the
  repeated pair leaves a connected unicyclic graph \(F_{xy}\) on the
  other five vertices.  For example, for \(xy=bd\),
  \[
  E(F_{bd})=\{ap,aq,ce,cq,ep\},
  \]
  which is a \(5\)-cycle.  The two exceptional choices \(ap,aq\) leave
  \(F_{xy}\cong K_{2,3}\).
* For \(G[N]=M+bd\), every choice of a nonedge gives a pseudoforest.
  For example,
  \[
  E(F_{ce})=\{ap,aq,bq,dp\},
  \]
  a tree, while the other choices give a tree or a connected unicyclic
  graph.

By Lemma 2.1 all these choices really occur as repeated pairs.  Thus, in
the pure-spindle cell, every colouring of \(J_{bd}\) assigns the five
edges of the displayed \(5\)-cycle to the two exterior components in a
way containing oppositely exclusive edges.  In the one-cross-edge cell,
the same holds already for the four-edge tree \(F_{ce}\).

Pseudoforest property \((*)\) alone does not eliminate (4.2): its standard
proof assembles bags from all the chosen two-coloured paths, and those
paths may lie in both components.  The genuinely finite next target in the
two-component route is therefore:

> **Moser support-switch lemma.**  Use the contraction-colouring witnesses
> for several different nonedges of \(M\) (respectively \(M+bd\)) to rule
> out the oppositely exclusive support pattern (4.2) for all of them.

This is strictly more specific than asking for an arbitrary
component-avoiding property-\((*)\) certificate.

## 7. Six-connectivity and saturation alone do not suffice

Here is a small explicit obstruction to the tempting fixed-colouring
lemma.

Let
\[
 S=\{u_1,u_2,u_3,u_4,u_5,x_1,x_2\}
\]
and let \(S\) induce \(K_7\) with precisely the three edges
\[
 u_1u_2,\quad u_1x_2,\quad u_2x_1                  \tag{6.1}
\]
deleted.  Add two nonadjacent vertices \(a,b\), each adjacent to every
vertex of \(S\).  Call the resulting graph \(L\), and put
\[
 N_0=\{a,b,u_1,u_2,u_3,u_4,u_5\}.
\]

Then all of the following hold.

1. \(\kappa(L)=6\).  Indeed, \(L=\overline{K_2}\vee L[S]\), and
   \(L[S]\) is four-connected (its complement is the path
   \(x_2u_1u_2x_1\) plus three isolated vertices).
2. \(\chi(L)=6\).  The set
   \(\{x_1,x_2,u_3,u_4,u_5\}\) is a \(K_5\), and joining
   \(\overline{K_2}\) adds one colour.
3. Every six-colouring uses all six colours on \(N_0\).  The displayed
   \(K_5\) receives five colours; \(a,b\) receive the sixth.  The
   adjacencies force \(u_1\) to have the colour of \(x_2\) and \(u_2\)
   the colour of \(x_1\).  Hence \(u_1,\ldots,u_5\) see all five colours.
4. \(\alpha(L[N_0])=2\).
5. In the forced colouring with repeated pair \(a,b\), the five unique
   roots are completely Kempe-connected.  The only missing root edge is
   \(u_1u_2\), and
   \[
   u_1x_1x_2u_2
   \]
   is an alternating path in their two colours.
6. Every rooted \(K_5\)-model on \(u_1,\ldots,u_5\) contained in the five
   unique colour classes uses both \(x_1,x_2\).  If \(x_1\) is omitted,
   the remaining extra vertex \(x_2\) cannot both connect a bag rooted at
   \(u_1\) and repair its missing adjacency to the \(u_2\)-bag, because
   \(u_1x_2,u_1u_2\notin E(L)\).  The symmetric argument applies when
   \(x_2\) is omitted.  Thus the union of every such model is all of
   \(S\), which separates \(a\) from \(b\).

This example satisfies the local colouring, saturation, independence,
Kempe, and connectivity data, yet the desired nonseparating certificate
does not exist for its fixed colouring.  It is not a counterexample to
the degree-seven reduction: it has a \(K_7\)-minor with bags
\[
 \{a,u_1\},\{b,u_2\},\{x_1\},\{x_2\},
 \{u_3\},\{u_4\},\{u_5\},
\]
and \(N_0\) is not inclusion-minimal colour-saturating.  In particular,
the other nonedge \(u_1u_2\) cannot be made the repeated pair in \(L\).
This is exactly where Lemma 2.1 and the minor exclusion add information.

Consequently, a valid proof cannot invoke a blanket theorem of the form

\[
 \text{six-connectivity + saturation + Kempe connectivity}
 \Longrightarrow\text{ nonseparating rooted }K_5.
\]

It must use either full accessibility across all edges of \(Q\), the
condition \(\eta(H)=6\), or further contraction-critical structure.

## 8. Exact residuals and recommended next attack

The new endpoint is as follows.

### One exterior component

For every \(xy\in E(Q)\), all paths from Lemma 2.2 lie in the unique
component \(C\), and Kriesell--Mohr gives a rooted \(K_5\) inside
\(U\cup C\).  What is missing is a path through the unused portion of
\(C\) joining \(x\) to \(y\).  By Lemma 3.2 it suffices to find an
\(x\)-\(y\) path whose deletion preserves the finitely many required
bichromatic root connections.

### Two exterior components

The neighbourhood is reduced to \(M\) or \(M+bd\).  For every accessible
pair and every contraction colouring, its missing-edge graph has the
opposite-exclusive support obstruction (4.2).  It is enough to show that
some contraction colouring makes all its missing edges supported by one
component.  The most constrained first cases are the cycle
\(F_{bd}=C_5\) in \(M\) and the tree \(F_{ce}\) in \(M+bd\).

The correct next proof attempt is to compare the boundary colour-extension
states of the two graphs
\[
 G[N[v]\cup C_1]\quad\text{and}\quad G[N[v]\cup C_2].
\]
If all contractions force opposite-exclusive supports, those states should
encode incompatible Kempe permutations on the seven-vertex boundary.  A
successful gluing of the two states would six-colour \(G\); a successful
failure analysis should instead produce the required one-component support.
This is a finite boundary-state problem for the two displayed Moser graphs,
not a general rooted-minor assertion.

## References

* M. Kriesell and S. Mohr, *Kempe Chains and Rooted Minors*, Theorem 7,
  arXiv:1911.09998 (revised 2022).
* M. Rolek and Z.-X. Song, *Coloring graphs with forbidden minors*, JCTB
  127 (2017), especially Lemma 1.7.
* S. Norin and A. Totschnig, *Every graph with no
  \(K_7^{\vee}\)-minor is 6-colorable*, arXiv:2507.03244, Claim 4.4.
