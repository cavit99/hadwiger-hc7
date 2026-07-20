# Positive boundary excess reduces to one partitioned opposite shore

**Status:** written proof; separate internal audit GREEN in
[`hc7_order8_positive_excess_frozen_outer_shore_audit.md`](hc7_order8_positive_excess_frozen_outer_shore_audit.md).
This is an unbounded conditional reduction inside the ordered order-eight
interface.  It does not prove `HC_7`.

## 1. Setting and terminology

Let `G` be a seven-connected graph satisfying

\[
 \chi(G)=7,\qquad K_7\not\preccurlyeq G,
 \qquad \chi(M)\le 6\text{ for every proper minor }M\text{ of }G.
 \tag{1.1}
\]

Suppose

\[
 V(G)=L\mathbin{\dot\cup}S\mathbin{\dot\cup}R,
 \qquad E_G(L,R)=\varnothing,
 \tag{1.2}
\]

where `G[L]` and `G[R]` are connected and

\[
 S=\{d,e,x_d,y_d,x_e,y_e,x_0,y_0\}.
 \tag{1.3}
\]

Assume that `G[S]` contains the two vertex-disjoint triangles

\[
                 d x_d y_d d,
             \qquad e x_e y_e e.                    \tag{1.4}
\]

Suppose `G[R]` contains vertex-disjoint connected subgraphs `P_0,P_1`
which are adjacent to each other and are each adjacent to every literal
vertex of `S`.

Retain the induced connected partition supplied by the ordered two--three
allocation theorem:

\[
                         L=E\mathbin{\dot\cup}D,       \tag{1.5}
\]

where `G[E]` and `G[D]` are connected and adjacent, and

\[
 N_G(E)\cap S=S-\{e\},
 \qquad
 N_G(D)\cap S=S-\{d\}.                               \tag{1.6}
\]

Put

\[
 W=N_G(E)\cap D,
 \qquad
 B=N_G(E)=(S-\{e\})\mathbin{\dot\cup}W,              \tag{1.7}
\]

and assume the positive-excess case

\[
                              |W|\ge2.                 \tag{1.8}
\]

Let `c` be the fixed proper six-colouring of `G[L\cup S]` from the
merged-root response, and let `Pi` be its equality partition on `B`.

We use the following response terminology only in this note.  A
**full-neighbourhood response side** is a nonempty connected set `A` such
that `T=N_G(A)` separates `A` from a nonempty set, together with an edge
`xy`, `x\in A`, `y\in T`, and a proper six-colouring `psi` of `G-xy`.
The partition induced by `psi` on `T` extends through `G-A` and through
`G[A\cup T]-xy`, but it is rejected by the intact graph `G[A\cup T]`.
A response side with smaller `|T|` is a **strict boundary-order response
descent**.  When `|T|=7`, it is a generic exact-seven response interface in
the established sense.

For a partition `Sigma` of a boundary into independent blocks, choose a
maximum clique `U` among its singleton blocks and list the other blocks as
`C_1,...,C_t`.  Its full-subgraph demand is

\[
                             t=|\Sigma|-|U|.           \tag{1.9}
\]

The **required boundary set** of `C_i` relative to `U` is

\[
 R_U(C_i)=C_i\cup\{u\in U:E_G(u,C_i)=\varnothing\}.   \tag{1.10}
\]

## 2. The positive-excess normal form

### Theorem 2.1

Under the hypotheses of Section 1, at least one of the following holds.

1. `G` contains an explicit `K_7`-minor model.
2. There is a strict boundary-order response descent from `B`.
3. The graph `G-B` has exactly two components, `E` and a connected set
   `C`.  The set `C` is adjacent to every literal vertex of `B`, contains
   `P_0\cup P_1`, and has a partition

   \[
                          C=Q_0\mathbin{\dot\cup}Q_1  \tag{2.1}
   \]

   such that `G[Q_0]` and `G[Q_1]` are connected and adjacent, and each
   `Q_i` is adjacent to every literal vertex of `S`.

In outcome 3 the following colouring constraints also hold.

4. The fixed partition `Pi` extends through `G[E\cup B]` and is rejected
   by `G[C\cup B]`.  Its full-subgraph demand is at least two.
