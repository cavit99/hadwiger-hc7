# Clique-star colouring responses and Kempe separation

**Status:** written proof; separate internal audit GREEN in
[`hc7_clique_star_kempe_separation_audit.md`](hc7_clique_star_kempe_separation_audit.md).

This note isolates a parameter-uniform colouring-space dichotomy behind the
dense degree-eight residue for `HC_7`.  It uses only ordinary Kempe
interchanges and literal connected subgraphs of the host graph.  The final
corollary records exactly what the theorem supplies in the `HC_7` setting and
what remains unproved.

## 1. Uniform response-separation theorem

Let `q` and `m` be integers with `2 <= m <= q`.  Let `G` be a graph that is
not `q`-colourable.  Let

\[
 A=\{a_1,\ldots,a_m\}
\]

be a clique, and let `v` be a vertex outside `A` adjacent in `G` to every
vertex of `A`.  Put

\[
 H=G-\{va_i:i\in[m]\}.
\]

Assume that `H` is `q`-colourable and that every proper `q`-colouring `c` of
`H` satisfies

\[
 \bigl|\{i:c(v)=c(a_i)\}\bigr|=1. \tag{1}
\]

For `i in [m]`, let `C_i` be the set of proper `q`-colourings of `H` for
which `c(v)=c(a_i)`.  We call `C_i` the `i`-th response class.  By (1), the
response classes partition the set of proper `q`-colourings of `H`.

A *Kempe interchange* means interchanging two colours on one connected
component of the subgraph induced by those two colour classes.  Two response
classes are *Kempe-adjacent* if one such interchange takes a colouring in one
class to a colouring in the other.

### Theorem 1 (clique-star response dichotomy)

Under the hypotheses above, exactly one of the following alternatives occurs.

1. **Response transition.** Two response classes are Kempe-adjacent.  More
   precisely, for some distinct `i,j` there is a colouring `c in C_i` such
   that, writing

   \[
   \gamma_r=c(a_r)\qquad(r\in[m]),
   \]

   the component `K` containing `v` in

   \[
   H[c^{-1}(\{\gamma_i,\gamma_j\})]
   \]

   is disjoint from `A`, and interchanging `gamma_i` and `gamma_j` on `K`
   produces a colouring in `C_j`.  Moreover,

   \[
   A\subseteq N_G(K), \tag{2}
   \]

   and the two colourings agree on `N_G(K)`.

2. **Kempe-separated component.** No two response classes are
   Kempe-adjacent.  For every
   proper `q`-colouring `c` of `H`, if

   \[
   \Gamma=c(A)
   \]

   and `D` is the component containing `v` of

   \[
   H[c^{-1}(\Gamma)],
   \]

   then

   \[
   A\subseteq V(D),
   \qquad
   G[D]\text{ is connected},
   \qquad
   \chi(G[D])=m+1. \tag{3}
   \]

If every response class is nonempty, both conclusions genuinely concern all
`m` prescribed responses.  Nonemptiness is not needed for the dichotomy
itself.

### Proof

The alternatives are mutually exclusive by definition.  Suppose first that
there is a Kempe interchange taking `c in C_i` to `c' in C_j`, where `i` and
`j` are distinct.  Let the interchange use colours `alpha,beta` on a
two-colour component `Q`.

Because `A` is a clique, its vertices have pairwise distinct colours in every
proper colouring.  If `Q` contains `v`, then the colour of `v` changes.  Its
new matching vertex `a_j` cannot lie in `Q`, because a vertex of colour
`beta` in `Q` would simultaneously change to `alpha`.  Thus the two colours
used are precisely `c(v)=c(a_i)` and `c(a_j)`.  If `Q` does not contain `v`,
then the colour of `v` stays fixed; changing the unique matching vertex from
`a_i` to `a_j` forces the interchange to swap the colours of `a_i` and
`a_j`.  Again the two colours are precisely `gamma_i` and `gamma_j`.

The edge `a_i a_j` places `a_i` and `a_j` in one component of the
`gamma_i,gamma_j` subgraph.  The component `K` containing `v` is a different
component: in the first case `a_j` lies outside the switched component, and
in the second case `v` lies outside it.  Interchanging the two colours on
`K`, whether or not `K=Q`, leaves all of `A` fixed and changes the colour of
`v` from `gamma_i` to `gamma_j`.  The resulting proper colouring therefore
belongs to `C_j` by (1).

