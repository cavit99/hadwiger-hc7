# Dynamic reduction of maximal-society portal frames

## Status

The maximal-society theorem reduces direct model-label geometry to two
finite tree frames: two edge-disjoint portal paths or a three-arm frame.
This note pushes those frames dynamically without asserting a false static
splitter.

For a clean two-frame, its two complementary linkage orientations together
are exactly a two-path linkage between the two portal pairs.  Menger's
theorem therefore gives either two disjoint adjacent repair packets or a
single gate separating the portal pairs.  After the protected bags are
restored, that gate promotes to a full ambient adhesion.  At `HC_7`, at
least six vertices of this adhesion lie in the five protected bags, so one
protected bag supplies a nonzero connected boundary trace.

For a direct maximal-society frame the gate is itself a society vertex and
belongs to every promoted separator of the two society components.  Full
two-sided component support gives an explicit `K_k` grouping; otherwise a
named one-sided label remains.  A sharp `I vee K_2` example shows that even
seven-connectivity, the exact six protected vertices, and repeated bag
ownership do not close this lock without the critical operation states.

For an individual prescribed orientation, failure still invokes the
classical Two Paths Theorem and gives a web.  Every nontrivial web cell
promotes to a full ambient adhesion.  Opposite boundary-faithful proper
minor operations have disjoint equality-state sets, even if a web side is
atomic.  The exact residue is therefore a planar web core or a full
operation-state adhesion; no exceptional atomic-state case is needed.

For a three-arm frame, an XOR identity proves that every successful split
must split an odd number of arms internally.  This forces one of three
explicit complementary two-linkages.  Such a linkage gives a two-label
repair packet; if all three fail, the same web/adhesion state alternatives
apply.  This is a structural reduction, not a closure of `HC_7`.

## 1. Setup and protected graph

Let `G` be a proper-minor-minimal counterexample at the least failing
parameter `k`.  Let

\[
                         S=A\mathbin{\dot\cup}B           \tag{1.1}
\]

be an inclusion-maximal connected induced bipartite society.  Contract it
to `z`, take a minimum z-rooted `K_{k-1}`-model, and expand its root bag to
`widehat T`.  Write the external bags as

\[
                         C_1,\ldots,C_{k-2},
\]

and put

\[
                         \mathcal C=\bigcup_i C_i,
                         \qquad J=G-\mathcal C.           \tag{1.2}
\]

The set `mathcal C` is protected: consuming one of its vertices in a repair
path can destroy a named branch bag.  The available graph `J` contains the
entire expanded root bag and the society `S`.

For every direct label `i notin Delta_S`, maximality supplies a vertex
`w_i in C_i` with neighbours

\[
                         a_i\in A,\qquad b_i\in B.        \tag{1.3}
\]

Thus any two disjoint connected available sets containing respectively
`a_i` and `b_i` retain label `i` through the two literal edges to `w_i`.

Choose a spanning tree of `G[widehat T]` which contains a spanning tree of
`G[S]`.  All selected `a_i-b_i` tree paths then lie in `S`.  Since every
induced subgraph of `G[S]` is bipartite, every connected vertex set on one
of those paths is a legitimate tight society contraction.

## 2. The clean two-frame

Take two direct labels `i,j` whose tree paths form the disjoint-pair frame.
First separate a collision outcome: if the four selected terminals are not
distinct, the common terminal is a literal society vertex supporting two
named labels.  This is a multi-label portal collision, not a four-terminal
two-paths instance.

Assume henceforth that

\[
                         a_i,a_j,b_i,b_j                 \tag{2.1}
\]

are distinct.  There are two complementary repair-linkage orientations:

\[
\begin{array}{c|c}
0&(a_i,a_j),\ (b_i,b_j)\\
1&(a_i,b_j),\ (b_i,a_j).
\end{array}                                               \tag{2.2}
\]

An orientation is **realized** when `J` contains vertex-disjoint paths for
its two terminal pairs.

### Lemma 2.1 (either orientation gives a two-label repair packet)

