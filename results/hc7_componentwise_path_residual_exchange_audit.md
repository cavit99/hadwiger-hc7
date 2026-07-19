# Independent audit of componentwise exchange at a forced boundary path

**Verdict:** **GREEN** for Lemma 2.1, Theorem 3.1, Corollary 3.2 and
Theorem 4.1 at the exact source revision below.

**Audited source:** `results/hc7_componentwise_path_residual_exchange.md`

**Audited source SHA-256:**

```text
ea1467caf64aa3019d7d86f4d0aa118f73b79f04d7fe7284e61a3addb36900b9
```

The change from the initially checked source is limited to the opening
status line recording this GREEN audit; the mathematics is unchanged.

This is a separate internal mathematical audit, not external peer review.

## 1. Disjointness and connectedness of the block realizations

Let `R` be a component of `G[V(P_1)-T]`, where
`T=V(P)\cap V(P_1)`.  Since `P_1` is connected and `T` is nonempty, `R`
has an edge to `T`.  Also `R` is disjoint from `V(P)`: any vertex common
to `R` and `P` would belong to `T`, whereas `R` lies in `V(P_1)-T`.
The hypotheses that `P_1,P_2` are disjoint and that `P` avoids `P_2`
therefore make all sets in (2.3) and (2.4) pairwise disjoint.

For `Pi_A`, in the representative case `Q_r(D)`, the sets

```text
R union D,   V(P_2) union E,   V(P)-{r},   {r}
```

are connected and pairwise adjacent:

- `R union D` is connected because every vertex of `D` has a neighbour
  in connected `R`;
- `P_2 union E` is connected because `P_2` meets every boundary vertex;
- `V(P)-{r}` is connected and nontrivial because `rz` is a nonedge;
- the first and third sets meet by an `R`--`T` edge;
- the first and second meet through a `P_2`--`D` edge;
- the second and third meet through a `P_2`--`z` edge; and
- `{r}` meets the second and third sets by fullness and the first path
  edge, and meets the first either through an `r`--`D` boundary edge or
  through the extra required `R`--`r` contact.

Interchanging `D,E` and/or `r,z` preserves this verification and proves
all four cases in (2.1).  For `Pi_B`, the three sets in (2.4) are connected,
disjoint and pairwise adjacent by the same `R`--`T`, `P_2`--boundary and
`P_2`--`D` (or `P_2`--`E`) edges.

## 2. Contractions, exactness and gluing

Each contracted set contains a boundary-contact edge, so the simultaneous
tree contractions produce a proper minor.  The resulting representatives
form a clique with one representative for each block of the selected
partition.  Hence a six-colouring assigns distinct colours to distinct
blocks.

The proof pulls this colouring back only to the untouched closed shore
`G[B union S]`; it never expands a contracted connected subgraph on its
own shore.  The boundary blocks `D`, `E`, and (in `Pi_B`) `{r,z}` are
independent because they are colour classes of the given proper boundary
colouring.  Thus giving every vertex of a block the colour of its
contraction representative is proper on the untouched shore.  Edges from
a block to `B` became edges incident with its representative, and edges
between distinct blocks are protected by the clique of representatives.
The returned equality partition is therefore exact, not a coarsening.

The original colouring of `G[A union S]` has the same exact partition.
The two injective block-to-colour maps differ by a partial permutation of
the six colours, which extends to a global colour permutation.  After
alignment the shore colourings agree on every literal boundary vertex and
glue because there is no `A`--`B` edge.

## 3. Componentwise missing contacts and separator excess

If `Pi_B` does not glue, Lemma 2.1 forces `R` to miss a vertex of each of
`D` and `E`.  If `Pi_A` does not glue, missing no boundary vertex meets all
four required contact sets, while missing exactly one boundary vertex
meets one of the four sets listed in lines 209--212.  Hence in either case

```text
|Lambda_R| >= 2.
```

By the definitions of `U_R` and `Lambda_R`, the equality

```text
N_G(R) = U_R dotunion (S-Lambda_R)
```

is literal and complete.  The old opposite shore `B` is nonempty and
anticomplete to `R`, so this full neighbourhood separates two nonempty
sets.  Seven-connectivity gives

```text
|U_R| + 7 - |Lambda_R| = |N_G(R)| >= 7,
```

which is exactly `|U_R|>=|Lambda_R|`.  Zero excess is therefore an actual
order-seven full-neighbourhood separation.  If `|U_R|<=2`, the already
proved lower bound on `|Lambda_R|` forces both quantities to equal two.

## 4. Strict generic restart at zero excess

For a crossing edge `xy`, with `x in R` and `y in N_G(R)`, every
six-colouring of the proper minor `G-xy` makes `x,y` monochromatic;
otherwise restoring the edge would six-colour `G`.  The colouring is
proper on the opposite closed shore.  Its complete boundary partition
cannot extend through the intact closed `R`-shore, since an extension with
the same equality partition would align and glue.

Thus the data satisfy the audited definition of a generic exact-seven
selected-response interface.  The decrease is host-measured:

```text
R subseteq V(P_1)-T,   T nonempty,
```

so `|R|<|V(P_1)|<=|A|`.  This restart does not claim to preserve the old
partition, the five inherited boundary vertices or old minor-model labels.

## 5. Path-component descent

At an actual order-seven separation, every component of either open shore
is adjacent to every boundary vertex: otherwise at most six boundary
vertices separate it from the nonempty opposite shore.

If a path component is the edge `uv`, seven-connectivity gives each
endpoint at least six boundary neighbours.  An endpoint missing a boundary
vertex consequently has full neighbourhood of order seven.  If neither
does, the two endpoint singletons and a different same-shore component are
three disjoint boundary-full connected subgraphs; any opposite-shore
component supplies the fourth.  The audited adaptive `(1,3)` theorem then
gives a `K_7` minor or a six-colouring, both excluded by the hypotheses.

If the path has order at least three, deleting an internal vertex `w`
leaves two connected subpaths `C_1,C_2` with

```text
N_G(C_i) = {w} dotunion N_S(C_i).
```

Seven-connectivity again gives at least six boundary neighbours.  A
deficient side yields an order-seven full neighbourhood; if both sides are
boundary-full, they and the other same-shore component give the forbidden
`(1,3)` configuration.  In every surviving case the returned connected
set is a proper subset of the old path component.  The final edge-deletion
argument is the same valid generic restart checked in Section 4.

## 6. Trust boundary

The source proves an unbounded componentwise extension of the earlier
connected-residual argument.  It does not prove that any residual component
has zero excess, does not transfer the old complete partition through the
new separator, and does not close the positive-excess or singleton modes.
The minimum-interface consequence applies after viewing each full component
as the connected shore of its own generic interface; it does not assert
that a generic interface itself has a disconnected selected shore.
