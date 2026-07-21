# Two exact-block transitions give disjoint opposite-shore paths

**Status:** written proof; [separately audited **GREEN**](hc7_bounded_interface_two_transition_disjoint_response_audit.md).
This is a nonterminal bounded-interface reduction.  It removes the
shore-tag and boundary-endpoint mismatch without applying a global
endpoint-family classification: the endpoint pair of a first-shore path is
used as the fixed exact block for a second transition.  The two paths may
come from different colouring operations.

## 1. Setup

Let `G` be a hypothetical minor-minimal counterexample to `HC_7`, with the
audited bounded-interface data

\[
  u,z,C,S,\qquad
  A=G[C\cup S],\qquad B=G-C,
\]

where

\[
  7\le |S|\le d_G(u)\le9,
  \qquad S=N_G(C)\subseteq N(u),
  \qquad z\in S,
  \qquad \chi(G-\{u,z\})=6.                         \tag{1.1}
\]

For every nonempty independent `I subseteq S`, use a shortest exact-`I`
boundary transition as in the audited exact-block Kempe reduction.

## 2. The two-transition reduction

### Theorem 2.1

At least one of the following holds.

1. **Common boundary partition.**  One complete equality partition of `S`
   is induced by proper six-colourings of both `A` and `B`.
2. **Exact aligned restart.**  Some component `D` of `G-N[u]` satisfies

   \[
                         z\in N_G(D),\qquad |D|<|C|.   \tag{2.1}
   \]

3. **Disjoint opposite-shore paths from two transitions.**  There are two
   disjoint boundary nonedges

   \[
                         e,f\in\binom S2               \tag{2.2}
   \]

   and paths `P_A,P_B` with ends `e,f`, respectively, such that

   \[
   \operatorname{int}(P_A)\subseteq C,
   \qquad
   \operatorname{int}(P_B)\subseteq B-(S\cup\{u\}).   \tag{2.3}
   \]

   The paths are vertex-disjoint.  The path `P_A` is the first failed lift
   of an exact-singleton transition; the path `P_B` is the last failed lift,
   or a pole-free realization of that same last move, in a second transition
   whose fixed exact block is `e`.
4. **Tight pole residue.**  For some boundary nonedge `e`, a shortest
   exact-`e` transition ends in the tight pole normal form: its final trace
   has five blocks, its predecessor has six, one singleton is merged into a
   non-singleton independent block disjoint from `e`, and in every final
   `B`-extension the corresponding two-colour component cannot reach
   another boundary vertex after deleting `u`.

In outcome 3, if `G[S]+e+f` has a `K_6` minor, then `G` has an explicit
`K_7`-minor model.  Hence in the hypothetical-counterexample setup the
remaining path outcome necessarily satisfies

\[
                         K_6\not\preccurlyeq G[S]+e+f. \tag{2.4}
\]

### Proof

If outcome 1 or 2 holds, there is nothing to prove.  Assume neither.

Fix any `x in S` and take a shortest exact-`{x}` transition.  At its first
interchange, the old boundary colouring extends through `A` and the new
one does not.  The one-interchange lifting lemma gives a path `P_A` whose
interior lies in `C` and whose ends form a pair

\[
                              e=\{p,q\}\subseteq S-\{x\}. \tag{2.5}
\]

The ends lie in distinct components of one boundary two-colour graph, so
`pq` is not an edge of `G[S]`.  Thus `e` is itself a nonempty independent
set and may be prescribed as one exact boundary block.

Take a shortest exact-`e` transition and fix a proper six-colouring `c` of
`B` inducing its final boundary trace.  Apply the canonical last-interchange
dichotomy relative to `c`.  If it has the pole-free outcome, let `P_B` be
the returned path.  If it is a pole move, apply the pole-move normal-form
theorem relative to the same extension.  Either that same last move has a
pole-free path `P_B`, or the transition is outcome 4.

Every interchange in the exact-`e` cylinder avoids the fixed colour on
`e` and never assigns that colour outside `e`.  The two colours supporting
`P_B` are therefore different from the colour on `e`, and both boundary
ends of `P_B` lie in `S-e`.  Write their pair as `f`.  As before, the ends
belong to distinct boundary two-colour components, so `f` is a boundary
nonedge.  We have

\[
                              e\cap f=\varnothing.       \tag{2.6}
\]

The first path has open interior in `C`; the second has open interior in
the opposite side and avoids `u`.  Their endpoints are disjoint by (2.6),
and the two open sides are disjoint (indeed anticomplete).  Thus
`P_A,P_B` are vertex-disjoint and outcome 3 holds.

For the final assertion, replace the two added edges in a `K_6` model of
`G[S]+e+f` by the two disjoint paths.  If an added edge lies inside one
branch set, add its path interior to that branch set; if it supplies an
adjacency between two branch sets, divide the path once and add the two
segments to the endpoint branch sets.  Disjointness of the endpoints and
paths makes the two replacements compatible.  Every resulting branch set
still meets `S`, so the singleton `{u}` is disjoint from and adjacent to
all six.  It completes an explicit `K_7` model in `G`.  Since the setup
excludes such a model, (2.4) follows.  \(\square\)

## 3. Localization and exact remaining inference

The path `P_B` has the same localization as in the exact-block reduction.
It meets at most three components `D` of `G-N[u]` other than `C`, and every
such component satisfies

\[
                         |N_G(D)\cap S|\ge |S|-2.       \tag{3.1}
\]

If any one also satisfies (2.1), outcome 2 applies.  Occurrence in an
arbitrary component, or in a component not adjacent to `z`, is not a valid
restart.

The theorem eliminates raw endpoint overlap and uncontrolled shore tags at
the level of literal paths.  It does not put the paths in one colouring
operation.  After (2.4), the unresolved decoder must actively use one of:

- full `K_7`-minor exclusion in the parts of the host outside the augmented
  boundary;
- the proper-minor colouring response while preserving the two transition
  labels; or
- an exact component `D` satisfying (2.1).

The alternative tight pole residue requires the same kind of host-level
input.  The independent-block pole-star barrier shows that exact-block
attainability, all pole-star responses, transition shortestness, and
seven-connectivity alone do not remove its six-block-to-five-block trace.

## 4. Dependencies

- [exact-block Kempe reduction](hc7_bounded_interface_exact_block_kempe_reduction.md),
  especially Lemma 3.1 and Theorem 4.1;
- [last-pole normal form](hc7_bounded_interface_pole_move_normal_form.md);
- [strict aligned restart](hc7_bounded_interface_endpoint_pair_selection.md#4-the-exact-strict-restart); and
- [independent-block pole-star barrier](../barriers/hc7_opposite_shore_shortest_transition_pole_barrier.md).
