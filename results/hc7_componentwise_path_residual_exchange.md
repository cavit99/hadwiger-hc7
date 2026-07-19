# Componentwise exchange at a forced boundary path

**Status:** written proof; separate internal audit GREEN in
[`hc7_componentwise_path_residual_exchange_audit.md`](hc7_componentwise_path_residual_exchange_audit.md).
This is an unbounded conditional theorem for an exact order-seven separation.  It strengthens the
connected-residual path-intersection argument by treating every component left
inside a boundary-full connected subgraph separately.  It does not prove that
one of those components has zero separator excess, and it does not prove
`HC_7`.

## 1. Setting

Let `G` be a seven-connected graph which is not six-colourable and every
proper minor of which is six-colourable.  Suppose

\[
 V(G)=A\mathbin{\dot\cup}S\mathbin{\dot\cup}B,
 \qquad E_G(A,B)=\varnothing,
 \qquad |S|=7,                                      \tag{1.1}
\]

where `A` and `B` are nonempty.  Write

\[
 S=D\mathbin{\dot\cup}E\mathbin{\dot\cup}\{r,z\},
 \qquad |D|=3,\quad |E|=2.                         \tag{1.2}
\]

Assume that a proper six-colouring of `G[A union S]` induces one of the
following two exact equality partitions on the literal boundary:

\[
 \Pi_A=D\mid E\mid\{r\}\mid\{z\},
 \qquad rz\notin E(G),                              \tag{1.3}
\]

or

\[
 \Pi_B=D\mid E\mid\{r,z\}.                         \tag{1.4}
\]

Let `P_1,P_2` be vertex-disjoint connected subgraphs of `G[A]`, each
adjacent to every literal vertex of `S`.  Let `P` be an `r`--`z` path whose
internal vertices lie in `A`, such that

\[
 V(P)\cap V(P_2)=\varnothing,
 \qquad T=V(P)\cap V(P_1)\ne\varnothing.             \tag{1.5}
\]

Let `R` be any component of

\[
        G[V(P_1)-T].                                  \tag{1.6}
\]

Since `G[V(P_1)]` is connected, `R` has a neighbour in `T`.  Put

\[
 U_R=N_G(R)-S,
 \qquad
 \Lambda_R=\{s\in S:E_G(s,R)=\varnothing\}.          \tag{1.7}
\]

Thus `U_R` is the complete set of literal neighbours of `R` outside the
old boundary, not a selected attachment set.

For `u in {r,z}` and `C in {D,E}`, define the required contact set

\[
 Q_u(C)=C\cup
 \begin{cases}
 \{u\},&E_G(u,C)=\varnothing,\\
 \varnothing,&E_G(u,C)\ne\varnothing.
 \end{cases}                                         \tag{1.8}
\]

The extra vertex `u` is required precisely when no boundary edge joins it
to `C`.

## 2. Componentwise realization of the boundary blocks

### Lemma 2.1

If the boundary partition is `Pi_A` and `R` has a neighbour at every
vertex of one of

\[
       Q_r(D),\quad Q_z(D),\quad Q_r(E),\quad Q_z(E), \tag{2.1}
\]

then `G` is six-colourable.

If the boundary partition is `Pi_B` and `R` has a neighbour at every
vertex of `D` or at every vertex of `E`, then `G` is six-colourable.

#### Proof

First assume `Pi_A`, and suppose for definiteness that `R` meets every
vertex of `Q_r(D)`.  Keep the singleton block `{r}` literal.  Let

\[
       P_z=G[V(P)-\{r\}].                              \tag{2.2}
\]

The graph `P_z` is connected and contains `z`.  Its open-side part is the
connected subgraph induced by the internal vertices of `P`; that subgraph
is nonempty because `rz` is a nonedge.

Consider the following three disjoint connected sets:

\[
       R\cup D,
       \qquad V(P_2)\cup E,
       \qquad V(P_z).                                  \tag{2.3}
\]

The first is connected because `R` meets every vertex of `D`; the second
is connected by boundary-fullness; and the third is the displayed path.
They are pairwise adjacent.  The second set has an edge to a vertex of
`D` and to `z`, while the first and third sets are adjacent through an edge
from `R` to `T subseteq V(P)-{r,z}`.  Each set is also adjacent to the
literal vertex `r`: for the second this follows from boundary-fullness, for
the third from the first edge of `P`, and for the first either a boundary
edge joins `r` to `D` or `r in Q_r(D)` and the required contact lies in
`R`.

Consequently the three sets in (2.3), together with the literal singleton
`{r}`, are pairwise adjacent connected realizations of the four blocks of
`Pi_A`.  Contract a spanning tree in each displayed set.  The four
contraction representatives form a clique, one representative for each
boundary block.  A six-colouring of this proper minor pulls back on the
untouched closed shore
`G[B union S]` to the exact partition `Pi_A`.  After a permutation of the
six colour names, it glues to the given colouring of `G[A union S]`, a
contradiction.

