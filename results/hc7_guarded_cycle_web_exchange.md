# Guarded cyclic-shore web exchange

## Status and purpose

This note isolates a label-free, unbounded interface theorem which is
actually strong enough to give the coherent two-apex outcome required by
the `HC_7` proof spine.  It also records a sharp falsification of the
naive interval formulation

\[
   \text{four disjoint spans}\quad\hbox{or}\quad
   \text{a two-vertex transversal}.                       \tag{0.1}
\]

Thus (0.1) must not be used as the missing capacity-state theorem.  The
correct geometric package has a third outcome: a cyclic web frame (and,
on an unwrapped interval, a genuine three-span capacity state).  The web
frame is closed below.  The three-span state is the exact place at which
the proper-minor equality-state machinery is still needed.

Nothing in the main theorem mentions Moser labels or a seven-vertex
neighbourhood.

## 1. The minimal interval statement and its falsification

For a finite family `F` of nonempty closed arcs on a circle, write
`nu(F)` for the maximum number of pairwise disjoint arcs and `tau(F)`
for the minimum number of circle points meeting every arc.

### Counterexample 1 (the `C_5` span obstruction)

Let the circle be subdivided by `x_0,...,x_4` in cyclic order and take

\[
                 I_i=x_ix_{i+1}\qquad(i\in\mathbb Z_5),   \tag{1.1}
\]

where endpoints are included.  Then

\[
                         \nu({\cal F})=2,
                 \qquad \tau({\cal F})=3.                \tag{1.2}
\]

Indeed two nonincident cycle-edge arcs are disjoint, while three pairwise
disjoint cycle-edge arcs do not exist.  A transversal is exactly
a vertex cover of `C_5`, whose minimum order is three.  Hence there need
not be four disjoint spans and two actual vertices need not hit all spans.

There is an even simpler noncyclic obstruction: three pairwise disjoint
proper arcs have `nu=tau=3`.  Consequently no assumption which merely
records intervals and their intersections can improve the residual
transversal from three to two.

### Lemma 1 (the exact elementary span trichotomy)

Let `F` be a finite family of proper arcs on a circle.  At least one of
the following holds.

1. `tau(F)<=2`;
2. `F` contains three pairwise disjoint arcs;
3. some inclusion-minimal subfamily of `F` covers the circle.

If outcome 3 is absent, then `tau(F)=nu(F)` after cutting the circle at
a point outside the union.  In particular the number three in outcome 2
cannot be replaced by four.

#### Proof

If the union of the arcs is the circle, delete arcs greedily while the
union remains the circle; the remaining family is the subfamily in
outcome 3.  Otherwise choose a point outside the union and cut there.
The arcs become intervals on a line.  For intervals the greedy
right-endpoint algorithm proves the equality between the transversal
and packing numbers.  Thus, if a two-point transversal does not exist,
there are at least three pairwise disjoint intervals, hence three
pairwise disjoint original arcs. \(\square\)

The two counterexamples explain the required proof-spine division:

* a cyclic minimal cover is a web-frame input;
* three separated spans are a capacity/equality-state input; and
* a two-point transversal is the possible coherent two-apex input.

Extension-state data cannot simply be added as arbitrary colours on the
arcs to repair (0.1): permutation-closed boundary extension relations are
too flexible in the absence of the actual proper-minor transitions.  At
an actual contraction-critical adhesion the legitimate terminal rule is
instead the audited one: equal boundary partitions returned by operations
on opposite open shores splice to a six-colouring.

## 2. Guarded cyclic-shore theorem

We use the same-vertex generalized Two Paths theorem in the form already
audited in `../results/hc7_near_k7_exact7_web_closures_audit.md`:
an ordered terminal tuple with no crossing has an edge-only completion to
a web with that frame.  A web consists of a planar rib plus cliques inserted
in facial triangles; an inserted clique has no neighbours in the web
outside its facial triangle and the clique itself.

### Theorem 2 (guarded cyclic-shore web exchange)

Let `G` be seven-connected and suppose

\[
 V(G)=A\mathbin{\dot\cup}R\mathbin{\dot\cup}D_1
                         \mathbin{\dot\cup}D_2,           \tag{2.1}
\]

where

* `|A|<=3`;
* `R={r_0,...,r_{m-1}}`, with `m>=4`, and `G[R]` contains the spanning
  cycle `r_0r_1...r_{m-1}r_0`;
* `D_1,D_2` are nonempty, have no edge between them, and every `r_i`
  has a neighbour in each `D_j`; and
