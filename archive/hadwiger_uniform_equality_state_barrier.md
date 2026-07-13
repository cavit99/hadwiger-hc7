# The equality layer `c=2m`: exact one-split states and a sharp state barrier

## 1. Forced states

Let `G,S,D_1,...,D_m` satisfy the hypotheses of
`hadwiger_uniform_full_cut_inequalities.md`, and suppose

\[
                         |S|=2m.                              \tag{1.1}
\]

The uniform cut inequality gives `chi(G[S])=m`.  Fix an optimal
partition

\[
             \Pi=A_1\mid\cdots\mid A_m,
             \qquad A_j=\{x_j,y_j\}.                         \tag{1.2}
\]

For `j in [m]`, let `Pi^j` be the one-split partition obtained by
replacing the block `A_j` by the two singleton blocks `{x_j},{y_j}`.
Let `E_i` be the equality-partition extension family of the closed side
`G[S union D_i]` in `(k-1)` colours.

### Theorem 1.1 (last-pair state dichotomy)

For every side `i` and every pair index `j`,

\[
                          \Pi\in E_i\quad\text{or}\quad
                          \Pi^j\in E_i.                       \tag{1.3}
\]

Moreover, if `Pi notin E_i`, then

\[
                          \Pi^j\in E_i\qquad(j\in[m]).        \tag{1.4}
\]

### Proof

Fix `i,j`.  Use the `m-1` components other than `D_i` to contract the
independent pairs `A_h`, `h ne j`, exactly as in the multi-block exact
trace theorem.  In the resulting proper minor the `m-1` contracted
vertices form a clique and are adjacent to both `x_j,y_j`.  Hence in a
`(k-1)`-colouring those `m-1` pair colours occur nowhere else on `S`.
After expanding the boundary pairs, the two vertices of `A_j` either
receive one common new colour or two distinct new colours.  The induced
boundary equality partition is respectively `Pi` or `Pi^j`, proving
(1.3).  If the first alternative is unavailable on side `i`, the second
holds for every `j`, proving (1.4).  QED.

Since a common state would colour `G`, the families have empty total
intersection.  Thus at least one side rejects `Pi` and accepts all
one-split states.  Conversely, for every `j`, some side rejects `Pi^j`
and therefore accepts `Pi`.  This is the exact crossed state forced at
the equality layer.

## 2. A minimal-empty-intersection state system

The preceding algebra does not force a common state.

### Theorem 2.1 (sharp abstract barrier)

For every `m>=2` there are `m` state families

\[
                         E_0,E_1,\ldots,E_{m-1}                \tag{2.1}
\]

on the state universe

\[
                         U=\{\Pi,\Pi^1,\ldots,\Pi^m\}         \tag{2.2}
\]

such that:

1. every family satisfies (1.3);
2. their total intersection is empty;
3. deleting any one family makes the intersection nonempty; and
4. the states absent from one family are exactly the states common to
   all the other families:
   \[
                       U-E_i=\bigcap_{h\ne i}E_h.             \tag{2.3}
   \]

### Proof

Partition `[m]` into `m-1` nonempty sets

\[
                         R_1\dot\cup\cdots\dot\cup R_{m-1}.
\tag{2.4}
\]

(Exactly one part has order two and the others order one.)  Put

\[
 \begin{aligned}
 E_0&=\{\Pi^1,\ldots,\Pi^m\},\\
 E_i&=\{\Pi\}\cup\{\Pi^j:j\notin R_i\}
                         \qquad(1\le i<m).                    \tag{2.5}
 \end{aligned}
\]

The exceptional family `E_0` rejects `Pi` and accepts every split.
Every other family accepts `Pi`, so (1.3) holds.  The base state is
rejected only by `E_0`; the split state `Pi^j` is rejected only by the
unique `E_i` with `j in R_i`.  Hence no state lies in every family, and
removing the unique rejecting family makes that state common.  This is
exactly (2.3).  QED.

Thus even the strongest possible crossed pattern suggested by one-step
minor-criticality is formally consistent: every side can reject exactly
the states accepted by all opposite sides.

