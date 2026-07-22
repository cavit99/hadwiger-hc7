# Audit: low-degree concentrated reserve elimination

**Audit type:** separate internal cold audit

**Verdict:** **GREEN**

Audited theorem:
[`hc7_low_degree_concentrated_reserve_elimination.md`](hc7_low_degree_concentrated_reserve_elimination.md)

Audited source SHA-256:

```text
41d0f9f8f923410f7058ded5d3001e9ea75e179fc28b4bef08504cb9adb83401
```

This is an internal mathematical audit, not external peer review.  The
result eliminates the stated concentrated alternative; it does not prove
`HC_7`.

## Lemma 1.1: response quantifiers and gluing

For either retained component `P`, both contracted sets

```text
{u} union I,   P' union T
```

are nontrivial, connected, and disjoint.  The first is a star, while the
second is connected because `P'` is connected and its full boundary is
`S`.  Contracting spanning trees therefore gives a proper minor.

The two contraction images are adjacent through an edge from `u` to `T`.
Each root `p,q` is adjacent to the first image through `u` and to the
second through the fullness of `P'`.  On restriction to the retained shore
and pullback to the boundary, `I` and `T` are consequently distinct exact
colour classes and both roots avoid their colours.  This proves that each
response set is nonempty; it does not incorrectly claim that either shore
realizes both root-equality types.

If the two shores realize the same equality type, their complete boundary
partitions are identical: they are either

```text
I | T | {p,q}
```

or

```text
I | T | {p} | {q}.
```

After a colour permutation the shore colourings therefore glue on all of
`S`.  The resulting colouring of `G-u` uses only three or four colours on
`S`, so a missing colour can be assigned to `u`.  Thus the two nonempty
response sets are disjoint subsets of a two-element set and must be the two
opposite singletons.  If `pq` were an edge, both could contain only the
split type, contradicting that conclusion.  The equality-type quantifiers
and the deduction that `pq` is a nonedge are sound.

## Theorem 2.1: contractions and reflection

For the merged response, the three contracted sets

```text
{u} union I,   T union K,   V(Q)
```

are pairwise disjoint, connected, and each contains an edge.  The first
and second images are adjacent through `uT`, the first and third through
`up` (or `uq`), and the second and third through a root-to-`T` edge.  They
form a triangle.  Pulling their three distinct colours back over the
independent blocks `I,T,{p,q}` is proper; the last block is independent by
Lemma 1.1.  This gives the exact merged partition on the closed `F`-shore.

The application of the audited root-connector reflection theorem matches
all of its hypotheses, for both boundary degrees:

- its decomposition is `L=F`, boundary `S=N(u)`, and open side
  `R'=E union {u}`; the two open sides are nonempty and anticomplete;
- its two independent blocks are `I,T`, of orders `3,3` in degree eight
  and `4,3` in degree nine; the reflection theorem has no cardinality
  restriction on these blocks;
- the open interior of `Q` is a nonempty connected root connector, since
  `pq` is a nonedge;
- `{u}` is a boundary-block carrier for `I`, and `K` is one for `T`;
- these carriers and the connector are pairwise disjoint;
- an `I`--`T` edge is forced because otherwise `I` plus one vertex of `T`
  is an independent set of order `d-4>d-5`;
- each root contacts `I` by the same independence-number argument, and
  each contacts `T` by hypothesis.

Reflection therefore gives the exact split partition on the same closed
`F`-shore.  One of its merged and split responses matches the unique
`E`-shore response from Lemma 1.1.  Gluing and colouring `u` with a colour
absent from the three- or four-colour boundary is valid.  No degree-eight
assumption is hidden in the reflection step.

## Lemma 3.1: five-vertex classification

The imported setup has `|D|>=7`, so `q>=7`; the audited upstream bounds
give `q<=8` in degree eight and `q<=9` in degree nine.  Lemma 1.1 excludes
every reserve edge whose complementary three vertices are independent.

The sparse classification is exhaustive:

