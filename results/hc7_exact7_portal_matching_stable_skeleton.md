# Portal matching and stable skeletons in a 3-connected shore

**Status:** proved and independently audited.  The stable-bridges input is
used only for a path system of order
at least three.  The one-segment formulation recorded in
`../barriers/hc7_exact7_tutte_single_segment_barrier.md` is false.

## 1. A full-adhesion portal matching

### Lemma 1.1 (component portal matching)

Let `G` be `k`-connected, let `S` be a vertex set of order `k`, and let `C`
be a component of `G-S`.  Assume that `G-(S union C)` is nonempty.  In the
bipartite incidence graph whose parts are `S,C` and whose edges are the
literal `S-C` edges of `G`,

\[
                         \nu(S,C)\ge \min\{k,|C|\}.       \tag{1.1}
\]

#### Proof

Suppose the maximum matching has order
`r<min{k,|C|}`.  By Konig's theorem the incidence graph has a vertex cover

\[
                         A\mathbin{\dot\cup}B,
             \qquad A\subseteq S,\quad B\subseteq C,
             \qquad |A|+|B|=r.                           \tag{1.2}
\]

Because `|B|<|C|`, choose a component `K` of `C-B`.  Every edge from `K`
to `S` has its `S`-end in `A`, since `A union B` covers all incidence
edges.  Every edge from `K` to `C-K` has its other end in `B`, by the
definition of `K`.  Finally, `C` is a component of `G-S`, so it has no edge
to `G-(S union C)`.  Consequently

\[
                              N_G(K)\subseteq A\cup B.    \tag{1.3}
\]

The set `K` is nonempty.  The opposite side is also nonempty: the assumed
far shore survives, and `S-A` is nonempty because `|A|<k=|S|`.
Thus `A union B` is a vertex cut of order `r<k`, contradicting
`k`-connectivity.  This proves (1.1). `square`

The lemma is label-free.  In particular, a component of order at least four
behind an actual seven-adhesion has four distinct literal boundary labels
with four distinct portal witnesses.

## 2. The exact stable-bridges input

We use the stable-bridges theorem of Tutte in the path-system formulation:

> Let `l>=3`, let `P={P_1,...,P_l}` be a path system of order `l` in a
> 3-connected graph, and prescribe the two endpoints of every `P_i`.
> There is an equivalent internally disjoint path system `P'` with the same
> endpoint pair for every index such that every `P'`-bridge is stable: no
> single member of `P'` contains all its attachments.

This is the theorem stated as Theorem 1.1 in Paul Wollan, *Bridges in
Highly Connected Graphs*, SIAM J. Discrete Math. 24 (2010), 1731--1741,
DOI `10.1137/070710214`.  The restriction `l>=3` is essential for this
application.

### Theorem 2.1 (portal-preserving stable tree)

Retain Lemma 1.1 with `k=7`.  Suppose `|C|>=4` and `C` is 3-connected.
Then `C` contains an `S`-full tree `T*` with at most twelve labelled
skeleton vertices and at most eleven skeleton segments such that every
`T*`-bridge in `C` has an attachment set not contained in any one segment.

#### Proof

Lemma 1.1 supplies matching edges

\[
                         s_i p_i\quad(1\le i\le4)         \tag{2.1}
\]

with the `s_i` distinct in `S` and the `p_i` distinct in `C`.  For each
remaining `s in S`, choose any literal neighbour `p(s) in C`.  Such a
neighbour exists because otherwise `S-{s}` would separate `C` from the
nonempty far shore with only six vertices.  For the four labels in (2.1),
retain their distinct matched witnesses.

Choose an inclusion-minimal tree `T` in `C` containing all distinct selected
portal witnesses.  Declare as skeleton vertices every selected witness and
every vertex of `T` of degree at least three.  Every leaf of `T` is selected
by minimality.  The skeleton segments are the paths between consecutive
skeleton vertices.  They are internally disjoint, and their union is `T`.

There are at least four skeleton vertices, namely `p_1,...,p_4`, so the
abstract skeleton tree has at least three edges.  Hence its segments form a
path system of order `l>=3`.  Apply Tutte's stable-bridges theorem inside the
3-connected graph `C`, preserving the endpoint pair of each segment.

The returned paths have the same intersection pattern at their fixed
endpoints and are otherwise disjoint.  Their union `T*` is therefore a
subdivision of the same abstract tree.  Every selected portal witness is a
fixed segment endpoint and remains in `T*`; hence `T*` is still `S`-full.
Stability says exactly that no bridge has all its attachments on one
skeleton segment.

There are at most seven distinct selected witnesses.  A minimal tree with
at most seven selected leaves has at most five unselected vertices of degree
at least three.  Thus there are at most twelve skeleton vertices and eleven
segments. `square`

## 3. Pure-Moser consequence and exact scope

In the audited pure-Moser two-component cell, every exterior component is
`S`-full and every component of order at least four is 3-connected.  The
far side contains the other exterior component and `v`.  Theorem 2.1
therefore applies to each such component.

This has one precise proof-spine consequence: the entire one-segment
portal-drift obstruction can be removed at once while preserving four
distinct labelled portal witnesses and all seven boundary contacts.  Every
remaining bridge has attachments not confined to any one of a bounded set
of at most eleven segments.

The theorem does **not** produce the two prescribed row carriers, a
support-five peel, two disjoint linkage paths, or a planar society.  A
stable bridge may meet two segments of the same tree while contacting few
boundary labels.  Thus the live step is a multi-segment bridge/web exchange,
not another local one-segment rotation.

The theorem also does not apply merely because the whole graph is
seven-connected: the component `C` itself must be 3-connected.  Components
of order at most three require separate treatment.
