# Near-\(K_7\) route: high-level state (12 July 2026)

## Honest verdict

This route has not proved \(HC_7\), and therefore does not prove
Hadwiger's Conjecture.  It has converted one independent near-clique route
from a vague splitting hope into a small number of exact structural
obstructions.

## What is now rigorous

Starting from a spanning \(K_7^-\) or \(K_7^\vee\) model with one complex
bag, deleting the deficient apex leaves one complex bag plus a singleton
clique.  The desired \(K_7\) is equivalent to an explicit two-shore
(respectively three-shore) labelled split of that bag.

The following infinite families and reductions are closed in the current
notes.

1. Universal portal rows are impossible in a least-parameter critical
   counterexample; every neutral row has at least two holes.
2. Every cyclic row-dense complex bag gives an explicit \(K_7\)-model.
3. At a two-cut, all varied multi-lobe profiles give an explicit split.
   The only survivor is a common owner row; every many-lobe survivor can
   be reduced inside the original graph to an exact two-lobe owner core.
4. Proper-minor colouring states on distinct actual lobes are
   incompatible by crossed splicing.  This is a valid retained-shore
   statement, not contraction-chain pigeonholing.
5. For a three-connected bag, Tutte's theorem gives a uniform blocker:
   every nonseparating \(F\)-to-\(C\) path avoiding another foot must
   contain an entire neutral portal row.  Equivalently, a reserved foot
   plus a rainbow transversal of the four neutral rows blocks every such
   path.
6. A nested planar owner web whose lobes lie behind a triangle and exactly
   four label vertices has actual order-seven adhesions.  Minor-critical
   state pumping bounds every such chain by \(2^{876}\) annuli.
7. At an owner triangle, three or more full components close immediately
   when the four owner labels form \(K_4\); four components close when they
   form \(K_4^-\).  The sole three-component \(K_4^-\) residue has at most
   four triangle-to-owner contacts and, up to symmetry, only four maximal
   contact forests.

## Strategic correction

Large treewidth is not itself the enemy.  The family \(K_2\vee P_n\), for
five-connected planar triangulations \(P_n\) of unbounded treewidth, is
seven-connected and \(K_7\)-minor-free.  Strengthened finite members also
survive all current static portal properness and load constraints.

Accordingly, the credible structural alternative is

\[
                \text{labelled split, or coherent two-apex web},
\]

not “labelled split or bounded treewidth.”  A coherent two-apex web is
harmless because deleting the two apices leaves a planar graph, hence the
whole graph is six-colourable.  The state machinery must synchronize
local web rotations; it cannot simply forbid a large planar torso.

## Exact remaining gap on this route

The live three-connected obstruction is a bounded-depth rotation conflict:

* an exact two-shore covering bad split;
* an owner-set change across adjacent web pieces; or
* the three-component \(K_4^-\) owner triangle in one of four sparse
  contact forests.

The missing uniform lemma is now precise:

> At the first owner-set or rural-rotation conflict, either the two pieces
> realize the labelled two/three-shore split, or faithful minor operations
> on the two retained shores induce the same transported equality state on
> their actual seven-vertex adhesion.

The second outcome would six-colour the graph by crossed splicing.  Proving
this exchange lemma would close a genuine unbounded near-\(K_7\) family;
it is not yet proved.

Primary details are in `hadwiger_near_k7_dynamic_split_web.md`.  The two
new exact verifiers are `near_k7_wall_web_counterarchitecture_verify.py`
and `near_k7_owner_triangle_quotient_verify.py`.
