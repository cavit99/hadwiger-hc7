# Stable-theta allocation for the four-root degree-eight disk

**Status:** written proof; separate internal audit.

This note closes the two root-clustering patterns left by the
[Hamiltonian-cycle reduction](../results/hc7_rooted_hamiltonian_cycle_reduction.md).
It does not reselect the
Hamiltonian cycle.  Instead it uses four internally disjoint paths between
the two deleted vertices and the standard stable-bridges theorem of Tutte.

## 1. Setup and external input

Let `H`, `U={u_0,u_1,u_2,u_3}`, `v`, and

\[
                         C=N_H(v),\qquad |C|=5,
\]

satisfy the setup in Section 1 of the
[Hamiltonian-cycle reduction](../results/hc7_rooted_hamiltonian_cycle_reduction.md).
In particular, `H` is a
simple three-connected plane graph, every member of `U` is incident with
the outer face, every vertex of `H-U` lies in the open disk bounded by
that face, and adjoining a new outer vertex `r` complete to `U` gives a
four-connected plane graph `J`.

Because `H` is three-connected, its outer facial boundary is a simple
cycle.  All four members of `U` lie on that boundary and no vertex outside
`U` does.  Thus, after choosing the cyclic indexing,

\[
                         u_0u_1u_2u_3u_0                 \tag{1.2}
\]

is a literal cycle of `H`.

We use the following standard theorem in its path-system form.  A path
system is a family of pairwise internally disjoint paths.  A bridge of the
system is either an unused edge with both ends in its union or a component
outside that union together with all its incident edges to the union.  It
is **2-stable** if its attachments are not all contained in one member of
the path system.

> **Tutte's stable-bridges theorem.**  If a path system lies in a
> three-connected graph, then it can be replaced by a path system with the
> same endpoint pair for every indexed path such that every bridge of the
> new system is 2-stable.

This is the theorem quoted as Theorem 1.1 in Paul Wollan, *Bridges in
Highly Connected Graphs*, SIAM J. Discrete Math. **24** (2010),
1731--1741, DOI `10.1137/070710214`.  We apply it to a system of order
four.  Thus the invalid one-segment extrapolation recorded in
`../barriers/hc7_exact7_tutte_single_segment_barrier.md` is not involved.

## 2. Allocation theorem

### Theorem 2.1 (four-root stable-theta allocation)

Under the setup above, there are five pairwise disjoint connected sets

\[
                              A_0,A_1,A_2,A_3,X           \tag{2.1}
\]

such that, after cyclic relabelling, each of the pairs

\[
              A_0A_1,\quad A_1A_2,\quad A_2A_3,\quad A_3X,\quad XA_0
                                                               \tag{2.2}
\]

is adjacent in `H`.  Each `A_i` contains a different member of `U` and a
different member of `C`, while `X` contains the fifth member of `C`.

Consequently the five sets are cyclically adjacent, contain all five
vertices of `C`, and four different sets contain the four different roots
in `U`.  In particular, neither root-clustering pattern from Lemma 3.1 of
`hc7_rooted_hamiltonian_cycle_reduction.md` survives.

#### Proof

Four-connectivity of `J` gives four internally vertex-disjoint `r-v`
paths.  Choose such a path system and apply Tutte's stable-bridges theorem,
retaining the notation

\[
                              P_0,P_1,P_2,P_3.            \tag{2.3}
\]

The rerouted paths are still pairwise internally disjoint and have common
endpoints `r,v`.  Since `d_J(r)=4`, their four first edges at `r` are
exactly the four edges `ru` with `u\in U`.  Since `d_J(v)=5`, their four
last edges at `v` have four distinct other ends in `C`.  Relabel the paths
in their cyclic order around `r`, so that `P_i` contains `u_i`.  The cyclic
order of internally disjoint `r-v` paths at `v` is the same order up to
reversal.

Let `c_i` be the last vertex of `P_i` before `v`, and let

\[
                              c_*\in C-\{c_0,c_1,c_2,c_3\}. \tag{2.4}
\]

Every vertex of \(U\cap C\) is among `c_0,c_1,c_2,c_3`.  Indeed, let
`u` belong to \(U\cap C\), and let `P_i` be the path whose first edge is
`ru`.  The vertex `u` lies on no other path.  If `uv` were not an edge of
`P_i`, then the unused edge `uv` would be a bridge with both attachments
on `P_i`, contrary to 2-stability.  Thus `P_i=r-u-v`, and `u=c_i`.  In
particular,

\[
                              c_*\notin U.              \tag{2.5}
\]

We first check that `c_*` is outside the union of the four paths.  If it
were an internal vertex of some `P_i`, then the unused edge `vc_*` would
be a bridge whose two attachments, `v` and `c_*`, both lie on `P_i`.
That bridge would not be 2-stable.  Hence

\[
                          c_*\notin\bigcup_{i=0}^3V(P_i). \tag{2.6}
\]

Let `K` be the component of

\[
                       J-\bigcup_{i=0}^3V(P_i)           \tag{2.7}
\]

which contains `c_*`, and let `B_*` be the corresponding bridge.  The edge
`vc_*` shows that `v` is an attachment of `B_*`.  Stability implies that
the remaining attachments are not confined to one `P_i`: otherwise all
attachments, including the common endpoint `v`, would lie on that path.

The union of the four paths is a plane subdivision of four parallel
`r-v` edges.  Its complement has four open sectors, each bounded by two
paths consecutive in the cyclic order.  A connected bridge is drawn in
the closure of one sector.  The edge `vc_*` places `B_*` in the sector
between the two paths whose last edges at `v` surround `vc_*`.  Therefore
planarity permits attachments only on those two boundary paths (apart
from the common endpoints), and stability forces attachments on both.
After a cyclic relabelling, assume that those paths are `P_3` and `P_0`.
It follows that

\[
              X:=V(K)                                   \tag{2.8}
\]

is connected, contains `c_*`, is disjoint from every path, and is adjacent
to both `P_3-\{r,v\}` and `P_0-\{r,v\}`.  The last assertion cannot be
witnessed only at `r`: all four neighbours of `r` already lie on the path
system, so `K` has no edge to `r`.  Nor can its only attachment on one
boundary path be `v`, because stability requires an attachment belonging
to the other path away from the common endpoints.  Thus the asserted
adjacencies remain after deleting `r` and `v`.

For `0\le i\le3`, put

\[
                         A_i=V(P_i)-\{r,v\}.             \tag{2.9}
\]

These four sets and `X` are pairwise disjoint and connected.  Each `A_i`
contains `u_i` and `c_i`.  By (1.2), the literal edges

\[
                              u_0u_1,\quad u_1u_2,\quad u_2u_3 \tag{2.10}
\]

give the first three adjacencies in (2.2).  The two attachments of `K`
away from the common endpoints give `A_3X` and `XA_0`.  This proves every
adjacency in (2.2), and (2.4), (2.8), and (2.9) verify the required root
and neighbour allocation.  \(\square\)

## 3. Trust boundary

The theorem is an unbounded planar allocation result for arbitrary overlap
between `U` and `C`; in particular, it removes both Hamiltonian
root-clustering patterns.  It uses no edge of a planar completion and no
Hamiltonian-cycle exchange.

It does not by itself verify the remaining hypotheses of the degree-eight
contact-allocation theorem: the three omitted boundary vertices must still
have the required adjacencies to the five connected sets, and the reserved
connected component must still be disjoint from them and meet the required
labels.  It also does not treat a use of stable bridges with fewer than
three path-system members.
