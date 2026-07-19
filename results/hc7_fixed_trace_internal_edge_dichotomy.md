# Internal edges in a fixed boundary-trace list obstruction

**Status:** written proof; separate internal audit GREEN in
[`hc7_fixed_trace_internal_edge_dichotomy_audit.md`](hc7_fixed_trace_internal_edge_dichotomy_audit.md).
This theorem
gives a fixed-trace dichotomy for every edge of the shore-filling two-root
list-critical graph.  It either lowers the list-degree excess after that
single edge deletion or supplies a fixed-trace Kempe certificate.  The
edge-deleted graph is not another counterexample, so the first alternative
is a normalization, not a recursive proof of `HC_7`.

## 1. Setting

Use the complete shore-filling setting and notation of the audited
[special two-edge list-critical reduction](hc7_special_exact7_two_edge_list_core.md).
Thus

\[
 V(G)=A\mathbin{\dot\cup}Y\mathbin{\dot\cup}B,
 \qquad |Y|=7,
 \qquad E_G(A,B)=\varnothing,
\tag{1.1}
\]

`G` is seven-connected, seven-chromatic, `K_7`-minor-free, every proper
minor of `G` is six-colourable, and the special five-plus-two exact-seven
interface and its two entrance edges have already been obtained.  A fixed
proper colouring `psi` of `G[B union Y]`, obtained from the double
contraction of those entrance edges, induces the boundary partition `Pi`.
Its boundary colours define lists

\[
 \mathcal L(v)=[6]\setminus
 \{\psi(y):y\in N_G(v)\cap Y\}
 \qquad(v\in A).
\tag{1.2}
\]

The graph `G[A]` is connected and vertex-minimal non-`mathcal L`-colourable.
Put

\[
 E=\sum_{v\in A}\bigl(d_{G[A]}(v)-|\mathcal L(v)|\bigr).
\tag{1.3}
\]

Let `nu_B` be the maximum number of pairwise disjoint connected subgraphs
of `B` adjacent to every vertex of `Y`.

## 2. The edge dichotomy

### Theorem 2.1

For every edge `f=uv` of `G[A]`, exactly one of the following alternatives
holds.

1. **The fixed list obstruction survives.**  The graph `G[A]-f` is
   connected and vertex-minimal non-`mathcal L`-colourable, and its total
   list-degree excess is `E-2`.  Every six-colouring of `G-f` induces on
   `Y` a partition `Omega ne Pi` which extends through `G[B union Y]` but
   not through the original closed shore `G[A union Y]`.  Consequently
   `Omega` has full-subgraph demand greater than `nu_B` and satisfies the
   transported-partition Hall deficiency for every displayed auxiliary
   support family to which the reflection theorem applies.

2. **The edge is locked by the fixed trace.**  The graph `G[A]-f` is
   `mathcal L`-colourable.  Such a colouring glues to `psi` and gives a
   six-colouring of `G-f` inducing exactly `Pi` on `Y`.  It gives `u,v` a
   common colour `alpha`.  For every `beta ne alpha`, inside
   `G[A union Y]-f` either

   - one `alpha`--`beta` component contains both `u,v`, and hence contains
     a literal `u`--`v` path; or
   - the two endpoint components are distinct and give vertex-disjoint
     first-hit paths from `u,v` to two distinct literal vertices of `Y`,
     with all internal vertices in `A`.

#### Proof

Suppose first that `G[A]-f` is not `mathcal L`-colourable.  Every proper
induced subgraph is `mathcal L`-colourable because the corresponding proper
induced subgraph of `G[A]` is.  If `G[A]-f` were disconnected, its
components would be proper induced subgraphs of `G[A]` and their list
colourings would combine, a contradiction.  It is therefore connected and
vertex-minimal.  Deleting `f` lowers its degree sum by two without changing
the lists, so its total excess is `E-2`.

Let `c` be a six-colouring of `G-f`.  Its boundary partition `Omega`
extends through `G[B union Y]`.  If it extended through the original graph
`G[A union Y]`, the two closed-shore colourings could be aligned on their
exact boundary blocks and glued to colour `G`.  Hence the original
`A`-shore rejects `Omega`.

