# Audit: polarized responses in the degree-eight `P_3`-plus-edge reserve

**Audit type:** separate internal cold audit

**Verdict:** **GREEN**

Audited theorem:
[`hc7_degree8_p3k2_polarized_response.md`](hc7_degree8_p3k2_polarized_response.md)

Audited source SHA-256:

```text
2ae33549d2b78b83cf3e7f6ad19e3ff48f8e02d0771e9f025468e2e474201708
```

## Fixed-colouring carriers and the three contractions

For fixed `z`, the paths for `ac,az` use only the three fixed colour
classes represented by `T_z`, while the path for `b bar-z` uses the two
disjoint colour classes represented by `P_z`.  Their boundary endpoints
are disjoint, so the connected union `L_z` and the path `Q_z` are
vertex-disjoint.  Their open interiors lie in `E`, and neither meets the
independent boundary block `I`.

The three sets `{u} union I`, `V(L_z)`, and `V(Q_z)` are therefore
pairwise disjoint and connected.  Contracting a spanning tree in each
strictly reduces the graph, so proper-minor six-colourability applies.
After retaining the opposite shore and expanding the three contraction
vertices only over `I,T_z,P_z`, properness follows from the independence
of those three boundary sets and from the fact that every retained
incident edge was represented after contraction.

The first contraction vertex is adjacent to the other two through `u`.
The latter two are adjacent through `ab` or `bc`, and also through `de`.
Their colours are consequently distinct, giving exactly

```text
I | T_z | P_z
```

on the `F`-closed shore.  No disjointness between the carriers for the two
different choices of `z` is used or claimed.

## Pole-side polarization

The sets `{u} union I` and `F union T_z` in Theorem 3.1 are disjoint and
connected.  The latter is connected because `F` is full to `X`.
Contracting both, colouring the proper minor, and expanding only over
`I,T_z` gives a proper colouring of `G[E union X]`.  The remaining roots
`b,bar-z` avoid both block colours: each sees the first contraction image
through `u` and the second through `F`.

If these two roots were equal-coloured, this pole-side colouring and the
coarse opposite-shore colouring would induce the same complete boundary
partition.  A blockwise colour bijection extends to a permutation of all
six colours, after which the shore colourings glue to colour `G-u`.
Only three colours occur on `X`, so a colour absent from `X` can be assigned
to `u`.  This contradiction forces the split partition in (3.1), for each
separately selected `z`.

## The two reverse Kempe obstructions

For one row of (3.2), the fine and coarse palettes can be aligned on
`I,T_z` and on the colour `beta` at `bar-z`.  The fine colour `alpha` at
`b` is absent from the coarse boundary.  Thus the two boundary colourings
differ only by changing `b` between `alpha` and `beta`.

In the fine `E`-shore colouring, if the full two-colour component through
`b` missed `bar-z`, its only boundary vertex would be `b`.  Swapping it
would produce the coarse boundary partition, which glues to the selected
coarse `F`-shore colouring and then extends to `u`.

Conversely, in the coarse `F`-shore colouring, `b,bar-z` are nonadjacent
vertices of colour `beta`, and `alpha` is absent from `X`.  If their full
two-colour components were distinct, swapping the component through `b`
would produce the fine boundary partition and the same gluing
contradiction.  Hence each shore contains the claimed bichromatic joining
path.  Only the two endpoints use its colours on `X`, so a shortest path
has no internal boundary vertex and its open interior lies wholly in the
named component.  The proof correctly keeps the two rows independently
quantified.

## Kriesell--Mohr hypothesis match

Let `Gamma` be the fixed colour class containing `I` and
`Q=(G-u)-Gamma`.  The restriction of the fixed colouring makes `Q` a
five-coloured graph with `R` as a transversal.  Every selected reserve
path uses two of the five singleton reserve colours, not the colour of
`Gamma`; the assumed `E`-interior paths for the six demands in `D_0`
therefore lie in `Q[E union R]`.  Each demanded root pair consequently
belongs to one component induced by its two colour classes.

Kriesell--Mohr, *Kempe Chains and Rooted Minors*, Theorem 7 states that
every graph on five vertices with at most six edges has property `(*)`.
Applied to the six-edge spanning demand graph `(R,D_0)`, this gives five
pairwise disjoint connected rooted bags in `Q[E union R]`, adjacent on all
six demands.  This is the exact hypothesis and conclusion of the cited
theorem; neither an unproved seven-demand instance nor property `(*)` for
`K_5` is used.  The three literal root edges `ab,bc,de` leave at most the
chosen pair `f` missing.

## Bilateral-path completion

For `f=be`, use the `z=d` response path; for `f=bd`, use the `z=e` path.
Its open interior lies in `F` and it meets `X` only at its two ends.  The
five rooted bags lie in `E union R`, so splitting this path at one edge
and adjoining the two disjoint subpaths to the corresponding endpoint
bags preserves connectivity and pairwise disjointness.  The split edge
supplies the only possibly absent adjacency, while every old adjacency
survives.  The result is an `R`-rooted `K_5` model in `G-u`.

This construction legitimately uses both exterior components.  It does
not leave, or claim to leave, a connected seventh bag.  Accordingly it is
not an explicit `K_7`-minor model.

## Response square, links, and trust boundary

The horizontal relations in (6.1) are exactly the singleton boundary
interchanges analysed above.  For each vertical relation, the two selected
colours induce the separate boundary edge `de`; on the coarse side the
other component is `a-b-c`, while on the fine side `a,c` are isolated.
Swapping the `de` component gives the displayed partition.  The source
correctly states this only at boundary level and does not infer a
same-shore full Kempe interchange.

All four local source links resolve.  The cited statement of
Kriesell--Mohr Theorem 7 matches both the primary source and its already
audited use in the five-reserve Kempe-packet theorem.

No gap remains in Theorems 2.1--5.1 at the audited hash.  The proof depends
on the full proper-minor colouring hypothesis, the two literal full
components, the fixed six-colouring with its exact boundary partition,
and `E`-interior fixed-colouring paths for all seven reserve nonedges.  It
proves a two-shore rooted `K_5`, not a reserved-shore model, bounded
separation, strict component descent, `K_7` model, or `HC_7`.

The status-only promotion linking this audit has SHA-256
`0cab22c0dd61f4c668cc5784772ca48673b66d98a735ea3c53723e0066c276e8` and
makes no mathematical change to the audited revision.
