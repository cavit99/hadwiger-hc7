# Clique-model completion at the shifted order-eight boundary

**Status:** written proof with a separate GREEN internal audit in
[`hc7_shifted_boundary_completion_audit.md`](hc7_shifted_boundary_completion_audit.md).
The first theorem is a uniform rooted-model completion lemma.  The remaining
theorems apply it and two separate anchoring arguments to eliminate the
`HC_7` shifted-separator configuration.  This closes that conditional proof
branch; it does not by itself prove `HC_7`.

## 1. Two full components complete a compact clique model

### Theorem 1.1

Let `k>=3`, let `G` be a `k`-connected graph, and let `S` be a vertex set
of order `k+1`.  Let `C_1,C_2` be two distinct components of `G-S`, and
assume that each `C_i` has a neighbour at every vertex of `S`.

Suppose `G-(C_1 union C_2)` contains a `K_{k-2}`-minor model `M` whose
support has order at most `k-1`.  Then `G` contains a `K_k` minor.

### Proof

Write the branch sets of `M` as

\[
                         M_1,\ldots,M_{k-2}
\]

and let

\[
        I=\{i:M_i\cap S=\varnothing\},\qquad q=|I|.
\]

If `q>0`, choose one vertex `a_i in M_i` for every `i in I`, and put

\[
 A_0=\{a_i:i\in I\},\qquad
 Z=\left(\bigcup_{i=1}^{k-2}M_i\right)-A_0,
 \qquad
 T=S-\bigcup_{i=1}^{k-2}M_i.
\]

The support bound gives

\[
                         |Z|\le k-1-q.                 \tag{1.1}
\]

Every branch set indexed outside `I` contains at least one boundary
vertex.  Hence the number of boundary vertices in the model support is at
most `k-1-q`, and therefore

\[
                         |T|\ge q+2.                   \tag{1.2}
\]

There are `q` pairwise vertex-disjoint `A_0`--`T` paths in `G-Z`.
Otherwise, the set form of Menger's theorem gives an `A_0`--`T` separator
`X` in `G-Z` with `|X|<=q-1`.  Both terminal sets retain a vertex after
deleting `X`, while

\[
                         |Z\cup X|\le k-2,
\]

contrary to `k`-connectivity.

Choose such a linkage and shorten its paths so that each path has exactly
one end in `A_0`.  Stop every path on its first visit to `S`.  Its first
boundary vertex lies in `T`, because all boundary vertices already in the
model belong to `Z`.  Before that first visit the path remains in the
component of `G-S` containing its initial branch set.  In particular it
does not enter `C_1` or `C_2`, since the model is disjoint from those two
components.

Enlarge each `M_i`, for `i in I`, along its corresponding stopped path.
The resulting `K_{k-2}` model is still disjoint from `C_1 union C_2`, and
each of its branch sets now contains a vertex of `S`.  Its boundary
vertices are distinct, and at most `k-1` boundary vertices are used.
Choose two unused vertices

\[
                         z_1,z_2\in S.
\]

The following `k` sets are connected and pairwise disjoint:

\[
       M_1,\ldots,M_{k-2},\qquad
       C_1\cup\{z_1\},\qquad C_2\cup\{z_2\}.          \tag{1.3}
\]

Each of the last two sets is adjacent to every old branch set through the
boundary vertex in that branch set.  They are adjacent to one another
because `C_1` has a neighbour at `z_2` (and, symmetrically, `C_2` has a
neighbour at `z_1`).  Thus (1.3) is a `K_k`-minor model.

When `q=0`, the same argument starts after the linkage step: all old branch
sets already meet `S`, their support uses at most `k-1` boundary vertices,
and two unused vertices `z_1,z_2` still exist.  This completes the proof.
\(\square\)

### Remark 1.2

The proof preserves every branch-set label of the original model.  It uses
only the exact connectivity budget

\[
  (\text{model vertices deleted except for one root per unanchored row})
  +(\text{failed-linkage separator})\le k-2.
\]

