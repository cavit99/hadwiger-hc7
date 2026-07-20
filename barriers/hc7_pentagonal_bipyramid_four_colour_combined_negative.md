# A four-colourable combined-negative pentagonal-bipyramid core

**Status:** barrier/counterexample to an intermediate rooted-model claim;
computer-checked by
[`hc7_pentagonal_bipyramid_four_colour_combined_negative_verify.py`](hc7_pentagonal_bipyramid_four_colour_combined_negative_verify.py).

This fourteen-vertex graph is a five-connected nonplanar expansion of the
pentagonal bipyramid.  It has neither of the two previously isolated local
positive mechanisms and has no `K_5` model whose five branch sets contain
five distinct whole columns.  It is nevertheless four-colourable.  It also
has a `K_5` model aligned with the two literal endpoints of every paired
column, showing that **whole-column anchoring is strictly stronger than the
root alignment actually needed by the host proof**.  Thus the correct
global structural target must retain the chromatic terminal outcome

\[
             \chi(F)\le4\quad\text{or a root-aligned `K_5` model},
\]

rather than demand the rooted model from nonplanarity and five-connectivity
alone.

## 1. Claim refuted

The example refutes the following statement.

> Let a five-connected nonplanar graph be partitioned into seven connected
> columns whose contact graph is the pentagonal bipyramid.  If no column
> path has a four-label alternating cut and all five adjacent-rim Two Paths
> instances are negative, then the graph has a `K_5`-minor model whose five
> branch sets contain five distinct whole columns.

The whole-column condition is a robust sufficient condition for adjoining
the two external root branch sets.  Its failure does not say that every
possible placement of external root contacts fails.

## 2. Construction

Use labels `0,1` for the poles and `2,3,4,5,6` for the cyclic rim.  For
each label `x`, take the two-vertex path

\[
                            C_x=\{(x,0),(x,1)\}.
\]

In addition to the seven internal column edges, add the following thirty
intercolumn edges.  A word `aibj` denotes the edge `(a,i)(b,j)`.

```text
1021 0040 0041 0140 0141 3140
1050 0031 1140 1141 0060 2030
2031 2130 0020 4150 2060 2160
2161 5061 5160 5161 0051 0150
0151 1061 1030 1031 1130 1131
```

The contact graph of the seven columns is exactly the pentagonal
bipyramid.  The verifier checks that the resulting graph has order fourteen,
size thirty-seven, connectivity five, and is nonplanar.

## 3. Exact negative properties

Every column has only its displayed internal path edge.  Deleting that
edge gives its only connected two-part cut.  The verifier records which old
neighbour labels meet each endpoint and checks that no cut alternates on
four distinct labels in the planar cyclic order around the corresponding
pentagonal-bipyramid vertex.

For each pair of adjacent rim columns `C_i,C_(i+1)`, the verifier exhausts
all pairs of disjoint nonempty connected vertex subsets `X,Y` in their
four-vertex union.  None simultaneously satisfies

\[
 X\sim C_0,C_1,
 \qquad
 Y\sim C_{i-1},C_{i+2},
\]

where the first two columns are the poles and rim subscripts are cyclic.
Thus all five adjacent-rim linkage completions are negative.

Finally, the verifier chooses every five-column anchor set.  The four
vertices of the two unchosen columns are independently assigned to one of
the five prospective branch sets or left unused.  All

\[
                         {7\choose5}6^4=27,216
\]

possibilities are checked for connectedness and pairwise adjacency.  None
is a `K_5` model.  This is exhaustive for models in which each of the five
branch sets contains a different whole two-vertex column.

## 4. A paired-rooted model still exists

Suppose the first external root meets every vertex `(x,0)` and the second
meets every vertex `(x,1)`, as in the natural two-ended paired-column
model.  Then the following five sets form a `K_5` model:

\[
\begin{aligned}
 &\{(0,0),(0,1)\},\qquad
   \{(2,0),(2,1)\},\\
 &\{(1,0),(3,1)\},\qquad
   \{(5,0),(6,1)\},\\
 &\{(1,1),(3,0),(4,1)\}.
\end{aligned}                                                  \tag{4.1}
\]

Every set is connected and every two sets are adjacent.  Moreover, every
set contains at least one vertex with second coordinate zero and at least
one with second coordinate one.  Hence each is adjacent to both external
roots.  The verifier checks all these assertions.

This certificate is precisely why a whole-column search is not the right
test of the live model-meeting theorem.  A viable global theorem may split
several columns across branch sets while retaining literal adjacency to
both roots.

## 5. The chromatic terminal

The following is a proper four-colouring, with the value after each vertex:

```text
(0,0):0  (0,1):2  (1,0):3  (1,1):2
(2,0):2  (2,1):1  (3,0):0  (3,1):1
(4,0):3  (4,1):1  (5,0):0  (5,1):1
(6,0):3  (6,1):2
```

The vertices `(0,0),(0,1),(4,0),(4,1)` induce a `K_4`, so the chromatic
number is exactly four.

In the spanning root setup of the pentagonal-bipyramid core theorem, this
is already terminal: four-colour the core, give the two nonadjacent outer
vertices one new colour, and give their common adjacent vertex a sixth
colour.  Hence this finite graph cannot be the core of a hypothetical
minor-minimal counterexample to `HC_7`, whose core has chromatic number at
least five.

## 6. Trust boundary

The example does not refute a theorem whose alternatives include
four-colourability, a compatible order-seven separation, or an arbitrary
root-aligned model using the literal external attachment vertices.  In
fact (4.1) supplies the last outcome for the natural paired attachment.
It has no operation-selected proper-minor colouring data.  Its role is to rule out
the purely structural implication

\[
 \text{five-connected + nonplanar + the two local negative tests}
 \Longrightarrow
 \text{whole-column anchored `K_5`}.
\]

The sharpened unbounded target is instead to prove that a combined-negative
core is four-colourable, has a root-aligned `K_5` model, or exposes an
actual four-cut/compatible order-seven separation.  Contraction-critical
responses may be needed to prove that trichotomy, but they are not needed
to exclude this particular four-colourable graph.
