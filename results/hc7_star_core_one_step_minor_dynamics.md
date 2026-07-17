# One-step minor dynamics in the connected bipartite compression

**Status:** written proof; separate independent audit.  This is a uniform
lemma whose first new application is the connected-star branch of `HC_7`.
It does not prove `HC_7` and it does not split the two bipartition classes
into connected branch sets.

## 1. Setup

Let `k>=4`, and let `G` be a `k`-chromatic graph such that every proper
minor of `G` is `(k-1)`-colourable.  Put

\[
                              p=k-2.
\]

Let

\[
                         X=G[A\mathbin{\dot\cup}B]
\]

be a connected induced bipartite subgraph with bipartition `(A,B)`, where
both `A` and `B` are nonempty, and suppose that `X` dominates

\[
                              Q=G-X.
\]

Let `m` be one elementary minor operation supported entirely in `Q`:

1. deletion of a vertex of `Q`;
2. deletion of an edge with both ends in `Q`; or
3. contraction of an edge with both ends in `Q`.

Write `H=G/m`, `Q_m=H-X`, and

\[
 S_m=N_H(A)\cap V(Q_m),\qquad
 T_m=N_H(B)\cap V(Q_m).                              \tag{1.1}
\]

For a proper `p`-colouring `psi` of `Q_m`, with palette `[p]`, put

\[
 M_S(\psi)=[p]-\psi(S_m),\qquad
 M_T(\psi)=[p]-\psi(T_m).                            \tag{1.2}
\]

The colouring is allowed to use fewer than all `p` colours.

## 2. Exact chromatic response to one elementary operation

### Lemma 2.1

For each of the three allowed operations,

\[
                              \chi(H)=k-1.            \tag{2.1}
\]

### Proof

The upper bound follows because `H` is a proper minor of `G`.

If `m` deletes a vertex and `H` were `(k-2)`-colourable, give the deleted
vertex one fresh `(k-1)`st colour.  This would `(k-1)`-colour `G`.

If `m` deletes an edge `vw` and `H` were `(k-2)`-colourable, restore the
edge.  If `v,w` have different colours, the colouring remains proper.  If
they have the same colour, recolour one endpoint with one fresh
`(k-1)`st colour.  Either way `G` would be `(k-1)`-colourable.

If `m` contracts `vw` and `H` were `(k-2)`-colourable, expand the contracted
vertex: retain its colour on one endpoint and give the other endpoint one
fresh `(k-1)`st colour.  Every old neighbour of the first endpoint was a
neighbour of the contracted vertex, while the second endpoint has the
fresh colour.  This again `(k-1)`-colours `G`.

All three possibilities contradict `chi(G)=k`.  Hence (2.1) holds.
\(\square\)

## 3. The common-hole law

### Theorem 3.1 (one-step common-hole law)

For every proper `p`-colouring `psi` of `Q_m`, the two missing-colour
sets in (1.2) contain no two distinct representatives.  Equivalently,

\[
 M_S(\psi)=\varnothing,
 \quad\hbox{or}\quad
 M_T(\psi)=\varnothing,
 \quad\hbox{or}\quad
 M_S(\psi)=M_T(\psi)=\{c\}                           \tag{3.1}
\]

for one colour `c`.

Moreover,

\[
                        p-1\leq\chi(Q_m)\leq p.      \tag{3.2}
\]

### Proof

Suppose that distinct colours `a in M_S(psi)` and `b in M_T(psi)` exist.
Keep `psi` on `Q_m`, colour every vertex of `A` with `a`, and colour every
vertex of `B` with `b`.  The external edges are proper by the definitions
of the two missing-colour sets.  Edges inside `X` join its two
bipartition classes and have differently coloured ends.  This is a
`p`-colouring of `H`, contrary to Lemma 2.1.  Therefore no such pair
exists.  Two nonempty subsets of `[p]` with no distinct representatives
must be the same singleton, proving (3.1).

The operation `m` does not destroy domination of `Q_m` by `X`.
Contracting `X` in `H` therefore gives

\[
                            H/X=K_1\vee Q_m.
\]

This is a proper minor of `G`, so it is `(k-1)`-colourable and
`chi(Q_m)<=k-2=p`.  If `Q_m` were `(p-2)`-colourable, regard such a
colouring as a `p`-colouring with two unused colours.  Both unused colours would lie
in both missing-colour sets, contradicting (3.1).  Hence
`chi(Q_m)>=p-1`. \(\square\)

The conclusion is deliberately weaker than saying that both attachment
sets use all `p` colours.  A proper minor is supposed to be
`(k-1)`-colourable, so expanding `X` to such a colouring of `H` is not a
contradiction.  Only an expansion using `p=k-2` colours contradicts (2.1),
and that is exactly what rules out two *distinct* holes.

