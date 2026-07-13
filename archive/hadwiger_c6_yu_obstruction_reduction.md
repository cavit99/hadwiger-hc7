# The \(C_6\) shore is a Yu three-path obstruction

## 1. Setting

Retain the audited \(C_6\dot\cup K_1\) full-shore configuration. Thus

\[
 S=W\dot\cup\{z\},\qquad W=P\dot\cup Q,
\]

where

\[
 P=\{0,1,2\},\qquad Q=\{3,4,5\},
\]

\(G[W]\) is the triangular prism with triangles \(P,Q\) and identity
matching

\[
 I=\{03,14,25\},
\]

and \(D,D'\) are the two anticomplete connected components of \(G-S\),
each full to \(S\). The ambient graph \(G\) is seven-connected and has
no \(K_7\)-minor.

For a shore \(D\), put

\[
 H_D=G[D\cup W].
\]

The point of retaining the boundary prism, but not \(z\) or the opposite
shore, is that \(H_D\) has a canonical identity \(P\)-to-\(Q\) linkage:
the three edges of \(I\).

## 2. Every linkage has the identity permutation

### Lemma 2.1

Every collection of three pairwise vertex-disjoint \(P\)-to-\(Q\) paths
in \(H_D\) induces the identity matching \(I\).

#### Proof

Three vertex-disjoint \(P\)-to-\(Q\) paths use all three vertices of
\(P\) and all three vertices of \(Q\) as their distinct endpoints. No
other vertex of \(W\) can therefore occur internally on one of the
paths. Consequently each path is either one of the direct identity
edges \(03,14,25\), or all its internal vertices lie in the single
shore \(D\).

If the induced bijection \(\pi:P\to Q\) were nonidentity, these paths
would be a \(\pi\)-linkage of precisely the kind excluded by Theorem 3.1
of hadwiger_c6_three_linkage_exclusion.md. That theorem handles both
types: a transposition contains an antipodal two-linkage, and a
three-cycle is one of the two alternating three-linkages. Either gives
an explicit \(K_7\)-model. Hence only \(I\) is possible.
\(\square\)

Thus, for each \(i\in\{0,1,2\}\), the structure obtained by declaring
the \(i\)-th identity pair fixed is a three-path **obstruction** in the
sense of Xingxing Yu: every linkage from \(P\) to \(Q\) contains the
path joining that prescribed pair.

## 3. Terminal-essentiality follows from ambient connectivity

### Lemma 3.1

For every \(X\subseteq V(H_D)\) with \(|X|\le3\), every component of
\(H_D-X\) contains a vertex of \(W=P\cup Q\).

#### Proof

Suppose a component \(C\) of \(H_D-X\) contains no vertex of \(W\).
Then \(C\subseteq D\). Since \(C\) is a component after deleting \(X\),
it has no neighbour in

\[
 (D\cup W)-(C\cup X).
\]

In the ambient graph \(G\), the only possible additional neighbour is
\(z\): the two components \(D,D'\) of \(G-S\) are anticomplete. Hence

\[
 N_G(C)\subseteq X\cup\{z\},
\]

so \(|N_G(C)|\le4\). The opposite shore \(D'\) lies outside
\(C\cup N_G(C)\), and therefore this is a vertex cut of order at most
four, contradicting seven-connectivity.
\(\square\)

## 4. The established obstruction characterization applies

We use Yu's characterization of three-path obstructions, in the
corrected formulation recorded as Theorem 3.4 in Ellingham--Plummer--Yu,
“Linkage for the Diamond and the Path With Four Vertices,” Journal of
Graph Theory, DOI 10.1002/jgt.20612. In the notation relevant here:

> Let \(A,B\) be distinct three-subsets of a graph \(H\). Assume that
> every component of \(H-X\) contains a terminal in \(A\cup B\) for
> every \(|X|\le3\). If every three-path \(A\)-to-\(B\) linkage fixes
> one prescribed terminal pair, then either
>
> 1. \(H\) has a separation of order at most two with \(A\) on one
>    side and \(B\) on the other; or
> 2. \(H\) is the edge-disjoint union of an \(X\)-ladder of Yu rungs
>    and a 3-planar graph attached along the ladder's central sequence.

The individual rungs are explicitly built from 3-planar pieces and
separations of order at most three. The theorem is an exact unbounded
classification, not a bounded-order enumeration.

### Theorem 4.1 (three simultaneous ladder descriptions)

For each full shore \(D\), and for each of the three identity pairs
\(03,14,25\), the graph \(H_D\) has one of the two outcomes in Yu's
characterization:

1. a \(P\)-to-\(Q\) separation of order at most two; or
2. an \(X\)-ladder plus a 3-planar attachment, oriented so that the
   selected identity pair is the fixed central pair.

#### Proof

Lemma 2.1 makes \(H_D\) an obstruction fixing any selected identity
pair. Lemma 3.1 supplies the terminal-essentiality hypothesis. The two
terminal triples are disjoint, so none of the trivial exceptions in the
obstruction definition applies. Invoke the characterization.
\(\square\)

### Lemma 4.2 (the small-separation outcome is absent)

For each of the three applications, outcome 1 of Theorem 4.1 is
impossible. Hence all three descriptions are (X)-ladders with a
3-planar central attachment.

#### Proof

The three identity edges (03,14,25) are vertex-disjoint edges from
(P) to (Q). In a separation with (P) on one side and (Q) on the
other, each such edge has an endpoint in the separator. Thus the
separator has order at least three, whereas outcome 1 has order at most
two. \(\square\)

### Lemma 4.3 (all 3-planar insertions are bare)

In any of the three ladder descriptions, the collection of induced
subgraphs contracted in the definition of the 3-planar central graph
is empty. The same holds for every 3-planar object occurring inside a
rung.

#### Proof

In the corrected definition of 3-planarity, every contracted induced
subgraph (A) has at most three neighbours in the graph, while all
listed foundation vertices remain outside (A). For the central graph
(J), its intersection with the ladder is precisely the central
sequence; hence none of the six global terminals can lie in such an
(A). Nor can (A) have an edge into a different rung. It is therefore
a terminal-free component after deletion of at most three vertices,
contradicting Lemma 3.1.

The identical argument applies to a contracted piece in any rung: the
listed rung terminals belong to the foundation, and an internal piece
has no edge outside that rung except through its displayed attachment.
Thus every 3-planar piece is an ordinary planar piece rather than a
clique-substituted one. \(\square\)

### Lemma 4.4 (exact adhesion of a nontrivial rung)

Let (R_i) be a rung with consecutive boundary triples (T_{i-1}) and
(T_i), and let (C) be a component of

\[
 R_i-(T_{i-1}\cup T_i).
\]

Then either no such (C) exists, or the two triples are disjoint and

\[
 N_G(C)=T_{i-1}\cup T_i\cup\{z\}.                  \tag{4.1}
\]

In particular every genuine rung interior lies behind an exact
seven-vertex adhesion.

#### Proof

The rung-intersection axioms and
(V(J\cap L)) equal to the central sequence imply

\[
 N_{H_D}(C)\subseteq T_{i-1}\cup T_i.
\]

The only possible additional neighbour in the ambient graph is (z).
If \(|T_{i-1}\cup T_i|\le5\), this gives a cut of order at most six,
contrary to seven-connectivity. Hence the triples are disjoint. The
right side of (4.1) now has order seven; seven-connectivity forces every
one of its vertices to be a neighbour of (C), proving equality.
\(\square\)

These lemmas reduce the infinite part of the characterization to bare
planar rungs, trivial transitions, and full seven-adhesion cells. They
do not identify portal representatives used by different linkages.

### Lemma 4.5 (portal multiplicity is finite)

Let \(P_i=N_D(c_i)\), \(0\le i<6\). Either the six full portal sets have
a system of six distinct representatives, or \(|D|\le5\).

#### Proof

Suppose Hall's condition fails. Choose \(I\subseteq\{0,\ldots,5\}\)
and put

\[
 U=\bigcup_{i\in I}P_i,\qquad |U|<|I|.              \tag{4.2}
\]

If \(D-U\neq\varnothing\), let \(C\) be one of its components. No vertex
of \(C\) is adjacent to \(c_i\) for \(i\in I\), because all such shore
portals belong to \(U\). Therefore

\[
 N_G(C)\subseteq
 U\cup\{c_j:j\notin I\}\cup\{z\}.
\]

The right side has order at most

\[
 (|I|-1)+(6-|I|)+1=6,
\]

and separates \(C\) from the opposite shore, contrary to
seven-connectivity. Hence \(D=U\), and (4.2) gives

\[
 |D|<|I|\le6.
\]

Thus \(|D|\le5\). The contrapositive and Hall's theorem give the desired
transversal for every shore of order at least six. \(\square\)

The tetrahedral order-four exception is eliminated, under the linkage
and frame hypotheses, by the exact portal classification in
hadwiger_c6_portal_tetrahedron_obstruction.md: it forces a vertex of
total degree at most six. Thus only order five remains as a finite
multiplicity base. For all unbounded shores, multiplicity is no longer
an obstacle to selecting six distinct roots; the remaining issue is
coherence of the three Yu ladder descriptions on that transversal.

## 5. What this closes and what remains

Theorem 4.1 proves the previously missing unbounded **prism-or-rope/web
decomposition**. It replaces the invalid attempt to infer a global
portal order from representatives chosen separately by different frame
locks. No coherent portal representatives are assumed: the
characterization is applied directly to all paths in \(H_D\).

There is still a real elimination step. Each shore has three
simultaneous obstruction descriptions, one for each identity column,
and the frame-ownership theorem says that one shore also owns at least
four prescribed pair linkages. A complete \(C_6\) closure must now prove
one of the following:

1. the three ladder descriptions are incompatible unless their common
   core is the triangular prism, whose degree pattern is already
   impossible;
2. some rung or 3-planar attachment supplies a forbidden nonidentity
   linkage and hence an explicit \(K_7\); or
3. the ladder adhesions carry common exact six-colour states, so the two
   proper-minor colourings glue.

This is a finite **rung-type** analysis plus an arbitrary-length state
composition problem, not an arbitrary-order graph enumeration. The
natural reusable invariant is the transfer relation of exact boundary
partitions across a rung. Acyclic ladder composition glues by the
laminar exact-state theorem; a cyclic composition must have trivial
colour holonomy.

## 6. General lesson

The reduction has a label-free formulation. Suppose a boundary quotient
forces every linkage between two terminal triples to use one prescribed
matching. If small terminal-free components are excluded by ambient
connectivity, Yu's theorem converts the linkage obstruction into:

\[
\text{small terminal separation}
\quad\text{or}\quad
\text{ladder of bounded-adhesion 3-planar rungs}.
\]

This is precisely the kind of reusable contact-or-separator mechanism
sought for general Hadwiger: positive demands give a rooted minor,
whereas failure of those demands produces a bounded-adhesion
decomposition on which exact coloring states can be propagated.
