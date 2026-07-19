# Independent audit of the two-edge list-critical direct-entry descent

**Verdict:** GREEN for Theorem 2.1, Corollaries 3.1--3.3, and the
direct-entry specialization at the exact source revision identified below.

**Audited source:** `hc7_direct_entry_two_edge_list_core.md`, SHA-256

```text
2a1f41bd8214e1e6abc34882e71a22fae302c421e9c13d4cd9fb06354405b74f
```

The audited mathematics is unchanged from the independently checked
revision; the pinned hash was refreshed after the source status line was
updated to record this GREEN audit.

This is a separate internal mathematical audit, not external peer review.
It checks the simultaneous contractions and their expansion, the boundary
lists, the minimal list-critical subgraph, all placements of the two deleted
edges at the returned separation, the degree identity, boundary-colour
bound, and Gallai-tree equality case in the shore-filling branch, and the
exact scope of the direct-entry consequence.

## 1. Simultaneous contraction and expansion

The two edges

\[
                       e=xp,\qquad f=yq_0
\]

are vertex-disjoint.  Contracting them therefore gives a proper minor with
two distinct contracted vertices.  Any additional edge with one end in
`{x,p}` and the other in `{y,q_0}` becomes an edge between those two
contracted vertices (parallel copies may be suppressed), so a proper
colouring assigns the two contracted vertices different colours.  The only
edges which become loops are the contracted edges themselves.

Consequently, expanding a proper `q`-colouring of the double contraction
over the four original vertices gives a proper colouring `psi` of
`H=G-{e,f}` with

\[
                  \psi(x)=\psi(p),\qquad
                  \psi(y)=\psi(q_0).
\]

This remains valid when cross-edges such as `xq_0` or `yp` are present:
their images force the required inequality between the two contracted
colours.  Thus the expansion does not silently assume that the two endpoint
pairs are anticomplete.

## 2. The boundary lists and noncolourability of the open shore

For `v in R`, the list

\[
 A(v)=[q]\setminus\{\psi(s):s\in N_G(v)\cap S\}
\]

uses every original `v-S` edge, including the two deleted edges.  In
particular, `x in N_G(p) cap S` and `y in N_G(q_0) cap S`, so the common
colours of the contracted pairs are absent from `A(p)` and `A(q_0)`.

The restriction `psi|G[L union S]` is proper because neither deleted edge
belongs to that induced graph.  If `G[R]` had an `A`-colouring, combining it
with this restriction would be proper

- inside each of `L`, `S`, and `R`;
- across `L-S`, by the properness of `psi`;
- across `R-S`, by the definition of the lists; and
- on `e,f`, because the colours `psi(x),psi(y)` are excluded at `p,q_0`.

There are no `L-R` edges.  The combined assignment would therefore
`q`-colour `G`, a contradiction.  Hence `G[R]` is not `A`-colourable.

## 3. The minimal induced list-critical subgraph

Choose a vertex-minimal induced non-`A`-colourable subgraph `K` of `G[R]`.
It is connected: otherwise each component would be a proper induced
subgraph and the component list-colourings could be combined.

Every vertex of `R-{p,q_0}` receives under `psi` a colour in its list,
because every incident boundary edge remains in `H`.  At each marked vertex
the only possibly conflicting boundary edge is its displayed deleted edge.
Thus `psi|K` is an `A^+`-colouring with precisely the two stated possible
list enlargements.  If neither marked vertex belonged to `K`, this would be
an `A`-colouring of `K`; therefore `K` contains at least one of them.

For every `v in K`, minimality gives an `A`-colouring of `K-v`.  If
`d_K(v)<|A(v)|`, one list colour is absent from the coloured neighbours and
extends the colouring to `v`.  This proves

\[
                              d_K(v)\ge |A(v)|.
\]

The argument includes the possible empty-list and singleton-core cases:
the implication is invoked only under the strict inequality.

## 4. The returned full-neighbourhood separation

Let `T=N_G(V(K))`.  The connected nonempty set `K` is anticomplete to
`G-(K union T)`.  The nonempty set `L` lies there because `K subseteq R`
and there are no `L-R` edges.  Hence

\[
 C=G[K\cup T],\qquad O=G-K
\]

are the two closed sides of an actual separation with intersection `T`.
In a `k`-connected graph, `|T|>=k`.  If `K` is a proper induced subgraph of
`G[R]`, then `|V(K)|<|R|` is a genuine decrease in the number of vertices
on this connected open side.  It is not, by itself, a recursive decrease
preserving the old boundary labels or the two selected boundary-full
subgraphs.

## 5. Exhaustion of the deleted-edge placements

### 5.1 Both marked vertices in `K`

If `p,q_0 in K`, then `x,y in T`.  Each of `e,f` has one end in `K` and
one in `T`, so both occur in `C` and neither occurs in `O`.  Therefore
`psi|O` is proper and `psi|C` fails precisely on `e,f`.  Neither deleted
edge lies inside `T`, so `psi|T` is proper.

If this boundary assignment extended to a proper colouring of the original
closed side `C`, it would glue to `psi|O`, contradicting the hypothesis on
`G`.  The asserted nonextension is therefore valid.

### 5.2 Exactly one marked vertex in `K`

Suppose `p in K` and `q_0 notin K`; the other orientation is symmetric.
The edge `e` crosses from `K` to `T`, so it occurs only in `C`.  Both ends
of `f` lie outside `K`, so `f` occurs in `O`.  It occurs in `C` exactly
when both `y,q_0` belong to `T`.

Thus the alternatives are exhaustive:

