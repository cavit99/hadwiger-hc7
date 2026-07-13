# Two-rail bridge overlap versus a rural carrier

**Status:** proved and independently audited after narrowing the
distinct-bridge and three-cut conclusions to their exact scope; pending
HC7-side application.  This note starts from the audited two-rail
certificate in `hc7_exact7_pair_carrier_bypass.md`.  It does not
claim that the remaining pure three-cut chain is already colour-gluable.

## 1. Abstract two-rail setting

Let `K` be a three-connected named carrier with nonadjacent trace roots
`x,y`.  Let

\[
 R_Q,R_P
\]

be internally vertex-disjoint nonseparating `x-y` paths.  Their union is a
cycle `C`.  Orient both paths from `x` to `y`.  Let

\[
 Q=\{q_1,q_2,q_3\}\subseteq V(R_Q)-\{x,y\},
 \qquad
 P_0\subseteq V(R_P)-\{x,y\},\quad |P_0|\ge3.       \tag{1.1}
\]

Each `q_i` is a literal movable portal from `K` to one of the other named
core blocks, and `P_0` consists of literal neighbours in `K` of the locked
connected region `L`.  The locked branch has

\[
  \text{no vertex-disjoint `x-y` and `q-p` paths in `K`}
  \quad(q\in Q,\ p\in P_0).                         \tag{1.2}
\]

Indeed, such a linkage is equivalent to a nonseparating `x-y` path
avoiding `q,p`; the generalized pair-carrier peel then applies.

For completeness, the nontrivial direction of this standard equivalence
uses the relative form of Tutte's path lemma.  Extend two disjoint
`x-y` and `q-p` paths to a partition `V(K)=C\mathbin{\dot\cup}D` with
`K[C]` and `K[D]` connected (contract the paths in a spanning tree and
cut one edge between them).  Applied to the connected induced graph
`K[C]` and its connected complement, the relative path lemma gives a
nonseparating `x-y` path inside `C`, hence avoiding `q,p`.

The purpose of this note is to identify exactly which bridge overlap
violates (1.2), and to package the absence of such overlap as a rural or
bounded-adhesion outcome.

## 2. Reversed rungs peel the carrier

A **cross-rail path** is a path whose ends lie one on `R_Q` and one on
`R_P`, and whose internal vertices avoid `C`.

### Theorem 2.1 (label-spanning reversed-rung exchange)

Let `D_1,D_2` be vertex-disjoint cross-rail paths, with ends

\[
 u_i\in V(R_Q),\qquad v_i\in V(R_P)\quad(i=1,2).
\]

Suppose that, in the orientations from `x` to `y`, the orders are

\[
 x,u_1,q,u_2,y\quad\hbox{on }R_Q,
 \qquad
 x,v_2,p,v_1,y\quad\hbox{on }R_P                 \tag{2.1}
\]

for some `q in Q` and `p in P_0`.  Then `K` has a labelled peel toward
the named block contacted by `q`.

#### Proof

The following two paths are vertex-disjoint:

\[
\begin{aligned}
 X_{xy}&=xR_Pv_2\;D_2\;u_2R_Qy,\\
 X_{qp}&=qR_Qu_1\;D_1\;v_1R_Pp.
\end{aligned}                                      \tag{2.2}
\]

The strict orders in (2.1) make their four rail segments disjoint, and
the two rungs are disjoint from each other and internally disjoint from
`C`.  Thus (2.2) is an `xy|qp` linkage.

By the connected-pair linkage equivalence, there is a nonseparating
`x-y` path avoiding `q,p`.  It avoids the movable portal `q` and omits the
marked attachment `p`; hence it does not contain all of `P_0`.  The
generalized clause after Theorem 4.1 of
`hc7_exact7_five_attachment_carrier_peel.md` gives the claimed
label-faithful peel. \(\square\)

The theorem is invariant under reversing either rail or interchanging the
two rungs.  Its content is order, not the displayed choice of orientation.

### Corollary 2.2 (bridge-overlap exclusion)

Let `B_1,B_2` be distinct `C`-bridges.  Choose in each `B_i` an attachment
`u_i` on `R_Q`, an attachment `v_i` on `R_P`, and a `u_i-v_i` path with
interior off `C`.  Assume that the four selected attachments are distinct.
If their strict orders are the reversed orders in (2.1), and both open
spans contain respectively a vertex of `Q` and a vertex of `P_0`, then the
carrier peels.

#### Proof

Paths chosen in distinct `C`-bridges are vertex-disjoint once their four
attachments are distinct.  The label-spanning reversed order is exactly
(2.1), so Theorem 2.1 applies. \(\square\)

Consequently, a locked carrier has no label-spanning reversed pair of
**distinct** `C`-bridges witnessed by internally off-`C` paths with four
distinct attachments.  This does not order all incidences inside one
bridge: a wheel hub, for example, supports many cross-rail paths which all
meet at the hub.  A further stable-bridge or bridge-splitting argument is
needed before the word “ladder” is justified globally.

## 3. Many crossless frames synchronize in a four-connected carrier

The next result no longer mentions HC7 labels.

### Theorem 3.1 (multi-frame rurality or a three-cut)

