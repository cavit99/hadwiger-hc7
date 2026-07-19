# Independent internal audit: strict reversal at an order-eight boundary

**Verdict:** **GREEN** for Lemma 1.1, Theorem 2.1, and Corollary 3.1
within the exact trust boundary stated below.  This is an internal
mathematical audit, not external peer review.  The result does not prove
`HC_7`.

## Audited revision

This audit checks the complete source file
[`hc7_order8_strict_reversal_completion.md`](hc7_order8_strict_reversal_completion.md)
at SHA-256

```text
1aa7c959a181b8d86075eb5c2822c5328c2438c5f2e4f47c0ee8c2a3bb18c059
```

This is the promoted `results/` revision of the source previously audited
at SHA-256

```text
db9e1ee90fd58fca330d503ab5d8d01215742ce883753867b0a904d55a59e615
```

The promotion changed only status and repository-path metadata.  The
theorem statements, proofs, dependency roles, and trust boundary are
mathematically unchanged.  The complete promoted source was compared with
the sections audited below before carrying the GREEN verdict to the current
hash.

The current promoted paths and hashes of the three mathematical
dependencies are:

```text
69a63c7899081defb83a15d838e636d6eb5dc96cdc1b0bf5a66ee029c0beafd7
  results/hc7_order8_two_defect_clique_oct_reflection.md
c973d105dd9441840de98bf9ebf0c7a362a76f4980400ea3a9e403bd5b116560
  results/hc7_order8_overlapping_interval_normal_form.md
1d976b6ece78b66c08a87df36cfc3f31a3e8511d57aa6990aeaa28c7c67c76b3
  results/hc7_order8_three_component_boundary_classification.md
```

Each dependency has its own adjacent audit.  This promotion repin does not
alter or enlarge those separate verdicts.

No unresolved assumption or gap remains in the displayed statements.

## 1. Lemma 1.1: the seven branch sets

Let `C` be the cycle in `S-{d,e}`.  Since `|S|=8` and `|C|<=5`, the
choice

```text
w in S-(V(C) union {d,e})
```

is always possible.  The three branch sets obtained from `C` use exactly
the vertices of `C`; a cyclic partition into three nonempty intervals
gives three connected pairwise adjacent sets for cycles of orders three,
four, and five.

The four remaining displayed sets are connected:

- `Q_0 union {w}` is connected because `Q_0` is boundary-full;
- `Q_1` is connected by hypothesis;
- `A_d union {e}` is connected because `e!=d` and `A_d` meets every
  boundary vertex except `d`; and
- `A_e union {d}` is connected symmetrically.

They are disjoint from one another and from the cycle branch sets because
the four given subgraphs lie outside `S`, are pairwise disjoint, and the
three anchors `w,d,e` are distinct and avoid `C`.

All twenty-one required adjacencies were checked explicitly.  Among the
first four branch sets, the six adjacencies are supplied by the edge from
`Q_1` to `w`, the edges from each boundary-full subgraph to `d,e`, and the
assumed edge between `A_d` and `A_e`.  There are six adjacencies from the
two boundary-full subgraphs to the three cycle sets and six from the two
one-defect subgraphs to the three cycle sets.  The latter are present
because the cycle avoids both missed vertices.  The final three
adjacencies are those of the `K_3` model obtained from the cycle.

Thus the displayed sets form an explicit `K_7`-minor model.  The
consequence for a nonbipartite graph on the six vertices `S-{d,e}` is
also exact: a shortest odd cycle has order three or five.

## 2. Theorem 2.1: direct colouring of the path side

The boundary partition

```text
X | Y | {d,e}
```

is proper.  The bipartition makes `X,Y` independent, and the theorem
assumes that `d,e` are nonadjacent.  Assigning three distinct colours to
these three blocks and using three disjoint colours on the three-colourable
component `P` is therefore a proper six-colouring of `G[P union S]`.
Using disjoint palettes makes every edge between `P` and `S` proper.  The
restriction to `S` is exactly the displayed equality partition.

## 3. Theorem 2.1: proper-minor contractions

For fixed distinct `i,j in {0,1}`, the three sets

```text
A_d union X,
A_e union Y,
Q_j union {d,e}
```

are pairwise disjoint and connected.  Every member of `X` has a neighbour
in `A_d`, every member of `Y` has a neighbour in `A_e`, and boundary
fullness connects both `d,e` through `Q_j`.  Each contraction contracts at
least one edge, so their simultaneous contraction is a proper minor of
`G`.