The cases `Q_r(E)`, `Q_z(D)` and `Q_z(E)` follow by interchanging `D,E`
and/or `r,z`.  Notice that in the `z`-literal cases one uses
`G[V(P)-{z}]` for the other singleton block.  This proves the first
assertion.

Now assume `Pi_B` and, for definiteness, that `R` meets every vertex of
`D`.  The three sets

\[
       R\cup D,
       \qquad V(P_2)\cup E,
       \qquad V(P)                                     \tag{2.4}
\]

are disjoint and connected.  They are pairwise adjacent: the first and
third through an edge from `R` to `T`, the second and third through a
boundary contact at `r` (or at `z`), and the first two through a contact
from the boundary-full subgraph `P_2` to `D`.  Contracting spanning trees
in (2.4) forces the exact partition `D|E|{r,z}` on the untouched closed
shore, which glues to the given colouring.  The case in which `R` meets
all of `E` is symmetric.  \(\square\)

## 3. Literal separator excess for every residual component

### Theorem 3.1

For every component `R` in (1.6), at least one of the following holds.

1. The complete boundary equality partition is attained on both original
   closed shores, and `G` is six-colourable.
2. One has

   \[
          |\Lambda_R|\ge2,
          \qquad |U_R|\ge|\Lambda_R|,                 \tag{3.1}
   \]

   and hence the literal separator excess

   \[
          \varepsilon(R)=|U_R|-|\Lambda_R|
                         =|N_G(R)|-7                  \tag{3.2}
   \]

   is a nonnegative integer.  If `epsilon(R)=0`, then

   \[
          N_G(R)=U_R\mathbin{\dot\cup}(S-\Lambda_R)  \tag{3.3}
   \]

   is the boundary of an actual nontrivial separation of order seven.

In particular, if `|U_R|<=2`, then either the complete partition glues or

\[
             |U_R|=|\Lambda_R|=2                     \tag{3.4}
\]

and (3.3) is an actual order-seven separator.

#### Proof

Suppose first that `Pi_B` is the given partition and outcome 1 does not
hold.  Lemma 2.1 says that `R` misses at least one vertex of `D` and at
least one vertex of `E`.  Hence `|Lambda_R|>=2`.

Suppose instead that `Pi_A` is the given partition.  Again assume outcome
1 does not hold.  Then `R` fails all four contact conditions in (2.1).  If
`|Lambda_R|=0`, it meets every required contact set, a contradiction.  If
`Lambda_R={s}`, inspect the four possible locations of `s`:

* when `s in D`, the subgraph `R` meets every vertex of `Q_r(E)`;
* when `s in E`, it meets every vertex of `Q_r(D)`;
* when `s=r`, it meets every vertex of `Q_z(D)`; and
* when `s=z`, it meets every vertex of `Q_r(D)`.

In each line, the possible additional singleton in the displayed contact
set is not `s`, and is therefore met by `R`.  Lemma 2.1 again gives
outcome 1.
Thus failure of outcome 1 implies `|Lambda_R|>=2` in both partition
forms.

By definition,

\[
       N_G(R)=U_R\mathbin{\dot\cup}(S-\Lambda_R),
       \qquad
       |N_G(R)|=|U_R|+7-|\Lambda_R|.                  \tag{3.5}
\]

The nonempty connected set `R` is disjoint from the nonempty opposite
shore `B`, and no edge joins it to `B`.  Thus `N_G(R)` is the boundary of
a nontrivial separation.  Seven-connectivity gives `|N_G(R)|>=7`.
Equation (3.5) is therefore equivalent to
`|U_R|>=|Lambda_R|`, proving (3.1)--(3.2).  Equality gives (3.3) with
order seven.  Finally, if `|U_R|<=2`, then

\[
             2\le|\Lambda_R|\le|U_R|\le2,
\]

which proves (3.4).  \(\square\)

### Corollary 3.2 (zero excess gives a strict generic restart)

If outcome 1 of Theorem 3.1 fails and `epsilon(R)=0`, choose any edge
`xy` with `x in R` and `y in N_G(R)`.  Every six-colouring of `G-xy`,
together with the order-seven separation having connected shore `R`, is a
generic exact-seven selected-response interface.  Its connected shore is
strictly smaller than the old shore `A`.

#### Proof

The graph `G-xy` is a proper minor and hence has a six-colouring.  Its
endpoints have the same colour, since otherwise restoring `xy` would give a
six-colouring of `G`.  The colouring is proper on the closed shore opposite
`R`.  Its equality partition on `N_G(R)` cannot extend through the intact
closed `R`-shore, because two such colourings would align after a global
permutation of the colour names and six-colour `G`.

The component `R` is contained in `V(P_1)-T`, while `T` is nonempty.
Consequently

\[
                         |R|<|V(P_1)|\le |A|.
\]

Thus the new interface is a strict host-level restart.  \(\square\)

## 4. Path-component descent

### Theorem 4.1 (a nontrivial path component gives strict generic restart)

