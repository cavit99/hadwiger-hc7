# Audit of the singleton full-component reduction

**Verdict:** GREEN.

**Audited source:**
`results/hc7_order8_two_cut_singleton_reduction.md`

**Audited SHA-256:**
`6b49df2039ecaa433b7d67c10939f4d6ee956dd6b06558d20ee1b249d9dd78f8`

**Promoted source SHA-256:**
`e3d0d077a9eda4cae3c05b327928e47adc6df2402674b55f1c443e3549b0d617`

The promoted revision changes only the status line and adds this audit link;
the theorem statement, proof, dependencies, and trust boundary audited
below are unchanged.

**Audit type:** independent internal mathematical audit.  This is not
external peer review and does not prove `HC_7`.

## Imported hypotheses

The audited response-orientation theorem supplies all imported facts.  In
particular, `P,R` are nonempty independent sets with an actual edge between
them; `d,e` are nonadjacent and each has a neighbour in both classes;
`A_d,A_e` are disjoint connected adjacent subgraphs of `C`, with exact
boundary defects `d,e`; and the closed `C`-side has a proper six-colouring
inducing

```text
P | R | {d} | {e}.
```

No palette colour is identified with either a boundary or branch-set label.

## Root-splittability and distinct representatives

For a boundary-full connected component `Q_i`, both portal sets

```text
N(d) intersect Q_i,   N(e) intersect Q_i
```

are nonempty.  Two nonempty sets admit distinct representatives precisely
when their union has order at least two.  Indeed, if the union contains two
vertices, choose one representative from each set; if an initial choice
coincides in their intersection, at least one of the two sets contains the
other vertex and that choice can be changed.  Conversely, distinct
representatives make the union have order at least two.  Thus failure of
root-splittability is equivalent to both portal sets being the same
singleton `{q}`.

When distinct representatives `q_d,q_e` exist, connectedness of `Q_i`
gives a nontrivial path between them.  Deleting any edge of a spanning path
tree partitions the whole path into two nonempty connected adjacent pieces,
one retaining the `d` contact and the other the `e` contact.  This is the
exact split required by the four-block part of the reserved-path theorem.

## Both opposite components root-splittable

Fix `i` and put `j=1-i`.  The reserved-path theorem requires only a vertex
partition

```text
V(G)=L dotcup S dotcup R',   E(L,R')=empty,
```

and three specified connected subgraphs in `R'`; it does not require `R'`
itself to be connected.  Therefore it is legitimate to take

```text
L=Q_i,   R'=C union Q_j.
```

The two open sets are anticomplete because they are unions of distinct
components of `G-S`.  In `R'`, use the nontrivial root-portal path in
`Q_j`, together with `A_d` and `A_e`.  These three connected subgraphs are
pairwise disjoint.  Exact defect information makes `A_d` adjacent to every
vertex of `P` and `A_e` adjacent to every vertex of `R`; the portal path
has both root contacts and has the required adjacent connected split.

All remaining boundary hypotheses of the reserved-path theorem—the
nonedge `de`, root contacts to both classes, and a `P`--`R` edge—come from
the response-orientation theorem.  Hence the closed `Q_i`-side realizes
the four-block partition.  Repeating for `i=0,1` and aligning both
colourings with the prescribed closed-`C` colouring is valid because the
three open components are pairwise anticomplete.  This proves outcome 1.

## Failure of root-splittability and the separator lift

Let both root portal sets of `Q_i` equal `{q}`, and suppose a component `W`
of `Q_i-q` exists.  No vertex of `W` is adjacent to `d` or `e`.  Because
`W` is a component after deleting `q`, every neighbour of `W` in
`Q_i-W` is `q`; and because `Q_i` is a component of `G-S`, there are no
edges from `W` to either of the other open components.  Therefore

```text
N_G(W) subseteq (S-{d,e}) union {q},
```

a seven-vertex set.

This is a genuine separation boundary, not merely a local cut: `W` is
nonempty, while `d,e` and both other components of `G-S` lie outside
`W union N_G(W)`.  Seven-connectivity excludes a smaller neighbourhood
and hence forces `|N_G(W)|=7`, proving outcome 2.  If that outcome is
absent, `Q_i-q` is empty and `Q_i` is the singleton `{q}`.

## Excluding two singleton components

If `Q_0,Q_1` are both singletons, give the four independent boundary
blocks four distinct colours.  The prescribed closed-`C` colouring uses
exactly those four boundary colours, up to a permutation.  Give both
singleton components one of the two colours absent from the boundary.
They are anticomplete to each other and have neighbours only in `S`, so
this extends to a proper six-colouring of `G`.  Thus, absent outcomes 1 and
2, at most one and at least one of `Q_0,Q_1` is a singleton.

## Trust boundary

The result is an unbounded reduction: it imposes no order bound on either
full component.  It does not colour the surviving non-singleton component
with the four-block partition, allocate the remaining boundary-class
connector in `C`, or make the returned order-seven separation
colour-compatible.  The theorem accurately confines its conclusion to the
three-component two-cut response normal form.

Within that scope, no gap was found.
