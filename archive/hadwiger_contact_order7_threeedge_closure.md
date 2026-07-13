# Order-seven contact separators: closure through three missing edges

## 1. Setting

Let (G) be a hypothetical proper-minor-minimal counterexample to
(mathrm{HC}_7). Fix a vertex (v), a contact-maximal (K_6)-model in
(G-v), and an inclusion-minimal separator (S) inside the union of the
contact bags separating (v) from the connected union of the noncontact
bags. Let (D_v,D_C) be the components of (G-S) containing (v) and
the noncontact bags, respectively.

Minimality of (S) gives the following facts:

* (D_v) and (D_C) are connected and disjoint;
* they are different components of (G-S), hence anticomplete; and
* each is adjacent to every vertex of (S).

We call them the two distinguished full shores.

The preceding full-shore augmentation lemma also gives

\[
  \eta(G[S])\le 5,                                      \tag{1.1}
\]

because a (K_6)-model in (G[S]), together with either full shore,
would be a (K_7)-model.

This note proves a stronger elementary consequence when (|S|=7):

\[
  \boxed{|E(\overline{G[S]})|\ge 4.}                   \tag{1.2}
\]

No coloring argument is needed.

## 2. Two-shore vertex-cover lemma

### Lemma 2.1

Let (Ssubseteq V(G)) have order (m), and let (D_1,D_2) be disjoint
connected subsets of (G-S), each adjacent to every vertex of (S).
If

\[
  \tau(\overline{G[S]})\le 2,
\]

then (G) contains a (K_m)-minor.

#### Proof

Choose distinct (x,yin S) such that every nonedge of (G[S]) is
incident with (x) or (y). (If a minimum vertex cover has order zero
or one, add arbitrary vertices until two distinct vertices have been
chosen.) Consider the bags

\[
  D_1\cup\{x\},\qquad D_2\cup\{y\},\qquad
  \{z\}\quad(z\in S-\{x,y\}).                         \tag{2.1}
\]

There are (m) bags. Each of the first two is connected because its
shore touches its boundary vertex. The singleton bags form a clique,
since (S-\{x,y\}) contains no nonedge. Each shore bag is adjacent to
every singleton bag because its shore is full to (S). Finally the two
shore bags are adjacent: (D_1) has an edge to (y), which belongs to
the second bag (and symmetrically (D_2) touches (x)). Thus (2.1) is a
(K_m)-model. \(\square\)

The two shores need not be adjacent to one another; their boundary
anchors create the required adjacency.

## 3. The exceptional three-matching

Every graph with at most three edges has vertex-cover number at most two,
except the three-edge matching (3K_2). The latter also closes in the
presence of two full shores.

### Lemma 3.1

Let

