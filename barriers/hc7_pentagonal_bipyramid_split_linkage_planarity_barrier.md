# Local split and adjacent-rim linkage tests do not characterize planarity

**Status:** barrier/counterexample to an intermediate structural theorem;
computer-assisted finite checks are reproduced by
[`hc7_pentagonal_bipyramid_split_linkage_planarity_barrier_verify.py`](hc7_pentagonal_bipyramid_split_linkage_planarity_barrier_verify.py).

This fourteen-vertex example is five-connected and nonplanar.  It is an
expansion of the pentagonal bipyramid into seven induced two-vertex paths,
but it has neither a four-label alternating path cut nor any of the five
adjacent-rim linkages from the audited linkage-completion theorem.

It is not a counterexample to the desired rooted-model theorem: it contains
an explicit anchored `K_5` model obtained by splitting two columns between
different branch sets.  Thus it identifies a missing global mechanism.

## 1. Claim refuted

The following statement is false.

> Let `F` be a five-connected graph partitioned into seven induced path
> columns whose contact graph is the pentagonal bipyramid.  Then at least
> one of the following holds:
>
> 1. an internal path edge separates four distinct old neighbour labels in
>    alternating cyclic order;
> 2. an adjacent pair of rim columns contains the two disjoint connected
>    subgraphs in the adjacent-rim linkage-completion theorem;
> 3. `F` is planar.

Equivalently, adding “or a cut of order at most four” does not repair the
claim.

## 2. Construction

Use labels `0,1` for the two poles and `2,3,4,5,6` for the cyclic rim.  For
each label `x`, let

\[
                         C_x=\{x_0,x_1\},
\]

and add the internal edge `x_0x_1`.  The remaining edges are listed below;
each row `xi-yj` denotes `x_i y_j`.

```text
10-21
00-41
30-40 31-40 31-41
10-50 11-50 11-51
00-31
10-40
01-60 01-61
20-30 20-31 21-30
00-20 00-21 01-20 01-21
40-50 41-50 41-51
21-60
51-61
01-51
10-60 10-61 11-60 11-61
10-30
```

There are no other edges.  Direct inspection shows that two columns
contact exactly when their labels are adjacent in the pentagonal
bipyramid.

The degrees, in the order

```text
00 01 10 11 20 21 30 31 40 41 50 51 60 61
```

are

```text
5 6 7 5 5 6 5 5 5 5 5 5 5 5.
```

The verifier checks every deletion of at most four vertices and confirms
that the remaining graph is connected.  Since the minimum degree is five,
this proves that the connectivity is exactly five.

## 3. No alternating path cut

The cyclic neighbour order and the labels seen by the two ends of each
path column are as follows.

| column | cyclic order | labels at `x_0` | labels at `x_1` |
|---|---|---|---|
| `0` | `2,3,4,5,6` | `2,3,4` | `2,5,6` |
| `1` | `2,6,5,4,3` | `2,6,5,4,3` | `6,5` |
| `2` | `0,3,1,6` | `0,3` | `0,3,1,6` |
| `3` | `0,4,1,2` | `4,1,2` | `0,4,2` |
| `4` | `0,5,1,3` | `5,1,3` | `0,5,3` |
| `5` | `0,6,1,4` | `1,4` | `0,6,1,4` |
| `6` | `0,2,1,5` | `0,2,1` | `0,1,5` |

Checking the four cyclic positions at a rim column, and the five choices
of four positions at a pole, shows that no two labels on one side alternate
with two labels on the other.  The verifier performs this check directly.

## 4. All five adjacent-rim linkages fail

For each adjacent rim pair `C_i,C_{i+1}`, the verifier enumerates every
assignment of its four vertices to two disjoint sets `X,Y` or to neither
set.  It checks connectedness and the four required portal contacts.  No
assignment gives both

\[
 E(X,C_0),E(X,C_1),E(Y,C_{i-1}),E(Y,C_{i+2})\ne\varnothing.
\]

Thus every one of the five set-terminal Two Paths instances from the
linkage-completion theorem is negative.

## 5. Explicit nonplanarity certificate

The graph contains a subdivision of `K_{3,3}` with bipartition

\[
 \{4_0,5_1,6_0\}\quad\hbox{and}\quad\{4_1,5_0,6_1\}.
\]

Six of its nine paths are the literal edges

\[
 4_04_1,\ 4_05_0,\ 5_14_1,\ 5_15_0,\ 5_16_1,\ 6_06_1,
\]

and the remaining three are

\[
 4_0-3_0-1_0-6_1,
 \qquad
 6_0-2_1-2_0-3_1-4_1,
 \qquad
 6_0-1_1-5_0.
\]

Their interiors are pairwise disjoint and avoid the six branch vertices.
Hence `F` is nonplanar.

## 6. The global rooted-model mechanism

The five sets

\[
\begin{aligned}
 B_0&=\{6_0,6_1\},\\
 B_1&=\{4_0,4_1,2_1,0_0\},\\
 B_2&=\{3_0,3_1,2_0,0_1\},\\
 B_3&=\{1_0,1_1\},\\
 B_4&=\{5_0,5_1\}
\end{aligned}
\]

are connected and pairwise adjacent.  They are an explicit `K_5`-minor
model.  Respectively, they contain the whole distinct columns

\[
                         C_6,C_4,C_3,C_1,C_5.
\]

The two unused columns `C_0,C_2` are split between `B_1,B_2`.  This is the
feature missed by every one-column alternating test and every adjacent-rim
linkage test.

## 7. Consequence and trust boundary

A correct structural theorem needs a global alternative that permits
simultaneous splitting and absorption of several columns.  Portal orders
or Two Paths tests confined to one column or one adjacent rim pair are not
complete, even at connectivity five.

This graph is only a five-connected core.  It is not asserted to be
five-chromatic, to arise from operation-specific proper-minor colourings,
or to lift to a seven-contraction-critical host.  It therefore does not
refute a theorem using those dynamic hypotheses, and it is positive rather
than negative evidence for a global anchored-`K_5` theorem.
