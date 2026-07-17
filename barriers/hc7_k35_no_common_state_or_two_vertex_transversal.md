# A seven-connected boundary-state obstruction with no two-vertex `K_5`-model transversal

## Status

**Written barrier theorem.**  This note strengthens the existing
`K_{3,5}` boundary-state realization barrier.  It is not a counterexample
to Hadwiger's Conjecture: the constructed graph contains a `K_7` minor and
is not asserted to be contraction-critical.

## Theorem

There is a finite graph `G` with a separation

\[
                 V(G)=L\mathbin{\dot\cup}S\mathbin{\dot\cup}R
\]

having all of the following properties.

1. `|S|=8`, `G[S]\cong K_{3,5}`, the open shores `L` and `R` are nonempty
   and connected, there is no `L`--`R` edge, and every vertex of `S` has
   a neighbour in each open shore.
2. `G` is seven-connected and `chi(G)=7`.
3. The two closed shores have no common equality partition on `S` induced
   by a proper six-colouring.
4. Each closed shore admits an exact trace for every nonempty independent
   set of `G[S]`.
5. There are two vertex-disjoint boundary edges `e,f` such that each of

   \[
      G-e,\quad G-f,\quad G-\{e,f\},\quad
      G/e,\quad G/f,\quad G/e/f
   \]

   is six-colourable.
6. Contracting the two open shores to two vertices gives
   `I_2\vee K_{3,5}=K_{2,3,5}`, which has no `K_7` minor.
7. No set of at most two vertices meets every `K_5`-minor model in `G`.
   Equivalently, for every `P\subseteq V(G)` with `|P|\le 2`, the graph
   `G-P` contains a `K_5` minor.

Consequently, even the alternative

\[
 \text{common proper boundary equality partition}
 \quad\text{or}\quad
 \text{two-vertex transversal of all `K_5`-minor models}
\]

does not follow from the static colouring data, full connected shores,
seven-connectivity, and named proper-minor responses in items 1--6.

## Proof

Start with the graph in
[`hc7_eight_boundary_gallai_state_transfer_barrier.md`](hc7_eight_boundary_gallai_state_transfer_barrier.md),
using the false-twin connectivity amplification with twin-class order
seven.  Sections 1--5 of that note prove items 1--6 above.  We prove the
new item 7.

Before amplification, the connected-full augmentation of either shore
contains an open-side edge: in its notation, for every boundary vertex
`x` it adds the path `x-l_x-c`, so `l_xc` is an edge with both ends in
the open shore.  Under false-twin amplification this edge is replaced by
a complete bipartite graph

\[
                            K_{7,7}                       \tag{1}
\]

on the two independent twin classes.  Fix one such copy and denote its
bipartition by

\[
              A=\{a_1,\ldots,a_7\},\qquad
              B=\{b_1,\ldots,b_7\}.
\]

Let `P\subseteq V(G)` have order at most two.  At most two vertices of
the fixed copy (1) are deleted.  Hence there are five undeleted vertices
`a_1,\ldots,a_5` in one bipartition class and five undeleted vertices
`b_1,\ldots,b_5` in the other, after relabelling.  Thus `G-P` contains a
subgraph isomorphic to `K_{5,5}`.

The following five disjoint connected sets form a `K_5`-minor model in
that `K_{5,5}`:

\[
       \{a_1,b_1\},\quad \{a_2,b_2\},\quad
       \{a_3,b_3\},\quad \{a_4,b_4\},\quad \{a_5\}.       \tag{2}
\]

Every two of the first four sets are adjacent by a cross-edge of the
complete bipartite graph, and `a_5` is adjacent to `b_i` for each
`i\in\{1,2,3,4\}`.  Therefore (2) is a `K_5`-minor model in `G-P`.
Since `P` was arbitrary, item 7 follows.  QED.

## Exact scope and missing host-level hypotheses

The construction simultaneously has:

- an actual order-eight separation with connected full shores;
- seven-connectivity and chromatic number seven;
- a two-colourable boundary (`K_{3,5}`);
- disjoint closed-shore extension languages;
- every exact independent-block response;
- the named one-edge and two-edge deletion/contraction responses above;
- a `K_7`-minor-free two-shore quotient; and
- no global two-vertex `K_5`-model transversal.

It deliberately does **not** have the decisive hypotheses of the live
`HC_7` problem:

1. **Global `K_7`-minor exclusion fails.**  The displayed `K_{7,7}`
   itself contains a `K_7` minor, for example using six paired branch
   sets `\{a_i,b_i\}` and the singleton `\{a_7\}`.
2. **Full contraction-criticality is not established.**  The realization
   theorem supplies connected-full high-connectivity amplification and
   internal one-step criticality as separate strengthenings; this graph
   uses the former.  It does not assert that every proper minor is
   six-colourable.
3. **No specified five labelled `K_5`-model branch sets are supplied whose
   literal geometry supports the boundary.**  The construction is an
   extension-language realization; it neither specifies nor guarantees
   the label-preserving model geometry present in the canonical defect-one
   separation.

The first two omissions cannot both be filled by this realization method
without confronting `HC_7` itself.  A nontrivial minor-minimal
seven-chromatic graph containing a `K_7` minor would have `K_7` as a
proper seven-chromatic minor.  Thus, in a genuine nontrivial
contraction-critical instance, `K_7`-minor exclusion is not a cosmetic
extra assumption.

The barrier therefore rules out an argument based only on boundary
chromatic number, extension languages, fullness, connectivity, or a
finite collection of proper-minor colourings.  A positive theorem must
use global `K_7`-minor exclusion together with all-operation
contraction-criticality through literal branch-set geometry.

## A rigorous sufficient condition for the colouring branch

The audited rigid-boundary splice theorem gives a precise sufficient
condition which the barrier does not force.  If the two open shores are
connected and full and there is a nonempty independent set `I\subseteq S`
such that `G[S-I]` is uniquely five-colourable, then the contraction of
each shore together with `I` produces the same boundary partition, after
permuting colours, and the two six-colourings glue.

Accordingly, the unresolved host-level step for the canonical
five-branch-set-supported separation is to derive either such a rigid
trace (or another common exact trace) from label-preserving minor
transitions, or an explicit `K_7`-minor model.  Merely proving
`chi(G[S])\le 5` cannot do this.
