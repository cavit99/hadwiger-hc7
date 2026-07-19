# Independent audit of the `K_2`-planar first-hit exposure barrier

**Verdict:** **GREEN** at the exact source and verifier revisions recorded
below.  The construction is seven-connected and `K_7`-minor-free, its five
terminal classes are nonempty, pairwise disjoint and connected, and the
selected two labels have clean first-hit rank zero although the corresponding
source component has a literal host neighbourhood of order twelve.

This is a separate internal mathematical audit, not external peer review.

## Exact revisions audited

```text
3740bb30892da5e38c3baa3b851dd307a349576c7e61d41a96daaf0927ba8835  barriers/hc7_labelled_first_hit_k2_planar_exposure_barrier.md
831c6ff0f885d1977e101260c5a7302e9d825e33746dd3c845b6765a2a02b41d  barriers/hc7_labelled_first_hit_k2_planar_exposure_barrier_verify.py
```

The source was corrected during audit: the subgraph called `C` is a
five-wheel, not a star.  The five selected sources are its rim vertices.
The hashes above identify the corrected revision.

## 1. The edgewise-subdivided icosahedron

The icosahedron has twelve vertices, thirty edges and twenty triangular
faces.  Subdividing every edge adds thirty midpoint vertices.  The two
half-edges replacing each original edge contribute sixty edges, and the
central triangle in each original face contributes another sixty.  Thus the
constructed planar triangulation `J` has 42 vertices and 120 edges.

For an old vertex `v`, the five midpoints on its incident edges induce a
five-cycle, because consecutive incident edges lie in a common original
face.  Together with `v` they form the five-wheel `C`.  Its external
neighbourhood alternates between the five old neighbours of `v` and the five
midpoints on the edges joining consecutive old neighbours.  These ten
vertices induce the displayed ten-cycle `W`, and direct inspection gives

```text
N_J(C)=W.
```

There are 26 vertices outside `C union W`, so two distinct singleton
terminals `t_1,t_2` can be chosen there.

The deterministic verifier reconstructs this graph and exhaustively checks
that deleting any set of at most four vertices leaves it connected.  This
proves the asserted five-connectivity of `J`.  The verifier also confirms
the vertex and edge counts, the orders of `C` and `W`, and the displayed
neighbourhood equality.  Planarity follows directly from the face-by-face
subdivision of the fixed planar icosahedral embedding.

## 2. Connectivity and minor exclusion in the join

Let `G=K_2 vee J`, with universal adjacent vertices `a,b`.  After deletion
of at most six vertices, either one of `a,b` remains and joins all remaining
vertices, or both are deleted and at most four vertices were deleted from
the five-connected graph `J`.  Hence `G` is seven-connected.  Conversely,
deleting `a,b` and the five neighbours in `J` of any old icosahedral vertex
isolates that vertex, so the connectivity is exactly seven, as reported by
the verifier.

If `G` had a `K_7`-minor model, at most two branch sets could contain `a` or
`b`.  At least five branch sets would therefore lie wholly in `J`; their
pairwise adjacencies would form a `K_5`-minor model in `J`.  This is
impossible because `J` is planar.  The minor exclusion is thus established
by the written argument rather than by a bounded minor search.

## 3. Terminal classes, rank and literal exposure

The five source vertices are the five rim vertices of `C`.  The terminal
classes

```text
{t_1}, {t_2}, {a}, {b}, W
```

are nonempty, pairwise disjoint and connected.  In the clean first-hit
network all terminal vertices are forbidden as path interiors.  Removing
their union leaves `C` as a component containing every source: its only
host neighbours are the ten vertices of `W` and the two universal vertices
`a,b`, all belonging to the three unselected terminal classes.  In
particular, a path from a source to `t_1` or `t_2` must first meet an
unselected terminal.  No clean path to either selected label exists, and

```text
r_P(T_1 union T_2)=0.
```

The empty set is consequently a minimum relative separator.  In the host,
however,

```text
N_G(C)=W union {a,b},
```

of order twelve.  This verifies the claimed failure of the static lift from
a relative first-hit deficiency to an order-seven host separator.

## 4. Verifier and trust boundary

Running

```text
python3 barriers/hc7_labelled_first_hit_k2_planar_exposure_barrier_verify.py
```

at the audited revision prints exactly the expected four lines.  It checks
the combinatorial construction, five-connectivity of `J`, all relevant
sets and neighbourhoods, and the isolated source component.  The written
proof, not the script, supplies the planarity implication excluding a
`K_7` minor.

The graph is six-colourable because `J` is planar and the two universal
adjacent vertices can receive two new colours.  It is therefore not a
hypothetical counterexample to `HC_7` and carries neither the selected
proper-minor response nor contraction-critical transition data.  The
example refutes only principles attempting to control omitted-label
exposure from connectivity, `K_7`-minor exclusion and connected terminal
classes alone.  Within that stated scope, no gap remains.
