# Two-lobe adaptive peel-or-six-cut: exact bounded probe

**Status:** candidate theorem plus an exact bounded UNSAT certificate.  This
is not a proof of the unbounded statement and is not promoted.

## 1. Strongest plausible statement

Retain the audited exact-seven `(1,2)` setup.  Thus

\[
V(G)=L\mathbin{\dot\cup}S\mathbin{\dot\cup}R,
\qquad |S|=7,
\]

is an actual separation, `G[L]` is three-connected, `R` contains two
disjoint adjacent `S`-full packets, and `H=G[S]` is one of the paired
width-two boundary graphs.  Let `T` be a three-cut of `G[L]` with exactly
two lobes, in one of the lobe-centred-star or capacity-triangle normal
forms of the audited support-four transition.

Call a bipartition `L=X dotcup Y` an **adaptive peel** when:

1. `X,Y` are nonempty and connected (hence adjacent);
2. there is a partition

   \[
   S=I\mathbin{\dot\cup}J\mathbin{\dot\cup}U
   \]

   in which `I,J` are nonempty independent sets and `U` is a clique; and
3. `X` contacts every literal of `I`, while `Y` contacts every literal of
   `J`, after possibly interchanging the two carriers.

The audited adaptive clique-reservoir theorem closes the counterexample as
soon as such a peel exists.  The strongest local statement which survived
the present falsification is:

> **Candidate adaptive peel-or-six-cut lemma.**  In the exact two-lobe
> star/triangle cell, either there is an adaptive peel, there is a literal
> labelled `K_7^vee`/`K_7` handoff, or `G` has a separation of order at most
> six.

The labelled-model alternative is retained because a connectivity-only
peel statement has not been proved.  In a hypothetical counterexample the
cut alternative is excluded by seven-connectivity; the peel alternative
gives an exact colouring contradiction.

## 2. A sharper four-state star target

The lobe-star support-only obstruction from the adaptive-return theorem can
be labelled

\[
S=\{z,a_1,a_2,a_3,b_1,b_2,b_3\},
\]

with boundary tree

\[
za_2,a_2a_3,a_3a_1,\qquad zb_1,b_1b_2,zb_3,
\]

and lobe supports

\[
A=\{z,a_1,a_2,a_3\},\qquad
C=\{z,b_1,b_2,b_3\}.
\]

All gates have support contained in `C`.  Taking the clique reservoir to be
`U={z}` leaves only four exact mixed-duty states:

\[
\begin{array}{c|c}
\{a_1,a_2,b_1\}&\{a_3,b_2,b_3\}\\
\{a_1,a_2,b_1,b_3\}&\{a_3,b_2\}\\
\{a_1,a_2,b_2\}&\{a_3,b_1,b_3\}\\
\{a_1,a_2,b_2,b_3\}&\{a_3,b_1\}.
\end{array}
\]

Thus a materially narrower proof target is:

> **Mixed-terminal packing target.**  Two disjoint adjacent connected
> carriers realize one row of the table, or a labelled near model occurs,
> or there is a cut of order at most six.

This target mentions literal terminal sets, not colours or unnamed model
bags.  It is the exact carrier statement needed by the adaptive-return
theorem in this star cell.

## 3. Exact search model

The verifier is
`archive/hc7_two_lobe_peel_or_cut_probe.py`.  It uses a finite Boolean
portal-edge encoding and checks every connected bipartition of the thin
shore.  For each split it forbids every legal independent-seed/clique-
reservoir state, not merely the old fixed bipartition duty.

Seven-connectivity is enforced exactly by cut generation.  Whenever a
portal assignment has a cut of order below seven, the verifier adds the
disjunction of every still-available portal edge crossing that literal
cut.  Termination with UNSAT therefore certifies that no portal assignment
in the stated finite class is seven-connected.

The rich shore is not represented by two artificially full singleton
vertices in the main checks.  It consists of two adjacent four-vertex
cliques.  In each clique two distinguished literals are split between two
compulsory vertices.  Every full packet in that clique contains both
compulsory vertices.  The verifier exhausts its connected subsets and
checks that the full-packet packing number of the complete rich shore is
exactly two.

