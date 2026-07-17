# Four-connected seven-root composition in the order-six overlap-three cell

## Status

**Computer-assisted theorem; independent audit pending.**  The exhaustive,
dependency-free checker is
[`hc7_overlap_three_order_six_four_connected_kernel_verify.py`](hc7_overlap_three_order_six_four_connected_kernel_verify.py).

This closes an unbounded carrier family, but it does not close the whole
arm-order-six, overlap-three cell or `HC_7`.  The remaining structural gap
is stated in Section 4.

## 1. Normalized relation

Use

```text
A={0,1,2,3,4,5},       I={0,1,2},
X={0,1,2,6,7},          p=8, q=9,
T={3,4,5,6,7,8,9}.
```

Impose the nine irredundant six-support relations

```text
A, X+p, X+q,
(A-{i})+p, (A-{i})+q  for i in I.
```

The exact join has `60,162` partial states, each with seven undecided
original edges.  The previously proved common rooted-`K_4` outcome removes
all but `140` symmetry orbits.  Direct literal `K_7` models remove a further
`30`, leaving

```text
110 orbits of weight 6,636.
```

## 2. Carrier theorem

### Theorem 2.1

Let `K` be any simple four-connected graph whose vertex set is the seven
labelled terminals `T`.  Add each edge of `K` only as an adjacency between
the corresponding `T`-rooted carrier bags.  For every surviving joined
state, the resulting ten-object quotient contains a `K_7` minor.

Consequently, if `G-I` contains seven pairwise disjoint connected bags,
one rooted at each member of `T`, whose bag-adjacency graph is
four-connected, then `G` contains a literal `K_7` minor.

### Proof certificate

The property of containing `K_7` is monotone under adding carrier edges, so
it is enough to test edge-minimal four-connected graphs on the seven
labels.  The checker enumerates all `2^21` labelled graphs and obtains

```text
1,522 edge-minimal four-connected carriers:
  360 with 14 edges,
1,162 with 15 edges.
```

It composes every carrier with every one of the `110` live state orbits.
The shared exact branch-set enumerator certifies `K_7` in all

```text
1,522 * 110 = 167,420
```

compositions.

For the lift, replace a terminal quotient vertex by its corresponding
rooted carrier bag and keep the three members of `I` as singleton bags.
Original edges incident with a terminal remain available through the
literal root in its bag.  Carrier edges are actual inter-bag adjacencies.
The seven rooted bags lie in `G-I`, are connected and pairwise disjoint, so
every quotient branch set and adjacency lifts literally.  No carrier edge
is used in an irredundant-support relation. \(\square\)

## 3. Sharpness against three-connectivity

Four-connectivity in Theorem 2.1 cannot be replaced by
three-connectivity.  The exact counterexample and checker are recorded in
[`hc7_order_six_arbitrary_rooted_kernel_barrier.md`](hc7_order_six_arbitrary_rooted_kernel_barrier.md).

Thus the theorem is not a disguised consequence of the universal
seven-root `C_7`-or-`K_{3,4}` carrier theorem.  The extra connectivity is
doing real composition work.

## 4. Exact remaining structural gap

In the application `H=G-I` is itself four-connected.  The theorem would
close the cell if every seven prescribed vertices in a four-connected
graph admitted a seven-bag rooted minor whose bag-adjacency graph remained
four-connected.  That rooted compression statement is **false**.  In the
cycle square `C_8^2`, take seven vertices as terminals and call the eighth
vertex `x`.  A seven-bag rooted quotient can only delete `x` or assign it
to one adjacent terminal.  Deletion leaves vertices of degree three, while
`C_8^2` is four-contraction-critical, so neither operation leaves a
four-connected seven-vertex quotient.

Thus ordinary contraction cannot supply the missing bridge.  The positive
finite theorem must be combined with a structured alternative.

Two mechanisms now have a precise target:

1. a terminal-legal four-contraction theorem, with the
   Fontet--Martinov cycle-square/line-graph alternatives retained and
   separately decoded; or
2. a label-preserving split of a branch bag whenever a three-connected
   terminal kernel loses four-connectivity.

Either mechanism need only return a four-connected seven-bag carrier, not
an arbitrarily prescribed rooted clique model.
