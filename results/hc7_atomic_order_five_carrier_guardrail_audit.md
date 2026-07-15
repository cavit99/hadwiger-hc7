# Independent audit: order-five carrier guardrail

**Verdict:** GREEN.

**Audited note:** `results/hc7_atomic_order_five_carrier_guardrail.md`

**Note SHA-256:** `8afbed4fe27590def48813fd96ae1ee1252d41493274106ae7e055f227c4f27b`

**Verifier:** `active/hc7_atomic_order_five_carrier_guardrail.py`

**Verifier SHA-256:** `e362b67b00476d1cb9ca5072d1c64e3951127bde216f57069c837fc8ed79fd70`

**Shared helper:** `active/hc7_atomic_order_four_carrier_exhaustion.py`

**Shared-helper SHA-256:** `a94ad97e93ae3ef0a38a4705e10f4a3305bbcd63844255106da9c1dd9b18882a`

## 1. Rooted order-five coverage

The graph-atlas filter ranges over every simple graph on five vertices and
keeps exactly the biconnected graphs.  An independent enumeration gives
ten unrooted graphs, 32 eligible labelled choices of `z` satisfying
`d_A(z)>=3` and connected `A-z`, and 14 rooted isomorphism types when the
root is preserved.  These agree with the asserted counts in the verifier.

The boundary generator is the repaired rooted generator audited with the
order-four exhaustion: it starts with all 192 labelled paired width-two
frontiers and preserves the compulsory literal under isomorphism, leaving
19 types.  Thus the run has `14*19=266` cells.  It does not collapse a
distinguished root or retain only unrooted representatives.

## 2. Contact and cut formula

For each cell the 30 Boolean variables are exactly the contacts from the
five thin vertices to the six literals in `W`.  The compulsory edge `zu`
is fixed, and the absence of any other `A-u` contact is represented by the
absence of corresponding variables.  Six clauses state that `A-z` is
`W`-full.

For every nonempty connected `D` in `A`, the shared helper now computes
the internal external-neighbour set over the local tuple `vertices`, not
the old four-vertex module constant.  It adds `u` precisely when `z` is in
`D`, counts each `W` literal once by an OR over contacts from `D`, and
imposes

    |N_A(D)| + |N_S(D)| >= 7.

This repairs the earlier vacuous order-five run.  Connected sets suffice:
every component of a disconnected thin set has no edge to the other
components, and its external neighbourhood is contained in that of the
whole set.

## 3. Adaptive exits

Every candidate carrier is nonempty and connected.  A candidate pair is
disjoint, adjacent by a literal thin edge, and has `z` in its first member.
Every clique reservoir of the rooted frontier is enumerated; its complement
is divided into two nonempty independent seeds.  Fixing the final free
literal in the second seed removes only seed-reversal symmetry, while the
solver tests both assignments of the two seeds to the two carriers.

For every such pair and partition, the added formula is exactly the
negation of the conjunction saying that the first carrier hits every
literal of one seed and the second hits every literal of the other seed.
Consequently a satisfying assignment would be precisely a legal contact
map satisfying all frozen cut constraints but admitting no adaptive
two-carrier return.

## 4. Reproduction and scope

I reran the corrected verifier.  It completed with

    GREEN unrooted_graphs 10 eligible_labelled_roots 32
    rooted_isomorphism_types 14 frontiers 19 unsat_cells 266

so every one of the 266 formulas is unsatisfiable.  The bounded conclusion
therefore follows: under the stated atomic hypotheses, an order-five thin
shore always has an adaptive carrier exit.  Together with the separately
audited adaptive clique-reservoir theorem this closes that bounded cell.

This is a finite guardrail only.  It does not prove the unbounded
crossed-hull implication, the all-locks residue, or `HC_7`; the note states
those limits explicitly.