Assume in addition that `G` has no `K_7` minor.  Let `C` be a component of
one open shore of an actual order-seven separation, suppose a different
component exists in the same open shore, and suppose `G[C]` is a path of
order at least two.  Then some nonempty proper connected set

\[
                         C'\subsetneq C                \tag{4.1}
\]

has

\[
                         |N_G(C')|=7.                  \tag{4.2}
\]

Consequently, for every edge `xy` with `x in C'` and
`y in N_G(C')`, any six-colouring of `G-xy` gives a generic exact-seven
selected-response interface whose connected shore `C'` is strictly smaller
than `C`.

#### Proof

Let the old boundary be `S`, and let `P` be a different component in the
same open shore.  Both `C` and `P` are `S`-full, since each component of
`G-S` has all its neighbours in the seven-set `S` and seven-connectivity
forces it to meet every member of `S`.

First suppose `|C|=2`, say `C` is the edge `uv`.  For either endpoint,

\[
                  N_G(u)=\{v\}\mathbin{\dot\cup}N_S(u).           \tag{4.3}
\]

The singleton `{u}` and the nonempty opposite open shore lie on different
sides of this neighbourhood, so seven-connectivity gives
`|N_S(u)|>=6`; the same holds for `v`.  If one endpoint, say `u`, misses a
boundary vertex, then `|N_S(u)|=6` and `N_G(u)` is the required actual
order-seven boundary, with `C'={u}`.  If neither endpoint misses a boundary
vertex, the two singletons `{u},{v}` and the component `P` are three
pairwise disjoint `S`-full connected subgraphs in one shore.  Any component
of the opposite shore is a fourth `S`-full connected subgraph.  The audited
adaptive `(1,3)` reflection theorem then gives a `K_7` minor or a
six-colouring of `G`, contradicting the present hypotheses.  Hence the
first alternative must occur.

Now suppose `|C|>=3`, and choose an internal vertex `w` of the path.  Let
`C_1,C_2` be the two components of `C-w`.  For `i=1,2`,

\[
                  N_G(C_i)=\{w\}\mathbin{\dot\cup}N_S(C_i).       \tag{4.4}
\]

Seven-connectivity gives `|N_S(C_i)|>=6`.  If either component misses a
member of `S`, equation (4.4) is an actual boundary of order seven and we
take that component for `C'`.  Otherwise both `C_1,C_2` are `S`-full.
Together with `P` they are three disjoint `S`-full connected subgraphs in
one shore.  The same adaptive `(1,3)` theorem, using any component of the
opposite shore as its fourth full connected subgraph, again gives the
forbidden `K_7` minor or six-colouring.  Thus one of `C_1,C_2` satisfies
(4.1)--(4.2).

Finally choose a crossing edge `xy`.  A six-colouring of the proper minor
`G-xy` makes `x,y` equal, since otherwise it would six-colour `G` after the
edge is restored.  Its restriction is proper on the opposite original
closed shore and cannot extend through the intact `C'`-side, or the two
colourings would glue.  This is precisely a generic exact-seven
selected-response interface.  The containment in (4.1) makes the connected
shore strictly smaller.  \(\square\)

### Consequence for a minimum selected-response interface

Consider an order-seven separation one of whose open sides has at least two
components.  Each component is itself the connected shore of a generic
exact-seven interface, because seven-connectivity makes it adjacent to all
seven boundary vertices.  If generic interfaces are chosen with minimum
connected-shore order over all orientations in the fixed host, no component
of that side can induce a path of order at least two: Theorem 4.1 would give
a strictly smaller interface.  Thus the only path component which survives
this normalization is a singleton, the separate degree-seven
singleton-shore terminal mode.

## 5. Exact contribution and trust boundary

The earlier connected-residual theorem assumed that all of
`V(P_1)-V(P)` formed one connected subgraph.  Theorem 3.1 applies to every
component separately and uses the exact contact requirement relative to
either literal singleton.  It therefore closes, without any bound on the
order of the shores, every residual component which meets one required
contact set.  Every residual component with zero separator excess gives a
strict generic exact-seven restart; in particular this holds whenever it
has at most two literal outside attachments.  Theorem 4.1 independently
eliminates every nontrivial induced-path component on a multicomponent side
of a minimum interface.

The theorem does not show that one residual component has at most two
outside attachments or zero separator excess.  It also does not preserve
the old equality partition through the new order-seven separator.  A
proof-closing continuation must use an operation-specific colouring at an
edge of `U_R` to lower positive excess, preserve the selected partition, or
construct an explicit `K_7`-minor model.

## 6. Dependencies

- [exact response reflection](../results/hc7_exact7_selected_response_preservation.md)
- [adaptive reflection for three boundary-full connected subgraphs on one
  shore](../results/hc7_exact7_adaptive_packet_reflection.md)
- [generic exact-seven selected-response interfaces](../results/hc7_generic_exact7_response_restart.md)
- [two full connected subgraphs force a first-hit path](../results/hc7_exact7_two_full_subgraph_kempe_compression.md)
- [connected path-intersection separator excess](../results/hc7_small_path_intersection_lobe.md)