## 4. The chromatic-drop state has a common colourful root

### Theorem 4.1 (intersection colourfulness after a drop)

Suppose `chi(Q_m)=p-1`, and put

\[
                               U=S_m\cap T_m.          \tag{4.1}
\]

Then `U` is colourful in `Q_m`: every proper `(p-1)`-colouring of `Q_m`
uses all `p-1` colours on `U`.

### Proof

Fix a proper `(p-1)`-colouring `phi` of `Q_m` and regard it as a
`p`-colouring with colour `p` unused.  The common-hole law first implies
that each of `S_m,T_m` meets every one of the `p-1` active colour classes.
Indeed, if (say) colour `i` were absent from `S_m`, then `i in M_S(phi)`
and the unused colour `p in M_T(phi)` would be distinct missing colours.

Let `C` be one colour class of `phi`, of colour `i`, and suppose
`C cap U` is empty.  The nonempty sets `C cap S_m` and `C cap T_m` are
then disjoint.  Recolour every vertex of `C cap S_m` with the unused
colour `p`.  This is proper because `C` is independent.  The resulting
`p`-colouring has colour `i` absent from `S_m`, while colour `p` is
absent from `T_m`.  These are two distinct holes, again contradicting
Theorem 3.1.  Thus every colour class meets `U`, as required. \(\square\)

Equivalently, add two adjacent auxiliary vertices with neighbourhoods
`S_m,T_m`.  The common-hole law says that the resulting graph is not
`p`-colourable, while two fresh colours give a `(p+1)`-colouring.  The
intersection conclusion is then Theorem 2.3 of the already promoted
[`hc7_leaf_rooted_chromatic_drop.md`](../results/hc7_leaf_rooted_chromatic_drop.md).
The direct proof above records exactly how the common-hole hypothesis is
used.

### Corollary 4.2 (two-sided rooted model after a chromatic drop)

In the setting of Theorem 4.1, if Strong Hadwiger holds for `p-1`
colours, then `Q_m` has a `K_{p-1}`-minor model every branch set of which
meets `U`, and hence meets both `S_m` and `T_m`.

### Proof

Apply Strong Hadwiger for `p-1` colours to the colourful set `U`.
\(\square\)

Lifting the model through `m` preserves both attachment contacts.  In the
contraction case the preimage of a quotient branch set is connected and
contains every endpoint responsible for its `A`- and `B`-contacts.

For `HC_7`, one has `p=5`, and the established Strong Hadwiger theorem
for four colours gives a `K_4` model.  This is a label-faithful closure of
the **chromatic-drop state**.  It is not by itself a `K_7` model: the independent sets `A,B` need not be
connected and therefore cannot simply be used as two branch sets.  A
separate branch-set split or a named outside pair is still needed.

## 5. Exactly when old full saturation transfers

Before applying `m`, one has `chi(Q)=p`.  Indeed, contracting the
connected dominating set `X` gives `K_1\vee Q` as a proper minor and hence
`chi(Q)<=p`; a `(p-1)`-colouring of `Q` together with two fresh colours on
the bipartite graph `X` would `(k-1)`-colour `G`.

Moreover, every `p`-colouring of `Q` uses all `p` colours on
both `N_Q(A)` and `N_Q(B)`: if a colour is absent on one side, use it on
that side and one fresh `(p+1)`st colour on the other side to
`(k-1)`-colour `G`.

That full saturation transfers to a colouring `psi` of `Q_m` only when
`psi` has a **root-trace-preserving lift** to `Q`: a proper `p`-colouring
`hat psi` of `Q` which agrees away from the operation and satisfies

\[
 \hat\psi(N_Q(A))=\psi(S_m),\qquad
 \hat\psi(N_Q(B))=\psi(T_m).                          \tag{5.1}
\]

The basic one-step lifting tests are as follows.

- If `m` deletes an edge `vw`, a colouring lifts precisely when
  `psi(v) != psi(w)`.  The root traces are then unchanged.
- If `m` deletes a vertex `v`, it extends precisely when a colour is
  absent from `psi(N_Q(v))`.  Trace preservation is automatic when
  `v` belongs to neither attachment set; otherwise (5.1) must be checked.
