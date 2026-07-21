# Audit of the all-double-critical terminal-cycle deletion theorem

**Status:** separate internal exact-file audit.

**Verdict:** GREEN.

**Audited theorem revision:** SHA-256
`7c1dc875c7d9c5ecee0b7fdfca91ec90ab78040bd7cf3699dc01efd6f6852bf3`.

**Final theorem revision after the status-only promotion:** SHA-256
`d4efb192d961c9fa00c2e43e56bb3ff26abf2146f950d0cede6931a4764dc4ad`.

**Audited barrier revision:** SHA-256
`d16fb5bda39f183ebef0ddef17591bf985faf9605d52f9fd7908057f0c2b52eb`.

## Verdict

**PASS.** Every stated hypothesis is used correctly, the deletion language
and six-core packing conclusions follow, both external theorems have the
required strength, and the scoped frame-selection counterexample has the
claimed connectivity, edge strata, extremal frames, and explicit
`K_7`-minor model.

The only change after the exact-file audit was replacement of the theorem's
draft status sentence by its audited status sentence. No mathematical
statement, proof, source, or scope assertion changed. This audit does not
promote the result to six-residual closure or to a proof of `HC_7`.

## Detailed checks

1. Strong seven-contraction-criticality gives `chi(G-{p,q})<=6`. A
   four-colouring extended by two fresh colours would six-colour `G`, so
   the value is five or six. The equivalence with avoidance by an induced
   vertex-minimal six-chromatic subgraph is exact.

2. For a nonempty proper `S subset V(C)`, independence permits one fresh
   colour. If `S` contains an edge, it lies over a double-critical cycle
   edge, while every proper induced subgraph of a chordless cycle is
   bipartite. These observations give both lines of (2.1). Restoring the
   whole cycle with two colours when even and three when odd gives (2.2).

3. The Dominating 4-Colour Theorem, Theorem 1.1 and its normalization
   remarks, give the fixed normalized dominating `K_5` model in Corollary
   2.2. The parity saturation recolouring uses one fresh colour on one
   parity class and independently available old colours on the other.

4. In Corollary 2.3, `V(C)-{v}` is proper and contains a cycle edge, so
   `H+v` is five-chromatic. A vertex-minimal five-chromatic induced
   subgraph contains `v`. Martinsson--Steiner Corollary 1.4 permits that
   prescribed vertex to be a singleton branch set of a `K_5` model.

5. Every double-critical cycle edge meets every six-core. A six-core in
   `G-v` contains both cycle neighbours of `v`. Three disjoint cores
   cannot meet one two-vertex edge; two disjoint cores force alternation
   and even parity.

6. For `K_1 vee C_5 vee C_5`, the join formula gives chromatic number
   seven, and minimum degree and vertex connectivity are both eight.
   Cycle-edge endpoint deletion leaves chromatic number six; every join
   edge is double-critical.

7. Both displayed ordered frames are singleton `K_5` models satisfying
   all domination adjacencies. Support order five and terminal-cycle
   length three are absolute minima. Their terminal triangles have the
   asserted opposite edge-stratum behaviour.

8. The barrier has clique number five. Contracting each `C_5` to a
   `K_3` and retaining the hub gives an explicit `K_7`-minor model.
   Therefore it is correctly excluded from the full strong
   minor-critical hypotheses.

## Unresolved assumptions

None inside the theorem or scoped barrier. The gate discussion correctly
records that neither result supplies label-preserving allocation, a
six-residual successor, or strict descent.
