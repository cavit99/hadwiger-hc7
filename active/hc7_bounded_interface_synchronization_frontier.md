# Bounded-interface bridge composition

**Status:** general bounded-interface continuation.  Sections 1--3 summarize
separately audited results and the theorem in Section 4 remains open.  The
degree-seven branch has a stronger active formulation in
[`hc7_degree7_model_separator_frontier.md`](hc7_degree7_model_separator_frontier.md);
this file remains the degree-eight/nine continuation.  Nothing here proves
`HC_7`.

## 1. Uniform entry from every hypothetical counterexample

Let `G` be a hypothetical minor-minimal counterexample to `HC_7`.  There
exist a vertex `u`, a component `C` of `G-N[u]`, and

\[
 z\in S:=N_G(C)\subseteq N(u)
\]

such that

\[
 7\le d_G(u)\le9,
 \qquad 7\le |S|\le d_G(u),
 \qquad \chi(G-\{u,z\})=6.                       \tag{1.1}
\]

Put

\[
 A=G[C\cup S],\qquad B=G-C.                     \tag{1.2}
\]

Then `(A,B)` is an actual separation.  The connected set `C` and the
singleton `{u}` are each adjacent to every boundary vertex.  Moreover,

\[
 \chi(G[S])\le4,
 \qquad \alpha(G[S])\le4,
 \qquad \overline K_2\vee G[S]
       \text{ has no }K_7\text{ minor}.           \tag{1.3}
\]

For every nonempty independent `I subseteq S`, both closed shores have a
six-colouring in which `I` is exactly one boundary colour class.

The edge `uz` gives a named asymmetric response.  Every six-colouring of
the edge deletion `G-uz` makes `u,z` monochromatic and induces on `A` an
exact singleton boundary block `{z}`.  That complete boundary partition
does not extend to the original shore `B`.

## 2. What static boundary information settles

If `G[S]` is split, the two shore colourings synchronize.  Indeed, for a
split partition `S=I dotunion Q` with `I` independent and `Q` a clique,
the cylinder having `I` as an exact block consists of the unique partition

\[
                         I\mid\{q\}\ (q\in Q).
\]

Both shores attain it, so their colours align and glue.  Hence every live
boundary is nonsplit.

This is the exact limit of the static argument.  For every nonsplit graph
`H` with `chi(H)<=4`, parity of the number of blocks splits all proper
six-colour partitions into two disjoint languages, each meeting every
exact-block cylinder.  These abstract languages need not arise from an
actual contraction-critical host, but they rule out any proof using only
independent-block attainability.

One additional infinite family is closed geometrically.  If the boundary
contains adjacent vertices `p,q` complete to a two-connected remainder
`X`, both open shores are connected and full to the boundary, and
`G-{p,q}` has a `K_5` minor, then a rooted-planarity argument gives an
explicit `K_7` minor.  Thus that branch requires no colour synchronization.

## 3. Forced pole-free paths

Fix `x in S`.  Begin with a six-colouring of the edge deletion `G-ux`;
the colour of `u=x` is an exact singleton colour on `S`.  Connect its
boundary colouring, inside that exact-singleton cylinder, to a boundary
colouring extending through `B`.  Four-degeneracy of `G[S-x]` and the
Las Vergnas--Meyniel theorem make this cylinder Kempe-connected.

Not every boundary interchange can lift to `G-ux`, or the final colouring
on `A` would glue to the chosen colouring on `B`.  The first failed lift
therefore gives a bichromatic path whose ends lie in distinct two-colour
components of `G[S]`, whose internal vertices avoid `S union {u,x}`, and
whose interior lies wholly in one open shore.

If it lies on the `u`-side, it meets at most three components `D` of
`G-N[u]` other than `C`, and each satisfies

\[
                         |N_G(D)\cap S|\ge |S|-2\ge5. \tag{3.1}
\]

This result holds for every `x in S`.  It converts arbitrary movement in
the boundary-colouring space into literal host paths with bounded contact
defect.

## 4. Primary open theorem

### Pole-free bridge composition theorem

Under the setup above, use the family of paths forced in Section 3 to
obtain at least one of:

1. an explicit `K_7`-minor model in `G`;
2. one equality partition of `S` induced by six-colourings of both `A`
   and `B`; or
3. another instance satisfying Sections 1--3 in the same graph, with a
   strictly smaller chosen anti-neighbourhood component and with the named
   edge-deletion boundary response preserved.

The third outcome must decrease the order of the literal connected
component in `G`; auxiliary path length, quotient size, or an unlabelled
minor model is not a valid rank.

The first two outcomes contradict the definition of `G`, while the third
permits finite descent.  A terminal singleton component is impossible:
in a six-colouring of the opposite shore, the colour of `u` is absent from
`S` and can be assigned to that one vertex, six-colouring `G`.  Hence this
theorem, together with the audited entry reduction, would prove `HC_7`.

## 5. Immediate constructive milestone

The next lemma should compose **two compatible failed Kempe lifts**.  For
two boundary vertices `x,y`, seek choices of their exact-singleton
transitions such that the two returned paths either

- have disjoint terminal pairs and can be split into labelled branch sets;
- use two different almost-full components on the `u`-side; or
- expose a connected residual piece whose full neighbourhood has order at
  most nine and is strictly smaller than `C`.

Failure must be recorded by literal first-hit vertices and the complete
boundary neighbourhood of a connected host subgraph.  A statement only
about equality partitions, colour names, or abstract path endpoints is
already defeated by the parity-language barriers.

## Dependencies and guardrails

- [bounded low-degree entry](../results/hc7_low_degree_adjacent_pair_alignment.md)
- [boundary-edge alignment](../results/hc7_low_degree_boundary_edge_alignment.md)
- [split-boundary synchronization](../results/hc7_split_boundary_synchronization.md)
- [exact-block Kempe reduction](../results/hc7_bounded_interface_exact_block_kempe_reduction.md)
- [two-connected boundary-core completion](../results/hc7_two_connected_boundary_completion.md)
- [four-colour parity-language barrier](../barriers/hc7_four_colour_parity_language_barrier.md)
- [eight-boundary state-transfer barrier](../barriers/hc7_eight_boundary_gallai_state_transfer_barrier.md)

Do not identify a colour class with a branch set without an explicit lift.
Do not treat a path as an extra branch set while simultaneously retaining
the connected shore containing it.  Any proper-minor operation must be
lifted back to the original fixed graph.
