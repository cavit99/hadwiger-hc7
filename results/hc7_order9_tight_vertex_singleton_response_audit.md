# Independent audit of the tight-vertex singleton-response theorem

## Verdict and audited revision

**Verdict: GREEN.**

This audit checks the complete source file
[`hc7_order9_tight_vertex_singleton_response.md`](hc7_order9_tight_vertex_singleton_response.md)
at SHA-256

```text
88fb6b91b66c72aa9ce23e0b259117b96467f6a336d6598985abd1798893c8df
```

The degree identity, exact singleton response, fixed-trace rainbow
replacement, mixed tight/non-tight reduction, boundary-aligned response,
and four-colourability of its returned boundary are correct under the
stated hypotheses.  In particular,
the map in (2.5) really is a bijection onto the old list `L(v)`: the proof
does not silently assume that an arbitrary neighbour of `v` is coloured
from `L(v)`.  Rather, it forces all `|L(v)|-1` colours other than
`lambda(v)` into exactly `|L(v)|-1` available neighbour positions, leaving
no position for any other colour.

The audit treats the degree-nine local-completion theorem as the separately
GREEN-audited computer-assisted input cited by the source.  Its current
promoted statement and verifier hashes are

```text
dd8817ceec58b083e12adae943f49cf2bb5a401f17ca87950477906f811c5a08  results/hc7_degree9_pole_verifier.md
b4bab9be44feb5dc749dc8ba3f41a85094896d4b3de8a7d8246342b2729c9c59  results/hc7_degree9_pole_verifier.py
```

The boundary-four-colourability argument is the one already audited in
[`hc7_low_degree_adjacent_pair_alignment.md`](hc7_low_degree_adjacent_pair_alignment.md),
whose current promoted source hash is

```text
263611a40dc7829788967250e031a3f3170e1c7a6c8c9a3fbfbb358231b1f9ca
```

The source's one-step trust boundary is essential.  None of the returned
partitions is claimed to preserve the old minor-model labels or to re-enter
the original paired-kernel configuration.

## 1. Setting, list criticality, and degree accounting

For `v in Z`, let

```text
q(v) = |phi(N_G(v) intersect B)|.
```

The definitions in (1.2) give

```text
|L(v)|                    = 6-q(v),
d_G[Z](v)                 = 6-q(v)+epsilon(v),
|N_G(v) intersect B|      = q(v)+rho(v).
```

There are no edges from `Z` to the opposite shore.  Therefore these two
degree contributions exhaust the neighbours of `v`, and their sum is

```text
d_G(v)=6+epsilon(v)+rho(v),
```

which is (1.3).

Vertex-minimal non-`L`-colourability also implies
`d_{G[Z]}(v)>=|L(v)|`.  Otherwise an `L`-colouring of `G[Z]-v`, supplied by
vertex-minimality, would leave an available colour for `v`.  Thus every
`epsilon(v)` is a nonnegative integer, as used later in Corollary 3.1.

## 2. Exact order-nine singleton response

Write the six nonempty colour classes of the boundary colouring as
`C_1,...,C_6`, and put `n_i=|N_G(v) intersect C_i|`.  Directly from the
definition,

```text
rho(v)=sum_i max(0,n_i-1).
```

Since the six class orders sum to nine,

```text
sum_i (|C_i|-1)=3,
```

and termwise comparison gives `rho(v)<=3`.  For a tight vertex,
`epsilon(v)=0`, while the assumed host-degree lower bound and (1.3) give
`rho(v)>=3`.  Hence

```text
rho(v)=3 and d_G(v)=9.
```

Equality of the sums is literal, not merely colourwise.  For every
nonsingleton class `C_i`, equality

```text
max(0,n_i-1)=|C_i|-1
```

forces `n_i=|C_i|`.  Thus a tight vertex is adjacent to every boundary
vertex in every nonsingleton colour class.

The open neighbourhood `S=N_G(v)` has order nine.  The opposite shore is
nonempty and anticomplete to `v`, so it lies in `G-N_G[v]`.  Explicitly,

```text
G_1=G[N_G[v]],   G_2=G-v
```

form a separation with intersection `S`, singleton open side `{v}`, and a
nonempty opposite open side.  This verifies the separation assertion in
Theorem 2.1(1).

Fix an edge `vx`.  Edge deletion is a proper minor, so `G-vx` has a proper
six-colouring `c`.  If its ends had different colours, restoring the edge
would six-colour `G`; hence `c(v)=c(x)=alpha`.  Every vertex of `S-{x}` is
still adjacent to `v`, so no such vertex has colour `alpha`.  This proves

```text
c^{-1}(alpha) intersect S = {x}.
```

For a different colour `beta`, if `beta` were absent from `S-{x}`, then it
would be absent from all neighbours of `v`: the remaining neighbour `x`
has colour `alpha`.  Recolouring `v` with `beta` and restoring `vx` would
again six-colour `G`.  Therefore all five colours other than `alpha` occur
on `S-{x}`.  In particular, `c|S` uses all six colours.

