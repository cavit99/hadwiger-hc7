# Atomic one-collision weak-immersion frontier

**Status:** frozen conditional laboratory.  The results linked below apply
after choosing a weak `K_7` immersion with exactly one binary collision.
No current theorem shows that an arbitrary guaranteed weak immersion has
this form, so this direction is not an exhaustive entry to `HC_7` and does
not replace the bounded-interface primary target.

## 1. Conditional entry

The audited
[atomic rounding theorem](../results/hc7_atomic_weak_k7_immersion_rounding.md)
classifies one binary collision.  A common-end collision gives an explicit
`K_7`-minor model.  Every other collision gives a spanning model of `K_7`
with one missing adjacency and singleton deficient roots.  In the
disjoint-demand case it also gives a common frame whose residual quotient is
the octahedral graph `K_8-3K_2`.  If the collision vertex has degree at most
nine, the theorem returns a bounded full response interface.

The general minimum-degree immersion theorem supplies some weak `K_7`
immersion in the hypothetical counterexample, but neither atomicity nor a
degree bound for a collision vertex is proved here.  Existing collision-
relocation and partial-contraction barriers show that the evident
lexicographic shortcuts do not supply either conclusion.

## 2. Audited reduction inside the atomic case

The audited atomic programme has several descendants.  In one two-bridge
descendant, it closes a clean missing-pair path, a crossing bridge, clean
three-arm attachment, exact forest landing, the exact shared-hub core, and
the exact dirty two-bridge core.  The current arbitrary-subdivision endpoint
of that descendant is the
[landing-star theorem](../results/hc7_atomic_two_bridge_subdivision_landing_stars.md).

Let `Omega_q` be the literal first-hit boundary in that theorem.  A common
first-hit component meeting both open landing stars at `e` and `x` gives an
explicit `K_7`-minor model, even when the two clean paths intersect.  Hence
a `K_7`-minor-free survivor avoids one complete open star.  For a
minimum-cardinality `q`--`b` separator `S subseteq Omega_q`:

- if `|S|<=9`, this chosen `S` is a full four-colourable response interface
  with exact independent-block and selected-edge responses; and
- otherwise every `q`--`b` separator contained in `Omega_q` has order at
  least ten.

The
[forced-hub transit-label barrier](../barriers/hc7_atomic_two_safe_transit_label_barrier.md)
shows that the proposed two-label small-boundary shortcut has only one safe
label under its prescribed ownership.  Further finite exact-core
enumeration therefore does not address the surviving inference.

## 3. Exact two-bridge descendant residue

The remaining configuration in this exact two-bridge descendant is an
arbitrary subdivision of the two-bridge core in which the first-hit boundary
avoids one whole open landing star and every contained `q`--`b` separator has
order at least ten.  The required label-preserving bridge-composition theorem
must produce one of:

1. an explicit `K_7`-minor model by rerouting into the avoided star;
2. a bounded full response interface that can be composed through the
   primary bounded-interface theorem; or
3. a strict same-host reduction with a declared decreasing literal
   component parameter and all named ownership data preserved.

Returning another dirty path, an unbounded quotient separator, or a fresh
unranked response is nonterminal.

No theorem reduces every atomic disjoint-demand collision to this
two-bridge descendant.  Hall-deficient clean-support configurations and the
first bad partial-quotient residue remain separate conditional obligations.

## 4. Frozen conditional target

This two-bridge laboratory remains frozen during the opposite-shore response
sprint.
It should be reopened only if a new theorem connects an arbitrary
collision-minimal weak immersion to the atomic case, or if the global
bounded-interface work supplies a label-preserving composition mechanism
that directly resolves the large one-star residue.

## Dependencies and guardrails

- [atomic weak-immersion rounding](../results/hc7_atomic_weak_k7_immersion_rounding.md)
- [octahedral-frame augmentation](../results/hc7_atomic_octahedral_frame_augmentation.md)
- [arbitrary-subdivision first-hit boundary](../results/hc7_atomic_subdivision_first_hit_boundary.md)
- [small-separator response boundary](../results/hc7_atomic_path_absence_response_boundary.md)
- [exact two-bridge seven-fan closure](../results/hc7_atomic_two_bridge_exact_core_seven_fan_closure.md)
- [landing-star closure](../results/hc7_atomic_two_bridge_subdivision_landing_stars.md)
- [dirty two-bridge-chain barrier](../barriers/hc7_atomic_dirty_two_bridge_chain_barrier.md)
- [forced-hub transit-label barrier](../barriers/hc7_atomic_two_safe_transit_label_barrier.md)

Internal audits establish only the repository's current trust status; they
are not external peer review.
