# Atomic three-pair nonowners cannot be minimum fragments

## 1. Statement

Let \(G\) be seven-connected with minimum degree at least seven. Let
\(S\) be a seven-cut, let \(D\) be a minimum fragment behind \(S\),
and assume there is a nonempty far shore. Fix a boundary mode

\[
 S=A\mathbin{\dot\cup}B\mathbin{\dot\cup}C
   \mathbin{\dot\cup}\{r\},\qquad |A|=|B|=|C|=2. \tag{1.1}
\]

Say that \(D\) is a **nonowner** of this mode when it contains no two
vertex-disjoint carriers for any two distinct blocks among \(A,B,C\).

### Theorem 1.1 (three-block atomic ownership)

If \(|D|\ge6\), then \(D\) is not a nonowner. Equivalently, every
minimum fragment of order at least six has two-block capacity for every
mode of the form (1.1).

The theorem uses no Moser labels and no finite boundary atlas.

### Theorem 1.2 (arbitrary nonsingleton shore: packet or exact adhesion)

Let (C) be any full component of (G-S) of order at least two, with a
nonempty far shore, and fix any mode (1.1).  Then at least one of the
following holds:

1. (C) has two-block capacity for the mode;
2. a nonempty proper connected subset of (C) is a component behind another
   exact seven-cut.

In particular, every packet-deficient accepting shore for a normalized
four-block transition exposes an exact adhesion.

#### Proof

Assume (C) has no two-block capacity.  If some (x\in C) has degree seven,
then (N_G(x)) is an exact seven-cut: ({x}) is an isolated component after
its deletion and the far shore remains.  Since (|C|\ge2), this is a proper
fragment of (C), giving conclusion 2.  We may therefore assume every vertex
of (C) has degree at least eight.

The small-carrier theorem shows that
no vertex of (C) can contact both roots of one pair block: a singleton
carrier forces a packet, with no exact-cut alternative.  Hence every vertex
has at most four neighbours in (S), one in each pair block and possibly
the singleton (r), and therefore

\[
d_C(x)\ge4.                                      \tag{1.3}
\]

If |C| ≤ 4, the degree bound

\[
d_G(x)\le (|C|-1)+4\le7
\]

contradicts the already proved minimum degree eight.  Let |C| = 5.  Then
(1.3) makes (C=K_5).  Choose portal vertices for the two roots of one pair
block.  They are distinct (there is no singleton carrier), and their edge is
a two-vertex carrier with nonempty complement.  The small-carrier theorem
gives either a packet or an exact seven-cut.  The former is excluded, so
conclusion 2 holds.

If |C| = 6, the six portal sets belonging to
the pair blocks have an SDR: a Hall failure for (I) labels either gives a
cut of order at most six or would require
6 = |C| < |I| ≤ 6.  Equation (1.3) makes (C) a (K_6) with at most a
matching deleted.  The two unused representatives route any two prescribed
pair demands exactly as in Section 4, giving a packet, a contradiction.

Let |C| ≥ 7.  Apply the separator-capacity theorem with the three pair
blocks.  A cutvertex forces capacity.  A two-separator either forces capacity
or exposes the exact cut in outcome 2.  Thus, unless conclusion 2 already
holds, (C) is three-connected.

Apply three-packet synchronization.  Its nonplanar branch is already the
exact-cut conclusion.  In the remaining branch, (C) has a plane disk
embedding with all six pair-root portal sets on one outer face.  Triangulate
the bounded faces.  An interior vertex has no neighbour in any pair root and
can see only (r) in (S), so its triangulated degree is at least seven.
An outer vertex has at most four boundary neighbours, so (1.3) gives
triangulated degree at least four.  The disk-curvature identity would then
have a nonpositive left side, contrary to its value six.  This contradiction
proves that the exact-cut branch must have occurred. \(\square\)

### Corollary 1.3 (an atomic three-shore pair-mode cut is impossible)

Assume \(G\) is six-minor-critical and \(G-S\) has at least three full
components. Fix one mode (1.1). Then some nonsingleton component
contains a proper exact seven-fragment.

In particular, if one component is a full singleton (the apex at a
degree-seven Moser neighbourhood) and there are two exterior
components, one exterior component exposes a proper exact seven-cut.

#### Proof

Suppose no nonsingleton component has a proper exact fragment.
Theorem 1.2 makes every nonsingleton component an owner of the fixed
mode. Among any three full components, the at-most-one-capacity theorem
allows at most one owner. Hence there is at most one nonsingleton
component.

But an exact cut in a minor-critical graph has at most one full
singleton component: two would be nonadjacent false twins. Thus there
are at most two components in total, contrary to the hypothesis.
\(\square\)

This corollary eliminates the whole atomic two-exterior Moser cell
without examining portal orders. It does not eliminate descent itself:
after passing to the new exact cut, its boundary need not retain the
Moser pair mode.

## 2. Minimum fragments have degree at least eight

