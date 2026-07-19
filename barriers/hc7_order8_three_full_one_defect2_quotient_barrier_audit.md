# Audit of the three-full-plus-defect-two quotient barrier

**Source SHA-256:**
`6b8ab1c914e59db6336facba13aa52853544321c8c3a53b542ff79eaaa145467`

**Verdict:** GREEN.  The graph in
[`hc7_order8_three_full_one_defect2_quotient_barrier.md`](hc7_order8_three_full_one_defect2_quotient_barrier.md)
is a valid counterexample to the stated intermediate claim, and its
treewidth proof is self-contained.

## 1. Contact hypotheses

The four outside singleton subgraphs are pairwise disjoint and disjoint
from `S`.  Each of `x_1,x_2,x_3` meets all eight boundary vertices, while
`p` meets exactly `S-\{a,b\}`.  Thus every hypothesis of the refuted claim
holds.

## 2. Boundary conditions

The graph

\[
                         H=2K_3\mathbin{\dot\cup}2K_1
\]

is exactly three-colourable.  No clique meets both triangle components, so
deleting a clique leaves at least one odd triangle.  Hence `H` has no
clique odd-cycle transversal.  Every component of `H` has order at most
three, so `H` is `K_4`-minor-free; consequently `H-Z` is `K_4`-minor-free
for every two-set `Z`.  These are the residual boundary conditions used in
the order-eight three-component classification.

## 3. Tree-decomposition check

For `R=Q[S\cup\{p\}]`, the six displayed bags cover every vertex and every
edge.  The two triangles lie in `A_0,B_0`, and the six edges incident with
`p` lie in `A_1,B_1,R_r,R_s`.

The bags containing `a_1,a_2`, respectively `b_1,b_2`, occur on adjacent
pairs of the displayed path.  The bags containing `p` induce the connected
subtree on `A_1,B_1,R_r,R_s`; every other vertex occurs in one bag.  Thus
the running-intersection property holds.  Maximum bag order is three, so

\[
                              \operatorname{tw}(R)\le2.
\]

Adding `x_1,x_2,x_3` to every bag covers all added edges and preserves
running intersection.  Maximum bag order becomes six, so
`\operatorname{tw}(Q)\le5`.  Treewidth is minor-monotone and
`\operatorname{tw}(K_7)=6`; therefore `Q` has no `K_7` minor.

## 4. Trust boundary

The stated limitations are accurate.  Each of `r,s` has exactly the four
neighbours `p,x_1,x_2,x_3`, so `Q` is not seven-connected.  Width five
implies six-colourability, and therefore `Q` is not
seven-contraction-critical.  The construction supplies neither an
operation-specific proper-minor response nor inherited branch-set labels.

I independently reran the finite probe on `geng -q 8`.  It returned

```text
boundaries=82
cases=3034
failures=62
explicit_triangle_anchor_failures=106
failures_by_defect=0:0 1:0 2:62
```

The graph6 code displayed in the source decodes to
`2K_3\mathbin{\dot\cup}2K_1` and is the unique six-edge boundary among the
exact quotient failures.

## 5. Unresolved assumptions

There are no unresolved assumptions inside the barrier statement.  The
62-case count retains the stated catalogue, decoder, and exact-minor-search
trust boundary and is contextual only; the counterexample proof does not
depend on that computation.