If either orientation in (2.2) is realized, there are disjoint connected
adjacent sets `X,Y` in `J` such that each contains one endpoint of each
portal pair.  In orientation zero they may be indexed so that

\[
                 \{a_i,a_j\}\subseteq X,\qquad
                 \{b_i,b_j\}\subseteq Y.                \tag{2.3}
\]

Consequently both sets are adjacent to both named bags `C_i,C_j`.

#### Proof

The two paths are disjoint and connected.  Since `S subseteq J` is
connected and contains all four terminals, the two paths lie in one
component of `J`.  Take a shortest path between them.  Its internal
vertices avoid both.  If it is a single edge, use that edge as the required
adjacency.  Otherwise delete one edge of the connector and absorb the two
resulting halves into the two linkage paths, respectively.  This gives disjoint
connected adjacent sets satisfying (2.3).  The portal edges in (1.3)
supply the two named bag adjacencies.  QED.

This is only a two-label packet.  It becomes a full `K_k` split if all
other direct portal pairs and all warehouse labels can be absorbed into
`X,Y` while preserving disjointness.

The proof is label-geometric rather than shore-specific.  Under
`|Delta_S|<=1`, Lemma 3.3 of the society-contraction note supplies two
distinct expanded-bag portals for the possible defect label.  Lemmas 2.1
and 2.2 therefore apply unchanged when one or both selected frame labels
is that defect, with the two portal edges allowed to meet different
vertices of its external bag.  What is then lost is only the claim that
every reference subpath lies inside the bipartite society.

Every connected two-piece split which separates both portal pairs realizes
one of the two orientations: inspect which of `a_j,b_j` lies with `a_i`.
Thus a genuine two-label obstruction requires both linkage orientations to
fail.

### Theorem 2.2 (two-frame repair or one-gate lock)

Let

\[
             U=\{a_i,b_i\},\qquad V=\{a_j,b_j\}.        \tag{2.4}
\]

For four distinct terminals, exactly one of the following conclusions is
forced:

1. one orientation in (2.2) is realized and hence Lemma 2.1 gives a
   two-label repair packet; or
2. there is a vertex `q in V(J)` such that `J-q` has no path from
   `U-{q}` to `V-{q}`.

In the second conclusion both displayed terminal remainders are nonempty.
If all four terminals lie in the connected expanded root bag, the
separator has order exactly one rather than zero.

#### Proof

Apply the set form of vertex Menger to the disjoint two-sets `U,V`.  Two
vertex-disjoint `U-V` paths have distinct endpoints in each set.  Their
endpoint matching is one of the two orientations in (2.2), so outcome 1
holds.  Otherwise Menger gives a `U-V` separator of order at most one.
Because `U` and `V` both have order two, deleting its possible vertex
leaves at least one terminal from each set, giving outcome 2.  If the four
terminals lie in one connected set, the empty set cannot separate them.
QED.

This simultaneous-orientation argument is strictly sharper than applying
the Two Paths Theorem twice: a clean disjoint-pair frame has a one-gate
lock, not two unrelated web certificates.

The same set-linkage idea gives a monotone exchange after a packet has
already been built.

### Theorem 2.3 (clean-label absorption or packet barrier)

Let `X,Y` be disjoint connected adjacent sets in `J`, and let `p,q` be two
distinct portals of another label, both outside `X union Y`.  Contract `X`
and `Y` separately to adjacent vertices `x,y`, obtaining `J^*`.  Then one
of the following holds:

1. there are enlarged disjoint connected adjacent sets `X',Y'` with
   `X subseteq X'`, `Y subseteq Y'`, and one of `p,q` in each; or
2. a vertex `w notin {x,y}` separates the remaining members of `{p,q}`
   from `{x,y}` in `J^*`; or
3. `J-X` contains no path from `{p,q}` to `Y`, or symmetrically `J-Y`
   contains no path from `{p,q}` to `X`.

If all four objects `p,q,X,Y` lie in one component of `J`, the obstruction
in outcomes 2--3 has order exactly one in `J^*`.

#### Proof

