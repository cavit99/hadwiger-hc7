# A two-edge list-critical descent at a direct bichromatic entry

**Status:** written proof; separate internal audit GREEN in
[`hc7_direct_entry_two_edge_list_core_audit.md`](hc7_direct_entry_two_edge_list_core_audit.md).
This is a parameter-uniform
host-level reduction for two disjoint edges crossing the same side of a
separation.  In the exact-seven application the two edges are the first and
last edges of the forced bichromatic path.  The theorem gives a strict
connected-side descent, a double-equality trace whose two failed edges lie
on opposite closed sides (or on the boundary), or a shore-filling two-root
list-critical graph.  It does not construct a
`K_7`-minor model and does not prove `HC_7`.

## 1. Setting

Let `q>=2`, and let `G` be a graph which is not `q`-colourable but every
proper minor of which is `q`-colourable.  Suppose

\[
 V(G)=L\mathbin{\dot\cup}S\mathbin{\dot\cup}R,
 \qquad E_G(L,R)=\varnothing,
 \qquad L,R\ne\varnothing.                              \tag{1.1}
\]

Let

\[
 e=xp,\qquad f=yq_0                                     \tag{1.2}
\]

be vertex-disjoint edges, where `x,y in S` and `p,q_0 in R`.  Put
`H=G-{e,f}`.

Contract `e` and `f`.  A proper `q`-colouring of the resulting proper minor
expands to a proper colouring `psi` of `H` satisfying

\[
 \psi(x)=\psi(p),\qquad \psi(y)=\psi(q_0).              \tag{1.3}
\]

Every edge of `G` other than the two displayed edges is represented after
the contractions.  Thus the expansion is proper even when there are other
edges between the two endpoint pairs.

For `v in R`, define the list

\[
 A(v)=[q]\setminus
      \{\psi(s):s\in N_G(v)\cap S\}.                    \tag{1.4}
\]

The lists use the original graph, so the common colour of `x,p` is excluded
from `A(p)` and the common colour of `y,q_0` is excluded from `A(q_0)`.

## 2. The list-critical core

### Theorem 2.1 (two-edge list-critical descent)

There is a connected induced subgraph `K` of `G[R]` with the following
properties.

1. `K` is not `A`-colourable, every proper induced subgraph of `K` is
   `A`-colourable, and

   \[
                         V(K)\cap\{p,q_0\}\ne\varnothing. \tag{2.1}
   \]

2. The restriction of `psi` to `K` colours every vertex from its list
   except possibly `p,q_0`.  More precisely it is a colouring from

   \[
    A^+(v)=
    \begin{cases}
      A(v)\cup\{\psi(v)\},&v\in\{p,q_0\},\\
      A(v),&v\notin\{p,q_0\}.
    \end{cases}                                         \tag{2.2}
   \]

3. Every vertex satisfies

   \[
                              d_K(v)\ge |A(v)|.          \tag{2.3}
   \]

4. Put

   \[
      T=N_G(V(K)),\qquad C=G[V(K)\cup T],\qquad O=G-V(K). \tag{2.4}
   \]

   Then `(C,O)` is an actual separation.  If `G` is `k`-connected, then
   `|T|>=k`.  If `K` is a proper subgraph of `G[R]`, then

   \[
                              |V(K)|<|R|.                \tag{2.5}
   \]

5. The colouring `psi` gives one of the following three exact placements.

   - **Both marked vertices in the core.**  If `p,q_0 in V(K)`, then
     `psi|O` is proper, `psi|C` fails only on `e,f`, and the common proper
     boundary trace `psi|T` does not extend to a proper `q`-colouring of
     `C`.
   - **One marked vertex in the core, clean placement.**  Suppose, after
     interchanging the names, that `p in V(K)` and `q_0 notin V(K)`.  If
     `\{y,q_0\}` is not contained in `T`, then `psi|C` fails only on `e`,
     `psi|O` fails only on `f`, and `psi|T` is a proper common boundary
     trace.  The two failed edges therefore occur on opposite sides of the
     returned separation.  This includes the case in which exactly one end
     of `f` belongs to `T`.
   - **One marked vertex in the core, boundary-edge placement.**  In the
     same orientation, if `y,q_0 in T`, then `f=yq_0` is an edge of the
     literal boundary graph `G[T]`.  This is the only placement in which
     the common restriction of `psi` fails to be a proper colouring of
     `G[T]`.

   In every placement, the two restrictions of `psi` agree literally as
   assignments on `T`; in the boundary-edge placement this common assignment
   is improper precisely on `f`.  With precisely the displayed deleted edges
   omitted, they cannot
   both be repaired, while retaining that trace, to proper colourings of
   the two original closed sides: two such repairs would glue to a
   `q`-colouring of `G`.

