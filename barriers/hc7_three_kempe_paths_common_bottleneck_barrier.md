# Three colour-indexed paths need not have a common bottleneck

**Status:** dependency-free finite barrier.  This is not a counterexample to
`HC_7` or to the boundary-edge Kempe theorem.  It refutes the abstract next
step

\[
 \text{three colour-indexed }b\text{--}I\text{ paths intersect only in
 alpha-coloured vertices}
 \Longrightarrow
 \begin{cases}
 \text{three internally disjoint paths},\text{ or}\\
 \text{one common internal alpha bottleneck}.
 \end{cases}
\]

## Construction

Take alpha-coloured vertices

\[
                  b,i_0,i_1,x_{12},x_{23},x_{31}
\]

and, for each `k in {1,2,3}`, three vertices
`u_k,v_k,w_k` of a private colour `beta_k`.  Add exactly the edges of the
following three paths:

\[
\begin{aligned}
 P_1&=b-u_1-x_{12}-v_1-x_{31}-w_1-i_0,\\
 P_2&=b-u_2-x_{12}-v_2-x_{23}-w_2-i_1,\\
 P_3&=b-u_3-x_{23}-v_3-x_{31}-w_3-i_0.
\end{aligned}                                                    \tag{1.1}
\]

Each `P_k` is an alpha--`beta_k` path from `b` to
`I={i_0,i_1}`.  For distinct indices, every common internal vertex is
alpha-coloured.  The three pairwise intersections are carried by three
different vertices:

\[
 P_1\cap P_2\supseteq\{x_{12}\},\qquad
 P_2\cap P_3\supseteq\{x_{23}\},\qquad
 P_3\cap P_1\supseteq\{x_{31}\}.                         \tag{1.2}
\]

There is no common internal vertex.  Nor are there three internally
disjoint `b-I` paths in their union.  Indeed, `b` has the three neighbours
`u_1,u_2,u_3`, but every path beginning with either `bu_1` or `bu_2` must
next use `x_{12}`.  A family of three would have to use both initial edges
and would therefore intersect internally at `x_{12}`.

The minimum internal separator between `b` and `I` in this union has order
two.  For example `{x_{12},x_{23}}` is a separator.  No single internal
vertex is a separator: deleting `x_{12}`, `x_{23}`, or `x_{31}` leaves,
respectively, `P_3`, `P_1`, or `P_2`, and deleting a private-colour vertex
leaves the other two displayed paths.

## Exact consequence

The absent-colour paths supplied by the boundary-edge Kempe theorem may
have a pairwise-intersection triangle rather than one common first portal.
Even when a separator of order two exists in the **union of the selected
paths**, it is not a separator of the host graph: edges and paths using the
other palette colours are not represented in (1.1).

Thus a positive continuation must apply a host-level operation at an
actual connected component or use the five labelled row subgraphs to
control every bypass.  It cannot promote a separator of the selected
Kempe-path union to a full-neighbourhood separator of `G`.

There is an even simpler warning when a common alpha vertex really does
exist.  Use the three paths

\[
                 b-u_k-x-v_k-i_0\qquad(k=1,2,3),       \tag{2.1}
\]

where `b,x,i_0` have colour `alpha` and `u_k,v_k` have the private colour
`beta_k`.  Every displayed absent-colour path uses `x`.  Add a path

\[
                              b-s-t-i_0                \tag{2.2}
\]

whose two internal vertices use two other colours.  The addition does not
change any of the three alpha--`beta_k` subgraphs, but `x` is no longer a
host separator.  Arbitrarily many such other-colour bypasses may be added.
Consequently even a genuine common vertex of all selected absent-colour
paths is not, without a separate completeness argument, a connected split
or a full-neighbourhood separator in the host.
