# Audit of the disconnected leaf-side completion

**Verdict:** GREEN.

**Audited source:**
[`hc7_star_order_eight_disconnected_leaf_side_completion.md`](hc7_star_order_eight_disconnected_leaf_side_completion.md)

**Promoted source SHA-256:**
`c27648dea26a24ae591a44baa71de6f80f16cf0c9c05cbab95892d6c9f98d09f`

**Original audited revision SHA-256:**
`0d2aaaf2cb57aed52b05faa0f5846e9155160360bd10d18cc92f96200b7696ea`

The promoted source differs from the original audited revision only in its
opening status paragraph: “written proof; awaiting a separate audit” was
replaced by a link to this GREEN audit, with corresponding line wrapping.
Mechanically restoring the original seven-line title/status block while
leaving the promoted theorem text unchanged reproduces the original
audited SHA-256 exactly.  No theorem statement, hypothesis, proof step,
corollary, or scope claim changed.  The GREEN verdict therefore rebinds to
the promoted source hash above.

The theorem closes the stated disconnected-leaf-side family and the stated
leaf-only-`x`-contact family.  It does not close the final connected
two-linkage obstruction or prove `HC_7`.

## 1. Quantifiers and setup

The theorem does not assume that `G-S` has exactly two components; it only
selects distinct connected components `C,D`, both full to the literal
boundary.  Every proof step remains valid if further components exist:
distinct components of `G-S` are anticomplete, and the selected nonempty
component `D` supplies the opposite side of every separator and the
opposite full branch set.

The two alternatives in the theorem are logically separate:

1. `C-{ell_e,ell_f}` has at least two components; or
2. every `x`--`C` edge ends at one of the two leaves.

Steps 1--4 prove the first alternative.  Only Steps 1, 2, and 4 are needed
for the second, so the statement correctly drops the disconnectedness
hypothesis there.

## 2. Step 1: component contacts

For a component `A` of `C-{ell_e,ell_f}`, connectedness of `C` gives
`t(A) in {1,2}`.  The displayed equality

\[
 N_G(A)=(N_G(A)\cap S)\mathbin{\dot\cup}
        (N_G(A)\cap\{\ell_e,\ell_f\})
\]

is exact.  There are no edges from `A` to another component after deleting
the leaves, nor to any other component of `G-S`.  Its neighbourhood
separates nonempty `A` from nonempty `D`.  Seven-connectivity excludes
orders at most six, and order seven is precisely an allowed theorem
conclusion.  Under the standing contradiction assumptions its order is at
least eight, proving

\[
                  |N_G(A)\cap S|\ge 8-t(A).
\]

The branch model (1.3) has seven disjoint connected branch sets.  All 21
adjacencies check:

- the three vertices of `R` give three mutual adjacencies;
- each of the four other branch sets contacts every `R` singleton, using
  respectively collective `g`--`R` contact, the two clique leaves, the
  assumed `A`--`R` contacts, and fullness of `D`;
- among those four sets, `g` contacts the leaf it does not omit, contacts
  `A` by its selection, and contacts `D` by fullness;
- the leaf-containing set contacts `A` because `t(A)>=1` and contacts `D`
  through a boundary endpoint of `h`; and
- `A union {x}` contacts `D` through an `x`--`D` edge.

No individual endpoint of `g` or `h` is assumed adjacent to all of `R`;
collective contact is sufficient for branch-set adjacency.  Hence every
component `A` must miss a vertex of `R union {x}`.

The conclusion that every `A` contacts both defect edges is also valid.
If `t(A)=1`, it has at least seven of the eight boundary neighbours, and
its forced miss in `R union {x}` is its unique miss; thus it contacts all
four endpoints of `e,f`.  If `t(A)=2`, it misses at most two boundary
vertices but already misses one in `R union {x}`; it therefore cannot miss
both endpoints of either edge.

## 3. Step 2: a leaf neighbourhood

If `ell_e` has no neighbour in the deleted interior, every one of its
neighbours lies in

\[
             \{\ell_f\}\cup R\cup V(f)\cup\{x\}.
\]

This set has order seven.  The omitted edge contacts do not enlarge it:
`ell_e` is anticomplete to `e`, and `C` has no edge to another component of
`G-S`.  Thus `d_G(ell_e)<=7`.  Seven-connectivity implies minimum degree
at least seven, so equality holds.  Deleting `N_G(ell_e)` leaves the
singleton `ell_e` and the nonempty component `D` on different open sides,
giving an actual order-seven separation.  The symmetric argument for
`ell_f` is valid after exchanging `e,f` and the two leaves.

Consequently, under the contradiction assumptions, each leaf has a
neighbour in `C-{ell_e,ell_f}`.

## 4. Step 3: every leaf-incidence case

Suppose an interior component `A` contacts `x`.

- If `A` contacts only `ell_f`, Step 2 supplies a different component `B`
  contacting `ell_e`.  Step 1 says `B` contacts `V(e)`.  Connectedness of
  `A,B` produces disjoint connected subgraphs joining `ell_f` to an
  `x`-contact and `ell_e` to an `e`-contact.
- If `A` contacts only `ell_e`, the symmetric construction uses `f`.
- If `A` contacts both leaves, hypothesis 6 supplies another component
  `B`.  If `B` contacts `ell_e`, the original orientation uses `A` for the
  `ell_f`--`x` subgraph and `B` for the `ell_e`--`e` subgraph.  Otherwise
  `B` must contact `ell_f`, and the symmetric orientation uses `A` for the
  `ell_e`--`x` subgraph and `B` for the `ell_f`--`f` subgraph.

The two selected subgraphs are disjoint in every case because their
interiors lie in different components after deleting the two distinct
leaves.  All other hypotheses of the promoted split-edge completion are
present literally.  Thus every case produces the claimed `K_7` minor, and
under hypothesis 6 there can be no interior `x`-contact.

## 5. Step 4 and the second theorem alternative

Boundary fullness at `x` ensures an `x`--`C` edge.  Once all such edges
end at the leaves, choose an adjacent leaf, say `ell_f`, as the singleton
first subgraph.  Step 2 supplies a component `B` adjacent to the other leaf
`ell_e`, and Step 1 supplies a contact from `B` to `V(e)`.  A path inside
`B union {ell_e}` is the disjoint second subgraph required by the promoted
completion.  The construction is symmetric if `x` contacts `ell_e`
instead.

This step does not use hypothesis 6.  It therefore proves both the last
step of the disconnected case and the theorem's independent leaf-only
contact alternative.

## 6. Corollary 2

Under `K_7`-minor-freeness and exclusion of an actual order-seven
separation:

- Theorem 1 forbids two or more components after deleting the leaves;
  Step 2 guarantees that the deletion is nonempty, so it has exactly one
  connected component.
- The second alternative of Theorem 1 forces an interior `x`-contact.
- Step 2 forces both leaf contacts.
- Step 1 forces contacts with both `V(e)` and `V(f)`.
- For the unique component, `t(A)=2`, so it has at least six boundary
  neighbours.  It must miss a vertex of `R union {x}`; the interior
  `x`-contact means the missed vertex lies in `R`.  Hence it has at most
  seven boundary neighbours and misses exactly one or two vertices.

The promoted split-edge completion and its symmetric form then forbid the
two labelled disjoint-path configurations exactly as claimed.  This is a
description of the remaining local obstruction, not an assertion that no
other global branches of the support-six programme remain.
