# Independent audit: ordered two-three-terminal path barrier

**Verdict:** **GREEN.**  The displayed graph is seven-connected and
`K_7`-minor-free, yet the two nominated ordered triples cannot be carried by
two vertex-disjoint paths.  It refutes only the connectivity-and-minor
exclusion assertion stated in the source; it is not a counterexample to
`HC_7`.

Audited source:
[`hc7_p3_union_p3_linkage_barrier.md`](hc7_p3_union_p3_linkage_barrier.md).

Source SHA-256:

```text
14636f42f7b3dfbfb53cb03a81dbe5fefce11daa904ed43b9dee401f252fe3f1
```

After that audit, the source status line was updated only to record this
GREEN audit and link back to this file.  No mathematical statement, proof,
construction, or trust boundary changed.  The resulting source SHA-256 is:

```text
3233bceb139184d91a9ab58330f08557d5e50aecc1bd088a3fdac7f875cfa779
```

Audited verifier:
[`hc7_p3_union_p3_linkage_barrier_verify.py`](hc7_p3_union_p3_linkage_barrier_verify.py).

Verifier SHA-256:

```text
eb3f361366a96803ad41b739cc2583a4238d05ff06cfff586babcbc19ef08d83
```

After the audit, one redundant blank line at end of file was removed.  The
executable code is byte-for-byte unchanged apart from that trailing
whitespace, and the resulting verifier SHA-256 is:

```text
8445d1363ccc49289d62119fb205a4283c84dc655772cfe45f3f4577fe110a01
```

The verifier was rerun at those hashes with

```bash
PYTHONPATH=active/runtime/deps python3 barriers/hc7_p3_union_p3_linkage_barrier_verify.py
```

and returned the expected final line `certificate=PASS`.

## 1. The planar core

The twenty triples in (2.1) have the required icosahedral incidence.  The
construction adds the sixty vertex--face incidence edges and the thirty
edges between faces sharing an icosahedron edge.  Before the deletion this
gives a simple plane triangulation on 32 vertices and 90 edges.  The faces
indexed zero and one are exactly the two faces containing the edge `01`, so
they are adjacent in the construction.

Deleting `h_0h_1` leaves 32 vertices and 89 edges.  The independent
planarity check returns 58 triangular facial walks and one quadrilateral
facial walk.  Up to rotation and reversal, that quadrilateral is

```text
p0,h1,p1,h0.
```

The count is also consistent with Euler's formula: the 59 facial lengths
satisfy `58*3+4=2*89`.

The verifier exhausts all

\[
             \sum_{i=0}^4 {32\choose i}=41,449
\]

vertex deletions of order at most four, and every remainder is connected.
Thus `kappa(H)>=5`.  After the deleted edge, the neighbours of `h_0` are

```text
h2,h7,p0,p1,p5.
```

Deleting those five vertices isolates `h_0` from a nonempty 26-vertex
component.  Hence `kappa(H)<=5`, proving `kappa(H)=5`.  The verifier also
checks directly that the minimum degree is five; the proof does not use
minimum degree as a substitute for the exhaustive lower-bound check.

## 2. Connectivity of the join

Let `G=K_2\vee H`, with universal adjacent vertices `a,b`.  Any separating
set of `G` must contain both `a,b`; otherwise the surviving universal vertex
joins every remaining vertex.  Once both are deleted, the remaining set
disconnects `G` exactly when its intersection with `H` disconnects `H`.
Consequently

\[
                         \kappa(G)=2+\kappa(H)=7.
\]

Both open sides are nonempty when a minimum five-cut of `H` is lifted, so
the upper bound is a genuine separation and not merely an isolation
convention.

## 3. Complete audit of the `K_7`-minor exclusion

Suppose that seven disjoint connected branch sets form a `K_7`-minor model
in `G`.  Classify the model by the number of its branch sets which meet
`{a,b}`.

* If two distinct branch sets meet `a,b`, replace those two branch sets by
  the corresponding universal singletons.  The five remaining branch sets
  lie in `H` and form a `K_5`-minor model there.
