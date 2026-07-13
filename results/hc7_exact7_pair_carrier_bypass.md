# Seven-connected pair carrier: outside bypass or a vital trace rail

**Status:** proved and independently audited after making the open-shore,
`w`-attachment, and endpoint-omission hypotheses explicit.  This is the constructive
continuation of the audited pair-trace peel in
`../results/hc7_exact7_five_attachment_carrier_peel.md`.

## 1. Exact setting

Work in one closed terminal shore of the exact order-six Moser cell from
`../results/hc7_exact7_moser_order6_decorated_exchange.md`.  Let `K,A,B`
be three disjoint connected pairwise adjacent core blocks.  Their traces
partition `U`, and

\[
                         K\cap T=\{x,y\},            \tag{1.1}
\]

where `xy` is a missing root edge.  The trace of `K` has a literal edge to
the trace of each of `A,B`.  Let `L` be a nonempty connected subgraph of
the present open shore, disjoint from the core and side terminal, and
assume that `w` has a neighbour in `L`.  Thus `W={w}\cup L` is connected.
Put

\[
                         P=N_G(L)\cap K,             \tag{1.2}
\]

and assume `|P|>=5`.  In the five-attachment application, `W` has raw
contact only with `K` among the three core blocks.

The exact cell supplies two facts used below:

* the opposite open shore is anticomplete to the present open shore and
  `v` has no neighbour in it; and
* after deleting the three core traces, `w`, and the side terminal `t`, no
  other literal boundary vertex remains outside `A\cup B`.

## 2. Promotion or vital rail

### Theorem 2.1 (outside bypass or vital trace rail)

Assume `K` is three-connected.  Then at least one of the following occurs.

1. **Direct outside promotion.**  One of `A,B` can be enlarged through
   vertices disjoint from the core and `L`, without changing its literal
   trace, so that it becomes adjacent to `L`.  Hence `W` has raw contact
   rank at least two.
2. **Labelled carrier peel.**  The block `K` has a labelled peel toward
   `A` or `B` in the sense of Section 1 of the audited carrier-peel theorem.
   Again `W` has raw contact rank at least two.
3. **Vital trace rail.**  There is a non-root vertex

   \[
                         q\in K-(\{x,y\}\cup P)      \tag{2.1}
   \]

   which can be made a portal to `A` or `B` through an outside-core path,
   and every nonseparating `x-y` path in `K-q` contains all of `P`.

#### Proof

Delete

\[
                         A\cup B\cup\{x,y,w,t\}      \tag{2.2}
\]

from `G`, and let `X_0` be the component containing the connected set `L`.
At most two members of `P` are the roots `x,y`, so `X_0` contains at least
three vertices of `K-\{x,y\}`.

If `X_0` had no neighbour in `A\cup B`, then

\[
                         N_G(X_0)\subseteq\{x,y,w,t\}. \tag{2.3}
\]

Indeed all other root traces lie in the deleted blocks `A,B`, the exact
separation excludes the opposite open shore, and `v` has no open-shore
neighbour.  The at-most-four set in (2.3) would separate nonempty `X_0`
from `v`, contrary to seven-connectivity.  Thus `X_0` has an edge to one
of `A,B`; call that block `A_0`.

Choose a shortest `A_0-L` path with internal vertices in `X_0`, first
entering `L` at its final vertex.  If it avoids `K`, absorb all vertices of
the path except its final vertex into `A_0`.  The enlargement is connected,
disjoint from the core and `L`, and has the old literal trace.  Its last
edge makes it adjacent to `L`, proving outcome 1.

Otherwise let `q` be the first vertex of the path in `K`.  Because (2.2)
deleted `x,y`, the vertex `q` is non-root.  Absorb the path prefix before
`q` into `A_0`; this preserves the trace of `A_0` and makes `q` a literal
portal from `K` to the enlarged block.

Tutte's nonseparating-path theorem supplies an `x-y` path `Q` in `K-q`
such that `K-V(Q)` is connected.  If some such path omits a member of `P`,
the generalized clause following Theorem 4.1 of the audited carrier-peel
theorem applies and gives a labelled peel toward `A_0`, which is outcome 2.
We may therefore assume that every such nonseparating path contains all of
`P`.  In particular `q\notin P`, because every path under consideration
avoids `q`.  This proves (2.1) and outcome 3. \(\square\)

## 3. Consequence for six-surplus

In the six-surplus branch of the audited exact-cell exchange,
`|P|>=6`.  Theorem 2.1 says that failure of geometric promotion is no
longer arbitrary portal concentration: one non-root portal `q` is avoided
by the trace rail, while every removable trace rail must contain all six
marked attachments.  Call this a **marked-vital labelled rail**: changing
the rail without losing nonseparation cannot move even one marked
attachment off it.  This terminology is local to the theorem; it does not
assert that the rail is a vital linkage in the stronger standard sense.

This theorem does not yet prove that the vital rail is rural or that its
two sides return a common exact colour state.  Those are the remaining
uses of contraction-criticality.  It does, however, eliminate every
three-connected six-surplus carrier except this single web-like mechanism,
without enumerating portal orders.

## 4. Three-bypass amplification

Seven-connectivity actually supplies three distinct vital portals, unless
the direct promotion or peel has already occurred.

