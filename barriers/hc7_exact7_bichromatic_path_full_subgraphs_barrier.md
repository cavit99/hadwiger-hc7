# Barrier: a boundary bichromatic path need not augment two boundary-full subgraphs

**Status:** explicit finite counterexample to a local exchange principle, with
a deterministic verifier.  This is not a counterexample to `HC_7`.

The graph below is six-connected and `K_7`-minor-free.  It has an actual
seven-vertex separation, the exact boundary-colouring pattern occurring in
the outer-edge branch of the critical-triangle transition, two disjoint
connected subgraphs adjacent to every boundary vertex, and the forced
bichromatic path supplied by a demand-critical singleton merge.  The path
runs directly through the two selected subgraphs and supplies neither a
third boundary-full connected subgraph in the same open shore, disjoint from
the selected pair, nor a smaller selected pair.

Thus the path and the two full subgraphs are not three independent resources.
Any positive exchange theorem must use a hypothesis absent here, such as
seven-connectivity together with `K_7`-minor exclusion, or the incompatible
proper-minor colouring responses of a hypothetical counterexample.

The graph is the one in the audited
[first-entry minimality barrier](hc7_first_entry_packet_minimality_barrier.md),
but with a different six-colouring.  The new colouring places that graph
inside the exact critical-triangle boundary family.

## 1. Graph and separation

Let

\[
 S=\{0,1,2,3,4,5,6\},\qquad
 A=\{a_1,a_2,c_1,c_2\},\qquad B=\{b\}.
\]

The boundary contains the cycle

\[
 01,12,23,34,45,56,60
\]

and the two chords `02,13`.  The open side `A` induces the path

\[
                       a_1a_2c_1c_2.                  \tag{1.1}
\]

There are no `A-B` edges, and `b` is adjacent to every member of `S`.
The boundary neighbourhoods on the four-vertex side are

\[
\begin{array}{c|c}
a_1&\{0,1,4,5,6\},\\
a_2&\{2,3,4,5\},\\
c_1&\{0,2,5,6\},\\
c_2&\{1,2,3,4,5,6\}.
\end{array}                                             \tag{1.2}
\]

These rules define the graph.  In particular, `S` is the literal boundary
of a separation with open sides `A` and `B`.

Put

\[
                  P_1=G[\{a_1,a_2\}],\qquad
                  P_2=G[\{c_1,c_2\}].                 \tag{1.3}
\]

Both are connected, are adjacent through `a_2c_1`, and are adjacent to
every vertex of `S`.  No singleton in `A` is boundary-full.  Exhaustion of
connected subsets shows that `P_1,P_2` are the only inclusion-minimal
boundary-full connected subgraphs in `A`.  Consequently the maximum number
of pairwise disjoint such subgraphs is two, and every such pair has total
order at least four.

## 2. Exact outer-edge boundary colouring and forced path

Give the boundary the colours

\[
\begin{array}{c|ccccccc}
s&0&1&2&3&4&5&6\\ \hline
\gamma(s)&4&0&1&4&2&4&3.
\end{array}                                             \tag{2.1}
\]

Thus the equality partition on `S` is

\[
       \{0,3,5\}\mid\{1\}\mid\{2\}\mid\{4\}\mid\{6\}. \tag{2.2}
\]

This is exactly the `(3,1,1,1)` outer-edge pattern of the
critical-triangle transition:

* take the distinguished singleton to be `v=1`;
* the colour `5` is absent from `S`;
* the remaining singleton vertices are `2,4,6`;
* with `x=4` and `y=6`, the pair `xy` is a nonedge; and
* the two singleton vertices left after merging `x,y` are `1,2`, which are
  adjacent.

The singleton graph on `Q=\{1,2,4,6\}` is a single edge `12`, so it is
triangle-free.  The exact packet demand in the terminology of the promoted
critical-triangle theorem is

\[
                  5-\omega(G[Q])=5-2=3>2.             \tag{2.3}
\]

Extend (2.1) over the closed side `G[A\cup S]` by

\[
 \gamma(a_1)=1,\qquad \gamma(a_2)=3,\qquad
 \gamma(c_1)=2,\qquad \gamma(c_2)=5.                  \tag{2.4}
\]

Then

\[
                         4-a_2-c_1-6                  \tag{2.5}
\]

