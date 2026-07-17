# The Gallai--Edmonds set need not meet a named support-six model

**Status:** written barrier to an intermediate claim, with a checkable
treewidth certificate.  This is not a counterexample to `HC_7`.

This example tests whether the canonical Gallai--Edmonds set on the
eight-vertex boundary of the two-edge contraction residue can itself be
used as the next pair in the support-height argument.  It shows that the
boundary decomposition, two full connected shores, two disjoint named
support-six `K_5` models, and global `K_7`-minor exclusion do not suffice.
Seven-connectivity, the seven-connected one-edge predecessors, or
contraction-critical colouring transitions must be used by any positive
theorem.

## 1. The graph

Let `G` have vertex set `{0,1,...,11}` and edge set

```text
01 08 0A
14 17 19 1A
25 26 27 28 2A
35 36 37 38 3A 3B
45 46 47 48 49 4A
56 57 58 5B
67 69 6A 6B
78 79 7A
89
AB
```

Here `A=10` and `B=11`; the hexadecimal-style notation is used only to
keep the edge list compact.

Put

\[
 S=\{0,1,\ldots,7\},\qquad
 C=\{8,9\},\qquad D=\{10,11\}.
\]

Then `C` and `D` are connected, there is no `C`--`D` edge, and every
vertex of `S` has a neighbour in each of `C,D`.  Thus `(C,S,D)` is an
actual order-eight two-shore interface of the same geometric kind as the
expanded two-edge contraction residue.

The graph has two vertex-disjoint six-vertex `K_5` models:

\[
\begin{aligned}
 \mathcal M_1 &: \{4\},\{7\},\{8\},\{9\},\{0,1\},\\
 \mathcal M_2 &: \{3\},\{6\},\{10\},\{11\},\{2,5\}.
\end{aligned}
\]

Indeed, `G[{4,7,8,9}]` and `G[{3,6,10,11}]` are cliques, `01` and
`25` are edges, and each displayed edge branch set is adjacent to every
singleton branch set in its row.  The two models partition `V(G)`.

Contracting `01` and `25` replaces the order-eight boundary by an
order-six boundary and leaves `C,D` as two full components.  The example
therefore retains the labelled expansion geometry.  It does not retain
the connectivity/minimality hypotheses of the actual minimal-bad
contraction theorem.

## 2. The canonical Gallai--Edmonds set

Let `J=G[S]` and `F=\overline J`.  The boundary edge set is

```text
01 14 17 25 26 27 35 36 37 45 46 47 56 57 67.
```

The complement has edge set

```text
02 03 04 05 06 07
12 13 15 16
23 24 34.
```

Its maximum matching number is three.  Every maximum matching saturates
`0` and `1`: after deleting either one, at most one edge can be taken from
the triangle on `{2,3,4}` and at most one further edge can meet the
remaining vertex in `{0,1}`.  Conversely, each vertex in
`{2,3,4,5,6,7}` is missed by a matching of order three; explicit examples
are

```text
miss 2: 07,15,34
miss 3: 07,15,24
miss 4: 07,15,23
miss 5: 07,16,23
miss 6: 07,15,23
miss 7: 04,15,23.
```

Consequently the Gallai--Edmonds decomposition of `F` is

\[
 D_F=\{2,3,4,5,6,7\},\qquad A_F=\{0,1\},\qquad C_F=\varnothing.
\]

Moreover, `F[D_F]` is the disjoint union of the triangle on `{2,3,4}`
and the three singleton components `{5},{6},{7}`.  This is precisely the
canonical case

\[
                 (|A_F|,o(F-A_F))=(2,4).
\]

But the canonical pair `A_F={0,1}` is disjoint from every branch set of
`\mathcal M_2`.  It therefore does not meet every support-at-most-six
`K_5` model.

## 3. A hand-checkable `K_7`-minor exclusion

The following elimination order has filled later-neighbour sets of order
at most five:

```text
vertex   filled later neighbours
0        1,8,10
11       3,5,6,10
1        4,7,8,9,10
2        5,6,7,8,10
3        5,6,7,8,10
5        4,6,7,8,10
4        6,7,8,9,10
6        7,8,9,10
7        8,9,10
8        9,10
9        10
10       -
```

Adding the fill edges at each elimination step gives a chordal completion
with largest clique of order six.  Hence `tw(G)<=5`.  Treewidth is
minor-monotone and `tw(K_7)=6`, so `G` has no `K_7` minor.

The two named singleton cores therefore do not force a `K_7` minor, even
when they coexist with the canonical Gallai--Edmonds decomposition and a
full order-eight two-shore interface.

## 4. Exact scope

This example has twelve vertices, the minimum possible order for two
vertex-disjoint support-six models.  No edge-minimality claim is made.

It is not seven-connected: vertex `0` has degree three.  It is not asserted
to be seven-chromatic or contraction-critical, and the one-edge
predecessor contractions are not asserted to be seven-connected.  Thus it
does not refute a theorem using the full hypotheses of a hypothetical
minor-minimal `HC_7` counterexample.

It does refute the boundary-only implication

> canonical Gallai--Edmonds set of order two + two full shores + two
> disjoint named support-six models + `K_7`-minor exclusion
> implies that the canonical set meets every support-at-most-six model.

The next positive exchange must use seven-connectivity at the level of
individual vertices, predecessor connectivity, or proper-minor colouring
transitions; the canonical matching decomposition and named cores alone
cannot supply the new maximal pair.
