# Oppositely ordered missing-colour paths need not repair the rooted model

**Status:** computer-assisted counterexample to a proposed intermediate
model-repair claim.  The deterministic verifier is
[`hc7_balanced_order8_two_missing_colour_paths_verify.py`](hc7_balanced_order8_two_missing_colour_paths_verify.py).
This graph is a quotient-level obstruction, not a counterexample to
`HC_7` or to the live balanced order-eight completion theorem.

## 1. Claim ruled out

The following inference is false without the literal split-edge and global
criticality hypotheses.

> Let `L=R union {a,b}` be a five-clique and put `g=ab`.  Suppose a proper
> six-colouring of `H-g` gives `a,b` one colour, gives the vertices of `R`
> three other colours, and the two colours absent from `L` each supply an
> `a-b` Kempe path.  Suppose also that the two contracted defect vertices
> occur in the canonical rooted-web configuration, with two connected
> boundary-full sides and a second five-clique.  Then the two nontrivial
> Kempe paths repair the missing rooted `K_4`, and hence force the intended
> `K_7`-minor construction.

The graph below satisfies all of this quotient data and is `K_7`-minor-free.
It has both a colouring locked at `g` against every ordinary Kempe
interchange and a simultaneous-equality colouring for two deleted clique
edges in which the two opposite cyclic orders give directed replacement
paths.  In the latter colouring the three-colour component containing the
ends of `g` is itself strongly connected.  Its significance is narrow but
sharp: even the ordered-path/SCC strengthening can live on the planar side
of the canonical web and need not interact with either deficient branch
set.

## 2. The eighteen-vertex graph

Start from the capped pentagonal-antiprism presentation of the icosahedron,
with vertices

\[
 p,q,A_0,\ldots,A_4,B_0,\ldots,B_4
\]

and, with subscripts modulo five, edges

\[
 A_iA_{i+1},\quad B_iB_{i+1},\quad pA_i,\quad qB_i,
 \quad A_iB_i,\quad A_{i+1}B_i.
\tag{2.1}
\]

Delete `pA_0` and `pA_1`.  Add a triangle `X={u,v,w}` and make every
vertex of `X` adjacent to each vertex of

\[
                         T=\{p,A_1,A_2\}.              \tag{2.2}
\]

Call the resulting fifteen-vertex graph `Q`.  Finally add a triangle
`R={r_0,r_1,r_2}`, make every member of `R` adjacent to each of

\[
                         A_0,A_4,p,A_1,                 \tag{2.3}
\]

and add the three edges

\[
                         r_0u,\quad r_1v,\quad r_2w.    \tag{2.4}
\]

The resulting graph is `H`.  Put

\[
 a=A_0,\qquad b=A_4,\qquad c=p,\qquad d=A_1,
 \qquad t=A_2.                                        \tag{2.5}
\]

Then

\[
 L=R\cup\{a,b\},\qquad Y=\{c,t,u,v,w\}               \tag{2.6}
\]

are disjoint literal five-cliques.  The four nominated vertices have the
defect pattern

\[
 ac,bd,cd\notin E(H),\qquad ab,ad,bc\in E(H).          \tag{2.7}
\]

Moreover, deleting the six-set `R union T` leaves exactly two connected
components,

\[
 X
 \quad\hbox{and}\quad
 \{q,A_0,A_3,A_4,B_0,B_1,B_2,B_3,B_4\},               \tag{2.8}
\]

and both are adjacent to every literal vertex of `R union T`.  Thus (2.8)
is the contracted analogue of the two full sides at the live order-eight
separator.

The graph `Q` is three-connected and its unique three-vertex cut is `T`.
It has the two linkages

\[
 (ab,cd),\qquad(ad,bc),                                \tag{2.9}
\]

but no `(ac,bd)` linkage.  Hence it has no `K_4` minor rooted at
`a,b,c,d`.  The extra five-clique `Y` is localized behind the same cut and
does not change this conclusion.

## 3. A fully locked edge-deletion colouring

Delete `g=ab`.  The following are the colour classes of a proper
six-colouring of `H-g`:

\[
\begin{array}{c|l}
0&A_0,A_4,A_2,q\\
1&A_1,B_2,p,B_4\\
2&B_0,B_3,u\\
3&B_1,A_3,v,r_0\\
4&w,r_1\\
5&r_2.
\end{array}                                             \tag{3.1}
\]

The clique `L-g` uses the four colours `0,3,4,5`; its two absent colours
are `1,2`.  Their nontrivial Kempe paths are

\[
 A_0-B_4-A_4,qquad
 A_0-B_0-q-B_3-A_4.                                    \tag{3.2}
\]

Both paths lie wholly in the large component of (2.8).  For the other
three colours the paths

\[
 A_0-r_i-A_4\qquad(i=0,1,2)                            \tag{3.3}
\]

show that `a,b` belong to one `0-j` Kempe component for every
`j in {1,...,5}`.  Consequently no single Kempe interchange applied to
(3.1) gives `a,b` different colours: an interchange involving colour zero
changes both or neither endpoint, while an interchange avoiding zero
changes neither endpoint.

Nevertheless the target `(ac,bd)` linkage in `Q` is absent.  Thus even the
complete five-colour edge lock, including both nontrivial missing-palette
paths, does not itself decode the missing labelled branch-set adjacency.

There is a second, more local failure which is relevant to the current
two-path completion.  Delete the canonical cut `T={c,d,t}` and let `C_0`
be the component containing `a,b`.  In the closed subgraph

\[
                         Q[C_0\cup\{c,t\}],
\]

