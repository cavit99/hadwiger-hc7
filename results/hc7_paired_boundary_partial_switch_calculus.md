# Partial Kempe switches at a paired exact-seven boundary

**Status:** written proof; separate internal audit GREEN in
[`hc7_paired_boundary_partial_switch_calculus_audit.md`](hc7_paired_boundary_partial_switch_calculus_audit.md).
This note classifies the
boundary partitions produced by every selected two-colour response in the
paired exact-seven form.  It rules out a response between the two exceptional
nonadjacent singleton blocks (and hence forces a lock for vertex-disjoint
critical edges) and gives exact demand tests for every other partial
footprint.  It also gives a nonsplit boundary showing that several surviving
footprints do not force a common partition by static boundary reasoning
alone.  It does not identify palette colours with minor-model branch sets or
prove `HC_7`.

## 1. Setting and the two-subgraph obstruction law

Let

\[
 V(G)=A\mathbin{\dot\cup}S\mathbin{\dot\cup}D,
 \qquad E_G(A,D)=\varnothing,
 \qquad |S|=7,                                         \tag{1.1}
\]

where `G` is seven-connected, has no `K_7` minor, is not six-colourable,
and every proper minor of `G` is six-colourable.  Put `H=G[S]`.  Suppose
`G[A\cup S]` has a proper six-colouring with equality partition

\[
 \Pi=M\mid\{x\}\mid\{y\}\mid\{k\}\ (k\in K),
 \qquad
 S=M\mathbin{\dot\cup}\{x,y\}\mathbin{\dot\cup}K,     \tag{1.2}
\]

where `M` is independent, `K` is a clique, `xy` is a nonedge, and

\[
                     (|M|,|K|)\in\{(2,3),(3,2)\}.       \tag{1.3}
\]

Assume that `A` contains two vertex-disjoint connected subgraphs, each
adjacent to every literal vertex of `S`.  For a proper partition `Omega`
of `S`, define

\[
 d_H(\Omega)=|\Omega|-
 \omega\bigl(H[\operatorname{sing}(\Omega)]\bigr).     \tag{1.4}
\]

The exact response-reflection theorem gives the obstruction law

\[
 \boxed{\text{if `Omega` extends through `A`, then }d_H(\Omega)>2.}
                                                               \tag{1.5}
\]

Indeed, when the demand is at most two, the two boundary-full connected
subgraphs form the required contraction supports.  A proper-minor
six-colouring then reflects `Omega` through the opposite closed shore and
the two shore colourings glue.

Assume also that we are in the common fixed-trace equality branch for two
distinct edges `e,f` of `G[D]`: a six-colouring `psi` of `G-{e,f}` agrees
with the displayed boundary colouring on `S`, makes the ends of each deleted
edge equal, and neither single-edge deletion has a six-colouring inducing
`Pi` on `S`.  A **selected response move** below means one of the endpoint
bichromatic-component switches from the disjoint-edge exposure theorem or
the incident-edge saturation-or-bypass theorem: it produces a proper
one-edge response and changes the equality partition on `S`.  Consequently
every partition produced by a selected response move extends through `A`
and obeys (1.5).  For vertex-disjoint `e,f`, every unlocked alternate colour
of either edge supplies such a move.

Write `Q=\{x,y\}\cup K` for the singleton vertices of `Pi`.  Since `K`
is a clique and `|Pi|-|K|=3`, the same obstruction law applied to `Pi`
itself gives the exact identity

\[
                  d_H(\Pi)=3,
                  \qquad \omega(H[Q])=|K|.             \tag{1.6}
\]

## 2. General two-block switch formula

Let `B,C` be two colour blocks of a proper boundary partition; allow
`C=\varnothing` when its palette colour is absent from `S`.  If a full
two-colour component has footprint

\[
                         B_0\subseteq B,\qquad C_0\subseteq C,
                                                               \tag{2.1}
\]

then switching it replaces `B,C` by the nonempty members of

\[
 B'=(B-B_0)\cup C_0,
 \qquad
 C'=(C-C_0)\cup B_0.                                  \tag{2.2}
\]

Both new sets are independent.  Moreover no edge of `H[B\cup C]` joins
`B_0\cup C_0` to its complement: otherwise the two boundary ends would
belong to the same full bichromatic component.

Conversely, every response switch at those two colours has exactly the
form (2.2).  It changes the equality partition precisely when the unordered
pair of nonempty sets in (2.2) differs from `{B,C}`.

