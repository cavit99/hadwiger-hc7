# Independent audit: three-vertex portal reversal barrier

**Verdict:** **GREEN** for Theorem 2.1, the exact exceptional classification,
the base and split-root colourings, the three Kempe paths, the subdivision
and two-contact variants, and the exact `K_7`-minor exclusions certified by
the adjacent verifier.  This is a separate internal mathematical and
computer-assisted audit, not external peer review.  The examples are not
counterexamples to `HC_7`.

## Audited revisions

This audit checks the complete mathematical source
[`hc7_order8_three_vertex_portal_reversal_barrier.md`](hc7_order8_three_vertex_portal_reversal_barrier.md)
at SHA-256

```text
15ca455c022c90fb3719c4a1341e792f77f4a2cf0725bf03b7598ebca0000290
```

The classified revision differs from the independently audited mathematical
source only in its status line and adjacent-audit link; the theorem,
examples, and verifier are unchanged.

and the complete deterministic verifier
[`hc7_order8_three_vertex_portal_reversal_barrier_verify.py`](hc7_order8_three_vertex_portal_reversal_barrier_verify.py)
at SHA-256

```text
d8aff574ca8ab4a054f4d58d18251fd97a1b74ad3c235b39e9ef1753e076ca5c
```

It was run from the repository root with

```text
PYTHONPATH=active/runtime/deps python3 \
  barriers/hc7_order8_three_vertex_portal_reversal_barrier_verify.py
```

and exited successfully with the exact output

```text
GREEN: three-vertex portal classification, exact reversal obstruction, three Kempe paths, subdivisions, and two-contact barriers verified
```

No unresolved mathematical or encoding gap was found at these revisions.
Three issues discovered during the audit were repaired before the pinned
revisions: the path-intersection sentence now retains the common endpoints,
the subdivided examples are each passed through the exact minor solver, and
the explicit closing-edge model is no longer placed after an early return.

## 1. Hypotheses inherited by the three-vertex part

A connected simple graph on three vertices is either a three-vertex path or
a triangle.  The assumed exact common portal gives one named vertex `v`,
and adjacency of `E` to every vertex of `S-{e}` makes all four portal sets
indexed by `W` nonempty.

The explanation of the pointwise `E`--`D` contact is valid in the intended
order-three application.  The three first internal vertices of the merged-
root Kempe paths lie in `E`, have three distinct private colours, and exhaust
its three vertices.  An `alpha`--`beta_i` path cannot next visit either of
the other two vertices of `E`, whose colours are different private colours.
Its next internal vertex therefore lies in `D`, so every vertex of `E` has
a literal neighbour in `D`.

The theorem itself states these contacts as hypotheses, so its proof does
not depend on reconstructing any additional colouring data.

## 2. The seven-branch-set construction

Suppose `w in W` and a nonempty proper connected `C subset E` satisfy
`v in C` and `N_E(w) intersect C` nonempty.  Then `F=E-C` is nonempty.  The
seven displayed sets

```text
P_0, P_1, {d}, {x_d}, {y_d}, C union {w},
V(D) union F union {e}
```

are pairwise disjoint: the first four connected subgraphs are disjoint and
outside `S`; `C,F` partition `E`; and the five displayed boundary vertices
are distinct, because `w in {x_e,y_e,x_0,y_0}`.

They are connected.  The sixth set is connected through an actual
`w`--`C` edge.  For the seventh, every vertex of `F` has a neighbour in
connected `D`, and `D` has a neighbour at `e`.

All twenty-one adjacencies are present:

- `P_0,P_1` are adjacent and their boundary fullness makes each adjacent
  to all five remaining sets through `d,x_d,y_d,w,e`;
- `d,x_d,y_d` form a triangle;
- `C union {w}` meets `x_d,y_d` through `v` and meets `d` because every
  vertex of `E` is adjacent to `d`;
- the final set meets `d` through any vertex of nonempty `F`, and meets
  `x_d,y_d` through `D`; and
- `C union {w}` meets the final set because every vertex of `C` has a
  neighbour in `D`.

Thus (2.3) is a literal, label-preserving `K_7`-minor model.

## 3. Exact classification of failure

If `E` is a triangle, a chosen portal `q in N_E(w)` either equals `v`, in
which case `{v}` works, or is adjacent to `v`, in which case `{v,q}` is a
proper connected two-vertex set.  If `E` is a path and `v` is its middle
vertex, the same alternatives work for every portal vertex.

It remains that `v` is one endpoint of a path `E=abc`, say `v=a`.  A portal
at `a` gives `C={a}` and a portal at the middle vertex `b` gives
`C={a,b}`.  The only portal vertex that forces the unique `a`--portal path
to use all of `E` is the opposite endpoint `c`.  Since each of the four
portal sets is nonempty, failure for every `w in W` is therefore equivalent
to

```text
N_E(w)={c} for every w in W.
```

Reversing the path accounts for the other orientation.  This proves that
the stated endpoint-reversal pattern is the exact exception, not merely a
necessary condition.

