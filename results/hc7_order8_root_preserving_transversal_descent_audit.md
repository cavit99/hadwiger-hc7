# Independent internal audit of the root-preserving transversal descent

**Verdict:** GREEN for the promoted source revision with SHA-256
`9909747c5612ad45d5c75e7a4bb66c51afe883e63530d8fcc1748760edaab161`.

The mathematical text is identical to the independently audited revision
`8a0d87d6c6df83f75682c133722a0ea18bd358e7f8a24a5545bf043868c2cbf2`;
the promoted revision changes only the status line to link this audit.

This audit checks the whole source file
[`hc7_order8_root_preserving_transversal_descent.md`](hc7_order8_root_preserving_transversal_descent.md),
including Theorems 2.1 and 3.1 and the trust-boundary statements in
Section 4.  It is an independent internal mathematical audit, not external
peer review.  No claim about `HC_7` beyond the written conditional
reductions is certified.

## 1. Setting and support definitions

The separation is literal:

```text
V(G) = L dot-union S dot-union R,   E(L,R) = empty,
```

with both open shores nonempty.  Hence every component selected inside
`R` has no neighbour in `L`, and the nonempty set `L` witnesses a genuine
opposite side whenever its full neighbourhood is deleted.

The support definitions have exactly the strength used in the proofs.
A root connector is a nonempty connected subgraph of `G[R]` with a
neighbour at each of `d,e`.  If a component `C` of `G[R-Z]` had both root
contacts, then `G[C]` itself would be a root connector disjoint from `Z`.

For `B` equal to `X` or `Y`, a boundary-block carrier is a vertex set
`F subseteq R` for which `G[B union F]` is connected and nontrivial.  It is
not assumed that `G[F]` is connected.  In the only converse application in
these proofs, `F=C` and `G[C]` is connected.  If `C` contacts every literal
vertex of `B`, then `G[B union C]` is connected and contains a boundary-to-
`C` edge, so `C` is indeed a carrier.  Thus meeting every carrier forces a
component disjoint from `Z` to miss at least one literal vertex of the
corresponding boundary block.  No stronger, unproved conversion from an
arbitrary support set to a connected subgraph is used.

Connectedness of `G[R]` and literal adjacency of `R` to every vertex of
`S` ensure that all three support families are nonempty, as stated.  The
counting arguments themselves need only the written transversal
hypotheses.

## 2. Excluding `R=Z`

Both theorems exclude `R=Z` before choosing a component of `G[R-Z]`.
If `R=Z`, then `|R|<=3` in Theorem 2.1 and `|R|<=2` in Theorem 3.1.
The independent boundary blocks

```text
X,  Y,  {d,e}
```

may be assigned three distinct colours.  Every graph on at most three
vertices is three-colourable, so `G[R]` may be coloured with the other
three colours.  The two palettes are disjoint; consequently all
boundary-to-`R` edges are proper.  This gives exactly the forbidden merged-
root partition on the closed `R`-shore.  The argument is valid even when
`G[R]` is a triangle and does not assume that `R` is independent.

Hence `R-Z` is nonempty in both theorems.

## 3. The three-family transversal (Theorem 2.1)

Let `C` be a component of `G[R-Z]`.  The three transversal conditions give
the sharp contact bounds

```text
|N(C) intersect {d,e}| <= 1,
|N(C) intersect X|     <= 2,
|N(C) intersect Y|     <= 2.
```

All neighbours of `C` in `R-C` lie in `Z`, while there are no `C-L` edges.
Therefore

```text
N(C) subseteq Z union S,   |N(C)| <= |Z|+5 <= 8.
```

This is a full-neighbourhood statement, not merely a quotient contact
count.

The set `N(C)` is a genuine vertex separator: `C` is nonempty and `L` is a
nonempty subset of `V(G)-(C union N(C))`.  Seven-connectivity therefore
gives `|N(C)|>=7`.  If equality occurs, the theorem correctly records only
the existence of an actual order-seven separation.

If no actual order-seven separation exists, integrality and the upper bound
force `|N(C)|=8`.  Equality in the sum forces all constituent inequalities
to be equalities:

