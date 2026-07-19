# Audit of the two-part shore normal form and common-transversal descent

**Verdict:** GREEN.

**Audited source:**
`results/hc7_order8_common_two_vertex_transversal_descent.md`

**Audited SHA-256:**
`d4a827d5c9836d001c2e4b9e9ef814ca671f506ffc9ac3d413e74fcf54baf960`

**Promoted source SHA-256:**
`8b34b36bf7c0da847453b7ba2683b5d470c4ca31bc5c6c6c5ff63c4af35befea`

The promoted revision changes only the status paragraph and adds the link
to this audit.  The theorem statement, proof, dependencies, and trust
boundary are identical to the audited revision.

**Audit type:** independent internal mathematical audit.  This is not
external peer review and does not prove `HC_7`.

## 1. Imported results and response orientation

The connected-rich width-two frontier proves its adjacent connected-cover
lemma under exactly the hypotheses used here: a connected graph containing
two disjoint nonempty connected subgraphs.  Its construction gives a
partition of the whole vertex set into two induced connected parts which
contain the prescribed subgraphs and have an edge between them.  Since the
prescribed subgraphs are each adjacent to every literal boundary vertex,
both enlarged parts retain that property.

The materially strengthened root-connector reflection theorem has a
separate current GREEN audit.  Its audited theorem hash is

```text
dd2b25e2f9e3918661f4fbb4900c82a661cbe72a170941d9f315ce5d7f565a79
```

and its status-only promoted hash is

```text
15f6fe1052426a0ccc0ee96a02d377370acfc00f0826d73c7ba5f1076106ddcc.
```

That theorem assumes exactly the boundary facts recorded in the present
setting: `de` is absent; `X,Y` are nonempty independent blocks with an
edge between them; and each root has a neighbour in each block.  It forces
the split-root response on the opposite closed shore from a root connector
and two disjoint boundary-block carriers.

The response orientation is consistent throughout.  The closed `L`-shore
realizes only the merged-root partition, while the closed `R`-shore
realizes only the split-root partition.  Thus producing the split-root
partition on `L` is a contradiction and ultimately a gluing certificate.

## 2. Adjacent two-part cover and symmetric intersection

Apply the connected-cover lemma to the two initially given disjoint
boundary-full connected subgraphs.  It yields

```text
R = P_0 dot-union P_1
```

with each induced part connected and boundary-full and with an actual
cross-edge.

Fix a root connector `D` contained in `P_i`.  If an `X`-carrier `F_X`
contained in `P_i` were disjoint from `D`, then

```text
V(D),  F_X,  P_{1-i}
```

would be pairwise disjoint open-side sets.  The first is a root connector,
the second is an `X`-carrier by assumption, and boundary fullness plus
connectedness makes `P_{1-i}` a `Y`-carrier.  The audited reflection theorem
would make the closed `L`-shore realize the forbidden split-root response.
Interchanging `X,Y` proves both asserted intersection statements.  No
palette colour is identified with either part or carrier.

## 3. The case `R=Z`

The source correctly excludes this case before selecting a component of
`G[R-Z]`.  If `R=Z` and `|Z|<=2`, the two disjoint nonempty boundary-full
connected subgraphs force `|R|=2` and force each of them to be a distinct
singleton, say `q_0,q_1`.  Connectedness of `G[R]` supplies the edge
`q_0q_1`, and singleton boundary fullness makes each `q_i` adjacent to
every vertex of `S`.

An exact merged-root response uses three distinct colours on `S`, one on
each of `X`, `Y`, and `{d,e}`.  Colour `q_0,q_1` with two distinct colours
among the remaining three.  This is proper because the two vertices are
adjacent to one another and to all of `S`.  It realizes the merged-root
partition on the closed `R`-shore, contradicting the assumed opposite
response.  Hence `G[R-Z]` has a component.

## 4. Component contact count and exact missed labels

Let `C` be a component of `G[R-Z]`.  It cannot meet both root vertices:
otherwise the connected graph `G[C]` is a root connector disjoint from
the purported transversal.  It cannot meet every vertex of `X`, because
then `C` itself is an `X`-carrier disjoint from the transversal.  The same
holds for `Y`.  Since the group sizes are `2,3,3`, respectively,

```text
|N(C) intersect S| <= 1 + 2 + 2 = 5.
```

All neighbours of `C` in `R-C` lie in `Z`, because `C` is a component
after deleting `Z`; there are no `C-L` edges.  Thus `|N(C)|<=|Z|+5<=7`.
The full neighbourhood is a genuine separator: `C` is nonempty and the
nonempty shore `L` remains on the other side.  Seven-connectivity forces
`|N(C)|=7`.

Equality in the two preceding bounds forces all of the following, rather
than merely their inequalities:

1. `|Z|=2`;
2. both vertices of `Z` have a neighbour in `C`;
3. `C` has exactly five boundary neighbours; and
4. it misses exactly one vertex from each of `{d,e}`, `X`, and `Y`.

The three groups are disjoint, so their missed vertices
`r_C,x_C,y_C` are unique and

```text
N(C) = Z dot-union (S - {r_C,x_C,y_C}).
```

This verifies both the exact order and every asserted literal label.

## 5. Fullness of every complementary component

Put `T=N(C)`.  There are at least two components of `G-T`, since `T` is
the full neighbourhood of `C` and the shore `L` is nonempty.  If a
component `K` of `G-T` missed a vertex `t` of `T`, then

```text
N(K) subseteq T - {t},
```

which has order six.  Another component of `G-T` remains after deleting
`N(K)`, so `N(K)` is a genuine separator of order at most six.  This
contradicts seven-connectivity.  Hence every component of `G-T` is adjacent
to every literal vertex of `T`.

## 6. The preserved one-sided response

The selected split-root colouring is a proper colouring of `G[R union S]`.
Restriction to `G[C union T]` therefore remains proper.  The retained
vertices from `S` inherit the three literal, pairwise distinct blocks

```text
X - {x_C},  Y - {y_C},  {d,e} - {r_C}.
```

The two vertices of `Z` are actual vertices of the selected coloured shore,
so their existing colours are retained without any inferred equality or
label.  The theorem correctly claims only this one-sided colouring.  It
does not claim that the other closed shore realizes the same full boundary
partition on the new seven-set.

## 7. Trust boundary

The theorem is conditional on a common transversal of order at most two;
it does not prove that one exists.  The exact order-seven output is not yet
a colour-compatible gluing certificate, because only one closed-shore
response has been preserved.  It also makes no use of `K_7`-minor exclusion
and derives no global conclusion beyond the stated conditional descent.

Within these hypotheses and this trust boundary, no gap was found.