Apply set Menger in `J^*` between `{p,q}` and `{x,y}`.  If there are two
vertex-disjoint paths, their endpoints are distinct on both sides.  Lift
the path ending at `x` and truncate it at its first vertex of `X`; absorb
the lifted initial segment into `X`.  Do the same at `Y`.  The two absorbed
segments are disjoint, and the old `X-Y` edge preserves adjacency.  This
is outcome 1.  Since `p,q` are both portals of the new label, the enlarged
packets now both meet its external bag.

Otherwise Menger gives a separator of order at most one.  If its vertex is
not `x` or `y`, outcome 2 is its literal lift (the vertex may itself be
`p` or `q`).  If it is `x`, deleting the preimage `X` leaves no path from
the portal pair to `Y`, which is outcome 3; the case `y` is symmetric.
Connectedness excludes the empty separator.  QED.

Thus a clean third label can be absorbed into a two-label repair packet
unless it exposes either another single gate or a packet-side dominance
barrier.  Portals already consumed by `X union Y` require a non-monotone
rerouting and are deliberately not counted by this lemma.

Maximal-society geometry localizes the single gate and gives an exact
clique-minor grouping whenever one society component has full two-sided
label support.

### Theorem 2.4 (society-gate localization and component split)

Assume the clean two-frame terminals lie in the connected society `S`, and
let `q` be the gate in outcome 2 of Theorem 2.2.  Then `q in S`.

For a component `H` of `G[S]-q`, suppose that every external model bag is
adjacent both to `H` and to `S-H`.  Then

\[
                         H,\quad S-H,\quad
                         C_1,\ldots,C_{k-2}              \tag{2.5}
\]

is a `K_k`-model.  Consequently, in a `K_k`-minor-free graph, every
component `H` of `S-q` has a one-sided label: some `C_i` misses `H` or
some `C_j` misses `S-H`.

Moreover, if `H_1,H_2` are distinct components of `S-q`, every
`H_1-H_2` separator contained in `{q} union mathcal C` contains `q`.
Thus the promoted one-gate adhesion in a 7-connected `HC_7` candidate has
exactly the form

\[
                         Z=\{q\}\mathbin{\dot\cup}
                           (Z\cap\mathcal C),
             \qquad |Z\cap\mathcal C|\ge6.              \tag{2.6}
\]

#### Proof

If `q` were outside `S`, the connected graph `G[S]` would contain a path
from a terminal in the first portal pair to a terminal in the second which
avoids `q`, contrary to the gate property.  Hence `q in S`.

Every component of `S-q` has a neighbour of `q`, because `S` is connected.
Therefore both `H` and `S-H` induce connected subgraphs, they are disjoint
and adjacent, and the assumed contacts make both adjacent to every
`C_i`.  The external bags remain pairwise adjacent.  This proves that
(2.5) is the displayed `K_k`-model.

Finally, the path from `H_1` to `H_2` through `q` lies wholly in `S` and
uses no protected bag.  A separator contained in `{q} union mathcal C`
must therefore contain `q`.  Seven-connectivity and Theorem 4.1 then give
(2.6).  QED.

The one-sided-label conclusion is the exact component-incidence lock left
by maximal-society bi-support.  Maximality says that each individual
outside vertex touching `S` has neighbours in both bipartition shores; it
does not say that those neighbours occur in two prescribed components of
`S-q`.

## 3. Failure of a linkage orientation is a web

Fix either orientation in (2.2) and assume it has no linkage.  Apply the
vertex form of the Two Paths Theorem to `J` with those terminal pairs.  For
orientation zero they are

\[
                         (a_i,a_j),\qquad(b_i,b_j).       \tag{3.1}
\]

For orientation one use `(a_i,b_j),(b_i,a_j)`.  If both orientations fail,
the two-frame carries two (possibly different) web certificates, but
Theorem 2.2 supersedes this pair by the stronger single-gate certificate.

In its standard maximal form, the theorem returns a web: a planar
near-triangulated skeleton with the four terminals on its outer boundary in
alternating order, with arbitrary pieces permitted inside facial triangles.
Only the following consequence is used here.

