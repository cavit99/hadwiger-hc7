# Independent audit: block-terminal Two-Paths certificate

Audited file: `results/hc7_exact7_block_terminal_web.md`.

## Superseding verdict

**GREEN after two local proof repairs and one explicit upfront convention.**
All three repairs listed below are now present in the source.

1. Throughout the carrier argument—not only when Corollary 4.1 is
   reached—`K` must mean the induced carrier `G[V(K)]`.  Otherwise
   `N_K(C)=Delta` does not exclude an omitted host edge from `C` to another
   vertex of the same branch set.  This convention must be imposed before
   the universal captured-path property is invoked: adding carrier edges
   only at the end is not formally harmless, because it can create new
   nonseparating paths.
2. The proof that `Q\cup P^circ` lies on the rib has a small circular
   far-side sentence.  When proving that a chosen `q` is a rib vertex, it
   cannot yet assume that the vertices of `P^circ` are rib vertices.  The
   two-case repair in Section 3 below proves the needed far side directly.
3. The connected-pair implication is correct, and the source now includes
   its connected-partition proof rather than relying on an unstable note.

The induced convention is legitimate when made at the start.  Replacing a
chosen carrier subgraph by the host graph induced on the same branch-set
vertices preserves its trace, connectivity, and every cross-block edge.
If an added internal edge creates a labelled peel, that peel is already a
valid host-graph outcome; otherwise the hard-branch and capture arguments
may be run on the induced carrier itself.  What is unsafe is silently
changing the carrier only after its captured-path property has been fixed.

Also, “full three-gate” means exactly

\[
                         N_K(C)=V(\Delta).
\]

It does not mean that every vertex of `C` is adjacent to every gate vertex,
and the three edges of the facial triangle in the web completion need not
be literal edges of `K`.  What is literal is the set of three carrier
vertices and at least one actual `C`--gate edge to each of them.

With these repairs, no counterexample or further missing implication was
found.

## 1. Artificial terminals

The equivalence in Theorem 2.1 is exact.  An `alpha-beta` path has only
`alpha,beta` outside `J`; deleting those endpoints leaves a path in `J`
from some `q in Q` to some `p in P`.  If necessary, trim at the first
`Q`-vertex and last `P`-vertex.  Vertex-disjointness from an `x-y` path is
unchanged.  Conversely, adjoining the two terminal edges to a disjoint
`q-p` path gives an `alpha-beta` path disjoint from the same `x-y` path.
The assumptions that `Q,P` are disjoint and avoid `x,y` make the four
frame terminals distinct.

The generalized Two Paths input is used in its audited exact scope.
Humeau--Pous, Theorem 1.5, says that a crossless ordered tuple has a
same-vertex edge-completion to a web with that frame.  This is the same
form independently checked in
`results/hc7_guarded_cycle_web_exchange_audit.md` and
`results/hc7_near_k7_exact7_web_closures_audit.md`.  It adds edges but no
vertices.  No completion edge is used later as an edge of the host.

Thus the two alternatives are mutually exclusive and exhaustive: a web
frame is crossless, while a crossless tuple has the stated completion.

## 2. Absence of the set-terminal cross

For every `q in Q` and `p in P^circ`, an `xy|qp` linkage in `K` is
equivalent, by the audited connected-pair lemma, to a nonseparating
`x-y` path avoiding `q,p`.  The universal capture property for `q`
requires every such path to contain all of `P`, contradicting omission of
the particular member `p`.  Hence no set-terminal cross exists and the
single augmented web certificate follows.

This step uses actual carrier paths only.  It does not combine separately
chosen pairwise web completions.

For a self-contained inclusion of the cited implication, contract the two
disjoint linkage paths, extend the two contracted vertices to a partition
of `V(K)` into two connected sets by deleting an edge on their path in a
spanning tree, and apply the relative nonseparating-path lemma to the side
containing `x,y`.  This returns a nonseparating `x-y` path disjoint from
the connected side containing `q,p`.  These are exactly the hypotheses of
Lemma 2.2; no planarity or extra linkage assumption is involved.

