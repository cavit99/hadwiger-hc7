# Relative pair-mode capacity or a tight adhesion

## 1. Relative-shore formulation

Let \(q\ge3\) and \(s\ge0\), put \(k=2q+s\), and let \(S\) be a
labelled set of order \(k\). Let \(C\) be a connected
\(S\)-boundaried graph, full to \(S\), of order at least two. For
nonempty proper \(X\subsetneq C\),
write

\[
 \partial_S(X)=
 (N_C(X)-X)\mathbin{\dot\cup}N_S(X).              \tag{1.1}
\]

Assume the relative connectivity inequality

\[
 |\partial_S(X)|\ge k
 \qquad(\varnothing\ne X\subsetneq C).            \tag{1.2}
\]

Fix a boundary mode

\[
 S=B_1\mathbin{\dot\cup}\cdots\mathbin{\dot\cup}B_q
   \mathbin{\dot\cup}R,\qquad |B_i|=2,\quad |R|=s.\tag{1.3}
\]

The labels in \(R\) are called singleton labels. No graph on \(S\) is
assumed. A \(B_i\)-carrier is a connected subgraph of \(C\) meeting
the two full portal sets of the roots in \(B_i\). Two-block capacity
means two vertex-disjoint carriers for two distinct blocks; the
carriers need not initially be adjacent.

### Theorem 1.1 (relative capacity-or-tight-adhesion)

At least one of the following holds.

1. \(C\) contains disjoint connected carriers for two distinct pair
   blocks in (1.3).
2. Some nonempty proper \(X\subsetneq C\) is tight:

   \[
   |\partial_S(X)|=k.                             \tag{1.4}
   \]

This strictly strengthens the global packet-or-exact theorem: it uses
only the local inequality (1.2), not ambient \(k\)-connectivity. It
also permits any number of singleton labels, including none.

## 2. No tight set forces high local degree

Assume neither outcome occurs. Then every proper nonempty \(X\) has

\[
 |\partial_S(X)|\ge k+1.                         \tag{2.1}
\]

No vertex \(x\in C\) sees both roots of a pair block. If it did,
\(\{x\}\) would be a singleton carrier. Let \(Y\) be a component of
\(C-x\). In the absence of a packet, for each of the other \(q-1\)
blocks choose one root missed by \(Y\). Then

 \[
 |\partial_S(Y)|
 \le 1+k-(q-1)=k-q+2<k,                          \tag{2.2}
 \]

because \(q\ge3\), a contradiction to (1.2).

Hence a shore vertex has at most one neighbour in each pair block and
at most all \(s\) singleton labels:

\[
 |N_S(x)|\le q+s=k-q.
\]

Apply (2.1) to \(\{x\}\). Since its relative boundary is its full
degree into \(C\cup S\),

\[
 d_C(x)\ge(k+1)-(q+s)=q+1.                       \tag{2.3}
\]

In particular

\[
 |C|\ge q+2.                                      \tag{2.4}
\]

## 3. Internal connectivity amplification

Suppose \(Z\subseteq C\), \(|Z|=a\le q-1\), separates \(C\), and let
\(Y\) be a component of \(C-Z\). Since
\(N_C(Y)-Y\subseteq Z\), (1.2) gives

\[
 |S-N_S(Y)|\le a.                                \tag{3.1}
\]

Let \(\mathcal F(Y)\) be the pair blocks fully contacted by \(Y\).
Every missed root spoils at most one block, so

\[
 |\mathcal F(Y)|\ge q-a.                         \tag{3.2}
\]

Take two components of \(C-Z\). If \(q\ge a+2\), their two families
in (3.2) each have order at least two and admit distinct
representatives. The two components are disjoint carriers for those
two blocks, a contradiction.

It remains \(q=a+1\). Every \(\mathcal F(Y)\) is nonempty. If two
component families admitted distinct representatives, they would again
give capacity. Hence all component families are the same singleton
\(\{B_*\}\). Each component must miss at least one root from every
one of the other \(a\) blocks. By (3.1), it misses exactly those
\(a\) roots, misses no singleton label and no root of \(B_*\), and
has all of \(Z\) as its internal boundary. Therefore

\[
 |\partial_S(Y)|=(k-a)+a=k,
\]