### Web consequence 3.1

Either `J` is the planar web core itself, or there is a separation

\[
                         (J_1,J_2),\qquad Q=J_1\cap J_2, \tag{3.2}
\]

with `|Q|<=3`, both open sides nonempty, and the four-terminal frame on one
side while a nontrivial substituted web piece lies on the other.

This is exactly the triangle-substitution clause in the Two Paths Theorem;
no planarity assertion is made about the substituted piece.

## 4. A web cell promotes to a full ambient adhesion

The separator `Q` in `J` need not separate `G`, because paths may use the
protected external bags.  Nevertheless it promotes canonically.

### Theorem 4.1 (protected available-graph separator to full adhesion)

Let `(J_1,J_2)` be any separation of `J`, with separator
`Q=J_1 intersect J_2`.  Let
`R_1 subseteq J_1-Q` and `R_2 subseteq J_2-Q` be nonempty connected sets.
Then `Q union mathcal C` separates `R_1` from `R_2` in `G`.  An
inclusion-minimal `R_1-R_2` subseparator `Z` satisfies

\[
                         Z\subseteq Q\cup\mathcal C.      \tag{4.1}
\]

If `G` is `s`-connected, then `|Z|>=s`; and the components `D_1,D_2` of
`G-Z` containing `R_1,R_2` are full to `Z`:

\[
                         N_G(D_1)=Z=N_G(D_2).             \tag{4.2}
\]

#### Proof

Every path avoiding `mathcal C` lies in `J`, where `Q` separates the two
open sides.  Thus `Q union mathcal C` is a separator in `G`, and a minimal
subseparator `Z` exists inside it.  Connectivity gives its order.  Restoring
any one vertex of a minimal separator creates an `R_1-R_2` path through
that vertex, proving adjacency to both distinguished components.  The
reverse containments follow because they are components of `G-Z`.  QED.

For `HC_7`, every such promoted adhesion has order at least seven, while
its non-model part `Z intersect Q` has order at most three.  Hence at least
four adhesion vertices lie in the five protected external bags.  This is
real portal capacity, but it does not by itself repeat a bag owner or align
with the two frame labels.

For the one-gate lock of Theorem 2.2 the count is stronger.

### Corollary 4.2 (one-gate promotion has protected trace surplus)

Assume the one-gate outcome of Theorem 2.2, and choose a component of
`J-q` meeting `U-{q}` and a component meeting `V-{q}`.  Let `Z` be an
inclusion-minimal separator between these components contained in
`{q} union mathcal C`, as in Theorem 4.1.  If `G` is `s`-connected, then

\[
 |Z\cap\mathcal C|\ge s-1.                              \tag{4.3}
\]

If the protected set is the union of `k-2` pairwise disjoint connected
model bags, their total boundary-trace rank on `Z` is at least

\[
             |Z\cap\mathcal C|-(k-2)\ge s-k+1,          \tag{4.4}
\]

whenever the right side is positive.  Here a trace unit is either an edge
inside `Z` belonging to one protected bag, or a connected carrier in one
component of that bag minus `Z` joining at least two of its boundary
vertices.

In particular, for `HC_7` the adhesion contains at least six protected-bag
vertices.  Since there are five protected bags, some named bag has at
least two adhesion vertices and supplies a nonzero connected trace.

#### Proof

The gate `q` separates the selected components in `J`, so
`{q} union mathcal C` separates them in `G`.  Theorem 4.1 gives
`|Z|>=s` and `Z subseteq {q} union mathcal C`, proving (4.3).

For every protected bag meeting `Z` in `p` vertices, contract the
components of the bag minus `Z` and take a spanning tree of the resulting
incidence graph.  Its terminal trace has rank exactly `p-1`.  Summing over
at most `k-2` nonempty protected bags gives

\[
 \sum (p_i-1)=|Z\cap\mathcal C|-\#\{i:C_i\cap Z\ne\varnothing\}
 \ge |Z\cap\mathcal C|-(k-2),
\]

which is (4.4).  Distinct-bag carriers are disjoint.  QED.

