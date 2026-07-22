# Normalizing a parallel common-root trace cycle

**Status:** written proof; separate internal audit **GREEN** in
[`hc7_common_root_parallel_two_cycle_normalization_audit.md`](hc7_common_root_parallel_two_cycle_normalization_audit.md).
This result normalizes the literal geometry of the parallel two-cycle.  It
also records
a conditional carrier test when the resulting connector has the independent-
block alignment required by an existing response theorem; that alignment is
not proved here.  This result does not prove `HC_7`.

## 1. Fixed-extension setup

Assume the exact two-full-component common-root setup of the audited
[alternating trace-cycle theorem](hc7_common_root_alternating_trace_cycle.md).
Thus `X=N_G(u)`, the components of `G-N_G[u]` are `E,F`, and

\[
                         W_0,\ldots,W_{n-1}             \tag{1.1}
\]

are the components of `G[X][alpha,beta]` for a proper five-colouring
`theta` of `G[X]`.  Fix a coordinate `k`.  Let `c_F` be one fixed extension
of `theta` through `F`, and let `c_E` be one fixed extension of
`theta^{\{k\}}` through `E`.

Let `K_F,K_E` be full `alpha`--`beta` components of these two fixed
extensions.  Suppose they give a parallel two-cycle: for some `l!=k`,

\[
                         W_k\cup W_l\subseteq K_F\cap K_E.       \tag{1.2}
\]

Neither full component is assumed to meet the boundary only in
`W_k union W_l`.

For `Q in {E,F}`, a **trimmed trace connector** is a simple path `P_Q`
inside `K_Q` from `W_k` to `W_l` which meets each endpoint trace only in
its corresponding end.  A trace `W_r`, with `r notin {k,l}`, is
**incidental** on `P_Q` when `P_Q` meets it.

Choose `l,P_E,P_F`, over every parallel partner `l` in (1.2) and every
pair of trimmed trace connectors, so as to minimize lexicographically

\[
 \left(
 |(V(P_E)\cup V(P_F))-X|,
 \sum_{Q\in\{E,F\}}\#\{r:W_r\cap V(P_Q)\ne\varnothing\},
 |E(P_E)|+|E(P_F)|
 \right).                                             \tag{1.3}
\]

The first coordinate is measured on literal open-shore vertices.  The
second retains, with multiplicity between the two paths, every boundary
trace visited by the connectors.

Whenever the degree-eight or degree-nine conclusions below are invoked,
assume in addition the full setup of the audited
[short-trace classification](hc7_common_root_short_trace_classification.md).
In particular, its sharp neighbourhood-independence bound is available;
the degree bound by itself would not imply the stated bound on `n`.

## 2. The bilateral normalization

### Theorem 2.1 (minimal parallel-pair geometry)

The selected paths have all of the following properties.

1. Each `P_Q` meets every boundary trace in at most one contiguous
   subpath.
2. No incidental trace is met by both `P_E` and `P_F`.
3. Cutting the two paths at their boundary visits gives at most `n`
   nonempty open-shore sectors in total.  Here a sector means only the
   open-shore subpath strictly between two consecutive boundary traces;
   its boundary ends are excluded.  Each sector is induced, and all
   distinct sectors are pairwise anticomplete.
4. The two connectors, joined inside `W_k` and `W_l`, contain a simple
   odd cycle which uses vertices of both open shores.

Consequently, in degree eight one of `P_E,P_F` is boundary-clean: its only
vertices in `X` are its two ends.  In degree nine the two connectors have
at most four open-shore sectors in total.  If the selected full-component
block on one shore is exactly `{k,l}`, its connector is boundary-clean on
that shore.

In the root-retaining synchronized degree-eight choice one may take
`k=0` and `W_0={x}`.  In that case the odd cycle in item 4 contains the
literal common root `x`.

### Proof

Fix `Q in {E,F}`.  Suppose `P_Q` leaves a trace `W_r` and later returns to
it.  Replace the subpath between its first and last relevant vertices of
`W_r` by a path inside the connected graph `W_r`, and then delete any
resulting closed subwalk.  Different boundary `alpha`--`beta` components
are anticomplete in `G[X]`, so the replaced excursion used an open-shore
vertex.  The replacement strictly decreases the first coordinate of
(1.3), a contradiction.  This proves item 1.

Suppose an incidental trace `W_r` is met by both selected paths.  On each
path retain the portion from `W_k` through its first visit to `W_r`, and
trim the new end inside `W_r`.  These are two valid connectors for the
parallel pair `k,r`.  On either old path, passage from `W_r` to the
different boundary component `W_l` necessarily used an open-shore vertex.
The two retained prefixes therefore strictly decrease the first coordinate
of (1.3), again a contradiction.  This proves item 2.

