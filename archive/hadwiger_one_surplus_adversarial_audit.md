# Adversarial audit of the one-surplus rooted-model principle

## 1. Verdict and indispensable scope correction

Theorems 1.1, 3.1, and 5.1 and Corollaries 5.2--5.3 of
`hadwiger_one_surplus_rooted_model_principle.md` are correct with the
following explicit interpretation.

> A **grouping** is obtained only by omitting some of the displayed
> pieces and taking unions of whole displayed pieces.  It may neither
> split a displayed piece nor use a vertex outside their union.

Under this interpretation, Theorems 1.1 and 5.1 are exact.  Without it,
Theorem 1.1 is false.  For example, let \(r=2\), let the three \(D_i\)
be independent rooted singleton vertices, and add an outside vertex
\(w\) adjacent to all three.  The support complement is \(K_3\), but

\[
                 D_1\cup\{w\}\cup D_3,\qquad D_2
\]

are two adjacent connected rooted branch sets.  Similarly, allowing a
multi-root displayed piece to split can create a rooted model invisible
in its support quotient.

The rootedness claims after an omission or a merge are correct: every
retained singleton is rooted and every nonsingleton union contains a
rooted displayed piece.  Corollaries 5.2 and 5.3 correctly allow the two
new halves to be unrooted, because they merge the halves with rooted
motif pieces.

## 2. Static claims

### 2.1 The one-surplus obstruction list is complete

With \(r+1\) indivisible support vertices and \(r\) branch sets, either
one support vertex is omitted, or all vertices are used and exactly one
pair is merged.  These are exactly the one-cover and admissible
two-cover alternatives in the complement.

The three minimal failures are precisely

\[
                         K_3,\qquad P_4,\qquad 3K_2.
\]

The only step worth making explicit in the written proof is the standard
fact that a connected graph with no (non-induced) \(P_4\) is a star or
a triangle.  If it is acyclic, its diameter is at most two and it is a
star.  If it has a cycle, it has a triangle; any further vertex in that
component creates a three-edge path, so the component is exactly that
triangle.

### 2.2 Full-shore lifting is valid

In Theorem 3.1 the spanning hypothesis is exactly what makes a quotient
separator an ambient vertex separator.  If \(Z\) is inclusion-minimal
between two fixed connected unions \(A,B\), then every \(z\in Z\) lies
on an \(A\)-\(B\) path in \(H-(Z-\{z\})\).  The two neighbours of \(z\)
on this path lie in the two reachable components of \(H-Z\).  Hence

\[
                         N_H(R_A)=Z=N_H(R_B).
\]

The counts \(r-2\) for \(K_3,P_4\), and \(r-1\) for \(3K_2\), are
correct.  So are the portal-surplus bounds.

For the \(HC_7\) application, \(\kappa(G)\ge7\) implies
\(\kappa(G-v)\ge6\).  If \(|Z|=6\), both selected shores contain an
unchanged rooted quotient piece and therefore see \(v\).  Thus
\(Z\cup\{v\}\) really is a full seven-vertex adhesion in \(G\).

### 2.3 The two-surplus list and the two bisections are valid

For \(r+2\) indivisible support vertices grouped into \(r\) sets, the
four possible size patterns are exactly:

1. two omissions;
2. one omission and one pair;
3. one triple;
4. two pairs.

The adjacency conditions in Theorem 5.1 are necessary and sufficient
for those four patterns.  In Corollary 5.2, if the two halves each see
at least two vertices of the missing triangle, their masks have a common
triangle vertex and their union is all three vertices; the displayed
two-pair construction is valid.  In Corollary 5.3 every asserted
adjacency is also necessary in the displayed construction, and the two
pairs are rooted through \(v_2,v_3\).

In both corollaries, “split” must mean an adjacent connected partition
of the old piece.

## 3. Exact dynamic converse: capacity states and two-linkages

Let \(D\) be a connected old universal piece.  For a motif vertex \(i\),
write

\[
 P_i=\{x\in V(D):x\text{ has a neighbour in the motif piece }i\}.
\]

A connected bisection is a partition \(V(D)=X\mathbin{\dot\cup}Y\)
with \(D[X]\) and \(D[Y]\) nonempty and connected.  The following
elementary extension observation is useful.

