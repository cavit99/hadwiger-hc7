# Cross-lobe curvature exchange

**Status:** proved and independently audited.  The proof is elementary once
the audited common-face theorem has supplied one literal facial cycle and a
six-label portal matching.

## 1. A six-label circle bound

Let `F` be a cycle and let

\[
                         P_0,P_1,\ldots,P_5\subseteq V(F)
\]

be six nonempty portal sets.  Indices in this section are modulo six.  The
three binary duties are

\[
                         \{P_i,P_{i+3}\},\qquad i=0,1,2.
\tag{1.1}
\]

Assume there are pairwise distinct representatives `x_i in P_i` which
occur on `F` in the cyclic order

\[
                         x_0,x_1,\ldots,x_5.             \tag{1.2}
\]

Assume also that no two distinct duties have vertex-disjoint paths on `F`:
for `i!=j` in `{0,1,2}`, there do not exist disjoint subpaths `R_i,R_j` of
`F` such that

\[
 R_i\cap P_i\ne\varnothing\ne R_i\cap P_{i+3},\qquad
 R_j\cap P_j\ne\varnothing\ne R_j\cap P_{j+3}.          \tag{1.3}
\]

For a vertex `v` put

\[
                         \lambda(v)=|\{i:v\in P_i\}|.
\]

### Theorem 1.1 (facial portal-incidence bound)

Under (1.1)--(1.3),

\[
                         \sum_{v\in V(F)}\lambda(v)
                              \le |F|+6.                 \tag{1.4}
\]

### Proof

For each `i`, let `I_i` be the closed `x_{i-1}-x_{i+1}` subpath of `F`
which contains `x_i` and no other selected representative.

We first claim

\[
                              P_i\subseteq I_i.          \tag{1.5}
\]

Before proving the claim, observe that

\[
                              P_i\cap P_{i+3}=\varnothing. \tag{1.6}
\]

Indeed, a common portal `v` would be a one-vertex carrier for duty `i`.
At most one of the other two selected duty pairs uses `v` as one of its
representatives, so choose the remaining selected duty pair.  Its two
representatives are joined by the path between them in `F-v`, disjoint
from `v`.  This contradicts (1.3).

Take `v in P_i`.  Compare duty `i` with the duty represented by
`P_{i+1},P_{i+4}`.  Unless `v` is one of `x_{i+1},x_{i+4}`, the four
vertices

\[
                       v,x_{i+3},x_{i+1},x_{i+4}
\]

are distinct.  If they do not alternate on the cycle, the two disjoint
complementary arcs give the two paths forbidden by (1.3).  Consequently
`v` lies on the closed `x_{i+4}-x_{i+1}` arc containing `x_i`.  This
conclusion also holds when `v` is one of the two displayed endpoints.

Comparing duty `i` with the remaining duty similarly puts `v` on the
closed `x_{i+5}-x_{i+2}` arc containing `x_i`.  The intersection of these
two arcs is exactly `I_i`, proving (1.5).  The four vertices used above are
indeed distinct: (1.6) excludes `v=x_{i+3}`, while the two endpoint
coincidences were handled separately.

It follows from (1.5) that a vertex in the open `x_i-x_{i+1}` segment of
`F` belongs only to `P_i` and `P_{i+1}`.  At a selected vertex `x_i`, the
only possible portal sets are

\[
                         P_{i-1},P_i,P_{i+1},            \tag{1.7}
\]

and `x_i` belongs to `P_i` by construction.

We next claim that for each `i`,

\[
                         |P_i\cap P_{i+1}|\le1.          \tag{1.8}
\]

By (1.5), this intersection lies on the closed `x_i-x_{i+1}` segment
containing no other selected representative.  If it contained distinct
vertices `u,v`, orient this segment so that `u` occurs before `v`.  On the
whole cycle the four vertices occur in the order

\[
                         u,v,x_{i+3},x_{i+4}.            \tag{1.9}
\]

The forward arc from `v` to `x_{i+3}` funds duty `i`, while the
complementary arc from `x_{i+4}` to `u` funds duty `i+1`.  They are
vertex-disjoint, contradicting (1.3).  This proves (1.8).

Let `W={v:lambda(v)>0}`.  Every unit above the first incidence at a vertex
can now be charged to a distinct adjacent pair `(P_i,P_{i+1})` containing
that vertex.  Indeed, an unselected vertex has at most the two labels
corresponding to its unique open segment.  At `x_i`, the mandatory middle
label `P_i` is present and each possible extra label in (1.7) is charged
to `(P_{i-1},P_i)` or `(P_i,P_{i+1})`.  By (1.8), each of the six adjacent
pairs receives at most one charge.  Therefore

\[
 \sum_{v\in V(F)}\lambda(v)
   =|W|+\sum_{v\in W}(\lambda(v)-1)
   \le |F|+6,
\]

