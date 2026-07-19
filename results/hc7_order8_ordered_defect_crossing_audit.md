# Independent audit: ordered crossings of the deficient connected subgraphs

**Verdict:** **GREEN** for Theorem 2.1, Corollaries 3.1 and 4.1, and the
stated scope of the three-edge obstruction in Section 5.  This is a separate
internal mathematical audit, not external peer review.  The result is
conditional and does not prove `HC_7`.

## Audited revision

This audit checks the complete source file
[`hc7_order8_ordered_defect_crossing.md`](hc7_order8_ordered_defect_crossing.md)
at promoted SHA-256

```text
434efeab93a4f693d212b4ee434532e81647df775a69494384ffcb3349735dde
```

The mathematical text is identical to the independently audited revision
`bf8d4e5f686b3cb37a1bb3a24e959268f39e9bf732e9da52b1038d8449ced20d`;
the promoted revision changes only the status line to link this audit.

No unresolved mathematical gap was found at this revision.

## 1. The two explicit `K_7`-minor models

Suppose first that a root connector `D` is disjoint from `A_e`.  The seven
sets in (2.1) are pairwise disjoint: the two subgraphs in `R` are disjoint
from the boundary and from `L`; the five displayed boundary vertices are
distinct; `A_d,A_e` are disjoint; and the only permitted overlap among the
listed `L`-subgraphs is between `D` and `A_d`, which occur in the same branch
set.  The sixth branch set is connected through `x_e`.  The seventh is
connected through `e`, since both `A_d` and `D` have a neighbour at `e`.

Every required adjacency is present:

- `P_0,P_1` are adjacent to each other, and their boundary fullness makes
  each adjacent to all five remaining branch sets;
- `d,x_d,y_d` form a triangle;
- `A_e` is adjacent to `d,x_d,y_d` by (1.2);
- `D` supplies the seventh branch set's adjacency to `d`, while `A_d`
  supplies its adjacencies to `x_d,y_d`; and
- the last two branch sets are adjacent through the stipulated
  `A_d`--`A_e` edge (independently also through `e x_e`).

Thus (2.1) is a valid explicit `K_7`-minor model.  The reverse orientation
in (2.2) is equally valid: `A_d union {x_d}` is connected; the final branch
set is connected through `d`; `e,x_e,y_e` form a triangle; `A_d` supplies
the sixth branch set's three triangle contacts; `D` and `A_e` supply the
final branch set's contacts; and the two large branch sets are adjacent
through the `A_d`--`A_e` edge (independently also through `d x_d`).  No
adjacency in either construction relies on an unstated edge.

These two orientations prove precisely that every root connector meets both
named deficient connected subgraphs.  The argument permits `D` to meet one
of them; that intersection is correctly absorbed into a single branch set.

## 2. Path order

If a `d`--`A_d` path in `G[L union {d}]` avoided `A_e`, adjoining its
internal vertices to `A_d` would give a connected subgraph in `L` adjacent
to `d` through the path and to `e` through (1.2), while remaining disjoint
from `A_e`.  This contradicts Theorem 2.1.  The symmetric argument proves
the `e`--`A_e` assertion.

Because `d e` is absent, the internal vertices of every `d`--`e` path with
interior in `L` form a nonempty connected root connector.  They therefore
meet both `A_d,A_e`.  An initial encounter in `A_d` would contradict the
first path assertion, and a final encounter in `A_e` would contradict its
reverse-orientation counterpart.  Hence the claimed first-`A_e`,
last-`A_d` order is correct even when a path enters either connected
subgraph more than once.

## 3. Use of the merged-root Kempe theorem

The boundary partition `X | Y | {d,e}` uses exactly three colours, so a
six-colouring has exactly three boundary-absent colours.  Together with the
nonexistence of the split-root partition, these are exactly the hypotheses
used by the GREEN-audited merged-root Kempe theorem.  Its proof does not
need the extra global non-six-colourability hypothesis once these two
response assumptions are stated.  It supplies all three `d`--`e` paths in
one fixed colouring, with interiors in `L`, and says that two paths with
different private colours can meet only at a vertex of the common root
colour.

Corollary 3.1 therefore gives the asserted order on each path.  Coincident
first `A_e`-vertices or coincident last `A_d`-vertices are common vertices
of two differently indexed paths and hence have the common root colour.
No palette colour is identified with a branch-set label.

## 4. Scope of the three-edge obstruction

After trimming between a last visit to `A_e` and the next visit to `A_d`,
each passage has endpoints in the two deficient connected subgraphs and no
internal vertex in either.  Three vertex-disjoint edges constitute a valid
abstract passage system satisfying the pairwise-intersection restriction
vacuously.  Their union contains no nonempty connected subgraph outside
`A_d union A_e` adjacent to both, and a transversal of the three independent
edges has order at least three.  Thus the proposed passage-system dichotomy
really is false from the intersection rule alone.

The source correctly does **not** claim that this matching is realized in a
seven-connected, seven-contraction-critical, `K_7`-minor-free graph.  It is
only a sharp obstruction to deriving a two-vertex bottleneck or an outside
connector from the three trimmed paths without additional host-level
information.

## 5. Trust boundary

The audited result constrains every root connector and orders the three
Kempe paths for arbitrary shore size.  It does not construct an `X`/`Y`
support transversal in the opposite shore, synchronize two shore
colourings, return an order-seven separation, split either deficient
connected subgraph, or provide a strict descent.  Those exclusions in the
source accurately delimit what has and has not been proved.