### Lemma 3.1 (two connected sets extend to a bisection)

If \(A,B\) are disjoint connected subgraphs of a connected graph \(D\),
then there is a connected bisection \((X,Y)\) with \(A\subseteq X\) and
\(B\subseteq Y\).

#### Proof

Contract \(A\) and \(B\), take a spanning tree of the resulting graph,
and delete an edge of the unique path between the two contracted
vertices.  The preimages of the two tree components give the required
bisection. \(\square\)

### Theorem 3.2 (exact triangle-bisection converse)

For three nonempty portal classes \(P_a,P_b,P_c\), the following are
equivalent.

1. There is a connected bisection whose two sides each meet at least two
   of the three portal classes.
2. For some permutation \((i,j,k)\) of \((a,b,c)\), there are two
   vertex-disjoint connected subgraphs \(L,R\) such that

   \[
      L\cap P_i\ne\varnothing,\quad L\cap P_j\ne\varnothing,
      \qquad
      R\cap P_i\ne\varnothing,\quad R\cap P_k\ne\varnothing.
      \tag{3.1}
   \]

Equivalently, for some class \(P_i\), there is a forked two-linkage
joining one copy of \(P_i\) to \(P_j\) and a disjoint copy of \(P_i\)
to \(P_k\).

#### Proof

Given the bisection, the two masks have size at least two and their union
is all three classes.  They therefore have a common class \(i\), and the
other two classes can be chosen as \(j\) on one side and \(k\) on the
other.  Take \(L=D[X]\), \(R=D[Y]\).  Conversely apply Lemma 3.1 to
\(L,R\). \(\square\)

Thus persistent failure of Corollary 5.2 has an exact dichotomy:

* **capacity failure:** no portal class can be used at two distinct
  vertices in the required fork; or
* **state/routing failure:** every possible forked two-linkage is
  obstructed.

Capacity cannot be omitted.  Even if \(D\) is an arbitrarily large
complete graph, assigning the three portal classes to three distinct
single vertices gives no good triangle bisection.  Hence failure does
not, by itself, force any small internal separator.

### Theorem 3.3 (exact path-bisection converse)

For portal classes \(P_1,P_2,P_3,P_4\), a connected bisection satisfying

\[
       X\cap P_1,X\cap P_2,Y\cap P_3,Y\cap P_4\ne\varnothing
       \tag{3.2}
\]

exists if and only if \(D\) contains two vertex-disjoint connected
subgraphs, one meeting \(P_1,P_2\) and the other meeting \(P_3,P_4\).
Equivalently it contains the corresponding set-to-set two-linkage.

#### Proof

The two sides of a bisection give the two subgraphs.  The converse is
Lemma 3.1. \(\square\)

Failure of Corollary 5.3 is therefore exactly a two-path obstruction.
A small separator alone is not a valid converse: a cycle with four
singleton portals in alternating cyclic order is 2-connected but has no
linkage for the crossing pairing.  The unavoidable second outcome is a
web/portal-order obstruction of the Two Paths Theorem.

For either Theorem 3.2 or 3.3, the set version reduces to the ordinary
four-terminal version by adjoining new terminal leaves complete to the
corresponding portal sets (using two clones of the repeated class in
Theorem 3.2).  Consequently, an edge-maximal failure has precisely the
separator/web form supplied by the Two Paths Theorem.  This is the
rigorous dynamic converse available without assuming that \(D\) is
2-connected.

## 4. A local block-level portal-order consequence

The triangle case also gives a useful elementary obstruction before the
full web theorem is invoked.

### Lemma 4.1 (duplicated portal in one block)

Let \(W\) be a 2-connected block of \(D\).  Suppose that, for some
permutation \((i,j,k)\), the block contains distinct vertices
\(s,t\in P_i\), a vertex \(b\in P_j\), and a vertex \(c\in P_k\) with
\(b\ne c\).  Then \(D\) has a good triangle bisection.

#### Proof

Take an \(s\)-\(t\) bipolar ordering of \(W\).  If \(b\) precedes
\(c\), cut the ordering between them; otherwise reverse their roles.
Every prefix and suffix of a bipolar ordering is connected.  The prefix
contains \(s\) and the earlier one of \(b,c\), while the suffix contains
\(t\) and the later one, so both sides meet two portal classes.