It is therefore an unbounded completion theorem, not a finite boundary
enumeration.

## 2. Consequences for the shifted `HC_7` separator

Use the notation and hypotheses of
[`hc7_endpoint_rigid_mixed_shore_frontier_closed.md`](../archive/hc7_endpoint_rigid_mixed_shore_frontier_closed.md).
Thus `S` is the original eight-vertex separator, `V-v` is nonempty, and
every component of `V-v` has the same unique missed boundary vertex

\[
                        y\in\{s,w_1,\ldots,w_{4-h}\}. \tag{2.1}
\]

The old support-six `K_5` model has branch sets

\[
       \{u_1\},\ldots,\{u_h\},
       \quad\{w_1\},\ldots,\{w_{4-h}\},
       \quad\{v,t\},                                  \tag{2.2}
\]

where `u_i in U`, `v in V`, and `t,w_j in S-{s,x}`.  Every component of
`V-v` is adjacent to every vertex of

\[
                         \{v\}\cup(S-\{y\}).          \tag{2.3}
\]

### Theorem 2.1 (the open side is connected)

If `V-v` has at least two components, then `G` contains a `K_7` minor.
Consequently, in the `K_7`-minor-free residue, `V-v` is connected.

### Proof

Put

\[
                         T=\{v\}\cup(S-\{y\}).
\]

This set has order eight.  Its deletion separates every component of
`V-v` from the connected set `U\cup\{y\}`.  The model (2.2) is contained
in the latter closed side together with `T`, and is disjoint from every
component of `V-v`.

If `C_1,C_2` are two such components, both are adjacent to every vertex of
`T` by (2.3).  Apply Theorem 1.1 with `k=7`, boundary `T`, the support-six
`K_5` model (2.2), and components `C_1,C_2`.  It gives a `K_7` minor.
\(\square\)

### Theorem 2.2 (the common missed vertex is `s`)

If `y!=s`, then `G` contains a `K_7` minor.  Hence every `K_7`-minor-free
residue has

\[
                              y=s.                     \tag{2.4}
\]

### Proof

Assume `y!=s`.  By (2.1), `y` is one of the vertices `w_j`.  Let `C` be
any component of `V-v`, and put

\[
                              W=S-\{s,y\}.             \tag{2.5}
\]

The set `W` has order six.  Among the five branch sets in (2.2), let
`I` index those which do not meet `W`, put `q=|I|`, and select one vertex
`a_i` from every such branch set.  In this exact model, the unanchored
branch sets are the `h` singleton sets in `U` and the singleton set
`{y}`, so `q=h+1`; the argument below only needs the displayed definition
of `q`.

Let `M` be the six-vertex support of (2.2), and define

\[
 A_0=\{a_i:i\in I\},\qquad
 Z=(M-A_0)\cup\{s\},\qquad
 T_0=W-M.                                              \tag{2.6}
\]

Then

\[
                         |Z|=7-q,
 \qquad                  |T_0|\ge q.                  \tag{2.7}
\]

The second inequality follows because `|W|=6` and at most `6-q` vertices
of the model support lie outside `A_0`.

There are `q` pairwise vertex-disjoint `A_0`--`T_0` paths in `G-Z`.
Otherwise Menger's theorem supplies a separator `X` of order at most
`q-1`.  Since `|A_0|=q` and `|T_0|>=q`, both sides remain nonempty after
deleting `X`, whereas

\[
                         |Z\cup X|\le6,
\]

contrary to seven-connectivity.

As in Theorem 1.1, shorten the paths at their initial set and stop each on
its first visit to `W`.  These stopped paths do not enter `V-v`.  Indeed,
they start in `U\cup\{y\}`; there is no edge from `U` to `V`, every
component of `V-v` misses `y`, the vertex `v` belongs to `Z`, the vertex
`s` belongs to `Z`, and every possible remaining boundary entrance either
belongs to `Z` or is a terminal in `T_0`.

