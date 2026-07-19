# A seven-connected sharpness example for tight persistent endpoints

**Status:** explicit counterexample to a static intermediate claim, with a
deterministic verifier in
[`hc7_persistent_edge_tight_endpoint_shadow_verify.py`](hc7_persistent_edge_tight_endpoint_shadow_verify.py).

The graph below is six-colourable and already has both a compatible
order-seven separation and a two-vertex `K_5`-minor transversal.  It is
therefore not a counterexample to the intended terminal theorem or to
Hadwiger's conjecture.  Its role is narrower: it shows that all of the
current *static* alignment data can coexist while every relevant endpoint
has positive list-degree excess.

## 1. The false static claim

The following implication is false.

> Let `G` be a seven-connected `K_7`-minor-free graph with an asymmetric
> order-eight separation, a fixed boundary colouring whose vertex-minimal
> list obstruction fills the full shore, and a spanning labelled
> `K_7`-minus-one-edge model.  Suppose the deficient branch set has at
> least two attachment vertices in one neighbouring branch set.  Suppose
> also that a boundary--shore edge at the deficient branch set has a
> fixed-trace deletion colouring with all five two-colour endpoint paths.
> Then either some deletion-persistent model edge at that vertex has a
> tight endpoint, `G` has a `K_7` minor, or the same boundary trace is
> rejected by a proper induced subgraph of the full shore.

The example refutes all three conclusions simultaneously.  It does not
refute a theorem retaining a compatible order-seven-separation or fixed-pair
terminal outcome: both are present here.  Nor does it refute a theorem that
uses global non-six-colourability or proper-minor criticality.

## 2. The planar core and the exact interface

Take two copies of the icosahedron with one degree-five vertex deleted and
identify their boundary 5-cycles.  Write the common cycle as

\[
                         U=u_0u_1u_2u_3u_4u_0.
\]

The first open disc has vertices `d_B,w_0,...,w_4`, and the second has
vertices `h,r_0,...,r_4`.  For each of the two rims `z_0,...,z_4`, add

\[
 z_iz_{i+1},\qquad dz_i,\qquad u_iz_i,\qquad u_iz_{i-1},
                                                               \tag{2.1}
\]

with subscripts modulo five.  Include the five edges of `U`.  Call the
resulting planar graph `P`.  It is a five-connected spherical
triangulation on 17 vertices.

Add adjacent vertices `a,b`, each complete to `P`, and put

\[
                              G=K_2\vee P.               \tag{2.2}
\]

Then `G` is seven-connected.  It has no `K_7` minor: after discarding the
at most two branch sets that contain `a,b`, a hypothetical seven-branch-set
model would leave a `K_5` model in the planar graph `P`.

Put

\[
\begin{aligned}
 Y&=\{a,b,u_0,u_1,u_2,u_3,u_4\},\\
 X&=Y\cup\{r_0\},\\
 A&=\{d_B,w_0,w_1,w_2,w_3,w_4\},\\
 D&=\{h,r_1,r_2,r_3,r_4\}.
\end{aligned}                                             \tag{2.3}
\]

These sets partition `V(G)`, there is no `A-D` edge, and

\[
                         N_G(A)=Y=X-\{r_0\},
             \qquad      N_G(D)=X.                        \tag{2.4}
\]

Thus this is the literal asymmetric order-eight interface, while `Y` is
already an actual order-seven separator.

## 3. A shore-filling list obstruction with no tight vertex

Use colours `0,...,5`.  On the common cycle, `r_0`, and the two universal
vertices set

\[
\begin{array}{c|ccccc|c|cc}
       &u_0&u_1&u_2&u_3&u_4&r_0&a&b\\ \hline
c      &0&1&0&1&2&3&4&5.
\end{array}                                                \tag{3.1}
\]

This boundary colouring extends through `A` by

\[
 (c(w_0),\ldots,c(w_4),c(d_B))=(2,3,2,0,3,1).             \tag{3.2}
\]

The resulting lists on `D`, obtained by removing the colours of literal
boundary neighbours, are

\[
\begin{array}{c|ccccc}
v&h&r_1&r_2&r_3&r_4\\ \hline
L(v)&\{0,1,2\}&\{2\}&\{2,3\}&\{0,3\}&\{1\}.
\end{array}                                                \tag{3.3}
\]

Call a vertex **tight** when its degree in `G[D]` equals the order of its
list.  The graph `G[D]` is the join of `h` with the path
`r_1r_2r_3r_4`.  It is not `L`-colourable, but deletion of any one of its
vertices makes it `L`-colourable.  Hence the fixed-trace vertex-minimal
obstruction fills the shore.

