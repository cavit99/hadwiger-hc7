# Independent audit of the adjacent-rim linkage theorem

**Verdict:** **GREEN AS PATCHED** for the exact source revision identified
below.

**Audited source:**
[`hc7_pentagonal_bipyramid_adjacent_rim_linkage.md`](hc7_pentagonal_bipyramid_adjacent_rim_linkage.md)

**Audited SHA-256:**
`8c7882e2897cedda5cb768ba34f9691a4f23f45a3482d55deae1874ab83e8e79`

This is an internal mathematical audit, not external peer review.  The
source supplies the positive completion arm for arbitrary connected PB
columns and identifies five exact set-terminal Two Paths obstructions in a
surviving expansion.  It does not eliminate those five obstructions or
prove `HC_7`.

The source was patched before hashing to say explicitly that every induced
column graph `F[V(C_x)]` is a tree in Section 4.  This is the hypothesis
needed for the exact edge count there; merely selecting a spanning tree
inside a column would not suffice.

## 1. The five branch sets

Fixing `i`, the two connected subgraphs `X,Y` lie in the two unused adjacent
rim columns `C_i union C_{i+1}`.  Hence they are disjoint from all five whole
columns used in

```text
C_a union X,
C_b,
C_{i-1} union Y,
C_{i+2},
C_{i+3}.
```

The first and third sets are connected by the first and third contacts in
(2.1), respectively; the other three are connected whole columns.

For the five PB labels

```text
a, b, r_(i-1), r_(i+2), r_(i+3),
```

the only missing quotient edges are `ab` and
`r_(i-1)r_(i+2)`.  The three selected rim vertices are consecutive in the
complementary three-vertex rim path: `r_(i+2)r_(i+3)` and
`r_(i+3)r_(i-1)` are rim edges, while the two endpoints are nonadjacent.
Every pole contacts every rim vertex.  The subgraph `X` repairs `ab`, and
`Y` repairs the missing rim edge.  Thus all ten pairwise adjacencies of the
five displayed branch sets are literal.

Each set contains a different whole column, so each fixed root contacts all
five.  Together with the root-root edge, this gives the asserted explicit
`K_7`-minor model.

The arbitrary-column split corollary uses the same lift without any tree
hypothesis.  A partition of one connected column into two nonempty
connected vertex sets has a literal edge between the two sides.  Giving
each clone every old neighbour label contacted on its side therefore
produces a valid adjacent vertex split of the PB quotient.  Four distinct
alternating labels invoke the audited split classifier.  Its explicit
`K_5` model puts a nonsplit old quotient vertex in every branch set, so the
two fixed roots contact all five lifted sets regardless of how their
contacts with the split column are distributed.  Thus Corollary 2.2 has no
hidden clone-to-root assumption.

## 2. Exact Two Paths equivalence

The four artificial vertices in `H_i` are new and distinct.  Their
neighbour sets are exactly the literal portals in `C_i union C_(i+1)` to
`C_a,C_b,C_(i-1),C_(i+2)`.

If `H_i` has disjoint `alpha-beta` and `gamma-delta` paths, deleting their
artificial endpoints leaves two nonempty, connected and vertex-disjoint
subgraphs `X,Y` with precisely the four required external contacts.

Conversely, choose in `X` a portal to `C_a` and a portal to `C_b`, and join
them inside connected `X`; adjoining `alpha,beta` gives the first path.
Do the same in `Y` for the other terminal pair.  If two portal sets overlap,
the two portals within one connected subgraph may be the same literal
vertex, yielding a length-two path such as `alpha-q-beta`; this is valid.
Because `X` and `Y` are vertex-disjoint and the four artificial terminals
are distinct, the two resulting paths are vertex-disjoint.  Thus overlap
among portal sets creates no hidden distinctness assumption.

The equivalence is exact, and absence of a `K_7` forces all five negative
Two Paths instances by the completion theorem.

## 3. Repeated-contact count

Under the patched induced-tree hypothesis, the seven columns contribute
exactly `n-7` internal edges, and `m` counts every inter-column edge exactly
once.  Therefore

```text
|E(F)| = n - 7 + m.
```

Five-connectivity gives minimum degree at least five, whence

```text
5n <= 2(n-7+m)
m >= ceil((3n+14)/2).
```

Since all seven columns are nonempty, `n>=7`, so `m>=18>15=|E(P)|`.
At least one quotient edge therefore has repeated literal contacts.  No
finite-order assumption or enumeration is used.

## 4. Trust boundary

Five-connectedness and the proper-minor colouring responses have not yet
been coupled to the five negative Two Paths certificates.  The adjacent
[barrier](../barriers/hc7_pentagonal_bipyramid_split_linkage_planarity_barrier.md)
shows more than failure of the linkage-only target: all five linkages can
fail in a five-connected nonplanar expansion with no alternating connected
split in any column.  That example still has an anchored `K_5` model, but
only through a simultaneous division and absorption of two columns.
Accordingly, the positive mechanisms proved here are sufficient but not
exhaustive.  The missing theorem must allow a global multi-column
allocation outcome, rather than infer planarity after the two local tests
fail.

The theorem does not assert that a web completion edge is literal, that a
failed linkage gives a small host separator, or that the five web orders
are globally compatible.

With the induced-tree clarification, every branch-set construction,
terminal equivalence and edge count is valid at the audited source hash.
**GREEN AS PATCHED.**
