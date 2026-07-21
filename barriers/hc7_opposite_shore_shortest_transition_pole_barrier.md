# Every shortest exact-block transition can end at the pole

**Status:** barrier/counterexample to an intermediate proof mechanism;
written proof; [separately audited **GREEN**](hc7_opposite_shore_shortest_transition_pole_barrier_audit.md).  The graph
constructed below has a bounded order-eight interface, seven-connectivity,
chromatic number seven, the sharp degree-eight independence bound, complete
exact-independent-block responses on both closed shores, and a
six-colouring after deleting every independent set of edges from the pole
to the boundary.  Nevertheless every shortest exact-block transition is a
single six-block-to-five-block move using the colour of the pole.  No such
transition has a pole-free last interchange.

This is not a counterexample to the opposite-shore response lemma under the
full hypothetical-counterexample hypotheses or to `HC_7`: the construction
is not asserted to exclude a `K_7` minor or to have every proper minor
six-colourable.

## 1. Statement

There is a finite graph `G`, a vertex `u`, a component `C` of `G-N[u]`,
and a vertex `z` in

\[
                         S=N_G(C)\subseteq N(u)
\]

such that:

1. `G` is seven-connected and seven-chromatic;
2. `|S|=d_G(u)=8`, `N(u)=S`, and `alpha(G[S])=3=d_G(u)-5`;
3. both `C` and `{u}` are connected and adjacent to every vertex of `S`;
4. `chi(G-{u,z})=6`, and for every nonempty independent set `I` of
   `G[S]`, the graph

   \[
                         G-E_I,\qquad E_I=\{ui:i\in I\}, \tag{1.1}
   \]

   is six-colourable with `u union I` monochromatic; in particular, the
   edge-deleted graph `G-uz` is six-colourable;
5. for every such `I`, each intact closed shore has a proper six-colouring
   in which `I` is exactly one boundary colour class;
6. the two intact closed shores induce no common complete equality
   partition of `S`;
7. no component `D` of `G-N[u]` with `z in N(D)` has `|D|<|C|`; and
8. for every nonempty independent set `I`, every shortest exact-`I`
   boundary transition from a colouring extending through the `C`-shore
   to one extending through the `u`-shore has length one.  It changes a
   singleton boundary component from a colour occurring nowhere else on
   `S` into an already nonempty colour class.  Relative to the final
   opposite-shore extension, the disappearing colour is the unique colour
   of `u`.  Thus every last interchange is the single-vertex pole move.

The contracted static quotient of the two distinguished full pieces is
also target-free: delete the unused `D`-interior and contract `C`; together
with the singleton `u` this gives `\overline K_2 join G[S]`, which has
treewidth at most four and hence no `K_7` minor.

Thus the displayed local interface, all independent-block pole-star
responses, shortest-transition minimality, endpoint selection, and
seven-connectivity do not force a pole-free last transition.  A positive
proof must use global `K_7`-minor exclusion in the uncontracted host or
proper-minor six-colourability beyond the pole-star operations.

## 2. The boundary and its two extension languages

Let

\[
 S=X\mathbin{\dot\cup}Y\mathbin{\dot\cup}Z,
 \qquad |X|=|Y|=3,\quad |Z|=2,
\]

and put

\[
                         H=K_3[X]\mathbin{\dot\cup}
                           K_3[Y]\mathbin{\dot\cup}K_2[Z]. \tag{2.1}
\]

Then `chi(H)=alpha(H)=3`.  The graph is nonsplit: a clique lies in one
component, while the union of the other two nontrivial clique components
is not independent.  This is therefore inside the unresolved static
boundary class, and it meets the degree-eight contraction-critical bound
`alpha(H)<=3` with equality.

Let `mathcal L_r` be the equality partitions of `S` induced by proper
six-colourings of `H` which have exactly `r` nonempty blocks.  Use the
exact colouring-relation realization theorem to obtain two
`S`-boundaried graphs with exact extension relations

\[
               \mathcal R_C=\mathcal L_6,
 \qquad        \mathcal R_D=\mathcal L_5\cup\mathcal L_6. \tag{2.2}
\]