Nevertheless every vertex has excess exactly one:

\[
                         d_{G[D]}(v)=|L(v)|+1
                         \quad(v\in D).                  \tag{3.4}
\]

There is no tight vertex in the entire obstruction, not merely at a
particular selected edge.

## 4. A spanning near-complete model and three persistent edges

The following seven connected sets partition `V(G)`:

\[
\begin{array}{c|l}
A_0&\{a\}\\
A_1&\{b\}\\
B_0&\{u_2,w_2\}\\
B_1&\{u_3\}\\
B_2&\{w_3\}\\
R&\{d_B,h,r_0,r_1,r_3,r_4,u_0,u_1,u_4,w_0,w_1,w_4\}\\
B&\{r_2\}.
\end{array}                                                \tag{4.1}
\]

They form a spanning `K_7`-minus-one-edge model.  Its only absent
branch-set adjacency is `B_2B`.  In particular `B` is a deficient branch
set and `R` is a neighbouring branch set.  Their cross-edges are exactly

\[
                         r_2h,\qquad r_2r_1,\qquad r_2r_3. \tag{4.2}
\]

Deleting any one of these edges leaves the same labelled model, so all
three are deletion-persistent.  Their three endpoints in `R` are distinct,
and all six endpoint occurrences lie in the fixed-trace obstruction `D`.
By (3.4), none has a tight endpoint.

The response to the fixed trace is itself nonuniform.  Deleting `r_2r_1`
or `r_2r_3` makes `G[D]` list-colourable with the trace (3.1), whereas
deleting `r_2h` does not.  Thus fixed-trace attainment and total
fixed-trace rejection occur on different persistent edges at the same
three-edge star.  The geometry of the labelled model does not select the
attaining edge.

## 5. The aligned boundary edge and all five two-colour paths

Let

\[
                              g=u_3r_2.                   \tag{5.1}
\]

There is a proper six-colouring of `G-g` which agrees with (3.1)--(3.2)
on `A union X` and has

\[
 (c(h),c(r_1),c(r_2),c(r_3),c(r_4))=(0,2,1,3,1).         \tag{5.2}
\]

The ends of `g` both have colour one.  For each other colour there is a
colour-alternating path between them; five pairwise internally disjoint
choices are

\[
\begin{array}{c|l}
0&r_2,u_2,u_3\\
2&r_2,r_1,u_1,w_0,d_B,w_2,u_3\\
3&r_2,r_3,u_3\\
4&r_2,a,u_3\\
5&r_2,b,u_3.
\end{array}                                                \tag{5.3}
\]

Their first hits on `Y`, viewed from `r_2`, lie in

\[
                         \{u_1,u_2,u_3,a,b\},             \tag{5.4}
\]

so the original target support has order five.  The corresponding
prescribed-first-edge six-ended fan inside the `r`-side component is also
explicit: retain `r_2u_3`, and use paths

\[
 r_2u_2,\quad r_2r_1u_1,\quad r_2r_3u_4,
 \quad r_2a,\quad r_2b.                                  \tag{5.5}
\]

Thus the persistent model edges, the fixed-trace critical edge, and the
exact-seven fan data are genuinely aligned at the literal vertex `r_2`.

## 6. Exact trust boundary

The example is six-colourable: a four-colouring of `P` together with two
new colours on `a,b` is recorded in the verifier.  Hence it lacks the
global condition that every edge-deletion colouring must be rejected when
the deleted edge is restored.  In particular, the selected colourings in
Sections 4--5 do not represent the full response language of a
minor-minimal seven-chromatic graph.

Moreover, the separator `Y` has a common labelled boundary trace on its
two closed shores.  The trace

\[
 (u_0,u_1,u_2,u_3,u_4,a,b)=(0,1,0,1,2,4,5)              \tag{6.1}
\]

extends to either punctured icosahedral disc by colouring its rim
`(2,3,2,0,3)` and its hub `1`.  Finally, `G-\{a,b\}=P` is planar, so
`\{a,b\}` meets every `K_5`-minor model.

Consequently the example establishes three sharp points.

1. Shore-filling fixed-trace criticality does not force a tight endpoint
   on a deletion-persistent model edge.
2. Even at one aligned vertex, different persistent edges can realize the
   two opposite fixed-trace alternatives.
3. Positive excess cannot by itself force a `K_7` model or a strict smaller
   fixed-trace obstruction.  A valid theorem must use the compatible
   order-seven/fixed-pair exit when it is present, and otherwise must use
   global non-six-colourability or proper-minor criticality to exclude this
   planar two-apex architecture.