5. Let `uv` be any edge with `u\in E`, `v\in B`, let `psi` be any proper
   six-colouring of `G-uv`, and let `Sigma` be its equality partition on
   `B`.  Then `Sigma` extends through `G[C\cup B]` and is rejected by the
   intact graph `G[E\cup B]`.  For every maximum singleton clique `U` of
   `Sigma`, form the incidence graph with left side `\{Q_0,Q_1\}` and
   right side the remaining blocks `C_1,...,C_t`, where

   \[
       Q_jC_i\text{ is an incidence edge}
       \quad\Longleftrightarrow\quad
       Q_j\text{ has a neighbour at every vertex of }R_U(C_i). \tag{2.2}
   \]

   This incidence graph has no matching saturating
   `\{C_1,...,C_t\}`.  Whenever an incidence edge is absent, its failure
   is witnessed by a literal vertex of `W`.

Consequently, if both `Q_0,Q_1` are adjacent to every vertex of `B`, every
partition `Sigma` in item 5 has full-subgraph demand at least three.  More
generally, when that demand is at most two, Hall failure has one of the
following exact forms:

- one required boundary set is met by neither `Q_0` nor `Q_1`; or
- there are two required boundary sets and at most one of `Q_0,Q_1` meets either of
  them.

In the first form there are distinct `w_0,w_1\in W` such that `Q_0` misses
`w_0`, `Q_1` misses `w_1`, and the opposite connected subgraph meets the
corresponding vertex.

### Proof

The set `E` is a component of `G-B`, by (1.7).  Let `K` be any other
component of `G-B`.  Then `N_G(K)\subseteq B`.  If `K` is not adjacent to
every vertex of `B`, put `T=N_G(K)`.  Seven-connectivity and proper
containment give

\[
                         7\le |T|<|B|.                \tag{2.3}
\]

Choose an edge `xy` with `x\in K`, `y\in T`, and a proper six-colouring
`psi` of `G-xy`.  Such a colouring exists by (1.1), and its ends receive
one common colour; otherwise the edge could be restored and would
six-colour `G`.  The restriction of `psi` to `G-K` is proper.  Its equality
partition on `T` cannot extend through the intact graph `G[K\cup T]`,
because that extension and `psi|G-K` could be aligned on their literal
blocks and glued.  Thus `K,T;xy,psi` is a full-neighbourhood response side,
and (2.3) is outcome 2.

Assume from now on that every component of `G-B` other than `E` is
adjacent to every literal vertex of `B`.  Since an edge joins `P_0` to
`P_1`, they lie in one component, say `C_0`, of `G-B`.

Suppose a second component `C_1` other than `E,C_0` exists.  Put

\[
 Q=\{d,x_d,y_d\},
 \qquad
 A=\{x_e,y_e,x_0,y_0\}.                              \tag{2.4}
\]

The set `Q` is a triangle by (1.4).  The four connected subgraphs

\[
                           E,\quad C_1,\quad P_0,\quad P_1              \tag{2.5}
\]

are pairwise vertex-disjoint, and each is adjacent to every vertex of
`A\cup Q`: this follows from boundary-fullness for `E,C_1` and from the
definition of `P_0,P_1` for the last two subgraphs.  Assign the four
vertices of `A` bijectively to the four subgraphs in (2.5), and adjoin each
assigned vertex to its subgraph.  The four resulting sets are connected.
Any two are adjacent because either underlying subgraph has a neighbour at
the anchor of the other.  Each is adjacent to each singleton vertex of
`Q`, and the three vertices of `Q` are pairwise adjacent.  These four sets
together with the three singleton sets from `Q` are an explicit
`K_7`-minor model.  Therefore, outside outcome 1, `C_0` is the unique
component other than `E`; call it `C`.

Among all pairs of vertex-disjoint connected subgraphs of `G[C]` with
`P_i\subseteq Q_i` for `i=0,1`, choose `Q_0,Q_1` maximizing
`|Q_0\cup Q_1|`.  The family is nonempty because it contains `P_0,P_1`;
each selected subgraph retains all contacts of its corresponding `P_i`
with `S`.
If a component `Z` of

\[
                         G[C-(Q_0\cup Q_1)]           \tag{2.6}
\]

