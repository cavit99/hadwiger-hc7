# Pair-trace capture gives common-frame four-terminal webs

**Status:** proved graph-theoretic consequences and exact clean-detour lift;
pending independent audit.
It converts the pair-trace rail-capture residue into a family of literal
Two-Paths web certificates.  It does not yet prove that the web expansions
on the two closed sides have one common equality state, nor that an
arbitrary edge-critical Kempe detour is clean.

## 1. Setting

Let `K` be a three-connected named carrier with exact literal trace
`{x,y}`, where `xy` is absent.  Let `q` be a non-root vertex of `K` which
is a movable portal to another named core block.  Let

\[
                         P\subseteq V(K)-\{x,y,q\}              \tag{1.1}
\]

be the locked attachment set of the connected `w`-region.  The current
HC7 residue has `|P|>=6`.

Call an `x-y` path **nonseparating** if deleting all its vertices leaves a
connected graph.  The rail-capture hypothesis is

\[
 \text{every nonseparating `x-y` path avoiding `q` contains all of `P`.}
                                                                    \tag{1.2}
\]

The point of this note is that (1.2) is already a labelled linkage
obstruction, not merely an assertion about a preferred path.

## 2. Connected-pair linkage and a reserved nonseparating path

We use the following standard path lemma in its exact needed form.

### Lemma 2.1 (relative nonseparating path)

Let `J` be three-connected.  Suppose `V(J)=C dotcup D`, both `J[C]` and
`J[D]` are connected, `x,y in C`, and `q,p in D`.  Then `J[C]` contains
an `x-y` path `Q` for which `J-V(Q)` is connected.  In particular `Q`
avoids `q,p`.

#### Proof

Apply the standard relative form of Tutte's path lemma: if `H` is a
connected induced subgraph of a three-connected graph and `F` is a
component of its complement, then, for any `x,y in H`, there is an
`x-y` path in `H` such that every component left in `H` after deleting the
path has a neighbour in `F`.

This is Lemma 1.1 of G. Chen, R. J. Gould and X. Yu, *Graph Connectivity
After Path Removal*.

Here take `H=J[C]` and `F=J[D]`.  The set `F` is connected, and every
component of `H-V(Q)` has an edge to it.  Therefore `F` together with all
those components is connected, and it is exactly `J-V(Q)`. \(\square\)

### Lemma 2.2 (linkage equivalence)

For distinct `x,y,q,p` in a three-connected graph `K`, the following are
equivalent.

1. `K` has a nonseparating `x-y` path avoiding both `q,p`.
2. `K` contains vertex-disjoint paths, one joining `x` to `y` and the
   other joining `q` to `p`.
3. `K` contains two disjoint connected subgraphs, one containing
   `{x,y}` and the other containing `{q,p}`.

#### Proof

Item 1 implies item 3 by taking the path and its connected complement;
item 3 implies item 2 by taking paths inside the two connected subgraphs.

For item 2 implies item 1, first extend the two disjoint paths to a
partition of `V(K)` into two connected sets.  This elementary extension is
obtained by contracting both paths, taking a spanning tree of the resulting
connected graph, deleting one edge on the unique tree path between the two
contracted vertices, and assigning the two resulting tree components to
the corresponding paths.  Apply Lemma 2.1 to that connected partition.
\(\square\)

No prescribed planarity or colour name occurs in this equivalence.

## 3. Capture-to-web theorem

### Theorem 3.1 (every captured attachment is a crossless frame)

Assume (1.2).  Then, for every `p in P`, `K` has no pair of vertex-disjoint
paths joining respectively

\[
                              x-y,qquad q-p.                    \tag{3.1}
\]

Consequently the four-terminal tuple

\[
                              (x,q,y,p)                           \tag{3.2}
\]

is crossless.  The generalized Two Paths Theorem therefore gives a
same-vertex completion of `K` to a web with outer frame (3.2).

#### Proof

If (3.1) existed, Lemma 2.2 would give a nonseparating `x-y` path avoiding
`q,p`.  It avoids `q` but omits the member `p` of `P`, contrary to (1.2).
Thus (3.1) is impossible.  The two forbidden pairs alternate in the order
`x,q,y,p`, so this is precisely the crossless tuple to which the generalized
Two Paths Theorem applies. \(\square\)

For `|P|>=6`, Theorem 3.1 supplies at least six literal web certificates
sharing the fixed ordered triple `(x,q,y)`; only the fourth frame vertex
varies.  These completions need not yet be canonical or mutually
compatible.  Corollary 3.2 below supplies the common literal frame cycle;
a continuation must still align the web ribs (or show that they force one
rotation) rather than treat the six attachments as unordered capacity.

### Corollary 3.2 (two internally disjoint nonseparating rails)

Under (1.2), there are two internally vertex-disjoint nonseparating
`x-y` paths `Q_P,Q_q` such that

\[
                 P\subseteq V(Q_P),\quad q\notin V(Q_P),
                 \qquad q\in V(Q_q),\quad
                 P\cap V(Q_q)=\varnothing.                       \tag{3.3}
\]

#### Proof

The standard `alpha(2)=3` strengthening of Tutte's theorem says that a
three-connected graph has two internally vertex-disjoint nonseparating
paths between any prescribed nonadjacent pair `x,y`; see Chen--Gould--Yu,
lines 37--39 and 123--127 of the cited paper.  At most one of the two paths
contains `q`, so at least one avoids it; call that path `Q_P`.
By (1.2), it contains all of `P`.

The other path is internally disjoint from `Q_P`, so it contains no member
of `P`.  It must contain `q`, since otherwise (1.2) would force it to
contain `P` as well.  Call it `Q_q`. \(\square\)

