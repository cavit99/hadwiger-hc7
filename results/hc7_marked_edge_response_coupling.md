# Marked-edge response coupling at the bounded interface

**Status:** written proof; [separately audited **GREEN**](hc7_marked_edge_response_coupling_audit.md).
This note records
the exact positive output of the marked-edge coupling experiment. It gives a
common-state one-sided split and a submodular bounded-separation lattice, but
neither output is terminal. In particular, it does not prove `HC_7`.

## 1. One edge has only one response family

### Lemma 1.1 (deletion and contraction responses coincide)

Let `G` be non-`q`-colourable and let `xy` be an edge such that both proper
minors `G-xy` and `G/xy` are `q`-colourable. Every `q`-colouring of `G-xy`
makes `x,y` monochromatic. Expansion and contraction therefore give a
bijection between the `q`-colourings of `G/xy` and those of `G-xy`.

#### Proof

If a `q`-colouring of `G-xy` gave `x,y` different colours, restoring `xy`
would give a `q`-colouring of `G`. Thus the two ends have the same colour,
and the colouring descends through the contraction. Conversely, every
colouring of `G/xy` expands with the two ends equal and is proper after
deleting `xy`. These operations are inverse. \(\square\)

Consequently, probing deletion and contraction of one marked edge does not
create two ordered response families. Any monotonicity must compare genuinely
different operations or preserve additional literal host data.

## 2. A common double-contraction state is only one-sided

### Theorem 2.1 (two anticomplete bipartite contractions)

Let `q>=2`, and let `G` be proper-minor-minimal non-`q`-colourable. Let
`X,Y` be disjoint anticomplete vertex sets, each of order at least two, such
that `G[X]` and `G[Y]` are connected and bipartite. Contract each set to one
vertex, obtaining

\[
                              M=G/X/Y.
\]

Then:

1. `chi(M)=q`.
2. Fix a `q`-colouring `c` of `M`, with palette `Q`, and let `a_X,a_Y` be
   the colours of the two contraction vertices. Put

   \[
   \begin{aligned}
   L_X(x)&=Q-c\bigl(N_G(x)-(X\cup Y)\bigr),\\
   L_Y(y)&=Q-c\bigl(N_G(y)-(X\cup Y)\bigr).
   \end{aligned}                                           \tag{2.1}
   \]

   At least one of `G[X]` and `G[Y]` is not colourable from its displayed
   lists.
3. For every spanning tree of each uncolourable side, some tree edge splits
   that side into nonempty connected adjacent sets `Z^-`,`Z^+` such that

   \[
   c\bigl(N_G(Z^-)-(X\cup Y)\bigr)
   =c\bigl(N_G(Z^+)-(X\cup Y)\bigr)
   =Q-\{a_Z\}.                                             \tag{2.2}
   \]

   Thus one side has a bilateral full-palette cut in the one fixed common
   contraction state. Both sides have such cuts if both list systems are
   uncolourable.
4. If exactly one list system is colourable, expanding that side gives a
   `q`-colouring of the minor in which only the other set remains contracted.

#### Proof

The graph `M` is a proper minor, so it is `q`-colourable. Suppose it had a
`(q-1)`-colouring. Fix a bipartition of each of `G[X]` and `G[Y]`. On one
class of `X`, reuse the colour of the `X`-contraction vertex; on its other
class use one fresh colour. Do the same for `Y`, using the same fresh colour.
Every outside neighbour avoids the relevant contraction colour, the fresh
colour occurs nowhere outside `X\cup Y`, and there are no `X-Y` edges. This
would `q`-colour `G`, a contradiction. Hence `chi(M)=q`.

Now fix `c`. Every list `L_X(x)` contains `a_X`, because every outside
neighbour of `x` is adjacent in `M` to the `X`-contraction vertex. Similarly,
`a_Y` belongs to every `Y`-list. If both induced bipartite graphs were
colourable from their lists, those two colourings and `c|G-(X\cup Y)` would
combine to a `q`-colouring of `G`; anticompleteness makes the two expansions
independent. Thus at least one list system is uncolourable.

Apply the audited poor-edge lemma for bipartite graphs to an uncolourable
side and any selected spanning tree. It gives a tree edge whose two sides
have list intersection exactly the common contraction colour. Taking palette
complements in (2.1) gives (2.2). If the other list system is colourable, its
list-colouring combines with the fixed exterior state and leaves only the
uncolourable set contracted, proving item 4. \(\square\)

The two-transition path interiors are anticomplete because they lie in
opposite open shores. When both interiors have at least two vertices,
Theorem 2.1 applies. It does not decide which interior is uncolourable, and
the explicit barrier in
[`../barriers/hc7_simultaneous_bipartite_bilateral_exposure_barrier.md`](../barriers/hc7_simultaneous_bipartite_bilateral_exposure_barrier.md)
shows that both need not be.

## 3. A bounded weighted-separation lattice

Use the path outcome of the audited two-transition theorem. Thus `G` is a
hypothetical minor-minimal counterexample, `C` is a component of `G-N[u]`,

\[
 S=N_G(C),\qquad
 A_0=C\cup S,\qquad B_0=V(G)-C,
 \qquad 7\le |S|\le9,                                  \tag{3.1}
\]

and `z in S`. There are vertex-disjoint paths in opposite open shores. Pick
endpoint edges

\[
 g=pv,\qquad h=qw,                                     \tag{3.2}
\]

where `p,q in S`, `v in C`, and
`w in B_0-(S\cup\{u\})`. Put `H=G-{g,h}`.

