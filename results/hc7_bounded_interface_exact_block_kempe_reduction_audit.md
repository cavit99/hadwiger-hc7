# Independent audit: exact-block Kempe reduction

**Verdict:** **GREEN** at the corrected exact revision below, conditional on the
GREEN-audited low-degree adjacent-pair theorem and its exact independent-block
trace conclusion.  The reduction does not prove `HC_7`, a common boundary
partition, or a labelled clique-minor model.

## Exact revision audited

```text
19382ff7bc0065bc18a7caaeffd5c5fff46cf4ddc226d40036c751081a9853ff  results/hc7_bounded_interface_exact_block_kempe_reduction.md
```

The preceding promoted revision incorrectly claimed that two labelled
exact-`I` colourings with different colour names on `I` could be connected
without changing that colour.  The corrected corollary fixes one colour
`gamma`, requires both endpoints to assign `gamma` exactly to `I`, and
states separately that arbitrary endpoints may first be globally relabelled
to align this name.  Theorem 4.1 now records that normalization explicitly.

This audit includes Lemma 2.1, Corollary 2.2, Lemma 3.1, Theorems 4.1 and
5.1, and the stated localization bounds.  Any mathematical change to the
source invalidates this verdict until the audit is renewed.

## 1. Setup and inherited facts

The setup is exactly the output of the audited low-degree adjacent-pair
alignment theorem.  In particular:

- `C` is a component of `G-N[u]`;
- `S=N_G(C)` is contained in `N(u)` and has order between seven and nine;
- `A=G[C union S]` and `B=G-C` are proper subgraphs and hence are
  six-colourable;
- an equality partition extending to both closed shores would allow a global
  permutation of the six colours on one shore and then gluing, so the two
  boundary extension languages are disjoint; and
- each nonempty independent `I subseteq S` is an exact boundary colour block
  in a six-colouring of either closed shore.

The definition `T=N(u)-S` gives `|T|=d_G(u)-|S|<=2`; no unstated equality is
used.

## 2. Lemma 2.1: four-degeneracy

The density contradiction is correct.

If a subgraph `H subseteq G[S-I]` has minimum degree at least five, then
`h=|V(H)|>=6`.  Since `I` is nonempty and `|S|<=9`, also `h<=8`.  Contracting
the connected set `C` to `c`, deleting unwanted vertices and edges, and
retaining `u,c,V(H)` produces

```text
overline(K_2) vee H
```

as a minor of `G`: `u` and `c` are nonadjacent, and each is complete to
`S`, hence to `V(H)`.  It has at least

```text
2h + 5h/2 = 9h/2
```

edges.  Mader's exact theorem applies because `h+2>=8`: a graph on `n>=7`
vertices with at least `5n-14` edges has a `K_7` minor, equivalently a
`K_7`-minor-free graph has at most `5n-15` edges.  Here

```text
9h/2 > 5(h+2)-15 = 5h-5
```

for `h<10`.  Since edge counts are integral, this is precisely enough to
cross Mader's threshold.  Thus every nonempty subgraph has a vertex of degree
at most four, which is the required four-degeneracy.

The threshold statement is Mader's 1968 theorem; a convenient explicit
restatement is Theorem 3 of Campbell--Mattman--Ottman--Pyzer--Rodrigues--
Williams, *Intrinsic knotting and linking of almost complete graphs*.

## 3. Corollary 2.2: exact use of Las Vergnas--Meyniel

Corollary 2.2 now assumes that both boundary colourings assign one fixed
colour `gamma` exactly to `I`.  Applying one common global colour
permutation sends `gamma` to colour six.  Their restrictions to `G[S-I]`
are then proper colourings from the same palette of five colours.
Surjectivity onto all five colours is not required in the definition of a
five-colouring.

The cited Las Vergnas--Meyniel result is applicable exactly as stated: every
pair of `k`-colourings of a `(k-1)`-degenerate graph are `k`-Kempe equivalent.
This is Proposition 2.1 of Las Vergnas and Meyniel, *Kempe classes and the
Hadwiger Conjecture*, JCTB 31 (1981), 95--104,
doi:10.1016/S0095-8956(81)80014-7.  Taking `k=5` is therefore valid.

Every interchange supplied on `S-I` uses two colours different from six.
The corresponding two-colour components in `G[S]` are unchanged by adjoining
the colour-six independent set `I`.  Hence the same interchanges are genuine
boundary Kempe interchanges, keep `I` fixed, and never put colour six on
`S-I`.

If the original exact-`I` endpoints use different names on `I`, a global
permutation of one complete endpoint colouring first aligns those names.
This preserves shore extension, but the Kempe sequence ends at the relabelled
endpoint.  The corrected source makes this distinction explicit and no
longer claims a fixed-`I` sequence between the two original labelled
endpoints.

## 4. Lemma 3.1: lift or interior path

Let `W` be one boundary component for colours `alpha,beta`.  All vertices of
`W` lie in one full `alpha,beta` component of `Y`.  If no full two-colour
component meeting `W` meets another boundary component, swapping every such
full component changes the boundary precisely on `W` and yields the requested
extension.

