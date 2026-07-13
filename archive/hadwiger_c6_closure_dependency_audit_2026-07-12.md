# Dependency audit of the proposed \(C_6\dot\cup K_1\) closure

> **Superseded verdict.** A later independent spot-check found a fatal
> gap in the orientation-free SPQR rank step. Cofaciality of four portal
> classes in one web embedding need not survive a leaf reflection.
> See `hadwiger_c6_closure_spotcheck_counteraudit.md` and
> `c6_rank_four_leaf_counterexample.py`. The full closure claimed
> below must not be cited.

## 1. Verdict

The local closure is logically supportable in the exact two-full-shore
equality cell, subject to the quoted generalized Two Paths/web theorem and
the archived finite certificates.  I did not find a surviving conditional
"lock" among the seven dependencies in
`hadwiger_c6_full_closure_audit.md`.

There is, however, a necessary statement repair.  Theorem 1.1 of
`hadwiger_c6_core_closure.md` lists seven-connectivity, minimum degree seven,
and the frame-crossing consequences, but its proof also uses Dirac's local
inequality

\[
  \alpha(G[N(x)])\le d_G(x)-5.                 \tag{1.1}
\]

Minimum degree seven does not imply (1.1).  In the intended application this
is not an open gap: (1.1) is a standard consequence of
seven-contraction-criticality.  It must nevertheless be stated explicitly
(or the theorem must assume that \(G\) is seven-contraction-critical).

The phrase "equivalently, the sole six-edge boundary type is eliminated" is
therefore safe only inside the counterexample-derived equality cell, not for
arbitrary seven-connected minimum-degree-seven graphs.

## 2. Exact safe theorem

The proof package establishes the following computer-assisted local theorem.

> **Two-full-shore \(C_6\dot\cup K_1\) theorem.**  Let \(G\) be a finite
> simple graph such that:
>
> 1. \(G\) is \(K_7\)-minor-free and not six-colourable;
> 2. \(G\) is seven-connected;
> 3. \(\alpha(G[N(x)])\le d_G(x)-5\) for every \(x\in V(G)\) (it is enough
>    to assume this for the degree-seven shore vertices used in the proof);
> 4. \(S=\{c_0,\ldots,c_5,z\}\) and
>    \(\overline{G[S]}=C_6\dot\cup K_1\), with \(z\) the isolated vertex of
>    the complement; and
> 5. \(G-S\) has exactly two connected components \(D_1,D_2\), with
>    \(N_G(D_1)=N_G(D_2)=S\).
>
> Then no such \(G\) exists.

For a minor-minimal \(HC_7\) counterexample, items 1--3 are already proved
criticality consequences.  At an exact full seven-adhesion, item 5 is the
surviving two-shore case (three shores give the displayed elementary
\(K_7\)-model).  No inference \(vz\in E(G)\) for separator vertices is used;
the universal boundary vertex in item 4 need not be identified in advance
with the apex that produced the adhesion.

An equivalent formulation may replace items 1 and 3 by "\(G\) is
seven-contraction-critical and \(K_7\)-minor-free", together with the known
seven-connectivity theorem.

## 3. Audit of the seven dependencies

### 3.1 Frame ownership -- proved

For each relaxed four-frame, if both shores are crossless, the two web disks
glue to make \(G-Z\) planar; \(G[Z]\) is bipartite, so the Four Colour
Theorem gives a six-colouring of \(G\).  Hence every frame is crossed in at
least one shore.  Compatible opposite crossings in distinct shores lift to
the explicit seven bags in Lemma 2.1 of
`hadwiger_c6_opposite_crossing_dichotomy.md`.  This proves unique ownership,
common ownership of opposite frames, and a high-owner shore.

This uses non-six-colourability, not an assumed operation state.  The
retracted coarse two-cut Lemma 4.1 in that file is not used.

### 3.2 Finite multiplicity base and Hall -- proved, computer assisted

If six portal classes fail Hall, deleting their union and the complementary
boundary labels gives a cut of order at most six unless the shore has order
at most five.  Two-connectivity excludes orders two and three, and the order
four/five programs exhaust all remaining shore graphs, portal assignments,
owned-frame signatures, outward locks, forbidden linkages, connected splits,
and degree rows.

The outward locks are not assumptions: the one-contact repair models in
`hadwiger_c6_crossing_portal_lock.md` show that any outward absorption gives
a \(K_7\)-minor.  Every positive connected split in the exact atlas likewise
lifts through the opposite full shore.

I recompiled both programs with C++20.  Their outputs reproduce the archived
zero-survivor table: all three order-four types and all ten order-five types
have zero actual survivors.

### 3.3 Forbidden antipodal and nonidentity linkages -- proved

The antipodal two-linkage quotients and the two alternating three-linkage
connector-tree cases have explicit \(K_7\)-models.  The constructions use
actual disjoint connected path pieces and the connected opposite shore; no
unrooted-to-rooted inference occurs.