\[
 S=\{a,a',b,b',c,c',r\}
\]

and suppose that the only nonedges of (G[S]) are

\[
 aa',\qquad bb',\qquad cc'.                            \tag{3.1}
\]

If (D_1,D_2) are two disjoint connected full shores for (S), then
(G) contains a (K_7)-minor.

#### Proof

On the six-vertex boundary (S-\{a\}), the only nonedges are
(bb') and (cc'). It has the following (K_5)-model:

\[
 \{b\},\qquad \{c\},\qquad \{a'\},\qquad \{r\},
 \qquad \{b',c'\}.                                    \tag{3.2}
\]

The last bag is connected, sees (b) through (c'), and sees (c)
through (b'); every other required adjacency is present. Append
(D_1\cup\{a\}) and (D_2) to (3.2). The first appended bag is
connected. Both appended bags see every bag in (3.2), since those bags
contain boundary vertices. They see each other because (D_2) has an
edge to (a), which belongs to (D_1\cup\{a\}). Thus the seven bags
form a (K_7)-model. \(\square\)

## 4. Closure through three missing edges

### Theorem 4.1

In the setting of Section 1, if (|S|=7), then

\[
 |E(\overline{G[S]})|\ge4.
\]

#### Proof

Suppose that the complement has at most three edges. If it is not
(3K_2\dot\cup K_1), those at most three edges have a vertex cover of
order at most two: if three pairwise disjoint edges do not occur, take
one endpoint cover greedily, or equivalently inspect the possible
components (a star, a path, a triangle, or a two-edge component plus one
independent edge). Lemma 2.1, with (D_1=D_v) and (D_2=D_C), then
gives a (K_7)-minor. If the complement is
(3K_2\dot\cup K_1), Lemma 3.1 gives the same contradiction. \(\square\)

For completeness, the short covering assertion used above can be seen
without classification. If a graph (F) with at most three edges has no
two-vertex cover, then after choosing any edge (uv), the edges outside
(u) and outside (v) cannot be covered by one common endpoint. With
only two remaining edges this forces all three edges to be pairwise
disjoint, so (F=3K_2) plus isolated vertices.

## 5. A further four-edge closure

The first four-edge geometry also closes.

### Lemma 5.1 (four-cycle complement)

Suppose

\[
 \overline{G[S]}=C_4\mathbin{\dot\cup}(|S|-4)K_1.
\]

If (D_1,D_2) are two disjoint connected full shores for (S), then
(G) contains a (K_{|S|})-minor.

#### Proof

Label the complementary four-cycle (x_1y_1x_2y_2x_1). In (G[S]),
the pairs (x_1x_2) and (y_1y_2) are edges. Use the bags

\[
 D_1\cup\{x_1,x_2\},\qquad \{y_1\},\qquad \{y_2\},
 \qquad \{r\}\ (r\in S-\{x_1,x_2,y_1,y_2\}),
 \qquad D_2.                                           \tag{5.1}
\]

There are (1+2+(|S|-4)+1=|S|) bags. The first is connected, and its
full shore makes it adjacent to every boundary-containing bag. The
vertices (y_1,y_2) are adjacent in (G[S]), and all vertices outside
the complementary cycle are universal in (G[S]), so all singleton
bags are pairwise adjacent. The last bag (D_2) sees every
boundary-containing bag. It also sees the first bag through either
(x_1) or (x_2). Thus (5.1) is a (K_{|S|})-model. \(\square\)

Consequently an order-seven contact separator in a hypothetical
(mathrm{HC}_7) counterexample has at least four missing boundary
edges, and the four missing edges cannot form (C_4) plus isolates.
The next sharp cyclic core is

\[
  \overline{G[S]}=C_5\mathbin{\dot\cup}2K_1,
  \qquad G[S]=C_5\vee K_2.                            \tag{5.2}
\]

Contracting each full shore to one universal, mutually nonadjacent
helper does not by itself create a (K_7)-minor in (5.2); hence further
connectivity or internal-shore structure is genuinely required there.

## 6. A two-vertex distinguished shore closes the five-cycle core

The next finite core also has a direct hand solution when either full
shore has exactly two vertices.  Importantly, contracting the opposite
shore does **not** preserve minimum degree.  The proof below uses minimum
degree only at the two vertices of the uncontracted shore.

### Lemma 6.1 (two-vertex shore)

Assume

\[
 |S|=7,\qquad G[S]=C_5\vee K_2,
\]

and let (D_1=\{x,y\}) be a component of (G-S), where (xy\in E(G)),
that is full to (S).  Let (D_2) be a second connected full shore.  If
(delta(G)\ge7), then (G) contains a (K_7)-minor.

#### Proof

Write the cycle part of (S) as (C) and the two universal boundary
vertices as (r_1,r_2).  Since (D_1) is a whole component of (G-S),
the only neighbours of (x) outside (S) consist of (y), and
similarly for (y).  Minimum degree seven therefore gives

\[
 |N(x)\cap S|\ge6,\qquad |N(y)\cap S|\ge6.             \tag{6.1}
\]

Let (M\subseteq C) be the set of cycle vertices missed by at least one
of (x,y).  Then (|M|\le2).  The vertex-cover number of (C_5) is
three, so there is a cycle edge (ab) disjoint from (M).  Hence both
(x) and (y) are adjacent to both (a) and (b).

Among the three vertices of (C-\{a,b\}), choose distinct vertices
(c,d) such that (xc,yd\in E(G)).  This is always possible: each of
(x,y) forbids at most one of the three candidates, so the two allowed
sets, each of order at least two, have distinct representatives.

Now use the seven bags

\[
 \{a\},\quad \{b\},\quad \{r_1\},\quad \{r_2\},
 \quad \{x,c\},\quad \{y,d\},\quad D_2.               \tag{6.2}
\]

The two nonsingleton boundary bags are connected by the choices of
(c,d), and they are adjacent to each other through (xy).  They see
(a,b) through (x,y), respectively, and see (r_1,r_2) through their
cycle anchors (c,d).  The first four singleton bags are pairwise
adjacent because (ab) is a cycle edge and (r_1,r_2) are universal in
(G[S]).  Finally (D_2) sees every other bag because each contains a
vertex of (S).  Thus (6.2) is a (K_7)-model. \(\square\)

The dependency-free script `c5_core_k2_shore_verify.py` independently
checks all (8^2=64) possible choices of the (optional) unique missed
boundary neighbour of (x) and (y), using an exact branch-set search.

## 7. Complete closure of the four-edge layer

In fact every four-edge complement closes with the two full shores.

### Lemma 7.1 (the three high-cover types)

Let (|S|=7), let (D_1,D_2) be two disjoint connected full shores,
and suppose (F=\overline{G[S]}) has four edges and
(\tau(F)\ge3).  Then (G) contains a (K_7)-minor.

#### Proof

There are only three possible isomorphism types for (F):

\[
 K_3\dot\cup K_2\dot\cup2K_1,
 \qquad P_4\dot\cup K_2\dot\cup K_1,
 \qquad P_3\dot\cup2K_2.                              \tag{7.1}
\]

Here is a quick derivation.  If (F) has a three-edge matching, its
fourth edge either joins two of the matching edges, giving
(P_4\dot\cup K_2\dot\cup K_1), or joins a matching endpoint to the
seventh vertex, giving (P_3\dot\cup2K_2).  Otherwise
(\nu(F)\le2).  A vertex of degree at least three, together with one
endpoint of the at most one remaining edge, would cover (F), so
(\Delta(F)\le2).  Thus (F) is a union of paths and cycles.  The
four-edge unions having cover number at least three are the two
matching-three types just listed and
(K_3\dot\cup K_2\dot\cup2K_1).

It remains to display models.  In the following lists, every unnamed
vertex is used as a singleton bag.

* If the missing edges are the triangle (ab,bc,ca) and the edge
  (de), with isolates (f,g), use

  \[
    \{a\},\{d\},\{f\},\{g\},D_1,\{b,e\},D_2\cup\{c\}.
  \]

* If the missing edges are the path (ab,bc,cd) and the edge (ef),
  with isolate (g), use

  \[
    \{a\},\{c\},\{e\},\{g\},D_1,\{b,f\},D_2\cup\{d\}.
  \]

* If the missing edges are the path (ab,bc) and the edges (de,fg),
  use

  \[
    \{a\},\{c\},\{d\},\{f\},D_1,\{b,e\},D_2\cup\{g\}.
  \]

Each displayed two-piece boundary bag is connected because its two
boundary vertices are not an edge of (F), or because a full shore
connects to its anchor.  Directly from the displayed missing-edge list,
the four singleton boundary bags form a clique, the ordinary two-vertex
bag sees all of them, and its boundary vertices also make it adjacent to
the anchored shore bag.  The unanchored full shore sees every
boundary-containing bag; the anchored shore bag sees it through its
boundary anchor.  Hence every list is a (K_7)-model. \(\square\)

### Theorem 7.2

In the setting of Section 1, if (|S|=7), then

\[
  \boxed{|E(\overline{G[S]})|\ge5.}                   \tag{7.2}
\]

#### Proof

Theorem 4.1 handles at most three missing edges.  Suppose there are four.
If their vertex-cover number is at most two, Lemma 2.1 gives a
(K_7)-minor.  If it is at least three, Lemma 7.1 does. \(\square\)

The dependency-free verifier `contact_order7_four_edge_verify.py`
independently enumerates all

\[
 \binom{\binom72}{4}=5985
\]

labelled four-edge complements.  For each it constructs the quotient
with two nonadjacent full helpers and checks an exact connected
seven-branch-set model.  It also replays the three hand models above.

## 8. Exact five-edge quotient classification

For five missing edges the two-helper quotient has exactly two
exceptions.

### Proposition 8.1 (finite, exhaustively certified)

Let (|S|=7), let (F=\overline{G[S]}) have exactly five edges, and add
two nonadjacent vertices (h_1,h_2), each complete to (S).  The
resulting nine-vertex graph has a (K_7)-minor unless

\[
 F\cong C_5\dot\cup2K_1
 \quad\hbox{or}\quad
 F\cong K_3\dot\cup2K_2.                              \tag{8.1}
\]

#### Certificate

The dependency-free script `contact_order7_five_edge_verify.py`
enumerates all

\[
 \binom{21}{5}=20349
\]

labelled five-edge graphs (F).  For each it constructs all connected
subsets of the nine-vertex quotient and performs a complete recursive
search for seven pairwise disjoint, pairwise adjacent connected branch
sets.  Every positive answer is independently replayed for disjointness,
connectivity, and all 21 bag adjacencies.  The 357 negative labelled
instances are compared, as edge-bitmasks, against the full permutation
orbits of the two graphs in (8.1): the (C_5\dot\cup2K_1) orbit has 252
members and the (K_3\dot\cup2K_2) orbit has 105.  The sets agree
exactly.  The two representatives are also independently rerun through
the exhaustive negative search.

Thus, for two arbitrary connected full shores (D_1,D_2), contracting
each shore proves a (K_7)-minor in every five-edge boundary type except
the two in (8.1).  No degree or connectivity information internal to a
shore is used in this quotient classification.

## 9. A third component closes both sharp five-edge cores

### Lemma 9.1 (all components are full)

Suppose (G) is seven-connected, (|S|=7), and (D) is a component of
(G-S).  Then (N(D)=S).

#### Proof

The neighbourhood (N(D)) is contained in (S) and separates (D)
from the rest of the graph.  Seven-connectivity gives
(|N(D)|\ge7), so equality holds and (N(D)=S). \(\square\)

### Lemma 9.2 (three-shore closure)

Let (D_1,D_2,D_3) be three distinct components of (G-S), all full to
an order-seven boundary (S).  If either graph in (8.1) is
(\overline{G[S]}), then (G) contains a (K_7)-minor.

#### Proof

First suppose the complement is (C_5\dot\cup2K_1).  Equivalently,
write

\[
 G[S]=C_5\vee K_2,
\]

with a cycle (0,1,2,3,4,0) and universal vertices (r_1,r_2).  Use

\[
 \{0\},\quad\{1\},\quad\{r_1\},\quad\{r_2\},
 \quad D_1,\quad D_2\cup\{2\},\quad D_3\cup\{3\}.     \tag{9.1}
\]

The four singleton bags form a clique.  Each shore bag sees every
boundary-containing bag, and the two anchored shore bags see each other
through either shore's edge to the other's anchor.  The unanchored shore
sees both anchored bags through their anchors.  Hence (9.1) is a
(K_7)-model.

Next suppose the missing edges are a triangle on (0,1,2) and the two
independent edges (34,56).  Use

\[
 \{0\},\quad\{3\},\quad\{1,4\},\quad\{5\},
 \quad D_1,\quad D_2\cup\{2\},\quad D_3\cup\{6\}.      \tag{9.2}
\]

The bag ({1,4}) is connected.  The four boundary-only bags in (9.2)
are pairwise adjacent: each listed missing edge has at least one endpoint
outside each relevant pair of bags.  The same full-shore argument as for
(9.1) checks every adjacency involving (D_1,D_2,D_3).  Thus (9.2) is
a (K_7)-model. \(\square\)

### Corollary 9.3

In a seven-connected (K_7)-minor-free realization of either sharp core
in (8.1), (G-S) has exactly two components, namely the two
distinguished full shores.

#### Proof

There are at least the two distinguished components.  A third component
would be full by Lemma 9.1 and would contradict Lemma 9.2. \(\square\)

Consequently there are no hidden exterior neighbours in the two sharp
cores.  For every (s\in S), minimum degree seven gives the exact useful
lower bound

\[
 |N(s)\cap(D_1\cup D_2)|
 \ge 7-d_{G[S]}(s)
 =1+d_{\overline{G[S]}}(s).                           \tag{9.3}
\]

Since each full shore already contributes one neighbour, a boundary
vertex of complement-degree (q) has at least (q-1) additional shore
incidences beyond this baseline.  The (C_5\dot\cup2K_1) core forces
five such extra incidences, one at each cycle vertex; the
(K_3\dot\cup2K_2) core forces three, one at each triangle vertex.

## 10. Small shores in both sharp five-edge cores

The two-vertex shore was closed by Lemma 6.1.  The next order is also
closed, by a finite attachment lemma that does not use the internal
structure of the opposite shore.

### Proposition 10.1 (three-vertex shore; finite, exhaustively certified)

Suppose

\[
 |S|=7,\qquad
 \overline{G[S]}\in
 \{C_5\dot\cup2K_1,\ K_3\dot\cup2K_2\},
\]

and (D) is a three-vertex component of (G-S), full to (S).  Let
(D') be any second connected full shore.  If every vertex of (D) has
degree at least seven in (G), then (G) has a (K_7)-minor.

#### Certificate

The connected graph (G[D]) is either a path (P_3) or contains a
spanning triangle after adding internal edges.  More precisely, among
the connected three-vertex graphs it is (P_3) or (K_3); the latter
may also stand for a supergraph of a chosen spanning path, but the script
checks the two actual isomorphism types directly.

If (G[D]=P_3), its endpoints have at least six neighbours in (S) and
its centre has at least five.  If (G[D]=K_3), every vertex has at least
five neighbours in (S).  Contract (D') to one helper complete to
(S).

The dependency-free script `c5_core_order3_shore_verify.py` enumerates,
for each of the two boundary cores,
all boundary-neighbour masks meeting these lower bounds and whose union
is all of (S).  It quotients only by genuine internal automorphisms:
endpoint reversal for (P_3) and all vertex permutations for (K_3).
It checks 995 path assignments and 3928 triangle assignments per core.
For every one it performs an exact connected-subset search for seven disjoint
pairwise adjacent branch sets and then independently replays the model's
disjointness, connectivity, and 21 pairwise adjacencies.  There are no
failures.

The enumeration is complete rather than monotonic: all neighbourhood
masks of order *at least* the degree threshold are included.  The only
contracted object is the opposite full shore, which is a legitimate
connected branch set.  Therefore every graph in the statement contains
one of the certified quotient models, proving the proposition.

### Proposition 10.2 (two-vertex shore in the second core)

The conclusion of Lemma 6.1 also holds when

\[
 \overline{G[S]}=K_3\dot\cup2K_2.
\]

Indeed, the same degree calculation says that each endpoint of the shore
edge has at least six boundary neighbours.  The dependency-free script
`c5_core_k2_shore_verify.py` enumerates all (8^2=64) choices of their
optional unique missed boundary neighbours for each of the two sharp
cores.  It finds and replays an exact (K_7)-model in every case.  For
the five-cycle core, Lemma 6.1 supplies the compact hand proof; the
second-core enumeration is the finite residual.

### Corollary 10.3

In a survivor of either sharp five-edge contact core, each of its exactly
two full shores has order either one or at least four.  Orders two and
three are excluded by Lemma 6.1, Propositions 10.1 and 10.2.

## 11. Four-vertex shores

Seven-connectivity supplies enough additional local information to close
shore order four as well.

### Lemma 11.1 (local cut inequality)

Let (G) be seven-connected, let (D) be a component of (G-S), and
let (|S|=7).  For every nonempty proper subset (X\subset D),

\[
 |N_D(X)|+|N_S(X)|\ge7.                               \tag{11.1}
\]

#### Proof

Because (D) is a component of (G-S), every neighbour of (X) lies
in (D-X) or in (S), and these two sets are disjoint.  The opposite
distinguished shore lies outside (X\cup N(X)), so (N(X)) is a vertex
cut separating a nonempty set from another nonempty set.  Therefore
seven-connectivity gives (|N(X)|\ge7), which is (11.1). \(\square\)

### Proposition 11.2 (four-vertex shore; finite, exhaustively certified)

Suppose the boundary is one of the two sharp cores in (8.1), one full
shore (D) has order four, the opposite shore is connected and full,
(delta(G)\ge7), and (11.1) holds.  Then (G) contains a
(K_7)-minor.

#### Certificate

There are six connected graphs on four vertices:

\[
 P_4, K_{1,3}, C_4, \text{the paw}, K_4-e, K_4.
\]

The script `sharp_core_order4_shore_sat.py` treats each of these six
types and both boundary cores.  Its Boolean variables are the 28
possible (D)-to-(S) edges.  It imposes:

1. every boundary vertex has a neighbour in (D);
2. every shore vertex has total degree at least seven; and
3. (11.1) for every nonempty proper subset of (D).

It contracts only the opposite connected full shore to a helper.  Z3
then proposes an attachment assignment.  A separate exact branch-set
search finds a (K_7)-model.  From that model the script extracts a
sorted set of optional edges sufficient for every bag's spanning tree
and every bag-pair adjacency.  Before adding the corresponding blocking
clause, it independently replays the same model in the graph consisting
of the fixed edges plus only this witness set.  Thus every blocked family
really contains a displayed (K_7)-model.  Exhaustion returns UNSAT in
all twelve cells.  The numbers of model-witness clauses are

\[
\begin{array}{c|rrrrrr}
 &P_4&K_{1,3}&C_4&\text{paw}&K_4-e&K_4\\ \hline
C_5\dot\cup2K_1&57&30&167&156&322&266\\
K_3\dot\cup2K_2&87&73&244&131&303&69
\end{array}
\]

and a fresh independent replay produces the same UNSAT outcomes.

### Corollary 11.3

In a survivor of either sharp five-edge contact core, each of the exactly
two full shores has order one or at least five.

## 12. Five-vertex shores

### Proposition 12.1 (five-vertex shore; finite, exhaustively certified)

Under the hypotheses of Proposition 11.2, the same conclusion holds if
the full shore (D) has order five.

#### Certificate

The dependency-free front end `sharp_core_order5_shore_sat.py` generates
all (2^{10}) labelled graphs on five vertices, retains the connected
ones, and canonically relabels them under all (5!) permutations.  It
asserts that the resulting list has exactly 21 representatives, the
known number of connected unlabeled five-vertex graphs.

For each representative and each of the two sharp boundary cores, it
configures the independently replaying CEGIS engine from Proposition
11.2 with 35 possible shore-to-boundary edges.  It imposes full
attachment, degree at least seven at all five shore vertices, and the
local cut inequality (11.1) for every nonempty proper shore subset.  The
opposite full shore is again the only contracted object.

All (21\times2=42) cells return UNSAT.  For the five-cycle core the
cells require between 43 and 690 certified model-witness clauses; for the
(K_3\dot\cup2K_2) core they require between 82 and 476.  Every clause
is checked on the fixed graph plus only its listed optional edges before
being admitted to the exhaustion, exactly as in Proposition 11.2.

### Corollary 12.2

In a survivor of either sharp five-edge contact core, each of its exactly
two full shores has order one or at least six.

## 13. Unbounded web closure of the two five-edge exceptions

The small-shore restrictions of Sections 10--12 are now superseded by
two unbounded structural theorems.

* `hadwiger_c5_full_web_closure.md` proves that, for
  (overline{G[S]}=C_5\dot\cup2K_1), a crossing in either five-terminal
  shore society gives an explicit (K_7)-model.  If both societies are
  crossless, the generalized Two Paths Theorem completes them to webs;
  seven-connectivity eliminates every inserted facial clique.  The two
  bare disk ribs glue along the five-cycle, and deleting the two
  universal boundary vertices leaves a planar graph.  The Four Color
  Theorem then gives a six-colouring.

* `hadwiger_k322_full_web_closure.md` does the same for
  (overline{G[S]}=K_3\dot\cup2K_2), equivalently
  (G[S]=K_{3,2,2}).  Its four-terminal order is (1,3,2,4), with
  crossing pairs (12,34).  A crossing has an explicit seven-bag
  model.  In the crossless case, facial cliques have at most three rib
  neighbours plus the three omitted boundary vertices, contradicting
  seven-connectivity.  Gluing the disk ribs leaves a planar graph after
  deleting an induced (K_{1,2}), so (4+2=6) colours suffice.

Combining these two hand proofs with the exact five-edge quotient
classification of Proposition 8.1 gives the strengthened conclusion:

### Theorem 13.1

In the counterexample-derived setting of Section 1, every order-seven
contact separator satisfies

\[
 \boxed{|E(\overline{G[S]})|\ge6.}                   \tag{13.1}
\]

#### Proof

Theorem 7.2 closes at most four missing edges.  With exactly five,
Proposition 8.1 says that contracting the two full shores already gives
a (K_7)-minor unless the complement is one of its two listed
exceptions.  The two web-closure theorems eliminate those exceptions
for arbitrary shores. \(\square\)

## 14. The six-edge layer

The exact atlas and web analysis in
hadwiger_six_edge_web_closures.md classifies all 54264 labelled
six-edge complements.  Twelve quotient-exception isomorphism types
occur.  Generalized-web arguments with explicit crossing models close
eight of them for shores of arbitrary order.  Consequently:

### Theorem 14.1

If an order-seven counterexample-derived contact separator has exactly
six missing edges, then, up to relabelling, its complement is

\[
C_6\dot\cup K_1,
\qquad E(C_6)=\{04,05,13,15,23,24\}.               \tag{14.1}
\]

Every other six-edge complement either has a (K_7)-minor already
after contracting the two full shores, is eliminated by an unbounded
web/planar-colouring closure, or is split and hence impossible by the
exact-block nonsplitness theorem (Corollary 4.1 of
`hadwiger_exact_block_hypergraph.md`), or is the
(2K_3\dot\cup K_1) core closed by the two-piece surgery and rooted
triangle theorem in `hadwiger_k331_two_piece_closure.md`.
