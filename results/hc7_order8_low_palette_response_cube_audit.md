# Independent audit of the low-palette response cube

## Verdict and audited revision

**Verdict: GREEN.**

This audit checks the complete source
[`hc7_order8_low_palette_response_cube.md`](hc7_order8_low_palette_response_cube.md)
at SHA-256

```text
c0d1bf31330246c99ab57d4d7d42784a9c21e481df53ac809aebaec75a2fac9e
```

The response-cube construction, the two shore-internal Kempe-path
arguments, the three-chromatic specialization, and the stated trust
boundary are correct.  The theorem is conditional on the exact extension-
language hypotheses in Section 1 and does not prove `HC_7`.

## 1. Setting and colour conventions

The sets `E_A` and `E_D` consist of labelled proper colourings of
`H=G[B-I]` by the five colours not assigned to the fixed independent set
`I`.  Thus a permutation of those five colour names leaves the sixth colour
on `I` fixed.  The theorem assumes, rather than derives, that the two
extension sets are disjoint, nonempty, invariant under these permutations,
and give exact ownership of every surjective five-colouring.

Because `E_A` is nonempty, a maximum-palette colouring `c` exists.  Its
palette order `p` is positive.  Hypothesis 3 gives `p<=3`; no chromatic
assumption on `H` is used until Corollary 3.1.

## 2. Selection and properness of the cube

After retaining one representative of each of the `p` nonempty colour
classes of `c`, exactly `8-p` vertices remain available.  Since

```text
8-p >= 5-p,
```

one may select `5-p` distinct vertices while retaining every old colour.
This argument is independent of the distribution of the eight vertices
among the old colour classes.

Each selected vertex is assigned a different colour absent from `c`.
Consequently, in every subcube trace `c_J`:

* a recoloured vertex cannot conflict with an unrecoloured vertex, because
  its new colour was absent from `c`;
* two recoloured vertices cannot conflict, because their new colours are
  distinct; and
* every old colour remains represented.

Thus every `c_J` is proper and uses exactly `p+|J|` colours.  In particular,
the top trace `c_[5-p]` is surjective.

## 3. Ownership and rejection of proper faces

The top trace cannot lie in `E_A`, because it uses five colours and
hypothesis 3 excludes four- and five-colour members of `E_A`.  Exact
surjective ownership therefore places it in `E_D`.  Since the empty trace
is `c in E_A` and the extension sets are disjoint, an inclusion-minimal
nonempty `J` with `c_J in E_D` exists.

If `|J|=1`, the two traces have opposite shore ownership and differ at one
literal boundary vertex, as stated.  If `|J|>=2` and
`empty != K proper_subset J`, inclusion-minimality excludes `c_K` from
`E_D`.  Its palette has order `p+|K|>p`, so maximality of `p` excludes it
from `E_A`.  Hence every proper nonempty face below `c_J` is rejected by
both shores.

## 4. The `A`-shore path

Fix one extension of `c` through the closed `A`-shore; the same fixed
extension may be used for every `i in J`.  In this extension, the new colour
`b_i` is absent from all boundary vertices in `B`: it is absent from `H`
under `c`, and `I` has the fixed sixth colour.

Consider the full `a_i`--`b_i` Kempe component containing `x_i`.  If it met
no other boundary vertex of colour `a_i`, then its only boundary vertex
would be `x_i`.  Swapping its two colours would preserve properness, leave
`I` unchanged, and change the boundary trace exactly from `c` to
`c_{\{i\}}`.  Since `|J|>=2`, this is a proper nonempty face and is rejected
by both shores, contradicting that the swapped colouring is an `A`-shore
extension.

The component must therefore meet another boundary vertex of colour
`a_i`.  Truncate a shortest component path at the first such boundary
vertex.  No internal vertex lies in `B`, by the first-hit choice, so all
internal vertices lie in `A`.  The interior is nonempty because the two
boundary endpoints have the same colour and hence are nonadjacent in a
proper colouring.  This proves every asserted property of `P_i^A`.

## 5. The `D`-shore path

Fix one extension of `c_J` through the closed `D`-shore.  At its boundary,
`x_i` is the unique vertex of colour `b_i`, because the new colours were
assigned bijectively to the selected vertices.  Every boundary vertex still
coloured `a_i` belonged to the original class `c^{-1}(a_i)`.

If the full `a_i`--`b_i` component at `x_i` met no other boundary
`a_i`-vertex, swapping that component would change the trace exactly to
`c_{J-\{i\}}`.  This is a nonempty proper face because `|J|>=2`, so the
rejection conclusion from Section 3 rules it out.  First-hit truncation now
gives a path whose internal vertices all lie in `D`; its interior is again
nonempty because its endpoints have the same colour.  This proves the
claims about `P_i^D`.

The proof does not claim that paths with different indices are disjoint in
this general form, nor that their remote boundary endpoints agree between
the two shores.

## 6. Three-chromatic specialization

If `chi(H)=3`, every proper colouring of `H` uses at least three colours.
Together with `p<=3`, this forces `p=3`, so the cube has exactly two
coordinates.  A minimal owned face is either a singleton, giving the
one-vertex transition, or the top face, in which case both singleton faces
are rejected by both shores.

When the two selected vertices come from distinct repeated old colour
classes, their old colours are distinct, their assigned new colours are
distinct, and every new colour is outside the old palette.  Their two
bichromatic colour pairs are therefore disjoint.  In each one fixed shore
extension, the two induced bichromatic subgraphs are vertex-disjoint, so
the selected paths are vertex-disjoint.

Such a selection is possible whenever at least two of the three colour
classes are repeated.  If it is impossible, exactly one class is repeated;
the other two are singletons and the eight class vertices therefore have
orders `(6,1,1)`, up to permutation.  Conversely, that pattern has only one
repeated class.  Since every colour class is independent, `alpha(H)<=4`
excludes the order-six class and guarantees the desired selection.

## 7. Trust boundary

The theorem proves a finite-dimensional response cube and supplies one
shore-internal bichromatic path per active coordinate in each shore.  It
does **not** prove any of the following:

* that an intermediate four-colour trace extends through either shore;
* that path endpoints or internal vertices align with named branch sets of
  a pre-existing minor model;
* that remote endpoints agree between the two shores;
* that the paths for different coordinates are disjoint without the
  distinct-repeated-class hypothesis;
* that `alpha(H)<=4` follows from the theorem's general hypotheses;
* that a compatible order-seven boundary colouring exists; or
* that `G` contains a `K_7` minor.

Those conclusions require additional host-level information such as
seven-connectivity, `K_7`-minor exclusion, or the full proper-minor
criticality assumptions of the live `HC_7` programme.