The following exact checks are green:

1. **Dense lobe-star.**  Both lobes are `K_4`, the three gates are complete
   to both lobes, and all legal portal assignments in the exact star normal
   form are tested.  There are `795` connected carrier splits.  Forbidding
   every adaptive peel plus exact seven-connectivity is UNSAT.
2. **Four-state dense lobe-star.**  Both lobes are `K_5`.  Only the four
   reservoir-`z` mixed states displayed above are forbidden.  There are
   `3,131` connected splits.  Exact seven-connectivity is already UNSAT.
3. **Atlas lobe-star.**  Every graph on at most seven thin vertices in the
   NetworkX graph atlas with connectivity exactly three, internal minimum
   degree at least four, and a three-cut leaving exactly two lobes is
   tested, with both lobe orientations.  All eight labelled skeleton
   orientations admit static nonpeel portal assignments, but none admits a
   seven-connected one, even with the expanded rich packets.
4. **Atlas capacity triangle.**  The analogous census tests all three
   choices of exceptional gate and both lobe orientations.  All twenty-four
   labelled skeleton instances admit static nonpeel assignments; none is
   seven-connected with the expanded rich packets.

The search becomes UNSAT before `K_7`-minor-freeness, absence of a labelled
`K_7^vee`, or Dirac's inequalities are imposed.  Hence adding those kernel
hypotheses cannot create a survivor inside the certified finite classes.
This does not make the unbounded theorem connectivity-only.

## 4. What the cut clauses expose

The relevant invariant is **literal mixed-terminal cut expansion**.
Static support existence is not enough.  Failure of all four mixed states
forces one of two kinds of low cut in every bounded survivor:

1. a cut isolating a boundary path segment whose required portal classes
   are concentrated on too few lobe vertices; or
2. a cut separating the combined gate/lobe core after one or two portal
   vertices and a small set of old boundary literals are deleted.

With expanded rich packets the generated obstructions have order four or
five in the dense `K_4` lobe cell.  Thus the extra rich-side boundary degree
does not repair the obstruction: the decisive cuts run through the literal
portal distribution inside the two lobes.

This identifies the proof mechanism to pursue.  Apply a two-disjoint-
connected-subgraphs theorem to the four mixed terminal rows.  If no row
packs, extract its Menger separator.  The target proof must uncross the four
separators so that their union with the unused boundary literals has order
at most six, unless the crossings themselves give the labelled
`K_7^vee` handoff.

## 5. Trust boundary

The experiment does **not** prove the candidate lemma:

- lobe interiors are bounded in the atlas census;
- the larger exact checks use clique lobes and complete gate-to-lobe
  incidence;
- only one explicit paired tree is used in each of the star and triangle
  checks; and
- proper-minor response and `K_7`-minor-freeness are not needed inside the
  tested classes, so the search says nothing about an unbounded web whose
  portal cuts drift with its order.

A five-connected dense-star assignment with no adaptive peel exists and
fails Dirac's inequalities.  The repository's independent static-split
barrier is also `K_7`-minor-free but only five-connected.  These failures
confirm that the exact seven-connectivity/cut-expansion hypothesis cannot
be dropped.

The bounded result is therefore a guardrail and a proof invariant, not a
new promoted theorem.

## 6. Reproduction

Run each mode in a fresh process (the exact Boolean formulas are large):

```text
PYTHONPATH=active/runtime/deps python3 \
  archive/hc7_two_lobe_peel_or_cut_probe.py dense-star
PYTHONPATH=active/runtime/deps python3 \
  archive/hc7_two_lobe_peel_or_cut_probe.py dense-cross
PYTHONPATH=active/runtime/deps python3 \
  archive/hc7_two_lobe_peel_or_cut_probe.py star-atlas
PYTHONPATH=active/runtime/deps python3 \
  archive/hc7_two_lobe_peel_or_cut_probe.py triangle-atlas
PYTHONPATH=active/runtime/deps python3 \
  archive/hc7_two_lobe_peel_or_cut_probe.py packet
```

The cut-clause count can vary with the SAT model order; the UNSAT/SAT
verdicts and exhaustive class sizes are invariant.
