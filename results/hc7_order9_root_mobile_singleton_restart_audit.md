# Independent audit of the root-mobile singleton restart theorem

## Verdict and audited revision

**Verdict: GREEN.**

This audit checks the complete source file
[`hc7_order9_root_mobile_singleton_restart.md`](hc7_order9_root_mobile_singleton_restart.md)
at SHA-256

```text
4a432a4e78605bda6a85e59f83c246aad598011aa5dffa54377877d62acb6f31
```

Relative to the revision originally checked at
`44bc2e2e385eaa712c9fab7b26c2476652e4683d6a0f21cd6ea7df1a1404b098`,
the only change is the status line linking this adjacent GREEN audit.  The
mathematical statement and proof are unchanged.

The explicit `K_7`-minor model, the two proper-minor contractions, the
exact-singleton boundary traces, the order-eight reconfiguration argument,
the two-root overlap, and the static-language limitation are all correct.
The theorem is a restart family only: it does not align the outcomes for
different roots or close the order-nine interface.

For the reconfiguration step, this audit uses the previously GREEN-audited
full-connectivity revision of
[`hc7_order8_full_five_colour_reconfiguration.md`](../results/hc7_order8_full_five_colour_reconfiguration.md)
at SHA-256

```text
c15e2a66b6926d926ff269c79a8abb33a9ee5e75ecbf925b4c43315a3c46dd07
```

The result is currently being strengthened to keep a path at four or five
colours.  That strengthened source has a fresh audit pending.  The present
restart theorem needs only the earlier full-connectivity statement and is
therefore not conditional on that strengthening.

## 1. Setting and the explicit `K_7` model

The partition

```text
V(G)=A disjoint-union B disjoint-union D
```

is literal, the two open shores are connected and nonempty, there are no
`A-D` edges, and every boundary vertex has a neighbour in each shore.  These
hypotheses are exactly what the subsequent branch-set and gluing arguments
use; no connectivity of the host is silently assumed.

Fix `s in B` and suppose that `G[B-{s}]` contains a `K_5` model with branch
sets `M_1,...,M_5`.  The seven proposed branch sets

```text
A union {s},  D,  M_1,...,M_5
```

are pairwise disjoint.  The first is connected because `A` is connected and
`s` has an `A`-neighbour; `D` is connected.  They are adjacent because `s`
has a `D`-neighbour.  Each of the first two sets is adjacent to every `M_i`:
choose any literal boundary vertex in the nonempty set `M_i` and use
boundary fullness of the appropriate shore.  The final five sets have all
required adjacencies by the definition of a clique-minor model.  Thus this
is an explicit `K_7`-minor model and proves that every `G[B-{s}]` is
`K_5`-minor-free.

## 2. Proper-minor contractions and exact singleton traces

For the trace on the `A`-closed shore, the source contracts a spanning tree
of `G[D union {s}]`.  This graph is connected: `D` is connected and `s` has
a neighbour in `D`.  It has at least two vertices, so the contraction
strictly reduces the graph and is a proper minor operation.

Let `z` be the contracted vertex.  For every `b in B-{s}`, boundary fullness
gives an edge from `b` to `D`, which becomes an edge `bz`.  Consequently the
colour of `z` occurs nowhere on `B-{s}` in any proper six-colouring of the
minor.  Restrict that colouring to `A union (B-{s})` and restore the literal
vertex `s` with the colour of `z`.  Every retained edge incident with `s`
was represented by the corresponding edge incident with `z`; all other
retained edges are unchanged.  The restored colouring is therefore proper,
and `{s}` is exactly the boundary class of its colour.

Contracting `A union {s}` gives the symmetric trace on the `D`-closed
shore.  The two trace partitions cannot coincide: after relabelling the six
colours on one shore, coincident boundary classes would agree literally on
`B`, and the absence of `A-D` edges would let the colourings glue to a
six-colouring of `G`.

## 3. Reconfiguration at a fixed root

For `|B|=9`, the graph `H_s=G[B-{s}]` has eight vertices and is
`K_5`-minor-free by the explicit model argument.  After naming the unique
colour of `s` as colour six, an exact-`{s}` boundary colouring is exactly a
proper five-colouring of `H_s`; any of the five colours may be unused.
Conversely, adding `s` in the fresh sixth colour turns every such
five-colouring into a proper boundary colouring.  Thus the two nonempty
shore-extension sets are literal subsets of `R_5(H_s)`.

