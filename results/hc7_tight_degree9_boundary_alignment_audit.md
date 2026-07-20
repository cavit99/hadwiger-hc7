# Independent audit of boundary alignment at a tight degree-nine vertex

## Verdict and audited revision

**Verdict: GREEN.**

This audit checks the complete source file
[`hc7_tight_degree9_boundary_alignment.md`](hc7_tight_degree9_boundary_alignment.md)
at SHA-256

```text
1ea36e3e3ba933c5d15b9fa6577005cc4ae7d584907fe55d0b52b35a40508f12
```

The boundary-aligned edge, operation-specific response, deletion of one
boundary vertex to a `K_5`-minor-free base, full-component density bound,
choice of a sparse boundary vertex, exterior-neighbour count, and rooted
`K_2 join (H-x)` minor are all correct.  The final revision correctly
separates Mader's strict density branch from the three finite regimes of
the degree-nine pole verifier and explicitly invokes `HC_6` before using a
spanning `K_6` model.

The archived degree-nine component-count result is mentioned only as
historical context and is not used by any theorem conclusion.  Its legacy
audit therefore does not enter the trust chain of this result.

## 1. Exact hypotheses and principal dependencies

The source assumes that `G` is seven-connected and seven-chromatic, has no
`K_7` minor, and has every proper minor six-colourable.  The chosen vertex
`v` has degree nine and a nonempty exterior `G-N_G[v]`.  Put

```text
H=G[N_G(v)].
```

The separately audited degree-nine pole completion has current promoted
statement and verifier hashes

```text
dd8817ceec58b083e12adae943f49cf2bb5a401f17ca87950477906f811c5a08  results/hc7_degree9_pole_verifier.md
b4bab9be44feb5dc749dc8ba3f41a85094896d4b3de8a7d8246342b2729c9c59  results/hc7_degree9_pole_verifier.py
```

The audited adjacent-pair palette theorem is used only after the source has
proved `chi(G-{v,x})=6` and invoked established `HC_6` to obtain a `K_6`
model.  Its current promoted source hash is

```text
2b0c30b9d8566f6da4959df145bf0f527249bf887dfa844d19a98e524080a9f2
```

The source also uses Mader's exact `5n-15` bound and established `HC_5` and
`HC_6`, all at their stated strengths.

## 2. The exterior-contact set and the aligned edge

Let `T` be the neighbours of `v` having a neighbour outside `N_G[v]`.
After deleting `T`, no edge joins the nonempty exterior to `v` or to a
neighbour in `N_G(v)-T`.  Hence `T` is a vertex separator and
seven-connectivity gives `|T|>=7`.

Assume every `y in T` has `chi(G-{v,y})=5`.  In a five-colouring of this
double vertex deletion, each colour has a common neighbour of `v,y`.
Otherwise recolour all neighbours of `v` in a missing common-neighbour
colour with a fresh sixth colour, then give `v` the old colour and `y` the
fresh colour.  The recoloured class is independent and anticomplete to
`y`, so this would six-colour `G`.  Thus `d_H(y)>=5` for `y in T`.

For `y in N_G(v)-T`, all its neighbours lie in `N_G[v]`.  Since
`d_G(y)>=7` and one neighbour is `v`, one has `d_H(y)>=6`.  Consequently
`delta(H)>=5` and `|E(H)|>=23`.

Contract an exterior component to `c` and delete every other exterior
vertex.  Seven-connectivity gives `d_H(c)>=7`.  On the eleven vertices
`{v} union V(H) union {c}`, the edge count is

```text
9+|E(H)|+d_H(c).
```

It exceeds Mader's threshold `40` except when

```text
(|E(H)|,d_H(c)) in {(23,7),(23,8),(24,7)}.
```

The strict branch gives a `K_7` minor directly.  In each of the three
equality regimes, the cited finite theorem gives a `K_6` model in `H+c`
whose every branch set meets `H`; the singleton `{v}`, complete to `H`,
supplies the seventh branch set.  This proves that some `x in T` instead
satisfies `chi(G-{v,x})=6`.  No finite verifier conclusion is used outside
its three stated regimes.

Choose an exterior component `C` adjacent to `x` and put `S=N_G(C)`.
Componenthood gives `S subseteq N_G(v)`, while seven-connectivity gives
`7<=|S|<=9`.  By definition `C` is connected and adjacent to every literal
member of `S`; `{v}` is connected and likewise full because `S` lies in
its neighbourhood.

## 3. Response orientation and exact singleton block

Here `G-{v,x}` denotes the double vertex deletion used to select the edge,
while `G-vx` denotes deletion of the edge itself.  Every proper
six-colouring of the latter graph gives `v,x` the same colour, since
otherwise the edge can be restored.  Every vertex of `S-{x}` remains
adjacent to `v`, so `{x}` is the exact boundary block in that common colour.

