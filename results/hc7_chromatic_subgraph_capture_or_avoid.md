# Chromatic subgraph alignment or separation by a dominating `K_5` model

**Status:** written proof. This is a new deduction from Lemma 2.1 and
Lemma 2.2 of Girão--Illingworth--Mohar--Norin--Steiner--Tamitegama--Tan--
Wood--Yip, *The Dominating 4-Colour Theorem*
([arXiv:2605.10112](https://arxiv.org/abs/2605.10112)). It is not a proof
of `HC_7`.

## 1. External input

A **dominating `K_5` model** in a graph `H` is an ordered tuple
`(T_1,...,T_5)` of pairwise vertex-disjoint connected subgraphs such that,
whenever `i<j`, every vertex of `T_j` has a neighbour in `T_i`.

For an ordered clique `L=(v_1,...,v_k)`, where `k<=2`, the cited paper
calls such a model **`L`-compatible** when

- `v_i` is unused or belongs to one of `T_1,...,T_i`; and
- if `k=2` and `v_2` belongs to `T_2`, then `v_1` belongs to `T_1`.

Its Lemma 2.1 states that every graph is either four-colourable or contains
an `L`-compatible dominating `K_5` model. Its Lemma 2.2 shows that this
compatibility lifts through contraction of a connected subgraph containing
the first member of `L`, and through contraction of a connected subgraph
containing the second member when every vertex of that subgraph has a
neighbour in the first.

## 2. One connected subgraph

### Theorem 2.1 (alignment, marked avoidance, and separation)

Let `r>=1`, let `G` be a graph with `chi(G)>=r+4`, and let `X` be a
nonempty connected induced subgraph of `G` with `chi(X)<=r`. At least one
of the following holds:

1. `G` has a dominating `K_5` model `(T_1,...,T_5)` with
   `V(X) subseteq V(T_1)`;
2. for every vertex `w` outside `X` with a neighbour in `X`, the graph
   `G-(V(X) union {w})` has a dominating `K_5` model.

If the first outcome fails, then for each such `w` the model in the second
outcome can be chosen so that `V(T_2) union ... union V(T_5)` separates
`X` from `T_1` in `G`.

#### Proof

Contract `X` to one vertex `x`, and call the resulting graph `Q`. The graph `Q` is not
four-colourable. Indeed, in a four-colouring of `Q`, one colour class of an
`r`-colouring of `G[X]` can reuse the colour of `x`: every outside neighbour
of `X` is adjacent to `x` in `Q` and therefore avoids that colour. Give the
other at most `r-1` classes fresh colours. This would colour `G` with at
most `r+3` colours, contrary to `chi(G)>=r+4`.

Suppose the first outcome fails, and fix any `w` outside `X` adjacent to
`X`. Choose a vertex `v_1` of `X` adjacent to `w`, and track the ordered
edge `(v_1,w)` through the contraction. Its image in `Q` is the ordered
edge `(x,w)`. Apply the external input to that edge.

If the compatible model uses `x`, then `x` lies in its first branch set;
uncontracting `X` gives the first outcome, contrary to the supposition.
Suppose instead that the model omits `x`. Compatibility then prevents `w`
from lying in the second branch set. If `w` lies in the first branch set,
add the unused vertex `x` to that branch set along the edge `xw`, and then
uncontract `X`. Enlarging the first branch set cannot destroy a domination
relation, so this again gives the first outcome. Therefore `w` is also
omitted. The model consequently lies in `Q-{x,w}`, which is the same graph
as `G-(V(X) union {w})`. Since `w` was arbitrary, outcome 2 follows.

Let `(T_1,...,T_5)` be the model obtained for a fixed `w`. If
`G-(V(T_2) union ... union V(T_5))` contains an `X`--`T_1` path, choose a
shortest one. Adding that path and `X` to `T_1` preserves connectedness,
disjointness from the other four branch sets, and every domination
relation. This gives the first outcome, a contradiction. Hence the stated
separation holds. `square`

The useful content is avoidance of an arbitrarily prescribed neighbour
`w`, the named first-branch alternative, and the four-branch-set separator
when alignment fails. At the sharp threshold `chi(G)=r+4`, the graph `G-X`
may be four-colourable, so ordinary unmarked regeneration does not imply
the theorem.

### Theorem 2.2 (normalized absorption or separator)

Under the hypotheses of Theorem 2.1, `G` has a dominating `K_5` model

`(T_1,T_2,T_3,{v},{w})`

such that `T_3 union {v,w}` induces a cycle and either

1. `X subseteq T_1`; or
2. the model avoids `X`, and
   `S=V(T_2) union V(T_3) union {v,w}` separates `X` from `T_1`.

#### Proof

Contract `X` to `x`. The colour-reuse argument from Theorem 2.1 shows that
the quotient is not four-colourable. Apply the external input to the
one-vertex ordered clique `(x)`. Compatibility puts `x` either in `T_1` or
outside the model. In the first case, lift the contraction to obtain the
first outcome.

In the second case, use the normalization recorded after the main theorem
of the cited paper: shrink the final branch sets so that the model has the
displayed form and `T_3 union {v,w}` induces a cycle. This operation still
avoids `x`. If `x` and `T_1` lie in one component of the graph obtained by
deleting `S`, add that entire component to `T_1` and then lift `X`; this
gives the first outcome. Otherwise `S` gives the second outcome after
lifting. `square`

## 3. Two connected subgraphs

### Theorem 3.1 (nested two-subgraph alignment)

Let `r_1,r_2>=1`, let `G` satisfy
`chi(G)>=r_1+r_2+3`, and let `X,Y` be disjoint nonempty connected induced
subgraphs such that

1. `G[X]` is `r_1`-colourable and `G[Y]` is `r_2`-colourable; and
2. every vertex of `Y` has a neighbour in `X`.

Then `G` has a dominating `K_5` model `(T_1,...,T_5)` with one of the
following forms:

1. all five branch sets avoid `X union Y`; or
2. `X subseteq T_1`, while `Y` is wholly unused, wholly contained in
   `T_1`, or wholly contained in `T_2`.

If no model of the second form exists, the first form can be chosen so that
`T_2 union ... union T_5` separates `X union Y` from `T_1`.

#### Proof

Choose an edge `v_1v_2` with `v_1` in `X` and `v_2` in `Y`. Contract `X`
to `x` and then `Y` to `y`, tracking the ordered edge `(v_1,v_2)` to
`(x,y)`. The final quotient is not four-colourable. In a four-colouring of
the quotient, colour one class of `G[X]` with the colour of `x` and one
class of `G[Y]` with the colour of `y`; use pairwise disjoint fresh palettes
of orders at most `r_1-1` and `r_2-1` on the remaining classes. This would
colour `G` with at most `r_1+r_2+2` colours.

Apply the external input to the ordered edge `(x,y)`. Compatibility leaves
only the index pairs

`(0,0), (0,1), (1,0), (1,1), (1,2)`.

For `(0,0)` the model avoids both sets. In case `(0,1)`, add `x` to the
first branch set along `xy`. In all other nonzero cases `x` is already in
the first branch set. First lift the contraction of `Y` using Lemma 2.2(b)
in the graph where `X` is still contracted, and then lift `X` using
Lemma 2.2(a). The pointwise assumption that every vertex of `Y` has a
neighbour in `X` is exactly the neighbourhood hypothesis of Lemma 2.2(b);
it preserves domination when `Y` becomes the second branch set in case
`(1,2)`. This gives the two listed forms.

The final separator assertion follows by the same shortest-path absorption
argument as in Theorem 2.1, now applied to the connected set `X union Y`.
`square`

## 4. Consequence for seven-chromatic graphs

### Corollary 4.1

Let `G` be seven-chromatic and let `X` be a nonempty connected induced
three-colourable subgraph. Then either a dominating `K_5` model of `G`
contains all of `X` in its first branch set, or, for every `w` outside `X`
adjacent to `X`, the graph `G-(V(X) union {w})` contains a dominating
`K_5` model.
In the latter case the union of the final four branch sets can be chosen as
an `X`--`T_1` separator. In a seven-connected graph that union has at least
seven vertices; equality is an actual separation of order seven.

This applies in particular to every induced path or induced odd cycle. It is a label-aware
regeneration theorem: a prescribed path is either retained intact in a
named branch set or can be avoided together with any one chosen adjacent
vertex. Theorem 3.1 applies at chromatic number seven to two connected
bipartite subgraphs satisfying its pointwise adjacency hypothesis.

The pointwise hypothesis in Theorem 3.1 is essential to the lifting
argument. It cannot be replaced by the assertion that two branch sets of a
near-`K_7` model have one edge between them. Neither theorem by itself
splits the first branch set, aligns the other four branch sets with a
pre-existing near-`K_7` model, or produces a `K_7` minor.

### Corollary 4.2 (two omitted nonadjacent vertices)

Let `G` be seven-connected and seven-chromatic, let `a,b` be nonadjacent
vertices, and suppose `J=G-{a,b}` is six-chromatic. Let `X` be a nonempty
connected induced bipartite subgraph of `J`. Then either

1. a dominating `K_5` model of `J` contains all of `X` in its first branch
   set; or
2. for every `w` in `N_J(X)`, the graph `J-(V(X) union {w})` contains a
   dominating `K_5` model whose last four branch sets separate `X` from its
   first branch set in `J`.

In the second outcome, let `E` be the component of `J-S` containing
`T_1`, and put

`R_E={r in {a,b}: r has a neighbour in E}`.

Then `S union R_E` separates `E` from `X` in `G`. Consequently
`|S|+|R_E|>=7`, and equality gives an actual separation of order seven.
In particular `|S|>=5`; the case `|S|=5` is terminal because then both
roots must belong to `R_E`.

The model may instead be chosen in the normalized form of Theorem 2.2. In
that form `S=T_2 union C`, where `C` is an induced cycle, every vertex of
`S` has a neighbour in `T_1`, and every vertex of `C` has a neighbour in
`T_2`.

#### Proof

Apply Theorem 2.1 to `J` with `r=2`. The set `S` separates `E` from `X`
inside `J`. In `G-(S union R_E)`, neither root outside `R_E` has a neighbour
in `E`, so no path can leave `E`. Thus `S union R_E` is a proper separator.
Seven-connectivity gives the displayed inequality, and equality is
precisely an order-seven separation. `square`

Under the hypotheses of Corollary 4.2, in the singleton-root near-`K_7`
setting choose in
`G[{a,b} union V(B_i)]` a shortest `a`--`b` path through any one of the
other five branch sets. Because `a,b` are nonadjacent, its internal
vertices form a nonempty induced path `X` lying in `J`. The corollary aligns
that path with one named branch set or returns the structured separator; it
does not yet align the other four branch sets with the pre-existing model.
