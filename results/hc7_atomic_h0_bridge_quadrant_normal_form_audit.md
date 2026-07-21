# Independent audit of the atomic `H_0` bridge normal form

**Status:** separate internal audit GREEN, 21 July 2026.

This is an internal mathematical and computational audit, not external peer
review.

## Revisions audited

- theorem:
  [`hc7_atomic_h0_bridge_quadrant_normal_form.md`](hc7_atomic_h0_bridge_quadrant_normal_form.md)
- theorem SHA-256:
  `821e79b0a7fbe77a23a77ce15eddb1257c29ebf04d35d7f5c3b8ab0f2458ca0e`
- retained checker:
  [`hc7_atomic_h0_single_bridge_falsifier.py`](../active/hc7_atomic_h0_single_bridge_falsifier.py)
- checker SHA-256:
  `ba78a7f17e3685aeca3a4a4fd014f5cf8a69007d080e170ad2bd7158e09511a3`

The hashes were computed with `shasum -a 256` after the theorem status was
changed to GREEN.  The audited prerequisites were the already-audited atomic
rounding and octahedral-frame results.

## Verdict

GREEN.  The written bridge allocations, the exact 488-case classification,
the order-seven separation response, and the critical component-joining
argument are correct under their stated hypotheses.  The retained checker
was independently rerun with

```bash
.venv/bin/python -B active/hc7_atomic_h0_single_bridge_falsifier.py
```

and returned the documented GREEN output and counts.

## Checks performed

1. In Theorem 2.1 the initial `a`- and `b`-side segment pieces are disjoint
   because `ab` is not a segment.  Splitting the added `T`-path supplies the
   missing `ab` adjacency.  The connected set containing `c,x` and the
   `x`-side of `T_xd` supplies `cd`; every remaining pair is joined by its
   original segment.  The symmetric `cd` construction, using the set
   containing `a,x`, is also valid.  Endpoint and segment-interior cases do
   not create overlaps in either allocation.
2. The definition of a `T`-bridge covers both an off-`T` edge and a component
   of `G-V(T)`.  Any two attachments of a component bridge are joined by a
   `T`-path through that component.  Hence a `K_7`-minor-free bridge cannot
   contain both endpoint labels of `ab`, nor both labels of `cd`, proving the
   four-region confinement.  For a component bridge its attachment set is
   exactly its neighbourhood; connectivity gives seven or eight attachments,
   with the separately handled all-of-`V(T)` case still having at least the
   eight branch vertices.
3. The finite classification is exhaustive.  There are eight branch classes
   and 23 segment-interior classes, giving 465 pairs of distinct classes and
   23 same-segment cases.  Reversal of the two same-segment attachments is an
   isomorphism.  Subdivision of a bridge path or an unused segment interval
   changes no clique-minor conclusion; the retained interval vertices also
   cover the incident-branch and consecutive-attachment parallel-path cases.
4. The restricted-growth recursion enumerates every partition into seven
   nonempty sets.  It tests connectivity of each set and all 21 quotient
   adjacencies.  Since every clique-minor model in a connected graph extends
   to a spanning one by absorbing complement components, this is an exact
   `K_7`-minor oracle.  The independent model validator rechecks each positive
   certificate.  The rerun found exactly 96 terminal and 392 negative cases,
   with the displayed endpoint-type and planarizing-pair counts.
5. In every negative case, deletion of the selected pair among `ef,eg,fg`
   leaves a validated planar rotation system.  If the original graph had a
   `K_7` model, deleting the at most two branch sets containing the apices
   would leave a `K_5` model in that planar graph, a contradiction.  Thus the
   two-apex inference is valid independently of the negative oracle output.
6. Deleting the six literal vertices in Theorem 5.1 leaves a connected graph
   by seven-connectivity.  In the nonterminal case, the order-two form of
   Menger gives either one separating vertex or two internally disjoint
   paths.  The former combines with the six deleted vertices to give an
   actual order-seven cut; the latter paths must each meet `T` internally.
   With at most one internal vertex of `T`, their internal disjointness rules
   out the latter outcome.
7. Every component behind the order-seven cut is adjacent to every boundary
   vertex, since otherwise its neighbourhood has order at most six.  For a
   nonempty independent boundary set `I`, a full component together with
   `I` is connected and may be contracted in a proper minor.  Expanding `I`
   after six-colouring gives one exact boundary colour class; using a
   component on the other side gives the reverse closed-shore response.
8. In Lemma 6.1, consecutive visits of a path in `G-S` to distinct components
   of `H-S` delimit a path whose internal vertices avoid `H`; contracting it
   adds the required edge while retaining `H`.  For `K_{3,2,2,2}`, the
   displayed seven branch sets after adding an edge in the part of order
   three are connected and pairwise adjacent.  Therefore such a subgraph
   cannot persist in a seven-connected `K_7`-minor-free host.

## Trust boundary

The theorem classifies one bridge path and confines each whole bridge, but it
does not combine an arbitrary family of confined bridges.  In particular it
does not force a common planarizing pair, an ownership-preserving `xe`, `ab`,
or `cd` augmentation, or a strict response-preserving reduction.  It also
does not prove that a collision-minimal weak `K_7` immersion is atomic, the
single-collision terminal disjunction, or `HC_7`.