### 3.4 Bare four-webs -- proved modulo the cited standard theorem

The generalized Two Paths theorem is used in its same-vertex web-completion
form.  A nonempty inserted piece lies behind a triangle; replacing artificial
terminals by their boundary labels and adding the three omitted boundary
vertices gives a separator of order at most six.  Seven-connectivity therefore
kills all insertions.  Deleting the artificial terminals leaves the full four
portal sets on one face.

This is the one external structural dependency whose exact published
statement should be quoted in a paper.  The local argument does not assume
six- or ten-connectivity of a rooted-linkage theorem.

### 3.5 Three-connected high-owner closure -- proved, computer assisted

Whitney uniqueness synchronizes the three bare-web embeddings.  The distinct
face alternative reduces to an unsubdivided triangular prism; any subdivided
or cap part is separated by at most three rung endpoints plus \(z\), while an
unsubdivided prism vertex has total degree at most six.  Hence all six portal
sets lie on one facial cycle.

Hall supplies an SDR.  The exact disk rule remains valid when the two portal
occurrences of one connector coincide.  The finite circular-occurrence system
for a second opposite frame pair is unsatisfiable.  I reran
`c6_circular_witness_degenerate_smt.py` and its independent sixteen-collapse
table: all twelve unnormalised instances and all sixteen collapse patterns are
UNSAT.  The weaker, retracted four-distinct-occurrence argument is not used.

### 3.6 Exact two-piece and degree-two locks -- proved, computer assisted

The exact adjacent-piece atlas is exhaustive: on the ten-vertex quotient it
enumerates every support of order seven through ten and every partition into
seven nonempty bags.  Seven-connectivity then proves two-connectivity of each
nonsingleton shore and that every shore two-cut has exactly two components.

For a shore-degree-two vertex \(x\), degree and cut bounds put the two split
defects in the low-defect atlas.  The only possible orientation is

\[
 S-N_S(x)=N_{C_6}(v_x),\qquad
 S-N_S(D-x)=\{v_x\}.                              \tag{3.1}
\]

Thus \(d_G(x)=7\).  This conclusion is derived, not assumed.

### 3.7 Cycle-leaf frontier and elimination -- proved, computer assisted

Dirac's inequality first makes every S-leaf a one-vertex ear and forces its
separator edge \(pq\).  The exact one-ear program leaves only the five maximal
negative contact rows recorded in the note.  I reran the program with
NetworkX 3.6.1: it reproduced 64 atlas states, the five maximal negative
frontier rows, and the exhaustive 1,899,612-partition negative checks.

A seven-fan from the degree-seven ear vertex uses its five direct boundary
neighbours and the two shore neighbours.  The archived verifier reproduces a
\(K_7\)-model whenever either cut vertex is broad.  In the double-thin state,
terminal-essentiality plus the standard web theorem makes four terminals
cofacial.  Contracting the connected body preserves planarity and cofaciality;
adding a cofacial apex exposes the displayed subdivision of \(K_{3,3}\).

The orientation-free rank-four SPQR argument yields a singleton on one side
of every leaf separation.  It does not claim that the selected leaf-node side
is the singleton.  Dirac forces \(pq\), and the three \(p\)-\(q\) bridges then
create an actual singleton S-leaf, which the preceding argument eliminates.
The retracted SPQR-path/oriented-end claim is not used.

## 4. Proper-minor and colouring audit

* Every helper contraction is of a connected nonempty shore or a connected
  path/body, and the displayed branch bags are pairwise disjoint.
* Opposite-shore helpers are never assumed adjacent to each other; there are
  exactly two anticomplete components.
* The seven-fan arms are internally disjoint and are contracted toward their
  distinct starts, so their endpoint adjacencies are legitimate.
* Contracting the body \(B\) in the plane web avoids all four terminals; the
  image of their common face remains incident with them.
* The relaxed-frame colouring is a direct proper colouring: four colours on
  the planar graph \(G-Z\) and a disjoint two-colour palette on the bipartite
  graph \(G[Z]\).  It is not a gluing of incompatible minor colourings.
* No step assumes \(\chi(G/e)\le\chi(G)\), identifies nonadjacent vertices by
  a nonminor operation, or uses a boundary contact absent from the relevant
  branch set.

## 5. Scope

After adding the missing Dirac/criticality hypothesis, the
\(C_6\dot\cup K_1\) two-full-shore family is a genuine infinite local
closure, not merely another finite narrowing.  It still does not prove
\(HC_7\): reaching this exact adhesion from every hypothetical counterexample,
the other degree-seven boundary cells, one-component cells, and degree-eight/
degree-nine cases remain separate issues.

The result should therefore be installed as a local theorem with the explicit
hypotheses in Section 2, while `hadwiger_c6_core_closure.md` should not be cited
verbatim until its theorem statement is repaired.