existed, connectedness of `G[C]` would give an edge from `Z` to one of the
two selected subgraphs.  Absorbing all of `Z` into that subgraph would
preserve disjointness, connectedness and all contacts with `S`, while
strictly increasing the covered vertex set.  Hence the selected pair
covers `C`.  Taking the induced graphs on their vertex sets preserves
connectedness.  Since `G[C]` is connected, an edge joins the two parts.
This proves (2.1) and outcome 3.

The colouring `c` restricts to a proper colouring of `G[E\cup B]` and
induces `Pi`.  If `Pi` extended through `G[C\cup B]`, the two colourings
would align by a global permutation of the six colour names and glue,
contrary to (1.1).  Thus `C` rejects `Pi`.

Apply the transported-partition Hall reflection theorem with coloured
shore `E`, opposite shore `C`, and the one boundary-full connected support
`E`.  The demand is nonzero: `|B|\ge9`, whereas a six-colouring has at
most six blocks, so at least one block is nonsingleton and is not contained
in the singleton clique `U`.  If the full-subgraph demand of `Pi` were at
most one, that theorem
would manufacture a colouring of `G[C\cup B]` inducing `Pi`, and the
preceding gluing contradiction would apply.  Therefore its demand is at
least two.  This proves item 4.

Now fix `uv,psi,Sigma` as in item 5.  The restriction of `psi` to
`G[C\cup B]` is proper because the deleted edge has its endpoint outside
`C\cup B`.  If `Sigma` extended through the intact graph `G[E\cup B]`, it
would glue to that restriction and six-colour `G`.  Thus the response has
the asserted orientation.

Apply the transported-partition Hall reflection theorem in the other
direction: its coloured shore is now `C`, its opposite shore is `E`, and
the two displayed connected supports are `Q_0,Q_1`.  They are disjoint and
adjacent, as required by that theorem.  Again the demand is nonzero because
`|B|\ge9` and there are at most six colour blocks.  A matching saturating all remaining
blocks would manufacture an intact colouring of `G[E\cup B]` inducing
`Sigma`, contradicting the preceding paragraph.  Hence no such matching
exists.

Both `Q_0,Q_1` are adjacent to every vertex of `S-\{e\}`.  Therefore every
vertex of a required boundary set in (2.2) which they can fail to meet belongs to

\[
                      B-(S-\{e\})=W.                 \tag{2.7}
\]

This proves the literal-witness assertion.  If both subgraphs are
`B`-full, they are two universal supports, so every partition of demand at
most two would have a saturating matching.  Its demand is consequently at
least three.

Finally suppose the demand is at most two.  Hall's theorem gives either a
single block with no incident support, or two blocks whose combined
neighbourhood has order at most one.  These are exactly the two displayed
forms.  In the single-block form, choose a missed required-set vertex `w_0\in W`
for `Q_0` and a missed required-set vertex `w_1\in W` for `Q_1`.  They are distinct:
`C=Q_0\dot\cup Q_1` is adjacent to every vertex of `B`, so no one vertex
of `W` can be missed by both parts.  Boundary-fullness of `C` then makes
`Q_1` meet `w_0` and `Q_0` meet `w_1`, proving the last assertion.
\(\square\)

## 3. A coupled proper-minor transition at every excess vertex

The frozen partition in Theorem 2.1 has a direct operation-specific
consequence.  It is the rigorous local replacement for treating colouring
changes as abstract permutations.

### Proposition 3.1

Assume outcome 3 of Theorem 2.1.  Let `w\in W`, choose neighbours

\[
                         u\in E,
 \qquad                  q\in C,                     \tag{3.1}
\]

and consider the two incident edges `wu,wq`.  The vertices `u,q` are
nonadjacent.  There is a proper six-colouring of
`G-\{wu,wq\}` in which `w,u,q` have one common colour, and at least one of
the following holds.

1. One of `wu,wq` has its ends in one bichromatic component for every one
   of the five alternate colours.
2. The graph `(G-\{wu,wq\})-w` contains a `u-q` path which is the union of
   two named bichromatic components and at most one joining edge.  A switch
   on the component through `u` gives a proper six-colouring of `G-wq`,
   and a switch on the component through `q` gives a proper six-colouring
   of `G-wu`.

In outcome 2, the two one-edge colourings induce different equality
partitions on the literal boundary `B`.  At least one of the two named
bichromatic components meets `B-\{w\}`.

### Proof