which is (1.4).  \(\square\)

## 2. Planar curvature contradicts the circle bound

Let `G` be a graph of minimum degree at least seven.  Let

\[
        S=\{c,s_0,s_1,\ldots,s_5\}
\]

and let `C` be a component of `G-S`.  Suppose `C` is a three-connected
plane graph with a facial cycle `F` such that

\[
                         N_C(s_i)\subseteq V(F)
                         \quad(0\le i<6).                \tag{2.1}
\]

Put `P_i=N_C(s_i)`.  Suppose the six portal sets satisfy the hypotheses of
Theorem 1.1.

### Theorem 2.1 (curvature exchange)

No such configuration exists.

### Proof

Write `n=|F|` and `I=V(C)-V(F)`.  Because `C` is a component of `G-S`,
an interior vertex has no neighbour outside `C` except possibly `c`:
condition (2.1) excludes all six other boundary labels.  Hence

\[
                         d_C(v)\ge6\qquad(v\in I).       \tag{2.2}
\]

For `v in V(F)`, let `lambda(v)` count its neighbours among
`s_0,...,s_5`.  The possible edge `vc` contributes at most one further
boundary neighbour.  Minimum degree seven gives

\[
                         \lambda(v)\ge6-d_C(v).          \tag{2.3}
\]

Take `F` as the outer face of the plane embedding.  Euler's formula
supplies the required curvature inequality.  If `f` is the number of
remaining (bounded) faces of `C`, then

\[
 |V(C)|-|E(C)|+f=1,
 \qquad 3f\le2|E(C)|-n.
\]

Equivalently,

\[
 \sum_{v\in I}(6-d_C(v))
   +\sum_{v\in V(F)}(4-d_C(v))\ge6.                    \tag{2.4}
\]

Every term in the first sum is nonpositive by (2.2), so

\[
                         \sum_{v\in V(F)}(4-d_C(v))\ge6.
\tag{2.5}
\]

Summing (2.3) and using (2.5) now gives

\[
 \sum_{v\in V(F)}\lambda(v)
   \ge \sum_{v\in V(F)}(6-d_C(v))
   =2n+\sum_{v\in V(F)}(4-d_C(v))
   \ge2n+6.                                             \tag{2.6}
\]

Theorem 1.1 gives the incompatible upper bound `n+6`.  Since a facial
cycle is nonempty, (2.6) is a contradiction.  \(\square\)

The mechanism is state-free after the three duties are named.  It spends
only a six-label SDR, failure of two disjoint duty paths, the common-face
conclusion, and the host minimum degree.  It is not a palette-to-label
lift.

## 3. Exact-seven cross-lobe closure

Use the notation and hypotheses of
`../results/hc7_exact7_cross_lobe_common_face.md`.  Thus

\[
 S=\{c,a_1,t_1,a_2,t_2,a_3,t_3\},\qquad
 \Pi=\bigl\{\{a_i,t_i\}:i\in[3]\bigr\}\cup\{\{c\}\},
\tag{3.1}
\]

`C` is the three-connected cross-lobe component, and a second disjoint
`S`-full packet `Q` funds the third duty.

### Corollary 3.1 (the cross-lobe family reflects)

The attained state `Pi` reflects across the rich shore.  Consequently the
cross-lobe one-sibling family cannot occur in a hypothetical minimal
counterexample to `HC_7`.

### Proof

Suppose `Pi` does not reflect.  Then no two distinct duties have disjoint
connected carriers in `C`: together with `Q`, such carriers would reproduce
the exact state.  The audited common-face theorem makes `C` planar and puts
every neighbour in `C` of the six non-`c` boundary labels on one facial
cycle `F`.

The audited order-five exclusion and Hall lemma give six pairwise distinct
literal portal representatives, one for each of those labels.  Their duty
word on `F` is `A B D A B D`.  Relabel the six literal portal sets in that
cyclic order as `P_0,...,P_5`; opposite indices are the three original
duties.  No two cycle paths can fund two distinct duties, because they
would be disjoint carriers in `C`.

The minimal-counterexample kernel has minimum degree at least seven, so all
hypotheses of Theorem 2.1 hold.  Its contradiction proves that `Pi` must
reflect.  The audited exact-state gluing argument then six-colours `G`.
\(\square\)

## 4. Exact scope

This closes the entire cross-lobe support family, including arbitrary
portal multiplicities and both rooted-expansion and parallel-strip
outcomes.  It does not close the second one-sibling family

```text
N_S(J)={c,a1,t2,t3}
```

from the Hall-and-duty funnel, nor the general `(1,2)` adhesion.  The proof
also depends essentially on all three duty-pair failures; a decorated wheel
which blocks only the two outer duties is not a counterexample.
