# Independent audit: component-uniform boundary alignment

**Verdict:** GREEN.

This is an internal cold audit, not external peer review.  The verdict is
conditional on the already GREEN-audited low-degree local-completion result,
its retained degree-nine verifier, and Mader's exact extremal bound.  The
source theorem does not prove `HC_7`.

## Exact revisions audited

The mathematical theorem content was audited at

```text
326c6f9239c6af58d4902726aa5d66f7240c07cd29b153c3223bef2d7293e439  audited theorem content
ba84bb4f3702ba47a1248a9b746b0c24a383a806e8135569ae024958ad1d1754  results/hc7_component_uniform_alignment_verifier.py
```

Promotion changed only the status paragraph.  The promoted theorem source
hash is

```text
a6046ab5538b8468bdc211d40b537dec5fca909d47ab9c30acb197d74767410e  results/hc7_component_uniform_boundary_alignment.md
```

The principal promoted dependencies remain pinned at

```text
263611a40dc7829788967250e031a3f3170e1c7a6c8c9a3fbfbb358231b1f9ca  results/hc7_low_degree_adjacent_pair_alignment.md
dd8817ceec58b083e12adae943f49cf2bb5a401f17ca87950477906f811c5a08  results/hc7_degree9_pole_verifier.md
b4bab9be44feb5dc749dc8ba3f41a85094896d4b3de8a7d8246342b2729c9c59  results/hc7_degree9_pole_verifier.py
```

Any mathematical change to the theorem, finite verifier, or invoked local
completion invalidates this audit until the affected checks are renewed.

## Claim checked

Under the hypothetical-counterexample hypotheses, for every vertex `u` with
`7<=d_G(u)<=9` and every component `D` of `G-N[u]`, the source proves that
some literal vertex `z_D in N_G(D)` satisfies

```text
chi(G-{u,z_D}) = 6.
```

The choice is component-specific.  It follows that every such component has
the complete bounded-interface entry and its own named edge-deletion
response.  An actual component `D` with `|D|<|C|` is therefore a strict
same-host restart even when the old vertex `z_C` is not adjacent to `D`.

These conclusions are established.  The theorem does not force a smaller
component to occur and does not close either remaining bridge-composition
case.

## 1. Recolouring and the degree-five boundary condition

For `S=N_G(D)`, seven-connectivity gives `S subseteq N(u)` and
`7<=|S|<=d_G(u)<=9`.  If no member of `S` gives a six-chromatic double
deletion, each graph `G-{u,s}` is five-chromatic: proper-minor minimality
gives the upper bound six, while a four-colouring would extend with two new
colours and contradict `chi(G)=7`.

In a five-colouring of `G-{u,s}`, suppose colour `i` has no common neighbour
of `u,s`.  Recolour all colour-`i` neighbours of `u` with a new sixth colour,
give `u` colour `i`, and give `s` the new colour.  The recoloured set is
independent, is anticomplete to `s`, and no neighbour of `u` retains colour
`i`.  This is a proper six-colouring of `G`, a contradiction.  Thus five
distinct common neighbours exist and `d_{G[N(u)]}(s)>=5` for every `s in S`.

## 2. Analytic cases and edge counts

When every vertex of `H=G[N(u)]` has degree at least five, contracting `D`
gives exactly the previously audited degree-seven/eight/nine local
completion.

If one vertex `x` of `H` lies outside `S` and has degree at most four, then
minimum degree in `G` gives an exterior support component `E` met by `x`.
It differs from `D`, and seven-connectivity gives `|N_G(E)|>=7`.  The source
correctly counts the following strict Mader inequalities after the displayed
contractions:

```text
d_G(u)=8:  7 + |E(H-x)| + 7 + 6 >= 36 > 35;
d_G(u)=9:  8 + |E(H-x)| + 8 + 6 >= 41 > 40;
equality residue before deleting x: 9 + 22 + 8 + 7 = 46 > 45.
```

No edge class is counted twice.  Deleting `x` leaves at least six neighbours
of the contracted support component because its original boundary has order
at least seven and contains `x`.

With two vertices outside `S`, necessarily `d_G(u)=9` and `|S|=7`.  A low
outside vertex again has a support component distinct from `D`.  For
`|E(H)|>=23`, contracting one support and `D` gives twelve vertices and at
least

```text
9 + 23 + 7 + 7 = 46 > 45
```

edges.  Since the seven vertices of `S` have degree at least five in `H`,
`|E(H)|>=18`; hence the finite layers 18 through 22 exhaust the residue.

## 3. Finite classification

The subject verifier was read completely and rerun with the repository
virtual environment and nauty `geng`.  It returned

```text
partial_partitions=5880
marked by layer: 2, 26, 236, 1270, 4379
total_marked=5913 residues=2
catalogue_sha256=2f0b0786c48521751dd720fa84b4999fbeea22d26f82c915cdd98946aec7d5be
witness_sha256=6243e811f0100d305e2f14203a3058a192e81963d281c3e996c8a65c3ddb24d2
residue_sha256=e107285f3bb4f6e10522ce1515229b2a2dde5e5fb6bd4715064aba6ca01145ff
PASS component-uniform alignment classification
```

The enumeration is complete.  `geng` supplies every unlabelled
nine-vertex graph in each edge layer, and testing every two-set `T` covers
every marked isomorphism type.  The 5,880 candidates are every partition of
an arbitrary subset of `V(H)` of order at least six into six nonempty bags.
The contracted component vertex is independently omitted or assigned to
one of the six bags.  Thus unused `H`-vertices are allowed; the invalid
earlier spanning-only inference is not present.  The checker then verifies
bag disjointness, an `H`-vertex in every bag, connectedness, and all fifteen
pairwise adjacencies.

As a separate check, a temporary NetworkX catalogue and certificate
validator independently matched all graph and marked-pair counts and
validated all 5,911 positive certificates.  A connected-subset
compatibility-clique oracle independently found no rooted model in either
residue.  Its cold-audit source hash was

```text
93977c3d11df544ca48b9463e29cf0a1337b2adc1affca861d8ffca01d49e12b
```

Both marked graph6 residues were independently decoded and matched the
stated `H_-` and `H_+` structures.

## 4. Exceptional contractions and lift

In both exceptions the two outside vertices have degree at most four, so
each has an exterior support component.  If the selected supports are
distinct, absorbing each low vertex into its support preserves every old
degree at `S`; each new vertex has at least six neighbours.  The resulting
nine-vertex neighbourhood therefore has minimum degree at least five and
the audited degree-nine completion applies.

If the supports coincide, their union with both low vertices is connected.
The exceptional graphs have disjoint `S`-neighbourhoods at the two low
vertices, so identifying them loses no degree at `S`; the new vertex sees
the two displayed triangles and has degree at least six.  The resulting
eight-vertex neighbourhood has minimum degree at least five, and the audited
degree-eight completion applies.

Every rooted finite model has all six branch sets meeting `H=N(u)`.  Lifting
the contracted component restores a connected branch set and all recorded
adjacencies; the singleton `{u}` is adjacent to all six branch sets and
completes the `K_7` model.  Minor transitivity supplies the same lift in the
Mader and exceptional-completion cases.

## 5. Trust boundary

The audit does not assert:

1. that a bridge path must meet a component smaller than the selected one;
2. that equal-order exterior components can be combined or synchronized;
3. that the tight pole residue is eliminated; or
4. that `HC_7` follows from component-uniform alignment alone.

The proved advance is exact: response-label preservation is no longer an
obligation when the recursive outcome is an actual smaller component of
`G-N[u]`.
