# Audit of the first-entry singleton-peel theorem

## Verdict

**GREEN** at the exact source revision

```text
ac4bdeaf72a40f68b57f501878941333255f9c2724172b60fa34c5da530af146  results/hc7_first_entry_singleton_peel.md
```

This is a separate internal audit, not external peer review.  The singleton
neighbourhood identity, the exact-separation alternative, the clean transfer,
the explicit pattern-`B` minor models and the finite sharpness example are all
correct under their stated hypotheses.  No unresolved mathematical assumption
remains inside the conditional result.

The promoted revision differs from the revision audited line by line only in
the status metadata: `internal audit pending` was replaced by `separate
internal audit`.  Reversing that edit reproduces the fully audited SHA-256
`011433af334f4f1bd269f51fdd970bf649b403cfe87efd889c6c59295e5fea5d`.
The theorem statement and proof are unchanged.

## 1. Exact neighbourhood and separator calculation

Because `D` is a component of `G-N_G[v]`, every neighbour of `D` outside
`D` belongs to `N_G(v)`; no vertex of `D` is adjacent to `v`.  Thus
`S=N_G(D)` is a genuine separator with `v` on its far side, and
seven-connectivity gives

```text
7 <= |S| <= 8.
```

For a vertex `y` such that `D-y` is nonempty and connected, every outside
neighbour of `D-y` is either `y` or a member of `S`.  A vertex `s in S`
has a neighbour in `D-y` exactly when its neighbourhood in `D` is not the
singleton `{y}`.  Finally, connectedness of `D` makes `y` adjacent to
`D-y`.  Since `y notin S`, this proves the disjoint identity

```text
N_G(D-y) = {y} dotunion (S-Lambda_D(y)).
```

The two numerical alternatives are exhaustive.  If at most six original
labels remain, the displayed neighbourhood has order at most seven.  It
separates the surviving nonempty connected set `D-y` from the surviving
vertex `v`, so seven-connectivity raises its order to exactly seven.  If at
least seven labels remain, the claimed connected seven-label residual is
immediate.  Adjoining `y` to a connected set with an edge to `y` preserves
that set's old adjacencies and leaves it disjoint from `D-y`.

## 2. Proper-minor colouring at the exact boundary

When `|D-y|>=2`, contracting a spanning tree of `D-y` strictly reduces the
graph and hence gives a proper minor.  Its representative is adjacent to
every vertex of `T'=N_G(D-y)`.  A proper six-colouring therefore omits the
representative's colour on all seven boundary vertices.  Edges between
unchanged vertices are unaffected by the contraction, so restricting the
colouring gives a proper colouring of `G-(D-y)` using at most five colours
on `T'`.

For the final edge `xy` of a clean first-entry path, `x` lies in `S` and

```text
x in T'  iff  x notin Lambda_D(y).
```

Thus the source correctly no longer assumes that both ends lie on `T'`.
Both ends do lie in the unchanged closed side `G-(D-y)`.  Under the
explicitly stated additional hypothesis that `G` is not six-colourable, the
ends have the same colour in every six-colouring of `G-xy`; otherwise that
colouring would also colour `G`.  A contraction colouring likewise assigns
one colour to the two literal ends.  Neither operation alone can therefore
be pulled back over the restored edge as a proper colouring of the original
closed side.

## 3. Clean direct and prefix entries

A clean path starts in `P_s`, has only its last vertex `y` in `D`, and has
no internal vertex in any other fixed connected subgraph.  Its first endpoint
already belongs to `P_s`, its other endpoint belongs only to `D`, and all
internal vertices avoid every competing named set.  Consequently

```text
P_s -> P_s union V(R_s),       D -> D-y
```

preserves pairwise disjointness.  The path makes the enlarged `P_s`
connected and preserves every old adjacency of `P_s`; only `y` is removed
from `D`.  Hence the singleton calculation applies equally to a direct edge
and to a clean longer prefix.  The definition deliberately does not cover a
prefix that first enters another named connected subgraph.

## 4. Cyclic-incidence consequences

Items 1--3 in Section 4.2 use the separately audited theorem

```text
cc3c6012b32e8f0116e4c3863ad9cbd7199620419ab2d8df9b3de517000029c2  results/hc7_connected_row_cyclic_corner_dichotomy.md
```

and its audited cyclic allocation dependency

```text
84c47863546f9800db24bf042e60952221dcf3649b4076170259efa9fde78049  results/hc7_degree8_contact_allocation.md
```