The trace is an actual connection packet inside a named model bag.  What
remains unproved is the ownership alignment which would turn it into the
missing label-preserving exchange across the gate.

The rank count is an incidence-tree rank, not a claim that all rank units
are represented by vertex-disjoint carriers: one component of a bag minus
`Z` may carry several units.  Only carriers belonging to distinct model
bags are automatically disjoint.

## 5. Canonical society state lock at a promoted cell

Suppose each open side in (3.2) contains a nontrivial connected vertex set
`U_h subseteq S` (`h=1,2`).  Since `G[S]` is induced bipartite, both are
connected induced bipartite societies in `G`.  Choose them inside the
distinguished components in Theorem 4.1.

Let `Sigma_h(Z)` be the equality partitions on `Z` induced by all
`(k-1)`-colourings of `G/U_h`.

### Theorem 5.1 (web-cell society states are disjoint)

One has

\[
                         \Sigma_1(Z)\cap\Sigma_2(Z)=\varnothing. \tag{5.1}
\]

Each contraction is tight:

\[
                         \chi(G/U_h)=\eta(G/U_h)=k-1.    \tag{5.2}
\]

#### Proof

Tightness is the bipartite-society contraction theorem and `HC_{k-1}`.
The two contraction branch sets lie in opposite open shores of the full
adhesion and leave the other closed shore literally unchanged.  If two
colourings induced the same equality partition on `Z`, align their palettes
on `Z` and splice the untouched closed shores.  This gives a
`(k-1)`-colouring of `G`, a contradiction.  QED.

The society theorem is useful because its contractions are chromatically
and Hadwiger-tight, but state disjointness itself does not require a
society.  The following boundary-faithful form also covers atomic sides.

### Theorem 5.2 (universal crossed-operation state lock)

Let `(P,Q)` be a separation of `G` with boundary `Z`, and suppose both open
sides are nonempty.  Let `M_P` be any proper minor obtained by an operation
supported wholly in `P-Z` which retains the closed `Q`-shore literally,
and define `M_Q` symmetrically.  For `r=k-1`, the equality partitions on
`Z` induced by `r`-colourings of `M_P` and `M_Q` are disjoint.

#### Proof

If two such colourings induce the same equality partition, permute one
palette so that they agree literally on `Z`.  Use the `M_Q` colouring on
the unchanged closed `P`-shore and the `M_P` colouring on `Q-Z`.  This
restores every vertex and edge of `G`: the operation in each colouring lies
on the open shore whose colours are discarded, and no edge joins the two
open shores.  The splice is an `r`-colouring of `G`, a contradiction.  QED.

Deleting one vertex in each open side supplies such a pair of operations,
even when a side is atomic.  Proper-minor minimality makes both minors
`r`-colourable.  Thus failure of a prescribed repair linkage has the exact
dynamic alternatives

\[
 \boxed{\text{planar web core}}
 \quad\text{or}\quad
 \boxed{\text{full promoted adhesion with crossed operation states}}.
                                                               \tag{5.3}
\]

Whenever both sides contain nontrivial induced bipartite societies,
Theorem 5.1 strengthens the second box by making both reference operations
tight society contractions.

There is also a tight operation available on every nonempty side.

### Corollary 5.3 (opposite tight deletion codes)

For any `u in P-Z` and `v in Q-Z`,

\[
                     \chi(G-u)=\chi(G-v)=k-1.           \tag{5.4}
\]

If `k` is the least failing Hadwiger parameter, then also

\[
                     \eta(G-u)=\eta(G-v)=k-1,           \tag{5.5}
\]

and the equality-partition sets on `Z` arising from their
`(k-1)`-colourings are disjoint.

#### Proof

Proper-minor minimality gives chromatic number at most `k-1`.  If, for
example, `G-u` were `(k-2)`-colourable, giving `u` one fresh colour would
`(k-1)`-colour `G`, a contradiction.  This proves (5.4).  At the least
failing parameter, `HC_{k-1}` and (5.4) give a `K_{k-1}` minor in each
deletion, while `K_k`-minor-freeness gives the reverse bound, proving
(5.5).  State disjointness is Theorem 5.2.  QED.