No vertex of `A` lies in `K`: the vertices `a_i,a_j` lie in the other
two-colour component, while every other `a_r` has a colour outside
`{gamma_i,gamma_j}`.  Since `v` lies in `K` and every edge `va_r` belongs to
`G`, (2) follows.  A Kempe interchange on `K` changes no vertex outside `K`,
so in particular the two colourings agree on `N_G(K)`.  This proves the
first alternative in its normalized form.

Now suppose that no two response classes are Kempe-adjacent.  Fix a proper
`q`-colouring `c in C_i`, and let `D` be as in the second alternative.  For
each `j` distinct from `i`, consider the component of

\[
 H[c^{-1}(\{\gamma_i,\gamma_j\})]
\]

containing `v`.  The edge `a_i a_j` places `a_i` and `a_j` in the same
two-colour component.  If the component containing `v` were different,
interchanging its two colours would leave `A` fixed and take `c` from `C_i`
to `C_j`, contrary to the hypothesis.  Hence `v,a_i,a_j` belong to one
two-colour component for every `j`.  Each of those components lies in `D`,
so `A` is contained in `D`.

The graph `H[D]` is connected by the definition of `D`.  Restoring the
deleted star edges cannot destroy connectivity, so `G[D]` is connected.
Moreover, \(A\cup\{v\}\) induces `K_{m+1}` in `G[D]`, giving
\(\chi(G[D])\ge m+1\).  On the other hand, the restriction of `c` to `D-v`
uses only the `m` colours in `Gamma`; retaining those colours and giving `v`
a new colour properly colours `G[D]` with `m+1` colours.  Thus
\(\chi(G[D])=m+1\), proving (3).  ∎

## 2. Separator consequences

The theorem deliberately distinguishes a connected subgraph from a
dominating connected subgraph.

### Corollary 2 (literal separators)

In the transition alternative, if `G-N_G[K]` is nonempty, then
`N_G(K)` is the boundary of an actual separation with both open sides
nonempty.  The two opposite response colourings agree on that boundary.

In the Kempe-separated alternative, if `G-N_G[D]` is nonempty, then
`N_G(D)` is the
boundary of an actual separation with both open sides nonempty.

Consequently, if `G` is `k`-connected, either boundary has order at least
`k`.

### Proof

For either `Y=K` or `Y=D`, the connected set `Y` is anticomplete to
`G-N_G[Y]`; hence `N_G(Y)` separates the two nonempty sets.  In the
transition case the agreement of the two colourings on `N_G(K)` is part of
Theorem 1.  The connectivity bound is immediate.  ∎

The agreement in the transition case is only a common boundary assignment.
It does not by itself prove that independently coloured closed shores can be
glued, nor does a lower bound of seven on the separator order make the
separator an exact order-seven interface.

## 3. Degree-eight dense singleton consequence for `HC_7`

The following is the intended application.  It is phrased so that the
model-preserving deletion hypothesis is explicit rather than hidden in the
terminology.

### Corollary 3 (three-edge dense response dichotomy)

Let `G` be a seven-connected, seven-chromatic, `K_7`-minor-free graph such
that every proper minor of `G` is six-colourable.  Suppose `G` has a spanning
labelled `K_7^-`-minor model whose deficient
branch set is the singleton `{x}`, and suppose `d_G(x)=8`.

Assume the *dense alternative*: whenever two edges incident with `x` can be
deleted simultaneously while preserving this fixed labelled model, their
outer endpoints are adjacent.  Let

\[
 F=\{xa_1,xa_2,xa_3\}
\]

be a maximum set of incident edges whose simultaneous deletion preserves the
model.  Then `|F|=3`, and `a_1a_2a_3` is a triangle.

Put

\[
 H=G-\{xa_1,xa_2,xa_3\}.
\]

Then every six-colouring of `H` matches `x` in colour with exactly one of
`a_1,a_2,a_3`, and each of the three matching responses occurs.  Consequently
one of the following holds.

