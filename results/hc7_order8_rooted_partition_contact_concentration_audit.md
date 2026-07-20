# Independent audit: rooted partitions and enlarged-boundary contact concentration

**Verdict:** **GREEN** for the exact source revision identified below.

This is a separate internal mathematical audit, not external peer review.  It
checks every hypothesis, conclusion, and proof step in Theorem 2.1,
Proposition 3.1, Theorem 4.1, and Corollary 5.1, including all branch-set
checks for the explicit model (4.5) and the exact specialization of the
cycle-completion theorem.  The result is an unbounded conditional reduction
and does not prove `HC_7`.

## Audited revision

The audited source is
[`hc7_order8_rooted_partition_contact_concentration.md`](hc7_order8_rooted_partition_contact_concentration.md)
at mathematical SHA-256

```text
b5fbe15bea8959a6cef393a6245e3310ca4917505bd2be8457e739e5642a4b9f
```

The promoted source changes only the status paragraph to link this audit;
its promoted SHA-256 is recorded below.

```text
86f53c727b7855b8ddea420a957320a188b61570924d8508f5dd8806ab138d20
```

The dependency revisions inspected for the uses made here are:

```text
b9e913fbece2258d4a9d8448c2ea414a5f2b76df7ab895ffe3a13a115becc9f3
  ../results/hc7_order8_positive_excess_frozen_outer_shore.md
e22e88a66d4a9eed07e1f86888adcb80c7ab826c03de99e4a5a830999f3ccbd4
  ../results/hc7_transported_partition_hall_reflection.md
e689c96686a936c27e58c2cba22d699c62ad649092eebfcdfc9c5db95a8e7b5a
  ../results/hc7_generic_exact7_response_restart.md
832fff95b699aa73b1f1b10cc52e1f562d6e108dad059962b3563a799bc3f875
  ../results/hc7_adjacent_full_pair_cycle_completion.md
```

Each dependency has an adjacent GREEN internal audit.  In particular, the
cycle-completion audit explicitly checks the final promoted revision whose
hash is recorded above.  The present source avoids duplicating that general
proof: Corollary 5.1 is only its specialization to the current interface.

## 1. Hypotheses and inherited normal form

The ambient assumptions provide seven-connectivity, non-six-colourability,
`K_7`-minor-freeness, and a proper six-colouring of every proper minor.  They
are exactly the properties invoked in the separator, edge-deletion, and
terminal-model arguments.

The inherited positive-excess outcome is quoted with the needed strength:

\[
 G-B\text{ has exactly the components }E,C,
 \qquad C\text{ is connected and full to }B,
 \qquad P_0\cup P_1\subseteq C.
\]

The source additionally assumes, rather than derives, an arbitrary rooted
connected partition `C=Q_0 dotcup Q_1` with `P_i` contained in `Q_i`.  No
later step silently assumes that such a partition has an extra optimization
property.  Both parts are nonempty because they contain the nonempty
connected subgraphs `P_0,P_1`.

The boundary identity

\[
 B=(S-\{e\})\mathbin{\dot\cup}W,
 \qquad |B|=7+|W|\ge9
\]

is used consistently.  In particular `e` is in `C`, whereas the other seven
literal vertices of `S` are in `B`.

## 2. Theorem 2.1: exact contact concentration

Deleting `B` from the displayed vertex partitions leaves exactly

\[
 E\mathbin{\dot\cup}(D-W)\mathbin{\dot\cup}\{e\}
   \mathbin{\dot\cup}R.
\]

Since the only component of `G-B` other than `E` is `C`, and `C` contains
`R` through `P_0,P_1`, the asserted identity

\[
 C=(D-W)\mathbin{\dot\cup}\{e\}\mathbin{\dot\cup}R
\]

is exact.  There are no `D-W`--`R` edges because `D-W` is contained in `L`
and the original open shores `L,R` are anticomplete.  Consequently every
path inside `C` from `D-W` to `R` must pass through the sole remaining
intermediate vertex `e`.