The restriction to `G-v` is a colouring of the intact outside side, and
the restriction to `G[S union {v}]-vx` colours the edge-deleted singleton
side.  Any six-colouring inducing the same equality partition on `S` has
six nonempty colour blocks, hence uses all six palette colours there.  No
colour is available for the vertex adjacent to all of `S`.  Thus the
intact singleton side rejects exactly that equality partition.  The source
does not infer rejection of an unrelated trace.

## 3. Fixed-trace rainbow replacement

Let `vw` be an internal shore edge and let `v` be tight.  Colour
`G[Z]-v` from `L`, which vertex-minimality permits.  In the edge-deleted
graph `G[Z]-vw`, the vertex `v` has exactly

```text
d_G[Z](v)-1 = |L(v)|-1
```

coloured neighbours.  Hence at least one colour of `L(v)` is available,
and the colouring extends properly to `G[Z]-vw`.  This proves existence;
it does not assume that a preselected colouring extends.

Now let `lambda` be any `L`-colouring of that edge-deleted graph.  If
`lambda(v)` and `lambda(w)` differed, restoring `vw` would give an
`L`-colouring of the intact shore, contradicting list criticality.  Put

```text
alpha=lambda(v)=lambda(w).
```

Every neighbour of `v` other than `w` is adjacent to `v` in the
edge-deleted graph and therefore avoids `alpha`.  If a colour
`beta in L(v)-{alpha}` were absent from those neighbours, recolouring `v`
with `beta` and restoring `vw` would colour the intact shore.  Thus every
one of the `|L(v)|-1` colours in `L(v)-{alpha}` occurs among the exactly
`|L(v)|-1` vertices of `N_{G[Z]}(v)-{w}`.

This counting point is enough even though a neighbour `y` is formally
coloured from `L(y)`, not from `L(v)`: all the required colours occupy all
available positions, each once.  Together with the value `alpha` at `w`,
the restriction

```text
lambda : N_G[Z](v) -> L(v)
```

is a bijection, exactly as asserted in (2.5).

The equality case in the boundary calculation showed that every
nonsingleton boundary class is complete to `v`.  Consequently a colour is
in `L(v)` if and only if its boundary class is a singleton `{b}` missed by
`v`.  Hence `B-N_G(v)` contains exactly one literal boundary vertex per
colour in `L(v)`.  Matching equal colours through (2.5) gives the bijection
(2.6).  Finally,

```text
N_G(v)=(B intersect N_G(v)) disjoint-union N_G[Z](v),
```

because the shores are anticomplete, while `B` is obtained by replacing
the second term with `B-N_G(v)`.  Both sets have order nine, and the
identity on their common boundary part plus (2.6) preserves every colour
class.  The final replacement statement is therefore exact.

## 4. The mixed tight/non-tight branch

A vertex-minimal non-list-colourable graph is connected: otherwise one of
its proper components would already be non-list-colourable.  Positive total
excess supplies a non-tight vertex.  If a tight vertex exists, a path from
the tight set to the non-tight set contains an edge `vw` with `v` tight and
`w` non-tight.  Theorem 2.1 applies to this literal edge and returns the
singleton response.

The original shore has more than one vertex.  A one-vertex
vertex-minimal list obstruction has empty list and internal degree zero,
so its excess is zero, contrary to the positive-total-excess hypothesis.
The returned rejected side therefore has order one strictly below
`|Z|`.  If no tight vertex exists, nonnegative integral excess gives
`epsilon(u)>=1` for every shore vertex.  This proves Corollary 3.1 exactly
as stated.  It is only a one-step reduction: the returned boundary and
trace are not asserted to retain the old endpoint data.

## 5. Boundary alignment at a tight vertex

Assume the extra hypotheses of Theorem 3.2.  Tightness and Theorem 2.1 give
`d_G(v)=9`.  The exterior `G-N_G[v]` is nonempty because it contains the
nonempty opposite shore.

Let `T_ext` be the neighbours of `v` with an exterior neighbour, and let
`R=N_G(v)-T_ext`.  There is no edge from `{v} union R` to the nonempty
exterior after deleting `T_ext`, so seven-connectivity gives
`|T_ext|>=7`.

Suppose every `x in T_ext` satisfied `chi(G-{v,x})=5`.  In a five-colouring
of `G-{v,x}`, each of the five colours has a common neighbour of `v,x`.
Indeed, if colour `i` had no such common neighbour, recolour every
colour-`i` neighbour of `v` with a fresh sixth colour, give `v` colour `i`,
and give `x` the fresh colour.  The recoloured vertices are independent and
none is adjacent to `x`; this would six-colour `G`.  Hence each
`x in T_ext` has at least five neighbours in `H=G[N_G(v)]`.

For `x in R`, all its neighbours lie in `N_G[v]`.  Seven-connectivity gives
`d_G(x)>=7`, so `d_H(x)=d_G(x)-1>=6`.  Thus `delta(H)>=5` and
`|E(H)|>=23`.

