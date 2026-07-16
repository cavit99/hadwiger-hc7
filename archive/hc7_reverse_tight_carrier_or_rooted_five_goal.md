# Active goal: reverse tight-lobe carrier or rooted five

**Status:** primary dependency-level target.  `HC_7` is not proved.

## Why the target changed

The former goal asked every actual `(1,2)` seven-adhesion to return an
exact boundary state of packet demand at most two.  That is too strong.
Seven connected-rich residual boundary types have absolute packet demand
three, so no such state exists for them.

The audited positive mechanism is already available: a returned
demand-three state reflects as soon as the rich shore supplies three
labelled carriers satisfying the exact duties of that state.  The missing
mathematics is therefore **carrier/model extraction**, not another
boundary-state census.

The superseded target is preserved in
`../archive/hc7_exact7_state_selection_goal_20260715.md`.

## Frozen input

Let `G` be a hypothetical minor-minimal counterexample to `HC_7`.  Use the
actual tight seven-separation

\[
 V(G)=D\mathbin{\dot\cup}\Omega\mathbin{\dot\cup}B,
 \qquad |\Omega|=7,
 \qquad (\nu_D,\nu_B)=(2,1),                         \tag{1}
\]

where `D` is the connected packet-two shore and `B` is the connected
`Omega`-full packet-one shore.  Put `H=G[Omega]`.

Apply the already-audited robust-block, two-anchor, and connected
one-anchor closures.  A survivor has `H` in the 96 connected-rich
boundary residue and

\[
                         \alpha(H)\in\{3,4\}.          \tag{2}
\]

Choose a maximum independent set `I` of `H`, contract the connected set
`B union I`, and take a six-colouring of this named proper minor.  Its
restriction to the untouched closed `D`-shore returns an exact boundary
partition `Pi` containing `I` as one exact block.

The counting proof of the seven-vertex demand bound in
`../results/hc7_exact7_adaptive_packet_reflection.md`, Lemma 5.1, applies
verbatim: `I` has order four, or it has order three with
`alpha(H)=3`.  Hence

\[
                              d_H(\Pi)\le3.             \tag{3}
\]

If `d_H(Pi)<=2`, the two full packets in `D` reflect `Pi` and the two
closed-shore colourings glue.  Fix any returned `Pi`; the only live case
for that trace is

\[
                              d_H(\Pi)=3.               \tag{4}
\]

Choose a maximum clique `U` among the singleton blocks of `Pi`.  Exactly
three blocks are not represented by `U`; call them `C_1,C_2,C_3`.  Their
state-specific duties are

\[
 D_{\Pi,U}(C_i)=C_i\cup
 \{u\in U:N_H(u)\cap C_i=\varnothing\}.               \tag{5}
\]

## The theorem to prove

### Single-trace reverse tight-lobe carrier-or-rooted-five theorem

Under (1)--(5), at least one of the following holds.

1. **Exact carrier reflection.**  The shore `D` contains three pairwise
   disjoint connected labelled carriers satisfying Lemma 2.1 of
   `../results/hc7_exact7_rich_cutpacket_exchange.md` for the actual state
   `Pi`.  A sufficient special form is: after reselecting two disjoint
   `Omega`-full packets `P_1,P_2`, a connected
   `X subseteq D-(P_1 union P_2)` funds one duty in (5).  Assign the other
   two blocks to `P_1,P_2` and reflect `Pi` exactly.

2. **Reserved-anchor rooted five.**  For distinct `x,y in Omega`, the
   closed packet-one side
   `G[B union (Omega-{x,y})]` contains five pairwise disjoint connected
   pairwise adjacent bags, one containing each prescribed literal in
   `Omega-{x,y}` and all avoiding `x,y`.  Adjoin `x` and `y` to two
   disjoint full packets in `D`; the seven bags form a literal `K_7`
   model.