- with one edge (`q=9`), its three-vertex complement is independent;
- with two edges (`q=8`), intersecting edges form a `P_3` and either edge
  has an independent complement, so only `2K_2 union K_1` remains;
- every three-edge graph on five vertices (`q=7`) is, up to isomorphism,
  `K_3 union 2K_1`, `K_{1,3} union K_1`, `P_4 union K_1`, or
  `P_3 union K_2`.  A triangle edge, a star edge, or the middle `P_4`
  edge excludes the first three respectively.

Thus the two displayed surviving reserve graphs are exactly the claimed
ones; there is no omitted `q=7,8,9` isomorphism type.

## Theorem 4.1: path selection

In the `q=7` graph, all seven reserve nonedges lie in `D`.  The pairs
`ac,ad` form a tree on the independent triple `T={a,c,d}`, while `be` is
the complementary root pair and both roots contact `T`.  The union of the
open interiors of the first two paths is a boundary-block carrier for
`T`.  It need not itself be connected before `T` is adjoined.  Its colour
set is disjoint from the two colours of the `be` connector, so the carrier
and connector are vertex-disjoint.

In the `q=8` graph, the four choices of one endpoint from each matching
edge, together with the isolated vertex, give four independent triples and
four distinct complementary cross nonedges.  Since

```text
|N| = q-|D| <= 1,
```

at least one complementary pair lies in `D`.  For its associated triple
`T`, at most one of the three internal nonedges lies in `N`; hence at least
two lie in `D`.  Any two distinct pairs on a three-vertex set form a
spanning tree.  Their path interiors give the `T`-carrier, while the chosen
complementary-pair path gives the root connector.  The two constructions
again use disjoint fixed-colouring palettes and are vertex-disjoint.  This
checks the sole-`N` case as well as `N` empty.

Paths used inside one carrier may intersect each other; the reflection
theorem requires only that their union with `T` be connected and that the
carrier be disjoint from the root connector.  Both requirements hold.

## Corollary 4.2 and dependency revisions

Corollary 3.2 of the audited five-reserve packet is an inclusive dichotomy:
either an `R`-rooted `K_5` model already exists, or at least seven reserve
nonedges are exclusive to one shore.  In the latter case, relabelling the
two full components makes the complete set of exclusive demands the set
`D` of Section 3, with the same fixed colouring and independent set.  This
is exactly the alternative eliminated by Theorem 4.1.  The corollary does
not infer a shore-confined model or an additional branch set.

The current dependency revisions and audit coverage checked are:

```text
hc7_common_root_short_trace_classification.md
  dc57ab0da71b46cf0e6e878f0f0612aa7ed2698b5227a527a806ec9091a83670

hc7_common_root_five_reserve_kempe_packet.md
  8471ee1cd4e82cf6e6906a4be0762c75df69ca0e09be76034c810d17e0f101cf

hc7_common_root_exclusive_reserve_response.md
  5d7e6a8520744fc6e4458a74fce2a41fe5fa04567b009b0860ccd30d1e230f19

hc7_order8_root_connector_reflection.md
  15f6fe1052426a0ccc0ee96a02d377370acfc00f0826d73c7ba5f1076106ddcc
```

The short-trace classification and concentrated-response sources match
the exact hashes in their GREEN audits.  The five-reserve and reflection
sources match the status-only promoted hashes recorded in their GREEN
audits; their mathematical statements and proofs are unchanged from the
audited revisions.

## Unresolved scope

No internal gap was found in the claimed elimination or in its degree-nine
extension.  The conclusion remains conditional on the tight atomic
common-root setup, full proper-minor six-colourability, the neighbourhood
independence bound, and the two full exterior components.

The forced `R`-rooted `K_5` may use both shores.  The theorem does not
reserve an `I`-connected seventh branch set, construct a `K_7`-minor model,
produce a bounded separation or strict descent, close the remaining
common-root programme, or prove `HC_7`.

The status-only promotion linking this audit has SHA-256
`55b2d8fb8c3732d25a81da541b0752580e6bee467b5090788c5071cabda2c930` and
makes no mathematical change to the audited revision.
