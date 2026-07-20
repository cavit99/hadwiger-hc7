# Audit of the near-full path-piece completion theorem

**Verdict:** **GREEN** for the exact source revision identified below.

**Audited source:**
[`hc7_distance_one_reversal_triangle_collision.md`](hc7_distance_one_reversal_triangle_collision.md)

**SHA-256:**
`b8896ebe1d25cedee9cc8f5bb56e477d2c5b4e344bbddbe60219a55c436f6bdd`

The final revision changes only the source status line to link this audit;
the audited mathematics is unchanged.

This is a separate internal proof audit, not external peer review.  The
source now states explicitly the response-exclusion hypothesis needed by
both path corollaries.

## 1. Theorem 1.1

The inherited declaration of distinct boundary vertices makes

\[
 A=\{x_e,y_e,x_0,y_0\}
\]

a four-set disjoint from the triangle `{d,x_d,y_d}`.  Since each defect
set `D_i` has order at most one, choose
`r_0 in A-D_0` and then
`r_1 in A-(D_1 union {r_0})`.  At least two choices remain at the second
step, so `r_0,r_1,q_0,q_1` are genuinely four distinct anchors.

The two `E` branch sets are connected because `r_i notin D_i` means that
`r_i` has a neighbour in `E_i`.  The two `Q` branch sets are connected
because both `Q` parts meet every vertex of `A subseteq S-{e}`.  The
path-side pair and `Q`-side pair are adjacent by hypothesis, and each of
the four cross pairs is adjacent through `r_0` or `r_1`, since every
`Q_j` has a neighbour at both anchors.

The defect sets avoid the distinguished triangle, so both `E` branch sets
meet all three triangle vertices.  Both `Q` branch sets also meet all
three.  Together with the three edges of the triangle, this verifies all
`6+12+3=21` adjacencies in the displayed `K_7`-minor model.  Disjointness
follows from the partition into `E,B,C` and the distinct anchors.

## 2. Strict reversal

Section 2 now explicitly assumes that the order-seven/order-eight response
from Lemma 2.1 of the shore-spanning path normal form has not occurred.
Thus every proper prefix and suffix meets at least eight of the nine
boundary vertices.

When `F_*>L_*`, a cut with `L_*<=i<F_*` has a prefix missing `a` and a
suffix missing `b`.  The near-full property makes these the exact defect
sets.  They are distinct by the prior normal-form argument.  If both avoid
the triangle, Theorem 1.1 applies, proving Corollary 2.1.

## 3. Shared portal

When `F_*=L_*=k` and `k>1`, the cut before `p_k` has nonempty adjacent
parts.  Its prefix misses `a` and, by the now-explicit near-full
hypothesis, no other boundary vertex.  Its suffix is full because every
boundary vertex satisfies `ell(s)>=k`.  Theorem 1.1 therefore forces
`a` into the triangle in a `K_7`-minor-free graph.

Symmetrically, when `k<r`, the cut after `p_k` has a full prefix because
every `f(s)<=k`, while its suffix has exact defect `{b}`.  Theorem 1.1
forces `b` into the triangle.  The endpoint qualifications are exact:
one of these cuts is empty when `k=1` or `k=r`, and both are unavailable
only in the atomic case `r=1`.

## 4. Trust boundary

The result closes only near-full two-piece configurations whose possible
defects avoid the distinguished triangle.  It does not eliminate a
triangle-owned defect, return a compatible separator colouring, or address
a non-spanning distance-one path.  No stronger conclusion is asserted.