- if `{y,q_0}` is not contained in `T`, then `psi|C` fails only on `e`,
  `psi|O` fails only on `f`, and their common boundary assignment is
  proper; and
- if `y,q_0 in T`, then `f` is a literal boundary edge and the common
  assignment is improper precisely on `f`.

The source now correctly calls the first alternative an opposite-side
failure interface.  The simultaneous-contraction colouring `psi` is a
double-equality colouring of `G-{e,f}`; it does **not** by itself produce
two one-edge response colourings with the same trace.

In every placement the restrictions are assignments inherited from the
same `psi`, so they agree vertex by vertex on `T`.  If the failed edges on
the two original closed sides could both be repaired while retaining that
assignment, the resulting colourings would glue.  This proves exactly the
stated incompatibility and no stronger trace-intersection assertion.

## 6. Shore-filling equality and the degree formula

Assume `K=G[R]`.  Then both marked vertices belong to `K`, so only the
first placement above is possible.  By definition,

\[
 |A(v)|=q-c_S(v),\qquad
 d_{G[R]}(v)=|A(v)|+\varepsilon(v),\qquad
 |N_G(v)\cap S|=c_S(v)+\rho(v).
\]

There are no `L-R` edges, and `R` is the whole open shore.  Adding the two
degree contributions gives the exact identity

\[
                         d_G(v)=q+\varepsilon(v)+\rho(v).
\]

Minimal list-criticality gives `epsilon(v)>=0`, and `rho(v)>=0` by its
definition as the number of repeated boundary-neighbour colours.

For `q=6`, if `epsilon(v)+rho(v)<=2`, then `d_G(v)<=8`; seven-connectivity
gives `d_G(v)>=7`.  The set `N_G(v)` separates the singleton `{v}` from
the nonempty set `L`, because `v in R` and `E_G(L,R)=emptyset`.  Hence it
is an actual singleton-side separation of order seven or eight.  If no
such vertex exists, integrality gives `epsilon(v)+rho(v)>=3` for every
`v in R`, and therefore every such vertex has degree at least nine.

If `epsilon(v)=0` for every `v`, then the fixed list assignment has
`|A(v)|=d_{G[R]}(v)` at every vertex.  The shore-filling core is connected
and is not `A`-colourable.  The classical degree-choosability theorem
therefore applies in exactly the required direction: a connected graph
admitting an uncolourable degree-sized list assignment is a Gallai tree.
Hence every block of `G[R]` is a complete graph or an odd cycle, as stated
in Corollary 3.2.  This step uses that established external theorem; it does
not purport to reprove it.

For Corollary 3.3, let the nonempty colour classes on the seven-vertex
boundary have orders `m_1,...,m_b`.  If `n_i` vertices of the `i`-th class
are adjacent to a fixed `v in R`, that class contributes
`max(n_i-1,0)` to `rho(v)`.  Thus

\[
 \rho(v)=\sum_i\max(n_i-1,0)
          \le \sum_i(m_i-1)=7-b.
\]

Substitution in the exact degree identity with `q=6` gives
`d_G(v)<=13-b+epsilon(v)`.  Hence `b=6, epsilon(v)<=1` and
`b=5, epsilon(v)=0` each imply `d_G(v)<=8`; Corollary 3.1 then gives the
claimed order-seven or order-eight singleton-side separation.  If every
vertex is tight (`epsilon=0`) and `b>=5`, the same bound applies at every
vertex.  No unstated assumption that every boundary colour appears in
`N_S(v)` is used: the inequality above remains valid when some `n_i=0`.

## 7. Direct-entry specialization and trust boundary

In the exact-seven application, `x,y` are nonadjacent boundary vertices
with distinct colours in a proper bichromatic path.  Such a path has odd
length; since it is not the edge `xy`, its length is at least three.  Its
first and last internal vertices `p,q_0` are therefore distinct, and the
four ends of `xp,yq_0` are distinct.  Theorem 2.1 applies.

Let `Pi` be the equality partition on `S` induced by the original proper
colouring of the closed `R`-shore, and let `Omega` be the partition induced
by `psi|S`.  The restriction of `psi` to the closed `L`-shore is proper,
because the two deleted edges join `S` to `R`.  If `Omega=Pi`, matching
boundary blocks define a bijection between the colours used on `S`; this
bijection extends to a permutation of all six colour names.  After applying
that permutation to the original `R`-shore colouring, the two shore
colourings agree at every boundary vertex and glue, a contradiction.
Therefore `Omega!=Pi` is valid.  It is only a change of equality partition;
no monotone order on partitions is asserted.

The theorem proves the following unbounded reduction:

1. a proper list-critical core gives a strictly smaller connected open
   side and an exact placement of the double-equality failure; or
2. the list-critical core fills the old shore and satisfies the degree
   identity, producing order-seven or order-eight singleton-side
   separations at low excess.

It does **not** prove any of the following.

- The smaller full-neighbourhood separation retains the old seven boundary
  labels, the two selected boundary-full connected subgraphs, or the old
  equality partition.
- The proper common assignment in the clean placement extends through
  either original closed side after the failed edge is restored.
- The shore-filling core contains a `K_7` minor when all its vertices have
  degree at least nine.
- The Gallai-tree equality case by itself supplies a minor model, bounded
  separator, or recursive colour-compatible interface.
- An order-eight singleton-side separation reduces to a colour-compatible
  order-seven separation.
- Repeating the construction is a state-preserving induction.

Accordingly, the source's final trust boundary is accurate.  The result is
a genuine host-level list-critical descent, not a closure of the direct-entry
configuration or of `HC_7`.