Let `e` belong to `Q_j`.  The other part `Q_{1-j}` contains
`P_{1-j}` in `R`.  If it met `D-W`, its connectedness would produce a
`D-W`--`R` path inside that part, which would have to contain `e`.  This is
impossible because the parts are disjoint.  Thus

\[
 Q_{1-j}\subseteq R,
 \qquad D-W\subseteq Q_j.
\]

Every `P_i` is adjacent to every literal vertex of `S`, so each `Q_i` meets
all seven boundary vertices in `S-{e}`.  For `w in W`, fullness of `C` to
`B` supplies a neighbour of `w` in `C`.  Since `w in D subseteq L`, the
absence of `L`--`R` edges and the exact decomposition of `C` give

\[
 N_G(w)\cap C\subseteq(D-W)\cup\{e\}\subseteq Q_j.
\]

Hence every `w` is met by `Q_j` and by no vertex of `Q_{1-j}`.  This proves
the two exact boundary-contact identities (2.2), not merely inclusions.
The three optimization consequences then hold for every admissible rooted
partition: the number of shared `W` contacts is identically zero, and the
labelled owner is precisely the side containing `e`.

## 3. Proposition 3.1: response orientation and Hall incidence

For a crossing edge `uv` with `u in E` and `v in B`, edge deletion is a
proper minor, so a proper six-colouring of `G-uv` exists.  Its endpoints
must have one colour; otherwise restoring `uv` would six-colour `G`.

The restriction to `G[C union B]` is proper because the deleted edge has
its nonboundary endpoint in `E`.  If its equality partition `Sigma` on `B`
also extended through the intact graph `G[E union B]`, the two boundary
colourings would induce the same blocks.  A permutation of the six colour
names would align them, and the absence of `E`--`C` edges would permit
gluing to a six-colouring of `G`.  Thus the legal/rejected orientation in
the proposition is correct.

The full-subgraph demand is nonzero.  The boundary has at least nine
vertices but `Sigma` has at most six blocks, so at least one block is
nonsingleton.  Such a block cannot be represented in the clique `U` of
singleton blocks and therefore occurs among `C_1,...,C_t`; hence `t>=1`.

The transported-partition Hall theorem is instantiated as follows:

- the coloured open shore is `C` and the rejected opposite shore is `E`;
- the literal boundary is `B`;
- `Q_j` is the one boundary-full universal support; and
- `Q_{1-j}` is the one subordinate support, incident with a block exactly
  when it is full to that block's duty `F_i`.

The two supports are disjoint and connected.  They are also adjacent: a
partition of the connected graph `G[C]` into two nonempty parts cannot have
no edge between the parts.  Adjacency is more than is needed between the
universal and subordinate families in the cited theorem, but is valid.

A matching saturating all demand blocks would, by the sufficiency direction
of the Hall theorem, extend `Sigma` through the rejected `E`-shore and hence
six-colour `G`.  Therefore no such matching exists.  This conclusion does
not rely on the theorem's restricted necessity statement.

Theorem 2.1 makes `Q_j` universal.  The other support is full to exactly
`S-{e}` among the vertices of `B`; it misses every vertex of `W`.  Since
each duty `F_i` is a literal subset of `B`, its exact incidence rule is

\[
 Q_{1-j}\sim C_i
 \quad\Longleftrightarrow\quad F_i\cap W=\varnothing.
\]

For `t=1`, the universal support itself is a saturating matching, a
contradiction.  Hence `t>=2`.  For `t=2`, assign the universal support to
either demand block.  A saturating matching then exists exactly when the
other support is incident with at least one block.  Hall failure is
therefore equivalent to both duties meeting `W`, as stated in (3.2).
Because every demand block is incident with the universal support, no block
is isolated; this excludes the isolated-duty alternative, including its
crossed two-contact specialization.

## 4. Theorem 4.1: component boundary and response descent

