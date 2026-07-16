# Decorated three-model genuine-cell decoder: exact falsifier

**Status:** audited computational barrier.  This falsifies the boxed
decoder (4.1) in `active/hc7_decorated_three_model_hwege.md`.  It does
**not** falsify the lifted seven-connected statement or the stronger
minimal-bad quotient condition that every ordinary six-separator contains
all three marked vertices.

## 1. The graph

Start with the planar 3-tree `R` on vertices `0,...,11`.  One construction
starts from the `K4` on `{1,5,10,11}` and stacks, in order,

```text
0 on 1,5,10;   2 on 0,1,5;   3 on 0,1,2;   4 on 0,1,3;
9 on 0,3,4;    6 on 1,2,5;   7 on 2,5,6;   8 on 2,6,7.
```

It has three vertex-disjoint `K4`s

```text
Q1 = {2,6,7,8},  Q2 = {0,3,4,9},  Q3 = {1,5,10,11}.
```

Add marked vertices `z1=12,z2=13,z3=14`, make `zi` complete to
`Qi`, and add

```text
4-14, 7-14, 8-14, 9-14, 10-13, 11-12, 12-13.
```

Then

```text
L1 = Q1 + 12,  L2 = Q2 + 13,  L3 = Q3 + 14
```

are three disjoint literal `K5`s and their union is the whole vertex set.
The full 49-edge list is frozen in the verifier.

## 2. Exact facts

Give each `zi` weight two and every other vertex weight one.  Exhaustive
enumeration of every vertex deletion set proves

\[
 \min\{|T|+|T\cap\{12,13,14\}|:T\text{ separates }H\}=7.
\]

There are eleven minimum weighted separators.  The ordinary connectivity
is five.  Its seven five-separators all contain exactly two marked
vertices, so all seven expand to literal order-seven cuts.

Two independent exact encodings prove that `H` has no `K7` minor.  The
first gives every branch set a unique root and a strictly decreasing
depth path to it.  The second computes Floyd--Warshall reachability using
only vertices assigned to the same branch set.  Both complete with
`unsat`.

Finally, there is no genuine Mader cell in any obstruction certificate.
Indeed, the Mader condition puts every vertex of
`(L1 union L2 union L3) intersect Y_j` in `X_j`.  Here the three cliques
cover `V(H)`, hence `Y_j=X_j` for every cell, independently of maximality.

Thus the host satisfies every stated hypothesis of (4.1), has no `K7`,
and has no genuine cell.  The proposed decoder is false.

## 3. Sharpness and what survives

The counterexample is not six-connected, so it does not refute

```text
six-connected + three disjoint K5s => K7,
```

nor the sharper condition that every six-separator contains all three
marks.  It also does not lift to an HC7 counterexample.  An exhaustive
edge-distribution search splitting each `zi` back into an edge found that
every degree-seven/seven-connected lift contains a literal `K7` model.

The ordinary five-cuts show exactly why the quotient-only weighted
decoder is too weak: contraction can hide a five-cut containing two
split vertices.  The missing hypothesis must retain split-edge incidence
or the minimal-bad six-separator property; weighted separator order alone
cannot force a genuine cell.

There are exactly twenty two-edge additions which minimally hit all seven
ordinary five-cuts.  Every one already creates a `K7` minor.  This is
positive evidence for the six-connected/minimal-bad successor, but is not
a proof for arbitrary augmentations.

## 4. Reproduction

```bash
python3 barriers/hc7_decorated_hwege_genuine_cell_falsifier_verify.py
```

Expected terminal lines include

```text
weighted_separator_order 7
ordinary_connectivity 5
depth_K7 False
warshall_K7 False
minimum_two_edge_connectivity_augmentations 20
all_minimum_augmentations_have_K7 True
genuine_Mader_cell_possible False
```
