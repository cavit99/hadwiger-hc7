# Barrier to a three-pattern extraction from a six-terminal crossing

**Status:** explicit counterexample to an intermediate extraction claim.

This note refutes only the proposed claim that every crossing of the six
terminals in the normalized `2+2` configuration must expose one of three
paths whose interiors avoid both supports and the complete six-path
linkage.  The displayed graph itself has a `K_7` minor, so it does not
refute the desired six-terminal crossing theorem or any case of Hadwiger's
Conjecture.

## 1. Refuted claim

Orient three pairwise disjoint paths as

\[
 P_0:a_0\mathbin{-}p,\qquad
 P_1:a_1\mathbin{-}b_0,\qquad
 P_5:y\mathbin{-}q,
\]

and put

\[
                    T=(a_0,a_1,y,q,b_0,p).
\]

Call a path **linkage-clean** when all its internal vertices avoid
$A\cup B$ and all six paths of the normalized linkage.  The following
extraction claim is false:

> If a graph containing these paths has two vertex-disjoint `T`-paths
> whose four ends alternate in the displayed order, then it contains at
> least one of:
>
> 1. a linkage-clean path from `P_0` to `P_5`;
> 2. two linkage-clean paths from `P_0` to `P_1` whose distinct attachments occur
>    in opposite orders on the two paths; or
> 3. two linkage-clean paths from `P_1` to `P_5` whose distinct attachments occur
>    in opposite orders on the two paths.

Here a single edge with ends on two of the three paths is allowed as an
internally disjoint path.

## 2. Explicit graph

Take

\[
 P_0=a_0p,\qquad P_1=a_1uvb_0,\qquad P_5=yq,
\]

where `u` precedes `v` from `a_1` toward `b_0`.  Add the four edges

\[
                         a_0u,\quad uy,\quad a_1v,\quad vq.       \tag{2.1}
\]

Complete the normalized `2+2` configuration by taking

\[
             P_2=a_2b_1,\qquad P_3=a_3b_2,\qquad P_4=xr,
\]

and retain all normalized support edges, including `a_0a_1`, `pb_0`, and
`qb_0`.
Then

\[
                 a_0-u-y\qquad\hbox{and}\qquad a_1-v-q           \tag{2.2}
\]

are vertex-disjoint paths joining positions `0,2` and `1,3` of `T`, so
they are a crossing of `T`.

Nevertheless none of the three asserted patterns occurs.

- There is no linkage-clean edge, and hence no linkage-clean path, from
  `P_0` to `P_5`.  The path `a_0-u-y` is not linkage-clean because its
  internal vertex `u` lies on `P_1`.  Paths such as
  `a_0-a_2-P_2-b_1-q` are also excluded because their interiors use the
  supports and another linkage path.
- The cross-path edges between `P_0` and `P_1` are `a_0a_1`, `a_0u`, and
  `pb_0`.  Any two with four distinct ends occur in the same order on
  `P_0` and `P_1`, so they are not oppositely ordered.
- The cross-path edges between `P_1` and `P_5` are `uy`, `vq`, and
  `b_0q`.  Again, any two with four distinct ends occur in the same order
  on `P_1` (from `a_1` to `b_0`) and `P_5` (from `y` to `q`).

Every vertex of the completed graph lies in $A\cup B$ or on one of the six
linkage paths.  Consequently a linkage-clean path can only be one of the
single cross-edges just listed.  This proves the counterexample to the
extraction claim.

## 3. Why this is not a barrier to the desired minor theorem

In the same completed normalized configuration, the seven branch sets

\[
\begin{gathered}
 \{b_0\},\quad\{b_1\},\quad\{b_2\},\quad\{r\},\quad\{q\},\\
 \{a_0,p,u,y\},
 \qquad\{a_1,v,a_2,a_3,x\}
\end{gathered}                                                   \tag{3.1}
\]

form a `K_7`-minor model.  The last two sets are connected by (2.1) and
the support edges, and they are adjacent along `uv`.  The first of them
meets the five right-side sets through `p` and `yq`; the second meets them
through `vb_0`, `vq`, `a_2b_1`, `a_3b_2`, and `xr`.  All remaining
adjacencies follow from the clique edges of the two normalized supports.

Thus the failed step is specifically the clean three-pattern extraction.
An arbitrary six-terminal decoder must retain the ordered sequence of
contacts along `P_1`, or use a stronger rooted-minor argument that is
insensitive to that sequence.