The three contraction images form a triangle:

- the first two are adjacent through the assumed edge between `A_d` and
  `A_e`;
- the first is adjacent to the third through an edge from `A_d` to `e`;
  and
- the second is adjacent to the third through an edge from `A_e` to `d`.

Consequently every six-colouring of the proper minor assigns three
distinct colours to these images.  Pulling such a colouring back only to
the untouched closed side `G[Q_i union S]` is legitimate.  All vertices
of `X` receive the first image colour, all vertices of `Y` the second, and
both `d,e` the third.  Edges within the three blocks are absent, edges
between different blocks have distinct endpoint colours, and every edge
from the boundary to `Q_i` was represented by the corresponding
contraction image.  The resulting boundary equality partition is exactly

```text
X | Y | {d,e}.
```

Repeating this construction with the two choices of `i` gives compatible
boundary partitions on both remaining component sides.  Since the three
block colours are distinct, a permutation of the six colour names aligns
each side with the direct colouring of the `P` side.  The three components
of `G-S` are pairwise anticomplete, so the aligned colourings glue to a
proper six-colouring of `G`.

This argument never identifies a palette colour with a branch-set label.

## 4. Corollary 3.1: import from the path normal form

In the strict-reversal case the audited path normal form has indices
`b<a`.  If none of its three distinguished subpaths has already returned
an order-seven separation, the two tails have exact boundary contact sets
`S-{d}` and `S-{e}`.  For any `b<=k<a`, the sets

```text
P[0,k]  and  P[k+1,m]
```

are nonempty, connected, disjoint, adjacent, and cover `P`.  The first
contains the full left tail and cannot meet `d` because `k<a=ell(d)`; the
second contains the full right tail and cannot meet `e` because
`k>=b=r(e)`.  Hence their boundary contact sets are exactly `S-{d}` and
`S-{e}`.  The other two components supply the required boundary-full
subgraphs.

The hypotheses of the audited three-component boundary classification
are all present: every proper minor is six-colourable, `G` itself is not,
`G` has no `K_7` minor, and the three components are boundary-full.  Its
universal conclusion therefore gives two vertex-disjoint odd cycles in
`G[S]`.

If `G[S-{d,e}]` is nonbipartite, Lemma 1.1 applies.  Otherwise every one
of the two disjoint odd cycles meets `{d,e}`; disjointness forces them to
meet different vertices.  Removing that distinguished vertex from either
odd cycle leaves a nonempty path of odd length, so both classes of the
bipartition of `G[S-{d,e}]` are nonempty.

When `de` is present, all hypotheses of the separately audited
adjacent-defect reflection theorem hold, with the path component as one
open shore and the union of the two full components as the other.  That
theorem six-colours `G`.  When `de` is absent, Theorem 2.1 applies because
the induced path is two-colourable.  Both alternatives contradict the
counterexample hypotheses.

The contradiction shows that at least one of the three distinguished path
subintervals returned one of the actual order-seven separations described
by the audited normal form.  The corollary does not assert that the two
closed shores induce a common boundary colouring on that separation.

## 5. Adversarial checks and trust boundary

The audit specifically tested the possible failure modes most likely to
invalidate the argument:

- no boundary vertex is used twice in Lemma 1.1, including for a
  five-cycle;
- no contraction in Theorem 2.1 identifies adjacent vertices that are
  later assigned one colour outside the contracted block;
- pulling a minor colouring back does not require colouring either of the
  two contracted-away open components;
- the direct colouring of `P` uses a palette disjoint from all three
  boundary colours;
- three equality partitions can be aligned by colour permutations even
  if interior vertices reuse boundary colours;
- the normal form supplies exact one-defect contact sets, not merely lower
  bounds; and
- the finite classification is used only for its audited two-disjoint-odd-
  cycle conclusion.

No counterexample or hidden assumption was found.

The GREEN verdict is confined to an order-eight boundary with exactly
three boundary-full components, one of which is the entire induced path in
the audited strict-reversal normal form.  It does not cover:

1. a shared portal at an endpoint or any other shared-portal residue;
2. a selected component with vertices outside the path;
3. an order-eight interface with only two complementary components;
4. compatibility of the colourings on the returned order-seven
   separation; or
5. any complete proof of `HC_7`.
