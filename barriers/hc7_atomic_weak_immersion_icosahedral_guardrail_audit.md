# Independent audit of the atomic weak-immersion icosahedral guardrail

**Status:** separate internal audit GREEN, 21 July 2026.

This is an internal mathematical and computational audit, not external peer
review.

## Revisions audited

- barrier:
  [`hc7_atomic_weak_immersion_icosahedral_guardrail.md`](hc7_atomic_weak_immersion_icosahedral_guardrail.md)
- barrier SHA-256:
  `325d4c44181910a8154f2ff028202b4e3ab9befbd40eca55722d819148ebd65e`
- retained checker:
  [`hc7_atomic_weak_immersion_icosahedral_guardrail_verify.py`](hc7_atomic_weak_immersion_icosahedral_guardrail_verify.py)
- checker SHA-256:
  `e47526f82367eec474df29b8ed055fec1fd39190a0685890573be6846946a68c`

## Verdict

GREEN.  The note's graph-theoretic claims and the retained finite
certificate agree.  The checker was independently rerun with

```bash
.venv/bin/python -B barriers/hc7_atomic_weak_immersion_icosahedral_guardrail_verify.py
```

and returned the documented GREEN output, including all `6,476` vertex
deletions of order at most six.

## Checks performed

1. The listed twenty triangular faces form a connected spherical
   triangulation of the icosahedral core: every edge occurs twice, every
   vertex link is a cycle, and Euler characteristic is two.
2. The join with the two adjacent apices is seven-connected.  The displayed
   seven-set is an actual separator, and planarity of the core excludes a
   `K_7` minor after at most two apex-containing branch sets are removed.
3. Each of the first two witnesses realizes all 21 demands with pairwise
   edge-disjoint paths, one nonbranch binary collision, no branch transit,
   and total length 26.  They avoid one another's collision vertex.
4. Both rounded seven-bag partitions are spanning, connected, disjoint, and
   have exactly the stated missing pair with singleton deficient roots.
5. Every ordinary `K_5` model meets the two apices.  The common-frame
   missed bag has no pair of disjoint connected subgraphs with the two
   prescribed attachment pairs; all seven nonempty subsets are checked.
6. The third witness realizes all 21 demands with 29 distinct edges.  The
   degree-13 apex `p` is the sole two-role vertex, consisting of one branch
   role and one foreign transit role.  Since `M=0` would give a
   topological `K_7`, its `M=1` excess is globally minimum in this
   `K_7`-minor-free host.

## Trust boundary

The host is six-colourable and is not a counterexample to `HC_7`.  It has
both a two-vertex `K_5`-model transversal and an order-seven separator.
The example refutes collision-only descent and several proposed local
inferences; it does not refute the atomic rounding theorem, the full
`(M,T,H,L)` tie-break, or an existential low-degree collision theorem in
all full-hypothesis hosts.