The clean transfer preserves the hypotheses needed there: all named sets
remain connected and disjoint, old cyclic and cross adjacencies survive,
and `D-y` is a connected seventh set retaining at least seven of the eight
neighbour labels.  The corrected `C_4` clause is sufficient: if the possible
lost label belongs to `C_4`, then `D-y` remains adjacent to
`P_0,P_1,P_2,C_0,C_1,C_2,C_3`, exactly as required by the explicit
all-defects-at-`C_4` construction.

If the enlarged `P_s` is anticomplete to a rooted `C_i`, it contains `y in R`
and hence meets the open shore.  The rooted-corner theorem therefore applies.
Its exact boundary or strict decrease retains `u_i` and `P_s`, as stated.
The revised source correctly limits this to a local incidence reduction: the
other labels and colouring data need not survive.

## 5. Independent check of the pattern-B completion

After a clean `s=1` peel repairs `P_1C_3` in normalized pattern `B`, the
only possible cross-nonadjacencies are `P_0C_0` and `P_0C_1`.  Put
`D'=D-y`.  At most one of the eight named connected sets is anticomplete to
`D'`.  Every row of (4.3) is a valid seven-branch-set model:

1. For `O` absent or in `{C_0,C_1,C_2}`, the three sector sets are
   `C_0 union C_1 union C_2`, `C_3`, and `C_4`.  They form three mutually
   adjacent cyclic arcs.  The set `{v} union P_0` is connected and reaches
   every sector through `v`; `D'` reaches the composite sector through at
   least two of its three labels and reaches every other displayed set.
2. For `O=P_0`, `D' union P_1` is connected and uses the complete
   `P_1`--sector contacts.  The singleton `P_0` reaches the composite sector
   through `C_2` and reaches `C_3,C_4` directly.
3. For `O=P_1` or `O=P_2`, `D' union P_0` is connected.  Its missing
   `P_0C_0,P_0C_1` contacts are supplied by `D'`, while `P_0` supplies its
   adjacencies to the other two row sets.
4. For `O=C_3`, the sector sets `C_0 union C_1`,
   `C_2 union C_3`, and `C_4` are connected and pairwise adjacent.  The
   missed `D'C_3` contact is replaced by `D'C_2` inside the second set.
5. For `O=C_4`, the sector sets `C_0 union C_1 union C_4`, `C_2`, and
   `C_3` are connected and pairwise adjacent.  The missed `D'C_4` contact is
   replaced by `D'C_0` or `D'C_1` inside the first set.

In every row, `P_1,P_2` are adjacent to all sector sets, the three `P`-sets
are pairwise adjacent, and `v` is adjacent to the named neighbour contained
in every `P`- or `C`-set.  These observations verify all twenty-one
branch-set adjacencies, including the formerly omitted pattern-`B`, `s=1`
case.

The owner table (4.4) is then exhaustive within the four normalized patterns:
patterns `A,D` have rooted defects only in row `0`; pattern `B` has them in
rows `0,1`; and pattern `C` has them in rows `0,1`.

## 6. Sharpness example

In the graph of Section 5, the four vertices of `D` induce `K_4`, so `D` is
three-connected.  Each of the eight boundary labels has a neighbour in `D`,
and the paths `b-y_k-i` have pairwise disjoint internal vertices.  No vertex
of `D` sees all eight labels.

Every proper connected `X subset D` adjacent to both `a` and `b` contains
`p` and exactly one or two of the three `y`-vertices.  If it contains `k`
of them, `D-X` is a nonempty clique and contacts precisely

```text
{b,i}, the 3-k surviving private t-labels, and {t_4,t_5},
```

for a total of `7-k<=6` labels.  Every vertex of `X` is adjacent to the
residual clique, so

```text
|N_G(D-X)| = |X| + (7-k) = (1+k)+(7-k)=8.
```

This proves exactly the claimed obstruction to replacing the singleton by
an arbitrary connector.  The source correctly states that this graph is not
seven-connected or contraction-critical and is not an `HC_7` counterexample.

## 7. Exact trust boundary

This audit does **not** establish any of the following:

- the existence of a clean first-entry path with an owner listed in (4.4);
- that a chosen first-entry vertex has connected nonempty deletion residual;
- preservation of both paired traces, all five cyclic connected sets, the
  selected boundary-edge response or a common colouring partition under the
  rooted-corner strict descent;
- extension of the one-sided boundary partition through the opposite closed
  shore of the returned order-seven separation;
- a label transfer when a path first meets the wrong named connected
  subgraph; or
- an extension of the singleton calculation to a larger connector.

These are correctly retained as the active host-level contact-transfer and
colour-synchronization obligations.  The theorem is a conditional unbounded
reduction, not a proof of `HC_7`.
