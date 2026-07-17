# Independent audit: the three-common-branch-set two-apex barrier

**Audited source:** `hc7_three_common_geodesic_two_apex_barrier.md`
**Repaired source SHA-256:**
`0bbb8a16c08ffaf9502f6931eaf01fec6f4c314eb0e30d5166f9d754b62063d6`
**Promoted source SHA-256:**
`4de8c7a1081d1e04b6f676e905afc9727ca9ef25c75e8d0d4b05973fb07083c1`
**Verifier:** `hc7_three_common_geodesic_two_apex_verify.py`
**Verifier SHA-256:**
`450a38ddf87c7a0ec911c4c714f78177acf69f8772596adca968ccd48c1cda26`
**Verdict:** **GREEN.**

The promoted source differs from the repaired audited revision only in its
status line.  The construction, claims, and proof are unchanged.

The construction and its stated falsification boundary are correct.  It is
a seven-connected, `K_7`-minor-free, six-colourable graph with an adjacent
pair whose deletion is exactly six-chromatic and has the displayed spanning
`K_6`-minor model.  It realizes all of the static colouring, Kempe-chain,
contact-profile, and two-path data claimed in the source.  It is not a
counterexample to `HC_7`: the host itself is six-colourable, an order-seven
separator is present, and deleting the two universal vertices leaves a
planar graph.

## 1. Construction, planarity, and connectivity

The edge description in the verifier is the standard icosahedron: two
pentagonal caps joined by the triangulated antiprism belt.  Subdividing each
edge once and joining the three subdivision vertices in every original face
is a planar frequency-two triangulation on 42 vertices.  Deleting the one
specified edge preserves planarity.

The verifier enumerates every deletion set of order at most four and checks
that the resulting planar graph `P` remains connected.  The enumeration is
complete, and its connectivity routine checks the induced remainder rather
than the original graph.  It also verifies that the minimum degree of `P` is
five.  Thus `P` is five-connected.

For `G=K_2 vee P`, deleting at most six vertices leaves a universal vertex
unless both vertices of the `K_2` were deleted.  In the latter case at most
four vertices of `P` were deleted, so the remainder is connected.  Hence
`G` is seven-connected.  The chosen vertex `z` has five neighbours in `P`
and the two universal neighbours, so its open neighbourhood is an
order-seven cut isolating `z`.  This also proves that the connectivity is
exactly seven.

## 2. Exclusion of a `K_7` minor

At most two branch sets of any minor model can contain the two universal
vertices.  If a `K_7`-minor model existed, deleting those at most two branch
sets would leave at least five pairwise adjacent connected branch sets
entirely in `P`.  They would form a `K_5` minor of a planar graph, which is
impossible.  This argument remains valid when both universal vertices occur
in one branch set or when their branch sets contain additional vertices of
`P`.

Consequently there is no hidden choice of a spanning `K_6` model in
`G-{z,u}` which is contacted by `{z,u}` in all six branch sets: the connected
set `{z,u}` together with such a model would itself be a `K_7`-minor model.
This proves precisely the claimed failure of a contact-count improvement
from five contacted branch sets to six.  It does not rule out changing other
features of the displayed model while retaining contact count five.

## 3. The displayed `K_6` model and contact profile

The six listed vertex sets are disjoint and partition
`V(G)-{z,u}`.  The verifier checks each induced branch set is connected and
checks every one of the fifteen required branch-set adjacencies.  Its direct
neighbourhood calculation gives

```text
z: {42}, {43}, {1}, {0,16,20}, empty,       empty
u: {42}, {43}, {1}, empty,       {5,14,19,32}, empty.
```

Thus exactly three branch sets are common contacts, with coincident
singleton pole-neighbourhoods; one branch set is contacted only by each
pole; and the sixth is contacted by neither.  The model is spanning and has
the exact three-common-branch-set profile asserted in the source.

## 4. Colouring and linkage checks

The six displayed colour classes are disjoint and cover all 44 vertices.
The verifier checks every edge other than `zu` is properly coloured and
that `z,u` both have the buffer colour.  The buffer colour occurs in
`G-{z,u}` and no buffer-coloured vertex there is adjacent to either pole.
Each pole sees all five other colours.

For each nonbuffer colour, a breadth-first search in the corresponding
induced two-colour subgraph of `G-zu` reaches `u` from `z`.  Hence all five
claimed Kempe connections are present.  The two displayed paths use host
edges, are vertex-disjoint, have their endpoints in the two exclusive
branch sets, and use both selected endpoint colours on each side.  No
colour-preserving or branch-set-avoiding property of their interiors is
claimed.

## 5. Exact chromatic claims

The repair to the source correctly avoids treating chromatic number as
minor-monotone.  Inductively, contracting an edge in `K_r vee P'`, where
`r<=2` and `P'` is planar, produces another graph of this form: a contraction
inside `P'` preserves planarity, a contraction incident with a universal
vertex removes one vertex from the planar part, and contracting the two
universal vertices decreases `r`.  Every arbitrary minor is a subgraph of a
contraction-only minor.  The Four-Colour Theorem therefore makes every minor
of this particular `G` at most six-colourable.

Moreover `P-{z,u}` contains the odd wheel with centre `10` and rim

```text
16, 20, 24, 28, 31.
```

All five centre edges and all five cyclic rim edges occur in the reconstructed
graph, and none of these six vertices is `z` or `u`.  Thus the planar graph
`P-{z,u}` is exactly four-chromatic.  Since chromatic numbers add under a
complete join,

```text
chi(G-{z,u}) = chi(K_2) + chi(P-{z,u}) = 6.
```

## 6. Trust boundary

The construction proves that the following static ingredients alone cannot
force a `K_7` minor or a sixth contacted branch set:

1. seven-connectivity and `K_7`-minor-freeness;
2. exact six-chromaticity after deleting the adjacent poles;
3. the displayed spanning `K_6` model with three common singleton contacts;
4. a nonempty buffer class, saturated pole palettes, and all five buffer
   Kempe connections; and
5. the displayed two-path linkage between the exclusive branch sets.

The example does **not** test the compulsory proper-minor transitions of a
seven-chromatic minor-minimal host.  It instead realizes both structural
escape outcomes that the active programme must retain: `N_G(z)` is an
order-seven separator, and the fixed pair consisting of the universal
vertices meets every `K_5` minor because deleting it leaves planar `P`.
Nothing in this audit promotes a theorem about arbitrary seven-chromatic
graphs or proves `HC_7`.

The verifier was rerun on the recorded revision and returned:

```text
GREEN: exact c=3 profile, buffer-colour locks and two-linkage; the sharp output is the order-seven separator/two-apex pair
```
