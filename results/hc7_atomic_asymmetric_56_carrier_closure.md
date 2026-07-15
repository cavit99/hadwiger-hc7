# Atomic asymmetric `(5,6)` carrier closure

**Status:** proved and independently audited.

## 1. Setup

Use the connected-bipartite atomic exact-seven interface

\[
 V(G)=A\mathbin{\dot\cup}S\mathbin{\dot\cup}R,
 \qquad S=W\mathbin{\dot\cup}\{u\},\qquad |S|=7,
\]

where:

1. `G` is strongly seven-contraction-critical and is not six-colourable;
2. there is no `A-R` edge;
3. `A` is connected and `S`-full;
4. `zu` is the unique `A-u` edge;
5. `H=G[S]` is connected and bipartite; and
6. `R` contains two disjoint connected `S`-full packets.

The adaptive clique-reservoir carrier return may therefore be used once two
adjacent connected carriers admit a proper two-list colouring of `H` after
deleting an empty or singleton clique reservoir.

## 2. The asymmetric carrier theorem

### Theorem 2.1 (unordered asymmetric support)

Suppose

\[
                         A=X\mathbin{\dot\cup}Y,
\]

where `X,Y` are nonempty connected adjacent sets, `z in Y`, and

\[
 \min\{|N_S(X)|,|N_S(Y)|\}\ge5,
 \qquad
 \max\{|N_S(X)|,|N_S(Y)|\}\ge6.                           \tag{2.1}
\]

Then `G` is six-colourable.

### Proof

Put

\[
 D_X=S-N_S(X),\qquad D_Y=S-N_S(Y).
\]

Since `X union Y=A` and `A` is `S`-full,

\[
                         D_X\cap D_Y=\varnothing.           \tag{2.2}
\]

The unique `A-u` edge is `zu`, and `z in Y`.  Hence

\[
 u\in D_X,\qquad u\notin D_Y.                              \tag{2.3}
\]

First suppose

\[
 D_X=\{u\}\text{ or }\{u,p\},
 \qquad |D_Y|\le1.                                        \tag{2.4}
\]

Give a vertex of `S` the singleton list `{Y}` if it belongs to `D_X`, the
singleton list `{X}` if it belongs to `D_Y`, and the list `{X,Y}` otherwise.
Fix the bipartition of the connected bipartite graph `H`.

If all vertices of `D_X` lie in one bipartition class, orient that class to
`Y`.  If the possible vertex of `D_Y` lies in the same class, delete it as
the singleton reservoir `U`; otherwise put `U=emptyset`.

It remains to consider the case in which `D_X={u,p}` and its two vertices
lie in opposite bipartition classes.  If `D_Y={q}`, retain from `D_X` the
vertex opposite `q`, delete the other member of `D_X` as `U`, and orient the
retained member's class to `Y`.  If `D_Y` is empty, delete either member of
`D_X` and use the orientation prescribed by the other.

This completes the construction when (2.4) holds.  If (2.4) does not hold,
the other orientation of (2.1) gives

\[
                         D_X=\{u\},\qquad |D_Y|\le2.       \tag{2.5}
\]

Let `C_0,C_1` be the bipartition classes of `H`, with `u in C_0`.  If
`D_Y subseteq C_1`, orient `C_0` to `Y` and `C_1` to `X`, deleting
nothing and put `U=emptyset`.  If `D_Y` has one member in each class,
delete its member in `C_0` as `U` and use the same orientation.  If
`D_Y subseteq C_0` and is nonempty, put `U={u}`; in every component of
`H-u` containing a member of
`D_Y`, orient that member's bipartition side to `X`, and orient every
remaining component arbitrarily.  All surviving prescriptions are
respected.  The empty `D_Y` case was already covered by the first choice.

Thus in every case `U` is empty or a singleton, and `H-U` has a proper list
colouring.  If `H-U` has an edge, both carrier labels occur automatically
in any component containing an edge.  If `H-U` is independent, six vertices
survive and at most two have singleton lists; assign a flexible vertex the
otherwise missing label.  Both colour classes are therefore nonempty.

The two classes are independent seed sets contacted by their named
carriers, and `U` is a clique.  The audited adaptive clique-reservoir return,
using the two full packets in `R`, six-colours `G`.  \(\square\)

## 3. Degree and planarity consequences

### Corollary 3.1

There is no vertex `v ne z` such that

\[
                         d_{G[A]}(v)\le2
             \quad\text{and}\quad A-v\text{ is connected}.       \tag{3.1}
\]

### Proof

Take `X={v}` and `Y=A-v`.  The sets are nonempty, connected and adjacent,
and `z in Y`.  Since `R` is nonempty and has no edge to `A`, relative
seven-connectivity applied first to `X` and then to `Y` gives

\[
 |N_S(X)|\ge7-d_{G[A]}(v)\ge5,
 \qquad |N_S(Y)|\ge6.
\]

Theorem 2.1 applies.  \(\square\)

The atomic shore is already known to be two-connected and to satisfy
`d_A(z)>=3`.  Deleting any vertex therefore leaves it connected, so
Corollary 3.1 gives

\[
                              \delta(G[A])\ge3.               \tag{3.2}
\]

Every two-connected outerplanar graph has at least two vertices of degree
two.  Consequently no surviving atomic shore is outerplanar.  In
particular, the entire outerplanar branch of the four-root rural outcome is
closed uniformly; any surviving rural disk has a genuine interior torso.

## 4. Exact boundary of the theorem

The symmetric support vector `(5,5)` is the first profile not covered by
Theorem 2.1 and is not a list-theoretic corollary.
For example, on the tree with edges

\[
                    01,12,23,24,25,26,
\]

take `u=0`, `D_X={0,1}` and `D_Y={2,3}`.  The two forced vertices for each
carrier span the edges `01` and `23`.  Deleting one singleton cannot remove
both monochromatic edges.  Thus a symmetric two-rung seam needs additional
host geometry: it must be re-split asymmetrically or yield rooted clique
bags.

Likewise, (3.2) does not close a general rural disk.  It removes the
outerplanar strip, but a planar minimum-degree-three shore may contain
interior bridges.  The next proof must exploit their bounded attachment
sets, not merely their contact counts.