Let `Z` be a component of `G[D-W]`.  Every possible neighbour class is
accounted for:

- `Z` has no neighbour in `E`, because every vertex of `D` with an
  `E`-neighbour lies in `W`;
- it has no neighbour in `R`, by the `L`--`R` anticompleteness;
- it has no neighbour in another component of `G[D-W]`; and
- it has no neighbour at `d`, because `N_G(D) intersect S=S-{d}`.

Thus

\[
 N_G(Z)\subseteq T=(S-\{d\})\mathbin{\dot\cup}W.
\]

This is an actual separator boundary.  The nonempty set `R` is disjoint
from both `Z` and `N_G(Z)`, so it survives on the other side of the full
neighbourhood.  Seven-connectivity supplies the lower bound seven, while
the containment and `|T|=|B|` supply the upper bound in (4.4).

For every edge `xy` crossing from `Z` to `N_G(Z)`, a proper six-colouring of
`G-xy` exists and gives `x,y` one colour.  Its outside restriction properly
colours the intact graph `G-Z`; its inside restriction colours
`G[Z union N_G(Z)]-xy`.  Both restrictions induce the same equality
partition on the boundary.  If that partition extended through the intact
inside shore, a palette permutation and the full-neighbourhood separation
would glue the two restrictions to a six-colouring of `G`.  The asserted
rejection is therefore exact and is available for every crossing edge and
every such colouring.

If the neighbourhood containment is proper, integrality gives either order
seven or an order in `[8,|B|-1]`, exactly outcomes 1 and 2.  At order seven,
`Z`, its full neighbourhood, the nonempty outside shore, a crossing edge,
and its edge-deletion colouring satisfy every clause in the cited definition
of a generic exact-seven response interface.  If the containment is
equality, then `N_G(Z)=T`, which by the definition of open neighbourhood
says that `Z` is full to every literal vertex of `T`.

## 5. Explicit verification of the model (4.5)

Assume two distinct components `Z_0,Z_1` have equality neighbourhood `T`.
The proposed seven branch sets are

\[
\begin{aligned}
 A_0&=Z_0\cup\{x_d\},&
 A_1&=Z_1\cup\{y_d\},\\
 A_2&=V(P_0)\cup\{x_0\},&
 A_3&=V(P_1)\cup\{y_0\},\\
 A_4&=\{e\},&A_5&=\{x_e\},&A_6&=\{y_e\}.
\end{aligned}
\]

All seven sets are nonempty and pairwise disjoint.  The first two have
their underlying vertices in distinct components of `D-W`; the next two
have disjoint underlying subgraphs in `R`; the four underlying subgraphs
are disjoint from `S`; and the seven displayed literal vertices are all
distinct.

Every branch set is connected.  The sets `Z_0,Z_1,P_0,P_1` are connected;
equality components are adjacent to every vertex of `S-{d}`, while each
`P_i` is adjacent to every vertex of `S`.  These facts supply respectively
the edges attaching `x_d,y_d,x_0,y_0`.  The last three branch sets are
singletons.

The twenty-one branch-set pairs are all adjacent:

- the six pairs among `A_0,...,A_3` are adjacent because the underlying
  subgraph of either member has a neighbour at the distinct boundary vertex
  attached to the other;
- the twelve pairs having one member among `A_0,...,A_3` and one among
  `A_4,A_5,A_6` are adjacent because every underlying subgraph is full to
  `S-{d}`, which contains `e,x_e,y_e`; and
- the three pairs among `A_4,A_5,A_6` are edges of the triangle
  `e x_e y_e e`.

Thus the seven disjoint connected branch sets are pairwise adjacent and
form an explicit `K_7`-minor model.

If the model and both response-descent outcomes are absent, every component
of `G[D-W]` must have equality neighbourhood `T`, while the model check
allows at most one such component.  Hence `D-W` is empty, or it is connected
and has neighbourhood exactly `T`, proving (4.6).