Call a separation `(A,B)` of `H` **anchored** if

\[
 v\in A-B,\qquad u,w\in B-A,\qquad z\in A\cap B.      \tag{3.3}
\]

For an edge `e`, let `epsilon_e(A,B)=1` when its ends lie in opposite open
sides and zero otherwise. Define

\[
 \lambda(A,B)=|A\cap B|+\epsilon_g(A,B)+\epsilon_h(A,B). \tag{3.4}
\]

### Theorem 3.1 (anchored marked-edge lattice)

Let

\[
 m=\min\{\lambda(A,B):(A,B)\text{ is an anchored separation of }H\}.
                                                               \tag{3.5}
\]

Then:

1. `7<=m<=|S|<=9`.
2. The anchored separations of weight `m` are closed under the standard
   separation meet and join. Their meet over the finite family is a
   canonical least member `(A_*,B_*)`. If `m=|S|`, then

   \[
                              A_*-B_*\subseteq C.       \tag{3.6}
   \]

   No containment in `C` is asserted when `m<|S|`.
3. Every minimum member lifts to a literal separation
   `(widehat A,widehat B)` of `G` of order `m`, retaining all four anchors,
   with `g` wholly in the left closed shore and `h,uz` wholly in the right
   closed shore.
4. On the lifted separator `T`, every `G-g` response extends through the
   right closed shore and is rejected by the intact left closed shore.
   Every `G-h` response extends through the left and is rejected by the
   intact right; the same orientation holds for every `G-uz` response.

#### Proof

Let `(A,B)` be anchored. If `g=pv` crosses, (3.3) forces `p in B-A`; add
`p` to `A`. If `h=qw` crosses, it forces `q in A-B`; add `q` to `B`. The
marked edges are vertex-disjoint. The resulting pair
`(widehat A,widehat B)` is a separation of `G`, its order is exactly
`lambda(A,B)`, and the vertices `v` and `u,w` remain in opposite open sides
while `z` remains in the separator. Seven-connectivity of `G` therefore
gives `lambda(A,B)>=7`.

The original pair `(A_0,B_0)` is anchored, neither marked edge crosses it,
and its order is `|S|`. This proves item 1.

For oriented separations `sigma=(A,B)` and `tau=(D,E)`, put

\[
\begin{aligned}
 \sigma\wedge\tau&=(A\cap D,B\cup E),\\
 \sigma\vee\tau&=(A\cup D,B\cap E).
\end{aligned}                                            \tag{3.7}
\]

Both are separations of `H` and preserve (3.3). Record the state of a vertex
as left-open, separator, or right-open. Meet and join take the two extrema
of these states, so the total separator contribution in the two corners
equals that in the two original separations. For a fixed marked edge, if it
crosses one corner it crossed at least one original separation; if it crosses
both corners it crossed both originals. Consequently,

\[
 \lambda(\sigma\wedge\tau)+\lambda(\sigma\vee\tau)
 \le \lambda(\sigma)+\lambda(\tau).                     \tag{3.8}
\]

If both original weights equal `m`, minimality bounds each corner below by
`m`, while (3.8) bounds their sum above by `2m`. Both corner weights are
therefore `m`. The finite minimum family is a lattice, and its meet
`(A_*,B_*)` is its least member. When `m=|S|`, the original separation also
belongs to this family, so the least member lies below it and (3.6) follows.
When `m<|S|`, submodularity with the nonminimum original separation does not
put their meet back in the minimum family; no containment in `C` follows.

The lift already constructed proves item 3.
For item 4, let `T=widehat A\cap widehat B`. A colouring of `G-g` restricts
properly to the right closed shore. If its partition of `T` also extended
through the intact left shore, permuting colour names to agree on `T` and
gluing would six-colour `G`. Thus the partition is rejected on the left.
The arguments for `h` and `uz` are symmetric. \(\square\)

## 4. Why Cycle 1 does not pass the continuation gate

The preceding results are genuine, but they do not supply the invariant
required for a second cycle.

- The common double contraction gives only unilateral exposure. Its lists
  are palette data, not five pairwise adjacent literal carriers.
- The minimum marked-edge lift may be exactly `(A_0,B_0)`. Even a different
  separation of `H` can lift back to the same separation of `G` merely by
  moving `p` or `q` across a deleted edge and then returning it to the
  separator.
- A response on a new separator records a fresh partition of that separator.
  It does not preserve the original partition of `S`, the exact-block
  cylinder, or the full boundary response language.
- When `d_G(u)=|S|=7`, the opposite open-shore path setup is empty: the
  audited degree-seven anti-neighbourhood theorem makes `C` the only
  component of `G-N[u]`.
- Total contraction of one whole path does give one bilateral five-colour
  exposure, but its boundary is `N(P)`, which can be unbounded, and its two
  pieces are not components of `G-N[u]`.

Thus Cycle 1 produced neither a strict same-host decrease nor a new literal
bounded interface carrying the original labelled response. Proceeding to
orders eight and nine or to the tight-pole residue would merely transport
fresh response partitions. Under the declared gate, Cycle 2 is not started.

## 5. Dependencies

- [two-transition opposite-shore paths](hc7_bounded_interface_two_transition_disjoint_response.md);
- [bipartite poor-edge lemma](hc7_near_k7_bipartite_total_contraction.md#lemma-12-poor-edge-lemma-for-bipartite-graphs); and
- [degree-seven anti-neighbourhood connectivity](hc7_degree7_anti_neighbourhood_connectivity.md).