Let `s_Q` be the number of boundary traces visited by `P_Q`.  Item 1 shows
that cutting at those visits gives exactly `s_Q-1` nonempty open-shore
sectors in `Q`.  By item 2, the two sets of visited trace labels
intersect only in `{k,l}`.  Hence

\[
 (s_E-1)+(s_F-1)
   =\left|\{r:W_r\cap(V(P_E)\cup V(P_F))\ne\varnothing\}\right|
   \le n.                                               \tag{2.1}
\]

There is no edge between an `E`-sector and an `F`-sector.  If an edge were
a chord of one sector, replacing the intervening subpath by that edge would
reduce the first coordinate of (1.3).  Thus every sector is induced.

Now suppose an edge joins two distinct sectors on one path.  If an entire
open sector lies between its ends, shortcutting along the edge reduces the
first coordinate.  Otherwise the two sectors are consecutive.  The same
shortcut either removes an open-shore vertex, again reducing the first
coordinate, or removes only their intervening incidental boundary trace,
reducing the second coordinate.  After deleting any closed subwalk the
result remains a valid trimmed connector for the same parallel pair.  Every
possibility contradicts (1.3), proving item 3.

The open interiors of `P_E,P_F` are disjoint because they lie in different
components of `G-N_G[u]`.  By item 2 their internal boundary traces are
also disjoint.  Join their two ends inside the connected graph `W_k`, and
join their other two ends inside `W_l`.  The connectors were trimmed, so
these four paths can be chosen to form a simple cycle `Z`.

To compute its parity, encode `alpha,beta` by `0,1`.  Along either fixed
shore colouring, the parity of a two-colour path is the xor of the colours
at its ends.  The traces of `c_E,c_F` agree on `W_l`, whereas they are
interchanged on `W_k`.  Summing the four path parities around `Z` therefore
gives one.  Thus `Z` is odd.  Since `W_k,W_l` are different components of
the boundary two-colour graph, each shore connector has a nonempty open
interior.  This proves item 4.

The audited short-trace bound gives `n<=3` in degree eight and `n<=4` in
degree nine.  Each connector contributes at least one sector, so (2.1)
makes one degree-eight connector consist of exactly one sector and hence
boundary-clean.  Finally, every boundary trace met by a connector belongs
to the full-component block containing it.  An exact block `{k,l}`
therefore makes that connector boundary-clean.  The root-retaining claim
follows from Theorem 4 of the short-trace classification: choose `k=0`,
where `W_0={x}`; the joined cycle necessarily contains its unique vertex
`x`. \(\square\)

## 3. A conditional carrier test

Let `P` be a `p`--`q` path whose open interior lies in `E`, and let `B` be
an independent boundary block of order at least two disjoint from `{p,q}`.
Let `mathcal C_E(P)` be the components of

\[
                         G[E-V(P^\circ)].              \tag{3.1}
\]

Define the bipartite incidence graph `J_B(P)` with parts
`B` and `mathcal C_E(P)`, putting an edge `bC` exactly when `b` has a
neighbour in `C`.

### Lemma 3.1 (incidence--carrier equivalence)

There is a set `K subseteq E-V(P^\circ)` for which
`G[B union K]` is connected and contains an edge if and only if one
connected component of `J_B(P)` contains every vertex of `B`.

### Proof

If such a carrier `K` exists, enlarge each nonempty intersection of `K`
with a component of (3.1) to that whole component.  Project paths in the
connected graph `G[B union K]` by replacing every maximal shore subpath by
the corresponding member of `mathcal C_E(P)`.  All vertices of `B`
then lie in one incidence component.

Conversely, suppose one incidence component contains all of `B`.  Let `K`
be the union of the vertex sets of all members of `mathcal C_E(P)` in that
incidence component.  Each such member is connected, and the incidence
component records paths between them through vertices of `B`.  Hence
`G[B union K]` is connected.  Since `B` is independent and has at least two
vertices, the incidence component contains a shore-component vertex and
therefore supplies an edge. \(\square\)

### Corollary 3.2 (conditional incidence test)

Retain the setup of Section 1 of the audited
[low-degree concentrated-reserve elimination](hc7_low_degree_concentrated_reserve_elimination.md),
including the full two-component shore structure, proper-minor
six-colourability, and boundary partition

\[
                         S=I\mathbin{\dot\cup}T
                              \mathbin{\dot\cup}\{p,q\}.          \tag{3.2}
\]

Assume additionally its independence bound

\[
                         \alpha(G[S])\le d_G(u)-5,                \tag{3.3}
\]

and that each of `p,q` has a neighbour in `T`.  No connector or carrier
from Section 2 of that result is assumed.

