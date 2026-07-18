# One missing far-side contact defeats the local three-path inference

**Status:** computer-assisted barrier to an intermediate local claim;
separate internal audit GREEN.  The adjacent deterministic script checks
all displayed incidences and uses an exact SMT encoding for `K_7`-minor
exclusion.  This graph is not a counterexample to `HC_7`.

## 1. The overstrong claim refuted

The following local inference is false without the complete five-subgraph
geometry on the opposite side:

> A literal four-root cycle, five cyclically adjacent connected sets, a
> common blocker-edge six-colouring with three absent-colour paths, and one
> three-connected far-side subgraph meeting almost all boundary labels force
> a `K_7` minor.

The example below retains all of those data, and the far-side subgraph meets
six of the seven boundary labels.  Its sole missed label is indispensable:
adding any contact to that label which is compatible with the displayed
colouring creates a `K_7` minor.

## 2. Construction

Use the eighteen vertices

\[
 U=\{u_0,u_1,u_2,u_3\},\quad B=\{b_0,b_1,b_2\},\quad
 X=\{x_0,\ldots,x_4\},\quad Y=\{y_0,\ldots,y_4\},\quad\{v\}.
\]

Make `U` a four-cycle and `X` a five-cycle.  Add `u_i x_i` for
`0<=i<=3`, make `v` adjacent to `X` and every vertex of `B`, make each of `b_1,b_2`
adjacent to all of `X`, and make `b_0` adjacent precisely to `x_3,x_4`
inside `X`.

On `Y`, take the wheel with hub `y_0` and rim
`y_1y_2y_3y_4y_1`.  Add

\[
 b_1u_0,\qquad b_1y_ku_0\ (1\le k\le3),\qquad
 y_1u_1,y_1u_2,y_1u_3,y_1b_2.                         \tag{2.1}
\]

There are no other edges.

Put

\[
 I=\{u_0,u_2\},\qquad J=\{u_1,u_3\}.
\]

After deleting the blocker edge `b_1u_0`, the following is a proper
six-colouring:

\[
\begin{array}{c|l}
0&b_0,b_1,u_0,u_2,y_0\\
1&b_2,u_1,u_3,y_4\\
2&v,y_1\\
3&x_0,x_3,y_2\\
4&x_1,x_4,y_3\\
5&x_2.
\end{array}                                             \tag{2.2}
\]

Thus `I union {b_1}` is monochromatic, `J union {b_2}` is
monochromatic in a different colour, and the internal vertices of

\[
 b_1y_1u_0,\qquad b_1y_2u_0,\qquad b_1y_3u_0             \tag{2.3}
\]

have three colours absent from `U union B`.

The five sets

\[
 \{u_0,x_0\},\ \{u_1,x_1\},\ \{u_2,x_2\},\
 \{u_3,x_3\},\ \{x_4\}                                \tag{2.4}
\]

are pairwise disjoint, connected, and cyclically adjacent.  They contain
the four roots separately and all five neighbours of `v` in `X`.  The
subgraph on `Y` is three-connected and is adjacent to every member of
`U union B` except `b_0`.

## 3. Exact finite conclusions

The checker verifies that this graph has no `K_7` minor.  It also verifies
that adding any one of

\[
 b_0y_1,\quad b_0y_2,\quad b_0y_3,\quad b_0y_4           \tag{3.1}
\]

creates a `K_7` minor.  These are exactly the possible new `b_0`--`Y`
contacts compatible with (2.2); `b_0` and `y_0` have the same colour.

Consequently, the local obstruction is not the existence of the three
paths or internal three-connectivity.  It is the missing labelled contact
to the far side.  A positive compression theorem must preserve the full
five named connected subgraphs (or use contraction-criticality to create
the missing contact), rather than replacing them by an almost-full
unlabelled connected subgraph.

## 4. Scope not refuted

The graph has vertex-connectivity three, is six-colourable after one edge
deletion, and is not asserted to be contraction-critical.  The `Y`-subgraph
misses `b_0` and does not realize the five pairwise-adjacent far-side
subgraphs.  Hence the example does not refute any theorem that retains
seven-connectivity, the complete five-subgraph structure, or the universal
proper-minor colouring constraints of a hypothetical `HC_7` counterexample.