Enlarge the branch sets indexed by `I` along these paths.  All five
branch sets of the resulting `K_5` model now contain distinct vertices of
`W`.  They remain disjoint from `C` and from `s`.

The five enlarged branch sets, `C`, and `\{s\}` form a `K_7`-minor model.
The component `C` is adjacent to every old branch set through its boundary
vertex in `W`, because `C` misses only `y`.  The vertex `s` is adjacent to
every old branch set through the same boundary vertices, because `s` is
adjacent to every vertex of `S-\{s\}`.  Finally, `C` is adjacent to `s`,
again because its unique missed boundary vertex is `y!=s`.  This proves
the theorem. \(\square\)

### Theorem 2.3 (completion when the common missed vertex is `s`)

If `y=s`, then `G` contains a `K_7` minor.

### Proof

Put

\[
                              B_0=S-\{s\}.             \tag{2.8}
\]

Let `M` be the six-vertex support of the model (2.2), and put

\[
 A_0=\{u_1,\ldots,u_h\},\qquad
 Z=(M-A_0)\cup\{s\},\qquad T_0=B_0-M.                \tag{2.9}
\]

The set `Z` has order `7-h`.  The model meets `B_0` exactly in `t` and the
`4-h` vertices `w_j`, so

\[
                         |T_0|=h+2.                   \tag{2.10}
\]

There are `h` pairwise vertex-disjoint `A_0`--`T_0` paths in `G-Z`.
Otherwise Menger's theorem gives an `A_0`--`T_0` separator `X` in `G-Z`
with `|X|<=h-1`.  Both terminal sets retain a vertex after deleting `X`,
whereas

\[
                         |Z\cup X|\le6,
\]

contrary to seven-connectivity.

Shorten the paths at their initial set and stop each on its first visit to
`B_0`.  Before that first visit no path enters `V-v`.  Indeed, each path
starts in `U`; there is no edge from `U` to `V`; the vertex `v` belongs to
`Z`; and the only boundary vertex outside `B_0` is the deleted vertex `s`.

Enlarge every singleton branch set `\{u_i\}` along its stopped path.  The
five branch sets of the resulting `K_5` model contain five distinct
vertices of `B_0`: the `h` new terminals, the `4-h` vertices `w_j`, and
the vertex `t` in the branch set `\{v,t\}`.  Choose an unused vertex

\[
                              z\in B_0.                \tag{2.11}
\]

Let `C` be any component of `V-v`.  The following seven sets are connected
and pairwise disjoint:

\[
       M'_1,M'_2,M'_3,M'_4,M'_5,qquad
       C\cup\{z\},\qquad \{s\},                     \tag{2.12}
\]

where `M'_1,...,M'_5` denote the enlarged model branch sets.  For
completeness, all required adjacencies are as follows.

- The sets `M'_1,...,M'_5` remain pairwise adjacent because they are
  enlargements of the five branch sets of the old `K_5` model.
- The component `C` is adjacent to every vertex of `B_0`.  It is therefore
  adjacent to each `M'_i` through the selected boundary vertex in that
  branch set, and it has a neighbour at `z`, making `C\cup\{z\}`
  connected.
- The vertex `s` is adjacent to each `M'_i` through the same selected
  boundary vertex, since `s` is adjacent to every vertex of `B_0`.
- The edge `sz` joins `\{s\}` to `C\cup\{z\}`.

Thus (2.12) is an explicit `K_7`-minor model. \(\square\)

### Corollary 2.4 (elimination of the shifted boundary)

Under the shifted-separator hypotheses (2.1)--(2.3), `G` contains a
`K_7` minor.

### Proof

If `y!=s`, apply Theorem 2.2.  If `y=s`, apply Theorem 2.3.  These cases
exhaust (2.1). \(\square\)

Theorem 2.1 remains useful independently: it shows that the same compact
opposite model also eliminates any shifted boundary with two full
components before the common missed vertex is identified.  Theorems 2.2
and 2.3 are stronger in the present branch and close it without requiring
a colouring-state synchronization theorem.
