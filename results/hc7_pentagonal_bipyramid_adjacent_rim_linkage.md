# An adjacent-rim linkage in a pentagonal-bipyramid expansion

**Status:** written proof; separately audited **GREEN AS PATCHED** in
[`hc7_pentagonal_bipyramid_adjacent_rim_linkage_audit.md`](hc7_pentagonal_bipyramid_adjacent_rim_linkage_audit.md).

This note gives a label-preserving completion theorem for arbitrary connected
columns whose contact graph is the pentagonal bipyramid.  It does not assume
that the columns are paths or trees.  Its negative case is an exact family of
five set-terminal Two Paths obstructions.

## 1. Setup

Let `P` be the pentagonal bipyramid.  Write its two nonadjacent poles as
`a,b` and its rim, in cyclic order, as

\[
                          r_0r_1r_2r_3r_4r_0.
\]

Let `F` have a vertex partition into seven nonempty connected subgraphs

\[
             C_a,C_b,C_0,C_1,C_2,C_3,C_4                         \tag{1.1}
\]

whose contact graph is exactly `P`: two different columns have an edge
between them if and only if their labels are adjacent in `P`.

Let `R_0,R_1` be disjoint connected subgraphs outside `F`, adjacent to one
another and each adjacent to every column in (1.1).

All rim subscripts below are read modulo five.

## 2. The completion theorem

### Theorem 2.1 (adjacent-rim linkage completion)

Fix \(i\).  Suppose that \(C_i\cup C_{i+1}\) contains two vertex-disjoint
connected subgraphs `X,Y` such that

\[
\begin{aligned}
 E(X,C_a)&\neq\varnothing,& E(X,C_b)&\neq\varnothing,\\
 E(Y,C_{i-1})&\neq\varnothing,& E(Y,C_{i+2})&\neq\varnothing.     \tag{2.1}
\end{aligned}
\]

Then `F` contains a `K_5`-minor model whose five branch sets each contain a
different whole column.  Together with `R_0,R_1`, this gives an explicit
`K_7`-minor model.

### Proof

Consider the five sets

\[
 C_a\cup X,\qquad
 C_b,\qquad
 C_{i-1}\cup Y,\qquad
 C_{i+2},\qquad
 C_{i+3}.                                                     \tag{2.2}
\]

They are pairwise disjoint.  The first and third are connected by (2.1),
and the remaining three are columns and hence connected.

Among the five old pentagonal-bipyramid labels

\[
                 a,b,r_{i-1},r_{i+2},r_{i+3},                  \tag{2.3}
\]

the only absent adjacencies are `ab` and `r_{i-1}r_{i+2}`.  The subgraph
`X` repairs the first: it belongs to the branch set containing `C_a` and
has an edge to `C_b`.  The subgraph `Y` repairs the second: it belongs to
the branch set containing `C_{i-1}` and has an edge to `C_{i+2}`.  Every
other pair in (2.2) is adjacent through an old quotient edge.  Thus (2.2)
is a `K_5`-minor model.

Each branch set in (2.2) contains one of the five whole columns displayed
in (2.3).  Hence each is adjacent to both `R_0` and `R_1`.  Those roots are
connected, disjoint from the five sets, and adjacent to one another.
Consequently the five sets in (2.2), together with `R_0,R_1`, are seven
branch sets of a `K_7`-minor model.  \(\square\)

### Corollary 2.2 (alternating connected column split)

Fix any label `x in V(P)`.  Suppose

\[
                         V(C_x)=A\mathbin{\dot\cup}D
\]

where `F[A]` and `F[D]` are nonempty and connected.  Suppose there are
four distinct labels `y_1,y_2,y_3,y_4`, in this cyclic order around `x`,
such that `A` contacts `C_{y_1},C_{y_3}` and `D` contacts
`C_{y_2},C_{y_4}`, after possibly interchanging `A,D`.  Then the graph
induced by the two roots and the seven columns contains an explicit
`K_7`-minor model.

### Proof

Since `C_x` is connected and its vertex set is partitioned into the two
nonempty sets `A,D`, an edge joins them.  Split the quotient vertex `x`
into adjacent vertices `x_A,x_D`, assigning every old neighbour label to
each side on which it has a literal contact.  Every old neighbour is
assigned at least once, and the four displayed labels alternate.

