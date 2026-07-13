# Flexible two-target portals split or have one common bottleneck

## Theorem 1.1

Let \(T\) be a connected graph and let \(A,B,C\subseteq V(T)\), where
\(|A|\ge2\) and \(B,C\) are nonempty.  Then at least one of the
following holds.

1. There is a partition

   \[
        V(T)=X\mathbin{\dot\cup}Y
   \]

   such that \(T[X]\) and \(T[Y]\) are connected, \(E_T(X,Y)\ne
   \varnothing\), both sides meet \(A\), and, after possibly exchanging
   the sides,

   \[
        X\cap B\ne\varnothing,qquad Y\cap C\ne\varnothing. \tag{1.1}
   \]

2. There is one vertex \(q\in V(T)\) which meets every path in \(T\)
   from \(A\) to \(B\cup C\).  Equivalently, no component of \(T-q\)
   contains both a vertex of \(A-\{q\}\) and a vertex of
   \((B\cup C)-\{q\}\).

The sets may overlap; a path of order one is allowed when an endpoint
belongs to two terminal sets.

### Proof

Use the standard vertex-capacitated flow network.  Split every vertex of
\(T\) into an in-node and an out-node joined by an arc of capacity one;
replace every graph edge by the two corresponding infinite-capacity
arcs.  Join a source to every member of \(A\) with infinite capacity.
Join every member of \(B\) to a target node \(b\), and every member of
\(C\) to a target node \(c\), again with infinite capacity.  Finally
join \(b,c\) to a common sink by arcs of capacity one.

An integral flow of value two is exactly a pair of vertex-disjoint paths
with distinct initial vertices in \(A\), one ending in \(B\) and the
other in \(C\).  Suppose first that such paths \(P_B,P_C\) exist.  If
they are not adjacent, take a shortest path between them; its internal
vertices avoid both paths.  Absorb its internal vertices into one of the
two paths.  We obtain disjoint connected adjacent sets \(U,V\), both
meeting \(A\), with \(U\) meeting one target class and \(V\) the other.

Contract \(U,V\) to adjacent vertices, take a spanning tree containing
their joining edge, and delete that tree edge.  Its two components,
expanded back into \(T\), give the required connected bipartition
\(X,Y\).  All four terminal incidences survive.

Now suppose the maximum flow has value at most one.  It has value at
least one because \(T\) is connected and all terminal sets are nonempty.
Thus a minimum cut has capacity one.  It cannot consist of just one of
the arcs \(b\)-sink or \(c\)-sink: after deleting either arc, a path
through the other nonempty target class remains.  All other finite arcs
are vertex-capacity arcs of \(T\).  Hence some vertex \(q\) alone
separates the source from both target nodes.  In the original graph every
\(A\)-to-\((B\cup C)\) path contains \(q\), which is outcome 2.
\(\square\)

## HC7 gate application

In the balanced degree-nine Moser lock, suppose the root component
\(K\subseteq L_6-6\) misses both right bags and has strict portal surplus
inside \(L_0\).  Put

\[
 A=N_{L_0}(K),\qquad
 B=N_{L_0}(R_5),\qquad
 C=N_{L_0}(R_0).
\]

The current connectivity reduction gives \(|A|\ge4\).  Outcome 1 of
Theorem 1.1 is exactly the cross-side protected split which the explicit
bag constructions in `hadwiger_degree9_protected_portal_peel.md` turn
into a \(K_7\)-model.  Therefore a minor-free residue has the single
bottleneck in outcome 2.  This replaces a family of prescribed-terminal
Two-Paths webs by one flexible portal cut.

The bottleneck does not by itself finish the case: components on the
\(A\)-side can still have cross-bag contacts into
\(D=L_6-K\).  Those contacts must either be peeled into the explicit
minor model or included in the eventual exact seven-adhesion.  Omitting
this extra portal class would make an invalid separator claim.