there are no two vertex-disjoint paths joining `b` to `t` and `a` to `c`,
respectively.  Thus the two Kempe paths in (3.2) do not force even the
clique-side linkage which, after lifting `c` back to a literal defect edge,
would give the explicit seven-branch-set construction.  The verifier checks
this assertion directly.

## 4. A simultaneous-equality colouring with both cyclic orders

There is a stronger colouring obstruction in the same graph.  Put

\[
                          h=uv,
\]

where `u,v` are two vertices of the second five-clique `Y`, and delete both
`g` and `h`.  The following classes form a proper six-colouring `kappa` of
`H-{g,h}`:

\[
\begin{array}{c|l}
0&A_0,A_4\\
1&A_1,A_3,B_4\\
2&p,B_0,B_3\\
3&q,A_2,r_0\\
4&B_1,w,r_1\\
5&B_2,u,v,r_2.
\end{array}                                             \tag{4.1}
\]

Thus both deleted edges are monochromatic:

\[
                 \kappa(A_0)=\kappa(A_4)=0,
        \qquad   \kappa(u)=\kappa(v)=5.                \tag{4.2}
\]

The reserved triangle `R` has colours `3,4,5`, so the colours absent from
`L-g` are `1,2`.  Orient every edge of the subgraph induced by colours
`0,1,2` from colour `0` to `1`, from `1` to `2`, and from `2` to `0`.
Then

\[
       A_0-B_4-B_3-A_4                               \tag{4.3}
\]

is a directed path for the cyclic order `(0,1,2)`, while

\[
       A_4-B_4-B_0-A_0                               \tag{4.4}
\]

is a directed path in the same orientation.  Equivalently, reversing
(4.4) gives the `A_0-A_4` path for the opposite cyclic order `(0,2,1)`.
Consequently the two ends of `g` lie in one strongly connected component
of this cyclic orientation.

In fact that strongly connected component is the entire connected
three-colour component containing `A_0,A_4`:

\[
  \{A_0,A_4,A_1,A_3,B_0,B_3,B_4,p\}.                  \tag{4.5}
\]

Both directed replacement paths in (4.3)--(4.4) remain on the large,
planar-skeleton side of the canonical cut.  Hence replacing the two
ordinary missing-colour paths by the oppositely ordered generalized-Kempe
paths, or even by the strongly connected cyclic component (4.5), still
does not force the absent rooted linkage.

This is exactly a simultaneous `(equal,equal)` trace for two deleted edges
of the two displayed five-cliques.  It is not a full instance of the
two-edge fork theorem, because the ambient graph is six-colourable; in
particular the forbidden `(proper,proper)` condition supplied by a genuine
seven-chromatic host is absent.

There is also a simultaneous-equality colouring which realizes the exact
disjoint-palette coupling theorem.  Keep `h=uv` and use

\[
\begin{array}{c|l}
0&A_0,A_2,A_4\\
1&A_1,B_4,p\\
2&B_0,B_3,w\\
3&A_3,B_1,r_0\\
4&B_2,r_1\\
5&q,r_2,u,v.
\end{array}                                             \tag{4.6}
\]

Now the natural supports of the two deleted clique edges are the disjoint
sets

\[
                \Omega_g=\{0,1,2\},\qquad
                \Omega_h=\{3,4,5\}.                    \tag{4.7}
\]

The edge `g` is locked in both cyclic orientations, witnessed by

\[
\begin{aligned}
 A_0-B_4-B_3-A_4
      &\quad(0,1,2,0),\\
 A_0-B_0-B_4-A_4
      &\quad(0,2,1,0).
\end{aligned}                                           \tag{4.8}
\]

For `h`, the cyclic order `(5,3,4)` has the path

\[
                         u-r_0-r_1-v,                   \tag{4.9}
\]

whereas `v` is not reachable from `u` in the reverse `(5,4,3)`
orientation.  Rotating the latter reachable set makes `h` proper while
leaving `g` equal, exactly as in the response-plus-path outcome of the
coupling theorem.  The paths in (4.8) are automatically disjoint from
(4.9), because their supports are disjoint.

Thus the canonical rooted-web quotient can realize the full conclusion of
the disjoint-palette coupling theorem—one edge locked in both directions,
the other supplying a disjoint ordered path and an opposite response—while
remaining `K_7`-minor-free.  What is absent is again the full host input:
literal split defect edges, seven-connectivity, and minor-critical
incompatibility of the boundary traces.

## 5. Minor exclusion and exact scope

The verifier encodes a spanning seven-branch-set clique model by Boolean
membership variables and integral connectivity flows.  Symmetry is removed
by ordering the least vertex in each branch set.  It returns `UNSAT` for
`H` and `SAT` for a positive `K_7` control.  Hence `H` has no `K_7` minor.
The spanning formulation is sound because `H` is connected: every unused
component of any clique-minor model can be absorbed along a path to an
existing branch set.

This example deliberately stops before the hypotheses that may still force
the live conclusion:

- `c,d` are contracted defect vertices, not two literal edges with four
  independently placed endpoints;
- `H` is only five-connected, not seven-connected;
- `H` is six-colourable and is not contraction-critical; and
- a low-order cut can be enlarged to an actual order-seven separation.

Accordingly it does not refute the full alternative “`K_7` minor, common
boundary colouring, or strict order-seven separation.”  It does refute the
proposed constructive engine in isolation.  Any surviving theorem must use
the literal endpoint distribution together with seven-connectivity or a
  proper-minor transition; the two ordered missing-colour paths and their
  strongly connected cyclic component cannot be treated as the missing
  rooted linkage.
