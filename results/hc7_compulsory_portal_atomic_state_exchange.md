# Atomic compulsory-portal state exchange

**Status:** proved and independently audited through the blocking-path
alternative.  The final blocking-path-to-model implication is open.

## 1. Atomic setup

Retain the atomic `|U|=1` outcome of
`hc7_compulsory_portal_bridge_composition.md`, without altering that frozen
source.  Thus

\[
 S=W\mathbin{\dot\cup}\{u\},\qquad |S|=7,
\]

the thin shore `A` is connected and `S`-full, the rich shore `R` contains
two disjoint `S`-full packets, and `zu` is the unique `A-u` portal edge.
Every proper minor is six-colourable.

The following theorem is stated in the reusable form actually supplied by
the connected-rich width-two frontier.  Assume that

\[
 S=I\mathbin{\dot\cup}J\mathbin{\dot\cup}K,            \tag{1.1}
\]

where:

* `I,J` are nonempty independent sets;
* `u in I` and `|I|>=2`; and
* `K` is a clique of order at most one.

For a connected bipartite frontier take `K=emptyset` and orient its
bipartition so that `u in I`.  For
`K_{1,3} dotcup K_3`, choose a triangle vertex different from `u` when
necessary for `K`; the audited frontier then gives (1.1), with both
bipartition classes nonempty and `|I|>=2`.

## 2. Exact independent trace

### Lemma 2.1

There is a legal six-colouring `c` of `G[R union S]` in which `I` is one
exact equality block and no member of `S-I` has its colour.

#### Proof

The set `A union I` is connected because `A` is connected and `S`-full.
It is nontrivial, and the members of `I` are independent.  Contract a
spanning tree of `A union I` to a vertex `a`.  This is a proper minor and
hence has a six-colouring.

Restrict the colouring to `R union S`, expanding the colour of `a` only
over the literal members of `I` and discarding the interior of `A`.  The
expansion is proper because `I` is independent and every `I-R` edge became
incident with `a`.  Since `A` is `S`-full, `a` is adjacent in the minor to
every member of `S-I`.  None of them has its colour.  \(\square\)

## 3. Block Kempe exchange

### Lemma 3.1

Let `B,C` be two distinct equality blocks of a boundary colouring, and
assume there is no literal edge between `B` and `C`.  Then either:

1. Kempe swaps merge exactly `B,C` into one equality block, leaving every
   other boundary block unchanged; or
2. there is a bichromatic path with one end in `B`, one end in `C`, and
   all internal vertices outside the boundary.

#### Proof

Consider the graph induced by the two colours of `B,C`.  If one component
meets both blocks, take a shortest path between the two boundary sets in
that component.  Minimality puts every internal vertex off the boundary,
giving item 2.

Otherwise interchange the two colours on every component meeting `B`.
No such component meets `C`, and no other boundary block has either
colour.  All vertices of `B union C` now have the colour formerly used on
`C`; every other boundary colour is unchanged.  The absent `B-C` edge
makes the merged colouring proper.  \(\square\)

## 4. Trace compression or a literal rich-shore path

### Theorem 4.1 (atomic trace exchange)

Under Section 1, either `G` is six-colourable or the rich closed-shore
colouring supplied by Lemma 2.1 contains a bichromatic path `Q` of one of
the following two labelled forms:

1. its ends lie in two distinct equality blocks, both meeting `J`; or
2. `K={k}`, one end is `k`, the other lies in `J`, and all internal
   vertices lie in `R`.

In both cases every internal vertex of `Q` lies in `R`.  Thus the output is
a literal carrier, not an abstract equality relation.

#### Proof

Start with the exact trace colouring from Lemma 2.1.  Its `I`-colour is
absent from `J union K`.

First detach the possible reservoir vertex.  Suppose `K={k}` and `k`
shares its colour with a vertex of `J`.  Because `|I|>=2`, the trace has at
most six boundary blocks; sharing `k` with `J` lowers this to at most five.
Hence some palette colour is absent from the whole boundary.  In the
two-colour graph consisting of this spare colour and the colour of `k`,
either the component containing `k` contains no `J`-vertex, in which case
swapping that component makes `{k}` a singleton block, or a shortest path
from `k` to a `J`-vertex has all internal vertices in `R`.  The latter is
item 2.  If `k` was already singleton, no operation is needed.

Assume no path has occurred.  Every equality block meeting `J` is now a
subset of `J`.  While two such blocks remain, apply Lemma 3.1 to them.
They are anticomplete because `J` is independent.  A path outcome is item
1; otherwise the number of `J`-blocks strictly decreases.  Thus the
process terminates.

If it terminates without a path, the exact boundary partition is

\[
                         I\mid J
 \quad\hbox{or}\quad I\mid J\mid\{k\}.                \tag{4.1}
\]

Its packet demand is at most two: in the first case there are two blocks;
in the second there are three blocks and `{k}` is a singleton clique of
order one.  The two disjoint full packets in `R` reproduce this exact
partition on the thin closed shore by the audited adaptive packet
reflection theorem.  The two closed-shore colourings then align and glue,
contrary to the assumption that `G` is not six-colourable.  \(\square\)

## 5. Exact unfinished implication

The theorem eliminates the entire **Kempe-compressible** atomic residue.
The sole remaining implication is now literal:

> A trace-blocking bichromatic path in the rich shore, with endpoints in
> the named bipartition duty `J` (or from its one-vertex clique reservoir
> to `J`), must yield a labelled `K_7/K_7^vee`, a state-preserving smaller
> seven-adhesion, or a coherent fixed pair.

One such path is not automatically a new branch set.  It may run through
both preselected full packets, and Lemma 3.1 supplies no disjointness from
either packet.  Contracting the path forces its two endpoint literals to
agree only in a colouring of the *opposite* closed shore; it does not
preserve the independently manufactured `I`-trace.  This is the first
exact failed implication of the mechanism:

\[
 \text{blocking path in }R
 \centernot\Longrightarrow
 \text{same traced state on }A\cup S.                 \tag{5.1}
\]

The failure is precisely state preservation, not path existence.  A
valid continuation must compose the path contraction with the compulsory
bridge/Kempe locks, or prove a packet-escape rerouting.  Treating the path
as disjoint from the packet cover would be invalid.
