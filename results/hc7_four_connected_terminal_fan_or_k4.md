# A rooted clique-or-fan theorem for four-connected graphs

## Status

Proved and independently cold-audited.  See
[`hc7_four_connected_terminal_fan_or_k4_audit.md`](hc7_four_connected_terminal_fan_or_k4_audit.md).

This theorem is independent of `HC_7`.  It packages the rooted-`K_4`
theorem of Fabila-Monroy and Wood with the peripheral-cycle structure of a
three-connected plane graph.  Its point is that the planar obstruction to a
rooted `K_4` supplies a larger labelled carrier rather than ending the
argument.

## Theorem

Let `H` be a simple four-connected graph, let `T` be a set of `k>=5`
distinct vertices, and prescribe any three-element anchor set
`A={a,b,c} subseteq T`.  Then at least one of the following holds.

1. For some `x in T-A`, the four vertices `A union {x}` root a `K_4`
   minor in `H`.
2. The graph `H` is planar, all members of `T` lie on one facial cycle, and,
   for every prescribed `t in T`, the set `T` roots

   ```text
   F_k = K_1 join P_{k-1}
   ```

   with the bag containing `t` as the universal bag.  The path order of the
   other `k-1` rooted bags is their cyclic order on that face with `t`
   removed.

Here a `T`-rooted model has one pairwise disjoint connected bag containing
each member of `T`; extra adjacencies between the bags are harmless.

## Proof

The rooted-`K_4` theorem of Fabila-Monroy and Wood has the following two
consequences.

* If a four-connected graph is nonplanar, every four prescribed vertices
  root a `K_4` minor.
* If a three-connected plane graph is planar, four prescribed vertices fail
  to root a `K_4` minor exactly when they lie on one face.

We may therefore assume that outcome 1 fails.  Then `H` is planar and every
anchored four-set `A union {x}` is cofacial.  Fix the unique plane embedding
of `H`, up to reflection.  For any two further terminals `x,y`, let `F_x`
contain `a,b,c,x` and let `F_y` contain
`a,b,c,y`.  Distinct faces of a three-connected plane graph share at most
two vertices, whereas these two faces share `a,b,c`.  Hence `F_x=F_y`.
Varying `x,y` shows that one face contains all of `T`.  Let `C` be its
boundary cycle.

A facial cycle in a three-connected plane graph is peripheral: it is
induced and `H-V(C)` is connected, when nonempty.  In the present graph the
remainder

```text
R = H-V(C)
```

is nonempty and every vertex of `C` has a neighbour in `R`.  Indeed,
four-connectivity gives minimum degree at least four, while an induced
facial cycle supplies exactly two neighbours on `C`.  Peripheral
nonseparation makes `R` connected.

Read the members of `T` in their cyclic order on `C`.  Partition `C` into
`k` vertex-disjoint path bags by assigning to each terminal the oriented arc
starting at it and stopping immediately before the next terminal.  These
bags are connected, rooted at `T`, and consecutive bags are adjacent.

Fix the prescribed terminal `t` and enlarge its path bag by all of `R`.
The enlarged bag is connected because `R` is connected and meets every
vertex of `C`.  It remains disjoint from the other path bags and is adjacent
to every one of them.  The other `k-1` bags occur as a path in facial cyclic
order.  They and the enlarged universal bag form the required rooted
`K_1 join P_{k-1}` model.  Since `t` was arbitrary, outcome 2 holds with any
prescribed universal root.  \(\square\)

## Exact scope

The anchor triple is arbitrary but must be fixed before applying the
theorem.  Thus an application need test only the `k-3` rooted four-sets
`A union {x}`, not all four-subsets of `T`.  The fan bags give actual
branch-set adjacencies; no facial completion edge is treated as an edge of
`H`.

## Published input

R. Fabila-Monroy and D. R. Wood, *Rooted K4-Minors*, Electronic Journal of
Combinatorics **20** (2013), P64,
[arXiv:1102.3760](https://arxiv.org/abs/1102.3760).
