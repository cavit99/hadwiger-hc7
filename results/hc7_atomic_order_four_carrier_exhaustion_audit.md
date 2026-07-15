# Independent audit: order-four carrier exhaustion

Verdict: GREEN.

Audited note: results/hc7_atomic_order_four_carrier_exhaustion.md

Note SHA-256: d737fceb75bb075fb9efcc73871b43162506d2b07e74bd07e9a9f18984f23f9e

Verifier: active/hc7_atomic_order_four_carrier_exhaustion.py

Verifier SHA-256: a94ad97e93ae3ef0a38a4705e10f4a3305bbcd63844255106da9c1dd9b18882a

Post-audit note: the shared helper was generalized to take the thin
vertex tuple from its argument rather than the order-four module constant,
and a SAT-witness return mode was added for the separate order-five
guardrail.  Neither change alters the order-four formula.  The 38-cell
order-four run was repeated after these changes and again returned
`UNSAT` in every cell.

## 1. Thin graphs and rooted frontiers

On four thin vertices, degree at least three makes z adjacent to the other
three. Two-connectivity makes A-z connected, so it induces a path or a
triangle. These give exactly K4-e and K4.

The repaired generator exhausts the paired width-two boundary conditions
and obtains 192 labelled frontiers. Distinguishing the compulsory literal
among the six paired vertices and quotienting only by rooted graph
isomorphism gives 19 types. I reproduced both counts independently.
Discarding the old pair names after this step is safe: the solver uses only
the literal rooted graph and enumerates every new clique-reservoir
partition.

## 2. Cut and contact encoding

The 24 Boolean variables are exactly the contacts from A to the six
noncompulsory literals. The edge zu is fixed and no other thin vertex sees
u. Six clauses state that A-z is W-full.

For every nonempty connected D in A, the verifier computes its thin
external neighbourhood, counts u exactly when z lies in D, and counts each
W literal once through an OR of its contacts. The pseudo-Boolean constraint
is exactly

    |N_A(D)| + |N_S(D)| >= 7.

Connected sets suffice because the neighbourhood of any component of a
disconnected D is contained in the neighbourhood of D. The nonempty
opposite shore makes these genuine relative cuts.

## 3. Adaptive partitions and carriers

Every carrier is nonempty and connected. Every tested pair is disjoint,
has a literal cross-edge, and puts z in the first carrier. Every clique
reservoir is considered. Its complement is split into two nonempty
independent seeds. Forcing the last free literal onto the second seed
removes only reversal symmetry, and both carrier orientations are then
tested explicitly. The fixed sparse frontiers never reach the negative
shift empty-free case; one free literal correctly gives no two-seed
partition.

The negated conjunction for each pair and partition is exactly failure of
the required literal seed contacts. Thus a satisfying assignment would be
precisely a frozen contact map with no adaptive return.

## 4. Reproduction and consequence

Running

    PYTHONPATH=active/runtime/deps python3 active/hc7_atomic_order_four_carrier_exhaustion.py

returns UNSAT for all 19 rooted frontiers with each of the two thin graphs,
38 cells total. The printed connected-set, carrier-pair and partition
counts agree with direct enumeration.

The resulting carriers meet every hypothesis of the audited adaptive
clique-reservoir theorem, while the frozen rich shore supplies the two
full packets. Hence the bounded order-four cell closes. The source
correctly makes no unbounded crossed-hull claim.