## 6. Corollary 5.1 and the cycle-completion specialization

All hypotheses of the audited general cycle-completion theorem are present.
The exact translation of its notation is

\[
 A_d=D,\qquad A_e=E,\qquad Q_i=P_i.
\]

Indeed `D,E` are vertex-disjoint connected subgraphs of the connected shore
`L`, and (1.6) gives

\[
 S-\{d\}\subseteq N_G(D)\cap S,
 \qquad S-\{e\}\subseteq N_G(E)\cap S.
\]

The subgraphs `P_0,P_1` are disjoint, nonempty, connected, lie in the
connected shore `R`, and are full to `S`.  The shores are anticomplete and
`|S|=8`.  Thus Lemma 2.1 of the dependency supplies a connected adjacent
partition `R=R_0 dotcup R_1` with `P_i subseteq R_i`.

The dependency normally joins `A_d,A_e` along a shortest path in `L` before
forming its off-cycle branch sets.  Here `D` and `E` are already adjacent,
so that path has one edge and no internal vertices.  Consequently the
enlarged subgraphs remain exactly `D,E`, and the four off-cycle branch sets
are, up to order,

\[
 R_0,\quad R_1,\quad E\cup\{d\},\quad D\cup\{e\},
\]

as claimed in (5.3).

The assertion for **any** partition satisfying (5.2) is also valid directly,
not only for the one returned by the dependency:

- disjointness follows from `L dotcup S dotcup R`, `E dotcup D`, and
  `R_0 dotcup R_1`;
- `E union {d}` and `D union {e}` are connected because (1.6) supplies an
  `E`--`d` edge and a `D`--`e` edge;
- `R_0,R_1` are adjacent by assumption, each `R_i` meets the two enlarged
  left sets through the `P_i` contacts at `d,e`, and the two left sets are
  adjacent through the assumed `E`--`D` edge; and
- every `R_i` is full to `F=S-{d,e}` through `P_i`, while (1.6) makes both
  enlarged left sets full to `F`.

For completeness, if a cycle of `G[F]` is divided into three nonempty
consecutive arcs `M_1,M_2,M_3`, the seven sets

\[
 R_0,\ R_1,\ E\cup\{d\},\ D\cup\{e\},\ M_1,\ M_2,\ M_3
\]

are pairwise disjoint and connected.  Their twenty-one adjacencies comprise
the six pairs among the first four sets, the twelve pairs between those four
`F`-full sets and the three nonempty arcs, and the three cycle-transition
edges among the arcs.  They therefore form the explicit `K_7`-minor model
from the cited theorem.  The standing exclusion of that minor makes `G[F]`
a forest.

The superseded local maximal-coverage proof is not present in the audited
revision and is not used.  Delegating the adjacent-cover construction and
cycle completion to the already audited general theorem avoids a second
proof of the same result while preserving the exact stronger local
description (5.2)--(5.3).

## 7. Trust boundary and unresolved work

No mathematical gap or unresolved assumption was found within the stated
conditional scope.  In particular, the proof is not a finite-enumeration
argument and makes no inference from bounded computational evidence.

The result deliberately does **not** establish any of the following:

- that the surviving connected equality component `D-W` carries a recursive
  rooted order-eight interface;
- that its reversed boundary `(S-{d}) union W` preserves the original
  prescribed roots or boundary labels;
- that the operation-specific edge-deletion colourings can be chosen
  compatibly across both intact shores;
- that a Hall obstruction of demand at least three can be repaired; or
- that the remaining demand-two residue yields a `K_7` minor or proves
  `HC_7`.

Indeed `D-W` contains neither `P_0` nor `P_1`, its equality boundary replaces
`d` by `e`, and every admissible rooted partition still places it on the
side containing `e`.  Corollary 5.1 adds only the independent forest
constraint on the six non-root boundary vertices.  The source therefore
states the available descent and the surviving obstruction at exactly the
strength proved.
