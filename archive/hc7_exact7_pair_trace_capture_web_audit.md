# Independent hostile audit: pair-trace capture webs

Audited file: `archive/hc7_exact7_pair_trace_capture_web.md`.

## Verdict

**YELLOW as written; GREEN after one local proof repair in Lemma 4.1.**

Lemmas 2.1 and 2.2, Theorem 3.1, Corollary 3.2, and the two sharp
examples are correct.  The statement of Lemma 4.1 is also correct, but its
current proof makes an invalid inference: a nonseparating path in `K+e`
which does not traverse `e` need not be nonseparating in `K`, because `e`
may connect two components of its complement.  The repair below uses the
clean detour on either the path side or the complement side and proves the
needed two-connectivity only after contracting the translated trace path.

## 1. Relative Tutte lemma

Lemma 2.1 uses an exact published result, not an informal strengthening.
Lemma 1.1 of G. Chen, R. J. Gould and X. Yu, *Graph Connectivity After
Path Removal*, states:

> If `G` is three-connected, `H` is a connected induced subgraph, and
> `F` is a component of `G-V(H)`, then for any `x,y in H` there is an
> `x-y` path `Q` in `H` such that every component of `H-V(Q)` has a
> neighbour in `F`.

In the application, `H=J[C]` is induced and connected and its whole
complement `J[D]` is connected, hence is one component `F`.  Joining `F`
to every component of `H-V(Q)` makes `J-V(Q)` connected.  The specified
vertices `q,p` lie in `D`, so the path avoids them.  This proves Lemma 2.1
exactly.

Primary source:
`https://yu.math.gatech.edu/Papers/tightpath.pdf`, Lemma 1.1.

## 2. Connected-partition equivalence

Lemma 2.2 is correct in all three directions.

For the only nontrivial direction, contract the two disjoint prescribed
paths to distinct vertices `u,v`.  In a spanning tree of the contracted
connected graph, delete an edge of the unique `u-v` path.  The two tree
components partition every contracted vertex into connected sides, one
containing `u` and one containing `v`.  Expanding the contractions gives a
partition `C dotcup D` of `V(K)` into connected induced sides containing
`{x,y}` and `{q,p}`, respectively.  Lemma 2.1 then gives the reserved
nonseparating `x-y` path.  No planarity or linkage theorem is hidden here.

## 3. Crossless frames and the two-rail cycle

Theorem 3.1 follows immediately from Lemma 2.2: an `xy|qp` linkage would
give a nonseparating `x-y` path avoiding `q,p`, contradicting capture of
the marked member `p`.  The ordered tuple `(x,q,y,p)` is therefore
crossless.  The same-vertex edge-completion conclusion is precisely the
audited form of Humeau--Pous, Theorem 1.5, already used in
`results/hc7_guarded_cycle_web_exchange.md` and its audit.

Corollary 3.2 also invokes an exact theorem.  Chen--Gould--Yu record that
in every three-connected graph, for any two vertices `x,y`, there are two
internally vertex-disjoint `x-y` paths `Q_1,Q_2` for which both
`G-V(Q_i)` are connected.  See the introductory statement on their first
page and the conclusion `alpha(2)=3` on page 3 of the primary source.

At most one of these paths contains the internal vertex `q`; the other is
therefore a captured path and contains all of `P`.  Internal disjointness
forces the second path to avoid every member of `P`, and capture forces it
to contain `q`.  Since `xy` is absent, their union is a literal cycle with
the marked set on one rail and the portal on the other.  This conclusion
does not claim that the separate web completions have one common rib.

## 4. Lemma 4.1: exact flaw and repair

Let `Q` be the nonseparating `x-y` path in `K+e` avoiding `q,p` supplied
by Lemma 2.2.  The current proof says `Q` must use `e`.  This is false as
an inference: when `Q` avoids `e`, the graph `(K+e)-V(Q)` may be connected
only because the artificial edge `e` joins two components of
`K-V(Q)`.

The statement is nevertheless repaired as follows.  Put

\[
                         K_D=K\cup D.
\]

If `Q` uses `e`, replace that edge in `Q` by `D`, obtaining an `x-y` path
`Q_D` in `K_D`.  Because both ends of `e` were deleted with `Q`,
nonseparation of `Q` in `K+e` says `K-V(Q)` is connected; this is exactly
the complement of `Q_D` in `K_D`.

If `Q` does not use `e`, take `Q_D=Q`.  Its complement in `K_D` is obtained
from the connected graph `(K+e)-V(Q)` by replacing the edge `e` with the
path `D`; it is therefore connected.  Thus in both cases `Q_D` is a
nonseparating `x-y` path of `K_D` avoiding `q,p`.

Now contract `Q_D` to a vertex `z`.  The quotient is two-connected:

* deleting `z` leaves the connected complement of `Q_D`; and
* deleting any other quotient vertex gives a contraction of `K_D-c`,
  which is connected.  Indeed `K-c` is connected because `K` is
  three-connected, and the two pieces of the clean ear `D-c` attach to
  the surviving graph at `a` and/or `b` (if `c` is an endpoint, the whole
  remaining ear attaches at the other endpoint).

Apply the marked bipolar split in this quotient with `q` on the target
side and `z` on the retained trace side.  The image of `P` has at least two
members: `p` is outside `Q_D`, while `|P|>=2` supplies either another
outside image or the image `z`.  Both lifted sides therefore meet `P`.
The clean-detour hypotheses keep every internal vertex of `D` away from
the other named blocks, `L`, and the adhesion, so the lift is a literal
label-faithful peel.  This proves the stated lemma without asserting that
adding an ear preserves three-connectivity.

## 5. Sharp examples

The atomic graph `K_5-{02,13}` has the asserted property.  Avoiding
`1,3`, the only `0-2` path is `0-4-2`, whose deletion leaves nonadjacent
vertices `1,3`.

The wheel proof is also exact.  A nonseparating `x-y` path avoiding `q`
cannot contain the hub, since its deletion would isolate `q` while marked
vertices remain.  Avoiding both hub and `q` forces the full opposite rim
arc and hence every member of `P`.  For a proposed peel, if the hub is on
the retained `x,y` side, the target side cannot connect `q` to `P`; if the
hub is on the target side, deleting `q` and one marked vertex breaks both
rim arcs between `x,y`.  Thus arbitrary attachment multiplicity alone
does not force a peel.

## Trust boundary

After the Lemma 4.1 repair, the note proves a uniform rooted-model
principle: capture is exactly an `xy|qp` linkage obstruction for each
marked attachment, with a common literal two-rail cycle.  It does not yet
prove that the Humeau--Pous web completions for different `p` share one
rib, nor that contraction-critical colouring automatically supplies a
clean detour.