Let `J` be a four-connected graph, let `x,y` be distinct vertices, and let
`Q_0,P_1` be disjoint subsets of
`V(J)-{x,y}`, each of order at least two.  Suppose that for every
`q in Q_0` and `p in P_1`, `J` has no pair of vertex-disjoint paths joining
respectively

\[
                             x-y,\qquad q-p.        \tag{3.1}
\]

Then `J` is planar.  In its unique plane embedding, all vertices of

\[
                         \{x,y\}\cup Q_0\cup P_1   \tag{3.2}
\]

lie on the boundary of one face.  On that facial cycle, all of `Q_0` lie
on one open `x-y` arc and all of `P_1` lie on the other.

Equivalently, for a merely three-connected `J`, failure of this rural
conclusion can persist only in the presence of a separation of order
three.

#### Proof

Fix `q in Q_0` and `p in P_1`.  The tuple `(x,q,y,p)` is crossless.  By
the same-vertex generalized Two Paths Theorem, `J` has an edge-only
completion to a web with that outer frame.

A web consists of a planar rib, with possible clique pieces inserted
behind facial triangles.  No inserted piece can contain a vertex of `J`:
its facial triangle would be a three-vertex separator between that vertex
and the four outer-frame vertices, contrary to four-connectivity.  Hence
`J` is a spanning subgraph of the planar rib and is planar.  Deleting the
completion edges only merges faces, so the four vertices `x,q,y,p` are
cofacial in the induced embedding of `J`, in their alternating cyclic
order.

Because `J` is three-connected, Whitney uniqueness identifies the plane
embedding obtained from every choice of `q,p`.  Fix `q_0 in Q_0` and
`p_0 in P_1`, and let `F` be the face containing
`x,q_0,y,p_0`.  For any `p in P_1`, the face supplied by the tuple
`(x,q_0,y,p)` shares the three vertices `x,q_0,y` with `F`.  In a
three-connected plane graph two distinct facial boundaries meet in at
most one edge, so these faces are equal.  Thus every vertex of `P_1` lies
on `F`.  Similarly, the face supplied by `(x,q,y,p_0)` shares
`x,y,p_0` with `F`, and hence every vertex of `Q_0` lies on `F`.

Finally, the alternating order for every pair says that each `q` lies on
the same open `x-y` facial arc as `q_0`, whereas every `p` lies on the
opposite arc.  This proves the assertion. \(\square\)

Applied to (1.1)--(1.2), Theorem 3.1 closes the bridge geometry of every
four-connected carrier: it is one literal rural society with the three
foreign portals on one boundary rail and all nonroot locked attachments
on the other.  Thus a nonrural carrier in the current HC7 branch must
expose an actual three-cut; it cannot hide behind unbounded bridge
enumeration.

## 4. Mixed three-cut lobes also peel

### Lemma 4.1 (mixed-lobe exchange)

Let `K` be three-connected and let `S` be a three-vertex cut.  Let `D` be
a component of `K-S`.  Suppose

\[
 x,y\notin V(D),\qquad q\in Q\cap V(D),             \tag{4.1}
\]

and both `D` and `K-D` contain a member of `P_0`.  Then `K` has a labelled
peel toward the named block contacted by `q`.

#### Proof

Every component of `K-S` has all three vertices of `S` as neighbours;
otherwise at most two vertices would separate that component in the
three-connected graph.  It follows that `K-D` is connected: any other
component of `K-S`, together with `S`, connects all of `S`, and every
remaining component attaches to it through `S`.

Now put

\[
                         X=V(D),\qquad Y=V(K)-V(D).
\]

Both induced sides are connected, `q in X`, and `x,y in Y`.  By
hypothesis both sides meet `P_0`.  The portal edge at `q` supplies the
target-block contact, so `X|Y` is exactly a labelled carrier peel.
\(\square\)

### Corollary 4.2 (purity of every residual three-cut)

In a locked carrier, every component of `K-S` which avoids `x,y` and
contains a portal from `Q` is either disjoint from `P_0` or contains all
of `P_0`.  In particular, a three-cut cannot isolate a lobe containing a
portal and a proper nonempty part of the attachment rail.

This is the exact bounded-adhesion residue of the rural theorem.  The
wheel and ladder examples survive because their natural three-cut lobes
are label-pure; arbitrary overlapping portal/attachment lobes do not.

## 5. Structural endpoint

Starting from the audited three-portal two-rail certificate, one now has
the following reusable dichotomy:

\[
\boxed{
\begin{array}{ll}
\text{reversed bridge overlap spanning both label sets}
   &\Longrightarrow\text{label-faithful peel};\\[1mm]
\text{four-connected carrier}
   &\Longrightarrow\text{one common rural facial society};\\[1mm]
\text{three-connected nonrural residue}
   &\Longrightarrow\text{a literal three-cut};\\[-1mm]
\text{each root-avoiding portal lobe}
   &\hphantom{\Longrightarrow}\text{is `P_0`-empty or contains all `P_0`.}
\end{array}}
\]

The remaining HC7 step is no longer a portal-order enumeration.  It is to
control the trace-containing and portal-free cut components not covered by
Lemma 4.1, then show that the surviving three-gate structure is either
pumpable by a proper-minor colour transition or has the same two apex
labels on both closed sides.  That state-transfer step is not proved here.
