# A pentagonal dynamic-language barrier at an exact seven-vertex boundary

**Status:** written finite combinatorial barrier; deterministic verification
script included; separately internally audited GREEN in the adjacent audit.

This note shows that the exceptional exact-seven boundary

\[
                         H=K_2\vee C_5
\]

does not force two oppositely oriented boundary-colouring response families
to intersect.  The obstruction survives every exact independent-set trace,
the strongest boundary condition supplied by deletion of a portal edge, and
equality of the deletion and contraction responses for each named edge.

The result is not a counterexample to `HC_7`.  Its graph realizations do not
simultaneously have global `K_7`-minor exclusion and the property that every
proper minor is six-colourable.  Those host-level hypotheses, together with
the five labelled branch sets in the active configuration, are exactly the
information not represented by the finite boundary language.

## 1. The ten equality partitions

Write

\[
 S=\{p,q\}\mathbin{\dot\cup}\{v_0,v_1,v_2,v_3,v_4\},
 \qquad H=G[S]=K_2\vee C_5,
\]

where `p,q` are the two universal adjacent vertices.  Relabel the five
cycle vertices so that the nonedges of `H` on them are

\[
                         e_i=v_iv_{i+1}\qquad(i\in\mathbb Z_5).       \tag{1.1}
\]

Thus the five `e_i` themselves form a cycle.

Let `Omega` be the equality partitions of `S` induced by proper
six-colourings of `H`.  Define:

* `s_i` to be the partition whose sole nonsingleton block is `e_i`; and
* `d_i` to be the partition whose two nonsingleton blocks are the two edges
  in the unique perfect matching of the path obtained from the cycle
  `(e_0,...,e_4)` by deleting `v_i`.

In particular, `d_i` has five blocks and leaves `v_i` as its only singleton
among the five cycle vertices.  Put

\[
              \mathcal S=\{s_i:i\in\mathbb Z_5\},\qquad
              \mathcal D=\{d_i:i\in\mathbb Z_5\}.                    \tag{1.2}
\]

### Lemma 1.1 (complete partition classification)

One has

\[
                         \Omega=\mathcal S\mathbin{\dot\cup}\mathcal D.
                                                                        \tag{1.3}
\]

The members of `mathcal S` have six blocks and the members of `mathcal D`
have five blocks.

#### Proof

The universal adjacent vertices `p,q` are distinct singleton blocks in
every proper partition.  A nonsingleton block on the other five vertices
is an edge of the complementary cycle (1.1), and the nonsingleton blocks
form a matching in that cycle.  At most six colours means at least one
matched edge.  A five-cycle has matching number two, five one-edge
matchings, and five two-edge matchings.  These give exactly (1.2).  QED.

## 2. Both parity families answer every contraction trace

For a nonempty independent set `I` of `H`, let

\[
       \mathcal T_I=\{\Pi\in\Omega:I\text{ is exactly one block of }\Pi\}.
                                                                        \tag{2.1}
\]

For a boundary vertex `x`, put

\[
       \mathcal U_x=\{\Pi\in\Omega:\{x\}\text{ is a singleton block of }
       \Pi\}.                                                          \tag{2.2}
\]

The cylinder `mathcal U_x` is the strongest equality-partition condition
which can be forced solely from deletion of a portal edge `ux` when the
open endpoint `u` is adjacent to every other boundary vertex: the deleted
edge must be monochromatic, so no other boundary neighbour of `u` may share
the colour of `x`.

### Theorem 2.1 (pentagonal parity obstruction)

The two disjoint families in (1.2) satisfy

\[
 \begin{aligned}
  \mathcal S\cap\mathcal T_I&\ne\varnothing,
  &\mathcal D\cap\mathcal T_I&\ne\varnothing
                       &&\text{for every nonempty independent }I,\\
  \mathcal S\cap\mathcal U_x&\ne\varnothing,
  &\mathcal D\cap\mathcal U_x&\ne\varnothing
                       &&\text{for every }x\in S.                     \tag{2.3}
 \end{aligned}
\]

Consequently all of the following finite requirements are consistent with
two disjoint opposite response languages on an exact seven-set:

1. every contraction of a connected full shore together with a nonempty
   independent boundary set returns a partition in the opposite language
   having that set as an exact colour class;
