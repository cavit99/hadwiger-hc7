# A barrier to surjective five-colouring Kempe connectivity

**Status:** written counterexample with deterministic verifier and exhaustive
eight-vertex census; separate internal audit GREEN in
[`hc7_surjective_five_colour_kempe_connectivity_barrier_audit.md`](hc7_surjective_five_colour_kempe_connectivity_barrier_audit.md).

## The refuted statement

The following statement is false:

> For every eight-vertex, `K_5`-minor-free, four-colourable graph `H`, the
> graph of labelled surjective proper five-colourings of `H` is connected
> under surjectivity-preserving single-component Kempe swaps.

Here the five colours are the fixed labels `1,2,3,4,5`.  A move chooses two
colours and one connected component of the subgraph induced by those two
colour classes, then interchanges the two colours on that component.  The
move is admitted only when the resulting colouring still uses every one of
the five colours.

## Counterexample

Let

```text
A = {6,7},   B = {0,1,2,3,4,5},
H = K_{A,B} = K_{2,6}.
```

Thus the edge set is

```text
06 07 16 17 26 27 36 37 46 47 56 57.
```

With the displayed vertex labels its graph6 encoding is `G??F~w`.
The graph is bipartite and has treewidth two, so it is four-colourable and
has no `K_5` minor.

For a surjective proper five-colouring `c`, put

```text
p(c) = |{c(6),c(7)}|.
```

The palettes used on `A` and `B` are disjoint, because every vertex in `A`
is adjacent to every vertex in `B`.  Hence `p(c)` is either one or two.

The value `p(c)` is invariant under every permitted Kempe move.  If the two
chosen colours occur on opposite sides, their induced subgraph is connected,
and its swap merely exchanges the two colour classes between the sides.  If
the two colours occur on the same side, that induced subgraph has only
singleton components.  A permitted singleton swap cannot remove its source
colour, so both colours remain on that same side.  In either case the number
of colours used on `A` is unchanged.

Both values occur.  In vertex order `0,1,...,7`, examples are

```text
(2,2,2,3,4,5,1,1),   with p=1,
(3,3,3,3,4,5,1,2),   with p=2.
```

They therefore lie in different Kempe components.

The deterministic verifier additionally checks that these are the only two
components.  Their orders are

```text
p=1: 5 * (number of surjections [6] -> [4]) = 7,800,
p=2: 5*4 * (number of surjections [6] -> [3]) = 10,800.
```

## Exhaustive eight-vertex scope

The accompanying census reads the complete `geng -q 8` stream of all 12,346
unlabelled eight-vertex graphs.  It uses direct finite algorithms for:

1. `K_5`-minor detection, by enumerating every partition of a vertex subset
   into five nonempty connected pairwise adjacent branch sets;
2. four-colourability;
3. all labelled surjective proper five-colourings; and
4. every permitted single-component Kempe move.

It finds 7,751 `K_5`-minor-free graphs (all four-colourable), of which 23
have disconnected colouring graphs.  Their edge-count distribution is

```text
12:1  13:1  14:2  15:5  16:7  17:6  18:1.
```

Thus `K_{2,6}` is, up to isomorphism, the unique minimum-edge counterexample
on eight vertices.  This is a finite classification statement only; the
explicit invariant above proves the counterexample without computation.
Here “minimum” refers to edge count within the order-eight scope of the
refuted statement; no claim of minimum order is intended.

## A closer static model of the live boundary geometry

The obstruction survives after adding the two prescribed forest edges that
occur in the current order-nine boundary problem.  Let

```text
W = {6,7},
F = {0,1,2,3,4,5},
E(F) = {04,15},
H* = I[W] join F.
```

Thus `H*` has graph6 code ``G?`F~w`` (the backtick is part of the code), and
its edges are `04,15` together with `i6,i7` for every `0 <= i <= 5`.
The same invariant

```text
c(6) = c(7)
```

is preserved by every surjectivity-preserving Kempe move.  Both modes occur:
when the twins have one common colour, `F` has a proper surjective
four-colouring; when they have distinct colours, `F` has a proper surjective
three-colouring.  Exact enumeration gives two Kempe components, each of
order 5,520.

There is a width-three tree decomposition with bags

```text
{6,7,0,4}, {6,7,1,5}, {6,7,2}, {6,7,3}.
```

Consequently `H*` is `K_5`-minor-free.  One may also add a vertex `d`
adjacent exactly to `0,4`; attaching the bag `{d,0,4}` to the first bag
preserves width three.  The resulting nine-vertex graph has graph6 code
``H?`F~yG``.

Under the customary boundary labels, one may read

```text
xd=0, yd=4, xe=1, ye=5, x0=2, y0=3.
```

This matches `|W|=2`, a six-vertex forest containing the two prescribed
disjoint edges, and a simplicial vertex `d` on the first prescribed edge.
It remains only a static boundary model: it is not asserted to arise from
two full shores, a seven-connected host, contraction-criticality, or
`K_7`-minor exclusion.  Those extra host hypotheses are exactly what any
positive transition theorem must use.

## Reproduction

Verify the explicit counterexample:

```sh
python3 barriers/hc7_surjective_five_colour_kempe_connectivity_barrier_verify.py
```

Run the full census when nauty `geng` and a C++17 compiler are available:

```sh
clang++ -O3 -std=c++17 \
  barriers/hc7_surjective_five_colour_kempe_connectivity_barrier_census.cpp \
  -o /tmp/hc7_kempe_census
geng -q 8 | /tmp/hc7_kempe_census
```

Expected final output:

```text
PASS graphs=12346 k5_minor_free=7751 four_colourable=7751 disconnected=23
histogram 12:1 13:1 14:2 15:5 16:7 17:6 18:1
minimum edges=12 count=1 graph6=G??F~w states=18600 components=7800,10800
representatives 11123400 22223401
```

The census representatives use colours `0,1,2,3,4`; adding one to every
entry gives the labelled colourings displayed above.

## Trust boundary

This barrier refutes an unconditional Kempe-connectivity principle.  It does
not refute a theorem carrying additional contraction-critical, shore,
minor-model, or exact-response data.  The strengthened static model shows
that merely adding the two prescribed forest edges and a simplicial boundary
vertex is still insufficient.