* If exactly one branch set meets `{a,b}`--including the case in which that
  one branch set contains both universal vertices--the other six branch
  sets lie in `H` and form a `K_6`-minor model there.
* If no branch set meets `{a,b}`, all seven branch sets lie in `H`.

The same classification covers a universal vertex omitted from the model;
there is no additional case hidden by the singleton replacement.  Each
outcome gives at least a `K_5` minor in the planar graph `H`, which is
impossible because every minor of a planar graph is planar.  Therefore `G`
is `K_7`-minor-free.

## 4. Ordered paths and the facial obstruction

Assume two vertex-disjoint paths carry the ordered triples

\[
                         (a,p_0,p_1),\qquad(b,h_1,h_0).
\]

A path is simple.  Hence the `p_0`--`p_1` segment of the first path cannot
revisit `a`; it cannot use `b` because `b` lies on the disjoint second path.
It is therefore a path in `H`.  Similarly, the `h_1`--`h_0` segment of the
second path avoids `a,b` and lies in `H`.  The two extracted segments remain
vertex-disjoint.  In particular, the first segment avoids `h_1,h_0` and the
second avoids `p_0,p_1`.

In the fixed plane embedding, draw an open arc through the interior of the
quadrilateral face from `p_0` to `p_1`.  Its union with the simple
`p_0`--`p_1` path is a Jordan curve.  The two boundary arcs between its
endpoints contain `h_1` and `h_0`, respectively, so those vertices lie on
opposite sides of the curve.  An embedded `H`-path cannot cross the added
open facial arc: the face interior contains no edge of `H`.  It therefore
must meet the `p_0`--`p_1` path, contradicting vertex-disjointness.  This
proves the claimed absence of the ordered path pair.

## 5. Verifier audit and trust boundary

### `build_core`

**Purpose and inputs.**  This deterministic function has no external input.
It creates the 12 vertex-nodes, the 20 face-nodes, all literal incidence and
shared-edge adjacencies, checks that `h0h1` exists, and deletes exactly that
edge.

**Outputs and invariants.**  It returns one simple undirected graph.  The
important invariants are: all 32 named vertices are present; a `p`--`h` edge
is present exactly for the listed incidence; an `h`--`h` edge is present
exactly for a two-vertex face intersection; and the only deliberate deletion
is `h0h1`.  The pairwise face loop tests every unordered pair once, so no
adjacency class is skipped or double-counted.

### `facial_walks`

**Purpose and inputs.**  Given the constructed graph, the function obtains
a combinatorial plane embedding from NetworkX, asserts planarity, and marks
directed half-edges while traversing faces.

**Outputs and invariants.**  Every directed half-edge occurs in exactly one
returned facial walk.  Marking during `traverse_face` prevents a face from
being returned twice.  This check establishes the facial structure of one
valid embedding; five-connectivity also makes the planar embedding unique up
to reflection, so the alternating facial order is not an artefact of an
arbitrary embedding choice.

### `main`

**Purpose and inputs.**  This is the only executable entry point.  It has no
untrusted input or state and performs a finite deterministic certificate
check.

**Outputs and effects.**  It writes no files and mutates only temporary graph
copies.  It checks the exact vertex and edge counts, minimum degree, all
vertex deletions through order four, planarity, uniqueness of the
nontriangular facial walk, and the quadrilateral's cyclic order.  It prints
the fixed certificate summary only after every assertion succeeds.

**Dependencies and risks.**  The sole external dependency is NetworkX's
graph, connectivity, and planarity implementation.  The exhaustive cut
loop independently checks connectivity rather than relying on a single
reported connectivity value.  The face check accepts rotations and reversal
instead of depending on an embedding orientation.  The verifier does not
check the join's `K_7`-minor exclusion or the Jordan-curve argument; those
are unbounded mathematical deductions audited in Sections 3 and 4 above,
and the source states that computational trust boundary accurately.

The example is not seven-chromatic and no contraction-criticality claim is
made.  Thus it blocks only a generic seven-connectivity plus
`K_7`-minor-exclusion linkage theorem.  It does not block a theorem using
the proper-minor colouring responses or labelled branch-set data available
in the live `HC_7` configuration.
