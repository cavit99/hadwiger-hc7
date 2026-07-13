# Counter-audit of the proposed \(C_6\dot\cup K_1\) closure

## Verdict

**RED: the full two-connected-shore closure is not proved.**

The finite contact certificates, the three-connected high-owner branch,
and the conditional elimination of an actual singleton S-leaf survive this
spot-check.  The step which is supposed to force such an S-leaf from an
arbitrary nontrivial SPQR tree is false: a web embedding with four portal
classes cofacial need not remain portal-cofacial after the relevant SPQR
reflection.  Consequently a two-portal block is allowed to disappear from
the distinguished face, rather than becoming a nonalternating block on that
face.

The claimed implication

\[
 \text{one crossless four-terminal web}
 \Longrightarrow
 \text{one side of every SPQR leaf has portal rank at most one}
\]

therefore has no valid proof and is false under its stated four-terminal
hypotheses.

## 1. Exact failed step

Lines 346--368 of `hadwiger_circular_obstruction_frame_theorem.md`,
lines 46--58 of `hadwiger_c6_full_closure_audit.md`, and lines 85--92 of
`hadwiger_c6_core_closure.md` argue as follows:

1. choose a plane embedding in which four portal classes lie on one facial
   cycle;
2. reflect an SPQR leaf;
3. regard the new circular order as a reversal of one contiguous portal
   block; and
4. assert that the four representatives must still alternate.

Step 4 is unjustified.  Reflecting a 2-sum side changes which of its two
pole-incident faces is paired with the relevant face of the other side.  The
four portal classes need not lie on one face in the reflected embedding.
Crosslessness constrains their order *when they are cofacial*; it does not
force them to remain cofacial in every SPQR embedding.

## 2. A concrete rank-two/rank-two counterexample

Let \(D\) have vertices

\[
 p,q,a,c,u,d,b,v
\]

and edges

\[
\begin{aligned}
 &pa,ac,cq,pu,uq,ua,uc,\\
 &pd,db,bq,pv,vq,vd,vb.
\end{aligned}
\]

Then:

1. \(D\) is planar and two-connected.
2. \(\{p,q\}\) is a two-cut with exactly two components
   \(L=\{a,c,u\}\) and \(R=\{b,d,v\}\).
3. Adding the virtual edge \(pq\) to either side produces a
   three-connected wheel-like torso.  Thus the reduced SPQR tree has an
   edge whose two leaf interiors are exactly \(L\) and \(R\).
4. The cycle

   \[
       p a c q b d p
   \]

   is facial in a plane embedding of \(D\).
5. Put four singleton portal classes at \(a,c,b,d\), with prescribed
   linkage pairs \(a b\) and \(c d\).  Their facial order is
   \(a,c,b,d\), so the pairs alternate.  Direct exhaustive path search
   confirms that \(D\) has no disjoint \(a\)-\(b\) and \(c\)-\(d\)
   paths.
6. The unique four-class SDR meets \(L\) in \(\{a,c\}\) and \(R\) in
   \(\{b,d\}\).  Hence both sides have transversal rank exactly two.
7. Every shore vertex has degree at least three, so a hypothesis only about
   degree-two portal locks is vacuous here.

The dependency-free verifier is
`c6_rank_four_leaf_counterexample.py`.  It prints

```text
planar with required facial cycle True
two-cut components [['a', 'c', 'u'], ['b', 'd', 'v']]
augmented torso connectivities (3, 3)
prescribed disjoint linkage False
portal ranks across SPQR edge (2, 2)
```

This example does not claim to be an HC7 counterexample and does not satisfy
all six labelled portal conditions.  It does something more targeted: it
falsifies the four-terminal SPQR inference used to derive Theorem 6.1.  The
extra high-owner hypotheses are never used to repair that inference.

## 3. What remains safe

Subject to the external generalized Two Paths Theorem in the precise
same-vertex web-completion form, and subject to independent replay of the
listed finite certificates, the following restricted conclusions remain
supportable.

1. **Three-connected branch.**  A three-connected high-owner shore is
   excluded by Whitney uniqueness, the face trichotomy, and the finite
   circular-occurrence obstruction.
2. **Actual S-leaf branch.**  If the high-owner shore already has a
   cycle-type SPQR leaf, Dirac reduces it to a singleton ear; the exact
   one-ear atlas, seven-fan, and bare-web \(K_{3,3}\) argument eliminate
   it.
3. **Finite Hall base.**  The order-four and order-five portal searches
   have zero survivors under a set of necessary conditions weaker than the
   full counterexample hypotheses.

What is not safe is the passage from an arbitrary non-three-connected shore
to an S-leaf.  A replacement must synchronize the relevant portal face
across the SPQR edge, or use two or three web states jointly to eliminate
the rank-two/rank-two leaf transition.

## 4. Dependency boundary

The external input is Humeau--Pous, Generalised Two Paths Theorem,
Theorem 1.5: a maximally crossless tuple is a web with that frame.  The
paper supports the same-vertex web-completion use.  It does **not** say that
a portal-cofacial face is invariant under every SPQR reflection.

The computer-assisted inputs replayed in this spot-check are:

* `c6_order4_portal_exhaustive.cpp` and
  `c6_order5_portal_exhaustive.cpp` (zero actual survivors);
* `c6_circular_witness_degenerate_smt.py` (all twelve systems UNSAT);
* `c6_cycle_leaf_probe.py` (64 states and the five-row negative frontier);
* `c6_cycle_leaf_fan_verify.py` (broad rows positive, double-thin rows
  negative at the quotient level); and
* `c6_double_thin_web_verify.py` (the displayed subdivided \(K_{3,3}\)).

These computations do not certify the invalid SPQR face-invariance step.

## 5. Exact safe theorem statement after the audit

The currently justified local result is the following disjunction, not the
full theorem in `hadwiger_c6_core_closure.md`:

> Under the exact two-full-shore hypotheses (including the Dirac local
> inequality), the high-owner shore is neither three-connected nor allowed
> to have a cycle-type SPQR leaf.

The unresolved residue is a nontrivial SPQR tree all of whose actual leaf
nodes are non-cycle torsos, with at least one rank-two/rank-two portal-face
transition.  Eliminating that residue requires a new simultaneous-web/SPQR
synchronisation lemma.

## 6. Follow-up: the displayed host is not a simultaneous six-state survivor

The counterexample in Section 2 refutes the *one-web inference*, but it
cannot itself be decorated with the full six-label high-owner packet.
`c6_two_r_torso_simultaneous_state_verify.py` proves the following exact
finite lemma on this eight-vertex host:

> If six portal classes have an SDR and all three antipodal demand pairs are
> crossless, then at most one opposite frame pair is present.

The verifier generates all 167 connected carrier masks and all 2270 ordered
disjoint carrier pairs.  All three choices of two owned opposite frame pairs
are UNSAT.  This uses neither outward-contact locks nor the alternating
three-linkage exclusions.  The detailed statement is in
`hadwiger_c6_two_r_torso_simultaneous_state_lemma.md`.

This does not validate the leaf-flip proof: the contradiction uses all three
web states and the six-class SDR simultaneously, whereas the proof under
audit invokes only one web state.  It does show that the smallest geometric
obstruction is eliminated by the correct kind of replacement theorem.
