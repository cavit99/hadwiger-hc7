# Audit: active-root face exchange

## Verdict

**GREEN for the stated conditional theorems.**  The note proves a new
uniform facial-coherence principle and a collision localization.  It does
not prove the final bilateral exact-seven state exchange and does not
close `HC_7`.

## 1. Rooted-quadruple coherence

Theorem 2.1 uses the rooted-`K_4` theorem at exactly its valid strength.

* In a four-connected graph, absence of the rooted model forces the graph
  to be planar with the four roots cofacial.
* In an already planar three-connected graph, the planar specialization
  of the rooted theorem gives the same cofacial conclusion.

Three-connected planar embeddings are unique up to reflection, and two
different faces share at most two vertices.  Therefore two cofacial
quadruples sharing three actual vertices use the same face.  Iteration
along the three-overlap graph is valid.  The theorem does not identify
portal classes with vertices: its overlap is explicitly overlap of
actual root vertices.

## 2. The SDR extension

The images of full SDRs of four portal sets are the bases of a rank-four
transversal matroid.  Its basis graph is connected under one-element
exchange, so the underlying four-sets form a connected three-overlap
family.  Coordinate swaps which leave the underlying basis unchanged
cause no problem: rooted `K_4` bags are rooted at the four actual
vertices, while the selected SDR only says which fixed private lobe is
adjoined to which rooted bag.

For fixed disjoint lobes `D_i`, the set `D_i union {p_i}` is connected
for every `p_i in N_H(D_i)`, intersects the torso only in `p_i`, and the
four such sets are disjoint for an SDR.  The common pool/reserve data are
now stated explicitly.  Hence every SDR is genuinely active and the
biportal completion is label-preserving.

## 3. Rotation and annular composition

At a four-column interface, a mismatch of the two facial orders gives a
column-rooted `K_4` by the audited two-cycle exchange.  The note separately
assumes the literal common pool/reserve contacts needed to lift it to
`K_7`; no abstract portal incidence is substituted.  Compatible orders
give an annulus, and the two-apex conclusion additionally assumes that
the pages and all other societies cover the remainder and are rural.

Thus the claimed closure is conditional on an active-overlap-saturated
chain.  It does not assert that seven-connectivity alone selects the four
columns.

## 4. Collision localization

Theorem 8.1 is the arbitrary-two-family form of the proved cross-Helly
argument.  Disjoint carriers extend to adjacent connected shores.  If
none exist, one Tutte bag meets every carrier of one family and each
off-bag component misses a required literal row and attaches through at
most two torso vertices.

In the spanning one-complex shell, all neighbours of such a component
are among those at most two vertices and the six literal singleton
labels.  Missing one label caps its neighbourhood at seven;
seven-connectivity forces equality.  It therefore attaches to exactly
two torso vertices, sees exactly five labels, misses exactly one label,
and lies behind an actual exact seven-cut.  This count is literal and
does not count a contracted carrier as one vertex.

## 5. Exact frontier

The proved chain is

```text
fixed disjoint extension lobes + rank four
    => one active facial order or K7;
shared extension role
    => disjoint full-row shores, or one torso;
dark off-torso lobe in the one-complex shell
    => exact seven-cut.
```

The unproved residue is exactly what the source says: a rank-at-most-three
portal family or shared-lobe core inside one torso, or two dark exact-seven
lobes with different missed rows.  Concluding that their proper-minor
state spectra meet would be an additional theorem, not a consequence of
the present audit.

For four distinct off-torso lobes, Lemma 9.1 correctly sharpens the Hall
residue.  Each portal set has order two by dark-lobe exactness.  A minimal
deficient family cannot have order one or two; at order three all three
two-sets coincide, and at order four their union has order at most three.
Hence the only rank-deficient geometries are the stated two-pole triple
bouquet and three-pole four-bouquet.  Their operation-state exchange is
not proved.