Thus the locked carrier contains a literal two-rail cycle: one arc carries
all attachment labels and the other carries the foreign portal.  This is
the exact infinite analogue of the atomic `K_5`-minus-two-edges rail cell.

## 4. Exact clean-detour repair

The web conclusion identifies precisely what an edge-critical detour has
to accomplish.

### Lemma 4.1 (one web-breaking detour peels the carrier)

Fix `p in P` and let `e=ab` be a nonedge of `K` such that `K+e` has the
linkage (3.1).  Suppose the ambient open shore contains an `a-b` path `D`
such that the internal vertices of `D` avoid `K`, the three named core
blocks, the locked region `L`, and the literal adhesion.

Then the named carrier has a label-faithful peel toward the core block
contacted by `q`.

#### Proof

Adding the edge `e` preserves three-connectivity, so Lemma 2.2 applied in
`K+e` gives a nonseparating `x-y` path `Q` avoiding `q,p`.  The path `Q`
need not use `e`: the artificial edge can instead connect the complement
of `Q`.  Run the generalized audited pair-carrier peel proof in `K+e`:
contract
`Q`, make a marked bipolar split with the image of `Q` on the retained
trace side and `q` on the target side, and lift.  This gives a connected
partition `X dotcup Y=V(K)` in the graph `K+e`, where `q in X`,
`x,y in Y`, and both parts meet `P`.

It remains only to remove the artificial edge from this connected
partition.  If `a,b` lie on different sides, the edge `e` is internal to
neither induced side.  Hence `K[X]` and `K[Y]` were already connected in
the original carrier, and `X dotcup Y` itself is the required peel.

If `a,b` lie on the same side, adjoin every internal vertex of `D` to that
side.  Replacing the possible use of `e` by the actual `a-b` path `D`
makes that enlarged side connected; the other side is unchanged and
connected in `K`.  The clean-detour hypothesis makes the enlargement
disjoint from the other named blocks, `L`, and the adhesion, so it changes
neither literal trace.  In both cases the target side still contains `q`
and meets `P`, while the retained side contains `x,y` and meets `P`.
Thus the resulting ambient partition is a label-faithful peel toward the
block contacted by `q`.
\(\square\)

This lemma is deliberately conditional on a **clean** detour.  An arbitrary
bichromatic path from an edge-deletion colouring may hit a reserved block
before realizing `e`; calling such a path a web edge would be the forbidden
palette-to-carrier inference.

## 5. Sharp rural obstruction

The smallest warning is already `K_5` with the two independent edges
`xy` and `qp` deleted.  With `(x,q,y,p)=(0,1,2,3)` in
`K_5-\{02,13\}`, every nonseparating `0-2` path avoiding `1` uses `3`.
For example, the path `0-4-2` avoids `3`, but its deletion leaves the two
nonadjacent vertices `1,3`; hence it is separating.  This is the atomic
crossless frame behind the larger rail family below.

The web alternative is real, even with arbitrarily many locked
attachments.  Let `K` be the wheel whose rim, in cyclic order, is

\[
                        x,q,y,p_1,p_2,\ldots,p_m,x,qquad m>=2,   \tag{5.1}
\]

and let `h` be its hub.  Put `P={p_1,\ldots,p_m}`.  The graph `K` is
three-connected.

Any nonseparating `x-y` path avoiding `q` cannot use `h`: deleting such a
path deletes `x,y,h` and leaves `q`, whose three neighbours are exactly
those deleted vertices, isolated.  A path avoiding both `q,h` must use the
other rim arc from `x` to `y`, and that arc contains every vertex of `P`.
Conversely its deletion leaves the edge `qh`, so it is nonseparating.
Thus (1.2) holds for arbitrary `m`.

If another core block contacts `K` only at `q`, there is no labelled peel:
write a hypothetical peel as `X dotcup Y=V(K)`, with `q in X`,
`x,y in Y`, both parts connected, and both meeting `P`.  If the hub `h`
belongs to `Y`, then `X` cannot connect `q` to a member of `P`, since all
three neighbours of `q`---namely `x,y,h`---belong to `Y`.  If `h` belongs
to `X`, then `Y` is contained in the rim.  The deletion of `q` already
breaks the short `x-q-y` arc; because `X` must also contain a member of
`P`, it breaks the other `x-y` rim arc as well.  Hence `Y` is disconnected.
Both cases contradict the definition of a peel.
Equivalently, Theorem 3.1 gives the usual plane wheel web with alternating
frame `(x,q,y,p_i)` for every `i`.

This wheel family shows that the capture hypothesis alone cannot yield a
peel, regardless of `|P|`.  What is special in the HC7 cell is the five
edge-critical detours around every operated edge.  Lemma 4.1 states the
exact event by which one of those detours breaks the web.  If no detour is
clean, the surviving certificate is a rural society with a fixed
attachment rail, a fixed foreign-portal rail, and every critical detour
blocked by a named carrier or adhesion.  Turning that common blocking set
into the promised coherent two-apex structure is the remaining state step.

## 6. Exact endpoint

The pair-trace residue no longer has an unspecified "all paths are
captured" form.  It has the following audited-ready dependency:

\[
\boxed{
\begin{array}{c}
\text{one clean edge-critical completion edge}
   \Longrightarrow \text{label-faithful peel};\\[2mm]
\text{no such edge}
   \Longrightarrow
   \text{six crossless frames }(x,q,y,p),\ p\in P,
   \text{ on the same two-rail carrier.}
\end{array}}
\]

The next lemma must use the common blockers of the critical detours to
align those six web frames or to exhibit the same bounded adhesion on both
closed sides.  No further attachment counting can improve this endpoint.
