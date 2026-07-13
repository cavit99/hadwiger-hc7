# Superseded audit: HC7 exact-seven Moser four-corner exchange

Audited file: `active/hc7_exact7_moser_multiframe_exchange.md`  
Verdict on Lemma 2.1, the exact-state theorem, and new Theorem 4.1:
**GREEN**.

The strengthened Theorem 4.1 removes the former common-embedding gap for
every order-at-least-four three-connected shore.  It applies the audited
four-port theorem once to the literal roots `1,2,3,4`; no favourable
five-root crossing and no composition of several rural pages is used.

## 1. What is actually proved

Under the literal carrier hypothesis

\[
X\leftrightarrow\{a,y\},\qquad
Y\leftrightarrow\{x,b\},\qquad E(X,Y)\ne\varnothing,
\]

where `X,Y` are disjoint connected subgraphs of the open shore `D`, the
argument correctly constructs matching equality states on the two closed
shores and hence a six-colouring of `G`.

The known wheel-society counterarchitecture does not refute this statement.
It only refutes an inference from the signs of separately chosen path pairs.
The theorem additionally uses minor-critical six-colourings of two specific
proper minors.

## 2. First proper minor and its boundary trace

Put `r={a,y}` and `e={x,b}`.  Both are independent because the pure Moser
boundary has no `L`--`R` edge.

The sets `v+r` and `C+e` are connected and disjoint.  The second is connected
because `C` is connected and `S`-full.  They are adjacent through the edges
from `v` to `e`, so their representatives receive different colours.

Pulling a six-colouring back only to `G[D\cup S]` is legitimate, even though
the contracted sets themselves contain edges: their intersections with that
closed shore are respectively the independent sets `r` and `e`.  This
shore-restricted pullback point should be retained explicitly in any final
proof.

Every vertex of `S-r` has a boundary edge to `r`, and every vertex of `S-e`
has a boundary edge to `e`.  Explicitly, the other `L` vertex sees the chosen
`L` vertex through `12`, the other `R` vertex sees the chosen `R` vertex
through `34`, `0` sees all four corners, `5` sees both `R` vertices, and `6`
sees both `L` vertices.  Thus neither representative colour can occur on
`{0,5,6}`.  Since `56` is an edge and `05,06` are nonedges, the three possible
literal equality partitions are exactly

\[
R_0=\{r,e,0,5,6\},\quad
R_5=\{r,e,05,6\},\quad
R_6=\{r,e,06,5\}.
\]

There is no omitted fourth case: `0` cannot share both colours because `5`
and `6` have distinct colours.

## 3. Opposite-shore realization

The contraction sets `X+r`, `Y+e`, and `v+I_q` are pairwise disjoint and
connected.  The first two are adjacent by `E(X,Y)\ne\varnothing`.

Each carrier representative sees `5` through its `R` corner and `6` through
its `L` corner.  The star representative sees every remaining boundary
representative through `v`, and `56` is literal.  Hence the five
representatives for `q=0` form a `K_5`, and the four representatives for
`q=5,6` form a `K_4`.

Again, the pullback only to `G[C\cup S]` is proper: the intersections of the
three contracted sets with this closed shore are the independent sets `r`,
`e`, and `I_q`.  Adjacency to the representative of every other block rules
out unintended equality.  The resulting boundary state is exactly `R_q`.

All three contractions are proper minors because the opposite open shore
`C` is nonempty and the displayed contractions reduce vertices.

## 4. Gluing

The two shore colourings induce the same literal equality partition on `S`.
A palette permutation therefore aligns their colours block by block.  Since
`C` and `D` are anticomplete, the aligned colourings glue on `G-v`.  At most
five colours occur on `S`, leaving a sixth colour for `v`.  This contradicts
seven-contraction-criticality.

## 5. Literal rural-disk extraction

The newly inserted Lemma 2.1 correctly derives (2) once the **literal** disk
embedding of `Q=G[D\cup{a,x,b,y}]` with boundary order `a,x,b,y` is given.
Its separator argument proves the two portal-union ranks are at least two;
the literal edges `ax=12` and `by=34` then give a two-connected closure by
the audited two-ear lemma.  The outer face is consequently a cycle, its two
consecutive nonedge arcs have disjoint nonempty interiors in `D`, and a
shortest connecting path in connected `D` enlarges one carrier so the two
become adjacent.  This handles overlapping raw portal sets after a literal
disk embedding has been obtained.

Thus a literal disk from the four-port theorem gives the carrier hypothesis
without any unsafe inference from abstract portal order.

## 6. Audit of Theorem 4.1

Take `S=N(v)`.  Since `G-N[v]` has the two nonempty components `C,D`, the
graph `G-S` has `D` as a component and has a nonempty far side containing
`C` and `v`.  Fullness of `D` supplies neighbours of all four distinct
roots `1,2,3,4`.  These are exactly the hypotheses of the already audited
seven-boundary four-port theorem in
`results/hc7_moser_crossing_carrier.md`, Theorem 4.1.

### Linkage outcome

For ordered roots `1,2,3,4`, the alternating linkage consists of disjoint
`1-3` and `2-4` paths with interiors in `D`.  Both interiors are nonempty:
`13` and `24` are literal nonedges of the pure Moser boundary.  Their
interiors are disjoint nonempty connected sets.  A shortest path between
them in connected `D`, truncated at its first and last hits, can be added
to one set except for the final endpoint; this preserves disjointness and
all four root contacts and creates an edge between the enlarged carriers.

The substitution

```
(a,x)=(1,2),  (b,y)=(4,3)
```

is legal and gives `r={1,3}`, `e={2,4}`.  Hence these linkage carriers are
exactly hypothesis (2), and the GREEN exact-state theorem applies.

### Rural outcome

The four-port theorem returns the literal graph
`G[D\cup{1,2,3,4}]` in a disk with boundary order `1,2,3,4`; it is not
merely an order on selected or overlapping portal representatives.  With
`(a,x,b,y)=(1,2,3,4)`, Lemma 2.1 produces adjacent disjoint carriers for
`{1,4}` and `{2,3}`.  These are the other perfect matching of the two
left and two right corners, so the exact-state theorem again applies.

The four-port outcomes are exhaustive.  Therefore every full open shore of
order at least four which is three-connected is impossible in this Moser
two-component cell.

## 7. Perfect-matching state check

The Section 3 proof does not depend on which of the two cross perfect
matchings was returned.  For any cross pair `r={l,r'}` and its complementary
cross pair `e`, both are independent and each dominates every boundary
vertex outside itself: use `12` within the left pair, `34` within the right
pair, the four `0` edges, the two right-to-`5` edges, and the two
left-to-`6` edges.  Each carrier therefore sees `5` through its right corner
and `6` through its left corner.  This verifies all representative-clique
and exact-trace claims uniformly for `(13|24)` and `(14|23)`.

## 8. Revised trust boundary

The wheel-society barrier remains a valid warning against a theorem based
only on independently selected frame signs, but it is irrelevant to
Theorem 4.1.  The strengthened argument invokes the literal four-port
linkage-or-disk theorem once and then spends the proper-minor exact-state
transition.

This theorem does **not** by itself close tiny open shores of order at most
three, shores not reduced to internal three-connectivity, the sole-exterior
Moser cell, or the other degree-seven boundary types.  Those are separate
dependencies.  Within its stated order-at-least-four three-connected
two-component Moser family, however, there is no remaining multi-frame or
favourable-crossing assumption.