- If `m` contracts an edge `vw` to `x`, keep the colours of all other
  vertices and define

  \[
  L_v=[p]-\psi(N_Q(v)-\{w\}),\qquad
  L_w=[p]-\psi(N_Q(w)-\{v\}).                         \tag{5.2}
  \]

  The quotient colouring expands precisely when there are distinct
  representatives of `L_v,L_w`.  The quotient colour `psi(x)` lies in
  both lists, so expansion fails exactly when

  \[
                         L_v=L_w=\{\psi(x)\}.          \tag{5.3}
  \]

  If `v,w` lie outside both attachment sets, expansion preserves the root
  traces.  Otherwise (5.1) is an additional requirement.

Thus no nonempty family consisting of all vertex deletions, all edge
deletions, or all edge contractions automatically preserves full
two-sided saturation.  The invariant available without an extra lifting
hypothesis is Theorem 3.1, not full saturation.

## 6. Mandatory test: the `HEhutxm` core

The planar-core barrier in
[`../barriers/hc7_paired_colourful_planar_core_barrier.md`](../barriers/hc7_paired_colourful_planar_core_barrier.md)
also gives sharp witnesses to the preceding distinction.  Use its graph
`Q` on vertices `0,...,10`, with poles `9,10`, and put

\[
 S_0=\{0,1,2,3,4,5,6,7,8\},\qquad
 T_0=\{0,3,4,5,6,7,8,9,10\}.                         \tag{6.1}
\]

Both sets use all five colours in every five-colouring of `Q`.
Indeed, if `S_0` used only four colours in a five-colouring of `Q`, its
restriction would be a four-colouring of the nine-vertex core.  The two
original pole-neighbourhoods are colourful in every such colouring, so
both adjacent poles would be forced to take the same fifth colour.  Thus
`S_0` necessarily uses five colours.  The graph induced by `T_0` is
itself five-chromatic:
in a hypothetical four-colouring, the two overlapping `K_4`s
`{0,10,4,6}`, `{8,10,4,6}` force `0` and `8` to agree, while
`{0,9,3,7}`, `{5,9,3,7}` force `0` and `5` to agree, contradicting the
edge `58`.

Nevertheless each of the three types of elementary operation admits a
non-lifting response that loses saturation on `S_0` while retaining it on
`T_0`.

1. In `Q-03`, the colouring

   ```text
   0:2 1:3 2:3 3:2 4:0 5:0 6:1 7:1 8:2 9:3 10:4
   ```

   misses colour `4` on `S_0` and uses all colours on `T_0`.  The deleted
   edge ends have the same colour, so the colouring does not lift.
2. In `Q-0`, the colouring

   ```text
   1:3 2:3 3:1 4:0 5:0 6:2 7:2 8:1 9:3 10:4
   ```

   has the same missing/full pattern.  The neighbours of the deleted
   vertex `0` use all five colours, so it does not extend.
3. Contract `03` to the vertex `0`.  The colouring

   ```text
   0:0 1:3 2:3 4:1 5:1 6:2 7:2 8:0 9:4 10:3
   ```

   again misses colour `4` on the image of `S_0` and uses all colours on
   the image of `T_0`.  Both lists in (5.2) equal `{0}`, so it does not
   expand.

These examples satisfy the common-hole law: one attachment set is full.
They disprove the stronger minor-dynamic saturation premise, not Theorem
3.1.  The construction does not supply a minor-minimal host `G` and a
connected bipartite subgraph `X` satisfying the setup; it tests only the
static-saturation inference.  The original `HEhutxm` sets from the
paired-root barrier are
separately colourful in four colours but have non-colourful intersection;
Theorem 4.1 explains the missing hypothesis exactly: a five-colour
refinement creates two different holes, so that static core is not a
valid chromatic-drop state of the minor-critical bipartite compression.

## 7. Consequence for the research programme

There is an exact chromatic dichotomy after every elementary
operation in `Q`.  In the `HC_7` specialization:

- if `chi(Q_m)=4`, Corollary 4.2 gives a two-sided rooted `K_4` model;
- if `chi(Q_m)=5`, chromatic order has not decreased and the only uniform
  information is the common-hole cover (3.1).

Therefore a recursive proof should not claim that arbitrary proper-minor
responses preserve full saturation.  Its remaining transition theorem
must either force the first branch, use the orientation of the three
possibilities in (3.1), or add host geometry that preserves a
root-trace-lift.  Repeating arbitrary minor operations does not by itself
give a strict descent, because Lemma 2.1 is a statement only about one
operation from the original minor-minimal graph.

## 8. External input

A. Martinsson and R. Steiner,
[*Strengthening Hadwiger's conjecture for 4- and 5-chromatic graphs*](https://doi.org/10.1016/j.jctb.2023.08.009),
Journal of Combinatorial Theory, Series B 164 (2024), 1--16, Theorem 1.3.
Their theorem says that a colourful set in a four-chromatic graph roots a
`K_4` minor.
