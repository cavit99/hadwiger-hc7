# Independent audit: guarded cyclic-shore web exchange

## Verdict

**GREEN.**  The two Hamiltonian-frame precision edits in Section 7 and
the five earlier local repairs in Section 6 have all been applied and
rechecked.  The main web
exchange theorem, its crossing-to-`K_4` lift, the `C_m\vee K_2`
corollary, and the opposite partition-carrier splice are correct.  The
repairs do not change any theorem-strength conclusion.  One repair is a
missing connectedness hypothesis in Corollary 6; the other four make
implicit or misleading steps literal.

The external theorem is used within its exact scope.  Humeau--Pous,
Theorem 1.5, applies to a tuple of any length `m>=3`: a crossless tuple
has a same-vertex edge-completion to an `m`-web with that tuple as its
frame.  Their definition of a crossing uses two vertex-disjoint
`T`-paths, so their interiors avoid every terminal of `T`.  Their
definition of a web also says that a clique inserted in a facial
triangle has no neighbours outside that clique and the three rib
vertices.  Thus the note may use it for every `m>=4` exactly as stated.

## 1. The span statement

Lemma 1 is correct.  If the arcs do not cover the circle, cutting at a
point outside their union gives an interval hypergraph, for which the
packing and point-transversal numbers agree by the standard greedy
right-endpoint proof.  If the arcs cover the circle, a finite
inclusion-minimal covering subfamily exists.

For the five closed arcs `I_i=x_ix_{i+1}`, setwise disjointness gives
the matching number of `C_5`, namely two, and a point transversal has
minimum order three.  An interior hitting point can be moved to an
endpoint of its arc without losing that arc, so the optimum is the
vertex-cover number of `C_5`.  The parenthetical about replacing every
endpoint by a private interval should be deleted: it is unnecessary,
and a literal private replacement can destroy the stated intersection
pattern.  The closed-arc construction itself is already exact.

## 2. Web completion and inserted-clique cut

For each shore, `Q_j` is a legitimate input to the generalized Two
Paths theorem.  Its terminals are pairwise distinct, `m>=4`, and its
crossless completion changes only the edge set.  Independence of the
terminals is not an hypothesis of Humeau--Pous Definition 1.4 or
Theorem 1.5.  Thus copying every edge of `G[R]` between the corresponding
terminals is permitted.

Let `X` be the original shore vertices in one inserted facial clique.
Every frame terminal is a rib vertex, so no artificial terminal lies in
the inserted clique; hence `X` is in fact the entire inserted clique.
Every `Q_j`-neighbour of `X` outside `X` is one of the at most three rib
vertices of the facial triangle.  If such a vertex is `t_i^j`, replacing
it by `r_i` accounts for every original `X`--`r_i` edge, because
`t_i^j` was joined precisely to `N_{D_j}(r_i)`.  The only other possible
neighbours are in `A`, since the shores are anticomplete.  Therefore

\[
                    |N_G(X)|\le 3+|A|\le 6.
\]

This set separates nonempty `X` from the nonempty opposite shore, in
contradiction with seven-connectivity.  Thus every original shore vertex
is a rib vertex.  Since a web has no edges between rib vertices other
than rib edges and `Q_j` is an edge-subgraph of its completion, every
original shore edge and every original shore--terminal edge lies in the
planar rib.  This justifies the sentence at line 167.

## 3. Terminal replacement and gluing

The strengthened terminal-to-root replacement is valid after first discarding every
completion edge that was not already in `Q_j`.  This deletion is
essential: an edge-only completion may add new terminal--shore edges,
which need not correspond to edges of `G`.  Frame terminals lie on the
outer `m`-cycle of the rib.  Replacing `t_i^j` by `r_i` then changes every
retained original edge `t_i^jx` into the existing edge `r_ix`, and the
copied terminal edge `t_i^jt_k^j` into the actual edge `r_ir_k`.
Consequently every edge of `G[R]`, including every chord of the displayed
Hamiltonian cycle, lies in the disk drawing of each closed shore.

When the two disk drawings are put on opposite sides, a nonframe edge of
`G[R]` appears once in each disk.  This is harmless but should be said
precisely: erase its copy from one disk, or regard the union as a planar
multigraph and delete one of the two parallel copies.  The remaining
drawing contains every edge of `G-A` exactly once.  The shores are
anticomplete, so there is no other gluing issue.

The bound `|A|<=3` is exact for this proof: it makes the inserted-clique
cut have order at most six.  It gives a coherent two-apex conclusion
only when `|A|<=2`; for three guards the later bipartite-`G[A]`
six-colouring statement is the correct weaker conclusion.

## 4. Crossing and the fixed rows

