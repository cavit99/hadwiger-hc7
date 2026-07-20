# Independent audit of the canonical type-5 minimum-degree theorem

**Verdict: GREEN** for theorem revision
`61fab69783f1f10bdb89f875e4ac9fc06e9e1d3c0edb445bcfa89bdfa7ad96f4`.

This separate internal audit checked the exact files

- theorem:
  `hc7_pentagonal_bipyramid_type5_minimum_degree_alignment.md`, SHA-256
  `61fab69783f1f10bdb89f875e4ac9fc06e9e1d3c0edb445bcfa89bdfa7ad96f4`;
- verifier:
  `hc7_pentagonal_bipyramid_type5_minimum_degree_alignment_verify.py`,
  SHA-256
  `493af68bb7f2d7674b2f6260bf744395f09ad02b6f11466aac7d3616ae3b5a62`.

The audit is GREEN only for the displayed canonical pole--rim orbit.  It
does not reinstate the deleted claim that every pole--rim type-5 enlargement
is equivalent to that graph.

## 1. Canonical graph and allowed supergraphs

With `a=0`, `b=1`, `c_0=2`, and `c_1,...,c_4=3,...,6`, the edge list in
(1.1) agrees exactly with one instance produced by the exact type-5
generator.  Deriving the allowed additional edges directly from the seven
parts and the pentagonal-bipyramid quotient gives precisely the nine edges
in (3.1), with no omission or extra edge.

In the displayed graph,

\[
             N(c_2)=\{a_1,b,c_1,c_3\}.
\]

Among the nine allowed missing edges, only `a_0c_2` is incident with
`c_2`.  Hence minimum degree at least five forces that edge exactly as
claimed.

## 2. Explicit minor model and roots

After adding the forced edge, the five bags

\[
 \{b\},\quad \{d_0,d_1\},\quad \{c_1\},\quad
 \{a_0,c_2\},\quad \{a_1,c_3\}
\]

are disjoint and connected.  Their ten adjacencies are witnessed by

```text
bd1, bc1, bc2, bc3, d0c1,
d0a0, d1a1, c1c2, c1a1, a0a1.
```

The edge `c_2c_3` is an alternative witness for the final adjacency.  The
bags containing `b,c_1,c_2,c_3` meet both nominated root sets, and the whole
`d`-fibre contains either selected `d`-root.  Thus the same five bags work
for all sixteen ordered choices of the two nominated root sets.

## 3. Reproduction of the finite check

Running the pinned verifier produced

```text
GREEN type-5 minimum-degree alignment: 35 supergraphs, 16 roots each
```

and exited with status zero.  It enumerates all `2^9=512`
part-respecting supergraphs.  On nine vertices, testing connectedness after
deleting every set of zero through four vertices is exactly the test for
vertex-connectivity at least five.  Exactly 35 supergraphs pass, each
contains the forced edge, and the explicit model is checked against all
sixteen root choices.  An independent recomputation also returned 35.

## 4. Trust boundary

Exact generation gives forty labelled pole--rim type-5 instances in two
degree-multiset classes of twenty:

\[
 (3,3,4,4,4,4,4,5,5),\qquad
 (3,4,4,4,4,4,4,4,5).
\]

The displayed graph is in the first class.  Since degree multiset is an
isomorphism invariant, the second class is not obtained from it by the
relabellings asserted in the rejected earlier corollary.  The theorem's
repaired scope statement is therefore necessary and correct.

The result remains a fixed nine-vertex theorem.  It does not lift an
abstract Hegde--Thomas enlargement minor to prescribed host branch sets,
preserve the two nominated root-contact sets, or make the path representing
the forced quotient edge avoid other labelled branch sets.  No such
relative conclusion was used in this audit.