## 3. Singleton pairs

### Theorem 3.1 (exact singleton-merge response criterion)

Let `u,v` be singleton blocks of `Pi`.  If `uv` is an edge, no selected
response move can use their two colours.  In particular, for vertex-disjoint
`e,f`, every selected critical edge is locked for those colours.  If `uv` is
a nonedge, every partition-changing switch merges the two blocks:

\[
                         \Omega=\Pi/uv.                \tag{3.1}
\]

Consequently such an unlocked response is possible only under the
following exact conditions.

1. If `(|M|,|K|)=(2,3)`, then

   \[
       \omega\bigl(H[(\{x,y\}\cup K)-\{u,v\}]\bigr)\le2. \tag{3.2}
   \]

2. If `(|M|,|K|)=(3,2)`, the two vertices in
   `(\{x,y\}\cup K)-\{u,v\}` are nonadjacent.          \tag{3.3}

In particular, for **both** paired forms, no selected response move uses the
colours of `{x}` and `{y}`.  For vertex-disjoint `e,f`, every selected
critical edge whose equality colour is the colour of `{x}` is therefore
locked against the colour of `{y}`, and symmetrically.

#### Proof

When `uv` is an edge, the graph on the two singleton blocks is connected.
A selected response move would have a nonempty proper footprint by the
fixed-trace exposure theorem, but a union of bichromatic components cannot
cut this boundary edge.  Hence no such move exists.  In the vertex-disjoint
case, an unlocked pair always supplies a selected move, so the edge is
locked.  Suppose `uv` is a nonedge.  A nontrivial footprint on two vertices
contains exactly one of them.  Formula (2.2) therefore replaces the two
singleton blocks by the single independent block `{u,v}`, proving (3.1).

In the `(2,3)` form, `Pi` has six blocks.  The merged partition has five
blocks and its singleton set is

\[
                         (\{x,y\}\cup K)-\{u,v\}.
\]

Obstruction law (1.5) says that five minus the clique number on this
three-set is greater than two, which is exactly (3.2).

In the `(3,2)` form, the merged partition has four blocks and exactly the
two complementary singleton vertices.  Inequality (1.5) says that their
clique number is at most one, which is (3.3).

Finally take `{u,v}={x,y}`.  In the first form the complementary set is
the triangle `K`; in the second it is the edge `K`.  Both violate the
necessary condition for an unlocked response.  Thus no selected response
move uses the `x`--`y` palette even though `xy` is absent from `H`; for
vertex-disjoint critical edges this says precisely that the palette is
locked. \(\square\)

This last exclusion is dynamic.  It is not forced by connectedness of
`H[{x,y}]`; it uses the two boundary-full connected subgraphs and
minor-critical response reflection.  For vertex-disjoint critical edges it
is exactly a new lock.

## 4. A singleton and the nonsingleton block

### Theorem 4.1 (exact partial-footprint demand)

Let `{u}` be one of the singleton blocks and switch its colour with the
colour of `M`.  Every partition-changing response has, for a unique proper
subset `W\subsetneq M`, the form

\[
 \Omega_W=
   (\Pi-\{M,\{u\}\})
   \cup
   \bigl(\{W,(M-W)\cup\{u\}\}\setminus\{\varnothing\}\bigr),
                                                               \tag{4.1}
\]

where `(M-W)\cup\{u\}` is independent.  Conversely every actual switch
has this form.  Put `Q=\{x,y\}\cup K`.  Then

\[
 d_H(\Omega_W)=
 \begin{cases}
  |\Pi|-1-\omega(H[Q-\{u\}]),&W=\varnothing,\\[2mm]
  |\Pi|-\omega(H[(Q-\{u\})\cup W]),&|W|=1,\\[2mm]
  |\Pi|-\omega(H[Q-\{u\}]),&2\le |W|<|M|.
 \end{cases}                                               \tag{4.2}
\]

Here in the middle line `W` is viewed as its unique singleton vertex.
Every actual unlocked response must make the corresponding quantity in
(4.2) greater than two.

#### Proof

Formula (2.2) partitions `M\cup\{u\}` into two independent colour
classes, exactly one of which contains `u`.  Name the other class `W`.
The case `W=M` reproduces the old two blocks and is not
partition-changing, so `W\subsetneq M`.  This proves (4.1).