* each `G[D_j]` is connected.

For `j in {1,2}`, form `Q_j` from `G[D_j]` by adding distinct terminals
`t_0^j,...,t_{m-1}^j`, where `t_i^j` is adjacent in `D_j` precisely to

\[
                         N_{D_j}(r_i),                    \tag{2.2}
\]

and where

\[
             t_i^jt_k^j\in E(Q_j)
       \quad\Longleftrightarrow\quad r_ir_k\in E(G[R]).  \tag{2.2a}
\]

Give the tuple the cyclic order of the displayed spanning cycle.

Then one of the following holds.

1. One of the two ordered terminal tuples is crossed: for some four
   terminals occurring alternately there are the two corresponding
   vertex-disjoint paths in `Q_j`.
2. `G-A` is planar.  More precisely, each

   \[
                    G[D_j\cup R]                          \tag{2.3}
   \]

   has a plane embedding in a closed disk with the displayed cycle on
   its boundary, and the two disks glue on opposite sides of that cycle.

#### Proof

Assume outcome 1 does not occur.  Apply the generalized Two Paths
theorem to each `Q_j`.  It has an edge-only completion `W_j`, on the same
vertex set, to an `m`-web with the ordered terminals as its frame.  Let
`B_j` be its planar rib.

We first prove that no original vertex of `D_j` lies in a clique inserted
in a facial triangle of `B_j`.  Suppose `X` is the nonempty set of all
original vertices in one such inserted clique.  Every neighbour of `X`
represented in `Q_j` is either in that clique or is one of the at most
three vertices of its facial triangle.  Replace an artificial terminal
among those three vertices by the corresponding actual root `r_i`.
This accounts for every edge from `X` to `R`, by (2.2).  In the original
graph the only additional possible neighbours of `X` lie in `A`: there
are no edges from `D_j` to the opposite shore.  Consequently

\[
                            |N_G(X)|\le 3+|A|\le6.         \tag{2.4}
\]

The set in (2.4) separates `X` from the nonempty opposite shore.  This
contradicts seven-connectivity.  Therefore every original shore vertex,
and hence every original shore edge, lies in the planar rib.

First delete every completion edge in `W_j-Q_j` from the rib drawing.
Delete the artificial terminals and place `r_i` at the position of
`t_i^j`.  Replace every retained terminal--shore edge by the
corresponding edge from `r_i` supplied by (2.2), and every retained
terminal--terminal edge by its corresponding edge of `G[R]` supplied by
(2.2a).  This gives the disk embedding (2.3), including all chords of
the displayed frame which occur in `G[R]`.

Erase every nonframe edge of `G[R]` from the second disk (the identical
edge remains in the first disk), and put the two disks on opposite sides
of the common boundary cycle.  The shores are anticomplete, so the
drawings glue without a crossing and contain every edge of `G-A` exactly
once.  Hence `G-A` is planar. \(\square\)

### Corollary 3 (literal `HC_7` termination with three fixed rows)

In Theorem 2, suppose outcome 1 gives a rooted `K_4` subdivision whose
four branch roots in `R` each have neighbours in three further pairwise
disjoint, connected, pairwise adjacent sets `F_1,F_2,F_3`, disjoint from
the subdivision.  Then `G` has a `K_7` minor.

If outcome 1 does not occur and `G[A]` is bipartite, `G` is
six-colourable: four-colour `G-A` and colour `G[A]` with two fresh
colours.  In particular this holds whenever `|A|<=2`.

#### Proof

For the crossed outcome, the two `T`-paths are terminal-clean by the
definition of a crossing.  Replace each of their four artificial ends
and its incident terminal edge by the corresponding actual root and
portal edge (or replace a one-edge terminal path by the corresponding
actual root--root edge from (2.2a)).  Add the four arcs of the displayed
frame cycle between the alternating roots.  The interiors of the two
crossing paths contain no terminal, so they avoid every other root on
those four frame arcs.  This is a rooted subdivision of `K_4`.  Split
each subdivided edge at one edge to obtain four disjoint rooted branch
sets.  Pointwise contact at their roots makes each adjacent to each
`F_i`; the three `F_i` complete them to seven clique branch sets.  The
second assertion follows from Theorem 2 and the Four Colour Theorem.
\(\square\)

### Corollary 4 (uniform `C_m\vee K_2` full-shore closure)