contradicting the no-tight assumption (2.1). Thus \(C\) has no
separator of order at most \(q-1\): it is \(q\)-connected, and in
particular three-connected.

## 4. Bare webs and one common portal face

Choose two blocks \(B_i,B_j\). Their packet fails. Apply the
set-terminal Two Paths Theorem stated precisely in Section 6 below to
their four full portal sets. An
inserted clique part behind a facial triangle would have relative
boundary consisting of:

* at most three rib vertices or represented labels; and
* the \(k-4\) omitted boundary labels.

Its boundary would have order at most

\[
 3+(k-4)=k-1,
\]

contrary to (1.2). Thus the web is bare: \(C\) is planar and has a
face \(F_{ij}\) containing all four full portal sets.

The inserted part is a proper subset of \(C\). Indeed a facial triangle
contains at most three of the four artificial terminals, while fullness
supplies an edge from \(C\) to every artificial terminal; hence all of
\(C\) cannot lie behind one such triangle.

The \(q\)-connected planar graph \(C\) forces \(q\le5\). Its embedding
is unique up to reflection.

For distinct \(i,j,h\), suppose \(F_{ij}\ne F_{ih}\). Their
intersection contains both full portal sets of \(B_i\). Distinct faces
of a three-connected plane graph meet in at most a vertex or one edge,
so those two portal sets lie in a connected carrier \(X\) of order at
most two.

Let \(Y\) be a component of \(C-X\), nonempty by (2.4). For every one
of the other \(q-1\) blocks, packet failure makes \(Y\) miss one root.
Consequently

 \[
 |\partial_S(Y)|
 \le 2+k-(q-1)=k-q+3\le k.                       \tag{4.1}
 \]

For \(q>3\), (4.1) contradicts (1.2); for \(q=3\), equality contradicts
the no-tight assumption (2.1). Hence all faces \(F_{ij}\) coincide.
The common outer face contains every vertex of every portal set of all
\(2q\) pair roots.

## 5. Curvature contradiction

Triangulate all bounded faces. An interior vertex has no contact with
any pair root, and can see only the \(s\) singleton labels in \(S\).
Equation (2.1) gives

\[
 d_T(x)\ge d_C(x)\ge(k+1)-s=2q+1\ge7
 \quad(x\in\operatorname{int}T).                 \tag{5.1}
\]

For a boundary vertex, (2.3) gives

\[
 d_T(x)\ge q+1\ge4.                              \tag{5.2}
\]

The disk-curvature identity

\[
 \sum_{\operatorname{int}T}(6-d_T(x))
 +\sum_{\partial T}(4-d_T(x))=6
\]

now has nonpositive left side, a contradiction. This proves
Theorem 1.1. \(\square\)

## 6. Exact external dependency

The only structural theorem used above is the following set-terminal
form of the generalized Two Paths Theorem.

> **Set-terminal Two Paths/Web Theorem.** Let \(H\) be a graph and
> let \(P_1,P_2,P_3,P_4\) be nonempty vertex subsets. Add four
> independent artificial terminals \(t_i\), with
> \(N(t_i)=P_i\), in cyclic frame order
> \(t_1,t_2,t_3,t_4\). If there are no vertex-disjoint connected
> subgraphs joining \(P_1\) to \(P_3\) and \(P_2\) to \(P_4\), then
> an edge-maximal same-vertex completion is a web: a planar rib with
> those four frame terminals on its outer face, together with clique
> parts inserted behind facial triangles. Every neighbour outside an
> inserted clique part belongs to its supporting facial triangle.

This is exactly the form used in Lemma 3.1 of
`hadwiger_three_pair_common_web.md`. Theorem 1.1 is conditional only
on this set-terminal formulation being available from the generalized
Two Paths Theorem; Section 4 uses no stronger rooted-minor or
linkedness assertion.

## 7. Why this matters for general Hadwiger

The theorem is a uniform finite-boundary criticality mechanism:

\[
 \text{packet failure}
 \Longrightarrow
 \text{relative separator or common web}
 \Longrightarrow
 \text{tight adhesion}.
\]

It applies whenever a counterexample-derived decomposition supplies the
local inequality (1.2), even if the whole graph is not
\((2q+s)\)-connected. The remaining general-\(t\) task is to produce a
palette-tight pair mode on a relative shore of this form, or to turn
failure of (1.2) itself into the colour-gluable separator.