- `|Z|=3` and every vertex of `Z` has a neighbour in `C`;
- `C` contacts exactly one of `d,e`;
- `C` contacts exactly two vertices of `X`; and
- `C` contacts exactly two vertices of `Y`.

The three boundary groups are disjoint, so the missed vertices
`r_C,x_C,y_C` are unique and the exact identity

```text
N(C) = Z dot-union (S-{r_C,x_C,y_C})
```

follows.  The source does not infer this identity in the order-seven
branch.

## 4. The root-preserving two-family transversal (Theorem 3.1)

Here only the `X`- and `Y`-carrier families are transversed.  Thus a
component `C` of `G[R-Z]` misses a vertex of each of `X,Y`, while both root
contacts remain possible.  This gives

```text
|N(C) intersect S| <= 2+2+2 = 6,
|N(C)|             <= |Z|+6 <= 8.
```

As above, `N(C)` is an actual separator because `L` is a nonempty opposite
side.  Seven-connectivity supplies the lower bound seven, and an order-
seven value is exactly outcome 1.

In the absence of an actual order-seven separation, equality eight forces

- `|Z|=2` and both vertices of `Z` to contact `C`;
- both root contacts; and
- exactly two contacts in each of `X,Y`.

Consequently the omitted vertices `x_C,y_C` are unique and

```text
N(C) = Z dot-union (S-{x_C,y_C}).
```

Both literal roots survive in this boundary.  This is the exact sense in
which Theorem 3.1 is root-preserving.

## 5. Fullness of complementary components

The fullness assertion in each theorem is correctly conditional on the
order-eight branch, hence on the global absence of an actual order-seven
separation.  Put `T=N(C)`, so `|T|=8`, and let `K` be any component of
`G-T`.  If `K` missed `t in T`, then

```text
N(K) subseteq T-{t},
```

so `|N(K)|<=7`.  This is again a genuine separator: `K` is nonempty, while
the missed vertex `t` lies outside `K union N(K)`.  Order at most six
contradicts seven-connectivity; order seven contradicts the assumed absence
of an actual order-seven separation.  Hence every component of `G-T` is
adjacent to every literal vertex of `T`.

The proof does not make this conclusion in the first outcome, where an
order-seven separation has already been found.

## 6. Restricted boundary-colouring data

The selected colouring `c` is defined on the full closed `R`-shore, and
each new closed component shore `C union N(C)` is contained in it.  Its
restriction is therefore proper without any recolouring or inferred label
alignment.

For Theorem 2.1, the retained old-boundary vertices inherit exactly the
following certified facts:

- `X-{x_C}` is monochromatic;
- `Y-{y_C}` is monochromatic in a distinct colour; and
- the retained root has a third colour.

For Theorem 3.1, the retained old-boundary sets

```text
X-{x_C},  Y-{y_C},  {d},  {e}
```

inherit four pairwise distinct colours.  In both theorems, vertices of `Z`
retain their actual colours and may enlarge an inherited equality block or
create additional blocks when properness permits.  Thus the source does
not overclaim a complete exact equality partition on the new boundary and
does not identify palette colours with new labels.

## 7. Strictness, recursion, and exact trust boundary

In the no-order-seven branch, equality forces `|Z|=3` or `|Z|=2`,
respectively.  Every selected component `C` is disjoint from this nonempty
set, so `C` is a proper subset of the old open shore `R`.  This verifies the
limited host-level strictness stated in Section 4.

The source expressly does **not** claim that this smaller component is a
recursive opposite-response instance.  It preserves only the selected
one-sided colouring response.  It neither proves that the opposite closed
shore realizes the same complete boundary partition nor transfers any old
minor-model labels.  It also does not prove that either required
transversal exists.  The cited split-shore barrier indeed has
`tau_XY=3`, so the written warning against a static two-vertex-transversal
principle is accurate.

Within these hypotheses and this trust boundary, every support,
connectivity, equality, separator, fullness, colouring, and strictness step
is valid.  No mathematical gap or overstatement was found.
