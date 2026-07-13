# A rooted five-packet: transversal fan, exact cut, or multiplicity

## 1. Setting

Let `G` be seven-connected.  Let `X` be a set of eight vertices such
that `G-X` has two anticomplete connected components `C,R`, both full to
`X`.  Put

\[
                         J=G[C\cup X].                         \tag{1.1}
\]

Suppose `J` contains five pairwise disjoint, pairwise adjacent connected
bags `L_1,...,L_5`, with

\[
                         L_i\cap X=\{b_i\},                    \tag{1.2}
\]

where the `b_i` are distinct.  Let `t in X-{b_1,...,b_5}`.  Finally let
`P` be a connected subgraph of `J` such that

\[
 P\cap X=\{t\},\qquad
 P\cap\bigcup_iL_i=\varnothing,\qquad
 P\cap C\ne\varnothing.                                      \tag{1.3}
\]

A **transversal `P`-fan** is a family of five paths, one ending in each
`L_i`, which are mutually vertex-disjoint outside `P`, meet `P` in their
initial vertices, and otherwise avoid `P` and all leaf bags except at
their final vertices.

## 2. The sound Menger trichotomy

### Theorem 2.1 (transversal fan, exact seven-cut, or multiplicity)

Under the hypotheses above, at least one of the following holds.

1. A transversal `P`-fan exists, and `G` has the explicit `K_7` bags

   \[
                 R,\quad A,\quad L_1,\ldots,L_5,               \tag{2.1}
   \]

   where `A` is a connected enlargement of `P` disjoint from all
   `L_i`.
2. There are a four-vertex set `S subseteq V(J)-P` and a component `U` of
   `J-S` such that

   \[
        P\subseteq U,qquad
        U\cap\bigcup_iL_i=\varnothing,qquad
        U\cap X=X-\{b_1,\ldots,b_5\}.                         \tag{2.2}
   \]

   The set

   \[
        K=S\mathbin{\dot\cup}(X-\{b_1,\ldots,b_5\})           \tag{2.3}
   \]

   is an exact seven-cut of `G`.
3. There are five paths from `P` to `union_i L_i`, mutually disjoint
   outside `P`, but every such five-path fan has two final vertices in
   the same leaf bag.  This is the **multiplicity obstruction**.

### Proof

Apply ordinary vertex Menger to `P` and the union of the five leaf bags,
with paths stopped at their first leaf-bag vertex.  If there are five
disjoint paths, then either their final bags are distinct, giving a
transversal fan, or outcome 3 holds.

In the transversal case, form `A` from `P` and all vertices of the paths
before their final vertices in the `L_i`.  Then `A` is connected,
disjoint from the leaves, and adjacent to each.  The leaf bags are
pairwise adjacent.  Fullness of `R` gives `R-A` adjacency through
`t in A cap X` and `R-L_i` adjacency through `b_i`.  Hence (2.1) is a
literal `K_7` model.

If there are at most four disjoint paths to the leaf union, Menger gives
a set `S` of order at most four, disjoint from `P`, which separates `P`
from every surviving vertex of every `L_i`.  The separator is allowed to
contain target vertices; excluding that possibility would be false.  Let
`U` be the component of `J-S`
containing `P`, and put `Z=U cap X`.  All five roots `b_i` lie outside
`U`, so

\[
                              |Z|\le3.                           \tag{2.4}
\]

After restoring the opposite shore `R`, the set `S union Z` separates
the nonempty set `U-Z` from `R` and the five leaves.  Its order is at
most seven.  Seven-connectivity forces equality throughout:

\[
          |S|=4,\qquad |Z|=3.                                  \tag{2.5}
\]

The only three boundary vertices outside the five roots are therefore
all in `U`, proving (2.2), and `S union Z` is the exact cut (2.3).  QED.

## 3. Why the former subset-Rado claim was invalid

A capacitated target-bag flow can use another leaf bag as a terminal
barrier.  Its dual set need only separate the chosen target after those
other leaf bags are deleted; it need not separate it in the original
closed shore.  Since the leaf bags here are pairwise adjacent, restoring
them can completely bypass that dual set.

Therefore no `h=2,3,4` global-cut rows follow from target-capacitated
Rado alone.  Outcome 3 records exactly the repeated-target case which
that invalid inference suppressed.

## 4. Minimum fragments eliminate only the cut outcome

### Corollary 4.1

Assume `C` is contained in a component `D` of minimum order among the
components behind all exact seven-cuts of `G`.  Then outcome 2 of
Theorem 2.1 is impossible.

#### Proof