Otherwise a full component meets `W` and `S-W`.  A shortest path between
these two boundary sets has no internal vertex in `S`: any internal boundary
vertex belongs either to `W` or to `S-W`, and would shorten the chosen path at
the corresponding end.  Thus the asserted path and its literal interior
localization are valid.

## 5. Theorem 4.1: shortest-sequence endpoints

For a fixed nonempty independent `I`, exact-block trace gives nonempty sets
of exact-`I` boundary colourings extending to `A` and to `B`.  Global
colour permutations preserve extension through either shore, so normalize
each endpoint to give `I` colour six.  Corollary 2.2 puts these normalized
fixed-colour endpoints in one Kempe component.  Choose endpoint colourings
and a shortest sequence globally over those normalized choices.

The shore languages are disjoint, so the sequence has positive length.  If a
later sequence vertex extended to `A`, the suffix from the latest such vertex
to the chosen `B` endpoint would be shorter.  If an earlier vertex extended
to `B`, the prefix from the chosen `A` endpoint would be shorter.  Therefore
only the first sequence vertex extends to `A` and only the last extends to
`B`.  Applying Lemma 3.1 in the forward direction at the first edge and in
the reverse direction at the last edge is legitimate because a Kempe
interchange is an involution and preserves the underlying two-colour
component vertex sets.

For every extension of the first boundary colouring to `A`, failure of the
next boundary colouring to extend forces the Lemma 3.1 path.  Since
`A-S=C`, all its internal vertices lie literally in `C`.

At the other end, let `delta` be the colour of `u` in the chosen extension of
the last boundary colouring to `B`.  Completeness of `u` to `S` makes
`delta` absent from `S`.

- If the last interchange avoids `delta`, its obstructing bichromatic path
  avoids `u` and has interior in `B-(S union {u})`.
- If it uses `delta`, the induced two-colour graph on `S` contains only
  vertices of the other colour.  That colour class is independent, so every
  boundary component is a singleton.  Reversing the last interchange assigns
  its unique vertex `x` the colour `delta` of `u`.

These cases are exhaustive and mutually exclusive.

## 6. Literal component count and neighbourhood bound

The localization in the pole-free case is correct.  Distinct components of
`G-N[u]` are anticomplete.  Once `S`, `C`, and `u` are unavailable as internal
vertices, a path can pass between two other such components only through
`T=N(u)-S`.  A simple path uses each vertex of `T` at most once, so it has at
most `|T|+1<=3` exterior-component intervals and hence meets at most three
distinct components other than `C`.

For every such component `D`, the set `N_G(D)` separates `D` from `u`.
Seven-connectivity therefore gives `|N_G(D)|>=7`.  Also
`N_G(D) subseteq N(u)`: a neighbour outside `N[u]` would lie in the same
component as `D`, and no vertex of `D` is adjacent to `u`.  Inclusion--
exclusion inside `N(u)=S union T` gives

```text
|N_G(D) intersect S|
  >= |N_G(D)| + |S| - d_G(u)
  >= |S|-2
  >= 5.
```

The theorem claims this almost-full boundary contact, not literal fullness;
that distinction is preserved.

## 7. Theorem 5.1: edge-deletion anchoring

For `x in S`, proper-minor minimality gives a six-colouring `phi` of `G-ux`.
It must colour `u,x` alike, or it would already colour `G`.  Every other
boundary vertex is adjacent to `u`, so `{x}` is an exact boundary colour
block.

Choose an exact-`{x}` colouring of `B`, align the colour of `x` by a global
permutation, and use Corollary 2.2.  The resulting boundary sequence never
uses the common colour of `u,x`.  Starting from `phi`, a requested boundary
move lifts to `G-ux` unless its full two-colour component also meets another
boundary component.  If all moves lifted, the final colouring restricted to
`A` and the independently chosen colouring of the original `B` would agree
on `S` and glue to a six-colouring of `G`; importantly, the edge `ux` lies in
the original `B` and is proper there.  Hence some move fails.

At the first failure, the shortest obstruction path has interior outside
`S`.  It avoids both `u` and `x` because its two colours exclude their fixed
colour.  Since `(A,B)` is a separation, an internally boundary-free path
cannot pass from `C` to `B-S`; its interior is wholly in `C` or wholly in
`B-(S union {u})`.  The latter case inherits the already checked component
count and neighbourhood bound.  Thus Theorem 5.1 is valid.

## Trust boundary

The result supplies bichromatic paths and a bounded number of almost-full
exterior components.  It does not show that a returned path can be contracted
while preserving its endpoint colouring, that the path can be split into a
new branch set, that the two shores have a common equality partition, or that
the conditional boundary interface occurs without the audited low-degree
alignment theorem.  The source states these limitations correctly.
It also does not connect differently labelled exact-`I` endpoints while
leaving the colour on `I` unchanged; one endpoint must first be globally
relabelled.