They are disjoint, because a colouring in their intersection would give
closed-shore extensions agreeing on `B` and hence a six-colouring of `G`.
The audited order-eight theorem makes `R_5(H_s)` connected, so a shortest
path between the two sets exists and has positive length.

If the path has one edge, its endpoints differ at one literal boundary
vertex.  The host-level consequence of the audited theorem applies with
the fixed independent block `I={s}` and yields one bichromatic obstruction
path through each open shore, with disjoint interiors.  All its hypotheses
have been established above.

If the path has at least two edges, no internal colouring extends through
either shore: an extension through one side would shorten the path to the
opposite endpoint set.  For a fixed rejected boundary colouring, extending
through one open shore is exactly the associated list-colouring problem on
that shore.  A vertex-minimal induced uncolourable subgraph is connected,
since otherwise its components could be coloured independently (or one
component would already be a smaller obstruction).  This proves the paired
connected-obstruction outcome.

## 4. Two-root overlap and colour relabelling

For distinct `s,t in B`, the known case `HC_5` makes
`G[B-{s}]` four-colourable, because that graph has no `K_5` minor.  Its
seven-vertex induced subgraph `G[B-{s,t}]` is therefore colourable with at
most four colours.  If fewer than four colours occur, a colour class has at
least two vertices; recolouring one member with a previously unused colour
is proper and leaves the old class nonempty.  Repetition gives exactly four
nonempty colour classes.

Giving `s` and `t` two distinct fresh colours now produces a proper boundary
colouring using all six colours, with `{s}` and `{t}` as distinct singleton
classes.  If every full exact-`s` trace and every full exact-`t` trace each
had a constant shore owner, the common trace just constructed shows that
those two owners cannot be opposite: otherwise the same boundary colouring
would extend through both shores and glue.  This proves precisely the stated
pairwise consistency; it does not prove that a root has a constant owner.

## 5. Static barrier and exact scope

On an independent boundary of order nine, the class-size pattern

```text
(4,1,1,1,1,1)
```

and its complement among full six-colour traces give two disjoint,
colour-permutation-invariant abstract types.  For one root, and also for any
specified pair of roots, both types have traces with the required singleton
classes:

- type `A` uses one four-vertex class and five singleton classes;
- type `D` uses three two-vertex classes and three singleton classes.

The counts sum to nine in each case and the indicated choices can avoid the
prescribed singleton roots.  Thus even complete pairwise overlap of the
rooted trace families does not force an abstract trace to have both
orientations.

The source states the trust boundary correctly.  These two types are not
asserted to be extension languages of actual connected shores and encode
neither contraction-critical operations nor `K_7`-minor exclusion.  They
refute only a static inference from root overlap and colour-permutation
symmetry.

## 6. Exact update available from four-or-five-colour reconfiguration

The strengthened finite theorem should **not** simply replace `R_5(H_s)` by
`R_5^{>=4}(H_s)` in Theorem 4.1.  Connectivity of the latter graph is useful
only if both shore-extension sets contain a trace whose restriction to
`H_s` uses at least four colours.  Lemma 3.1 guarantees an exact singleton
trace on each shore, but it does not guarantee that either trace uses four
of the remaining five colours.

The safe corollary is the following.

> Fix `s in B` and assume, in addition, that each closed shore has an
> exact-`{s}` extension whose restriction to `H_s` uses at least four of the
> other five colours.  Then the shortest path in Theorem 4.1 may be chosen
> wholly in `R_5^{>=4}(H_s)`.  The same one-step/paired-core fork holds, and
> every internal rejected trace in the paired-core outcome uses four or five
> colours.  If, further, every surjective exact-`{s}` trace extends through
> exactly one shore, then every such internal trace uses exactly four
> colours and the two list assignments share the same boundary-absent
> fifth colour.

Without the displayed endpoint hypothesis, the earlier full-`R_5`
argument remains valid but the four-colour lower bound on internal traces
does not follow.  This is a dependency qualification, not a defect in the
current root-mobile theorem.

## 7. Trust boundary

The theorem produces one valid restart fork for every literal boundary
vertex.  Different roots may use unrelated proper-minor colourings,
one-vertex transitions, list-critical subgraphs, remote path endpoints, and
minor-model labels.  No common boundary colouring, compatible order-seven
separation, label-preserving model repair, strict host-level descent, or
`K_7` minor follows beyond the explicit model in Lemma 2.1.
