# Independent audit: the `Q`-full quotient rooted-`K_4` theorem

## Verdict

**GREEN.**  The strengthened contraction-first residue is also sound.

## 1. Rooted-model lifting

Every quotient vertex represents a connected set which is adjacent to
all three vertices of `Q`; this includes the singleton sets `a,b,c`.
A connected quotient branch set lifts to the connected union of the
represented sets, because every quotient edge is witnessed by a literal
edge of `H`.  Distinct quotient bags lift disjointly.  Each lifted rooted
bag contains one of `a,b,c,d_i`, hence is adjacent to every member of
`Q`.  A rooted `K_4` therefore lifts with the three singleton `Q` bags to
a literal `K_7` model; no owner is reused.

## 2. Common-face argument

If no root choice `a,b,c,d_i` gives a rooted model, the exact
Fabila-Monroy--Wood theorem makes the four-connected quotient planar and
makes each such quadruple cofacial.  Four-connectivity implies
three-connectivity, so the embedding is unique and two distinct faces
share at most an edge.  Faces for different `d_i` already share the three
distinct vertices `a,b,c`, so they coincide.  Every quotient vertex lies
on one face, making the quotient outerplanar, contrary to minimum degree
at least four.

## 3. Corollary 3.1 and the `K_4` convention

The current corollary uses the stronger direct observation: **any**
`K_4` minor in `R` lifts to `K_7`, since every quotient branch bag is
`Q`-full.  Hence a `K_7`-free quotient is `K_4`-minor-free, so it is a
partial 2-tree.  With at least four vertices it cannot be three-connected
and therefore has a separator of order at most two.

This automatically handles the convention-sensitive graph `R=K_4`.
Although `K_4` is not called four-connected under the usual order
convention and has no small separator, it is excluded by the direct
lifting observation.  A quotient separator containing only singleton
vertices among `a,b,c` would lift unchanged to a separator of the
four-connected graph `H`; thus every quotient two-cut uses an actual
carrier.

No lifting, overlap, or face-order defect was found.
