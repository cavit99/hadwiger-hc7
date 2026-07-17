# A removable path through the facial critical triangle

**Status:** written proof, independently audited in
[`hc7_facial_triangle_removable_path_normalization_audit.md`](hc7_facial_triangle_removable_path_normalization_audit.md).
The first
theorem is a direct application of the removable-path theorem of Du, Li,
Xie, and Yu.  The second theorem states the exact branch-set split which
would complete the surviving facial-triangle configuration.  Neither
theorem proves that this split exists, and this note does not prove `HC_7`.

## 1. First-hit removable path

### Theorem 1.1

Let `G` be a six-connected graph.  Let

\[
                       R=\{r_0,r_1,r_2\}
\]

be a triangle, and let `a,b,w` be distinct vertices outside `R`.  Suppose
that `a` is adjacent to every vertex of `R`.  Then there are a vertex
`r in R` and a `w-r` path `P` such that

\[
 V(P)\cap(\{a,b\}\cup R)=\{w,r\},
 \qquad G-V(P)\text{ is connected}.                 \tag{1.1}
\]

### Proof

Choose any `q in R`.  Apply Theorem 1.5 of Du--Li--Xie--Yu with the two
vertices `a,b` to be avoided and with path ends `w,q`.  Its connectivity
threshold is `2m+2=6` for `m=2`.  It gives a `w-q` path `P'` avoiding
`a,b` such that `G-V(P')` is connected.

Traverse `P'` from `w`, let `r` be its first vertex in `R`, and let `P`
be the initial `w-r` segment.  This path has the intersection property in
(1.1).  If `r=q`, its complement is connected by the cited theorem.
Otherwise, every vertex of the deleted suffix `P'-V(P)` is joined along
that suffix to `q`.  The vertex `q` is adjacent to `a`, while `a` lies in
the connected graph `G-V(P')`.  Restoring the suffix therefore preserves
connectedness, so `G-V(P)` is connected.  \(\square\)

## 2. Exact branch-set split

### Theorem 2.1

In addition to the hypotheses of Theorem 1.1, suppose that `a,b` are
adjacent, both are adjacent to every vertex of `R`, and `w` is adjacent to
both `a,b`.  Let `P` be a path satisfying (1.1), with end `r`, and write
`R-{r}={s,t}`.

Suppose an edge of `P` splits it into connected subpaths `P_w,P_r`
containing `w,r`, respectively, such that

1. `P_w` is adjacent to both `s,t`; and
2. `G-(V(P) union {a,b,s,t})` contains a connected subgraph `B` adjacent
   to each of

   \[
                 \{a\},\ \{b\},\ \{s\},\ \{t\},\ P_w,\ P_r.
                                                               \tag{2.1}
   \]

Then `G` contains a `K_7` minor.

### Proof

The seven sets

\[
                 \{a\},\ \{b\},\ \{s\},\ \{t\},\
                 V(P_w),\ V(P_r),\ V(B)              \tag{2.2}
\]

are pairwise disjoint and connected.  The first four singleton sets are
pairwise adjacent because `R` is a triangle, `ab` is an edge, and both
`a,b` are complete to `R`.  The set `P_w` is adjacent to `a,b` through
`w` and to `s,t` by hypothesis.  The set `P_r` is adjacent to `a,b,s,t`
through `r`.  The two path sets are adjacent through the edge at which
`P` was split.  Finally, `B` is adjacent to the other six sets by (2.1).
Thus (2.2) is an explicit `K_7`-minor model.  \(\square\)

## 3. Application and exact gap

In the balanced order-eight branch, take

\[
 a=\ell_e,\qquad b=\ell_f,
\]

and let `w` be the third vertex of the zero-slack facial critical
triangle.  The original five-clique supplies every adjacency involving
`a,b,R`, and `abw` is a triangle.  Since the hypothetical host is
seven-connected, Theorem 1.1 applies.

The live problem is therefore no longer the existence of a path from the
facial triangle to `R`.  It is the following root-preserving splitting
problem: choose the removable path so that its `w`-side retains the two
required adjacencies to `R-{r}`, while its connected complement still
contains a connected subgraph adjacent to the four reserved singleton
vertices and both path sides.  Existing removable-path theorems do not
preserve those six labelled adjacencies.

## Reference

The external input is Theorem 1.5 of Xiying Du, Yanjia Li, Shijie Xie,
and Xingxing Yu, [*Linkages and removable paths avoiding
vertices*](https://doi.org/10.1016/j.jctb.2024.06.006), Journal of
Combinatorial Theory, Series B **169** (2024), 211--232.