### Lemma 2.1

Every vertex of \(D\) has degree at least eight in \(G\).

#### Proof

Suppose \(d_G(x)=7\). Then \(N_G(x)\) is a seven-cut: after deleting
it, \(\{x\}\) is an isolated component, while the far shore is still
present because distinct components of \(G-S\) are anticomplete. Thus
\(\{x\}\) is a fragment of order one, smaller than \(D\), contrary to
the choice of \(D\). \(\square\)

## 3. A nonowner has no short block carrier

### Lemma 3.1

If \(D\) is a nonowner and \(|D|\ge4\), every carrier of any one of
\(A,B,C\) has order at least three. Consequently no vertex of \(D\)
has neighbours at both roots of one pair block.

#### Proof

Let \(X\subseteq D\) be a carrier of one block with \(|X|\le2\).
Since \(|D|\ge4\), the complement \(D-X\) is nonempty. The uniform
small-carrier exchange theorem, applied to the three pair blocks, gives
either two-block capacity or an exact seven-cut whose shore is a proper
connected subset of \(D\). The first contradicts nonownership. The
second contradicts the minimum choice of \(D\). Hence no such \(X\)
exists. The singleton assertion is immediate. \(\square\)

It follows from Lemmas 2.1 and 3.1 that

\[
 d_D(x)\ge4\qquad(x\in D),                        \tag{3.1}
\]

because \(x\) has at most one boundary neighbour in each of \(A,B,C\)
and at most the singleton neighbour \(r\), hence at most four neighbours
in \(S\).

## 4. The six-vertex base is impossible

Assume first that \(|D|=6\). The six portal sets belonging to
\(A\cup B\cup C\) have an SDR by the relative portal Hall lemma.
Let the six distinct representatives be the terminals of the three
pair demands.

Equation (3.1) says that the complement of \(D\) has maximum degree at
most one. Thus \(D\) is \(K_6\) with a (possibly empty) matching
deleted. Any two prescribed disjoint terminal pairs have disjoint
connecting paths:

* use the two terminal edges when both are present;
* if one demanded edge is absent, route it through either unused
  vertex and use the other demanded edge directly; and
* if both are absent, route them through the two unused vertices,
  one per pair.

An absent demanded edge is itself one of the deleted matching edges, so
each unused vertex is adjacent to both of its ends. These two disjoint
paths are carriers for two blocks, contradicting nonownership.

## 5. Disk curvature eliminates every larger nonowner

Now let \(|D|\ge7\). A minimum fragment has no proper exact
seven-fragment inside it. The separator-capacity theorem therefore makes
the nonowner \(D\) three-connected.

Apply the three-packet synchronization theorem to \(A,B,C\). Its exact
cut outcome is forbidden by minimum-fragment choice, and the six-vertex
core is too small. Hence \(D\) has a plane disk embedding with all six
full portal sets of \(A\cup B\cup C\) on one outer face.

Triangulate all bounded faces without changing the outer face, obtaining
a triangulated disk \(T\). An interior vertex has no neighbour in any
of the six matched boundary roots, because every such portal vertex is
on the outer face. It can see only \(r\) in \(S\). Lemma 2.1 therefore
gives

\[
 d_T(x)\ge d_D(x)\ge7
 \quad\text{for every interior vertex }x.         \tag{5.1}
\]

Euler curvature for a triangulated disk is

\[
 \sum_{x\in\operatorname{int}T}(6-d_T(x))
 +\sum_{x\in\partial T}(4-d_T(x))=6.              \tag{5.2}
\]

If every outer vertex had \(T\)-degree at least four, the left side
would be nonpositive, contradicting (5.2). Thus some outer vertex
\(z\) has \(d_T(z)\le3\). Three-connectivity and the fact that
triangulation only adds edges give

\[
 d_D(z)=3.                                        \tag{5.3}
\]

By Lemma 3.1, \(z\) meets at most one root in each of \(A,B,C\), and
it may also meet \(r\). Hence

\[
 d_G(z)\le d_D(z)+4=7,
\]

contradicting Lemma 2.1. This proves Theorem 1.1. \(\square\)

## 6. Consequence for a three-edge interface

Combine Theorem 1.1 with
hadwiger_three_interface_packet_reduction.md. In the packet-free
complementary-row outcome, the three interface edges form a matching,
so \(|D|\ge6\). Theorem 1.1 then says that \(D\) has two-block
capacity after all. Therefore:

> Every minimum-fragment covering split with exactly three interface
> edges has two-block capacity for every available four-block matching
> transition state.

This closes the entire three-edge branch at the capacity level. The
remaining direction-sensitive issue is global: capacity lies in the
operated minimum shore, while the transition state is accepted by the
opposite shore. The theorem must therefore be combined with ownership
counting or a mode-preserving exchange; packet transfer by itself goes
from the owner to the already accepting side and is not a colouring
contradiction.