Every component of \(D-V(W)\) attaches to a maximal 2-connected block
at at most one vertex: two attachments would give an ear enlarging the
block.  Assign each such component to the side containing its attachment.
This extends the cut of \(W\) to a connected bisection of \(D\).
\(\square\)

Hence, if every triangle bisection fails, then in every 2-connected
block \(W\), whenever one portal class occurs at two distinct vertices,
the other two portal classes cannot have distinct representatives in
that block.  Either one of them is absent from \(W\), or both are
concentrated at the same single vertex.  Duplicated portals that evade
this rule must be ordered through the block-cut tree.  This is a precise
capacity--state portal-order obstruction; it does not incorrectly infer
an internal cutvertex when the true obstruction is lack of portal
capacity or a 2-connected web.

## 5. Audit of the operation-state continuation

The Mader min--max formula used in Theorem 2.1 of
`hadwiger_atomic_portal_order_operation_states.md` is correct.  Its
boundary set is

\[
 B_i=\{u\in U_i:u\text{ is a terminal or has a neighbour outside }
 U_0\cup U_i\},
\]

and value one gives exactly the two displayed numerical patterns.
Theorems 2.1 and 3.1 are therefore valid.

Four later qualifications are necessary.

### 5.1 A completion does not confine bridges of the original graph

Lemma 3.2 is valid as a statement about \(W\cup C\), but its claimed
consequence for an obstruction in the original graph is false.  A
linkage created in the completion can use completion edges other than
the one replaced by \(C\).

Here is an explicit counterexample.  Let \(W\) be the five-wheel, with
its four outer terminals in cyclic order

\[
                         s_1,s_3,s_2,s_4.
\]

It is edge-maximal without disjoint \(s_1s_2\)- and
\(s_3s_4\)-paths: its only missing outer diagonals are \(s_1s_2\) and
\(s_3s_4\), and adding either one gives the other path through the hub.
Let \(D\) consist of the outer four-cycle and the hub joined only to
\(s_1\).  Add an external path \(C=s_1cs_2\).  The attachments
\(s_1,s_2\) are nonadjacent in \(W\), and \(W\cup C\) is linkable, but
\(D\cup C\) is not: every \(s_3s_4\)-path in \(D\) uses \(s_1\) or
\(s_2\).

Thus actual bridge confinement needs a stable-bridge/minimal-linkage
argument; it cannot be read off from an independently completed web.

### 5.2 The gate separation must be induced

Lemma 4.1 is correct only when \((L,R)\) is a separation of
\(H[V(D)]\), not merely of a chosen connected subgraph on \(D\).  For
example, in \(H=K_3\), take \(D\) to be a spanning two-edge path.  Its
middle vertex is a one-vertex gate in the chosen path, but the omitted
triangle edge crosses the two open sides and there is no component of
\(H-D\).  With the induced-subgraph formulation, the component-assignment
proof is valid.

### 5.3 Open-shore operations need both endpoints off the adhesion

The hypothesis

\[
 e_A\in E(H[A])-E(H[B])
\]

allows an edge from \(A-X\) to \(X\).  Contracting such an edge does not
preserve the opposite closed shore or the boundary literally.  The
“strictly open-shore supported” conclusion in Theorem 5.1 therefore
requires

\[
                 e_A\in E(H[A-X]),\qquad
                 e_B\in E(H[B-X]).
\]

With this correction, item 1 is the standard crossed-splicing argument.
Items 2--3 are valid if a *repair* is defined to be a single Kempe switch
which separates the operated endpoints while leaving every boundary
colour fixed.  If each side admitted such a repair, item 1 would be
contradicted.  On a locked side, for each second colour, the two endpoint
components are therefore either equal (giving the bichromatic detour) or
both meet the marked boundary.  The present prose should state this
definition rather than suggest a stronger arbitrary-recolouring claim.

### 5.4 The matching exchanges require the exact atomic support

Theorems 7.1 and 7.2 use that every two vertices belonging to different
matched pairs are adjacent.  This follows in exactly
\(K_7-3K_2\), but not from the mere presence of a \(3K_2\) certificate
in the complement.  Both theorems are correct after assuming the exact
support graph (or listing the cross-pair adjacencies used in the proof).
They are not justified in a quotient with additional nonedges.
