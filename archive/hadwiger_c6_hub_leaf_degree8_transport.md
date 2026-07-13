# A tight `C6+K1` hub leaf becomes a defect-one degree-eight cell

## 1. Setting

Use the tight leaf outcome of Theorem 3.3 and Corollary 3.4 in
`hadwiger_c6_specified_side_warehouse_exchange.md`.  Thus `S` is the old
seven-boundary, `D,H` are its two full shores, and `u in D` has

\[
 P=N_S(u),\qquad
 N_D(u)=\{w\}\dot\cup\{y_s:s\in S-P\},             \tag{1.1}
\]

where

\[
 N_D(s)=\{y_s\}\quad(s\in S-P).                    \tag{1.2}
\]

The sets in (1.1) are disjoint, `|N_G(u)|=8`, and `D-u` is full to
`S`.

Put

\[
 U=N_G(u)=P\dot\cup\{w\}\dot\cup
                  \{y_s:s\in S-P\}                \tag{1.3}
\]

and

\[
 R=D-(\{u,w\}\cup\{y_s:s\in S-P\}).               \tag{1.4}
\]

## 2. Exact exterior structure at `u`

### Theorem 2.1 (hub-leaf transport)

The graph `G-N[u]` has one canonical component `F` containing

\[
                         H\cup(S-P),                \tag{2.1}
\]

and

\[
                         N_U(F)=U-\{w\}.            \tag{2.2}
\]

Moreover `R` is either empty or connected.  When it is nonempty, it is
the only other component of `G-N[u]` and

\[
                         |U-N_U(R)|\le1.             \tag{2.3}
\]

Thus the tight hub leaf is a degree-eight vertex with one or two exterior
components; one component has exact defect `w`, and the possible second
component also has defect at most one.

### Proof

The full shore `H` is connected and adjacent to every vertex of `S`, so
the nonempty set `H union(S-P)` lies in one component `F` of
`G-N[u]`.  Every `p in P` has an edge to `H`, and for every `s in S-P`
the edge `sy_s` puts `y_s` in `N_U(F)`.  Hence `F` sees every vertex of
`U` except possibly `w`.

It does not see `w`.  There is no `D-H` edge.  Also (1.2) says that no
vertex of `D-\{y_s\}`, in particular `w`, is adjacent to any
`s in S-P`.  These are all vertices of (2.1), and no third old shore
exists.  This proves (2.2).

Every vertex of `D` outside `\{u,w\} union \{y_s\}` belongs to `R`.
It has no neighbour in `H`, and by (1.2) it has no neighbour in
`S-P`.  The vertices of `P` have been deleted in `N[u]`.  Therefore
every component of `R` is a component of `G-N[u]`, distinct from `F`.

The audited degree-eight component theorem says that a hypothetical
minimal `HC_7` counterexample has at most two components outside the
closed neighbourhood of a degree-eight vertex.  Hence `R` is empty or
connected.  In the latter case seven-connectivity gives
`|N_U(R)|>=7`; since `|U|=8`, this is (2.3).  QED.

## 3. Consequence

This transport removes the unbounded tight-star endpoint from the
`C6+K1` atom.  It is now one explicit degree-eight two-shore problem:

* one near-full exterior component has the named unique defect `w`;
* the other, when present, has at most one defect; and
* the `P` part of the degree-eight neighbourhood lies in one of the
  clique rows supplied by the exact `C6+K1` two-piece atlas.

Closing this defect-one two-shore cell would simultaneously eliminate
every leaf component of the full-deletion hub graph.  The remaining hub
alternative would then be a cycle of faithful deletion edges, where the
only live issue is operation-state holonomy.
