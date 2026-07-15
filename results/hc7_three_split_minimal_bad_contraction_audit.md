# Audit of the minimal bad split-contraction theorem

**Verdict:** green, with one scope correction incorporated into the theorem
file.

This audit covers
[`hc7_three_split_minimal_bad_contraction.md`](hc7_three_split_minimal_bad_contraction.md).

## 1. Minimal quotient cut

For each `e_i in F`, the graph `H_i=G/(F-{e_i})` is seven-connected by
inclusion-minimality.  If a separator `T` of `H=H_i/e_i` of order at most
six omitted the contracted image, splitting that image back would leave
the same separated components in `H_i`.  Hence every contracted image is
in `T`.  Replacing one image by its two ends produces a separator of
`H_i` of order `|T|+1`, so `|T|=6`; the same argument excludes cuts of
order at most five.

Every component of `H-T` is `T`-full by six-connectivity.  Splitting one
boundary image gives an actual seven-boundary in `H_i`, so every expanded
component has a neighbour of each literal endpoint.  Repeating this for
all hit edges proves pointwise fullness of the expanded boundary.  These
steps are valid.

## 2. Fan and literal branch sets

For a hit model, write `R=Q_i cap T`, `K=Q_i-T`, and `r=|K|`.  The
forbidden set `R union {x_i,y_i}` has order `6-r`; after deleting it, the
seven-connected host is at least `(r+1)`-connected.  Menger therefore
gives the asserted `r` disjoint paths from `K` to distinct unused expanded
boundary atoms.  Truncation at the first boundary hit keeps each interior
in the core component and preserves disjointness.

The four extended `Q_i` bags use four distinct boundary atoms.  The split
bag uses `x_i,y_i`, so the five model bags use exactly six expanded
boundary atoms.  When the expanded order is at least eight, an unused atom
`w` exists.  With two further quotient components `D,E`, the bags

```text
the four extended Q_i bags,
{x_i,y_i},
D union {w},
E
```

are disjoint, connected and pairwise adjacent.  Every adjacency involving
`D` or `E` follows from pointwise boundary fullness; the original model
supplies the other adjacencies.  This is a literal `K_7` model.

## 3. Scope correction

When `|F|=1`, the lifted order-seven separation certainly preserves the
one contracted carrier.  It need not orient either uncontracted
support-six model: a boundary endpoint of an uncontracted split bag can
carry all contacts while its mate and singleton core lie on different
open sides.  The theorem and its corollary now state only the justified
contracted-carrier conclusion.

## 4. Remaining boundary

The proof closes expanded orders eight and nine whenever the quotient cut
has at least three components.  It does not close the exactly-two-component
case.  Pointwise fullness supplies only one external component bag after
the five model bags have been rooted; a seventh bag needs a genuinely
reserved connected carrier or a label-faithful split.  No such carrier is
inferred in the audited proof.