Contract a component of `G-N_G[v]` to a vertex `c` and delete all other
exterior vertices.  Its neighbourhood is contained in `H` and has order at
least seven by seven-connectivity.  The resulting graph on
`{v} union V(H) union {c}` has eleven vertices and exactly

```text
9+|E(H)|+d_H(c)
```

edges.  Mader's `K_7` bound gives a `K_7` minor whenever this quantity is
greater than `5*11-15=40`.  With `|E(H)|>=23` and `d_H(c)>=7`, the only
non-strict regimes are

```text
(|E(H)|,d_H(c)) in {(23,7),(23,8),(24,7)}.
```

These are exactly the three hypotheses of the cited degree-nine local
completion theorem.  It supplies a `K_6` model in `H+c` all of whose six
branch sets meet `H`.  Since `v` is complete to `H`, the singleton `{v}`
is adjacent to every branch set and produces a `K_7` model.  Both the
strict and equality regimes contradict the source hypothesis.

Therefore some `z in T_ext` has `chi(G-{v,z})` different from five.  It is
at least five because deleting two vertices lowers chromatic number by at
most two, and at most six because it is a proper minor of `G`; hence it is
six.

Choose an exterior component `C` adjacent to `z`.  Its full neighbourhood
`S=N_G(C)` is contained in `N_G(v)`: exterior vertices have no edge to `v`,
and every neighbour outside `C` lies in the closed neighbourhood deleted
when defining the exterior.  Seven-connectivity and `d_G(v)=9` give

```text
z in S subseteq N_G(v),  7<=|S|<=9.
```

In a six-colouring of `G-vz`, the ends receive one common colour.  Every
member of `S-{z}` is still adjacent to `v`, so `{z}` is the exact boundary
block in that colour.  The `C`-side omits `v` and is intact.  The opposite
side contains the only deleted edge; if its intact version admitted the
same equality partition, colour-name alignment and gluing across the full
neighbourhood `S` would six-colour `G`.  Thus the operation-specific
response statement is correct.

If `|S|=9`, inclusion in the nine-set `N_G(v)` gives equality.  The
component `C` and singleton `{v}` are then connected and each adjacent to
every literal vertex of `S`.  Applying Theorem 2.1 to the same edge `vz`
shows that this trace uses all six colours.  If `|S|` is seven or eight, it
is exactly the smaller-boundary response stated in outcome 1.

The added conclusion `chi(G[S])<=4` uses no unproved property of the
operation-specific trace.  Its geometry matches the audited bounded-
boundary argument exactly: `C` is a connected `S`-full component, and the
component of `G-S` containing `v` is a distinct connected `S`-full
component because `v` is adjacent to every member of `S`.

- At order seven, seven-connectivity makes all complementary components
  full.  The exact-seven classification leaves a five-chromatic boundary
  only in the `K_2 join C_5` case, and the audited cycle-boundary completion
  excludes that case.  Thus the boundary is four-colourable.
- At order eight, the audited two-full-shore absorption theorem directly
  makes the boundary four-colourable.
- At order nine, that theorem leaves only `K_2 join C_7`.  If `G-S` has
  exactly two components, the cycle-boundary completion theorem applies to
  them; its required `K_5` minor after deleting the universal boundary edge
  follows from `chi(G)=7` and `HC_5`.  If there is a third component,
  seven-connectivity makes it miss at most two boundary vertices, and the
  explicit seven-branch-set construction in the audited low-degree theorem
  gives a `K_7` minor in every possible missed-pair orbit.

These alternatives exhaust the number of components of `G-S`.  Therefore
the sole order-nine exception is impossible and `chi(G[S])<=4` holds in
all three boundary orders.  This conclusion is structural; it does not say
that the particular six-colour response partition has a compatible
extension through both intact shores.

## 6. Companion barrier and trust boundary

The companion
[`hc7_order9_tight_forest_block_descent_barrier.md`](../barriers/hc7_order9_tight_forest_block_descent_barrier.md)
is consistent with this theorem.  Its four-cycle shore has the stated
lists, is vertex-minimal non-list-colourable, has tight subgraph equal to
the single edge `uv`, and has positive total excess.  The common
neighbourhood of that tight edge has order ten, so it correctly refutes a
small-*block*-boundary shortcut.  Each tight endpoint nevertheless has
host degree nine and hence exposes the singleton response proved here.

The audited theorem does **not** prove any of the following:

- that the new boundary is `K_5`-minor-free;
- that all exterior components are adjacent to every new boundary vertex;
- that the returned partition preserves the old trace or any named
  minor-model branch sets;
- that the edge-deleted response extends through both intact shores; or
- that iterating the one-step reduction stays in the same class.

Theorem 3.2 selects one exterior component and makes it full only in its
order-nine outcome.  It does not remove these trust-boundary restrictions.
Subject to the cited degree-nine completion input, there is no unresolved
gap in the source statement.
