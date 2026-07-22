# Separate internal audit: full exterior common-root exchange

**Verdict:** GREEN.

This is a separate internal cold audit, not external peer review.  The
source proves a precise reduction for the multi-component, singleton-
rejection case; it does not prove `HC_7`.

## Exact revisions audited

The mathematical theorem was audited at

```text
050311ac7489eb51d8ec49c19fd31ea9d8a9552669d11ddf569bd20d594a2b4c  audited theorem content
```

Promotion changed only its status paragraph.  The promoted source hash is

```text
11f7c6433687847edc3635f3284a074fa2f6157c304035ea9fc42e6a224fbc2f  results/hc7_full_exterior_component_common_root_exchange.md
```

The two promoted inputs used directly were checked at

```text
a6046ab5538b8468bdc211d40b537dec5fca909d47ab9c30acb197d74767410e  results/hc7_component_uniform_boundary_alignment.md
f2dcd7f81c7994b5344748bcd29f6b685f02cfb50c776816ea7d16bfad61b21b  component-deletion exchange audited content
```

Any mathematical change to the theorem or either invoked input invalidates
the affected part of this audit until it is renewed.

## Claim checked

Suppose that a hypothetical minor-minimal counterexample is entered at a
degree-eight or degree-nine vertex with at least two exterior components,
and every labelled boundary five-colouring is rejected by exactly one
component.  The source proves:

1. either one component has a literal boundary of lower order, together
   with its own deletion response; or
2. there are exactly two exterior components, both full to the common
   neighbourhood, and one legal single-vertex recolouring transfers the
   unique rejection between them.

In the second outcome the two failed lifts have the same literal boundary
root `x`, their supported nonedges form a `K_6`-minor-free augmentation,
and `chi(G-x)=6`.  Completion by the singleton `{x}` is reduced to a
`K_6` model in `G-x` all of whose branch sets meet `N(x)`.  These
claims are established.

## 1. Lower boundary outcome

If an exterior component `E` is not full to `X=N(u)`, its neighbourhood
separates it from `u`.  Seven-connectivity and non-fullness give
`7<=|N(E)|<=d(u)-1`.  The separately audited component-uniform theorem
applies to this literal component and supplies `z_E in N(E)` with
`chi(G-{u,z_E})=6`.  The source correctly warns that lower separator
order alone is not a strict component-size descent.

## 2. Compact minor exclusion

For two full components `C,D`, a `K_4` model in
`H-{z_1,z_2}` combines with

```text
{u}, C union {z_1}, D union {z_2}
```

to give seven pairwise adjacent connected bags.  Fullness supplies every
component-to-boundary adjacency, including the adjacency between the two
anchored component bags.  Thus every two-vertex deletion of `H` is
`K_4`-minor-free.

All later displayed `K_7` models were checked similarly:

- five singleton vertices of a boundary `K_5`, with two anchored full
  components;
- for at least five components of `G-X` and a boundary edge, two endpoint
  singletons, four distinctly anchored full components, and one unanchored
  full component; and
- for four components of `G-X` and a boundary triangle, its three
  singleton vertices, three anchored full components, and one unanchored
  full component.

Every bag is literal, connected and disjoint, and fullness supplies all
cross-bag adjacencies.

## 3. Three-degeneracy

If an induced `F subseteq H` has minimum degree four, contracting two full
components and retaining `u` produces exactly `overline K_3 vee F`.
Mader's exact `K_7` extremal bound and the degree sum force
`|E(F)|=2|V(F)|`, so `F` is connected and four-regular.

For each edge `xy`, the graph `J=F-{x,y}` is `K_4`-minor-free and has
`2|V(J)|-3` edges.  The equality characterization for the exact
`K_4` extremal bound makes `J` a 2-tree.  Its degree-two vertices show
that every edge of `F` has at least two common neighbours.

