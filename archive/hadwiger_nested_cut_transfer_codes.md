# What a nested exact cut actually transports

## Status

The theta theorem strictly descends to a proper nested exact seven-cut.
This note identifies the exact finite colouring datum carried through the
annulus between the two cuts.

Seven disjoint transport paths preserve the old boundary graph only as a
rooted minor shell. They do not preserve the graph induced by the new cut,
a boundary equality partition, or either theta orientation bit. The right
object is the full two-boundary six-colour transfer relation. These
relations compose exactly and transport all faithful-operation codes.

There is no partition-only decreasing potential under transport paths
alone. An explicit connected `K_7`-minor-free annulus implements a
nontrivial permutation of seven boundary colours, and an inverse annulus
returns every state.

## 1. The rooted shell

Let disjoint nested cuts `S,Z` split a graph into an outer piece `O`, an
annulus `A`, and an inner piece `I`. Thus adjacent pieces meet exactly in
`S` and `Z`, respectively, and there are no other cross-edges. Suppose
`A` contains seven pairwise vertex-disjoint paths `P_s`, one from each
`s in S` to a distinct vertex `z_s in Z`.

### Lemma 1.1 (automatic graph transport)

The sets `V(P_s)` form a rooted model of `G[S]`, with the bag indexed by
`s` meeting the new cut in `z_s`.

#### Proof

The paths are disjoint and connected. Every old edge `st` remains an
edge between the bags containing its literal ends `s,t`. The endpoint
condition supplies the roots on `Z`. QED.

Contracting the paths therefore transports the old shell as a graph
minor. It says nothing about `G[Z]`: the old shell edges remain at the old
ends of the path bags and need not be literal edges of the new cut. This
prevents a direct reapplication of the theta exact-block theorem at `Z`.

## 2. Exact boundary transfer codes

For a graph `H` with boundary `B`, define

```text
Ext6(H,B) = { assignments a:B->[6] extending to a proper 6-colouring of H }.
```

For an annulus with boundaries `S,Z`, define

```text
T_A = { (a,b) : a on S and b on Z extend together over A }.
```

Assignments are kept labelled. Quotienting by one simultaneous
permutation of the six colours is harmless, but retaining only the two
marginal equality partitions loses which colour on `S` equals which
colour on `Z`.

### Theorem 2.1 (exact pullback and gluing)

For every inner piece `I`,

```text
Ext6(A union I,S) = { a : some b in Ext6(I,Z) has (a,b) in T_A }.
```

Consequently `G` is six-colourable exactly when this pullback intersects
`Ext6(O,S)`.

#### Proof

A colouring of `A union I` restricts to a transfer pair `(a,b)` and an
inner assignment `b`. Conversely, colourings agreeing literally on `b`
glue because the pieces share only `Z`. Glue once more across `S` for the
second assertion. QED.

### Corollary 2.2 (annular composition)

If `A_1` runs from `S` to `Z` and `A_2` from `Z` to `W`, then the
transfer relation of their union is the ordinary relational composition
of `T_A1` and `T_A2`, using literal equality of the intermediate
assignment on `Z`.

If colour-permutation orbits are stored instead, every alignment of
colours absent from `Z` must be included. Marginal equality partitions
alone do not determine the composition.

## 3. Faithful operations use the same pullback

Let `o` be any proper minor operation supported strictly in `I-Z`, and
put `E_o=Ext6(o(I),Z)`.

### Theorem 3.1 (operation-signature transport)

For every faithful inner operation,

```text
Ext6(A union o(I),S) = T_A^{-1}(E_o).
```

Thus the whole family of faithful-operation codes at `Z` is transported
exactly by applying the same relational pullback to every member.

#### Proof

Apply Theorem 2.1 with `o(I)` in place of `I`. QED.

This family, not one boundary state, is the data preserved by theta
descent. A state match with an opposite faithful operation closes by the
standard crossed splice, provided the operation lies on the side whose
colours are discarded. One operated colouring alone never restores its
deleted or contracted object.

## 4. A permutation transfer cycle

Fix a permutation `pi` of seven labels. For each `i`, take a fresh
five-clique `C_i`, make it complete to the two nonadjacent boundary
vertices `s_i` and `z_pi(i)`, and add no other edge incident with those
two vertices inside the gadget. Connect the seven gadgets by six bridge
edges in a tree; call the result `A_pi`.

### Lemma 4.1 (exact permutation code)

Every proper six-colouring of `A_pi` satisfies

```text
colour(z_pi(i)) = colour(s_i) for every i.
```

Conversely every boundary assignment satisfying these equalities extends
over `A_pi`.

#### Proof

Each `C_i` uses five distinct colours. Both endpoints are adjacent to all
five clique vertices and not to one another, so they receive the same
sixth colour. Conversely colour `C_i` with the other five colours. Their
orders can be chosen successively along the tree of bridge edges so the
two ends of each bridge differ. QED.

Each gadget is `K_7` minus the edge between its endpoints and has no
`K_7` minor. Intergadget edges are bridges. Every clique minor of order at
least three lies in one 2-connected block, so the connected annulus is
also `K_7`-minor-free. Choosing one clique vertex per gadget gives seven
disjoint length-two transport paths.

Concatenate `A_pi` with `A_pi_inverse`. By Corollary 2.2 the composite
transfer is the identity on every labelled boundary assignment.

### Theorem 4.2 (no linkage-only strict state order)

No isomorphism-invariant function of a boundary colour assignment or
equality partition strictly decreases across every `K_7`-minor-free
annulus having seven disjoint transport paths.

#### Proof

Take `pi` to be a nontrivial seven-cycle. Strict decrease through `A_pi`
and its inverse would make a state strictly smaller than itself. If the
function ignores labels, the first permutation already leaves its value
unchanged. QED.

The verifier `nested_cut_transfer_cycle_verify.py` brute-forces the local
six-colour equality gadget, constructs a connected 91-vertex
forward/inverse architecture, checks its fourteen `K_7-e` blocks and six
bridge blocks, exhibits both seven-path linkages, and verifies identity
composition.

## 5. Exact endpoint of theta descent

Theta descent is well-founded in vertex set: each new inner shore is a
proper subset of the old one. Its theta boundary hypothesis is not
preserved. The rooted shell of Lemma 1.1 and the transfer signature of
Theorem 3.1 are preserved instead.

A genuine termination theorem must therefore prove a new
counterexample-specific assertion of the following kind:

> Every transfer relation arising between nested minimum seven-cuts of a
> 7-contraction-critical `K_7`-minor-free graph is state-contracting,
> exposes a common crossed-operation code, or yields a labelled `K_7`
> model.

The permutation architecture is not seven-connected or
contraction-critical, so it does not refute that target. It proves that
those hypotheses must be used: disjoint transport paths, minor-freeness,
finite boundary type, and strict shore inclusion alone do not give a
decreasing partition potential.
