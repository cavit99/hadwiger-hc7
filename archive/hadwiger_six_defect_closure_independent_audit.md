# Independent audit: exact-six-defect package

## Verdict

**RED FOR THE CLAIMED COMPLETE CLOSURE; GREEN THROUGH THE
\(C_6\dot\cup K_1\) SPQR RESIDUE.**

The quotient atlas, eight crossing/web closures, split exclusions, and
the \(2K_3\dot\cup K_1\) hand closure survive. The proposed final
\(C_6\dot\cup K_1\) proof has a fatal gap: one cofacial crossless
four-terminal web does not remain portal-cofacial after reflecting an
SPQR leaf. Therefore the block-reversal argument cannot force portal
rank at most one on one side of every leaf edge.

Consequently the package does **not** prove

\[
                         |E(\overline{G[S]})|\ge7.
\]

The exact safe conclusion is:

> In a minor-minimal \(HC_7\) counterexample, an exact seven-cut with
> six boundary defects has exactly two full shores and
> \[
>                   \overline{G[S]}=C_6\dot\cup K_1.
> \]
> Its high-owner shore is not three-connected and cannot have an
> already-present cycle-type SPQR leaf. The unresolved case is a
> nontrivial SPQR tree with non-cycle leaves and an unsynchronised
> rank-two/rank-two portal-face transition.

## 1. Exact quotient layer: computer assisted

The program contact_order7_six_edge_atlas.py was rerun. It checked all

\[
                         \binom{21}{6}=54264
\]

labelled six-edge missing graphs. Exactly 11,697 labelled instances,
forming twelve isomorphism types, have no \(K_7\) model after adjoining
two nonadjacent helpers complete to the boundary.

Adding a third full helper makes all twelve types \(K_7\)-positive; this
was checked with the complete 5,880-partition search from
exact7_multicomponent_quotient_atlas.py. Hence a six-defect survivor has
exactly two shores.

## 2. Eight crossing/web types

Types \(0,1,4,5,6,7,8,9\) are correctly closed by the web-template
lemma:

* a crossing has an explicit labelled \(K_7\) quotient;
* if both societies are crossless, Humeau--Pous Theorem 1.5 gives
  same-vertex web completions;
* seven-connectivity eliminates every facial inserted clique; and
* the two bare ribs glue, leaving a planar part and a bipartite omitted
  boundary, hence a six-colouring.

The finite crossing models were replayed by
six_edge_web_template_search.py. The external dependency is exactly
Humeau--Pous, *On the Two Paths Theorem and the Two Disjoint Paths
Problem*, arXiv:2505.16431, Theorem 1.5.

## 3. The \(2K_3\dot\cup K_1\) type

The hand closure in hadwiger_k331_two_piece_closure.md is sound under
the stated counterexample-derived criticality hypothesis.

The two-piece surgery forces every connected bipartition to have one
triangle-limited contact side. This makes each shore four-connected and
each vertex row triangle-limited. Fullness then gives three distinct
portal vertices for either independent boundary triple. A two-connected
graph has a rooted \(K_3\) model at any prescribed three vertices.
Opposite rooted triangles in the two shores, together with the universal
boundary vertex, give \(K_7\).

The program k331_two_piece_contact_atlas.py is independent confirmation:
it checks all \(3^7=2187\) contact pairs and returns exactly the eighteen
maximal triangle-limited negative rows. The finite atlas is not needed
for the hand surgery itself.

## 4. Split types

Types 10 and 11 are excluded by the exact-block nonsplit theorem. This
step uses proper-minor six-colourability and is not a static
\(K_7\)-minor argument.

The only remaining type is therefore \(C_6\dot\cup K_1\).

## 5. What survives in the \(C_6\) package

Subject to the external web theorem and the archived finite
certificates, the following restricted conclusions remain valid.

1. Every relaxed frame has a unique shore owner; opposite frames have
   the same owner.
2. Alternating three-linkages and the specified nonidentity linkages
   have explicit positive \(K_7\) quotients.
3. Hall failure reduces the high-owner shore to orders four or five,
   which the exact C++ searches eliminate.
4. If the high-owner shore is three-connected, Whitney uniqueness
   synchronizes the three web embeddings. The face trichotomy and the
   degenerate circular-occurrence UNSAT certificate then eliminate it.
5. If a cycle-type S-node leaf is already present, Dirac reduces it to
   a singleton ear. The one-ear atlas, seven-fan, and bare-web
   \(K_{3,3}\) argument eliminate that leaf.

The finite computations all reran:

* zero actual order-four/order-five survivors;
* all twelve circular systems and sixteen collapse patterns UNSAT;
* 762 negative adjacent-piece rows and 28 maximal rows;
* the 64-state one-ear frontier and its five maximal negative rows; and
* the displayed subdivided \(K_{3,3}\).

## 6. Fatal SPQR step

The failed inference in hadwiger_circular_obstruction_frame_theorem.md
and hadwiger_c6_core_closure.md is

\[
 \text{one crossless cofacial four-web}
 \Longrightarrow
 \text{one side of every SPQR leaf has portal rank at most one}.
                                                               \tag{A.1}
\]

Reflecting a two-sum side changes which pole-incident faces are paired.
The four portal classes need not remain on one face after the
reflection. Crosslessness constrains their cyclic order only when they
are cofacial.

The explicit counterexample in c6_rank_four_leaf_counterexample.py is a
planar two-sum of two three-connected wheel-like torsos along
\(\{p,q\}\). Four singleton portal classes occur alternately on one
facial cycle and have no prescribed two-linkage, yet the two SPQR
interiors both have portal rank two. The graph has no degree-two
vertices, so the degree-two lock is vacuous. Its verifier prints:

\[
\begin{array}{c|c}
\text{torso connectivities}&(3,3)\\
\text{prescribed disjoint linkage}&\text{false}\\
\text{portal ranks}&(2,2).
\end{array}
\]

This is not an \(HC_7\) counterexample; it directly falsifies the local
four-terminal lemma used in the closure. The additional high-owner web
states might eliminate it, but no simultaneous-face synchronization
proof is currently supplied.

## 7. Exact remaining theorem

The explicit eight-vertex counterexample to (A.1) is itself eliminated
once all six portal states are imposed simultaneously.  The exact
verifier `c6_two_r_torso_simultaneous_state_verify.py` proves:

> On the minimal two-(R)-torso host, if the six portal classes have an
> SDR and all three antipodal demand pairs are crossless, then at most
> one opposite frame pair can be present.

All three choices of two owned opposite pairs are UNSAT.  The statement
is sharp on that host: deleting the SDR, any one antipodal exclusion, or
any one of the four normalized owned-frame requirements makes the
formula SAT.  Thus the single-web proof is false, but the smallest
rank-two/rank-two obstruction is killed by the full simultaneous packet.

To finish the six-defect layer one needs:

> **Simultaneous-web SPQR exchange.** At a rank-two/rank-two leaf
> transition, the three crossless antipodal web states either synchronize
> a common portal face, give one of the positive crossing quotients, or
> expose a smaller exact seven-adhesion/state-gluable separation.

Until that theorem is proved, the six-defect threshold remains open.