If `Omega=Pi`, permute the six colour names of `c` so that its boundary
assignment agrees with `psi`.  The restriction to `A` would then be an
`mathcal L`-colouring of `G[A]-f`, contrary to the present case.  Thus
`Omega ne Pi`.  Orient the exact full-subgraph reflection theorem from `B`
toward `A`.  If `Omega` had demand at most `nu_B`, the chosen `nu_B`
disjoint boundary-full subgraphs in `B` would reproduce `Omega` through the
intact closed `A`-shore and six-colour `G`.  Thus its demand is greater than
`nu_B`.  More generally, for every auxiliary support family allowed by the
transported-partition Hall theorem, a saturating matching would give the
same forbidden reflection.  Hall's theorem therefore supplies its stated
deficient block family.

Suppose instead that `G[A]-f` has an `mathcal L`-colouring `lambda`.  It
glues to `psi` on `G[B union Y]`, producing a six-colouring of `G-f` with
boundary partition `Pi`.  Necessarily `lambda(u)=lambda(v)=alpha`; otherwise
restoring `f` would six-colour `G`.

Fix `beta ne alpha` and consider the `alpha`--`beta` components in the
properly coloured graph `G[A union Y]-f`.  If the endpoint component is
common, it contains the asserted path.  Otherwise neither endpoint
component can avoid `Y`: interchanging `alpha,beta` on such a component
would preserve the boundary assignment, give the ends of `f` different
colours, and allow `f` to be restored.  Both components therefore meet
`Y`.  Shortest paths to their first boundary vertices have internal
vertices in `A`; the paths and their boundary ends are distinct because
the two components are disjoint.  This proves alternative 2.  The two
alternatives are exhaustive and exclusive.  \(\square\)

### Proposition 2.2 (deletion and contraction give the same response)

For an edge `f=uv` of `G`, identifying `u,v` while retaining their common
colour gives a bijection between the six-colourings of `G-f` and those of
`G/f`.  In particular, the two operations induce exactly the same family
of boundary partitions on every boundary disjoint from `{u,v}`.

#### Proof

Every six-colouring of `G-f` gives `u,v` the same colour, since otherwise
`f` could be restored.  It therefore factors through `G/f`.  Conversely a
colouring of `G/f` expands to a colouring of `G-f` with equal endpoint
colours.  \(\square\)

## 3. The all-locked normal form

### Corollary 3.1

If alternative 2 of Theorem 2.1 holds for every edge of `G[A]`, then
`G[A]` is both vertex-minimal and edge-minimal non-`mathcal L`-colourable.
Every proper subgraph is `mathcal L`-colourable, every internal edge has the
fixed-trace Kempe certificate in Theorem 2.1(2), and the subgraph induced by

\[
 \{v\in A:d_{G[A]}(v)=|\mathcal L(v)|\}
\tag{3.1}
\]

is a Gallai forest.

#### Proof

Vertex-minimality is part of the setting and edge-minimality is the
hypothesis.  A proper subgraph either omits a vertex, in which case it is a
subgraph of a colourable proper induced subgraph, or is spanning and omits
an edge, in which case it is a subgraph of `G[A]-f` for some missing edge
`f`.  The fixed-trace certificate is Theorem 2.1(2).  The Gallai-forest
conclusion is the standard degree-choosability argument for the tight
vertices of a vertex-minimal list obstruction.  \(\square\)

## 4. Exact scope

Alternative 1 lowers an exact scalar for one edge-deleted fixed-list
obstruction, but it does not produce another seven-chromatic minor-minimal
host and cannot be iterated as an `HC_7` induction without additional
state-preserving geometry.  Proposition 2.2 shows that deleting and
contracting the same edge cannot provide two independent responses.

The all-locked branch can have unbounded excess under the local list data.
The wheel family is the simplest example; the separate
[six-spoke boundary completion](hc7_six_spoke_boundary_completion.md)
eliminates that entire family under the actual host degree and opposite-
shore hypotheses.  The remaining theorem must use `K_7`-minor exclusion and
literal first-hit locations across different edges to construct a labelled
minor model, a compatible order-seven separation, or a genuinely smaller
host configuration.

## 5. Dependencies

- [special exact-seven two-edge list-critical reduction](hc7_special_exact7_two_edge_list_core.md)
- [adaptive exact-seven reflection](hc7_exact7_adaptive_packet_reflection.md)
- [transported-partition Hall reflection](hc7_transported_partition_hall_reflection.md)
- the degree-choosability theorem for list-critical graphs
