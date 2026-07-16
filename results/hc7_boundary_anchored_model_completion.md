# Completing a small rooted model across an eight-vertex separation

**Status:** written proof with a separate GREEN internal audit in
[`hc7_boundary_anchored_model_completion_audit.md`](hc7_boundary_anchored_model_completion_audit.md).
The main lemma is a uniform linkage-and-minor construction.  Its corollary
reduces the endpoint-rigid Gallai--Edmonds residue to models which genuinely
use both open shores.  This does not prove `HC_7`.

## 1. Boundary-anchor completion

### Theorem 1.1

Let `G` be a seven-connected graph.  Let `S` be an eight-vertex separator
such that `G-S` has exactly two components `U,V`.  Assume that `V` is
adjacent to every vertex of `S`, and let `s\in S` be adjacent to every
vertex of `S-\{s\}`.

Suppose `G-s` contains a `K_5`-minor model `\mathcal M` supported on at
most six vertices, and suppose its support is disjoint from `V`.  Then `G`
contains a `K_7` minor.

### Proof

Write the five branch sets of `\mathcal M` as

\[
                         M_1,\ldots,M_5
\]

and put `m=|\bigcup_i M_i|\le6`.  If every branch set meets `S`, then

\[
                         M_1,\ldots,M_5,\quad V,\quad\{s\}
                                                               \tag{1.1}
\]

are already seven pairwise adjacent connected branch sets: `V` is adjacent
to each `M_i` through a boundary vertex in that branch set, `s` is adjacent
to the same boundary vertex, and `V` is adjacent to `s` by boundary
fullness.

It remains to anchor the branch sets disjoint from `S`.  Let

\[
       \mathcal I=\{i:M_i\cap S=\varnothing\},
       \qquad h=|\mathcal I|.                            \tag{1.2}
\]

The preceding paragraph handles `h=0`, so assume `h\ge1`.  Since the
model avoids `V`, every `M_i` with `i\in\mathcal I` lies in `U`.  Choose
one vertex `a_i\in M_i` for every such `i` and put

\[
       A=\{a_i:i\in\mathcal I\},\qquad
       Z=\left(\bigcup_iM_i-A\right)\cup\{s\},
       \qquad
       T=S-\left(\{s\}\cup\bigcup_iM_i\right).         \tag{1.3}
\]

The sets `A,T,Z` are pairwise disjoint.  Moreover

\[
                     |Z|=m-h+1\le7-h.                  \tag{1.4}
\]

If `b=|S\cap\bigcup_iM_i|`, then every branch set outside `\mathcal I`
contains a boundary vertex, while a branch set in `\mathcal I` contains
none.  In particular `b\le m-h`, and hence

\[
                     |T|=7-b\ge7-m+h\ge h+1.           \tag{1.5}
\]

We claim that `G-Z` contains `h` pairwise vertex-disjoint `A`--`T` paths.
If not, the set form of Menger's theorem supplies a set `X` of order at
most `h-1` separating `A` from `T` in `G-Z`.  Since `|A|=h` and
`|T|\ge h+1`, at least one vertex of each set remains after deleting `X`.
Thus `Z\cup X` separates two nonempty parts of `G`, whereas

\[
                     |Z\cup X|\le(7-h)+(h-1)=6,        \tag{1.6}
\]

contrary to seven-connectivity.  The claimed paths therefore exist.
They use every vertex of `A` and have distinct terminal vertices in `T`.

For each path, stop it on its first visit to `S`.  Its first boundary
vertex belongs to `T`: the vertex `s` and every boundary vertex already
used by the model belong to `Z`.  Before that first visit the path remains
inside `U`, because it starts in `U` and `U,V` are distinct components of
`G-S`.  We have therefore obtained pairwise disjoint paths

\[
                         P_i:a_i\longrightarrow t_i
                         \quad(i\in\mathcal I),         \tag{1.7}
\]

whose internal vertices lie in `U-\bigcup_jM_j` and whose distinct ends
`t_i` lie in `T`.

Replace `M_i` by `M_i\cup P_i` for `i\in\mathcal I`.  These enlarged
branch sets remain connected, pairwise disjoint, and pairwise adjacent,
and now every one of the five branch sets contains a vertex of `S-\{s\}`.
Consequently the seven sets in (1.1), with these replacements, are
pairwise adjacent.  They form a `K_7`-minor model in `G`.  \(\square\)

### Remark 1.2

The proof is label-preserving: it never changes which of the five original
branch sets a model vertex belongs to.  Its only use of seven-connectivity
is the exact budget

\[
          (\text{deleted model vertices and }s)
          +(\text{failed-linkage separator})\le6.
\]

Thus it is a rooted-model principle rather than a finite boundary census.

## 2. Consequence for the endpoint-rigid Gallai--Edmonds residue

The following corollary uses the normalization proved in the companion
Gallai--Edmonds reduction.  It is stated separately so that Theorem 1.1
does not depend on that special boundary graph.

### Corollary 2.1 (only a two-shore support-six model can survive)

Assume the hypotheses of Theorem 1.1 and additionally:

1. `G` is `K_7`-minor-free;
2. `U`, as well as `V`, is adjacent to every vertex of `S`;
3. there is a second vertex `x\in S-\{s\}` such that every two-vertex set
   `P` satisfies `\mu_G(P)\le6`, where `\mu_G(P)` is the minimum support
   order of a `K_5`-minor model in `G-P` (and is infinity if no such model
   exists);