## 3. Why every marked terminal is a rib vertex

The frame vertices `x,alpha,y,beta` lie in the planar rib by the definition
of a web.  A vertex outside the rib belongs to a clique cell behind one
facial rib triangle, and every edge from that cell to the rib ends on that
triangle.

Suppose `z in Q` were in a cell behind `Delta`.  The literal edge
`alpha-z` of `K^+` forces `alpha in V(Delta)`.  For the component `C` of
the actual `K`-vertices of that cell containing `z`, every actual
`K`-neighbour lies in

\[
                         V(\Delta)-\{\alpha\},
\]

a set of order at most two.  The far side must be justified without
assuming the conclusion.  If at least one of `x,y` is outside `Delta`,
that frame root is a carrier vertex outside `C union N_K(C)`.  Otherwise
`Delta={alpha,x,y}`.  Then `beta notin Delta`, so no
`p in P^circ` can lie in this clique cell: its literal edge `beta-p`
would force `beta in Delta` by the web incidence rule.  Any such `p`
therefore lies outside `C union N_K(C)`.  In both cases the at-most-two
set separates two nonempty carrier sides, contradicting
three-connectivity.  Interchanging `(alpha,Q)` with `(beta,P^circ)` proves
the assertion for `P^circ`.

This reasoning also proves item 2.  Once item 1 is known, any cell
containing an actual carrier vertex has many marked rib vertices on its far
side.  If its facial triangle used `alpha` or `beta`, its actual carrier
neighbourhood would again have order at most two.

## 4. Literal full three-gate

For a remaining cell component `C`, item 2 ensures that all three vertices
of `Delta` are literal vertices of `K`.  The web incidence rule gives

\[
                         N_K(C)\subseteq V(\Delta).
\]

At least one of the six distinct rib vertices in `Q union P^circ` lies
outside `V(Delta)`, and none lies in `C`.  Hence this neighbourhood
separates two nonempty sides.  Three-connectivity makes its order at least
three, so equality follows.  This proves three distinct actual gate
contacts.  It does not assert that the gate is a clique in `K`; some or all
of its triangle edges may have been added by the web completion.

If no cell contains an actual carrier vertex, every vertex and every edge
of `K` lies in the planar rib, so item 4 is also exact.

## 5. Four-connected common face

If `K` is four-connected, the literal equality
`N_K(C)=V(Delta)` forbids every nonempty cell.  Thus `K` is planar.

For each `q,p`, apply the same-vertex theorem to the crossless tuple
`(x,q,y,p)`.  Four-connectivity again removes every nonempty clique cell,
so deleting the added planar-rib edges leaves the four literal terminals
cofacial in a plane embedding of `K`.  Three-connectivity gives Whitney
uniqueness.  Fixing `q_0,p_0`, the face for `(x,q_0,y,p)` shares the three
vertices `x,q_0,y` with the base face and hence is the same face; in a
three-connected plane graph two distinct facial cycles cannot share three
vertices.  Varying `q` with `p_0` gives the same conclusion for `Q`.
The alternating orders put `Q` and `P^circ` on opposite open `x-y` arcs.

An exhaustive graph-atlas falsification pass checked 16,110 assignments in
four-connected graphs of order at most seven.  None satisfied the full
no-cross hypothesis for two terminals in each block, so the pass was
vacuous rather than confirmatory; it found no counterexample.

## 6. Ambient external contacts

Under the upfront convention `K=G[V(K)]`, item 3 gives exactly three
neighbours of `C` inside the carrier.  The component `C` contains no trace root: its
cell is disjoint from the rib containing `x,y,Q,P^circ`.  Since the pair
carrier has exact trace `{x,y}`, `C` consists of present-open-shore
vertices.  The host has a nonempty far side (in particular `v`), so
seven-connectivity gives

\[
 |N_G(C)|\ge7,
 \qquad
 |N_G(C)-V(K)|=|N_G(C)|-3\ge4.
\]

