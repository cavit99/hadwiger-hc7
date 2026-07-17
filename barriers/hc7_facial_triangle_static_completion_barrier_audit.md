# Independent audit: facial-triangle static-completion barrier

**Verdict:** **GREEN** as a computer-assisted counterexample to the narrow
static inference stated in the source note.  The example does not satisfy
the seven-connectivity or proper-minor criticality hypotheses of the live
`HC_7` problem, and therefore is not an `HC_7` counterexample.

## Audited revision

This audit checks exactly:

- `hc7_facial_triangle_static_completion_barrier.md`, SHA-256
  `b6e806a23f5258b89241601e3d84e4462a04875a1dbab2ec194a55301e338615`;
- `hc7_facial_triangle_static_completion_barrier_verify.py`, SHA-256
  `c4f828c1959e977873a88d0f8a762caafaa5d3b0a00cbbcb5f1a17dae28636ad`;
- the imported exact-minor and linkage implementation in
  `hc7_balanced_order8_two_missing_colour_paths_verify.py`, SHA-256
  `792d6108748c255966424abd2c6649a0a30fe0fe3437898633e5d4ef90092ad8`.

Any change to the source note, its verifier, or the imported solver requires
a new audit or an explicit hash update after rechecking the affected claims.

## Reproduction

From the repository root I ran

```text
PYTHONPATH=active/runtime/deps \
python3 barriers/hc7_facial_triangle_static_completion_barrier_verify.py
```

with NetworkX 3.6.1 and Z3 4.15.4.  It completed successfully and reported

```text
VERIFIED
vertices 16 edges 49
host connectivity 3
quotient connectivity 3
K7 minor False
```

## Independent checks

### Construction and boundary data

Direct reconstruction gives 16 vertices and 49 edges.  Deleting the
eight-vertex boundary leaves exactly the two anticomplete connected
components `C={a,b,w}` and `D={y0,...,y4}`.  Each component has a neighbour
at every boundary vertex.  The sets `R union {a,b}` and `D` are disjoint
five-cliques.  The edge `e` is anticomplete to `a` and collectively adjacent
to `R union {b}`; the symmetric assertion holds for `f` and `b`.  For each
of `e` and `f`, the two endpoint nonneighbour sets in `R` are nonempty and
disjoint.

The four displayed complement edges are pairwise disjoint and cover all
eight boundary vertices, so they are indeed a perfect matching of the
boundary complement.  The verifier additionally computes a maximum
matching of size four.

### Fixed-boundary critical triangle

After deleting `ab`, the six displayed colour classes cover every vertex
and are independent.  For each of `a,b,w`, the colours seen on the boundary
are exactly `{2,3,4,5}`.  Its available list is therefore exactly `{0,1}`.
The induced graph on `a,b,w` is `K_3`, which is not colourable from that
common two-element list, while each proper induced subgraph is.  Thus it is
the claimed vertex-minimal fixed-boundary list-critical core, not merely an
unrelated triangle.

The one-vertex remainder `A={w}` is connected.  Both `a` and `b`, as well as
`x`, are adjacent to it; it has a neighbour in each of `e` and `f`; and its
only missed boundary vertices are `r1` and `f0`.  These checks establish the
stated zero-slack contact pattern.

### Rooted quotient and facial location

Deleting `R` and contracting `e` and `f` gives the stated quotient `Q`.
NetworkX computes vertex-connectivity three.  The linkage routine is exact
for this finite graph: it enumerates every simple path for the first pair,
deletes its vertices, and tests the second pair for connectivity.  It finds
the `(ab,z_ez_f)` and `(az_f,bz_e)` linkages and excludes the
`(az_e,bz_f)` linkage.

The usual Two Paths web theorem therefore gives an
`(a,b,z_e,z_f)`-web completion.  The deduction that `abw` is the bounded
facial triangle is sound but is theorem-level rather than an embedding
computed by the verifier.  The vertex `w` is adjacent to all four outer
roots, so it cannot belong to a clique attached behind a three-vertex face
and must be a skeleton vertex.  The triangle `abw` is nonseparating in `Q`,
as the verifier checks.  An attachment clique cannot reconnect two
components of the skeleton after deleting `a,b,w`; hence the skeleton
triangle is also nonseparating.  Since `ab` is an outer edge and every
bounded skeleton face is triangular, `abw` is its unique incident bounded
facial triangle.

The set `{y0,y1,x}` disconnects `Q` and does not contain both contracted
edge vertices.  Together with three-connectivity, this is an exact
three-cut and is precisely the failure of the cut-rigidity hypothesis
identified in the source note.

### Exact `K_7`-minor exclusion

The reused Z3 flow formulation is sound.  It partitions every host vertex
among seven nonempty branch sets.  In each branch set, the least-indexed
member supplies `|B|-1` units of nonnegative integral flow and every other
member consumes one unit, with flow allowed only across internal edges.
This is feasible exactly when the branch set is connected.  The remaining
constraints demand an edge between every pair of branch sets, and ordering
their least members removes only label symmetry.

Restricting to spanning models is harmless because the host is connected:
each component outside a minor model can be absorbed into an adjacent
branch set without losing connectedness or any branch-set adjacency.  The
solver returned `UNSAT` on the 16-vertex host.  Positive controls returned
`SAT` on `K_7` and `UNSAT` on `K_6`.

As an independent cross-check, I used a second Z3 encoding with one root in
each branch set and integer levels: every nonroot member must have an
internal neighbour at a strictly smaller level.  With the same spanning
partition and pairwise-adjacency requirements, this independent
connectivity formulation also returned `UNSAT`.  The minor exclusion thus
does not depend on the flow encoding alone.

## Exact trust boundary

The checked conclusion is only that the listed static boundary contacts,
the two named five-cliques, the abstract rooted-web obstruction, and a
common-list facial critical triangle do not by themselves force a `K_7`
minor.  The host has vertex-connectivity three, is six-colourable, and hence
is not a 7-contraction-critical graph.  Its quotient has the forbidden
three-cut displayed above.  It does not refute any completion theorem that
uses seven-connectivity, the corresponding cut rigidity, or incompatible
colouring transitions supplied by proper-minor criticality.  The source
note states these limitations accurately.
