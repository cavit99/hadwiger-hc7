# Independent audit: double-triangle partial-packet exchange

**Status:** GREEN.

## Verdict

**GREEN after one hypothesis clarification.**  Section 1 now explicitly
states the intended exact packet maxima `(nu_L,nu_R)=(1,2)`.  This matters
for the cutvertex corollary: seven-connectivity makes every open-shore
component `S`-full, so `nu_L=1` implies that `G[L]` is connected.  Merely
saying that `L` contains one full packet would not have supplied that fact.

The demand normalization, one-extra-carrier reflection, crossed-pure funnel,
cutvertex grouping, Moser consequence, and explicit width-five obstruction
all survive independent checking.  The Moser conclusion does **not** exclude
`|L|=1` and therefore does not yet imply that the thin shore is 2-connected.

## 1. Exact demand-three normalization

For each of the nine hard boundary orbits with `alpha(H)=3`, any maximum
independent triple `I` has a nonsplit four-vertex remainder.  On four
vertices a nonsplit graph is `2K_2` or `C_4`, hence has clique number two.
The audited split-remainder criterion and maximum-demand formula give

```text
min d_H(Pi) = 3,
max d_H(Pi) = 1 + 4 - 2 = 3.
```

For the standard Moser spindle, `I={0,5}` is independent and the remainder
is exactly the disjoint union of triangle `126` and edge `34`.  It is
nonsplit with clique number three, so

```text
min d_H(Pi) = 3,
max d_H(Pi) = 1 + 5 - 3 = 3.
```

An independent enumeration of all proper equality partitions confirmed the
singleton demand set `{3}` for the stated `I` in all ten orbits.

## 2. One-extra-carrier reflection

Let `C` be a maximum clique among the singleton blocks of the returned
partition `Pi`.  Since `d_H(Pi)=3`, precisely three blocks are not represented
by vertices of `C`; call them `B_1,B_2,B_3`.

The sets

```text
P_1 union B_1,
P_2 union B_2,
T   union B_3
```

are pairwise disjoint and connected.  The first two packets are disjoint and
full; `T` lies outside them and contacts every vertex of `B_3`.  Their three
contracted representatives are pairwise adjacent:

* representatives 1 and 2 use a `P_1`--`B_2` edge;
* representatives 1 and 3 use a `P_1`--`B_3` edge;
* representatives 2 and 3 use a `P_2`--`B_3` edge.

The first two representatives see every `c in C` by fullness.  The third
sees `c` either through a `T`--`c` edge or through a literal edge from `c`
to `B_3`.  Hence the representatives together with `C` form a clique with
one vertex for every block of `Pi`.

At least one packet--boundary edge is contracted, so the minor is proper.
Its colouring is restricted only to the untouched thin closed shore;
no rich packet is expanded on its own side.  Expanding the independent
blocks `B_i` is proper edge by edge, and the representative clique forces
the equality partition to be exactly `Pi`.  Palette alignment and gluing are
therefore valid.

## 3. Near-full carriers and the crossed-pure funnel

For adjacent connected thin carriers `X,Y` with one-point defects, put
`C_0=N_S(X) intersection N_S(Y)`.  Since each defect has order at most one,
`|C_0|>=5`.

If a boundary triangle `T` avoids both defects, choose two distinct anchors
outside `T` and the defects.  The seven bags

```text
P_1 plus anchor 1,
P_2 plus anchor 2,
X, Y,
three singleton vertices of T
```

are literal, disjoint, connected, and pairwise adjacent.  The anchors are
contacted by both thin carriers; fullness supplies every packet incidence;
`XY` is an edge; and `T` is a triangle.  This verifies the label-free
triangle-transversal lemma and the first branch of the funnel.

In the double-triangle setting, avoiding this model forces the two singleton
defects to be distinct and to lie in different triangles.  Suppose
`D(X)={a}` with `a in A` and `a` has a boundary neighbour `c outside A`.
Because `X` misses only `a`, it contacts `c`, so `X union {c}` is connected;
the edge `ca` makes it adjacent to the last singleton of `A`.  The proof's
anchor choices exclude `A`, the other defect `b`, and `c`, leaving exactly
two anchors when `c!=b` and at least two when `c=b`.  Both enlarged thin
carriers contact them.  Reusing the seven bags above therefore gives every
one of the 21 `K_7` adjacencies.  Thus `a` is `A`-pure, and symmetry makes
the other defect `B`-pure.

No edge between `P_1` and `P_2` is assumed in any of these models; their
distinct literal anchors supply their adjacency.

## 4. Cutvertex grouping

The exact packet hypothesis and seven-connectivity imply `G[L]` is
connected.  If `w` is a cutvertex and `D` a component of `L-w`, then

```text
N_G(D) subseteq S union {w}.
```

The opposite rich shore remains outside `D union N_G(D)`, so
seven-connectivity gives `|N_S(D)|>=6`.  Every component therefore has
defect empty or a singleton and is adjacent to `w`.

With two components, one component and the union of the other with `w`
satisfy the crossed-pure theorem.  With at least three components, choose
the isolated component so that the other side contains either an empty-
defect component or two different singleton defects whenever possible; its
union is then `S`-full.  If all component defects are the same singleton,
both sides miss at most that one vertex.  In either situation the common
contact set contains all of `A` or all of `B`, giving the explicit triangle
model.  Hence only two components with distinct pure defects in different
triangles survive.

## 5. Moser scope

Use the disjoint triangles `A={1,2,6}` and `B={3,4,5}`, with `z=0`.  The
only triangle-to-triangle edge is `65`, while `z` sees `1,2,3,4`.  Every
vertex of both triangles consequently has a boundary neighbour outside its
own triangle.  Neither triangle contains a pure vertex.

The crossed-pure theorem therefore excludes every near-full adjacent split,
and the cutvertex corollary excludes a cutvertex.  If `|L|=2`, connectedness
and minimum degree seven make each singleton vertex contact at least six
boundary vertices, producing exactly such a split.  Thus `|L|!=2`.

A singleton thin shore has no cutvertex and no two-part split.  Dirac's
neighbourhood bound allows its Moser boundary.  The result is therefore

```text
no cutvertex, |L| != 2,
```

not 2-connectivity; `|L|=1` remains an explicit live case.

## 6. Width-five obstruction and verifier

For the displayed crossed-pure quotient over `2K_3 plus K_1`, every graph
edge occurs in at least one of the six listed decomposition bags.  For each
of the eleven vertices, the bags containing it induce a connected subtree
of the five listed tree edges.  The maximum bag order is six, so the
decomposition has width five.  Since `tw(K_7)=6` and treewidth is
minor-monotone, this host has no `K_7` minor.

The tree-decomposition conditions were checked independently by script.
The exhaustive deletion/contraction verifier also passed:

```text
tested_hosts=56
counterexamples=38
VERIFIED
```

Its recursion is exact: it starts with singleton connected branch sets,
merges only adjacent branch sets, permits deletion of unused sets, and tests
for seven pairwise adjacent current branch sets at every order at least
seven.  The 28 crossed-pure markings cover every disjoint-triangle/pure-pair
marking in the ten hard atlas orbits; swapping the two triangles merely
swaps the symmetric carriers `X,Y`.

## 7. Promoted scope

This package supplies a genuine adaptive closure theorem: any third partial
carrier satisfying Theorem 3.1 funds the exact demand-three state.  It also
reduces every adjacent near-full thin split to the crossed-pure pattern.
The explicit width-five host proves that static contact data cannot eliminate
that pattern.  The remaining work must obtain the third carrier from internal
shore geometry or a proper-minor transition, and must handle the singleton
Moser thin shore separately.
