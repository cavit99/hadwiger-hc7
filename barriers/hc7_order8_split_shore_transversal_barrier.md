# A minor-free split shore need not have a two-vertex common transversal

**Status:** computer-assisted counterexample to an intermediate claim;
separate internal audit GREEN in
[`hc7_order8_split_shore_transversal_barrier_audit.md`](hc7_order8_split_shore_transversal_barrier_audit.md).
The deterministic verifier is
[`hc7_order8_split_shore_transversal_barrier_verify.py`](hc7_order8_split_shore_transversal_barrier_verify.py).
This graph is not a counterexample to `HC_7` and is not asserted to be a
closed two-shore interface in a contraction-critical graph.

## Refuted statement

The following static one-shore implication is false.

> Let `S={d,e} dotcup X dotcup Y`, with `|X|=|Y|=3`. Suppose a connected
> graph `R` contains two disjoint connected subgraphs adjacent to every
> vertex of `S`. Assume `G[S]` has no `K_5` minor and `G[S union R]` has no
> `K_7` minor. If the closed shore realizes the split partition
> `X | Y | {d} | {e}` but not the merged partition
> `X | Y | {d,e}`, and there are no pairwise-disjoint vertex sets
> `D,F_X,F_Y subseteq R` such that `D` is connected and adjacent to both
> roots, while `G[X union F_X]` and `G[Y union F_Y]` are connected, then the
> three corresponding support families have a common transversal of order at
> most two.

Here a connected subgraph connects `{d,e}` when it has a neighbour at both
roots. A set `F subseteq R` connects `X` when `G[X union F]` is connected,
and similarly for `Y`.

## Construction

Number

```text
d=0, e=1, X={2,3,4}, Y={5,6,7}, R={8,9,10,11}.
```

The edge set is

```text
(0,3) (0,6) (0,8) (0,9) (0,10)
(1,3) (1,4) (1,5) (1,6) (1,9) (1,11)
(2,8) (2,9) (2,11)
(3,5) (3,6) (3,8) (3,10)
(4,5) (4,9) (4,11)
(5,9) (5,10) (5,11)
(6,8) (6,9) (6,10) (6,11)
(7,8) (7,11)
(8,9) (8,10) (8,11) (9,10) (9,11) (10,11).
```

The two parts `{8,9}` and `{10,11}` are connected and each is adjacent to
every literal boundary vertex.

With boundary colours

```text
X=0, Y=1, d=2, e=3,
```

the assignment on `R` is `(3,4,5,2)`. Exhaustive six-colour enumeration
shows that merging the colours of `d,e` has no extension.

## Packing and transversal certificates

The inclusion-minimal connected root sets are

```text
{9}, {8,11}, {10,11}.
```

The inclusion-minimal `X`-connecting sets are

```text
{8,9}, {8,11}, {9,10}, {10,11},
```

and the inclusion-minimal `Y`-connecting sets are

```text
{11}, {8,9}, {8,10}.
```

These lists contain no pairwise-disjoint choice of one set of each kind.
No subset of `R` of order at most two meets every displayed set, whereas
`{8,9,11}` does. Thus the common transversal number is exactly three.

The verifier checks all subsets rather than trusting the displayed minimal
lists.

## Minor exclusion and exact scope

The verifier checks an explicit width-five tree decomposition of
`G[S union R]`, proving that it has no `K_7` minor. It also checks a
width-two decomposition of `G[S]`, which is stronger than the stated
`K_5`-minor exclusion.

The construction has only one closed shore. It does not provide:

- a merged-only opposite shore;
- seven-connectivity of a complete host;
- seven-chromaticity or proper-minor six-colourability; or
- a counterexample to the disjunction allowing an explicit `K_7` model or
  a compatible order-seven separation.

Therefore global two-shore minor exclusion and the operation-specific
colouring responses cannot be replaced by a static theorem about the
split-response shore. In particular, the next positive theorem must use
information crossing the separation, not merely the three support families
inside `R`.
