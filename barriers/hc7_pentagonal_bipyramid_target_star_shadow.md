# A seven-connected target-star shadow on the pentagonal bipyramid

**Status:** barrier/counterexample to two intermediate geometric claims;
computer-checked by
[`hc7_pentagonal_bipyramid_target_star_shadow_verify.py`](hc7_pentagonal_bipyramid_target_star_shadow_verify.py).
This graph is six-colourable and has order-seven separations.  It is not a
counterexample to `HC_7` or to a theorem retaining contraction-criticality
and an exact-seven compatible-separation outcome.

## 1. The claims refuted

Consider two adjacent connected root subgraphs, each adjacent to seven
pairwise disjoint connected **columns**, and suppose that the column-contact
graph is the pentagonal bipyramid.  The following conclusions do not follow
from seven-connectivity and exclusion of a `K_7` minor.

1. If one root has a distinguished target spoke, five labelled source spokes
   indexed by putative alternate colours, and one auxiliary spoke entering
   the seven distinct columns, then one source column must fail to contact
   the target column.
2. If a source and target are the two nonadjacent poles and a source--target
   path runs through one intermediate column, then that intermediate column
   necessarily admits the connected split used by the column-peeling
   construction.

The obstruction is literal rather than merely a seven-vertex quotient.
It realizes only this labelled spoke geometry, not the operation-specific
six-colouring from which the live response-star theorem obtains its labels.

## 2. Construction

Let `I` be the icosahedral graph on vertices `0,...,11`, with edge set

```text
01 05 07 08 0(11)
12 15 16 18
23 26 28 29
34 36 39 3(10)
45 46 4(10) 4(11)
56 5(11)
78 79 7(10) 7(11)
89
9(10)
10(11).
```

Adjoin adjacent vertices `v,w`, each complete to `I`, and call the resulting
graph

\[
                         G_0=K_2\mathbin\vee I.
\]

Inside `I` take the following seven connected columns:

\[
\begin{array}{c|c}
A_0&\{2\}\\
A_1&\{4\}\\
R_0&\{6\}\\
R_1&\{3\}\\
R_2&\{9,10\}\\
R_3&\{7,8,11\}\\
R_4&\{0,1,5\}.
\end{array}
\]

They partition `V(I)`.  Their contact graph has precisely the edges

\[
 A_iR_j\quad(i\in\{0,1\},\ j\in\mathbb Z_5),
 \qquad R_jR_{j+1}\quad(j\in\mathbb Z_5).
\]

Thus it is the pentagonal bipyramid: `A_0,A_1` are its nonadjacent poles
and `R_0,...,R_4` its rim cycle.  The singleton roots `{v},{w}` are adjacent
and are each adjacent to every column.

## 3. Target-pole obstruction

Use the edge from `v` to `A_0` as the target spoke, the five edges from `v`
to the rim columns as the five source spokes, and the edge from `v` to
`A_1` as the auxiliary spoke.  These seven edges enter seven distinct
columns.  Nevertheless `A_0` contacts all five source columns.  Its unique
nonneighbour is exactly the auxiliary column `A_1`.

Consequently the target-star geometry alone does not force a noncontact
source--target pair, even in a seven-connected `K_7`-minor-free host.

## 4. Atomic dirty-intermediate obstruction

Instead take `A_1` as one of the source columns and `A_0` as the target.
The path

\[
                            2-6-4
\]

joins them and its sole internal vertex is the entire intermediate column
`R_0={6}`.  This column has no nontrivial connected partition at all.
In particular it cannot be divided into a part retaining both root contacts
and the old column contacts and a second part contacting both missing
endpoint columns.  Thus a path with one dirty intermediate column need not
admit the proposed label-preserving peel.

## 5. Host properties and trust boundary

The icosahedron is planar and five-connected.  Hence `G_0` is
seven-connected: after deleting at most six vertices, either one universal
root remains, or both roots were deleted and at most four vertices were
deleted from `I`.

The graph has no `K_7` minor.  At most two branch sets of a putative
`K_7` model can contain `v` or `w`; deleting those branch sets leaves at
least five pairwise adjacent connected branch sets in `I`, a `K_5` minor
of the planar graph `I`, which is impossible.

This is the exact limit of the example.  Four-colourability of `I` makes
`G_0` six-colourable, and every vertex of `I` has degree seven in `G_0`.
Thus the graph has singleton-side order-seven separations.  The example
does **not** refute a disjunction whose alternatives include an exact-seven
response separation, nor does it realize the universal operation-specific
nonextendability of a hypothetical contraction-critical counterexample.
