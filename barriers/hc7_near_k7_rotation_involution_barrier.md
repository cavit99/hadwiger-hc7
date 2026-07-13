# Deficiency pivots are involutions: the exact obstruction to a raw rotation potential

## Status

This note audits one proposed well-founded-potential endgame after the
seven-root trichotomy.  A **single-gate** gate-to-centre deficiency
rotation is not an
intrinsically directed move.  Under its exact literal hypotheses it has a
legal inverse, obtained by moving the same gate back.  Consequently no
potential can strictly decrease under **every** legal gate rotation.

The obstruction already occurs, in balanced form, in the seven-connected
`K_7`-minor-free graph obtained by joining an edge to the icosahedron.  That
graph is coherently two-apex.  Thus the example does not challenge `HC_7`;
it proves that termination has to recognize the coherent alternative or use
proper-minor boundary states.  Bag sizes, portal ownership, and rotation
alone cannot orient the endgame.

## 1. Literal pivot and its inverse

Let

\[
                      A,U,F_1,\ldots,F_5                 \tag{1.1}
\]

be pairwise disjoint nonempty connected bags.  Assume that
`U,F_1,...,F_5` are pairwise adjacent.  Let

\[
 M=\{j:E(A,F_j)=\varnothing\}.                           \tag{1.2}
\]

Assume that `A` meets `U` and meets every `F_j` outside `M`.  Thus (1.1)
is a missing-star near-`K_7` model, with `A` as centre and missing set
`M`.

Suppose

\[
                       U=W\mathbin{\dot\cup} Z            \tag{1.3}
\]

where `W,Z` are nonempty and connected and have an edge between them.
Assume also that `A` meets `Z` and that `Z` meets every `F_j` for
`j in M`.  Put

\[
 A'=A\cup Z,
 \qquad
 \Omega=\{j:E(W,F_j)=\varnothing\}.                     \tag{1.4}
\]

### Lemma 1 (pivot involution)

The bags

\[
                       W,A',F_1,\ldots,F_5               \tag{1.5}
\]

form a missing-star near-`K_7` model with centre `W` and missing set
`Omega`.  Moreover the operation is exactly reversible: regarding `A'`
as the donor, split it as `A dotcup Z` and move `Z` into `W`.  This
recovers (1.1), with centre `A` and missing set `M`.

#### Proof

The enlarged bag `A'` is connected through an actual `A-Z` edge.  It is
adjacent to every `F_j`: the old bag `A` supplies the adjacency when
`j notin M`, while `Z` supplies it when `j in M`.  Hence
`A',F_1,...,F_5` are pairwise adjacent.  The residual bag `W` is
connected and meets `A'` through an actual `W-Z` edge.  Its only absent
spokes are exactly those indexed by `Omega`.  This proves the first
assertion.

For the inverse operation, `A` and `Z` are connected and adjacent, and
`W` meets `Z`.  If `j in Omega`, then `W` is anticomplete to `F_j`, but
the old donor `U=W union Z` met `F_j`; consequently `Z` meets `F_j`.
Thus moving `Z` into `W` repairs every spoke currently missing at `W`.
After `Z` is removed from `A'`, the residual `A` meets precisely all the
rows outside `M`, by (1.2).  The recovered donor is `W union Z=U`.
Every bag and every claimed adjacency is therefore exactly the one in
(1.1). \(\square\)

If both `|M|` and `|Omega|` are at most two, both directions stay inside
the class of labelled `K_7^-`/`K_7^vee` models used by the current proof
spine.  The move is then an undirected edge of the near-model state graph,
not a descent.

### Lemma 2 (size tradeoff)

Write

\[
 a=|A|,\qquad w=|W|,\qquad z=|Z|.
\]

The pivot preserves the used vertex set and the total bag order.  For the
quadratic bag-size statistic

\[
                         Q=\sum_{H\text{ a bag}}|H|^2
\]

one has

\[
                         Q'-Q=2z(a-w).                   \tag{1.6}
\]

In particular, moving to a larger centre strictly decreases `Q`, moving
to a smaller centre strictly increases `Q`, and a balanced pivot
`a=w` preserves the complete multiset of bag sizes.

#### Proof

Only `A,U` change.  Their old orders are `a,w+z`, and the new orders are
`a+z,w`.  Hence

\[
 Q'-Q=(a+z)^2+w^2-a^2-(w+z)^2=2z(a-w).
\]

If `a=w`, the affected size pair is merely interchanged. \(\square\)

Lemma 1 already rules out a scalar which is required to decrease on every
legal pivot: applying it to a pivot and its inverse would give both
`Phi(M')<Phi(M)` and `Phi(M)<Phi(M')`.  Lemma 2 shows the more specific
failure of the natural centre-order/convex-dispersion attempts.  The two
coordinates move in opposite directions, and in the balanced cell neither
moves at all.

## 2. A balanced cycle in `K_2` joined with the icosahedron

Let `I` be the icosahedral graph with vertices

\[
 t,b,u_0,\ldots,u_4,w_0,\ldots,w_4
\]

and, with subscripts modulo five, edges

\[
 tu_i,\quad bw_i,\quad u_iu_{i+1},\quad w_iw_{i+1},
 \quad u_iw_i,\quad u_iw_{i-1}.                         \tag{2.1}
\]

Let `p,q` be adjacent new vertices, each complete to `I`, and put

\[
                              G=K_2\vee I.               \tag{2.2}
\]

