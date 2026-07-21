# Two-apex exclusion for the atomic shared-hub graph

**Status:** computer-assisted finite result and written subdivision
corollary; separate internal audit GREEN.

This note isolates a reusable restriction on the thirteen-vertex graph
`G_*` from the
[`atomic shared-hub barrier`](../barriers/hc7_atomic_shared_hub_defect_rotation_barrier.md).
It rules out every subdivision of that graph in a two-apex host.  In
particular, the standard hosts obtained by joining an edge to a planar graph
cannot realize the exact shared-hub subdivision residue.

The deterministic verifier is
[`hc7_atomic_shared_hub_two_apex_exclusion_verify.py`](hc7_atomic_shared_hub_two_apex_exclusion_verify.py).

## 1. The graph

Let

\[
 H_0=(K_7-\{ab,cd\})+\{xa,xb,xc,xd\}
\]

on vertices `a,b,c,d,e,f,g,x`.  Form `G_*` by subdividing `ac,bd,ad,bc`
once, with respective subdivision vertices
`p_ac,p_bd,p_ad,p_bc`; add

```text
f-p_ac, f-p_bd, g-p_ad, g-p_bc;
```

replace `fg` by `f-h-g`; and add `eh,hx`.  Thus `G_*` has thirteen
vertices and thirty-four edges.  Its vertices `f,g` both have degree eight.

For a set

\[
             D\subseteq V(G_*)\mathbin{\dot\cup}E(G_*),
\]

write `G_*-D` for the graph obtained by deleting the selected vertices and
then every selected edge whose ends survive.  This convention includes the
redundant case in which a selected edge is incident with a selected vertex.

## 2. Two-object nonplanarity

### Theorem 2.1 (computer-assisted finite result)

For every `D` with `|D|<=2`, the graph `G_*-D` is nonplanar.

#### Finite proof

There are thirteen vertex objects and thirty-four edge objects.  The
verifier checks all deletion sets of orders zero, one and two.  The counts
are

| deletion type | cases |
|---|---:|
| none | 1 |
| one vertex | 13 |
| one edge | 34 |
| two vertices | 78 |
| one vertex and one edge | 442 |
| two edges | 561 |
| **total** | **1,129** |

For every remainder, the planarity algorithm returns a Kuratowski
subgraph.  The verifier checks that the returned graph is a literal
subgraph of the remainder, suppresses its degree-two paths, and verifies
that the resulting graph is `K_5` or `K_{3,3}`.  It obtains 155
subdivisions of `K_5` and 974 subdivisions of `K_{3,3}`.  Thus every one of
the 1,129 remainders has an independently checkable nonplanarity
certificate.  This proves the theorem. \(\square\)

Run from the repository root:

```text
.venv/bin/python -B results/hc7_atomic_shared_hub_two_apex_exclusion_verify.py
```

The expected output begins and ends with

```text
GREEN shared-hub two-apex exclusion
deletion_cases=1129 none=1 v=13 e=34 vv=78 ve=442 ee=561
...
consequence=no subdivision of G_* embeds in a two-apex graph
```

## 3. Subdivision corollary

### Corollary 3.1

No two-apex graph contains a subdivision of `G_*` as a subgraph.
Consequently, if `P` is planar, then `K_2 join P` contains no subdivision
of `G_*`.

#### Proof

Suppose that a graph `J` contains a subdivision `S` of `G_*`, and that
deleting a set `Z` of at most two vertices makes `J` planar.  Consider a
vertex `z in Z` that belongs to `S`.  If `z` represents a vertex `v` of
`G_*`, record the vertex object `v`.  Otherwise `z` is internal on the
unique subdivided path representing some edge `uv` of `G_*`; record the
edge object `uv`.  Ignore vertices of `Z` outside `S`, and identify repeated
records.  This produces a set `D` of at most two vertex or edge objects.

After deleting `Z` from `S`, discard the broken remnants of paths
corresponding to recorded objects.  What remains contains a subdivision of
`G_*-D`.  It lies in the planar graph `J-Z`, so suppressing its degree-two
vertices would give a planar embedding of `G_*-D`.  This contradicts
Theorem 2.1.

Deleting the two vertices of the complete factor from `K_2 join P` leaves
the planar graph `P`, proving the final assertion. \(\square\)

## 4. Direct sharpening for the icosahedral host

Let `I` be the icosahedral graph and let `J=K_2 join I`.  Every vertex of
`I` has degree seven in `J`, while the two vertices of the complete factor
have degree thirteen.  Therefore, in a hypothetical subdivision of `G_*`
in `J`, the degree-eight vertices `f,g` would have to map to those two
complete-factor vertices.

This already gives a direct contradiction.  The graph `G_*-{f,g}` contains
a subdivision of `K_5` rooted at `b,c,d,e,x`.  Use the paths

```text
b-p_bc-c,
b-p_bd-d,
c-p_ac-a-p_ad-d,
e-h-x,
```

and the literal edges for the other six root pairs.  Their interiors are
pairwise disjoint.  Deleting the two complete-factor vertices from the
hypothetical subdivision would therefore put a subdivision of `K_5` in the
planar icosahedron, which is impossible.  The verifier checks the displayed
paths as a supplementary certificate.

## 5. Scope

Corollary 3.1 is unbounded in the order of the ambient graph, but it uses
the exact labelled graph `G_*` up to subdivision.  It does not prove that
arbitrary branch-vertex-avoiding paths through an `H_0` subdivision can be
decoded when they meet other route interiors.  Rather, it shows that the
standard two-apex planar examples cannot realize that exact shared-hub
residue at all.  Any adversarial example to the proposed dirty-path
extension must either occur in a host that is not two-apex or weaken the
literal `G_*` subdivision structure.
