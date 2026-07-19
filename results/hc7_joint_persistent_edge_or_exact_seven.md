# Jointly persistent incident edges or an exact order-seven separation

**Status:** written proof; separate internal audit GREEN in
[`hc7_joint_persistent_edge_or_exact_seven_audit.md`](hc7_joint_persistent_edge_or_exact_seven_audit.md).

The rooted persistence theorem gives at least two incident edges which can
be deleted separately while preserving one spanning labelled
`K_7`-minus-one-edge model.  In the common-label case, either two such
edges can be deleted simultaneously, or the rooted branch set is a single
degree-seven vertex.  The latter outcome gives an actual order-seven
separation.

## Theorem

Let `G` be a seven-connected graph with no `K_7` minor, and let
`F=K_7-e`.  Let

\[
                         \mathcal M=(B_y:y\in V(F))             \tag{1}
\]

be a spanning labelled `F`-model.  Fix a label `r` which is not an end of
the missing edge of `F`, a vertex `v\in B_r`, a required neighbour label
`a`, and a vertex `x` such that

\[
                         B_a=\{x\},\qquad xv\in E(G).           \tag{2}
\]

Among all spanning labelled `F`-models satisfying (2) and retaining `v`
in the branch set with label `r`, choose `\mathcal M` so that

\[
                                 R=B_r
\]

has minimum order.  Then one of the following holds.

1. There are two distinct edges incident with `v` whose simultaneous
   deletion leaves the same seven sets in (1) as a spanning labelled
   `F`-model.
2. `R=\{v\}`, `d_G(v)=7`, and `N_G(v)` is the boundary of an actual
   order-seven separation whose two open sides are nonempty.

## Proof

Call an incident edge **persistent** if deleting it alone leaves the same
branch sets in (1) as a spanning labelled `F`-model.  Since `r` is
adjacent in `F` to all six foreign labels, the protected rooted persistence
theorem gives at least two persistent edges incident with `v`.

We first group these edges according to the part of the model whose
connectivity or required adjacency supports their persistence.

Let `Z_1,\ldots,Z_k` be the components of `G[R]-v`, and let `q_i` be the
number of `v-Z_i` edges.  An internal edge from `v` to `Z_i` is persistent
exactly when `q_i>=2`; in that event all `q_i` such edges are persistent.
These edges form the **internal support class** belonging to `Z_i`.

A persistent edge from `v` to a foreign branch set `B_y` belongs to the
**external support class** labelled by `y`.  Its persistence means that
some other edge still joins `R` to `B_y` after it is deleted.

Two persistent incident edges in different support classes are jointly
persistent.  Indeed, deleting edges belonging to two different internal
classes leaves at least one `v-Z_i` edge in each affected component;
deleting an internal and an external edge independently preserves the
connectivity of `R` and the relevant foreign adjacency; and deleting
external edges of two different labels leaves the required adjacency at
each label because each deletion separately has a second realizing edge.

Furthermore, any support class containing at least three persistent
incident edges contains a jointly persistent pair.  For an internal class,
one may delete any two of its at least three `v-Z_i` edges and retain a
third.  For an external class, deleting any two leaves the third edge from
`v` to the same foreign branch set and hence retains that required
adjacency.

Assume that outcome 1 fails.  All persistent incident edges therefore lie
in one support class, and there are exactly two of them.  Put `p=2`.

We use the notation from the rooted persistence count.  Let `k_0` be the
number of components `Z_i` with `q_i=1`, let `k_1` be the number with
`q_i>=2`, let `\ell` be the number of nonpersistent edges from `v` to
foreign branch sets, and let `q` be the number of foreign labels receiving
a persistent edge from `v`.  Minimality of `R`, with the protected
singleton fixed, gives

\[
                     2(k_0+k_1)+\ell+q\le6,                    \tag{3}
\]

and spanning gives the exact degree identity

\[
                              d_G(v)=k_0+\ell+p.                 \tag{4}
\]

Suppose first that the unique support class is internal.  Then `k_1=1`,
`q=0`, and (3) gives

\[
                              2k_0+\ell\le4.
\]

Together with (4) and `p=2`, this yields

\[
                              d_G(v)=k_0+\ell+2\le6,
\]

contrary to seven-connectivity.

The unique support class is therefore external.  In this case `k_1=0`
and `q=1`.  Equations (3)--(4), together with `d_G(v)>=7`, give

\[
                       2k_0+\ell\le5,
             \qquad    k_0+\ell+2\ge7.                          \tag{5}
\]

The two inequalities force

\[
                              k_0=0,\qquad \ell=5,
             \qquad          d_G(v)=7.                          \tag{6}
\]

Since `k_0=k_1=0`, the graph `G[R]-v` has no component, and hence
`R=\{v\}`.  The unique external support class consists of exactly two
edges from `R` to its foreign branch set: a third such edge would also be
persistent and would contradict `p=2`.

It remains to verify that the seven neighbours of `v` form an actual
separator.  There is a vertex outside `N_G[v]`.  Otherwise
`V(G)=N_G[v]` has eight vertices; seven-connectivity then gives minimum
degree at least seven, so `G=K_8`, contrary to the exclusion of a `K_7`
minor.  Thus deleting the seven-set `N_G(v)` leaves the singleton component
`\{v\}` and a nonempty set outside `N_G[v]`, with no edge between them.
Consequently `N_G(v)` is the boundary of an actual order-seven separation
with two nonempty open sides.  This proves outcome 2. \(\square\)

## Exact scope

Outcome 1 preserves the labelled near-complete minor model after deleting
both edges, but it does not produce a six-colouring of that two-edge
deletion or align any boundary equality partition.  Outcome 2 gives a
literal order-seven separator, but it does not synchronize the colourings
of its two closed shores.  The theorem therefore advances the edge/model
alignment step without by itself closing the exact-seven colour-gluing
problem or proving `HC_7`.

## Dependency

- [Rooted incident-edge persistence with a protected singleton](hc7_rooted_persistent_model_edge.md), especially Theorem 2.2 and the label count in its proof.