The separator `S` contains a vertex of `C`.  Otherwise `S subseteq X`;
as `|S|=4`, some leaf root `b_i` survives.  Connectedness of `C`,
`P cap C ne empty`, and fullness of `C` to `b_i` would give a
`P`--`b_i` path avoiding `S`, contrary to the choice of `S`.

Let `A` be the component of `G-K` containing a vertex of `P cap C`.
Its neighbourhood is contained in the seven-set `K`; seven-connectivity
forces `N_G(A)=K`.  Thus `A` is a component behind an exact seven-cut.
Because `S cap C` is nonempty,

\[
                              |A|<|C|\le|D|,                     \tag{4.1}
\]

contrary to the minimum choice of `D`.  QED.

The global minimum does not eliminate outcome 3.  Closing that repeated-
target fan is the exact packet-exchange problem still requiring leaf-bag
rerouting or proper-minor state novelty.

## 5. Fullness at the exact cut

In outcome 2, every component `Q` of `G-K` is collectively full to `K`.
Indeed `N_G(Q) subseteq K`, while seven-connectivity gives
`|N_G(Q)|>=7=|K|`.  In particular the source component and the component
containing `R` and all five pairwise adjacent leaf bags are two full
shores of the new exact-seven adhesion.

This forced fullness is useful but does not by itself give a matching
from the four vertices of `S` into five leaf bags.  It records contact
with the target component, not with five prescribed subbags inside that
component.  Any recombination must use a port-labelled split of that
component, rather than treating it as one black-box full shore.

## 6. Trust boundary

The theorem now has no hidden terminal-capacity inference.  It gives
literal `K_7` bags in outcome 1 and the literal exact cut
`S union (X-{b_1,...,b_5})` in outcome 2.  Outcome 3 is not called a
separator: it is the precise geometric obstruction to converting
ordinary Menger capacity into one contact with each rooted leaf bag.

## 7. Build the leaf bags after the fan: the `W_5` skeleton

The exact-eight application has extra structure which avoids fixing the
two nonsingleton leaf bags too early.  Let

\[
 B=\{z,r_1,r_2,r_3,r_4\}
\]

induce `W_5`, with missing rim pairs `r_1r_3,r_2r_4`.  Suppose `J`
contains vertex-disjoint paths

\[
 W_{13}:r_1\leadsto r_3,qquad
 W_{24}:r_2\leadsto r_4,                                \tag{7.1}
\]

whose interiors avoid `X`.  Assume also that the seed `P` in (1.3) is
disjoint from `W_{13} union W_{24} union {z}`.

### Lemma 7.1 (balanced skeleton fan completion)

If there is a five-path fan from `P` to

\[
                  W_{13}\cup W_{24}\cup\{z\}                  \tag{7.2}
\]

whose endpoint counts on `W_{13},W_{24},{z}` are `2,2,1`, respectively,
then `G` contains a `K_7` model.

#### Proof

On each path `W_ij`, its two fan
endpoints are distinct.  Choose an edge of `W_ij` lying strictly between
them in the linear order.  The two components obtained by deleting that
edge are connected bags rooted at `r_i,r_j`, one containing each fan
endpoint, and they are adjacent across the deleted edge.  Together the
four path segments and `{z}` are five disjoint bags.

They are pairwise adjacent: the two repaired missing pairs use the two
chosen cut edges, and every other pair uses the corresponding literal
root edge of `W_5`.  Form a sixth bag from `P` and the five fan prefixes,
excluding their final skeleton vertices.  It is connected, disjoint from
the five leaf bags, and adjacent to all of them.  The opposite full shore
`R` is adjacent to it through `t` and to every leaf through its boundary
root.  These are the seven explicit clique-model bags.

This proves the lemma.  QED.

No separator conclusion follows from ordinary Menger alone here: a
minimum separator may contain vertices of the repair skeleton itself.
The quota-rank theorem below is the sound statement which permits target
vertices in the separator and keeps track of the corresponding lost
boundary roots.

## 8. The quota-rank theorem: only skeleton transit remains

There is a stronger way to separate rank failure from geometry.  Put

\[
 Y_1=V(W_{13}),\qquad Y_2=V(W_{24}),\qquad Y_3=\{z\},
 \qquad(q_1,q_2,q_3)=(2,2,1).                         \tag{8.1}
\]

Let `M` be the gammoid on `Y=Y_1 dotunion Y_2 dotunion Y_3`: a set of
vertices is independent when it is the endpoint set of mutually
vertex-disjoint paths from the connected source `P` (paths may share
vertices of `P`).  At this stage paths are allowed to pass through other
vertices of `Y` before their final endpoints.  This qualification is
essential.

