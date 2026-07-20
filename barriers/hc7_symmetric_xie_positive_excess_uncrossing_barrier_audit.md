# Independent audit: symmetric positive-excess cuts do not uncross by neighbourhood submodularity

**Verdict:** **GREEN.**  The stated graph is a valid explicit counterexample
to the symmetric-cut uncrossing principle in the source.  This is a separate
internal mathematical audit, not external peer review.  The graph is not a
counterexample to `HC_7`.

## Audited revisions

This audit checks the complete source file
[`hc7_symmetric_xie_positive_excess_uncrossing_barrier.md`](hc7_symmetric_xie_positive_excess_uncrossing_barrier.md)
at SHA-256

```text
d9a9b0553b0040dc6e83234d2a04ff32992ec8004311c851092008ff356d447d
```

The promoted source revision has SHA-256

```text
6c5c54530d6d82cb143601cf58cdf7084ac6340338e20cf78ba21d140235cf04
```

It differs from the audited revision only in the opening status declaration,
which now records this GREEN audit and links to it.  No mathematical content
changed during promotion.

The audit also checks the deterministic verifier
[`hc7_symmetric_xie_positive_excess_uncrossing_barrier_verify.py`](hc7_symmetric_xie_positive_excess_uncrossing_barrier_verify.py)
at SHA-256

```text
e9a50b3d8548d19b5a9f265942e00cb851fa4bf2cbc9ae31e7f68d80b461da25
```

## Construction and host hypotheses

The verifier constructs the stated 32-vertex graph `H`.  Before every one of
the five replacements, the deleted edge has exactly the two endpoints of the
displayed added edge as its common neighbours.  Thus these are genuine
diagonal flips.  Planarity is checked after every flip.  The final graph has
90 edges, vertex-connectivity five, nonadjacent vertices `0,4` of degree
seven, and disjoint open neighbourhoods at those vertices.

For `G=K_2 join H`, the checker computes vertex-connectivity seven.  The
minor exclusion also follows without relying on a bounded minor search.  At
most two disjoint branch sets of a putative `K_7` model can contain the two
new universal vertices.  Hence at least five branch sets would be contained
in `H`; their host adjacencies would give a `K_5` minor in the planar graph
`H`, which is impossible.

Deleting

```text
S = {p,q,2,12,13,17,18,19}
```

leaves exactly the singleton component `{1}` and the displayed 25-vertex
component `L`.  The checker verifies `N_G(1)=S`.  The displayed sets `E,D`
are disjoint, cover `L`, induce connected graphs, and have an edge between
them.  Consequently `(L,S,{1})` is the claimed actual order-eight
separation, and its singleton shore is adjacent to every literal boundary
vertex.

## The two completion cuts

On the `E` side, the actual completion graph is
`G[E union {12}]` with terminal triple `(6,7,12)` and terminal pair
`(9,21)`.  The five terminals are distinct.  After adding the Xie-completion
edges, deleting

```text
K_E = {5,8,12,14,15}
```

leaves `{0}` as a terminal-free component and leaves a second nonempty
component.  Its original internal neighbourhood is exactly
`N_E(0)={5,8,14,15}`.

On the `D` side, the completion graph is `G[D union {2}]`, with terminal
triple `(3,10,2)` and terminal pair `(16,20)`.  Again the terminals are
distinct.  Deleting

```text
K_D = {11,23,24}
```

isolates the terminal-free component `{4}` and leaves a second nonempty
component.  Its original internal neighbourhood is exactly
`N_D(4)={11,23,24}`.  In particular, the phrase “on both `E` and `D`” in
the refuted principle is instantiated by the two side completions just
specified; no virtual completion edge is treated as an edge of `G`.

## Full neighbourhoods and uncrossing

The literal full neighbourhoods are

```text
N_G(0) = {p,q,5,8,12,13,14,15,16},
N_G(4) = {p,q,6,11,23,24,26,27,28}.
```

They have order nine and intersect exactly in `{p,q}`.  Since `0,4` are
nonadjacent,

```text
|N_G({0,4})| = 9 + 9 - 2 = 16.
```

Each singleton neighbourhood is an actual separation boundary: deleting it
isolates its singleton while the other selected singleton remains outside.
Thus none of `{0}`, `{4}`, or `{0,4}` has boundary of order at most eight,
and `G` has no `K_7` minor.  The neighbourhood-submodularity inequality used
in the source reduces only to `18 >= 16`; it supplies no selected small
boundary.  This verifies the advertised counterexample to the intermediate
principle.

## Verifier execution

Running

```text
PYTHONPATH=active/runtime/deps python3 barriers/hc7_symmetric_xie_positive_excess_uncrossing_barrier_verify.py
```

at the audited revisions exits successfully and prints exactly:

```text
GREEN symmetric Xie positive-excess uncrossing barrier
H: vertices=32 edges=90 connectivity=5 degrees(0,4)=(7,7)
G: vertices=34 edges=155 connectivity=7; exact order-8 separator with component sizes 1,25
Xie cuts: east=5 terminal-free {0}; west=3 terminal-free {4}
full boundaries: b(0)=9 b(4)=9 b({0,4})=16 common={p,q}
scope: no proper-minor response or two-full-subgraph claim
```

## Trust boundary

The source states the limitation accurately.  The example is six-colourable,
is not contraction-critical, has only one boundary-full connected subgraph
on the opposite shore, and does not realize the labelled triangles,
proper-minor boundary responses, or branch-set data of the live `HC_7`
configuration.  It also has unrelated order-seven separators.  It therefore
refutes only uncrossing based on the two selected low-order completion cuts
and ordinary full-neighbourhood submodularity; it does not refute a theorem
using the omitted host-level hypotheses or one allowed to return an arbitrary
order-seven separation.

No mathematical gap or verifier mismatch was found.