A crossing consists, by definition, of two disjoint `T`-paths whose
interiors avoid all terminals.  A crossing path which is a single
terminal--terminal edge copies an actual root--root edge.  Every longer
crossing path starts and ends with terminal--shore edges and otherwise
lies in the shore: if it used another terminal, that terminal would be
an illegal internal `T`-vertex.  Replace its ends by the actual roots and
portal edges.  The four arcs of the displayed Hamiltonian cycle between
the alternating selected roots may contain unselected roots internally;
this is allowed in a subdivision, and the two crossing paths avoid all
of them.  Hence the union is a literal rooted subdivision of `K_4`.

To obtain rooted branch sets, choose one edge on each of the six
subdivided root-to-root paths, delete those six chosen edges, and assign
the component containing each root to that root.  These four connected
sets are disjoint and are pairwise adjacent across the chosen edges.
This is the precise version of “split each subdivided edge at one edge.”
If each root contacts each of three disjoint connected pairwise adjacent
sets `F_1,F_2,F_3`, those three sets and the four rooted branch sets are
a `K_7` model.

In Corollary 4, `{a}`, `{b}`, and `D_{3-j}` meet all these hypotheses:
`ab` supplies the first adjacency, fullness at `a,b` supplies the other
two, and the opposite shore meets every root.  In the crossless case,
four colours on `G-A` and two fresh colours on the bipartite graph
`G[A]` give a proper six-colouring.  Thus the arbitrary-`m`
Hamiltonian-frame join-`K_2` closure is correct and genuinely extends
the audited five-cycle closure.  Chords in the frame do not harm either
branch of the argument.

## 5. Opposite partition-carrier splice

Theorem 5 is correct.  For fixed `j`, the sets `B_i^j` are disjoint and
connected.  Simultaneously contracting those indexed by `I_j` and
deleting the unused vertices of `D_j` is a minor operation.  It is
proper if `I_j` is nonempty because a contracted set contains both a
nonempty boundary block and a nonempty shore set; if `I_j` is empty,
deleting the nonempty shore is already proper.

The `q` images form a literal `K_q`, so a `q`-colouring assigns them all
different colours.  On expanding only the boundary labels, every
retained edge from `P_i` to `S\cup D_{3-j}` is represented by an edge
from the corresponding image in the minor.  Independence of each
`P_i` handles edges within a block.  Hence this expansion properly
colours the unchanged opposite closed side and induces exactly the
partition `Pi`, not merely a coarsening.  The minor formed from `D_1`
colours the side containing `D_2`, and conversely.  A global permutation
of one side's `q` colours aligns the blocks vertex by vertex; shore
anticompleteness then makes the glued colouring proper.

## 6. Repairs applied and verified

1. **Delete lines 45--47's private-terminal parenthetical.**  Replace
   the sentence by: “Two nonincident cycle edges are disjoint, while
   three pairwise disjoint cycle edges do not exist.”
2. **Discard completion edges before terminal replacement.**  At lines
   169--171, first delete every rib edge not belonging to the original
   `Q_j`; then replace each retained original terminal edge by the
   corresponding root edge.  “Every terminal edge” is too broad because
   the web completion may have added terminal--shore edges absent from
   `G`.
3. **Make the artificial-end lift explicit in Corollary 3.**  Before
   adding the four frame arcs, say that the two `T`-paths are terminal
   clean by the definition of a crossing and replace each terminal end
   by its actual root and portal edge.
4. **Correct lines 321--324.**  “Here one must exist” is not implied.
   Say instead: “If `I_j` is nonempty, an actual contraction makes the
   minor proper; if `I_j` is empty, deleting the nonempty `D_j` makes it
   proper.”  At lines 331--332 restrict “every original edge” to every
   retained edge with its other end in `S\cup D_{3-j}`.
5. **Add connectedness to Corollary 6.**  The statement must require
   each augmented set `X_i^j\cup P_i` to be connected, in addition to
   the six sets being pairwise adjacent.  Connectedness of `X_i^j`
   alone does not ensure this when `P_i` has more than one vertex.

All five changes now appear in the source note.  The repaired note is
ready for promotion as an audited result.

## 7. Strengthened Hamiltonian-frame formulation

The strengthening from an induced cycle to a spanning cycle in `G[R]`
is valid.  The two final precision edits have been applied:

1. The gluing paragraph explicitly deletes the duplicate copy of each
   chord of `G[R]` from the second disk.
2. The conclusion after Corollary 4 now says “arbitrary Hamiltonian
   cyclic frame, with arbitrary additional chords,” rather than
   “induced cyclic frame.”  Under the strengthened hypotheses
   `G[A\cup R]` need not be literally `C_m\vee K_2`; the corollary's
   traditional title names its principal special case.

The strengthened note is ready for promotion.