#### Proof

First observe that `G[R]` is not `A`-colourable.  If `lambda` were such a
colouring, combine it with `psi|G[L\cup S]`.  There are no `L-R` edges, and
the definition of `A(v)` prevents every conflict on an `R-S` edge.  In
particular, `lambda(p)` avoids `psi(x)` and `lambda(q_0)` avoids `psi(y)`,
so the two deleted edges can also be restored.  This would give a proper
`q`-colouring of `G`, a contradiction.

Choose an induced non-`A`-colourable subgraph `K` of `G[R]` minimal by
vertex inclusion.  It is connected, since otherwise one of its components
would be a smaller non-`A`-colourable induced subgraph.  Every proper
induced subgraph is `A`-colourable by the choice of `K`.

The colouring `psi` is proper on `H`.  If `v in R-{p,q_0}`, every original
edge from `v` to `S` remains in `H`, so `psi(v) in A(v)`.  At `p` and
`q_0`, the only possibly conflicting boundary edges are respectively
`e,f`; hence (2.2) holds.  If `K` contained neither marked vertex,
`psi|K` would be an `A`-colouring, a contradiction.  This proves items 1
and 2.

For (2.3), colour `K-v` from its lists.  If `d_K(v)<|A(v)|`, one colour in
`A(v)` is absent from all coloured neighbours of `v`, so the colouring
extends to `v`.  That would colour `K` from `A`, a contradiction.

The set `K` is a nonempty connected subset of `R`.  Its full neighbourhood
`T` separates it from the nonempty set `L`, because there is no `L-R`
edge.  This proves that (2.4) is an actual separation.  Connectivity gives
the asserted lower bound on `|T|`, and a proper inclusion `V(K) subsetneq R`
gives (2.5).

It remains to check the edge placements.  If both `p,q_0` lie in `K`, each
of `e,f` has one end in `K` and the other in `T`.  Hence neither belongs to
`O`, while both are the only failed edges of `psi|C`.  No deleted edge lies
inside `T`, so the trace is proper.  If it extended through the original
graph `C`, that extension would glue to the proper colouring `psi|O` and
colour `G`.  Thus no such extension exists.

Suppose instead that `p in K` and `q_0 notin K`.  The edge `e` crosses from
`K` to `T`, so it occurs only on the `C` side and is the only failed edge
there unless `f` is a boundary edge.  The edge `f` has both ends outside
`K`, so it occurs in `O`.  It occurs in `C` exactly when both `y,q_0`
belong to `T`; in that event it is a literal boundary edge.  Otherwise it
lies only in `O` and the placement is clean.  These are all possibilities.
The case `q_0 in K,p notin K` is symmetric.

Finally, in each case the restrictions are restrictions of the same
colouring `psi`, so they agree literally on the common vertex set.  If both
failed-edge sets could be repaired on their respective closed sides while
retaining those boundary colours, the repaired colourings would glue,
contrary to the non-`q`-colourability of `G`.  This proves item 5 and the
theorem.  \(\square\)

## 3. The shore-filling equality case

Assume `K=G[R]`.  Then both `p,q_0` belong to `K`, so only the first
placement in Theorem 2.1(5) occurs.  For `v in R`, put

\[
\begin{aligned}
 c_S(v)&=|\{\psi(s):s\in N_G(v)\cap S\}|,\\
 \rho(v)&=|N_G(v)\cap S|-c_S(v),\\
 \varepsilon(v)&=d_{G[R]}(v)-|A(v)|.
\end{aligned}                                           \tag{3.1}
\]

### Corollary 3.1 (degree identity and low-degree separator)

For every `v in R`,

\[
                         d_G(v)=q+\varepsilon(v)+\rho(v). \tag{3.2}
\]

In particular, in the `HC_7` application (`q=6` and `G` seven-connected),
every vertex with `epsilon(v)+rho(v)<=2` has degree seven or eight, and
`N_G(v)` is the boundary of an actual order-seven or order-eight separation
with singleton open side `{v}`.  If no such vertex exists, every vertex of
the shore-filling core has degree at least nine.

