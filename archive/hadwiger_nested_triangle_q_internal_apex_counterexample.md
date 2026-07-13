# The neutral triangle does not determine the apex pair

## Proposition

There is a seven-connected `K_7`-minor-free graph `G`, a triangle `Q`,
three literal common neighbours of `Q`, and a connected spanning shell
piece meeting all three `Q`-portal sets, such that deleting any two
vertices of `Q` leaves a nonplanar graph.  Nevertheless `G` is two-apex.

Thus a connected-set strengthening of the nested-triangle theorem may
return **some one global apex pair**, but it cannot require that pair to
lie in the initially chosen neutral triangle.

## Construction

Let `I` be the icosahedron and let `p,q` be two new adjacent vertices
complete to `I`.  Thus

\[
                             G=K_2\vee I.
\]

Choose an edge `uv` of `I` and put `Q={p,u,v}`.  The edge `uv` lies in
exactly two triangular faces of `I`; call their third vertices `r,s`.
Then

\[
                              q,r,s
\]

are three literal common neighbours of `Q`.  Put `H=G-Q` and

\[
                   B=V(H)-\{q,r,s\}.
\]

The graph `I-{u,v,r,s}` is connected, so `B` is a connected shell piece.
It meets the `p`-portal set because `p` is universal, and it meets both
the `u`- and `v`-portal sets because each endpoint of an icosahedron edge
has two neighbours outside the two incident facial triangles.  It also
meets each of the three literal common-root bags.

## Verification of the alternatives

The icosahedron is five-connected, and the join formula for connectivity
gives

\[
                         \kappa(K_2\vee I)=2+5=7.
\]

It is planar and has Hadwiger number four.  The join formula for clique
minors therefore gives

\[
                         \eta(K_2\vee I)=2+4=6,
\]

so four pairwise adjacent bags in `H` all adjacent to `Q` cannot exist:
with the three singleton bags of `Q` they would be a `K_7` model.

No pair internal to `Q` is an apex pair.  Deleting `p,u` leaves
`q\vee(I-u)`, with 36 edges on 12 vertices, exceeding the planar bound
30; the case `p,v` is symmetric.  Deleting `u,v` leaves `K_2` joined to
`I-{u,v}`; the latter still contains a triangle disjoint from `uv`, so
the remainder contains a `K_5`.

On the other hand

\[
                            G-\{p,q\}=I
\]

is planar.  The coherent pair is `{p,q}`, with `q` appearing as a common
shell root rather than a member of the selected neutral triangle.

The dependency-light verifier
`nested_triangle_q_internal_apex_counterexample.py` checks the displayed
connectivities, portal incidences, connected piece, all three failed
`Q`-internal pairs, and the true global apex pair.

## Exact lesson

The planar/cofacial outcome must be global and model-flexible.  A correct
uniform principle has to do one of two things:

1. return an arbitrary coherent apex pair; or
2. realign the near-`K_7` model before applying the nested-triangle
   theorem.

For this example the realignment is explicit: choose
`Q'={p,q,z}` for any `z in V(I)`.  Then

\[
 N_{G-Q'}(z)\subseteq
 N_{G-Q'}(p)\cap N_{G-Q'}(q),
\]

and the audited nested-triangle theorem returns the correct pair
`{p,q}`.