If `C` had an edge to `L`, its carrier endpoint would belong to
`P=N(L)\cap K`.  Its nonroot members are `P^circ`, and its possible root
members are `x,y`; all are rib vertices, contrary to `C` lying in a cell.
Likewise item 1 places all selected portals `Q` on the rib.  The last two
claims of Corollary 4.1 are therefore literal.

The bound proves four **distinct outside neighbour vertices**.  It does not
by itself supply four mutually disjoint external paths or assign those
contacts to four different named blocks.

The induced convention is genuinely necessary for this deduction.  If a
carrier is represented only by a chosen connected spanning subgraph, one
may add in the host an omitted edge from a cell vertex to a carrier vertex
outside `Delta`.  The abstract equality `N_K(C)=Delta` in the chosen
subgraph then coexists with an additional host neighbour still lying in
`V(K)`, and subtracting three from `|N_G(C)|` no longer counts outside
contacts.  This is a local counterexample to the inference, even though it
is not an HC7 counterexample.  Defining every carrier induced from the
outset removes it.

## 7. Web and 3-sum falsification checks

A genuine web cell is not a counterexample to item 3.  Glue a nonempty
clique cell behind a facial triangle `Delta` of a four-rib.  After the two
artificial frame terminals are removed, any three-connected induced
carrier component inside the cell must have an actual neighbour at every
vertex of `Delta`; missing one gate would leave a separator of order at
most two.  Thus the construction realizes exactly
`N_K(C)=V(Delta)` and shows that the three-gate residue is sharp.

Likewise a triangle 3-sum can retain an arbitrarily complicated piece
behind `Delta`, but it cannot falsify the equality: the web incidence rule
gives containment in `Delta`, and three-connectivity forces all three
literal contacts.  If the common triangle contains `alpha` or `beta`, only
two literal carrier gate vertices remain and the same construction is not
three-connected; this is precisely why item 2 is valid.

## 8. Lexicographic cell evacuation

Lemma 5.1 and Theorem 5.2 are **GREEN** under the inherited Section 3
setting now stated explicitly in the source.  Let `D` be one carrier
component in a web cell behind `Delta`.  The equality
`N_K(D)=V(Delta)` makes `D` a component of `K-V(Delta)`.  Another
component contains marked rib vertices outside the gate.  Three-
connectivity makes every component full to the three gate vertices, so
`K-D` is connected even though it need not remain three-connected.

The four reallocations according as `D` sees `W` and/or a target block are
literal.  A cell seeing neither is discarded.  A cell seeing only `W` is
absorbed into `W`; one seeing only a target is absorbed into that target;
one seeing both is absorbed into `W`, thereby retaining and possibly
increasing target contact.  The actual `D-Delta` edges keep an enlarged
`W` adjacent to `K-D`.  When `W` is not enlarged, its carrier contact
survives through the fixed set
`P^circ\subseteq N_G(L)\cap V(K)`, all of which lies on the rib and hence
outside `D`.  Exact trace adjacencies preserve all three core-block
adjacencies.  No cell contains an adhesion vertex, so no trace changes.

Admissibility depends only on `w` and those fixed traces.  Thus the
admissible rank, then raw rank, never decreases, while `|K|` strictly
decreases.  Corollary 4.1 gives `E(D,L)=\varnothing`, so the fixed region
`L` and the threshold `|N_G(L)\cap V(K)|\ge5` are unchanged.  A carrier
chosen by rank-first, size-last optimization therefore has no nonempty web
cell whenever it is three-connected.  Its entire block-terminal residue is
the planar rib.  This optimization is over all connected supported
realizations; the smaller competitor need not remain three-connected.

## Trust boundary

The theorem genuinely replaces a drifting family of pairwise webs by one
block-terminal web, and lexicographic cell evacuation removes every
nonplanar cell from a three-connected optimized carrier.  The surviving
carrier is a literal planar/rural page.  This audit does not turn that page
into a common colouring state or a fixed two-apex certificate; the
bilateral rural endgame remains open.