#### Proof

Minimality and (2.3) give `epsilon(v)>=0`.  From (1.4),
`|A(v)|=q-c_S(v)`.  Since `R` is the entire open shore, all neighbours of
`v` lie in `R\cup S`, and therefore

\[
\begin{aligned}
 d_G(v)
   &=d_{G[R]}(v)+|N_G(v)\cap S|\\
   &=q-c_S(v)+\varepsilon(v)+c_S(v)+\rho(v),
\end{aligned}
\]

which is (3.2).  For `q=6`, the displayed inequality gives `d_G(v)<=8`,
whereas seven-connectivity gives `d_G(v)>=7`.  The nonempty opposite shore
`L` is anticomplete to `v`, so `N_G(v)` separates `{v}` from `L`.  This is
the claimed singleton-side separation.  \(\square\)

### Corollary 3.2 (the tight shore is a Gallai tree)

If `epsilon(v)=0` for every `v in R`, then every block of `G[R]` is a
complete graph or an odd cycle.

#### Proof

In this case `|A(v)|=d_{G[R]}(v)` for every vertex.  The connected graph
`G[R]` is not colourable from these lists.  The degree-choosability theorem
therefore says that each of its blocks is a complete graph or an odd cycle.
\(\square\)

### Corollary 3.3 (many boundary colours force a small separator)

Assume `q=6` and `|S|=7`, and let `b` be the number of colours used by
`psi` on `S`.  Then every `v in R` satisfies

\[
             \rho(v)\le 7-b,
 \qquad      d_G(v)\le 13-b+\varepsilon(v).             \tag{3.3}
\]

Consequently, if `b=6` and `epsilon(v)<=1`, or if `b=5` and
`epsilon(v)=0`, then `N_G(v)` is an actual singleton-side separation of
order seven or eight.  In particular, if the shore is tight at every
vertex and `psi|S` uses at least five colours, every vertex of the shore
has degree at most eight.

#### Proof

Write the colour classes of `psi|S` as `B_1,...,B_b`.  For the set of
boundary neighbours of `v`, the number of repeated colours is at most

\[
              \sum_{i=1}^b (|B_i|-1)=7-b.
\]

The degree bound follows from (3.2).  The displayed special cases give
`d_G(v)<=8`, so Corollary 3.1 supplies the asserted separation.  \(\square\)

## 4. Direct-entry consequence and trust boundary

In the exact-seven residual, let `P` be the forced `x-y` bichromatic path,
and suppose its first internal vertex `p` and last internal vertex `q_0`
lie in the selected boundary-full connected subgraphs.  Since `xy` is a
nonedge and `x,y` are distinct singleton colour blocks, they have different
colours.  A proper two-colour `x-y` path therefore has odd length, and the
boundary nonedge forces that length to be at least three.  Its first and
last internal vertices are consequently distinct; hence `xp,yq_0` are
disjoint crossing edges and Theorem 2.1 applies.

There is also a genuine change of boundary partition.  Let `Pi` be the
exact equality partition induced on `S` by the original proper colouring of
the closed `R`-shore, and let `Omega` be the equality partition induced by
`psi|S`.  Then

\[
                              \Omega\ne\Pi.              \tag{4.1}
\]

Indeed, `psi` is proper on the closed `L`-shore.  If the two equality
partitions were the same, a permutation of the six colour names would align
the original `R`-shore colouring with `psi` on every literal vertex of `S`;
the two colourings would then glue to a six-colouring of `G`.

Thus the direct-entry geometry has a well-founded host-level alternative:

1. a strictly smaller connected open side carrying one common
   double-equality assignment, with the two failed edges either both crossing into the
   smaller side, lying on opposite sides, or producing the literal
   boundary-edge placement above; or
2. a shore-filling two-root list-critical graph, with an order-seven or
   order-eight singleton-side separation at every vertex satisfying the
   low-excess inequality in Corollary 3.1.

This spends the proper-minor colouring response missing from the known
six-connected geometric barrier.  It does not yet preserve the two
boundary-full connected subgraphs on the smaller side, force the returned
separator to have order seven, or align the list colours with the three
specific demand sets of the old boundary partition.  The remaining theorem
must couple the two-root list-critical core to those named demand sets, or
show that every shore-filling high-degree core contains a `K_7` minor.
