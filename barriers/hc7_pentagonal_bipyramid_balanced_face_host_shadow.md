# A seven-connected balanced-face shadow with no alternating column split

**Status:** barrier/sharpness example; computer-checked by
[`hc7_pentagonal_bipyramid_balanced_face_host_shadow_verify.py`](hc7_pentagonal_bipyramid_balanced_face_host_shadow_verify.py).
It is not a counterexample to `HC_7` or to the full compatible-separation-or-split
disjunction: it is five-colourable and realizes the compatible order-seven
separation alternative.

## Statement refuted

The following purely structural inference is false.

> Let a seven-connected `K_7`-minor-free graph contain vertices `v,p,w`
> with `vp,pw` edges and `vw` a nonedge, root branch sets `G[{v,p}]` and
> `{w}`, and seven disjoint connected columns spanning the remaining graph,
> each adjacent to both root branch sets and having pentagonal-bipyramid
> contact graph.  If the neighbours of `p` in the columns are confined to
> one facial triangle, then some column has
> a connected split whose two sides attach alternately to four old neighbour
> columns in the cyclic order around that column.

The example below has all of those hypotheses but no such split.  Therefore
seven-connectivity, `K_7`-minor exclusion, and facial-triangle concentration
cannot by themselves discharge the live exchange step.  A proof in a
hypothetical contraction-critical host must use dynamic colouring data to
produce the *other* outcome: a compatible boundary colouring, or a response
whose first contact leaves the facial triangle.

## Construction

Let `I` be the icosahedral graph on vertices `0,...,11`, and put

\[
                   G_0=\overline {K_2}\mathbin\vee I.
\]

Write the two nonadjacent universal vertices as `v,w`, and distinguish the
icosahedral vertex `p=0`.  Thus `vp,pw` are edges and `vw` is not.  Take
the connected root branch sets `G_0[{v,p}]` and `{w}`.  The remaining
eleven vertices are partitioned into seven connected columns as follows:

\[
\begin{array}{c|c}
A_0&\{1,5,11\}\\
A_1&\{9\}\\
R_0&\{7\}\\
R_1&\{8\}\\
R_2&\{2,6\}\\
R_3&\{3,4\}\\
R_4&\{10\}.
\end{array}
\]

Their contact graph is exactly the pentagonal bipyramid:

\[
 A_iR_j\quad(i\in\{0,1\},\ j\in\mathbb Z_5),
 \qquad R_jR_{j+1}\quad(j\in\mathbb Z_5).
\]

Both root branch sets are adjacent to every column.  The distinguished
vertex `p` has neighbours in exactly the three columns

\[
                         A_0,\ R_0,\ R_1.
\]

These three vertices form a facial triangle of the column-contact graph.

## No alternating split

Consider any partition of a nonsingleton column `B` into nonempty connected
sets `B_1,B_2`.  For `k=1,2`, record the old neighbour columns having an edge
to `B_k`.  In the unique plane embedding of the pentagonal bipyramid, these
two incidence sets never alternate around `B`.

This is a finite statement about the displayed literal columns, not merely
about the seven-vertex quotient.  The verifier enumerates every connected
bipartition of each of `A_0,R_2,R_3` and checks the cyclic criterion from the
audited pentagonal-bipyramid vertex-split theorem.  The other four columns
are singletons and cannot be split nontrivially.

For direct inspection, the four unordered connected bipartitions and their
two sets of contacted column labels are

| column | two sides | contact labels of the two sides |
|---|---|---|
| `A_0` | `1 | 5,11` | `R_1,R_2 | R_0,R_2,R_3,R_4` |
| `A_0` | `1,5 | 11` | `R_1,R_2,R_3 | R_0,R_3,R_4` |
| `R_2` | `2 | 6` | `A_0,A_1,R_1,R_3 | A_0,R_3` |
| `R_3` | `3 | 4` | `A_1,R_2,R_4 | A_0,R_2,R_4` |

Reading these sets in the relevant cyclic neighbour order shows directly
that none contains an alternating quadruple.

Hence no column admits the alternating connected split that would create a
`K_5` minor in the column-contact graph and, together with the two roots, an
explicit `K_7`-minor model.

## Host properties and the surviving alternative

The icosahedron is planar and five-connected, so `G_0` is seven-connected.
It has no `K_7` minor: after deleting the at most two branch sets meeting
`v,w`, a putative `K_7` model would leave a `K_5` model in the planar graph
`I`.

The example deliberately realizes the opposite terminal outcome.  Every
icosahedral vertex has degree seven in `G_0`.  In particular

\[
 S=N_{G_0}(p)=\{v,w,1,5,11,7,8\}
\]

is the boundary of an actual order-seven separation with both open shores
nonempty.  Since `I` is four-colourable and `v,w` can share one fresh
colour, `G_0` is five-colourable.  Restricting one global colouring to the
two closed shores gives exactly the same boundary partition on `S`.

Thus the example does not refute the desired disjunction.  It proves that
its alternating-split arm is not a consequence of the static host geometry.
The first indispensable contraction-critical step is a **response-transfer
lemma**: using a second operation-specific proper-minor colouring, one must
either obtain a first contact outside the facial triangle or reproduce one
boundary equality partition on both closed shores.  A single response,
facial concentration, and seven-connectivity do not supply that step.

## Trust boundary

This construction realizes the root/column setup of the audited
spanning-core theorem: the root branch sets have the required `v-p-w`
pattern, the columns span the rest of the graph, and the host is
seven-connected and `K_7`-minor-free.  Its induced column core is planar,
whereas seven-chromaticity makes the core in that theorem nonplanar.  It
also does not realize the operation-specific response family because it is
five-colourable rather than seven-contraction-critical.  Those omitted
chromatic and dynamic hypotheses are precisely where a positive theorem
must act.
