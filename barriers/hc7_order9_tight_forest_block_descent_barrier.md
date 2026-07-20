# A tight forest with positive excess need not expose a small block boundary

**Status:** explicit counterexample to a local intermediate claim; separate
internal audit GREEN in
[`hc7_order9_tight_forest_block_descent_barrier_audit.md`](hc7_order9_tight_forest_block_descent_barrier_audit.md).
This is not a counterexample to any host-level `HC_7` statement.

## 1. Refuted statement

The following inference is false if one uses only the fixed boundary lists,
vertex-minimal list-uncolourability, shore fullness, the degree-nine lower
bound, and the fact that the tight-vertex graph is a forest:

> A positive-excess shore with a nonempty tight forest has a nontrivial
> tight block whose full neighbourhood has order at most nine.

The four-vertex construction below has one tight block, positive total
excess, and full-neighbourhood order ten for that block.  It shows why the
singleton response in the companion positive theorem cannot simply be
strengthened to an order-seven or order-eight block separator from local
list data alone.

## 2. Construction

Let the nine boundary vertices be divided into six colour classes

\[
       M_1,M_2,M_3,\{p\},\{a\},\{b\},
       \qquad |M_1|=|M_2|=|M_3|=2,                  \tag{2.1}
\]

and give all vertices in one displayed class its displayed colour.  Take
the boundary graph to be edgeless, so this is a proper six-colouring.

Let the shore be the four-cycle

\[
                         x-u-v-y-x.                  \tag{2.2}
\]

For a two-shore realization, add one opposite-shore vertex `d`, adjacent
to all nine boundary vertices and anticomplete to the four-cycle.

Every shore vertex is adjacent to all six vertices in
`M_1 union M_2 union M_3`.  Add the following singleton-boundary
adjacencies:

\[
\begin{array}{c|c|c}
\text{vertex}&\text{seen singletons}&\text{list of missed colours}\\ \hline
u&\{b\}&\{p,a\}\\
v&\{a\}&\{p,b\}\\
x&\{p,b\}&\{a\}\\
y&\{p,a\}&\{b\}.
\end{array}                                           \tag{2.3}
\]

Thus the boundary-induced lists are

\[
 L(u)=\{p,a\},\quad L(v)=\{p,b\},\quad
 L(x)=\{a\},\quad L(y)=\{b\}.                       \tag{2.4}
\]

The list of `d` is empty.  Hence the singleton opposite shore and the
four-cycle shore are both spanning vertex-minimal list obstructions for
the same boundary trace, and both are adjacent collectively to every
literal boundary vertex.

## 3. Verification

The graph in (2.2) is not colourable from (2.4).  The vertices `x,y` are
forced to colours `a,b`, respectively.  Hence `u` is forced to `p`, and
then `v` is also forced to `p`, contradicting the edge `uv`.

It is vertex-minimal non-list-colourable.  Explicit colourings after one
vertex deletion are:

\[
\begin{array}{c|c}
\text{deleted vertex}&\text{colours on the remaining vertices}\\ \hline
x&(u,v,y)=(a,p,b),\\
y&(x,u,v)=(a,p,b),\\
u&(x,v,y)=(a,p,b),\\
v&(x,u,y)=(a,p,b).
\end{array}                                           \tag{3.1}
\]

The internal degree of every vertex is two.  Therefore `u,v` are tight,
while

\[
                         \varepsilon(x)=\varepsilon(y)=1. \tag{3.2}
\]

The tight-vertex graph is the single edge `uv`, hence a forest, and the
total excess is two.  Every vertex has host degree at least nine in the
graph consisting of the shore and boundary: `u,v` have degree nine and
`x,y` have degree ten.  The shore is two-connected and is adjacent,
collectively, to every literal boundary vertex.

For the unique nontrivial tight block `H=G[{u,v}]`, the two internal
attachment vertices are `x,y`, while the only boundary vertex missed by
both `u` and `v` is `p`.  Hence

\[
 N(H)=\{x,y\}\mathbin{\dot\cup}(B-\{p\}),
 \qquad |N(H)|=2+8=10.                               \tag{3.3}
\]

So this block yields neither an order-seven, order-eight, nor order-nine
full-neighbourhood separator.

## 4. Scope

The construction deliberately does not supply a seven-connected,
seven-chromatic, contraction-critical host or all of the operation-specific
colourings of the live endpoint.  It does supply two anticomplete full
shores and paired spanning list obstructions for the fixed trace.  It therefore
does not refute a theorem using those host-level hypotheses.  It refutes
only the local shortcut from positive list-degree excess plus a tight
forest to a small tight-block boundary.  Any stronger conclusion must use
the global `K_7`-minor exclusion or proper-minor response dynamics.
