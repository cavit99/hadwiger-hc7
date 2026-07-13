# Independent audit: uniform inequalities at a full minimum cut

## Verdict

**GREEN AS PATCHED.**  The inequalities, exact trace construction,
reserve lift, model-support reformulation, and equality cases are correct.
No off-by-one error in `k`, the `(k-1)`-colour palette, or the
`K_{k-m}` reserve core was found.

Three exposition patches were made in the source:

1. connectedness of the strong minor-minimal graph is now stated before
   the full-component argument;
2. `p<=k-1` is recorded explicitly, which also guarantees `k-m>=1` in
   the induction paragraph; and
3. the proof of `p>=m` now invokes the already proved exact-trace theorem
   directly instead of referring elliptically to block gluing.

## 1. Definitions and full components

The parameter convention is consistent:

```text
chi(G)=k,
every proper minor is (k-1)-colourable,
p=chi(G[S]),
c=|S|=kappa(G).
```

Strong minor-minimality makes `G` connected.  For a component `D_i` of
`G-S`, its external neighbourhood is contained in `S`.  Since another
component remains outside `D_i union N(D_i)`, the set `N(D_i)` is an
actual vertex cut.  Minimality of `|S|` gives

```text
|N(D_i)|>=c,
```

while containment in `S` gives the reverse inequality.  Hence
`N(D_i)=S`; “full” is literal collective adjacency to every vertex of
`S`, not vertexwise completeness from every vertex of the component.

Deleting all components of `G-S` gives the proper minor `G[S]`, so
`p<=k-1`.  This omitted observation was patched into Section 1.

## 2. Exact partial traces

For a fixed closed side `S union D_i` and `ell<=m-1`, there are enough
distinct opposite components to assign one to every prescribed
independent block `A_j`.  Each set

```text
D_{h_j} union A_j
```

is connected because `D_{h_j}` is connected and collectively adjacent
to every vertex of `A_j`.  Distinct contracted sets are adjacent: a
vertex in one nonempty `A_j` has an edge to the other full component.
Every uncontracted boundary vertex is adjacent to every contracted set.
Thus their images are a clique and their colours are absent from the
rest of the boundary.

Partially expanding the colouring is safe.  Each `A_j` is independent;
an edge from `A_j` to `D_i` was represented by an edge from the contracted
vertex to `D_i`; and every outside boundary vertex was forced away from
the contracted colour.  Therefore the resulting colouring of
`G[S union D_i]` has each `A_j` as an exact boundary colour class.

The minor used is proper even at both endpoints:

* for `ell=0`, at least one opposite component is deleted;
* for `ell=m-1`, every opposite component is contracted together with a
  nonempty boundary set.

A common equality partition in all `E_i` can be aligned by extending the
boundary colour bijection to a permutation of the full `(k-1)`-palette.
The components of `G-S` are anticomplete, so the aligned side colourings
glue.  Hence the empty-intersection claim is correct.

## 3. The inequality `m<=p<=c-m`

If `p<=m-1`, apply Theorem 2.1 to all `p` classes of an optimal boundary
colouring.  The resulting equality partition lies in every `E_i`, a
contradiction.  Thus `p>=m`.

Let `a` be the number of nonsingleton classes in an optimal `p`-colouring
of `S`.  The singleton vertices form a clique: two nonadjacent singleton
classes could be merged.  If `a<=m-1`, select all nonsingleton classes
and enough singleton classes to obtain exactly `m-1` prescribed blocks.
Theorem 2.1 makes those blocks exact on every side.  Every remaining
boundary vertex is adjacent to all contracted block vertices by fullness,
and the remaining vertices form a clique.  Hence they receive pairwise
distinct new colours, giving exactly the original `p`-block equality
partition on every side.  This contradicts the empty intersection.

Therefore `a>=m`, and

```text
c >= 2a+(p-a)=p+a >= p+m.
```

This proves `p<=c-m`; combined with the lower bound it gives `c>=2m`.
No assumption that a full component is complete to the boundary was used.

## 4. Equality layers

For `c=2m`, the interval for `p` collapses to `p=m`.  Since at least `m`
classes are nonsingleton, all classes have order exactly two.

For `c=2m+1`:

* if `p=m`, all `m` classes are nonsingleton and the one surplus vertex
  produces sizes `3,2,...,2`;
* if `p=m+1`, exactly `m` classes are nonsingleton (having all
  `m+1` nonsingleton would require at least `2m+2` vertices), so their
  sizes are all two and the last class is a singleton.

These conclusions hold for every optimal colouring, exactly as stated.

## 5. Reserve lift and induction indices

Choose `m-1` distinct reserves `Z subseteq S`.  If `S-Z` contained a
`K_{k-m}` model, use one full component as a bare shore and attach each
reserve vertex to one of the other `m-1` full components.  These `m`
shore-derived bags are pairwise adjacent and adjacent to every core bag;
together with the `k-m` core bags they form `K_k`.  Therefore

```text
eta(G[S-Z]) <= k-m-1.
```

The index is correct: the reserve core has `k-m` bags and the shore part
has `m` bags.  Since `m<=p<=k-1`, the parameter `k-m` is positive.

The support reformulation is exactly equivalent.  A `K_{k-m}` model with
support `U` avoids some `(m-1)`-set precisely when

```text
c-|U| >= m-1,
```

or `|U|<=c-m+1`.  Thus every such model must use at least `c-m+2`
boundary vertices, and the converse follows because `S-Z` itself has
only `c-m+1` vertices.

At the least failing parameter, `HC_{k-m}` turns absence of a
`K_{k-m}` minor into

```text
chi(G[S-Z])<=k-m-1.
```

Adding the `m-1` reserve vertices individually gives `p<=k-2`.  If
`p=k-2`, the standard reverse inequality

```text
chi(G[S-Z]) >= p-|Z|
```

matches the upper bound, so equality holds for every reserve set.  No
unsupported clique conclusion is drawn from this chromatic equality.

## 6. Exact scope

The theorem is a valid uniform parameter restriction, not a closure of
the full-cut state obstruction.  It proves saturation for at most `m-1`
prescribed independent blocks and proves that every optimal boundary
partition has at least `m` nonsingleton blocks.  Synchronizing the
completion states of those `m` blocks remains genuinely additional; the
source does not hide that missing step.

