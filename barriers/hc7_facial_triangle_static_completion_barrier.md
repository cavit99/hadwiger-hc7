# A facial critical triangle does not complete the model from static data

**Status:** computer-assisted counterexample to an intermediate claim.  The
deterministic verifier is
[`hc7_facial_triangle_static_completion_barrier_verify.py`](hc7_facial_triangle_static_completion_barrier_verify.py).
This graph is not a counterexample to `HC_7`.

## 1. Claim ruled out

The following static inference is false.

> In the balanced order-eight configuration, suppose the two open shores
> are connected and adjacent to every boundary vertex, the complement of
> the boundary graph has a perfect matching, the two named disjoint
> five-cliques exist, and the contracted four-root graph is three-connected
> with the canonical missing same-index linkage.  If a fixed-boundary
> critical core on the first shore is the facial triangle on the outer
> edge, with one common two-element list, then the displayed data force a
> `K_7` minor.

The example below satisfies all of those hypotheses except the cut
rigidity inherited from seven-connectivity.  It has no `K_7` minor.  Thus
the facial triangle cannot be closed by its boundary contacts, the two
five-cliques, or the abstract web obstruction alone.  A valid completion
theorem must use the fact that every three-cut of the contracted graph has
the prescribed two vertices (equivalently, the corresponding forbidden
small separations in the original host), or must use proper-minor
colouring transitions.

## 2. Construction

Let

\[
 R=\{r_0,r_1,r_2\},\quad e=e_0e_1,\quad f=f_0f_1,
 \quad S=R\mathbin{\dot\cup}V(e)\mathbin{\dot\cup}V(f)
          \mathbin{\dot\cup}\{x\}.
\]

Make `R` a triangle, and make `e` and `f` edges which are anticomplete to
one another.  Their nonneighbour sets in `R` are

\[
\begin{array}{c|cccc}
z&e_0&e_1&f_0&f_1\\ \hline
R-N(z)&\{r_2\}&\{r_0,r_1\}&\{r_2\}&\{r_0,r_1\}.
\end{array}                                           \tag{2.1}
\]

The first open shore is the triangle `C={a,b,w}`.  Make `a,b` complete to
`R`, add

\[
             af_0,\ af_1,\ be_0,
\]

and make `w` adjacent to every vertex of `S` except `r_1,f_0`.

The second open shore is the five-clique

\[
                         D=\{y_0,y_1,y_2,y_3,y_4\}.
\]

Make `y_0` adjacent to every vertex of `S`, and add the two further edges

\[
                         y_1e_0,\qquad y_2x.           \tag{2.2}
\]

There are no edges between `C` and `D`.  This completes the construction.

## 3. Verified properties

Both components of `G-S` are connected and adjacent to every vertex of
`S`.  The sets

\[
              L=R\cup\{a,b\},\qquad Y=D
\]

are disjoint five-cliques.  Relative to `L`, the edge `e` is anticomplete
to `a` and collectively adjacent to `L-\{a\}`; symmetrically `f` is
anticomplete to `b` and collectively adjacent to `L-\{b\}`.  The endpoint
nonneighbour sets in (2.1) are nonempty and disjoint for each edge.

The complement of `G[S]` has the perfect matching

\[
        f_1r_1,\quad r_2e_0,\quad xr_0,\quad f_0e_1.  \tag{3.1}
\]

Delete `ab`.  The following colour classes form a proper six-colouring:

\[
\begin{array}{c|l}
0&a,b,y_0\\
1&w,y_1\\
2&r_0,e_1,y_2\\
3&r_1,f_1,y_3\\
4&r_2,x,y_4\\
5&e_0,f_0.
\end{array}                                           \tag{3.2}
\]

With the boundary fixed by (3.2), each of `a,b,w` sees precisely the four
boundary colours `2,3,4,5`.  Hence the triangle `abw` has the common list
`{0,1}` and is a vertex-minimal non-list-colourable induced subgraph
containing `ab`.  Moreover `A=C-\{a,b\}=\{w\}` is connected, both leaves
and `x` meet it, it contacts both defect edges, and it misses exactly two
boundary vertices including a member of `R`.  Thus this is exactly the
zero-slack triangular fixed-boundary core, not merely a triangle in the
underlying graph.

Delete `R` and contract `e,f` to `z_e,z_f`.  The resulting graph `Q` is
three-connected.  For the four roots `(a,b,z_e,z_f)`, it contains the
linkages

\[
                    (ab,z_ez_f),\qquad(az_f,bz_e),
\]

but no `(az_e,bz_f)` linkage.  Consequently the rooted Two Paths theorem
places `Q` in an `(a,b,z_e,z_f)`-web.  The triangle `abw` belongs to the
planar skeleton: an attachment vertex cannot be adjacent to all four
outer roots, whereas `w` is.  It is nonseparating in `Q`, so it is the
bounded facial triangle incident with the outer edge `ab`.

Finally, the exact branch-set solver returns `UNSAT` for a `K_7` minor in
`G`.

## 4. Exact trust boundary

The host has vertex-connectivity three, not seven.  More specifically,
the contracted graph has three-cuts other than sets containing both
`z_e,z_f`; for example `\{y_0,y_1,x\}` separates
`\{y_2,y_3,y_4\}`.  This is precisely the hypothesis excluded by the
audited canonical-web reduction in a hypothetical counterexample.

The graph is also six-colourable and is not contraction-critical.  It
therefore does not refute a facial-triangle completion theorem which
genuinely uses seven-connectivity/cut rigidity or incompatible proper-minor
colouring languages.  It does refute treating the common-list facial
triangle as an automatic labelled branch-set completion.

## 5. Verification

From the repository root, run

```text
PYTHONPATH=active/runtime/deps \
python3 barriers/hc7_facial_triangle_static_completion_barrier_verify.py
```

The verifier checks all stated adjacencies, the boundary matching, the
six-colouring and exact lists, both open-shore conditions, the three rooted
linkage assertions, the facial-triangle certificate, the relevant
three-cut, and exact `K_7`-minor exclusion.
