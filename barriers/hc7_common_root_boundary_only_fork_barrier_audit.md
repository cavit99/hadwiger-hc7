# Audit of the boundary-only three-bridge barrier

**Status:** separate internal audit; GREEN within the stated abstract-boundary
scope.

**Audited source:** `barriers/hc7_common_root_boundary_only_fork_barrier.md`

```text
sha256 e774fb867c13e8bd75c07f22cf959de0ce3867878b3978e5fc96787d2bf800df
```

## Verdict

GREEN.  The revised singleton-root labelling, all four asserted nonedges, the
independence bound, and the width-two elimination certificate are correct.
The witness disproves a decoder depending only on the compact boundary and
the three or four shore-labelled added edges.  It does not construct an exact
minor-minimal `HC_7` host, as the source explicitly acknowledges.

## Checks

Reconstructing `H` from

```text
04,08,48,15,18,26,28,37,38
```

gives the following graph6 string:

```text
H?`@?bw
```

Under

```text
alpha={0}, beta={5,6,7,8}, gamma={1,2,3,4},
```

every edge is bichromatic and `H[alpha,beta]` has precisely the components

```text
{0,8}, {5}, {6}, {7}.
```

The relabelling

```text
W_0={5}, W_1={0,8}, W_2={6}, W_3={7}
```

is therefore valid.  Vertex `5` has the single neighbour `1`, of colour
`gamma`, so the distinguished component `W_0={5}` is indeed a singleton
`alpha`--`beta` component with no `alpha`- or `beta`-coloured neighbour.

The pairs `57`, `06`, `87`, and `56` are all absent from `E(H)`.  They join,
respectively,

```text
W_0-W_3, W_1-W_2, W_1-W_3, W_0-W_2.
```

Thus each shore-labelled pair is a matching on the four distinct components,
and their union is the claimed component-level four-cycle.

The four vertex-disjoint cliques

```text
{0,4,8}, {1,5}, {2,6}, {3,7}
```

cover `V(H)`, proving `alpha(H)<=4`; the independent set `{5,6,7,8}` proves
equality.  Since `H` is a triangle with three attached paths, it is
two-degenerate and `K_4`-minor-free.  The stated compact consequences follow.

For `H_4=H+{06,57,87,56}`, eliminate `1,2,3,4`.  The only new fill edges are
`58` and `68`.  The remaining neighbours of `0` are `6,8`, already adjacent;
after eliminating `0`, the vertices `5,6,7,8` induce `K_4-67`.  Vertex `6`
then has adjacent remaining neighbours `5,8`, and the residue on `5,7,8` is a
triangle.  Every elimination has at most two current neighbours, so
`tw(H_4)<=2` and `H_4` has no `K_4` minor.  The three-edge graph is a subgraph
of `H_4`; it is therefore also `K_4`-minor-free.  Independently, it has only
twelve edges, below the fifteen inter-bag edges required by a `K_6` model.

## Trust boundary

No unresolved arithmetic, adjacency, colouring, or minor check remains.  The
only limitation is intentional: shore support is retained as abstract edge
provenance, not realized inside a seven-connected, seven-chromatic,
minor-minimal host.  Accordingly the promoted statement must remain a
barrier to **boundary-only** closure and must not be described as a
counterexample to the synchronized-fork theorem or to its exact host-level
completion.
