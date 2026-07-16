# Cold audit of the unbalanced marked-row collapse

**Verdict:** GREEN.

Audited source:
[`hc7_marked_three_clique_unbalanced_collapse.md`](hc7_marked_three_clique_unbalanced_collapse.md).

Source SHA-256:

```text
d7ee14308e3786afee54ca760f02e733c61c618cb6bdbdef2404665360722eb5
```

The separator arguments, use of disjoint row sets, placement of the three
marks, and all three arithmetic cases are valid.  No graph-minor decoder or
predecessor connectivity is used.

## 1. Dependencies checked

The proof uses exactly the following source properties of the marked Mader
certificate.

1. `H` is six-connected.
2. The three literal cliques `L_i` are pairwise vertex-disjoint, and
   `z_i in L_i`.
3. Every six-separator contains all three `z_i`.
4. The auxiliary rows `A_i` are pairwise disjoint, `B_i subseteq A_i`, and
   `L_i-W subseteq A_i`.
5. If `A_i-B_i` is nonempty, then `W union B_i` separates that tail from
   the other rows.
6. For `2<=w=|W|<=5`, every row satisfies `|B_i|>=5-w`, and the rows obey
   `sum_i |B_i|<=3(6-w)`.

These are the audited outputs of the preceding cut/counting reduction.  In
particular, the proof does not assume that `W` is itself a separator or
that it initially contains any prescribed mark.

## 2. The deficient row is tail-free

Assume `|B_h|=5-w`.  If `A_h-B_h` were nonempty, its displayed boundary
`W union B_h` would have order five.  Both open sides are nonempty.  The
tail supplies one side.  For the other, among the two cliques distinct from
`L_h`, at least one has a vertex outside `W`: a set of order at most five
cannot contain both disjoint five-cliques.  Its `L_j-W` vertices lie in the
disjoint row `A_j`, hence outside `A_h union W`.  Thus the boundary really
is a separator of order five, contradicting six-connectivity.

Consequently `A_h=B_h`.  Since `L_h-W subseteq B_h`,

\[
  5-|W\cap L_h|=|L_h-W|\le |B_h|=5-w.
\]

It follows that `|W cap L_h|>=w=|W|`, so

\[
                              W\subseteq L_h.                   \tag{2.1}
\]

The same inequalities are equalities, so in fact `B_h=L_h-W`, although
only (2.1) is subsequently needed.  Since `w>=2`, `W` is nonempty; no
second disjoint `L_j` can also contain it.  Hence the deficient row is
unique.  For each `j ne h`, disjointness of the named cliques gives

\[
                    W\cap L_j=\varnothing,\qquad L_j\subseteq A_j. \tag{2.2}
\]

## 3. The two other row bounds

Fix `j ne h`.

If its tail is empty, then `A_j=B_j`; equation (2.2) gives

\[
                              |B_j|\ge5.                         \tag{3.1}
\]

If its tail is nonempty, its boundary has order at least six, so
`|B_j|>=6-w`.  Equality is impossible.  Indeed, equality makes
`W union B_j` a genuine six-separator: the tail is one open side and the
remaining outside row is nonempty on the other side.  Let
`{h,j,k}={1,2,3}`.  By (2.1) and disjointness of the cliques,
`z_k notin W`.  Moreover,

\[
                      z_k\in L_k\subseteq A_k,
\]

while `B_j subseteq A_j` and `A_j cap A_k=emptyset`.  Therefore this
six-separator omits `z_k`, contradicting the marked-cut law.  The integer
bound strengthens to

\[
                              |B_j|\ge7-w.                       \tag{3.2}
\]

This verifies that the proof does not silently put the third mark in the
wrong row or assume that all marks lie in `W`.

## 4. Exhaustive arithmetic

There are only three cases for the two rows other than `h`.

* If both have tails, (3.2) gives

  \[
  \sum_i|B_i|\ge(5-w)+2(7-w)=19-3w>18-3w.
  \]

* If exactly one has a tail, (3.1)--(3.2) give

  \[
  \sum_i|B_i|\ge(5-w)+(7-w)+5=17-2w.
  \]

  The difference from the allowed upper bound `18-3w` is `w-1>0`
  because `w>=2`.

* If neither has a tail, (3.1) gives

  \[
  \sum_i|B_i|\ge(5-w)+10=15-w.
  \]

  The difference from `18-3w` is `2w-3>0` for `w>=2`.

All cases contradict the sum bound.  Hence no row has order `5-w`.
Integrality and the lower bound imply every row has order at least `6-w`;
the upper bound on their sum then forces all three orders to equal `6-w`.

## 5. Scope

The lemma eliminates the unbalanced row-size branch only in the stated
range `2<=|W|<=5` and under the literal marked-separator and source-row
axioms.  It neither constructs a `K_7` model nor treats an arbitrary set
system lacking the separator realization.  Within the exact marked Mader
setup, however, there is no surviving unbalanced row vector.

## 6. Independent confirmation

A second cold audit reconstructed the separator argument independently and
attempted to realize the listed axioms with a deficient row.  It confirmed
that every displayed separator has two nonempty open shores, that the third
mark is outside each forbidden six-cut, and that no abstract certificate
satisfying the stated axioms can violate the conclusion.  It also confirmed
the combined consequence: after the previously audited balanced decoders,
only the unbalanced `|W|=0,1` outcomes remain in the actual
minimal-three-contraction route.