Thus a promoted gate or web adhesion is locked by two tight clique-model
states even when neither side contains a nontrivial society.  What society
contraction adds is prescribed rooting inside the open side, not tightness
itself.

The capacity and state conclusions combine in a form which covers both a
single gate and a packet-side barrier.

### Theorem 5.4 (connected-barrier capacity--state lock)

Let `W subseteq J` be connected and suppose that `W union mathcal C`
separates nonempty connected sets `R_1,R_2` disjoint from it.  Let `Z` be
an inclusion-minimal `R_1-R_2` separator contained in
`W union mathcal C`.  If `G` is `s`-connected, then:

1. `|Z|>=s`, and the two distinguished components of `G-Z` are full to
   `Z`;
2. the `k-1` pairwise disjoint connected carriers

   \[
                         W,C_1,\ldots,C_{k-2}            \tag{5.6}
   \]

   supply boundary traces of total rank at least

   \[
                         |Z|-(k-1)\ge s-k+1;             \tag{5.7}
   \]

3. for vertices `u,v` in the two opposite open components, the tight
   deletion models `G-u,G-v` have disjoint equality-state sets on `Z`.

Consequently, if `s>=k`, every such barrier carries both a nonzero concrete
connection trace and a crossed tight-state lock.

#### Proof

The first assertion is Theorem 4.1 with the available barrier `W` in place
of `Q`.  For each carrier in (5.6) meeting `Z` in `p` vertices, its exact
trace rank is `p-1`, by the incidence-tree construction used in Corollary
4.2.  At most `k-1` carriers meet `Z`, so the sum is at least
`|Z|-(k-1)`, proving (5.7).  The carriers are pairwise disjoint because
`W subseteq J=G-mathcal C` and the model bags are pairwise disjoint.
The final assertion is Corollary 5.3.  QED.

As above, (5.7) is additive rank across the connected carriers in (5.6),
not a promise of that many pairwise vertex-disjoint internal packets.

For the one-gate outcome take `W={q}`.  For outcome 3 of Theorem 2.3 take
`W=X` or `W=Y`, and choose the distinguished sets in components of the
corresponding available-graph deletion.  Thus every clean monotone
absorption failure now ends in the same capacity--state object.  The
remaining missing exchange is sharply localized: it must align one of the
trace carriers in (5.6) with a label absent from one packet, or force the
two tight state codes to meet.

## 6. The three-arm frame has an odd local-split parity

Let the three frame arms at `q` be numbered `1,2,3`.  Denote the two owner
terminals in arm `1` by `x_{12},x_{13}`, those in arm `2` by
`x_{21},x_{23}`, and those in arm `3` by `x_{31},x_{32}`.  The three label
pairs are

\[
                         x_{12}x_{21},\qquad
                         x_{23}x_{32},\qquad
                         x_{13}x_{31}.                   \tag{6.1}
\]

### Lemma 6.1 (odd arm parity)

In every two-colouring of these six terminals which separates the ends of
all three pairs in (6.1), an odd number of arms have their two local
terminals in different colours.  In particular, at least one arm must be
split internally by every label-preserving two-piece partition.

#### Proof

Write colours in `F_2` and put

\[
 d_1=x_{12}+x_{13},\quad
 d_2=x_{21}+x_{23},\quad
 d_3=x_{31}+x_{32}.
\]

The three pair constraints say

\[
 x_{12}+x_{21}=x_{23}+x_{32}=x_{13}+x_{31}=1.
\]

Adding them gives

\[
                              d_1+d_2+d_3=1,             \tag{6.2}
\]

which is the assertion.  QED.

For arm `h`, let `R_h` be the unique tree path between its two local owner
terminals.  It is a proper subpath of the original three-arm frame and lies
in the induced bipartite society `S`.  Contracting any nontrivial connected
subpath of `R_h` is therefore tight and carries a rooted `K_{k-1}`-model.

There are three canonical complementary linkage instances:

\[
\begin{array}{c|c}
\text{arm split locally}&\text{same-side terminal pairs}\\
\hline
1&(x_{12},x_{31}),\ (x_{13},x_{21})\\
2&(x_{21},x_{32}),\ (x_{23},x_{12})\\
3&(x_{31},x_{23}),\ (x_{32},x_{13})
\end{array}                                               \tag{6.3}
\]

### Theorem 6.2 (three-arm linkage or web-state reduction)

First, if one row of (6.3) has repeated terminals, the repeated society
vertex is a literal multi-label portal collision.  Otherwise all three rows
are clean four-terminal instances.  If one has a pair of vertex-disjoint
paths in `J`, those paths give a two-label repair packet by the connector
argument of Lemma 2.1.  If all three clean instances fail, each is a
four-terminal Two Paths obstruction and hence has the alternatives (5.3):
a planar web core or a promoted full adhesion with crossed operation
states.

Moreover, every successful global label-preserving split of the expanded
bag `widehat T` realizes at least one of the three linkage instances.

#### Proof

Suppose arm 1 is locally split.  The constraint on pair
`x_{13}x_{31}` makes `x_{31}` share the colour of `x_{12}`, while the
constraint on `x_{12}x_{21}` makes `x_{21}` share the colour of `x_{13}`.
The two connected global sides therefore contain vertex-disjoint paths for
the first row of (6.3).  The other rows follow cyclically.  Lemma 6.1 says
that every successful split has at least one locally split arm, proving the
last assertion.

Conversely, a linkage in one row consists of two disjoint connected paths
whose terminal sets contain one endpoint of each of the two named label
pairs on both paths.  Join the paths by a shortest connector as in Lemma
2.1; the resulting two packets are adjacent and both meet those two labels.

If a row has no linkage, apply Sections 3--5 to its four distinct terminals.
The collision case was separated at the outset precisely because the
four-terminal theorem cannot be invoked there.  QED.

Thus the three-arm frame no longer creates recursive raw arm cases.  It
produces a two-label repair packet, a multi-label collision, or one of the
same explicit web/state locks as the disjoint-pair frame.

## 7. HC7 accounting and exact residue

At `k=7` there are five external labels and at most two inherited
multi-label warehouse lobes.  The dynamic frame reduction gives:

1. either complementary linkage orientation produces a concrete two-label
   repair packet;
2. simultaneous failure in a clean two-frame gives a one-gate lock; its
   promoted full adhesion has at least six protected-bag vertices and a
   nonzero trace in a repeated protected bag;
3. a three-arm frame gives a multi-label collision, a two-label repair
   packet, or one of three clean Two Paths planar/operation-state locks;
4. after a two-label packet is obtained, every further label whose selected
   portals remain outside the packet is either absorbed monotonically or
   yields a single gate or a packet-side dominance barrier;
5. warehouse labels remain grouped in at most two named branches and are
   not silently counted as repaired by a direct-label packet.

To close the frame theorem one still needs one of the following genuinely
dynamic statements:

* a label-preserving absorption of the other three direct labels and the
  at most two warehouse charges into a parallel repair packet;
* exclusion of the planar web alternatives by seven-connectivity and
  the one-step operation states; or
* synchronization of the two disjoint operation-state sets at a promoted
  adhesion.

The note proves none of these final assertions.  Its advance is that both
tree frames now terminate in an explicit repair packet, a classical planar
web, or a genuine full-adhesion state lock rather than further raw cases.

## 8. Sharp static tests

The gate and planar alternatives are necessary under the static hypotheses.

1. The cycle `x-a-b-y-x`, with society bipartition
   `A={x,b}`, `B={a,y}` and portal pairs `(x,a)` and `(b,y)`, is a warning
   that one must test both orientations.  The same-shore orientation
   `(x,b),(a,y)` fails, but the crossed orientation succeeds through the
   disjoint edges `xy,ab`, producing the split `{x,y}` and `{a,b}`.