is a path with colour sequence `2,3,2,3`.  No other boundary vertex has
either of these two colours.  Hence (2.5) is precisely the literal
bichromatic path returned when the singleton merge `\{4\},\{6\}` is
blocked.

The internal vertices of (2.5) lie respectively in `P_1` and `P_2`.
Moreover `A=P_1\cup P_2`.  The path therefore gives no connected subgraph
in `A` disjoint from the selected pair, and no third boundary-full connected
subgraph exists in that open shore.  Since `P_1,P_2` already have minimum
possible total order, deleting an entry vertex cannot produce a smaller
full pair.

Giving `b` colour `5` produces a proper colouring of the whole graph.  This
last fact is part of the trust boundary: the example does not model the
incompatible extension languages of a hypothetical counterexample.

## 3. Connectivity and minor exclusion

The graph has twelve vertices, thirty-eight edges, and vertex connectivity
six.  It is `K_7`-minor-free.  Both statements are checked exhaustively by
the verifier: connectivity is tested under every deletion of at most five
vertices, and `K_7`-minor exclusion is tested over all spanning partitions
into seven nonempty connected branch sets.  Spanning is without loss in a
connected host, because every unused component can be absorbed along a
path into an existing branch set.

The missing connectivity unit is essential for this skeleton.  Consider
every absent edge whose addition simultaneously preserves

1. the separation, by forbidding `A-B` edges;
2. the colouring (2.1)--(2.4), by forbidding equal-colour endpoints;
3. the nonedge `46`; and
4. triangle-freeness of `G[Q]`.

There are seventeen admissible edges.  The verifier enumerates every
inclusion-minimal subset whose addition makes the graph seven-connected.
The census is

\[
\begin{array}{c|rrrr|r}
\text{number of added edges}&4&5&6&7&\text{total}\\ \hline
\text{minimal seven-connected augmentations}&2&66&89&8&165.
\end{array}                                             \tag{3.1}
\]

An exact connected-partition search finds a `K_7` minor in every one of
the 165 augmented graphs.  Every admissible seven-connected supergraph
contains one of these inclusion-minimal augmentations, so the census proves:

> **Fixed-skeleton completion certificate.** Every edge augmentation of
> this graph which preserves the displayed separation and colouring, keeps
> `46` absent and `G[Q]` triangle-free, and raises connectivity to seven,
> contains a `K_7` minor.

This finite statement is not promoted to an unbounded exchange theorem.
It records that the nearest completion of the obstruction is terminal,
rather than furnishing a seven-connected counterexample.

## 4. Exact trust boundary

The example satisfies:

* an actual separator of order seven with both open sides nonempty;
* the exact residual outer-edge boundary equality pattern;
* two disjoint, adjacent, boundary-full connected subgraphs;
* the demand-critical bichromatic singleton path;
* six-connectivity; and
* `K_7`-minor exclusion.

It deliberately fails the following hypotheses of the active `HC_7`
programme:

1. it is six-connected, not seven-connected;
2. it is colourable (indeed the displayed partition extends across both
   closed sides), rather than seven-chromatic;
3. the displayed partition extends over both closed shores (indeed over the
   whole graph), so the example does not model the incompatible boundary
   responses required in a hypothetical counterexample; and
4. it is not asserted to arise from an actual critical-triangle Kempe
   component--only its boundary colouring has the exact required form.

Accordingly it refutes only the unconditional geometric implication

\[
 \text{forced bichromatic path + two boundary-full connected subgraphs in one shore}
 \Longrightarrow
 \text{a third disjoint boundary-full subgraph in that shore or strict geometric peel}.
\]

The surviving positive theorem must spend seven-connectivity and the
host's proper-minor colouring dynamics at the direct entry.  The audited
first-entry reduction already shows what happens away from direct entry:
a failed absorption yields a connected residual piece with at most four
boundary neighbours and at least three distinct attachments to the two
selected subgraphs.

## 5. Verification

Run

```text
python3 barriers/hc7_exact7_bichromatic_path_full_subgraphs_barrier_verify.py
```

Expected output:

```text
GREEN exact-seven bichromatic-path/full-subgraph barrier
base: vertices=12 edges=38 connectivity=6 K7_minor=no demand=3
augmentations: allowed_edges=17 minimal_7_connected=165 all_have_K7=yes
augmentation_sizes: 4:2 5:66 6:89 7:8
```