The relations mean all labelled colourings with the displayed equality
partitions, so they are invariant under permutations of the six colours.
Section 4 below shows that both relations contain a partition equating the
ends of every nonedge of `H`.  The realizers may consequently be chosen
with boundary induced graph exactly `H`.

Before applying the connected-full augmentation, add a disjoint `K_6` to
the `C`-realizer.  This does not change its boundary extension relation:
every six-colouring of the old realizer extends independently over the
clique, and every colouring of the enlarged graph restricts to the old
one.  The connected-full augmentation then attaches this new component to
the rest of that open interior while still preserving the relation.  Apply
the same augmentation to the `D`-realizer, and call the resulting connected
open interiors `C,D`.

Amplify every open vertex into an independent false-twin class of order at
least seven.  Use sufficiently larger classes on the `D` side that

\[
                              |D|\ge |C|.                \tag{2.3}
\]

Varying the class orders does not change the usual connectivity proof:
after deleting fewer than seven vertices every twin class has a survivor.
Nor does it change either exact extension relation.

Glue the two realizers along `S` and add one new vertex `u` with

\[
                              N_G(u)=S.                  \tag{2.4}
\]

There are no edges between `C` and `D`, and `u` has no neighbour in either
open interior.

## 3. Connectivity, chromatic number, and absence of descent

Before adding `u`, connectivity amplification makes the glued graph
seven-connected.  After adding `u`, deleting fewer than seven vertices
leaves the old graph connected and, if `u` survives, leaves at least two
of its eight neighbours.  Hence `G` remains seven-connected.

The closed `C`-shore accepts exactly `mathcal L_6`.  The `D`-realizer
accepts `mathcal L_5 union mathcal L_6`, but the added universal vertex
`u` can be coloured precisely when at least one of the six colours is
absent from `S`.  Consequently the intact opposite closed shore accepts
exactly

\[
                               \mathcal L_5.             \tag{3.1}
\]

The two intact shore languages are disjoint, so `G` is not six-colourable.
Section 4 gives a six-colouring of `G-uz`.  Recolouring `u` with a fresh
seventh colour gives a seven-colouring of `G`, and therefore

\[
                    \chi(G)=7,\qquad \chi(G-uz)=6.       \tag{3.2}
\]

The selected representatives of the six amplified clique classes induce a
`K_6` disjoint from `u,z`.  Deleting `u,z` from the six-colouring of
`G-uz` gives the reverse inequality, so

\[
                              \chi(G-\{u,z\})=6.          \tag{3.3}
\]

The same retained `K_6` proves the second equality in (3.2).

By (2.4), the components of `G-N[u]` are exactly `C,D`, and both have
neighbourhood `S`.  Thus both contain neighbours of the chosen `z`, while
(2.3) makes `C` minimum.  The aligned strict component-order restart is
absent.

Finally, delete `D` and contract `C`.  The image of `C` and the singleton
`u` are nonadjacent and each is complete to `S`, giving
`\overline K_2 join H`.  It has a tree decomposition whose three bags
consist of those two vertices together with one clique component of `H`.
Every bag has order at most five, so the quotient has treewidth at most
four and no `K_7` minor.

## 4. Exact five- and six-block responses

Every independent set `I` of `H` contains at most one vertex from each of
`X,Y,Z`; write `r=|I|`.

We first construct a five-block partition exact at `I` and having another
nonsingleton block `J` disjoint from `I`.

- If `r=3`, the five vertices outside `I` occupy the three clique
  components in sizes `2,2,1`.  Pair vertices from the two size-two
  components to form `J` and leave the other three vertices singleton.
- If `r=2`, all three clique components still have an unused vertex.
  Choose one from each as an independent three-set `J` and leave the other
  three vertices singleton.
- If `r=1`, choose an independent three-set `J` from the remaining
  vertices, then an independent pair from the vertices still remaining,
  and leave the last two vertices singleton.

Together with the block `I`, each construction has exactly five blocks.
Choose `x in J` and split `x` from `J` into a new singleton block.  This
gives a six-block partition exact at `I`.

These two partitions are adjacent in the exact-`I` boundary Kempe graph.
Give `J` one colour `beta` in the five-block partition and let `delta` be
the unused sixth colour.  The `beta`--`delta` boundary subgraph has every
vertex of `J` as a singleton component because `J` is independent.
Interchanging on `{x}` gives the six-block partition, and reversing that
move merges `{x}` back into `J`.