### Proposition 3 (ambient properties)

The graph `G` is seven-connected and `K_7`-minor-free, and deleting
`p,q` leaves a planar graph.

#### Proof

The icosahedral graph is planar and five-connected.  Delete at most six
vertices from `G`.  If at least one of `p,q` remains, that vertex is
adjacent to every other remaining vertex, so the remainder is connected.
If both are deleted, at most four vertices of `I` were also deleted, and
five-connectivity of `I` again leaves a connected graph.  Thus `G` is
seven-connected.

Suppose that `G` had a `K_7` model.  At most two of its branch bags could
contain `p` or `q`.  Deleting those bags would leave at least five
pairwise adjacent connected branch bags wholly inside `I`, hence a
`K_5` minor in `I`.  This is impossible because planarity is preserved
under minors and `K_5` is nonplanar.  Therefore `G` is `K_7`-minor-free.
Finally `G-{p,q}=I` is planar, so `{p,q}` is a coherent two-apex pair.
\(\square\)

### Proposition 4 (explicit inverse `K_7^-` pivots)

In `G`, define

\[
\begin{aligned}
 A&=\{u_3\},             & D&=\{t,u_0\},\\
 B&=\{u_1\},             & R&=\{u_2\},\\
 E&=\{b,w_0,w_2\},       & P&=\{p\},\qquad Q=\{q\}.
\end{aligned}                                                \tag{2.3}
\]

These seven bags form a `K_7^-` model whose unique missing pair is
`AB`.  Splitting

\[
                 D=W\mathbin{\dot\cup}Z,qquad
                 W=\{u_0\},\quad Z=\{t\},                \tag{2.4}
\]

and moving `Z` into `A` gives a second `K_7^-` model

\[
       W,\ A'=\{u_3,t\},\ B,\ R,\ E,\ P,\ Q              \tag{2.5}
\]

whose unique missing pair is `WR`.  Moving the same vertex `t` back is
the inverse pivot and recovers (2.3).  Both pivots are balanced.

#### Proof

The bags `D` and `E` are connected through `tu_0` and the two edges
`bw_0,bw_2`, respectively.  The six foreign bags

\[
                         D,B,R,E,P,Q                       \tag{2.6}
\]

are pairwise adjacent.  Adjacencies involving `P,Q` follow from their
universality.  The six remaining checks are witnessed by

\[
\begin{array}{c|c}
\text{bag pair}&\text{literal edge}\\ \hline
DB&tu_1\\
DR&tu_2\\
DE&u_0w_0\\
BR&u_1u_2\\
BE&u_1w_0\\
RE&u_2w_2.
\end{array}                                                \tag{2.7}
\]

The centre `A={u_3}` meets `D,R,E,P,Q` through, respectively,

\[
                  u_3t,\quad u_3u_2,\quad u_3w_2,
                  \quad u_3p,\quad u_3q.                 \tag{2.8}
\]

It is anticomplete to `B={u_1}`, since `u_1u_3` is not an edge of the
upper five-cycle.  This proves the first exact `K_7^-` model.

For (2.4), `Z={t}` meets the old centre through `tu_3` and the old
missed row `B` through `tu_1`.  The residual `W={u_0}` meets

\[
                  B,E,P,Q
\]

through `u_0u_1,u_0w_0,u_0p,u_0q`, but it is anticomplete to
`R={u_2}`.  Thus its new missing set is exactly `{R}`.  The enlarged
bag `A'={u_3,t}` is connected and meets `B,R,E,P,Q` through

\[
                  tu_1,\quad tu_2,\quad u_3w_2,
                  \quad tp,\quad tq.                     \tag{2.9}
\]

All other foreign-foreign adjacencies are unchanged, and `W` meets
`A'` through `u_0t`.  Hence (2.5) is the claimed exact `K_7^-` model.

For the reverse move, split `A'` into the residual `{u_3}` and the gate
`{t}`.  The gate meets the current missed row `R` through `tu_2`.
The residual `{u_3}` meets `R,E,P,Q` and misses exactly `B`, by (2.8).
Moving `t` into `{u_0}` recreates `D={t,u_0}`.  This verifies the
inverse without appealing merely to symmetry.

Both centres have order one and both donors have order two.  Thus
`a=w=z=1`, and the pivot is balanced in the sense of Lemma 2. \(\square\)

## 3. Consequence for the `HC_7` spine

The example is six-colourable (four-colour `I` and give `p,q` two fresh
colours), so it is not a contraction-critical counterexample.  Its role
is a falsification gate for the proposed termination mechanism:

\[
 \boxed{\text{a raw single-gate deficiency pivot must be quotiented as an
 exchange equivalence, not oriented as an automatic descent.}}
\]

Accordingly, the single-gate rotation output of the seven-root
trichotomy cannot be closed by centre size, sum of bag sizes, a convex
bag-size potential, or portal-monopoly order alone.  (The separate
two-piece/two-target rotation is not claimed to be an involution here.)
A valid next theorem must add information absent from (2.2), for
example one of the following.

1. A proper-minor boundary state which changes across the pivot and
   eventually matches an opposite-shore state, giving a six-colouring by
   gluing.
2. A port-labelled expansion theorem showing that every pivot in one
   exchange component uses the same two actual apex vertices.

The explicit cycle proves why the coherent two-apex output in the proof
spine is necessary rather than cosmetic.  It does not prove that every
rotation component in a contraction-critical graph is coherent, which is
the exact remaining termination gap.
