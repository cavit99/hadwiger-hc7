# Two barriers to the partial-loss chromatic lift

**Status:** explicit barriers to two intermediate inferences; separate
internal audit GREEN.

These examples delimit the attachment-hull and bipartite-fibre theorem.
They are not seven-connected strongly contraction-critical counterexamples
and do not refute the atomic common-frame target.

## 1. A contraction colouring need not expand through a tree fibre

Consider three vertices `r_0,r_1,r_2` spanning a triangle and take

\[
                         F_0=\{r_0r_1,r_1r_2\}.         \tag{1.1}
\]

The edge set `F_0` is a two-edge tree.  Contracting all of it identifies
the three vertices.  The remaining chord `r_0r_2` becomes a loop and is
suppressed in the simple quotient.  Consequently any proper colouring of
the quotient gives the three original vertices one common colour when it
is naively expanded.

That expansion is not a colouring of `G-F_0`: the edge `r_0r_2` remains
there and has monochromatic ends.  Thus the matching argument

> colour every nonempty contraction of `F_0`, expand it to `G-F_0`, and
> read off the contracted edges as the exact equality set

is false for a multi-edge tree.  The displayed triangle is the smallest
possible obstruction.  More generally, any non-forest edge whose ends lie
in one contracted `F_0`-component is suppressed as a loop and can invalidate
the expansion.

There are two distinct trust boundaries here.  Even a chord joining
opposite classes of the tree bipartition blocks the naive all-equal
expansion.  By contrast, such a chord does not block the two-colour fibre
lift in the bipartite-fibre theorem.  The latter fails precisely when the
induced fibre is non-bipartite; the triangle above is again the smallest
case.

## 2. Arbitrarily many selected contacts need not give three clean supports

Let

\[
                H_0=(K_7-\{ab,cd\})+\{xa,xb,xc,xd\},
\]

and let `T_n` be the subdivision obtained by replacing the segment `ef`
with

\[
                      e-p_1-p_2-\cdots-p_n-f,
                      \qquad n\ge5.                   \tag{2.1}
\]

Add new vertices `y,l_1,...,l_n` and the edges

\[
                         xy,\qquad yl_i,\qquad l_ip_i
                         \quad(1\le i\le n).           \tag{2.2}
\]

Call the resulting graph `G_n`, and put

\[
                  X=G_n[\{x,y,l_1,\ldots,l_n\}].       \tag{2.3}
\]

The graph `X` is a tree, it meets `T_n` exactly in `x`, and each leaf
`l_i` carries its own selected contact to the distinct attachment `p_i`.
It is minimal as a connected subgraph containing `x` and all the
contact-owning vertices `l_i`.

Every `p_i` has endpoint support `\{e,f\}`.  The other attachments supplied
by the vertex `x` are `a,b,c,d`, none of which has a clean-root support.
Therefore the clean-incidence graph with left side `\{e,f,g\}` has

\[
                   N(e)=N(f)=\{p_1,\ldots,p_n\},
                   \qquad N(g)=\varnothing,            \tag{2.4}
\]

and its maximum matching has order two.  This remains true for arbitrarily
large `n`.

### Proposition 2.1

The graph `G_n` has no `K_7` minor.

#### Proof

Delete `e` and `f`.  The six branch vertices

\[
                          x,g,a,b,c,d
\]

induce the octahedral graph `K_{2,2,2}`, with parts
`\{x,g\},\{a,b\},\{c,d\}`.  The remaining vertices in (2.1)--(2.2) form
a subdivided fan: `p_1\ldots p_n` is its rim path and every spoke from the
hub `y` to `p_i` is subdivided by `l_i`.  This fan is planar and is joined
to the octahedron only by the bridge `xy`.  Hence `G_n-\{e,f\}` is planar.

If `G_n` had a `K_7` model, discarding the at most two branch sets that
contain `e` or `f` would leave a `K_5` model in the planar graph
`G_n-\{e,f\}`, which is impossible.  \(\square\)

Thus five selected contacts cannot be converted into the clean three-arm
closure by counting.  The attachment-hull theorem adds the stronger fact
that its forest leaves meet every lifted component, but it still supplies
no map from those leaves to distinct endpoint supports on `T_n`.  A
successful use of those common leaves must separately prove literal support
diversity: it must place contacts in all three clean-root incidence classes,
rather than merely route many leaves to one clean--clean segment.

## 3. Exact scope

The triangle in Section 1 blocks a colouring expansion, not a theorem that
uses the non-bipartite fibre geometrically.  The family in Section 2 is
low-connectivity and does not impose the first-loss separator or the
proper-minor colouring responses.  It proves only that neither a large
number of tree leaves nor a large number of distinct attachments forces a
clean-root matching without a separate label-preserving argument.