The sets `E` and `C` are distinct components of `G-B`, so `u,q` are
nonadjacent.  Contract the two-edge tree `u-w-q`.  The resulting proper
minor is six-colourable; expanding its contraction vertex gives the
displayed colouring of `G-\{wu,wq\}`.  The audited shared-interface
bichromatic-bypass theorem gives alternatives 1 and 2 and the two named
component switches.

Let `psi_C` be the colouring of `G-wq` obtained by switching the component
through `u`, and let `psi_E` be the colouring of `G-wu` obtained by
switching the component through `q`.  The restriction of `psi_C` to
`G[E\cup B]` is proper, because it restores `wu`; the restriction of
`psi_E` to `G[C\cup B]` is proper, because it restores `wq`.  If these
restrictions induced the same equality partition on `B`, they could be
aligned on their blocks and glued to a proper six-colouring of `G`.
Therefore the two partitions are different.

If neither switched bichromatic component met `B-\{w\}`, both switches
would leave the complete boundary assignment unchanged: neither component
contains the common centre `w`.  The two induced boundary partitions would
then be equal, a contradiction.  Thus at least one component has the
asserted literal boundary exposure.  \(\square\)

## 4. Optional extremal sharpening

Suppose a full-neighbourhood response side `E` with boundary order at least
eight is chosen lexicographically, among all such positive-excess response
sides, to minimize

\[
                         (|N_G(E)|,|E|),              \tag{4.1}
\]

and suppose no connected proper subset of `E` has a full neighbourhood of
order seven.  For every nonempty proper connected `A\subsetneq E`, put

\[
 h(A)=|N_G(A)\cap E|,
 \qquad
 m(A)=|B-N_G(A)|.                                    \tag{4.2}
\]

Then

\[
                              h(A)\ge m(A)+1.          \tag{4.3}
\]

Indeed, every neighbour of `A` outside `E` belongs to `B`, and hence

\[
                         |N_G(A)|=|B|+h(A)-m(A).       \tag{4.4}
\]

Any crossing-edge deletion makes `A` another response side.  If
`h(A)<m(A)`, its boundary is smaller than `B`; seven-connectivity and the
extra hypothesis exclude order seven, so it remains a positive-excess
response side and contradicts (4.1).  If equality holds, its boundary has
the same order and its connected side is smaller.  This also contradicts
(4.1), proving (4.3).

In particular, if `A` is a component behind an internal separator `K` of
`G[E]`, then `h(A)\le |K|` and

\[
                  |N_G(A)\cap B|
                    \ge |B|-|K|+1.                   \tag{4.5}
\]

Thus a five-vertex completion cut in an extremal positive-excess side
exposes its connected residual part to all but at most four literal
boundary vertices.

## 5. Exact contribution and trust boundary

Theorem 2.1 eliminates, for arbitrary shore sizes, every positive-excess
ordered instance whose opposite side has more than one component, unless a
strict boundary-order response descent already exists.  Its final case is
one connected opposite shore, normalized as two adjacent induced connected
subgraphs carrying all old boundary contacts.  Every operation-specific
partition then has an exact, literal Hall obstruction on those two
subgraphs.  Proposition 3.1 couples the two opposite one-edge responses in
one simultaneous-contraction colouring.

This does not close the final two-piece obstruction.  The Hall-deficient
required boundary sets can remain concentrated on one part, and the saturated alternative
in Proposition 3.1 does not assign palette colours to the old branch-set
labels.  A bare order-seven boundary returned in outcome 2 carries a
selected rejected response, not necessarily one partition extending
through both intact closed shores.

No transfer group or holonomy invariant is asserted.  Legal proper-minor
transitions can change the number and ownership of boundary blocks and need
not act as permutations of a fixed labelled set.  The well-founded quantity
proved here is literal boundary order; the retained dynamic data are the
required-set incidence graph and the two coupled one-edge colourings.

## 6. Dependencies

- [ordered two--three allocation in the order-eight interface](../results/hc7_order8_ordered_two_three_allocation.md)
- [host lift for positive boundary excess](../results/hc7_order8_small_completion_host_lift.md)
- [transported-partition Hall reflection](../results/hc7_transported_partition_hall_reflection.md)
- [bichromatic saturation or a bypass at two incident critical edges](../results/hc7_shared_interface_bichromatic_bypass.md)
- [generic exact-seven response restart](../results/hc7_generic_exact7_response_restart.md), only to identify the order-seven special case