This proves that both `mathcal L_5` and `mathcal L_6` meet every exact
independent-block cylinder.  It also proves the equatability condition used
after (2.2), by applying the six-block construction with `I` equal to the
ends of any boundary nonedge.

There is a stronger proper-subgraph response.  Fix the six-block partition
exact at `I` and label the colour on `I` as `gamma`.  Both realizers accept
this boundary colouring.  Give `u` colour `gamma`.  Every edge from `u` to
`S-I` is proper, and precisely the edges `E_I` in (1.1) were deleted.
Thus the two realizer colourings and `u` glue to a proper six-colouring of
`G-E_I`, with `u union I` monochromatic.

## 5. Every shortest transition is a pole move

Fix a nonempty independent set `I`.  Section 4 supplies adjacent exact-`I`
states in `mathcal L_6` and `mathcal L_5`.  Therefore the minimum distance
between the two intact shore extension languages in the exact-`I` boundary
Kempe graph is one.  Every shortest transition has one interchange from a
six-block state `phi_0` to a five-block state `phi_1`.

In a proper colouring of the disjoint union of cliques (2.1), a connected
two-colour boundary component is either a singleton or an edge inside one
clique component.  Interchanging on an edge retains one vertex of each
colour and cannot change the number of nonempty boundary colours.  Since
the transition from `phi_0` to `phi_1` decreases that number, its operated
component must be a singleton `{x}`.

Write `delta=phi_0(x)` and `beta=phi_1(x)`.  The colour `delta` occurs
nowhere else in `phi_0`, since it disappears at `phi_1`; the colour `beta`
already occurs on another boundary vertex, since the number of blocks
decreases.  Thus the move merges the singleton `delta`-block `{x}` into a
nonsingleton independent `beta`-block.  The exact block `I` is fixed by the
transition, so `x` and its `beta`-block are disjoint from `I`.

The final boundary state uses exactly five of the six labelled colours.
In every extension through the opposite closed shore, the universal vertex
`u` is therefore forced to use the unique missing colour `delta`.  The last
interchange uses that colour and, in reverse, assigns `x` the colour of
`u`.  It is exactly the single-vertex pole move in the canonical
exact-block transition theorem.  This proves item 8 of Section 1 for every
shortest transition, not only for the adjacent pair constructed in
Section 4.

## 6. Exact scope and consequence

The construction realizes all static and pole-star data used by the
proposed tagged-family proof:

- the live boundary order, chromatic bound, nonsplit condition, and sharp
  independence bound;
- connected full shores and seven-connectivity;
- every exact independent-block response on both intact shores;
- every independent-block contraction/star-deletion colouring at `u`;
- the aligned response `G-uz`; and
- shortest exact-block transitions for every `I`.

Yet all canonical last moves are pole moves.  Endpoint-pair selection and
robust independent-triple escape concern the separately anchored failed
lifts arising from the colourings of `G-E_I`; they do not turn any of the
last moves above into a pole-free transition or place an anchored response
inside the same shortest transition.

The graph deliberately lacks the two global hypotheses which could break
this realization: it is not asserted to be `K_7`-minor-free, and proper
minors outside the pole-star family (1.1) are not asserted six-colourable.
The target-free contracted quotient does not substitute for minor exclusion
in the uncontracted realizers.  Thus this note does not refute the full
opposite-shore lemma.  It proves that lexicographic shortest-path surgery,
static exact-block attainability, all pole-star responses, and endpoint
set-system classification are insufficient without a new host-level
operation-coupling or terminal decoding theorem.

## 7. Inputs

- Exact colouring-relation realization and connectivity amplification are
  stated and proved for repository use in
  [`hc7_state_realization_barrier.md`](hc7_state_realization_barrier.md).
  Its external input is Z. Dvořák and J. Swart, *A note on extendable sets
  of colorings and rooted minors*, arXiv:2504.07764, Theorem 3.
- The canonical pole-move alternative is Theorem 4.1 of
  [`../results/hc7_bounded_interface_exact_block_kempe_reduction.md`](../results/hc7_bounded_interface_exact_block_kempe_reduction.md).