2. every single portal-edge deletion returns a partition in the opposite
   language in which its boundary endpoint is a singleton, even if its open
   endpoint meets all seven boundary vertices; and
3. the deletion and contraction response of each named edge are identical
   as labelled boundary partitions.

#### Proof

The only independent sets of `H` are singletons and the five pairs `e_i`.
Every state contains the singleton blocks `p,q`.  For a cycle vertex `v_i`,
the state `d_i` leaves it singleton, while any `s_j` whose edge is not
incident with `v_i` leaves it singleton.  For the pair `e_i`, the state
`s_i` contains that block, and either of the two size-two matchings which
contains `e_i` supplies a member of `mathcal D`.  This proves (2.3).

Assign responses to operations supported on one side from `mathcal D` and
responses to operations supported on the other side from `mathcal S`, using
the choices just displayed for exact-set and portal constraints.  Assign
the same response to deletion and contraction of each named edge.  Since
the requirements are existential operation by operation, these choices are
simultaneously consistent and the two response families remain disjoint.
QED.

The last sentence is deliberately a statement about the finite response
system.  It does not assert that arbitrarily chosen responses arise from a
single host colouring.  Section 4 identifies the exact graph-realization
boundary.

## 3. Sharp size and structure of a trace-complete language

Call `mathcal A subseteq Omega` **trace-complete** when it meets every
cylinder `mathcal T_I` from (2.1).

### Theorem 3.1 (minimum trace-complete families)

Every trace-complete family has at least three members.  Equality holds
exactly for the following five families.  For an edge `e_i=v_iv_{i+1}` of
the complementary cycle, take

\[
                        \{s_i,d_i,d_{i+1}\}.                           \tag{3.1}
\]

Here `d_i,d_{i+1}` are precisely the two edge-disjoint two-matchings whose
union is the other four edges of the complementary cycle.

Two minimum trace-complete families are disjoint exactly when their
defining complementary-cycle edges are vertex-disjoint.

#### Proof

It suffices first to cover the five two-vertex traces `e_i`.  A state `s_i`
covers one such trace and a state `d_i` covers two.  Two states cover at
most four, proving the lower bound.

If three states cover all five traces, their pair-block counts must be
`2,2,1`, with no repeated edge.  Indeed, three one-edge states or two
one-edge states and one two-edge state miss a pair trace.  Three two-edge
states can cover the five pair traces, but each leaves only its indexed
cycle vertex singleton, so three such states miss two singleton traces.
Thus the two two-matchings are edge-disjoint and the one-edge state uses the
remaining edge.  In a five-cycle, the two edge-disjoint two-matchings leaving
the edge `v_iv_{i+1}` are exactly the matchings which leave `v_i` and
`v_{i+1}` unmatched.  This gives (3.1).  The two endpoints are singleton in
the corresponding `d` states, and every other cycle vertex is singleton in
`s_i`; hence all singleton traces are also covered.

Finally, two families (3.1) share a `d` state exactly when their defining
edges share its unmatched endpoint.  Their `s` states are distinct unless
the defining edges are equal.  Thus they are disjoint exactly when the two
defining edges are vertex-disjoint.  QED.

This theorem gives a usable positive reduction: if host geometry bounds one
closed-shore extension language to three partitions, then its language is
one of the five explicitly labelled triples (3.1).  No such size bound is
currently proved in the active `HC_7` configuration.

### Corollary 3.2 (sharp host-level language bounds)

Let `G` be a graph which is not six-colourable and for which every proper
minor is six-colourable.  Suppose `G` has an actual order-seven separation
with boundary `S`, both open shores connected and `S`-full, and
`G[S]=K_2\vee C_5`.  If `mathcal E_L,mathcal E_R` are the equality-partition
languages of the two closed shores, then

\[
  3\le |\mathcal E_L|,|\mathcal E_R|\le7,
  \qquad |\mathcal E_L|+|\mathcal E_R|\le10.             \tag{3.2}
\]

If either language has order three, it is one of the five families (3.1).
If both have order three, their defining complementary-cycle edges are
vertex-disjoint and hence leave one uniquely determined cycle vertex outside
their four endpoints.

#### Proof

The languages are disjoint: a common equality partition permits a
permutation of the six colour names on one side followed by gluing.