The audited pentagonal-bipyramid vertex-split theorem gives a `K_5` model
in this split quotient.  Use its explicit model, in which every one of the
five branch sets contains an old nonsplit vertex of `P`.  Lift old vertices
to their whole columns and lift `x_A,x_D` to `A,D`.  Literal contacts make
the five lifted sets connected and pairwise adjacent.  Every lifted set
contains a whole nonsplit column, so both fixed roots contact all five.
Together with the root-root edge, the two roots and these five sets are an
explicit `K_7`-minor model.  \(\square\)

## 3. Exact negative formulation

For a fixed `i`, form an auxiliary graph `H_i` from
\(F[C_i\cup C_{i+1}]\) by adding four new vertices
\(\alpha,\beta,\gamma,\delta\).  Join them respectively to the vertices of
\(C_i\cup C_{i+1}\) which have a
neighbour in

\[
                         C_a,C_b,C_{i-1},C_{i+2}.               \tag{3.1}
\]

There are connected subgraphs `X,Y` as in Theorem 2.1 if and only if `H_i`
has vertex-disjoint paths joining `alpha` to `beta` and `gamma` to `delta`.
Indeed, the interiors of two such paths give `X,Y`; conversely, take one
path through each of the two connected subgraphs.

### Corollary 3.1 (five simultaneous Two Paths obstructions)

If the graph induced by the two roots and the seven columns has no
`K_7` minor, then for every \(i\in\mathbb Z/5\mathbb Z\), the auxiliary graph
\(H_i\) has no
pair of vertex-disjoint paths joining

\[
                       (alpha,beta)\quad\hbox{and}\quad
                       (gamma,delta).                           \tag{3.2}
\]

Thus a surviving pentagonal-bipyramid expansion is not described merely by
the absence of a local alternating cut.  It carries five coupled negative
Two Paths instances, one on every pair of adjacent rim columns.

## 4. Repeated contacts are forced in a five-connected tree expansion

The repeated-contact obstruction is not optional in the live
five-connected branch.  Suppose, in addition, that every induced column
graph `F[V(C_x)]` is a tree.  Put

\[
 n=|V(F)|\quad\hbox{and}\quad
 m=\sum_{xy\in E(P)}|E_F(C_x,C_y)|.
\]

The tree edges contribute \(n-7\) edges, so

\[
                              |E(F)|=n-7+m.                    \tag{4.1}
\]

If \(F\) is five-connected, then its minimum degree is at least five.
Consequently

\[
  5n\le 2|E(F)|=2n-14+2m,
  \qquad\hbox{and hence}\qquad
  m\ge \left\lceil\frac{3n+14}{2}\right\rceil.                \tag{4.2}
\]

In particular, because \(n\ge7\), one contact on each of the fifteen
quotient edges is impossible in the five-connected core.  Thus the
single-contact tree theorem is a genuine unbounded theorem before the
connectivity reduction, but the live five-connected residue necessarily
uses repeated contacts.  Any proof of that residue must exploit their
placement rather than treat them as a perturbation.

## 5. Trust boundary and next structural target

Theorem 2.1 is independent of connectivity and of colouring criticality.
Five simultaneous failures in Corollary 3.1 can coexist even in a
five-connected nonplanar pentagonal-bipyramid expansion.  More strongly,
the audited
[split/linkage/planarity barrier](../barriers/hc7_pentagonal_bipyramid_split_linkage_planarity_barrier.md)
has neither a positive adjacent-rim linkage nor an alternating connected
split in any column.  It is nevertheless nonplanar and five-connected.
Thus neither the five negative Two Paths certificates alone nor their
combination with the one-column split test implies planarity or a cut of
order at most four.

In the live order-eight application, maximal enlargement of the columns
makes their union span the graph outside the three roots, and the resulting
core is five-connected and nonplanar unless an actual order-seven
separation has already occurred.  The next unbounded statement must include
a genuinely global allocation mechanism:

> produce an anchored `K_5` model, possibly by simultaneously dividing and
> absorbing parts of several columns; or return a cut of order at most four
> or a compatible planar representation and hence a six-colouring.

Theorem 2.1 supplies the adjacent-rim positive branch, and Corollary 2.2
supplies the alternating-split branch for arbitrary connected columns.
They are useful sufficient certificates, but they are not an exhaustive
local characterization.  In the barrier, the anchored `K_5` model divides
two omitted columns between two different branch sets.  Nothing here
proves the required multi-column allocation/separator theorem or `HC_7`.