4. for `B=S-\{s,x\}`, contracting the two components `U,V` in
   `G-\{s,x\}` produces `I_2\vee G[B]`, and this quotient has no
   `K_5`-minor model supported on at most six vertices.

Then `\mu_G(\{s,x\})=6`.  Every minimum `K_5`-minor model in
`G-\{s,x\}` has the following form after possibly interchanging `U,V`.

There is an integer `h\in\{2,3\}` such that its branch sets are

\[
       \{u_1\},\ldots,\{u_h\},
       \quad\{w_1\},\ldots,\{w_{4-h}\},
       \quad\{v,t\},                                   \tag{2.1}
\]

where

\[
       u_i\in U,qquad v\in V,qquad
       t,w_j\in B.                                     \tag{2.2}
\]

The vertices `u_1,\ldots,u_h,w_1,\ldots,w_{4-h}` form a clique;
`t` is adjacent to every `u_i`; and `t` is nonadjacent to at least one
`w_j`, whose adjacency to the edge branch set is therefore supplied by
`v`.

For `z\in\{v,t\}`, let `D_z` be the set of the four singleton-model
vertices not adjacent to `z`.

Equivalently, relative to the four singleton branch sets, the edge
`vt` has one of the following complementary-defect patterns:

\[
          (|D_v|,|D_t|,4-|D_v\cup D_t|)
          \in\{(3,1,0),(2,1,1),(2,2,0)\},              \tag{2.3}
\]

where every `u_i` belongs to `D_v` and at least one `w_j` belongs to
`D_t`.

### Proof

By assumption 3, let `\mathcal N` be an arbitrary minimum `K_5` model in
`G-\{s,x\}`; it is supported on at most six vertices.  If each of `U,V`
met at most one branch set of
`\mathcal N`, enlarge that branch set to contain the rest of the
corresponding connected shore and contract the two shores.  This would
give a support-at-most-six `K_5` model in `I_2\vee G[B]`, contrary to
assumption 4.  Hence one shore, say `U`, meets at least two distinct branch
sets.

If the model avoided `V`, Theorem 1.1 (applied to `s`, and noting that the
model also avoids `s`) would give a `K_7` minor.  This application remains
valid after interchanging `U,V`, because assumption 2 makes both shores
adjacent to every boundary vertex.  Thus the model meets both open shores.

A five-vertex support would make every branch set a singleton.  A
singleton in `U` is nonadjacent to a singleton in `V`, so such a model
cannot meet both shores.  Therefore the minimum support has order six and
`\mu_G(\{s,x\})=6`.  Its branch-set orders are `2,1,1,1,1`.

Among two distinct branch sets meeting `U`, at least one is a singleton
`{u\}`.  Any branch set meeting `V` must be adjacent to `u`.  Since
there is no `U`--`V` edge, that branch set must be the unique two-vertex
branch set and must have the form `\{v,t\}` with `v\in V` and `t\in S`.
It is the only branch set meeting `V`.  All branch sets meeting `U` are
therefore singleton vertices, and every remaining singleton branch set
lies in `S`.  The model avoids `s,x`, so all of its boundary vertices lie
in `B`.  This proves (2.1)--(2.2), except for the value of `h`.

Certainly `2\le h\le4`.  If `h=4`, adjacency of the edge branch set to
each `u_i` must be supplied by `t`, because `v` has no neighbour in `U`.
Then `\{t,u_1,u_2,u_3,u_4\}` is a literal `K_5` in
`G-\{s,x\}`, contradicting the already proved equality
`\mu_G(\{s,x\})=6`.  Hence `h\in\{2,3\}`.

The four singleton branch sets form a clique.  The same no-`U`--`V`
observation gives `tu_i\in E(G)` for every `i`.  If `t` were adjacent to
every `w_j`, then `t` together with all four singleton vertices would
again be a literal `K_5` avoiding `\{s,x\}`.  Thus `t` misses at least one
`w_j`; model adjacency forces `vw_j\in E(G)` for every such missed vertex.

Finally, `v` misses every `u_i`, while `t` meets every `u_i`; moreover
`D_v\cap D_t=\varnothing` because the edge branch set is adjacent to each
singleton branch set.  For `h=3`, the unique `w_j` is missed by `t` and
met by `v`, giving `(3,1,0)`.  For `h=2`, if `t` misses both `w_j` the
triple is `(2,2,0)`.  If `t` misses exactly one `w_j`, then `v` meets that
vertex and may meet or miss the other, giving `(2,1,1)` or `(3,1,0)`.
This is exactly the list in (2.3).  \(\square\)

## 3. Exact remaining step

The endpoint-rigid Gallai--Edmonds reduction supplies assumptions 1, 2,
and 4
of Corollary 2.1 with `s` the universal boundary vertex and `G[B]` the
six-vertex theta graph.  Global maximality at support height six supplies
assumption 3.  Consequently the no-perfect-matching order-eight branch no
longer permits an arbitrary regenerated model: it permits only the three
mixed-shore patterns in (2.3).

Closing those patterns requires using the placement of `t,w_j` on the
theta graph and the vertex-level structure of `V-v`.  Replacing `V-v` by
one universal quotient vertex is not legitimate, and the theorem makes no
such replacement.  The remaining target is a simultaneous boundary-anchor
linkage which either leaves a connected subgraph of `V-v` adjacent to the
five anchored branch sets or exposes an actual order-seven separation.