Assume in addition to Theorem 2 that `A={a,b}`, `ab` is an edge, both
`a,b` are complete to `R`, and both `D_1,D_2` have a neighbour at each
of `a,b`.  Then `G` contains a `K_7` minor or is six-colourable.

#### Proof

If the tuple of `D_j` is crossed, take

\[
                         F_1=\{a\},\quad F_2=\{b\},
                  \quad F_3=D_{3-j}.                      \tag{2.5}
\]

These sets are connected, disjoint and pairwise adjacent.  Every root in
`R` contacts all three, so Corollary 3 gives a `K_7` minor.  In the
crossless case Corollary 3 gives a six-colouring. \(\square\)

Corollary 4 strictly generalizes the audited five-cycle theorem from a
five-vertex frame to an arbitrary Hamiltonian cyclic frame, with arbitrary
additional chords.

### Corollary 4.1 (cross forcing at a full actual adhesion)

Let `G` be seven-connected and non-six-colourable, and let an actual
two-shore separation have boundary `S`.  If `G[S]` contains a cycle `R`
such that every vertex of `R` has a neighbour in both open
shores and, with `A=S-R`, either `|A|<=2` or `G[A]` is bipartite and
`|A|=3`, then at least one of the two full portal tuples on `R` is
crossed.

This conclusion is independent of all edges between `A` and `R`.

#### Proof

The two open shores, `R`, and `A` satisfy Theorem 2.  If neither tuple
were crossed, `G-A` would be planar.  The stated hypothesis on `A` would
then six-colour `G` as in Corollary 3. \(\square\)

Thus an induced `C_5` in an exact seven-boundary already forces a literal
same-shore cross without requiring that the two omitted vertices be
universal.  What universality supplied in the old sharp `C_5` theorem was
only the final three-row lift of that cross.  The audited distributed-row
theorem is exactly the replacement needed when those two row contacts are
not pointwise.

### Corollary 4.2 (structural cross forcing on seven vertices)

Let `|S|=7` in Corollary 4.1 and suppose both open shores are full to
`S`.  If `G[S]` is nonchordal, then at least one of the following holds.

1. One shore has a crossed portal tuple on a cycle of `G[S]`.
2. Every induced cycle of `G[S]` has order four and the three vertices
   outside each such cycle induce a triangle.

Thus, in the absence of a literal same-shore cross, the actual boundary
is either chordal or has the structural shape “induced four-cycle with a
complementary triangle”; no labelled graph enumeration is used.

#### Proof

A nonchordal graph has an induced cycle `C` of order at least four.  If
`|C|>=5`, at most two boundary vertices lie outside it, so Corollary 4.1
forces a crossing.  If `|C|=4`, exactly three vertices lie outside it.
A graph on three vertices is nonbipartite exactly when it is a triangle.
Hence Corollary 4.1 again forces a crossing unless the complementary
three vertices induce a triangle.  Apply the same argument to every
induced cycle. \(\square\)

## 3. Exact applicability boundary

Theorem 2 closes an entire infinite family, rather than a finite labelled
cell: every two-shore actual adhesion with at most three omitted vertices
and one full spanning cyclic frame has a crossed carrier or one planar
remainder.  If at most two vertices are omitted, this is the required
structural alternative

\[
        \text{crossed rooted carrier}\quad\hbox{or}\quad
        \text{one fixed coherent two-apex pair}.          \tag{3.1}
\]

With three omitted vertices the planar remainder is not literally a
two-apex certificate, but a bipartite omitted graph still gives the
terminal six-colouring in Corollary 3.

It also identifies, without hiding it, what remains at the general
trichotomy adhesion.

1. A crossed tuple still needs three labelled fixed rows.  Pointwise
   contacts invoke Corollary 3; distributed contacts must be lifted by
   `../results/hc7_port_distributed_row_exchange.md`.
2. If more than two actual boundary vertices lie outside the cyclic
   frame, (2.4) no longer returns the desired common two-apex pair, and
   seven-connectivity only kills an inserted triangle when the external
   guard has order at most three.
3. If the span family unwraps and has packing number three, Lemma 1 gives
   neither four sectors nor a two-vertex transversal.  Static geometry is
   exhausted there.  A proof must use an internal deletion/contraction on
   one shore and force the *same actual-boundary equality partition* from
   the opposite shore.  The audited dynamic locked-gate theorem then
   splices the two proper-minor colourings.

Thus the remaining state problem is not “prove (0.1)”.  It is the much
sharper statement:

> **Three-span state target.**  At an actual contraction-critical
> adhesion, three separated capacity spans which admit neither a labelled
> distributed-row lift nor a cyclic web frame force equal boundary
> partitions from operations on the two open shores.

This target genuinely uses contraction-criticality and cannot be replaced
by arbitrary boundary extension data.  Proving it would attach the
state branch to the geometric theorem above and complete the desired
capacity-state web exchange.

## 4. A terminating state mechanism for separated spans

The following lemma gives a concrete way for span geometry to force the
same equality partition.  Unlike an abstract appeal to “criticality”, it
constructs two proper minors and checks the labelled partition literally.
It is uniform in the number of colours.

### Theorem 5 (opposite partition-carrier splice)

Let `q>=2`, and let `G` be proper-minor-minimal non-`q`-colourable.  Let

\[
 V(G)=S\mathbin{\dot\cup}D_1\mathbin{\dot\cup}D_2,        \tag{4.1}
\]

where `D_1,D_2` are nonempty and anticomplete.  Let

\[
                         \Pi=(P_1,\ldots,P_q)             \tag{4.2}
\]

be a partition of `S` into `q` nonempty independent sets.

Suppose that, for each `j in {1,2}`, there are an index set
`I_j subseteq {1,...,q}` and pairwise disjoint connected nonempty sets

\[
                         X_i^j\subseteq D_j\quad(i\in I_j) \tag{4.3}
\]

such that

1. `X_i^j union P_i` is connected for every `i in I_j`;
2. `P_i` is a singleton for every `i notin I_j`; and
3. the following `q` sets are pairwise adjacent:

   \[
       B_i^j=
       \begin{cases}
          X_i^j\cup P_i,&i\in I_j,\\
          P_i,&i\notin I_j.
       \end{cases}                                      \tag{4.4}
   \]

Then `G` is `q`-colourable, a contradiction.

#### Proof

Fix `j`.  Contract every connected set `B_i^j` with `i in I_j` to one
vertex and delete all unused vertices of `D_j`.  Call the resulting
minor `M_j`.  It is a proper minor: every `B_i^j` with `i in I_j`
contains the nonempty shore set `X_i^j` and the nonempty boundary block
`P_i`, so if `I_j` is nonempty its contraction performs an actual edge
contraction.  If `I_j` is empty, deleting the nonempty set `D_j` already
makes `M_j` a proper minor.

The images of the `q` sets in (4.4) form a literal `K_q` in `M_j`.
Hence every `q`-colouring of `M_j` gives them `q` distinct colours.
Expand only the boundary labels: give every member of `P_i` the colour
of the image of `B_i^j`.  This is proper on the whole unchanged opposite
closed side `G[S\cup D_{3-j}]`.  Indeed each `P_i` is independent, and
every retained edge from `P_i` to `S\cup D_{3-j}` became incident with
the contracted image in `M_j`.  Its labelled equality partition on `S`
is therefore exactly `Pi`.

Minor-minimality gives a `q`-colouring of each `M_j`.  Use the colouring
coming from `M_1` on `G[S\cup D_2]` and the colouring coming from `M_2`
on `G[S\cup D_1]`.  Both induce the same labelled partition `Pi` on
`S`; permute the `q` colours on one side so that they agree vertex by
vertex on `S`, and glue.  This is a `q`-colouring of `G`, contrary to the
hypothesis. \(\square\)

### Corollary 6 (the literal three-span six-colour state)

In Theorem 5 take `q=6` and

\[
            \Pi=(P_1,P_2,P_3,\{s_4\},\{s_5\},\{s_6\}).  \tag{4.5}
\]

If each open shore contains three disjoint connected span packets
`X_1^j,X_2^j,X_3^j` such that the six augmented sets

\[
 X_1^j\cup P_1, X_2^j\cup P_2, X_3^j\cup P_3,
 \{s_4\},\{s_5\},\{s_6\}                               \tag{4.6}
\]

are connected and pairwise adjacent, then the two shores force the same actual-boundary
six-block partition and `G` is six-colourable.

This is the promised use of contraction-critical states in the
three-separated-span branch.  The remaining applicability question is
now geometric and label-preserving, not a vague state conjecture:
do the three separated capacity spans at the trichotomy adhesion augment
the same three independent boundary blocks on both shores so that (4.6)
is a clique model?  If yes, Corollary 6 terminates immediately; if not,
the first failed adjacency is an actual labelled repair duty for the
distributed-row theorem or an actual low-order portal separation for the
rural torso tree.
