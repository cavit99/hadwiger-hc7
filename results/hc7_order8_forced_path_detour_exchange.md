# Detouring a forced root path reserves a boundary-block subgraph

**Status:** written proof; separate internal audit GREEN in
[`hc7_order8_forced_path_detour_exchange_audit.md`](hc7_order8_forced_path_detour_exchange_audit.md).
This is a positive exchange lemma inside the order-eight two-cut response
configuration.  It does not prove `HC_7`.

## 1. Setting

Assume the hypotheses and notation of the audited
[two-cut response-orientation theorem](../results/hc7_order8_two_cut_response_orientation.md).
Thus `S` has order eight, `G-S` has the three boundary-full components
`C,Q_0,Q_1`, and

\[
 S-\{d,e\}=P\mathbin{\dot\cup}R
\]

is a bipartition into nonempty independent sets.  The closed `C`-side has
the split response

\[
                  P\mid R\mid\{d\}\mid\{e\},          \tag{1.1}
\]

and every colouring in the selected response family supplies a
bichromatic `d`--`e` path with all internal vertices in `C`.

Fix one such path and write its internal path as

\[
                  D=v_0v_1\cdots v_k,                 \tag{1.2}
\]

where `d v_0` and `v_k e` are edges.  The endpoints `v_0,v_k` are
distinct: the first belongs to `L_e`, the second to the disjoint lobe
`L_d`.

For a boundary vertex `s`, a set `Z subseteq C` **meets the `s`-portal
set** if some vertex of `Z` is adjacent to `s`.

## 2. The path-detour exchange

### Lemma 2.1

Let `B` be either `P` or `R`.  Suppose there are indices

\[
                        0\le i<j\le k,
                        \qquad j\ge i+2,               \tag{2.1}
\]

and a `v_i`--`v_j` path `W` in `G[C]` whose internal vertices are disjoint
from `D`.  If the open path segment

\[
                         K=D[v_{i+1},v_{j-1}]           \tag{2.2}
\]

meets the portal set of every literal vertex of `B`, then `G` is
six-colourable.

The same conclusion holds if a component of `G[C]-V(D)` meets the portal
set of every literal vertex of `B`.

#### Proof

Replace the segment `D[v_i,v_j]` by `W`.  Because the interior of `W` is
disjoint from all of `D`, the resulting walk is the simple path

\[
 D'=D[v_0,v_i]\cup W\cup D[v_j,v_k].                  \tag{2.3}
\]

Its vertex set is disjoint from `V(K)`.  The path `D'` has a neighbour at
both `d` and `e`, through `v_0` and `v_k`, respectively, while the
connected subgraph `K` meets every portal set indexed by `B`.

Choose either `Q_0` or `Q_1` as a third connected subgraph.  It is disjoint
from `D'` and `K` and is adjacent to every vertex of the other bipartition
class.  The three connected subgraphs therefore satisfy the hypotheses of
the audited
[reserved-path boundary-response theorem](../results/hc7_order8_three_block_linkage_reflection.md).
That theorem realizes both (1.1) and the merged-root partition

\[
                       P\mid R\mid\{d,e\}              \tag{2.4}
\]

on each opposite closed component-side.  One can align the two component-
side colourings with the selected split-response colouring on the closed
`C`-side, so the three colourings glue to a proper six-colouring of `G`.

For the second assertion, retain `D' = D` and take the stated component of
`G[C]-V(D)` as `K`.  The same three-subgraph construction applies.
\(\square\)

### Corollary 2.2 (a bridge-span test)

Regard every component `A` of `G[C]-V(D)`, together with all its edges to
`D`, as a bridge of `D`.  If a bridge has two attachments `v_i,v_j` and
contains a `v_i`--`v_j` path internally in `A`, then either of the following
is terminal:

1. `A` meets every portal set indexed by one of `P,R`; or
2. the open span `D[v_{i+1},v_{j-1}]` is nonempty and meets every portal
   set indexed by one of `P,R`.

In either case `G` is six-colourable.

#### Proof

The first case is the second assertion of Lemma 2.1.  The internal bridge
path is the detour `W` in the second case. \(\square\)

No shortest-path hypothesis is needed.  In particular, the lemma preserves
the literal boundary labels: a class is funded only by actual neighbours of
each named boundary vertex, not by the colours appearing on `D`.

## 3. What failure of every single bridge proves

Failure of the two tests in Corollary 2.2 is **not**, by itself, a web or a
separator certificate.  Several bridges may compose to give the required
disjoint connected subgraphs even though no single bridge passes either
test.  The correct negative object is failure of the whole packing:

* a nontrivial path between the `d`- and `e`-portal sets; and
* disjoint from it, a connected subgraph meeting every portal set indexed
  by a chosen class `B`.

Choose `B` to be a smaller class of the bipartition.  Since
`|P|+|R|=6`, one has `|B|<=3`.  The existing unbounded reductions then give
the following exhaustive consequences.

1. If `|B|=1`, the singleton-class reduction gives a six-colouring, an
   actual order-seven separation, or a strict order-eight lobe descent.
2. If `|B|=2`, the Two Paths theorem gives a six-colouring, an actual
   order-seven separation, or an attachment-free planar web with outer
   order `d,b_1,e,b_2`.
3. If `|B|=3`, the two--three linkage reduction gives a six-colouring, an
   actual order-seven separation, a component of order at most six, or a
   proper connected subgraph behind at most five internal vertices.  After
   excluding small-boundary descent, the last subgraph has boundary order
   at least nine and positive boundary excess.

The first two statements are proved in the
[small-class web reduction](../results/hc7_order8_two_cut_small_class_web_reduction.md).
The third is the
[three-portal two--three reduction](../results/hc7_order8_three_portal_two_three_reduction.md),
applied to `C`.

Thus the single-bridge test is a useful explicit exchange, but its failure
must not be promoted to a structural conclusion.  For two portals, the
whole-packing failure is exactly the web case.  For three portals, the
current exact residue is the positive-excess confined subgraph, not yet a
web and not yet an order-seven boundary.

## 4. Trust boundary

Lemma 2.1 and Corollary 2.2 terminate every stated detour or off-path-
component configuration by an actual six-colouring of `G`.  They retain
the selected split response and every literal boundary label.

They do not show that every positive packing is witnessed by one bridge,
and they do not convert the three-portal positive-excess subgraph into a
common boundary equality partition.  Restricting the selected colouring to
that subgraph preserves a one-sided colouring, but does not preserve all
five portal labels or the complete response on both new closed shores.
The deterministic eight-connected wheel barrier to a three-portal packing
shows that connectivity and boundary fullness alone cannot supply this
missing conclusion.