Fix a nonempty independent set `I` of `G[S]`.  Contract the connected set
consisting of the left open shore together with `I`.  The opposite open
shore is nonempty, so this is a proper minor and has a six-colouring.  All
vertices of `I` receive the contracted vertex's colour.  Every vertex of
`S-I` is adjacent to the left shore and therefore to the contracted vertex,
so no such vertex receives that colour.  Restricting to the unchanged right
closed shore gives a member of `mathcal E_R` in which `I` is an exact block.
Interchanging the shores proves that `mathcal E_L` is also trace-complete.

Theorem 3.1 gives both lower bounds.  Lemma 1.1 gives ten available states,
and disjointness gives the sum and upper bounds.  The equality
classifications follow from Theorem 3.1 and its last sentence.  QED.

## 4. Graph realization and its exact limitation

The finite obstruction is graph-realizable in the standard bounded-boundary
sense.  The colouring-relation realization theorem of Dvořák--Swart
([Theorem 3 of *A note on extendable sets of colorings and rooted
minors*](https://arxiv.org/abs/2504.07764))
applied to `mathcal S` and `mathcal D` gives two finite `S`-boundaried
graphs with exactly those six-colour extension languages.  Both families
contain a state equating each nonedge of `H`, so the boundary can be made
induced by adding exactly the edges of `H`.  Gluing the realizers along `S`
is not six-colourable because their exact languages are disjoint.

The realization can be made elementary-minor-critical away from the fixed
boundary.  On each side repeatedly delete an open vertex or a nonboundary
edge whenever doing so preserves its exact language.  For every remaining
nonboundary edge `uv`, deletion creates a new proper boundary partition in
the opposite parity family.  In a colouring witnessing that new partition,
`u,v` have the same colour; otherwise the edge could be restored and the
partition would have belonged to the original language.  Hence both edge
deletion and edge contraction glue to the opposite side.  The identical
minimality argument handles deletion of every remaining open vertex.

Boundary operations can also be supplied without changing (1.3).  Before
adding the boundary edges, add to both realized relations, for every edge
`xy` of `H`, the six-block partition

\[
                \{\{x,y\}\}\cup\{\{z\}:z\in S-\{x,y\}\}.             \tag{4.1}
\]

Adding `H` filters all these common partitions.  Deleting or contracting
`xy` makes (4.1) available on both sides.  Deleting a boundary vertex `x`
also makes the restriction of (4.1), for any edge incident with `x`, a
common partition of `S-x`.  Thus one obtains an actual non-six-colourable
graph for which every elementary vertex deletion, edge deletion, and edge
contraction is six-colourable, while the two original exact-seven boundary
languages remain `mathcal S` and `mathcal D`.

In particular this graph is seven-chromatic: it is not six-colourable, and
after deleting any vertex the resulting six-colouring extends to a
seven-colouring by giving the deleted vertex a fresh colour.

This last property is **one-step** minor criticality.  It is not the much
stronger assertion that every proper minor is six-colourable: chromatic
number is not monotone under edge contraction, so later contractions of an
already six-colourable one-step minor need not remain six-colourable.

The construction also has separate standard strengthenings to connected
full shores and seven-connectivity by connected-full augmentation and
false-twin amplification, but those operations are not compatible with the
one-step minimality just used and introduce large clique minors.

Accordingly, a positive exact-seven collision theorem must use at least one
of the following genuinely host-level couplings:

1. every proper minor, not merely every elementary proper minor, is
   six-colourable;
2. global exclusion of a `K_7` minor;
3. the five labelled branch sets and literal contact witnesses of the
   near-`K_7` configuration; or
4. a theorem coupling responses to different operations, rather than
   choosing one witness independently for each operation.

The live hypothetical counterexample has all four.  The finite language and
the standard realization theorem do not encode any of them simultaneously.

## 5. Verification

Run:

```text
python3 barriers/hc7_exact7_pentagonal_dynamic_language_barrier_verify.py
```

The checker enumerates all set partitions of the seven labelled vertices,
filters the proper at-most-six-block partitions, verifies (1.3), checks all
trace and portal cylinders, and independently classifies the minimum
trace-complete families.

## 6. Dependencies

- [exact seven-vertex boundary classification](../results/hc7_exact7_no_rigid_trace.md)
- [oppositely oriented boundary responses](../results/hc7_rotation_opposite_boundary_responses.md)
- [uniform boundary-state realization barrier](hc7_state_realization_barrier.md)