1. **Transition branch.** For some distinct `i,j`, a connected component
   `K` of a two-colour subgraph of `H` contains `x`, avoids the triangle
   `{a_1,a_2,a_3}`, and has all three triangle vertices in `N_G(K)`.  A Kempe
   interchange on `K` changes the matching response from `i` to `j` and
   leaves the colouring of `N_G(K)` fixed.

   If `K` is not dominating, `N_G(K)` is the boundary of an actual separation
   of order at least seven carrying that common boundary assignment.  If `K`
   is dominating, then `K` is connected and bipartite and

   \[
   \chi(G-K)=5,
   \qquad
   K_6\not\preccurlyeq G-K. \tag{4}
   \]

2. **Four-chromatic separated component.** There is a connected subgraph
   `D` containing
   `x,a_1,a_2,a_3` such that

   \[
   \chi(G[D])=4.
   \]

   If `D` is not dominating, `N_G(D)` is the boundary of an actual separation
   of order at least seven.  If `D` is dominating, then

   \[
   3\le \chi(G-D)\le5,
   \qquad
   K_6\not\preccurlyeq G-D. \tag{5}
   \]

### Proof

By the audited
[deficient-singleton joint-persistence theorem](../results/hc7_deficient_singleton_joint_persistence.md),
a maximum model-preserving incident-edge deletion has order

\[
d_G(x)-(7-2)=3.
\]

Every pair of edges in `F` is itself jointly model-preserving.  The dense
alternative therefore makes every pair of their distinct outer endpoints
adjacent, so `a_1a_2a_3` is a triangle.

Let `c` be a six-colouring of `H`.  If the colour of `x` differed from all
three triangle colours, restoring the three deleted edges would give a
six-colouring of `G`, which is impossible.  Since the three vertices form a
clique, `x` can match at most one of them.  Thus it matches exactly one.

For each `i`, contract the edge `xa_i` in `G`.  The resulting proper minor is
six-colourable.  Expanding its contracted vertex gives a six-colouring of
`G-xa_i` in which `x` and `a_i` have the same colour.  Restricting this
colouring to `H` gives the `i`-th response.  The other two star edges are
still present in `G-xa_i`, so their endpoints have different colours.  Hence
all three response classes are nonempty.

Apply Theorem 1 with `q=6`, `m=3`, `v=x`, and
`A={a_1,a_2,a_3}`.  The non-dominating conclusions follow from Corollary 2
and seven-connectivity.

In the transition branch, `G[K]=H[K]`: the set `K` avoids all three outer
endpoints, so none of the restored star edges has both ends in `K`.
Therefore `G[K]` is connected and bipartite.  If `K` is dominating and
`G-K` contained a `K_6` minor, the connected set `K`, adjacent to every
vertex outside it, would be a seventh branch set of a `K_7` minor.  Hence
`G-K` is `K_6`-minor-free and is five-colourable by the established
`t=6` case of Hadwiger's conjecture.  If it were four-colourable, disjoint
palettes of sizes two and four would six-colour `G`.  This proves (4).

In the Kempe-separated branch, Theorem 1 gives \(\chi(G[D])=4\).  If `D` is
dominating,
the same branch-set argument shows that `G-D` is `K_6`-minor-free, so it is
five-colourable.  It cannot be two-colourable, since disjoint palettes of
sizes four and two would six-colour `G`.  This proves (5).  ∎

## 4. Trust boundary

Theorem 1 is uniform in `q` and in the size of the clique.  It proves that
pairwise Kempe separation of the exact responses forces a connected
`(m+1)`-chromatic subgraph, while a transition supplies two opposite response
colourings agreeing on a literal separator boundary.

The theorem does **not** prove any of the following.

- It does not identify colours with branch-set labels of the preserved minor
  model.
- It does not show that the separator has order exactly seven.
- It does not by itself align proper colourings of both closed shores.
- It does not turn the four-chromatic separated component into a `K_7`
  minor.
- It does not prove that every degree-eight configuration supplies the stated
  dense alternative.  The corollary applies after that alternative has been
  obtained from the separate deficient-singleton reduction.
- It does not use, and must not be read as using, a two-edge saturation
  statement after a third edge has been deleted.  The response conclusion is
  instead derived directly from the exact three-edge graph `H` and the clique
  condition.

Thus the result closes a colouring-space subproblem and produces two
standard graph-theoretic residues—an actual separation or a connected
dominating bounded-chromatic subgraph—but it does not prove `HC_7`.