### Theorem 8.1 (finite quota-rank dichotomy)

At least one of the following holds.

1. There is an exact seven-cut strictly inside the closed shore.  More
   precisely, for one of the seven nonempty subsets
   `I subseteq {1,2,3}`, there is a `P`--`union_{i in I}Y_i`
   separator `S` with

   \[
                 |S|\le q(I)-1,
                 \qquad q(I)=\sum_{i\in I}q_i,                 \tag{8.2}
   \]

   and this lifts through `R` to a global cut of order exactly seven.
2. There are five disjoint `P`-paths whose final endpoints consist of
   two vertices of `Y_1`, two of `Y_2`, and `z`.

If outcome 2 has a choice of paths whose internal vertices avoid all of
`Y`, then `G` has the explicit `K_7` model of Lemma 7.1.  Hence, at a
global minimum exact-seven fragment in a `K_7`-minor-free graph, every
balanced linkage in outcome 2 must meet a nonfinal skeleton group
internally.  This is the **skeleton-transit obstruction**.

#### Proof

Apply Rado's theorem to the gammoid `M` and the multiset consisting of
two copies of `Y_1`, two copies of `Y_2`, and one copy of `Y_3`.  A full
independent transversal is exactly outcome 2.  If none exists, Rado
gives a nonempty set of copies whose union has gammoid rank smaller than
the number of copies.

Copies of the same group have the same union.  Enlarging a chosen proper
subcollection of copies of one group to all `q_i` copies leaves the union
unchanged and only strengthens the inequality.  Thus one of only seven
group subsets `I` satisfies

\[
             r_M\!\left(\bigcup_{i\in I}Y_i\right)
                         \le q(I)-1.                            \tag{8.3}
\]

Menger supplies the separator `S` in (8.2), in the original graph `J`;
unlike the retracted target-capacity argument, no other skeleton group
has been made an absorbing barrier.

Let `U` be the component of `J-S` containing `P`, and put `Z=U cap X`.
The target union in (8.3) contains exactly `q(I)` of the five boundary
roots in `B`: two for each selected repair path and one when `Y_3` is
selected.  Some of those roots may lie in `S`, but every one lies outside
`Z`.  Consequently

\[
                              |Z|\le8-q(I).                      \tag{8.4}
\]

Restoring `R`, the set `S union Z` separates `U-Z` from `R` and from at
least one surviving target vertex.  Hence

\[
  7\le |S\cup Z|
     =|S|+|Z|
     \le(q(I)-1)+(8-q(I))=7.                                  \tag{8.5}
\]

This is the exact seven-cut in outcome 1.  (For `I={3}`, connectedness
already rules out rank zero, so that nominal row never occurs.)

If `C` lies in a globally minimum component `D` behind an exact
seven-cut, outcome 1 is impossible.  Every live deficient set `I`
contains `1` or `2`, since the singleton row `I={3}` is impossible.
Thus its target union contains an internal vertex of one of the repair
paths in `C`.  The separator `S` must meet `C`: otherwise connectedness
of `C` joins `P cap C` to that internal target vertex while avoiding
`S subseteq X`.  The component of `G-(S union Z)` containing
`P cap C` is therefore a proper subset of `C`, has neighbourhood the
exact seven-set `S union Z`, and is smaller than `D`, contradicting the
global minimum choice.

If Rado instead supplies the full independent transversal, take its five
linkage paths.  When their interiors avoid `Y`, they are a first-hit fan
with endpoint counts `2,2,1`; the segmentation proof of Lemma 7.1 gives
the seven displayed bags.  If every balanced linkage transits `Y`, the
last stated obstruction is exactly what remains.  QED.

The seven quota rows are

\[
\begin{array}{c|c|c}
 I&q(I)&|S|\le q(I)-1\\ \hline
 \{1\},\{2\}&2&1\\
 \{3\}&1&0\\
 \{1,2\}&4&3\\
 \{1,3\},\{2,3\}&3&2\\
 \{1,2,3\}&5&4.
\end{array}                                                   \tag{8.6}
\]

No portal labels occur in this list.  All remaining difficulty is the
single geometric question of removing a nonfinal skeleton transit from a
balanced gammoid linkage while preserving disjointness.

## 9. Finite normal form of the transit obstruction

Take a balanced linkage from outcome 2 of Theorem 8.1 and truncate every
path at its first vertex of `Y`.  Let

\[
                         p=(p_1,p_2,p_3)                         \tag{9.1}
\]

be the numbers of truncated endpoints in the three groups.  The paths
are disjoint, so `p_3<=1`, and `p_1+p_2+p_3=5`.