3. **Literal terminal.**  `G` contains a literal `K_7` model, or there is
   a fixed pair `{p,q}` such that `G-{p,q}` is `K_5`-minor-free.

4. **Ranked state-preserving descent.**  There is a strictly smaller
   actual seven-adhesion and an explicit boundary bijection mapping every
   block of `Pi`, the retained clique `U`, and each named duty in (5) to its
   descendant counterpart.  The map preserves every literal adjacency
   used by reflection and identifies the legal proper-minor operations
   attaining the mapped state on both closed shores.  The transition
   strictly decreases a declared lexicographic rank which cannot be
   restored by reversing the shore orientation.  A normalized labelled
   near-`K_7` handoff counts only if it carries such a nonreversible rank.

The new theorem is the implication to outcomes 1--4.  Reflection after
outcome 1, the seven-bag completion after outcome 2, the demand arithmetic,
and packet-path normalization are existing tools and must not be presented
as new progress.

## Constructive route

Use only the single legally attained trace `Pi` above.

1. Optimize the two full packets in `D` against the three duties in (5).
   Apply the audited attained-duty tree/point-tree gate theorem.  Disjoint
   duty hulls give outcome 1; otherwise each packet has either a universal
   literal gate vertex or a nontrivial gate core with the exceptional-duty
   leaf-witness structure.
2. Apply the Humeau--Pous generalized web decomposition to the complete
   ordered terminal interface, not to three unrelated four-terminal
   instances.  Decode every crossing using literal host paths.
3. At the first parallel-composition seam, prove one of: a third
   duty-correct carrier; the five prescribed rooted bags of outcome 2; or
   an actual seven-separation carrying the exact state data and strict
   rank of outcome 4.
4. Use the universal response of proper minors to break a reversible gate
   cycle.  One named colouring or one Kempe toggle is insufficient.

Completion edges in a web are never literal graph edges and cannot serve
as carrier contacts.  Unrooted regenerated `K_5` or `K_6` models are not
outcomes unless their five literal roots and two reserved anchors are
proved.

## Mandatory falsifiers

The ten-vertex local orientation shell in
`../barriers/hc7_tight_gate_local_orientation_shell.md` has connectivity
seven, vector `(2,1)`, an attained demand-three state, and no spare third
carrier.  It contains a literal `K_7` and is not contraction-critical.
Every proof must identify the step using `K_7`-minor-freeness or the full
proper-minor response.

## Literature boundary checked on 15 July 2026

- [Humeau--Pous](https://arxiv.org/abs/2505.16431) gives the constructive
  arbitrary-terminal crossing/web dichotomy and recursive parallel
  composition, but no exact colour-state transport.
- [Dvořák--Swart](https://arxiv.org/abs/2504.07764) shows that abstract
  boundary extension languages alone can be arbitrarily flexible while
  the relevant rooted and unrooted clique minors remain excluded.
- [Norin--Totschnig](https://arxiv.org/abs/2507.03244) supplies the
  `K_7^vee` near model in every non-six-colourable graph, not the labelled
  upgrade to `K_7`.
- [Kawarabayashi--Yu](https://arxiv.org/abs/2606.01586) validates
  separator-to-colour gluing through knittedness, but its connectivity
  threshold is far above this seven-connected interface.
- [Colorful Minors](https://arxiv.org/abs/2507.10467) and the 2026
  [rooted-folio bounds](https://arxiv.org/abs/2605.14902) preserve finite
  rooted geometry, not exact equality-state compatibility.  They remain
  backup certification tools.

No located theorem supplies the implication above.

## Success and stopping rules

Success is an audited proof of outcomes 1--4 for the single trace `Pi`.
A new portal taxonomy, an unlabelled near model, a naked smaller adhesion,
or a reversible state transition is not success.

Terminate any route whose state space grows with shore order or whose only
input is the abstract extension language.  General `t` is a generality
check only; the immediate objective remains `HC_7`.