## 3. Actual boundaried realizations

The abstract system is realized by finite graph gadgets.

Let

\[
                         F=K_{2,2,\ldots,2}                    \tag{3.1}
\]

be the complete `m`-partite graph on the pairs `A_1,...,A_m`, and use
`r=m+1` colours.  Every colour class of a proper colouring of `F` lies
within one pair.  If `s` pairs are split, the colouring uses exactly
`m+s` colours.  Therefore the complete equality-state universe of
proper `r`-colourings of `F` is precisely

\[
                              U=\{\Pi,\Pi^1,\ldots,\Pi^m\}.   \tag{3.2}
\]

The finite colouring-relation realization theorem of Dvorak--Swart now
gives an `S`-boundaried graph `H_i` whose exact `r`-colour extension
family is `E_i`, for every family in (2.5).  The boundary can be kept
induced as exactly `F`: every missing pair edge is equated by some state
of every `E_i` (for `E_0`, use a split at a different pair).

### Proposition 3.1 (full minimum-cut realization)

There is a non-`r`-colourable graph with boundary `S` such that

* `|S|=2m` and `S` is a minimum cut;
* the graph has exactly `m` components behind `S`;
* every component is connected and full to `S`; and
* the exact side extension families are (2.5).

### Proof

Make every open realizer connected and full without changing its
extension relation by the standard length-two connector construction.
Then replace every open vertex by an independent false-twin class of
order `2m`, replacing every old edge by the corresponding complete
bipartite graph.  Glue the `m` amplified realizers along `S`.

Deleting fewer than `2m` vertices leaves a representative of every twin
class and at least one boundary vertex.  Each side remains connected and
full, so all surviving vertices lie in one component.  Hence the glued
graph is `2m`-connected.  Deleting `S` leaves the `m` open interiors, so
`S` is a minimum cut and they are exactly its full components.

A global `r`-colouring would induce a state in the total intersection
of (2.5), which is empty.  Thus the graph is not `r`-colourable.  QED.

This graph is not asserted to exclude a prescribed clique minor or to be
minor-minimal.  It shows that full components, the exact equality
`c=2m`, high connectivity up to the adhesion order, and the complete
one-split state algebra still do not force a common state.

### Proposition 3.2 (crossed one-step critical realizations)

Separately, the realizers can be chosen so that deleting an internal
vertex, deleting an internal edge, or contracting an internal edge on
any one side makes the glued graph `r`-colourable.

### Proof

Choose each exact realizer deletion-minimal while preserving its family
`E_i`.  Deleting an internal object creates a new boundary state outside
`E_i`.  By (2.3), every such state is accepted by all opposite sides, so
the colourings glue.  For an internal edge contraction, a colouring made
new by deleting the edge gives its ends the same colour—otherwise it
would colour the original side—and therefore descends through the
contraction.  QED.

The connectivity amplification in Proposition 3.1 introduces redundant
twins, so Propositions 3.1 and 3.2 are deliberately separate.  Their
conjunction, together with `K_k`-minor exclusion, is exactly the geometric
information not encoded by the state families.

## 4. The genuine last-pair target

At `c=2m`, state manipulation alone is exhausted.  A positive theorem
must use the geometry of a side `D_i` which accepts every `Pi^j` but
rejects `Pi`.

In each `Pi^j` state, the other `m-1` pairs have disjoint connected
realizations supplied by opposite full shores, while the last pair is
forced apart.  The missing uniform statement is therefore a geometric
last-pair exchange:

> either the `m-1` block carriers can be rerouted so that the two vertices
> of the last pair join without meeting them, producing `Pi`, or their
> failure exposes a relative separator which is incompatible with the
> minimum-cut geometry or yields the target clique minor.

Theorem 2.1 and Propositions 3.1--3.2 prove that no theorem phrased only
in terms of accepted states or crossed proper-minor novelty can supply
that rerouting.  Portal placement, linkage, or target-minor exclusion
must enter explicitly.