The four-regular classification is exhaustive.  For a vertex `v`, the
four-vertex graph induced by `N_F(v)` has minimum degree at least two and
is therefore `C_4`, `K_4-e`, or `K_4`.  The three cases force,
respectively, the octahedron, a degree contradiction, or `K_5`.
Independent enumeration of all connected four-regular graphs of orders
five through nine reproduced only `K_5` and `K_{2,2,2}` under the
two-common-neighbour condition.  The source closes both by its explicit
minor constructions.  Hence `H` is three-degenerate.

## 4. Recolouring and the common root

The inductive single-vertex recolouring argument is valid for five
colours on a three-degenerate graph.  At a deleted vertex of degree at most
three, its current colour and at least one other colour are absent from its
neighbourhood whenever a temporary move is required.

Every exterior component occurs as the unique rejector of its private
component-deletion colouring.  The rejection label is therefore a
nonconstant map on a connected single-vertex recolouring graph.  Some
legal recolouring of one vertex `x`, from `alpha` to `beta`, transfers
the label from `C` to `D`.  Properness makes `{x}` the operated
component in the two-colour boundary graph.

The lifting directions were checked.  Reverse lifting the
`psi`-extension through `C` yields a path from `x` with an
`alpha`-coloured first exterior neighbour.  Forward lifting the
`phi`-extension through `D` yields a path from the same `x` with a
`beta`-coloured first exterior neighbour.  Their open interiors lie in
different anticomplete components and contract simultaneously, including
when their other endpoints coincide.  A `K_6` model in the resulting
boundary augmentation would lift to six bags meeting `X`, and
`{u}` would complete an explicit `K_7` model.

## 5. Exactly two full exterior components

Let `q=1+#comp(G-N[u])`, counting `{u}` among the full components of
`G-X`.

If `q>=5`, a boundary edge gives the explicit model audited in Section 2.
If the boundary is edgeless, contract the star `u union X`, six-colour
the proper minor, discard `u` and all but one exterior component when
expanding the independent boundary, and repeat for every retained
component.  The one boundary colour aligns across the sides and a second
colour can be given to `u`.

If `q=4`, a boundary triangle gives the second explicit model.  Otherwise
the source correctly three-colours every triangle-free graph on at most
nine vertices: use Brooks componentwise when the maximum degree is at most
three, and otherwise colour an independent neighbourhood and the bipartite
antineighbourhood separately.  Splitting colour classes gives three
nonempty independent boundary blocks.  For each retained exterior side,
the other three full components of `G-X`, including `{u}`, are
contracted with the three blocks.  These sets are connected and pairwise
adjacent.  Expansion and palette alignment colour every retained side;
a fourth boundary-absent colour on `u` completes a six-colouring.

Thus `q` is neither at least five nor four.  Since at least two exterior
components were assumed, `q=3`, and exactly `C,D` remain.

## 6. Rooted residue

Delete `x`.  The `psi`-extension through `C` and the
`phi`-extension through `D` agree on `X-{x}`, the two components are
exhaustive and anticomplete, and colour six can be assigned to `u`.
This proves `chi(G-x)<=6`.  A five-colouring of `G-x` would extend to a
six-colouring of `G`, so equality holds.

The established case `HC_6` therefore supplies an unrooted `K_6` minor
in `G-x`.  The proof correctly stops: it does not show that all six bags
meet `N(x)`.  The stated rooted condition is exactly what is needed to
complete this construction using the singleton bag `{x}`; the audit does
not assert that it is necessary for every conceivable `K_7` construction.

## 7. Trust boundary

No finite computation is part of the theorem.  The independent
four-regular enumeration was an audit cross-check, not a proof dependency.
The proof uses Mader's exact `K_4` and `K_7` extremal results, the
equality characterization of extremal `K_4`-minor-free graphs, Brooks'
theorem, and the established case `HC_6`.

The common-root outcome is a sharp structural reduction, not a terminal
theorem.  A bare unrooted `K_6` minor cannot be adjoined to `{x}`
without proving the six required neighbourhood contacts.