The closed side `G[C union S]` omits `v` and therefore does not contain the
deleted edge; its restriction is a colouring of the intact `C`-side.  The
opposite side `G-C` contains `v,x` and is coloured only after deleting
`vx`.  If the same equality partition extended through the intact graph
`G-C`, a permutation of colour names would align it with the intact
`C`-side colouring and the two would glue across the full neighbourhood
`S`.  This would six-colour `G`.  Thus the intact opposite side rejects the
partition.  The orientation in Theorem 2.1(3) is correct.

## 4. Deleting the selected boundary vertex removes every `K_5` minor

Suppose `G[S-{x}]` contained a `K_5` model with branch sets
`M_1,...,M_5`.  Then

```text
M_1,...,M_5, C, {v,x}
```

are seven disjoint connected sets.  The first five are pairwise adjacent;
`C` is adjacent to each because it is full to every literal boundary
vertex; and `{v,x}` is adjacent to each through `v`.  Finally `{v,x}` is
connected by the selected edge and is adjacent to `C` through an
`x-C` edge, since `x in S=N_G(C)`.  These are explicit `K_7` branch sets,
contrary to the hypothesis.

Therefore `G[S-{x}]` is `K_5`-minor-free.  Established `HC_5` makes it
four-colourable.  This conclusion is about the literal induced boundary
minus `x`; it is not inferred merely from a palette or a quotient label.

When `|S|=9`, inclusion in the nine-set `N_G(v)` gives equality.  In an
edge-deletion colouring, the common endpoint colour occurs at `x` and
nowhere else in `S`; if one of the other five colours were absent from
`S-{x}`, recolouring `v` with it and restoring `vx` would six-colour `G`.
Hence all six colours occur on the equality boundary, as stated.

## 5. The full exterior component

Now suppose a component `C` is adjacent to all nine vertices of `H`.
Contract it to `c`, discard every other exterior vertex, and retain
`v,H,c`.  The two vertices `v,c` are nonadjacent and each complete to `H`,
so the resulting eleven-vertex minor has exactly

```text
18+|E(H)|
```

edges.  Mader's upper bound `40` therefore gives `|E(H)|<=22`.

The average degree of the nine-vertex graph `H` is at most `44/9<5`, so
some `x` has `d_H(x)<=4`.  If `chi(G-{v,x})=5`, the common-neighbour
argument above gives five distinct common neighbours, all lying in `H`,
contradicting this degree.  Double vertex deletion lowers chromatic number
by at most two and the resulting proper minor is six-colourable, so its
chromatic number is exactly six.

Fullness of `C` makes this same `x` exterior-contacting, so the response
argument applies with `S=N_G(v)` and the selected component `C`.  The exact
degree decomposition is

```text
d_G(x)=1+d_H(x)+|N_G(x) intersect (V(G)-N_G[v])|.
```

Seven-connectivity implies `d_G(x)>=7`; therefore `x` has at least
`6-d_H(x)>=2` exterior neighbours.  If `C` is the unique exterior
component, both of these neighbours lie in `C`.  The preceding `K_5`
exclusion with `S=N_G(v)` gives that `H-x` is `K_5`-minor-free.

Established `HC_6` gives a `K_6` model in the six-chromatic graph
`G-{v,x}`.  This graph is five-connected, hence connected; any such model
can be enlarged along the components outside its branch-set union to a
spanning model.  All hypotheses of the audited adjacent-pair
palette-permutation theorem are now satisfied.  It yields the five
pairwise vertex-disjoint paths with the complete five-colour palettes at
the poles.  No same-colour endpoint pairing or label-preserving path system
is inferred.

## 6. The rooted two-apex-type minor

In the full-component branch, contract `C` to one branch set and contract
the connected edge `vx` to another.  Retain every vertex of `H-x` as a
singleton.  The two contracted branch sets are adjacent through the
`x-C` edge.  Each is adjacent to every singleton of `H-x`: `C` is full to
`H`, and `v` is complete to `H`.  All base edges of `H-x` remain.
Therefore these branch sets realize the rooted minor

```text
K_2 join (H-x).
```

The base is `K_5`-minor-free by Section 5.  This is a structural local
minor, not a `K_7` contradiction and not a global two-vertex transversal.

## 7. Trust boundary

The theorem does not prove that the aligned `x` belongs to the old shore
rather than the old boundary, identify any palette colour with a named
minor-model branch set, synchronize the fixed-trace and whole-host
colourings, or re-enter the paired list obstruction after the returned
response.  It also does not bound the number of exterior components.

The source explicitly labels the archived degree-nine component closure as
a legacy, unrepinned result and does not use it.  Thus no archived or
legacy-audited claim is required for this GREEN verdict.