If `W` is empty, the two old blocks merge, decreasing the block count by
one and deleting `u` from the singleton set.  If `|W|=1`, the block count
is unchanged and the unique member of `W` becomes a new singleton.  If
`2\le|W|<|M|`, both new blocks are nonsingletons and the only change to the
singleton set is deletion of `u`.  These are exactly the three lines of
(4.2).  Inequality (1.5) gives the final assertion. \(\square\)

For example, merging `M` with `x` or with `y` is always forbidden.  In
the `(2,3)` form the remaining singleton set contains the triangle `K`,
so the demand would be `5-3=2`.  In the `(3,2)` form it contains the edge
`K`, so the demand would be `4-2=2`.

## 5. The absent colour in the `(3,2)` form

There is one palette colour absent from `S` when `(|M|,|K|)=(3,2)`.
Switching it with a singleton-block colour cannot change the equality
partition: the only nonempty boundary footprint is the whole singleton.
Thus no selected response move uses those two colours; for vertex-disjoint
critical edges this forces a lock.

Switching the absent colour with the colour of `M` can change the
partition only by splitting

\[
                             M=W\mathbin{\dot\cup}(M-W),          \tag{5.1}
\]

where `W` is a nonempty proper subset.  One part has order one and the
other order two.  The resulting partition has six blocks and singleton
set `Q\cup\{m\}`, where `m` is the singleton part.  Therefore

\[
        d_H(\Omega)=6-\omega(H[Q\cup\{m\}])\ge3,        \tag{5.2}
\]

because `omega(H[Q])=2` and adjoining one vertex raises clique number by
at most one.  Hence the two-subgraph reflection test alone never excludes
this split of `M`.

## 6. Several partial footprints do not force static synchronization

The preceding restrictions are sharp at boundary level.  In the `(3,2)`
form let

\[
 M=\{m_1,m_2,m_3\},\qquad K=\{k_1,k_2\},               \tag{6.1}
\]

and let `H` have precisely the two edges

\[
                              k_1k_2,\qquad xm_1.       \tag{6.2}
\]

The partition `Pi` is proper and has demand

\[
                    5-\omega(H[\{x,y,k_1,k_2\}])=3.   \tag{6.3}
\]

The graph `H` is nonsplit: the vertices `k_1,k_2,x,m_1` induce `2K_2`.
For each of the four cross-pairs

\[
             xk_1, xk_2, yk_1, yk_2,                \tag{6.4}
\]

the pair and its complementary pair inside `\{x,y,k_1,k_2\}` are both
nonedges.  Thus every corresponding singleton merge passes the exact
test (3.3), and each resulting partition still has demand three.

Moreover the even- and odd-block partition languages of the split-boundary
synchronization theorem are disjoint and each meets every exact-block
cylinder on this nonsplit `H`.  The original five-block partition and the
four displayed four-block merges lie on opposite sides of that abstract
parity obstruction.  Consequently, even several admissible partial
footprints do not force a split boundary or a common shore partition from
boundary data alone.

This is an abstract boundary sharpness example, not a realization by the
two shores of a seven-connected contraction-critical host.  In particular
it says nothing against a positive theorem using the literal response
components, their first model-branch-set hits, or global `K_7`-minor
exclusion.  A connected subgraph adjacent to a prescribed part of the
boundary is open-shore geometry and cannot be inferred from `H` alone.

## 7. Exact remaining use

The paired boundary now forces three kinds of response behaviour without
enumerating boundary graphs:

1. connected two-block boundary graphs force locks;
2. every nonedge singleton pair satisfying the complementary-clique test
   either is locked or gives a demand-three merge; and
3. every partial `M`-switch has the explicit form and demand in (4.1)--(4.2).

In particular the exceptional `x`--`y` nonedge is no longer an unlocked
case.  The surviving partial footprints are exactly those whose new
partitions still have demand at least three.  The example in Section 6
shows that the next theorem must use their literal host paths: static
boundary adjacency, nonsplitness and multiplicity of transitions do not
force synchronization.

## 8. Dependencies

- [fixed-trace alternatives for repeated-exposure edges](hc7_repeated_exposure_fixed_trace_fork.md)
- [boundary-forced Kempe locks](hc7_paired_boundary_forced_kempe_locks.md)
- [exact selected-response preservation](hc7_exact7_selected_response_preservation.md)
- [adaptive reflection across an exact seven-separator](../results/hc7_exact7_adaptive_packet_reflection.md)
- [split-boundary synchronization](../results/hc7_split_boundary_synchronization.md)