2. A genuine clean one-gate lock is the induced path
   `a_i-b_i-q-b_j-a_j`, with portal pairs `(a_i,b_i)` and `(a_j,b_j)`.
   Both orientations fail and the middle vertex `q` is the separator from
   Theorem 2.2.  This shows that the one-gate alternative cannot be removed
   under static hypotheses.
3. In a tree with centre `q` and three arms, put one owner pair across each
   pair of arms.  This is the three-arm frame.  The complementary linkage
   instances in (6.3) all fail in the bare tree, and the obstruction is
   atomic/planar rather than a hidden label-preserving split.
4. Maximal-society bi-support does not by itself eliminate the clean gate.
   Let `S` be the tree with vertices `q,a_i,b_i` (`1<=i<=5`) and edges
   `qb_i,b_ia_i`.  Give it bipartition
   `q,a_1,...,a_5` versus `b_1,...,b_5`.  Add a clique
   `c_1,...,c_5`, where `c_i` is adjacent to exactly `a_i,b_i` in `S`.
   Then `S` is an inclusion-maximal induced bipartite society, every
   singleton bag `{c_i}` is bi-supported, and

   \[
                          S,\{c_1\},\ldots,\{c_5\}
   \]

   is a `K_6`-model.  For distinct `i,j`, the clean portal pairs
   `(a_i,b_i),(a_j,b_j)` have gate `q`.  Nevertheless the graph has no
   `K_7` minor: eliminate each `a_i` and then each `b_i`; the fill graph
   left on `q,c_1,...,c_5` is `K_6`, so the elimination width is at most
   five.  This example fails seven-connectivity--its relevant separator is
   only `{q,c_i}`--and therefore isolates exactly why the six protected
   adhesion vertices in (2.6), rather than bi-support alone, are essential.
5. Even seven-connectivity, an exact full seven-adhesion, six protected
   adhesion vertices, and a repeated protected owner do not force `K_7`
   statically.  Let `I` be the icosahedron with edge set

   \[
   \begin{split}
   &01,05,07,08,0\!-\!11,12,15,16,18,23,26,28,29,34,36,39,3\!-\!10,\\
   &45,46,4\!-\!10,4\!-\!11,56,5\!-\!11,78,79,7\!-\!10,7\!-\!11,
     89,9\!-\!10,10\!-\!11,
   \end{split}
   \]

   where, for example, `0 11` denotes the edge `0-11`.  Form
   `G=I vee K_2`, with the two join vertices denoted `u,v`.  The set

   \[
             Z=\{1,5,7,8,11,u,v\}
   \]

   is a full seven-cut with shores `{0}` and `{2,3,4,6,9,10}`.  The six
   bags

   \[
       \{0,1,2\},\quad\{3\},\quad\{4,5\},\quad
       \{7,8,9,11\},\quad\{u\},\quad\{v\}
   \]

   form a `K_6`-model.  Taking `q=1`, the root bag crosses both shores,
   `Z subseteq {q} union mathcal C`, six vertices of `Z` are protected,
   one protected bag misses `Z`, and another contains three vertices of
   `Z`.

   Nevertheless `G` has no `K_7` minor.  The icosahedron is planar, so it
   has no `K_5` minor.  In any hypothetical seven-bag model in
   `I vee K_2`, deleting the at most two bags containing `u,v` would leave
   at least five pairwise adjacent branch sets wholly in `I`, a
   contradiction.  The graph is seven-connected: if a join vertex
   survives a deletion of at most six vertices it connects the remainder;
   if both are deleted, at most four icosahedron vertices were deleted and
   the icosahedron is five-connected.  The displayed cut proves equality.

   This example has no asserted maximal-society clean-frame realization
   and is six-colourable.  It sharply falsifies every attempted closure
   using only connectivity, owner counts, or the repeated trace.  A valid
   closure must use the contraction-critical crossed operation states (or
   additional maximal-society incidence) in an essential way.

Mutually adjacent external label bags may be added at the selected portal
vertices to realize the first three examples inside fixed clique models.  These
examples are deliberately low-connectivity and need not be
contraction-critical or target-minor-free.  They show exactly why the
full-adhesion state information, rather than the static frame alone, is
needed for the next step.