### Lemma 9.1 (surplus-to-deficit bridge)

In a `K_7`-minor-free realization at a global minimum,

\[
                              p\ne(2,2,1).                       \tag{9.2}
\]

Up to interchanging the two repair paths, the only possibilities are

\[
 \begin{array}{c|c}
 p_3=1&(4,0,1),(3,1,1)\\
 p_3=0&(5,0,0),(4,1,0),(3,2,0),
          (2,3,0),(1,4,0),(0,5,0).
 \end{array}                                                    \tag{9.3}
\]

(The last row is left unsymmetrized to display all endpoint counts.)
Moreover the original balanced linkage contains a path segment joining
two distinct skeleton groups, with interior outside `Y`, which transports
one unit from a group surplus in `p-q` toward a group deficit.

#### Proof

If `p=(2,2,1)`, the truncated paths are a first-hit fan with the balanced
counts of Lemma 7.1, and its explicit segmentation gives `K_7`.  This
proves (9.2).  The integer solutions to `p_1+p_2+p_3=5`, `p_3<=1`, after
removing `(2,2,1)`, are exactly (9.3), modulo the stated symmetry.

Record, for each original linkage path, its first-hit group and its final
group.  The resulting directed group multigraph has outdegree vector `p`
and indegree vector `q=(2,2,1)`.  Since `p!=q`, it carries positive net
flow out of a surplus group and into a deficit group.  Following this
flow gives an off-diagonal transition directed toward a deficit.  Along
the corresponding linkage path, take two consecutive visits to distinct
skeleton groups.  The subpath between them has interior outside `Y`.
Linkage disjointness makes it disjoint from all other linkage paths, and
it is the asserted clean group-to-group bridge.  QED.

Thus the final packet exchange no longer ranges over arbitrary portals.
It has two repair paths, one universal root, one of the endpoint-count
vectors (9.3), and a clean surplus-to-deficit bridge.  A successful
bridge-switch lemma must use that bridge either to move a centre contact
without breaking the repaired missing pair, or to expose one more exact
seven-cut.

The existence of the bridge is **not** itself a packet theorem.  A
diagnostic exhaustive search on the smallest skeleton
`W_1=a_0-a_1-a_2`, `W_2=b_0-b_1-b_2`, with first-hit roots
`a_0,a_1,a_2,b_1,z` and the cross edge `a_1b_1`, finds no clique model
with five connected bags rooted at those five marks.  The corresponding
search over all single-crosslink endpoint choices is likewise negative.
Thus the bridge must be combined
with atomic portal surplus or proper-minor operation novelty; it cannot
simply be absorbed as an automatic repair.  This diagnostic is a warning
about the next lemma, not an asserted counterexample to the full
seven-connected critical configuration.

## 10. Exact leaf split for an arbitrary repeated bag

For the original multiplicity outcome, the label-preserving split is now
proved in `hadwiger_full_shore_packet_leaf_split.md`.  If the fan-end
distribution is

\[
                          L,L,N_1,N_2,N_3
\]

and `M` is missed, take a spanning portal tree in `L`, with repeated ends
`u,v`, root `b`, three retained portal classes `Q_1,Q_2,Q_3`, and missed
class `Q_M`.  For either repeated end `e`, project the four portal classes
onto the arm from `e` to the `b`--other-end path and put

\[
 \alpha_e=\text{first projected }Q_M\text{ position},\qquad
 \beta_e=\min_j\text{(last projected }Q_j\text{ position)}.
\]

If `alpha_e<beta_e`, one tree edge splits off a connected piece containing
`e` and a missed-leaf portal while the residual contains the other fan
end, the root, and all three retained portal classes.  Absorb the split
piece into `M`.  The split edge supplies the residual--`M` adjacency, so
no second `L-M` portal is assumed.  The literal seven bags are

\[
 R,\quad P^+,\quad L_{\rm residual},\quad
 M\cup L_{\rm peel},\quad N_1,\quad N_2,\quad N_3.
\]

If neither end opens, each has a blocker label `j_e in {1,2,3}` whose
last portal occurs no deeper than the first missed-leaf portal.  These
two inequalities have a certificate in a labelled topological tree on
at most twenty vertices.  Thus the sound residual is a bounded two-ended
ordered blocker skeleton, not an arbitrary five-portal tree.

Tree minimality alone cannot promote that skeleton to an ambient cut:
an internal corridor vertex can have arbitrarily many neighbours outside
the bag.  An actual order-seven cut requires the additional portal/
interface-surplus data of the ambient seven-connected graph.
