# Independent audit: endpoint allocation at the balanced order-eight boundary

**Verdict:** GREEN for the exact source revision audited below.

**Source:** [`hc7_balanced_endpoint_allocation.md`](hc7_balanced_endpoint_allocation.md)

**Audited SHA-256:**
`e3241a86c22f380eae6207b585bbe8fac4fb355da5e9b6c493aa5995205d5fd3`

The independently audited mathematical revision had SHA-256
`85a575e9103b0f8d1440d64d8ae2322cf089cafe958225cbcf7e4f4649e920c8`.
The promoted revision differs only in its opening status paragraph, which
now records this GREEN audit; no theorem statement or proof step changed.

This is an internal mathematical audit, not external peer review.  The
audit verifies the endpoint-allocation construction, the finite
row-cover classification, the forced-theta corollary, and the stated
minimum-degree consequence.  It does not audit the upstream reductions
which produce the balanced order-eight configuration.

## 1. The explicit minor model

The seven branch sets in (2.3) are pairwise disjoint.  The set `K` is
connected because every added boundary vertex lies in `Z` and therefore
has a neighbour in the connected graph `H`; `x` also has an `H`-neighbour.
The two leaf-and-endpoint sets are connected by the definitions of
`A_L,B_L`, and `D` is connected.

All twenty-one adjacencies check as follows.

1. The three `R`-singletons give three pairs.
2. Each `R`-singleton meets each leaf set through the corresponding
   clique vertex, giving six pairs.
3. Each `R`-singleton meets `D` by boundary fullness, giving three pairs.
4. Each `R`-singleton meets `K`: through `H` outside `U_H`, through `x`
   in `U_H-M`, and through (2.1) in `M`.  This gives three pairs.
5. The two leaf sets meet along `ell_A ell_B`.
6. Each leaf set meets `K` through its leaf's edge to `H`, giving two
   pairs.
7. Each leaf set meets `D` through its selected boundary endpoint, giving
   two pairs.
8. `K` meets `D` through an `x`--`D` edge.

The total is `3+6+3+3+1+2+2+1=21`.  No adjacency is inferred from an
edge between `C` and `D`, and unused boundary vertices need not belong to
any branch set.  Theorem 2.1 is correct.

## 2. The row-cover theorem

The boundary neighbours of `H` are exactly

\[
          (R-U_H)\mathbin{\dot\cup}Z\mathbin{\dot\cup}\{x\}.
\]

Hence the assumed six boundary contacts give
`|Z|>=2+|U_H|>=2+|M|`.  For a fixed `r in R`, endpoint rigidity permits
at most one nonneighbour in each of `A,B`.  Since `M` is nonempty, the
preceding bound gives `|Z|>=3`; at least one member of `Z` therefore sees
`r`.  Thus every `T_r` is nonempty.

For a fixed anchor pair `(a,b)`, failure of (2.1) is equivalent to

\[
                    T_r\subseteq\{a,b\}

for at least one `r in M`.  Since a successful pair would give the minor
already audited above, this proves the equality (3.3), not merely one
inclusion.

If both anchor sets had order two, one nonempty row can cover at most two
of the four anchor pairs when `|M|=1`.  When `|M|=2`, the contact bound
forces `Z=A union B`; each row then contains an endpoint from each defect
edge and covers at most one pair.  Two rows cannot cover four pairs.

For assertion 4, with one missed row every member of its nonempty `T_r`
must occur in every anchor pair, so it is the unique member of its anchor
set.  With two rows, `Z=A union B` and every row contains both an `A` and
a `B` endpoint.  If one anchor set is a singleton and the other has order
two, the two product pairs must be covered by different rows, each row
being exactly the corresponding two-element pair.  The two-singleton
case is immediate from a row which covers the sole product pair.  In all
cases the selected endpoint belongs to `Z`, so it has an `H`-neighbour.

As an independent finite sanity check, I enumerated all abstract choices
of nonempty anchor sets, endpoint-contact set `Z`, and one or two row
traces satisfying the inequalities and collective-adjacency constraints.
All 124 row-cover configurations satisfied assertions 3 and 4.  This
enumeration is only a check of the written finite argument; the theorem
does not depend on a computer search.

## 3. Forced-theta specialization

When `p in M`, the row `T_p` is all four endpoints and covers no anchor
pair.  The other row contains exactly one endpoint of each defect edge
and covers at most one pair.  Thus the anchor product has order one.

When `M={r,q}`, the two traces are complementary pairs with no common
coordinate.  A two-element Cartesian product of nonempty subsets of
`A,B` has a fixed coordinate, while a four-element product contains all
four pairs.  Neither can be contained in the two complementary traces.
The product again has order one.  Since `|Z|>=4`, all four endpoints meet
`H`.  Corollary 4.1 is correct with the stated literal theta labels.

## 4. Degree calculation

The separator has eight vertices and both open components are nonempty,
so `|G|>=10`.  Seven-connectivity gives minimum degree at least seven.
If a vertex had degree seven, its open neighbourhood would isolate it
from a vertex outside its eight-vertex closed neighbourhood, producing
the excluded actual order-seven separation.  Therefore `delta(G)>=8` in
this branch.

The required nonadjacencies `x ell_A,x ell_B notin E(G)` are supplied by
Lemma 3.2 of the already audited planar-boundary critical-core note (the
source draft calls this the “tight-core argument,” but the precise input
is the preceding split-edge lemma in that file).  Under Corollary 4.1,
`ell_B` has exactly five neighbours outside `H`: `ell_A`, the three
vertices of `R`, and its unique neighbour in `A`.  It has no neighbour in
`B`, at `x`, or in `D`.  Hence

\[
                  d_H(\ell_B)=d_G(\ell_B)-5\ge3,
\]

and symmetrically for `ell_A`.  Corollary 4.2 is correct.

## 5. Trust boundary

The GREEN verdict assumes the following previously established inputs
exactly as invoked by the source:

- the connected leaf-side graph `H` has at least six literal boundary
  contacts and contains an `x`-neighbour;
- some vertex of `R` is missed by both `H` and `x`;
- the two endpoint nonneighbour sets on either defect edge are nonempty
  and disjoint;
- the forced-theta boundary has the literal endpoint orientation stated
  in Section 4; and
- neither clique leaf is adjacent to `x` after the earlier minor and
  order-seven exits are excluded.

The audit does not claim that endpoint allocation produces either of the
two crossed path systems in Section 5.  Indeed, the current canonical-web
description permits those alternating pairings to remain obstructed.  The
source correctly leaves that label-preserving linkage or colouring
transition open and does not claim `HC_7`.
