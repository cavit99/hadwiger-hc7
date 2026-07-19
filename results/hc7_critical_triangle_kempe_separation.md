# Kempe-separated responses at a critical triangle

**Status:** written proof; separate internal audit GREEN in
[`hc7_critical_triangle_kempe_separation_audit.md`](hc7_critical_triangle_kempe_separation_audit.md).
This result does not prove `HC_7`.

Two incident deleted edges whose other ends are adjacent give a triangle in
the original graph.  The two possible six-colouring responses can fail to be
Kempe-equivalent.  This note identifies the exact graph-theoretic object then
forced by that failure: a connected three-chromatic subgraph containing the
triangle.  Its full neighbourhood is an actual separator unless the subgraph
dominates, in which case its complement is a four- or five-chromatic
`K_6`-minor-free graph.

The conclusion does not align colours with the labels of a fixed minor model.

## 1. Critical-triangle responses

Let `q>=2`, let `G` be a graph which is not `q`-colourable, and let

\[
                 e=va,\qquad f=vb,\qquad ab\in E(G),              \tag{1.1}
\]

where `v,a,b` are distinct.  Put

\[
                          H=G-\{e,f\}.                            \tag{1.2}
\]

For a proper `q`-colouring of `H`, record whether the ends of `e` and
`f` have equal or different colours.  Let

\[
\begin{aligned}
 X&=\{c:c(v)=c(a)\ne c(b)\},\\
 Y&=\{c:c(v)=c(b)\ne c(a)\}.                              \tag{1.3}
\end{aligned}
\]

The edge `ab` shows that the two equalities cannot hold simultaneously.
The assumption that `G` is not `q`-colourable shows that a colouring of
`H` cannot make both deleted edges proper.  Hence every `q`-colouring of
`H` lies in `X` or `Y`.  In the contraction-critical application both
sets are nonempty, because colourings of `G/e` and `G/f` expand to exact
members of `X` and `Y`, respectively.

Say that `X` and `Y` are **Kempe-separated** if no component of the
`q`-colouring Kempe-reconfiguration graph of `H` meets both sets.

## 2. The forced bichromatic component

### Theorem 2.1 (critical-triangle Kempe-separated component)

Assume that `X` and `Y` are nonempty and Kempe-separated.  Let `c` be a
colouring in `X`, write

\[
                       c(v)=c(a)=\alpha,\qquad c(b)=\beta,         \tag{2.1}
\]

and let `D` be the component containing `v` of

\[
                    H[c^{-1}(\{\alpha,\beta\})].                 \tag{2.2}
\]

Then

\[
                              a,b\in V(D).                         \tag{2.3}
\]

The symmetric assertion holds for every colouring in `Y`.

Moreover, `G[D]` is connected and

\[
                              \chi(G[D])=3.                        \tag{2.4}
\]

#### Proof

The edge `ab` belongs to `H`, and its ends have colours `alpha,beta`.
Thus `a` and `b` lie in one common `alpha`--`beta` component of `H`.
If that component were different from `D`, interchange `alpha,beta` only
on `D`.  The resulting proper colouring `c'` of `H` would satisfy

\[
                      c'(v)=c(b)\ne c(a),
\]

so `c'` would belong to `Y`.  This would be one Kempe interchange from
`X` to `Y`, contrary to their separation.  Therefore `D` contains both
`a` and `b`, proving (2.3).  Interchanging the roles of `a,b` proves the
symmetric assertion.

The graph `H[D]` is connected and bipartite, with colour classes

\[
        P=V(D)\cap c^{-1}(\alpha),\qquad
        Q=V(D)\cap c^{-1}(\beta).                                \tag{2.5}
\]

Here `v,a` belong to `P` and `b` belongs to `Q`.  Passing from `H[D]` to
`G[D]` restores `va` and `vb`.  The edge `vb`, like the already present
edge `ab`, joins `P` to `Q`; the only restored edge inside a class of
(2.5) is `va`.  Consequently

\[
                         \{v\},\quad P-\{v\},\quad Q              \tag{2.6}
\]

are three independent sets which partition `V(D)`.  They properly
three-colour `G[D]`.  On the other hand, `v,a,b` induce a triangle in
`G[D]`, so two colours do not suffice.  This proves (2.4).  \(\square\)

## 3. Consequence in the `HC_7` setting

### Corollary 3.1 (separator or lower-chromatic core)

In addition to Theorem 2.1, suppose that

\[
 \chi(G)=7,\qquad G\text{ is seven-connected},\qquad
 K_7\not\preccurlyeq G.                                      \tag{3.1}
\]

For every colouring `c` in either response family, its subgraph `D` from
Theorem 2.1 satisfies exactly one of the following alternatives.

1. `D` is not dominating.  Then

   \[
                               S=N_G(D)                           \tag{3.2}
   \]

   is the boundary of an actual separation with two nonempty open sides,
   and `|S|>=7`.
2. `D` is dominating, and

   \[
                  4\le \chi(G-D)\le5,
                  \qquad K_6\not\preccurlyeq G-D.                \tag{3.3}
   \]

#### Proof

Suppose first that `D` is not dominating.  A vertex outside `N_G[D]`
and the nonempty connected set `D` lie in different components after
deleting `N_G(D)`.  Thus (3.2) is an actual separator, and
seven-connectivity gives `|S|>=7`.

Now suppose that `D` dominates.  If `G-D` were three-colourable, its
colouring and the three-colouring (2.6), on disjoint palettes, would
six-colour `G`.  Hence `chi(G-D)>=4`.  If `G-D` contained a `K_6` minor,
its six branch sets together with the connected dominating set `D` would
form a `K_7`-minor model in `G`.  Therefore `G-D` is `K_6`-minor-free.
Hadwiger's Conjecture for parameter six gives `chi(G-D)<=5`, proving
(3.3).  \(\square\)

## 4. Application to a persistent labelled near-clique model

Suppose additionally that the same spanning labelled
`K_7`-minus-one-edge model survives in `H`.  Theorem 2.1 and Corollary 3.1
do not modify its branch sets, so the model remains available throughout
the argument.  However, the sets `P,Q,D` are defined by palette colours,
not by branch-set labels.  In particular, the theorem does not show that
either side of (2.5) meets prescribed branch sets.

The [adjacent finite barrier](../barriers/hc7_critical_triangle_kempe_separation_barrier.md)
shows that seven-connectivity, vertex-criticality, exact opposite
responses, and one common spanning labelled near-clique model do not force
the two response families to meet.  That construction exits through both
an explicit `K_7` model and an actual order-seven separator.

## 5. Exact trust boundary

This note proves an unbounded structural reduction for the
Kempe-separated branch.  It does **not** prove any of the following.

- The separator in (3.2) has order at most seven.
- The two closed shores attain one common full boundary partition.
- The dominating alternative in (3.3) aligns any colourful set with the
  fixed labels of the spanning `K_7`-minus-one-edge model.
- A proper-minor operation produces a strictly smaller configuration
  preserving all named labels.

Thus the remaining operation is still label-preserving model repair,
colour gluing at an exact order-seven separation, or a strict labelled
descent.

## 6. Dependency

- Hadwiger's Conjecture for parameter six, used only for the upper bound
  in (3.3).