### Theorem 4.1 (three-bypass vital rail)

Under the hypotheses of Theorem 2.1, at least one of its first two outcomes
occurs, or there are three distinct vertices

\[
 q_1,q_2,q_3\in K-(\{x,y\}\cup P)                 \tag{4.1}
\]

and three paths from `A\cup B` to `L` which are pairwise
vertex-disjoint outside `L`, have distinct ends in `A\cup B`, and whose
first hits on `K` from the `A\cup B` side are respectively
`q_1,q_2,q_3`.  After absorbing each target-side prefix into its target
block, every nonseparating `x-y` path in `K-q_i` contains all of `P`, for
each `i=1,2,3`.

### Proof

Put `F={x,y,w,t}` and work in `G-F`.  Contract the connected set `L` to a
single source only for the following application of Menger's theorem, and
take `A\cup B` as the target set.  There are three paths from the source
to distinct target vertices, disjoint outside the source.

Indeed, otherwise vertex Menger gives a set `Z` of order at most two,
disjoint from the contracted source, which separates it from every target
vertex outside `Z`.  Expand `L` and let `C` be the component containing
`L` in `G-(F\cup Z)`.  The separation says that `C` contains no target
vertex and has no edge to one outside `Z`.  Every boundary exit from the
present open shore lies either in `F` or in one of the remaining literal
root traces, and all those remaining traces lie in the target blocks
`A,B`.  Thus `C` cannot leave the present open shore, and its whole-graph
neighbourhood lies in `F\cup Z`,
of order at most six, while `v` is on the nonempty far side.  This
contradicts seven-connectivity.

Expand the source and trim each path to end at its first vertex of `L` and
at its first target vertex.  Orient the paths from their distinct target
ends toward `L`.  If one path avoids `K`, absorb all its vertices except
its last `L` vertex into the corresponding target block.  This is the
direct outside promotion of Theorem 2.1(1).

Otherwise, on each path let `q_i` be its first vertex in `K`.  The paths
are disjoint outside `L`, so the `q_i` are distinct.  They avoid `F`, hence
are nonroot vertices.  The target-to-`q_i` prefixes have mutually disjoint
internal vertices, avoid all three core blocks except at their indicated
target and `q_i`, and avoid `L`.  Absorb all three prefixes into `A` or
`B` according to their target ends, always omitting the endpoint `q_i`
from the absorbed prefix.  The two target blocks remain disjoint,
connected, and retain their literal traces, while every `q_i` becomes a
literal foreign-block portal.  The carrier `K` and the marked set `P` are
unchanged.

For a fixed `i`, Tutte's theorem supplies a nonseparating `x-y` path in
`K-q_i`.  If any such path omits a member of `P`, the generalized clause
of the audited pair-carrier peel gives Theorem 2.1(2).  Otherwise every
such path contains all of `P`; this also forces `q_i\notin P`.  Apply the
same argument for all three indices to obtain (4.1). \(\square\)

The conclusion is a simultaneous, literal three-portal rail certificate.
It is stronger than three abstract colour contacts: the portal paths can be
absorbed without changing either target trace, and all three avoided
vertices refer to the same fixed carrier and marked attachment set.

## 5. Two-rail segregation

The three universal portals force one coherent two-rail skeleton.  We use
Tutte's second nonseparating-path theorem: for any distinct `x,y` in a
three-connected graph, there are two internally vertex-disjoint `x-y`
paths, each of whose vertex deletion leaves the graph connected.

### Theorem 5.1 (marked and portal rails segregate)

Assume the third outcome of Theorem 4.1.  Then `K` has internally
vertex-disjoint nonseparating `x-y` paths `R_P,R_Q` such that

\[
 P-\{x,y\}\subseteq V(R_P)-\{x,y\},\qquad
 \{q_1,q_2,q_3\}\subseteq V(R_Q)-\{x,y\},          \tag{5.1}
\]

and

\[
 (P-\{x,y\})\cap V(R_Q)=\varnothing.              \tag{5.2}
\]

Thus all nonroot marked attachments occur on one rail and all three movable
foreign portals on the other.  Both rail complements are connected.

### Proof

Apply Tutte's theorem to obtain internally disjoint nonseparating `x-y`
paths `R_1,R_2`.  Each `q_i` is distinct from `x,y`, so it belongs to at
most one of these paths.  Whenever `R_j` avoids `q_i`, the universal
property in Theorem 4.1 says that `R_j` contains all of `P`.

No `q_i` can lie outside both paths: then both paths would contain all of
`P`, impossible because `|P|>=5` and the paths have no common internal
vertex.  Nor can two of the `q_i` lie on different paths.  In that case
each path avoids the portal lying on the other and again both would contain
all of `P`.  Therefore all three `q_i` lie on one path, say `R_Q`.  The
other path `R_P` avoids all three and hence contains all of `P`.  Internal
disjointness then gives (5.2).  Both paths are nonseparating by their
choice. \(\square\)

Theorem 5.1 is the desired structural change of language: the hard
six-surplus carrier is a two-rail society with three labelled portals on
one rail and at least three nonroot attachment vertices on the other.  The
remaining bridge theorem must show that overlapping rail bridges create a
peel, while nonoverlap gives a rural ladder compatible with the fixed-pair
endgame.