The verifier independently enumerates all four labelled connected graphs
on three vertices (the three labelled paths and the triangle), all three
choices of `v`, and all `3^4` selections of the four nonempty portal sets.
Every nonexceptional choice is accompanied by the explicit seven bags and
passed through `validate_model`.  Exactly six labelled survivors remain:
the three labelled paths and their two orientations.  Each has `v` as an
endpoint and all four selected portals at the opposite endpoint.  Allowing
larger portal sets creates no omitted case: selecting any portal at `v` or
the middle vertex triggers the same monotone explicit model, while a
nonempty set with neither is exactly the singleton opposite endpoint.

The verifier also validates explicit models after adding a middle portal or
the closing edge that turns the canonical path into a triangle.

## 4. The expanded barrier and its colourings

The expanded graph has exactly 17 vertices: eight boundary vertices, three
vertices in `E`, four vertices in the `D`-star, and `P_0,P_1`.  Direct edge
inspection confirms every static hypothesis:

- the boundary consists of the two displayed triangles and `d,e` have
  boundary degree two;
- `P_0,P_1` are adjacent and complete to `S`;
- the connected `D`-star is anticomplete to `d` and collectively adjacent
  to every vertex of `S-{d}`;
- `E=u_1u_2u_3` is a path, is anticomplete to `e`, and collectively meets
  all of `S-{e}`;
- every `u_i` sees `d` and the centre `z` of `D`; and
- `u_1` is the unique `x_d,y_d` portal while `u_3` is the unique portal for
  every vertex of `W`.

The colouring in (3.1) is proper on every edge.  Boundary triangles use
three colours, the `E`-path alternates among distinct private colours, the
`D`-star edges join `alpha` to private colours, each full vertex
`P_0,P_1` has a private colour absent from `S`, and their mutual edge has
different endpoint colours.

For each `i`, every edge of

```text
d-u_i-z-b_i-e
```

exists and the path uses exactly `alpha,beta_i`.  The three paths have the
common endpoints `d,e`; their internal vertex sets have intersection
exactly the common `alpha`-vertex `z`.  They therefore satisfy the stated
merged-root path data.

The split-root colouring (3.4) is also proper.  On the boundary it assigns
one colour to each named three-vertex class and distinct colours to `d,e`,
so it induces exactly `X | Y | {d} | {e}`.  The verifier checks the colouring
on the whole displayed graph after assigning two additional colours to
`P_0,P_1`.  This correctly identifies the live hypothesis absent from the
barrier: the split-root response is available rather than rejected.

## 5. Exact `K_7`-minor encoding

For every graph passed to `k7_model`, the SMT formula has seven indexed
branch sets.  Each host vertex is selected by at most one set, and every set
has exactly one root which is selected at depth zero.  Every selected
nonroot vertex has a selected neighbour in the same set at strictly smaller
nonnegative depth.  Iterating this decrease terminates at the unique root,
so each selected set is nonempty and connected.  Conversely, any connected
branch set can satisfy these constraints by rooting a spanning tree and
using tree distance as depth; the upper bound by the host order is harmless.

For every pair of branch sets, the formula requires a literal host edge
with one endpoint selected in each.  Thus a satisfying assignment is
exactly a `K_7`-minor model.  The increasing root-index constraints remove
only permutation symmetry: any unordered model can be reordered by its
seven distinct root indices.  They do not exclude a genuine model.

On satisfiable instances the decoded sets are independently checked for
nonemptiness, disjointness, connectedness, and all pairwise adjacencies.
Consequently an `unsat` result is an exhaustive finite exclusion with no
branch-set size bound or unverified virtual edge.

The solver returns `unsat` for the 17-vertex base graph.

## 6. Subdivision and two-contact variants

For one and two subdivisions of the edge `u_2u_3`, the verifier constructs
the stated path extensions, checks the extended proper colouring, retains
the three original Kempe paths, verifies that exactly `u_1,u_2,u_3` are
`d`-portals, and checks suppression back to the base graph.  More
importantly, both subdivided graphs are independently sent through the exact
SMT solver and return no `K_7` model.  The computer-assisted conclusion
therefore does not rely solely on an informal subdivision principle.

For each choice `u_i`, the two-contact variant adds the literal path
`z-r-z'` inside connected `D` and the edge `z'u_i`.  The displayed colouring
extends properly with `z'` coloured `alpha` and `r` a different colour.  The
original three Kempe paths remain unchanged.  Direct neighbourhood
calculation gives exactly two `D`-vertices adjacent to `E`, namely `z,z'`.
The verifier constructs and exact-solves all three choices independently;
each has no `K_7` minor.

## 7. Trust boundary

The examples are low-connectivity, are not contraction-critical, admit the
split-root colouring, and do not realize the incompatible operation-specific
boundary response required by the live branch.  The source does not claim
otherwise.  It establishes only that the listed static portal, contact, and
Kempe-path data do not by themselves close the endpoint-reversal case.

Within this exact scope, the mathematical classification and all certified
barrier claims are correct.