Let `B` be either `I` or `T`, and let `A` be the other block.  If `P` is a
`p`--`q` connector through `E` and one component of `J_B(P)` contains all
of `B`, then `G` is six-colourable.  Consequently every `p`--`q` connector
satisfying these hypotheses and surviving in a hypothetical counterexample
splits both `I` and `T` between at least two components of `J_I(P)` and
`J_T(P)`, respectively.

### Proof

Lemma 3.1 supplies a boundary-block carrier `K` for `B` disjoint from the
open interior of `P`.  The singleton `{u}` is a disjoint carrier for `A`.

For the merged response on the closed `F`-shore, simultaneously contract
spanning trees of the three pairwise disjoint connected sets

\[
                  A\cup\{u\},\qquad B\cup K,\qquad V(P).         \tag{3.4}
\]

Their images form a triangle: the first meets the second through an edge
from `u`, the first meets the third through `up`, and the second meets the
third through a root-to-`B` edge.  Six-colour this proper minor, retain its
colouring on `F`, and expand the three image colours over `A,B,{p,q}`.
This gives the exact boundary partition

\[
                              I\mid T\mid\{p,q\}.                 \tag{3.5}
\]

For the split response, apply the audited root-connector reflection theorem
with root connector `V(P^circ)`, carrier `{u}` for `A`, and carrier `K` for
`B`.  The imported hypotheses give an `I`--`T` edge and a neighbour of each
root in each block.  Reflection therefore gives the exact partition

\[
                         I\mid T\mid\{p\}\mid\{q\}               \tag{3.6}
\]

on the closed `F`-shore.  The opposite-response lemma in the cited result
gives one of (3.5),(3.6) on the closed `E`-shore.  Choose the matching
`F`-response; after permuting colour names, the two colourings glue and
six-colour `G`. \(\square\)

### Corollary 3.3 (what seven-connectivity actually gives)

Assume additionally that `G` is seven-connected, and let `P` satisfy the
hypotheses of Corollary 3.2 in a hypothetical counterexample.  For every
component `D` of `G[E-V(P^circ)]`, put

\[
 m_D=|S-N_G(D)|,\qquad h_D=|N_G(D)\cap V(P^circ)|.                \tag{3.7}
\]

Then `D` misses at least one vertex of each of `I,T`, so `m_D>=2`, and

\[
 h_D\ge m_D-1\quad(d=8),\qquad
 h_D\ge m_D-2\quad(d=9).                                       \tag{3.8}
\]

### Proof

If `D` had a neighbour at every vertex of `I`, the incidence component of
`J_I(P)` containing `D` would contain all of `I`, contrary to Corollary 3.2.
The same argument applies to `T`.  The two missed vertices lie in disjoint
blocks, so `m_D>=2`.

Every neighbour of `D` outside `D` lies in `S` or in `V(P^circ)`: distinct
components of `E-V(P^circ)` are anticomplete, `E,F` are anticomplete, and
`u` has no neighbour in `E`.  Thus

\[
                 |N_G(D)|=d-m_D+h_D.                            \tag{3.9}
\]

The set `N_G(D)` separates the nonempty set `D` from `u`, so
seven-connectivity gives `|N_G(D)|>=7`.  Rearranging (3.9) proves (3.8).
\(\square\)

## 4. Exact gain and trust boundary

Theorem 2.1 turns a parallel incidence edge pair into one literal odd cycle
with a bounded number of pairwise anticomplete shore sectors.  It does not
silently assume that either full-component block consists of the two
selected traces.  In degree eight it nevertheless gives one boundary-clean
connector.

Independently, Corollary 3.2 identifies the precise obstruction once a
connector is aligned with the partition and root-contact hypotheses of the
independent-block response theorem: deleting its open interior must split
the incidence of each independent block with the remaining shore.  The
parallel-cycle theorem does **not** show
that its clean connector admits this alignment.  Establishing that alignment
or replacing it by another operation-compatible response is still open.
Even in the aligned case, the incidence split need not be a bounded
separator, an actual component of `G-N[u]`, or a response-preserving
descent.  Corollary 3.3 gives only a lower bound on the number of contacts
with the deleted connector; that number is unbounded.  The second
synchronized cube coordinate may use a different
opposite-shore extension and must not be combined with the first without an
additional synchronization argument.

No `K_7`-minor model, common complete boundary partition in the general
parallel case, or strict same-host anti-neighbourhood component descent is
claimed.

## Inputs

- [alternating full-component trace cycle](hc7_common_root_alternating_trace_cycle.md)
- [low-degree short-trace classification](hc7_common_root_short_trace_classification.md)
- [dual response from a connector and independent-triple carrier](hc7_low_degree_concentrated_reserve_elimination.md)
- [root-connector reflection](hc7_order8_root_connector_reflection.md)
