# Portal-preserving packet-bridge rotation

**Status:** proved and independently audited.

## 1. Packet skeletons

Let `P` be an `S`-full packet in a rich shore.  Choose, for every
`s in S`, one portal witness

\[
                         p(s)\in V(P)\cap N_G(s),
\]

and choose a tree `T subseteq P` inclusion-minimal subject to containing all selected
portal witnesses.  Suppress nothing.  Call the selected portal witnesses
and the vertices of degree different from two in `T` the **skeleton
vertices**.  A **segment** is the path between consecutive skeleton
vertices; its open segment has no selected portal witness and every one of
its vertices has degree two in `T`.

### Lemma 1.1 (bounded labelled skeleton)

The packet skeleton has at most twelve vertices and at most eleven
segments.  A pair of packet skeletons therefore has at most twenty-two
segments, independently of the orders of the packets and the rich shore.

#### Proof

Let `r<=7` be the number of distinct selected portal-witness vertices.
Minimality of `T` implies that every leaf is selected.  A tree with at most
`r` leaves has at most `r-2` vertices of degree at least three when
`r>=2`; for `r=1`, the minimal tree is a singleton.  Every
skeleton vertex is either one of the at most `r` selected vertices or one
of those branch vertices.  For `r>=2` there are therefore at most

\[
                              r+(r-2)\le12
\]

skeleton vertices; the case `r=1` is immediate.  Suppressing its open
degree-two segments gives a tree,
so it has at most eleven skeleton edges, one for each segment. `square`

Let `P_2` be a second disjoint `S`-full packet in the same open shore.  A
**packet bridge** is a connected subgraph `K` of that open shore, disjoint
from `T union P_2`, with at least one edge to `T`.  Its attachments are the
vertices of `T` incident with such edges.

## 2. Local rotation

### Lemma 2.1 (portal-free segment rotation)

Suppose a packet bridge `K` has distinct attachments `x,y` on one segment
of `T`.  Let `W` be the nonempty set of internal vertices of the `x-y`
subpath `xTy`, and suppose `W` contains no skeleton vertex.  Then there is an
`x-y` path `Q` whose internal vertices lie in `K`, and

\[
                     T'=(T-W)\cup Q
\]

is a tree containing every selected portal witness.  Consequently `T'`
and `P_2` remain disjoint `S`-full packets.

Moreover, `W` is a connected subgraph disjoint from both new packets.
Hence, in the audited hard exact-seven cell, either

\[
                              |N_S(W)|\le4,              \tag{2.1}
\]

or the defect-two carrier theorem reflects an exact state and six-colours
`G`.

#### Proof

Because `K` is connected and has an edge to each of `x,y`, it contains an
`x-y` path `Q` with all internal vertices in `K`.  The open path `W` has no
branch vertex of `T`; deleting it separates `T` into exactly two trees, one
containing `x` and one containing `y`.  Adding `Q` joins them without a
cycle, so `T'` is a tree.

No selected portal witness lies in `W`.  Thus every selected `p(s)` remains
in `T'`, and `T'` is still `S`-full.  Its only new vertices lie in `K`,
which is disjoint from `P_2`, so the two packets remain disjoint.

The nonempty set `W` induces a path and is disjoint from `T' union P_2`.
When it contacts at least five literal boundary vertices it is a connected
carrier of defect at most two alongside the two full packets `T',P_2`.
The audited adaptive defect-two theorem then chooses the thin contraction
block before the returned state and reflects that state through these three
carriers, six-colouring `G`.  Therefore every surviving rotation satisfies
(2.1). `square`

### Corollary 2.2 (three attachments on one segment)

If a complementary bridge has at least three attachments all lying on one
packet segment, choose the two extreme attachments along that segment.
Lemma 2.1 gives either an immediate six-colouring or a portal-preserving
rotation whose freed old segment has support at most four.

The operation is exactly reversible at the level of packet trees: the freed
internal subpath `W` is a packet bridge of `T'` attached at `x,y`, while the
internal vertices of `Q` are portal-free degree-two vertices of `T'`.
Replacing `Q` by the old `x-W-y` path therefore restores `T`.  Thus a failure
to close is not an unstructured portal collision; it is a reversible
low-support rotation.

## 3. Geometric handoff

The audited three-attachment theorem says that every component outside a
selected pair of full packets has at least three distinct packet
attachments.  Lemma 2.1 now handles the unstable case in which two extreme
attachments lie on one portal-free segment:

* a freed segment of support at least five is the required partial carrier;
* otherwise the packet rotates while preserving all seven literal portal
  witnesses, and the inverse bridge has support at most four.

Accordingly, after closing these rotations under composition, the only
genuinely stable bridge geometry is one whose attachments meet multiple
skeleton segments (or both packet trees).  By Lemma 1.1 this is a society
on at most twenty-two labelled segments, rather than an unbounded packet
interior.  That is the finite-terminal society on which a Two-Paths/web
theorem should be applied.  The remaining
global task is to prove that a component of reversible low-support rotations
either exposes a support-five peel, yields a common exact state, or has a
coherent rural embedding.  Lemma 2.1 supplies the literal label-preserving
edge of that exchange graph; it does not by itself prove the global
composition theorem.
