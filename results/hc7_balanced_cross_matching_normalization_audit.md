# Independent audit: cross-pair perfect-matching normalization

**Verdict:** **GREEN** for the exact draft revision audited.

**Audited file:** `results/hc7_balanced_cross_matching_normalization.md`

**Final source SHA-256:**
`40ef6d44af400455ae322a61971ec7208ec8db615a0be809bfa03411ee9dc430`

**Independently audited mathematical revision SHA-256:**
`479e0ae0bdb99e1bab6e1d46e026dd14465ff97769ae3192d1c60408ffdd965c`

This is a separate internal mathematical audit, not external peer review.
It checks the perfect-matching count, all four switching arguments, the
quotient lift, the seven host branch sets, and the final matching form.  No
mathematical correction is required.

The first final source differed from the independently audited revision
only in its opening status paragraph.  The current source additionally
contains Corollary 2.2 and its summary sentence.  That corollary was checked
in a separate follow-up audit: its negation says exactly that every vertex
of `R` is adjacent to `x` or has a neighbour in `H`, which supplies the only
new adjacencies needed by the same seven branch sets.  The follow-up audit
returned GREEN at the final source hash above.  No earlier theorem statement
or proof step changed.

## 1. Perfect-matching count and switches

The set `R` is independent in `F`, so all three of its vertices are matched
outside `R`.  If `x` is matched to `R`, the other two vertices of `R` use
two of the four endpoints in `A union B`; the remaining two endpoints must
be matched together.  Since `F[A]` and `F[B]` have no edges and every
`A`--`B` edge is present, this is exactly a forbidden cross-pair matching.
Thus the normalization

```text
xa, r1b, r2c, r3d
```

is exhaustive after relabelling.

The nonempty `F`-neighbour set of `a` in `R` is disjoint from that of `b`.
Since `br1` is present, `a` has a neighbour in `{r2,r3}`.  Each displayed
replacement is a genuine perfect matching:

- `xr2, ac, br1, dr3`;
- `xr3, ad, br1, cr2`;
- if `ar2` is present, `xr1, bc, ar2, dr3`; and
- otherwise `ar3` is present and `xr1, bd, ar3, cr2`.

Every replacement contains one `A`--`B` edge.  Hence `x` has no
`F`-neighbour in `R`.

## 2. The quotient lift

Suppose, for example, that `xb` is an edge of `J`.  The three singleton
vertices of `R`, the singleton `{x}`, and the connected edge `A` form a
`K_5`-minor model supported on six vertices.  The endpoint nonneighbour
sets in `R` being disjoint is exactly what makes `A` collectively adjacent
to every vertex of `R`; and `R union {x}` is a clique because `x` has no
`F`-neighbour in `R`.

There is an unused boundary vertex `w`.  If `p,q` are the two nonadjacent
universal vertices of `I_2 vee J`, adjoining `{p,w}` and `{q}` gives seven
disjoint connected branch sets.  Their mutual adjacency uses the join
edges and the edge `wq`; it does not require the absent edge `pq`.  Thus
`xb` cannot be present in `J`.  The identical argument for the connected
edge `B` excludes either `xc` or `xd` in `J`.  Together with the fixed
matching edge `xa`, this proves `N_F(x)=A union B` on the other seven
boundary vertices.

## 3. Host branch sets

The seven proposed branch sets are

```text
{r} for r in R,
V(e) union {ell_f},
V(f) union {ell_e},
V(H) union {x},
V(D).
```

They are pairwise disjoint.  Their connectivity follows from the two
cross-index leaf contacts, connectedness of `H,D`, and the `x`--`H`
contact.

All 21 adjacencies are forced:

1. three pairs inside the clique `R`;
2. twelve pairs from the three `R` singletons to the other four sets,
   using the two clique leaves, completeness of `x` to `R`, and fullness
   of `D`;
3. the pair between the two leaf-and-edge sets through
   `ell_e ell_f`;
4. two pairs from those sets to `H union {x}` through the corresponding
   leaf--`H` contacts;
5. two pairs from those sets to `D` through boundary fullness; and
6. the pair from `H union {x}` to `D` through `x`.

The total is `3+12+1+2+2+1=21`.  Hence failure of a cross-pair perfect
matching really gives an explicit `K_7`-minor model.

## 4. Final matching form and scope

Once a perfect matching contains an `e`--`f` cross pair, the remaining
six vertices are the three vertices of `R`, `x`, and the two unused defect
endpoints.  Since `R` is independent in `F`, its three vertices must be
matched bijectively to the other three vertices.  The cross pair is
therefore the unique matching edge internal to
`V(e) union V(f) union {x}`.

The audited theorem only normalizes the boundary matching.  It does not
show that the resulting four independent pairs extend through either
closed shore, align the two colouring languages, complete the balanced
order-eight branch, or prove `HC_7`.

## 5. Shared missing contact

The negation of Corollary 2.2 is that, for every `r in R`, either `xr` is
an edge or `H` has a neighbour at `r`.  Therefore the connected branch set
`H union {x}` is adjacent to every singleton `{r}`.  The other three
nonsingleton branch sets in (2.1) retain all connectivity and adjacencies
checked in Section 3 above.  The same count of 21 pairs gives a `K_7`
minor.  The contrapositive proves the corollary without using the matching
lemma, and the common missed vertex is literal rather than an abstract
matching class.
