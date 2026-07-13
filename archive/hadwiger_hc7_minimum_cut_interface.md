# The complete minimum-cut interface of a hypothetical `HC_7` counterexample

## 1. Setting

Let `G` satisfy

\[
 \chi(G)=7,\qquad \chi(H)\le6\text{ for every proper minor }H<G,
 \qquad \eta(G)\le6.                                      \tag{1.1}
\]

Let `S` be a minimum vertex cut, put `c=|S|`, and let `m` be the number
of components of `G-S`.  Write `p=chi(G[S])`.

## Theorem 2 (bounded minimum-cut interface)

One has

\[
 c\in\{7,8,9\},\qquad m\in\{2,3\}.                         \tag{2.1}
\]

Every component of `G-S` is connected and full to `S`.  Moreover:

1. if `m=2`, then `2<=p<=5`, and for every `z in S`,
   \[
       \eta(G[S-z])\le4,\qquad \chi(G[S-z])\le4;            \tag{2.2}
   \]
2. if `m=3`, then `3<=p<=4`, and for every two-set `Z subseteq S`,
   \[
       \eta(G[S-Z])\le3,\qquad \chi(G[S-Z])\le3.            \tag{2.3}
   \]

In the first case, `p=5` makes `G[S]` 5-vertex-critical.  In the second
case the formally possible value `p=5` is excluded without any boundary
enumeration.

### Proof

Corollary 3 of `hadwiger_hc7_minimum_eight_cut_four_shores.md` gives
(2.1).  Fullness follows because the neighbourhood of any component of
`G-S` is a cut contained in the minimum cut `S`.

The uniform minimum-cut inequalities give

\[
                         m\le p\le c-m.                       \tag{2.4}
\]

The full-shore reserve obstruction says that, for every reserve set
`Z subseteq S` of order `m-1`,

\[
                         \eta(G[S-Z])\le 6-m.                 \tag{2.5}
\]

For `m=2`, known `HC_5` turns (2.5) into
`chi(G[S-z])<=4`.  Adding back `z` gives `p<=5`, proving (2.2) and the
stated range.  If `p=5`, every vertex deletion has chromatic number
exactly four: it is at most four by (2.2), and at least four because
adding one vertex raises chromatic number by at most one.  Thus `G[S]`
is 5-vertex-critical.

For `m=3`, known `HC_4` turns (2.5) into (2.3), and adding back the two
reserved vertices initially gives only `p<=5`.  Suppose `p=5`.  If two
boundary vertices `x,y` were nonadjacent, take a 3-colouring of
`G[S-\{x,y\}]`, supplied by (2.3), and give both `x,y` one new colour.
This would be a 4-colouring of `G[S]`, a contradiction.  Hence `G[S]`
is complete.  A complete graph with chromatic number five has exactly
five vertices, contrary to `|S|=c>=7`.  Therefore `p<=4`; together with
(2.4), this gives the second range.  \(\square\)

## 3. Exact trace data retained on every side

If `D` is any component of `G-S`, then every collection of at most
`m-1` pairwise disjoint nonempty independent subsets of `S` occurs as
distinct exact boundary colour classes in a six-colouring of
`G[S\cup D]`.  This is the multi-block exact-trace theorem, using the
other full components as contraction reserves.

Thus the remaining `HC_7` minimum-cut problem is finite in boundary
order but not merely a finite graph enumeration:

* a bilateral gate of order 7--9 with boundary chromatic number at most
  five; or
* a three-shore gate of order 7--9 with boundary chromatic number at most
  four, robustly 3-colourable after every two-vertex deletion.

Any closure must use the exact trace families together with `K_7`-minor
exclusion.  Abstract extension states alone are insufficient by the
complementary-state realization barrier.
