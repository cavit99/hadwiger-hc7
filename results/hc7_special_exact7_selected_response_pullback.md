# Pulling one selected edge-deletion response through a proper list-critical core

**Status:** written proof; separate internal audit GREEN in
[`hc7_special_exact7_selected_response_pullback_audit.md`](hc7_special_exact7_selected_response_pullback_audit.md).
This theorem
turns a proper two-root list-critical core with an exact order-seven full
neighbourhood into a strict generic five-plus-two response interface when
the five inherited boundary vertices are retained.  It does not preserve
the old boundary partition, the old full-subgraph identities, or the
order-eight provenance of the original special interface, and it does not
prove `HC_7`.

## 1. Setting

Use the complete setting and notation of the audited
[two-root list-critical reduction](hc7_special_exact7_two_edge_list_core.md):

\[
 V(G)=A\mathbin{\dot\cup}Y\mathbin{\dot\cup}B,
 \qquad Y=Y_0\mathbin{\dot\cup}\{z_1,z_2\},
 \qquad |Y_0|=5,
\tag{1.1}
\]

with entrance edges `e_i=z_i a_i`, and let `K subsetneq A` be its connected
induced list-critical core.  Put

\[
                              T=N_G(K).
\tag{1.2}
\]

Choose `i in {1,2}` with `a_i in K`, and let `c_i` be any proper
six-colouring of `G-e_i`.

## 2. Selected-response pullback

### Theorem 2.1

The colouring `c_i` is proper on the closed shore opposite `K` at the
separation with boundary `T`.  Its exact equality partition on `T` is not
attainable by a proper six-colouring of `G[K union T]`.

Suppose in addition that

\[
                             |T|=7,
                   \qquad Y_0\subseteq T.
\tag{2.1}
\]

Then there is a vertex `t in A-K` such that

\[
                    T=Y_0\mathbin{\dot\cup}\{z_i,t\}.
\tag{2.2}
\]

Moreover:

1. `N_A(K)={t}`;
2. `z_j notin T` and `a_j notin K`, where `{i,j}={1,2}`;
3. every component of `G-T` is adjacent to every literal vertex of `T`;
4. up to orientation, the full-subgraph packing vector at `T` is `(1,1)`
   or `(1,2)`;
5. `chi(G[T])<=4`; and
6. the same edge `e_i` and colouring `c_i` give a selected response on the
   smaller connected shore `K`: its partition is legal on the opposite
   closed shore, rejected on the intact `K`-shore, and has demand greater
   than the opposite full-subgraph packing number.

In particular `|K|<|A|`, and (2.2) is a strict generic five-plus-two
exact-seven response interface retaining the five literal vertices `Y_0`.

#### Proof

The only edge on which `c_i` can fail in the original graph is
`e_i=z_i a_i`.  Its endpoint `a_i` lies in `K`, whereas `z_i` lies in
`T=N_G(K)`.  Hence `e_i` belongs to the closed `K`-shore but not to the
opposite closed shore, so the restriction of `c_i` to the latter is proper.
If its exact partition on `T` extended through `G[K union T]`, a permutation
of the six colour names would align the two boundary assignments and glue
them to a six-colouring of `G`, a contradiction.

Because `A` is connected and `K` is a nonempty proper connected induced
subgraph of `A`, some vertex `t in A-K` has a neighbour in `K`; hence
`t in T`.  Also `z_i in T` through the edge `z_i a_i`.  The seven distinct
vertices

\[
                         Y_0\cup\{z_i,t\}
\]

therefore fill `T`, proving (2.2).  It follows at once that `t` is the only
member of `N_A(K)`.  If `a_j` also belonged to `K`, then `z_j in T`, which
would be an eighth vertex; hence `a_j notin K` and `z_j notin T`.

Let `D` be a component of `G-T`.  Its neighbourhood lies in `T`.  If it
missed a literal boundary vertex, at most six vertices would separate it
from the nonempty opposite side, contrary to seven-connectivity.  Thus all
components are `T`-full.  The exact-seven full-subgraph packing theorem and
adaptive `(1,3)` reflection leave, up to orientation, only `(1,1)` and
`(1,2)`.  The exact-seven boundary classification, together with the
cycle-boundary completion of its sole five-chromatic case, gives
`chi(G[T])<=4`.

Finally, the first paragraph already proves that `c_i` is legal on one
closed shore and rejected on the other.  If its boundary partition had
demand at most the opposite packing number, exact full-subgraph reflection
would reproduce it through the intact `K`-shore or construct a `K_7`
minor.  Both outcomes contradict the setting.  This proves item 6 and the
theorem.  \(\square\)

## 3. Retaining the five inherited vertices through a bridge descent

### Corollary 3.1

In the audited bipartite `(1,2)` bridge descent, let `x,y` be the two
exclusive old-boundary contacts and

\[
 \Omega_1=(Y-\{y\})\cup\{v\},\qquad
 \Omega_2=(Y-\{x\})\cup\{u\}.
\tag{3.1}
\]

If `y in {z_1,z_2}`, then `Omega_1` retains every vertex of `Y_0`.  If
`x in {z_1,z_2}`, then `Omega_2` retains every vertex of `Y_0`.  Therefore
both orientations lose an inherited `Y_0`-vertex exactly when

\[
                              x,y\in Y_0.
\tag{3.2}
\]

#### Proof

The two identities in (3.1) are part of the bridge theorem.  Each new
boundary deletes exactly the displayed old vertex, so the assertions are
immediate from `Y=Y_0 dotcup {z_1,z_2}`.  \(\square\)

The operation-specific response after the bridge move is the new
`G-uv` colouring supplied by that theorem.  Corollary 3.1 preserves the
five literal vertices, not the old selected partition.

## 4. Exact scope

Theorem 2.1 proves recursion for a **generic selected-response** exact-seven
interface.  The currently worded special five-plus-two theorem formally
includes provenance from the concentrated order-eight construction, which
the new boundary need not retain.  Of the five vertices in `Y_0`, only
three are original branch-set representatives; the other two are inherited
internal-transversal vertices.  Thus retaining `Y_0` must not be described
as retaining five branch-set labels.

Within the proper-core and bridge pullbacks considered here, the remaining
exact-order-seven noncomposable placement is literal loss of at least one
vertex of `Y_0`.  Before exact order seven, separator excess `|T|-7` is
still open.  Neither issue is resolved here.

## 5. Dependencies

- [special two-root list-critical reduction](hc7_special_exact7_two_edge_list_core.md)
- [exact-seven full-subgraph packing](hc7_exact_seven_packet_packing.md)
- [adaptive exact-seven reflection](hc7_exact7_adaptive_packet_reflection.md)
- [exact-seven boundary classification](hc7_exact7_no_rigid_trace.md)
- [cycle-boundary completion](hc7_cycle_boundary_completion.md)
- [bipartite bridge response descent](hc7_exact7_bipartite_bridge_response_descent.md)
